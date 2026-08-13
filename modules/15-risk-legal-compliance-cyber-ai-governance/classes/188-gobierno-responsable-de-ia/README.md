# Clase 188 — Gobierno responsable de IA

**Parte:** 15 — Riesgo, legal, compliance, ciberseguridad e IA  
**Nivel:** Etapa 4 — Gerente → Director  
**Duración sugerida:** 150–180 minutos · **Estándar:** deep-class-v2

## 🎯 Propósito

Gobernanza responsable de IA aborda valor, riesgo, accountability, datos, evaluación, supervisión humana y monitoreo a lo largo del ciclo de vida. NIST AI RMF organiza Govern, Map, Measure y Manage; el desafío ejecutivo es decidir dónde IA es apropiada y bajo qué controles.

La salida de esta parte es **gobernar riesgo, legal, cumplimiento, ciberseguridad, datos e IA de forma integrada**. En esta clase, esa progresión se concreta al exigir que cada afirmación sobre **gobierno responsable de IA** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

## 📚 Resultados de aprendizaje

Al finalizar podrás:

1. **Distinguir** `AI governance`, `AI risk`, `human oversight`, `model evaluation`, `AI inventory` mediante observables, no por memoria verbal.
2. **Explicar** por qué esas distinciones cambian una decisión de gerente → director.
3. **Aplicar** la secuencia **1. inventariar casos de IA → 2. clasificar impacto y contexto → 3. definir evaluación y guardrails → 4. asignar accountability y human oversight → 5. monitorizar drift incidentes y cambios** conservando supuestos, alternativas y trazabilidad.
4. **Interpretar** AI inventory coverage, evaluation pass rate, human override sin confundir señal, explicación y causalidad.
5. **Resolver** el caso ejecutivo con al menos dos opciones plausibles y un criterio explícito de stop/revisión.
6. **Contrastar** dos obras de referencia y explicar dónde sus lentes son complementarias o entran en tensión.

## 🧭 Agenda

| Tramo | Evidencia de aprendizaje |
|---|---|
| 0–20 min | Recuperación: define AI governance y AI risk sin mirar la tabla; corrige con la fuente. |
| 20–70 min | Lectura guiada de conceptos + contraste de dos referencias. |
| 70–115 min | Ejemplo trabajado con AI inventory coverage y trazabilidad de supuestos. |
| 115–155 min | Caso ejecutivo: dos alternativas, trade-offs y decisión provisional. |
| 155–180 min | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar comprensión |
|---|---|---|
| **AI governance** | sistema de responsabilidades y controles para desarrollar o usar IA | Distingue un hecho compatible y otro que lo refute. |
| **AI risk** | posible daño o pérdida derivada de comportamiento uso o dependencia de IA | Distingue un hecho compatible y otro que lo refute. |
| **human oversight** | intervención humana con autoridad y capacidad real de revisar | Distingue un hecho compatible y otro que lo refute. |
| **model evaluation** | medición de desempeño robustez y riesgos en contexto | Distingue un hecho compatible y otro que lo refute. |
| **AI inventory** | registro de sistemas owners finalidad datos y criticidad | Distingue un hecho compatible y otro que lo refute. |

## 🧠 Modelo mental

```text
1. inventariar casos de IA → 2. clasificar impacto y contexto → 3. definir evaluación y guardrails → 4. asignar accountability y human oversight → 5. monitorizar drift incidentes y cambios
```

La secuencia nace del problema de esta clase: **Gobernanza responsable de IA aborda valor, riesgo, accountability, datos, evaluación, supervisión humana y monitoreo a lo largo del ciclo de vida. NIST AI RMF organiza Govern, Map, Measure y Manage; el desafío ejecutivo es decidir dónde IA es apropiada y bajo qué controles.** El método es útil mientras las condiciones permitan observar las señales requeridas. No elimina incertidumbre; la hace visible y obliga a decidir proporcionalmente a la evidencia. Límite principal: **No todo uso de IA requiere el mismo control. Ajusta rigor a impacto y reversibilidad, pero no trates una herramienta de bajo costo como excusa para ignorar privacidad, discriminación o seguridad.**

## 📖 Desarrollo

### 1. AI governance: mecanismo central

**AI governance** se entiende aquí como **sistema de responsabilidades y controles para desarrollar o usar IA**. Esta es la pieza causal o estructural desde la que se inicia **gobierno responsable de IA**: antes de inventariar casos de ia, el gerente debe poder señalar qué cambia en el sistema si el concepto está presente y qué debería observar si no lo está. Una definición que no produce predicciones observables todavía es demasiado vaga para dirigir.

La lectura rectora de este bloque es COSO — *Enterprise Risk Management—Integrating with Strategy and Performance*. Su aporte se usa para examinar **riesgo integrado con estrategia, desempeño, revisión e información**. Aplica esa lente al caso sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **AI inventory coverage**; regístrala con periodo, unidad, población y baseline.

Relaciona el mecanismo con **AI risk**. Si ambos cambian juntos, no concluyas causalidad automáticamente: identifica una tercera variable o mecanismo alternativo que también pueda explicar el patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. AI risk: frontera conceptual y error de clasificación

**Definición operacional:** posible daño o pérdida derivada de comportamiento uso o dependencia de IA. Su valor está en distinguirlo de **AI governance** y **human oversight**. En una decisión real, clasificar una situación en la categoría equivocada cambia la intervención: puedes asignar autoridad donde faltaba información, medir un output cuando debías observar un proceso o tratar una restricción como si fuera una preferencia.

Contrasta el problema con John C. Hull — *Risk Management and Financial Institutions*, que aporta una mirada sobre **identificación y medición de riesgos financieros y no financieros**. Formula dos mini-casos: uno que sí satisface la definición de **AI risk** y otro que solo se parece superficialmente. Luego pregunta qué señal distinguiría ambos; para esta clase, **evaluation pass rate** es una candidata, pero debe combinarse con evidencia cualitativa o documental cuando el fenómeno no sea directamente medible.

Antes de clasificar impacto y contexto, registra explícitamente qué decisión sería errónea si esta frontera conceptual se ignora. Esa frase convierte el vocabulario en criterio gerencial.

### 3. human oversight: operacionalización y medición

**human oversight** significa **intervención humana con autoridad y capacidad real de revisar**. El problema ya no es definirlo, sino **operacionalizarlo**: qué contar, durante qué ventana, con qué denominador, contra qué baseline y con qué segmentación. Una métrica útil conserva suficiente contexto para no confundir mejora local con mejora del sistema.

Bob Tricker — *Corporate Governance* orienta este bloque mediante **separación entre dirección, supervisión, accountability y gobierno corporativo**. Usa esa perspectiva para diseñar una ficha de medición: `señal → fórmula/criterio → fuente → frecuencia → owner → interpretación permitida → interpretación prohibida`. La señal asignada es **human override**. Si no existe un dato confiable, la salida correcta no es inventar precisión: diseña el mecanismo de captura y declara la incertidumbre.

Al llegar a definir evaluación y guardrails, compara tendencia, distribución y casos atípicos. Pregunta además si el indicador es *leading* o *lagging* y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; nunca convertirse en el objetivo que reemplaza al fenómeno.

### 4. model evaluation: trade-offs y efectos de segundo orden

**Definición:** medición de desempeño robustez y riesgos en contexto. Este concepto obliga a abandonar la idea de que **gobierno responsable de IA** tiene una solución gratuita. Toda intervención consume autonomía, tiempo, caja, capacidad, atención, reputación o tolerancia al riesgo. Por eso, antes de asignar accountability y human oversight, se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

NIST — *Cybersecurity Framework (CSF) 2.0* aporta una lente sobre **gobierno, identificación, protección, detección, respuesta y recuperación en ciberseguridad**. Úsala para construir una matriz `beneficio / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **incident rate** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la necesidad de observar efectos laterales fuera del KPI principal.

Haz un *pre-mortem* de **gobierno responsable de IA**: supone que la opción recomendada fracasó seis meses después y enumera tres mecanismos que podrían explicarlo. Al menos uno debe provenir de un efecto de segundo orden asociado a **model evaluation** y otro de una hipótesis del caso que nunca fue validada.

### 5. AI inventory: gobernanza, límites e integración

**AI inventory** se define como **registro de sistemas owners finalidad datos y criticidad** y cierra el circuito porque traduce análisis en responsabilidad. La pregunta ejecutiva es quién decide, quién ejecuta, quién debe ser consultado, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar.

OECD — *OECD AI Principles* se utiliza para estudiar **principios para IA confiable, responsable y centrada en las personas** y contrastar la recomendación final. Al ejecutar monitorizar drift incidentes y cambios, deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento. Esa trazabilidad protege contra el sesgo retrospectivo y mejora las revisiones posteriores.

La frontera de esta clase es explícita: **No todo uso de IA requiere el mismo control. Ajusta rigor a impacto y reversibilidad, pero no trates una herramienta de bajo costo como excusa para ignorar privacidad, discriminación o seguridad.**. Conviértela en una regla operativa: `si ocurre X → no aplicar automáticamente → consultar/escalar/revalidar`. Integrar **AI governance**, **AI risk**, **human oversight**, **model evaluation** y **AI inventory** significa poder explicar qué parte del diagnóstico sostiene la decisión y cuál sigue siendo una apuesta.

### 6. Integración: de conceptos a una decisión defendible

La síntesis de **gobierno responsable de IA** no consiste en sumar cinco definiciones. Empieza por **AI governance**, contrasta **AI risk** con **human oversight**, incorpora **model evaluation** como restricción o mecanismo y usa **AI inventory** para cerrar el ciclo. Si el análisis no puede explicar cuál de esas piezas cambió la recomendación, todavía no hay comprensión transferible.

Aplica ahora la secuencia **1. inventariar casos de IA → 2. clasificar impacto y contexto → 3. definir evaluación y guardrails → 4. asignar accountability y human oversight → 5. monitorizar drift incidentes y cambios**. Para cada paso conserva tres columnas: evidencia utilizada, alternativa descartada y razón. Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado y evita reescribir la historia después de conocer el desenlace.

## 🔧 Profundización específica

### NIST AI RMF y ciclo de riesgo

AI RMF organiza trabajo en **Govern, Map, Measure, Manage**. `Map` obliga a comprender contexto y afectados; `Measure` evalúa propiedades/riesgos con métodos apropiados; `Manage` prioriza respuestas; `Govern` atraviesa el ciclo.

Para cada caso de IA registra propósito, datos, modelo/proveedor, decisiones que afecta, supervisión humana, métricas de calidad, fallos previsibles, privacidad/seguridad, sesgo y plan de incidentes. “Tiene human-in-the-loop” no basta si la persona no tiene información, tiempo o autoridad real para intervenir.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla señala el lente que debes buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| COSO — *Enterprise Risk Management—Integrating with Strategy and Performance* | riesgo integrado con estrategia, desempeño, revisión e información | ¿Qué supuesto de **gobierno responsable de IA** ayuda a desafiar? |
| John C. Hull — *Risk Management and Financial Institutions* | identificación y medición de riesgos financieros y no financieros | ¿Qué supuesto de **gobierno responsable de IA** ayuda a desafiar? |
| Bob Tricker — *Corporate Governance* | separación entre dirección, supervisión, accountability y gobierno corporativo | ¿Qué supuesto de **gobierno responsable de IA** ayuda a desafiar? |
| NIST — *Cybersecurity Framework (CSF) 2.0* | gobierno, identificación, protección, detección, respuesta y recuperación en ciberseguridad | ¿Qué supuesto de **gobierno responsable de IA** ayuda a desafiar? |
| OECD — *OECD AI Principles* | principios para IA confiable, responsable y centrada en las personas | ¿Qué supuesto de **gobierno responsable de IA** ayuda a desafiar? |

En **gobierno responsable de IA**, la lectura se evalúa por **uso**, no por cantidad de páginas. La nota debe indicar qué tesis de las fuentes modifica tu lectura de **AI governance**, qué evidencia del caso tensiona esa tesis y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación:** RR.HH. adopta un modelo externo para filtrar candidatos sin conocer datos de entrenamiento. El proveedor cambia versión automáticamente y no existe evaluación de sesgo ni mecanismo de apelación.

**Paso 1 — inventariar casos de IA.** La gerencia escribe primero el supuesto asociado a **AI governance** y evita convertirlo en hecho. Luego busca **AI inventory coverage** para contrastarlo en el caso de **gobierno responsable de IA**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 2 — clasificar impacto y contexto.** La gerencia escribe primero el supuesto asociado a **AI risk** y evita convertirlo en hecho. Luego busca **evaluation pass rate** para contrastarlo en el caso de **gobierno responsable de IA**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 3 — definir evaluación y guardrails.** La gerencia escribe primero el supuesto asociado a **human oversight** y evita convertirlo en hecho. Luego busca **human override** para contrastarlo en el caso de **gobierno responsable de IA**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 4 — asignar accountability y human oversight.** La gerencia escribe primero el supuesto asociado a **model evaluation** y evita convertirlo en hecho. Luego busca **incident rate** para contrastarlo en el caso de **gobierno responsable de IA**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 5 — monitorizar drift incidentes y cambios.** La gerencia escribe primero el supuesto asociado a **AI inventory** y evita convertirlo en hecho. Luego busca **model drift** para contrastarlo en el caso de **gobierno responsable de IA**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Síntesis del caso.** La recomendación debe terminar con responsable, fecha, evidencia de éxito y señal de stop. En **gobierno responsable de IA**, omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo |
|---|---|---|---|
| **AI governance** | sistema de responsabilidades y controles para desarrollar o usar IA | Cuando AI inventory coverage es observable y accionable. | Sobrerreaccionar a una señal parcial. |
| **AI risk** | posible daño o pérdida derivada de comportamiento uso o dependencia de IA | Cuando la primera explicación no distingue mecanismo o responsabilidad. | Convertir el concepto en etiqueta. |
| **Experimento/revisión** | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar eternamente y no decidir. |
| **Escalamiento** | Elevar autoridad o especialidad | Cuando hay derechos, capital material, regulación o irreversibilidad. | Delegar hacia arriba lo que sí corresponde decidir. |

**Frontera de aplicación:** No todo uso de IA requiere el mismo control. Ajusta rigor a impacto y reversibilidad, pero no trates una herramienta de bajo costo como excusa para ignorar privacidad, discriminación o seguridad.

## 🪜 De profesional a owner

| Nivel | Responsabilidad sobre gobierno responsable de IA |
|---|---|
| **Profesional** | usa **gobierno responsable de IA** para mejorar una contribución propia y explicar sus supuestos con evidencia. |
| **Jefe / Team Lead** | aplica **AI governance** y **AI risk** para coordinar personas sin sustituir conversación por métricas. |
| **Manager / Gerente** | conecta AI inventory coverage con capacidad, presupuesto, dependencias y riesgo interáreas. |
| **CEO / Director** | decide si gobierno responsable de IA cambia estrategia, economía o riesgo de empresa y qué debe llegar al comité o directorio. |
| **Founder / Owner** | pregunta si la solución de gobierno responsable de IA reduce dependencia del fundador, preserva caja y puede operar como sistema repetible. |

El cambio de nivel en **gobierno responsable de IA** aumenta el número de personas, dinero, dependencias y consecuencias que quedan dentro de la decisión. Por eso la misma herramienta debe volverse más explícita en evidencia, gobernanza y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

RR.HH. adopta un modelo externo para filtrar candidatos sin conocer datos de entrenamiento. El proveedor cambia versión automáticamente y no existe evaluación de sesgo ni mecanismo de apelación.

Entrega un **decision brief de gobierno responsable de IA** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre personas, cliente, operación, caja y riesgo; (e) recomendación; (f) condición que haría cambiarla; (g) dueño y fecha de revisión. Utiliza al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica

1. Reconstruye el caso de **gobierno responsable de IA** con una tabla `hecho / interpretación / hipótesis / decisión`.
2. Ejecuta **1. inventariar casos de IA → 2. clasificar impacto y contexto → 3. definir evaluación y guardrails → 4. asignar accountability y human oversight → 5. monitorizar drift incidentes y cambios** y adjunta evidencia para cada transición entre pasos.
3. Calcula o documenta AI inventory coverage, evaluation pass rate; si no existe dato, diseña cómo obtenerlo.
4. Escribe una alternativa que contradiga tu preferencia inicial y haz un *pre-mortem* específico del caso.
5. Lee dos referencias, registra una coincidencia y una tensión, y modifica el brief si corresponde.
6. Repite la decisión desde el rol de CEO/owner: identifica qué cambia al aumentar el alcance y la irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar AI governance y AI risk como sinónimos | Se pierde la distinción entre “sistema de responsabilidades y controles para desarrollar o usar IA” y “posible daño o pérdida derivada de comportamiento uso o dependencia de IA” | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por “monitorizar drift incidentes y cambios” | Se saltó “inventariar casos de IA” y la solución llegó antes que el diagnóstico | Reconstruye la cadena 1. inventariar casos de IA → 2. clasificar impacto y contexto → 3. definir evaluación y guardrails → 4. asignar accountability y human oversight → 5. monitorizar drift incidentes y cambios y marca el primer supuesto no demostrado. |
| Optimizar solo AI inventory coverage | La métrica local sustituyó al resultado del sistema | Contrástala con evaluation pass rate y explicita el costo de oportunidad. |
| Generalizar desde un caso favorable | Se confundió evidencia local con una regla universal sobre gobierno responsable de IA | No todo uso de IA requiere el mismo control. Ajusta rigor a impacto y reversibilidad, pero no trates una herramienta de bajo costo como excusa para ignorar privacidad, discriminación o seguridad. |
| No fijar revisión | Una decisión sobre gobierno responsable de IA se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de stop. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **AI governance** y **AI risk** usando un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **human oversight** y qué observación obligaría a rechazar tu interpretación?
3. Aplica **inventariar casos de IA → clasificar impacto y contexto** al caso de la clase. ¿Qué dato todavía falta?
4. ¿Por qué **AI inventory coverage** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la tabla de lectura. ¿Dónde podrían llevar a recomendaciones distintas para **gobierno responsable de IA**?
6. ¿Qué decisión equivocada podría producirse si se ignora este límite: **No todo uso de IA requiere el mismo control. Ajusta rigor a impacto y reversibilidad, pero no trates una herramienta de bajo costo como excusa para ignorar privacidad, discriminación o seguridad.**?

## 📥 Entregable

Guarda en `portfolio/188-gobierno-responsable-de-ia/`:

- `risk-governance-brief.md` con el problema específico de **gobierno responsable de IA**, evidencia, alternativas, decisión y gobernanza;
- `reading-note.md` contrastando las fuentes de **gobierno responsable de IA** con edición/páginas consultadas;
- `decision-journal.md` registrando los supuestos de **AI governance**, confianza, responsable y revisión;
- `red-team.md` con la objeción más fuerte al caso **RR.HH. adopta un modelo externo para filtrar candidatos sin conocer datos de entrenamiento. El proveedor cambia versión automáticamente y no existe evaluación de sesgo ni mecanismo de apelación.** y el dato que podría invalidar la recomendación.

## 📗 Fuentes y verificación

- COSO — *Enterprise Risk Management—Integrating with Strategy and Performance*. **Uso en esta clase:** riesgo integrado con estrategia, desempeño, revisión e información. Lectura selectiva: índice/capítulos pertinentes a **gobierno responsable de IA**; registra edición y páginas consultadas.
- John C. Hull — *Risk Management and Financial Institutions*. **Uso en esta clase:** identificación y medición de riesgos financieros y no financieros. Lectura selectiva: índice/capítulos pertinentes a **gobierno responsable de IA**; registra edición y páginas consultadas.
- Bob Tricker — *Corporate Governance*. **Uso en esta clase:** separación entre dirección, supervisión, accountability y gobierno corporativo. Lectura selectiva: índice/capítulos pertinentes a **gobierno responsable de IA**; registra edición y páginas consultadas.
- NIST — *Cybersecurity Framework (CSF) 2.0*. **Uso en esta clase:** gobierno, identificación, protección, detección, respuesta y recuperación en ciberseguridad. Lectura selectiva: índice/capítulos pertinentes a **gobierno responsable de IA**; registra edición y páginas consultadas.
- OECD — *OECD AI Principles*. **Uso en esta clase:** principios para IA confiable, responsable y centrada en las personas. Lectura selectiva: índice/capítulos pertinentes a **gobierno responsable de IA**; registra edición y páginas consultadas.
- Ross Anderson — *Security Engineering*. **Uso en esta clase:** perspectiva de Ciberseguridad aplicada al problema de la clase. Lectura selectiva: índice/capítulos pertinentes a **gobierno responsable de IA**; registra edición y páginas consultadas.
- NIST — *AI Risk Management Framework*. Fuente primaria: <https://www.nist.gov/itl/ai-risk-management-framework>.
- Susan A. Ambrose et al. — *How Learning Works*. Diseño de objetivos, práctica y feedback.
- Peter C. Brown, Henry L. Roediger III & Mark A. McDaniel — *Make It Stick*. Recuperación, elaboración y transferencia.
- Grant Wiggins & Jay McTighe — *Understanding by Design*. Diseño inverso desde desempeño observable.
- Anders Ericsson & Robert Pool — *Peak*. Práctica deliberada con criterios y retroalimentación.
- William Ellet — *The Case Study Handbook*. Análisis de problema/decisión, evidencia y recomendación.

> **Regla de fuentes para Gobierno responsable de IA:** las obras anteriores estructuran las perspectivas de esta materia; cualquier norma, ley, impuesto o estándar vivo mencionado en **gobierno responsable de IA** debe comprobarse nuevamente en su fuente primaria vigente. El desarrollo es original y no reproduce capítulos protegidos.
