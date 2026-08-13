"""El árbol del programa cumple lo que el README promete.

Estas pruebas no comprueban código: comprueban que el material publicado tenga
la forma que el repositorio declara. Si alguna falla, hay una diferencia entre
lo que se dice que hay y lo que hay.
"""

from __future__ import annotations

from pathlib import Path

PARTES = 24
CLASES_POR_PARTE = 12
LABS_POR_PARTE = 4
CLASES = PARTES * CLASES_POR_PARTE


def test_hay_veinticuatro_partes(partes):
    assert len(partes) == PARTES


def test_cada_parte_tiene_doce_clases(partes):
    desviadas = {p.numero: len(p.clases) for p in partes if len(p.clases) != CLASES_POR_PARTE}
    assert not desviadas, f"partes con un número de clases distinto de 12: {desviadas}"


def test_cada_parte_tiene_cuatro_laboratorios(partes):
    desviadas = {p.numero: len(p.labs) for p in partes if len(p.labs) != LABS_POR_PARTE}
    assert not desviadas, f"partes con un número de laboratorios distinto de 4: {desviadas}"


def test_el_total_de_clases_es_288(clases):
    assert len(clases) == CLASES


def test_cada_parte_tiene_proyecto_y_readme(partes):
    faltan = [p.numero for p in partes
              if not (p.directorio / "project.md").exists()
              or not (p.directorio / "README.md").exists()]
    assert not faltan, f"partes sin README o project.md: {faltan}"


def test_cada_clase_tiene_sus_tres_archivos(clases):
    faltan = []
    for clase in clases:
        carpeta = clase.ruta.parent
        for archivo in ("README.md", "assessment.md", "lesson.yaml"):
            if not (carpeta / archivo).exists():
                faltan.append(f"{carpeta.name}/{archivo}")
    assert not faltan, f"archivos ausentes: {faltan[:10]}"


def test_la_numeracion_de_clases_es_continua(clases):
    numeros = sorted(c.numero for c in clases)
    assert numeros == list(range(1, CLASES + 1))


def test_hay_un_caso_integrador_por_parte(raiz: Path, partes):
    casos = list((raiz / "cases").glob("case-*.md"))
    assert len(casos) == len(partes)


def test_las_etapas_cubren_todas_las_partes(partes):
    import inventario

    cubiertas = set()
    for _, desde, hasta, *_ in inventario.ETAPAS:
        cubiertas |= set(range(desde, hasta + 1))
    assert cubiertas == {p.numero for p in partes}


def test_cada_parte_declara_etapa_salida_y_horas(partes):
    incompletas = [p.numero for p in partes if not (p.etapa and p.salida and p.horas)]
    assert not incompletas, f"partes con cabecera incompleta: {incompletas}"


def test_las_horas_declaradas_suman_720(resumen):
    assert resumen.horas == 720


def test_la_version_dice_lo_mismo_en_todos_los_archivos(raiz: Path):
    """Llegó a haber tres versiones distintas conviviendo sin que nada avisara."""
    import validate_repository

    problemas = validate_repository.validar_version()
    assert not problemas, f"la versión no está sincronizada: {problemas}"
