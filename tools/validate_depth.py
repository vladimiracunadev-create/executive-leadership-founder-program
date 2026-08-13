#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
from collections import Counter
import re, sys, math

ROOT=Path(__file__).resolve().parents[1]
FILES=sorted(ROOT.glob('modules/[0-9][0-9]-*/classes/*/README.md'))
REQUIRED=[
    '## 🎯 Propósito','## 📚 Resultados de aprendizaje','## 🧭 Agenda','## 🧩 Conceptos centrales',
    '## 🧠 Modelo mental','## 📖 Desarrollo','## 🧮 Ejemplo trabajado','## 🔀 Comparación y límites',
    '## 🪜 De profesional a owner','## 🏢 Caso ejecutivo','## 🧪 Práctica','## ⚠️ Errores frecuentes',
    '## ❓ Preguntas de comprobación','## 📥 Entregable','## 📗 Fuentes y verificación'
]

def norm(s): return re.sub(r'\s+',' ',s.strip()).lower()
def words(s): return re.findall(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ0-9]+",s)

def shingles(text,k=5):
    ws=[w.lower() for w in words(text)]
    return set(tuple(ws[i:i+k]) for i in range(max(0,len(ws)-k+1)))

def jaccard(a,b):
    if not a or not b: return 0.0
    return len(a&b)/len(a|b)

errors=[]; warnings=[]; paragraph_owners={}; sh={}
for f in FILES:
    t=f.read_text(encoding='utf-8')
    wc=len(words(t))
    if wc < 1150: errors.append(f'{f.relative_to(ROOT)}: only {wc} words (<1150)')
    for h in REQUIRED:
        if h not in t: errors.append(f'{f.relative_to(ROOT)}: missing {h}')
    refs=t.split('## 📗 Fuentes y verificación',1)[-1]
    ref_lines=[x for x in refs.splitlines() if x.lstrip().startswith('- ')]
    if len(ref_lines)<5: errors.append(f'{f.relative_to(ROOT)}: only {len(ref_lines)} references')
    dev=t.split('## 📖 Desarrollo',1)[-1].split('## 🧮 Ejemplo trabajado',1)[0] if '## 📖 Desarrollo' in t and '## 🧮 Ejemplo trabajado' in t else ''
    if len(re.findall(r'^### ',dev,re.M))<5: errors.append(f'{f.relative_to(ROOT)}: development has <5 subsections')
    q=t.split('## ❓ Preguntas de comprobación',1)[-1].split('## 📥 Entregable',1)[0] if '## ❓ Preguntas de comprobación' in t else ''
    if len(re.findall(r'^\d+\.',q,re.M))<5: errors.append(f'{f.relative_to(ROOT)}: <5 check questions')
    for p in re.split(r'\n\s*\n',t):
        n=norm(p)
        if len(words(n))>=28 and not n.startswith('##'):
            paragraph_owners.setdefault(n,[]).append(f)
    sh[f]=shingles(t)

for p,owners in paragraph_owners.items():
    if len(owners)>=4:
        errors.append(f'Long paragraph repeated in {len(owners)} classes: {p[:120]}...')

# Near-duplicate protection. Only compare within each module to keep it fast and meaningful.
by_module={}
for f in FILES: by_module.setdefault(f.parents[2].name,[]).append(f)
for module,fs in by_module.items():
    for i,a in enumerate(fs):
        for b in fs[i+1:]:
            score=jaccard(sh[a],sh[b])
            if score>0.56:
                errors.append(f'Near duplicate {score:.2f}: {a.parent.name} vs {b.parent.name}')

# Chile regulatory classes need official primary sources.
for f in ROOT.glob('modules/21-chile-founder-track/classes/*/README.md'):
    t=f.read_text(encoding='utf-8').lower()
    if not any(d in t for d in ('sii.cl','dt.gob.cl','bcn.cl','registrodeempresasysociedades.cl','inapi.cl','chilecompra.cl','sercotec.cl','corfo.cl')):
        errors.append(f'{f.relative_to(ROOT)}: no Chilean official source detected')

print(f'Checked {len(FILES)} classes')
if errors:
    print('DEPTH VALIDATION FAILED')
    for e in errors[:160]: print(' -',e)
    if len(errors)>160: print(f' ... {len(errors)-160} more')
    sys.exit(1)
print('DEPTH VALIDATION OK')
