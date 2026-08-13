"""Busca datos personales reales en los datos, las plantillas y el portafolio.

El programa trabaja con casos de empresa, contratos y datos laborales chilenos,
y exige que todo eso sea sintético. Este detector comprueba que la exigencia se
cumple justo donde el dato viaja: `data/`, `templates/`, `portfolio/`,
`academy/` y `cases/`.

Los identificadores se confirman antes de dar la alarma —dígito verificador del
RUT, Luhn de la tarjeta—, porque un número inventado que no valida es
precisamente lo que se espera de un dato didáctico, y avisar de él sería ruido.

Uso:
    python tools/detect_pii.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

AMBITOS = ("data", "templates", "portfolio", "academy", "cases")
EXTENSIONES = {".csv", ".json", ".tsv", ".txt", ".md", ".yml", ".yaml"}


def luhn(numero: str) -> bool:
    """Dígito verificador de una tarjeta.

    Un número de 16 cifras que NO pasa Luhn es casi con seguridad sintético;
    uno que sí lo pasa merece una mirada humana.
    """
    digitos = [int(c) for c in numero if c.isdigit()]
    if len(digitos) < 13:
        return False
    total = 0
    for indice, digito in enumerate(reversed(digitos)):
        if indice % 2 == 1:
            digito *= 2
            if digito > 9:
                digito -= 9
        total += digito
    return total % 10 == 0


def rut_valido(rut: str) -> bool:
    """Dígito verificador de un RUT chileno (módulo 11)."""
    cuerpo = re.sub(r"[^0-9]", "", rut[:-1])
    verificador = rut[-1].upper()
    if not cuerpo or len(cuerpo) < 7:
        return False
    suma, factor = 0, 2
    for caracter in reversed(cuerpo):
        suma += int(caracter) * factor
        factor = 2 if factor == 7 else factor + 1
    resto = 11 - (suma % 11)
    return {11: "0", 10: "K"}.get(resto, str(resto)) == verificador


DETECTORES = (
    ("RUT con dígito verificador válido",
     re.compile(r"\b\d{1,2}\.?\d{3}\.?\d{3}-[\dkK]\b"), rut_valido),
    ("número de tarjeta que pasa Luhn",
     re.compile(r"\b(?:\d[ -]?){13,19}\b"), luhn),
    ("IBAN con formato completo",
     re.compile(r"\b[A-Z]{2}\d{2}[A-Z0-9]{11,30}\b"), lambda s: True),
    ("dirección de correo con dominio real",
     re.compile(r"\b[\w.+-]+@[\w-]+\.[\w.]{2,}\b"),
     lambda s: not s.lower().endswith((".example", ".test", ".invalid",
                                       "example.com", "empresa.cl", "correo.cl"))),
)


def archivos() -> list[Path]:
    encontrados: set[Path] = set()
    for ambito in AMBITOS:
        base = ROOT / ambito
        if base.exists():
            encontrados |= {p for p in base.rglob("*")
                            if p.is_file() and p.suffix.lower() in EXTENSIONES}
    return sorted(encontrados)


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
            for nombre, patron, confirma in DETECTORES:
                for coincidencia in patron.findall(linea):
                    valor = coincidencia if isinstance(coincidencia, str) else coincidencia[0]
                    if confirma(valor.strip()):
                        hallazgos.append(f"{rel}:{numero}: {nombre} → {valor.strip()[:24]}")
                        break

    print(f"archivos revisados: {revisados}")

    if hallazgos:
        print(f"\n{len(hallazgos)} hallazgo(s):")
        for item in hallazgos[:40]:
            print(f"  - {item}")
        if len(hallazgos) > 40:
            print(f"  ... y {len(hallazgos) - 40} más")
        print("\nLos datos del repositorio deben ser sintéticos. Si un valor lo es y aun así "
              "pasa la comprobación, cámbialo: un dato que parece real se trata como real.")
        return 1

    print("\nSin datos personales detectados en los ámbitos revisados")
    return 0


if __name__ == "__main__":
    sys.exit(main())
