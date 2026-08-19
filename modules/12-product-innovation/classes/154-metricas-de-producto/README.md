# Clase 154 — Métricas de producto

**Parte:** 12 — Producto e innovación  
**Nivel:** Etapa 3 — Manager → Gerente  
**Duración sugerida:** 150–180 minutos · **Estándar:** deep-class-v2

## 🎯 Propósito

Las métricas de producto deben conectar adquisición y uso con valor para el usuario y economía para la empresa. Vanity metrics crecen sin cambiar decisiones; métricas operables tienen definición, población, ventana temporal, owner y vínculo con un outcome.

La salida de esta parte es **convertir problemas de clientes en productos validados y outcomes medibles**. En esta clase, esa progresión se concreta al exigir que cada afirmación sobre **métricas de producto** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

## 📚 Resultados de aprendizaje

Al finalizar podrás:

1. **Distinguir** `north star metric`, `activation`, `retention`, `engagement`, `vanity metric` mediante observables, no por memoria verbal.
2. **Explicar** por qué esas distinciones cambian una decisión de manager → gerente.
3. **Aplicar** la secuencia **1. definir valor entregado → 2. mapear funnel y eventos → 3. seleccionar métrica de outcome y drivers → 4. segmentar cohortes y ventanas → 5. establecer review y decisiones asociadas** conservando supuestos, alternativas y trazabilidad.
4. **Interpretar** activation rate, cohort retention, frequency of value event sin confundir señal, explicación y causalidad.
5. **Resolver** el caso ejecutivo con al menos dos opciones plausibles y un criterio explícito de stop/revisión.
6. **Contrastar** dos obras de referencia y explicar dónde sus lentes son complementarias o entran en tensión.

## 🧭 Agenda

| Tramo | Evidencia de aprendizaje |
|---|---|
| 0–20 min | Recuperación: define north star metric y activation sin mirar la tabla; corrige con la fuente. |
| 20–70 min | Lectura guiada de conceptos + contraste de dos referencias. |
| 70–115 min | Ejemplo trabajado con activation rate y trazabilidad de supuestos. |
| 115–155 min | Caso ejecutivo: dos alternativas, trade-offs y decisión provisional. |
| 155–180 min | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar comprensión |
|---|---|---|
| **north star metric** | señal de valor recurrente creada para clientes y negocio | Distingue un hecho compatible y otro que lo refute. |
| **activation** | evento que indica que un nuevo usuario alcanzó valor inicial | Distingue un hecho compatible y otro que lo refute. |
| **retention** | proporción que vuelve o mantiene uso relevante después de un periodo | Distingue un hecho compatible y otro que lo refute. |
| **engagement** | frecuencia o profundidad de conducta valiosa | Distingue un hecho compatible y otro que lo refute. |
| **vanity metric** | número atractivo que no guía una decisión causal u operativa | Distingue un hecho compatible y otro que lo refute. |

## 🧠 Modelo mental

```text
1. definir valor entregado → 2. mapear funnel y eventos → 3. seleccionar métrica de outcome y drivers → 4. segmentar cohortes y ventanas → 5. establecer review y decisiones asociadas
```

La secuencia nace del problema de esta clase: **Las métricas de producto deben conectar adquisición y uso con valor para el usuario y economía para la empresa. Vanity metrics crecen sin cambiar decisiones; métricas operables tienen definición, población, ventana temporal, owner y vínculo con un outcome.** El método es útil mientras las condiciones permitan observar las señales requeridas. No elimina incertidumbre; la hace visible y obliga a decidir proporcionalmente a la evidencia. Límite principal: **Una North Star puede inducir gaming si se desconecta de calidad, margen o bienestar. Acompáñala con guardrails y análisis de cohortes.**

## 📖 Desarrollo

### 1. north star metric: mecanismo central

**north star metric** se entiende aquí como **señal de valor recurrente creada para clientes y negocio**. Esta es la pieza causal o estructural desde la que se inicia **métricas de producto**: antes de definir valor entregado, el gerente debe poder señalar qué cambia en el sistema si el concepto está presente y qué debería observar si no lo está. Una definición que no produce predicciones observables todavía es demasiado vaga para dirigir.

La lectura rectora de este bloque es Marty Cagan — *Inspired*. Su aporte se usa para examinar **equipos de producto, discovery, riesgos de producto y outcomes**. Aplica esa lente al caso sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **activation rate**; regístrala con periodo, unidad, población y baseline.

Relaciona el mecanismo con **activation**. Si ambos cambian juntos, no concluyas causalidad automáticamente: identifica una tercera variable o mecanismo alternativo que también pueda explicar el patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. activation: frontera conceptual y error de clasificación

**Definición operacional:** evento que indica que un nuevo usuario alcanzó valor inicial. Su valor está en distinguirlo de **north star metric** y **retention**. En una decisión real, clasificar una situación en la categoría equivocada cambia la intervención: puedes asignar autoridad donde faltaba información, medir un output cuando debías observar un proceso o tratar una restricción como si fuera una preferencia.

Contrasta el problema con Teresa Torres — *Continuous Discovery Habits*, que aporta una mirada sobre **discovery continuo, oportunidades, experimentos y decisiones basadas en evidencia**. Formula dos mini-casos: uno que sí satisface la definición de **activation** y otro que solo se parece superficialmente. Luego pregunta qué señal distinguiría ambos; para esta clase, **cohort retention** es una candidata, pero debe combinarse con evidencia cualitativa o documental cuando el fenómeno no sea directamente medible.

Antes de mapear funnel y eventos, registra explícitamente qué decisión sería errónea si esta frontera conceptual se ignora. Esa frase convierte el vocabulario en criterio gerencial.

### 3. retention: operacionalización y medición

**retention** significa **proporción que vuelve o mantiene uso relevante después de un periodo**. El problema ya no es definirlo, sino **operacionalizarlo**: qué contar, durante qué ventana, con qué denominador, contra qué baseline y con qué segmentación. Una métrica útil conserva suficiente contexto para no confundir mejora local con mejora del sistema.

Melissa Perri — *Escaping the Build Trap* orienta este bloque mediante **perspectiva de Producto aplicada al problema de la clase**. Usa esa perspectiva para diseñar una ficha de medición: `señal → fórmula/criterio → fuente → frecuencia → owner → interpretación permitida → interpretación prohibida`. La señal asignada es **frequency of value event**. Si no existe un dato confiable, la salida correcta no es inventar precisión: diseña el mecanismo de captura y declara la incertidumbre.

Al llegar a seleccionar métrica de outcome y drivers, compara tendencia, distribución y casos atípicos. Pregunta además si el indicador es *leading* o *lagging* y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; nunca convertirse en el objetivo que reemplaza al fenómeno.

### 4. engagement: trade-offs y efectos de segundo orden

**Definición:** frecuencia o profundidad de conducta valiosa. Este concepto obliga a abandonar la idea de que **métricas de producto** tiene una solución gratuita. Toda intervención consume autonomía, tiempo, caja, capacidad, atención, reputación o tolerancia al riesgo. Por eso, antes de segmentar cohortes y ventanas, se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Alexander Osterwalder et al. — *Value Proposition Design* aporta una lente sobre **perspectiva de Producto aplicada al problema de la clase**. Úsala para construir una matriz `beneficio / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **conversion** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la necesidad de observar efectos laterales fuera del KPI principal.

Haz un *pre-mortem* de **métricas de producto**: supone que la opción recomendada fracasó seis meses después y enumera tres mecanismos que podrían explicarlo. Al menos uno debe provenir de un efecto de segundo orden asociado a **engagement** y otro de una hipótesis del caso que nunca fue validada.

### 5. vanity metric: gobernanza, límites e integración

**vanity metric** se define como **número atractivo que no guía una decisión causal u operativa** y cierra el circuito porque traduce análisis en responsabilidad. La pregunta ejecutiva es quién decide, quién ejecuta, quién debe ser consultado, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar.

David J. Bland & Alexander Osterwalder — *Testing Business Ideas* se utiliza para estudiar **hipótesis de negocio, experimentos, evidencia y reducción de riesgo** y contrastar la recomendación final. Al ejecutar establecer review y decisiones asociadas, deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento. Esa trazabilidad protege contra el sesgo retrospectivo y mejora las revisiones posteriores.

La frontera de esta clase es explícita: **Una North Star puede inducir gaming si se desconecta de calidad, margen o bienestar. Acompáñala con guardrails y análisis de cohortes.**. Conviértela en una regla operativa: `si ocurre X → no aplicar automáticamente → consultar/escalar/revalidar`. Integrar **north star metric**, **activation**, **retention**, **engagement** y **vanity metric** significa poder explicar qué parte del diagnóstico sostiene la decisión y cuál sigue siendo una apuesta.

### 6. Integración: de conceptos a una decisión defendible

La síntesis de **métricas de producto** no consiste en sumar cinco definiciones. Empieza por **north star metric**, contrasta **activation** con **retention**, incorpora **engagement** como restricción o mecanismo y usa **vanity metric** para cerrar el ciclo. Si el análisis no puede explicar cuál de esas piezas cambió la recomendación, todavía no hay comprensión transferible.

Aplica ahora la secuencia **1. definir valor entregado → 2. mapear funnel y eventos → 3. seleccionar métrica de outcome y drivers → 4. segmentar cohortes y ventanas → 5. establecer review y decisiones asociadas**. Para cada paso conserva tres columnas: evidencia utilizada, alternativa descartada y razón. Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado y evita reescribir la historia después de conocer el desenlace.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla señala el lente que debes buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Marty Cagan — *Inspired* | equipos de producto, discovery, riesgos de producto y outcomes | ¿Qué supuesto de **métricas de producto** ayuda a desafiar? |
| Teresa Torres — *Continuous Discovery Habits* | discovery continuo, oportunidades, experimentos y decisiones basadas en evidencia | ¿Qué supuesto de **métricas de producto** ayuda a desafiar? |
| Melissa Perri — *Escaping the Build Trap* | perspectiva de Producto aplicada al problema de la clase | ¿Qué supuesto de **métricas de producto** ayuda a desafiar? |
| Alexander Osterwalder et al. — *Value Proposition Design* | perspectiva de Producto aplicada al problema de la clase | ¿Qué supuesto de **métricas de producto** ayuda a desafiar? |
| David J. Bland & Alexander Osterwalder — *Testing Business Ideas* | hipótesis de negocio, experimentos, evidencia y reducción de riesgo | ¿Qué supuesto de **métricas de producto** ayuda a desafiar? |

En **métricas de producto**, la lectura se evalúa por **uso**, no por cantidad de páginas. La nota debe indicar qué tesis de las fuentes modifica tu lectura de **north star metric**, qué evidencia del caso tensiona esa tesis y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación:** Una app celebra un millón de registros, pero 70% nunca completa la primera acción valiosa y la retención a ocho semanas es 4%. Marketing sigue optimizando descargas.

**Paso 1 — definir valor entregado.** La gerencia escribe primero el supuesto asociado a **north star metric** y evita convertirlo en hecho. Luego busca **activation rate** para contrastarlo en el caso de **métricas de producto**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 2 — mapear funnel y eventos.** La gerencia escribe primero el supuesto asociado a **activation** y evita convertirlo en hecho. Luego busca **cohort retention** para contrastarlo en el caso de **métricas de producto**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 3 — seleccionar métrica de outcome y drivers.** La gerencia escribe primero el supuesto asociado a **retention** y evita convertirlo en hecho. Luego busca **frequency of value event** para contrastarlo en el caso de **métricas de producto**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 4 — segmentar cohortes y ventanas.** La gerencia escribe primero el supuesto asociado a **engagement** y evita convertirlo en hecho. Luego busca **conversion** para contrastarlo en el caso de **métricas de producto**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 5 — establecer review y decisiones asociadas.** La gerencia escribe primero el supuesto asociado a **vanity metric** y evita convertirlo en hecho. Luego busca **support-adjusted margin** para contrastarlo en el caso de **métricas de producto**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Síntesis del caso.** La recomendación debe terminar con responsable, fecha, evidencia de éxito y señal de stop. En **métricas de producto**, omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo |
|---|---|---|---|
| **north star metric** | señal de valor recurrente creada para clientes y negocio | Cuando activation rate es observable y accionable. | Sobrerreaccionar a una señal parcial. |
| **activation** | evento que indica que un nuevo usuario alcanzó valor inicial | Cuando la primera explicación no distingue mecanismo o responsabilidad. | Convertir el concepto en etiqueta. |
| **Experimento/revisión** | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar eternamente y no decidir. |
| **Escalamiento** | Elevar autoridad o especialidad | Cuando hay derechos, capital material, regulación o irreversibilidad. | Delegar hacia arriba lo que sí corresponde decidir. |

**Frontera de aplicación:** Una North Star puede inducir gaming si se desconecta de calidad, margen o bienestar. Acompáñala con guardrails y análisis de cohortes.

## 🪜 De profesional a owner

| Nivel | Responsabilidad sobre métricas de producto |
|---|---|
| **Profesional** | usa **métricas de producto** para mejorar una contribución propia y explicar sus supuestos con evidencia. |
| **Jefe / Team Lead** | aplica **north star metric** y **activation** para coordinar personas sin sustituir conversación por métricas. |
| **Manager / Gerente** | conecta activation rate con capacidad, presupuesto, dependencias y riesgo interáreas. |
| **CEO / Director** | decide si métricas de producto cambia estrategia, economía o riesgo de empresa y qué debe llegar al comité o directorio. |
| **Founder / Owner** | pregunta si la solución de métricas de producto reduce dependencia del fundador, preserva caja y puede operar como sistema repetible. |

El cambio de nivel en **métricas de producto** aumenta el número de personas, dinero, dependencias y consecuencias que quedan dentro de la decisión. Por eso la misma herramienta debe volverse más explícita en evidencia, gobernanza y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Una app celebra un millón de registros, pero 70% nunca completa la primera acción valiosa y la retención a ocho semanas es 4%. Marketing sigue optimizando descargas.

Entrega un **decision brief de métricas de producto** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre personas, cliente, operación, caja y riesgo; (e) recomendación; (f) condición que haría cambiarla; (g) dueño y fecha de revisión. Utiliza al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica

1. Reconstruye el caso de **métricas de producto** con una tabla `hecho / interpretación / hipótesis / decisión`.
2. Ejecuta **1. definir valor entregado → 2. mapear funnel y eventos → 3. seleccionar métrica de outcome y drivers → 4. segmentar cohortes y ventanas → 5. establecer review y decisiones asociadas** y adjunta evidencia para cada transición entre pasos.
3. Calcula o documenta activation rate, cohort retention; si no existe dato, diseña cómo obtenerlo.
4. Escribe una alternativa que contradiga tu preferencia inicial y haz un *pre-mortem* específico del caso.
5. Lee dos referencias, registra una coincidencia y una tensión, y modifica el brief si corresponde.
6. Repite la decisión desde el rol de CEO/owner: identifica qué cambia al aumentar el alcance y la irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar north star metric y activation como sinónimos | Se pierde la distinción entre “señal de valor recurrente creada para clientes y negocio” y “evento que indica que un nuevo usuario alcanzó valor inicial” | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por “establecer review y decisiones asociadas” | Se saltó “definir valor entregado” y la solución llegó antes que el diagnóstico | Reconstruye la cadena 1. definir valor entregado → 2. mapear funnel y eventos → 3. seleccionar métrica de outcome y drivers → 4. segmentar cohortes y ventanas → 5. establecer review y decisiones asociadas y marca el primer supuesto no demostrado. |
| Optimizar solo activation rate | La métrica local sustituyó al resultado del sistema | Contrástala con cohort retention y explicita el costo de oportunidad. |
| Generalizar desde un caso favorable | Se confundió evidencia local con una regla universal sobre métricas de producto | Una North Star puede inducir gaming si se desconecta de calidad, margen o bienestar. Acompáñala con guardrails y análisis de cohortes. |
| No fijar revisión | Una decisión sobre métricas de producto se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de stop. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **north star metric** y **activation** usando un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **retention** y qué observación obligaría a rechazar tu interpretación?
3. Aplica **definir valor entregado → mapear funnel y eventos** al caso de la clase. ¿Qué dato todavía falta?
4. ¿Por qué **activation rate** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la tabla de lectura. ¿Dónde podrían llevar a recomendaciones distintas para **métricas de producto**?
6. ¿Qué decisión equivocada podría producirse si se ignora este límite: **Una North Star puede inducir gaming si se desconecta de calidad, margen o bienestar. Acompáñala con guardrails y análisis de cohortes.**?

## 📥 Entregable

Guarda en `portfolio/154-metricas-de-producto/`:

- `product-evidence-brief.md` con el problema específico de **métricas de producto**, evidencia, alternativas, decisión y gobernanza;
- `reading-note.md` contrastando las fuentes de **métricas de producto** con edición/páginas consultadas;
- `decision-journal.md` registrando los supuestos de **north star metric**, confianza, responsable y revisión;
- `red-team.md` con la objeción más fuerte al caso **Una app celebra un millón de registros, pero 70% nunca completa la primera acción valiosa y la retención a ocho semanas es 4%. Marketing sigue optimizando descargas.** y el dato que podría invalidar la recomendación.

## 📗 Fuentes y verificación

- Marty Cagan — *Inspired*. **Uso en esta clase:** equipos de producto, discovery, riesgos de producto y outcomes. Lectura selectiva: índice/capítulos pertinentes a **métricas de producto**; registra edición y páginas consultadas.
- Teresa Torres — *Continuous Discovery Habits*. **Uso en esta clase:** discovery continuo, oportunidades, experimentos y decisiones basadas en evidencia. Lectura selectiva: índice/capítulos pertinentes a **métricas de producto**; registra edición y páginas consultadas.
- Melissa Perri — *Escaping the Build Trap*. **Uso en esta clase:** perspectiva de Producto aplicada al problema de la clase. Lectura selectiva: índice/capítulos pertinentes a **métricas de producto**; registra edición y páginas consultadas.
- Alexander Osterwalder et al. — *Value Proposition Design*. **Uso en esta clase:** perspectiva de Producto aplicada al problema de la clase. Lectura selectiva: índice/capítulos pertinentes a **métricas de producto**; registra edición y páginas consultadas.
- David J. Bland & Alexander Osterwalder — *Testing Business Ideas*. **Uso en esta clase:** hipótesis de negocio, experimentos, evidencia y reducción de riesgo. Lectura selectiva: índice/capítulos pertinentes a **métricas de producto**; registra edición y páginas consultadas.
- Clayton M. Christensen et al. — *Competing Against Luck*. **Uso en esta clase:** jobs to be done y comprensión causal de por qué un cliente elige una solución. Lectura selectiva: índice/capítulos pertinentes a **métricas de producto**; registra edición y páginas consultadas.
- Susan A. Ambrose et al. — *How Learning Works*. **Uso en esta clase:** diseñar los objetivos, la práctica y el feedback de **métricas de producto** sobre conocimiento previo verificable.
- Peter C. Brown, Henry L. Roediger III & Mark A. McDaniel — *Make It Stick*. **Uso en esta clase:** justificar la recuperación inicial y las preguntas de comprobación de **métricas de producto**.
- Grant Wiggins & Jay McTighe — *Understanding by Design*. **Uso en esta clase:** derivar el entregable de **métricas de producto** desde el desempeño observable y no desde el temario.
- Anders Ericsson & Robert Pool — *Peak*. **Uso en esta clase:** convertir la práctica de **métricas de producto** en práctica deliberada con criterios explícitos.
- William Ellet — *The Case Study Handbook*. **Uso en esta clase:** estructurar el caso ejecutivo de **métricas de producto** como problema, evidencia, alternativas y recomendación.

> **Regla de fuentes para Métricas de producto:** las obras anteriores estructuran las perspectivas de esta materia; cualquier norma, ley, impuesto o estándar vivo mencionado en **métricas de producto** debe comprobarse nuevamente en su fuente primaria vigente. El desarrollo es original y no reproduce capítulos protegidos.
