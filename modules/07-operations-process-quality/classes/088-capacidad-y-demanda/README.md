# Clase 088 — Capacidad y demanda

**Parte:** 07 — Operaciones, procesos y calidad  
**Nivel:** Etapa 2 — Jefe → Manager  
**Duración sugerida:** 150–180 minutos · **Estándar:** deep-class-v2

## 🎯 Propósito

Capacidad y demanda deben compararse en la misma unidad y horizonte. Cuando utilización se acerca continuamente al 100%, la variabilidad crea colas y tiempos de espera desproporcionados. Operaciones saludables mantienen buffers y gestionan picos, mix y restricciones.

La salida de esta parte es **operar procesos end-to-end con capacidad, calidad, continuidad y mejora**. En esta clase, esa progresión se concreta al exigir que cada afirmación sobre **capacidad y demanda** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

## 📚 Resultados de aprendizaje

Al finalizar podrás:

1. **Distinguir** `demand rate`, `capacity rate`, `utilization`, `queue`, `buffer` mediante observables, no por memoria verbal.
2. **Explicar** por qué esas distinciones cambian una decisión de jefe → manager.
3. **Aplicar** la secuencia **1. medir demanda por tipo y periodo → 2. medir capacidad efectiva → 3. segmentar variabilidad y picos → 4. diseñar buffer o flex capacity → 5. regular ingreso cuando supera sistema** conservando supuestos, alternativas y trazabilidad.
4. **Interpretar** utilization, queue length, wait time sin confundir señal, explicación y causalidad.
5. **Resolver** el caso ejecutivo con al menos dos opciones plausibles y un criterio explícito de stop/revisión.
6. **Contrastar** dos obras de referencia y explicar dónde sus lentes son complementarias o entran en tensión.

## 🧭 Agenda

| Tramo | Evidencia de aprendizaje |
|---|---|
| 0–20 min | Recuperación: define demand rate y capacity rate sin mirar la tabla; corrige con la fuente. |
| 20–70 min | Lectura guiada de conceptos + contraste de dos referencias. |
| 70–115 min | Ejemplo trabajado con utilization y trazabilidad de supuestos. |
| 115–155 min | Caso ejecutivo: dos alternativas, trade-offs y decisión provisional. |
| 155–180 min | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar comprensión |
|---|---|---|
| **demand rate** | ritmo de llegada de trabajo | Distingue un hecho compatible y otro que lo refute. |
| **capacity rate** | ritmo máximo sostenible de procesamiento | Distingue un hecho compatible y otro que lo refute. |
| **utilization** | porcentaje de capacidad ocupado | Distingue un hecho compatible y otro que lo refute. |
| **queue** | trabajo esperando servicio | Distingue un hecho compatible y otro que lo refute. |
| **buffer** | reserva de capacidad, inventario o tiempo para absorber variabilidad | Distingue un hecho compatible y otro que lo refute. |

## 🧠 Modelo mental

```text
1. medir demanda por tipo y periodo → 2. medir capacidad efectiva → 3. segmentar variabilidad y picos → 4. diseñar buffer o flex capacity → 5. regular ingreso cuando supera sistema
```

La secuencia nace del problema de esta clase: **Capacidad y demanda deben compararse en la misma unidad y horizonte. Cuando utilización se acerca continuamente al 100%, la variabilidad crea colas y tiempos de espera desproporcionados. Operaciones saludables mantienen buffers y gestionan picos, mix y restricciones.** El método es útil mientras las condiciones permitan observar las señales requeridas. No elimina incertidumbre; la hace visible y obliga a decidir proporcionalmente a la evidencia. Límite principal: **Más buffer cuesta dinero. La meta no es baja utilización universal, sino equilibrar costo de capacidad con costo de espera, pérdida de demanda y criticidad.**

## 📖 Desarrollo

### 1. demand rate: mecanismo central

**demand rate** se entiende aquí como **ritmo de llegada de trabajo**. Esta es la pieza causal o estructural desde la que se inicia **capacidad y demanda**: antes de medir demanda por tipo y periodo, el gerente debe poder señalar qué cambia en el sistema si el concepto está presente y qué debería observar si no lo está. Una definición que no produce predicciones observables todavía es demasiado vaga para dirigir.

La lectura rectora de este bloque es Nigel Slack & Alistair Brandon-Jones — *Operations Management*. Su aporte se usa para examinar **capacidad, procesos, variabilidad, calidad y estrategia de operaciones**. Aplica esa lente al caso sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **utilization**; regístrala con periodo, unidad, población y baseline.

Relaciona el mecanismo con **capacity rate**. Si ambos cambian juntos, no concluyas causalidad automáticamente: identifica una tercera variable o mecanismo alternativo que también pueda explicar el patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. capacity rate: frontera conceptual y error de clasificación

**Definición operacional:** ritmo máximo sostenible de procesamiento. Su valor está en distinguirlo de **demand rate** y **utilization**. En una decisión real, clasificar una situación en la categoría equivocada cambia la intervención: puedes asignar autoridad donde faltaba información, medir un output cuando debías observar un proceso o tratar una restricción como si fuera una preferencia.

Contrasta el problema con Eliyahu M. Goldratt & Jeff Cox — *The Goal*, que aporta una mirada sobre **restricciones, throughput, inventario y pensamiento de flujo**. Formula dos mini-casos: uno que sí satisface la definición de **capacity rate** y otro que solo se parece superficialmente. Luego pregunta qué señal distinguiría ambos; para esta clase, **queue length** es una candidata, pero debe combinarse con evidencia cualitativa o documental cuando el fenómeno no sea directamente medible.

Antes de medir capacidad efectiva, registra explícitamente qué decisión sería errónea si esta frontera conceptual se ignora. Esa frase convierte el vocabulario en criterio gerencial.

### 3. utilization: operacionalización y medición

**utilization** significa **porcentaje de capacidad ocupado**. El problema ya no es definirlo, sino **operacionalizarlo**: qué contar, durante qué ventana, con qué denominador, contra qué baseline y con qué segmentación. Una métrica útil conserva suficiente contexto para no confundir mejora local con mejora del sistema.

Michael Hammer & James Champy — *Reengineering the Corporation* orienta este bloque mediante **perspectiva de Procesos aplicada al problema de la clase**. Usa esa perspectiva para diseñar una ficha de medición: `señal → fórmula/criterio → fuente → frecuencia → owner → interpretación permitida → interpretación prohibida`. La señal asignada es **wait time**. Si no existe un dato confiable, la salida correcta no es inventar precisión: diseña el mecanismo de captura y declara la incertidumbre.

Al llegar a segmentar variabilidad y picos, compara tendencia, distribución y casos atípicos. Pregunta además si el indicador es *leading* o *lagging* y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; nunca convertirse en el objetivo que reemplaza al fenómeno.

### 4. queue: trade-offs y efectos de segundo orden

**Definición:** trabajo esperando servicio. Este concepto obliga a abandonar la idea de que **capacidad y demanda** tiene una solución gratuita. Toda intervención consume autonomía, tiempo, caja, capacidad, atención, reputación o tolerancia al riesgo. Por eso, antes de diseñar buffer o flex capacity, se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

James P. Womack & Daniel T. Jones — *Lean Thinking* aporta una lente sobre **valor, flujo, pull, desperdicio y mejora continua**. Úsala para construir una matriz `beneficio / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **lost demand** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la necesidad de observar efectos laterales fuera del KPI principal.

Haz un *pre-mortem* de **capacidad y demanda**: supone que la opción recomendada fracasó seis meses después y enumera tres mecanismos que podrían explicarlo. Al menos uno debe provenir de un efecto de segundo orden asociado a **queue** y otro de una hipótesis del caso que nunca fue validada.

### 5. buffer: gobernanza, límites e integración

**buffer** se define como **reserva de capacidad, inventario o tiempo para absorber variabilidad** y cierra el circuito porque traduce análisis en responsabilidad. La pregunta ejecutiva es quién decide, quién ejecuta, quién debe ser consultado, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar.

Geary A. Rummler & Alan P. Brache — *Improving Performance* se utiliza para estudiar **perspectiva de Procesos aplicada al problema de la clase** y contrastar la recomendación final. Al ejecutar regular ingreso cuando supera sistema, deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento. Esa trazabilidad protege contra el sesgo retrospectivo y mejora las revisiones posteriores.

La frontera de esta clase es explícita: **Más buffer cuesta dinero. La meta no es baja utilización universal, sino equilibrar costo de capacidad con costo de espera, pérdida de demanda y criticidad.**. Conviértela en una regla operativa: `si ocurre X → no aplicar automáticamente → consultar/escalar/revalidar`. Integrar **demand rate**, **capacity rate**, **utilization**, **queue** y **buffer** significa poder explicar qué parte del diagnóstico sostiene la decisión y cuál sigue siendo una apuesta.

### 6. Integración: de conceptos a una decisión defendible

La síntesis de **capacidad y demanda** no consiste en sumar cinco definiciones. Empieza por **demand rate**, contrasta **capacity rate** con **utilization**, incorpora **queue** como restricción o mecanismo y usa **buffer** para cerrar el ciclo. Si el análisis no puede explicar cuál de esas piezas cambió la recomendación, todavía no hay comprensión transferible.

Aplica ahora la secuencia **1. medir demanda por tipo y periodo → 2. medir capacidad efectiva → 3. segmentar variabilidad y picos → 4. diseñar buffer o flex capacity → 5. regular ingreso cuando supera sistema**. Para cada paso conserva tres columnas: evidencia utilizada, alternativa descartada y razón. Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado y evita reescribir la historia después de conocer el desenlace.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla señala el lente que debes buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Nigel Slack & Alistair Brandon-Jones — *Operations Management* | capacidad, procesos, variabilidad, calidad y estrategia de operaciones | ¿Qué supuesto de **capacidad y demanda** ayuda a desafiar? |
| Eliyahu M. Goldratt & Jeff Cox — *The Goal* | restricciones, throughput, inventario y pensamiento de flujo | ¿Qué supuesto de **capacidad y demanda** ayuda a desafiar? |
| Michael Hammer & James Champy — *Reengineering the Corporation* | perspectiva de Procesos aplicada al problema de la clase | ¿Qué supuesto de **capacidad y demanda** ayuda a desafiar? |
| James P. Womack & Daniel T. Jones — *Lean Thinking* | valor, flujo, pull, desperdicio y mejora continua | ¿Qué supuesto de **capacidad y demanda** ayuda a desafiar? |
| Geary A. Rummler & Alan P. Brache — *Improving Performance* | perspectiva de Procesos aplicada al problema de la clase | ¿Qué supuesto de **capacidad y demanda** ayuda a desafiar? |

En **capacidad y demanda**, la lectura se evalúa por **uso**, no por cantidad de páginas. La nota debe indicar qué tesis de las fuentes modifica tu lectura de **demand rate**, qué evidencia del caso tensiona esa tesis y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación:** Un equipo procesa en promedio 100 solicitudes semanales y recibe 98. Dirección concluye que hay capacidad suficiente, pero la llegada varía entre 70 y 140 y la cola crece cada fin de mes.

**Paso 1 — medir demanda por tipo y periodo.** La gerencia escribe primero el supuesto asociado a **demand rate** y evita convertirlo en hecho. Luego busca **utilization** para contrastarlo en el caso de **capacidad y demanda**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 2 — medir capacidad efectiva.** La gerencia escribe primero el supuesto asociado a **capacity rate** y evita convertirlo en hecho. Luego busca **queue length** para contrastarlo en el caso de **capacidad y demanda**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 3 — segmentar variabilidad y picos.** La gerencia escribe primero el supuesto asociado a **utilization** y evita convertirlo en hecho. Luego busca **wait time** para contrastarlo en el caso de **capacidad y demanda**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 4 — diseñar buffer o flex capacity.** La gerencia escribe primero el supuesto asociado a **queue** y evita convertirlo en hecho. Luego busca **lost demand** para contrastarlo en el caso de **capacidad y demanda**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 5 — regular ingreso cuando supera sistema.** La gerencia escribe primero el supuesto asociado a **buffer** y evita convertirlo en hecho. Luego busca **overtime** para contrastarlo en el caso de **capacidad y demanda**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Síntesis del caso.** La recomendación debe terminar con responsable, fecha, evidencia de éxito y señal de stop. En **capacidad y demanda**, omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo |
|---|---|---|---|
| **demand rate** | ritmo de llegada de trabajo | Cuando utilization es observable y accionable. | Sobrerreaccionar a una señal parcial. |
| **capacity rate** | ritmo máximo sostenible de procesamiento | Cuando la primera explicación no distingue mecanismo o responsabilidad. | Convertir el concepto en etiqueta. |
| **Experimento/revisión** | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar eternamente y no decidir. |
| **Escalamiento** | Elevar autoridad o especialidad | Cuando hay derechos, capital material, regulación o irreversibilidad. | Delegar hacia arriba lo que sí corresponde decidir. |

**Frontera de aplicación:** Más buffer cuesta dinero. La meta no es baja utilización universal, sino equilibrar costo de capacidad con costo de espera, pérdida de demanda y criticidad.

## 🪜 De profesional a owner

| Nivel | Responsabilidad sobre capacidad y demanda |
|---|---|
| **Profesional** | usa **capacidad y demanda** para mejorar una contribución propia y explicar sus supuestos con evidencia. |
| **Jefe / Team Lead** | aplica **demand rate** y **capacity rate** para coordinar personas sin sustituir conversación por métricas. |
| **Manager / Gerente** | conecta utilization con capacidad, presupuesto, dependencias y riesgo interáreas. |
| **CEO / Director** | decide si capacidad y demanda cambia estrategia, economía o riesgo de empresa y qué debe llegar al comité o directorio. |
| **Founder / Owner** | pregunta si la solución de capacidad y demanda reduce dependencia del fundador, preserva caja y puede operar como sistema repetible. |

El cambio de nivel en **capacidad y demanda** aumenta el número de personas, dinero, dependencias y consecuencias que quedan dentro de la decisión. Por eso la misma herramienta debe volverse más explícita en evidencia, gobernanza y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Un equipo procesa en promedio 100 solicitudes semanales y recibe 98. Dirección concluye que hay capacidad suficiente, pero la llegada varía entre 70 y 140 y la cola crece cada fin de mes.

Entrega un **decision brief de capacidad y demanda** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre personas, cliente, operación, caja y riesgo; (e) recomendación; (f) condición que haría cambiarla; (g) dueño y fecha de revisión. Utiliza al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica

1. Reconstruye el caso de **capacidad y demanda** con una tabla `hecho / interpretación / hipótesis / decisión`.
2. Ejecuta **1. medir demanda por tipo y periodo → 2. medir capacidad efectiva → 3. segmentar variabilidad y picos → 4. diseñar buffer o flex capacity → 5. regular ingreso cuando supera sistema** y adjunta evidencia para cada transición entre pasos.
3. Calcula o documenta utilization, queue length; si no existe dato, diseña cómo obtenerlo.
4. Escribe una alternativa que contradiga tu preferencia inicial y haz un *pre-mortem* específico del caso.
5. Lee dos referencias, registra una coincidencia y una tensión, y modifica el brief si corresponde.
6. Repite la decisión desde el rol de CEO/owner: identifica qué cambia al aumentar el alcance y la irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar demand rate y capacity rate como sinónimos | Se pierde la distinción entre “ritmo de llegada de trabajo” y “ritmo máximo sostenible de procesamiento” | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por “regular ingreso cuando supera sistema” | Se saltó “medir demanda por tipo y periodo” y la solución llegó antes que el diagnóstico | Reconstruye la cadena 1. medir demanda por tipo y periodo → 2. medir capacidad efectiva → 3. segmentar variabilidad y picos → 4. diseñar buffer o flex capacity → 5. regular ingreso cuando supera sistema y marca el primer supuesto no demostrado. |
| Optimizar solo utilization | La métrica local sustituyó al resultado del sistema | Contrástala con queue length y explicita el costo de oportunidad. |
| Generalizar desde un caso favorable | Se confundió evidencia local con una regla universal sobre capacidad y demanda | Más buffer cuesta dinero. La meta no es baja utilización universal, sino equilibrar costo de capacidad con costo de espera, pérdida de demanda y criticidad. |
| No fijar revisión | Una decisión sobre capacidad y demanda se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de stop. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **demand rate** y **capacity rate** usando un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **utilization** y qué observación obligaría a rechazar tu interpretación?
3. Aplica **medir demanda por tipo y periodo → medir capacidad efectiva** al caso de la clase. ¿Qué dato todavía falta?
4. ¿Por qué **utilization** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la tabla de lectura. ¿Dónde podrían llevar a recomendaciones distintas para **capacidad y demanda**?
6. ¿Qué decisión equivocada podría producirse si se ignora este límite: **Más buffer cuesta dinero. La meta no es baja utilización universal, sino equilibrar costo de capacidad con costo de espera, pérdida de demanda y criticidad.**?

## 📥 Entregable

Guarda en `portfolio/088-capacidad-y-demanda/`:

- `operating-improvement-brief.md` con el problema específico de **capacidad y demanda**, evidencia, alternativas, decisión y gobernanza;
- `reading-note.md` contrastando las fuentes de **capacidad y demanda** con edición/páginas consultadas;
- `decision-journal.md` registrando los supuestos de **demand rate**, confianza, responsable y revisión;
- `red-team.md` con la objeción más fuerte al caso **Un equipo procesa en promedio 100 solicitudes semanales y recibe 98. Dirección concluye que hay capacidad suficiente, pero la llegada varía entre 70 y 140 y la cola crece cada fin de mes.** y el dato que podría invalidar la recomendación.

## 📗 Fuentes y verificación

- Nigel Slack & Alistair Brandon-Jones — *Operations Management*. **Uso en esta clase:** capacidad, procesos, variabilidad, calidad y estrategia de operaciones. Lectura selectiva: índice/capítulos pertinentes a **capacidad y demanda**; registra edición y páginas consultadas.
- Eliyahu M. Goldratt & Jeff Cox — *The Goal*. **Uso en esta clase:** restricciones, throughput, inventario y pensamiento de flujo. Lectura selectiva: índice/capítulos pertinentes a **capacidad y demanda**; registra edición y páginas consultadas.
- Michael Hammer & James Champy — *Reengineering the Corporation*. **Uso en esta clase:** perspectiva de Procesos aplicada al problema de la clase. Lectura selectiva: índice/capítulos pertinentes a **capacidad y demanda**; registra edición y páginas consultadas.
- James P. Womack & Daniel T. Jones — *Lean Thinking*. **Uso en esta clase:** valor, flujo, pull, desperdicio y mejora continua. Lectura selectiva: índice/capítulos pertinentes a **capacidad y demanda**; registra edición y páginas consultadas.
- Geary A. Rummler & Alan P. Brache — *Improving Performance*. **Uso en esta clase:** perspectiva de Procesos aplicada al problema de la clase. Lectura selectiva: índice/capítulos pertinentes a **capacidad y demanda**; registra edición y páginas consultadas.
- James P. Womack, Daniel T. Jones & Daniel Roos — *The Machine That Changed the World*. **Uso en esta clase:** perspectiva de Lean aplicada al problema de la clase. Lectura selectiva: índice/capítulos pertinentes a **capacidad y demanda**; registra edición y páginas consultadas.
- Susan A. Ambrose et al. — *How Learning Works*. **Uso en esta clase:** diseñar los objetivos, la práctica y el feedback de **capacidad y demanda** sobre conocimiento previo verificable.
- Peter C. Brown, Henry L. Roediger III & Mark A. McDaniel — *Make It Stick*. **Uso en esta clase:** justificar la recuperación inicial y las preguntas de comprobación de **capacidad y demanda**.
- Grant Wiggins & Jay McTighe — *Understanding by Design*. **Uso en esta clase:** derivar el entregable de **capacidad y demanda** desde el desempeño observable y no desde el temario.
- Anders Ericsson & Robert Pool — *Peak*. **Uso en esta clase:** convertir la práctica de **capacidad y demanda** en práctica deliberada con criterios explícitos.
- William Ellet — *The Case Study Handbook*. **Uso en esta clase:** estructurar el caso ejecutivo de **capacidad y demanda** como problema, evidencia, alternativas y recomendación.

> **Regla de fuentes para Capacidad y demanda:** las obras anteriores estructuran las perspectivas de esta materia; cualquier norma, ley, impuesto o estándar vivo mencionado en **capacidad y demanda** debe comprobarse nuevamente en su fuente primaria vigente. El desarrollo es original y no reproduce capítulos protegidos.
