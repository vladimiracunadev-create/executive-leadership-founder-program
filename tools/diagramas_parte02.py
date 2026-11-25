"""Diagramas a medida de la parte 02 (comunicación, influencia y presencia ejecutiva).

Cada diagrama dibuja el marco que enseña su clase; ninguno es una plantilla común.
"""

from __future__ import annotations

from diagramas_clase import (ANCHO, AZUL, BORDE, GRIS, NARANJA, PAPEL, ROJO, SUAVE, TINTA, VERDE, VIOLETA, Lienzo)

COLOR = AZUL  # etapa 1 usa verde en las fichas; aquí cada marco elige sus colores


def _fila_caja(L, x, y, w, h, titulo, texto, color, tam=12.5, borde=None):
    L.caja(x, y, w, h, "#ffffff", borde or color, 10, 1.6)
    L.partes.append(f'<rect x="{x}" y="{y}" width="6" height="{h}" rx="3" fill="{color}"/>')
    L.texto(x + 18, y + 22, titulo, 14, TINTA, "700")
    L.parrafo(x + 18, y + 40, texto, w - 32, tam, SUAVE)


# ---------------------------------------------------------------- 025
def riqueza_del_canal() -> str:
    L = Lienzo("Elegir el canal según la ambigüedad del mensaje",
               "Matriz de riqueza del canal: los canales pobres sirven a mensajes sin ambigüedad y los ricos a los equívocos; "
               "las esquinas opuestas son desajustes.", 600, "025")
    L.cabecera("MARCO", "Clase 025 · El canal debe corresponder al mensaje", VERDE, "Daft & Lengel (1986)")
    x0, y0, w, h = 120, 84, 520, 380
    L.caja(x0, y0, w, h, "#ffffff", BORDE, 12, 1.2)
    L.partes.append(f'<path d="M{x0 + 20},{y0 + h - 20} L{x0 + w - 20},{y0 + 20}" stroke="{VERDE}" stroke-width="30" '
                    f'stroke-opacity="0.13" stroke-linecap="round"/>')
    L.texto(x0 + w / 2, y0 + h + 28, "MENSAJE:  poca ambigüedad  →  muy ambiguo (varias lecturas posibles)", 12, SUAVE, "700", "middle")
    L.partes.append(f'<text transform="translate(52,{y0 + h / 2}) rotate(-90)" font-size="12" font-weight="700" fill="{SUAVE}" '
                    f'text-anchor="middle">CANAL:  pobre  →  rico</text>')
    puntos = [
        (x0 + 28, y0 + h - 98, 200, "Informe, tablero, correo", "Un cambio de horario ya decidido.", AZUL),
        (x0 + 160, y0 + 168, 210, "Reunión con preguntas", "Una política nueva que genera dudas.", NARANJA),
        (x0 + 300, y0 + 30, 205, "Conversación directa", "Una reestructuración o una mala noticia.", ROJO),
    ]
    for x, y, ww, t, d, c in puntos:
        L.caja(x, y, ww, 74, "#ffffff", c, 10, 1.8)
        L.texto(x + 12, y + 22, t, 13, TINTA, "700")
        L.parrafo(x + 12, y + 40, d, ww - 22, 11.5, SUAVE)
    L.texto(x0 + w - 10, y0 + h - 14, "desajuste: canal pobre", 11, ROJO, "600", "end")
    L.texto(x0 + w - 10, y0 + h - 1, "para algo ambiguo", 11, ROJO, "600", "end")
    L.texto(x0 + 12, y0 + 22, "desajuste: canal rico", 11, ROJO, "600")
    L.texto(x0 + 12, y0 + 35, "para algo simple", 11, ROJO, "600")
    xr = 680
    L.texto(xr, 92, "QUÉ DICE EL MARCO", 11.5, SUAVE, "700", "start", 'letter-spacing="1.4"')
    y = 108
    for t, d, c in [
        ("Incertidumbre", "Falta información. Se resuelve con más datos: un canal pobre basta.", AZUL),
        ("Equivocidad", "Hay varias interpretaciones posibles. Se resuelve conversando, con retroalimentación inmediata: un canal rico.", ROJO),
        ("Retroalimentación", "Pide que repitan el mensaje con sus palabras: así se sabe que llegó.", VERDE),
    ]:
        _fila_caja(L, xr, y, ANCHO - xr - 28, 98, t, d, c)
        y += 112
    L.pie(558, "Lo que se decide por escrito conviene dejarlo también por escrito después de la conversación: el canal rico aclara, el pobre deja registro.")
    return L.svg()


# ---------------------------------------------------------------- 026
def tipos_de_pregunta() -> str:
    L = Lienzo("Cuatro tipos de pregunta según cuánto controla quien pregunta",
               "Indagación humilde, diagnóstica, confrontacional y de proceso: cada una con su pregunta típica, "
               "su función y su riesgo.", 560, "026")
    L.cabecera("MARCO", "Clase 026 · Preguntar para entender, no para confirmar", VERDE, "Schein (2013)")
    tipos = [
        ("Humilde", "¿Qué pasó? ¿Cómo lo ves tú?", "Invita a hablar sin dirigir. Se pregunta algo que no se sabe.", "Puede dispersarse si no hay foco.", VERDE),
        ("Diagnóstica", "¿Qué sentiste? ¿Por qué crees que ocurrió?", "Dirige la atención hacia causas o emociones del otro.", "Puede inducir una explicación.", AZUL),
        ("Confrontacional", "¿Has pensado en probar otra cosa?", "Introduce la idea de quien pregunta en forma de pregunta.", "Es una opinión disfrazada; puede cerrar la conversación.", NARANJA),
        ("De proceso", "¿Cómo vamos en esta conversación?", "Se pregunta por la conversación misma.", "Mal usada, evade el contenido.", VIOLETA),
    ]
    w, gap = 232, 24
    for i, (n, q, f, r, c) in enumerate(tipos):
        x = 28 + i * (w + gap)
        L.caja(x, 96, w, 340, "#ffffff", c, 12, 1.8)
        L.partes.append(f'<path d="M{x},134 V108 a12,12 0 0 1 12,-12 H{x + w - 12} a12,12 0 0 1 12,12 V134 Z" fill="{c}"/>')
        L.texto(x + 16, 121, n.upper(), 13, "#ffffff", "800", "start", 'letter-spacing="1.2"')
        L.texto(x + 16, 160, "Pregunta típica", 11, SUAVE, "700")
        yy = L.parrafo(x + 16, 178, q, w - 32, 14, TINTA, "600")
        L.texto(x + 16, yy + 14, "Qué hace", 11, SUAVE, "700")
        yy = L.parrafo(x + 16, yy + 32, f, w - 32, 12.5)
        L.texto(x + 16, yy + 12, "Riesgo", 11, SUAVE, "700")
        L.parrafo(x + 16, yy + 30, r, w - 32, 12.5, SUAVE)
    L.flecha(28, 470, ANCHO - 28, 470, GRIS, 2)
    L.texto(28, 494, "más abierta, más información del otro", 12, SUAVE, "600")
    L.texto(ANCHO - 28, 494, "más dirigida por quien pregunta", 12, SUAVE, "600", "end")
    L.pie(528, "Regla de la clase: empieza humilde. Pasa a un tipo más dirigido solo después de haber escuchado, y dilo en voz alta.")
    return L.svg()


# ---------------------------------------------------------------- 027
def piramide() -> str:
    L = Lienzo("Pirámide: primero la respuesta, luego las razones, luego los datos",
               "Estructura descendente de un documento ejecutivo: respuesta arriba, tres líneas clave que la sostienen, "
               "datos de apoyo debajo, con una introducción de situación, complicación y pregunta.", 590, "027")
    L.cabecera("MARCO", "Clase 027 · Escribir para que decidan", VERDE, "Minto (2005)")
    cx = 390
    niveles = [
        (300, "RESPUESTA", "Lo que quieres que se decida, en una frase", ROJO, 100),
        (480, "LÍNEAS CLAVE", "Tres razones, agrupadas y ordenadas", NARANJA, 202),
        (680, "DATOS Y SUPUESTOS", "Hechos, cifras y fuentes que sostienen cada razón", AZUL, 304),
    ]
    for ww, t, d, c, y in niveles:
        L.caja(cx - ww / 2, y, ww, 84, "#ffffff", c, 12, 2)
        L.texto(cx, y + 34, t, 14, c, "800", "middle", 'letter-spacing="1.2"')
        L.parrafo(cx, y + 54, d, ww - 30, 12.5, SUAVE, "400", "middle")
    L.flecha(cx, 186, cx, 200, GRIS, 2)
    L.flecha(cx, 288, cx, 302, GRIS, 2)
    # Pruebas
    L.partes.append(f'<path d="M752,120 V380" stroke="{VERDE}" stroke-width="2" marker-end="url(#p-027)"/>')
    L.partes.append(f'<path d="M782,380 V120" stroke="{ROJO}" stroke-width="2" marker-end="url(#p-027)"/>')
    L.texto(804, 112, "El lector pregunta", 11.5, VERDE, "700")
    L.texto(804, 130, "¿por qué? ¿cómo lo sabes?", 12, TINTA)
    L.texto(804, 148, "y se baja un nivel", 12, SUAVE)
    L.texto(804, 330, "El autor comprueba", 11.5, ROJO, "700")
    L.texto(804, 348, "¿y entonces?", 12, TINTA)
    L.texto(804, 366, "y se sube un nivel", 12, SUAVE)
    # Introducción
    L.caja(28, 410, 480, 120, "#ffffff", VIOLETA, 12, 1.8)
    L.texto(46, 434, "INTRODUCCIÓN: SITUACIÓN → COMPLICACIÓN → PREGUNTA", 11.5, VIOLETA, "700", "start", 'letter-spacing="0.8"')
    L.parrafo(46, 454, "Lo que ya se sabe y nadie discute; lo que cambió o se complica; la pregunta que la respuesta contesta.", 440, 12.5)
    L.caja(530, 410, ANCHO - 558, 120, "#ffffff", AZUL, 12, 1.8)
    L.texto(548, 434, "CADA GRUPO DE IDEAS", 11.5, AZUL, "700", "start", 'letter-spacing="0.8"')
    L.parrafo(548, 454, "Debe ser de un mismo tipo, sin solaparse y sin dejar fuera lo importante (excluyentes y exhaustivas).", ANCHO - 590, 12.5)
    L.pie(566, "Orden dentro de un grupo: por tiempo, por estructura o por importancia; elige uno y dilo.")
    return L.svg()


# ---------------------------------------------------------------- 028
def lamina_de_decision() -> str:
    L = Lienzo("Anatomía de una presentación para decidir",
               "Una lámina de decisión: el título es la afirmación, la evidencia la respalda, y al pie se pide la decisión.", 600, "028")
    L.cabecera("MARCO", "Clase 028 · La lámina existe para que alguien decida", VERDE, "Duarte (2010) · Minto (2005)")
    sx, sy, sw, sh = 28, 84, 600, 400
    L.caja(sx, sy, sw, sh, "#ffffff", GRIS, 12, 1.6)
    L.texto(sx + 24, sy + 44, "Mantener el proveedor actual cuesta 8 % menos en 3 años", 17, TINTA, "700")
    L.partes.append(f'<line x1="{sx + 24}" y1="{sy + 58}" x2="{sx + sw - 24}" y2="{sy + 58}" stroke="{BORDE}"/>')
    # gráfico ficticio
    bx = sx + 40
    for i, (a, b) in enumerate([(120, 150), (140, 150), (150, 150)]):
        L.partes.append(f'<rect x="{bx + i * 70}" y="{sy + 340 - a}" width="26" height="{a}" fill="{AZUL}" fill-opacity="0.8"/>')
        L.partes.append(f'<rect x="{bx + i * 70 + 30}" y="{sy + 340 - b}" width="26" height="{b}" fill="{NARANJA}" fill-opacity="0.8"/>')
    L.texto(bx, sy + 362, "Año 1        Año 2        Año 3", 11, SUAVE)
    L.texto(sx + 270, sy + 130, "Actual", 12, AZUL, "700"); L.texto(sx + 270, sy + 148, "Alternativa", 12, NARANJA, "700")
    L.parrafo(sx + 270, sy + 180, "Las tres cifras que sostienen el título, con la fuente y la fecha al pie.", 300, 12.5, SUAVE)
    L.partes.append(f'<rect x="{sx}" y="{sy + sh - 44}" width="{sw}" height="44" rx="0" fill="{VERDE}" fill-opacity="0.14"/>')
    L.texto(sx + 24, sy + sh - 17, "Decisión pedida: renovar por 36 meses, antes del 30 de marzo.", 13.5, TINTA, "700")
    anot = [
        (sy + 44, "1", "El título es una afirmación, no un tema: se puede aceptar o rebatir."),
        (sy + 200, "2", "Una sola idea y la evidencia mínima que la sostiene."),
        (sy + sh - 22, "3", "Se pide una decisión concreta, con fecha."),
    ]
    for y, n, t in anot:
        L.partes.append(f'<circle cx="{sx + sw + 28}" cy="{y}" r="13" fill="{VERDE}"/>')
        L.texto(sx + sw + 28, y + 5, n, 13, "#ffffff", "700", "middle")
        L.parrafo(sx + sw + 52, y - 4, t, ANCHO - sx - sw - 90, 12.5, TINTA)
    L.caja(sx + sw + 20, sy + 270, ANCHO - sx - sw - 48, 112, PAPEL, BORDE, 10, 1)
    L.texto(sx + sw + 36, sy + 296, "ANTES DE LA LÁMINA", 11, SUAVE, "700", "start", 'letter-spacing="1.2"')
    L.parrafo(sx + sw + 36, sy + 316, "Cómo es hoy y cómo podría ser: el cambio que se propone es el puente entre ambos.", ANCHO - sx - sw - 80, 12.5)
    L.pie(556, "Los datos del ejemplo son ilustrativos. Las alternativas que se descartaron van en un anexo, no en la lámina.")
    return L.svg()


# ---------------------------------------------------------------- 029
def succes() -> str:
    L = Lienzo("Seis rasgos de una idea que se entiende, se recuerda y se actúa",
               "Simple, inesperada, concreta, creíble, emocional y contada como historia, cada una con su pregunta de control.", 560, "029")
    L.cabecera("MARCO", "Clase 029 · Qué hace que un mensaje se quede", VERDE, "Heath & Heath (2007)")
    rasgos = [
        ("S", "Simple", "¿Cuál es el núcleo, en una frase?", "Una idea que prioriza: lo demás se omite.", AZUL),
        ("I", "Inesperada", "¿Qué rompe lo que la audiencia da por hecho?", "Genera curiosidad al abrir un hueco.", NARANJA),
        ("C", "Concreta", "¿Se puede ver, medir o tocar?", "Cifras y ejemplos en lugar de abstracciones.", VERDE),
        ("C", "Creíble", "¿Por qué debería creérmelo?", "Detalle comprobable o un caso que la audiencia pueda verificar.", VIOLETA),
        ("E", "Emocional", "¿Por qué le importa a esta persona?", "Conecta con algo que le importa, no solo con una cifra.", ROJO),
        ("H", "Historia", "¿Qué relato lo muestra en acción?", "Un caso con personas y decisiones.", GRIS),
    ]
    w, h, gx, gy = 320, 190, 28, 28
    for i, (letra, n, q, d, c) in enumerate(rasgos):
        x, y = 28 + (i % 3) * (w + gx), 90 + (i // 3) * (h + gy)
        L.caja(x, y, w, h, "#ffffff", c, 12, 1.8)
        L.partes.append(f'<circle cx="{x + 34}" cy="{y + 38}" r="22" fill="{c}"/>')
        L.texto(x + 34, y + 46, letra, 22, "#ffffff", "800", "middle")
        L.texto(x + 68, y + 44, n, 17, TINTA, "700")
        L.texto(x + 18, y + 86, "Pregunta de control", 11, SUAVE, "700")
        yy = L.parrafo(x + 18, y + 104, q, w - 36, 13.5, TINTA, "600")
        L.parrafo(x + 18, yy + 6, d, w - 36, 12.5, SUAVE)
    L.pie(556, "Es una guía de diseño de mensajes, no una receta: un mensaje puede funcionar sin cumplir los seis rasgos.")
    return L.svg()


# ---------------------------------------------------------------- 030
def niveles_de_feedback() -> str:
    L = Lienzo("A qué nivel apunta el feedback decide si ayuda",
               "El feedback centrado en la tarea tiende a mejorar el desempeño; el que dirige la atención al yo tiende a "
               "debilitarlo. Al recibirlo, tres disparadores explican por qué cuesta: verdad, relación e identidad.", 580, "030")
    L.cabecera("MARCO", "Clase 030 · Feedback: dónde se dirige la atención", VERDE, "Kluger & DeNisi (1996) · Stone & Heen (2014)")
    L.texto(28, 84, "DAR: EL NIVEL AL QUE APUNTA", 11.5, SUAVE, "700", "start", 'letter-spacing="1.4"')
    niveles = [
        ("TAREA", "Qué se hizo y qué faltó en esa tarea", "«El informe omite el costo de mantenimiento.»", VERDE, "tiende a ayudar"),
        ("PROCESO", "Cómo se trabajó y qué se puede cambiar", "«Contrasta dos fuentes antes de la conclusión.»", AZUL, "puede ayudar"),
        ("YO", "Qué dice el resultado de quién eres", "«Eres desordenado.»", ROJO, "tiende a debilitar"),
    ]
    y = 100
    for n, d, ej, c, ef in niveles:
        L.caja(28, y, 560, 100, "#ffffff", c, 12, 1.8)
        L.partes.append(f'<rect x="28" y="{y}" width="150" height="100" rx="12" fill="{c}"/>')
        L.texto(103, y + 52, n, 15, "#ffffff", "800", "middle", 'letter-spacing="1.2"')
        L.texto(103, y + 72, ef, 11.5, "#ffffff", "600", "middle")
        L.parrafo(194, y + 30, d, 380, 13.5, TINTA, "600")
        L.parrafo(194, y + 64, ej, 380, 12.5, SUAVE)
        y += 116
    L.flecha(604, 100, 604, 440, GRIS, 2)
    L.texto(616, 270, "más cerca", 11, SUAVE, "600"); L.texto(616, 284, "del yo", 11, SUAVE, "600")
    L.caja(28, 452, 560, 74, PAPEL, BORDE, 10, 1)
    L.parrafo(44, 474, "En la revisión de Kluger y DeNisi, más de un tercio de las intervenciones de feedback redujo el desempeño: "
              "dar feedback no garantiza que ayude.", 530, 12.5, TINTA, "600")
    x0 = 680
    L.texto(x0, 84, "RECIBIR: TRES DISPARADORES", 11.5, SUAVE, "700", "start", 'letter-spacing="1.4"')
    y = 100
    for t, d, c in [("Verdad", "«Esto no es cierto ni justo.» Se discute el contenido.", AZUL),
                    ("Relación", "«¿Quién eres tú para decírmelo?» Se discute al emisor.", NARANJA),
                    ("Identidad", "«Esto dice que no valgo.» Se vive como un ataque a quién soy.", ROJO)]:
        _fila_caja(L, x0, y, ANCHO - x0 - 28, 100, t, d, c)
        y += 116
    L.caja(x0, 452, ANCHO - x0 - 28, 74, PAPEL, BORDE, 10, 1)
    L.parrafo(x0 + 16, 474, "Identificar el disparador permite separar el contenido útil de la reacción.", ANCHO - x0 - 60, 12.5, TINTA, "600")
    L.pie(560, "Los resultados de Kluger y DeNisi son promedios de muchos estudios: orientan, no predicen un caso concreto.")
    return L.svg()


# ---------------------------------------------------------------- 031
def camino_a_la_accion() -> str:
    L = Lienzo("El camino a la acción: de lo que se observa a lo que se hace",
               "Se observan hechos, se cuenta una historia sobre ellos, se siente una emoción y se actúa. "
               "Para cambiar una conversación se retrocede por el camino.", 560, "031")
    L.cabecera("MARCO", "Clase 031 · Volver a los hechos antes de hablar", VERDE, "Patterson et al. (2012) · Stone, Patton & Heen (1999)")
    pasos = [
        ("VER Y OÍR", "Lo observable: qué se dijo, qué se hizo, cuándo.", "«No contestó mi correo en dos días.»", AZUL),
        ("CONTAR UNA HISTORIA", "La interpretación que se agrega: motivos, intención, carácter.", "«Me ignora a propósito.»", NARANJA),
        ("SENTIR", "La emoción que genera la historia.", "Enojo, desconfianza, vergüenza.", ROJO),
        ("ACTUAR", "Lo que se hace con esa emoción: callar, atacar o hablar.", "Evitar, reclamar o conversar.", VIOLETA),
    ]
    w, gap = 232, 24
    for i, (t, d, e, c) in enumerate(pasos):
        x = 28 + i * (w + gap)
        L.caja(x, 96, w, 210, "#ffffff", c, 12, 1.8)
        L.partes.append(f'<path d="M{x},134 V108 a12,12 0 0 1 12,-12 H{x + w - 12} a12,12 0 0 1 12,12 V134 Z" fill="{c}"/>')
        L.texto(x + 16, 121, t, 12.5, "#ffffff", "800", "start", 'letter-spacing="1"')
        yy = L.parrafo(x + 16, 160, d, w - 32, 13.5, TINTA, "600")
        L.texto(x + 16, yy + 14, "Ejemplo", 11, SUAVE, "700")
        L.parrafo(x + 16, yy + 32, e, w - 32, 12.5, SUAVE)
        if i < 3:
            L.flecha(x + w + 3, 200, x + w + gap - 3, 200, GRIS, 2)
    L.trazo(f"M{28 + 3 * (w + gap) + w / 2},308 V340 H{28 + w / 2} V312", GRIS, 2,
            extra=f'stroke-dasharray="7 6" marker-end="url(#p-031)"')
    L.caja(300, 326, 440, 28, PAPEL, GRIS, 14, 1.2)
    L.texto(520, 345, "retroceder: de la acción a la emoción, a la historia y a los hechos", 12, TINTA, "600", "middle")
    L.caja(28, 380, 480, 130, "#ffffff", VERDE, 12, 1.8)
    L.texto(46, 404, "CÓMO SE USA", 11.5, VERDE, "700", "start", 'letter-spacing="1.2"')
    L.parrafo(46, 424, "Antes de hablar, separa lo observado de la historia. Empieza la conversación por los hechos y presenta la "
              "historia como una hipótesis, no como un hecho.", 444, 12.5)
    L.caja(532, 380, ANCHO - 560, 130, "#ffffff", AZUL, 12, 1.8)
    L.texto(550, 404, "TRES CONVERSACIONES EN UNA", 11.5, AZUL, "700", "start", 'letter-spacing="1.2"')
    L.parrafo(550, 424, "Qué ocurrió, los sentimientos y la identidad (Stone, Patton y Heen). El camino a la acción ayuda a ordenar "
              "las dos primeras.", ANCHO - 590, 12.5)
    L.pie(540, "Es un modelo de trabajo propuesto por los autores, no una ley de la conducta: sirve para preparar, no para predecir.")
    return L.svg()


# ---------------------------------------------------------------- 032
def conflicto_tarea_relacion() -> str:
    L = Lienzo("Conflicto de tarea y conflicto de relación",
               "Cuadrante según haya poco o mucho conflicto de tarea y de relación: el debate sobre la tarea puede ayudar; "
               "el conflicto personal tiende a dañar.", 600, "032")
    L.cabecera("MARCO", "Clase 032 · Discutir la tarea sin atacar a la persona", VERDE, "Jehn (1995)")
    x0, y0, cw, ch = 130, 92, 250, 170
    celdas = [
        (0, 0, "Debate productivo", "Se discuten ideas y criterios sin que se vuelva personal.", VERDE),
        (1, 0, "Conflicto tóxico", "La discusión sobre la tarea se mezcla con ataques personales.", ROJO),
        (0, 1, "Falta de contraste", "Nadie discute: pueden pasar por alto alternativas.", GRIS),
        (1, 1, "Conflicto personal", "La tensión es entre personas, con poca discusión de fondo.", NARANJA),
    ]
    for cx, cy, t, d, c in celdas:
        x, y = x0 + cx * (cw + 12), y0 + cy * (ch + 12)
        L.caja(x, y, cw, ch, "#ffffff", c, 12, 1.8)
        L.partes.append(f'<rect x="{x}" y="{y}" width="{cw}" height="36" rx="12" fill="{c}"/>')
        L.texto(x + 16, y + 24, t, 14, "#ffffff", "700")
        L.parrafo(x + 16, y + 62, d, cw - 32, 13, TINTA)
    L.texto(x0 + cw + 6, y0 + 2 * ch + 40, "CONFLICTO DE RELACIÓN:   poco                         mucho", 11.5, SUAVE, "700", "middle")
    L.partes.append(f'<text transform="translate(86,{y0 + ch + 6}) rotate(-90)" font-size="11.5" font-weight="700" fill="{SUAVE}" '
                    f'text-anchor="middle">CONFLICTO DE TAREA:   mucho  ←  poco</text>')
    xr = 700
    L.texto(xr, 100, "QUÉ MUESTRA LA EVIDENCIA", 11.5, SUAVE, "700", "start", 'letter-spacing="1.4"')
    y = 116
    for t, d, c in [("Tarea", "En tareas no rutinarias, un nivel moderado de conflicto de tarea se asoció a mejor decisión.", VERDE),
                    ("Relación", "El conflicto de relación se asoció a menor satisfacción y a menor desempeño del grupo.", ROJO),
                    ("Condición", "Aun el debate de tarea se vuelve dañino cuando se contamina de conflicto personal.", NARANJA)]:
        _fila_caja(L, xr, y, ANCHO - xr - 28, 108, t, d, c)
        y += 122
    L.caja(28, 482, ANCHO - 56, 56, PAPEL, BORDE, 10, 1)
    L.parrafo(44, 504, "Práctica: nombra el asunto («el plazo», «el criterio»), separa a la persona del problema y pregunta por los "
              "intereses detrás de cada posición.", ANCHO - 90, 12.5, TINTA, "600")
    L.pie(566, "Jehn estudió equipos de trabajo; el efecto depende del tipo de tarea y del nivel de conflicto. No hay un nivel «óptimo» universal.")
    return L.svg()


# ---------------------------------------------------------------- 033
def persuasion_etica() -> str:
    L = Lienzo("Persuasión, manipulación y coerción: dos pruebas",
               "Un espectro de influencia con dos preguntas, si el interés es transparente y si la otra persona es libre de rechazar; "
               "y seis palancas de influencia con su uso legítimo y su abuso.", 620, "033")
    L.cabecera("MARCO", "Clase 033 · Influir sin engañar ni forzar", VERDE, "Cialdini (2016) · Yukl (2010)")
    x = 28
    tramos = [("PERSUASIÓN", "Expone su propósito y deja decidir.", VERDE),
              ("MANIPULACIÓN", "Oculta el propósito o explota una debilidad.", NARANJA),
              ("COERCIÓN", "Condiciona la decisión con una amenaza.", ROJO)]
    for i, (t, d, c) in enumerate(tramos):
        xx = x + i * 340
        L.caja(xx, 90, 316, 84, "#ffffff", c, 12, 2)
        L.texto(xx + 16, 118, t, 14, c, "800", "start", 'letter-spacing="1.2"')
        L.parrafo(xx + 16, 140, d, 284, 12.5)
        if i < 2:
            L.flecha(xx + 318, 132, xx + 336, 132, GRIS, 2)
    L.caja(28, 188, 490, 52, PAPEL, BORDE, 10, 1)
    L.texto(44, 210, "PRUEBA 1  ·  ¿mi interés es transparente?", 13, TINTA, "700")
    L.texto(44, 229, "Si lo ocultaría, algo falla.", 12, SUAVE)
    L.caja(530, 188, ANCHO - 558, 52, PAPEL, BORDE, 10, 1)
    L.texto(546, 210, "PRUEBA 2  ·  ¿puede decir que no sin castigo?", 13, TINTA, "700")
    L.texto(546, 229, "Si no, ya no es persuasión.", 12, SUAVE)
    L.texto(28, 268, "SEIS PALANCAS DE INFLUENCIA", 11.5, SUAVE, "700", "start", 'letter-spacing="1.4"')
    palancas = [("Reciprocidad", "Reconocer un favor real.", "Crear una deuda para cobrarla."),
                ("Coherencia", "Recordar un compromiso propio.", "Escalar un compromiso pequeño hasta atrapar."),
                ("Prueba social", "Mostrar lo que otros hacen de verdad.", "Inventar un consenso."),
                ("Autoridad", "Citar experiencia relevante.", "Apelar al cargo para callar preguntas."),
                ("Simpatía", "Encontrar afinidades reales.", "Halagar para bajar la guardia."),
                ("Escasez", "Informar un plazo real.", "Fabricar urgencia.")]
    w, h = 320, 100
    for i, (n, ok, mal) in enumerate(palancas):
        xx, yy = 28 + (i % 3) * (w + 18), 284 + (i // 3) * (h + 14)
        L.caja(xx, yy, w, h, "#ffffff", BORDE, 10, 1.2)
        L.texto(xx + 14, yy + 22, n, 14, TINTA, "700")
        L.partes.append(f'<circle cx="{xx + 20}" cy="{yy + 44}" r="5" fill="{VERDE}"/>')
        L.parrafo(xx + 34, yy + 49, ok, w - 48, 12, TINTA)
        L.partes.append(f'<circle cx="{xx + 20}" cy="{yy + 74}" r="5" fill="{ROJO}"/>')
        L.parrafo(xx + 34, yy + 79, mal, w - 48, 12, SUAVE)
    L.pie(600, "Verde: uso legítimo. Rojo: abuso. Cialdini describe estos mecanismos; la frontera ética es criterio de la clase, no de su autor.")
    return L.svg()


# ---------------------------------------------------------------- 035
def ajuste_de_contexto() -> str:
    L = Lienzo("Ajuste de contexto: la presencia se decide mirando el entorno",
               "El propósito de la reunión, en el centro, se ajusta con variables de industria, organización, audiencia, cultura, "
               "modalidad y clima; apariencia no equivale a competencia.", 580, "035")
    L.cabecera("MARCO", "Clase 035 · Presencia: claridad y criterio ante la atención", VERDE, "Hall et al. (2019) · Chang & Cortina (2024)")
    cx, cy = 330, 300
    L.partes.append(f'<circle cx="{cx}" cy="{cy}" r="78" fill="{VERDE}" fill-opacity="0.14" stroke="{VERDE}" stroke-width="2"/>')
    L.texto(cx, cy - 4, "PROPÓSITO", 14, VERDE, "800", "middle", 'letter-spacing="1.2"')
    L.texto(cx, cy + 16, "qué debe lograr", 11.5, SUAVE, "400", "middle")
    L.texto(cx, cy + 30, "la reunión", 11.5, SUAVE, "400", "middle")
    import math
    vars_ = ["Industria", "Organización", "Rol y responsabilidad", "Audiencia", "Tipo de reunión", "Cultura y país", "Modalidad", "Clima"]
    for i, v in enumerate(vars_):
        a = -math.pi / 2 + i * 2 * math.pi / len(vars_)
        x, y = cx + 190 * math.cos(a), cy + 160 * math.sin(a)
        L.partes.append(f'<path d="M{cx + 78 * math.cos(a):g},{cy + 78 * math.sin(a):g} L{x - 40 * math.cos(a):g},{y - 20 * math.sin(a):g}" stroke="{BORDE}" stroke-width="1.6"/>')
        L.caja(x - 70, y - 17, 140, 34, "#ffffff", AZUL, 17, 1.4)
        L.texto(x, y + 5, v, 12, TINTA, "600", "middle")
    xr = 650
    L.texto(xr, 100, "DOS DESIGUALDADES QUE ORDENAN LA CLASE", 11.5, SUAVE, "700", "start", 'letter-spacing="1.2"')
    for i, (a, b) in enumerate([("apariencia  ≠  competencia", "Una primera impresión no mide capacidad ni liderazgo, y puede reflejar sesgos de quien observa."),
                                ("vestirse formal  ≠  presencia ejecutiva", "La presencia es claridad, estabilidad y criterio bajo atención.")]):
        y = 118 + i * 130
        L.caja(xr, y, ANCHO - xr - 28, 114, "#ffffff", VERDE, 12, 1.8)
        L.texto(xr + 16, y + 30, a, 16, TINTA, "800")
        L.parrafo(xr + 16, y + 54, b, ANCHO - xr - 60, 12.5, SUAVE)
    L.caja(xr, 390, ANCHO - xr - 28, 120, PAPEL, BORDE, 10, 1)
    L.texto(xr + 16, 414, "CÓMO SE DECIDE", 11.5, SUAVE, "700", "start", 'letter-spacing="1.2"')
    L.parrafo(xr + 16, 434, "Investiga el contexto, identifica restricciones funcionales y elige una opción coherente con quien "
              "serás en el cargo, de modo que el mensaje concentre la atención.", ANCHO - xr - 60, 12.5)
    L.pie(558, "Ninguna variable decide sola. Las impresiones dependen del contexto y del observador; esto no es un código de vestimenta.")
    return L.svg()


# ---------------------------------------------------------------- 036
def cuatro_justicias() -> str:
    L = Lienzo("Cuatro formas de justicia en una decisión impopular",
               "Distributiva, procedimental, interpersonal e informacional: lo que las personas evalúan al recibir una decisión "
               "que las perjudica, y qué debe contener el anuncio.", 600, "036")
    L.cabecera("MARCO", "Clase 036 · Comunicar una decisión que no gusta", VERDE, "Colquitt et al. (2001)")
    dims = [("Distributiva", "¿Es justo el resultado?", "Qué cambia, para quién y en qué medida; sin eufemismos.", ROJO),
            ("Procedimental", "¿Fue justo el proceso?", "Cómo se decidió, qué alternativas se evaluaron y quién participó.", NARANJA),
            ("Interpersonal", "¿Me trataron con respeto?", "Trato digno, sincero y cuidadoso al comunicar.", AZUL),
            ("Informacional", "¿Se explicó con claridad?", "Razones honestas, oportunas y suficientes.", VERDE)]
    w, gap = 232, 24
    for i, (n, q, d, c) in enumerate(dims):
        x = 28 + i * (w + gap)
        L.caja(x, 92, w, 230, "#ffffff", c, 12, 1.8)
        L.partes.append(f'<path d="M{x},130 V104 a12,12 0 0 1 12,-12 H{x + w - 12} a12,12 0 0 1 12,12 V130 Z" fill="{c}"/>')
        L.texto(x + 16, 117, n.upper(), 12.5, "#ffffff", "800", "start", 'letter-spacing="1"')
        L.parrafo(x + 16, 158, q, w - 32, 14.5, TINTA, "700")
        L.texto(x + 16, 214, "Qué debe contener el anuncio", 11, SUAVE, "700")
        L.parrafo(x + 16, 232, d, w - 32, 12.5)
    L.texto(28, 356, "SECUENCIA DEL ANUNCIO", 11.5, SUAVE, "700", "start", 'letter-spacing="1.4"')
    seq = ["Primero a los más afectados", "Hecho y resultado, sin rodeos", "Proceso y razones", "Qué viene y qué se hará por ellos", "Canal para preguntas y fecha de seguimiento"]
    w2 = (ANCHO - 56 - 4 * 18) / 5
    for i, s in enumerate(seq):
        x = 28 + i * (w2 + 18)
        L.caja(x, 372, w2, 76, "#ffffff", GRIS, 10, 1.4)
        L.partes.append(f'<circle cx="{x + 18}" cy="{390}" r="11" fill="{GRIS}"/>')
        L.texto(x + 18, 394.5, str(i + 1), 11.5, "#ffffff", "700", "middle")
        L.parrafo(x + 36, 394, s, w2 - 46, 12, TINTA, "600")
        if i < 4:
            L.flecha(x + w2 + 2, 410, x + w2 + 16, 410, GRIS, 1.8)
    L.caja(28, 466, ANCHO - 56, 60, PAPEL, BORDE, 10, 1)
    L.parrafo(44, 488, "Colquitt et al. hallaron que las cuatro dimensiones se distinguen y se relacionan con distintos resultados: "
              "explicar bien no compensa un proceso injusto ni un trato irrespetuoso.", ANCHO - 90, 12.5, TINTA, "600")
    L.pie(566, "Es un metaanálisis de investigación organizacional: indica qué evalúan las personas, no garantiza su aceptación.")
    return L.svg()


DIAGRAMAS = {
    25: riqueza_del_canal, 26: tipos_de_pregunta, 27: piramide, 28: lamina_de_decision, 29: succes,
    30: niveles_de_feedback, 31: camino_a_la_accion, 32: conflicto_tarea_relacion, 33: persuasion_etica,
    35: ajuste_de_contexto, 36: cuatro_justicias,
}
