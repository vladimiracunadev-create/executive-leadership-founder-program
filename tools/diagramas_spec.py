"""Renderizador de diagramas a medida dirigido por datos.

Cada clase escrita a mano declara un diagrama como una especificación (un dict) que
describe SU marco: qué cajas, qué relaciones, qué colores. Este módulo solo sabe
dibujarlas. Los tipos disponibles son formas de explicar, no plantillas de relleno:

* ``cuadrante``   dos ejes con cuatro zonas;
* ``columnas``    de dos a cuatro grupos comparados, con viñetas;
* ``cadena``      pasos en orden, con retorno opcional;
* ``escalera``    niveles que ascienden;
* ``tabla``       filas y columnas con encabezados;
* ``paneles``     dos listas de tarjetas enfrentadas.

Todos admiten una ``nota`` destacada y un ``pie`` con el límite del marco.
Solo biblioteca estándar.
"""

from __future__ import annotations

import textwrap

from diagramas_clase import (ANCHO, AZUL, BORDE, GRIS, NARANJA, PAPEL, ROJO, SUAVE, TINTA, VERDE, VIOLETA, Lienzo)

PALETA = [AZUL, VERDE, NARANJA, VIOLETA, ROJO, GRIS]
COLORES = {"azul": AZUL, "verde": VERDE, "naranja": NARANJA, "violeta": VIOLETA, "rojo": ROJO, "gris": GRIS}


def _c(valor, i=0):
    if valor is None:
        return PALETA[i % len(PALETA)]
    return COLORES.get(valor, valor)


def _lineas(texto, ancho, tam):
    n = max(8, int(ancho / (tam * 0.56)))
    return len(textwrap.wrap(texto, n, break_long_words=False) or [texto])


def _alto_texto(texto, ancho, tam, interlinea=1.38):
    return _lineas(texto, ancho, tam) * tam * interlinea


def _cabecera(L, s):
    L.cabecera("MARCO", s["titulo"], _c(s.get("color"), 1), s.get("autores", ""))


def _nota(L, s, y):
    if not s.get("nota"):
        return y
    h = _alto_texto(s["nota"], ANCHO - 90, 12.5) + 26
    L.caja(28, y, ANCHO - 56, h, PAPEL, BORDE, 10, 1)
    L.parrafo(44, y + 22, s["nota"], ANCHO - 90, 12.5, TINTA, "600")
    return y + h + 14


def _pie(L, s, y):
    if s.get("pie"):
        L.pie(y + 12, s["pie"])
        y += 12 + _alto_texto(s["pie"], ANCHO - 56, 12) + 6
    return y + 18


def _cierre(L, s, y):
    y = _nota(L, s, y)
    y = _pie(L, s, y)
    L.alto = y


# --------------------------------------------------------------------------- cuadrante
def _cuadrante(L, s):
    ex, ey = s["ejes"]
    x0, y0 = 150, 112
    cw = (ANCHO - 56 - 122 - 12) / 2
    celdas = s["celdas"]
    ch = max(_alto_texto(c[1], cw - 32, 12.5) for c in celdas) + 62
    L.texto(x0 + cw / 2, 100, ex[0], 11.5, SUAVE, "700", "middle")
    L.texto(x0 + cw + 12 + cw / 2, 100, ex[1], 11.5, SUAVE, "700", "middle")
    L.partes.append(f'<text transform="translate(120,{y0 + ch / 2}) rotate(-90)" font-size="11.5" font-weight="700" fill="{SUAVE}" text-anchor="middle">{ey[1]}</text>')
    L.partes.append(f'<text transform="translate(120,{y0 + ch + 12 + ch / 2}) rotate(-90)" font-size="11.5" font-weight="700" fill="{SUAVE}" text-anchor="middle">{ey[0]}</text>')
    for i, (t, d, col) in enumerate(celdas):
        x = x0 + (i % 2) * (cw + 12)
        y = y0 + (i // 2) * (ch + 12)
        c = _c(col, i)
        L.caja(x, y, cw, ch, "#ffffff", c, 12, 1.8)
        L.partes.append(f'<rect x="{x}" y="{y}" width="{cw}" height="34" rx="12" fill="{c}"/>')
        L.texto(x + 16, y + 23, t, 14, "#ffffff", "700")
        L.parrafo(x + 16, y + 58, d, cw - 32, 12.5, TINTA)
    return y0 + 2 * ch + 24


# --------------------------------------------------------------------------- columnas
def _columnas(L, s):
    cols = s["columnas"]
    n = len(cols)
    gap = 20
    w = (ANCHO - 56 - (n - 1) * gap) / n
    tam = 12.5
    altos = []
    for t, col, items in cols:
        h = 52
        for it in items:
            h += _alto_texto(it, w - 50, tam) + 10
        altos.append(h + 12)
    h = max(altos)
    y0 = 96
    for i, (t, col, items) in enumerate(cols):
        x = 28 + i * (w + gap)
        c = _c(col, i)
        L.caja(x, y0, w, h, "#ffffff", c, 12, 1.8)
        L.partes.append(f'<path d="M{x},{y0 + 40} V{y0 + 12} a12,12 0 0 1 12,-12 H{x + w - 12} a12,12 0 0 1 12,12 V{y0 + 40} Z" fill="{c}"/>')
        L.texto(x + 16, y0 + 26, t, 13.5, "#ffffff", "800")
        y = y0 + 62
        for it in items:
            L.partes.append(f'<circle cx="{x + 22}" cy="{y - 4}" r="4" fill="{c}"/>')
            y = L.parrafo(x + 36, y, it, w - 50, tam, TINTA) + 10
    return y0 + h + 16


# --------------------------------------------------------------------------- cadena
def _cadena(L, s):
    pasos = s["pasos"]
    n = len(pasos)
    por_fila = 4 if n > 4 else n
    gap = 22
    w = (ANCHO - 56 - (por_fila - 1) * gap) / por_fila
    tam = 12.5
    filas = (n + por_fila - 1) // por_fila
    h = max(_alto_texto(p[1], w - 32, tam) for p in pasos) + 62
    y = 96
    centros = []
    for i, (t, d, *resto) in enumerate(pasos):
        col = resto[0] if resto else None
        c = _c(col, i)
        f, k = divmod(i, por_fila)
        x = 28 + k * (w + gap)
        yy = y + f * (h + 34)
        L.caja(x, yy, w, h, "#ffffff", c, 12, 1.8)
        L.partes.append(f'<circle cx="{x + 24}" cy="{yy + 26}" r="13" fill="{c}"/>')
        L.texto(x + 24, yy + 31, str(i + 1), 13, "#ffffff", "700", "middle")
        yt = L.parrafo(x + 44, yy + 24, t, w - 56, 13.5, TINTA, "700")
        L.parrafo(x + 16, max(yt, yy + 54) + 2, d, w - 32, tam, SUAVE)
        centros.append((x, yy))
        if k < por_fila - 1 and i < n - 1:
            L.flecha(x + w + 3, yy + h / 2, x + w + gap - 3, yy + h / 2, GRIS, 2)
        elif k == por_fila - 1 and i < n - 1:
            L.trazo(f"M{x + w / 2},{yy + h + 2} V{yy + h + 14} H{28 + w / 2} V{yy + h + 32}", GRIS, 2,
                    extra=f'marker-end="url(#p-{L.ident})"')
    fin = y + filas * (h + 34) - 20
    if s.get("retorno"):
        x_f, y_f = centros[-1]
        x_i, y_i = centros[0]
        yl = fin + 8
        L.trazo(f"M{x_f + w / 2},{y_f + h + 2} V{yl} H{x_i + w / 2} V{y_i + h + 4}", GRIS, 2,
                extra=f'stroke-dasharray="7 6" marker-end="url(#p-{L.ident})"')
        L.texto((x_f + x_i) / 2 + w / 2, yl - 6, s["retorno"], 11.5, SUAVE, "600", "middle")
        fin = yl + 16
    return fin


# --------------------------------------------------------------------------- escalera
def _escalera(L, s):
    niv = s["niveles"]
    n = len(niv)
    paso = 34
    w = ANCHO - 56 - (n - 1) * paso
    tam = 12.5
    y = 96
    # de arriba abajo: el último nivel (más alto) arriba
    hs = [max(60, _alto_texto(d, w - 80, tam) + 46) for t, d, *_ in niv]
    ytot = y
    for i in range(n - 1, -1, -1):
        t, d, *resto = niv[i]
        c = _c(resto[0] if resto else None, i)
        x = 28 + i * paso
        L.caja(x, ytot, w, hs[i], "#ffffff", c, 10, 1.8)
        L.partes.append(f'<rect x="{x}" y="{ytot}" width="6" height="{hs[i]}" rx="3" fill="{c}"/>')
        L.partes.append(f'<circle cx="{x + 32}" cy="{ytot + hs[i] / 2}" r="15" fill="{c}"/>')
        L.texto(x + 32, ytot + hs[i] / 2 + 5, str(i + 1), 14, "#ffffff", "700", "middle")
        L.texto(x + 60, ytot + 24, t, 14, TINTA, "700")
        L.parrafo(x + 60, ytot + 42, d, w - 80, tam, SUAVE)
        ytot += hs[i] + 10
    return ytot + 6


# --------------------------------------------------------------------------- tabla
def _tabla(L, s):
    enc = s["encabezados"]
    filas = s["filas"]
    n = len(enc)
    anchos = s.get("anchos") or [1] * n
    tot = sum(anchos)
    W = ANCHO - 56
    xs = [28]
    for a in anchos:
        xs.append(xs[-1] + W * a / tot)
    tam = 12
    y = 96
    c = _c(s.get("color"), 1)
    L.partes.append(f'<rect x="28" y="{y}" width="{W}" height="34" rx="10" fill="{c}"/>')
    for j, h in enumerate(enc):
        L.texto(xs[j] + 12, y + 22, h, 12.5, "#ffffff", "700")
    y += 40
    for r, fila in enumerate(filas):
        h = max(_alto_texto(str(cel), xs[j + 1] - xs[j] - 20, tam) for j, cel in enumerate(fila)) + 20
        L.caja(28, y, W, h, "#ffffff" if r % 2 == 0 else PAPEL, BORDE, 0, 1)
        for j, cel in enumerate(fila):
            L.parrafo(xs[j] + 12, y + 20, str(cel), xs[j + 1] - xs[j] - 20, tam, TINTA, "700" if j == 0 else "400")
        y += h
    return y + 16


# --------------------------------------------------------------------------- paneles
def _paneles(L, s):
    izq, der = s["izquierda"], s["derecha"]
    mitad = (ANCHO - 56 - 24) / 2
    tam = 12.5
    ys = []
    for lado, (tit, tarjetas) in enumerate((izq, der)):
        x = 28 + lado * (mitad + 24)
        L.texto(x, 90, tit.upper(), 11.5, SUAVE, "700", "start", 'letter-spacing="1.4"')
        y = 104
        for i, (t, d, *resto) in enumerate(tarjetas):
            c = _c(resto[0] if resto else None, i + lado * 2)
            h = _alto_texto(d, mitad - 32, tam) + 46
            L.caja(x, y, mitad, h, "#ffffff", c, 10, 1.7)
            L.partes.append(f'<rect x="{x}" y="{y}" width="6" height="{h}" rx="3" fill="{c}"/>')
            L.texto(x + 18, y + 22, t, 14, TINTA, "700")
            L.parrafo(x + 18, y + 40, d, mitad - 32, tam, SUAVE)
            y += h + 10
        ys.append(y)
    return max(ys) + 6


_TIPOS = {"cuadrante": _cuadrante, "columnas": _columnas, "cadena": _cadena, "escalera": _escalera,
          "tabla": _tabla, "paneles": _paneles}


def renderizar(spec: dict, ident: str, descripcion: str) -> str:
    L = Lienzo(spec["titulo"], descripcion, 600, ident)
    _cabecera(L, spec)
    y = _TIPOS[spec["tipo"]](L, spec)
    _cierre(L, spec, y)
    return L.svg()


def fabricar(specs: dict[int, dict]):
    """Convierte {n_clase: spec} en {n_clase: función sin argumentos}."""
    def hacer(n, spec):
        def f():
            desc = spec.get("descripcion") or spec["titulo"]
            return renderizar(spec, f"s{n}", desc)
        return f
    return {n: hacer(n, spec) for n, spec in specs.items()}
