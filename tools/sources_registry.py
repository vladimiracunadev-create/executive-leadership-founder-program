"""Modelo compartido del registro de fuentes.

El registro (`sources/bibliography.json`) es la única lista de obras, normas y
portales oficiales en los que se apoya el programa. Este módulo sabe dos cosas:

1. leer el registro y comprobar su forma sin tocar la red;
2. leer las citas reales de las 288 clases.

`scripts/verify-sources` (offline, bloquea en CI) y `scripts/refresh-sources`
(en red, no bloquea) construyen sobre esto. La separación es deliberada: si la
red entra en el CI, el CI se vuelve inestable y se acaba ignorando.
"""

from __future__ import annotations

import json
import re
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
REGISTRO = RAIZ / "sources" / "bibliography.json"

CABECERA_FUENTES = "## 📗 Fuentes y verificación"

#: Forma canónica de una cita dentro de una clase.
#: `- <emisor> — *<obra>*. **Uso en esta clase:** <uso>.` y, opcionalmente, cola.
LINEA = re.compile(
    r"^- (?P<emisor>[^—*]+?) — \*(?P<obra>.+?)\*\. "
    r"\*\*Uso en esta clase:\*\* (?P<uso>.+?)\.(?P<cola>\s.*)?$"
)

TIPOS = ("book", "paper", "standard", "reference", "dataset")
ESTADOS = ("verificada", "pendiente")

#: Cada tipo admite un solo localizador, y el localizador tiene una sola forma.
LOCALIZADOR = {
    "book": "https://openlibrary.org/isbn/{isbn13}",
    "paper": "https://doi.org/{doi}",
}

FECHA = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ID = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
DOI = re.compile(r"^10\.\d{4,9}/\S+$")


# --------------------------------------------------------------------------- #
# Utilidades                                                                   #
# --------------------------------------------------------------------------- #
def isbn13_valido(valor: str) -> bool:
    """ISBN-13 con dígito de control correcto. No basta con que tenga 13 cifras."""
    if not isinstance(valor, str) or not re.fullmatch(r"\d{13}", valor):
        return False
    suma = sum(int(d) * (1 if i % 2 == 0 else 3) for i, d in enumerate(valor[:12]))
    return (10 - suma % 10) % 10 == int(valor[12])


def doi_valido(valor: str) -> bool:
    return isinstance(valor, str) and bool(DOI.match(valor))


def identificador(emisor: str, obra: str) -> str:
    """Id estable en kebab-case a partir de cómo se cita la obra."""
    crudo = f"{emisor} {obra}"
    plano = unicodedata.normalize("NFKD", crudo).encode("ascii", "ignore").decode()
    palabras = [p for p in re.split(r"[^A-Za-z0-9]+", plano.lower()) if p]
    return "-".join(palabras)[:80].strip("-")


def cita(emisor: str, obra: str) -> str:
    return f"{emisor} — {obra}"


# --------------------------------------------------------------------------- #
# Citas reales de las clases                                                   #
# --------------------------------------------------------------------------- #
@dataclass
class Clase:
    ruta: Path
    bloque: str
    lineas: list[str] = field(default_factory=list)

    @property
    def relativa(self) -> str:
        return self.ruta.parent.relative_to(RAIZ).as_posix()


def clases(raiz: Path = RAIZ) -> list[Clase]:
    salida = []
    for ruta in sorted(raiz.glob("modules/[0-9][0-9]-*/classes/*/README.md")):
        texto = ruta.read_text(encoding="utf-8")
        if CABECERA_FUENTES not in texto:
            salida.append(Clase(ruta=ruta, bloque="", lineas=[]))
            continue
        bloque = texto.split(CABECERA_FUENTES, 1)[1]
        lineas = [x.strip() for x in bloque.splitlines() if x.strip().startswith("- ")]
        salida.append(Clase(ruta=ruta, bloque="\n".join(lineas), lineas=lineas))
    return salida


def citas(lista: list[Clase] | None = None) -> dict[str, list[str]]:
    """`"emisor — obra"` -> rutas de las clases que la citan, sin repetir."""
    lista = clases() if lista is None else lista
    salida: dict[str, list[str]] = {}
    for clase in lista:
        for linea in clase.lineas:
            m = LINEA.match(linea)
            if not m:
                continue
            clave = cita(m.group("emisor").strip(), m.group("obra").strip())
            rutas = salida.setdefault(clave, [])
            if clase.relativa not in rutas:
                rutas.append(clase.relativa)
    return {k: sorted(v) for k, v in sorted(salida.items())}


def lineas_invalidas(lista: list[Clase] | None = None) -> list[str]:
    lista = clases() if lista is None else lista
    malas = []
    for clase in lista:
        for linea in clase.lineas:
            if not LINEA.match(linea):
                malas.append(f"{clase.relativa}: {linea}")
    return malas


# --------------------------------------------------------------------------- #
# Registro                                                                     #
# --------------------------------------------------------------------------- #
def cargar(ruta: Path = REGISTRO) -> dict:
    return json.loads(ruta.read_text(encoding="utf-8"))


def guardar(registro: dict, ruta: Path = REGISTRO) -> None:
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(
        json.dumps(registro, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def localizador_esperado(entrada: dict) -> str | None:
    tipo = entrada.get("type")
    if tipo == "book" and entrada.get("isbn13"):
        return LOCALIZADOR["book"].format(isbn13=entrada["isbn13"])
    if tipo == "paper" and entrada.get("doi"):
        return LOCALIZADOR["paper"].format(doi=entrada["doi"])
    if tipo in ("standard", "reference", "dataset"):
        return entrada.get("url")
    return None


def resumen(registro: dict, usos: dict[str, list[str]]) -> dict:
    entradas = registro.get("entries", [])
    por_tipo: dict[str, int] = {}
    for e in entradas:
        por_tipo[e.get("type", "?")] = por_tipo.get(e.get("type", "?"), 0) + 1
    verificadas = [e for e in entradas if e.get("status") == "verificada"]
    pendientes = [e for e in entradas if e.get("status") == "pendiente"]
    declaradas = {e.get("cited_as") for e in entradas}
    sin_declarar = [c for c in usos if c not in declaradas]
    return {
        "clases": len(clases()),
        "citas_distintas": len(usos),
        "citas_totales": sum(len(v) for v in usos.values()),
        "entradas": len(entradas),
        "verificadas": len(verificadas),
        "pendientes": len(pendientes),
        "por_tipo": dict(sorted(por_tipo.items())),
        "sin_declarar": sorted(sin_declarar),
        "cobertura": 0.0 if not usos else round(100 * (len(usos) - len(sin_declarar)) / len(usos), 1),
        "verified_on": registro.get("verified_on", ""),
    }
