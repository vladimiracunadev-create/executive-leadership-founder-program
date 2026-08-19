# Clase 082 — Calidad y Definition of Done

**Parte:** 06 — Proyectos, Agile y entrega  
**Nivel:** Etapa 2 — Jefe → Manager  
**Duración sugerida:** 150–180 minutos · **Estándar:** deep-class-v2

## 🎯 Propósito

Calidad y Definition of Done convierten 'terminado' en un estándar verificable. La calidad no se inspecciona únicamente al final; se diseña en criterios, pruebas y controles del proceso. Una DoD común evita que cada persona declare completo un trabajo con deuda oculta distinta.

La salida de esta parte es **entregar proyectos con alcance, flujo, riesgo, calidad y gobernanza adaptativa**. En esta clase, esa progresión se concreta al exigir que cada afirmación sobre **calidad y Definition of Done** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

## 📚 Resultados de aprendizaje

Al finalizar podrás:

1. **Distinguir** `quality`, `Definition of Done`, `acceptance criteria`, `defect`, `quality debt` mediante observables, no por memoria verbal.
2. **Explicar** por qué esas distinciones cambian una decisión de jefe → manager.
3. **Aplicar** la secuencia **1. definir calidad relevante al usuario y riesgo → 2. crear DoD común → 3. automatizar controles repetibles → 4. detectar defectos cerca de origen → 5. medir defect escape y rework** conservando supuestos, alternativas y trazabilidad.
4. **Interpretar** defect escape rate, rework, automated checks sin confundir señal, explicación y causalidad.
5. **Resolver** el caso ejecutivo con al menos dos opciones plausibles y un criterio explícito de stop/revisión.
6. **Contrastar** dos obras de referencia y explicar dónde sus lentes son complementarias o entran en tensión.

## 🧭 Agenda

| Tramo | Evidencia de aprendizaje |
|---|---|
| 0–20 min | Recuperación: define quality y Definition of Done sin mirar la tabla; corrige con la fuente. |
| 20–70 min | Lectura guiada de conceptos + contraste de dos referencias. |
| 70–115 min | Ejemplo trabajado con defect escape rate y trazabilidad de supuestos. |
| 115–155 min | Caso ejecutivo: dos alternativas, trade-offs y decisión provisional. |
| 155–180 min | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar comprensión |
|---|---|---|
| **quality** | grado en que un resultado cumple requisitos y es apto para uso | Distingue un hecho compatible y otro que lo refute. |
| **Definition of Done** | criterios comunes que un incremento debe cumplir para considerarse terminado | Distingue un hecho compatible y otro que lo refute. |
| **acceptance criteria** | condiciones específicas de una historia o deliverable | Distingue un hecho compatible y otro que lo refute. |
| **defect** | desviación de requisito o expectativa verificable | Distingue un hecho compatible y otro que lo refute. |
| **quality debt** | trabajo futuro creado al aceptar calidad insuficiente | Distingue un hecho compatible y otro que lo refute. |

## 🧠 Modelo mental

```text
1. definir calidad relevante al usuario y riesgo → 2. crear DoD común → 3. automatizar controles repetibles → 4. detectar defectos cerca de origen → 5. medir defect escape y rework
```

La secuencia nace del problema de esta clase: **Calidad y Definition of Done convierten 'terminado' en un estándar verificable. La calidad no se inspecciona únicamente al final; se diseña en criterios, pruebas y controles del proceso. Una DoD común evita que cada persona declare completo un trabajo con deuda oculta distinta.** El método es útil mientras las condiciones permitan observar las señales requeridas. No elimina incertidumbre; la hace visible y obliga a decidir proporcionalmente a la evidencia. Límite principal: **Una DoD maximalista puede bloquear aprendizaje temprano. Diferencia prototipo experimental de incremento de producción y aplica estándares acordes al propósito.**

## 📖 Desarrollo

### 1. quality: mecanismo central

**quality** se entiende aquí como **grado en que un resultado cumple requisitos y es apto para uso**. Esta es la pieza causal o estructural desde la que se inicia **calidad y Definition of Done**: antes de definir calidad relevante al usuario y riesgo, el gerente debe poder señalar qué cambia en el sistema si el concepto está presente y qué debería observar si no lo está. Una definición que no produce predicciones observables todavía es demasiado vaga para dirigir.

La lectura rectora de este bloque es Project Management Institute — *A Guide to the Project Management Body of Knowledge (PMBOK Guide)*. Su aporte se usa para examinar **gobernanza, dominios de desempeño, riesgo, stakeholders y entrega de valor**. Aplica esa lente al caso sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **defect escape rate**; regístrala con periodo, unidad, población y baseline.

Relaciona el mecanismo con **Definition of Done**. Si ambos cambian juntos, no concluyas causalidad automáticamente: identifica una tercera variable o mecanismo alternativo que también pueda explicar el patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Definition of Done: frontera conceptual y error de clasificación

**Definición operacional:** criterios comunes que un incremento debe cumplir para considerarse terminado. Su valor está en distinguirlo de **quality** y **acceptance criteria**. En una decisión real, clasificar una situación en la categoría equivocada cambia la intervención: puedes asignar autoridad donde faltaba información, medir un output cuando debías observar un proceso o tratar una restricción como si fuera una preferencia.

Contrasta el problema con Harold Kerzner — *Project Management*, que aporta una mirada sobre **integración de proyectos, control, madurez y alineación organizacional**. Formula dos mini-casos: uno que sí satisface la definición de **Definition of Done** y otro que solo se parece superficialmente. Luego pregunta qué señal distinguiría ambos; para esta clase, **rework** es una candidata, pero debe combinarse con evidencia cualitativa o documental cuando el fenómeno no sea directamente medible.

Antes de crear dod común, registra explícitamente qué decisión sería errónea si esta frontera conceptual se ignora. Esa frase convierte el vocabulario en criterio gerencial.

### 3. acceptance criteria: operacionalización y medición

**acceptance criteria** significa **condiciones específicas de una historia o deliverable**. El problema ya no es definirlo, sino **operacionalizarlo**: qué contar, durante qué ventana, con qué denominador, contra qué baseline y con qué segmentación. Una métrica útil conserva suficiente contexto para no confundir mejora local con mejora del sistema.

David J. Anderson — *Kanban* orienta este bloque mediante **flujo, trabajo en proceso, políticas explícitas y evolución del sistema**. Usa esa perspectiva para diseñar una ficha de medición: `señal → fórmula/criterio → fuente → frecuencia → owner → interpretación permitida → interpretación prohibida`. La señal asignada es **automated checks**. Si no existe un dato confiable, la salida correcta no es inventar precisión: diseña el mecanismo de captura y declara la incertidumbre.

Al llegar a automatizar controles repetibles, compara tendencia, distribución y casos atípicos. Pregunta además si el indicador es *leading* o *lagging* y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; nunca convertirse en el objetivo que reemplaza al fenómeno.

### 4. defect: trade-offs y efectos de segundo orden

**Definición:** desviación de requisito o expectativa verificable. Este concepto obliga a abandonar la idea de que **calidad y Definition of Done** tiene una solución gratuita. Toda intervención consume autonomía, tiempo, caja, capacidad, atención, reputación o tolerancia al riesgo. Por eso, antes de detectar defectos cerca de origen, se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Atul Gawande — *The Checklist Manifesto* aporta una lente sobre **perspectiva de Ejecución aplicada al problema de la clase**. Úsala para construir una matriz `beneficio / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **DoD compliance** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la necesidad de observar efectos laterales fuera del KPI principal.

Haz un *pre-mortem* de **calidad y Definition of Done**: supone que la opción recomendada fracasó seis meses después y enumera tres mecanismos que podrían explicarlo. Al menos uno debe provenir de un efecto de segundo orden asociado a **defect** y otro de una hipótesis del caso que nunca fue validada.

### 5. quality debt: gobernanza, límites e integración

**quality debt** se define como **trabajo futuro creado al aceptar calidad insuficiente** y cierra el circuito porque traduce análisis en responsabilidad. La pregunta ejecutiva es quién decide, quién ejecuta, quién debe ser consultado, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar.

Gene Kim — *The Unicorn Project* se utiliza para estudiar **perspectiva de Operaciones tecnológicas aplicada al problema de la clase** y contrastar la recomendación final. Al ejecutar medir defect escape y rework, deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento. Esa trazabilidad protege contra el sesgo retrospectivo y mejora las revisiones posteriores.

La frontera de esta clase es explícita: **Una DoD maximalista puede bloquear aprendizaje temprano. Diferencia prototipo experimental de incremento de producción y aplica estándares acordes al propósito.**. Conviértela en una regla operativa: `si ocurre X → no aplicar automáticamente → consultar/escalar/revalidar`. Integrar **quality**, **Definition of Done**, **acceptance criteria**, **defect** y **quality debt** significa poder explicar qué parte del diagnóstico sostiene la decisión y cuál sigue siendo una apuesta.

### 6. Integración: de conceptos a una decisión defendible

La síntesis de **calidad y Definition of Done** no consiste en sumar cinco definiciones. Empieza por **quality**, contrasta **Definition of Done** con **acceptance criteria**, incorpora **defect** como restricción o mecanismo y usa **quality debt** para cerrar el ciclo. Si el análisis no puede explicar cuál de esas piezas cambió la recomendación, todavía no hay comprensión transferible.

Aplica ahora la secuencia **1. definir calidad relevante al usuario y riesgo → 2. crear DoD común → 3. automatizar controles repetibles → 4. detectar defectos cerca de origen → 5. medir defect escape y rework**. Para cada paso conserva tres columnas: evidencia utilizada, alternativa descartada y razón. Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado y evita reescribir la historia después de conocer el desenlace.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla señala el lente que debes buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Project Management Institute — *A Guide to the Project Management Body of Knowledge (PMBOK Guide)* | gobernanza, dominios de desempeño, riesgo, stakeholders y entrega de valor | ¿Qué supuesto de **calidad y Definition of Done** ayuda a desafiar? |
| Harold Kerzner — *Project Management* | integración de proyectos, control, madurez y alineación organizacional | ¿Qué supuesto de **calidad y Definition of Done** ayuda a desafiar? |
| David J. Anderson — *Kanban* | flujo, trabajo en proceso, políticas explícitas y evolución del sistema | ¿Qué supuesto de **calidad y Definition of Done** ayuda a desafiar? |
| Atul Gawande — *The Checklist Manifesto* | perspectiva de Ejecución aplicada al problema de la clase | ¿Qué supuesto de **calidad y Definition of Done** ayuda a desafiar? |
| Gene Kim — *The Unicorn Project* | perspectiva de Operaciones tecnológicas aplicada al problema de la clase | ¿Qué supuesto de **calidad y Definition of Done** ayuda a desafiar? |

En **calidad y Definition of Done**, la lectura se evalúa por **uso**, no por cantidad de páginas. La nota debe indicar qué tesis de las fuentes modifica tu lectura de **quality**, qué evidencia del caso tensiona esa tesis y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación:** Un equipo marca historias 'Done' cuando termina desarrollo, aunque pruebas de seguridad y documentación ocurren semanas después. El sprint parece exitoso y el release acumula cola invisible.

**Paso 1 — definir calidad relevante al usuario y riesgo.** La gerencia escribe primero el supuesto asociado a **quality** y evita convertirlo en hecho. Luego busca **defect escape rate** para contrastarlo en el caso de **calidad y Definition of Done**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 2 — crear DoD común.** La gerencia escribe primero el supuesto asociado a **Definition of Done** y evita convertirlo en hecho. Luego busca **rework** para contrastarlo en el caso de **calidad y Definition of Done**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 3 — automatizar controles repetibles.** La gerencia escribe primero el supuesto asociado a **acceptance criteria** y evita convertirlo en hecho. Luego busca **automated checks** para contrastarlo en el caso de **calidad y Definition of Done**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 4 — detectar defectos cerca de origen.** La gerencia escribe primero el supuesto asociado a **defect** y evita convertirlo en hecho. Luego busca **DoD compliance** para contrastarlo en el caso de **calidad y Definition of Done**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 5 — medir defect escape y rework.** La gerencia escribe primero el supuesto asociado a **quality debt** y evita convertirlo en hecho. Luego busca **customer incidents** para contrastarlo en el caso de **calidad y Definition of Done**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Síntesis del caso.** La recomendación debe terminar con responsable, fecha, evidencia de éxito y señal de stop. En **calidad y Definition of Done**, omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo |
|---|---|---|---|
| **quality** | grado en que un resultado cumple requisitos y es apto para uso | Cuando defect escape rate es observable y accionable. | Sobrerreaccionar a una señal parcial. |
| **Definition of Done** | criterios comunes que un incremento debe cumplir para considerarse terminado | Cuando la primera explicación no distingue mecanismo o responsabilidad. | Convertir el concepto en etiqueta. |
| **Experimento/revisión** | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar eternamente y no decidir. |
| **Escalamiento** | Elevar autoridad o especialidad | Cuando hay derechos, capital material, regulación o irreversibilidad. | Delegar hacia arriba lo que sí corresponde decidir. |

**Frontera de aplicación:** Una DoD maximalista puede bloquear aprendizaje temprano. Diferencia prototipo experimental de incremento de producción y aplica estándares acordes al propósito.

## 🪜 De profesional a owner

| Nivel | Responsabilidad sobre calidad y Definition of Done |
|---|---|
| **Profesional** | usa **calidad y Definition of Done** para mejorar una contribución propia y explicar sus supuestos con evidencia. |
| **Jefe / Team Lead** | aplica **quality** y **Definition of Done** para coordinar personas sin sustituir conversación por métricas. |
| **Manager / Gerente** | conecta defect escape rate con capacidad, presupuesto, dependencias y riesgo interáreas. |
| **CEO / Director** | decide si calidad y Definition of Done cambia estrategia, economía o riesgo de empresa y qué debe llegar al comité o directorio. |
| **Founder / Owner** | pregunta si la solución de calidad y Definition of Done reduce dependencia del fundador, preserva caja y puede operar como sistema repetible. |

El cambio de nivel en **calidad y Definition of Done** aumenta el número de personas, dinero, dependencias y consecuencias que quedan dentro de la decisión. Por eso la misma herramienta debe volverse más explícita en evidencia, gobernanza y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Un equipo marca historias 'Done' cuando termina desarrollo, aunque pruebas de seguridad y documentación ocurren semanas después. El sprint parece exitoso y el release acumula cola invisible.

Entrega un **decision brief de calidad y Definition of Done** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre personas, cliente, operación, caja y riesgo; (e) recomendación; (f) condición que haría cambiarla; (g) dueño y fecha de revisión. Utiliza al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica

1. Reconstruye el caso de **calidad y Definition of Done** con una tabla `hecho / interpretación / hipótesis / decisión`.
2. Ejecuta **1. definir calidad relevante al usuario y riesgo → 2. crear DoD común → 3. automatizar controles repetibles → 4. detectar defectos cerca de origen → 5. medir defect escape y rework** y adjunta evidencia para cada transición entre pasos.
3. Calcula o documenta defect escape rate, rework; si no existe dato, diseña cómo obtenerlo.
4. Escribe una alternativa que contradiga tu preferencia inicial y haz un *pre-mortem* específico del caso.
5. Lee dos referencias, registra una coincidencia y una tensión, y modifica el brief si corresponde.
6. Repite la decisión desde el rol de CEO/owner: identifica qué cambia al aumentar el alcance y la irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar quality y Definition of Done como sinónimos | Se pierde la distinción entre “grado en que un resultado cumple requisitos y es apto para uso” y “criterios comunes que un incremento debe cumplir para considerarse terminado” | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por “medir defect escape y rework” | Se saltó “definir calidad relevante al usuario y riesgo” y la solución llegó antes que el diagnóstico | Reconstruye la cadena 1. definir calidad relevante al usuario y riesgo → 2. crear DoD común → 3. automatizar controles repetibles → 4. detectar defectos cerca de origen → 5. medir defect escape y rework y marca el primer supuesto no demostrado. |
| Optimizar solo defect escape rate | La métrica local sustituyó al resultado del sistema | Contrástala con rework y explicita el costo de oportunidad. |
| Generalizar desde un caso favorable | Se confundió evidencia local con una regla universal sobre calidad y Definition of Done | Una DoD maximalista puede bloquear aprendizaje temprano. Diferencia prototipo experimental de incremento de producción y aplica estándares acordes al propósito. |
| No fijar revisión | Una decisión sobre calidad y Definition of Done se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de stop. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **quality** y **Definition of Done** usando un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **acceptance criteria** y qué observación obligaría a rechazar tu interpretación?
3. Aplica **definir calidad relevante al usuario y riesgo → crear DoD común** al caso de la clase. ¿Qué dato todavía falta?
4. ¿Por qué **defect escape rate** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la tabla de lectura. ¿Dónde podrían llevar a recomendaciones distintas para **calidad y Definition of Done**?
6. ¿Qué decisión equivocada podría producirse si se ignora este límite: **Una DoD maximalista puede bloquear aprendizaje temprano. Diferencia prototipo experimental de incremento de producción y aplica estándares acordes al propósito.**?

## 📥 Entregable

Guarda en `portfolio/082-calidad-y-definition-of-done/`:

- `operating-improvement-brief.md` con el problema específico de **calidad y Definition of Done**, evidencia, alternativas, decisión y gobernanza;
- `reading-note.md` contrastando las fuentes de **calidad y Definition of Done** con edición/páginas consultadas;
- `decision-journal.md` registrando los supuestos de **quality**, confianza, responsable y revisión;
- `red-team.md` con la objeción más fuerte al caso **Un equipo marca historias 'Done' cuando termina desarrollo, aunque pruebas de seguridad y documentación ocurren semanas después. El sprint parece exitoso y el release acumula cola invisible.** y el dato que podría invalidar la recomendación.

## 📗 Fuentes y verificación

- Project Management Institute — *A Guide to the Project Management Body of Knowledge (PMBOK Guide)*. **Uso en esta clase:** gobernanza, dominios de desempeño, riesgo, stakeholders y entrega de valor. Lectura selectiva: índice/capítulos pertinentes a **calidad y Definition of Done**; registra edición y páginas consultadas.
- Harold Kerzner — *Project Management*. **Uso en esta clase:** integración de proyectos, control, madurez y alineación organizacional. Lectura selectiva: índice/capítulos pertinentes a **calidad y Definition of Done**; registra edición y páginas consultadas.
- David J. Anderson — *Kanban*. **Uso en esta clase:** flujo, trabajo en proceso, políticas explícitas y evolución del sistema. Lectura selectiva: índice/capítulos pertinentes a **calidad y Definition of Done**; registra edición y páginas consultadas.
- Atul Gawande — *The Checklist Manifesto*. **Uso en esta clase:** perspectiva de Ejecución aplicada al problema de la clase. Lectura selectiva: índice/capítulos pertinentes a **calidad y Definition of Done**; registra edición y páginas consultadas.
- Gene Kim — *The Unicorn Project*. **Uso en esta clase:** perspectiva de Operaciones tecnológicas aplicada al problema de la clase. Lectura selectiva: índice/capítulos pertinentes a **calidad y Definition of Done**; registra edición y páginas consultadas.
- Ken Schwaber & Jeff Sutherland — *The Scrum Guide*. **Uso en esta clase:** empirismo, transparencia, inspección y adaptación. Lectura selectiva: índice/capítulos pertinentes a **calidad y Definition of Done**; registra edición y páginas consultadas.
- Susan A. Ambrose et al. — *How Learning Works*. **Uso en esta clase:** diseñar los objetivos, la práctica y el feedback de **calidad y definition of done** sobre conocimiento previo verificable.
- Peter C. Brown, Henry L. Roediger III & Mark A. McDaniel — *Make It Stick*. **Uso en esta clase:** justificar la recuperación inicial y las preguntas de comprobación de **calidad y definition of done**.
- Grant Wiggins & Jay McTighe — *Understanding by Design*. **Uso en esta clase:** derivar el entregable de **calidad y definition of done** desde el desempeño observable y no desde el temario.
- Anders Ericsson & Robert Pool — *Peak*. **Uso en esta clase:** convertir la práctica de **calidad y definition of done** en práctica deliberada con criterios explícitos.
- William Ellet — *The Case Study Handbook*. **Uso en esta clase:** estructurar el caso ejecutivo de **calidad y definition of done** como problema, evidencia, alternativas y recomendación.

> **Regla de fuentes para Calidad y Definition of Done:** las obras anteriores estructuran las perspectivas de esta materia; cualquier norma, ley, impuesto o estándar vivo mencionado en **calidad y Definition of Done** debe comprobarse nuevamente en su fuente primaria vigente. El desarrollo es original y no reproduce capítulos protegidos.
