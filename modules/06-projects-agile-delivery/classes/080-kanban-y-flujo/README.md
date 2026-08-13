# Clase 080 — Kanban y flujo

**Parte:** 06 — Proyectos, Agile y entrega  
**Nivel:** Etapa 2 — Jefe → Manager  
**Duración sugerida:** 150–180 minutos · **Estándar:** deep-class-v2

## 🎯 Propósito

Kanban gestiona flujo visualizando trabajo, limitando WIP y midiendo tiempo de ciclo. Su lógica central es que iniciar menos puede terminar más. Las políticas explícitas y clases de servicio permiten coordinar sin convertir cada urgencia en bypass.

La salida de esta parte es **entregar proyectos con alcance, flujo, riesgo, calidad y gobernanza adaptativa**. En esta clase, esa progresión se concreta al exigir que cada afirmación sobre **kanban y flujo** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

## 📚 Resultados de aprendizaje

Al finalizar podrás:

1. **Distinguir** `WIP`, `cycle time`, `lead time`, `throughput`, `pull` mediante observables, no por memoria verbal.
2. **Explicar** por qué esas distinciones cambian una decisión de jefe → manager.
3. **Aplicar** la secuencia **1. mapear flujo real → 2. visualizar estados y bloqueos → 3. establecer límites WIP → 4. definir políticas de pull y clases → 5. medir cycle time y mejorar cuello** conservando supuestos, alternativas y trazabilidad.
4. **Interpretar** WIP, cycle time percentiles, throughput sin confundir señal, explicación y causalidad.
5. **Resolver** el caso ejecutivo con al menos dos opciones plausibles y un criterio explícito de stop/revisión.
6. **Contrastar** dos obras de referencia y explicar dónde sus lentes son complementarias o entran en tensión.

## 🧭 Agenda

| Tramo | Evidencia de aprendizaje |
|---|---|
| 0–20 min | Recuperación: define WIP y cycle time sin mirar la tabla; corrige con la fuente. |
| 20–70 min | Lectura guiada de conceptos + contraste de dos referencias. |
| 70–115 min | Ejemplo trabajado con WIP y trazabilidad de supuestos. |
| 115–155 min | Caso ejecutivo: dos alternativas, trade-offs y decisión provisional. |
| 155–180 min | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar comprensión |
|---|---|---|
| **WIP** | trabajo iniciado pero no terminado | Distingue un hecho compatible y otro que lo refute. |
| **cycle time** | tiempo desde inicio hasta finalización | Distingue un hecho compatible y otro que lo refute. |
| **lead time** | tiempo desde solicitud hasta entrega | Distingue un hecho compatible y otro que lo refute. |
| **throughput** | items terminados por periodo | Distingue un hecho compatible y otro que lo refute. |
| **pull** | principio de iniciar trabajo cuando existe capacidad en la etapa siguiente | Distingue un hecho compatible y otro que lo refute. |

## 🧠 Modelo mental

```text
1. mapear flujo real → 2. visualizar estados y bloqueos → 3. establecer límites WIP → 4. definir políticas de pull y clases → 5. medir cycle time y mejorar cuello
```

La secuencia nace del problema de esta clase: **Kanban gestiona flujo visualizando trabajo, limitando WIP y midiendo tiempo de ciclo. Su lógica central es que iniciar menos puede terminar más. Las políticas explícitas y clases de servicio permiten coordinar sin convertir cada urgencia en bypass.** El método es útil mientras las condiciones permitan observar las señales requeridas. No elimina incertidumbre; la hace visible y obliga a decidir proporcionalmente a la evidencia. Límite principal: **Límites WIP no deben impedir respuesta a incidentes críticos. Define clases de servicio y políticas de expedite con costo visible para evitar que la excepción destruya el sistema.**

## 📖 Desarrollo

### 1. WIP: mecanismo central

**WIP** se entiende aquí como **trabajo iniciado pero no terminado**. Esta es la pieza causal o estructural desde la que se inicia **kanban y flujo**: antes de mapear flujo real, el gerente debe poder señalar qué cambia en el sistema si el concepto está presente y qué debería observar si no lo está. Una definición que no produce predicciones observables todavía es demasiado vaga para dirigir.

La lectura rectora de este bloque es Project Management Institute — *A Guide to the Project Management Body of Knowledge (PMBOK Guide)*. Su aporte se usa para examinar **gobernanza, dominios de desempeño, riesgo, stakeholders y entrega de valor**. Aplica esa lente al caso sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **WIP**; regístrala con periodo, unidad, población y baseline.

Relaciona el mecanismo con **cycle time**. Si ambos cambian juntos, no concluyas causalidad automáticamente: identifica una tercera variable o mecanismo alternativo que también pueda explicar el patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. cycle time: frontera conceptual y error de clasificación

**Definición operacional:** tiempo desde inicio hasta finalización. Su valor está en distinguirlo de **WIP** y **lead time**. En una decisión real, clasificar una situación en la categoría equivocada cambia la intervención: puedes asignar autoridad donde faltaba información, medir un output cuando debías observar un proceso o tratar una restricción como si fuera una preferencia.

Contrasta el problema con Harold Kerzner — *Project Management*, que aporta una mirada sobre **integración de proyectos, control, madurez y alineación organizacional**. Formula dos mini-casos: uno que sí satisface la definición de **cycle time** y otro que solo se parece superficialmente. Luego pregunta qué señal distinguiría ambos; para esta clase, **cycle time percentiles** es una candidata, pero debe combinarse con evidencia cualitativa o documental cuando el fenómeno no sea directamente medible.

Antes de visualizar estados y bloqueos, registra explícitamente qué decisión sería errónea si esta frontera conceptual se ignora. Esa frase convierte el vocabulario en criterio gerencial.

### 3. lead time: operacionalización y medición

**lead time** significa **tiempo desde solicitud hasta entrega**. El problema ya no es definirlo, sino **operacionalizarlo**: qué contar, durante qué ventana, con qué denominador, contra qué baseline y con qué segmentación. Una métrica útil conserva suficiente contexto para no confundir mejora local con mejora del sistema.

Nicole Forsgren, Jez Humble & Gene Kim — *Accelerate* orienta este bloque mediante **métricas de entrega, capacidades técnicas y desempeño organizacional**. Usa esa perspectiva para diseñar una ficha de medición: `señal → fórmula/criterio → fuente → frecuencia → owner → interpretación permitida → interpretación prohibida`. La señal asignada es **throughput**. Si no existe un dato confiable, la salida correcta no es inventar precisión: diseña el mecanismo de captura y declara la incertidumbre.

Al llegar a establecer límites wip, compara tendencia, distribución y casos atípicos. Pregunta además si el indicador es *leading* o *lagging* y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; nunca convertirse en el objetivo que reemplaza al fenómeno.

### 4. throughput: trade-offs y efectos de segundo orden

**Definición:** items terminados por periodo. Este concepto obliga a abandonar la idea de que **kanban y flujo** tiene una solución gratuita. Toda intervención consume autonomía, tiempo, caja, capacidad, atención, reputación o tolerancia al riesgo. Por eso, antes de definir políticas de pull y clases, se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Atul Gawande — *The Checklist Manifesto* aporta una lente sobre **perspectiva de Ejecución aplicada al problema de la clase**. Úsala para construir una matriz `beneficio / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **blocked time** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la necesidad de observar efectos laterales fuera del KPI principal.

Haz un *pre-mortem* de **kanban y flujo**: supone que la opción recomendada fracasó seis meses después y enumera tres mecanismos que podrían explicarlo. Al menos uno debe provenir de un efecto de segundo orden asociado a **throughput** y otro de una hipótesis del caso que nunca fue validada.

### 5. pull: gobernanza, límites e integración

**pull** se define como **principio de iniciar trabajo cuando existe capacidad en la etapa siguiente** y cierra el circuito porque traduce análisis en responsabilidad. La pregunta ejecutiva es quién decide, quién ejecuta, quién debe ser consultado, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar.

Gene Kim — *The Unicorn Project* se utiliza para estudiar **perspectiva de Operaciones tecnológicas aplicada al problema de la clase** y contrastar la recomendación final. Al ejecutar medir cycle time y mejorar cuello, deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento. Esa trazabilidad protege contra el sesgo retrospectivo y mejora las revisiones posteriores.

La frontera de esta clase es explícita: **Límites WIP no deben impedir respuesta a incidentes críticos. Define clases de servicio y políticas de expedite con costo visible para evitar que la excepción destruya el sistema.**. Conviértela en una regla operativa: `si ocurre X → no aplicar automáticamente → consultar/escalar/revalidar`. Integrar **WIP**, **cycle time**, **lead time**, **throughput** y **pull** significa poder explicar qué parte del diagnóstico sostiene la decisión y cuál sigue siendo una apuesta.

### 6. Integración: de conceptos a una decisión defendible

La síntesis de **kanban y flujo** no consiste en sumar cinco definiciones. Empieza por **WIP**, contrasta **cycle time** con **lead time**, incorpora **throughput** como restricción o mecanismo y usa **pull** para cerrar el ciclo. Si el análisis no puede explicar cuál de esas piezas cambió la recomendación, todavía no hay comprensión transferible.

Aplica ahora la secuencia **1. mapear flujo real → 2. visualizar estados y bloqueos → 3. establecer límites WIP → 4. definir políticas de pull y clases → 5. medir cycle time y mejorar cuello**. Para cada paso conserva tres columnas: evidencia utilizada, alternativa descartada y razón. Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado y evita reescribir la historia después de conocer el desenlace.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla señala el lente que debes buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Project Management Institute — *A Guide to the Project Management Body of Knowledge (PMBOK Guide)* | gobernanza, dominios de desempeño, riesgo, stakeholders y entrega de valor | ¿Qué supuesto de **kanban y flujo** ayuda a desafiar? |
| Harold Kerzner — *Project Management* | integración de proyectos, control, madurez y alineación organizacional | ¿Qué supuesto de **kanban y flujo** ayuda a desafiar? |
| Nicole Forsgren, Jez Humble & Gene Kim — *Accelerate* | métricas de entrega, capacidades técnicas y desempeño organizacional | ¿Qué supuesto de **kanban y flujo** ayuda a desafiar? |
| Atul Gawande — *The Checklist Manifesto* | perspectiva de Ejecución aplicada al problema de la clase | ¿Qué supuesto de **kanban y flujo** ayuda a desafiar? |
| Gene Kim — *The Unicorn Project* | perspectiva de Operaciones tecnológicas aplicada al problema de la clase | ¿Qué supuesto de **kanban y flujo** ayuda a desafiar? |

En **kanban y flujo**, la lectura se evalúa por **uso**, no por cantidad de páginas. La nota debe indicar qué tesis de las fuentes modifica tu lectura de **WIP**, qué evidencia del caso tensiona esa tesis y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación:** Un equipo tiene 32 tareas 'en progreso' para seis personas. Cada nueva urgencia se inicia inmediatamente y el trabajo más antiguo lleva 47 días abierto.

**Paso 1 — mapear flujo real.** La gerencia escribe primero el supuesto asociado a **WIP** y evita convertirlo en hecho. Luego busca **WIP** para contrastarlo en el caso de **kanban y flujo**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 2 — visualizar estados y bloqueos.** La gerencia escribe primero el supuesto asociado a **cycle time** y evita convertirlo en hecho. Luego busca **cycle time percentiles** para contrastarlo en el caso de **kanban y flujo**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 3 — establecer límites WIP.** La gerencia escribe primero el supuesto asociado a **lead time** y evita convertirlo en hecho. Luego busca **throughput** para contrastarlo en el caso de **kanban y flujo**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 4 — definir políticas de pull y clases.** La gerencia escribe primero el supuesto asociado a **throughput** y evita convertirlo en hecho. Luego busca **blocked time** para contrastarlo en el caso de **kanban y flujo**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 5 — medir cycle time y mejorar cuello.** La gerencia escribe primero el supuesto asociado a **pull** y evita convertirlo en hecho. Luego busca **aging WIP** para contrastarlo en el caso de **kanban y flujo**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Síntesis del caso.** La recomendación debe terminar con responsable, fecha, evidencia de éxito y señal de stop. En **kanban y flujo**, omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo |
|---|---|---|---|
| **WIP** | trabajo iniciado pero no terminado | Cuando WIP es observable y accionable. | Sobrerreaccionar a una señal parcial. |
| **cycle time** | tiempo desde inicio hasta finalización | Cuando la primera explicación no distingue mecanismo o responsabilidad. | Convertir el concepto en etiqueta. |
| **Experimento/revisión** | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar eternamente y no decidir. |
| **Escalamiento** | Elevar autoridad o especialidad | Cuando hay derechos, capital material, regulación o irreversibilidad. | Delegar hacia arriba lo que sí corresponde decidir. |

**Frontera de aplicación:** Límites WIP no deben impedir respuesta a incidentes críticos. Define clases de servicio y políticas de expedite con costo visible para evitar que la excepción destruya el sistema.

## 🪜 De profesional a owner

| Nivel | Responsabilidad sobre kanban y flujo |
|---|---|
| **Profesional** | usa **kanban y flujo** para mejorar una contribución propia y explicar sus supuestos con evidencia. |
| **Jefe / Team Lead** | aplica **WIP** y **cycle time** para coordinar personas sin sustituir conversación por métricas. |
| **Manager / Gerente** | conecta WIP con capacidad, presupuesto, dependencias y riesgo interáreas. |
| **CEO / Director** | decide si kanban y flujo cambia estrategia, economía o riesgo de empresa y qué debe llegar al comité o directorio. |
| **Founder / Owner** | pregunta si la solución de kanban y flujo reduce dependencia del fundador, preserva caja y puede operar como sistema repetible. |

El cambio de nivel en **kanban y flujo** aumenta el número de personas, dinero, dependencias y consecuencias que quedan dentro de la decisión. Por eso la misma herramienta debe volverse más explícita en evidencia, gobernanza y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Un equipo tiene 32 tareas 'en progreso' para seis personas. Cada nueva urgencia se inicia inmediatamente y el trabajo más antiguo lleva 47 días abierto.

Entrega un **decision brief de kanban y flujo** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre personas, cliente, operación, caja y riesgo; (e) recomendación; (f) condición que haría cambiarla; (g) dueño y fecha de revisión. Utiliza al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica

1. Reconstruye el caso de **kanban y flujo** con una tabla `hecho / interpretación / hipótesis / decisión`.
2. Ejecuta **1. mapear flujo real → 2. visualizar estados y bloqueos → 3. establecer límites WIP → 4. definir políticas de pull y clases → 5. medir cycle time y mejorar cuello** y adjunta evidencia para cada transición entre pasos.
3. Calcula o documenta WIP, cycle time percentiles; si no existe dato, diseña cómo obtenerlo.
4. Escribe una alternativa que contradiga tu preferencia inicial y haz un *pre-mortem* específico del caso.
5. Lee dos referencias, registra una coincidencia y una tensión, y modifica el brief si corresponde.
6. Repite la decisión desde el rol de CEO/owner: identifica qué cambia al aumentar el alcance y la irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar WIP y cycle time como sinónimos | Se pierde la distinción entre “trabajo iniciado pero no terminado” y “tiempo desde inicio hasta finalización” | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por “medir cycle time y mejorar cuello” | Se saltó “mapear flujo real” y la solución llegó antes que el diagnóstico | Reconstruye la cadena 1. mapear flujo real → 2. visualizar estados y bloqueos → 3. establecer límites WIP → 4. definir políticas de pull y clases → 5. medir cycle time y mejorar cuello y marca el primer supuesto no demostrado. |
| Optimizar solo WIP | La métrica local sustituyó al resultado del sistema | Contrástala con cycle time percentiles y explicita el costo de oportunidad. |
| Generalizar desde un caso favorable | Se confundió evidencia local con una regla universal sobre kanban y flujo | Límites WIP no deben impedir respuesta a incidentes críticos. Define clases de servicio y políticas de expedite con costo visible para evitar que la excepción destruya el sistema. |
| No fijar revisión | Una decisión sobre kanban y flujo se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de stop. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **WIP** y **cycle time** usando un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **lead time** y qué observación obligaría a rechazar tu interpretación?
3. Aplica **mapear flujo real → visualizar estados y bloqueos** al caso de la clase. ¿Qué dato todavía falta?
4. ¿Por qué **WIP** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la tabla de lectura. ¿Dónde podrían llevar a recomendaciones distintas para **kanban y flujo**?
6. ¿Qué decisión equivocada podría producirse si se ignora este límite: **Límites WIP no deben impedir respuesta a incidentes críticos. Define clases de servicio y políticas de expedite con costo visible para evitar que la excepción destruya el sistema.**?

## 📥 Entregable

Guarda en `portfolio/080-kanban-y-flujo/`:

- `modelo-financiero-y-memo-de-decision.md` con el problema específico de **kanban y flujo**, evidencia, alternativas, decisión y gobernanza;
- `reading-note.md` contrastando las fuentes de **kanban y flujo** con edición/páginas consultadas;
- `decision-journal.md` registrando los supuestos de **WIP**, confianza, responsable y revisión;
- `red-team.md` con la objeción más fuerte al caso **Un equipo tiene 32 tareas 'en progreso' para seis personas. Cada nueva urgencia se inicia inmediatamente y el trabajo más antiguo lleva 47 días abierto.** y el dato que podría invalidar la recomendación.

## 📗 Fuentes y verificación

- Project Management Institute — *A Guide to the Project Management Body of Knowledge (PMBOK Guide)*. **Uso en esta clase:** gobernanza, dominios de desempeño, riesgo, stakeholders y entrega de valor. Lectura selectiva: índice/capítulos pertinentes a **kanban y flujo**; registra edición y páginas consultadas.
- Harold Kerzner — *Project Management*. **Uso en esta clase:** integración de proyectos, control, madurez y alineación organizacional. Lectura selectiva: índice/capítulos pertinentes a **kanban y flujo**; registra edición y páginas consultadas.
- Nicole Forsgren, Jez Humble & Gene Kim — *Accelerate*. **Uso en esta clase:** métricas de entrega, capacidades técnicas y desempeño organizacional. Lectura selectiva: índice/capítulos pertinentes a **kanban y flujo**; registra edición y páginas consultadas.
- Atul Gawande — *The Checklist Manifesto*. **Uso en esta clase:** perspectiva de Ejecución aplicada al problema de la clase. Lectura selectiva: índice/capítulos pertinentes a **kanban y flujo**; registra edición y páginas consultadas.
- Gene Kim — *The Unicorn Project*. **Uso en esta clase:** perspectiva de Operaciones tecnológicas aplicada al problema de la clase. Lectura selectiva: índice/capítulos pertinentes a **kanban y flujo**; registra edición y páginas consultadas.
- Ken Schwaber & Jeff Sutherland — *The Scrum Guide*. **Uso en esta clase:** empirismo, transparencia, inspección y adaptación. Lectura selectiva: índice/capítulos pertinentes a **kanban y flujo**; registra edición y páginas consultadas.
- Susan A. Ambrose et al. — *How Learning Works*. Diseño de objetivos, práctica y feedback.
- Peter C. Brown, Henry L. Roediger III & Mark A. McDaniel — *Make It Stick*. Recuperación, elaboración y transferencia.
- Grant Wiggins & Jay McTighe — *Understanding by Design*. Diseño inverso desde desempeño observable.
- Anders Ericsson & Robert Pool — *Peak*. Práctica deliberada con criterios y retroalimentación.
- William Ellet — *The Case Study Handbook*. Análisis de problema/decisión, evidencia y recomendación.

> **Regla de fuentes para Kanban y flujo:** las obras anteriores estructuran las perspectivas de esta materia; cualquier norma, ley, impuesto o estándar vivo mencionado en **kanban y flujo** debe comprobarse nuevamente en su fuente primaria vigente. El desarrollo es original y no reproduce capítulos protegidos.
