# Clase 075 — Work breakdown y planificación

**Parte:** 06 — Proyectos, Agile y entrega  
**Nivel:** Etapa 2 — Jefe → Manager  
**Duración sugerida:** 150–180 minutos · **Estándar:** deep-class-v2

## 🎯 Propósito

Work Breakdown Structure descompone entregables en trabajo manejable; no es una lista de tareas cronológica. La planificación conecta alcance, dependencias, recursos y hitos, permitiendo ver qué trabajo controla el camino y qué paquetes requieren detalle posterior.

La salida de esta parte es **entregar proyectos con alcance, flujo, riesgo, calidad y gobernanza adaptativa**. En esta clase, esa progresión se concreta al exigir que cada afirmación sobre **work breakdown y planificación** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

## 📚 Resultados de aprendizaje

Al finalizar podrás:

1. **Distinguir** `WBS`, `work package`, `dependency`, `milestone`, `critical path` mediante observables, no por memoria verbal.
2. **Explicar** por qué esas distinciones cambian una decisión de jefe → manager.
3. **Aplicar** la secuencia **1. partir de entregables → 2. descomponer hasta paquetes gestionables → 3. mapear dependencias → 4. estimar secuencia y recursos → 5. identificar critical path y hitos** conservando supuestos, alternativas y trazabilidad.
4. **Interpretar** paquetes sin owner, dependencias tardías, critical path changes sin confundir señal, explicación y causalidad.
5. **Resolver** el caso ejecutivo con al menos dos opciones plausibles y un criterio explícito de stop/revisión.
6. **Contrastar** dos obras de referencia y explicar dónde sus lentes son complementarias o entran en tensión.

## 🧭 Agenda

| Tramo | Evidencia de aprendizaje |
|---|---|
| 0–20 min | Recuperación: define WBS y work package sin mirar la tabla; corrige con la fuente. |
| 20–70 min | Lectura guiada de conceptos + contraste de dos referencias. |
| 70–115 min | Ejemplo trabajado con paquetes sin owner y trazabilidad de supuestos. |
| 115–155 min | Caso ejecutivo: dos alternativas, trade-offs y decisión provisional. |
| 155–180 min | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar comprensión |
|---|---|---|
| **WBS** | descomposición jerárquica orientada a entregables | Distingue un hecho compatible y otro que lo refute. |
| **work package** | unidad gestionable con resultado y estimación | Distingue un hecho compatible y otro que lo refute. |
| **dependency** | relación donde un trabajo condiciona otro | Distingue un hecho compatible y otro que lo refute. |
| **milestone** | evento sin duración que marca un punto verificable | Distingue un hecho compatible y otro que lo refute. |
| **critical path** | secuencia cuya demora afecta fecha final | Distingue un hecho compatible y otro que lo refute. |

## 🧠 Modelo mental

```text
1. partir de entregables → 2. descomponer hasta paquetes gestionables → 3. mapear dependencias → 4. estimar secuencia y recursos → 5. identificar critical path y hitos
```

La secuencia nace del problema de esta clase: **Work Breakdown Structure descompone entregables en trabajo manejable; no es una lista de tareas cronológica. La planificación conecta alcance, dependencias, recursos y hitos, permitiendo ver qué trabajo controla el camino y qué paquetes requieren detalle posterior.** El método es útil mientras las condiciones permitan observar las señales requeridas. No elimina incertidumbre; la hace visible y obliga a decidir proporcionalmente a la evidencia. Límite principal: **Descomponer en exceso produce falsa precisión y alto mantenimiento. El horizonte cercano necesita más detalle que el lejano; usa rolling-wave planning.**

## 📖 Desarrollo

### 1. WBS: mecanismo central

**WBS** se entiende aquí como **descomposición jerárquica orientada a entregables**. Esta es la pieza causal o estructural desde la que se inicia **work breakdown y planificación**: antes de partir de entregables, el gerente debe poder señalar qué cambia en el sistema si el concepto está presente y qué debería observar si no lo está. Una definición que no produce predicciones observables todavía es demasiado vaga para dirigir.

La lectura rectora de este bloque es Project Management Institute — *A Guide to the Project Management Body of Knowledge (PMBOK Guide)*. Su aporte se usa para examinar **gobernanza, dominios de desempeño, riesgo, stakeholders y entrega de valor**. Aplica esa lente al caso sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **paquetes sin owner**; regístrala con periodo, unidad, población y baseline.

Relaciona el mecanismo con **work package**. Si ambos cambian juntos, no concluyas causalidad automáticamente: identifica una tercera variable o mecanismo alternativo que también pueda explicar el patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. work package: frontera conceptual y error de clasificación

**Definición operacional:** unidad gestionable con resultado y estimación. Su valor está en distinguirlo de **WBS** y **dependency**. En una decisión real, clasificar una situación en la categoría equivocada cambia la intervención: puedes asignar autoridad donde faltaba información, medir un output cuando debías observar un proceso o tratar una restricción como si fuera una preferencia.

Contrasta el problema con Harold Kerzner — *Project Management*, que aporta una mirada sobre **integración de proyectos, control, madurez y alineación organizacional**. Formula dos mini-casos: uno que sí satisface la definición de **work package** y otro que solo se parece superficialmente. Luego pregunta qué señal distinguiría ambos; para esta clase, **dependencias tardías** es una candidata, pero debe combinarse con evidencia cualitativa o documental cuando el fenómeno no sea directamente medible.

Antes de descomponer hasta paquetes gestionables, registra explícitamente qué decisión sería errónea si esta frontera conceptual se ignora. Esa frase convierte el vocabulario en criterio gerencial.

### 3. dependency: operacionalización y medición

**dependency** significa **relación donde un trabajo condiciona otro**. El problema ya no es definirlo, sino **operacionalizarlo**: qué contar, durante qué ventana, con qué denominador, contra qué baseline y con qué segmentación. Una métrica útil conserva suficiente contexto para no confundir mejora local con mejora del sistema.

Atul Gawande — *The Checklist Manifesto* orienta este bloque mediante **perspectiva de Ejecución aplicada al problema de la clase**. Usa esa perspectiva para diseñar una ficha de medición: `señal → fórmula/criterio → fuente → frecuencia → owner → interpretación permitida → interpretación prohibida`. La señal asignada es **critical path changes**. Si no existe un dato confiable, la salida correcta no es inventar precisión: diseña el mecanismo de captura y declara la incertidumbre.

Al llegar a mapear dependencias, compara tendencia, distribución y casos atípicos. Pregunta además si el indicador es *leading* o *lagging* y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; nunca convertirse en el objetivo que reemplaza al fenómeno.

### 4. milestone: trade-offs y efectos de segundo orden

**Definición:** evento sin duración que marca un punto verificable. Este concepto obliga a abandonar la idea de que **work breakdown y planificación** tiene una solución gratuita. Toda intervención consume autonomía, tiempo, caja, capacidad, atención, reputación o tolerancia al riesgo. Por eso, antes de estimar secuencia y recursos, se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Michael Hammer & James Champy — *Reengineering the Corporation* aporta una lente sobre **perspectiva de Procesos aplicada al problema de la clase**. Úsala para construir una matriz `beneficio / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **milestones cumplidos** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la necesidad de observar efectos laterales fuera del KPI principal.

Haz un *pre-mortem* de **work breakdown y planificación**: supone que la opción recomendada fracasó seis meses después y enumera tres mecanismos que podrían explicarlo. Al menos uno debe provenir de un efecto de segundo orden asociado a **milestone** y otro de una hipótesis del caso que nunca fue validada.

### 5. critical path: gobernanza, límites e integración

**critical path** se define como **secuencia cuya demora afecta fecha final** y cierra el circuito porque traduce análisis en responsabilidad. La pregunta ejecutiva es quién decide, quién ejecuta, quién debe ser consultado, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar.

David J. Anderson — *Kanban* se utiliza para estudiar **flujo, trabajo en proceso, políticas explícitas y evolución del sistema** y contrastar la recomendación final. Al ejecutar identificar critical path y hitos, deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento. Esa trazabilidad protege contra el sesgo retrospectivo y mejora las revisiones posteriores.

La frontera de esta clase es explícita: **Descomponer en exceso produce falsa precisión y alto mantenimiento. El horizonte cercano necesita más detalle que el lejano; usa rolling-wave planning.**. Conviértela en una regla operativa: `si ocurre X → no aplicar automáticamente → consultar/escalar/revalidar`. Integrar **WBS**, **work package**, **dependency**, **milestone** y **critical path** significa poder explicar qué parte del diagnóstico sostiene la decisión y cuál sigue siendo una apuesta.

### 6. Integración: de conceptos a una decisión defendible

La síntesis de **work breakdown y planificación** no consiste en sumar cinco definiciones. Empieza por **WBS**, contrasta **work package** con **dependency**, incorpora **milestone** como restricción o mecanismo y usa **critical path** para cerrar el ciclo. Si el análisis no puede explicar cuál de esas piezas cambió la recomendación, todavía no hay comprensión transferible.

Aplica ahora la secuencia **1. partir de entregables → 2. descomponer hasta paquetes gestionables → 3. mapear dependencias → 4. estimar secuencia y recursos → 5. identificar critical path y hitos**. Para cada paso conserva tres columnas: evidencia utilizada, alternativa descartada y razón. Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado y evita reescribir la historia después de conocer el desenlace.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla señala el lente que debes buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Project Management Institute — *A Guide to the Project Management Body of Knowledge (PMBOK Guide)* | gobernanza, dominios de desempeño, riesgo, stakeholders y entrega de valor | ¿Qué supuesto de **work breakdown y planificación** ayuda a desafiar? |
| Harold Kerzner — *Project Management* | integración de proyectos, control, madurez y alineación organizacional | ¿Qué supuesto de **work breakdown y planificación** ayuda a desafiar? |
| Atul Gawande — *The Checklist Manifesto* | perspectiva de Ejecución aplicada al problema de la clase | ¿Qué supuesto de **work breakdown y planificación** ayuda a desafiar? |
| Michael Hammer & James Champy — *Reengineering the Corporation* | perspectiva de Procesos aplicada al problema de la clase | ¿Qué supuesto de **work breakdown y planificación** ayuda a desafiar? |
| David J. Anderson — *Kanban* | flujo, trabajo en proceso, políticas explícitas y evolución del sistema | ¿Qué supuesto de **work breakdown y planificación** ayuda a desafiar? |

En **work breakdown y planificación**, la lectura se evalúa por **uso**, no por cantidad de páginas. La nota debe indicar qué tesis de las fuentes modifica tu lectura de **WBS**, qué evidencia del caso tensiona esa tesis y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación:** Un equipo planifica 'analizar, desarrollar, probar, lanzar' sin descomponer integraciones externas. A mitad del proyecto descubre una certificación de seis semanas que controla la fecha.

**Paso 1 — partir de entregables.** La gerencia escribe primero el supuesto asociado a **WBS** y evita convertirlo en hecho. Luego busca **paquetes sin owner** para contrastarlo en el caso de **work breakdown y planificación**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 2 — descomponer hasta paquetes gestionables.** La gerencia escribe primero el supuesto asociado a **work package** y evita convertirlo en hecho. Luego busca **dependencias tardías** para contrastarlo en el caso de **work breakdown y planificación**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 3 — mapear dependencias.** La gerencia escribe primero el supuesto asociado a **dependency** y evita convertirlo en hecho. Luego busca **critical path changes** para contrastarlo en el caso de **work breakdown y planificación**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 4 — estimar secuencia y recursos.** La gerencia escribe primero el supuesto asociado a **milestone** y evita convertirlo en hecho. Luego busca **milestones cumplidos** para contrastarlo en el caso de **work breakdown y planificación**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 5 — identificar critical path y hitos.** La gerencia escribe primero el supuesto asociado a **critical path** y evita convertirlo en hecho. Luego busca **replanificaciones** para contrastarlo en el caso de **work breakdown y planificación**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Síntesis del caso.** La recomendación debe terminar con responsable, fecha, evidencia de éxito y señal de stop. En **work breakdown y planificación**, omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo |
|---|---|---|---|
| **WBS** | descomposición jerárquica orientada a entregables | Cuando paquetes sin owner es observable y accionable. | Sobrerreaccionar a una señal parcial. |
| **work package** | unidad gestionable con resultado y estimación | Cuando la primera explicación no distingue mecanismo o responsabilidad. | Convertir el concepto en etiqueta. |
| **Experimento/revisión** | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar eternamente y no decidir. |
| **Escalamiento** | Elevar autoridad o especialidad | Cuando hay derechos, capital material, regulación o irreversibilidad. | Delegar hacia arriba lo que sí corresponde decidir. |

**Frontera de aplicación:** Descomponer en exceso produce falsa precisión y alto mantenimiento. El horizonte cercano necesita más detalle que el lejano; usa rolling-wave planning.

## 🪜 De profesional a owner

| Nivel | Responsabilidad sobre work breakdown y planificación |
|---|---|
| **Profesional** | usa **work breakdown y planificación** para mejorar una contribución propia y explicar sus supuestos con evidencia. |
| **Jefe / Team Lead** | aplica **WBS** y **work package** para coordinar personas sin sustituir conversación por métricas. |
| **Manager / Gerente** | conecta paquetes sin owner con capacidad, presupuesto, dependencias y riesgo interáreas. |
| **CEO / Director** | decide si work breakdown y planificación cambia estrategia, economía o riesgo de empresa y qué debe llegar al comité o directorio. |
| **Founder / Owner** | pregunta si la solución de work breakdown y planificación reduce dependencia del fundador, preserva caja y puede operar como sistema repetible. |

El cambio de nivel en **work breakdown y planificación** aumenta el número de personas, dinero, dependencias y consecuencias que quedan dentro de la decisión. Por eso la misma herramienta debe volverse más explícita en evidencia, gobernanza y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Un equipo planifica 'analizar, desarrollar, probar, lanzar' sin descomponer integraciones externas. A mitad del proyecto descubre una certificación de seis semanas que controla la fecha.

Entrega un **decision brief de work breakdown y planificación** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre personas, cliente, operación, caja y riesgo; (e) recomendación; (f) condición que haría cambiarla; (g) dueño y fecha de revisión. Utiliza al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica

1. Reconstruye el caso de **work breakdown y planificación** con una tabla `hecho / interpretación / hipótesis / decisión`.
2. Ejecuta **1. partir de entregables → 2. descomponer hasta paquetes gestionables → 3. mapear dependencias → 4. estimar secuencia y recursos → 5. identificar critical path y hitos** y adjunta evidencia para cada transición entre pasos.
3. Calcula o documenta paquetes sin owner, dependencias tardías; si no existe dato, diseña cómo obtenerlo.
4. Escribe una alternativa que contradiga tu preferencia inicial y haz un *pre-mortem* específico del caso.
5. Lee dos referencias, registra una coincidencia y una tensión, y modifica el brief si corresponde.
6. Repite la decisión desde el rol de CEO/owner: identifica qué cambia al aumentar el alcance y la irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar WBS y work package como sinónimos | Se pierde la distinción entre “descomposición jerárquica orientada a entregables” y “unidad gestionable con resultado y estimación” | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por “identificar critical path y hitos” | Se saltó “partir de entregables” y la solución llegó antes que el diagnóstico | Reconstruye la cadena 1. partir de entregables → 2. descomponer hasta paquetes gestionables → 3. mapear dependencias → 4. estimar secuencia y recursos → 5. identificar critical path y hitos y marca el primer supuesto no demostrado. |
| Optimizar solo paquetes sin owner | La métrica local sustituyó al resultado del sistema | Contrástala con dependencias tardías y explicita el costo de oportunidad. |
| Generalizar desde un caso favorable | Se confundió evidencia local con una regla universal sobre work breakdown y planificación | Descomponer en exceso produce falsa precisión y alto mantenimiento. El horizonte cercano necesita más detalle que el lejano; usa rolling-wave planning. |
| No fijar revisión | Una decisión sobre work breakdown y planificación se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de stop. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **WBS** y **work package** usando un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **dependency** y qué observación obligaría a rechazar tu interpretación?
3. Aplica **partir de entregables → descomponer hasta paquetes gestionables** al caso de la clase. ¿Qué dato todavía falta?
4. ¿Por qué **paquetes sin owner** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la tabla de lectura. ¿Dónde podrían llevar a recomendaciones distintas para **work breakdown y planificación**?
6. ¿Qué decisión equivocada podría producirse si se ignora este límite: **Descomponer en exceso produce falsa precisión y alto mantenimiento. El horizonte cercano necesita más detalle que el lejano; usa rolling-wave planning.**?

## 📥 Entregable

Guarda en `portfolio/075-work-breakdown-y-planificacion/`:

- `leadership-decision-brief.md` con el problema específico de **work breakdown y planificación**, evidencia, alternativas, decisión y gobernanza;
- `reading-note.md` contrastando las fuentes de **work breakdown y planificación** con edición/páginas consultadas;
- `decision-journal.md` registrando los supuestos de **WBS**, confianza, responsable y revisión;
- `red-team.md` con la objeción más fuerte al caso **Un equipo planifica 'analizar, desarrollar, probar, lanzar' sin descomponer integraciones externas. A mitad del proyecto descubre una certificación de seis semanas que controla la fecha.** y el dato que podría invalidar la recomendación.

## 📗 Fuentes y verificación

- Project Management Institute — *A Guide to the Project Management Body of Knowledge (PMBOK Guide)*. **Uso en esta clase:** gobernanza, dominios de desempeño, riesgo, stakeholders y entrega de valor. Lectura selectiva: índice/capítulos pertinentes a **work breakdown y planificación**; registra edición y páginas consultadas.
- Harold Kerzner — *Project Management*. **Uso en esta clase:** integración de proyectos, control, madurez y alineación organizacional. Lectura selectiva: índice/capítulos pertinentes a **work breakdown y planificación**; registra edición y páginas consultadas.
- Atul Gawande — *The Checklist Manifesto*. **Uso en esta clase:** perspectiva de Ejecución aplicada al problema de la clase. Lectura selectiva: índice/capítulos pertinentes a **work breakdown y planificación**; registra edición y páginas consultadas.
- Michael Hammer & James Champy — *Reengineering the Corporation*. **Uso en esta clase:** perspectiva de Procesos aplicada al problema de la clase. Lectura selectiva: índice/capítulos pertinentes a **work breakdown y planificación**; registra edición y páginas consultadas.
- David J. Anderson — *Kanban*. **Uso en esta clase:** flujo, trabajo en proceso, políticas explícitas y evolución del sistema. Lectura selectiva: índice/capítulos pertinentes a **work breakdown y planificación**; registra edición y páginas consultadas.
- Ken Schwaber & Jeff Sutherland — *The Scrum Guide*. **Uso en esta clase:** empirismo, transparencia, inspección y adaptación. Lectura selectiva: índice/capítulos pertinentes a **work breakdown y planificación**; registra edición y páginas consultadas.
- Susan A. Ambrose et al. — *How Learning Works*. Diseño de objetivos, práctica y feedback.
- Peter C. Brown, Henry L. Roediger III & Mark A. McDaniel — *Make It Stick*. Recuperación, elaboración y transferencia.
- Grant Wiggins & Jay McTighe — *Understanding by Design*. Diseño inverso desde desempeño observable.
- Anders Ericsson & Robert Pool — *Peak*. Práctica deliberada con criterios y retroalimentación.
- William Ellet — *The Case Study Handbook*. Análisis de problema/decisión, evidencia y recomendación.

> **Regla de fuentes para Work breakdown y planificación:** las obras anteriores estructuran las perspectivas de esta materia; cualquier norma, ley, impuesto o estándar vivo mencionado en **work breakdown y planificación** debe comprobarse nuevamente en su fuente primaria vigente. El desarrollo es original y no reproduce capítulos protegidos.
