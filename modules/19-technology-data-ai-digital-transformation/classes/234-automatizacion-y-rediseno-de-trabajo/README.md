# Clase 234 — Automatización y rediseño de trabajo

**Parte:** 19 — Tecnología, datos, IA y transformación digital para ejecutivos  
**Nivel:** Etapa 5 — CEO → Transformador digital  
**Duración sugerida:** 150–180 minutos · **Estándar:** deep-class-v2

## 🎯 Propósito

Automatizar cambia trabajo, roles y controles; el mayor valor suele venir de rediseñar workflow, no de sustituir cada tarea 1:1. Task decomposition, exception handling y human judgment ayudan a decidir qué automatizar, augmentar o mantener humano.

La salida de esta parte es **gobernar tecnología, datos e IA como capacidades económicas y organizacionales**. En esta clase, esa progresión se concreta al exigir que cada afirmación sobre **automatización y rediseño de trabajo** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

## 📚 Resultados de aprendizaje

Al finalizar podrás:

1. **Distinguir** `task decomposition`, `augmentation`, `straight-through processing`, `exception handling`, `job redesign` mediante observables, no por memoria verbal.
2. **Explicar** por qué esas distinciones cambian una decisión de ceo → transformador digital.
3. **Aplicar** la secuencia **1. mapear workflow end-to-end → 2. clasificar tareas por repetición judgment y risk → 3. diseñar target workflow y exceptions → 4. redefinir roles y controles → 5. pilotear y medir productivity y quality** conservando supuestos, alternativas y trazabilidad.
4. **Interpretar** touch time, automation rate, exception rate sin confundir señal, explicación y causalidad.
5. **Resolver** el caso ejecutivo con al menos dos opciones plausibles y un criterio explícito de stop/revisión.
6. **Contrastar** dos obras de referencia y explicar dónde sus lentes son complementarias o entran en tensión.

## 🧭 Agenda

| Tramo | Evidencia de aprendizaje |
|---|---|
| 0–20 min | Recuperación: define task decomposition y augmentation sin mirar la tabla; corrige con la fuente. |
| 20–70 min | Lectura guiada de conceptos + contraste de dos referencias. |
| 70–115 min | Ejemplo trabajado con touch time y trazabilidad de supuestos. |
| 115–155 min | Caso ejecutivo: dos alternativas, trade-offs y decisión provisional. |
| 155–180 min | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar comprensión |
|---|---|---|
| **task decomposition** | descomposición del trabajo en actividades con distinto potencial de automatización | Distingue un hecho compatible y otro que lo refute. |
| **augmentation** | uso de tecnología para aumentar capacidad humana | Distingue un hecho compatible y otro que lo refute. |
| **straight-through processing** | flujo automatizado sin intervención manual | Distingue un hecho compatible y otro que lo refute. |
| **exception handling** | proceso para casos fuera de reglas | Distingue un hecho compatible y otro que lo refute. |
| **job redesign** | reconfiguración de responsabilidades después de automatización | Distingue un hecho compatible y otro que lo refute. |

## 🧠 Modelo mental

```text
1. mapear workflow end-to-end → 2. clasificar tareas por repetición judgment y risk → 3. diseñar target workflow y exceptions → 4. redefinir roles y controles → 5. pilotear y medir productivity y quality
```

La secuencia nace del problema de esta clase: **Automatizar cambia trabajo, roles y controles; el mayor valor suele venir de rediseñar workflow, no de sustituir cada tarea 1:1. Task decomposition, exception handling y human judgment ayudan a decidir qué automatizar, augmentar o mantener humano.** El método es útil mientras las condiciones permitan observar las señales requeridas. No elimina incertidumbre; la hace visible y obliga a decidir proporcionalmente a la evidencia. Límite principal: **Automatización de alto riesgo necesita controles y fallback. No uses capacidad técnica como justificación para eliminar juicio humano donde daño potencial es material.**

## 📖 Desarrollo

### 1. task decomposition: mecanismo central

**task decomposition** se entiende aquí como **descomposición del trabajo en actividades con distinto potencial de automatización**. Esta es la pieza causal o estructural desde la que se inicia **automatización y rediseño de trabajo**: antes de mapear workflow end-to-end, el gerente debe poder señalar qué cambia en el sistema si el concepto está presente y qué debería observar si no lo está. Una definición que no produce predicciones observables todavía es demasiado vaga para dirigir.

La lectura rectora de este bloque es Marco Iansiti & Karim R. Lakhani — *Competing in the Age of AI*. Su aporte se usa para examinar **modelo operativo AI-first, escala digital, redes y arquitectura de decisión**. Aplica esa lente al caso sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **touch time**; regístrala con periodo, unidad, población y baseline.

Relaciona el mecanismo con **augmentation**. Si ambos cambian juntos, no concluyas causalidad automáticamente: identifica una tercera variable o mecanismo alternativo que también pueda explicar el patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. augmentation: frontera conceptual y error de clasificación

**Definición operacional:** uso de tecnología para aumentar capacidad humana. Su valor está en distinguirlo de **task decomposition** y **straight-through processing**. En una decisión real, clasificar una situación en la categoría equivocada cambia la intervención: puedes asignar autoridad donde faltaba información, medir un output cuando debías observar un proceso o tratar una restricción como si fuera una preferencia.

Contrasta el problema con Thomas H. Davenport & Nitin Mittal — *All-In on AI*, que aporta una mirada sobre **casos empresariales, estrategia y organización para inteligencia artificial**. Formula dos mini-casos: uno que sí satisface la definición de **augmentation** y otro que solo se parece superficialmente. Luego pregunta qué señal distinguiría ambos; para esta clase, **automation rate** es una candidata, pero debe combinarse con evidencia cualitativa o documental cuando el fenómeno no sea directamente medible.

Antes de clasificar tareas por repetición judgment y risk, registra explícitamente qué decisión sería errónea si esta frontera conceptual se ignora. Esa frase convierte el vocabulario en criterio gerencial.

### 3. straight-through processing: operacionalización y medición

**straight-through processing** significa **flujo automatizado sin intervención manual**. El problema ya no es definirlo, sino **operacionalizarlo**: qué contar, durante qué ventana, con qué denominador, contra qué baseline y con qué segmentación. Una métrica útil conserva suficiente contexto para no confundir mejora local con mejora del sistema.

Martin Kleppmann — *Designing Data-Intensive Applications* orienta este bloque mediante **perspectiva de Arquitectura tecnológica aplicada al problema de la clase**. Usa esa perspectiva para diseñar una ficha de medición: `señal → fórmula/criterio → fuente → frecuencia → owner → interpretación permitida → interpretación prohibida`. La señal asignada es **exception rate**. Si no existe un dato confiable, la salida correcta no es inventar precisión: diseña el mecanismo de captura y declara la incertidumbre.

Al llegar a diseñar target workflow y exceptions, compara tendencia, distribución y casos atípicos. Pregunta además si el indicador es *leading* o *lagging* y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; nunca convertirse en el objetivo que reemplaza al fenómeno.

### 4. exception handling: trade-offs y efectos de segundo orden

**Definición:** proceso para casos fuera de reglas. Este concepto obliga a abandonar la idea de que **automatización y rediseño de trabajo** tiene una solución gratuita. Toda intervención consume autonomía, tiempo, caja, capacidad, atención, reputación o tolerancia al riesgo. Por eso, antes de redefinir roles y controles, se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

NIST — *Cybersecurity Framework (CSF) 2.0* aporta una lente sobre **gobierno, identificación, protección, detección, respuesta y recuperación en ciberseguridad**. Úsala para construir una matriz `beneficio / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **quality** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la necesidad de observar efectos laterales fuera del KPI principal.

Haz un *pre-mortem* de **automatización y rediseño de trabajo**: supone que la opción recomendada fracasó seis meses después y enumera tres mecanismos que podrían explicarlo. Al menos uno debe provenir de un efecto de segundo orden asociado a **exception handling** y otro de una hipótesis del caso que nunca fue validada.

### 5. job redesign: gobernanza, límites e integración

**job redesign** se define como **reconfiguración de responsabilidades después de automatización** y cierra el circuito porque traduce análisis en responsabilidad. La pregunta ejecutiva es quién decide, quién ejecuta, quién debe ser consultado, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar.

George Westerman, Didier Bonnet & Andrew McAfee — *Leading Digital* se utiliza para estudiar **transformación digital desde capacidades de liderazgo y capacidades digitales** y contrastar la recomendación final. Al ejecutar pilotear y medir productivity y quality, deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento. Esa trazabilidad protege contra el sesgo retrospectivo y mejora las revisiones posteriores.

La frontera de esta clase es explícita: **Automatización de alto riesgo necesita controles y fallback. No uses capacidad técnica como justificación para eliminar juicio humano donde daño potencial es material.**. Conviértela en una regla operativa: `si ocurre X → no aplicar automáticamente → consultar/escalar/revalidar`. Integrar **task decomposition**, **augmentation**, **straight-through processing**, **exception handling** y **job redesign** significa poder explicar qué parte del diagnóstico sostiene la decisión y cuál sigue siendo una apuesta.

### 6. Integración: de conceptos a una decisión defendible

La síntesis de **automatización y rediseño de trabajo** no consiste en sumar cinco definiciones. Empieza por **task decomposition**, contrasta **augmentation** con **straight-through processing**, incorpora **exception handling** como restricción o mecanismo y usa **job redesign** para cerrar el ciclo. Si el análisis no puede explicar cuál de esas piezas cambió la recomendación, todavía no hay comprensión transferible.

Aplica ahora la secuencia **1. mapear workflow end-to-end → 2. clasificar tareas por repetición judgment y risk → 3. diseñar target workflow y exceptions → 4. redefinir roles y controles → 5. pilotear y medir productivity y quality**. Para cada paso conserva tres columnas: evidencia utilizada, alternativa descartada y razón. Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado y evita reescribir la historia después de conocer el desenlace.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla señala el lente que debes buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Marco Iansiti & Karim R. Lakhani — *Competing in the Age of AI* | modelo operativo AI-first, escala digital, redes y arquitectura de decisión | ¿Qué supuesto de **automatización y rediseño de trabajo** ayuda a desafiar? |
| Thomas H. Davenport & Nitin Mittal — *All-In on AI* | casos empresariales, estrategia y organización para inteligencia artificial | ¿Qué supuesto de **automatización y rediseño de trabajo** ayuda a desafiar? |
| Martin Kleppmann — *Designing Data-Intensive Applications* | perspectiva de Arquitectura tecnológica aplicada al problema de la clase | ¿Qué supuesto de **automatización y rediseño de trabajo** ayuda a desafiar? |
| NIST — *Cybersecurity Framework (CSF) 2.0* | gobierno, identificación, protección, detección, respuesta y recuperación en ciberseguridad | ¿Qué supuesto de **automatización y rediseño de trabajo** ayuda a desafiar? |
| George Westerman, Didier Bonnet & Andrew McAfee — *Leading Digital* | transformación digital desde capacidades de liderazgo y capacidades digitales | ¿Qué supuesto de **automatización y rediseño de trabajo** ayuda a desafiar? |

En **automatización y rediseño de trabajo**, la lectura se evalúa por **uso**, no por cantidad de páginas. La nota debe indicar qué tesis de las fuentes modifica tu lectura de **task decomposition**, qué evidencia del caso tensiona esa tesis y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación:** Un equipo automatiza clasificación de facturas, pero cada excepción vuelve por correo a tres personas y genera más retrabajo que antes.

**Paso 1 — mapear workflow end-to-end.** La gerencia escribe primero el supuesto asociado a **task decomposition** y evita convertirlo en hecho. Luego busca **touch time** para contrastarlo en el caso de **automatización y rediseño de trabajo**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 2 — clasificar tareas por repetición judgment y risk.** La gerencia escribe primero el supuesto asociado a **augmentation** y evita convertirlo en hecho. Luego busca **automation rate** para contrastarlo en el caso de **automatización y rediseño de trabajo**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 3 — diseñar target workflow y exceptions.** La gerencia escribe primero el supuesto asociado a **straight-through processing** y evita convertirlo en hecho. Luego busca **exception rate** para contrastarlo en el caso de **automatización y rediseño de trabajo**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 4 — redefinir roles y controles.** La gerencia escribe primero el supuesto asociado a **exception handling** y evita convertirlo en hecho. Luego busca **quality** para contrastarlo en el caso de **automatización y rediseño de trabajo**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 5 — pilotear y medir productivity y quality.** La gerencia escribe primero el supuesto asociado a **job redesign** y evita convertirlo en hecho. Luego busca **capacity released** para contrastarlo en el caso de **automatización y rediseño de trabajo**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Síntesis del caso.** La recomendación debe terminar con responsable, fecha, evidencia de éxito y señal de stop. En **automatización y rediseño de trabajo**, omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo |
|---|---|---|---|
| **task decomposition** | descomposición del trabajo en actividades con distinto potencial de automatización | Cuando touch time es observable y accionable. | Sobrerreaccionar a una señal parcial. |
| **augmentation** | uso de tecnología para aumentar capacidad humana | Cuando la primera explicación no distingue mecanismo o responsabilidad. | Convertir el concepto en etiqueta. |
| **Experimento/revisión** | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar eternamente y no decidir. |
| **Escalamiento** | Elevar autoridad o especialidad | Cuando hay derechos, capital material, regulación o irreversibilidad. | Delegar hacia arriba lo que sí corresponde decidir. |

**Frontera de aplicación:** Automatización de alto riesgo necesita controles y fallback. No uses capacidad técnica como justificación para eliminar juicio humano donde daño potencial es material.

## 🪜 De profesional a owner

| Nivel | Responsabilidad sobre automatización y rediseño de trabajo |
|---|---|
| **Profesional** | usa **automatización y rediseño de trabajo** para mejorar una contribución propia y explicar sus supuestos con evidencia. |
| **Jefe / Team Lead** | aplica **task decomposition** y **augmentation** para coordinar personas sin sustituir conversación por métricas. |
| **Manager / Gerente** | conecta touch time con capacidad, presupuesto, dependencias y riesgo interáreas. |
| **CEO / Director** | decide si automatización y rediseño de trabajo cambia estrategia, economía o riesgo de empresa y qué debe llegar al comité o directorio. |
| **Founder / Owner** | pregunta si la solución de automatización y rediseño de trabajo reduce dependencia del fundador, preserva caja y puede operar como sistema repetible. |

El cambio de nivel en **automatización y rediseño de trabajo** aumenta el número de personas, dinero, dependencias y consecuencias que quedan dentro de la decisión. Por eso la misma herramienta debe volverse más explícita en evidencia, gobernanza y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Un equipo automatiza clasificación de facturas, pero cada excepción vuelve por correo a tres personas y genera más retrabajo que antes.

Entrega un **decision brief de automatización y rediseño de trabajo** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre personas, cliente, operación, caja y riesgo; (e) recomendación; (f) condición que haría cambiarla; (g) dueño y fecha de revisión. Utiliza al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica

1. Reconstruye el caso de **automatización y rediseño de trabajo** con una tabla `hecho / interpretación / hipótesis / decisión`.
2. Ejecuta **1. mapear workflow end-to-end → 2. clasificar tareas por repetición judgment y risk → 3. diseñar target workflow y exceptions → 4. redefinir roles y controles → 5. pilotear y medir productivity y quality** y adjunta evidencia para cada transición entre pasos.
3. Calcula o documenta touch time, automation rate; si no existe dato, diseña cómo obtenerlo.
4. Escribe una alternativa que contradiga tu preferencia inicial y haz un *pre-mortem* específico del caso.
5. Lee dos referencias, registra una coincidencia y una tensión, y modifica el brief si corresponde.
6. Repite la decisión desde el rol de CEO/owner: identifica qué cambia al aumentar el alcance y la irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar task decomposition y augmentation como sinónimos | Se pierde la distinción entre “descomposición del trabajo en actividades con distinto potencial de automatización” y “uso de tecnología para aumentar capacidad humana” | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por “pilotear y medir productivity y quality” | Se saltó “mapear workflow end-to-end” y la solución llegó antes que el diagnóstico | Reconstruye la cadena 1. mapear workflow end-to-end → 2. clasificar tareas por repetición judgment y risk → 3. diseñar target workflow y exceptions → 4. redefinir roles y controles → 5. pilotear y medir productivity y quality y marca el primer supuesto no demostrado. |
| Optimizar solo touch time | La métrica local sustituyó al resultado del sistema | Contrástala con automation rate y explicita el costo de oportunidad. |
| Generalizar desde un caso favorable | Se confundió evidencia local con una regla universal sobre automatización y rediseño de trabajo | Automatización de alto riesgo necesita controles y fallback. No uses capacidad técnica como justificación para eliminar juicio humano donde daño potencial es material. |
| No fijar revisión | Una decisión sobre automatización y rediseño de trabajo se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de stop. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **task decomposition** y **augmentation** usando un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **straight-through processing** y qué observación obligaría a rechazar tu interpretación?
3. Aplica **mapear workflow end-to-end → clasificar tareas por repetición judgment y risk** al caso de la clase. ¿Qué dato todavía falta?
4. ¿Por qué **touch time** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la tabla de lectura. ¿Dónde podrían llevar a recomendaciones distintas para **automatización y rediseño de trabajo**?
6. ¿Qué decisión equivocada podría producirse si se ignora este límite: **Automatización de alto riesgo necesita controles y fallback. No uses capacidad técnica como justificación para eliminar juicio humano donde daño potencial es material.**?

## 📥 Entregable

Guarda en `portfolio/234-automatizacion-y-rediseno-de-trabajo/`:

- `operating-improvement-brief.md` con el problema específico de **automatización y rediseño de trabajo**, evidencia, alternativas, decisión y gobernanza;
- `reading-note.md` contrastando las fuentes de **automatización y rediseño de trabajo** con edición/páginas consultadas;
- `decision-journal.md` registrando los supuestos de **task decomposition**, confianza, responsable y revisión;
- `red-team.md` con la objeción más fuerte al caso **Un equipo automatiza clasificación de facturas, pero cada excepción vuelve por correo a tres personas y genera más retrabajo que antes.** y el dato que podría invalidar la recomendación.

## 📗 Fuentes y verificación

- Marco Iansiti & Karim R. Lakhani — *Competing in the Age of AI*. **Uso en esta clase:** modelo operativo AI-first, escala digital, redes y arquitectura de decisión. Lectura selectiva: índice/capítulos pertinentes a **automatización y rediseño de trabajo**; registra edición y páginas consultadas.
- Thomas H. Davenport & Nitin Mittal — *All-In on AI*. **Uso en esta clase:** casos empresariales, estrategia y organización para inteligencia artificial. Lectura selectiva: índice/capítulos pertinentes a **automatización y rediseño de trabajo**; registra edición y páginas consultadas.
- Martin Kleppmann — *Designing Data-Intensive Applications*. **Uso en esta clase:** perspectiva de Arquitectura tecnológica aplicada al problema de la clase. Lectura selectiva: índice/capítulos pertinentes a **automatización y rediseño de trabajo**; registra edición y páginas consultadas.
- NIST — *Cybersecurity Framework (CSF) 2.0*. **Uso en esta clase:** gobierno, identificación, protección, detección, respuesta y recuperación en ciberseguridad. Lectura selectiva: índice/capítulos pertinentes a **automatización y rediseño de trabajo**; registra edición y páginas consultadas.
- George Westerman, Didier Bonnet & Andrew McAfee — *Leading Digital*. **Uso en esta clase:** transformación digital desde capacidades de liderazgo y capacidades digitales. Lectura selectiva: índice/capítulos pertinentes a **automatización y rediseño de trabajo**; registra edición y páginas consultadas.
- Andrew McAfee & Erik Brynjolfsson — *Machine, Platform, Crowd*. **Uso en esta clase:** perspectiva de Economía digital aplicada al problema de la clase. Lectura selectiva: índice/capítulos pertinentes a **automatización y rediseño de trabajo**; registra edición y páginas consultadas.
- Susan A. Ambrose et al. — *How Learning Works*. **Uso en esta clase:** diseñar los objetivos, la práctica y el feedback de **automatización y rediseño de trabajo** sobre conocimiento previo verificable.
- Peter C. Brown, Henry L. Roediger III & Mark A. McDaniel — *Make It Stick*. **Uso en esta clase:** justificar la recuperación inicial y las preguntas de comprobación de **automatización y rediseño de trabajo**.
- Grant Wiggins & Jay McTighe — *Understanding by Design*. **Uso en esta clase:** derivar el entregable de **automatización y rediseño de trabajo** desde el desempeño observable y no desde el temario.
- Anders Ericsson & Robert Pool — *Peak*. **Uso en esta clase:** convertir la práctica de **automatización y rediseño de trabajo** en práctica deliberada con criterios explícitos.
- William Ellet — *The Case Study Handbook*. **Uso en esta clase:** estructurar el caso ejecutivo de **automatización y rediseño de trabajo** como problema, evidencia, alternativas y recomendación.

> **Regla de fuentes para Automatización y rediseño de trabajo:** las obras anteriores estructuran las perspectivas de esta materia; cualquier norma, ley, impuesto o estándar vivo mencionado en **automatización y rediseño de trabajo** debe comprobarse nuevamente en su fuente primaria vigente. El desarrollo es original y no reproduce capítulos protegidos.
