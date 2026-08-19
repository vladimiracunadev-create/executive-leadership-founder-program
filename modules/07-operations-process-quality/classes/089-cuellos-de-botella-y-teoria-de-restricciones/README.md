# Clase 089 — Cuellos de botella y teoría de restricciones

**Parte:** 07 — Operaciones, procesos y calidad  
**Nivel:** Etapa 2 — Jefe → Manager  
**Duración sugerida:** 150–180 minutos · **Estándar:** deep-class-v2

## 🎯 Propósito

La Teoría de Restricciones sostiene que el throughput del sistema está limitado por una restricción dominante. Mejorar etapas no limitantes puede crear más WIP sin aumentar output. La secuencia es identificar, explotar, subordinar, elevar y luego buscar la nueva restricción.

La salida de esta parte es **operar procesos end-to-end con capacidad, calidad, continuidad y mejora**. En esta clase, esa progresión se concreta al exigir que cada afirmación sobre **cuellos de botella y teoría de restricciones** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

## 📚 Resultados de aprendizaje

Al finalizar podrás:

1. **Distinguir** `constraint`, `bottleneck`, `throughput`, `buffer`, `subordination` mediante observables, no por memoria verbal.
2. **Explicar** por qué esas distinciones cambian una decisión de jefe → manager.
3. **Aplicar** la secuencia **1. medir flujo y localizar restricción → 2. explotar capacidad sin inversión → 3. subordinar upstream y downstream → 4. elevar restricción si el valor lo justifica → 5. repetir cuando migra el cuello** conservando supuestos, alternativas y trazabilidad.
4. **Interpretar** throughput de restricción, idle time del cuello, buffer penetration sin confundir señal, explicación y causalidad.
5. **Resolver** el caso ejecutivo con al menos dos opciones plausibles y un criterio explícito de stop/revisión.
6. **Contrastar** dos obras de referencia y explicar dónde sus lentes son complementarias o entran en tensión.

## 🧭 Agenda

| Tramo | Evidencia de aprendizaje |
|---|---|
| 0–20 min | Recuperación: define constraint y bottleneck sin mirar la tabla; corrige con la fuente. |
| 20–70 min | Lectura guiada de conceptos + contraste de dos referencias. |
| 70–115 min | Ejemplo trabajado con throughput de restricción y trazabilidad de supuestos. |
| 115–155 min | Caso ejecutivo: dos alternativas, trade-offs y decisión provisional. |
| 155–180 min | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar comprensión |
|---|---|---|
| **constraint** | recurso o política que limita throughput global | Distingue un hecho compatible y otro que lo refute. |
| **bottleneck** | etapa cuya capacidad efectiva restringe el flujo | Distingue un hecho compatible y otro que lo refute. |
| **throughput** | ritmo al que el sistema genera unidades de valor | Distingue un hecho compatible y otro que lo refute. |
| **buffer** | protección colocada antes de la restricción | Distingue un hecho compatible y otro que lo refute. |
| **subordination** | alinear otras etapas para no sobrecargar ni dejar ociosa la restricción | Distingue un hecho compatible y otro que lo refute. |

## 🧠 Modelo mental

```text
1. medir flujo y localizar restricción → 2. explotar capacidad sin inversión → 3. subordinar upstream y downstream → 4. elevar restricción si el valor lo justifica → 5. repetir cuando migra el cuello
```

La secuencia nace del problema de esta clase: **La Teoría de Restricciones sostiene que el throughput del sistema está limitado por una restricción dominante. Mejorar etapas no limitantes puede crear más WIP sin aumentar output. La secuencia es identificar, explotar, subordinar, elevar y luego buscar la nueva restricción.** El método es útil mientras las condiciones permitan observar las señales requeridas. No elimina incertidumbre; la hace visible y obliga a decidir proporcionalmente a la evidencia. Límite principal: **No todos los sistemas tienen un único cuello estable; mix, demanda y políticas pueden moverlo. Observa datos y horizonte antes de convertir TOC en dogma.**

## 📖 Desarrollo

### 1. constraint: mecanismo central

**constraint** se entiende aquí como **recurso o política que limita throughput global**. Esta es la pieza causal o estructural desde la que se inicia **cuellos de botella y teoría de restricciones**: antes de medir flujo y localizar restricción, el gerente debe poder señalar qué cambia en el sistema si el concepto está presente y qué debería observar si no lo está. Una definición que no produce predicciones observables todavía es demasiado vaga para dirigir.

La lectura rectora de este bloque es Nigel Slack & Alistair Brandon-Jones — *Operations Management*. Su aporte se usa para examinar **capacidad, procesos, variabilidad, calidad y estrategia de operaciones**. Aplica esa lente al caso sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **throughput de restricción**; regístrala con periodo, unidad, población y baseline.

Relaciona el mecanismo con **bottleneck**. Si ambos cambian juntos, no concluyas causalidad automáticamente: identifica una tercera variable o mecanismo alternativo que también pueda explicar el patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. bottleneck: frontera conceptual y error de clasificación

**Definición operacional:** etapa cuya capacidad efectiva restringe el flujo. Su valor está en distinguirlo de **constraint** y **throughput**. En una decisión real, clasificar una situación en la categoría equivocada cambia la intervención: puedes asignar autoridad donde faltaba información, medir un output cuando debías observar un proceso o tratar una restricción como si fuera una preferencia.

Contrasta el problema con Eliyahu M. Goldratt & Jeff Cox — *The Goal*, que aporta una mirada sobre **restricciones, throughput, inventario y pensamiento de flujo**. Formula dos mini-casos: uno que sí satisface la definición de **bottleneck** y otro que solo se parece superficialmente. Luego pregunta qué señal distinguiría ambos; para esta clase, **idle time del cuello** es una candidata, pero debe combinarse con evidencia cualitativa o documental cuando el fenómeno no sea directamente medible.

Antes de explotar capacidad sin inversión, registra explícitamente qué decisión sería errónea si esta frontera conceptual se ignora. Esa frase convierte el vocabulario en criterio gerencial.

### 3. throughput: operacionalización y medición

**throughput** significa **ritmo al que el sistema genera unidades de valor**. El problema ya no es definirlo, sino **operacionalizarlo**: qué contar, durante qué ventana, con qué denominador, contra qué baseline y con qué segmentación. Una métrica útil conserva suficiente contexto para no confundir mejora local con mejora del sistema.

W. Edwards Deming — *Out of the Crisis* orienta este bloque mediante **variación, sistemas, aprendizaje y responsabilidad gerencial por la calidad**. Usa esa perspectiva para diseñar una ficha de medición: `señal → fórmula/criterio → fuente → frecuencia → owner → interpretación permitida → interpretación prohibida`. La señal asignada es **buffer penetration**. Si no existe un dato confiable, la salida correcta no es inventar precisión: diseña el mecanismo de captura y declara la incertidumbre.

Al llegar a subordinar upstream y downstream, compara tendencia, distribución y casos atípicos. Pregunta además si el indicador es *leading* o *lagging* y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; nunca convertirse en el objetivo que reemplaza al fenómeno.

### 4. buffer: trade-offs y efectos de segundo orden

**Definición:** protección colocada antes de la restricción. Este concepto obliga a abandonar la idea de que **cuellos de botella y teoría de restricciones** tiene una solución gratuita. Toda intervención consume autonomía, tiempo, caja, capacidad, atención, reputación o tolerancia al riesgo. Por eso, antes de elevar restricción si el valor lo justifica, se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Jeffrey K. Liker — *The Toyota Way* aporta una lente sobre **perspectiva de Operaciones aplicada al problema de la clase**. Úsala para construir una matriz `beneficio / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **WIP upstream** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la necesidad de observar efectos laterales fuera del KPI principal.

Haz un *pre-mortem* de **cuellos de botella y teoría de restricciones**: supone que la opción recomendada fracasó seis meses después y enumera tres mecanismos que podrían explicarlo. Al menos uno debe provenir de un efecto de segundo orden asociado a **buffer** y otro de una hipótesis del caso que nunca fue validada.

### 5. subordination: gobernanza, límites e integración

**subordination** se define como **alinear otras etapas para no sobrecargar ni dejar ociosa la restricción** y cierra el circuito porque traduce análisis en responsabilidad. La pregunta ejecutiva es quién decide, quién ejecuta, quién debe ser consultado, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar.

ISO — *ISO 9001 Quality management systems* se utiliza para estudiar **gestión de calidad basada en procesos, evidencia y mejora** y contrastar la recomendación final. Al ejecutar repetir cuando migra el cuello, deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento. Esa trazabilidad protege contra el sesgo retrospectivo y mejora las revisiones posteriores.

La frontera de esta clase es explícita: **No todos los sistemas tienen un único cuello estable; mix, demanda y políticas pueden moverlo. Observa datos y horizonte antes de convertir TOC en dogma.**. Conviértela en una regla operativa: `si ocurre X → no aplicar automáticamente → consultar/escalar/revalidar`. Integrar **constraint**, **bottleneck**, **throughput**, **buffer** y **subordination** significa poder explicar qué parte del diagnóstico sostiene la decisión y cuál sigue siendo una apuesta.

### 6. Integración: de conceptos a una decisión defendible

La síntesis de **cuellos de botella y teoría de restricciones** no consiste en sumar cinco definiciones. Empieza por **constraint**, contrasta **bottleneck** con **throughput**, incorpora **buffer** como restricción o mecanismo y usa **subordination** para cerrar el ciclo. Si el análisis no puede explicar cuál de esas piezas cambió la recomendación, todavía no hay comprensión transferible.

Aplica ahora la secuencia **1. medir flujo y localizar restricción → 2. explotar capacidad sin inversión → 3. subordinar upstream y downstream → 4. elevar restricción si el valor lo justifica → 5. repetir cuando migra el cuello**. Para cada paso conserva tres columnas: evidencia utilizada, alternativa descartada y razón. Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado y evita reescribir la historia después de conocer el desenlace.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla señala el lente que debes buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Nigel Slack & Alistair Brandon-Jones — *Operations Management* | capacidad, procesos, variabilidad, calidad y estrategia de operaciones | ¿Qué supuesto de **cuellos de botella y teoría de restricciones** ayuda a desafiar? |
| Eliyahu M. Goldratt & Jeff Cox — *The Goal* | restricciones, throughput, inventario y pensamiento de flujo | ¿Qué supuesto de **cuellos de botella y teoría de restricciones** ayuda a desafiar? |
| W. Edwards Deming — *Out of the Crisis* | variación, sistemas, aprendizaje y responsabilidad gerencial por la calidad | ¿Qué supuesto de **cuellos de botella y teoría de restricciones** ayuda a desafiar? |
| Jeffrey K. Liker — *The Toyota Way* | perspectiva de Operaciones aplicada al problema de la clase | ¿Qué supuesto de **cuellos de botella y teoría de restricciones** ayuda a desafiar? |
| ISO — *ISO 9001 Quality management systems* | gestión de calidad basada en procesos, evidencia y mejora | ¿Qué supuesto de **cuellos de botella y teoría de restricciones** ayuda a desafiar? |

En **cuellos de botella y teoría de restricciones**, la lectura se evalúa por **uso**, no por cantidad de páginas. La nota debe indicar qué tesis de las fuentes modifica tu lectura de **constraint**, qué evidencia del caso tensiona esa tesis y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación:** Una línea tiene cinco etapas. Cuatro producen 120 unidades/día y una 70. El director financia automatización de una etapa que ya produce 120 porque es la más visible.

**Paso 1 — medir flujo y localizar restricción.** La gerencia escribe primero el supuesto asociado a **constraint** y evita convertirlo en hecho. Luego busca **throughput de restricción** para contrastarlo en el caso de **cuellos de botella y teoría de restricciones**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 2 — explotar capacidad sin inversión.** La gerencia escribe primero el supuesto asociado a **bottleneck** y evita convertirlo en hecho. Luego busca **idle time del cuello** para contrastarlo en el caso de **cuellos de botella y teoría de restricciones**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 3 — subordinar upstream y downstream.** La gerencia escribe primero el supuesto asociado a **throughput** y evita convertirlo en hecho. Luego busca **buffer penetration** para contrastarlo en el caso de **cuellos de botella y teoría de restricciones**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 4 — elevar restricción si el valor lo justifica.** La gerencia escribe primero el supuesto asociado a **buffer** y evita convertirlo en hecho. Luego busca **WIP upstream** para contrastarlo en el caso de **cuellos de botella y teoría de restricciones**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 5 — repetir cuando migra el cuello.** La gerencia escribe primero el supuesto asociado a **subordination** y evita convertirlo en hecho. Luego busca **throughput total** para contrastarlo en el caso de **cuellos de botella y teoría de restricciones**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Síntesis del caso.** La recomendación debe terminar con responsable, fecha, evidencia de éxito y señal de stop. En **cuellos de botella y teoría de restricciones**, omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo |
|---|---|---|---|
| **constraint** | recurso o política que limita throughput global | Cuando throughput de restricción es observable y accionable. | Sobrerreaccionar a una señal parcial. |
| **bottleneck** | etapa cuya capacidad efectiva restringe el flujo | Cuando la primera explicación no distingue mecanismo o responsabilidad. | Convertir el concepto en etiqueta. |
| **Experimento/revisión** | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar eternamente y no decidir. |
| **Escalamiento** | Elevar autoridad o especialidad | Cuando hay derechos, capital material, regulación o irreversibilidad. | Delegar hacia arriba lo que sí corresponde decidir. |

**Frontera de aplicación:** No todos los sistemas tienen un único cuello estable; mix, demanda y políticas pueden moverlo. Observa datos y horizonte antes de convertir TOC en dogma.

## 🪜 De profesional a owner

| Nivel | Responsabilidad sobre cuellos de botella y teoría de restricciones |
|---|---|
| **Profesional** | usa **cuellos de botella y teoría de restricciones** para mejorar una contribución propia y explicar sus supuestos con evidencia. |
| **Jefe / Team Lead** | aplica **constraint** y **bottleneck** para coordinar personas sin sustituir conversación por métricas. |
| **Manager / Gerente** | conecta throughput de restricción con capacidad, presupuesto, dependencias y riesgo interáreas. |
| **CEO / Director** | decide si cuellos de botella y teoría de restricciones cambia estrategia, economía o riesgo de empresa y qué debe llegar al comité o directorio. |
| **Founder / Owner** | pregunta si la solución de cuellos de botella y teoría de restricciones reduce dependencia del fundador, preserva caja y puede operar como sistema repetible. |

El cambio de nivel en **cuellos de botella y teoría de restricciones** aumenta el número de personas, dinero, dependencias y consecuencias que quedan dentro de la decisión. Por eso la misma herramienta debe volverse más explícita en evidencia, gobernanza y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Una línea tiene cinco etapas. Cuatro producen 120 unidades/día y una 70. El director financia automatización de una etapa que ya produce 120 porque es la más visible.

Entrega un **decision brief de cuellos de botella y teoría de restricciones** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre personas, cliente, operación, caja y riesgo; (e) recomendación; (f) condición que haría cambiarla; (g) dueño y fecha de revisión. Utiliza al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica

1. Reconstruye el caso de **cuellos de botella y teoría de restricciones** con una tabla `hecho / interpretación / hipótesis / decisión`.
2. Ejecuta **1. medir flujo y localizar restricción → 2. explotar capacidad sin inversión → 3. subordinar upstream y downstream → 4. elevar restricción si el valor lo justifica → 5. repetir cuando migra el cuello** y adjunta evidencia para cada transición entre pasos.
3. Calcula o documenta throughput de restricción, idle time del cuello; si no existe dato, diseña cómo obtenerlo.
4. Escribe una alternativa que contradiga tu preferencia inicial y haz un *pre-mortem* específico del caso.
5. Lee dos referencias, registra una coincidencia y una tensión, y modifica el brief si corresponde.
6. Repite la decisión desde el rol de CEO/owner: identifica qué cambia al aumentar el alcance y la irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar constraint y bottleneck como sinónimos | Se pierde la distinción entre “recurso o política que limita throughput global” y “etapa cuya capacidad efectiva restringe el flujo” | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por “repetir cuando migra el cuello” | Se saltó “medir flujo y localizar restricción” y la solución llegó antes que el diagnóstico | Reconstruye la cadena 1. medir flujo y localizar restricción → 2. explotar capacidad sin inversión → 3. subordinar upstream y downstream → 4. elevar restricción si el valor lo justifica → 5. repetir cuando migra el cuello y marca el primer supuesto no demostrado. |
| Optimizar solo throughput de restricción | La métrica local sustituyó al resultado del sistema | Contrástala con idle time del cuello y explicita el costo de oportunidad. |
| Generalizar desde un caso favorable | Se confundió evidencia local con una regla universal sobre cuellos de botella y teoría de restricciones | No todos los sistemas tienen un único cuello estable; mix, demanda y políticas pueden moverlo. Observa datos y horizonte antes de convertir TOC en dogma. |
| No fijar revisión | Una decisión sobre cuellos de botella y teoría de restricciones se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de stop. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **constraint** y **bottleneck** usando un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **throughput** y qué observación obligaría a rechazar tu interpretación?
3. Aplica **medir flujo y localizar restricción → explotar capacidad sin inversión** al caso de la clase. ¿Qué dato todavía falta?
4. ¿Por qué **throughput de restricción** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la tabla de lectura. ¿Dónde podrían llevar a recomendaciones distintas para **cuellos de botella y teoría de restricciones**?
6. ¿Qué decisión equivocada podría producirse si se ignora este límite: **No todos los sistemas tienen un único cuello estable; mix, demanda y políticas pueden moverlo. Observa datos y horizonte antes de convertir TOC en dogma.**?

## 📥 Entregable

Guarda en `portfolio/089-cuellos-de-botella-y-teoria-de-restricciones/`:

- `risk-governance-brief.md` con el problema específico de **cuellos de botella y teoría de restricciones**, evidencia, alternativas, decisión y gobernanza;
- `reading-note.md` contrastando las fuentes de **cuellos de botella y teoría de restricciones** con edición/páginas consultadas;
- `decision-journal.md` registrando los supuestos de **constraint**, confianza, responsable y revisión;
- `red-team.md` con la objeción más fuerte al caso **Una línea tiene cinco etapas. Cuatro producen 120 unidades/día y una 70. El director financia automatización de una etapa que ya produce 120 porque es la más visible.** y el dato que podría invalidar la recomendación.

## 📗 Fuentes y verificación

- Nigel Slack & Alistair Brandon-Jones — *Operations Management*. **Uso en esta clase:** capacidad, procesos, variabilidad, calidad y estrategia de operaciones. Lectura selectiva: índice/capítulos pertinentes a **cuellos de botella y teoría de restricciones**; registra edición y páginas consultadas.
- Eliyahu M. Goldratt & Jeff Cox — *The Goal*. **Uso en esta clase:** restricciones, throughput, inventario y pensamiento de flujo. Lectura selectiva: índice/capítulos pertinentes a **cuellos de botella y teoría de restricciones**; registra edición y páginas consultadas.
- W. Edwards Deming — *Out of the Crisis*. **Uso en esta clase:** variación, sistemas, aprendizaje y responsabilidad gerencial por la calidad. Lectura selectiva: índice/capítulos pertinentes a **cuellos de botella y teoría de restricciones**; registra edición y páginas consultadas.
- Jeffrey K. Liker — *The Toyota Way*. **Uso en esta clase:** perspectiva de Operaciones aplicada al problema de la clase. Lectura selectiva: índice/capítulos pertinentes a **cuellos de botella y teoría de restricciones**; registra edición y páginas consultadas.
- ISO — *ISO 9001 Quality management systems*. **Uso en esta clase:** gestión de calidad basada en procesos, evidencia y mejora. Lectura selectiva: índice/capítulos pertinentes a **cuellos de botella y teoría de restricciones**; registra edición y páginas consultadas.
- James P. Womack & Daniel T. Jones — *Lean Thinking*. **Uso en esta clase:** valor, flujo, pull, desperdicio y mejora continua. Lectura selectiva: índice/capítulos pertinentes a **cuellos de botella y teoría de restricciones**; registra edición y páginas consultadas.
- Susan A. Ambrose et al. — *How Learning Works*. **Uso en esta clase:** diseñar los objetivos, la práctica y el feedback de **cuellos de botella y teoría de restricciones** sobre conocimiento previo verificable.
- Peter C. Brown, Henry L. Roediger III & Mark A. McDaniel — *Make It Stick*. **Uso en esta clase:** justificar la recuperación inicial y las preguntas de comprobación de **cuellos de botella y teoría de restricciones**.
- Grant Wiggins & Jay McTighe — *Understanding by Design*. **Uso en esta clase:** derivar el entregable de **cuellos de botella y teoría de restricciones** desde el desempeño observable y no desde el temario.
- Anders Ericsson & Robert Pool — *Peak*. **Uso en esta clase:** convertir la práctica de **cuellos de botella y teoría de restricciones** en práctica deliberada con criterios explícitos.
- William Ellet — *The Case Study Handbook*. **Uso en esta clase:** estructurar el caso ejecutivo de **cuellos de botella y teoría de restricciones** como problema, evidencia, alternativas y recomendación.

> **Regla de fuentes para Cuellos de botella y teoría de restricciones:** las obras anteriores estructuran las perspectivas de esta materia; cualquier norma, ley, impuesto o estándar vivo mencionado en **cuellos de botella y teoría de restricciones** debe comprobarse nuevamente en su fuente primaria vigente. El desarrollo es original y no reproduce capítulos protegidos.
