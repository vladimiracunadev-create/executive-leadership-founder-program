"""Genera MANIFEST.md: qué contiene el repositorio, qué lo genera y qué garantiza.

La ficha técnica responde a una pregunta que ni el README ni el temario
contestan: **de qué me puedo fiar aquí y por qué**. Distingue lo que verifica
una máquina de lo que descansa en la bibliografía, y nombra la herramienta
concreta que produce cada documento generado.

Uso:
    python tools/build_manifest.py           # regenera MANIFEST.md
    python tools/build_manifest.py --check   # falla si está desactualizado
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import inventario  # noqa: E402

ROOT = inventario.ROOT
SALIDA = ROOT / "MANIFEST.md"

REPO = "https://github.com/vladimiracunadev-create/executive-leadership-founder-program"

PLANTILLA = """<!-- portada:inicio -->
<div align="center">

# 🧾 Ficha técnica

**Qué contiene el repositorio, qué herramienta genera cada documento y qué garantiza cada comprobación.**

[![Versión](https://img.shields.io/badge/versión-{version}-e67e22?style=flat-square)](CHANGELOG.md)
[![Generados](https://img.shields.io/badge/documentos%20generados-4-007c83?style=flat-square)](STATUS.md)
[![Validadores](https://img.shields.io/badge/validadores-8-2e8b57?style=flat-square)](README.md)

[🏠 Inicio](README.md) ·
[📚 Temario](SYLLABUS.md) ·
[📊 Estado](STATUS.md) ·
[🗂️ Índice de archivos](FILE_INDEX.md)

</div>
<!-- portada:fin -->

---

## 🏷️ Identificación

| Campo | Valor |
|---|---|
| **Nombre** | `executive-leadership-founder-program` |
| **Versión** | `{version}` |
| **Estado** | Programa completo · {etapas} etapas · {partes} partes · {clases} clases |
| **Licencia** | MIT para el contenido original y el código |
| **Idioma** | Español |
| **Repositorio** | <{repo}> |
| **Portal** | <https://vladimiracunadev-create.github.io/executive-leadership-founder-program/> |

> Las cifras de esta ficha describen la entrega actual y se recalculan al
> generarla. El avance vivo lo cuenta [`STATUS.md`](STATUS.md) leyendo los
> archivos: si esta ficha y aquel documento discrepan, el correcto es aquel.

## 📚 Contenido

| Componente | Cantidad |
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
| Obras catalogadas | {bibliografia} |
| Referencias citadas al cierre de clase | {referencias} |
| Documentos Markdown | {documentos} |

## 🧱 Contrato de una clase

Cada clase es una carpeta con tres archivos y un contrato fijo:

```text
modules/XX-slug/classes/NNN-tema/
├── README.md       ← teoría original, modelo mental, caso y práctica
├── assessment.md   ← prueba de criterio y aplicación
└── lesson.yaml     ← objetivos, duración, referencias y entregable
```

El `README.md` trae las **16 secciones** del estándar `deep-class-v2`, en este
orden: propósito · resultados de aprendizaje · agenda · conceptos centrales ·
modelo mental · desarrollo · lectura comparada · ejemplo trabajado · comparación
y límites · de profesional a owner · caso ejecutivo · práctica · errores
frecuentes · preguntas de comprobación · entregable · fuentes y verificación.

`tools/validate_repository.py` comprueba que estén las dieciséis, que los tres
archivos existan y que el título sea el mismo en los tres sitios.

## ⚙️ Documentos generados

Estos cuatro archivos **no se editan a mano**. Se regeneran desde el
repositorio y la CI los verifica con `--check`, de modo que un cambio que los
deje desfasados no puede entrar:

| Documento | Lo genera | Desde |
|---|---|---|
| [`SYLLABUS.md`](SYLLABUS.md) | `tools/build_syllabus.py` | Los `lesson.yaml` y los README de parte |
| [`STATUS.md`](STATUS.md) | `tools/build_status.py` | El recuento real de archivos y palabras |
| [`FILE_INDEX.md`](FILE_INDEX.md) | `tools/build_file_index.py` | Los archivos versionados |
| [`MANIFEST.md`](MANIFEST.md) | `tools/build_manifest.py` | El inventario del repositorio |

El portal de [GitHub Pages](https://vladimiracunadev-create.github.io/executive-leadership-founder-program/)
también se genera, con `tools/build_site.py`, y por eso `site/` no se versiona.

## ✅ Qué garantiza cada comprobación

| Comprobación | Garantiza | No garantiza |
|---|---|---|
| `validate_repository.py --strict` | Estructura, secciones, metadatos y numeración continua | Que el contenido de una sección sea correcto |
| `validate_depth.py` | Densidad mínima, referencias suficientes, ausencia de párrafos replicados y de similitud anormal | Que el argumento sea sólido |
| `check_links.py` | Que todo enlace relativo resuelva | Que el destino diga lo que promete el enlace |
| `build_*.py --check` | Que los documentos generados reflejen el repositorio | Nada sobre el material que describen |
| `build_site.py --check` | Que el portal se genere y sus enlaces internos resuelvan | Que el despliegue esté publicado |
| `pytest` | Estructura del árbol, integridad de los datos y del simulador | Corrección pedagógica |
| `detect_secrets.py` · `gitleaks` | Que no haya credenciales versionadas | — |
| `detect_pii.py` | Que los datos y plantillas sean sintéticos | — |

## ⚠️ Lo que ninguna comprobación cubre

La **exactitud conceptual** de un argumento de gestión y la **vigencia de una
norma** citada no las puede verificar un script. Descansan en la bibliografía de
cada clase y en la fecha de verificación que declara. El material chileno
—laboral, tributario y de formalización— exige revalidación en la fuente oficial
antes de cualquier uso real; el repositorio no sustituye a un abogado, un
contador ni un asesor.

---

<div align="center">

[🏠 Inicio](README.md) · [📚 Temario](SYLLABUS.md) · [📊 Estado](STATUS.md) · [🗂️ Índice de archivos](FILE_INDEX.md)

</div>
"""


def render() -> str:
    resumen = inventario.resumen()

    def miles(valor: int) -> str:
        return f"{valor:,}".replace(",", ".")

    return PLANTILLA.format(
        version=inventario.version(), repo=REPO,
        etapas=len(inventario.ETAPAS), partes=resumen.partes, clases=resumen.clases,
        horas=resumen.horas, labs=resumen.labs, proyectos=resumen.proyectos,
        casos=resumen.casos, plantillas=resumen.plantillas, escenarios=resumen.escenarios,
        bibliografia=resumen.bibliografia, referencias=miles(resumen.referencias_en_clase),
        documentos=resumen.documentos,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    contenido = render()
    actual = SALIDA.read_text(encoding="utf-8") if SALIDA.exists() else ""

    if args.check:
        if actual != contenido:
            print("MANIFEST.md está desactualizado. Ejecuta: python tools/build_manifest.py")
            return 1
        print("MANIFEST.md refleja el repositorio real")
        return 0

    SALIDA.write_text(contenido, encoding="utf-8", newline="\n")
    print("MANIFEST.md generado")
    return 0


if __name__ == "__main__":
    sys.exit(main())
