# Clase 077 — Gestión de riesgos y dependencias

**Parte:** 06 — Proyectos, Agile y entrega  
**Nivel:** Etapa 2 — Jefe → Manager  
**Duración sugerida:** 150–180 minutos · **Estándar:** deep-class-v2

## 🎯 Propósito

Gestionar riesgos y dependencias es hacer visible lo que puede alterar el plan antes de que sea incidente. Riesgo combina probabilidad e impacto; dependencia condiciona secuencia o autonomía. Ambos requieren owner, respuesta, trigger y fecha, no una celda roja olvidada en una planilla.

La salida de esta parte es **entregar proyectos con alcance, flujo, riesgo, calidad y gobernanza adaptativa**. En esta clase, esa progresión se concreta al exigir que cada afirmación sobre **gestión de riesgos y dependencias** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

## 📚 Resultados de aprendizaje

Al finalizar podrás:

1. **Distinguir** `risk`, `issue`, `dependency`, `mitigation`, `contingency` mediante observables, no por memoria verbal.
2. **Explicar** por qué esas distinciones cambian una decisión de jefe → manager.
3. **Aplicar** la secuencia **1. identificar riesgos por objetivo → 2. priorizar exposición material → 3. asignar mitigación y contingency → 4. mapear dependencias con fechas y owners → 5. revisar triggers semanalmente** conservando supuestos, alternativas y trazabilidad.
4. **Interpretar** riesgos vencidos, issues que antes eran riesgos, dependencias sin compromiso sin confundir señal, explicación y causalidad.
5. **Resolver** el caso ejecutivo con al menos dos opciones plausibles y un criterio explícito de stop/revisión.
6. **Contrastar** dos obras de referencia y explicar dónde sus lentes son complementarias o entran en tensión.

## 🧭 Agenda

| Tramo | Evidencia de aprendizaje |
|---|---|
| 0–20 min | Recuperación: define risk y issue sin mirar la tabla; corrige con la fuente. |
| 20–70 min | Lectura guiada de conceptos + contraste de dos referencias. |
| 70–115 min | Ejemplo trabajado con riesgos vencidos y trazabilidad de supuestos. |
| 115–155 min | Caso ejecutivo: dos alternativas, trade-offs y decisión provisional. |
| 155–180 min | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar comprensión |
|---|---|---|
| **risk** | evento incierto que puede afectar objetivos | Distingue un hecho compatible y otro que lo refute. |
| **issue** | problema que ya ocurrió | Distingue un hecho compatible y otro que lo refute. |
| **dependency** | condición donde un deliverable depende de otro actor o trabajo | Distingue un hecho compatible y otro que lo refute. |
| **mitigation** | acción que reduce probabilidad o impacto | Distingue un hecho compatible y otro que lo refute. |
| **contingency** | respuesta preparada si el evento ocurre | Distingue un hecho compatible y otro que lo refute. |

## 🧠 Modelo mental

```text
1. identificar riesgos por objetivo → 2. priorizar exposición material → 3. asignar mitigación y contingency → 4. mapear dependencias con fechas y owners → 5. revisar triggers semanalmente
```

La secuencia nace del problema de esta clase: **Gestionar riesgos y dependencias es hacer visible lo que puede alterar el plan antes de que sea incidente. Riesgo combina probabilidad e impacto; dependencia condiciona secuencia o autonomía. Ambos requieren owner, respuesta, trigger y fecha, no una celda roja olvidada en una planilla.** El método es útil mientras las condiciones permitan observar las señales requeridas. No elimina incertidumbre; la hace visible y obliga a decidir proporcionalmente a la evidencia. Límite principal: **Un risk register enorme puede ocultar lo material. Distingue riesgos de proyecto de incertidumbre normal y escala los que afectan estrategia, seguridad o compliance.**

## 📖 Desarrollo

### 1. risk: mecanismo central

**risk** se entiende aquí como **evento incierto que puede afectar objetivos**. Esta es la pieza causal o estructural desde la que se inicia **gestión de riesgos y dependencias**: antes de identificar riesgos por objetivo, el gerente debe poder señalar qué cambia en el sistema si el concepto está presente y qué debería observar si no lo está. Una definición que no produce predicciones observables todavía es demasiado vaga para dirigir.

La lectura rectora de este bloque es Project Management Institute — *A Guide to the Project Management Body of Knowledge (PMBOK Guide)*. Su aporte se usa para examinar **gobernanza, dominios de desempeño, riesgo, stakeholders y entrega de valor**. Aplica esa lente al caso sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **riesgos vencidos**; regístrala con periodo, unidad, población y baseline.

Relaciona el mecanismo con **issue**. Si ambos cambian juntos, no concluyas causalidad automáticamente: identifica una tercera variable o mecanismo alternativo que también pueda explicar el patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. issue: frontera conceptual y error de clasificación

**Definición operacional:** problema que ya ocurrió. Su valor está en distinguirlo de **risk** y **dependency**. En una decisión real, clasificar una situación en la categoría equivocada cambia la intervención: puedes asignar autoridad donde faltaba información, medir un output cuando debías observar un proceso o tratar una restricción como si fuera una preferencia.

Contrasta el problema con Harold Kerzner — *Project Management*, que aporta una mirada sobre **integración de proyectos, control, madurez y alineación organizacional**. Formula dos mini-casos: uno que sí satisface la definición de **issue** y otro que solo se parece superficialmente. Luego pregunta qué señal distinguiría ambos; para esta clase, **issues que antes eran riesgos** es una candidata, pero debe combinarse con evidencia cualitativa o documental cuando el fenómeno no sea directamente medible.

Antes de priorizar exposición material, registra explícitamente qué decisión sería errónea si esta frontera conceptual se ignora. Esa frase convierte el vocabulario en criterio gerencial.

### 3. dependency: operacionalización y medición

**dependency** significa **condición donde un deliverable depende de otro actor o trabajo**. El problema ya no es definirlo, sino **operacionalizarlo**: qué contar, durante qué ventana, con qué denominador, contra qué baseline y con qué segmentación. Una métrica útil conserva suficiente contexto para no confundir mejora local con mejora del sistema.

Gene Kim — *The Unicorn Project* orienta este bloque mediante **perspectiva de Operaciones tecnológicas aplicada al problema de la clase**. Usa esa perspectiva para diseñar una ficha de medición: `señal → fórmula/criterio → fuente → frecuencia → owner → interpretación permitida → interpretación prohibida`. La señal asignada es **dependencias sin compromiso**. Si no existe un dato confiable, la salida correcta no es inventar precisión: diseña el mecanismo de captura y declara la incertidumbre.

Al llegar a asignar mitigación y contingency, compara tendencia, distribución y casos atípicos. Pregunta además si el indicador es *leading* o *lagging* y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; nunca convertirse en el objetivo que reemplaza al fenómeno.

### 4. mitigation: trade-offs y efectos de segundo orden

**Definición:** acción que reduce probabilidad o impacto. Este concepto obliga a abandonar la idea de que **gestión de riesgos y dependencias** tiene una solución gratuita. Toda intervención consume autonomía, tiempo, caja, capacidad, atención, reputación o tolerancia al riesgo. Por eso, antes de mapear dependencias con fechas y owners, se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

David J. Anderson — *Kanban* aporta una lente sobre **flujo, trabajo en proceso, políticas explícitas y evolución del sistema**. Úsala para construir una matriz `beneficio / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **exposición residual** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la necesidad de observar efectos laterales fuera del KPI principal.

Haz un *pre-mortem* de **gestión de riesgos y dependencias**: supone que la opción recomendada fracasó seis meses después y enumera tres mecanismos que podrían explicarlo. Al menos uno debe provenir de un efecto de segundo orden asociado a **mitigation** y otro de una hipótesis del caso que nunca fue validada.

### 5. contingency: gobernanza, límites e integración

**contingency** se define como **respuesta preparada si el evento ocurre** y cierra el circuito porque traduce análisis en responsabilidad. La pregunta ejecutiva es quién decide, quién ejecuta, quién debe ser consultado, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar.

Eliyahu M. Goldratt & Jeff Cox — *The Goal* se utiliza para estudiar **restricciones, throughput, inventario y pensamiento de flujo** y contrastar la recomendación final. Al ejecutar revisar triggers semanalmente, deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento. Esa trazabilidad protege contra el sesgo retrospectivo y mejora las revisiones posteriores.

La frontera de esta clase es explícita: **Un risk register enorme puede ocultar lo material. Distingue riesgos de proyecto de incertidumbre normal y escala los que afectan estrategia, seguridad o compliance.**. Conviértela en una regla operativa: `si ocurre X → no aplicar automáticamente → consultar/escalar/revalidar`. Integrar **risk**, **issue**, **dependency**, **mitigation** y **contingency** significa poder explicar qué parte del diagnóstico sostiene la decisión y cuál sigue siendo una apuesta.

### 6. Integración: de conceptos a una decisión defendible

La síntesis de **gestión de riesgos y dependencias** no consiste en sumar cinco definiciones. Empieza por **risk**, contrasta **issue** con **dependency**, incorpora **mitigation** como restricción o mecanismo y usa **contingency** para cerrar el ciclo. Si el análisis no puede explicar cuál de esas piezas cambió la recomendación, todavía no hay comprensión transferible.

Aplica ahora la secuencia **1. identificar riesgos por objetivo → 2. priorizar exposición material → 3. asignar mitigación y contingency → 4. mapear dependencias con fechas y owners → 5. revisar triggers semanalmente**. Para cada paso conserva tres columnas: evidencia utilizada, alternativa descartada y razón. Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado y evita reescribir la historia después de conocer el desenlace.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla señala el lente que debes buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Project Management Institute — *A Guide to the Project Management Body of Knowledge (PMBOK Guide)* | gobernanza, dominios de desempeño, riesgo, stakeholders y entrega de valor | ¿Qué supuesto de **gestión de riesgos y dependencias** ayuda a desafiar? |
| Harold Kerzner — *Project Management* | integración de proyectos, control, madurez y alineación organizacional | ¿Qué supuesto de **gestión de riesgos y dependencias** ayuda a desafiar? |
| Gene Kim — *The Unicorn Project* | perspectiva de Operaciones tecnológicas aplicada al problema de la clase | ¿Qué supuesto de **gestión de riesgos y dependencias** ayuda a desafiar? |
| David J. Anderson — *Kanban* | flujo, trabajo en proceso, políticas explícitas y evolución del sistema | ¿Qué supuesto de **gestión de riesgos y dependencias** ayuda a desafiar? |
| Eliyahu M. Goldratt & Jeff Cox — *The Goal* | restricciones, throughput, inventario y pensamiento de flujo | ¿Qué supuesto de **gestión de riesgos y dependencias** ayuda a desafiar? |

En **gestión de riesgos y dependencias**, la lectura se evalúa por **uso**, no por cantidad de páginas. La nota debe indicar qué tesis de las fuentes modifica tu lectura de **risk**, qué evidencia del caso tensiona esa tesis y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación:** Una integración depende de un proveedor que aún no firmó API SLA. El proyecto la marca 'verde' porque el equipo interno está en fecha.

**Paso 1 — identificar riesgos por objetivo.** La gerencia escribe primero el supuesto asociado a **risk** y evita convertirlo en hecho. Luego busca **riesgos vencidos** para contrastarlo en el caso de **gestión de riesgos y dependencias**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 2 — priorizar exposición material.** La gerencia escribe primero el supuesto asociado a **issue** y evita convertirlo en hecho. Luego busca **issues que antes eran riesgos** para contrastarlo en el caso de **gestión de riesgos y dependencias**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 3 — asignar mitigación y contingency.** La gerencia escribe primero el supuesto asociado a **dependency** y evita convertirlo en hecho. Luego busca **dependencias sin compromiso** para contrastarlo en el caso de **gestión de riesgos y dependencias**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 4 — mapear dependencias con fechas y owners.** La gerencia escribe primero el supuesto asociado a **mitigation** y evita convertirlo en hecho. Luego busca **exposición residual** para contrastarlo en el caso de **gestión de riesgos y dependencias**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 5 — revisar triggers semanalmente.** La gerencia escribe primero el supuesto asociado a **contingency** y evita convertirlo en hecho. Luego busca **contingencias activadas** para contrastarlo en el caso de **gestión de riesgos y dependencias**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Síntesis del caso.** La recomendación debe terminar con responsable, fecha, evidencia de éxito y señal de stop. En **gestión de riesgos y dependencias**, omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo |
|---|---|---|---|
| **risk** | evento incierto que puede afectar objetivos | Cuando riesgos vencidos es observable y accionable. | Sobrerreaccionar a una señal parcial. |
| **issue** | problema que ya ocurrió | Cuando la primera explicación no distingue mecanismo o responsabilidad. | Convertir el concepto en etiqueta. |
| **Experimento/revisión** | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar eternamente y no decidir. |
| **Escalamiento** | Elevar autoridad o especialidad | Cuando hay derechos, capital material, regulación o irreversibilidad. | Delegar hacia arriba lo que sí corresponde decidir. |

**Frontera de aplicación:** Un risk register enorme puede ocultar lo material. Distingue riesgos de proyecto de incertidumbre normal y escala los que afectan estrategia, seguridad o compliance.

## 🪜 De profesional a owner

| Nivel | Responsabilidad sobre gestión de riesgos y dependencias |
|---|---|
| **Profesional** | usa **gestión de riesgos y dependencias** para mejorar una contribución propia y explicar sus supuestos con evidencia. |
| **Jefe / Team Lead** | aplica **risk** y **issue** para coordinar personas sin sustituir conversación por métricas. |
| **Manager / Gerente** | conecta riesgos vencidos con capacidad, presupuesto, dependencias y riesgo interáreas. |
| **CEO / Director** | decide si gestión de riesgos y dependencias cambia estrategia, economía o riesgo de empresa y qué debe llegar al comité o directorio. |
| **Founder / Owner** | pregunta si la solución de gestión de riesgos y dependencias reduce dependencia del fundador, preserva caja y puede operar como sistema repetible. |

El cambio de nivel en **gestión de riesgos y dependencias** aumenta el número de personas, dinero, dependencias y consecuencias que quedan dentro de la decisión. Por eso la misma herramienta debe volverse más explícita en evidencia, gobernanza y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Una integración depende de un proveedor que aún no firmó API SLA. El proyecto la marca 'verde' porque el equipo interno está en fecha.

Entrega un **decision brief de gestión de riesgos y dependencias** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre personas, cliente, operación, caja y riesgo; (e) recomendación; (f) condición que haría cambiarla; (g) dueño y fecha de revisión. Utiliza al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica

1. Reconstruye el caso de **gestión de riesgos y dependencias** con una tabla `hecho / interpretación / hipótesis / decisión`.
2. Ejecuta **1. identificar riesgos por objetivo → 2. priorizar exposición material → 3. asignar mitigación y contingency → 4. mapear dependencias con fechas y owners → 5. revisar triggers semanalmente** y adjunta evidencia para cada transición entre pasos.
3. Calcula o documenta riesgos vencidos, issues que antes eran riesgos; si no existe dato, diseña cómo obtenerlo.
4. Escribe una alternativa que contradiga tu preferencia inicial y haz un *pre-mortem* específico del caso.
5. Lee dos referencias, registra una coincidencia y una tensión, y modifica el brief si corresponde.
6. Repite la decisión desde el rol de CEO/owner: identifica qué cambia al aumentar el alcance y la irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar risk y issue como sinónimos | Se pierde la distinción entre “evento incierto que puede afectar objetivos” y “problema que ya ocurrió” | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por “revisar triggers semanalmente” | Se saltó “identificar riesgos por objetivo” y la solución llegó antes que el diagnóstico | Reconstruye la cadena 1. identificar riesgos por objetivo → 2. priorizar exposición material → 3. asignar mitigación y contingency → 4. mapear dependencias con fechas y owners → 5. revisar triggers semanalmente y marca el primer supuesto no demostrado. |
| Optimizar solo riesgos vencidos | La métrica local sustituyó al resultado del sistema | Contrástala con issues que antes eran riesgos y explicita el costo de oportunidad. |
| Generalizar desde un caso favorable | Se confundió evidencia local con una regla universal sobre gestión de riesgos y dependencias | Un risk register enorme puede ocultar lo material. Distingue riesgos de proyecto de incertidumbre normal y escala los que afectan estrategia, seguridad o compliance. |
| No fijar revisión | Una decisión sobre gestión de riesgos y dependencias se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de stop. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **risk** y **issue** usando un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **dependency** y qué observación obligaría a rechazar tu interpretación?
3. Aplica **identificar riesgos por objetivo → priorizar exposición material** al caso de la clase. ¿Qué dato todavía falta?
4. ¿Por qué **riesgos vencidos** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la tabla de lectura. ¿Dónde podrían llevar a recomendaciones distintas para **gestión de riesgos y dependencias**?
6. ¿Qué decisión equivocada podría producirse si se ignora este límite: **Un risk register enorme puede ocultar lo material. Distingue riesgos de proyecto de incertidumbre normal y escala los que afectan estrategia, seguridad o compliance.**?

## 📥 Entregable

Guarda en `portfolio/077-gestion-de-riesgos-y-dependencias/`:

- `risk-governance-brief.md` con el problema específico de **gestión de riesgos y dependencias**, evidencia, alternativas, decisión y gobernanza;
- `reading-note.md` contrastando las fuentes de **gestión de riesgos y dependencias** con edición/páginas consultadas;
- `decision-journal.md` registrando los supuestos de **risk**, confianza, responsable y revisión;
- `red-team.md` con la objeción más fuerte al caso **Una integración depende de un proveedor que aún no firmó API SLA. El proyecto la marca 'verde' porque el equipo interno está en fecha.** y el dato que podría invalidar la recomendación.

## 📗 Fuentes y verificación

- Project Management Institute — *A Guide to the Project Management Body of Knowledge (PMBOK Guide)*. **Uso en esta clase:** gobernanza, dominios de desempeño, riesgo, stakeholders y entrega de valor. Lectura selectiva: índice/capítulos pertinentes a **gestión de riesgos y dependencias**; registra edición y páginas consultadas.
- Harold Kerzner — *Project Management*. **Uso en esta clase:** integración de proyectos, control, madurez y alineación organizacional. Lectura selectiva: índice/capítulos pertinentes a **gestión de riesgos y dependencias**; registra edición y páginas consultadas.
- Gene Kim — *The Unicorn Project*. **Uso en esta clase:** perspectiva de Operaciones tecnológicas aplicada al problema de la clase. Lectura selectiva: índice/capítulos pertinentes a **gestión de riesgos y dependencias**; registra edición y páginas consultadas.
- David J. Anderson — *Kanban*. **Uso en esta clase:** flujo, trabajo en proceso, políticas explícitas y evolución del sistema. Lectura selectiva: índice/capítulos pertinentes a **gestión de riesgos y dependencias**; registra edición y páginas consultadas.
- Eliyahu M. Goldratt & Jeff Cox — *The Goal*. **Uso en esta clase:** restricciones, throughput, inventario y pensamiento de flujo. Lectura selectiva: índice/capítulos pertinentes a **gestión de riesgos y dependencias**; registra edición y páginas consultadas.
- Ken Schwaber & Jeff Sutherland — *The Scrum Guide*. **Uso en esta clase:** empirismo, transparencia, inspección y adaptación. Lectura selectiva: índice/capítulos pertinentes a **gestión de riesgos y dependencias**; registra edición y páginas consultadas.
- Susan A. Ambrose et al. — *How Learning Works*. **Uso en esta clase:** diseñar los objetivos, la práctica y el feedback de **gestión de riesgos y dependencias** sobre conocimiento previo verificable.
- Peter C. Brown, Henry L. Roediger III & Mark A. McDaniel — *Make It Stick*. **Uso en esta clase:** justificar la recuperación inicial y las preguntas de comprobación de **gestión de riesgos y dependencias**.
- Grant Wiggins & Jay McTighe — *Understanding by Design*. **Uso en esta clase:** derivar el entregable de **gestión de riesgos y dependencias** desde el desempeño observable y no desde el temario.
- Anders Ericsson & Robert Pool — *Peak*. **Uso en esta clase:** convertir la práctica de **gestión de riesgos y dependencias** en práctica deliberada con criterios explícitos.
- William Ellet — *The Case Study Handbook*. **Uso en esta clase:** estructurar el caso ejecutivo de **gestión de riesgos y dependencias** como problema, evidencia, alternativas y recomendación.

> **Regla de fuentes para Gestión de riesgos y dependencias:** las obras anteriores estructuran las perspectivas de esta materia; cualquier norma, ley, impuesto o estándar vivo mencionado en **gestión de riesgos y dependencias** debe comprobarse nuevamente en su fuente primaria vigente. El desarrollo es original y no reproduce capítulos protegidos.
