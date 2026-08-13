"""Valida la estructura del programa contra el contrato de clase.

El programa promete una cosa concreta: 24 partes, 12 clases por parte, cuatro
laboratorios por parte, y cada clase con sus tres archivos y sus dieciséis
secciones obligatorias. Este validador es lo que impide que esa promesa se
convierta en una afirmación del README que ya no describe el repositorio.

Comprueba, por orden:

* que existan las 24 partes con su `README.md` y su `project.md`;
* que cada parte tenga exactamente 12 clases y 4 laboratorios;
* que cada clase traiga `README.md`, `assessment.md` y `lesson.yaml`;
* que el `README.md` de cada clase tenga las 16 secciones del contrato;
* que el `lesson.yaml` declare los campos que el resto de herramientas leen;
* que la numeración de clases sea continua de 001 a 288, sin huecos ni saltos;
* que los conjuntos de datos que el material usa estén completos.

Uso:
    python tools/validate_repository.py
    python tools/validate_repository.py --strict   # además exige metadatos ricos
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULES = ROOT / "modules"

PARTES_ESPERADAS = 24
CLASES_POR_PARTE = 12
LABS_POR_PARTE = 4
ESCENARIOS_ESPERADOS = 48

# Las dieciséis secciones del estándar `deep-class-v2`. El orden importa: es el
# recorrido pedagógico de la clase, no una lista de comprobación suelta.
SECCIONES = (
    "## 🎯 Propósito",
    "## 📚 Resultados de aprendizaje",
    "## 🧭 Agenda",
    "## 🧩 Conceptos centrales",
    "## 🧠 Modelo mental",
    "## 📖 Desarrollo",
    "## 📚 Lectura comparada",
    "## 🧮 Ejemplo trabajado",
    "## 🔀 Comparación y límites",
    "## 🪜 De profesional a owner",
    "## 🏢 Caso ejecutivo",
    "## 🧪 Práctica",
    "## ⚠️ Errores frecuentes",
    "## ❓ Preguntas de comprobación",
    "## 📥 Entregable",
    "## 📗 Fuentes y verificación",
)

# Campos que `lesson.yaml` debe declarar porque otras herramientas los leen:
# el generador del temario, el del portal y el índice de archivos.
CAMPOS_LECCION = ("id", "part", "title", "duration_minutes", "level", "objectives", "references")


def leer_yaml_plano(ruta: Path) -> dict[str, object]:
    """Lee el subconjunto de YAML que usan los `lesson.yaml`.

    Se hace a mano y no con PyYAML a propósito: las herramientas de validación
    del repositorio funcionan con la biblioteca estándar, de modo que cualquiera
    pueda comprobar el material sin instalar nada. El formato de los archivos
    es fijo (`clave: valor` y listas de guiones), así que no hace falta más.
    """
    datos: dict[str, object] = {}
    clave_lista: str | None = None
    for linea in ruta.read_text(encoding="utf-8").splitlines():
        if not linea.strip() or linea.lstrip().startswith("#"):
            continue
        if linea.startswith("  - ") and clave_lista:
            datos.setdefault(clave_lista, [])
            lista = datos[clave_lista]
            assert isinstance(lista, list)
            lista.append(linea[4:].strip().strip('"'))
            continue
        if re.match(r"^[A-Za-z_][\w-]*:", linea):
            clave, _, valor = linea.partition(":")
            clave = clave.strip()
            valor = valor.strip().strip('"')
            if valor:
                datos[clave] = valor
                clave_lista = None
            else:
                datos[clave] = []
                clave_lista = clave
    return datos


def titulo_de_parte(parte: Path) -> str:
    """Título en español de la parte, tomado de la primera línea de su README."""
    primera = (parte / "README.md").read_text(encoding="utf-8").splitlines()[0]
    return re.sub(r"^#\s*Parte\s+\d+\s*[—-]\s*", "", primera).strip()


def titulos_coherentes(clase: Path, titulo: str, rel: str) -> list[str]:
    """El título de `lesson.yaml` debe encabezar el README y la evaluación."""
    problemas: list[str] = []
    numero = clase.name.split("-", 1)[0]

    readme = clase / "README.md"
    if readme.exists():
        primera = readme.read_text(encoding="utf-8").splitlines()[0]
        if primera.strip() != f"# Clase {numero} — {titulo}":
            problemas.append(f"{rel}: el H1 del README no coincide con lesson.yaml")

    assessment = clase / "assessment.md"
    if assessment.exists():
        primera = assessment.read_text(encoding="utf-8").splitlines()[0]
        if primera.strip() != f"# Evaluación — Clase {numero}: {titulo}":
            problemas.append(f"{rel}: el H1 de la evaluación no coincide con lesson.yaml")

    return problemas


def validar(estricto: bool) -> list[str]:
    errores: list[str] = []

    partes = sorted(p for p in MODULES.glob("[0-9][0-9]-*") if p.is_dir())
    if len(partes) != PARTES_ESPERADAS:
        errores.append(f"se esperaban {PARTES_ESPERADAS} partes y hay {len(partes)}")

    numeros_de_clase: list[int] = []
    total_clases = 0
    total_labs = 0

    for parte in partes:
        rel = parte.relative_to(ROOT).as_posix()

        for obligatorio in ("README.md", "project.md"):
            if not (parte / obligatorio).exists():
                errores.append(f"{rel}: falta {obligatorio}")

        clases = sorted(d for d in (parte / "classes").glob("*") if d.is_dir())
        labs = sorted((parte / "labs").glob("lab-*.md"))
        total_clases += len(clases)
        total_labs += len(labs)

        if len(clases) != CLASES_POR_PARTE:
            errores.append(f"{rel}: {len(clases)} clases, se esperaban {CLASES_POR_PARTE}")
        if len(labs) != LABS_POR_PARTE:
            errores.append(f"{rel}: {len(labs)} laboratorios, se esperaban {LABS_POR_PARTE}")

        for clase in clases:
            rel_clase = clase.relative_to(ROOT).as_posix()

            for obligatorio in ("README.md", "assessment.md", "lesson.yaml"):
                if not (clase / obligatorio).exists():
                    errores.append(f"{rel_clase}: falta {obligatorio}")

            readme = clase / "README.md"
            if readme.exists():
                texto = readme.read_text(encoding="utf-8")
                faltantes = [s for s in SECCIONES if s not in texto]
                # Se reporta la cuenta y no cada sección: una clase a la que le
                # faltan diez secciones no está incompleta, está sin escribir.
                if len(faltantes) > 3:
                    errores.append(
                        f"{rel_clase}: faltan {len(faltantes)} de {len(SECCIONES)} secciones"
                    )
                else:
                    errores += [f"{rel_clase}: falta la sección {s}" for s in faltantes]

                # La cabecera de la clase declara a qué parte pertenece. Si
                # cita otra, quien llega desde el temario cree haberse perdido.
                titulo_parte = titulo_de_parte(parte)
                esperado = f"**Parte:** {parte.name.split('-', 1)[0]} — {titulo_parte}"
                if esperado not in texto:
                    errores.append(f"{rel_clase}: la cabecera no declara «{esperado}»")

            leccion = clase / "lesson.yaml"
            if leccion.exists():
                datos = leer_yaml_plano(leccion)
                # El mismo título tiene que aparecer en los tres archivos de la
                # clase. Cuando divergen, el temario enlaza un nombre y el
                # documento muestra otro, que es como se pierde la confianza en
                # un índice de 288 entradas.
                titulo = str(datos.get("title", "")).strip()
                if titulo:
                    errores += titulos_coherentes(clase, titulo, rel_clase)
                for campo in CAMPOS_LECCION:
                    if not datos.get(campo):
                        errores.append(f"{rel_clase}/lesson.yaml: falta el campo `{campo}`")
                if datos.get("id"):
                    try:
                        numeros_de_clase.append(int(str(datos["id"])))
                    except ValueError:
                        errores.append(f"{rel_clase}/lesson.yaml: `id` no es un número")
                if estricto:
                    objetivos = datos.get("objectives") or []
                    referencias = datos.get("references") or []
                    if isinstance(objetivos, list) and len(objetivos) < 5:
                        errores.append(f"{rel_clase}/lesson.yaml: menos de 5 objetivos")
                    if isinstance(referencias, list) and len(referencias) < 5:
                        errores.append(f"{rel_clase}/lesson.yaml: menos de 5 referencias")

    esperado = PARTES_ESPERADAS * CLASES_POR_PARTE
    if total_clases != esperado:
        errores.append(f"se esperaban {esperado} clases y hay {total_clases}")
    if total_labs != PARTES_ESPERADAS * LABS_POR_PARTE:
        errores.append(
            f"se esperaban {PARTES_ESPERADAS * LABS_POR_PARTE} laboratorios y hay {total_labs}"
        )

    # Una numeración con huecos rompe el temario y las referencias cruzadas
    # entre clases, que se citan por número y no por ruta.
    if numeros_de_clase:
        continua = sorted(numeros_de_clase) == list(range(1, len(numeros_de_clase) + 1))
        if not continua:
            faltan = sorted(set(range(1, esperado + 1)) - set(numeros_de_clase))
            errores.append(f"numeración discontinua; faltan los números {faltan[:12]}")

    errores += validar_datos()
    return errores


def validar_datos() -> list[str]:
    """Los conjuntos de datos que el simulador y la bibliografía necesitan."""
    errores: list[str] = []

    escenarios_json = ROOT / "data" / "scenarios.json"
    if not escenarios_json.exists():
        return ["falta data/scenarios.json"]

    escenarios = json.loads(escenarios_json.read_text(encoding="utf-8"))
    if len(escenarios) != ESCENARIOS_ESPERADOS:
        errores.append(
            f"data/scenarios.json: {len(escenarios)} escenarios, "
            f"se esperaban {ESCENARIOS_ESPERADOS}"
        )
    for escenario in escenarios:
        for campo in ("id", "part", "title", "prompt", "options", "debrief"):
            if campo not in escenario:
                errores.append(f"escenario {escenario.get('id', '?')}: falta `{campo}`")
        # Sin efectos declarados el escenario no puede puntuarse y el simulador
        # solo mostraría texto.
        for opcion in escenario.get("options", []):
            if not opcion.get("effects"):
                errores.append(f"escenario {escenario.get('id', '?')}: opción sin `effects`")

    for obligatorio in ("data/books.csv", "data/official_sources.json",
                        "data/chile_labor_law_map.json", "docs/BOOKS.md"):
        if not (ROOT / obligatorio).exists():
            errores.append(f"falta {obligatorio}")

    errores += validar_version()
    return errores


def validar_version() -> list[str]:
    """La versión vive en tres archivos y tiene que decir lo mismo en los tres.

    Llegó a haber `1.1.0` en `VERSION` mientras el README anunciaba `2.0.0` y el
    currículo seguía en `1.0.0`. Ninguna herramienta se quejaba, porque nadie las
    comparaba.
    """
    errores: list[str] = []
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()

    curriculo = json.loads((ROOT / "curriculum" / "curriculum.json").read_text(encoding="utf-8"))
    if curriculo.get("version") != version:
        errores.append(
            f"curriculum.json declara la versión {curriculo.get('version')!r} "
            f"y VERSION dice {version!r}"
        )

    yaml_texto = (ROOT / "curriculum" / "curriculum.yaml").read_text(encoding="utf-8")
    encontrada = re.search(r'^version:\s*"?([^"\n]+)"?', yaml_texto, re.M)
    if not encontrada or encontrada.group(1).strip() != version:
        declarada = encontrada.group(1).strip() if encontrada else None
        errores.append(
            f"curriculum.yaml declara la versión {declarada!r} y VERSION dice {version!r}"
        )

    if f"versión-{version}-" not in (ROOT / "README.md").read_text(encoding="utf-8"):
        errores.append(f"la insignia de versión del README no dice {version}")

    if f"## {version} —" not in (ROOT / "CHANGELOG.md").read_text(encoding="utf-8"):
        errores.append(f"CHANGELOG.md no tiene una entrada para la versión {version}")

    return errores


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict", action="store_true",
                        help="exige además objetivos y referencias completos en lesson.yaml")
    args = parser.parse_args()

    errores = validar(args.strict)

    if errores:
        print(f"VALIDACIÓN FALLIDA: {len(errores)} problema(s)")
        for problema in errores[:120]:
            print(f"  - {problema}")
        if len(errores) > 120:
            print(f"  ... y {len(errores) - 120} más")
        return 1

    clases = len(list(MODULES.glob("*/classes/*/README.md")))
    labs = len(list(MODULES.glob("*/labs/lab-*.md")))
    escenarios = len(json.loads((ROOT / "data" / "scenarios.json").read_text(encoding="utf-8")))
    print(
        f"OK · {PARTES_ESPERADAS} partes · {clases} clases · {labs} laboratorios · "
        f"{escenarios} escenarios"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
