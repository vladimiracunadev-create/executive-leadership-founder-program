"""El registro de fuentes cuadra con lo que las clases citan.

`scripts/verify-sources` ya hace estas comprobaciones y bloquea el CI; aquí se
repiten desde las pruebas por la misma razón que el resto de validadores: que
quien trabaje en local vea el fallo sin recordar qué script ejecutar, y que el
fallo señale la entrada concreta. Todo es offline: ninguna prueba abre la red.
"""

from __future__ import annotations

import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "tools"))

import sources_registry as reg  # noqa: E402


def test_el_registro_existe_y_parsea():
    registro = reg.cargar()
    assert registro["schema_version"] == 1
    assert registro["entries"], "el registro está vacío"


def test_cada_cita_de_clase_tiene_la_forma_canonica():
    malas = reg.lineas_invalidas()
    assert not malas, f"citas fuera de forma: {malas[:5]}"


def test_toda_obra_citada_esta_declarada():
    registro = reg.cargar()
    declaradas = {e["cited_as"] for e in registro["entries"]}
    faltan = sorted(set(reg.citas()) - declaradas)
    assert not faltan, f"citadas y no declaradas: {faltan[:5]}"


def test_ninguna_entrada_del_registro_queda_sin_usar():
    registro = reg.cargar()
    usadas = set(reg.citas())
    sobran = sorted(e["id"] for e in registro["entries"] if e["cited_as"] not in usadas)
    assert not sobran, f"entradas que nadie cita: {sobran[:5]}"


def test_los_libros_verificados_traen_isbn13_valido():
    registro = reg.cargar()
    malos = [
        e["id"]
        for e in registro["entries"]
        if e["type"] == "book" and e["status"] == "verificada" and not reg.isbn13_valido(e.get("isbn13", ""))
    ]
    assert not malos, f"ISBN-13 inválido o ausente: {malos}"


def test_los_articulos_verificados_traen_doi():
    registro = reg.cargar()
    malos = [
        e["id"]
        for e in registro["entries"]
        if e["type"] == "paper" and e["status"] == "verificada" and not reg.doi_valido(e.get("doi", ""))
    ]
    assert not malos, f"DOI inválido o ausente: {malos}"


def test_el_localizador_usa_la_forma_canonica_de_su_tipo():
    registro = reg.cargar()
    malos = []
    for entrada in registro["entries"]:
        esperado = reg.localizador_esperado(entrada)
        if esperado and entrada.get("locator") != esperado:
            malos.append(entrada["id"])
    assert not malos, f"localizadores fuera de forma: {malos[:5]}"


def test_ningun_bloque_de_fuentes_se_repite_entre_clases():
    bloques: dict[str, list[str]] = {}
    for clase in reg.clases():
        bloques.setdefault(clase.bloque, []).append(clase.relativa)
    repetidos = {k: v for k, v in bloques.items() if len(v) > 1}
    assert not repetidos, f"bloques repetidos: {list(repetidos.values())[:3]}"


def test_las_entradas_pendientes_declaran_su_motivo():
    registro = reg.cargar()
    mudas = [
        e["id"]
        for e in registro["entries"]
        if e["status"] == "pendiente" and not (e.get("note") or e.get("last_error"))
    ]
    assert not mudas, f"pendientes sin motivo declarado: {mudas}"
