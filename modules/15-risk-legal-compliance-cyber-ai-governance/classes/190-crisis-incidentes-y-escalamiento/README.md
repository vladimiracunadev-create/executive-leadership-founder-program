# Clase 190 — Crisis, incidentes y escalamiento

**Parte:** 15 — Riesgo, legal, compliance, ciberseguridad e IA  
**Nivel:** Etapa 4 — Gerente → Director  
**Duración sugerida:** 150–180 minutos · **Estándar:** deep-class-v2

## 🎯 Propósito

Gestionar una crisis exige distinguir incidente, crisis y emergencia, activar estructura de comando, proteger personas, estabilizar operación, comunicar hechos confirmados y tomar decisiones reversibles cuando la información es incompleta. La preparación previa reduce improvisación bajo presión.

La salida de esta parte es **gobernar riesgo, legal, cumplimiento, ciberseguridad, datos e IA de forma integrada**. En esta clase, esa progresión se concreta al exigir que cada afirmación sobre **crisis, incidentes y escalamiento** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

## 📚 Resultados de aprendizaje

Al finalizar podrás:

1. **Distinguir** `incident`, `crisis`, `incident commander`, `situation report`, `decision log` mediante observables, no por memoria verbal.
2. **Explicar** por qué esas distinciones cambian una decisión de gerente → director.
3. **Aplicar** la secuencia **1. detectar y clasificar → 2. activar roles y war room → 3. proteger personas y contener impacto → 4. comunicar hechos y decisiones → 5. recuperar investigar y aprender** conservando supuestos, alternativas y trazabilidad.
4. **Interpretar** time-to-escalate, MTTR, stakeholder update latency sin confundir señal, explicación y causalidad.
5. **Resolver** el caso ejecutivo con al menos dos opciones plausibles y un criterio explícito de stop/revisión.
6. **Contrastar** dos obras de referencia y explicar dónde sus lentes son complementarias o entran en tensión.

## 🧭 Agenda

| Tramo | Evidencia de aprendizaje |
|---|---|
| 0–20 min | Recuperación: define incident y crisis sin mirar la tabla; corrige con la fuente. |
| 20–70 min | Lectura guiada de conceptos + contraste de dos referencias. |
| 70–115 min | Ejemplo trabajado con time-to-escalate y trazabilidad de supuestos. |
| 115–155 min | Caso ejecutivo: dos alternativas, trade-offs y decisión provisional. |
| 155–180 min | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar comprensión |
|---|---|---|
| **incident** | evento gestionable dentro de capacidades operativas normales | Distingue un hecho compatible y otro que lo refute. |
| **crisis** | evento que amenaza objetivos críticos y requiere coordinación ejecutiva | Distingue un hecho compatible y otro que lo refute. |
| **incident commander** | rol que coordina respuesta y prioridades | Distingue un hecho compatible y otro que lo refute. |
| **situation report** | resumen periódico de hechos impacto acciones y necesidades | Distingue un hecho compatible y otro que lo refute. |
| **decision log** | registro de decisiones supuestos y responsables durante respuesta | Distingue un hecho compatible y otro que lo refute. |

## 🧠 Modelo mental

```text
1. detectar y clasificar → 2. activar roles y war room → 3. proteger personas y contener impacto → 4. comunicar hechos y decisiones → 5. recuperar investigar y aprender
```

La secuencia nace del problema de esta clase: **Gestionar una crisis exige distinguir incidente, crisis y emergencia, activar estructura de comando, proteger personas, estabilizar operación, comunicar hechos confirmados y tomar decisiones reversibles cuando la información es incompleta. La preparación previa reduce improvisación bajo presión.** El método es útil mientras las condiciones permitan observar las señales requeridas. No elimina incertidumbre; la hace visible y obliga a decidir proporcionalmente a la evidencia. Límite principal: **Centralizar crisis no significa que el CEO decida cada acción. Define incident command y delegación; reserva nivel ejecutivo para trade-offs, stakeholders y decisiones materiales.**

## 📖 Desarrollo

### 1. incident: mecanismo central

**incident** se entiende aquí como **evento gestionable dentro de capacidades operativas normales**. Esta es la pieza causal o estructural desde la que se inicia **crisis, incidentes y escalamiento**: antes de detectar y clasificar, el gerente debe poder señalar qué cambia en el sistema si el concepto está presente y qué debería observar si no lo está. Una definición que no produce predicciones observables todavía es demasiado vaga para dirigir.

La lectura rectora de este bloque es COSO — *Enterprise Risk Management—Integrating with Strategy and Performance*. Su aporte se usa para examinar **riesgo integrado con estrategia, desempeño, revisión e información**. Aplica esa lente al caso sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **time-to-escalate**; regístrala con periodo, unidad, población y baseline.

Relaciona el mecanismo con **crisis**. Si ambos cambian juntos, no concluyas causalidad automáticamente: identifica una tercera variable o mecanismo alternativo que también pueda explicar el patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. crisis: frontera conceptual y error de clasificación

**Definición operacional:** evento que amenaza objetivos críticos y requiere coordinación ejecutiva. Su valor está en distinguirlo de **incident** y **incident commander**. En una decisión real, clasificar una situación en la categoría equivocada cambia la intervención: puedes asignar autoridad donde faltaba información, medir un output cuando debías observar un proceso o tratar una restricción como si fuera una preferencia.

Contrasta el problema con John C. Hull — *Risk Management and Financial Institutions*, que aporta una mirada sobre **identificación y medición de riesgos financieros y no financieros**. Formula dos mini-casos: uno que sí satisface la definición de **crisis** y otro que solo se parece superficialmente. Luego pregunta qué señal distinguiría ambos; para esta clase, **MTTR** es una candidata, pero debe combinarse con evidencia cualitativa o documental cuando el fenómeno no sea directamente medible.

Antes de activar roles y war room, registra explícitamente qué decisión sería errónea si esta frontera conceptual se ignora. Esa frase convierte el vocabulario en criterio gerencial.

### 3. incident commander: operacionalización y medición

**incident commander** significa **rol que coordina respuesta y prioridades**. El problema ya no es definirlo, sino **operacionalizarlo**: qué contar, durante qué ventana, con qué denominador, contra qué baseline y con qué segmentación. Una métrica útil conserva suficiente contexto para no confundir mejora local con mejora del sistema.

OECD — *OECD AI Principles* orienta este bloque mediante **principios para IA confiable, responsable y centrada en las personas**. Usa esa perspectiva para diseñar una ficha de medición: `señal → fórmula/criterio → fuente → frecuencia → owner → interpretación permitida → interpretación prohibida`. La señal asignada es **stakeholder update latency**. Si no existe un dato confiable, la salida correcta no es inventar precisión: diseña el mecanismo de captura y declara la incertidumbre.

Al llegar a proteger personas y contener impacto, compara tendencia, distribución y casos atípicos. Pregunta además si el indicador es *leading* o *lagging* y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; nunca convertirse en el objetivo que reemplaza al fenómeno.

### 4. situation report: trade-offs y efectos de segundo orden

**Definición:** resumen periódico de hechos impacto acciones y necesidades. Este concepto obliga a abandonar la idea de que **crisis, incidentes y escalamiento** tiene una solución gratuita. Toda intervención consume autonomía, tiempo, caja, capacidad, atención, reputación o tolerancia al riesgo. Por eso, antes de comunicar hechos y decisiones, se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Ross Anderson — *Security Engineering* aporta una lente sobre **perspectiva de Ciberseguridad aplicada al problema de la clase**. Úsala para construir una matriz `beneficio / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **decision reversals** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la necesidad de observar efectos laterales fuera del KPI principal.

Haz un *pre-mortem* de **crisis, incidentes y escalamiento**: supone que la opción recomendada fracasó seis meses después y enumera tres mecanismos que podrían explicarlo. Al menos uno debe provenir de un efecto de segundo orden asociado a **situation report** y otro de una hipótesis del caso que nunca fue validada.

### 5. decision log: gobernanza, límites e integración

**decision log** se define como **registro de decisiones supuestos y responsables durante respuesta** y cierra el circuito porque traduce análisis en responsabilidad. La pregunta ejecutiva es quién decide, quién ejecuta, quién debe ser consultado, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar.

OECD — *G20/OECD Principles of Corporate Governance 2023* se utiliza para estudiar **derechos de accionistas, directorio, disclosure, sostenibilidad y buen gobierno** y contrastar la recomendación final. Al ejecutar recuperar investigar y aprender, deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento. Esa trazabilidad protege contra el sesgo retrospectivo y mejora las revisiones posteriores.

La frontera de esta clase es explícita: **Centralizar crisis no significa que el CEO decida cada acción. Define incident command y delegación; reserva nivel ejecutivo para trade-offs, stakeholders y decisiones materiales.**. Conviértela en una regla operativa: `si ocurre X → no aplicar automáticamente → consultar/escalar/revalidar`. Integrar **incident**, **crisis**, **incident commander**, **situation report** y **decision log** significa poder explicar qué parte del diagnóstico sostiene la decisión y cuál sigue siendo una apuesta.

### 6. Integración: de conceptos a una decisión defendible

La síntesis de **crisis, incidentes y escalamiento** no consiste en sumar cinco definiciones. Empieza por **incident**, contrasta **crisis** con **incident commander**, incorpora **situation report** como restricción o mecanismo y usa **decision log** para cerrar el ciclo. Si el análisis no puede explicar cuál de esas piezas cambió la recomendación, todavía no hay comprensión transferible.

Aplica ahora la secuencia **1. detectar y clasificar → 2. activar roles y war room → 3. proteger personas y contener impacto → 4. comunicar hechos y decisiones → 5. recuperar investigar y aprender**. Para cada paso conserva tres columnas: evidencia utilizada, alternativa descartada y razón. Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado y evita reescribir la historia después de conocer el desenlace.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla señala el lente que debes buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| COSO — *Enterprise Risk Management—Integrating with Strategy and Performance* | riesgo integrado con estrategia, desempeño, revisión e información | ¿Qué supuesto de **crisis, incidentes y escalamiento** ayuda a desafiar? |
| John C. Hull — *Risk Management and Financial Institutions* | identificación y medición de riesgos financieros y no financieros | ¿Qué supuesto de **crisis, incidentes y escalamiento** ayuda a desafiar? |
| OECD — *OECD AI Principles* | principios para IA confiable, responsable y centrada en las personas | ¿Qué supuesto de **crisis, incidentes y escalamiento** ayuda a desafiar? |
| Ross Anderson — *Security Engineering* | perspectiva de Ciberseguridad aplicada al problema de la clase | ¿Qué supuesto de **crisis, incidentes y escalamiento** ayuda a desafiar? |
| OECD — *G20/OECD Principles of Corporate Governance 2023* | derechos de accionistas, directorio, disclosure, sostenibilidad y buen gobierno | ¿Qué supuesto de **crisis, incidentes y escalamiento** ayuda a desafiar? |

En **crisis, incidentes y escalamiento**, la lectura se evalúa por **uso**, no por cantidad de páginas. La nota debe indicar qué tesis de las fuentes modifica tu lectura de **incident**, qué evidencia del caso tensiona esa tesis y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación:** A las 09:00 se filtran datos de clientes. Seguridad, legal y comunicaciones trabajan por separado; a las 13:00 tres ejecutivos entregan cifras distintas a prensa y clientes.

**Paso 1 — detectar y clasificar.** La gerencia escribe primero el supuesto asociado a **incident** y evita convertirlo en hecho. Luego busca **time-to-escalate** para contrastarlo en el caso de **crisis, incidentes y escalamiento**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 2 — activar roles y war room.** La gerencia escribe primero el supuesto asociado a **crisis** y evita convertirlo en hecho. Luego busca **MTTR** para contrastarlo en el caso de **crisis, incidentes y escalamiento**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 3 — proteger personas y contener impacto.** La gerencia escribe primero el supuesto asociado a **incident commander** y evita convertirlo en hecho. Luego busca **stakeholder update latency** para contrastarlo en el caso de **crisis, incidentes y escalamiento**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 4 — comunicar hechos y decisiones.** La gerencia escribe primero el supuesto asociado a **situation report** y evita convertirlo en hecho. Luego busca **decision reversals** para contrastarlo en el caso de **crisis, incidentes y escalamiento**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 5 — recuperar investigar y aprender.** La gerencia escribe primero el supuesto asociado a **decision log** y evita convertirlo en hecho. Luego busca **recovery objective** para contrastarlo en el caso de **crisis, incidentes y escalamiento**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Síntesis del caso.** La recomendación debe terminar con responsable, fecha, evidencia de éxito y señal de stop. En **crisis, incidentes y escalamiento**, omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo |
|---|---|---|---|
| **incident** | evento gestionable dentro de capacidades operativas normales | Cuando time-to-escalate es observable y accionable. | Sobrerreaccionar a una señal parcial. |
| **crisis** | evento que amenaza objetivos críticos y requiere coordinación ejecutiva | Cuando la primera explicación no distingue mecanismo o responsabilidad. | Convertir el concepto en etiqueta. |
| **Experimento/revisión** | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar eternamente y no decidir. |
| **Escalamiento** | Elevar autoridad o especialidad | Cuando hay derechos, capital material, regulación o irreversibilidad. | Delegar hacia arriba lo que sí corresponde decidir. |

**Frontera de aplicación:** Centralizar crisis no significa que el CEO decida cada acción. Define incident command y delegación; reserva nivel ejecutivo para trade-offs, stakeholders y decisiones materiales.

## 🪜 De profesional a owner

| Nivel | Responsabilidad sobre crisis, incidentes y escalamiento |
|---|---|
| **Profesional** | usa **crisis, incidentes y escalamiento** para mejorar una contribución propia y explicar sus supuestos con evidencia. |
| **Jefe / Team Lead** | aplica **incident** y **crisis** para coordinar personas sin sustituir conversación por métricas. |
| **Manager / Gerente** | conecta time-to-escalate con capacidad, presupuesto, dependencias y riesgo interáreas. |
| **CEO / Director** | decide si crisis, incidentes y escalamiento cambia estrategia, economía o riesgo de empresa y qué debe llegar al comité o directorio. |
| **Founder / Owner** | pregunta si la solución de crisis, incidentes y escalamiento reduce dependencia del fundador, preserva caja y puede operar como sistema repetible. |

El cambio de nivel en **crisis, incidentes y escalamiento** aumenta el número de personas, dinero, dependencias y consecuencias que quedan dentro de la decisión. Por eso la misma herramienta debe volverse más explícita en evidencia, gobernanza y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

A las 09:00 se filtran datos de clientes. Seguridad, legal y comunicaciones trabajan por separado; a las 13:00 tres ejecutivos entregan cifras distintas a prensa y clientes.

Entrega un **decision brief de crisis, incidentes y escalamiento** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre personas, cliente, operación, caja y riesgo; (e) recomendación; (f) condición que haría cambiarla; (g) dueño y fecha de revisión. Utiliza al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica

1. Reconstruye el caso de **crisis, incidentes y escalamiento** con una tabla `hecho / interpretación / hipótesis / decisión`.
2. Ejecuta **1. detectar y clasificar → 2. activar roles y war room → 3. proteger personas y contener impacto → 4. comunicar hechos y decisiones → 5. recuperar investigar y aprender** y adjunta evidencia para cada transición entre pasos.
3. Calcula o documenta time-to-escalate, MTTR; si no existe dato, diseña cómo obtenerlo.
4. Escribe una alternativa que contradiga tu preferencia inicial y haz un *pre-mortem* específico del caso.
5. Lee dos referencias, registra una coincidencia y una tensión, y modifica el brief si corresponde.
6. Repite la decisión desde el rol de CEO/owner: identifica qué cambia al aumentar el alcance y la irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar incident y crisis como sinónimos | Se pierde la distinción entre “evento gestionable dentro de capacidades operativas normales” y “evento que amenaza objetivos críticos y requiere coordinación ejecutiva” | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por “recuperar investigar y aprender” | Se saltó “detectar y clasificar” y la solución llegó antes que el diagnóstico | Reconstruye la cadena 1. detectar y clasificar → 2. activar roles y war room → 3. proteger personas y contener impacto → 4. comunicar hechos y decisiones → 5. recuperar investigar y aprender y marca el primer supuesto no demostrado. |
| Optimizar solo time-to-escalate | La métrica local sustituyó al resultado del sistema | Contrástala con MTTR y explicita el costo de oportunidad. |
| Generalizar desde un caso favorable | Se confundió evidencia local con una regla universal sobre crisis, incidentes y escalamiento | Centralizar crisis no significa que el CEO decida cada acción. Define incident command y delegación; reserva nivel ejecutivo para trade-offs, stakeholders y decisiones materiales. |
| No fijar revisión | Una decisión sobre crisis, incidentes y escalamiento se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de stop. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **incident** y **crisis** usando un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **incident commander** y qué observación obligaría a rechazar tu interpretación?
3. Aplica **detectar y clasificar → activar roles y war room** al caso de la clase. ¿Qué dato todavía falta?
4. ¿Por qué **time-to-escalate** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la tabla de lectura. ¿Dónde podrían llevar a recomendaciones distintas para **crisis, incidentes y escalamiento**?
6. ¿Qué decisión equivocada podría producirse si se ignora este límite: **Centralizar crisis no significa que el CEO decida cada acción. Define incident command y delegación; reserva nivel ejecutivo para trade-offs, stakeholders y decisiones materiales.**?

## 📥 Entregable

Guarda en `portfolio/190-crisis-incidentes-y-escalamiento/`:

- `leadership-decision-brief.md` con el problema específico de **crisis, incidentes y escalamiento**, evidencia, alternativas, decisión y gobernanza;
- `reading-note.md` contrastando las fuentes de **crisis, incidentes y escalamiento** con edición/páginas consultadas;
- `decision-journal.md` registrando los supuestos de **incident**, confianza, responsable y revisión;
- `red-team.md` con la objeción más fuerte al caso **A las 09:00 se filtran datos de clientes. Seguridad, legal y comunicaciones trabajan por separado; a las 13:00 tres ejecutivos entregan cifras distintas a prensa y clientes.** y el dato que podría invalidar la recomendación.

## 📗 Fuentes y verificación

- COSO — *Enterprise Risk Management—Integrating with Strategy and Performance*. **Uso en esta clase:** riesgo integrado con estrategia, desempeño, revisión e información. Lectura selectiva: índice/capítulos pertinentes a **crisis, incidentes y escalamiento**; registra edición y páginas consultadas.
- John C. Hull — *Risk Management and Financial Institutions*. **Uso en esta clase:** identificación y medición de riesgos financieros y no financieros. Lectura selectiva: índice/capítulos pertinentes a **crisis, incidentes y escalamiento**; registra edición y páginas consultadas.
- OECD — *OECD AI Principles*. **Uso en esta clase:** principios para IA confiable, responsable y centrada en las personas. Lectura selectiva: índice/capítulos pertinentes a **crisis, incidentes y escalamiento**; registra edición y páginas consultadas.
- Ross Anderson — *Security Engineering*. **Uso en esta clase:** perspectiva de Ciberseguridad aplicada al problema de la clase. Lectura selectiva: índice/capítulos pertinentes a **crisis, incidentes y escalamiento**; registra edición y páginas consultadas.
- OECD — *G20/OECD Principles of Corporate Governance 2023*. **Uso en esta clase:** derechos de accionistas, directorio, disclosure, sostenibilidad y buen gobierno. Lectura selectiva: índice/capítulos pertinentes a **crisis, incidentes y escalamiento**; registra edición y páginas consultadas.
- NIST — *Cybersecurity Framework (CSF) 2.0*. **Uso en esta clase:** gobierno, identificación, protección, detección, respuesta y recuperación en ciberseguridad. Lectura selectiva: índice/capítulos pertinentes a **crisis, incidentes y escalamiento**; registra edición y páginas consultadas.
- Susan A. Ambrose et al. — *How Learning Works*. Diseño de objetivos, práctica y feedback.
- Peter C. Brown, Henry L. Roediger III & Mark A. McDaniel — *Make It Stick*. Recuperación, elaboración y transferencia.
- Grant Wiggins & Jay McTighe — *Understanding by Design*. Diseño inverso desde desempeño observable.
- Anders Ericsson & Robert Pool — *Peak*. Práctica deliberada con criterios y retroalimentación.
- William Ellet — *The Case Study Handbook*. Análisis de problema/decisión, evidencia y recomendación.

> **Regla de fuentes para Crisis, incidentes y escalamiento:** las obras anteriores estructuran las perspectivas de esta materia; cualquier norma, ley, impuesto o estándar vivo mencionado en **crisis, incidentes y escalamiento** debe comprobarse nuevamente en su fuente primaria vigente. El desarrollo es original y no reproduce capítulos protegidos.
