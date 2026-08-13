"""Genera SYLLABUS.md desde las 288 clases reales del repositorio.

El temario estaba escrito a mano, y por eso conservaba los títulos correctos
mientras los `lesson.yaml` los perdían: dos fuentes de verdad para el mismo
dato acaban siempre así. Ahora hay una sola, y este generador la publica.

Uso:
    python tools/build_syllabus.py           # regenera SYLLABUS.md
    python tools/build_syllabus.py --check   # falla si está desactualizado
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import inventario  # noqa: E402

ROOT = inventario.ROOT
SALIDA = ROOT / "SYLLABUS.md"

PORTADA = """<!-- portada:inicio -->
<div align="center">

# 📚 Temario maestro

**Las {clases} clases del programa, en el orden en que se estudian.**

[![Clases](https://img.shields.io/badge/clases-{clases}%20·%20{partes}%20partes-7c5cff?style=flat-square)](SYLLABUS.md)
[![Horas](https://img.shields.io/badge/horas-{horas}-2e8b57?style=flat-square)](STATUS.md)
[![Generado por](https://img.shields.io/badge/generado%20por-build__syllabus.py-007c83?style=flat-square)](tools/build_syllabus.py)

[🏠 Inicio](README.md) ·
[📊 Estado](STATUS.md) ·
[🧾 Ficha técnica](MANIFEST.md) ·
[🗂️ Índice de archivos](FILE_INDEX.md) ·
[🌐 Portal](https://vladimiracunadev-create.github.io/executive-leadership-founder-program/)

</div>
<!-- portada:fin -->

---

> Este documento **se genera**. Para cambiar un título o una duración se edita
> el `lesson.yaml` de la clase y se vuelve a ejecutar `tools/build_syllabus.py`.

## 🧭 Las {etapas} etapas

| Etapa | Nombre | Partes | Clases | Horas | Nivel de salida |
|---:|---|---:|---:|---:|---|
{tabla_etapas}
"""

PIE = """
---

<div align="center">

[🏠 Inicio](README.md) · [📊 Estado](STATUS.md) · [🧾 Ficha técnica](MANIFEST.md) · [🗂️ Índice de archivos](FILE_INDEX.md)

</div>
"""


def horas_legibles(minutos: int) -> str:
    horas = minutos / 60
    return f"{horas:.1f}".replace(".0", "").replace(".", ",") + " h"


def render() -> str:
    partes = inventario.partes()
    resumen = inventario.resumen(partes)

    filas_etapa = []
    for indice, etapa in enumerate(inventario.ETAPAS, start=1):
        nombre, desde, hasta, _, emoji, salida, _ = etapa
        propias = [p for p in partes if desde <= p.numero <= hasta]
        clases = sum(len(p.clases) for p in propias)
        horas = sum(p.horas for p in propias)
        filas_etapa.append(
            f"| {indice} | {emoji} {nombre} | {desde:02d}–{hasta:02d} | "
            f"{clases} | {horas} | {salida} |"
        )

    lineas = [
        PORTADA.format(
            clases=resumen.clases, partes=resumen.partes, horas=resumen.horas,
            etapas=len(inventario.ETAPAS), tabla_etapas="\n".join(filas_etapa),
        ).rstrip(),
        "",
    ]

    etapa_actual = None
    for parte in partes:
        etapa = inventario.etapa_de(parte.numero)
        nombre, _, _, _, emoji, salida, idea = etapa
        if nombre != etapa_actual:
            etapa_actual = nombre
            lineas += [
                f"## {emoji} Etapa {inventario.ETAPAS.index(etapa) + 1} — {nombre}",
                "",
                idea,
                "",
                f"**Nivel de salida:** {salida}",
                "",
            ]

        lineas += [
            f"### Parte {parte.numero:02d} — [{parte.titulo}]({parte.ruta_md})",
            "",
            f"**Salida:** {parte.salida}",
            "",
            f"**{len(parte.clases)} clases · {parte.horas} horas · "
            f"{len(parte.labs)} laboratorios · 1 proyecto integrador**",
            "",
        ]
        for clase in parte.clases:
            lineas.append(
                f"- **{clase.numero:03d}.** [{clase.titulo}]({clase.ruta_md}) — "
                f"{horas_legibles(clase.minutos)}"
            )
        lineas += [
            "",
            f"📁 [Laboratorios]({(parte.directorio / 'labs').relative_to(ROOT).as_posix()}/lab-01.md) ·"
            f" 🎓 [Proyecto de parte]({(parte.directorio / 'project.md').relative_to(ROOT).as_posix()})",
            "",
        ]

    lineas += PIE.strip().splitlines() + [""]
    return "\n".join(lineas)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    contenido = render()
    actual = SALIDA.read_text(encoding="utf-8") if SALIDA.exists() else ""

    if args.check:
        if actual != contenido:
            print("SYLLABUS.md está desactualizado. Ejecuta: python tools/build_syllabus.py")
            return 1
        print("SYLLABUS.md refleja las clases reales")
        return 0

    SALIDA.write_text(contenido, encoding="utf-8", newline="\n")
    resumen = inventario.resumen()
    print(f"SYLLABUS.md generado: {resumen.clases} clases en {resumen.partes} partes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
