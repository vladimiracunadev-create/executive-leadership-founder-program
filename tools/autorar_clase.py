#!/usr/bin/env python3
"""Deriva `lesson.yaml` y `assessment.md` de una clase escrita a mano.

Una clase con `authoring: manual` tiene su README como única fuente. Este script
sincroniza lo derivable: objetivos (de «Resultados de aprendizaje»), entregable
(de «Entregable»), referencias (de «Fuentes y verificación»), límite (de
«Comparación y límites») y la evaluación (preguntas A, caso B, método C y fuentes D).
Las señales de evidencia no se derivan: se pasan en un JSON
`{"49": ["señal", ...]}` la primera vez y después se conservan.

Uso:
    python tools/autorar_clase.py --clases 49-60 [--senales señales.json]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]


def _sec(t: str, nombre: str) -> str:
    m = re.search(rf"^## {re.escape(nombre)}\n(.*?)(?=^## |\Z)", t, re.S | re.M)
    return m.group(1) if m else ""


def _senales_actuales(y: str) -> list[str]:
    m = re.search(r"^evidence_signals:\n((?:\s+-\s+.*\n?)+)", y, re.M)
    if not m:
        return []
    return [re.sub(r'^\s+-\s+"?(.*?)"?\s*$', r"\1", f) for f in m.group(1).splitlines() if f.strip()]


def _expandir_fuentes(t: str) -> str:
    """Convierte `- @@prefijo-de-id:: uso` en la cita canónica tomada del registro."""
    sys.path.insert(0, str(RAIZ / "tools"))
    import sources_registry as reg
    entradas = reg.cargar()["entries"]

    def buscar(pref: str) -> dict:
        c = [e for e in entradas if e["id"].startswith(pref)]
        if len(c) != 1:
            raise SystemExit(f"prefijo de fuente ambiguo o inexistente: {pref!r} ({len(c)} coincidencias)")
        return c[0]

    def sustituir(m: re.Match) -> str:
        e = buscar(m.group(1).strip())
        emisor, obra = e["cited_as"].split(" — ", 1)
        return f"- {emisor} — *{obra}*. **Uso en esta clase:** {m.group(2).strip()}."

    return re.sub(r"^- @@([a-z0-9\-]+)::\s*(.+?)\.?[ \t]*$", sustituir, t, flags=re.M)


def autorar(cid: int, senales: list[str] | None) -> None:
    d = next(RAIZ.glob(f"modules/*/classes/{cid:03d}-*"))
    t = (d / "README.md").read_text(encoding="utf-8")
    expandido = _expandir_fuentes(t)
    if expandido != t:
        (d / "README.md").write_text(expandido, encoding="utf-8", newline="\n")
        t = expandido
    y = (d / "lesson.yaml").read_text(encoding="utf-8")
    cab = y.split("objectives:")[0]
    if "authoring:" not in cab:
        cab = cab.replace("pedagogy: retrieval-case-deliberate-practice\n",
                          "pedagogy: retrieval-case-deliberate-practice\nauthoring: manual\n")
    cab = cab.replace("source_mode: books-plus-primary", "source_mode: primary-literature")
    titulo = re.search(r'^title:\s*"(.*)"', cab, re.M).group(1)
    objetivos = [re.sub(r"\*\*", "", re.sub(r"^\d+\.\s*", "", l)).strip()
                 for l in _sec(t, "📚 Resultados de aprendizaje").splitlines() if re.match(r"^\d+\.", l)]
    refs = [re.sub(r"\s*\([^)]*\)$", "", re.sub(r"\. \*\*Uso en esta clase:.*", "", l[2:]).strip())
            for l in _sec(t, "📗 Fuentes y verificación").splitlines() if l.startswith("- ")]
    ent = re.search(r"`([a-z\-]+\.md)` \(plantilla", _sec(t, "📥 Entregable")).group(1)
    caso_sec = _sec(t, "🏢 Caso ejecutivo").strip().split("\n\n")
    caso = caso_sec[0].replace('"', "'")
    entrega = next(p for p in caso_sec if p.startswith("Entrega"))
    preg = [re.sub(r"^\d+\.\s*", "", l) for l in _sec(t, "❓ Preguntas de comprobación").splitlines()
            if re.match(r"^\d+\.", l)][:3]
    lim = re.search(r"\*\*Límites[^.]*\.\*\*\s*(.+)", _sec(t, "🔀 Comparación y límites"))
    limite = (lim.group(1).split(". ")[0] + ".").replace('"', "'") if lim else "Ver la sección de límites de la clase."
    if senales is None:
        senales = _senales_actuales(y)
    out = cab + "objectives:\n" + "".join(f'  - "{o}"\n' for o in objetivos)
    out += f'deliverable: "{ent}"\nreferences:\n' + "".join(f'  - "{r}"\n' for r in refs)
    out += f'limits:\n  - "{limite}"\nevidence_signals:\n' + "".join(f'  - "{s}"\n' for s in senales)
    (d / "lesson.yaml").write_text(out, encoding="utf-8", newline="\n")
    n = f"{cid:03d}"
    ass = (f"# Evaluación — Clase {n}: {titulo}\n\nEsta evaluación exige haber estudiado la clase y sus fuentes; "
           "respuestas genéricas sin evidencia no cumplen el criterio.\n\n## A. Comprensión conceptual — 25 %\n\n"
           + "".join(f"{i}. {p}\n" for i, p in enumerate(preg, 1))
           + f"\n## B. Caso de decisión — 30 %\n\n**Caso:** {caso}\n\n"
           "Construye dos alternativas plausibles. Para cada una indica beneficio esperado, costo de oportunidad, "
           "riesgo, reversibilidad y qué actor asume la consecuencia. Después recomienda una y declara qué nueva "
           "información cambiaría tu decisión.\n\n"
           f"## C. Método y evidencia — 30 %\n\n{entrega} Separa hechos, inferencias y supuestos.\n\n"
           "## D. Fuentes, límites y red team — 15 %\n\nContrasta dos de las fuentes de la clase: qué aporta cada una, "
           f"qué tensión hay entre ellas y cómo cambia tu recomendación. Luego responde al límite de la clase: {limite}\n\n"
           "## Criterios de aprobación\n\n| Criterio | Peso | Evidencia esperada |\n|---|---:|---|\n"
           "| Precisión conceptual | 25 % | Definiciones correctas, con la fuente y con un ejemplo propio. |\n"
           "| Diagnóstico y evidencia | 30 % | Cada afirmación del caso respaldada por un hecho y separada de la suposición. |\n"
           "| Decisión y trade-offs | 30 % | Dos opciones defendibles, costo de oportunidad, riesgo y condición de revisión. |\n"
           "| Fuentes y comunicación | 15 % | Dos lecturas realmente utilizadas, trazabilidad y argumento claro. |\n\n"
           "**Aprobación sugerida:** 80/100 y ningún criterio bajo 60 %. Una respuesta que podría copiarse sin cambiar "
           "nada a otra clase se considera insuficiente.\n")
    (d / "assessment.md").write_text(ass, encoding="utf-8", newline="\n")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--clases", required=True, help="rango, p. ej. 49-60")
    ap.add_argument("--senales", help="JSON {clase: [señales]}")
    args = ap.parse_args()
    a, b = (int(x) for x in args.clases.split("-"))
    sj = json.loads(Path(args.senales).read_text(encoding="utf-8")) if args.senales else {}
    for cid in range(a, b + 1):
        autorar(cid, sj.get(str(cid)))
    print(f"Derivadas las clases {a}-{b}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
