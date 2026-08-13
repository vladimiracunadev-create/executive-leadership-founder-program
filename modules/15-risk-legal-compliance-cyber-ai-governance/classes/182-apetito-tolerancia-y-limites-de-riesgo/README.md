# Clase 182 — Apetito, tolerancia y límites de riesgo

**Parte:** 15 — Riesgo, legal, compliance, ciberseguridad e IA  
**Nivel:** Etapa 4 — Gerente → Director  
**Duración sugerida:** 150–180 minutos · **Estándar:** deep-class-v2

## 🎯 Propósito

Apetito de riesgo expresa cuánto y qué tipo de riesgo una organización está dispuesta a aceptar para perseguir objetivos; tolerancias y límites lo traducen a operación. Sin esa jerarquía, cada área interpreta prudencia de forma distinta y escala demasiado o demasiado poco.

La salida de esta parte es **gobernar riesgo, legal, cumplimiento, ciberseguridad, datos e IA de forma integrada**. En esta clase, esa progresión se concreta al exigir que cada afirmación sobre **apetito, tolerancia y límites de riesgo** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

## 📚 Resultados de aprendizaje

Al finalizar podrás:

1. **Distinguir** `risk appetite`, `risk tolerance`, `limit`, `breach`, `capacity` mediante observables, no por memoria verbal.
2. **Explicar** por qué esas distinciones cambian una decisión de gerente → director.
3. **Aplicar** la secuencia **1. derivar apetito desde estrategia y capacidad → 2. traducirlo a tolerancias → 3. establecer límites y owners → 4. definir breach y escalamiento → 5. revisar apetito ante cambios de estrategia** conservando supuestos, alternativas y trazabilidad.
4. **Interpretar** limit utilization, breaches, loss absorption capacity sin confundir señal, explicación y causalidad.
5. **Resolver** el caso ejecutivo con al menos dos opciones plausibles y un criterio explícito de stop/revisión.
6. **Contrastar** dos obras de referencia y explicar dónde sus lentes son complementarias o entran en tensión.

## 🧭 Agenda

| Tramo | Evidencia de aprendizaje |
|---|---|
| 0–20 min | Recuperación: define risk appetite y risk tolerance sin mirar la tabla; corrige con la fuente. |
| 20–70 min | Lectura guiada de conceptos + contraste de dos referencias. |
| 70–115 min | Ejemplo trabajado con limit utilization y trazabilidad de supuestos. |
| 115–155 min | Caso ejecutivo: dos alternativas, trade-offs y decisión provisional. |
| 155–180 min | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar comprensión |
|---|---|---|
| **risk appetite** | nivel y tipo de riesgo aceptable en busca de objetivos | Distingue un hecho compatible y otro que lo refute. |
| **risk tolerance** | rango de variación aceptable alrededor de objetivos | Distingue un hecho compatible y otro que lo refute. |
| **limit** | umbral cuantitativo u operativo que restringe exposición | Distingue un hecho compatible y otro que lo refute. |
| **breach** | superación de un límite que activa respuesta | Distingue un hecho compatible y otro que lo refute. |
| **capacity** | máxima pérdida o exposición que la organización puede soportar | Distingue un hecho compatible y otro que lo refute. |

## 🧠 Modelo mental

```text
1. derivar apetito desde estrategia y capacidad → 2. traducirlo a tolerancias → 3. establecer límites y owners → 4. definir breach y escalamiento → 5. revisar apetito ante cambios de estrategia
```

La secuencia nace del problema de esta clase: **Apetito de riesgo expresa cuánto y qué tipo de riesgo una organización está dispuesta a aceptar para perseguir objetivos; tolerancias y límites lo traducen a operación. Sin esa jerarquía, cada área interpreta prudencia de forma distinta y escala demasiado o demasiado poco.** El método es útil mientras las condiciones permitan observar las señales requeridas. No elimina incertidumbre; la hace visible y obliga a decidir proporcionalmente a la evidencia. Límite principal: **Apetito no elimina incertidumbre y no debe disfrazar restricciones legales como preferencias. Riesgos prohibidos por ley o ética no son negociables por apetito.**

## 📖 Desarrollo

### 1. risk appetite: mecanismo central

**risk appetite** se entiende aquí como **nivel y tipo de riesgo aceptable en busca de objetivos**. Esta es la pieza causal o estructural desde la que se inicia **apetito, tolerancia y límites de riesgo**: antes de derivar apetito desde estrategia y capacidad, el gerente debe poder señalar qué cambia en el sistema si el concepto está presente y qué debería observar si no lo está. Una definición que no produce predicciones observables todavía es demasiado vaga para dirigir.

La lectura rectora de este bloque es COSO — *Enterprise Risk Management—Integrating with Strategy and Performance*. Su aporte se usa para examinar **riesgo integrado con estrategia, desempeño, revisión e información**. Aplica esa lente al caso sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **limit utilization**; regístrala con periodo, unidad, población y baseline.

Relaciona el mecanismo con **risk tolerance**. Si ambos cambian juntos, no concluyas causalidad automáticamente: identifica una tercera variable o mecanismo alternativo que también pueda explicar el patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. risk tolerance: frontera conceptual y error de clasificación

**Definición operacional:** rango de variación aceptable alrededor de objetivos. Su valor está en distinguirlo de **risk appetite** y **limit**. En una decisión real, clasificar una situación en la categoría equivocada cambia la intervención: puedes asignar autoridad donde faltaba información, medir un output cuando debías observar un proceso o tratar una restricción como si fuera una preferencia.

Contrasta el problema con John C. Hull — *Risk Management and Financial Institutions*, que aporta una mirada sobre **identificación y medición de riesgos financieros y no financieros**. Formula dos mini-casos: uno que sí satisface la definición de **risk tolerance** y otro que solo se parece superficialmente. Luego pregunta qué señal distinguiría ambos; para esta clase, **breaches** es una candidata, pero debe combinarse con evidencia cualitativa o documental cuando el fenómeno no sea directamente medible.

Antes de traducirlo a tolerancias, registra explícitamente qué decisión sería errónea si esta frontera conceptual se ignora. Esa frase convierte el vocabulario en criterio gerencial.

### 3. limit: operacionalización y medición

**limit** significa **umbral cuantitativo u operativo que restringe exposición**. El problema ya no es definirlo, sino **operacionalizarlo**: qué contar, durante qué ventana, con qué denominador, contra qué baseline y con qué segmentación. Una métrica útil conserva suficiente contexto para no confundir mejora local con mejora del sistema.

NIST — *AI Risk Management Framework (AI RMF 1.0)* orienta este bloque mediante **gobierno y gestión de riesgos de IA confiable a lo largo del ciclo de vida**. Usa esa perspectiva para diseñar una ficha de medición: `señal → fórmula/criterio → fuente → frecuencia → owner → interpretación permitida → interpretación prohibida`. La señal asignada es **loss absorption capacity**. Si no existe un dato confiable, la salida correcta no es inventar precisión: diseña el mecanismo de captura y declara la incertidumbre.

Al llegar a establecer límites y owners, compara tendencia, distribución y casos atípicos. Pregunta además si el indicador es *leading* o *lagging* y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; nunca convertirse en el objetivo que reemplaza al fenómeno.

### 4. breach: trade-offs y efectos de segundo orden

**Definición:** superación de un límite que activa respuesta. Este concepto obliga a abandonar la idea de que **apetito, tolerancia y límites de riesgo** tiene una solución gratuita. Toda intervención consume autonomía, tiempo, caja, capacidad, atención, reputación o tolerancia al riesgo. Por eso, antes de definir breach y escalamiento, se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Ross Anderson — *Security Engineering* aporta una lente sobre **perspectiva de Ciberseguridad aplicada al problema de la clase**. Úsala para construir una matriz `beneficio / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **override count** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la necesidad de observar efectos laterales fuera del KPI principal.

Haz un *pre-mortem* de **apetito, tolerancia y límites de riesgo**: supone que la opción recomendada fracasó seis meses después y enumera tres mecanismos que podrían explicarlo. Al menos uno debe provenir de un efecto de segundo orden asociado a **breach** y otro de una hipótesis del caso que nunca fue validada.

### 5. capacity: gobernanza, límites e integración

**capacity** se define como **máxima pérdida o exposición que la organización puede soportar** y cierra el circuito porque traduce análisis en responsabilidad. La pregunta ejecutiva es quién decide, quién ejecuta, quién debe ser consultado, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar.

OECD — *G20/OECD Principles of Corporate Governance 2023* se utiliza para estudiar **derechos de accionistas, directorio, disclosure, sostenibilidad y buen gobierno** y contrastar la recomendación final. Al ejecutar revisar apetito ante cambios de estrategia, deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento. Esa trazabilidad protege contra el sesgo retrospectivo y mejora las revisiones posteriores.

La frontera de esta clase es explícita: **Apetito no elimina incertidumbre y no debe disfrazar restricciones legales como preferencias. Riesgos prohibidos por ley o ética no son negociables por apetito.**. Conviértela en una regla operativa: `si ocurre X → no aplicar automáticamente → consultar/escalar/revalidar`. Integrar **risk appetite**, **risk tolerance**, **limit**, **breach** y **capacity** significa poder explicar qué parte del diagnóstico sostiene la decisión y cuál sigue siendo una apuesta.

### 6. Integración: de conceptos a una decisión defendible

La síntesis de **apetito, tolerancia y límites de riesgo** no consiste en sumar cinco definiciones. Empieza por **risk appetite**, contrasta **risk tolerance** con **limit**, incorpora **breach** como restricción o mecanismo y usa **capacity** para cerrar el ciclo. Si el análisis no puede explicar cuál de esas piezas cambió la recomendación, todavía no hay comprensión transferible.

Aplica ahora la secuencia **1. derivar apetito desde estrategia y capacidad → 2. traducirlo a tolerancias → 3. establecer límites y owners → 4. definir breach y escalamiento → 5. revisar apetito ante cambios de estrategia**. Para cada paso conserva tres columnas: evidencia utilizada, alternativa descartada y razón. Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado y evita reescribir la historia después de conocer el desenlace.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla señala el lente que debes buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| COSO — *Enterprise Risk Management—Integrating with Strategy and Performance* | riesgo integrado con estrategia, desempeño, revisión e información | ¿Qué supuesto de **apetito, tolerancia y límites de riesgo** ayuda a desafiar? |
| John C. Hull — *Risk Management and Financial Institutions* | identificación y medición de riesgos financieros y no financieros | ¿Qué supuesto de **apetito, tolerancia y límites de riesgo** ayuda a desafiar? |
| NIST — *AI Risk Management Framework (AI RMF 1.0)* | gobierno y gestión de riesgos de IA confiable a lo largo del ciclo de vida | ¿Qué supuesto de **apetito, tolerancia y límites de riesgo** ayuda a desafiar? |
| Ross Anderson — *Security Engineering* | perspectiva de Ciberseguridad aplicada al problema de la clase | ¿Qué supuesto de **apetito, tolerancia y límites de riesgo** ayuda a desafiar? |
| OECD — *G20/OECD Principles of Corporate Governance 2023* | derechos de accionistas, directorio, disclosure, sostenibilidad y buen gobierno | ¿Qué supuesto de **apetito, tolerancia y límites de riesgo** ayuda a desafiar? |

En **apetito, tolerancia y límites de riesgo**, la lectura se evalúa por **uso**, no por cantidad de páginas. La nota debe indicar qué tesis de las fuentes modifica tu lectura de **risk appetite**, qué evidencia del caso tensiona esa tesis y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación:** Un marketplace dice tener bajo apetito de fraude pero incentiva crecimiento sin límite y no define pérdidas máximas ni cuándo bloquear cuentas de alto GMV.

**Paso 1 — derivar apetito desde estrategia y capacidad.** La gerencia escribe primero el supuesto asociado a **risk appetite** y evita convertirlo en hecho. Luego busca **limit utilization** para contrastarlo en el caso de **apetito, tolerancia y límites de riesgo**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 2 — traducirlo a tolerancias.** La gerencia escribe primero el supuesto asociado a **risk tolerance** y evita convertirlo en hecho. Luego busca **breaches** para contrastarlo en el caso de **apetito, tolerancia y límites de riesgo**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 3 — establecer límites y owners.** La gerencia escribe primero el supuesto asociado a **limit** y evita convertirlo en hecho. Luego busca **loss absorption capacity** para contrastarlo en el caso de **apetito, tolerancia y límites de riesgo**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 4 — definir breach y escalamiento.** La gerencia escribe primero el supuesto asociado a **breach** y evita convertirlo en hecho. Luego busca **override count** para contrastarlo en el caso de **apetito, tolerancia y límites de riesgo**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 5 — revisar apetito ante cambios de estrategia.** La gerencia escribe primero el supuesto asociado a **capacity** y evita convertirlo en hecho. Luego busca **escalation time** para contrastarlo en el caso de **apetito, tolerancia y límites de riesgo**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Síntesis del caso.** La recomendación debe terminar con responsable, fecha, evidencia de éxito y señal de stop. En **apetito, tolerancia y límites de riesgo**, omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo |
|---|---|---|---|
| **risk appetite** | nivel y tipo de riesgo aceptable en busca de objetivos | Cuando limit utilization es observable y accionable. | Sobrerreaccionar a una señal parcial. |
| **risk tolerance** | rango de variación aceptable alrededor de objetivos | Cuando la primera explicación no distingue mecanismo o responsabilidad. | Convertir el concepto en etiqueta. |
| **Experimento/revisión** | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar eternamente y no decidir. |
| **Escalamiento** | Elevar autoridad o especialidad | Cuando hay derechos, capital material, regulación o irreversibilidad. | Delegar hacia arriba lo que sí corresponde decidir. |

**Frontera de aplicación:** Apetito no elimina incertidumbre y no debe disfrazar restricciones legales como preferencias. Riesgos prohibidos por ley o ética no son negociables por apetito.

## 🪜 De profesional a owner

| Nivel | Responsabilidad sobre apetito, tolerancia y límites de riesgo |
|---|---|
| **Profesional** | usa **apetito, tolerancia y límites de riesgo** para mejorar una contribución propia y explicar sus supuestos con evidencia. |
| **Jefe / Team Lead** | aplica **risk appetite** y **risk tolerance** para coordinar personas sin sustituir conversación por métricas. |
| **Manager / Gerente** | conecta limit utilization con capacidad, presupuesto, dependencias y riesgo interáreas. |
| **CEO / Director** | decide si apetito, tolerancia y límites de riesgo cambia estrategia, economía o riesgo de empresa y qué debe llegar al comité o directorio. |
| **Founder / Owner** | pregunta si la solución de apetito, tolerancia y límites de riesgo reduce dependencia del fundador, preserva caja y puede operar como sistema repetible. |

El cambio de nivel en **apetito, tolerancia y límites de riesgo** aumenta el número de personas, dinero, dependencias y consecuencias que quedan dentro de la decisión. Por eso la misma herramienta debe volverse más explícita en evidencia, gobernanza y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Un marketplace dice tener bajo apetito de fraude pero incentiva crecimiento sin límite y no define pérdidas máximas ni cuándo bloquear cuentas de alto GMV.

Entrega un **decision brief de apetito, tolerancia y límites de riesgo** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre personas, cliente, operación, caja y riesgo; (e) recomendación; (f) condición que haría cambiarla; (g) dueño y fecha de revisión. Utiliza al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica

1. Reconstruye el caso de **apetito, tolerancia y límites de riesgo** con una tabla `hecho / interpretación / hipótesis / decisión`.
2. Ejecuta **1. derivar apetito desde estrategia y capacidad → 2. traducirlo a tolerancias → 3. establecer límites y owners → 4. definir breach y escalamiento → 5. revisar apetito ante cambios de estrategia** y adjunta evidencia para cada transición entre pasos.
3. Calcula o documenta limit utilization, breaches; si no existe dato, diseña cómo obtenerlo.
4. Escribe una alternativa que contradiga tu preferencia inicial y haz un *pre-mortem* específico del caso.
5. Lee dos referencias, registra una coincidencia y una tensión, y modifica el brief si corresponde.
6. Repite la decisión desde el rol de CEO/owner: identifica qué cambia al aumentar el alcance y la irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar risk appetite y risk tolerance como sinónimos | Se pierde la distinción entre “nivel y tipo de riesgo aceptable en busca de objetivos” y “rango de variación aceptable alrededor de objetivos” | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por “revisar apetito ante cambios de estrategia” | Se saltó “derivar apetito desde estrategia y capacidad” y la solución llegó antes que el diagnóstico | Reconstruye la cadena 1. derivar apetito desde estrategia y capacidad → 2. traducirlo a tolerancias → 3. establecer límites y owners → 4. definir breach y escalamiento → 5. revisar apetito ante cambios de estrategia y marca el primer supuesto no demostrado. |
| Optimizar solo limit utilization | La métrica local sustituyó al resultado del sistema | Contrástala con breaches y explicita el costo de oportunidad. |
| Generalizar desde un caso favorable | Se confundió evidencia local con una regla universal sobre apetito, tolerancia y límites de riesgo | Apetito no elimina incertidumbre y no debe disfrazar restricciones legales como preferencias. Riesgos prohibidos por ley o ética no son negociables por apetito. |
| No fijar revisión | Una decisión sobre apetito, tolerancia y límites de riesgo se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de stop. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **risk appetite** y **risk tolerance** usando un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **limit** y qué observación obligaría a rechazar tu interpretación?
3. Aplica **derivar apetito desde estrategia y capacidad → traducirlo a tolerancias** al caso de la clase. ¿Qué dato todavía falta?
4. ¿Por qué **limit utilization** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la tabla de lectura. ¿Dónde podrían llevar a recomendaciones distintas para **apetito, tolerancia y límites de riesgo**?
6. ¿Qué decisión equivocada podría producirse si se ignora este límite: **Apetito no elimina incertidumbre y no debe disfrazar restricciones legales como preferencias. Riesgos prohibidos por ley o ética no son negociables por apetito.**?

## 📥 Entregable

Guarda en `portfolio/182-apetito-tolerancia-y-limites-de-riesgo/`:

- `risk-governance-brief.md` con el problema específico de **apetito, tolerancia y límites de riesgo**, evidencia, alternativas, decisión y gobernanza;
- `reading-note.md` contrastando las fuentes de **apetito, tolerancia y límites de riesgo** con edición/páginas consultadas;
- `decision-journal.md` registrando los supuestos de **risk appetite**, confianza, responsable y revisión;
- `red-team.md` con la objeción más fuerte al caso **Un marketplace dice tener bajo apetito de fraude pero incentiva crecimiento sin límite y no define pérdidas máximas ni cuándo bloquear cuentas de alto GMV.** y el dato que podría invalidar la recomendación.

## 📗 Fuentes y verificación

- COSO — *Enterprise Risk Management—Integrating with Strategy and Performance*. **Uso en esta clase:** riesgo integrado con estrategia, desempeño, revisión e información. Lectura selectiva: índice/capítulos pertinentes a **apetito, tolerancia y límites de riesgo**; registra edición y páginas consultadas.
- John C. Hull — *Risk Management and Financial Institutions*. **Uso en esta clase:** identificación y medición de riesgos financieros y no financieros. Lectura selectiva: índice/capítulos pertinentes a **apetito, tolerancia y límites de riesgo**; registra edición y páginas consultadas.
- NIST — *AI Risk Management Framework (AI RMF 1.0)*. **Uso en esta clase:** gobierno y gestión de riesgos de IA confiable a lo largo del ciclo de vida. Lectura selectiva: índice/capítulos pertinentes a **apetito, tolerancia y límites de riesgo**; registra edición y páginas consultadas.
- Ross Anderson — *Security Engineering*. **Uso en esta clase:** perspectiva de Ciberseguridad aplicada al problema de la clase. Lectura selectiva: índice/capítulos pertinentes a **apetito, tolerancia y límites de riesgo**; registra edición y páginas consultadas.
- OECD — *G20/OECD Principles of Corporate Governance 2023*. **Uso en esta clase:** derechos de accionistas, directorio, disclosure, sostenibilidad y buen gobierno. Lectura selectiva: índice/capítulos pertinentes a **apetito, tolerancia y límites de riesgo**; registra edición y páginas consultadas.
- NIST — *Cybersecurity Framework (CSF) 2.0*. **Uso en esta clase:** gobierno, identificación, protección, detección, respuesta y recuperación en ciberseguridad. Lectura selectiva: índice/capítulos pertinentes a **apetito, tolerancia y límites de riesgo**; registra edición y páginas consultadas.
- NIST — *AI Risk Management Framework*. Fuente primaria: <https://www.nist.gov/itl/ai-risk-management-framework>.
- COSO — *Enterprise Risk Management* / *Internal Control*. Fuente institucional: <https://www.coso.org/>.
- Susan A. Ambrose et al. — *How Learning Works*. Diseño de objetivos, práctica y feedback.
- Peter C. Brown, Henry L. Roediger III & Mark A. McDaniel — *Make It Stick*. Recuperación, elaboración y transferencia.
- Grant Wiggins & Jay McTighe — *Understanding by Design*. Diseño inverso desde desempeño observable.
- Anders Ericsson & Robert Pool — *Peak*. Práctica deliberada con criterios y retroalimentación.
- William Ellet — *The Case Study Handbook*. Análisis de problema/decisión, evidencia y recomendación.

> **Regla de fuentes para Apetito, tolerancia y límites de riesgo:** las obras anteriores estructuran las perspectivas de esta materia; cualquier norma, ley, impuesto o estándar vivo mencionado en **apetito, tolerancia y límites de riesgo** debe comprobarse nuevamente en su fuente primaria vigente. El desarrollo es original y no reproduce capítulos protegidos.
