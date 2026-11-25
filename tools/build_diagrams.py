#!/usr/bin/env python3
"""Genera el SVG del «Modelo mental» de cada clase.

La secuencia de pasos que cada clase declara en su sección «🧠 Modelo mental»
(un bloque de texto `1. … → 2. … → …`) se dibuja como un diagrama: cinco
tarjetas numeradas unidas por flechas, un bucle de revisión que vuelve al primer
paso y las señales que conviene observar (`evidence_signals` de `lesson.yaml`).

Escribe, por clase:

* `modelo-mental.svg` junto al `README.md`;
* en el README, entre `<!-- modelo:inicio -->` y `<!-- modelo:fin -->`, la imagen
  y la misma secuencia como texto plegable, para quien lee sin imágenes.

El SVG es autónomo: lleva su propio fondo y sus colores, de modo que se lee igual
en el tema claro y en el oscuro del portal y en GitHub. Solo biblioteca estándar.

Uso:
    python tools/build_diagrams.py           # escribe
    python tools/build_diagrams.py --check   # falla si algo está desfasado

Si se regenera una clase con `tools/deep_curriculum_builder.py`, vuelve a
ejecutar este script (y `build_navigation.py`): el generador de clases no
conoce estas marcas.
"""

from __future__ import annotations

import argparse
import re
import sys
import textwrap
from pathlib import Path
from xml.sax.saxutils import escape

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "tools"))
import inventario  # noqa: E402

INI = "<!-- modelo:inicio -->"
FIN = "<!-- modelo:fin -->"
ARCHIVO = "modelo-mental.svg"

ANCHO = 1040
MARGEN = 28
HUECO = 34
FUENTE = "'Segoe UI', 'Helvetica Neue', Helvetica, Arial, sans-serif"
TINTA = "#1f2328"
SUAVE = "#59636e"
PAPEL = "#f6f8fa"
BORDE = "#d0d7de"


def pasos_de(texto_readme: str) -> list[str]:
    """Lee la secuencia: del bloque original o del texto plegable ya generado."""
    m = re.search(r"```text\n(.*?)\n```", seccion_modelo(texto_readme), re.S)
    if not m:
        raise ValueError("la clase no trae su secuencia de modelo mental")
    return [re.sub(r"^\d+\.\s*", "", p).strip() for p in re.split(r"\s*→\s*", m.group(1).strip())]


def seccion_modelo(texto: str) -> str:
    m = re.search(r"^## 🧠 Modelo mental\n(.*?)(?=^## )", texto, re.S | re.M)
    if not m:
        raise ValueError("la clase no trae la sección «Modelo mental»")
    return m.group(1)


def senales_de(yaml_texto: str) -> list[str]:
    m = re.search(r"^evidence_signals:\n((?:\s+-\s+.*\n?)+)", yaml_texto, re.M)
    if not m:
        return []
    return [re.sub(r'^\s+-\s+"?(.*?)"?\s*$', r"\1", f) for f in m.group(1).splitlines() if f.strip()]


def _envolver(texto: str, ancho_px: float, tam: float) -> list[str]:
    caracteres = max(8, int(ancho_px / (tam * 0.56)))
    return textwrap.wrap(texto, caracteres, break_long_words=False) or [texto]


def _texto(x, y, s, tam, color=TINTA, peso="400", ancla="start", extra=""):
    return (f'<text x="{x:g}" y="{y:g}" font-size="{tam:g}" font-weight="{peso}" fill="{color}" '
            f'text-anchor="{ancla}" {extra}>{escape(s)}</text>')


def dibujar(numero: int, titulo: str, parte_n: int, pasos: list[str], senales: list[str]) -> str:
    etapa = inventario.etapa_de(parte_n)
    color = etapa.color_claro
    n = len(pasos)
    ancho_t = (ANCHO - 2 * MARGEN - (n - 1) * HUECO) / n
    interior = ancho_t - 28
    tam = 15.5
    envueltos = [_envolver(p, interior, tam) for p in pasos]
    lineas = max(len(e) for e in envueltos)
    alto_cab = 34
    alto_cuerpo = 20 + lineas * 20 + 14
    y0 = 92
    y_fin = y0 + alto_cab + alto_cuerpo

    o: list[str] = []
    # Cabecera.
    o.append(f'<rect x="{MARGEN}" y="24" width="132" height="26" rx="13" fill="{color}"/>')
    o.append(_texto(MARGEN + 66, 41.5, "MODELO MENTAL", 11.5, "#ffffff", "700", "middle", 'letter-spacing="1.2"'))
    o.append(_texto(MARGEN + 148, 43, f"Clase {numero:03d} · {titulo}", 19, TINTA, "700"))
    o.append(_texto(ANCHO - MARGEN, 43, f"Parte {parte_n:02d} · {etapa.nombre}", 12.5, SUAVE, "400", "end"))

    # Tarjetas y flechas.
    centros = []
    for i, lineas_paso in enumerate(envueltos):
        x = MARGEN + i * (ancho_t + HUECO)
        centros.append(x + ancho_t / 2)
        o.append(f'<rect x="{x:g}" y="{y0}" width="{ancho_t:g}" height="{alto_cab + alto_cuerpo:g}" rx="12" '
                 f'fill="#ffffff" stroke="{BORDE}" stroke-width="1.2"/>')
        o.append(f'<path d="M{x:g},{y0 + alto_cab} V{y0 + 12} a12,12 0 0 1 12,-12 H{x + ancho_t - 12:g} '
                 f'a12,12 0 0 1 12,12 V{y0 + alto_cab} Z" fill="{color}"/>')
        o.append(_texto(x + 16, y0 + 22.5, f"PASO {i + 1}", 12, "#ffffff", "700", "start", 'letter-spacing="1.4"'))
        for k, linea in enumerate(lineas_paso):
            o.append(_texto(x + 14, y0 + alto_cab + 28 + k * 20, linea, tam, TINTA))
        if i < n - 1:
            xa = x + ancho_t + 6
            ym = y0 + alto_cab + alto_cuerpo / 2
            o.append(f'<path d="M{xa:g},{ym:g} H{xa + HUECO - 14:g}" stroke="{color}" stroke-width="2.4" '
                     f'stroke-linecap="round" marker-end="url(#punta)"/>')

    # Bucle de revisión: del último paso de vuelta al primero.
    yb = y_fin
    yl = yb + 34
    x_fin, x_ini = centros[-1], centros[0]
    o.append(f'<path d="M{x_fin:g},{yb + 2} V{yl - 10} a10,10 0 0 1 -10,10 H{x_ini + 10:g} '
             f'a10,10 0 0 1 -10,-10 V{yb + 4}" fill="none" stroke="{color}" stroke-width="2" '
             f'stroke-dasharray="7 6" stroke-linecap="round" marker-end="url(#punta)"/>')
    etiqueta = "revisar y ajustar cuando la evidencia cambie"
    ancho_e = len(etiqueta) * 6.7 + 28
    xm = (x_fin + x_ini) / 2
    o.append(f'<rect x="{xm - ancho_e / 2:g}" y="{yl - 12}" width="{ancho_e:g}" height="24" rx="12" '
             f'fill="{PAPEL}" stroke="{color}" stroke-width="1.2"/>')
    o.append(_texto(xm, yl + 4.5, etiqueta, 12.5, color, "600", "middle"))

    # Señales a observar.
    y_s = yl + 46
    o.append(_texto(MARGEN, y_s, "QUÉ OBSERVAR", 11.5, SUAVE, "700", "start", 'letter-spacing="1.4"'))
    x, y = MARGEN, y_s + 14
    limite = ANCHO - MARGEN
    filas = 1
    for s in senales[:8]:
        w = len(s) * 6.9 + 26
        if x + w > limite:
            filas += 1
            if filas > 2:
                break
            x, y = MARGEN, y + 34
        o.append(f'<rect x="{x:g}" y="{y}" width="{w:g}" height="26" rx="13" fill="#ffffff" stroke="{color}" stroke-width="1.2"/>')
        o.append(f'<circle cx="{x + 13:g}" cy="{y + 13}" r="3.5" fill="{color}"/>')
        o.append(_texto(x + 24, y + 17.5, s, 12.5, TINTA))
        x += w + 10
    alto = (y + 26 + 24) if senales else (y_s + 10)

    descripcion = " → ".join(f"{i + 1}. {p}" for i, p in enumerate(pasos))
    cabecera = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {ANCHO} {alto:g}" width="{ANCHO}" '
        f'role="img" aria-labelledby="t d" font-family="{FUENTE}">\n'
        f'<title id="t">Modelo mental de la clase {numero:03d}: {escape(titulo)}</title>\n'
        f'<desc id="d">{escape(descripcion)}</desc>\n'
        f'<defs><marker id="punta" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" '
        f'orient="auto-start-reverse"><path d="M1,1 L9,5 L1,9 Z" fill="{color}"/></marker></defs>\n'
        f'<rect width="{ANCHO}" height="{alto:g}" rx="16" fill="{PAPEL}" stroke="{BORDE}"/>\n'
    )
    return cabecera + "\n".join(o) + "\n</svg>\n"


def bloque_readme(numero: int, titulo: str, pasos: list[str]) -> str:
    alt = f"Modelo mental de la clase {numero:03d}: " + " → ".join(f"{i + 1}. {p}" for i, p in enumerate(pasos))
    texto = " → ".join(f"{i + 1}. {p}" for i, p in enumerate(pasos))
    return (f"{INI}\n![{alt}]({ARCHIVO})\n\n<details>\n<summary>La misma secuencia, en texto</summary>\n\n"
            f"```text\n{texto}\n```\n\n</details>\n{FIN}")


def calcular() -> dict[Path, str]:
    salida: dict[Path, str] = {}
    for readme in sorted((RAIZ / "modules").glob("*/classes/*/README.md")):
        clase = readme.parent
        numero = int(clase.name[:3])
        parte_n = int(readme.parents[2].name[:2])
        texto = readme.read_text(encoding="utf-8")
        titulo = re.search(r'^title:\s*"?(.*?)"?\s*$', (clase / "lesson.yaml").read_text(encoding="utf-8"), re.M).group(1)
        pasos = pasos_de(texto)
        senales = senales_de((clase / "lesson.yaml").read_text(encoding="utf-8"))
        salida[clase / ARCHIVO] = dibujar(numero, titulo, parte_n, pasos, senales)

        bloque = bloque_readme(numero, titulo, pasos)
        m = re.search(r"(^## 🧠 Modelo mental\n\n)(.*?)(?=^## )", texto, re.S | re.M)
        cuerpo = m.group(2)
        if INI in cuerpo:
            nuevo = re.sub(re.escape(INI) + r".*?" + re.escape(FIN), lambda _: bloque, cuerpo, count=1, flags=re.S)
        else:
            nuevo = re.sub(r"```text\n.*?\n```", lambda _: bloque, cuerpo, count=1, flags=re.S)
        salida[readme] = texto[:m.start(2)] + nuevo + texto[m.end(2):]
    return salida


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true", help="falla si algún archivo está desfasado")
    args = ap.parse_args()
    esperado = calcular()
    desfasados = [p for p, t in esperado.items() if not p.exists() or p.read_text(encoding="utf-8") != t]
    if args.check:
        if desfasados:
            print(f"Diagramas desfasados en {len(desfasados)} archivos; ejecuta tools/build_diagrams.py")
            for p in desfasados[:10]:
                print("  ", p.relative_to(RAIZ).as_posix())
            return 1
        print(f"Los {len(esperado) // 2} modelos mentales reflejan sus clases")
        return 0
    for p in desfasados:
        p.write_text(esperado[p], encoding="utf-8", newline="\n")
    print(f"Diagramas escritos: {len(desfasados)} archivos de {len(esperado)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
