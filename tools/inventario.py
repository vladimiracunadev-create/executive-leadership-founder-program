"""Lee el repositorio y devuelve lo que hay, no lo que se dijo que había.

Todos los documentos generados —el temario, el estado, el índice de archivos y
el portal— parten de aquí. Tener un único lector evita el problema clásico de
este tipo de repositorios: que cada documento cuente las clases a su manera y
acaben discrepando entre sí sin que nadie sepa cuál miente.

Ninguna cifra del programa se escribe a mano en ningún sitio: se cuenta.
"""

from __future__ import annotations

import csv
import json
import re
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULES = ROOT / "modules"

# Etapa, rango de partes, color, emoji, nivel de salida e idea. El color es el
# mismo en el README, en el temario y en el portal, para que las tres
# superficies se lean como el mismo programa.
ETAPAS: tuple[tuple[str, int, int, str, str, str, str], ...] = (
    ("Autoliderazgo y fundamentos ejecutivos", 0, 3, "#2ea44f", "🟢",
     "Profesional → Líder",
     "El punto de partida es la persona. Al terminarla se decide con supuestos "
     "explícitos, se comunica una decisión impopular y se sostiene criterio bajo presión."),
    ("Liderazgo de equipos y ejecución", 4, 7, "#1f6feb", "🔵",
     "Líder → Jefe / Team Lead",
     "El salto de responder por uno mismo a responder por otros: equipo, talento, "
     "entrega y una operación que no dependa de heroísmos."),
    ("Gestión de negocio", 8, 11, "#8957e5", "🟣",
     "Manager → Gerente",
     "La unidad de negocio por dentro. Objetivos y métricas, economía real, "
     "sistema comercial y crecimiento con clientes rentables."),
    ("Dirección, estrategia y organización", 12, 15, "#e67e22", "🟠",
     "Gerente → Director / Head",
     "La vista del comité de dirección: qué construir, dónde competir, cómo "
     "organizarse y qué riesgos supervisar sin delegar la responsabilidad."),
    ("Alta dirección y gobierno", 16, 19, "#d1242f", "🔴",
     "Ejecutivo → CEO",
     "La empresa completa: oficina del CEO, directorio, capital y tecnología "
     "dirigida por valor y riesgo, no por moda."),
    ("Fundador, propietario e independencia", 20, 23, "#6e7781", "⚫",
     "Founder → Business Owner",
     "Crear en vez de administrar lo creado: validación, formalización en Chile, "
     "escalamiento y una estrategia de independencia ejecutable."),
)

# Formato fijo del encabezado de cada parte, comprobado por el validador.
CABECERA_ETAPA = re.compile(r"^\*\*Etapa:\*\*\s*(\d+)\s*[—-]\s*(.+?)\s*$", re.M)
CABECERA_SALIDA = re.compile(r"^\*\*Resultado de salida:\*\*\s*(.+?)\s*$", re.M)
CABECERA_DURACION = re.compile(r"^\*\*Duración:\*\*\s*(\d+)\s*clases\s*·\s*(\d+)\s*horas", re.M)


@dataclass
class Clase:
    numero: int
    titulo: str
    nivel: str
    minutos: int
    conceptos: list[str]
    referencias: list[str]
    ruta: Path

    @property
    def ruta_md(self) -> str:
        return self.ruta.relative_to(ROOT).as_posix()

    @property
    def horas(self) -> float:
        return self.minutos / 60


@dataclass
class Parte:
    numero: int
    slug: str
    titulo: str
    etapa: int
    etapa_nombre: str
    salida: str
    horas: int
    clases: list[Clase] = field(default_factory=list)
    labs: list[Path] = field(default_factory=list)
    directorio: Path = ROOT

    @property
    def ruta_md(self) -> str:
        return (self.directorio / "README.md").relative_to(ROOT).as_posix()


def _yaml_plano(ruta: Path) -> dict[str, object]:
    """Subconjunto de YAML suficiente para los `lesson.yaml` del programa.

    Se resuelve con la biblioteca estándar para que validar el material no
    exija instalar nada: el formato es `clave: valor` y listas de guiones.
    """
    datos: dict[str, object] = {}
    clave_lista: str | None = None
    for linea in ruta.read_text(encoding="utf-8").splitlines():
        if not linea.strip() or linea.lstrip().startswith("#"):
            continue
        if linea.startswith("  - ") and clave_lista:
            lista = datos.setdefault(clave_lista, [])
            assert isinstance(lista, list)
            lista.append(linea[4:].strip().strip('"'))
            continue
        if re.match(r"^[A-Za-z_][\w-]*:", linea):
            clave, _, valor = linea.partition(":")
            clave, valor = clave.strip(), valor.strip().strip('"')
            if valor:
                datos[clave] = valor
                clave_lista = None
            else:
                datos[clave] = []
                clave_lista = clave
    return datos


# Tabla de «Conceptos centrales»: el término va en la primera columna, en negrita.
FILA_CONCEPTO = re.compile(r"^\|\s*\*\*(.+?)\*\*\s*\|", re.M)


def _conceptos(texto: str) -> list[str]:
    """Términos de la tabla de conceptos de una clase.

    El buscador del portal los indexa junto al título. Sin ellos solo se puede
    buscar por el nombre de la clase, y conceptos como «EBITDA», «OKR» o
    «Ley Karin» no devolverían nada aunque el programa les dedique secciones.
    """
    bloque = texto.split("## 🧩 Conceptos centrales", 1)
    if len(bloque) < 2:
        return []
    cuerpo = re.split(r"^## ", bloque[1], maxsplit=1, flags=re.M)[0]
    return [c.strip() for c in FILA_CONCEPTO.findall(cuerpo)]


def _referencias(texto: str) -> list[str]:
    bloque = texto.split("## 📗 Fuentes y verificación", 1)
    if len(bloque) < 2:
        return []
    cuerpo = re.split(r"^## ", bloque[1], maxsplit=1, flags=re.M)[0]
    return [l.strip()[2:].strip() for l in cuerpo.splitlines() if l.strip().startswith("- ")]


def partes() -> list[Parte]:
    """Las 24 partes con sus clases, leídas del árbol de archivos."""
    resultado: list[Parte] = []

    for directorio in sorted(p for p in MODULES.glob("[0-9][0-9]-*") if p.is_dir()):
        numero = int(directorio.name.split("-", 1)[0])
        slug = directorio.name.split("-", 1)[1]
        readme = (directorio / "README.md").read_text(encoding="utf-8")

        titulo = readme.splitlines()[0].lstrip("# ").strip()
        titulo = re.sub(r"^Parte\s+\d+\s*[—-]\s*", "", titulo)

        etapa_encontrada = CABECERA_ETAPA.search(readme)
        salida_encontrada = CABECERA_SALIDA.search(readme)
        duracion_encontrada = CABECERA_DURACION.search(readme)

        clases: list[Clase] = []
        for carpeta in sorted(d for d in (directorio / "classes").glob("*") if d.is_dir()):
            leccion = _yaml_plano(carpeta / "lesson.yaml")
            texto = (carpeta / "README.md").read_text(encoding="utf-8")
            clases.append(Clase(
                numero=int(str(leccion.get("id", 0))),
                titulo=str(leccion.get("title", carpeta.name)),
                nivel=str(leccion.get("level", "")),
                minutos=int(str(leccion.get("duration_minutes", 150))),
                conceptos=_conceptos(texto),
                referencias=_referencias(texto),
                ruta=carpeta / "README.md",
            ))

        resultado.append(Parte(
            numero=numero,
            slug=slug,
            titulo=titulo,
            etapa=int(etapa_encontrada.group(1)) if etapa_encontrada else 0,
            etapa_nombre=etapa_encontrada.group(2) if etapa_encontrada else "",
            salida=salida_encontrada.group(1) if salida_encontrada else "",
            horas=int(duracion_encontrada.group(2)) if duracion_encontrada else 0,
            clases=sorted(clases, key=lambda c: c.numero),
            labs=sorted((directorio / "labs").glob("lab-*.md")),
            directorio=directorio,
        ))

    return resultado


def etapa_de(numero_de_parte: int) -> tuple[str, int, int, str, str, str, str]:
    for etapa in ETAPAS:
        if etapa[1] <= numero_de_parte <= etapa[2]:
            return etapa
    return ETAPAS[-1]


@dataclass
class Resumen:
    partes: int
    clases: int
    horas: int
    labs: int
    proyectos: int
    casos: int
    plantillas: int
    escenarios: int
    bibliografia: int
    referencias_en_clase: int
    documentos: int
    palabras: int


def _palabras(texto: str) -> int:
    return len(re.findall(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ0-9]+", texto))


def resumen(datos: list[Parte] | None = None) -> Resumen:
    datos = datos if datos is not None else partes()
    todas = [c for p in datos for c in p.clases]

    escenarios = json.loads((ROOT / "data" / "scenarios.json").read_text(encoding="utf-8"))
    with (ROOT / "data" / "books.csv").open(encoding="utf-8", newline="") as archivo:
        bibliografia = sum(1 for _ in csv.DictReader(archivo))

    return Resumen(
        partes=len(datos),
        clases=len(todas),
        horas=sum(p.horas for p in datos),
        labs=sum(len(p.labs) for p in datos),
        proyectos=len(list(MODULES.glob("*/project.md"))),
        casos=len(list((ROOT / "cases").glob("*.md"))),
        plantillas=len(list((ROOT / "templates").glob("*.md"))),
        escenarios=len(escenarios),
        bibliografia=bibliografia,
        referencias_en_clase=sum(len(c.referencias) for c in todas),
        documentos=len([p for p in ROOT.rglob("*.md")
                        if not any(x in p.parts for x in (".git", "site", "node_modules"))]),
        palabras=sum(_palabras(c.ruta.read_text(encoding="utf-8")) for c in todas),
    )


def version() -> str:
    return (ROOT / "VERSION").read_text(encoding="utf-8").strip()
