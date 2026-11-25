"""Diagramas a medida de las clases que se escriben a mano.

Cada diagrama dibuja **el marco que enseña su clase**, no una plantilla común:
la prominencia de un interesado es un diagrama de Venn de tres atributos, el
escalamiento de un incidente es una escalera con roles, la confianza es un
modelo causal y la respuesta a una crisis es una matriz de atribución. Si una
clase no tiene un esquema que ayude a entenderla mejor que su texto, no lleva
ninguno: es preferible a un dibujo decorativo repetido en todas.

Cada función devuelve un documento SVG autónomo (con fondo propio, legible en
tema claro y oscuro). Solo biblioteca estándar.
"""

from __future__ import annotations

import textwrap
from xml.sax.saxutils import escape

FUENTE = "'Segoe UI', 'Helvetica Neue', Helvetica, Arial, sans-serif"
TINTA, SUAVE, PAPEL, BORDE = "#1f2328", "#59636e", "#f6f8fa", "#d0d7de"
AZUL, VERDE, NARANJA, ROJO, VIOLETA, GRIS = "#0969da", "#1a7f37", "#bc4c00", "#cf222e", "#8250df", "#59636e"
ANCHO = 1040


class Lienzo:
    def __init__(self, titulo: str, descripcion: str, alto: float, ident: str):
        self.titulo, self.descripcion, self.alto, self.ident = titulo, descripcion, alto, ident
        self.partes: list[str] = []

    # -- primitivas ---------------------------------------------------------
    def texto(self, x, y, s, tam=14, color=TINTA, peso="400", ancla="start", extra=""):
        self.partes.append(
            f'<text x="{x:g}" y="{y:g}" font-size="{tam:g}" font-weight="{peso}" fill="{color}" '
            f'text-anchor="{ancla}" {extra}>{escape(s)}</text>')

    def parrafo(self, x, y, s, ancho_px, tam=14, color=TINTA, peso="400", ancla="start", interlinea=1.38):
        """Texto envuelto por ancho estimado; devuelve la y de la línea siguiente."""
        n = max(8, int(ancho_px / (tam * 0.56)))
        for linea in textwrap.wrap(s, n, break_long_words=False) or [s]:
            self.texto(x, y, linea, tam, color, peso, ancla)
            y += tam * interlinea
        return y

    def caja(self, x, y, w, h, relleno="#ffffff", borde=BORDE, r=10, grosor=1.2, extra=""):
        self.partes.append(f'<rect x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" rx="{r}" '
                           f'fill="{relleno}" stroke="{borde}" stroke-width="{grosor}" {extra}/>')

    def pildora(self, x, y, s, color, tam=11.5, ancho=None, texto_color="#ffffff"):
        w = ancho or (len(s) * tam * 0.66 + 22)
        self.partes.append(f'<rect x="{x:g}" y="{y:g}" width="{w:g}" height="24" rx="12" fill="{color}"/>')
        self.texto(x + w / 2, y + 16, s, tam, texto_color, "700", "middle", 'letter-spacing="1"')
        return w

    def flecha(self, x1, y1, x2, y2, color=GRIS, grosor=2.2, trazo=""):
        self.partes.append(
            f'<path d="M{x1:g},{y1:g} L{x2:g},{y2:g}" stroke="{color}" stroke-width="{grosor}" fill="none" '
            f'stroke-linecap="round" {trazo} marker-end="url(#p-{self.ident})"/>')

    def trazo(self, d, color=GRIS, grosor=2.2, relleno="none", extra=""):
        self.partes.append(f'<path d="{d}" stroke="{color}" stroke-width="{grosor}" fill="{relleno}" {extra}/>')

    def cabecera(self, etiqueta, titulo, color, derecha=""):
        w = self.pildora(28, 24, etiqueta, color)
        self.texto(28 + w + 16, 43, titulo, 19, TINTA, "700")
        if derecha:
            self.texto(ANCHO - 28, 43, derecha, 12.5, SUAVE, "400", "end")

    def pie(self, y, texto):
        self.parrafo(28, y, texto, ANCHO - 56, 12, SUAVE)

    def svg(self) -> str:
        i = self.ident
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {ANCHO} {self.alto:g}" width="{ANCHO}" '
            f'role="img" aria-labelledby="t-{i} d-{i}" font-family="{FUENTE}">\n'
            f'<title id="t-{i}">{escape(self.titulo)}</title>\n<desc id="d-{i}">{escape(self.descripcion)}</desc>\n'
            f'<defs><marker id="p-{i}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" '
            f'orient="auto"><path d="M1,1 L9,5 L1,9 Z" fill="{GRIS}"/></marker></defs>\n'
            f'<rect width="{ANCHO}" height="{self.alto:g}" rx="16" fill="{PAPEL}" stroke="{BORDE}"/>\n'
            + "\n".join(self.partes) + "\n</svg>\n")


# ------------------------------------------------------------------------------
# 034 · Prominencia de un interesado (Mitchell, Agle & Wood, 1997)
# ------------------------------------------------------------------------------
def prominencia_interesados() -> str:
    L = Lienzo("Prominencia de un interesado según poder, legitimidad y urgencia",
               "Tres círculos que se solapan, poder, legitimidad y urgencia, definen siete clases de interesado: "
               "latentes (durmiente, discrecional, demandante), expectantes (dominante, peligroso, dependiente) "
               "y definitivo cuando reúne los tres atributos.", 560, "034")
    L.cabecera("MARCO", "Clase 034 · Quién cuenta y por qué: los tres atributos", VERDE,
               "Mitchell, Agle & Wood (1997)")
    r = 112
    centros = {"poder": (190, 205), "legit": (330, 205), "urg": (260, 322)}
    colores = {"poder": ROJO, "legit": AZUL, "urg": NARANJA}
    for k, (cx, cy) in centros.items():
        L.partes.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{colores[k]}" fill-opacity="0.16" '
                        f'stroke="{colores[k]}" stroke-width="2"/>')
    L.texto(120, 98, "PODER", 13, ROJO, "700", "middle", 'letter-spacing="1.4"')
    L.texto(120, 114, "puede imponer su voluntad", 11, SUAVE, "400", "middle")
    L.texto(400, 98, "LEGITIMIDAD", 13, AZUL, "700", "middle", 'letter-spacing="1.4"')
    L.texto(400, 114, "su reclamo se reconoce como apropiado", 11, SUAVE, "400", "middle")
    L.texto(260, 478, "URGENCIA", 13, NARANJA, "700", "middle", 'letter-spacing="1.4"')
    L.texto(260, 494, "no admite espera y es crítico", 11, SUAVE, "400", "middle")
    # Regiones
    regiones = [
        (140, 190, "Durmiente", "solo poder"), (380, 190, "Discrecional", "solo legitimidad"),
        (260, 372, "Demandante", "solo urgencia"), (260, 168, "Dominante", "poder + legitimidad"),
        (186, 292, "Peligroso", "poder + urgencia"), (336, 292, "Dependiente", "legitimidad + urgencia"),
    ]
    for x, y, a, b in regiones:
        L.texto(x, y, a, 13.5, TINTA, "700", "middle")
        L.texto(x, y + 15, b, 10.5, SUAVE, "400", "middle")
    L.texto(260, 244, "DEFINITIVO", 13.5, TINTA, "800", "middle", 'letter-spacing="0.6"')
    L.texto(260, 259, "los tres", 10.5, SUAVE, "400", "middle")
    # Panel de lectura
    x0 = 560
    L.caja(x0, 76, ANCHO - x0 - 28, 436, "#ffffff")
    L.texto(x0 + 20, 106, "QUÉ HACER SEGÚN LA CLASE", 11.5, SUAVE, "700", "start", 'letter-spacing="1.4"')
    filas = [
        ("Definitivo", ROJO, "Prioridad máxima. Atender ya y dejar registro de lo acordado."),
        ("Dominante", ROJO, "Institucionalizar la relación: cauce regular, no atención ocasional."),
        ("Peligroso", ROJO, "Contener sin ignorar: dialogar antes de que el poder se use por la fuerza."),
        ("Dependiente", AZUL, "Depende de otro para ser oído: protege su acceso y su voz."),
        ("Discrecional", AZUL, "Sin poder ni urgencia: es decisión de la empresa cuánto atender."),
        ("Demandante", NARANJA, "Ruido urgente sin poder ni legitimidad: escuchar, no reaccionar."),
        ("Durmiente", GRIS, "Poder sin interés hoy: vigilar si adquiere legitimidad o urgencia."),
    ]
    y = 126
    for nombre, color, texto in filas:
        L.partes.append(f'<rect x="{x0 + 20}" y="{y}" width="6" height="42" rx="3" fill="{color}"/>')
        L.texto(x0 + 38, y + 16, nombre, 14, TINTA, "700")
        L.parrafo(x0 + 38, y + 33, texto, ANCHO - x0 - 90, 12.5, SUAVE)
        y += 54
    L.caja(28, 520, 504, 28, PAPEL, PAPEL, 0)
    L.texto(28, 538, "Los atributos son variables y construidos socialmente: un interesado puede ganar o perder uno.", 12, SUAVE)
    return L.svg()


# ------------------------------------------------------------------------------
# 190 · Declarar, escalar y mandar un incidente
# ------------------------------------------------------------------------------
def escalamiento_incidente() -> str:
    L = Lienzo("Escalamiento por niveles y roles de un incidente",
               "Una escalera de cuatro niveles (operación, gerencia, comité de crisis, directorio) con su criterio de "
               "paso, cuatro roles separados bajo un mando único y cuatro prioridades en orden.", 620, "190")
    L.cabecera("MARCO", "Clase 190 · Quién actúa, cuándo sube y en qué orden", AZUL,
               "Beyer et al. (2016) · Coombs (2007)")
    # Escalera
    niveles = [
        ("4", "Directorio", "La decisión excede al comité o compromete la continuidad o la licencia para operar.", ROJO),
        ("3", "Comité de crisis", "Afecta a clientes, datos personales, un regulador, a personas o es público.", NARANJA),
        ("2", "Gerencia", "Necesita un segundo equipo o no se resuelve tras una hora de análisis concentrado.", AZUL),
        ("1", "Operación", "Un equipo lo detecta, lo contiene y lo registra con su propia autoridad.", VERDE),
    ]
    x0, ancho_p, y = 28, 470, 82
    escal = [0, 28, 56, 84]
    for i, (n, nombre, criterio, color) in enumerate(niveles):
        dx = escal[3 - i]
        L.caja(x0 + dx, y, ancho_p - dx, 86, "#ffffff", color, 10, 1.8)
        L.partes.append(f'<circle cx="{x0 + dx + 28}" cy="{y + 43}" r="17" fill="{color}"/>')
        L.texto(x0 + dx + 28, y + 49, n, 17, "#ffffff", "700", "middle")
        L.texto(x0 + dx + 56, y + 28, nombre, 15, TINTA, "700")
        L.parrafo(x0 + dx + 56, y + 47, criterio, ancho_p - dx - 74, 12.5, SUAVE)
        if i < 3:
            L.flecha(x0 + 34 + escal[3 - i - 1] - 6, y + 94, x0 + 34 + escal[3 - i - 1] - 6, y + 100, GRIS, 1.6)
        y += 98
    L.texto(28, y + 8, "Declarar un incidente es una decisión barata; no declararlo, la cara.", 12.5, SUAVE, "600")
    # Roles
    xr = 540
    L.texto(xr, 80, "UN SOLO MANDO, ROLES SEPARADOS", 11.5, SUAVE, "700", "start", 'letter-spacing="1.4"')
    L.caja(xr + 130, 94, 230, 62, "#ffffff", ROJO, 12, 2)
    L.texto(xr + 245, 120, "Mando del incidente", 15, TINTA, "700", "middle")
    L.texto(xr + 245, 139, "decide y responde por la decisión", 12, SUAVE, "400", "middle")
    roles = [
        (xr, "Operaciones", "contiene y repara", AZUL), (xr + 250, "Comunicación", "un solo mensaje", VERDE),
    ]
    for x, n, d, c in roles:
        L.caja(x, 196, 230, 58, "#ffffff", c, 12, 1.8)
        L.texto(x + 115, 220, n, 14.5, TINTA, "700", "middle")
        L.texto(x + 115, 239, d, 12, SUAVE, "400", "middle")
        L.flecha(xr + 245, 156, x + 115, 194, c, 1.8)
    L.caja(xr + 130, 292, 230, 58, "#ffffff", VIOLETA, 12, 1.8)
    L.texto(xr + 245, 316, "Registro y planificación", 14.5, TINTA, "700", "middle")
    L.texto(xr + 245, 335, "hechos, decisiones y relevos", 12, SUAVE, "400", "middle")
    L.flecha(xr + 245, 156, xr + 245, 290, VIOLETA, 1.8, 'stroke-dasharray="6 5"')
    L.parrafo(xr, 386, "Quien opera no habla por la empresa, y quien habla no repara. "
              "Legal y personas asesoran al mando; no lo sustituyen.", 480, 12.5, SUAVE)
    # Prioridades
    L.texto(xr, 450, "PRIORIDADES, EN ESTE ORDEN", 11.5, SUAVE, "700", "start", 'letter-spacing="1.4"')
    prios = [("1", "Proteger a las personas"), ("2", "Detener el daño"), ("3", "Preservar la evidencia"), ("4", "Restablecer")]
    for i, (n, t) in enumerate(prios):
        x = xr + (i % 2) * 250
        y2 = 466 + (i // 2) * 44
        L.partes.append(f'<circle cx="{x + 14}" cy="{y2 + 14}" r="13" fill="{AZUL}"/>')
        L.texto(x + 14, y2 + 19, n, 13, "#ffffff", "700", "middle")
        L.texto(x + 36, y2 + 19, t, 13.5, TINTA, "600")
    L.pie(594, "Niveles y criterios: adaptación docente de Beyer et al. (2016) y Coombs (2007); cada organización fija los suyos por escrito.")
    return L.svg()


# ------------------------------------------------------------------------------
# 137 · Confianza (Mayer, Davis & Schoorman) y reparación (Kim et al.)
# ------------------------------------------------------------------------------
def confianza_y_reparacion() -> str:
    L = Lienzo("Qué sostiene la confianza y cómo se repara según lo que falló",
               "Modelo de confianza: capacidad, benevolencia e integridad forman la confiabilidad percibida, que junto a "
               "la propensión a confiar y al riesgo percibido produce confianza y conducta de riesgo. A la derecha, "
               "cómo cambia la reparación según la falla haya sido de competencia o de integridad.", 600, "137")
    L.cabecera("MARCO", "Clase 137 · Qué sostiene la confianza y qué reparar", VIOLETA,
               "Mayer, Davis & Schoorman (1995) · Kim et al. (2004)")
    L.texto(28, 84, "MODELO DE CONFIANZA", 11.5, SUAVE, "700", "start", 'letter-spacing="1.4"')
    factores = [("Capacidad", "habilidad y conocimiento para el asunto", AZUL),
                ("Benevolencia", "quiere el bien de quien confía, más allá de su interés", VERDE),
                ("Integridad", "se rige por principios que quien confía acepta", ROJO)]
    y = 100
    for n, d, c in factores:
        L.caja(28, y, 250, 70, "#ffffff", c, 10, 1.8)
        L.texto(44, y + 26, n, 15, TINTA, "700")
        L.parrafo(44, y + 45, d, 222, 12, SUAVE)
        L.flecha(278, y + 35, 318, 178, c, 1.8)
        y += 84
    L.caja(318, 142, 170, 72, "#ffffff", VIOLETA, 12, 2)
    L.texto(403, 170, "Confiabilidad", 14.5, TINTA, "700", "middle")
    L.texto(403, 188, "percibida", 14.5, TINTA, "700", "middle")
    L.texto(403, 205, "lo que observa quien confía", 10.5, SUAVE, "400", "middle")
    L.caja(318, 280, 170, 48, PAPEL, GRIS, 10, 1.2)
    L.texto(403, 301, "Propensión a confiar", 12.5, TINTA, "600", "middle")
    L.texto(403, 317, "rasgo de quien confía", 10.5, SUAVE, "400", "middle")
    L.caja(318, 340, 170, 48, PAPEL, GRIS, 10, 1.2)
    L.texto(403, 361, "Riesgo percibido", 12.5, TINTA, "600", "middle")
    L.texto(403, 377, "lo que está en juego", 10.5, SUAVE, "400", "middle")
    L.flecha(403, 214, 403, 236, VIOLETA, 2)
    L.partes.append(f'<circle cx="403" cy="250" r="14" fill="{VIOLETA}"/>')
    L.texto(403, 255, "+", 17, "#ffffff", "700", "middle")
    L.flecha(403, 328, 403, 268, GRIS, 1.4)
    L.caja(28, 400, 460, 64, "#ffffff", VIOLETA, 12, 2)
    L.texto(258, 427, "CONFIANZA", 15, VIOLETA, "800", "middle", 'letter-spacing="1.2"')
    L.texto(258, 448, "disposición a ser vulnerable ante la acción del otro, sin poder vigilarlo ni controlarlo", 12, SUAVE, "400", "middle")
    L.flecha(403, 388, 403, 398, VIOLETA, 2)
    # Panel de reparación
    x0 = 540
    L.texto(x0, 84, "REPARAR: PRIMERO, DIAGNOSTICAR QUÉ FALLÓ", 11.5, SUAVE, "700", "start", 'letter-spacing="1.4"')
    L.caja(x0, 100, ANCHO - x0 - 28, 160, "#ffffff", AZUL, 12, 1.8)
    L.partes.append(f'<rect x="{x0}" y="100" width="{ANCHO - x0 - 28}" height="34" rx="12" fill="{AZUL}"/>')
    L.texto(x0 + 18, 122, "Falla de competencia: se equivocó, no mintió", 14, "#ffffff", "700")
    y = L.parrafo(x0 + 18, 158, "Se repara con reconocimiento del error, explicación de la causa y corrección verificable.", 400, 13)
    y = L.parrafo(x0 + 18, y + 6, "En los experimentos de Kim et al., la disculpa repara mejor este tipo de falla que negarla.", 400, 12.5, SUAVE)
    L.caja(x0, 280, ANCHO - x0 - 28, 190, "#ffffff", ROJO, 12, 1.8)
    L.partes.append(f'<rect x="{x0}" y="280" width="{ANCHO - x0 - 28}" height="34" rx="12" fill="{ROJO}"/>')
    L.texto(x0 + 18, 302, "Falla de integridad: se duda de su honestidad", 14, "#ffffff", "700")
    y = L.parrafo(x0 + 18, 338, "Lo que se discute no es la habilidad sino el carácter: cuesta más y tarda más.", 400, 13)
    y = L.parrafo(x0 + 18, y + 6, "Los experimentos hallaron que, con evidencia ambigua, negar rindió más que disculparse. "
                  "La clase fija un límite: nunca se niega lo que se sabe cierto.", 400, 12.5, SUAVE)
    L.caja(x0, 490, ANCHO - x0 - 28, 70, PAPEL, PAPEL, 0)
    L.parrafo(x0, 506, "En ambos casos la reparación se mide por conducta sostenida que un tercero pueda comprobar, "
              "no por lo que la organización anuncia.", ANCHO - x0 - 28, 12.5, TINTA, "600")
    L.pie(584, "Los hallazgos de Kim et al. provienen de escenarios experimentales; orientan el diagnóstico, no sustituyen el juicio ante hechos reales.")
    return L.svg()


# ------------------------------------------------------------------------------
# 200 · Responsabilidad atribuida y respuesta (SCCT, Coombs)
# ------------------------------------------------------------------------------
def respuesta_scct() -> str:
    L = Lienzo("Cómo la responsabilidad atribuida decide la respuesta pública",
               "Matriz de la teoría situacional de comunicación de crisis: tres grupos de crisis según la responsabilidad "
               "que el público atribuye (víctima, accidental, evitable) y la postura de respuesta que corresponde, "
               "siempre precedida de información e instrucción.", 600, "200")
    L.cabecera("MARCO", "Clase 200 · La respuesta del CEO sigue a la responsabilidad atribuida", ROJO,
               "Coombs (2007), teoría situacional")
    L.caja(28, 76, ANCHO - 56, 62, "#ffffff", VERDE, 12, 2)
    L.texto(48, 100, "SIEMPRE PRIMERO", 11.5, VERDE, "700", "start", 'letter-spacing="1.4"')
    L.texto(48, 124, "Informar e instruir: qué pasó, qué debe hacer quien está en riesgo, "
            "y reconocer el daño humano antes de hablar de la imagen.", 14, TINTA, "600")
    cols = [
        ("VÍCTIMA", "responsabilidad atribuida mínima", AZUL,
         ["Desastre natural, rumor, violencia ajena, manipulación maliciosa del producto."],
         "Informar y mostrar apoyo. Reafirmar lo que la organización sí hace bien.",
         "Bastan información y cuidado; no hace falta disculparse por lo que no se hizo."),
        ("ACCIDENTAL", "responsabilidad atribuida moderada", NARANJA,
         ["Falla técnica o error no deliberado, un reto de terceros, un accidente."],
         "Informar y explicar el contexto con evidencia. Disminuir: justificar solo lo que se pruebe.",
         "La explicación vale solo si es verificable; una excusa que cae agrava."),
        ("EVITABLE", "responsabilidad atribuida fuerte", ROJO,
         ["Error humano evitable, falta de supervisión, conducta indebida de la organización."],
         "Reconstruir: asumir responsabilidad, disculparse, reparar y compensar.",
         "Negar o minimizar aquí es la peor opción: el público ya atribuye culpa."),
    ]
    w, gap = 320, 20
    for i, (nombre, sub, c, ejemplos, postura, nota) in enumerate(cols):
        x = 28 + i * (w + gap)
        L.caja(x, 160, w, 330, "#ffffff", c, 12, 1.8)
        L.partes.append(f'<path d="M{x},194 V172 a12,12 0 0 1 12,-12 H{x + w - 12} a12,12 0 0 1 12,12 V194 Z" fill="{c}"/>')
        L.texto(x + 16, 182, nombre, 13.5, "#ffffff", "800", "start", 'letter-spacing="1.2"')
        L.texto(x + 16, 216, sub, 12, SUAVE)
        L.texto(x + 16, 246, "Ejemplos del grupo", 11.5, SUAVE, "700")
        y = L.parrafo(x + 16, 264, ejemplos[0], w - 32, 12.5)
        L.texto(x + 16, y + 14, "Postura", 11.5, SUAVE, "700")
        y = L.parrafo(x + 16, y + 32, postura, w - 32, 13.5, TINTA, "600")
        L.texto(x + 16, y + 12, "Cuidado", 11.5, SUAVE, "700")
        L.parrafo(x + 16, y + 30, nota, w - 32, 12.5, SUAVE)
        if i < 2:
            L.flecha(x + w + 3, 325, x + w + gap - 3, 325, GRIS, 2)
    L.texto(28, 514, "Sube un escalón cuando hay crisis previas similares o una reputación ya dañada.", 12.5, TINTA, "600")
    L.partes.append(f'<path d="M28,526 H{ANCHO - 28}" stroke="{GRIS}" stroke-width="2" marker-end="url(#p-200)"/>')
    L.texto(28, 548, "más responsabilidad atribuida  →  respuesta más cercana a asumir y reparar", 12, SUAVE)
    L.pie(580, "Antes de elegir la postura, el CEO comprueba que lo que dirá coincide con lo que la empresa sabe y hace por dentro.")
    return L.svg()


DIAGRAMAS = {
    34: prominencia_interesados,
    137: confianza_y_reparacion,
    190: escalamiento_incidente,
    200: respuesta_scct,
}
