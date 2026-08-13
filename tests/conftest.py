"""Contexto compartido de las pruebas.

Las pruebas leen el repositorio real: no hay accesorios sintéticos porque lo que
se comprueba es precisamente que el material publicado cumpla su contrato.
Leerlo una sola vez por sesión evita recorrer 288 clases en cada prueba.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import inventario  # noqa: E402


@pytest.fixture(scope="session")
def raiz() -> Path:
    return ROOT


@pytest.fixture(scope="session")
def partes() -> list[inventario.Parte]:
    return inventario.partes()


@pytest.fixture(scope="session")
def clases(partes: list[inventario.Parte]) -> list[inventario.Clase]:
    return [clase for parte in partes for clase in parte.clases]


@pytest.fixture(scope="session")
def resumen(partes: list[inventario.Parte]) -> inventario.Resumen:
    return inventario.resumen(partes)
