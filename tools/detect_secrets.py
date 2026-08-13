"""Busca credenciales reales versionadas en el repositorio.

El material del programa habla de gobierno de riesgo, ciberseguridad y
cumplimiento; publicar un token dentro de él sería la peor forma posible de
enseñarlo. Este detector distingue dos cosas:

* un patrón de secreto REAL (clave privada, token de proveedor, cadena de
  conexión con contraseña) → error;
* un valor de ejemplo marcado como tal en la propia línea → se ignora, porque
  una plantilla necesita poder mostrar la forma de un secreto sin contenerlo.

Complementa a gitleaks, que mira el historial completo con reglas genéricas:
esto mira el árbol actual con reglas que conocen el material.

Uso:
    python tools/detect_secrets.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXCLUIDOS = {".git", ".venv", "node_modules", "site", "__pycache__", ".pytest_cache"}
SUFIJOS_BINARIOS = {".png", ".jpg", ".jpeg", ".gif", ".pdf", ".zip", ".ico", ".woff2"}

PATRONES: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("clave privada", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |PGP )?PRIVATE KEY-----")),
    ("clave de acceso AWS", re.compile(r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b")),
    ("token de GitHub", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{36,}\b")),
    ("token de Slack", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}\b")),
    ("clave de Google", re.compile(r"\bAIza[0-9A-Za-z_\-]{35}\b")),
    ("token de Stripe", re.compile(r"\b(?:sk|rk)_live_[0-9A-Za-z]{20,}\b")),
    ("cadena de conexión con contraseña",
     re.compile(r"\b[a-z][a-z0-9+.-]*://[^\s:/@]+:[^\s:/@]{6,}@[^\s/]+")),
    ("asignación de secreto",
     re.compile(r"(?i)\b(?:password|passwd|secret|api[_-]?key|token|private[_-]?key)\b"
                r"\s*[:=]\s*[\"'][^\"'\n]{12,}[\"']")),
)

# Marcas que identifican un valor didáctico. Cada una está aquí porque el
# material la usa para mostrar la FORMA de un secreto, no por comodidad.
MARCAS_DE_EJEMPLO = (
    "ejemplo", "example", "sample", "placeholder", "cambiar", "changeme",
    "tu-clave", "tu_clave", "your-", "xxxxx", "<", "...", "ficticio",
    "sintétic", "sintetic", "synthetic", "dummy", "fake", "redacted", "no-usar",
)


def archivos() -> list[Path]:
    return sorted(
        ruta for ruta in ROOT.rglob("*")
        if ruta.is_file()
        and not any(parte in EXCLUIDOS for parte in ruta.relative_to(ROOT).parts)
        and ruta.suffix.lower() not in SUFIJOS_BINARIOS
    )


def es_ejemplo(linea: str) -> bool:
    minuscula = linea.lower()
    return any(marca in minuscula for marca in MARCAS_DE_EJEMPLO)


def main() -> int:
    hallazgos: list[str] = []
    revisados = 0

    for ruta in archivos():
        try:
            texto = ruta.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        revisados += 1
        rel = ruta.relative_to(ROOT).as_posix()
        for numero, linea in enumerate(texto.splitlines(), start=1):
            if es_ejemplo(linea):
                continue
            for nombre, patron in PATRONES:
                if patron.search(linea):
                    hallazgos.append(f"{rel}:{numero}: posible {nombre}")
                    break

    # Un .env versionado es un hallazgo por sí mismo, tenga lo que tenga dentro.
    for env in ROOT.rglob(".env"):
        if not any(parte in EXCLUIDOS for parte in env.relative_to(ROOT).parts):
            hallazgos.append(f"{env.relative_to(ROOT).as_posix()}: un .env nunca se versiona")

    print(f"archivos revisados: {revisados}")

    if hallazgos:
        print(f"\n{len(hallazgos)} hallazgo(s):")
        for item in hallazgos[:40]:
            print(f"  - {item}")
        if len(hallazgos) > 40:
            print(f"  ... y {len(hallazgos) - 40} más")
        print("\nSi alguno es un valor de ejemplo, márcalo como tal en la propia línea.")
        return 1

    print("\nSin credenciales detectadas")
    return 0


if __name__ == "__main__":
    sys.exit(main())
