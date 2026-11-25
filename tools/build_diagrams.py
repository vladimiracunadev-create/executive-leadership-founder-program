#!/usr/bin/env python3
"""Genera el diagrama de «Modelo mental» de **todas** las clases.

Hay dos clases de diagrama, y ambas viven en `tools/diagramas_clase.py`:

* **A medida**: las clases escritas a mano dibujan el marco que enseñan (un
  diagrama de Venn, una escalera, un modelo causal…). Su README ya enlaza la
  imagen.
* **Ficha**: todas las demás reciben una ficha visual construida con lo que la
  propia clase declara: los conceptos que hay que distinguir, la secuencia del
  método (cuyo diseño varía de una clase a otra), las señales a observar y el
  límite. Cambia el texto de la clase y la ficha cambia con él.

Escribe `modelo-mental.svg` junto a cada `README.md` y, en las clases con ficha,
el bloque de imagen entre `<!-- modelo:inicio -->` y `<!-- modelo:fin -->` con la
misma secuencia en texto plegable.

Uso:
    python tools/build_diagrams.py           # escribe
    python tools/build_diagrams.py --check   # falla si algo está desfasado
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "tools"))
import diagramas_clase  # noqa: E402
import diagramas_parte02  # noqa: E402
import diagramas_parte03  # noqa: E402

DIAGRAMAS = {**diagramas_clase.DIAGRAMAS, **diagramas_parte02.DIAGRAMAS, **diagramas_parte03.DIAGRAMAS}

INI = "<!-- modelo:inicio -->"
FIN = "<!-- modelo:fin -->"
ARCHIVO = "modelo-mental.svg"
SECCION = re.compile(r"^## 🧠 Modelo mental\n\n(.*?)(?=^## )", re.S | re.M)


def _seccion(texto: str) -> re.Match:
    m = SECCION.search(texto)
    if not m:
        raise ValueError("la clase no trae la sección «Modelo mental»")
    return m


def _pasos(cuerpo: str) -> list[str]:
    m = re.search(r"```text\n(.*?)\n```", cuerpo, re.S)
    if not m:
        raise ValueError("la clase no trae su secuencia de modelo mental")
    return [re.sub(r"^\d+\.\s*", "", p).strip() for p in re.split(r"\s*→\s*", m.group(1).strip())]


def _conceptos(texto: str) -> list[tuple[str, str]]:
    m = re.search(r"^## 🧩 Conceptos centrales\n(.*?)(?=^## )", texto, re.M | re.S)
    out = []
    for fila in (m.group(1).splitlines() if m else []):
        c = re.match(r"\|\s*\*\*(.+?)\*\*\s*\|\s*(.+?)\s*\|", fila)
        if c:
            out.append((c.group(1).strip(), c.group(2).strip().rstrip(".")))
    return out


def _lista_yaml(y: str, clave: str) -> list[str]:
    m = re.search(rf"^{clave}:\n((?:\s+-\s+.*\n?)+)", y, re.M)
    if not m:
        return []
    return [re.sub(r'^\s+-\s+"?(.*?)"?\s*$', r"\1", f) for f in m.group(1).splitlines() if f.strip()]


def _bloque(numero: int, pasos: list[str]) -> str:
    seq = " → ".join(f"{i + 1}. {p}" for i, p in enumerate(pasos))
    return (f"{INI}\n![Modelo mental de la clase {numero:03d}: {seq}]({ARCHIVO})\n\n<details>\n"
            f"<summary>La misma secuencia, en texto</summary>\n\n```text\n{seq}\n```\n\n</details>\n{FIN}")


def calcular() -> dict[Path, str]:
    escribir: dict[Path, str] = {}
    for readme in sorted((RAIZ / "modules").glob("*/classes/*/README.md")):
        clase = readme.parent
        numero = int(clase.name[:3])
        parte_n = int(readme.parents[2].name[:2])
        texto = readme.read_text(encoding="utf-8")
        y = (clase / "lesson.yaml").read_text(encoding="utf-8")
        titulo = re.search(r'^title:\s*"?(.*?)"?\s*$', y, re.M).group(1)
        svg = clase / ARCHIVO
        if numero in DIAGRAMAS:
            escribir[svg] = DIAGRAMAS[numero]()
            if f"]({ARCHIVO})" not in texto:
                raise SystemExit(f"{readme.relative_to(RAIZ)}: el README no enlaza {ARCHIVO}")
            continue
        m = _seccion(texto)
        cuerpo = m.group(1)
        # La secuencia se lee del bloque original o del texto plegable ya generado.
        pasos = _pasos(cuerpo)
        limites = _lista_yaml(y, "limits")
        escribir[svg] = diagramas_clase.ficha_de_clase(
            numero, titulo, parte_n, pasos, _conceptos(texto), _lista_yaml(y, "evidence_signals"),
            limites[0] if limites else "")
        bloque = _bloque(numero, pasos)
        if INI in cuerpo:
            nuevo = re.sub(re.escape(INI) + r".*?" + re.escape(FIN), lambda _: bloque, cuerpo, count=1, flags=re.S)
        else:
            nuevo = re.sub(r"```text\n.*?\n```", lambda _: bloque, cuerpo, count=1, flags=re.S)
        escribir[readme] = texto[:m.start(1)] + nuevo + texto[m.end(1):]
    return escribir


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true", help="falla si algo está desfasado")
    args = ap.parse_args()
    escribir = calcular()
    desfasados = [p for p, t in escribir.items() if not p.exists() or p.read_text(encoding="utf-8") != t]
    svgs = sum(1 for p in escribir if p.suffix == ".svg")
    if args.check:
        if desfasados:
            print(f"Diagramas desfasados en {len(desfasados)} archivos; ejecuta tools/build_diagrams.py")
            for p in desfasados[:10]:
                print("  ", p.relative_to(RAIZ).as_posix())
            return 1
        print(f"Los {svgs} diagramas de modelo mental están al día")
        return 0
    for p in desfasados:
        p.write_text(escribir[p], encoding="utf-8", newline="\n")
    print(f"Diagramas escritos: {len(desfasados)} archivos ({svgs} SVG)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
