# Clase 183 — Controles internos y segregación

**Parte:** 15 — Riesgo, legal, compliance, ciberseguridad e IA  
**Nivel:** Etapa 4 — Gerente → Director  
**Duración sugerida:** 150–180 minutos · **Estándar:** deep-class-v2

## 🎯 Propósito

Control interno reduce riesgos a un nivel aceptable mediante ambiente de control, evaluación, actividades, información y monitoreo. Segregación de funciones evita que una persona pueda iniciar, aprobar, ejecutar y ocultar una transacción material sin detección.

La salida de esta parte es **gobernar riesgo, legal, cumplimiento, ciberseguridad, datos e IA de forma integrada**. En esta clase, esa progresión se concreta al exigir que cada afirmación sobre **controles internos y segregación** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

## 📚 Resultados de aprendizaje

Al finalizar podrás:

1. **Distinguir** `internal control`, `segregation of duties`, `preventive control`, `detective control`, `control owner` mediante observables, no por memoria verbal.
2. **Explicar** por qué esas distinciones cambian una decisión de gerente → director.
3. **Aplicar** la secuencia **1. mapear riesgo y objetivo → 2. identificar puntos de fraude o error → 3. diseñar control preventivo y detective → 4. separar funciones incompatibles → 5. testear evidencia y remediar fallas** conservando supuestos, alternativas y trazabilidad.
4. **Interpretar** control exceptions, SoD conflicts, test failure rate sin confundir señal, explicación y causalidad.
5. **Resolver** el caso ejecutivo con al menos dos opciones plausibles y un criterio explícito de stop/revisión.
6. **Contrastar** dos obras de referencia y explicar dónde sus lentes son complementarias o entran en tensión.

## 🧭 Agenda

| Tramo | Evidencia de aprendizaje |
|---|---|
| 0–20 min | Recuperación: define internal control y segregation of duties sin mirar la tabla; corrige con la fuente. |
| 20–70 min | Lectura guiada de conceptos + contraste de dos referencias. |
| 70–115 min | Ejemplo trabajado con control exceptions y trazabilidad de supuestos. |
| 115–155 min | Caso ejecutivo: dos alternativas, trade-offs y decisión provisional. |
| 155–180 min | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar comprensión |
|---|---|---|
| **internal control** | proceso diseñado para dar seguridad razonable sobre objetivos | Distingue un hecho compatible y otro que lo refute. |
| **segregation of duties** | separación de funciones incompatibles para reducir fraude o error | Distingue un hecho compatible y otro que lo refute. |
| **preventive control** | control que evita ocurrencia | Distingue un hecho compatible y otro que lo refute. |
| **detective control** | control que identifica después de ocurrir | Distingue un hecho compatible y otro que lo refute. |
| **control owner** | rol responsable de diseño y operación del control | Distingue un hecho compatible y otro que lo refute. |

## 🧠 Modelo mental

```text
1. mapear riesgo y objetivo → 2. identificar puntos de fraude o error → 3. diseñar control preventivo y detective → 4. separar funciones incompatibles → 5. testear evidencia y remediar fallas
```

La secuencia nace del problema de esta clase: **Control interno reduce riesgos a un nivel aceptable mediante ambiente de control, evaluación, actividades, información y monitoreo. Segregación de funciones evita que una persona pueda iniciar, aprobar, ejecutar y ocultar una transacción material sin detección.** El método es útil mientras las condiciones permitan observar las señales requeridas. No elimina incertidumbre; la hace visible y obliga a decidir proporcionalmente a la evidencia. Límite principal: **Separar toda función puede ser inviable en equipos pequeños. Usa controles compensatorios —revisión independiente, límites, alertas, reconciliación— proporcionales al riesgo.**

## 📖 Desarrollo

### 1. internal control: mecanismo central

**internal control** se entiende aquí como **proceso diseñado para dar seguridad razonable sobre objetivos**. Esta es la pieza causal o estructural desde la que se inicia **controles internos y segregación**: antes de mapear riesgo y objetivo, el gerente debe poder señalar qué cambia en el sistema si el concepto está presente y qué debería observar si no lo está. Una definición que no produce predicciones observables todavía es demasiado vaga para dirigir.

La lectura rectora de este bloque es COSO — *Enterprise Risk Management—Integrating with Strategy and Performance*. Su aporte se usa para examinar **riesgo integrado con estrategia, desempeño, revisión e información**. Aplica esa lente al caso sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **control exceptions**; regístrala con periodo, unidad, población y baseline.

Relaciona el mecanismo con **segregation of duties**. Si ambos cambian juntos, no concluyas causalidad automáticamente: identifica una tercera variable o mecanismo alternativo que también pueda explicar el patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. segregation of duties: frontera conceptual y error de clasificación

**Definición operacional:** separación de funciones incompatibles para reducir fraude o error. Su valor está en distinguirlo de **internal control** y **preventive control**. En una decisión real, clasificar una situación en la categoría equivocada cambia la intervención: puedes asignar autoridad donde faltaba información, medir un output cuando debías observar un proceso o tratar una restricción como si fuera una preferencia.

Contrasta el problema con John C. Hull — *Risk Management and Financial Institutions*, que aporta una mirada sobre **identificación y medición de riesgos financieros y no financieros**. Formula dos mini-casos: uno que sí satisface la definición de **segregation of duties** y otro que solo se parece superficialmente. Luego pregunta qué señal distinguiría ambos; para esta clase, **SoD conflicts** es una candidata, pero debe combinarse con evidencia cualitativa o documental cuando el fenómeno no sea directamente medible.

Antes de identificar puntos de fraude o error, registra explícitamente qué decisión sería errónea si esta frontera conceptual se ignora. Esa frase convierte el vocabulario en criterio gerencial.

### 3. preventive control: operacionalización y medición

**preventive control** significa **control que evita ocurrencia**. El problema ya no es definirlo, sino **operacionalizarlo**: qué contar, durante qué ventana, con qué denominador, contra qué baseline y con qué segmentación. Una métrica útil conserva suficiente contexto para no confundir mejora local con mejora del sistema.

OECD — *OECD AI Principles* orienta este bloque mediante **principios para IA confiable, responsable y centrada en las personas**. Usa esa perspectiva para diseñar una ficha de medición: `señal → fórmula/criterio → fuente → frecuencia → owner → interpretación permitida → interpretación prohibida`. La señal asignada es **test failure rate**. Si no existe un dato confiable, la salida correcta no es inventar precisión: diseña el mecanismo de captura y declara la incertidumbre.

Al llegar a diseñar control preventivo y detective, compara tendencia, distribución y casos atípicos. Pregunta además si el indicador es *leading* o *lagging* y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; nunca convertirse en el objetivo que reemplaza al fenómeno.

### 4. detective control: trade-offs y efectos de segundo orden

**Definición:** control que identifica después de ocurrir. Este concepto obliga a abandonar la idea de que **controles internos y segregación** tiene una solución gratuita. Toda intervención consume autonomía, tiempo, caja, capacidad, atención, reputación o tolerancia al riesgo. Por eso, antes de separar funciones incompatibles, se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Richard A. Clarke & Robert K. Knake — *The Fifth Domain* aporta una lente sobre **perspectiva de Ciberseguridad aplicada al problema de la clase**. Úsala para construir una matriz `beneficio / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **override count** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la necesidad de observar efectos laterales fuera del KPI principal.

Haz un *pre-mortem* de **controles internos y segregación**: supone que la opción recomendada fracasó seis meses después y enumera tres mecanismos que podrían explicarlo. Al menos uno debe provenir de un efecto de segundo orden asociado a **detective control** y otro de una hipótesis del caso que nunca fue validada.

### 5. control owner: gobernanza, límites e integración

**control owner** se define como **rol responsable de diseño y operación del control** y cierra el circuito porque traduce análisis en responsabilidad. La pregunta ejecutiva es quién decide, quién ejecuta, quién debe ser consultado, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar.

Bob Tricker — *Corporate Governance* se utiliza para estudiar **separación entre dirección, supervisión, accountability y gobierno corporativo** y contrastar la recomendación final. Al ejecutar testear evidencia y remediar fallas, deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento. Esa trazabilidad protege contra el sesgo retrospectivo y mejora las revisiones posteriores.

La frontera de esta clase es explícita: **Separar toda función puede ser inviable en equipos pequeños. Usa controles compensatorios —revisión independiente, límites, alertas, reconciliación— proporcionales al riesgo.**. Conviértela en una regla operativa: `si ocurre X → no aplicar automáticamente → consultar/escalar/revalidar`. Integrar **internal control**, **segregation of duties**, **preventive control**, **detective control** y **control owner** significa poder explicar qué parte del diagnóstico sostiene la decisión y cuál sigue siendo una apuesta.

### 6. Integración: de conceptos a una decisión defendible

La síntesis de **controles internos y segregación** no consiste en sumar cinco definiciones. Empieza por **internal control**, contrasta **segregation of duties** con **preventive control**, incorpora **detective control** como restricción o mecanismo y usa **control owner** para cerrar el ciclo. Si el análisis no puede explicar cuál de esas piezas cambió la recomendación, todavía no hay comprensión transferible.

Aplica ahora la secuencia **1. mapear riesgo y objetivo → 2. identificar puntos de fraude o error → 3. diseñar control preventivo y detective → 4. separar funciones incompatibles → 5. testear evidencia y remediar fallas**. Para cada paso conserva tres columnas: evidencia utilizada, alternativa descartada y razón. Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado y evita reescribir la historia después de conocer el desenlace.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla señala el lente que debes buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| COSO — *Enterprise Risk Management—Integrating with Strategy and Performance* | riesgo integrado con estrategia, desempeño, revisión e información | ¿Qué supuesto de **controles internos y segregación** ayuda a desafiar? |
| John C. Hull — *Risk Management and Financial Institutions* | identificación y medición de riesgos financieros y no financieros | ¿Qué supuesto de **controles internos y segregación** ayuda a desafiar? |
| OECD — *OECD AI Principles* | principios para IA confiable, responsable y centrada en las personas | ¿Qué supuesto de **controles internos y segregación** ayuda a desafiar? |
| Richard A. Clarke & Robert K. Knake — *The Fifth Domain* | perspectiva de Ciberseguridad aplicada al problema de la clase | ¿Qué supuesto de **controles internos y segregación** ayuda a desafiar? |
| Bob Tricker — *Corporate Governance* | separación entre dirección, supervisión, accountability y gobierno corporativo | ¿Qué supuesto de **controles internos y segregación** ayuda a desafiar? |

En **controles internos y segregación**, la lectura se evalúa por **uso**, no por cantidad de páginas. La nota debe indicar qué tesis de las fuentes modifica tu lectura de **internal control**, qué evidencia del caso tensiona esa tesis y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación:** Una pyme permite que la misma persona cree proveedores, cargue facturas y apruebe pagos porque confían en ella. Un proveedor ficticio pasa inadvertido seis meses.

**Paso 1 — mapear riesgo y objetivo.** La gerencia escribe primero el supuesto asociado a **internal control** y evita convertirlo en hecho. Luego busca **control exceptions** para contrastarlo en el caso de **controles internos y segregación**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 2 — identificar puntos de fraude o error.** La gerencia escribe primero el supuesto asociado a **segregation of duties** y evita convertirlo en hecho. Luego busca **SoD conflicts** para contrastarlo en el caso de **controles internos y segregación**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 3 — diseñar control preventivo y detective.** La gerencia escribe primero el supuesto asociado a **preventive control** y evita convertirlo en hecho. Luego busca **test failure rate** para contrastarlo en el caso de **controles internos y segregación**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 4 — separar funciones incompatibles.** La gerencia escribe primero el supuesto asociado a **detective control** y evita convertirlo en hecho. Luego busca **override count** para contrastarlo en el caso de **controles internos y segregación**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 5 — testear evidencia y remediar fallas.** La gerencia escribe primero el supuesto asociado a **control owner** y evita convertirlo en hecho. Luego busca **reconciliation breaks** para contrastarlo en el caso de **controles internos y segregación**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Síntesis del caso.** La recomendación debe terminar con responsable, fecha, evidencia de éxito y señal de stop. En **controles internos y segregación**, omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo |
|---|---|---|---|
| **internal control** | proceso diseñado para dar seguridad razonable sobre objetivos | Cuando control exceptions es observable y accionable. | Sobrerreaccionar a una señal parcial. |
| **segregation of duties** | separación de funciones incompatibles para reducir fraude o error | Cuando la primera explicación no distingue mecanismo o responsabilidad. | Convertir el concepto en etiqueta. |
| **Experimento/revisión** | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar eternamente y no decidir. |
| **Escalamiento** | Elevar autoridad o especialidad | Cuando hay derechos, capital material, regulación o irreversibilidad. | Delegar hacia arriba lo que sí corresponde decidir. |

**Frontera de aplicación:** Separar toda función puede ser inviable en equipos pequeños. Usa controles compensatorios —revisión independiente, límites, alertas, reconciliación— proporcionales al riesgo.

## 🪜 De profesional a owner

| Nivel | Responsabilidad sobre controles internos y segregación |
|---|---|
| **Profesional** | usa **controles internos y segregación** para mejorar una contribución propia y explicar sus supuestos con evidencia. |
| **Jefe / Team Lead** | aplica **internal control** y **segregation of duties** para coordinar personas sin sustituir conversación por métricas. |
| **Manager / Gerente** | conecta control exceptions con capacidad, presupuesto, dependencias y riesgo interáreas. |
| **CEO / Director** | decide si controles internos y segregación cambia estrategia, economía o riesgo de empresa y qué debe llegar al comité o directorio. |
| **Founder / Owner** | pregunta si la solución de controles internos y segregación reduce dependencia del fundador, preserva caja y puede operar como sistema repetible. |

El cambio de nivel en **controles internos y segregación** aumenta el número de personas, dinero, dependencias y consecuencias que quedan dentro de la decisión. Por eso la misma herramienta debe volverse más explícita en evidencia, gobernanza y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Una pyme permite que la misma persona cree proveedores, cargue facturas y apruebe pagos porque confían en ella. Un proveedor ficticio pasa inadvertido seis meses.

Entrega un **decision brief de controles internos y segregación** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre personas, cliente, operación, caja y riesgo; (e) recomendación; (f) condición que haría cambiarla; (g) dueño y fecha de revisión. Utiliza al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica

1. Reconstruye el caso de **controles internos y segregación** con una tabla `hecho / interpretación / hipótesis / decisión`.
2. Ejecuta **1. mapear riesgo y objetivo → 2. identificar puntos de fraude o error → 3. diseñar control preventivo y detective → 4. separar funciones incompatibles → 5. testear evidencia y remediar fallas** y adjunta evidencia para cada transición entre pasos.
3. Calcula o documenta control exceptions, SoD conflicts; si no existe dato, diseña cómo obtenerlo.
4. Escribe una alternativa que contradiga tu preferencia inicial y haz un *pre-mortem* específico del caso.
5. Lee dos referencias, registra una coincidencia y una tensión, y modifica el brief si corresponde.
6. Repite la decisión desde el rol de CEO/owner: identifica qué cambia al aumentar el alcance y la irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar internal control y segregation of duties como sinónimos | Se pierde la distinción entre “proceso diseñado para dar seguridad razonable sobre objetivos” y “separación de funciones incompatibles para reducir fraude o error” | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por “testear evidencia y remediar fallas” | Se saltó “mapear riesgo y objetivo” y la solución llegó antes que el diagnóstico | Reconstruye la cadena 1. mapear riesgo y objetivo → 2. identificar puntos de fraude o error → 3. diseñar control preventivo y detective → 4. separar funciones incompatibles → 5. testear evidencia y remediar fallas y marca el primer supuesto no demostrado. |
| Optimizar solo control exceptions | La métrica local sustituyó al resultado del sistema | Contrástala con SoD conflicts y explicita el costo de oportunidad. |
| Generalizar desde un caso favorable | Se confundió evidencia local con una regla universal sobre controles internos y segregación | Separar toda función puede ser inviable en equipos pequeños. Usa controles compensatorios —revisión independiente, límites, alertas, reconciliación— proporcionales al riesgo. |
| No fijar revisión | Una decisión sobre controles internos y segregación se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de stop. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **internal control** y **segregation of duties** usando un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **preventive control** y qué observación obligaría a rechazar tu interpretación?
3. Aplica **mapear riesgo y objetivo → identificar puntos de fraude o error** al caso de la clase. ¿Qué dato todavía falta?
4. ¿Por qué **control exceptions** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la tabla de lectura. ¿Dónde podrían llevar a recomendaciones distintas para **controles internos y segregación**?
6. ¿Qué decisión equivocada podría producirse si se ignora este límite: **Separar toda función puede ser inviable en equipos pequeños. Usa controles compensatorios —revisión independiente, límites, alertas, reconciliación— proporcionales al riesgo.**?

## 📥 Entregable

Guarda en `portfolio/183-controles-internos-y-segregacion/`:

- `leadership-decision-brief.md` con el problema específico de **controles internos y segregación**, evidencia, alternativas, decisión y gobernanza;
- `reading-note.md` contrastando las fuentes de **controles internos y segregación** con edición/páginas consultadas;
- `decision-journal.md` registrando los supuestos de **internal control**, confianza, responsable y revisión;
- `red-team.md` con la objeción más fuerte al caso **Una pyme permite que la misma persona cree proveedores, cargue facturas y apruebe pagos porque confían en ella. Un proveedor ficticio pasa inadvertido seis meses.** y el dato que podría invalidar la recomendación.

## 📗 Fuentes y verificación

- COSO — *Enterprise Risk Management—Integrating with Strategy and Performance*. **Uso en esta clase:** riesgo integrado con estrategia, desempeño, revisión e información. Lectura selectiva: índice/capítulos pertinentes a **controles internos y segregación**; registra edición y páginas consultadas.
- John C. Hull — *Risk Management and Financial Institutions*. **Uso en esta clase:** identificación y medición de riesgos financieros y no financieros. Lectura selectiva: índice/capítulos pertinentes a **controles internos y segregación**; registra edición y páginas consultadas.
- OECD — *OECD AI Principles*. **Uso en esta clase:** principios para IA confiable, responsable y centrada en las personas. Lectura selectiva: índice/capítulos pertinentes a **controles internos y segregación**; registra edición y páginas consultadas.
- Richard A. Clarke & Robert K. Knake — *The Fifth Domain*. **Uso en esta clase:** perspectiva de Ciberseguridad aplicada al problema de la clase. Lectura selectiva: índice/capítulos pertinentes a **controles internos y segregación**; registra edición y páginas consultadas.
- Bob Tricker — *Corporate Governance*. **Uso en esta clase:** separación entre dirección, supervisión, accountability y gobierno corporativo. Lectura selectiva: índice/capítulos pertinentes a **controles internos y segregación**; registra edición y páginas consultadas.
- NIST — *Cybersecurity Framework (CSF) 2.0*. **Uso en esta clase:** gobierno, identificación, protección, detección, respuesta y recuperación en ciberseguridad. Lectura selectiva: índice/capítulos pertinentes a **controles internos y segregación**; registra edición y páginas consultadas.
- COSO — *Enterprise Risk Management* / *Internal Control*. Fuente institucional: <https://www.coso.org/>.
- Susan A. Ambrose et al. — *How Learning Works*. Diseño de objetivos, práctica y feedback.
- Peter C. Brown, Henry L. Roediger III & Mark A. McDaniel — *Make It Stick*. Recuperación, elaboración y transferencia.
- Grant Wiggins & Jay McTighe — *Understanding by Design*. Diseño inverso desde desempeño observable.
- Anders Ericsson & Robert Pool — *Peak*. Práctica deliberada con criterios y retroalimentación.
- William Ellet — *The Case Study Handbook*. Análisis de problema/decisión, evidencia y recomendación.

> **Regla de fuentes para Controles internos y segregación:** las obras anteriores estructuran las perspectivas de esta materia; cualquier norma, ley, impuesto o estándar vivo mencionado en **controles internos y segregación** debe comprobarse nuevamente en su fuente primaria vigente. El desarrollo es original y no reproduce capítulos protegidos.
