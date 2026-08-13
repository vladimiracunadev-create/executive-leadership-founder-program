# Clase 107 — Escalamiento y gestión por excepción

**Parte:** 08 — Sistemas de gestión, KPI y OKR  
**Nivel:** Etapa 3 — Manager → Gerente  
**Duración sugerida:** 150–180 minutos · **Estándar:** deep-class-v2

## 🎯 Propósito

Escalar por excepción permite que niveles superiores se ocupen de decisiones que exceden tolerancias, no de toda operación. Requiere límites claros de costo, tiempo, riesgo o calidad y una cultura donde escalar temprano no sea castigo. Sin límites, se microgestiona o se ocultan problemas hasta ser crisis.

La salida de esta parte es **dirigir mediante outcomes, métricas, revisiones y asignación explícita de recursos**. En esta clase, esa progresión se concreta al exigir que cada afirmación sobre **escalamiento y gestión por excepción** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

## 📚 Resultados de aprendizaje

Al finalizar podrás:

1. **Distinguir** `tolerance`, `exception`, `threshold`, `decision right`, `early warning` mediante observables, no por memoria verbal.
2. **Explicar** por qué esas distinciones cambian una decisión de manager → gerente.
3. **Aplicar** la secuencia **1. definir tolerancias por objetivo → 2. asignar derechos de decisión → 3. instrumentar early warnings → 4. escalar con opciones y recomendación → 5. revisar umbrales según aprendizaje** conservando supuestos, alternativas y trazabilidad.
4. **Interpretar** breaches, late escalations, false escalations sin confundir señal, explicación y causalidad.
5. **Resolver** el caso ejecutivo con al menos dos opciones plausibles y un criterio explícito de stop/revisión.
6. **Contrastar** dos obras de referencia y explicar dónde sus lentes son complementarias o entran en tensión.

## 🧭 Agenda

| Tramo | Evidencia de aprendizaje |
|---|---|
| 0–20 min | Recuperación: define tolerance y exception sin mirar la tabla; corrige con la fuente. |
| 20–70 min | Lectura guiada de conceptos + contraste de dos referencias. |
| 70–115 min | Ejemplo trabajado con breaches y trazabilidad de supuestos. |
| 115–155 min | Caso ejecutivo: dos alternativas, trade-offs y decisión provisional. |
| 155–180 min | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar comprensión |
|---|---|---|
| **tolerance** | rango dentro del cual un equipo puede decidir sin escalar | Distingue un hecho compatible y otro que lo refute. |
| **exception** | desviación material fuera de tolerancia | Distingue un hecho compatible y otro que lo refute. |
| **threshold** | valor observable que activa escalamiento | Distingue un hecho compatible y otro que lo refute. |
| **decision right** | autoridad definida para resolver una clase de excepción | Distingue un hecho compatible y otro que lo refute. |
| **early warning** | señal previa al breach | Distingue un hecho compatible y otro que lo refute. |

## 🧠 Modelo mental

```text
1. definir tolerancias por objetivo → 2. asignar derechos de decisión → 3. instrumentar early warnings → 4. escalar con opciones y recomendación → 5. revisar umbrales según aprendizaje
```

La secuencia nace del problema de esta clase: **Escalar por excepción permite que niveles superiores se ocupen de decisiones que exceden tolerancias, no de toda operación. Requiere límites claros de costo, tiempo, riesgo o calidad y una cultura donde escalar temprano no sea castigo. Sin límites, se microgestiona o se ocultan problemas hasta ser crisis.** El método es útil mientras las condiciones permitan observar las señales requeridas. No elimina incertidumbre; la hace visible y obliga a decidir proporcionalmente a la evidencia. Límite principal: **Tolerancias demasiado amplias pueden esconder deterioro; demasiado estrechas destruyen autonomía. Ajusta al riesgo, madurez y capacidad de corrección.**

## 📖 Desarrollo

### 1. tolerance: mecanismo central

**tolerance** se entiende aquí como **rango dentro del cual un equipo puede decidir sin escalar**. Esta es la pieza causal o estructural desde la que se inicia **escalamiento y gestión por excepción**: antes de definir tolerancias por objetivo, el gerente debe poder señalar qué cambia en el sistema si el concepto está presente y qué debería observar si no lo está. Una definición que no produce predicciones observables todavía es demasiado vaga para dirigir.

La lectura rectora de este bloque es John Doerr — *Measure What Matters*. Su aporte se usa para examinar **objetivos, resultados clave, foco, transparencia y cadencia de seguimiento**. Aplica esa lente al caso sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **breaches**; regístrala con periodo, unidad, población y baseline.

Relaciona el mecanismo con **exception**. Si ambos cambian juntos, no concluyas causalidad automáticamente: identifica una tercera variable o mecanismo alternativo que también pueda explicar el patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. exception: frontera conceptual y error de clasificación

**Definición operacional:** desviación material fuera de tolerancia. Su valor está en distinguirlo de **tolerance** y **threshold**. En una decisión real, clasificar una situación en la categoría equivocada cambia la intervención: puedes asignar autoridad donde faltaba información, medir un output cuando debías observar un proceso o tratar una restricción como si fuera una preferencia.

Contrasta el problema con Robert S. Kaplan & David P. Norton — *The Balanced Scorecard*, que aporta una mirada sobre **traducción de estrategia a objetivos, indicadores y relaciones causales**. Formula dos mini-casos: uno que sí satisface la definición de **exception** y otro que solo se parece superficialmente. Luego pregunta qué señal distinguiría ambos; para esta clase, **late escalations** es una candidata, pero debe combinarse con evidencia cualitativa o documental cuando el fenómeno no sea directamente medible.

Antes de asignar derechos de decisión, registra explícitamente qué decisión sería errónea si esta frontera conceptual se ignora. Esa frase convierte el vocabulario en criterio gerencial.

### 3. threshold: operacionalización y medición

**threshold** significa **valor observable que activa escalamiento**. El problema ya no es definirlo, sino **operacionalizarlo**: qué contar, durante qué ventana, con qué denominador, contra qué baseline y con qué segmentación. Una métrica útil conserva suficiente contexto para no confundir mejora local con mejora del sistema.

John Doerr — *Speed & Scale* orienta este bloque mediante **perspectiva de Ejecución aplicada al problema de la clase**. Usa esa perspectiva para diseñar una ficha de medición: `señal → fórmula/criterio → fuente → frecuencia → owner → interpretación permitida → interpretación prohibida`. La señal asignada es **false escalations**. Si no existe un dato confiable, la salida correcta no es inventar precisión: diseña el mecanismo de captura y declara la incertidumbre.

Al llegar a instrumentar early warnings, compara tendencia, distribución y casos atípicos. Pregunta además si el indicador es *leading* o *lagging* y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; nunca convertirse en el objetivo que reemplaza al fenómeno.

### 4. decision right: trade-offs y efectos de segundo orden

**Definición:** autoridad definida para resolver una clase de excepción. Este concepto obliga a abandonar la idea de que **escalamiento y gestión por excepción** tiene una solución gratuita. Toda intervención consume autonomía, tiempo, caja, capacidad, atención, reputación o tolerancia al riesgo. Por eso, antes de escalar con opciones y recomendación, se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Andrew S. Grove — *High Output Management* aporta una lente sobre **output managerial, leverage, reuniones, indicadores y gestión por procesos**. Úsala para construir una matriz `beneficio / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **decision latency** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la necesidad de observar efectos laterales fuera del KPI principal.

Haz un *pre-mortem* de **escalamiento y gestión por excepción**: supone que la opción recomendada fracasó seis meses después y enumera tres mecanismos que podrían explicarlo. Al menos uno debe provenir de un efecto de segundo orden asociado a **decision right** y otro de una hipótesis del caso que nunca fue validada.

### 5. early warning: gobernanza, límites e integración

**early warning** se define como **señal previa al breach** y cierra el circuito porque traduce análisis en responsabilidad. La pregunta ejecutiva es quién decide, quién ejecuta, quién debe ser consultado, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar.

Larry Bossidy & Ram Charan — *Execution* se utiliza para estudiar **disciplina de ejecución, personas, estrategia y operaciones** y contrastar la recomendación final. Al ejecutar revisar umbrales según aprendizaje, deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento. Esa trazabilidad protege contra el sesgo retrospectivo y mejora las revisiones posteriores.

La frontera de esta clase es explícita: **Tolerancias demasiado amplias pueden esconder deterioro; demasiado estrechas destruyen autonomía. Ajusta al riesgo, madurez y capacidad de corrección.**. Conviértela en una regla operativa: `si ocurre X → no aplicar automáticamente → consultar/escalar/revalidar`. Integrar **tolerance**, **exception**, **threshold**, **decision right** y **early warning** significa poder explicar qué parte del diagnóstico sostiene la decisión y cuál sigue siendo una apuesta.

### 6. Integración: de conceptos a una decisión defendible

La síntesis de **escalamiento y gestión por excepción** no consiste en sumar cinco definiciones. Empieza por **tolerance**, contrasta **exception** con **threshold**, incorpora **decision right** como restricción o mecanismo y usa **early warning** para cerrar el ciclo. Si el análisis no puede explicar cuál de esas piezas cambió la recomendación, todavía no hay comprensión transferible.

Aplica ahora la secuencia **1. definir tolerancias por objetivo → 2. asignar derechos de decisión → 3. instrumentar early warnings → 4. escalar con opciones y recomendación → 5. revisar umbrales según aprendizaje**. Para cada paso conserva tres columnas: evidencia utilizada, alternativa descartada y razón. Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado y evita reescribir la historia después de conocer el desenlace.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla señala el lente que debes buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| John Doerr — *Measure What Matters* | objetivos, resultados clave, foco, transparencia y cadencia de seguimiento | ¿Qué supuesto de **escalamiento y gestión por excepción** ayuda a desafiar? |
| Robert S. Kaplan & David P. Norton — *The Balanced Scorecard* | traducción de estrategia a objetivos, indicadores y relaciones causales | ¿Qué supuesto de **escalamiento y gestión por excepción** ayuda a desafiar? |
| John Doerr — *Speed & Scale* | perspectiva de Ejecución aplicada al problema de la clase | ¿Qué supuesto de **escalamiento y gestión por excepción** ayuda a desafiar? |
| Andrew S. Grove — *High Output Management* | output managerial, leverage, reuniones, indicadores y gestión por procesos | ¿Qué supuesto de **escalamiento y gestión por excepción** ayuda a desafiar? |
| Larry Bossidy & Ram Charan — *Execution* | disciplina de ejecución, personas, estrategia y operaciones | ¿Qué supuesto de **escalamiento y gestión por excepción** ayuda a desafiar? |

En **escalamiento y gestión por excepción**, la lectura se evalúa por **uso**, no por cantidad de páginas. La nota debe indicar qué tesis de las fuentes modifica tu lectura de **tolerance**, qué evidencia del caso tensiona esa tesis y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación:** Un proyecto puede variar 5% de presupuesto sin aprobación, pero nadie sabe el límite de fecha. El PM oculta un retraso de tres semanas porque espera recuperarlo.

**Paso 1 — definir tolerancias por objetivo.** La gerencia escribe primero el supuesto asociado a **tolerance** y evita convertirlo en hecho. Luego busca **breaches** para contrastarlo en el caso de **escalamiento y gestión por excepción**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 2 — asignar derechos de decisión.** La gerencia escribe primero el supuesto asociado a **exception** y evita convertirlo en hecho. Luego busca **late escalations** para contrastarlo en el caso de **escalamiento y gestión por excepción**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 3 — instrumentar early warnings.** La gerencia escribe primero el supuesto asociado a **threshold** y evita convertirlo en hecho. Luego busca **false escalations** para contrastarlo en el caso de **escalamiento y gestión por excepción**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 4 — escalar con opciones y recomendación.** La gerencia escribe primero el supuesto asociado a **decision right** y evita convertirlo en hecho. Luego busca **decision latency** para contrastarlo en el caso de **escalamiento y gestión por excepción**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 5 — revisar umbrales según aprendizaje.** La gerencia escribe primero el supuesto asociado a **early warning** y evita convertirlo en hecho. Luego busca **management attention** para contrastarlo en el caso de **escalamiento y gestión por excepción**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Síntesis del caso.** La recomendación debe terminar con responsable, fecha, evidencia de éxito y señal de stop. En **escalamiento y gestión por excepción**, omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo |
|---|---|---|---|
| **tolerance** | rango dentro del cual un equipo puede decidir sin escalar | Cuando breaches es observable y accionable. | Sobrerreaccionar a una señal parcial. |
| **exception** | desviación material fuera de tolerancia | Cuando la primera explicación no distingue mecanismo o responsabilidad. | Convertir el concepto en etiqueta. |
| **Experimento/revisión** | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar eternamente y no decidir. |
| **Escalamiento** | Elevar autoridad o especialidad | Cuando hay derechos, capital material, regulación o irreversibilidad. | Delegar hacia arriba lo que sí corresponde decidir. |

**Frontera de aplicación:** Tolerancias demasiado amplias pueden esconder deterioro; demasiado estrechas destruyen autonomía. Ajusta al riesgo, madurez y capacidad de corrección.

## 🪜 De profesional a owner

| Nivel | Responsabilidad sobre escalamiento y gestión por excepción |
|---|---|
| **Profesional** | usa **escalamiento y gestión por excepción** para mejorar una contribución propia y explicar sus supuestos con evidencia. |
| **Jefe / Team Lead** | aplica **tolerance** y **exception** para coordinar personas sin sustituir conversación por métricas. |
| **Manager / Gerente** | conecta breaches con capacidad, presupuesto, dependencias y riesgo interáreas. |
| **CEO / Director** | decide si escalamiento y gestión por excepción cambia estrategia, economía o riesgo de empresa y qué debe llegar al comité o directorio. |
| **Founder / Owner** | pregunta si la solución de escalamiento y gestión por excepción reduce dependencia del fundador, preserva caja y puede operar como sistema repetible. |

El cambio de nivel en **escalamiento y gestión por excepción** aumenta el número de personas, dinero, dependencias y consecuencias que quedan dentro de la decisión. Por eso la misma herramienta debe volverse más explícita en evidencia, gobernanza y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Un proyecto puede variar 5% de presupuesto sin aprobación, pero nadie sabe el límite de fecha. El PM oculta un retraso de tres semanas porque espera recuperarlo.

Entrega un **decision brief de escalamiento y gestión por excepción** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre personas, cliente, operación, caja y riesgo; (e) recomendación; (f) condición que haría cambiarla; (g) dueño y fecha de revisión. Utiliza al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica

1. Reconstruye el caso de **escalamiento y gestión por excepción** con una tabla `hecho / interpretación / hipótesis / decisión`.
2. Ejecuta **1. definir tolerancias por objetivo → 2. asignar derechos de decisión → 3. instrumentar early warnings → 4. escalar con opciones y recomendación → 5. revisar umbrales según aprendizaje** y adjunta evidencia para cada transición entre pasos.
3. Calcula o documenta breaches, late escalations; si no existe dato, diseña cómo obtenerlo.
4. Escribe una alternativa que contradiga tu preferencia inicial y haz un *pre-mortem* específico del caso.
5. Lee dos referencias, registra una coincidencia y una tensión, y modifica el brief si corresponde.
6. Repite la decisión desde el rol de CEO/owner: identifica qué cambia al aumentar el alcance y la irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar tolerance y exception como sinónimos | Se pierde la distinción entre “rango dentro del cual un equipo puede decidir sin escalar” y “desviación material fuera de tolerancia” | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por “revisar umbrales según aprendizaje” | Se saltó “definir tolerancias por objetivo” y la solución llegó antes que el diagnóstico | Reconstruye la cadena 1. definir tolerancias por objetivo → 2. asignar derechos de decisión → 3. instrumentar early warnings → 4. escalar con opciones y recomendación → 5. revisar umbrales según aprendizaje y marca el primer supuesto no demostrado. |
| Optimizar solo breaches | La métrica local sustituyó al resultado del sistema | Contrástala con late escalations y explicita el costo de oportunidad. |
| Generalizar desde un caso favorable | Se confundió evidencia local con una regla universal sobre escalamiento y gestión por excepción | Tolerancias demasiado amplias pueden esconder deterioro; demasiado estrechas destruyen autonomía. Ajusta al riesgo, madurez y capacidad de corrección. |
| No fijar revisión | Una decisión sobre escalamiento y gestión por excepción se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de stop. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **tolerance** y **exception** usando un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **threshold** y qué observación obligaría a rechazar tu interpretación?
3. Aplica **definir tolerancias por objetivo → asignar derechos de decisión** al caso de la clase. ¿Qué dato todavía falta?
4. ¿Por qué **breaches** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la tabla de lectura. ¿Dónde podrían llevar a recomendaciones distintas para **escalamiento y gestión por excepción**?
6. ¿Qué decisión equivocada podría producirse si se ignora este límite: **Tolerancias demasiado amplias pueden esconder deterioro; demasiado estrechas destruyen autonomía. Ajusta al riesgo, madurez y capacidad de corrección.**?

## 📥 Entregable

Guarda en `portfolio/107-escalamiento-y-gestion-por-excepcion/`:

- `leadership-decision-brief.md` con el problema específico de **escalamiento y gestión por excepción**, evidencia, alternativas, decisión y gobernanza;
- `reading-note.md` contrastando las fuentes de **escalamiento y gestión por excepción** con edición/páginas consultadas;
- `decision-journal.md` registrando los supuestos de **tolerance**, confianza, responsable y revisión;
- `red-team.md` con la objeción más fuerte al caso **Un proyecto puede variar 5% de presupuesto sin aprobación, pero nadie sabe el límite de fecha. El PM oculta un retraso de tres semanas porque espera recuperarlo.** y el dato que podría invalidar la recomendación.

## 📗 Fuentes y verificación

- John Doerr — *Measure What Matters*. **Uso en esta clase:** objetivos, resultados clave, foco, transparencia y cadencia de seguimiento. Lectura selectiva: índice/capítulos pertinentes a **escalamiento y gestión por excepción**; registra edición y páginas consultadas.
- Robert S. Kaplan & David P. Norton — *The Balanced Scorecard*. **Uso en esta clase:** traducción de estrategia a objetivos, indicadores y relaciones causales. Lectura selectiva: índice/capítulos pertinentes a **escalamiento y gestión por excepción**; registra edición y páginas consultadas.
- John Doerr — *Speed & Scale*. **Uso en esta clase:** perspectiva de Ejecución aplicada al problema de la clase. Lectura selectiva: índice/capítulos pertinentes a **escalamiento y gestión por excepción**; registra edición y páginas consultadas.
- Andrew S. Grove — *High Output Management*. **Uso en esta clase:** output managerial, leverage, reuniones, indicadores y gestión por procesos. Lectura selectiva: índice/capítulos pertinentes a **escalamiento y gestión por excepción**; registra edición y páginas consultadas.
- Larry Bossidy & Ram Charan — *Execution*. **Uso en esta clase:** disciplina de ejecución, personas, estrategia y operaciones. Lectura selectiva: índice/capítulos pertinentes a **escalamiento y gestión por excepción**; registra edición y páginas consultadas.
- Bernard Marr — *Key Performance Indicators*. **Uso en esta clase:** selección de métricas útiles y conexión entre indicadores y decisiones. Lectura selectiva: índice/capítulos pertinentes a **escalamiento y gestión por excepción**; registra edición y páginas consultadas.
- Susan A. Ambrose et al. — *How Learning Works*. Diseño de objetivos, práctica y feedback.
- Peter C. Brown, Henry L. Roediger III & Mark A. McDaniel — *Make It Stick*. Recuperación, elaboración y transferencia.
- Grant Wiggins & Jay McTighe — *Understanding by Design*. Diseño inverso desde desempeño observable.
- Anders Ericsson & Robert Pool — *Peak*. Práctica deliberada con criterios y retroalimentación.
- William Ellet — *The Case Study Handbook*. Análisis de problema/decisión, evidencia y recomendación.

> **Regla de fuentes para Escalamiento y gestión por excepción:** las obras anteriores estructuran las perspectivas de esta materia; cualquier norma, ley, impuesto o estándar vivo mencionado en **escalamiento y gestión por excepción** debe comprobarse nuevamente en su fuente primaria vigente. El desarrollo es original y no reproduce capítulos protegidos.
