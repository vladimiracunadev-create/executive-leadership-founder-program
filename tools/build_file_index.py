"""Genera FILE_INDEX.md desde los archivos reales del repositorio.

Un índice escrito a mano se desactualiza en el primer cambio de estructura, y
un índice que miente es peor que no tener índice: quien lo lee deja de
comprobar. Este se recalcula y la CI lo verifica con `--check`.

Uso:
    python tools/build_file_index.py           # regenera FILE_INDEX.md
    python tools/build_file_index.py --check   # falla si está desactualizado
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDICE = ROOT / "FILE_INDEX.md"

EXCLUIDOS = {".git", ".venv", "node_modules", "site", "__pycache__",
             ".pytest_cache", ".ruff_cache", ".mypy_cache"}
BINARIOS = {".png", ".jpg", ".jpeg", ".gif", ".pdf", ".zip", ".ico", ".woff2"}


def rastreados() -> list[Path] | None:
    """Archivos que formarán parte del repositorio.

    Se prefiere git porque respeta `.gitignore` sin reimplementarlo, pero con
    `--others --exclude-standard`: sin esa parte, un archivo nuevo todavía sin
    `git add` quedaría fuera y el resultado dependería del orden en que se
    ejecutaran el generador y el `add`. Un generador cuyo resultado depende del
    orden no sirve como puerta de `--check`.
    """
    try:
        salida = subprocess.run(
            ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
            cwd=ROOT, capture_output=True, text=True, check=True, encoding="utf-8",
        ).stdout
    except (OSError, subprocess.CalledProcessError):
        return None
    return [ROOT / linea for linea in salida.splitlines() if linea]


def recorrido() -> list[Path]:
    return [p for p in ROOT.rglob("*")
            if p.is_file()
            and not any(parte in EXCLUIDOS for parte in p.relative_to(ROOT).parts)]


def archivos() -> list[str]:
    candidatos = rastreados()
    if candidatos is None:
        candidatos = recorrido()
    relativos = []
    for ruta in candidatos:
        rel = ruta.relative_to(ROOT).as_posix() if ruta.is_absolute() else str(ruta)
        if any(parte in EXCLUIDOS for parte in Path(rel).parts):
            continue
        if Path(rel).suffix.lower() in BINARIOS:
            continue
        relativos.append(rel)
    return sorted(set(relativos))


PORTADA = """<!-- portada:inicio -->
<div align="center">

# 🗂️ Índice de archivos

**Todo el texto versionado del repositorio, en un listado plano y ordenado.**

[![Archivos](https://img.shields.io/badge/archivos-{total}-7c5cff?style=flat-square)](FILE_INDEX.md)
[![Generado por](https://img.shields.io/badge/generado%20por-build__file__index.py-007c83?style=flat-square)](tools/build_file_index.py)
[![Se edita](https://img.shields.io/badge/se%20edita-nunca%20a%20mano-8b0000?style=flat-square)](MANIFEST.md)

[🏠 Inicio](README.md) ·
[📚 Temario](SYLLABUS.md) ·
[📊 Estado](STATUS.md) ·
[🧾 Ficha técnica](MANIFEST.md)

</div>
<!-- portada:fin -->

---

## 📊 Reparto por extensión

| Extensión | Archivos |
|---|---:|
{tabla}

## 📁 Listado completo
"""

PIE = """
## ✅ Verificación

```bash
python tools/build_file_index.py --check
```

---

<div align="center">

[🏠 Inicio](README.md) · [📚 Temario](SYLLABUS.md) · [📊 Estado](STATUS.md) · [🧾 Ficha técnica](MANIFEST.md)

</div>
"""


def render() -> str:
    rutas = archivos()
    extensiones = Counter(Path(r).suffix or "(sin extensión)" for r in rutas)
    tabla = "\n".join(
        f"| `{ext}` | {cantidad} |"
        for ext, cantidad in sorted(extensiones.items(), key=lambda x: (-x[1], x[0]))
    )

    lineas = [*PORTADA.format(total=len(rutas), tabla=tabla).rstrip().splitlines(), ""]

    # Se agrupa por directorio antes de escribir. Recorrer la lista ordenada de
    # rutas no basta: `modules/00-x/README.md` ordena antes que
    # `modules/00-x/classes/...` y `modules/00-x/project.md` después, así que el
    # mismo directorio aparecía dos veces con su encabezado repetido.
    por_directorio: dict[str, list[str]] = {}
    for ruta in rutas:
        por_directorio.setdefault(Path(ruta).parent.as_posix(), []).append(Path(ruta).name)

    for directorio in sorted(por_directorio):
        if directorio != ".":
            lineas += ["", f"### `{directorio}/`", ""]
        else:
            lineas += ["", "### Raíz", ""]
        lineas += [f"- `{nombre}`" for nombre in sorted(por_directorio[directorio])]

    lineas += ["", *PIE.strip().splitlines(), ""]
    # Dos saltos seguidos aparecen al abrir el primer grupo; se normalizan para
    # que markdownlint no marque MD012 en un documento generado.
    texto = "\n".join(lineas)
    while "\n\n\n" in texto:
        texto = texto.replace("\n\n\n", "\n\n")
    return texto


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    contenido = render()
    actual = INDICE.read_text(encoding="utf-8") if INDICE.exists() else ""

    if args.check:
        if actual != contenido:
            print("FILE_INDEX.md está desactualizado. "
                  "Ejecuta: python tools/build_file_index.py")
            return 1
        print("FILE_INDEX.md refleja los archivos reales")
        return 0

    INDICE.write_text(contenido, encoding="utf-8", newline="\n")
    print(f"FILE_INDEX.md generado: {len(archivos())} archivos")
    return 0


if __name__ == "__main__":
    sys.exit(main())
