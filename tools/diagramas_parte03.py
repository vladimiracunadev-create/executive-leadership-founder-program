"""Diagramas a medida de la parte 03 (inteligencia emocional, resiliencia y liderazgo adaptativo).

Cada diagrama dibuja el marco que enseña su clase; ninguno es una plantilla común.
"""

from __future__ import annotations

from diagramas_clase import (ANCHO, AZUL, BORDE, GRIS, NARANJA, PAPEL, ROJO, SUAVE, TINTA, VERDE, VIOLETA, Lienzo)


def _tarjeta(L, x, y, w, h, titulo, texto, color, tam=12.5):
    L.caja(x, y, w, h, "#ffffff", color, 10, 1.7)
    L.partes.append(f'<rect x="{x}" y="{y}" width="6" height="{h}" rx="3" fill="{color}"/>')
    L.texto(x + 18, y + 22, titulo, 14, TINTA, "700")
    L.parrafo(x + 18, y + 40, texto, w - 32, tam, SUAVE)


def _cuadrante(L, x0, y0, cw, ch, celdas, gap=12):
    for cx, cy, t, d, c in celdas:
        x, y = x0 + cx * (cw + gap), y0 + cy * (ch + gap)
        L.caja(x, y, cw, ch, "#ffffff", c, 12, 1.8)
        L.partes.append(f'<rect x="{x}" y="{y}" width="{cw}" height="34" rx="12" fill="{c}"/>')
        L.texto(x + 16, y + 23, t, 14, "#ffffff", "700")
        L.parrafo(x + 16, y + 58, d, cw - 32, 12.5, TINTA)


# ---------------------------------------------------------------- 037
def autoconocimiento() -> str:
    L = Lienzo("Lo que sé de mí y lo que otros ven de mí",
               "Cuadrante de conocimiento de uno mismo: lo que sé y los demás ven, lo que solo yo sé, lo que solo los demás ven "
               "(punto ciego) y lo que nadie ve todavía, con la práctica que reduce cada zona de desconocimiento.", 580, "037")
    L.cabecera("MARCO", "Clase 037 · Verse con exactitud", VERDE, "Goleman (1996) · Stone & Heen (2014)")
    x0, y0, cw, ch = 150, 100, 330, 168
    L.texto(x0 + cw / 2, 92, "LO QUE YO SÉ DE MÍ", 11.5, SUAVE, "700", "middle", 'letter-spacing="1.2"')
    L.texto(x0 + cw + 12 + cw / 2, 92, "LO QUE NO SÉ DE MÍ", 11.5, SUAVE, "700", "middle", 'letter-spacing="1.2"')
    L.partes.append(f'<text transform="translate(116,{y0 + ch / 2}) rotate(-90)" font-size="11.5" font-weight="700" fill="{SUAVE}" text-anchor="middle" letter-spacing="1.2">LO QUE LOS DEMÁS VEN</text>')
    L.partes.append(f'<text transform="translate(116,{y0 + ch + 12 + ch / 2}) rotate(-90)" font-size="11.5" font-weight="700" fill="{SUAVE}" text-anchor="middle" letter-spacing="1.2">LO QUE NO VEN</text>')
    _cuadrante(L, x0, y0, cw, ch, [
        (0, 0, "Visible y conocido", "Lo que sabes de ti y los demás confirman. Es la base de la credibilidad.", VERDE),
        (1, 0, "Punto ciego", "Lo que otros ven y tú no. Solo se reduce pidiendo feedback concreto.", ROJO),
        (0, 1, "Reservado", "Lo que sabes y no muestras. Decide qué compartir para que te conozcan.", AZUL),
        (1, 1, "Aún desconocido", "Ni tú ni otros lo ven. Aparece con experiencias nuevas.", GRIS)])
    L.caja(28, 478, ANCHO - 56, 62, PAPEL, BORDE, 10, 1)
    L.parrafo(44, 500, "Autoconciencia, en el modelo de Goleman, es reconocer una emoción mientras ocurre, evaluarse con exactitud y confiar en las "
              "propias capacidades. La exactitud necesita datos de otros: la sola introspección no basta.", ANCHO - 90, 12.5, TINTA, "600")
    L.pie(566, "El cuadrante es una herramienta de trabajo de la clase; Goleman y Stone y Heen describen los conceptos, no este esquema.")
    return L.svg()


# ---------------------------------------------------------------- 038
def proceso_de_regulacion() -> str:
    L = Lienzo("Cinco puntos donde se puede regular una emoción",
               "Línea de tiempo de una emoción con cinco familias de estrategias según Gross: elegir la situación, modificarla, "
               "dirigir la atención, reinterpretar y modular la respuesta; las primeras actúan antes de que la emoción se genere.", 600, "038")
    L.cabecera("MARCO", "Clase 038 · Regular a tiempo, no solo contenerse", VERDE, "Gross (1998)")
    L.partes.append(f'<path d="M40,150 H{ANCHO - 40}" stroke="{GRIS}" stroke-width="3" marker-end="url(#p-038)"/>')
    L.texto(40, 130, "ANTES de que la emoción se genere", 11.5, VERDE, "700")
    L.texto(ANCHO - 40, 130, "DESPUÉS: la emoción ya está en marcha", 11.5, ROJO, "700", "end")
    pasos = [
        ("1", "Elegir la situación", "Acercarte o evitar lo que sabes que te desborda: preparar una reunión, no responder de noche.", VERDE),
        ("2", "Modificar la situación", "Cambiar lo que se puede: dividir la tarea, pedir más tiempo, cambiar el lugar.", VERDE),
        ("3", "Dirigir la atención", "Mover el foco: a la tarea, a otro aspecto, a una pausa de respiración.", AZUL),
        ("4", "Reinterpretar", "Cambiar el significado: «no me ataca, necesita datos». Cambia la emoción desde su origen.", AZUL),
        ("5", "Modular la respuesta", "Actuar sobre la expresión: suprimir, pausar. Es lo último y lo más costoso.", ROJO),
    ]
    w, gap = 190, 14
    for i, (n, t, d, c) in enumerate(pasos):
        x = 28 + i * (w + gap)
        L.partes.append(f'<circle cx="{x + w / 2}" cy="150" r="14" fill="{c}"/>')
        L.texto(x + w / 2, 155, n, 13, "#ffffff", "700", "middle")
        L.caja(x, 184, w, 220, "#ffffff", c, 12, 1.7)
        L.texto(x + 14, 212, t, 14, TINTA, "700")
        L.parrafo(x + 14, 234, d, w - 28, 12.5, SUAVE)
    L.caja(28, 424, 500, 110, "#ffffff", VERDE, 12, 1.8)
    L.texto(46, 448, "LO QUE SUGIERE LA REVISIÓN", 11.5, VERDE, "700", "start", 'letter-spacing="1.2"')
    L.parrafo(46, 468, "Las estrategias que actúan antes (reinterpretar) cambian la experiencia y la conducta; suprimir la expresión reduce lo que se ve, "
              "pero no necesariamente lo que se siente, y tiene costos.", 466, 12.5)
    L.caja(548, 424, ANCHO - 576, 110, "#ffffff", AZUL, 12, 1.8)
    L.texto(566, 448, "CÓMO SE USA EN LA CLASE", 11.5, AZUL, "700", "start", 'letter-spacing="1.2"')
    L.parrafo(566, 468, "Antes de una situación de presión, decide en cuál de los cinco puntos intervendrás y qué harás.", ANCHO - 612, 12.5)
    L.pie(570, "El modelo de Gross es una revisión teórica; los efectos dependen de la persona y del contexto.")
    return L.svg()


# ---------------------------------------------------------------- 039
def candor() -> str:
    L = Lienzo("Interesarse por la persona y desafiarla directamente",
               "Cuadrante de dos ejes, interesarse personalmente y desafiar de forma directa, con cuatro posturas: franqueza radical, "
               "empatía ruinosa, agresión odiosa e insinceridad manipuladora.", 580, "039")
    L.cabecera("MARCO", "Clase 039 · Empatía sin perder exigencia", VERDE, "Scott (2017) · Goleman (1996)")
    x0, y0, cw, ch = 140, 96, 330, 170
    L.texto(x0 + cw / 2, 86, "PREOCUPARSE POR LA PERSONA:  poco", 11.5, SUAVE, "700", "middle")
    L.texto(x0 + cw + 12 + cw / 2, 86, "mucho", 11.5, SUAVE, "700", "middle")
    L.partes.append(f'<text transform="translate(116,{y0 + ch / 2}) rotate(-90)" font-size="11.5" font-weight="700" fill="{SUAVE}" text-anchor="middle">DESAFIAR: mucho</text>')
    L.partes.append(f'<text transform="translate(116,{y0 + ch + 12 + ch / 2}) rotate(-90)" font-size="11.5" font-weight="700" fill="{SUAVE}" text-anchor="middle">DESAFIAR: poco</text>')
    _cuadrante(L, x0, y0, cw, ch, [
        (0, 0, "Agresión odiosa", "Dice lo directo sin importarle la persona: «esto es un desastre».", NARANJA),
        (1, 0, "Franqueza radical", "Dice lo difícil porque le importa: «esto no está a tu nivel; te muestro por qué».", VERDE),
        (0, 1, "Insinceridad manipuladora", "Ni se involucra ni dice lo que piensa: halaga o calla.", GRIS),
        (1, 1, "Empatía ruinosa", "Cuida tanto la relación que evita decir lo que ayudaría.", ROJO)])
    xr = 700
    L.texto(xr + 140, 480, "", 1)
    L.caja(28, 478, ANCHO - 56, 62, PAPEL, BORDE, 10, 1)
    L.parrafo(44, 500, "Goleman describe la empatía como percibir y comprender las emociones de otros; la exigencia viene de los estándares. "
              "Ambas se necesitan: la empatía sin estándar no ayuda, y el estándar sin empatía no se escucha.", ANCHO - 90, 12.5, TINTA, "600")
    L.pie(566, "El cuadrante es un marco práctico de la autora, no el resultado de una medición; sirve para revisar cómo se da un mensaje difícil.")
    return L.svg()


# ---------------------------------------------------------------- 040
def motivacion() -> str:
    L = Lienzo("Tres necesidades y un continuo de motivación",
               "Autonomía, competencia y vínculo sostienen la motivación según la teoría de la autodeterminación; "
               "el continuo va de la motivación controlada a la intrínseca.", 580, "040")
    L.cabecera("MARCO", "Clase 040 · Qué mueve a las personas a hacer bien su trabajo", VERDE, "Ryan & Deci (2000) · Amabile & Kramer (2011)")
    L.texto(28, 88, "TRES NECESIDADES PSICOLÓGICAS BÁSICAS", 11.5, SUAVE, "700", "start", 'letter-spacing="1.4"')
    y = 104
    for t, d, c in [("Autonomía", "Sentir que la propia acción es elegida, no impuesta.", AZUL),
                    ("Competencia", "Sentirse eficaz: avanzar y dominar lo que se hace.", VERDE),
                    ("Vínculo", "Sentirse conectado y valorado por las personas con quienes se trabaja.", NARANJA)]:
        _tarjeta(L, 28, y, 380, 96, t, d, c)
        y += 108
    L.texto(440, 88, "EL CONTINUO DE LA MOTIVACIÓN", 11.5, SUAVE, "700", "start", 'letter-spacing="1.4"')
    pasos = [("Sin motivación", GRIS), ("Externa", ROJO), ("Introyectada", NARANJA), ("Identificada", AZUL), ("Intrínseca", VERDE)]
    h = 56
    for i, (t, c) in enumerate(pasos):
        yy = 104 + i * 66
        L.caja(440, yy, 570 - i * 0, h, "#ffffff", c, 10, 1.6)
        L.partes.append(f'<rect x="440" y="{yy}" width="{120 + i * 112}" height="{h}" rx="10" fill="{c}" fill-opacity="0.2"/>')
        L.texto(456, yy + 33, t, 14, TINTA, "700")
    L.flecha(1000, 98, 1000, 440, GRIS, 2)
    L.texto(1004, 270, "más", 10.5, SUAVE, "600"); L.texto(1004, 283, "autónoma", 10.5, SUAVE, "600")
    L.caja(28, 440, 380, 98, PAPEL, BORDE, 10, 1)
    L.parrafo(44, 462, "Progreso en un trabajo con sentido: Amabile y Kramer hallaron que los pequeños avances percibidos sostienen la motivación diaria.", 350, 12.5, TINTA, "600")
    L.caja(440, 440, ANCHO - 468, 98, PAPEL, BORDE, 10, 1)
    L.parrafo(456, 462, "Más a la derecha, la persona hace lo que hace porque lo valora; a la izquierda, por presión, recompensa o evitación de culpa.", ANCHO - 500, 12.5, TINTA, "600")
    L.pie(566, "Es una teoría de la motivación con amplio respaldo experimental; los incentivos externos no son «malos», pero pueden desplazar la motivación propia.")
    return L.svg()


# ---------------------------------------------------------------- 041
def trayectorias() -> str:
    L = Lienzo("Resiliencia y recuperación son trayectorias distintas",
               "Tras un evento adverso, algunas personas mantienen un funcionamiento estable (resiliencia), otras caen y vuelven "
               "(recuperación) y otras se mantienen deterioradas (crónica).", 580, "041")
    L.cabecera("MARCO", "Clase 041 · Resiliencia: lo común, no lo excepcional", VERDE, "Bonanno (2004) · Masten (2001)")
    x0, y0, w, h = 60, 96, 600, 330
    L.partes.append(f'<path d="M{x0},{y0} V{y0 + h} H{x0 + w}" stroke="{GRIS}" stroke-width="2" fill="none"/>')
    L.texto(x0 - 14, y0 + 8, "funcionamiento", 11, SUAVE, "600", "end")
    L.texto(x0 + w, y0 + h + 22, "tiempo", 11, SUAVE, "600", "end")
    ev = x0 + 150
    L.partes.append(f'<path d="M{ev},{y0} V{y0 + h}" stroke="{ROJO}" stroke-width="1.6" stroke-dasharray="6 5"/>')
    L.texto(ev + 6, y0 + 14, "evento adverso", 11.5, ROJO, "700")
    yb = y0 + 90
    L.partes.append(f'<path d="M{x0},{yb} H{ev} Q{ev + 40},{yb + 22} {ev + 90},{yb + 6} T{x0 + w},{yb}" stroke="{VERDE}" stroke-width="3.5" fill="none"/>')
    L.partes.append(f'<path d="M{x0},{yb} H{ev} Q{ev + 30},{yb + 150} {ev + 150},{yb + 130} T{x0 + w},{yb + 12}" stroke="{AZUL}" stroke-width="3.5" fill="none"/>')
    L.partes.append(f'<path d="M{x0},{yb} H{ev} Q{ev + 30},{yb + 150} {ev + 150},{yb + 190} T{x0 + w},{yb + 175}" stroke="{ROJO}" stroke-width="3.5" fill="none"/>')
    L.texto(x0 + w - 4, yb - 8, "Resiliencia", 12.5, VERDE, "700", "end")
    L.texto(x0 + w - 4, yb + 30, "Recuperación", 12.5, AZUL, "700", "end")
    L.texto(x0 + w - 4, yb + 160, "Deterioro crónico", 12.5, ROJO, "700", "end")
    xr = 700
    y = 98
    for t, d, c in [("Resiliencia", "Funcionamiento relativamente estable; es más común de lo que se supone.", VERDE),
                    ("Recuperación", "Un período de disfunción y luego el retorno gradual.", AZUL),
                    ("Procesos ordinarios", "Para Masten surge de sistemas adaptativos comunes: relaciones, capacidad de resolver, sentido.", VIOLETA)]:
        _tarjeta(L, xr, y, ANCHO - xr - 28, 104, t, d, c)
        y += 116
    L.caja(xr, 446, ANCHO - xr - 28, 80, PAPEL, BORDE, 10, 1)
    L.parrafo(xr + 14, 468, "Implicancia: no tratar como patología la reacción esperable, ni exigir que nadie «se sobreponga».", ANCHO - xr - 56, 12.5, TINTA, "600")
    L.pie(566, "Las trayectorias son esquemáticas; los estudios las describen en poblaciones, no predicen a una persona.")
    return L.svg()


# ---------------------------------------------------------------- 042
def seguridad_y_estandar() -> str:
    L = Lienzo("Seguridad psicológica y exigencia son dos ejes, no una disyuntiva",
               "Cuadrante según el nivel de seguridad psicológica y el de estándares: zona de aprendizaje, de ansiedad, de confort y de apatía; "
               "y la cadena de la seguridad al desempeño.", 600, "042")
    L.cabecera("MARCO", "Clase 042 · Poder decir lo que se piensa y exigir resultados", VERDE, "Edmondson (1999, 2018)")
    x0, y0, cw, ch = 120, 100, 280, 150
    L.texto(x0 + cw / 2, 90, "SEGURIDAD PSICOLÓGICA:  baja", 11.5, SUAVE, "700", "middle")
    L.texto(x0 + cw + 12 + cw / 2, 90, "alta", 11.5, SUAVE, "700", "middle")
    L.partes.append(f'<text transform="translate(98,{y0 + ch / 2}) rotate(-90)" font-size="11.5" font-weight="700" fill="{SUAVE}" text-anchor="middle">ESTÁNDARES: altos</text>')
    L.partes.append(f'<text transform="translate(98,{y0 + ch + 12 + ch / 2}) rotate(-90)" font-size="11.5" font-weight="700" fill="{SUAVE}" text-anchor="middle">ESTÁNDARES: bajos</text>')
    _cuadrante(L, x0, y0, cw, ch, [
        (0, 0, "Zona de ansiedad", "Se exige mucho y es peligroso hablar: se oculta el error.", ROJO),
        (1, 0, "Zona de aprendizaje", "Se exige y se puede decir la verdad: se aprende del error.", VERDE),
        (0, 1, "Zona de apatía", "Poca exigencia y poca seguridad: se hace lo mínimo.", GRIS),
        (1, 1, "Zona de confort", "Hay confianza, pero sin reto: se cuida el clima y no el resultado.", AZUL)])
    xr = 740
    L.texto(xr, 90, "LA CADENA", 11.5, SUAVE, "700", "start", 'letter-spacing="1.4"')
    cad = [("Conducta del líder", "Pide opiniones, admite errores.", VIOLETA), ("Seguridad psicológica", "Creencia compartida de que hablar es seguro.", VERDE),
           ("Conductas de aprendizaje", "Preguntar, pedir ayuda, probar, discutir errores.", AZUL), ("Desempeño", "Mediado por el aprendizaje del equipo.", NARANJA)]
    y = 104
    for i, (t, d, c) in enumerate(cad):
        L.caja(xr, y, ANCHO - xr - 28, 74, "#ffffff", c, 10, 1.7)
        L.texto(xr + 14, y + 24, t, 13.5, TINTA, "700")
        L.parrafo(xr + 14, y + 42, d, ANCHO - xr - 56, 11.5, SUAVE)
        if i < 3:
            L.flecha(xr + (ANCHO - xr - 28) / 2, y + 76, xr + (ANCHO - xr - 28) / 2, y + 88, GRIS, 1.8)
        y += 90
    L.caja(28, 440, 680, 86, PAPEL, BORDE, 10, 1)
    L.parrafo(44, 462, "Seguridad psicológica no es amabilidad ni bajar el estándar: es la creencia compartida de que el equipo es seguro para asumir riesgos "
              "interpersonales como preguntar, admitir un error o discrepar.", 650, 12.5, TINTA, "600")
    L.pie(566, "El efecto sobre el desempeño depende de la tarea y del contexto; la evidencia más fuerte es de equipos de trabajo concretos.")
    return L.svg()


# ---------------------------------------------------------------- 043
def tecnico_o_adaptativo() -> str:
    L = Lienzo("Problema técnico y problema adaptativo",
               "Dos tipos de problema según si existe una respuesta conocida: los técnicos se resuelven con experticia y los "
               "adaptativos exigen que las personas aprendan y cambien valores, hábitos o lealtades.", 580, "043")
    L.cabecera("MARCO", "Clase 043 · Qué tipo de problema es", VERDE, "Heifetz (1994) · Heifetz, Grashow & Linsky (2009)")
    cols = [("PROBLEMA TÉCNICO", "Se conoce la definición y la solución", AZUL, [
                ("Quién trabaja", "Quien tiene la experticia."), ("Qué se pide", "Aplicar el conocimiento existente."),
                ("Qué se pierde", "Poco: el cambio es técnico."), ("Ejemplo", "Una falla de un sistema con procedimiento conocido.")]),
            ("PROBLEMA ADAPTATIVO", "Exige aprender y cambiar", ROJO, [
                ("Quién trabaja", "Las personas con el problema."), ("Qué se pide", "Revisar valores, hábitos y lealtades."),
                ("Qué se pierde", "Algo que se valora: hay resistencia."), ("Ejemplo", "Pasar de un modelo de ventas por relación a uno por datos.")])]
    w = 480
    for i, (t, sub, c, filas) in enumerate(cols):
        x = 28 + i * (w + 24)
        L.caja(x, 92, w, 360, "#ffffff", c, 12, 1.8)
        L.partes.append(f'<path d="M{x},142 V104 a12,12 0 0 1 12,-12 H{x + w - 12} a12,12 0 0 1 12,12 V142 Z" fill="{c}"/>')
        L.texto(x + 18, 116, t, 13, "#ffffff", "800", "start", 'letter-spacing="1.2"')
        L.texto(x + 18, 134, sub, 12, "#ffffff", "400")
        y = 166
        for k, v in filas:
            L.texto(x + 18, y + 14, k, 11.5, SUAVE, "700")
            L.parrafo(x + 18, y + 32, v, w - 36, 13)
            y += 70
    L.caja(28, 468, ANCHO - 56, 62, PAPEL, BORDE, 10, 1)
    L.parrafo(44, 490, "El error frecuente es tratar un problema adaptativo con una solución técnica: se «arregla» el síntoma y reaparece. "
              "Heifetz propone alternar entre la acción y el balcón, desde donde se observa el patrón.", ANCHO - 90, 12.5, TINTA, "600")
    L.pie(566, "La mayoría de los problemas reales mezcla ambos componentes: se separan para decidir qué parte exige aprendizaje.")
    return L.svg()


# ---------------------------------------------------------------- 044
def construccion_de_sentido() -> str:
    L = Lienzo("Dar sentido a una situación incierta mientras se actúa",
               "Ciclo de construcción de sentido: notar señales, construir un relato plausible, actuar de forma acotada y corregir; "
               "con las siete propiedades que describe Weick.", 590, "044")
    L.cabecera("MARCO", "Clase 044 · Liderar cuando no hay certeza", VERDE, "Weick (1995) · Klein (1999)")
    pasos = [("Notar señales", "Extraer datos del entorno, incluidos los que no encajan.", AZUL),
             ("Construir un relato plausible", "Una explicación suficiente para actuar, no una verdad definitiva.", VIOLETA),
             ("Actuar de forma acotada", "Una acción pequeña y reversible que revele más.", VERDE),
             ("Corregir con lo que se ve", "Revisar el relato con la respuesta del entorno.", NARANJA)]
    w, gap = 232, 24
    for i, (t, d, c) in enumerate(pasos):
        x = 28 + i * (w + gap)
        L.caja(x, 92, w, 130, "#ffffff", c, 12, 1.8)
        L.partes.append(f'<circle cx="{x + 24}" cy="118" r="13" fill="{c}"/>')
        L.texto(x + 24, 123, str(i + 1), 13, "#ffffff", "700", "middle")
        L.texto(x + 46, 123, t, 13.5, TINTA, "700")
        L.parrafo(x + 16, 150, d, w - 32, 12.5, SUAVE)
        if i < 3:
            L.flecha(x + w + 3, 157, x + w + gap - 3, 157, GRIS, 2)
    L.trazo(f"M{28 + 3 * (w + gap) + w / 2},224 V250 H{28 + w / 2} V226", GRIS, 2, extra=f'stroke-dasharray="7 6" marker-end="url(#p-044)"')
    L.texto(ANCHO / 2, 270, "se repite mientras la situación cambia", 11.5, SUAVE, "600", "middle")
    L.texto(28, 306, "LAS SIETE PROPIEDADES DEL SENTIDO (WEICK)", 11.5, SUAVE, "700", "start", 'letter-spacing="1.4"')
    props = [("Identidad", "quién soy al interpretar"), ("Retrospectivo", "se entiende mirando lo ocurrido"), ("Activo", "actuar crea el entorno que se interpreta"),
             ("Social", "se construye con otros"), ("Continuo", "no tiene un final"), ("Señales", "se apoya en indicios concretos"), ("Plausibilidad", "importa más que la exactitud")]
    x, y = 28, 322
    for t, d in props:
        w2 = len(t + d) * 6.5 + 40
        if x + w2 > ANCHO - 28:
            x, y = 28, y + 44
        L.caja(x, y, w2, 34, "#ffffff", AZUL, 17, 1.3)
        L.texto(x + 14, y + 22, t + ":", 12, TINTA, "700")
        L.texto(x + 22 + len(t) * 7.2, y + 22, d, 11.5, SUAVE)
        x += w2 + 10
    L.caja(28, 452, ANCHO - 56, 78, PAPEL, BORDE, 10, 1)
    L.parrafo(44, 474, "Klein describe cómo los expertos deciden bajo presión de tiempo: reconocen un patrón, simulan mentalmente una acción y la ajustan. "
              "Funciona cuando hay experiencia; si no la hay, conviene acción acotada y consulta.", ANCHO - 90, 12.5, TINTA, "600")
    L.pie(566, "No elimina la incertidumbre: la hace manejable. Si la acción no es reversible, se necesita más evidencia antes de actuar.")
    return L.svg()


# ---------------------------------------------------------------- 045
def dilemas() -> str:
    L = Lienzo("Dilemas de «bien contra bien» y tres lentes para decidir",
               "Cuatro tensiones típicas entre valores legítimos y tres criterios de resolución: consecuencias, reglas y cuidado; "
               "al final, una decisión con registro.", 600, "045")
    L.cabecera("MARCO", "Clase 045 · Cuando dos valores correctos chocan", VERDE, "Kidder (2009) · Bazerman & Moore (2013)")
    L.texto(28, 88, "CUATRO TENSIONES", 11.5, SUAVE, "700", "start", 'letter-spacing="1.4"')
    pares = [("Verdad", "Lealtad"), ("Individuo", "Comunidad"), ("Corto plazo", "Largo plazo"), ("Justicia", "Misericordia")]
    for i, (a, b) in enumerate(pares):
        x, y = 28 + (i % 2) * 330, 104 + (i // 2) * 80
        L.caja(x, y, 150, 56, "#ffffff", AZUL, 12, 1.7); L.texto(x + 75, y + 34, a, 14, TINTA, "700", "middle")
        L.caja(x + 168, y, 150, 56, "#ffffff", VERDE, 12, 1.7); L.texto(x + 243, y + 34, b, 14, TINTA, "700", "middle")
        L.partes.append(f'<path d="M{x + 152},{y + 28} H{x + 166}" stroke="{GRIS}" stroke-width="2"/>')
    L.texto(28, 290, "TRES LENTES PARA RESOLVER", 11.5, SUAVE, "700", "start", 'letter-spacing="1.4"')
    lentes = [("Consecuencias", "¿Qué decisión produce el mayor bien para el mayor número?", ROJO),
              ("Reglas", "¿Qué haría yo si mi decisión fuera una regla para todos?", AZUL),
              ("Cuidado", "¿Cómo querría ser tratado si estuviera en el lugar del otro?", VERDE)]
    for i, (t, d, c) in enumerate(lentes):
        _tarjeta(L, 28 + i * 340, 306, 320, 110, t, d, c)
    L.flecha(ANCHO / 2, 420, ANCHO / 2, 440, GRIS, 2)
    L.caja(28, 442, ANCHO - 56, 86, "#ffffff", VIOLETA, 12, 1.8)
    L.texto(46, 466, "DECISIÓN CON REGISTRO", 11.5, VIOLETA, "700", "start", 'letter-spacing="1.2"')
    L.parrafo(46, 486, "Escribe qué valor cedió, por qué y qué harías distinto con otra información. Bazerman y Moore advierten que solemos "
              "subestimar nuestra propia parcialidad: consulta a un tercero independiente.", ANCHO - 100, 12.5)
    L.pie(566, "Los tres criterios simplifican tradiciones filosóficas amplias. Los dilemas de la clase no sustituyen asesoría legal ni normas vigentes.")
    return L.svg()


# ---------------------------------------------------------------- 046
def inmunidad_al_cambio() -> str:
    L = Lienzo("Por qué no cambio aunque quiero: el mapa de inmunidad",
               "Mapa de cuatro columnas: compromiso de mejora, lo que hago o dejo de hacer, compromisos en competencia con su "
               "miedo y gran supuesto; y las etapas del cambio personal.", 600, "046")
    L.cabecera("MARCO", "Clase 046 · Resistencia: lo que protege el statu quo", VERDE, "Kegan & Lahey (2009) · Prochaska & DiClemente (1983)")
    cols = [("1 · Compromiso de mejora", "Delegar más y confiar en mi equipo.", VERDE),
            ("2 · Lo que hago o dejo de hacer", "Reviso todo antes de enviarlo. Reasigno tareas ya delegadas.", AZUL),
            ("3 · Compromisos en competencia", "No quiero que algo salga mal con mi nombre. Miedo: parecer descuidado.", NARANJA),
            ("4 · Gran supuesto", "«Si no superviso, el trabajo bajará de nivel y se notará en mí.»", ROJO)]
    w, gap = 232, 24
    for i, (t, ej, c) in enumerate(cols):
        x = 28 + i * (w + gap)
        L.caja(x, 92, w, 200, "#ffffff", c, 12, 1.8)
        L.partes.append(f'<path d="M{x},130 V104 a12,12 0 0 1 12,-12 H{x + w - 12} a12,12 0 0 1 12,12 V130 Z" fill="{c}"/>')
        L.texto(x + 14, 116, t, 12, "#ffffff", "800")
        L.texto(x + 14, 152, "Ejemplo", 11, SUAVE, "700")
        L.parrafo(x + 14, 170, ej, w - 28, 13)
        if i < 3:
            L.flecha(x + w + 3, 192, x + w + gap - 3, 192, GRIS, 2)
    L.texto(28, 330, "ETAPAS DEL CAMBIO PERSONAL", 11.5, SUAVE, "700", "start", 'letter-spacing="1.4"')
    et = [("Precontemplación", "No ve el problema"), ("Contemplación", "Lo evalúa, aún sin decidir"), ("Preparación", "Planea y prueba"),
          ("Acción", "Cambia la conducta"), ("Mantenimiento", "Sostiene y previene recaídas")]
    w2 = (ANCHO - 56 - 4 * 14) / 5
    for i, (t, d) in enumerate(et):
        x = 28 + i * (w2 + 14)
        L.caja(x, 346, w2, 84, "#ffffff", GRIS, 10, 1.5)
        L.partes.append(f'<rect x="{x}" y="346" width="{w2}" height="8" rx="4" fill="{VERDE}" fill-opacity="{0.25 + i * 0.18}"/>')
        L.texto(x + 12, 378, t, 13, TINTA, "700")
        L.parrafo(x + 12, 396, d, w2 - 24, 11.5, SUAVE)
    L.caja(28, 446, ANCHO - 56, 82, PAPEL, BORDE, 10, 1)
    L.parrafo(44, 468, "Si el gran supuesto parece obvio, se pone a prueba con un experimento pequeño y seguro: delegar una tarea de bajo riesgo y observar qué ocurre. "
              "La resistencia es protección, no pereza.", ANCHO - 90, 12.5, TINTA, "600")
    L.pie(566, "El ejemplo es ilustrativo. Las etapas surgieron del estudio de cambio de conductas de salud y se aplican con cautela al trabajo.")
    return L.svg()


# ---------------------------------------------------------------- 047
def agotamiento_y_recuperacion() -> str:
    L = Lienzo("Agotamiento y recuperación",
               "Las tres dimensiones del burnout, las seis áreas donde el trabajo se desajusta con la persona y las cuatro "
               "experiencias de recuperación fuera del trabajo.", 600, "047")
    L.cabecera("MARCO", "Clase 047 · Sostener el rendimiento sin agotarse", VERDE, "Maslach, Schaufeli & Leiter (2001) · Sonnentag & Fritz (2007)")
    L.texto(28, 88, "BURNOUT: TRES DIMENSIONES", 11.5, SUAVE, "700", "start", 'letter-spacing="1.4"')
    y = 104
    for t, d, c in [("Agotamiento", "Cansancio emocional y físico prolongado.", ROJO), ("Cinismo", "Distancia y actitud negativa hacia el trabajo.", NARANJA),
                    ("Menor eficacia", "Sensación de logro reducido.", GRIS)]:
        _tarjeta(L, 28, y, 330, 82, t, d, c)
        y += 94
    L.texto(380, 88, "SEIS ÁREAS DE DESAJUSTE", 11.5, SUAVE, "700", "start", 'letter-spacing="1.4"')
    areas = ["Carga de trabajo", "Control", "Reconocimiento", "Comunidad", "Justicia", "Valores"]
    for i, a in enumerate(areas):
        x, yy = 380 + (i % 2) * 150, 104 + (i // 2) * 94
        L.caja(x, yy, 140, 82, "#ffffff", AZUL, 10, 1.6)
        L.texto(x + 70, yy + 48, a, 13, TINTA, "700", "middle")
    L.texto(700, 88, "CUATRO EXPERIENCIAS DE RECUPERACIÓN", 11.5, SUAVE, "700", "start", 'letter-spacing="1.4"')
    y = 104
    for t, d, c in [("Desconexión psicológica", "No pensar en el trabajo fuera de él.", VERDE), ("Relajación", "Reducir la activación.", AZUL),
                    ("Dominio", "Aprender o lograr algo fuera del trabajo.", VIOLETA), ("Control del tiempo libre", "Decidir cómo usarlo.", NARANJA)]:
        L.caja(700, y, ANCHO - 728, 66, "#ffffff", c, 10, 1.6)
        L.texto(716, y + 26, t, 13, TINTA, "700")
        L.texto(716, y + 46, d, 11.5, SUAVE)
        y += 74
    L.caja(28, 410, 650, 116, PAPEL, BORDE, 10, 1)
    L.parrafo(44, 434, "El agotamiento suele ser un problema del trabajo y de la persona. Por eso la solución no es solo individual: se revisan carga, control, "
              "reconocimiento y valores, y se protege el descanso con reglas del equipo.", 610, 12.5, TINTA, "600")
    L.pie(566, "Burnout no es un diagnóstico clínico en todos los sistemas y esta clase no reemplaza atención profesional de salud.")
    return L.svg()


# ---------------------------------------------------------------- 048
def crisis_humana() -> str:
    L = Lienzo("Las primeras 72 horas de una crisis humana",
               "Tres tramos con las decisiones y el criterio que gobierna cada uno: proteger y reconocer, abrir diálogo con hechos "
               "y cuidar las cuatro formas de justicia, y cerrar con acuerdos y seguimiento.", 600, "048")
    L.cabecera("MARCO", "Clase 048 · Liderar cuando el problema son las personas", VERDE, "Coombs (2007) · Colquitt et al. (2001) · Heifetz et al. (2009)")
    tramos = [("0–6 HORAS", "Proteger y reconocer", ROJO,
               ["Seguridad de las personas primero.", "Reconocer el reclamo sin aceptar ni rechazar su contenido.", "Un solo responsable y un registro de hechos."],
               "Coombs: informar e instruir antes de cuidar la imagen."),
              ("6–48 HORAS", "Dialogar con hechos", NARANJA,
               ["Interlocutores definidos y mesa de diálogo.", "Separar lo negociable de la obligación legal.", "Un mismo mensaje hacia dentro y hacia fuera."],
               "Colquitt: resultado, proceso, trato y explicación."),
              ("48–72 HORAS", "Acordar y seguir", VERDE,
               ["Compromisos con responsable y fecha.", "Sin represalias contra quienes reclamaron.", "Revisión sin culpas y fecha de seguimiento."],
               "Heifetz: ver desde el balcón qué cambio de fondo se pide.")]
    w, gap = 320, 20
    for i, (h, t, c, accs, marco) in enumerate(tramos):
        x = 28 + i * (w + gap)
        L.caja(x, 92, w, 396, "#ffffff", c, 12, 1.8)
        L.partes.append(f'<path d="M{x},138 V104 a12,12 0 0 1 12,-12 H{x + w - 12} a12,12 0 0 1 12,12 V138 Z" fill="{c}"/>')
        L.texto(x + 16, 112, h, 11.5, "#ffffff", "700", "start", 'letter-spacing="1.2"')
        L.texto(x + 16, 130, t, 15, "#ffffff", "800")
        y = 162
        for a in accs:
            L.partes.append(f'<circle cx="{x + 22}" cy="{y + 6}" r="4" fill="{c}"/>')
            y = L.parrafo(x + 36, y + 11, a, w - 56, 13) + 8
        L.caja(x + 14, 404, w - 28, 68, PAPEL, BORDE, 10, 1)
        L.parrafo(x + 26, 424, marco, w - 52, 12, TINTA, "600")
        if i < 2:
            L.flecha(x + w + 2, 290, x + w + gap - 2, 290, GRIS, 2)
    L.caja(28, 500, ANCHO - 56, 40, PAPEL, BORDE, 10, 1)
    L.texto(44, 525, "Un conflicto público con trabajadores se mide por cómo se trata a las personas, no solo por cómo se cierra.", 13, TINTA, "600")
    L.pie(574, "Los tramos son una guía docente; la norma laboral aplicable se verifica con asesoría y no la reemplaza esta clase.")
    return L.svg()


DIAGRAMAS = {
    37: autoconocimiento, 38: proceso_de_regulacion, 39: candor, 40: motivacion, 41: trayectorias, 42: seguridad_y_estandar,
    43: tecnico_o_adaptativo, 44: construccion_de_sentido, 45: dilemas, 46: inmunidad_al_cambio, 47: agotamiento_y_recuperacion,
    48: crisis_humana,
}
