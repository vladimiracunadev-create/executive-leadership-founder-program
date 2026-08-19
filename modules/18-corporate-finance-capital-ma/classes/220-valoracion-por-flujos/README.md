# Clase 220 — Valoración por flujos

**Parte:** 18 — Finanzas corporativas, capital y M&A  
**Nivel:** Etapa 5 — CEO → Capital allocator  
**Duración sugerida:** 150–180 minutos · **Estándar:** deep-class-v2

## 🎯 Propósito

Valoración por DCF convierte flujos libres futuros en valor presente mediante una tasa consistente con su riesgo. La mayor parte del valor suele depender de pocos supuestos —crecimiento, margen, reinversión, WACC y terminal—, por lo que sensibilidad y coherencia económica son centrales.

La salida de esta parte es **decidir estructura de capital, valoración, fundraising y transacciones**. En esta clase, esa progresión se concreta al exigir que cada afirmación sobre **valoración por flujos** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

## 📚 Resultados de aprendizaje

Al finalizar podrás:

1. **Distinguir** `free cash flow`, `DCF`, `terminal value`, `discount rate`, `NOPAT` mediante observables, no por memoria verbal.
2. **Explicar** por qué esas distinciones cambian una decisión de ceo → capital allocator.
3. **Aplicar** la secuencia **1. proyectar drivers operativos → 2. convertir beneficio a FCF → 3. estimar discount rate → 4. calcular terminal value → 5. hacer sensibilidad y sanity checks** conservando supuestos, alternativas y trazabilidad.
4. **Interpretar** FCF, growth, operating margin sin confundir señal, explicación y causalidad.
5. **Resolver** el caso ejecutivo con al menos dos opciones plausibles y un criterio explícito de stop/revisión.
6. **Contrastar** dos obras de referencia y explicar dónde sus lentes son complementarias o entran en tensión.

## 🧭 Agenda

| Tramo | Evidencia de aprendizaje |
|---|---|
| 0–20 min | Recuperación: define free cash flow y DCF sin mirar la tabla; corrige con la fuente. |
| 20–70 min | Lectura guiada de conceptos + contraste de dos referencias. |
| 70–115 min | Ejemplo trabajado con FCF y trazabilidad de supuestos. |
| 115–155 min | Caso ejecutivo: dos alternativas, trade-offs y decisión provisional. |
| 155–180 min | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar comprensión |
|---|---|---|
| **free cash flow** | efectivo generado después de inversión necesaria disponible para financiadores | Distingue un hecho compatible y otro que lo refute. |
| **DCF** | valor presente de flujos esperados | Distingue un hecho compatible y otro que lo refute. |
| **terminal value** | valor de flujos posteriores al horizonte explícito | Distingue un hecho compatible y otro que lo refute. |
| **discount rate** | tasa que refleja tiempo y riesgo | Distingue un hecho compatible y otro que lo refute. |
| **NOPAT** | beneficio operativo después de impuestos sin efecto de financiación | Distingue un hecho compatible y otro que lo refute. |

## 🧠 Modelo mental

```text
1. proyectar drivers operativos → 2. convertir beneficio a FCF → 3. estimar discount rate → 4. calcular terminal value → 5. hacer sensibilidad y sanity checks
```

La secuencia nace del problema de esta clase: **Valoración por DCF convierte flujos libres futuros en valor presente mediante una tasa consistente con su riesgo. La mayor parte del valor suele depender de pocos supuestos —crecimiento, margen, reinversión, WACC y terminal—, por lo que sensibilidad y coherencia económica son centrales.** El método es útil mientras las condiciones permitan observar las señales requeridas. No elimina incertidumbre; la hace visible y obliga a decidir proporcionalmente a la evidencia. Límite principal: **DCF no crea información que no existe. Para startups o negocios en transición, escenarios y unit economics pueden ser más informativos que un punto de valoración.**

## 📖 Desarrollo

### 1. free cash flow: mecanismo central

**free cash flow** se entiende aquí como **efectivo generado después de inversión necesaria disponible para financiadores**. Esta es la pieza causal o estructural desde la que se inicia **valoración por flujos**: antes de proyectar drivers operativos, el gerente debe poder señalar qué cambia en el sistema si el concepto está presente y qué debería observar si no lo está. Una definición que no produce predicciones observables todavía es demasiado vaga para dirigir.

La lectura rectora de este bloque es Richard Brealey, Stewart Myers & Franklin Allen — *Principles of Corporate Finance*. Su aporte se usa para examinar **valor del dinero, riesgo, costo de capital, inversión y financiación**. Aplica esa lente al caso sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **FCF**; regístrala con periodo, unidad, población y baseline.

Relaciona el mecanismo con **DCF**. Si ambos cambian juntos, no concluyas causalidad automáticamente: identifica una tercera variable o mecanismo alternativo que también pueda explicar el patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. DCF: frontera conceptual y error de clasificación

**Definición operacional:** valor presente de flujos esperados. Su valor está en distinguirlo de **free cash flow** y **terminal value**. En una decisión real, clasificar una situación en la categoría equivocada cambia la intervención: puedes asignar autoridad donde faltaba información, medir un output cuando debías observar un proceso o tratar una restricción como si fuera una preferencia.

Contrasta el problema con Stephen Ross, Randolph Westerfield et al. — *Corporate Finance*, que aporta una mirada sobre **decisiones de inversión, financiación, capital de trabajo y valoración**. Formula dos mini-casos: uno que sí satisface la definición de **DCF** y otro que solo se parece superficialmente. Luego pregunta qué señal distinguiría ambos; para esta clase, **growth** es una candidata, pero debe combinarse con evidencia cualitativa o documental cuando el fenómeno no sea directamente medible.

Antes de convertir beneficio a fcf, registra explícitamente qué decisión sería errónea si esta frontera conceptual se ignora. Esa frase convierte el vocabulario en criterio gerencial.

### 3. terminal value: operacionalización y medición

**terminal value** significa **valor de flujos posteriores al horizonte explícito**. El problema ya no es definirlo, sino **operacionalizarlo**: qué contar, durante qué ventana, con qué denominador, contra qué baseline y con qué segmentación. Una métrica útil conserva suficiente contexto para no confundir mejora local con mejora del sistema.

Brad Feld & Jason Mendelson — *Venture Deals* orienta este bloque mediante **term sheets, economics/control y negociación de venture capital**. Usa esa perspectiva para diseñar una ficha de medición: `señal → fórmula/criterio → fuente → frecuencia → owner → interpretación permitida → interpretación prohibida`. La señal asignada es **operating margin**. Si no existe un dato confiable, la salida correcta no es inventar precisión: diseña el mecanismo de captura y declara la incertidumbre.

Al llegar a estimar discount rate, compara tendencia, distribución y casos atípicos. Pregunta además si el indicador es *leading* o *lagging* y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; nunca convertirse en el objetivo que reemplaza al fenómeno.

### 4. discount rate: trade-offs y efectos de segundo orden

**Definición:** tasa que refleja tiempo y riesgo. Este concepto obliga a abandonar la idea de que **valoración por flujos** tiene una solución gratuita. Toda intervención consume autonomía, tiempo, caja, capacidad, atención, reputación o tolerancia al riesgo. Por eso, antes de calcular terminal value, se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

David Skok — *SaaS Metrics resources* aporta una lente sobre **perspectiva de Unit economics aplicada al problema de la clase**. Úsala para construir una matriz `beneficio / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **WACC** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la necesidad de observar efectos laterales fuera del KPI principal.

Haz un *pre-mortem* de **valoración por flujos**: supone que la opción recomendada fracasó seis meses después y enumera tres mecanismos que podrían explicarlo. Al menos uno debe provenir de un efecto de segundo orden asociado a **discount rate** y otro de una hipótesis del caso que nunca fue validada.

### 5. NOPAT: gobernanza, límites e integración

**NOPAT** se define como **beneficio operativo después de impuestos sin efecto de financiación** y cierra el circuito porque traduce análisis en responsabilidad. La pregunta ejecutiva es quién decide, quién ejecuta, quién debe ser consultado, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar.

Ben Horowitz — *The Hard Thing About Hard Things* se utiliza para estudiar **decisiones difíciles de CEO, organización, personas y ejecución bajo presión** y contrastar la recomendación final. Al ejecutar hacer sensibilidad y sanity checks, deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento. Esa trazabilidad protege contra el sesgo retrospectivo y mejora las revisiones posteriores.

La frontera de esta clase es explícita: **DCF no crea información que no existe. Para startups o negocios en transición, escenarios y unit economics pueden ser más informativos que un punto de valoración.**. Conviértela en una regla operativa: `si ocurre X → no aplicar automáticamente → consultar/escalar/revalidar`. Integrar **free cash flow**, **DCF**, **terminal value**, **discount rate** y **NOPAT** significa poder explicar qué parte del diagnóstico sostiene la decisión y cuál sigue siendo una apuesta.

### 6. Integración: de conceptos a una decisión defendible

La síntesis de **valoración por flujos** no consiste en sumar cinco definiciones. Empieza por **free cash flow**, contrasta **DCF** con **terminal value**, incorpora **discount rate** como restricción o mecanismo y usa **NOPAT** para cerrar el ciclo. Si el análisis no puede explicar cuál de esas piezas cambió la recomendación, todavía no hay comprensión transferible.

Aplica ahora la secuencia **1. proyectar drivers operativos → 2. convertir beneficio a FCF → 3. estimar discount rate → 4. calcular terminal value → 5. hacer sensibilidad y sanity checks**. Para cada paso conserva tres columnas: evidencia utilizada, alternativa descartada y razón. Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado y evita reescribir la historia después de conocer el desenlace.

## 🔧 Profundización específica

### DCF paso a paso

Para FCFF, una formulación común es `FCFF = NOPAT + D&A - CAPEX - ΔNWC`. Descuenta cada periodo por una tasa coherente con riesgo y flujo. Valor terminal por perpetuidad: `TV = FCF_(n+1)/(WACC-g)`, con `g < WACC` y crecimiento sostenible.

Después calcula sensibilidad WACC/g y de drivers operativos. Si 70–90 % del enterprise value viene del terminal, dilo explícitamente: la valoración depende más de supuestos lejanos que del forecast cercano.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla señala el lente que debes buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Richard Brealey, Stewart Myers & Franklin Allen — *Principles of Corporate Finance* | valor del dinero, riesgo, costo de capital, inversión y financiación | ¿Qué supuesto de **valoración por flujos** ayuda a desafiar? |
| Stephen Ross, Randolph Westerfield et al. — *Corporate Finance* | decisiones de inversión, financiación, capital de trabajo y valoración | ¿Qué supuesto de **valoración por flujos** ayuda a desafiar? |
| Brad Feld & Jason Mendelson — *Venture Deals* | term sheets, economics/control y negociación de venture capital | ¿Qué supuesto de **valoración por flujos** ayuda a desafiar? |
| David Skok — *SaaS Metrics resources* | perspectiva de Unit economics aplicada al problema de la clase | ¿Qué supuesto de **valoración por flujos** ayuda a desafiar? |
| Ben Horowitz — *The Hard Thing About Hard Things* | decisiones difíciles de CEO, organización, personas y ejecución bajo presión | ¿Qué supuesto de **valoración por flujos** ayuda a desafiar? |

En **valoración por flujos**, la lectura se evalúa por **uso**, no por cantidad de páginas. La nota debe indicar qué tesis de las fuentes modifica tu lectura de **free cash flow**, qué evidencia del caso tensiona esa tesis y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación:** Un DCF justifica valoración de USD 200M, pero 78% proviene de terminal value con crecimiento perpetuo 6% en economía que crece 3% nominal.

**Paso 1 — proyectar drivers operativos.** La gerencia escribe primero el supuesto asociado a **free cash flow** y evita convertirlo en hecho. Luego busca **FCF** para contrastarlo en el caso de **valoración por flujos**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 2 — convertir beneficio a FCF.** La gerencia escribe primero el supuesto asociado a **DCF** y evita convertirlo en hecho. Luego busca **growth** para contrastarlo en el caso de **valoración por flujos**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 3 — estimar discount rate.** La gerencia escribe primero el supuesto asociado a **terminal value** y evita convertirlo en hecho. Luego busca **operating margin** para contrastarlo en el caso de **valoración por flujos**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 4 — calcular terminal value.** La gerencia escribe primero el supuesto asociado a **discount rate** y evita convertirlo en hecho. Luego busca **WACC** para contrastarlo en el caso de **valoración por flujos**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 5 — hacer sensibilidad y sanity checks.** La gerencia escribe primero el supuesto asociado a **NOPAT** y evita convertirlo en hecho. Luego busca **terminal value share** para contrastarlo en el caso de **valoración por flujos**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Síntesis del caso.** La recomendación debe terminar con responsable, fecha, evidencia de éxito y señal de stop. En **valoración por flujos**, omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo |
|---|---|---|---|
| **free cash flow** | efectivo generado después de inversión necesaria disponible para financiadores | Cuando FCF es observable y accionable. | Sobrerreaccionar a una señal parcial. |
| **DCF** | valor presente de flujos esperados | Cuando la primera explicación no distingue mecanismo o responsabilidad. | Convertir el concepto en etiqueta. |
| **Experimento/revisión** | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar eternamente y no decidir. |
| **Escalamiento** | Elevar autoridad o especialidad | Cuando hay derechos, capital material, regulación o irreversibilidad. | Delegar hacia arriba lo que sí corresponde decidir. |

**Frontera de aplicación:** DCF no crea información que no existe. Para startups o negocios en transición, escenarios y unit economics pueden ser más informativos que un punto de valoración.

## 🪜 De profesional a owner

| Nivel | Responsabilidad sobre valoración por flujos |
|---|---|
| **Profesional** | usa **valoración por flujos** para mejorar una contribución propia y explicar sus supuestos con evidencia. |
| **Jefe / Team Lead** | aplica **free cash flow** y **DCF** para coordinar personas sin sustituir conversación por métricas. |
| **Manager / Gerente** | conecta FCF con capacidad, presupuesto, dependencias y riesgo interáreas. |
| **CEO / Director** | decide si valoración por flujos cambia estrategia, economía o riesgo de empresa y qué debe llegar al comité o directorio. |
| **Founder / Owner** | pregunta si la solución de valoración por flujos reduce dependencia del fundador, preserva caja y puede operar como sistema repetible. |

El cambio de nivel en **valoración por flujos** aumenta el número de personas, dinero, dependencias y consecuencias que quedan dentro de la decisión. Por eso la misma herramienta debe volverse más explícita en evidencia, gobernanza y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Un DCF justifica valoración de USD 200M, pero 78% proviene de terminal value con crecimiento perpetuo 6% en economía que crece 3% nominal.

Entrega un **decision brief de valoración por flujos** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre personas, cliente, operación, caja y riesgo; (e) recomendación; (f) condición que haría cambiarla; (g) dueño y fecha de revisión. Utiliza al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica

1. Reconstruye el caso de **valoración por flujos** con una tabla `hecho / interpretación / hipótesis / decisión`.
2. Ejecuta **1. proyectar drivers operativos → 2. convertir beneficio a FCF → 3. estimar discount rate → 4. calcular terminal value → 5. hacer sensibilidad y sanity checks** y adjunta evidencia para cada transición entre pasos.
3. Calcula o documenta FCF, growth; si no existe dato, diseña cómo obtenerlo.
4. Escribe una alternativa que contradiga tu preferencia inicial y haz un *pre-mortem* específico del caso.
5. Lee dos referencias, registra una coincidencia y una tensión, y modifica el brief si corresponde.
6. Repite la decisión desde el rol de CEO/owner: identifica qué cambia al aumentar el alcance y la irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar free cash flow y DCF como sinónimos | Se pierde la distinción entre “efectivo generado después de inversión necesaria disponible para financiadores” y “valor presente de flujos esperados” | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por “hacer sensibilidad y sanity checks” | Se saltó “proyectar drivers operativos” y la solución llegó antes que el diagnóstico | Reconstruye la cadena 1. proyectar drivers operativos → 2. convertir beneficio a FCF → 3. estimar discount rate → 4. calcular terminal value → 5. hacer sensibilidad y sanity checks y marca el primer supuesto no demostrado. |
| Optimizar solo FCF | La métrica local sustituyó al resultado del sistema | Contrástala con growth y explicita el costo de oportunidad. |
| Generalizar desde un caso favorable | Se confundió evidencia local con una regla universal sobre valoración por flujos | DCF no crea información que no existe. Para startups o negocios en transición, escenarios y unit economics pueden ser más informativos que un punto de valoración. |
| No fijar revisión | Una decisión sobre valoración por flujos se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de stop. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **free cash flow** y **DCF** usando un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **terminal value** y qué observación obligaría a rechazar tu interpretación?
3. Aplica **proyectar drivers operativos → convertir beneficio a FCF** al caso de la clase. ¿Qué dato todavía falta?
4. ¿Por qué **FCF** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la tabla de lectura. ¿Dónde podrían llevar a recomendaciones distintas para **valoración por flujos**?
6. ¿Qué decisión equivocada podría producirse si se ignora este límite: **DCF no crea información que no existe. Para startups o negocios en transición, escenarios y unit economics pueden ser más informativos que un punto de valoración.**?

## 📥 Entregable

Guarda en `portfolio/220-valoracion-por-flujos/`:

- `modelo-financiero-y-memo-de-decision.md` con el problema específico de **valoración por flujos**, evidencia, alternativas, decisión y gobernanza;
- `reading-note.md` contrastando las fuentes de **valoración por flujos** con edición/páginas consultadas;
- `decision-journal.md` registrando los supuestos de **free cash flow**, confianza, responsable y revisión;
- `red-team.md` con la objeción más fuerte al caso **Un DCF justifica valoración de USD 200M, pero 78% proviene de terminal value con crecimiento perpetuo 6% en economía que crece 3% nominal.** y el dato que podría invalidar la recomendación.

## 📗 Fuentes y verificación

- Richard Brealey, Stewart Myers & Franklin Allen — *Principles of Corporate Finance*. **Uso en esta clase:** valor del dinero, riesgo, costo de capital, inversión y financiación. Lectura selectiva: índice/capítulos pertinentes a **valoración por flujos**; registra edición y páginas consultadas.
- Stephen Ross, Randolph Westerfield et al. — *Corporate Finance*. **Uso en esta clase:** decisiones de inversión, financiación, capital de trabajo y valoración. Lectura selectiva: índice/capítulos pertinentes a **valoración por flujos**; registra edición y páginas consultadas.
- Brad Feld & Jason Mendelson — *Venture Deals*. **Uso en esta clase:** term sheets, economics/control y negociación de venture capital. Lectura selectiva: índice/capítulos pertinentes a **valoración por flujos**; registra edición y páginas consultadas.
- David Skok — *SaaS Metrics resources*. **Uso en esta clase:** perspectiva de Unit economics aplicada al problema de la clase. Lectura selectiva: índice/capítulos pertinentes a **valoración por flujos**; registra edición y páginas consultadas.
- Ben Horowitz — *The Hard Thing About Hard Things*. **Uso en esta clase:** decisiones difíciles de CEO, organización, personas y ejecución bajo presión. Lectura selectiva: índice/capítulos pertinentes a **valoración por flujos**; registra edición y páginas consultadas.
- Tim Koller, Marc Goedhart & David Wessels — *Valuation: Measuring and Managing the Value of Companies*. **Uso en esta clase:** drivers de valor, ROIC, crecimiento y valoración por flujo descontado. Lectura selectiva: índice/capítulos pertinentes a **valoración por flujos**; registra edición y páginas consultadas.
- Susan A. Ambrose et al. — *How Learning Works*. **Uso en esta clase:** diseñar los objetivos, la práctica y el feedback de **valoración por flujos** sobre conocimiento previo verificable.
- Peter C. Brown, Henry L. Roediger III & Mark A. McDaniel — *Make It Stick*. **Uso en esta clase:** justificar la recuperación inicial y las preguntas de comprobación de **valoración por flujos**.
- Grant Wiggins & Jay McTighe — *Understanding by Design*. **Uso en esta clase:** derivar el entregable de **valoración por flujos** desde el desempeño observable y no desde el temario.
- Anders Ericsson & Robert Pool — *Peak*. **Uso en esta clase:** convertir la práctica de **valoración por flujos** en práctica deliberada con criterios explícitos.
- William Ellet — *The Case Study Handbook*. **Uso en esta clase:** estructurar el caso ejecutivo de **valoración por flujos** como problema, evidencia, alternativas y recomendación.

> **Regla de fuentes para Valoración por flujos:** las obras anteriores estructuran las perspectivas de esta materia; cualquier norma, ley, impuesto o estándar vivo mencionado en **valoración por flujos** debe comprobarse nuevamente en su fuente primaria vigente. El desarrollo es original y no reproduce capítulos protegidos.
