# Clase 076 — Estimación y capacidad

**Parte:** 06 — Proyectos, Agile y entrega  
**Nivel:** Etapa 2 — Jefe → Manager  
**Duración sugerida:** 150–180 minutos · **Estándar:** deep-class-v2

## 🎯 Propósito

Estimar combina incertidumbre de trabajo, capacidad y variabilidad. Una estimación es una distribución o rango, no una promesa automática. Equipos maduros distinguen effort, duration y throughput, calibran con historia y actualizan forecast a medida que aparece evidencia.

La salida de esta parte es **entregar proyectos con alcance, flujo, riesgo, calidad y gobernanza adaptativa**. En esta clase, esa progresión se concreta al exigir que cada afirmación sobre **estimación y capacidad** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

## 📚 Resultados de aprendizaje

Al finalizar podrás:

1. **Distinguir** `effort`, `duration`, `capacity`, `throughput`, `forecast` mediante observables, no por memoria verbal.
2. **Explicar** por qué esas distinciones cambian una decisión de jefe → manager.
3. **Aplicar** la secuencia **1. definir unidad de trabajo → 2. usar datos históricos comparables → 3. estimar rango y confianza → 4. modelar capacidad, dependencias y buffers → 5. actualizar forecast con throughput real** conservando supuestos, alternativas y trazabilidad.
4. **Interpretar** error de forecast, throughput, cycle time sin confundir señal, explicación y causalidad.
5. **Resolver** el caso ejecutivo con al menos dos opciones plausibles y un criterio explícito de stop/revisión.
6. **Contrastar** dos obras de referencia y explicar dónde sus lentes son complementarias o entran en tensión.

## 🧭 Agenda

| Tramo | Evidencia de aprendizaje |
|---|---|
| 0–20 min | Recuperación: define effort y duration sin mirar la tabla; corrige con la fuente. |
| 20–70 min | Lectura guiada de conceptos + contraste de dos referencias. |
| 70–115 min | Ejemplo trabajado con error de forecast y trazabilidad de supuestos. |
| 115–155 min | Caso ejecutivo: dos alternativas, trade-offs y decisión provisional. |
| 155–180 min | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar comprensión |
|---|---|---|
| **effort** | trabajo necesario medido en unidades de esfuerzo | Distingue un hecho compatible y otro que lo refute. |
| **duration** | tiempo calendario desde inicio a fin | Distingue un hecho compatible y otro que lo refute. |
| **capacity** | trabajo disponible de personas o sistemas por periodo | Distingue un hecho compatible y otro que lo refute. |
| **throughput** | unidades terminadas por periodo | Distingue un hecho compatible y otro que lo refute. |
| **forecast** | proyección actualizada basada en datos y supuestos | Distingue un hecho compatible y otro que lo refute. |

## 🧠 Modelo mental

```text
1. definir unidad de trabajo → 2. usar datos históricos comparables → 3. estimar rango y confianza → 4. modelar capacidad, dependencias y buffers → 5. actualizar forecast con throughput real
```

La secuencia nace del problema de esta clase: **Estimar combina incertidumbre de trabajo, capacidad y variabilidad. Una estimación es una distribución o rango, no una promesa automática. Equipos maduros distinguen effort, duration y throughput, calibran con historia y actualizan forecast a medida que aparece evidencia.** El método es útil mientras las condiciones permitan observar las señales requeridas. No elimina incertidumbre; la hace visible y obliga a decidir proporcionalmente a la evidencia. Límite principal: **No persigas precisión costosa para trabajo exploratorio. El objetivo de estimar es mejorar decisiones de alcance y fecha, no producir un número aparentemente exacto.**

## 📖 Desarrollo

### 1. effort: mecanismo central

**effort** se entiende aquí como **trabajo necesario medido en unidades de esfuerzo**. Esta es la pieza causal o estructural desde la que se inicia **estimación y capacidad**: antes de definir unidad de trabajo, el gerente debe poder señalar qué cambia en el sistema si el concepto está presente y qué debería observar si no lo está. Una definición que no produce predicciones observables todavía es demasiado vaga para dirigir.

La lectura rectora de este bloque es Project Management Institute — *A Guide to the Project Management Body of Knowledge (PMBOK Guide)*. Su aporte se usa para examinar **gobernanza, dominios de desempeño, riesgo, stakeholders y entrega de valor**. Aplica esa lente al caso sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **error de forecast**; regístrala con periodo, unidad, población y baseline.

Relaciona el mecanismo con **duration**. Si ambos cambian juntos, no concluyas causalidad automáticamente: identifica una tercera variable o mecanismo alternativo que también pueda explicar el patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. duration: frontera conceptual y error de clasificación

**Definición operacional:** tiempo calendario desde inicio a fin. Su valor está en distinguirlo de **effort** y **capacity**. En una decisión real, clasificar una situación en la categoría equivocada cambia la intervención: puedes asignar autoridad donde faltaba información, medir un output cuando debías observar un proceso o tratar una restricción como si fuera una preferencia.

Contrasta el problema con Harold Kerzner — *Project Management*, que aporta una mirada sobre **integración de proyectos, control, madurez y alineación organizacional**. Formula dos mini-casos: uno que sí satisface la definición de **duration** y otro que solo se parece superficialmente. Luego pregunta qué señal distinguiría ambos; para esta clase, **throughput** es una candidata, pero debe combinarse con evidencia cualitativa o documental cuando el fenómeno no sea directamente medible.

Antes de usar datos históricos comparables, registra explícitamente qué decisión sería errónea si esta frontera conceptual se ignora. Esa frase convierte el vocabulario en criterio gerencial.

### 3. capacity: operacionalización y medición

**capacity** significa **trabajo disponible de personas o sistemas por periodo**. El problema ya no es definirlo, sino **operacionalizarlo**: qué contar, durante qué ventana, con qué denominador, contra qué baseline y con qué segmentación. Una métrica útil conserva suficiente contexto para no confundir mejora local con mejora del sistema.

Gene Kim et al. — *The Phoenix Project* orienta este bloque mediante **perspectiva de Operaciones tecnológicas aplicada al problema de la clase**. Usa esa perspectiva para diseñar una ficha de medición: `señal → fórmula/criterio → fuente → frecuencia → owner → interpretación permitida → interpretación prohibida`. La señal asignada es **cycle time**. Si no existe un dato confiable, la salida correcta no es inventar precisión: diseña el mecanismo de captura y declara la incertidumbre.

Al llegar a estimar rango y confianza, compara tendencia, distribución y casos atípicos. Pregunta además si el indicador es *leading* o *lagging* y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; nunca convertirse en el objetivo que reemplaza al fenómeno.

### 4. throughput: trade-offs y efectos de segundo orden

**Definición:** unidades terminadas por periodo. Este concepto obliga a abandonar la idea de que **estimación y capacidad** tiene una solución gratuita. Toda intervención consume autonomía, tiempo, caja, capacidad, atención, reputación o tolerancia al riesgo. Por eso, antes de modelar capacidad, dependencias y buffers, se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Ken Schwaber & Jeff Sutherland — *The Scrum Guide* aporta una lente sobre **empirismo, transparencia, inspección y adaptación**. Úsala para construir una matriz `beneficio / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **capacity utilization** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la necesidad de observar efectos laterales fuera del KPI principal.

Haz un *pre-mortem* de **estimación y capacidad**: supone que la opción recomendada fracasó seis meses después y enumera tres mecanismos que podrían explicarlo. Al menos uno debe provenir de un efecto de segundo orden asociado a **throughput** y otro de una hipótesis del caso que nunca fue validada.

### 5. forecast: gobernanza, límites e integración

**forecast** se define como **proyección actualizada basada en datos y supuestos** y cierra el circuito porque traduce análisis en responsabilidad. La pregunta ejecutiva es quién decide, quién ejecuta, quién debe ser consultado, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar.

Nicole Forsgren, Jez Humble & Gene Kim — *Accelerate* se utiliza para estudiar **métricas de entrega, capacidades técnicas y desempeño organizacional** y contrastar la recomendación final. Al ejecutar actualizar forecast con throughput real, deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento. Esa trazabilidad protege contra el sesgo retrospectivo y mejora las revisiones posteriores.

La frontera de esta clase es explícita: **No persigas precisión costosa para trabajo exploratorio. El objetivo de estimar es mejorar decisiones de alcance y fecha, no producir un número aparentemente exacto.**. Conviértela en una regla operativa: `si ocurre X → no aplicar automáticamente → consultar/escalar/revalidar`. Integrar **effort**, **duration**, **capacity**, **throughput** y **forecast** significa poder explicar qué parte del diagnóstico sostiene la decisión y cuál sigue siendo una apuesta.

### 6. Integración: de conceptos a una decisión defendible

La síntesis de **estimación y capacidad** no consiste en sumar cinco definiciones. Empieza por **effort**, contrasta **duration** con **capacity**, incorpora **throughput** como restricción o mecanismo y usa **forecast** para cerrar el ciclo. Si el análisis no puede explicar cuál de esas piezas cambió la recomendación, todavía no hay comprensión transferible.

Aplica ahora la secuencia **1. definir unidad de trabajo → 2. usar datos históricos comparables → 3. estimar rango y confianza → 4. modelar capacidad, dependencias y buffers → 5. actualizar forecast con throughput real**. Para cada paso conserva tres columnas: evidencia utilizada, alternativa descartada y razón. Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado y evita reescribir la historia después de conocer el desenlace.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla señala el lente que debes buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Project Management Institute — *A Guide to the Project Management Body of Knowledge (PMBOK Guide)* | gobernanza, dominios de desempeño, riesgo, stakeholders y entrega de valor | ¿Qué supuesto de **estimación y capacidad** ayuda a desafiar? |
| Harold Kerzner — *Project Management* | integración de proyectos, control, madurez y alineación organizacional | ¿Qué supuesto de **estimación y capacidad** ayuda a desafiar? |
| Gene Kim et al. — *The Phoenix Project* | perspectiva de Operaciones tecnológicas aplicada al problema de la clase | ¿Qué supuesto de **estimación y capacidad** ayuda a desafiar? |
| Ken Schwaber & Jeff Sutherland — *The Scrum Guide* | empirismo, transparencia, inspección y adaptación | ¿Qué supuesto de **estimación y capacidad** ayuda a desafiar? |
| Nicole Forsgren, Jez Humble & Gene Kim — *Accelerate* | métricas de entrega, capacidades técnicas y desempeño organizacional | ¿Qué supuesto de **estimación y capacidad** ayuda a desafiar? |

En **estimación y capacidad**, la lectura se evalúa por **uso**, no por cantidad de páginas. La nota debe indicar qué tesis de las fuentes modifica tu lectura de **effort**, qué evidencia del caso tensiona esa tesis y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación:** Un backlog de 120 ítems se estima en 12 semanas porque diez personas 'harán un ítem por semana'. Los datos históricos muestran variabilidad 2–8 días y trabajo bloqueado por QA.

**Paso 1 — definir unidad de trabajo.** La gerencia escribe primero el supuesto asociado a **effort** y evita convertirlo en hecho. Luego busca **error de forecast** para contrastarlo en el caso de **estimación y capacidad**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 2 — usar datos históricos comparables.** La gerencia escribe primero el supuesto asociado a **duration** y evita convertirlo en hecho. Luego busca **throughput** para contrastarlo en el caso de **estimación y capacidad**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 3 — estimar rango y confianza.** La gerencia escribe primero el supuesto asociado a **capacity** y evita convertirlo en hecho. Luego busca **cycle time** para contrastarlo en el caso de **estimación y capacidad**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 4 — modelar capacidad, dependencias y buffers.** La gerencia escribe primero el supuesto asociado a **throughput** y evita convertirlo en hecho. Luego busca **capacity utilization** para contrastarlo en el caso de **estimación y capacidad**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 5 — actualizar forecast con throughput real.** La gerencia escribe primero el supuesto asociado a **forecast** y evita convertirlo en hecho. Luego busca **variance** para contrastarlo en el caso de **estimación y capacidad**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Síntesis del caso.** La recomendación debe terminar con responsable, fecha, evidencia de éxito y señal de stop. En **estimación y capacidad**, omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo |
|---|---|---|---|
| **effort** | trabajo necesario medido en unidades de esfuerzo | Cuando error de forecast es observable y accionable. | Sobrerreaccionar a una señal parcial. |
| **duration** | tiempo calendario desde inicio a fin | Cuando la primera explicación no distingue mecanismo o responsabilidad. | Convertir el concepto en etiqueta. |
| **Experimento/revisión** | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar eternamente y no decidir. |
| **Escalamiento** | Elevar autoridad o especialidad | Cuando hay derechos, capital material, regulación o irreversibilidad. | Delegar hacia arriba lo que sí corresponde decidir. |

**Frontera de aplicación:** No persigas precisión costosa para trabajo exploratorio. El objetivo de estimar es mejorar decisiones de alcance y fecha, no producir un número aparentemente exacto.

## 🪜 De profesional a owner

| Nivel | Responsabilidad sobre estimación y capacidad |
|---|---|
| **Profesional** | usa **estimación y capacidad** para mejorar una contribución propia y explicar sus supuestos con evidencia. |
| **Jefe / Team Lead** | aplica **effort** y **duration** para coordinar personas sin sustituir conversación por métricas. |
| **Manager / Gerente** | conecta error de forecast con capacidad, presupuesto, dependencias y riesgo interáreas. |
| **CEO / Director** | decide si estimación y capacidad cambia estrategia, economía o riesgo de empresa y qué debe llegar al comité o directorio. |
| **Founder / Owner** | pregunta si la solución de estimación y capacidad reduce dependencia del fundador, preserva caja y puede operar como sistema repetible. |

El cambio de nivel en **estimación y capacidad** aumenta el número de personas, dinero, dependencias y consecuencias que quedan dentro de la decisión. Por eso la misma herramienta debe volverse más explícita en evidencia, gobernanza y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Un backlog de 120 ítems se estima en 12 semanas porque diez personas 'harán un ítem por semana'. Los datos históricos muestran variabilidad 2–8 días y trabajo bloqueado por QA.

Entrega un **decision brief de estimación y capacidad** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre personas, cliente, operación, caja y riesgo; (e) recomendación; (f) condición que haría cambiarla; (g) dueño y fecha de revisión. Utiliza al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica

1. Reconstruye el caso de **estimación y capacidad** con una tabla `hecho / interpretación / hipótesis / decisión`.
2. Ejecuta **1. definir unidad de trabajo → 2. usar datos históricos comparables → 3. estimar rango y confianza → 4. modelar capacidad, dependencias y buffers → 5. actualizar forecast con throughput real** y adjunta evidencia para cada transición entre pasos.
3. Calcula o documenta error de forecast, throughput; si no existe dato, diseña cómo obtenerlo.
4. Escribe una alternativa que contradiga tu preferencia inicial y haz un *pre-mortem* específico del caso.
5. Lee dos referencias, registra una coincidencia y una tensión, y modifica el brief si corresponde.
6. Repite la decisión desde el rol de CEO/owner: identifica qué cambia al aumentar el alcance y la irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar effort y duration como sinónimos | Se pierde la distinción entre “trabajo necesario medido en unidades de esfuerzo” y “tiempo calendario desde inicio a fin” | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por “actualizar forecast con throughput real” | Se saltó “definir unidad de trabajo” y la solución llegó antes que el diagnóstico | Reconstruye la cadena 1. definir unidad de trabajo → 2. usar datos históricos comparables → 3. estimar rango y confianza → 4. modelar capacidad, dependencias y buffers → 5. actualizar forecast con throughput real y marca el primer supuesto no demostrado. |
| Optimizar solo error de forecast | La métrica local sustituyó al resultado del sistema | Contrástala con throughput y explicita el costo de oportunidad. |
| Generalizar desde un caso favorable | Se confundió evidencia local con una regla universal sobre estimación y capacidad | No persigas precisión costosa para trabajo exploratorio. El objetivo de estimar es mejorar decisiones de alcance y fecha, no producir un número aparentemente exacto. |
| No fijar revisión | Una decisión sobre estimación y capacidad se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de stop. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **effort** y **duration** usando un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **capacity** y qué observación obligaría a rechazar tu interpretación?
3. Aplica **definir unidad de trabajo → usar datos históricos comparables** al caso de la clase. ¿Qué dato todavía falta?
4. ¿Por qué **error de forecast** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la tabla de lectura. ¿Dónde podrían llevar a recomendaciones distintas para **estimación y capacidad**?
6. ¿Qué decisión equivocada podría producirse si se ignora este límite: **No persigas precisión costosa para trabajo exploratorio. El objetivo de estimar es mejorar decisiones de alcance y fecha, no producir un número aparentemente exacto.**?

## 📥 Entregable

Guarda en `portfolio/076-estimacion-y-capacidad/`:

- `operating-improvement-brief.md` con el problema específico de **estimación y capacidad**, evidencia, alternativas, decisión y gobernanza;
- `reading-note.md` contrastando las fuentes de **estimación y capacidad** con edición/páginas consultadas;
- `decision-journal.md` registrando los supuestos de **effort**, confianza, responsable y revisión;
- `red-team.md` con la objeción más fuerte al caso **Un backlog de 120 ítems se estima en 12 semanas porque diez personas 'harán un ítem por semana'. Los datos históricos muestran variabilidad 2–8 días y trabajo bloqueado por QA.** y el dato que podría invalidar la recomendación.

## 📗 Fuentes y verificación

- Project Management Institute — *A Guide to the Project Management Body of Knowledge (PMBOK Guide)* (1996). **Uso en esta clase:** gobernanza, dominios de desempeño, riesgo, stakeholders y entrega de valor. Lectura selectiva sobre **estimación y capacidad**. **Localizador:** [ISBN-13 9781880410127](https://openlibrary.org/isbn/9781880410127).
- Harold Kerzner — *Project Management* (John Wiley & Sons Inc, 2003). **Uso en esta clase:** integración de proyectos, control, madurez y alineación organizacional. Lectura selectiva sobre **estimación y capacidad**. **Localizador:** [ISBN-13 9780471281580](https://openlibrary.org/isbn/9780471281580).
- Gene Kim et al. — *The Phoenix Project* (IT Revolution Press, 2018). **Uso en esta clase:** perspectiva de Operaciones tecnológicas aplicada al problema de la clase. Lectura selectiva sobre **estimación y capacidad**. **Localizador:** [ISBN-13 9781942788294](https://openlibrary.org/isbn/9781942788294).
- Ken Schwaber & Jeff Sutherland — *The Scrum Guide* (Scrum.org / Scrum Alliance). **Uso en esta clase:** empirismo, transparencia, inspección y adaptación. **Fuente primaria:** <https://scrumguides.org/>.
- Nicole Forsgren, Jez Humble & Gene Kim — *Accelerate* (IT Revolution Press, 2018). **Uso en esta clase:** métricas de entrega, capacidades técnicas y desempeño organizacional. Lectura selectiva sobre **estimación y capacidad**. **Localizador:** [ISBN-13 9781942788379](https://openlibrary.org/isbn/9781942788379).
- David J. Anderson — *Kanban* (Blue hole press, 2010). **Uso en esta clase:** flujo, trabajo en proceso, políticas explícitas y evolución del sistema. Lectura selectiva sobre **estimación y capacidad**. **Localizador:** [ISBN-13 9780984521401](https://openlibrary.org/isbn/9780984521401).
- Susan A. Ambrose et al. — *How Learning Works* (John Wiley & Sons, Incorporated, 2010). **Uso en esta clase:** diseñar los objetivos, la práctica y el feedback de **estimación y capacidad** sobre conocimiento previo verificable. **Localizador:** [ISBN-13 9780470617601](https://openlibrary.org/isbn/9780470617601).
- Peter C. Brown, Henry L. Roediger III & Mark A. McDaniel — *Make It Stick* (Harvard University Press, 2014). **Uso en esta clase:** justificar la recuperación inicial y las preguntas de comprobación de **estimación y capacidad**. **Localizador:** [ISBN-13 9780674986572](https://openlibrary.org/isbn/9780674986572).
- Grant Wiggins & Jay McTighe — *Understanding by Design* (Pearson Education, Inc., 2006). **Uso en esta clase:** derivar el entregable de **estimación y capacidad** desde el desempeño observable y no desde el temario. **Localizador:** [ISBN-13 9780131950849](https://openlibrary.org/isbn/9780131950849).
- Anders Ericsson & Robert Pool — *Peak* (Penguin Random House, 2016). **Uso en esta clase:** convertir la práctica de **estimación y capacidad** en práctica deliberada con criterios explícitos. **Localizador:** [ISBN-13 9781473513143](https://openlibrary.org/isbn/9781473513143).
- William Ellet — *The Case Study Handbook* (Harvard Business Review Press, 2018). **Uso en esta clase:** estructurar el caso ejecutivo de **estimación y capacidad** como problema, evidencia, alternativas y recomendación. **Localizador:** [ISBN-13 9781633696150](https://openlibrary.org/isbn/9781633696150).

> **Regla de fuentes para Estimación y capacidad:** las obras anteriores estructuran las perspectivas de esta materia; cualquier norma, ley, impuesto o estándar vivo mencionado en **estimación y capacidad** debe comprobarse nuevamente en su fuente primaria vigente. El desarrollo es original y no reproduce capítulos protegidos.
