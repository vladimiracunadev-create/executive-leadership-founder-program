# Clase 186 — Privacidad y gobierno de datos

**Parte:** 15 — Riesgo, legal, compliance, ciberseguridad e IA  
**Nivel:** Etapa 4 — Gerente → Director  
**Duración sugerida:** 150–180 minutos · **Estándar:** deep-class-v2

## 🎯 Propósito

Gobierno de datos define quién puede recopilar, usar, compartir, retener y eliminar datos, con qué propósito y controles. Privacidad exige principios como finalidad, minimización, seguridad y derechos; una empresa debe mapear datos y decisiones, no solo publicar una política.

La salida de esta parte es **gobernar riesgo, legal, cumplimiento, ciberseguridad, datos e IA de forma integrada**. En esta clase, esa progresión se concreta al exigir que cada afirmación sobre **privacidad y gobierno de datos** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

## 📚 Resultados de aprendizaje

Al finalizar podrás:

1. **Distinguir** `data governance`, `data minimization`, `purpose limitation`, `legal basis`, `data lineage` mediante observables, no por memoria verbal.
2. **Explicar** por qué esas distinciones cambian una decisión de gerente → director.
3. **Aplicar** la secuencia **1. inventariar datos y finalidades → 2. clasificar sensibilidad y bases → 3. definir acceso retención y sharing → 4. implementar derechos y controles → 5. monitorear incidentes y cambios de uso** conservando supuestos, alternativas y trazabilidad.
4. **Interpretar** data inventory coverage, access exceptions, retention violations sin confundir señal, explicación y causalidad.
5. **Resolver** el caso ejecutivo con al menos dos opciones plausibles y un criterio explícito de stop/revisión.
6. **Contrastar** dos obras de referencia y explicar dónde sus lentes son complementarias o entran en tensión.

## 🧭 Agenda

| Tramo | Evidencia de aprendizaje |
|---|---|
| 0–20 min | Recuperación: define data governance y data minimization sin mirar la tabla; corrige con la fuente. |
| 20–70 min | Lectura guiada de conceptos + contraste de dos referencias. |
| 70–115 min | Ejemplo trabajado con data inventory coverage y trazabilidad de supuestos. |
| 115–155 min | Caso ejecutivo: dos alternativas, trade-offs y decisión provisional. |
| 155–180 min | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar comprensión |
|---|---|---|
| **data governance** | roles políticas y controles sobre ciclo de vida de datos | Distingue un hecho compatible y otro que lo refute. |
| **data minimization** | recopilar solo datos necesarios para propósito legítimo | Distingue un hecho compatible y otro que lo refute. |
| **purpose limitation** | usar datos de acuerdo con finalidad definida | Distingue un hecho compatible y otro que lo refute. |
| **legal basis** | fundamento jurídico que autoriza tratamiento cuando la ley lo exige | Distingue un hecho compatible y otro que lo refute. |
| **data lineage** | rastreo de origen transformación y uso de datos | Distingue un hecho compatible y otro que lo refute. |

## 🧠 Modelo mental

```text
1. inventariar datos y finalidades → 2. clasificar sensibilidad y bases → 3. definir acceso retención y sharing → 4. implementar derechos y controles → 5. monitorear incidentes y cambios de uso
```

La secuencia nace del problema de esta clase: **Gobierno de datos define quién puede recopilar, usar, compartir, retener y eliminar datos, con qué propósito y controles. Privacidad exige principios como finalidad, minimización, seguridad y derechos; una empresa debe mapear datos y decisiones, no solo publicar una política.** El método es útil mientras las condiciones permitan observar las señales requeridas. No elimina incertidumbre; la hace visible y obliga a decidir proporcionalmente a la evidencia. Límite principal: **Las obligaciones varían por jurisdicción y cambian. En Chile la Ley 21.719 entra en vigor el 1 de diciembre de 2026; verifica siempre fuente oficial vigente antes de operar.**

## 📖 Desarrollo

### 1. data governance: mecanismo central

**data governance** se entiende aquí como **roles políticas y controles sobre ciclo de vida de datos**. Esta es la pieza causal o estructural desde la que se inicia **privacidad y gobierno de datos**: antes de inventariar datos y finalidades, el gerente debe poder señalar qué cambia en el sistema si el concepto está presente y qué debería observar si no lo está. Una definición que no produce predicciones observables todavía es demasiado vaga para dirigir.

La lectura rectora de este bloque es COSO — *Enterprise Risk Management—Integrating with Strategy and Performance*. Su aporte se usa para examinar **riesgo integrado con estrategia, desempeño, revisión e información**. Aplica esa lente al caso sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **data inventory coverage**; regístrala con periodo, unidad, población y baseline.

Relaciona el mecanismo con **data minimization**. Si ambos cambian juntos, no concluyas causalidad automáticamente: identifica una tercera variable o mecanismo alternativo que también pueda explicar el patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. data minimization: frontera conceptual y error de clasificación

**Definición operacional:** recopilar solo datos necesarios para propósito legítimo. Su valor está en distinguirlo de **data governance** y **purpose limitation**. En una decisión real, clasificar una situación en la categoría equivocada cambia la intervención: puedes asignar autoridad donde faltaba información, medir un output cuando debías observar un proceso o tratar una restricción como si fuera una preferencia.

Contrasta el problema con John C. Hull — *Risk Management and Financial Institutions*, que aporta una mirada sobre **identificación y medición de riesgos financieros y no financieros**. Formula dos mini-casos: uno que sí satisface la definición de **data minimization** y otro que solo se parece superficialmente. Luego pregunta qué señal distinguiría ambos; para esta clase, **access exceptions** es una candidata, pero debe combinarse con evidencia cualitativa o documental cuando el fenómeno no sea directamente medible.

Antes de clasificar sensibilidad y bases, registra explícitamente qué decisión sería errónea si esta frontera conceptual se ignora. Esa frase convierte el vocabulario en criterio gerencial.

### 3. purpose limitation: operacionalización y medición

**purpose limitation** significa **usar datos de acuerdo con finalidad definida**. El problema ya no es definirlo, sino **operacionalizarlo**: qué contar, durante qué ventana, con qué denominador, contra qué baseline y con qué segmentación. Una métrica útil conserva suficiente contexto para no confundir mejora local con mejora del sistema.

Richard A. Clarke & Robert K. Knake — *The Fifth Domain* orienta este bloque mediante **perspectiva de Ciberseguridad aplicada al problema de la clase**. Usa esa perspectiva para diseñar una ficha de medición: `señal → fórmula/criterio → fuente → frecuencia → owner → interpretación permitida → interpretación prohibida`. La señal asignada es **retention violations**. Si no existe un dato confiable, la salida correcta no es inventar precisión: diseña el mecanismo de captura y declara la incertidumbre.

Al llegar a definir acceso retención y sharing, compara tendencia, distribución y casos atípicos. Pregunta además si el indicador es *leading* o *lagging* y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; nunca convertirse en el objetivo que reemplaza al fenómeno.

### 4. legal basis: trade-offs y efectos de segundo orden

**Definición:** fundamento jurídico que autoriza tratamiento cuando la ley lo exige. Este concepto obliga a abandonar la idea de que **privacidad y gobierno de datos** tiene una solución gratuita. Toda intervención consume autonomía, tiempo, caja, capacidad, atención, reputación o tolerancia al riesgo. Por eso, antes de implementar derechos y controles, se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

NIST — *Cybersecurity Framework (CSF) 2.0* aporta una lente sobre **gobierno, identificación, protección, detección, respuesta y recuperación en ciberseguridad**. Úsala para construir una matriz `beneficio / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **privacy requests** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la necesidad de observar efectos laterales fuera del KPI principal.

Haz un *pre-mortem* de **privacidad y gobierno de datos**: supone que la opción recomendada fracasó seis meses después y enumera tres mecanismos que podrían explicarlo. Al menos uno debe provenir de un efecto de segundo orden asociado a **legal basis** y otro de una hipótesis del caso que nunca fue validada.

### 5. data lineage: gobernanza, límites e integración

**data lineage** se define como **rastreo de origen transformación y uso de datos** y cierra el circuito porque traduce análisis en responsabilidad. La pregunta ejecutiva es quién decide, quién ejecuta, quién debe ser consultado, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar.

OECD — *OECD AI Principles* se utiliza para estudiar **principios para IA confiable, responsable y centrada en las personas** y contrastar la recomendación final. Al ejecutar monitorear incidentes y cambios de uso, deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento. Esa trazabilidad protege contra el sesgo retrospectivo y mejora las revisiones posteriores.

La frontera de esta clase es explícita: **Las obligaciones varían por jurisdicción y cambian. En Chile la Ley 21.719 entra en vigor el 1 de diciembre de 2026; verifica siempre fuente oficial vigente antes de operar.**. Conviértela en una regla operativa: `si ocurre X → no aplicar automáticamente → consultar/escalar/revalidar`. Integrar **data governance**, **data minimization**, **purpose limitation**, **legal basis** y **data lineage** significa poder explicar qué parte del diagnóstico sostiene la decisión y cuál sigue siendo una apuesta.

### 6. Integración: de conceptos a una decisión defendible

La síntesis de **privacidad y gobierno de datos** no consiste en sumar cinco definiciones. Empieza por **data governance**, contrasta **data minimization** con **purpose limitation**, incorpora **legal basis** como restricción o mecanismo y usa **data lineage** para cerrar el ciclo. Si el análisis no puede explicar cuál de esas piezas cambió la recomendación, todavía no hay comprensión transferible.

Aplica ahora la secuencia **1. inventariar datos y finalidades → 2. clasificar sensibilidad y bases → 3. definir acceso retención y sharing → 4. implementar derechos y controles → 5. monitorear incidentes y cambios de uso**. Para cada paso conserva tres columnas: evidencia utilizada, alternativa descartada y razón. Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado y evita reescribir la historia después de conocer el desenlace.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla señala el lente que debes buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| COSO — *Enterprise Risk Management—Integrating with Strategy and Performance* | riesgo integrado con estrategia, desempeño, revisión e información | ¿Qué supuesto de **privacidad y gobierno de datos** ayuda a desafiar? |
| John C. Hull — *Risk Management and Financial Institutions* | identificación y medición de riesgos financieros y no financieros | ¿Qué supuesto de **privacidad y gobierno de datos** ayuda a desafiar? |
| Richard A. Clarke & Robert K. Knake — *The Fifth Domain* | perspectiva de Ciberseguridad aplicada al problema de la clase | ¿Qué supuesto de **privacidad y gobierno de datos** ayuda a desafiar? |
| NIST — *Cybersecurity Framework (CSF) 2.0* | gobierno, identificación, protección, detección, respuesta y recuperación en ciberseguridad | ¿Qué supuesto de **privacidad y gobierno de datos** ayuda a desafiar? |
| OECD — *OECD AI Principles* | principios para IA confiable, responsable y centrada en las personas | ¿Qué supuesto de **privacidad y gobierno de datos** ayuda a desafiar? |

En **privacidad y gobierno de datos**, la lectura se evalúa por **uso**, no por cantidad de páginas. La nota debe indicar qué tesis de las fuentes modifica tu lectura de **data governance**, qué evidencia del caso tensiona esa tesis y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación:** Marketing compra una base de 300.000 contactos y la cruza con datos de clientes para entrenar un modelo de propensión. Nadie puede explicar origen, consentimiento, base legal ni retención.

**Paso 1 — inventariar datos y finalidades.** La gerencia escribe primero el supuesto asociado a **data governance** y evita convertirlo en hecho. Luego busca **data inventory coverage** para contrastarlo en el caso de **privacidad y gobierno de datos**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 2 — clasificar sensibilidad y bases.** La gerencia escribe primero el supuesto asociado a **data minimization** y evita convertirlo en hecho. Luego busca **access exceptions** para contrastarlo en el caso de **privacidad y gobierno de datos**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 3 — definir acceso retención y sharing.** La gerencia escribe primero el supuesto asociado a **purpose limitation** y evita convertirlo en hecho. Luego busca **retention violations** para contrastarlo en el caso de **privacidad y gobierno de datos**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 4 — implementar derechos y controles.** La gerencia escribe primero el supuesto asociado a **legal basis** y evita convertirlo en hecho. Luego busca **privacy requests** para contrastarlo en el caso de **privacidad y gobierno de datos**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 5 — monitorear incidentes y cambios de uso.** La gerencia escribe primero el supuesto asociado a **data lineage** y evita convertirlo en hecho. Luego busca **data incidents** para contrastarlo en el caso de **privacidad y gobierno de datos**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Síntesis del caso.** La recomendación debe terminar con responsable, fecha, evidencia de éxito y señal de stop. En **privacidad y gobierno de datos**, omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo |
|---|---|---|---|
| **data governance** | roles políticas y controles sobre ciclo de vida de datos | Cuando data inventory coverage es observable y accionable. | Sobrerreaccionar a una señal parcial. |
| **data minimization** | recopilar solo datos necesarios para propósito legítimo | Cuando la primera explicación no distingue mecanismo o responsabilidad. | Convertir el concepto en etiqueta. |
| **Experimento/revisión** | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar eternamente y no decidir. |
| **Escalamiento** | Elevar autoridad o especialidad | Cuando hay derechos, capital material, regulación o irreversibilidad. | Delegar hacia arriba lo que sí corresponde decidir. |

**Frontera de aplicación:** Las obligaciones varían por jurisdicción y cambian. En Chile la Ley 21.719 entra en vigor el 1 de diciembre de 2026; verifica siempre fuente oficial vigente antes de operar.

## 🪜 De profesional a owner

| Nivel | Responsabilidad sobre privacidad y gobierno de datos |
|---|---|
| **Profesional** | usa **privacidad y gobierno de datos** para mejorar una contribución propia y explicar sus supuestos con evidencia. |
| **Jefe / Team Lead** | aplica **data governance** y **data minimization** para coordinar personas sin sustituir conversación por métricas. |
| **Manager / Gerente** | conecta data inventory coverage con capacidad, presupuesto, dependencias y riesgo interáreas. |
| **CEO / Director** | decide si privacidad y gobierno de datos cambia estrategia, economía o riesgo de empresa y qué debe llegar al comité o directorio. |
| **Founder / Owner** | pregunta si la solución de privacidad y gobierno de datos reduce dependencia del fundador, preserva caja y puede operar como sistema repetible. |

El cambio de nivel en **privacidad y gobierno de datos** aumenta el número de personas, dinero, dependencias y consecuencias que quedan dentro de la decisión. Por eso la misma herramienta debe volverse más explícita en evidencia, gobernanza y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Marketing compra una base de 300.000 contactos y la cruza con datos de clientes para entrenar un modelo de propensión. Nadie puede explicar origen, consentimiento, base legal ni retención.

Entrega un **decision brief de privacidad y gobierno de datos** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre personas, cliente, operación, caja y riesgo; (e) recomendación; (f) condición que haría cambiarla; (g) dueño y fecha de revisión. Utiliza al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica

1. Reconstruye el caso de **privacidad y gobierno de datos** con una tabla `hecho / interpretación / hipótesis / decisión`.
2. Ejecuta **1. inventariar datos y finalidades → 2. clasificar sensibilidad y bases → 3. definir acceso retención y sharing → 4. implementar derechos y controles → 5. monitorear incidentes y cambios de uso** y adjunta evidencia para cada transición entre pasos.
3. Calcula o documenta data inventory coverage, access exceptions; si no existe dato, diseña cómo obtenerlo.
4. Escribe una alternativa que contradiga tu preferencia inicial y haz un *pre-mortem* específico del caso.
5. Lee dos referencias, registra una coincidencia y una tensión, y modifica el brief si corresponde.
6. Repite la decisión desde el rol de CEO/owner: identifica qué cambia al aumentar el alcance y la irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar data governance y data minimization como sinónimos | Se pierde la distinción entre “roles políticas y controles sobre ciclo de vida de datos” y “recopilar solo datos necesarios para propósito legítimo” | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por “monitorear incidentes y cambios de uso” | Se saltó “inventariar datos y finalidades” y la solución llegó antes que el diagnóstico | Reconstruye la cadena 1. inventariar datos y finalidades → 2. clasificar sensibilidad y bases → 3. definir acceso retención y sharing → 4. implementar derechos y controles → 5. monitorear incidentes y cambios de uso y marca el primer supuesto no demostrado. |
| Optimizar solo data inventory coverage | La métrica local sustituyó al resultado del sistema | Contrástala con access exceptions y explicita el costo de oportunidad. |
| Generalizar desde un caso favorable | Se confundió evidencia local con una regla universal sobre privacidad y gobierno de datos | Las obligaciones varían por jurisdicción y cambian. En Chile la Ley 21.719 entra en vigor el 1 de diciembre de 2026; verifica siempre fuente oficial vigente antes de operar. |
| No fijar revisión | Una decisión sobre privacidad y gobierno de datos se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de stop. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **data governance** y **data minimization** usando un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **purpose limitation** y qué observación obligaría a rechazar tu interpretación?
3. Aplica **inventariar datos y finalidades → clasificar sensibilidad y bases** al caso de la clase. ¿Qué dato todavía falta?
4. ¿Por qué **data inventory coverage** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la tabla de lectura. ¿Dónde podrían llevar a recomendaciones distintas para **privacidad y gobierno de datos**?
6. ¿Qué decisión equivocada podría producirse si se ignora este límite: **Las obligaciones varían por jurisdicción y cambian. En Chile la Ley 21.719 entra en vigor el 1 de diciembre de 2026; verifica siempre fuente oficial vigente antes de operar.**?

## 📥 Entregable

Guarda en `portfolio/186-privacidad-y-gobierno-de-datos/`:

- `risk-governance-brief.md` con el problema específico de **privacidad y gobierno de datos**, evidencia, alternativas, decisión y gobernanza;
- `reading-note.md` contrastando las fuentes de **privacidad y gobierno de datos** con edición/páginas consultadas;
- `decision-journal.md` registrando los supuestos de **data governance**, confianza, responsable y revisión;
- `red-team.md` con la objeción más fuerte al caso **Marketing compra una base de 300.000 contactos y la cruza con datos de clientes para entrenar un modelo de propensión. Nadie puede explicar origen, consentimiento, base legal ni retención.** y el dato que podría invalidar la recomendación.

## 📗 Fuentes y verificación

- COSO — *Enterprise Risk Management—Integrating with Strategy and Performance*. **Uso en esta clase:** riesgo integrado con estrategia, desempeño, revisión e información. Lectura selectiva: índice/capítulos pertinentes a **privacidad y gobierno de datos**; registra edición y páginas consultadas.
- John C. Hull — *Risk Management and Financial Institutions*. **Uso en esta clase:** identificación y medición de riesgos financieros y no financieros. Lectura selectiva: índice/capítulos pertinentes a **privacidad y gobierno de datos**; registra edición y páginas consultadas.
- Richard A. Clarke & Robert K. Knake — *The Fifth Domain*. **Uso en esta clase:** perspectiva de Ciberseguridad aplicada al problema de la clase. Lectura selectiva: índice/capítulos pertinentes a **privacidad y gobierno de datos**; registra edición y páginas consultadas.
- NIST — *Cybersecurity Framework (CSF) 2.0*. **Uso en esta clase:** gobierno, identificación, protección, detección, respuesta y recuperación en ciberseguridad. Lectura selectiva: índice/capítulos pertinentes a **privacidad y gobierno de datos**; registra edición y páginas consultadas.
- OECD — *OECD AI Principles*. **Uso en esta clase:** principios para IA confiable, responsable y centrada en las personas. Lectura selectiva: índice/capítulos pertinentes a **privacidad y gobierno de datos**; registra edición y páginas consultadas.
- NIST — *AI Risk Management Framework (AI RMF 1.0)*. **Uso en esta clase:** gobierno y gestión de riesgos de IA confiable a lo largo del ciclo de vida. Lectura selectiva: índice/capítulos pertinentes a **privacidad y gobierno de datos**; registra edición y páginas consultadas.
- Susan A. Ambrose et al. — *How Learning Works*. Diseño de objetivos, práctica y feedback.
- Peter C. Brown, Henry L. Roediger III & Mark A. McDaniel — *Make It Stick*. Recuperación, elaboración y transferencia.
- Grant Wiggins & Jay McTighe — *Understanding by Design*. Diseño inverso desde desempeño observable.
- Anders Ericsson & Robert Pool — *Peak*. Práctica deliberada con criterios y retroalimentación.
- William Ellet — *The Case Study Handbook*. Análisis de problema/decisión, evidencia y recomendación.

> **Regla de fuentes para Privacidad y gobierno de datos:** las obras anteriores estructuran las perspectivas de esta materia; cualquier norma, ley, impuesto o estándar vivo mencionado en **privacidad y gobierno de datos** debe comprobarse nuevamente en su fuente primaria vigente. El desarrollo es original y no reproduce capítulos protegidos.
