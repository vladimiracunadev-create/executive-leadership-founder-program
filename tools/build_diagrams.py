#!/usr/bin/env python3
"""Genera los diagramas a medida de las clases y retira los genéricos.

Un diagrama solo se publica si ayuda a entender el marco de **esa** clase
(`tools/diagramas_clase.py`). Las clases que aún no tienen uno no llevan imagen:
un esquema idéntico repetido en las 288 no enseñaba nada.

Qué hace, por clase:

* con diagrama a medida: escribe `modelo-mental.svg` junto al `README.md`, que
  el README (escrito a mano) enlaza en su sección «Modelo mental»;
* sin diagrama: garantiza que no quede un `modelo-mental.svg` huérfano y que el
  README conserve su secuencia en texto.

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

INI = "<!-- modelo:inicio -->"
FIN = "<!-- modelo:fin -->"
ARCHIVO = "modelo-mental.svg"


def _restaurar_secuencia(texto: str) -> str:
    """Quita el bloque del diagrama genérico y devuelve la secuencia como bloque de texto."""
    pat = re.compile(re.escape(INI) + r".*?" + re.escape(FIN), re.S)
    m = pat.search(texto)
    if not m:
        return texto
    cod = re.search(r"```text\n(.*?)\n```", m.group(0), re.S)
    return pat.sub(lambda _: f"```text\n{cod.group(1)}\n```", texto, count=1)


def calcular() -> tuple[dict[Path, str], list[Path]]:
    escribir: dict[Path, str] = {}
    borrar: list[Path] = []
    for readme in sorted((RAIZ / "modules").glob("*/classes/*/README.md")):
        clase = readme.parent
        numero = int(clase.name[:3])
        svg = clase / ARCHIVO
        texto = readme.read_text(encoding="utf-8")
        if numero in diagramas_clase.DIAGRAMAS:
            escribir[svg] = diagramas_clase.DIAGRAMAS[numero]()
            if f"]({ARCHIVO})" not in texto:
                raise SystemExit(f"{readme.relative_to(RAIZ)}: el README no enlaza {ARCHIVO}")
        else:
            if svg.exists():
                borrar.append(svg)
            limpio = _restaurar_secuencia(texto)
            if limpio != texto:
                escribir[readme] = limpio
    return escribir, borrar


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true", help="falla si algo está desfasado")
    args = ap.parse_args()
    escribir, borrar = calcular()
    desfasados = [p for p, t in escribir.items() if not p.exists() or p.read_text(encoding="utf-8") != t]
    if args.check:
        if desfasados or borrar:
            print(f"Diagramas desfasados ({len(desfasados)} por escribir, {len(borrar)} por retirar); "
                  "ejecuta tools/build_diagrams.py")
            return 1
        print(f"Los {len(diagramas_clase.DIAGRAMAS)} diagramas a medida están al día; ninguna clase lleva uno genérico")
        return 0
    for p in desfasados:
        p.write_text(escribir[p], encoding="utf-8", newline="\n")
    for p in borrar:
        p.unlink()
    print(f"Diagramas escritos: {len(desfasados)} · retirados: {len(borrar)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
