"""Genera STATUS.md contando el repositorio, no leyendo lo que dijo la versión anterior.

Un documento de estado escrito a mano deja de ser un estado en cuanto alguien
añade una clase y se olvida de la tabla. Este generador vuelve a contar cada
vez, y la CI lo ejecuta con `--check`: si el archivo del repositorio y lo que
hay en disco no coinciden, el cambio no entra.

Uso:
    python tools/build_status.py           # regenera STATUS.md
    python tools/build_status.py --check   # falla si está desactualizado
"""

from __future__ import annotations

import argparse
import re
import statistics
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import inventario  # noqa: E402

ROOT = inventario.ROOT
SALIDA = ROOT / "STATUS.md"

PLANTILLA = """<!-- portada:inicio -->
<div align="center">

# 📊 Estado del programa

**Lo que hay hoy en el repositorio, contado archivo por archivo.**

[![Versión](https://img.shields.io/badge/versión-{version}-e67e22?style=flat-square)](CHANGELOG.md)
[![Clases](https://img.shields.io/badge/clases-{clases}%2F{clases}-3fb950?style=flat-square)](SYLLABUS.md)
[![Generado por](https://img.shields.io/badge/generado%20por-build__status.py-007c83?style=flat-square)](tools/build_status.py)

[🏠 Inicio](README.md) ·
[📚 Temario](SYLLABUS.md) ·
[🧾 Ficha técnica](MANIFEST.md) ·
[🗺️ Roadmap](ROADMAP.md)

</div>
<!-- portada:fin -->

---

> Este documento **se genera**. Las cifras salen de contar los archivos del
> repositorio; ninguna está escrita a mano. Si una tabla del README discrepa de
> esta, la correcta es esta.

## 📦 Contenido publicado

| Métrica | Valor |
|---|---:|
| Etapas | {etapas} |
| Partes | {partes} |
| Clases | {clases} |
| Horas de estudio | {horas} |
| Laboratorios ejecutivos | {labs} |
| Evaluaciones de clase | {clases} |
| Proyectos de parte | {proyectos} |
| Casos integradores | {casos} |
| Plantillas de trabajo | {plantillas} |
| Escenarios del simulador | {escenarios} |
| Documentos Markdown | {documentos} |

## 📚 Densidad del material

| Métrica | Valor |
|---|---:|
| Palabras en las clases | {palabras} |
| Palabras por clase | {palabras_min}–{palabras_max} (mediana {palabras_mediana}) |
| Subsecciones de desarrollo por clase | {subsecciones_min}–{subsecciones_max} |
| Referencias citadas al cierre de clase | {referencias} |
| Referencias por clase | {referencias_min}–{referencias_max} (mediana {referencias_mediana}) |
| Bibliografía catalogada | {bibliografia} obras |

## 🧭 Cobertura por etapa

| Etapa | Partes | Clases | Horas | Nivel de salida |
|---|---:|---:|---:|---|
{tabla_etapas}

## ✅ Controles automáticos

Cada uno responde a una pregunta concreta sobre el material, y ninguno responde
por los demás:

| Control | Qué garantiza |
|---|---|
| `tools/validate_repository.py --strict` | Las {partes} partes, sus {clases} clases y sus tres archivos existen, con las 16 secciones del contrato y títulos coherentes entre `lesson.yaml`, clase y evaluación. |
| `tools/validate_depth.py` | Profundidad mínima por clase, referencias suficientes, ausencia de párrafos largos replicados y de similitud anormal dentro de una parte. |
| `tools/check_links.py` | Todos los enlaces relativos del repositorio resuelven. |
| `tools/build_syllabus.py --check` | El temario refleja las clases reales. |
| `tools/build_status.py --check` | Este documento refleja el repositorio real. |
| `tools/build_file_index.py --check` | El índice de archivos refleja los archivos reales. |
| `tools/build_site.py --check` | El portal se genera y sus enlaces internos resuelven. |
| `pytest` | Pruebas estructurales del árbol, los datos y el simulador. |

## ⚠️ Qué no verifica una máquina

Los controles anteriores comprueban estructura, integridad y densidad. **No**
comprueban la corrección conceptual de un argumento ni la vigencia de una norma
citada: eso descansa en la bibliografía de cada clase y en la fecha de
verificación que declara. El material legal, tributario y laboral chileno exige
revalidación en la fuente oficial antes de cualquier uso real.
"""


def render() -> str:
    partes = inventario.partes()
    resumen = inventario.resumen(partes)
    clases = [c for p in partes for c in p.clases]

    palabras = [len(re.findall(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ0-9]+",
                               c.ruta.read_text(encoding="utf-8"))) for c in clases]
    referencias = [len(c.referencias) for c in clases]
    subsecciones = []
    for clase in clases:
        texto = clase.ruta.read_text(encoding="utf-8")
        desarrollo = texto.split("## 📖 Desarrollo", 1)[-1].split("## 📚 Lectura comparada", 1)[0]
        subsecciones.append(len(re.findall(r"^### ", desarrollo, re.M)))

    filas = []
    for indice, etapa in enumerate(inventario.ETAPAS, start=1):
        nombre, desde, hasta, _, emoji, salida, _ = etapa
        propias = [p for p in partes if desde <= p.numero <= hasta]
        filas.append(
            f"| {emoji} {indice} · {nombre} | {len(propias)} | "
            f"{sum(len(p.clases) for p in propias)} | "
            f"{sum(p.horas for p in propias)} | {salida} |"
        )

    def miles(valor: int) -> str:
        return f"{valor:,}".replace(",", ".")

    return PLANTILLA.format(
        version=inventario.version(),
        etapas=len(inventario.ETAPAS),
        partes=resumen.partes,
        clases=resumen.clases,
        horas=resumen.horas,
        labs=resumen.labs,
        proyectos=resumen.proyectos,
        casos=resumen.casos,
        plantillas=resumen.plantillas,
        escenarios=resumen.escenarios,
        documentos=resumen.documentos,
        palabras=miles(resumen.palabras),
        palabras_min=miles(min(palabras)),
        palabras_max=miles(max(palabras)),
        palabras_mediana=miles(int(statistics.median(palabras))),
        subsecciones_min=min(subsecciones),
        subsecciones_max=max(subsecciones),
        referencias=miles(resumen.referencias_en_clase),
        referencias_min=min(referencias),
        referencias_max=max(referencias),
        referencias_mediana=int(statistics.median(referencias)),
        bibliografia=resumen.bibliografia,
        tabla_etapas="\n".join(filas),
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    contenido = render()
    actual = SALIDA.read_text(encoding="utf-8") if SALIDA.exists() else ""

    if args.check:
        if actual != contenido:
            print("STATUS.md está desactualizado. Ejecuta: python tools/build_status.py")
            return 1
        print("STATUS.md refleja el repositorio real")
        return 0

    SALIDA.write_text(contenido, encoding="utf-8", newline="\n")
    print("STATUS.md generado")
    return 0


if __name__ == "__main__":
    sys.exit(main())
