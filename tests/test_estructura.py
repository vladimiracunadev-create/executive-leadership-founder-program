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
    for etapa in inventario.ETAPAS:
        cubiertas |= set(range(etapa.desde, etapa.hasta + 1))
    assert cubiertas == {p.numero for p in partes}


def _contraste(color: str, fondo: str) -> float:
    """Razón de contraste WCAG entre dos colores en formato `#rrggbb`."""
    def luminancia(hexadecimal: str) -> float:
        canales = [int(hexadecimal[i:i + 2], 16) / 255 for i in (1, 3, 5)]
        lineal = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
                  for c in canales]
        return 0.2126 * lineal[0] + 0.7152 * lineal[1] + 0.0722 * lineal[2]

    claro, oscuro = sorted((luminancia(color), luminancia(fondo)), reverse=True)
    return (claro + 0.05) / (oscuro + 0.05)


def test_los_colores_de_etapa_son_legibles_en_los_dos_temas():
    """El color de etapa se usa en el número de clase del temario: texto de 16 px.

    Con un solo tono por etapa, cuatro de las seis quedaban por debajo del
    mínimo AA en uno de los dos temas —el verde se desvanecía en claro y el
    azul en oscuro— y no lo notaba nadie porque el portal se revisa en un tema
    a la vez.
    """
    import inventario

    minimo = 4.5
    flojos = []
    for etapa in inventario.ETAPAS:
        sobre_claro = _contraste(etapa.color_claro, "#ffffff")
        sobre_oscuro = _contraste(etapa.color_oscuro, "#0d1117")
        if sobre_claro < minimo:
            flojos.append(f"{etapa.nombre}: {sobre_claro:.2f} sobre fondo claro")
        if sobre_oscuro < minimo:
            flojos.append(f"{etapa.nombre}: {sobre_oscuro:.2f} sobre fondo oscuro")
    assert not flojos, f"colores por debajo de AA ({minimo}:1): {flojos}"


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
