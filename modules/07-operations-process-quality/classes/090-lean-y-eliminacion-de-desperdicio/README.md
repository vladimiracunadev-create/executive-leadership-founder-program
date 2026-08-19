# Clase 090 — Lean y eliminación de desperdicio

**Parte:** 07 — Operaciones, procesos y calidad  
**Nivel:** Etapa 2 — Jefe → Manager  
**Duración sugerida:** 150–180 minutos · **Estándar:** deep-class-v2

## 🎯 Propósito

Lean entiende desperdicio como consumo de recursos que no crea valor para el cliente y puede reducirse sin dañar seguridad o calidad. Mejora flujo, calidad en origen y aprendizaje continuo. El objetivo no es recortar personas sino eliminar trabajo inútil y usar capacidad liberada para más valor.

La salida de esta parte es **operar procesos end-to-end con capacidad, calidad, continuidad y mejora**. En esta clase, esa progresión se concreta al exigir que cada afirmación sobre **lean y eliminación de desperdicio** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

## 📚 Resultados de aprendizaje

Al finalizar podrás:

1. **Distinguir** `valor`, `waste`, `flow`, `pull`, `kaizen` mediante observables, no por memoria verbal.
2. **Explicar** por qué esas distinciones cambian una decisión de jefe → manager.
3. **Aplicar** la secuencia **1. definir valor desde cliente → 2. mapear value stream → 3. identificar espera, defectos y exceso → 4. reducir lotes y crear pull → 5. estandarizar mejora y repetir** conservando supuestos, alternativas y trazabilidad.
4. **Interpretar** lead time, first-pass yield, WIP sin confundir señal, explicación y causalidad.
5. **Resolver** el caso ejecutivo con al menos dos opciones plausibles y un criterio explícito de stop/revisión.
6. **Contrastar** dos obras de referencia y explicar dónde sus lentes son complementarias o entran en tensión.

## 🧭 Agenda

| Tramo | Evidencia de aprendizaje |
|---|---|
| 0–20 min | Recuperación: define valor y waste sin mirar la tabla; corrige con la fuente. |
| 20–70 min | Lectura guiada de conceptos + contraste de dos referencias. |
| 70–115 min | Ejemplo trabajado con lead time y trazabilidad de supuestos. |
| 115–155 min | Caso ejecutivo: dos alternativas, trade-offs y decisión provisional. |
| 155–180 min | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar comprensión |
|---|---|---|
| **valor** | resultado por el que el cliente reconoce utilidad | Distingue un hecho compatible y otro que lo refute. |
| **waste** | actividad que consume recursos sin crear valor necesario | Distingue un hecho compatible y otro que lo refute. |
| **flow** | movimiento continuo con mínimas esperas y lotes | Distingue un hecho compatible y otro que lo refute. |
| **pull** | producción disparada por demanda real | Distingue un hecho compatible y otro que lo refute. |
| **kaizen** | mejora continua mediante cambios pequeños basados en observación | Distingue un hecho compatible y otro que lo refute. |

## 🧠 Modelo mental

```text
1. definir valor desde cliente → 2. mapear value stream → 3. identificar espera, defectos y exceso → 4. reducir lotes y crear pull → 5. estandarizar mejora y repetir
```

La secuencia nace del problema de esta clase: **Lean entiende desperdicio como consumo de recursos que no crea valor para el cliente y puede reducirse sin dañar seguridad o calidad. Mejora flujo, calidad en origen y aprendizaje continuo. El objetivo no es recortar personas sino eliminar trabajo inútil y usar capacidad liberada para más valor.** El método es útil mientras las condiciones permitan observar las señales requeridas. No elimina incertidumbre; la hace visible y obliga a decidir proporcionalmente a la evidencia. Límite principal: **Lean no es austeridad. Eliminar capacidad protectora sin comprender variabilidad puede hacer el sistema frágil; seguridad y calidad no son desperdicio.**

## 📖 Desarrollo

### 1. valor: mecanismo central

**valor** se entiende aquí como **resultado por el que el cliente reconoce utilidad**. Esta es la pieza causal o estructural desde la que se inicia **lean y eliminación de desperdicio**: antes de definir valor desde cliente, el gerente debe poder señalar qué cambia en el sistema si el concepto está presente y qué debería observar si no lo está. Una definición que no produce predicciones observables todavía es demasiado vaga para dirigir.

La lectura rectora de este bloque es Nigel Slack & Alistair Brandon-Jones — *Operations Management*. Su aporte se usa para examinar **capacidad, procesos, variabilidad, calidad y estrategia de operaciones**. Aplica esa lente al caso sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **lead time**; regístrala con periodo, unidad, población y baseline.

Relaciona el mecanismo con **waste**. Si ambos cambian juntos, no concluyas causalidad automáticamente: identifica una tercera variable o mecanismo alternativo que también pueda explicar el patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. waste: frontera conceptual y error de clasificación

**Definición operacional:** actividad que consume recursos sin crear valor necesario. Su valor está en distinguirlo de **valor** y **flow**. En una decisión real, clasificar una situación en la categoría equivocada cambia la intervención: puedes asignar autoridad donde faltaba información, medir un output cuando debías observar un proceso o tratar una restricción como si fuera una preferencia.

Contrasta el problema con Eliyahu M. Goldratt & Jeff Cox — *The Goal*, que aporta una mirada sobre **restricciones, throughput, inventario y pensamiento de flujo**. Formula dos mini-casos: uno que sí satisface la definición de **waste** y otro que solo se parece superficialmente. Luego pregunta qué señal distinguiría ambos; para esta clase, **first-pass yield** es una candidata, pero debe combinarse con evidencia cualitativa o documental cuando el fenómeno no sea directamente medible.

Antes de mapear value stream, registra explícitamente qué decisión sería errónea si esta frontera conceptual se ignora. Esa frase convierte el vocabulario en criterio gerencial.

### 3. flow: operacionalización y medición

**flow** significa **movimiento continuo con mínimas esperas y lotes**. El problema ya no es definirlo, sino **operacionalizarlo**: qué contar, durante qué ventana, con qué denominador, contra qué baseline y con qué segmentación. Una métrica útil conserva suficiente contexto para no confundir mejora local con mejora del sistema.

Geary A. Rummler & Alan P. Brache — *Improving Performance* orienta este bloque mediante **perspectiva de Procesos aplicada al problema de la clase**. Usa esa perspectiva para diseñar una ficha de medición: `señal → fórmula/criterio → fuente → frecuencia → owner → interpretación permitida → interpretación prohibida`. La señal asignada es **WIP**. Si no existe un dato confiable, la salida correcta no es inventar precisión: diseña el mecanismo de captura y declara la incertidumbre.

Al llegar a identificar espera, defectos y exceso, compara tendencia, distribución y casos atípicos. Pregunta además si el indicador es *leading* o *lagging* y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; nunca convertirse en el objetivo que reemplaza al fenómeno.

### 4. pull: trade-offs y efectos de segundo orden

**Definición:** producción disparada por demanda real. Este concepto obliga a abandonar la idea de que **lean y eliminación de desperdicio** tiene una solución gratuita. Toda intervención consume autonomía, tiempo, caja, capacidad, atención, reputación o tolerancia al riesgo. Por eso, antes de reducir lotes y crear pull, se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

James P. Womack, Daniel T. Jones & Daniel Roos — *The Machine That Changed the World* aporta una lente sobre **perspectiva de Lean aplicada al problema de la clase**. Úsala para construir una matriz `beneficio / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **rework** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la necesidad de observar efectos laterales fuera del KPI principal.

Haz un *pre-mortem* de **lean y eliminación de desperdicio**: supone que la opción recomendada fracasó seis meses después y enumera tres mecanismos que podrían explicarlo. Al menos uno debe provenir de un efecto de segundo orden asociado a **pull** y otro de una hipótesis del caso que nunca fue validada.

### 5. kaizen: gobernanza, límites e integración

**kaizen** se define como **mejora continua mediante cambios pequeños basados en observación** y cierra el circuito porque traduce análisis en responsabilidad. La pregunta ejecutiva es quién decide, quién ejecuta, quién debe ser consultado, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar.

ISO — *ISO 22301 Business continuity management systems* se utiliza para estudiar **sistema de gestión de continuidad y preparación ante disrupciones** y contrastar la recomendación final. Al ejecutar estandarizar mejora y repetir, deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento. Esa trazabilidad protege contra el sesgo retrospectivo y mejora las revisiones posteriores.

La frontera de esta clase es explícita: **Lean no es austeridad. Eliminar capacidad protectora sin comprender variabilidad puede hacer el sistema frágil; seguridad y calidad no son desperdicio.**. Conviértela en una regla operativa: `si ocurre X → no aplicar automáticamente → consultar/escalar/revalidar`. Integrar **valor**, **waste**, **flow**, **pull** y **kaizen** significa poder explicar qué parte del diagnóstico sostiene la decisión y cuál sigue siendo una apuesta.

### 6. Integración: de conceptos a una decisión defendible

La síntesis de **lean y eliminación de desperdicio** no consiste en sumar cinco definiciones. Empieza por **valor**, contrasta **waste** con **flow**, incorpora **pull** como restricción o mecanismo y usa **kaizen** para cerrar el ciclo. Si el análisis no puede explicar cuál de esas piezas cambió la recomendación, todavía no hay comprensión transferible.

Aplica ahora la secuencia **1. definir valor desde cliente → 2. mapear value stream → 3. identificar espera, defectos y exceso → 4. reducir lotes y crear pull → 5. estandarizar mejora y repetir**. Para cada paso conserva tres columnas: evidencia utilizada, alternativa descartada y razón. Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado y evita reescribir la historia después de conocer el desenlace.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla señala el lente que debes buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Nigel Slack & Alistair Brandon-Jones — *Operations Management* | capacidad, procesos, variabilidad, calidad y estrategia de operaciones | ¿Qué supuesto de **lean y eliminación de desperdicio** ayuda a desafiar? |
| Eliyahu M. Goldratt & Jeff Cox — *The Goal* | restricciones, throughput, inventario y pensamiento de flujo | ¿Qué supuesto de **lean y eliminación de desperdicio** ayuda a desafiar? |
| Geary A. Rummler & Alan P. Brache — *Improving Performance* | perspectiva de Procesos aplicada al problema de la clase | ¿Qué supuesto de **lean y eliminación de desperdicio** ayuda a desafiar? |
| James P. Womack, Daniel T. Jones & Daniel Roos — *The Machine That Changed the World* | perspectiva de Lean aplicada al problema de la clase | ¿Qué supuesto de **lean y eliminación de desperdicio** ayuda a desafiar? |
| ISO — *ISO 22301 Business continuity management systems* | sistema de gestión de continuidad y preparación ante disrupciones | ¿Qué supuesto de **lean y eliminación de desperdicio** ayuda a desafiar? |

En **lean y eliminación de desperdicio**, la lectura se evalúa por **uso**, no por cantidad de páginas. La nota debe indicar qué tesis de las fuentes modifica tu lectura de **valor**, qué evidencia del caso tensiona esa tesis y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación:** Una organización 'lean' elimina buffer y headcount sin rediseñar flujo. La utilización sube, pero incidentes y espera empeoran porque cualquier variación paraliza el proceso.

**Paso 1 — definir valor desde cliente.** La gerencia escribe primero el supuesto asociado a **valor** y evita convertirlo en hecho. Luego busca **lead time** para contrastarlo en el caso de **lean y eliminación de desperdicio**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 2 — mapear value stream.** La gerencia escribe primero el supuesto asociado a **waste** y evita convertirlo en hecho. Luego busca **first-pass yield** para contrastarlo en el caso de **lean y eliminación de desperdicio**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 3 — identificar espera, defectos y exceso.** La gerencia escribe primero el supuesto asociado a **flow** y evita convertirlo en hecho. Luego busca **WIP** para contrastarlo en el caso de **lean y eliminación de desperdicio**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 4 — reducir lotes y crear pull.** La gerencia escribe primero el supuesto asociado a **pull** y evita convertirlo en hecho. Luego busca **rework** para contrastarlo en el caso de **lean y eliminación de desperdicio**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 5 — estandarizar mejora y repetir.** La gerencia escribe primero el supuesto asociado a **kaizen** y evita convertirlo en hecho. Luego busca **porcentaje de valor agregado** para contrastarlo en el caso de **lean y eliminación de desperdicio**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Síntesis del caso.** La recomendación debe terminar con responsable, fecha, evidencia de éxito y señal de stop. En **lean y eliminación de desperdicio**, omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo |
|---|---|---|---|
| **valor** | resultado por el que el cliente reconoce utilidad | Cuando lead time es observable y accionable. | Sobrerreaccionar a una señal parcial. |
| **waste** | actividad que consume recursos sin crear valor necesario | Cuando la primera explicación no distingue mecanismo o responsabilidad. | Convertir el concepto en etiqueta. |
| **Experimento/revisión** | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar eternamente y no decidir. |
| **Escalamiento** | Elevar autoridad o especialidad | Cuando hay derechos, capital material, regulación o irreversibilidad. | Delegar hacia arriba lo que sí corresponde decidir. |

**Frontera de aplicación:** Lean no es austeridad. Eliminar capacidad protectora sin comprender variabilidad puede hacer el sistema frágil; seguridad y calidad no son desperdicio.

## 🪜 De profesional a owner

| Nivel | Responsabilidad sobre lean y eliminación de desperdicio |
|---|---|
| **Profesional** | usa **lean y eliminación de desperdicio** para mejorar una contribución propia y explicar sus supuestos con evidencia. |
| **Jefe / Team Lead** | aplica **valor** y **waste** para coordinar personas sin sustituir conversación por métricas. |
| **Manager / Gerente** | conecta lead time con capacidad, presupuesto, dependencias y riesgo interáreas. |
| **CEO / Director** | decide si lean y eliminación de desperdicio cambia estrategia, economía o riesgo de empresa y qué debe llegar al comité o directorio. |
| **Founder / Owner** | pregunta si la solución de lean y eliminación de desperdicio reduce dependencia del fundador, preserva caja y puede operar como sistema repetible. |

El cambio de nivel en **lean y eliminación de desperdicio** aumenta el número de personas, dinero, dependencias y consecuencias que quedan dentro de la decisión. Por eso la misma herramienta debe volverse más explícita en evidencia, gobernanza y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Una organización 'lean' elimina buffer y headcount sin rediseñar flujo. La utilización sube, pero incidentes y espera empeoran porque cualquier variación paraliza el proceso.

Entrega un **decision brief de lean y eliminación de desperdicio** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre personas, cliente, operación, caja y riesgo; (e) recomendación; (f) condición que haría cambiarla; (g) dueño y fecha de revisión. Utiliza al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica

1. Reconstruye el caso de **lean y eliminación de desperdicio** con una tabla `hecho / interpretación / hipótesis / decisión`.
2. Ejecuta **1. definir valor desde cliente → 2. mapear value stream → 3. identificar espera, defectos y exceso → 4. reducir lotes y crear pull → 5. estandarizar mejora y repetir** y adjunta evidencia para cada transición entre pasos.
3. Calcula o documenta lead time, first-pass yield; si no existe dato, diseña cómo obtenerlo.
4. Escribe una alternativa que contradiga tu preferencia inicial y haz un *pre-mortem* específico del caso.
5. Lee dos referencias, registra una coincidencia y una tensión, y modifica el brief si corresponde.
6. Repite la decisión desde el rol de CEO/owner: identifica qué cambia al aumentar el alcance y la irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar valor y waste como sinónimos | Se pierde la distinción entre “resultado por el que el cliente reconoce utilidad” y “actividad que consume recursos sin crear valor necesario” | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por “estandarizar mejora y repetir” | Se saltó “definir valor desde cliente” y la solución llegó antes que el diagnóstico | Reconstruye la cadena 1. definir valor desde cliente → 2. mapear value stream → 3. identificar espera, defectos y exceso → 4. reducir lotes y crear pull → 5. estandarizar mejora y repetir y marca el primer supuesto no demostrado. |
| Optimizar solo lead time | La métrica local sustituyó al resultado del sistema | Contrástala con first-pass yield y explicita el costo de oportunidad. |
| Generalizar desde un caso favorable | Se confundió evidencia local con una regla universal sobre lean y eliminación de desperdicio | Lean no es austeridad. Eliminar capacidad protectora sin comprender variabilidad puede hacer el sistema frágil; seguridad y calidad no son desperdicio. |
| No fijar revisión | Una decisión sobre lean y eliminación de desperdicio se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de stop. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **valor** y **waste** usando un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **flow** y qué observación obligaría a rechazar tu interpretación?
3. Aplica **definir valor desde cliente → mapear value stream** al caso de la clase. ¿Qué dato todavía falta?
4. ¿Por qué **lead time** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la tabla de lectura. ¿Dónde podrían llevar a recomendaciones distintas para **lean y eliminación de desperdicio**?
6. ¿Qué decisión equivocada podría producirse si se ignora este límite: **Lean no es austeridad. Eliminar capacidad protectora sin comprender variabilidad puede hacer el sistema frágil; seguridad y calidad no son desperdicio.**?

## 📥 Entregable

Guarda en `portfolio/090-lean-y-eliminacion-de-desperdicio/`:

- `leadership-decision-brief.md` con el problema específico de **lean y eliminación de desperdicio**, evidencia, alternativas, decisión y gobernanza;
- `reading-note.md` contrastando las fuentes de **lean y eliminación de desperdicio** con edición/páginas consultadas;
- `decision-journal.md` registrando los supuestos de **valor**, confianza, responsable y revisión;
- `red-team.md` con la objeción más fuerte al caso **Una organización 'lean' elimina buffer y headcount sin rediseñar flujo. La utilización sube, pero incidentes y espera empeoran porque cualquier variación paraliza el proceso.** y el dato que podría invalidar la recomendación.

## 📗 Fuentes y verificación

- Nigel Slack & Alistair Brandon-Jones — *Operations Management* (Pearson Education, Limited, 2019). **Uso en esta clase:** capacidad, procesos, variabilidad, calidad y estrategia de operaciones. Lectura selectiva sobre **lean y eliminación de desperdicio**. **Localizador:** [ISBN-13 9781292254036](https://openlibrary.org/isbn/9781292254036).
- Eliyahu M. Goldratt & Jeff Cox — *The Goal* (HighBridge Audio, 2014). **Uso en esta clase:** restricciones, throughput, inventario y pensamiento de flujo. Lectura selectiva sobre **lean y eliminación de desperdicio**. **Localizador:** [ISBN-13 9781622313945](https://openlibrary.org/isbn/9781622313945).
- Geary A. Rummler & Alan P. Brache — *Improving Performance* (Jossey-Bass, 1995). **Uso en esta clase:** perspectiva de Procesos aplicada al problema de la clase. Lectura selectiva sobre **lean y eliminación de desperdicio**. **Localizador:** [ISBN-13 9780787900908](https://openlibrary.org/isbn/9780787900908).
- James P. Womack, Daniel T. Jones & Daniel Roos — *The Machine That Changed the World* (Free Press, 2007). **Uso en esta clase:** perspectiva de Lean aplicada al problema de la clase. Lectura selectiva sobre **lean y eliminación de desperdicio**. **Localizador:** [ISBN-13 9780743299794](https://openlibrary.org/isbn/9780743299794).
- ISO — *ISO 22301 Business continuity management systems*. **Uso en esta clase:** sistema de gestión de continuidad y preparación ante disrupciones. **Localizador pendiente:** ver [el registro de fuentes](../../../../docs/FUENTES.md).
- James P. Womack & Daniel T. Jones — *Lean Thinking* (Free Press, 2003). **Uso en esta clase:** valor, flujo, pull, desperdicio y mejora continua. Lectura selectiva sobre **lean y eliminación de desperdicio**. **Localizador:** [ISBN-13 9780743231640](https://openlibrary.org/isbn/9780743231640).
- Susan A. Ambrose et al. — *How Learning Works* (John Wiley & Sons, Incorporated, 2010). **Uso en esta clase:** diseñar los objetivos, la práctica y el feedback de **lean y eliminación de desperdicio** sobre conocimiento previo verificable. **Localizador:** [ISBN-13 9780470617601](https://openlibrary.org/isbn/9780470617601).
- Peter C. Brown, Henry L. Roediger III & Mark A. McDaniel — *Make It Stick* (Harvard University Press, 2014). **Uso en esta clase:** justificar la recuperación inicial y las preguntas de comprobación de **lean y eliminación de desperdicio**. **Localizador:** [ISBN-13 9780674986572](https://openlibrary.org/isbn/9780674986572).
- Grant Wiggins & Jay McTighe — *Understanding by Design* (Pearson Education, Inc., 2006). **Uso en esta clase:** derivar el entregable de **lean y eliminación de desperdicio** desde el desempeño observable y no desde el temario. **Localizador:** [ISBN-13 9780131950849](https://openlibrary.org/isbn/9780131950849).
- Anders Ericsson & Robert Pool — *Peak* (Penguin Random House, 2016). **Uso en esta clase:** convertir la práctica de **lean y eliminación de desperdicio** en práctica deliberada con criterios explícitos. **Localizador:** [ISBN-13 9781473513143](https://openlibrary.org/isbn/9781473513143).
- William Ellet — *The Case Study Handbook* (Harvard Business Review Press, 2018). **Uso en esta clase:** estructurar el caso ejecutivo de **lean y eliminación de desperdicio** como problema, evidencia, alternativas y recomendación. **Localizador:** [ISBN-13 9781633696150](https://openlibrary.org/isbn/9781633696150).

> **Regla de fuentes para Lean y eliminación de desperdicio:** las obras anteriores estructuran las perspectivas de esta materia; cualquier norma, ley, impuesto o estándar vivo mencionado en **lean y eliminación de desperdicio** debe comprobarse nuevamente en su fuente primaria vigente. El desarrollo es original y no reproduce capítulos protegidos.
