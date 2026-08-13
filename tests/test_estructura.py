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


def test_el_readme_lista_las_24_partes_con_su_rango_real(raiz: Path, partes):
    """La tabla de partes del README se escribe a mano y se desincroniza sola.

    Ya pasó con el título de la parte 19, que el README traía recortado. Aquí se
    comprueba fila por fila contra el árbol: número, título exacto, número de
    clases, rango de numeración y enlace al README de la parte.
    """
    readme = (raiz / "README.md").read_text(encoding="utf-8")
    problemas = []
    for parte in partes:
        primera, ultima = parte.clases[0].numero, parte.clases[-1].numero
        fila = (f"| {parte.numero:02d} | {parte.titulo} | "
                f"{len(parte.clases)} ({primera:03d}–{ultima:03d}) |")
        if fila not in readme:
            problemas.append(f"parte {parte.numero:02d}: fila ausente o desactualizada")
        if f"({parte.ruta_md})" not in readme:
            problemas.append(f"parte {parte.numero:02d}: falta el enlace a su README")
    assert not problemas, f"el README no refleja las partes reales: {problemas}"


def test_el_readme_no_anuncia_cifras_que_no_existen(raiz: Path, resumen):
    """Las cifras de la cabecera y de la tabla resumen salen del recuento real."""
    readme = (raiz / "README.md").read_text(encoding="utf-8")
    esperadas = {
        "clases": resumen.clases,
        "partes": resumen.partes,
        "horas": resumen.horas,
        "laboratorios": resumen.labs,
        "casos": resumen.casos,
        "plantillas": resumen.plantillas,
        "escenarios": resumen.escenarios,
        "obras": resumen.bibliografia,
    }
    ausentes = [f"{nombre}={valor}" for nombre, valor in esperadas.items()
                if str(valor) not in readme]
    assert not ausentes, f"el README no menciona estas cifras reales: {ausentes}"
