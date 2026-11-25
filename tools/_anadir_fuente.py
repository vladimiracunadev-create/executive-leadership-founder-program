"""Ayuda de trabajo: añade una fila de lectura comparada y una fuente (@@) a una clase escrita a mano."""
import pathlib, re, sys

RAIZ = pathlib.Path(__file__).resolve().parents[1]


def anadir(clase: int, fila: str, prefijo: str, uso: str) -> None:
    p = next(RAIZ.glob(f"modules/*/classes/{clase:03d}-*")) / "README.md"
    t = p.read_text(encoding="utf-8")
    m = re.search(r"(## 📚 Lectura comparada\n\n\|.*?\n\|---.*?\n(?:\|.*\n)+)", t)
    t = t.replace(m.group(1), m.group(1) + fila + "\n", 1)
    k = t.index("\n> **Regla de fuentes")
    t = t[:k].rstrip("\n") + f"\n- @@{prefijo}:: {uso}\n" + t[k:]
    p.write_text(t, encoding="utf-8", newline="\n")
