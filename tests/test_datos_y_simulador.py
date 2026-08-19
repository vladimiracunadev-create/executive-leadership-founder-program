"""Los datos que alimentan el simulador y la bibliografía están completos.

Un escenario sin efectos declarados o con opciones repetidas no enseña a decidir:
muestra texto. Estas pruebas cubren esa clase de fallo, que no rompe nada al
ejecutar y solo se nota cuando alguien ya está usando el simulador.
"""

from __future__ import annotations

import csv
import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

DIMENSIONES = {"cash", "people", "trust", "execution", "risk", "growth"}


@pytest.fixture(scope="module")
def escenarios(raiz: Path) -> list[dict]:
    return json.loads((raiz / "data" / "scenarios.json").read_text(encoding="utf-8"))


def test_hay_cuarenta_y_ocho_escenarios(escenarios):
    assert len(escenarios) == 48


def test_los_identificadores_de_escenario_son_unicos(escenarios):
    identificadores = [e["id"] for e in escenarios]
    assert len(set(identificadores)) == len(identificadores)


def test_cada_escenario_trae_sus_campos(escenarios):
    incompletos = [e.get("id", "?") for e in escenarios
                   if not all(k in e for k in ("id", "part", "title", "prompt",
                                               "options", "debrief"))]
    assert not incompletos, f"escenarios incompletos: {incompletos}"


def test_cada_escenario_ofrece_al_menos_dos_opciones(escenarios):
    """Una sola opción no es una decisión."""
    pobres = [e["id"] for e in escenarios if len(e.get("options", [])) < 2]
    assert not pobres, f"escenarios con menos de dos opciones: {pobres}"


def test_cada_opcion_declara_efectos_en_dimensiones_conocidas(escenarios):
    problemas = []
    for escenario in escenarios:
        for opcion in escenario.get("options", []):
            efectos = opcion.get("effects") or {}
            if not efectos:
                problemas.append(f"{escenario['id']}/{opcion.get('key')}: sin efectos")
            elif not set(efectos) <= DIMENSIONES:
                desconocidas = set(efectos) - DIMENSIONES
                problemas.append(f"{escenario['id']}: dimensión desconocida {desconocidas}")
    assert not problemas, f"efectos mal declarados: {problemas[:10]}"


def test_los_escenarios_apuntan_a_partes_existentes(escenarios, partes):
    numeros = {p.numero for p in partes}
    huerfanos = [e["id"] for e in escenarios if e["part"] not in numeros]
    assert not huerfanos, f"escenarios de una parte inexistente: {huerfanos}"


def test_la_bibliografia_esta_catalogada(raiz: Path):
    with (raiz / "data" / "books.csv").open(encoding="utf-8", newline="") as archivo:
        filas = list(csv.DictReader(archivo))
    assert len(filas) >= 200
    assert {"key", "author", "title", "area", "type"} <= set(filas[0])
    claves = [f["key"] for f in filas]
    assert len(set(claves)) == len(claves), "hay claves de obra repetidas"


def test_el_mapa_normativo_laboral_es_json_valido(raiz: Path):
    datos = json.loads((raiz / "data" / "chile_labor_law_map.json").read_text(encoding="utf-8"))
    assert datos, "chile_labor_law_map.json está vacío"


def test_el_simulador_lista_los_escenarios(raiz: Path, escenarios):
    """Comprueba que el simulador arranca y ve los mismos datos que las pruebas.

    La salida se lee como UTF-8 y el hijo se ejecuta con `PYTHONIOENCODING` en
    UTF-8: sin eso, en Windows el proceso escribe en cp1252 y los titulos con
    tilde llegan como bytes que no decodifican.
    """
    entorno = {**os.environ, "PYTHONIOENCODING": "utf-8"}
    resultado = subprocess.run(
        [sys.executable, str(raiz / "apps" / "executive_simulator.py"), "--list"],
        capture_output=True, text=True, encoding="utf-8", timeout=60, check=True,
        env=entorno,
    )
    lineas = [l for l in resultado.stdout.splitlines() if l.strip()]
    assert len(lineas) == len(escenarios)


def test_hay_una_plantilla_por_cada_entregable_citado(raiz: Path, clases):
    """Un entregable sin plantilla deja al estudiante ante una hoja en blanco."""
    disponibles = {p.name for p in (raiz / "templates").glob("*.md")}
    citados = set()
    for clase in clases:
        for linea in (clase.ruta.parent / "lesson.yaml").read_text(encoding="utf-8").splitlines():
            if linea.startswith("deliverable:"):
                citados.add(linea.split(":", 1)[1].strip().strip('"'))
    faltan = sorted(citados - disponibles)
    assert not faltan, f"entregables sin plantilla en templates/: {faltan}"
