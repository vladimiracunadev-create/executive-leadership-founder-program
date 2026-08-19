# Clase 096 — Capstone: rediseñar una operación

**Parte:** 07 — Operaciones, procesos y calidad  
**Nivel:** Etapa 2 — Jefe → Manager  
**Duración sugerida:** 150–180 minutos · **Estándar:** deep-class-v2

## 🎯 Propósito

Rediseñar una operación integra flujo, capacidad, cuello, calidad, nivel de servicio, terceros, continuidad y automatización. El capstone exige demostrar que la mejora global no solo desplaza espera o costo a otra área.

La salida de esta parte es **operar procesos end-to-end con capacidad, calidad, continuidad y mejora**. En esta clase, esa progresión se concreta al exigir que cada afirmación sobre **capstone: rediseñar una operación** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

## 📚 Resultados de aprendizaje

Al finalizar podrás:

1. **Distinguir** `target operating model`, `baseline`, `future state`, `benefit case`, `transition plan` mediante observables, no por memoria verbal.
2. **Explicar** por qué esas distinciones cambian una decisión de jefe → manager.
3. **Aplicar** la secuencia **1. medir baseline end-to-end → 2. identificar constraint y causas → 3. diseñar future state → 4. calcular beneficio y riesgos → 5. pilotear, migrar y estabilizar** conservando supuestos, alternativas y trazabilidad.
4. **Interpretar** lead time, throughput, quality sin confundir señal, explicación y causalidad.
5. **Resolver** el caso ejecutivo con al menos dos opciones plausibles y un criterio explícito de stop/revisión.
6. **Contrastar** dos obras de referencia y explicar dónde sus lentes son complementarias o entran en tensión.

## 🧭 Agenda

| Tramo | Evidencia de aprendizaje |
|---|---|
| 0–20 min | Recuperación: define target operating model y baseline sin mirar la tabla; corrige con la fuente. |
| 20–70 min | Lectura guiada de conceptos + contraste de dos referencias. |
| 70–115 min | Ejemplo trabajado con lead time y trazabilidad de supuestos. |
| 115–155 min | Caso ejecutivo: dos alternativas, trade-offs y decisión provisional. |
| 155–180 min | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar comprensión |
|---|---|---|
| **target operating model** | diseño futuro de procesos, roles, tecnología y controles | Distingue un hecho compatible y otro que lo refute. |
| **baseline** | medición del sistema antes de intervenir | Distingue un hecho compatible y otro que lo refute. |
| **future state** | flujo objetivo con hipótesis de mejora | Distingue un hecho compatible y otro que lo refute. |
| **benefit case** | valor esperado versus costo y riesgo | Distingue un hecho compatible y otro que lo refute. |
| **transition plan** | secuencia para migrar sin interrumpir servicio | Distingue un hecho compatible y otro que lo refute. |

## 🧠 Modelo mental

```text
1. medir baseline end-to-end → 2. identificar constraint y causas → 3. diseñar future state → 4. calcular beneficio y riesgos → 5. pilotear, migrar y estabilizar
```

La secuencia nace del problema de esta clase: **Rediseñar una operación integra flujo, capacidad, cuello, calidad, nivel de servicio, terceros, continuidad y automatización. El capstone exige demostrar que la mejora global no solo desplaza espera o costo a otra área.** El método es útil mientras las condiciones permitan observar las señales requeridas. No elimina incertidumbre; la hace visible y obliga a decidir proporcionalmente a la evidencia. Límite principal: **Rediseño puede fallar por perseguir un diagrama ideal sin capacidad de transición. Protege servicio durante migración y valida con pilotos antes de cambios irreversibles.**

## 📖 Desarrollo

### 1. target operating model: mecanismo central

**target operating model** se entiende aquí como **diseño futuro de procesos, roles, tecnología y controles**. Esta es la pieza causal o estructural desde la que se inicia **capstone: rediseñar una operación**: antes de medir baseline end-to-end, el gerente debe poder señalar qué cambia en el sistema si el concepto está presente y qué debería observar si no lo está. Una definición que no produce predicciones observables todavía es demasiado vaga para dirigir.

La lectura rectora de este bloque es Nigel Slack & Alistair Brandon-Jones — *Operations Management*. Su aporte se usa para examinar **capacidad, procesos, variabilidad, calidad y estrategia de operaciones**. Aplica esa lente al caso sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **lead time**; regístrala con periodo, unidad, población y baseline.

Relaciona el mecanismo con **baseline**. Si ambos cambian juntos, no concluyas causalidad automáticamente: identifica una tercera variable o mecanismo alternativo que también pueda explicar el patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. baseline: frontera conceptual y error de clasificación

**Definición operacional:** medición del sistema antes de intervenir. Su valor está en distinguirlo de **target operating model** y **future state**. En una decisión real, clasificar una situación en la categoría equivocada cambia la intervención: puedes asignar autoridad donde faltaba información, medir un output cuando debías observar un proceso o tratar una restricción como si fuera una preferencia.

Contrasta el problema con Eliyahu M. Goldratt & Jeff Cox — *The Goal*, que aporta una mirada sobre **restricciones, throughput, inventario y pensamiento de flujo**. Formula dos mini-casos: uno que sí satisface la definición de **baseline** y otro que solo se parece superficialmente. Luego pregunta qué señal distinguiría ambos; para esta clase, **throughput** es una candidata, pero debe combinarse con evidencia cualitativa o documental cuando el fenómeno no sea directamente medible.

Antes de identificar constraint y causas, registra explícitamente qué decisión sería errónea si esta frontera conceptual se ignora. Esa frase convierte el vocabulario en criterio gerencial.

### 3. future state: operacionalización y medición

**future state** significa **flujo objetivo con hipótesis de mejora**. El problema ya no es definirlo, sino **operacionalizarlo**: qué contar, durante qué ventana, con qué denominador, contra qué baseline y con qué segmentación. Una métrica útil conserva suficiente contexto para no confundir mejora local con mejora del sistema.

ISO — *ISO 9001 Quality management systems* orienta este bloque mediante **gestión de calidad basada en procesos, evidencia y mejora**. Usa esa perspectiva para diseñar una ficha de medición: `señal → fórmula/criterio → fuente → frecuencia → owner → interpretación permitida → interpretación prohibida`. La señal asignada es **quality**. Si no existe un dato confiable, la salida correcta no es inventar precisión: diseña el mecanismo de captura y declara la incertidumbre.

Al llegar a diseñar future state, compara tendencia, distribución y casos atípicos. Pregunta además si el indicador es *leading* o *lagging* y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; nunca convertirse en el objetivo que reemplaza al fenómeno.

### 4. benefit case: trade-offs y efectos de segundo orden

**Definición:** valor esperado versus costo y riesgo. Este concepto obliga a abandonar la idea de que **capstone: rediseñar una operación** tiene una solución gratuita. Toda intervención consume autonomía, tiempo, caja, capacidad, atención, reputación o tolerancia al riesgo. Por eso, antes de calcular beneficio y riesgos, se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

James P. Womack & Daniel T. Jones — *Lean Thinking* aporta una lente sobre **valor, flujo, pull, desperdicio y mejora continua**. Úsala para construir una matriz `beneficio / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **cost-to-serve** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la necesidad de observar efectos laterales fuera del KPI principal.

Haz un *pre-mortem* de **capstone: rediseñar una operación**: supone que la opción recomendada fracasó seis meses después y enumera tres mecanismos que podrían explicarlo. Al menos uno debe provenir de un efecto de segundo orden asociado a **benefit case** y otro de una hipótesis del caso que nunca fue validada.

### 5. transition plan: gobernanza, límites e integración

**transition plan** se define como **secuencia para migrar sin interrumpir servicio** y cierra el circuito porque traduce análisis en responsabilidad. La pregunta ejecutiva es quién decide, quién ejecuta, quién debe ser consultado, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar.

Geary A. Rummler & Alan P. Brache — *Improving Performance* se utiliza para estudiar **perspectiva de Procesos aplicada al problema de la clase** y contrastar la recomendación final. Al ejecutar pilotear, migrar y estabilizar, deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento. Esa trazabilidad protege contra el sesgo retrospectivo y mejora las revisiones posteriores.

La frontera de esta clase es explícita: **Rediseño puede fallar por perseguir un diagrama ideal sin capacidad de transición. Protege servicio durante migración y valida con pilotos antes de cambios irreversibles.**. Conviértela en una regla operativa: `si ocurre X → no aplicar automáticamente → consultar/escalar/revalidar`. Integrar **target operating model**, **baseline**, **future state**, **benefit case** y **transition plan** significa poder explicar qué parte del diagnóstico sostiene la decisión y cuál sigue siendo una apuesta.

### 6. Integración: de conceptos a una decisión defendible

La síntesis de **capstone: rediseñar una operación** no consiste en sumar cinco definiciones. Empieza por **target operating model**, contrasta **baseline** con **future state**, incorpora **benefit case** como restricción o mecanismo y usa **transition plan** para cerrar el ciclo. Si el análisis no puede explicar cuál de esas piezas cambió la recomendación, todavía no hay comprensión transferible.

Aplica ahora la secuencia **1. medir baseline end-to-end → 2. identificar constraint y causas → 3. diseñar future state → 4. calcular beneficio y riesgos → 5. pilotear, migrar y estabilizar**. Para cada paso conserva tres columnas: evidencia utilizada, alternativa descartada y razón. Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado y evita reescribir la historia después de conocer el desenlace.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla señala el lente que debes buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Nigel Slack & Alistair Brandon-Jones — *Operations Management* | capacidad, procesos, variabilidad, calidad y estrategia de operaciones | ¿Qué supuesto de **capstone: rediseñar una operación** ayuda a desafiar? |
| Eliyahu M. Goldratt & Jeff Cox — *The Goal* | restricciones, throughput, inventario y pensamiento de flujo | ¿Qué supuesto de **capstone: rediseñar una operación** ayuda a desafiar? |
| ISO — *ISO 9001 Quality management systems* | gestión de calidad basada en procesos, evidencia y mejora | ¿Qué supuesto de **capstone: rediseñar una operación** ayuda a desafiar? |
| James P. Womack & Daniel T. Jones — *Lean Thinking* | valor, flujo, pull, desperdicio y mejora continua | ¿Qué supuesto de **capstone: rediseñar una operación** ayuda a desafiar? |
| Geary A. Rummler & Alan P. Brache — *Improving Performance* | perspectiva de Procesos aplicada al problema de la clase | ¿Qué supuesto de **capstone: rediseñar una operación** ayuda a desafiar? |

En **capstone: rediseñar una operación**, la lectura se evalúa por **uso**, no por cantidad de páginas. La nota debe indicar qué tesis de las fuentes modifica tu lectura de **target operating model**, qué evidencia del caso tensiona esa tesis y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación:** Una operación de soporte tarda 11 días, tiene 18 handoffs y 22% de retrabajo. Dirección pide reducir costo 20% sin empeorar experiencia ni riesgo.

**Paso 1 — medir baseline end-to-end.** La gerencia escribe primero el supuesto asociado a **target operating model** y evita convertirlo en hecho. Luego busca **lead time** para contrastarlo en el caso de **capstone: rediseñar una operación**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 2 — identificar constraint y causas.** La gerencia escribe primero el supuesto asociado a **baseline** y evita convertirlo en hecho. Luego busca **throughput** para contrastarlo en el caso de **capstone: rediseñar una operación**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 3 — diseñar future state.** La gerencia escribe primero el supuesto asociado a **future state** y evita convertirlo en hecho. Luego busca **quality** para contrastarlo en el caso de **capstone: rediseñar una operación**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 4 — calcular beneficio y riesgos.** La gerencia escribe primero el supuesto asociado a **benefit case** y evita convertirlo en hecho. Luego busca **cost-to-serve** para contrastarlo en el caso de **capstone: rediseñar una operación**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 5 — pilotear, migrar y estabilizar.** La gerencia escribe primero el supuesto asociado a **transition plan** y evita convertirlo en hecho. Luego busca **resilience** para contrastarlo en el caso de **capstone: rediseñar una operación**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Síntesis del caso.** La recomendación debe terminar con responsable, fecha, evidencia de éxito y señal de stop. En **capstone: rediseñar una operación**, omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo |
|---|---|---|---|
| **target operating model** | diseño futuro de procesos, roles, tecnología y controles | Cuando lead time es observable y accionable. | Sobrerreaccionar a una señal parcial. |
| **baseline** | medición del sistema antes de intervenir | Cuando la primera explicación no distingue mecanismo o responsabilidad. | Convertir el concepto en etiqueta. |
| **Experimento/revisión** | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar eternamente y no decidir. |
| **Escalamiento** | Elevar autoridad o especialidad | Cuando hay derechos, capital material, regulación o irreversibilidad. | Delegar hacia arriba lo que sí corresponde decidir. |

**Frontera de aplicación:** Rediseño puede fallar por perseguir un diagrama ideal sin capacidad de transición. Protege servicio durante migración y valida con pilotos antes de cambios irreversibles.

## 🪜 De profesional a owner

| Nivel | Responsabilidad sobre capstone: rediseñar una operación |
|---|---|
| **Profesional** | usa **capstone: rediseñar una operación** para mejorar una contribución propia y explicar sus supuestos con evidencia. |
| **Jefe / Team Lead** | aplica **target operating model** y **baseline** para coordinar personas sin sustituir conversación por métricas. |
| **Manager / Gerente** | conecta lead time con capacidad, presupuesto, dependencias y riesgo interáreas. |
| **CEO / Director** | decide si capstone: rediseñar una operación cambia estrategia, economía o riesgo de empresa y qué debe llegar al comité o directorio. |
| **Founder / Owner** | pregunta si la solución de capstone: rediseñar una operación reduce dependencia del fundador, preserva caja y puede operar como sistema repetible. |

El cambio de nivel en **capstone: rediseñar una operación** aumenta el número de personas, dinero, dependencias y consecuencias que quedan dentro de la decisión. Por eso la misma herramienta debe volverse más explícita en evidencia, gobernanza y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Una operación de soporte tarda 11 días, tiene 18 handoffs y 22% de retrabajo. Dirección pide reducir costo 20% sin empeorar experiencia ni riesgo.

Entrega un **decision brief de capstone: rediseñar una operación** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre personas, cliente, operación, caja y riesgo; (e) recomendación; (f) condición que haría cambiarla; (g) dueño y fecha de revisión. Utiliza al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica

1. Reconstruye el caso de **capstone: rediseñar una operación** con una tabla `hecho / interpretación / hipótesis / decisión`.
2. Ejecuta **1. medir baseline end-to-end → 2. identificar constraint y causas → 3. diseñar future state → 4. calcular beneficio y riesgos → 5. pilotear, migrar y estabilizar** y adjunta evidencia para cada transición entre pasos.
3. Calcula o documenta lead time, throughput; si no existe dato, diseña cómo obtenerlo.
4. Escribe una alternativa que contradiga tu preferencia inicial y haz un *pre-mortem* específico del caso.
5. Lee dos referencias, registra una coincidencia y una tensión, y modifica el brief si corresponde.
6. Repite la decisión desde el rol de CEO/owner: identifica qué cambia al aumentar el alcance y la irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar target operating model y baseline como sinónimos | Se pierde la distinción entre “diseño futuro de procesos, roles, tecnología y controles” y “medición del sistema antes de intervenir” | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por “pilotear, migrar y estabilizar” | Se saltó “medir baseline end-to-end” y la solución llegó antes que el diagnóstico | Reconstruye la cadena 1. medir baseline end-to-end → 2. identificar constraint y causas → 3. diseñar future state → 4. calcular beneficio y riesgos → 5. pilotear, migrar y estabilizar y marca el primer supuesto no demostrado. |
| Optimizar solo lead time | La métrica local sustituyó al resultado del sistema | Contrástala con throughput y explicita el costo de oportunidad. |
| Generalizar desde un caso favorable | Se confundió evidencia local con una regla universal sobre capstone: rediseñar una operación | Rediseño puede fallar por perseguir un diagrama ideal sin capacidad de transición. Protege servicio durante migración y valida con pilotos antes de cambios irreversibles. |
| No fijar revisión | Una decisión sobre capstone: rediseñar una operación se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de stop. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **target operating model** y **baseline** usando un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **future state** y qué observación obligaría a rechazar tu interpretación?
3. Aplica **medir baseline end-to-end → identificar constraint y causas** al caso de la clase. ¿Qué dato todavía falta?
4. ¿Por qué **lead time** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la tabla de lectura. ¿Dónde podrían llevar a recomendaciones distintas para **capstone: rediseñar una operación**?
6. ¿Qué decisión equivocada podría producirse si se ignora este límite: **Rediseño puede fallar por perseguir un diagrama ideal sin capacidad de transición. Protege servicio durante migración y valida con pilotos antes de cambios irreversibles.**?

## 📥 Entregable

Guarda en `portfolio/096-capstone-redisenar-una-operacion/`:

- `operating-improvement-brief.md` con el problema específico de **capstone: rediseñar una operación**, evidencia, alternativas, decisión y gobernanza;
- `reading-note.md` contrastando las fuentes de **capstone: rediseñar una operación** con edición/páginas consultadas;
- `decision-journal.md` registrando los supuestos de **target operating model**, confianza, responsable y revisión;
- `red-team.md` con la objeción más fuerte al caso **Una operación de soporte tarda 11 días, tiene 18 handoffs y 22% de retrabajo. Dirección pide reducir costo 20% sin empeorar experiencia ni riesgo.** y el dato que podría invalidar la recomendación.

## 📗 Fuentes y verificación

- Nigel Slack & Alistair Brandon-Jones — *Operations Management*. **Uso en esta clase:** capacidad, procesos, variabilidad, calidad y estrategia de operaciones. Lectura selectiva: índice/capítulos pertinentes a **capstone: rediseñar una operación**; registra edición y páginas consultadas.
- Eliyahu M. Goldratt & Jeff Cox — *The Goal*. **Uso en esta clase:** restricciones, throughput, inventario y pensamiento de flujo. Lectura selectiva: índice/capítulos pertinentes a **capstone: rediseñar una operación**; registra edición y páginas consultadas.
- ISO — *ISO 9001 Quality management systems*. **Uso en esta clase:** gestión de calidad basada en procesos, evidencia y mejora. Lectura selectiva: índice/capítulos pertinentes a **capstone: rediseñar una operación**; registra edición y páginas consultadas.
- James P. Womack & Daniel T. Jones — *Lean Thinking*. **Uso en esta clase:** valor, flujo, pull, desperdicio y mejora continua. Lectura selectiva: índice/capítulos pertinentes a **capstone: rediseñar una operación**; registra edición y páginas consultadas.
- Geary A. Rummler & Alan P. Brache — *Improving Performance*. **Uso en esta clase:** perspectiva de Procesos aplicada al problema de la clase. Lectura selectiva: índice/capítulos pertinentes a **capstone: rediseñar una operación**; registra edición y páginas consultadas.
- W. Edwards Deming — *Out of the Crisis*. **Uso en esta clase:** variación, sistemas, aprendizaje y responsabilidad gerencial por la calidad. Lectura selectiva: índice/capítulos pertinentes a **capstone: rediseñar una operación**; registra edición y páginas consultadas.
- Susan A. Ambrose et al. — *How Learning Works*. **Uso en esta clase:** diseñar los objetivos, la práctica y el feedback de **capstone: rediseñar una operación** sobre conocimiento previo verificable.
- Peter C. Brown, Henry L. Roediger III & Mark A. McDaniel — *Make It Stick*. **Uso en esta clase:** justificar la recuperación inicial y las preguntas de comprobación de **capstone: rediseñar una operación**.
- Grant Wiggins & Jay McTighe — *Understanding by Design*. **Uso en esta clase:** derivar el entregable de **capstone: rediseñar una operación** desde el desempeño observable y no desde el temario.
- Anders Ericsson & Robert Pool — *Peak*. **Uso en esta clase:** convertir la práctica de **capstone: rediseñar una operación** en práctica deliberada con criterios explícitos.
- William Ellet — *The Case Study Handbook*. **Uso en esta clase:** estructurar el caso ejecutivo de **capstone: rediseñar una operación** como problema, evidencia, alternativas y recomendación.

> **Regla de fuentes para Capstone: rediseñar una operación:** las obras anteriores estructuran las perspectivas de esta materia; cualquier norma, ley, impuesto o estándar vivo mencionado en **capstone: rediseñar una operación** debe comprobarse nuevamente en su fuente primaria vigente. El desarrollo es original y no reproduce capítulos protegidos.
