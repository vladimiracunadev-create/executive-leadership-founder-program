"""Cada clase cumple el contrato `deep-class-v2`.

El validador de estructura ya recorre esto en CI; aquí se comprueba desde las
pruebas para que quien trabaje en local vea el fallo sin recordar qué script
ejecutar, y para que el fallo señale la clase concreta.
"""

from __future__ import annotations

import re

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

MINIMO_PALABRAS = 1150
MINIMO_REFERENCIAS = 5
MINIMO_CONCEPTOS = 5


def test_todas_las_clases_traen_las_dieciseis_secciones(clases):
    incompletas = []
    for clase in clases:
        texto = clase.ruta.read_text(encoding="utf-8")
        faltan = [s for s in SECCIONES if s not in texto]
        if faltan:
            incompletas.append(f"{clase.numero:03d}: faltan {len(faltan)}")
    assert not incompletas, f"clases incompletas: {incompletas[:10]}"


def test_todas_las_clases_superan_la_densidad_minima(clases):
    flojas = []
    for clase in clases:
        palabras = len(re.findall(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ0-9]+",
                                  clase.ruta.read_text(encoding="utf-8")))
        if palabras < MINIMO_PALABRAS:
            flojas.append((clase.numero, palabras))
    assert not flojas, f"clases por debajo de {MINIMO_PALABRAS} palabras: {flojas[:10]}"


def test_todas_las_clases_citan_al_menos_cinco_fuentes(clases):
    escasas = [(c.numero, len(c.referencias)) for c in clases
               if len(c.referencias) < MINIMO_REFERENCIAS]
    assert not escasas, f"clases con menos de {MINIMO_REFERENCIAS} referencias: {escasas[:10]}"


def test_todas_las_clases_definen_al_menos_cinco_conceptos(clases):
    escasas = [(c.numero, len(c.conceptos)) for c in clases
               if len(c.conceptos) < MINIMO_CONCEPTOS]
    assert not escasas, f"clases con menos de {MINIMO_CONCEPTOS} conceptos: {escasas[:10]}"


def test_el_titulo_es_el_mismo_en_los_tres_archivos(clases):
    """Si divergen, el temario enlaza un nombre y el documento muestra otro."""
    incoherentes = []
    for clase in clases:
        carpeta = clase.ruta.parent
        numero = carpeta.name.split("-", 1)[0]
        readme = clase.ruta.read_text(encoding="utf-8").splitlines()[0].strip()
        evaluacion = (carpeta / "assessment.md").read_text(
            encoding="utf-8").splitlines()[0].strip()
        if readme != f"# Clase {numero} — {clase.titulo}":
            incoherentes.append(f"{numero}: README")
        if evaluacion != f"# Evaluación — Clase {numero}: {clase.titulo}":
            incoherentes.append(f"{numero}: assessment")
    assert not incoherentes, f"títulos incoherentes: {incoherentes[:10]}"


def test_la_cabecera_declara_la_parte_correcta(partes):
    erroneas = []
    for parte in partes:
        esperado = f"**Parte:** {parte.numero:02d} — {parte.titulo}"
        for clase in parte.clases:
            if esperado not in clase.ruta.read_text(encoding="utf-8"):
                erroneas.append(clase.numero)
    assert not erroneas, f"clases con cabecera de parte incorrecta: {erroneas[:10]}"


def test_las_clases_de_chile_citan_una_fuente_oficial(partes):
    """La parte 21 trata trámites reales: sin fuente oficial no sirve."""
    oficiales = ("sii.cl", "dt.gob.cl", "bcn.cl", "registrodeempresasysociedades.cl",
                 "inapi.cl", "chilecompra.cl", "sercotec.cl", "corfo.cl")
    parte = next(p for p in partes if p.numero == 21)
    sin_fuente = [c.numero for c in parte.clases
                  if not any(d in c.ruta.read_text(encoding="utf-8").lower() for d in oficiales)]
    assert not sin_fuente, f"clases chilenas sin fuente oficial: {sin_fuente}"
