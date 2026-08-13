"""Verifica que todos los enlaces relativos del repositorio apunten a algo real.

Un enlace roto en un programa de estudio es un callejón sin salida para quien lo
recorre: el temario promete una clase, la clase promete una plantilla, y quien
sigue el hilo se encuentra un 404. Por eso se trata como error de integración y
no como detalle cosmético.

Uso:
    python tools/check_links.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXCLUIDOS = {".git", ".github", "__pycache__", ".venv", "node_modules", "site"}

# Se busca el destino `](...)` sin exigir cómo es la etiqueta. La forma
# `[![insignia](url-externa)](destino-local)` que usan las portadas anida
# corchetes, y un patrón que empiece por `[` y prohíba `]` dentro nunca la
# alcanza: así es como los enlaces de las insignias dejaban de comprobarse.
ENLACE = re.compile(r"\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
EXTERNOS = ("http://", "https://", "mailto:", "tel:", "#")

# Lo que está dentro de un bloque cercado o de un tramo `entre acentos` no es un
# enlace, es texto que ilustra la forma de uno. La documentación del propio
# repositorio escribe patrones de enlace como ejemplo, y sin esto se
# comprobarían como si fueran destinos reales.
BLOQUE_CERCADO = re.compile(r"^```.*?^```", re.S | re.M)
CODIGO_EN_LINEA = re.compile(r"`[^`\n]*`")


def sin_codigo(texto: str) -> str:
    return CODIGO_EN_LINEA.sub("`` ", BLOQUE_CERCADO.sub("", texto))


def archivos_markdown() -> list[Path]:
    return sorted(
        ruta for ruta in ROOT.rglob("*.md")
        if not any(parte in EXCLUIDOS for parte in ruta.relative_to(ROOT).parts)
    )


def main() -> int:
    rotos: list[str] = []
    revisados = 0
    archivos = archivos_markdown()

    for ruta in archivos:
        texto = sin_codigo(ruta.read_text(encoding="utf-8"))
        for crudo in ENLACE.findall(texto):
            destino = crudo.strip()
            if not destino or destino.startswith(EXTERNOS) or "://" in destino:
                continue
            revisados += 1
            resuelto = (ruta.parent / destino.split("#", 1)[0]).resolve()
            if not resuelto.exists():
                rotos.append(f"{ruta.relative_to(ROOT).as_posix()} -> {destino}")

    print(f"archivos revisados: {len(archivos)}")
    print(f"enlaces relativos:  {revisados}")

    if rotos:
        print(f"\n{len(rotos)} enlace(s) roto(s):")
        for item in rotos[:60]:
            print(f"  - {item}")
        if len(rotos) > 60:
            print(f"  ... y {len(rotos) - 60} más")
        return 1

    print("\nTodos los enlaces relativos resuelven")
    return 0


if __name__ == "__main__":
    sys.exit(main())
