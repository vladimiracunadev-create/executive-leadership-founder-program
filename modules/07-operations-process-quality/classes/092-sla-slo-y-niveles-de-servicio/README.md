# Clase 092 — SLA, SLO y niveles de servicio

**Parte:** 07 — Operaciones, procesos y calidad  
**Nivel:** Etapa 2 — Jefe → Manager  
**Duración sugerida:** 150–180 minutos · **Estándar:** deep-class-v2

## 🎯 Propósito

SLA y SLO traducen confiabilidad en expectativas medibles. Un SLI observa desempeño; un SLO fija objetivo interno o de diseño; un SLA es un compromiso contractual o externo con consecuencias definidas. Mezclarlos lleva a prometer al cliente el mismo umbral con el que opera internamente, sin buffer.

La salida de esta parte es **operar procesos end-to-end con capacidad, calidad, continuidad y mejora**. En esta clase, esa progresión se concreta al exigir que cada afirmación sobre **sLA, SLO y niveles de servicio** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

## 📚 Resultados de aprendizaje

Al finalizar podrás:

1. **Distinguir** `SLI`, `SLO`, `SLA`, `error budget`, `availability` mediante observables, no por memoria verbal.
2. **Explicar** por qué esas distinciones cambian una decisión de jefe → manager.
3. **Aplicar** la secuencia **1. seleccionar experiencia crítica y SLI → 2. definir SLO según usuario y costo → 3. crear buffer antes del SLA → 4. medir error budget → 5. tocar capacidad o cambios cuando se consume** conservando supuestos, alternativas y trazabilidad.
4. **Interpretar** availability, latency percentiles, error budget burn sin confundir señal, explicación y causalidad.
5. **Resolver** el caso ejecutivo con al menos dos opciones plausibles y un criterio explícito de stop/revisión.
6. **Contrastar** dos obras de referencia y explicar dónde sus lentes son complementarias o entran en tensión.

## 🧭 Agenda

| Tramo | Evidencia de aprendizaje |
|---|---|
| 0–20 min | Recuperación: define SLI y SLO sin mirar la tabla; corrige con la fuente. |
| 20–70 min | Lectura guiada de conceptos + contraste de dos referencias. |
| 70–115 min | Ejemplo trabajado con availability y trazabilidad de supuestos. |
| 115–155 min | Caso ejecutivo: dos alternativas, trade-offs y decisión provisional. |
| 155–180 min | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar comprensión |
|---|---|---|
| **SLI** | indicador medido de un aspecto del servicio | Distingue un hecho compatible y otro que lo refute. |
| **SLO** | objetivo de confiabilidad o desempeño para un SLI | Distingue un hecho compatible y otro que lo refute. |
| **SLA** | acuerdo externo que especifica nivel y consecuencia | Distingue un hecho compatible y otro que lo refute. |
| **error budget** | margen de incumplimiento tolerado respecto del SLO | Distingue un hecho compatible y otro que lo refute. |
| **availability** | proporción de tiempo o solicitudes en que el servicio está utilizable | Distingue un hecho compatible y otro que lo refute. |

## 🧠 Modelo mental

```text
1. seleccionar experiencia crítica y SLI → 2. definir SLO según usuario y costo → 3. crear buffer antes del SLA → 4. medir error budget → 5. tocar capacidad o cambios cuando se consume
```

La secuencia nace del problema de esta clase: **SLA y SLO traducen confiabilidad en expectativas medibles. Un SLI observa desempeño; un SLO fija objetivo interno o de diseño; un SLA es un compromiso contractual o externo con consecuencias definidas. Mezclarlos lleva a prometer al cliente el mismo umbral con el que opera internamente, sin buffer.** El método es útil mientras las condiciones permitan observar las señales requeridas. No elimina incertidumbre; la hace visible y obliga a decidir proporcionalmente a la evidencia. Límite principal: **Más nueves cuestan mucho y pueden no crear valor. La confiabilidad objetivo debe responder al impacto del usuario, no al deseo abstracto de perfección.**

## 📖 Desarrollo

### 1. SLI: mecanismo central

**SLI** se entiende aquí como **indicador medido de un aspecto del servicio**. Esta es la pieza causal o estructural desde la que se inicia **sLA, SLO y niveles de servicio**: antes de seleccionar experiencia crítica y sli, el gerente debe poder señalar qué cambia en el sistema si el concepto está presente y qué debería observar si no lo está. Una definición que no produce predicciones observables todavía es demasiado vaga para dirigir.

La lectura rectora de este bloque es Nigel Slack & Alistair Brandon-Jones — *Operations Management*. Su aporte se usa para examinar **capacidad, procesos, variabilidad, calidad y estrategia de operaciones**. Aplica esa lente al caso sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **availability**; regístrala con periodo, unidad, población y baseline.

Relaciona el mecanismo con **SLO**. Si ambos cambian juntos, no concluyas causalidad automáticamente: identifica una tercera variable o mecanismo alternativo que también pueda explicar el patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. SLO: frontera conceptual y error de clasificación

**Definición operacional:** objetivo de confiabilidad o desempeño para un SLI. Su valor está en distinguirlo de **SLI** y **SLA**. En una decisión real, clasificar una situación en la categoría equivocada cambia la intervención: puedes asignar autoridad donde faltaba información, medir un output cuando debías observar un proceso o tratar una restricción como si fuera una preferencia.

Contrasta el problema con Eliyahu M. Goldratt & Jeff Cox — *The Goal*, que aporta una mirada sobre **restricciones, throughput, inventario y pensamiento de flujo**. Formula dos mini-casos: uno que sí satisface la definición de **SLO** y otro que solo se parece superficialmente. Luego pregunta qué señal distinguiría ambos; para esta clase, **latency percentiles** es una candidata, pero debe combinarse con evidencia cualitativa o documental cuando el fenómeno no sea directamente medible.

Antes de definir slo según usuario y costo, registra explícitamente qué decisión sería errónea si esta frontera conceptual se ignora. Esa frase convierte el vocabulario en criterio gerencial.

### 3. SLA: operacionalización y medición

**SLA** significa **acuerdo externo que especifica nivel y consecuencia**. El problema ya no es definirlo, sino **operacionalizarlo**: qué contar, durante qué ventana, con qué denominador, contra qué baseline y con qué segmentación. Una métrica útil conserva suficiente contexto para no confundir mejora local con mejora del sistema.

W. Edwards Deming — *Out of the Crisis* orienta este bloque mediante **variación, sistemas, aprendizaje y responsabilidad gerencial por la calidad**. Usa esa perspectiva para diseñar una ficha de medición: `señal → fórmula/criterio → fuente → frecuencia → owner → interpretación permitida → interpretación prohibida`. La señal asignada es **error budget burn**. Si no existe un dato confiable, la salida correcta no es inventar precisión: diseña el mecanismo de captura y declara la incertidumbre.

Al llegar a crear buffer antes del sla, compara tendencia, distribución y casos atípicos. Pregunta además si el indicador es *leading* o *lagging* y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; nunca convertirse en el objetivo que reemplaza al fenómeno.

### 4. error budget: trade-offs y efectos de segundo orden

**Definición:** margen de incumplimiento tolerado respecto del SLO. Este concepto obliga a abandonar la idea de que **sLA, SLO y niveles de servicio** tiene una solución gratuita. Toda intervención consume autonomía, tiempo, caja, capacidad, atención, reputación o tolerancia al riesgo. Por eso, antes de medir error budget, se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

James P. Womack, Daniel T. Jones & Daniel Roos — *The Machine That Changed the World* aporta una lente sobre **perspectiva de Lean aplicada al problema de la clase**. Úsala para construir una matriz `beneficio / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **SLA breaches** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la necesidad de observar efectos laterales fuera del KPI principal.

Haz un *pre-mortem* de **sLA, SLO y niveles de servicio**: supone que la opción recomendada fracasó seis meses después y enumera tres mecanismos que podrían explicarlo. Al menos uno debe provenir de un efecto de segundo orden asociado a **error budget** y otro de una hipótesis del caso que nunca fue validada.

### 5. availability: gobernanza, límites e integración

**availability** se define como **proporción de tiempo o solicitudes en que el servicio está utilizable** y cierra el circuito porque traduce análisis en responsabilidad. La pregunta ejecutiva es quién decide, quién ejecuta, quién debe ser consultado, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar.

ISO — *ISO 22301 Business continuity management systems* se utiliza para estudiar **sistema de gestión de continuidad y preparación ante disrupciones** y contrastar la recomendación final. Al ejecutar tocar capacidad o cambios cuando se consume, deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento. Esa trazabilidad protege contra el sesgo retrospectivo y mejora las revisiones posteriores.

La frontera de esta clase es explícita: **Más nueves cuestan mucho y pueden no crear valor. La confiabilidad objetivo debe responder al impacto del usuario, no al deseo abstracto de perfección.**. Conviértela en una regla operativa: `si ocurre X → no aplicar automáticamente → consultar/escalar/revalidar`. Integrar **SLI**, **SLO**, **SLA**, **error budget** y **availability** significa poder explicar qué parte del diagnóstico sostiene la decisión y cuál sigue siendo una apuesta.

### 6. Integración: de conceptos a una decisión defendible

La síntesis de **sLA, SLO y niveles de servicio** no consiste en sumar cinco definiciones. Empieza por **SLI**, contrasta **SLO** con **SLA**, incorpora **error budget** como restricción o mecanismo y usa **availability** para cerrar el ciclo. Si el análisis no puede explicar cuál de esas piezas cambió la recomendación, todavía no hay comprensión transferible.

Aplica ahora la secuencia **1. seleccionar experiencia crítica y SLI → 2. definir SLO según usuario y costo → 3. crear buffer antes del SLA → 4. medir error budget → 5. tocar capacidad o cambios cuando se consume**. Para cada paso conserva tres columnas: evidencia utilizada, alternativa descartada y razón. Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado y evita reescribir la historia después de conocer el desenlace.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla señala el lente que debes buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Nigel Slack & Alistair Brandon-Jones — *Operations Management* | capacidad, procesos, variabilidad, calidad y estrategia de operaciones | ¿Qué supuesto de **sLA, SLO y niveles de servicio** ayuda a desafiar? |
| Eliyahu M. Goldratt & Jeff Cox — *The Goal* | restricciones, throughput, inventario y pensamiento de flujo | ¿Qué supuesto de **sLA, SLO y niveles de servicio** ayuda a desafiar? |
| W. Edwards Deming — *Out of the Crisis* | variación, sistemas, aprendizaje y responsabilidad gerencial por la calidad | ¿Qué supuesto de **sLA, SLO y niveles de servicio** ayuda a desafiar? |
| James P. Womack, Daniel T. Jones & Daniel Roos — *The Machine That Changed the World* | perspectiva de Lean aplicada al problema de la clase | ¿Qué supuesto de **sLA, SLO y niveles de servicio** ayuda a desafiar? |
| ISO — *ISO 22301 Business continuity management systems* | sistema de gestión de continuidad y preparación ante disrupciones | ¿Qué supuesto de **sLA, SLO y niveles de servicio** ayuda a desafiar? |

En **sLA, SLO y niveles de servicio**, la lectura se evalúa por **uso**, no por cantidad de páginas. La nota debe indicar qué tesis de las fuentes modifica tu lectura de **SLI**, qué evidencia del caso tensiona esa tesis y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación:** Un servicio promete 99,9% SLA y usa exactamente 99,9% como objetivo interno. Cualquier desviación rompe contrato porque no existe margen operacional.

**Paso 1 — seleccionar experiencia crítica y SLI.** La gerencia escribe primero el supuesto asociado a **SLI** y evita convertirlo en hecho. Luego busca **availability** para contrastarlo en el caso de **sLA, SLO y niveles de servicio**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 2 — definir SLO según usuario y costo.** La gerencia escribe primero el supuesto asociado a **SLO** y evita convertirlo en hecho. Luego busca **latency percentiles** para contrastarlo en el caso de **sLA, SLO y niveles de servicio**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 3 — crear buffer antes del SLA.** La gerencia escribe primero el supuesto asociado a **SLA** y evita convertirlo en hecho. Luego busca **error budget burn** para contrastarlo en el caso de **sLA, SLO y niveles de servicio**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 4 — medir error budget.** La gerencia escribe primero el supuesto asociado a **error budget** y evita convertirlo en hecho. Luego busca **SLA breaches** para contrastarlo en el caso de **sLA, SLO y niveles de servicio**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 5 — tocar capacidad o cambios cuando se consume.** La gerencia escribe primero el supuesto asociado a **availability** y evita convertirlo en hecho. Luego busca **customer impact** para contrastarlo en el caso de **sLA, SLO y niveles de servicio**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Síntesis del caso.** La recomendación debe terminar con responsable, fecha, evidencia de éxito y señal de stop. En **sLA, SLO y niveles de servicio**, omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo |
|---|---|---|---|
| **SLI** | indicador medido de un aspecto del servicio | Cuando availability es observable y accionable. | Sobrerreaccionar a una señal parcial. |
| **SLO** | objetivo de confiabilidad o desempeño para un SLI | Cuando la primera explicación no distingue mecanismo o responsabilidad. | Convertir el concepto en etiqueta. |
| **Experimento/revisión** | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar eternamente y no decidir. |
| **Escalamiento** | Elevar autoridad o especialidad | Cuando hay derechos, capital material, regulación o irreversibilidad. | Delegar hacia arriba lo que sí corresponde decidir. |

**Frontera de aplicación:** Más nueves cuestan mucho y pueden no crear valor. La confiabilidad objetivo debe responder al impacto del usuario, no al deseo abstracto de perfección.

## 🪜 De profesional a owner

| Nivel | Responsabilidad sobre sLA, SLO y niveles de servicio |
|---|---|
| **Profesional** | usa **sLA, SLO y niveles de servicio** para mejorar una contribución propia y explicar sus supuestos con evidencia. |
| **Jefe / Team Lead** | aplica **SLI** y **SLO** para coordinar personas sin sustituir conversación por métricas. |
| **Manager / Gerente** | conecta availability con capacidad, presupuesto, dependencias y riesgo interáreas. |
| **CEO / Director** | decide si sLA, SLO y niveles de servicio cambia estrategia, economía o riesgo de empresa y qué debe llegar al comité o directorio. |
| **Founder / Owner** | pregunta si la solución de sLA, SLO y niveles de servicio reduce dependencia del fundador, preserva caja y puede operar como sistema repetible. |

El cambio de nivel en **sLA, SLO y niveles de servicio** aumenta el número de personas, dinero, dependencias y consecuencias que quedan dentro de la decisión. Por eso la misma herramienta debe volverse más explícita en evidencia, gobernanza y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Un servicio promete 99,9% SLA y usa exactamente 99,9% como objetivo interno. Cualquier desviación rompe contrato porque no existe margen operacional.

Entrega un **decision brief de sLA, SLO y niveles de servicio** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre personas, cliente, operación, caja y riesgo; (e) recomendación; (f) condición que haría cambiarla; (g) dueño y fecha de revisión. Utiliza al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica

1. Reconstruye el caso de **sLA, SLO y niveles de servicio** con una tabla `hecho / interpretación / hipótesis / decisión`.
2. Ejecuta **1. seleccionar experiencia crítica y SLI → 2. definir SLO según usuario y costo → 3. crear buffer antes del SLA → 4. medir error budget → 5. tocar capacidad o cambios cuando se consume** y adjunta evidencia para cada transición entre pasos.
3. Calcula o documenta availability, latency percentiles; si no existe dato, diseña cómo obtenerlo.
4. Escribe una alternativa que contradiga tu preferencia inicial y haz un *pre-mortem* específico del caso.
5. Lee dos referencias, registra una coincidencia y una tensión, y modifica el brief si corresponde.
6. Repite la decisión desde el rol de CEO/owner: identifica qué cambia al aumentar el alcance y la irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar SLI y SLO como sinónimos | Se pierde la distinción entre “indicador medido de un aspecto del servicio” y “objetivo de confiabilidad o desempeño para un SLI” | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por “tocar capacidad o cambios cuando se consume” | Se saltó “seleccionar experiencia crítica y SLI” y la solución llegó antes que el diagnóstico | Reconstruye la cadena 1. seleccionar experiencia crítica y SLI → 2. definir SLO según usuario y costo → 3. crear buffer antes del SLA → 4. medir error budget → 5. tocar capacidad o cambios cuando se consume y marca el primer supuesto no demostrado. |
| Optimizar solo availability | La métrica local sustituyó al resultado del sistema | Contrástala con latency percentiles y explicita el costo de oportunidad. |
| Generalizar desde un caso favorable | Se confundió evidencia local con una regla universal sobre sLA, SLO y niveles de servicio | Más nueves cuestan mucho y pueden no crear valor. La confiabilidad objetivo debe responder al impacto del usuario, no al deseo abstracto de perfección. |
| No fijar revisión | Una decisión sobre sLA, SLO y niveles de servicio se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de stop. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **SLI** y **SLO** usando un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **SLA** y qué observación obligaría a rechazar tu interpretación?
3. Aplica **seleccionar experiencia crítica y SLI → definir SLO según usuario y costo** al caso de la clase. ¿Qué dato todavía falta?
4. ¿Por qué **availability** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la tabla de lectura. ¿Dónde podrían llevar a recomendaciones distintas para **sLA, SLO y niveles de servicio**?
6. ¿Qué decisión equivocada podría producirse si se ignora este límite: **Más nueves cuestan mucho y pueden no crear valor. La confiabilidad objetivo debe responder al impacto del usuario, no al deseo abstracto de perfección.**?

## 📥 Entregable

Guarda en `portfolio/092-sla-slo-y-niveles-de-servicio/`:

- `operating-improvement-brief.md` con el problema específico de **sLA, SLO y niveles de servicio**, evidencia, alternativas, decisión y gobernanza;
- `reading-note.md` contrastando las fuentes de **sLA, SLO y niveles de servicio** con edición/páginas consultadas;
- `decision-journal.md` registrando los supuestos de **SLI**, confianza, responsable y revisión;
- `red-team.md` con la objeción más fuerte al caso **Un servicio promete 99,9% SLA y usa exactamente 99,9% como objetivo interno. Cualquier desviación rompe contrato porque no existe margen operacional.** y el dato que podría invalidar la recomendación.

## 📗 Fuentes y verificación

- Nigel Slack & Alistair Brandon-Jones — *Operations Management*. **Uso en esta clase:** capacidad, procesos, variabilidad, calidad y estrategia de operaciones. Lectura selectiva: índice/capítulos pertinentes a **sLA, SLO y niveles de servicio**; registra edición y páginas consultadas.
- Eliyahu M. Goldratt & Jeff Cox — *The Goal*. **Uso en esta clase:** restricciones, throughput, inventario y pensamiento de flujo. Lectura selectiva: índice/capítulos pertinentes a **sLA, SLO y niveles de servicio**; registra edición y páginas consultadas.
- W. Edwards Deming — *Out of the Crisis*. **Uso en esta clase:** variación, sistemas, aprendizaje y responsabilidad gerencial por la calidad. Lectura selectiva: índice/capítulos pertinentes a **sLA, SLO y niveles de servicio**; registra edición y páginas consultadas.
- James P. Womack, Daniel T. Jones & Daniel Roos — *The Machine That Changed the World*. **Uso en esta clase:** perspectiva de Lean aplicada al problema de la clase. Lectura selectiva: índice/capítulos pertinentes a **sLA, SLO y niveles de servicio**; registra edición y páginas consultadas.
- ISO — *ISO 22301 Business continuity management systems*. **Uso en esta clase:** sistema de gestión de continuidad y preparación ante disrupciones. Lectura selectiva: índice/capítulos pertinentes a **sLA, SLO y niveles de servicio**; registra edición y páginas consultadas.
- James P. Womack & Daniel T. Jones — *Lean Thinking*. **Uso en esta clase:** valor, flujo, pull, desperdicio y mejora continua. Lectura selectiva: índice/capítulos pertinentes a **sLA, SLO y niveles de servicio**; registra edición y páginas consultadas.
- Susan A. Ambrose et al. — *How Learning Works*. Diseño de objetivos, práctica y feedback.
- Peter C. Brown, Henry L. Roediger III & Mark A. McDaniel — *Make It Stick*. Recuperación, elaboración y transferencia.
- Grant Wiggins & Jay McTighe — *Understanding by Design*. Diseño inverso desde desempeño observable.
- Anders Ericsson & Robert Pool — *Peak*. Práctica deliberada con criterios y retroalimentación.
- William Ellet — *The Case Study Handbook*. Análisis de problema/decisión, evidencia y recomendación.

> **Regla de fuentes para SLA, SLO y niveles de servicio:** las obras anteriores estructuran las perspectivas de esta materia; cualquier norma, ley, impuesto o estándar vivo mencionado en **sLA, SLO y niveles de servicio** debe comprobarse nuevamente en su fuente primaria vigente. El desarrollo es original y no reproduce capítulos protegidos.
