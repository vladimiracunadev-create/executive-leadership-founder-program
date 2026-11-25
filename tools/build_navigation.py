#!/usr/bin/env python3
"""Genera la navegación del programa: portada de cada parte y migas de cada clase.

Qué escribe, y solo dentro de bloques con marca:

* `modules/NN-*/README.md`: la portada de la parte (de qué trata, con qué hay
  que llegar, resultados, mapa, **tabla de clases con enlaces**, glosario,
  evidencia, cómo se conecta y cómo se trabaja). Lo que va después de la marca
  `<!-- parte:fin -->` (laboratorios, proyecto, bibliografía, criterio) es
  contenido propio y no se toca.
* `modules/NN-*/classes/*/README.md`: una miga bajo el título (parte, posición,
  anterior y siguiente) y un pie `Anterior | Índice | Siguiente`.
* `modules/NN-*/labs/lab-NN.md` y `project.md`: el mismo pie.

El contenido pedagógico propio de cada parte vive en `curriculum/part_pedagogy.py`;
lo demás se deriva de lo que ya declaran las clases, de modo que un título, una
duración o un entregable se cambian en `lesson.yaml` y se propagan aquí.

Uso:
    python tools/build_navigation.py           # escribe
    python tools/build_navigation.py --check   # falla si algo está desfasado

Solo biblioteca estándar. Si se regenera una clase con
`tools/deep_curriculum_builder.py`, vuelve a ejecutar este script: el generador
de clases no conoce estas marcas y las descarta.
"""

from __future__ import annotations

import argparse
import importlib.util
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "tools"))
import inventario  # noqa: E402
MODULOS = RAIZ / "modules"

PARTE_INI = "<!-- parte:inicio -->"
PARTE_FIN = "<!-- parte:fin -->"
NAV_INI = "<!-- nav:inicio -->"
NAV_FIN = "<!-- nav:fin -->"
PIE_INI = "<!-- pie:inicio -->"
PIE_FIN = "<!-- pie:fin -->"

ETAPAS = {
    range(0, 4): "🟢 Etapa 1 — Autoliderazgo y fundamentos ejecutivos",
    range(4, 8): "🔵 Etapa 2 — Liderazgo de equipos y ejecución",
    range(8, 12): "🟣 Etapa 3 — Gestión de negocio",
    range(12, 16): "🟠 Etapa 4 — Dirección, estrategia y organización",
    range(16, 20): "🔴 Etapa 5 — Alta dirección y gobierno",
    range(20, 24): "⚫ Etapa 6 — Fundador, propietario e independencia",
}


def etapa_de(n: int) -> str:
    return next(v for k, v in ETAPAS.items() if n in k)


def cargar_pedagogia() -> dict:
    ruta = RAIZ / "curriculum" / "part_pedagogy.py"
    spec = importlib.util.spec_from_file_location("curriculum.part_pedagogy", ruta)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo.PARTES


@dataclass
class Clase:
    numero: int
    carpeta: Path
    titulo: str
    minutos: int
    entregable: str
    conceptos: list[tuple[str, str]] = field(default_factory=list)

    @property
    def ruta(self) -> Path:
        return self.carpeta / "README.md"


@dataclass
class Parte:
    numero: int
    carpeta: Path
    titulo: str
    clases: list[Clase]
    labs: list[Path]

    @property
    def ruta(self) -> Path:
        return self.carpeta / "README.md"


def _yaml_valor(texto: str, clave: str) -> str:
    m = re.search(rf'^{clave}:\s*"?(.*?)"?\s*$', texto, re.M)
    return m.group(1) if m else ""


def _conceptos(readme: str) -> list[tuple[str, str]]:
    m = re.search(r"^## 🧩 Conceptos centrales\n(.*?)(?=^## )", readme, re.M | re.S)
    if not m:
        return []
    out = []
    for fila in m.group(1).splitlines():
        c = re.match(r"\|\s*\*\*(.+?)\*\*\s*\|\s*(.+?)\s*\|", fila)
        if c:
            out.append((c.group(1).strip(), c.group(2).strip().rstrip(".")))
    return out


def leer_programa() -> list[Parte]:
    partes: list[Parte] = []
    for carpeta in sorted(MODULOS.glob("[0-9][0-9]-*")):
        n = int(carpeta.name[:2])
        h1 = (carpeta / "README.md").read_text(encoding="utf-8").splitlines()[0]
        titulo = re.sub(r"^#\s*Parte\s+\d+\s*[—-]\s*", "", h1).strip()
        clases = []
        for d in sorted((carpeta / "classes").iterdir()):
            if not d.is_dir():
                continue
            y = (d / "lesson.yaml").read_text(encoding="utf-8")
            clases.append(Clase(
                numero=int(d.name[:3]),
                carpeta=d,
                titulo=_yaml_valor(y, "title"),
                minutos=int(_yaml_valor(y, "duration_minutes") or 0),
                entregable=_yaml_valor(y, "deliverable"),
                conceptos=_conceptos((d / "README.md").read_text(encoding="utf-8")),
            ))
        labs = sorted((carpeta / "labs").glob("lab-*.md"))
        partes.append(Parte(n, carpeta, titulo, clases, labs))
    return partes


def rel(origen: Path, destino: Path) -> str:
    """Ruta relativa con barras, desde el directorio que contiene `origen`."""
    return Path(__import__("os").path.relpath(destino, origen.parent)).as_posix()


# ---------------------------------------------------------------- portada de parte

def _meta_previa(texto: str) -> dict[str, str]:
    """Rescata etapa/resultado ya escritos, para no inventarlos de nuevo."""
    return {
        "resultado": (re.search(r"\*\*Resultado de salida:\*\* (.*)", texto) or [None, ""])[1].strip(),
    }


def _mermaid(parte: Parte, datos: dict) -> str:
    por_id = {c.numero: c for c in parte.clases}
    nodos, flechas = [], []
    for i, (a, b, _) in enumerate(datos["grupos"]):
        titulo = por_id[a].titulo.replace('"', "'")
        nodos.append(f'    G{i}["Clases {a}–{b}<br/>{titulo} …"]')
        if i:
            flechas.append(f"    G{i - 1} --> G{i}")
    n = len(datos["grupos"])
    nodos.append('    L["Laboratorios<br/>práctica guiada"]')
    nodos.append('    P["Proyecto de parte<br/>defensa y rúbrica"]')
    flechas.append(f"    G{n - 1} --> P")
    flechas.append(f"    G{max(n - 2, 0)} -.-> L")
    flechas.append("    L -.-> P")
    return "```mermaid\nflowchart LR\n" + "\n".join(nodos + flechas) + "\n```"


def bloque_parte(parte: Parte, partes: list[Parte], datos: dict, resultado: str) -> str:
    n = parte.numero
    ini, fin = parte.clases[0].numero, parte.clases[-1].numero
    horas = sum(c.minutos for c in parte.clases) / 60
    horas_txt = f"{horas:g}".replace(".", ",")
    ant = partes[n - 1] if n > 0 else None
    sig = partes[n + 1] if n < len(partes) - 1 else None

    def enlace_parte(p: Parte) -> str:
        return f"[Parte {p.numero:02d} — {p.titulo}](../{p.carpeta.name}/README.md)"

    nav = " · ".join([
        f"← {enlace_parte(ant)}" if ant else "← Inicio del programa",
        "[Temario](../../SYLLABUS.md)",
        f"{enlace_parte(sig)} →" if sig else "Fin del programa →",
    ])

    L: list[str] = []
    etapa = inventario.etapa_de(n)
    L += [PARTE_INI, "", f"> {nav}", "", f"*{datos['lema']}*", ""]
    # Estas tres líneas conservan su forma: `tools/inventario.py` las lee.
    L += [f"**Etapa:** {inventario.numero_de_etapa(etapa)} — {etapa.nombre}  ",
          f"**Duración:** {len(parte.clases)} clases · {round(horas)} horas  ",
          f"**Resultado de salida:** {resultado}", ""]
    L += [f"{etapa.emoji} [Ver las 6 etapas](../../SYLLABUS.md) · {len(parte.clases)} clases "
          f"({ini:03d}–{fin:03d}) · {len(parte.labs)} laboratorios · [proyecto de parte](project.md)", ""]

    L += ["## 🎯 De qué trata esta parte", ""]
    for p in datos["intro"]:
        L += [p, ""]

    L += ["## 🧱 Con qué hay que llegar", ""]
    if datos["previo"]:
        L += ["| Parte | Qué aporta |", "|---|---|"]
        for pn, aporte in datos["previo"]:
            p = partes[pn]
            L += [f"| [{pn:02d} — {p.titulo}](../{p.carpeta.name}/README.md) | {aporte} |"]
        L += ["", "Cada clase supone la anterior: el orden importa, y saltarse una deja sin base a las que vienen después."]
    else:
        L += ["Nada previo: es la puerta de entrada del programa. Solo se necesita un trabajo o proyecto real sobre el cual practicar."]
    L += [""]

    L += ["## 📚 Resultados de la parte", "", "Al terminar esta parte podrás:", ""]
    for i, r in enumerate(datos["aprendizajes"], 1):
        L += [f"{i}. {r}"]
    L += [""]

    L += ["## 🗺️ Mapa de la parte", "", _mermaid(parte, datos), ""]

    L += [f"## 🧭 Cómo se encadenan las {len(parte.clases)} clases", ""]
    for _, _, texto in datos["grupos"]:
        L += [texto, ""]

    L += [f"## 📘 Las {len(parte.clases)} clases", "",
          "| # | Clase | Qué se trabaja | Entregable | Min |", "|---:|---|---|---|---:|"]
    for c in parte.clases:
        claves = ", ".join(t for t, _ in c.conceptos[:3]) or "—"
        ruta = rel(parte.ruta, c.ruta)
        plantilla = c.entregable
        ent = f"[{plantilla[:-3]}](../../templates/{plantilla})" if plantilla else "—"
        L += [f"| {c.numero:03d} | [{c.titulo}]({ruta}) | {claves} | {ent} | {c.minutos} |"]
    L += [""]

    L += ["## ⚠️ Riesgos característicos", ""]
    L += [f"- {r}" for r in datos["riesgos"]] + [""]

    glos: dict[str, tuple[str, str]] = {}
    for c in parte.clases:
        for t, d in c.conceptos:
            glos.setdefault(t.lower(), (t, d))
    L += ["## 🔤 Glosario de la parte", "", f"{len(glos)} conceptos definidos en las clases, con la definición operacional que usa cada una.", "",
          "| Concepto | Definición operacional |", "|---|---|"]
    for _, (t, d) in sorted(glos.items(), key=lambda kv: kv[0]):
        L += [f"| **{t}** | {d}. |"]
    L += [""]

    L += ["## 📦 Qué queda como evidencia", ""]
    L += [f"- {e}" for e in datos["evidencia"]] + [""]

    L += ["## 🔗 Cómo se conecta", "", datos["conecta"], ""]

    L += ["## 🧪 Cómo se trabaja", "",
          f"Son **{len(parte.clases)} clases de {parte.clases[0].minutos} minutos** —{horas_txt} horas— con "
          f"**{len(parte.labs)} laboratorios** y un proyecto integrador. Cada clase trae su propósito, sus conceptos, "
          "un caso, práctica, errores frecuentes, preguntas de comprobación, entregable y fuentes, y se evalúa con su "
          "`assessment.md`. Los laboratorios se resuelven con datos propios o sintéticos, nunca con datos reales de terceros, "
          "y la parte se cierra con el proyecto y su defensa. Las reglas de recorrido están en "
          "[la guía de navegación](../../docs/NAVIGATION.md).", ""]
    L += [PARTE_FIN]
    return "\n".join(L)


def render_parte(parte: Parte, partes: list[Parte], datos: dict) -> str:
    actual = parte.ruta.read_text(encoding="utf-8")
    h1 = actual.splitlines()[0]
    if PARTE_FIN in actual:
        cola = actual.split(PARTE_FIN, 1)[1]
        resultado = (re.search(r"\*\*Resultado de salida:\*\* (.*)", actual) or [None, ""])[1].strip()
    else:
        i = actual.index("## Laboratorios")
        cola = "\n\n" + actual[i:]
        resultado = _meta_previa(actual)["resultado"]
    return h1 + "\n\n" + bloque_parte(parte, partes, datos, resultado) + cola.rstrip("\n") + "\n"


# ---------------------------------------------------------------- clases, labs, proyecto

def _reemplazar_bloque(texto: str, ini: str, fin: str, bloque: str, donde: str) -> str:
    pat = re.compile(re.escape(ini) + r".*?" + re.escape(fin), re.S)
    if pat.search(texto):
        return pat.sub(lambda _: bloque, texto, count=1)
    if donde == "tras_h1":
        lineas = texto.split("\n")
        return "\n".join([lineas[0], "", bloque] + lineas[1:])
    return texto.rstrip("\n") + "\n\n" + bloque + "\n"


def _fila_pie(ant: tuple[str, str] | None, indice: str, sig: tuple[str, str] | None) -> str:
    a = f"[← {ant[0]}]({ant[1]})" if ant else "—"
    s = f"[{sig[0]} →]({sig[1]})" if sig else "—"
    return f"{PIE_INI}\n---\n\n| Anterior | Índice | Siguiente |\n|---|---|---|\n| {a} | {indice} | {s} |\n{PIE_FIN}"


def render_clase(c: Clase, i: int, parte: Parte, todas: list[Clase], partes_por_clase: dict[int, Parte]) -> str:
    texto = c.ruta.read_text(encoding="utf-8")
    ant = todas[i - 1] if i > 0 else None
    sig = todas[i + 1] if i < len(todas) - 1 else None

    def par(x: Clase | None) -> tuple[str, str] | None:
        return (f"{x.numero:03d} · {x.titulo}", rel(c.ruta, x.ruta)) if x else None

    pos = parte.clases.index(c) + 1
    cab = (f"{NAV_INI}\n> **Parte {parte.numero:02d} · {parte.titulo}** — clase {pos} de {len(parte.clases)} · "
           f"[índice de la parte]({rel(c.ruta, parte.ruta)}) · [temario]({rel(c.ruta, RAIZ / 'SYLLABUS.md')})\n{NAV_FIN}")
    texto = _reemplazar_bloque(texto, NAV_INI, NAV_FIN, cab, "tras_h1")
    indice = f"[Parte {parte.numero:02d}]({rel(c.ruta, parte.ruta)}) · [Programa]({rel(c.ruta, RAIZ / 'SYLLABUS.md')})"
    pie = _fila_pie(par(ant), indice, par(sig))
    texto = _reemplazar_bloque(texto, PIE_INI, PIE_FIN, pie, "final")
    return texto.rstrip("\n") + "\n"


def render_lab(lab: Path, parte: Parte) -> str:
    texto = lab.read_text(encoding="utf-8")
    labs = parte.labs
    i = labs.index(lab)

    def nombre(p: Path) -> str:
        return f"Laboratorio {int(p.stem.split('-')[1])}"

    ant = (nombre(labs[i - 1]), rel(lab, labs[i - 1])) if i else None
    sig = (nombre(labs[i + 1]), rel(lab, labs[i + 1])) if i < len(labs) - 1 else ("Proyecto de parte", rel(lab, parte.carpeta / "project.md"))
    indice = f"[Parte {parte.numero:02d}]({rel(lab, parte.ruta)}) · [Programa]({rel(lab, RAIZ / 'SYLLABUS.md')})"
    return _reemplazar_bloque(texto, PIE_INI, PIE_FIN, _fila_pie(ant, indice, sig), "final").rstrip("\n") + "\n"


def render_proyecto(parte: Parte, partes: list[Parte]) -> str:
    p = parte.carpeta / "project.md"
    texto = p.read_text(encoding="utf-8")
    ant = (f"Laboratorio {len(parte.labs)}", rel(p, parte.labs[-1])) if parte.labs else None
    sig_parte = partes[parte.numero + 1] if parte.numero < len(partes) - 1 else None
    sig = (f"Parte {sig_parte.numero:02d} — {sig_parte.titulo}", rel(p, sig_parte.ruta)) if sig_parte else None
    indice = f"[Parte {parte.numero:02d}]({rel(p, parte.ruta)}) · [Programa]({rel(p, RAIZ / 'SYLLABUS.md')})"
    return _reemplazar_bloque(texto, PIE_INI, PIE_FIN, _fila_pie(ant, indice, sig), "final").rstrip("\n") + "\n"


# ---------------------------------------------------------------- principal

def calcular() -> dict[Path, str]:
    partes = leer_programa()
    pedagogia = cargar_pedagogia()
    todas = [c for p in partes for c in p.clases]
    por_clase = {c.numero: p for p in partes for c in p.clases}
    salida: dict[Path, str] = {}
    for p in partes:
        salida[p.ruta] = render_parte(p, partes, pedagogia[p.numero])
        salida[p.carpeta / "project.md"] = render_proyecto(p, partes)
        for lab in p.labs:
            salida[lab] = render_lab(lab, p)
    for i, c in enumerate(todas):
        salida[c.ruta] = render_clase(c, i, por_clase[c.numero], todas, por_clase)
    return salida


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true", help="falla si algún archivo está desfasado")
    args = ap.parse_args()
    esperado = calcular()
    desfasados = [p for p, t in esperado.items() if p.read_text(encoding="utf-8") != t]
    if args.check:
        if desfasados:
            print(f"Navegación desfasada en {len(desfasados)} archivos; ejecuta tools/build_navigation.py")
            for p in desfasados[:10]:
                print("  ", p.relative_to(RAIZ).as_posix())
            return 1
        print(f"La navegación refleja las {len(esperado)} páginas (partes, clases, laboratorios y proyectos)")
        return 0
    for p in desfasados:
        p.write_text(esperado[p], encoding="utf-8", newline="\n")
    print(f"Navegación escrita en {len(desfasados)} de {len(esperado)} archivos")
    return 0


if __name__ == "__main__":
    sys.exit(main())
