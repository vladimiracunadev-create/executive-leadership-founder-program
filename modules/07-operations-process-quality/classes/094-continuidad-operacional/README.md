# Clase 094 — Continuidad operacional

**Parte:** 07 — Operaciones, procesos y calidad  
**Nivel:** Etapa 2 — Jefe → Manager  
**Duración sugerida:** 150–180 minutos · **Estándar:** deep-class-v2

## 🎯 Propósito

Continuidad operacional protege servicios críticos durante disrupciones mediante análisis de impacto, objetivos de recuperación, estrategias y ejercicios. No es solo backup tecnológico: personas, proveedores, instalaciones, datos y decisiones forman parte del plan.

La salida de esta parte es **operar procesos end-to-end con capacidad, calidad, continuidad y mejora**. En esta clase, esa progresión se concreta al exigir que cada afirmación sobre **continuidad operacional** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

## 📚 Resultados de aprendizaje

Al finalizar podrás:

1. **Distinguir** `BIA`, `RTO`, `RPO`, `BCP`, `DR` mediante observables, no por memoria verbal.
2. **Explicar** por qué esas distinciones cambian una decisión de jefe → manager.
3. **Aplicar** la secuencia **1. identificar servicios críticos → 2. hacer BIA y dependencias → 3. definir RTO/RPO → 4. diseñar estrategias y playbooks → 5. ejercitar y corregir brechas** conservando supuestos, alternativas y trazabilidad.
4. **Interpretar** RTO alcanzado, RPO alcanzado, servicios sin plan sin confundir señal, explicación y causalidad.
5. **Resolver** el caso ejecutivo con al menos dos opciones plausibles y un criterio explícito de stop/revisión.
6. **Contrastar** dos obras de referencia y explicar dónde sus lentes son complementarias o entran en tensión.

## 🧭 Agenda

| Tramo | Evidencia de aprendizaje |
|---|---|
| 0–20 min | Recuperación: define BIA y RTO sin mirar la tabla; corrige con la fuente. |
| 20–70 min | Lectura guiada de conceptos + contraste de dos referencias. |
| 70–115 min | Ejemplo trabajado con RTO alcanzado y trazabilidad de supuestos. |
| 115–155 min | Caso ejecutivo: dos alternativas, trade-offs y decisión provisional. |
| 155–180 min | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar comprensión |
|---|---|---|
| **BIA** | análisis de impacto que prioriza procesos y tiempos críticos | Distingue un hecho compatible y otro que lo refute. |
| **RTO** | tiempo objetivo para restaurar una capacidad | Distingue un hecho compatible y otro que lo refute. |
| **RPO** | pérdida máxima de datos tolerada medida en tiempo | Distingue un hecho compatible y otro que lo refute. |
| **BCP** | plan de continuidad de negocio | Distingue un hecho compatible y otro que lo refute. |
| **DR** | recuperación de tecnología e infraestructura después de incidente | Distingue un hecho compatible y otro que lo refute. |

## 🧠 Modelo mental

```text
1. identificar servicios críticos → 2. hacer BIA y dependencias → 3. definir RTO/RPO → 4. diseñar estrategias y playbooks → 5. ejercitar y corregir brechas
```

La secuencia nace del problema de esta clase: **Continuidad operacional protege servicios críticos durante disrupciones mediante análisis de impacto, objetivos de recuperación, estrategias y ejercicios. No es solo backup tecnológico: personas, proveedores, instalaciones, datos y decisiones forman parte del plan.** El método es útil mientras las condiciones permitan observar las señales requeridas. No elimina incertidumbre; la hace visible y obliga a decidir proporcionalmente a la evidencia. Límite principal: **Continuidad total es imposible y costosa. Prioriza por impacto y tiempos; los objetivos deben estar aprobados por negocio, no elegidos solo por tecnología.**

## 📖 Desarrollo

### 1. BIA: mecanismo central

**BIA** se entiende aquí como **análisis de impacto que prioriza procesos y tiempos críticos**. Esta es la pieza causal o estructural desde la que se inicia **continuidad operacional**: antes de identificar servicios críticos, el gerente debe poder señalar qué cambia en el sistema si el concepto está presente y qué debería observar si no lo está. Una definición que no produce predicciones observables todavía es demasiado vaga para dirigir.

La lectura rectora de este bloque es Nigel Slack & Alistair Brandon-Jones — *Operations Management*. Su aporte se usa para examinar **capacidad, procesos, variabilidad, calidad y estrategia de operaciones**. Aplica esa lente al caso sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **RTO alcanzado**; regístrala con periodo, unidad, población y baseline.

Relaciona el mecanismo con **RTO**. Si ambos cambian juntos, no concluyas causalidad automáticamente: identifica una tercera variable o mecanismo alternativo que también pueda explicar el patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. RTO: frontera conceptual y error de clasificación

**Definición operacional:** tiempo objetivo para restaurar una capacidad. Su valor está en distinguirlo de **BIA** y **RPO**. En una decisión real, clasificar una situación en la categoría equivocada cambia la intervención: puedes asignar autoridad donde faltaba información, medir un output cuando debías observar un proceso o tratar una restricción como si fuera una preferencia.

Contrasta el problema con Eliyahu M. Goldratt & Jeff Cox — *The Goal*, que aporta una mirada sobre **restricciones, throughput, inventario y pensamiento de flujo**. Formula dos mini-casos: uno que sí satisface la definición de **RTO** y otro que solo se parece superficialmente. Luego pregunta qué señal distinguiría ambos; para esta clase, **RPO alcanzado** es una candidata, pero debe combinarse con evidencia cualitativa o documental cuando el fenómeno no sea directamente medible.

Antes de hacer bia y dependencias, registra explícitamente qué decisión sería errónea si esta frontera conceptual se ignora. Esa frase convierte el vocabulario en criterio gerencial.

### 3. RPO: operacionalización y medición

**RPO** significa **pérdida máxima de datos tolerada medida en tiempo**. El problema ya no es definirlo, sino **operacionalizarlo**: qué contar, durante qué ventana, con qué denominador, contra qué baseline y con qué segmentación. Una métrica útil conserva suficiente contexto para no confundir mejora local con mejora del sistema.

Jeffrey K. Liker — *The Toyota Way* orienta este bloque mediante **perspectiva de Operaciones aplicada al problema de la clase**. Usa esa perspectiva para diseñar una ficha de medición: `señal → fórmula/criterio → fuente → frecuencia → owner → interpretación permitida → interpretación prohibida`. La señal asignada es **servicios sin plan**. Si no existe un dato confiable, la salida correcta no es inventar precisión: diseña el mecanismo de captura y declara la incertidumbre.

Al llegar a definir rto/rpo, compara tendencia, distribución y casos atípicos. Pregunta además si el indicador es *leading* o *lagging* y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; nunca convertirse en el objetivo que reemplaza al fenómeno.

### 4. BCP: trade-offs y efectos de segundo orden

**Definición:** plan de continuidad de negocio. Este concepto obliga a abandonar la idea de que **continuidad operacional** tiene una solución gratuita. Toda intervención consume autonomía, tiempo, caja, capacidad, atención, reputación o tolerancia al riesgo. Por eso, antes de diseñar estrategias y playbooks, se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

ISO — *ISO 22301 Business continuity management systems* aporta una lente sobre **sistema de gestión de continuidad y preparación ante disrupciones**. Úsala para construir una matriz `beneficio / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **ejercicios** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la necesidad de observar efectos laterales fuera del KPI principal.

Haz un *pre-mortem* de **continuidad operacional**: supone que la opción recomendada fracasó seis meses después y enumera tres mecanismos que podrían explicarlo. Al menos uno debe provenir de un efecto de segundo orden asociado a **BCP** y otro de una hipótesis del caso que nunca fue validada.

### 5. DR: gobernanza, límites e integración

**DR** se define como **recuperación de tecnología e infraestructura después de incidente** y cierra el circuito porque traduce análisis en responsabilidad. La pregunta ejecutiva es quién decide, quién ejecuta, quién debe ser consultado, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar.

James P. Womack & Daniel T. Jones — *Lean Thinking* se utiliza para estudiar **valor, flujo, pull, desperdicio y mejora continua** y contrastar la recomendación final. Al ejecutar ejercitar y corregir brechas, deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento. Esa trazabilidad protege contra el sesgo retrospectivo y mejora las revisiones posteriores.

La frontera de esta clase es explícita: **Continuidad total es imposible y costosa. Prioriza por impacto y tiempos; los objetivos deben estar aprobados por negocio, no elegidos solo por tecnología.**. Conviértela en una regla operativa: `si ocurre X → no aplicar automáticamente → consultar/escalar/revalidar`. Integrar **BIA**, **RTO**, **RPO**, **BCP** y **DR** significa poder explicar qué parte del diagnóstico sostiene la decisión y cuál sigue siendo una apuesta.

### 6. Integración: de conceptos a una decisión defendible

La síntesis de **continuidad operacional** no consiste en sumar cinco definiciones. Empieza por **BIA**, contrasta **RTO** con **RPO**, incorpora **BCP** como restricción o mecanismo y usa **DR** para cerrar el ciclo. Si el análisis no puede explicar cuál de esas piezas cambió la recomendación, todavía no hay comprensión transferible.

Aplica ahora la secuencia **1. identificar servicios críticos → 2. hacer BIA y dependencias → 3. definir RTO/RPO → 4. diseñar estrategias y playbooks → 5. ejercitar y corregir brechas**. Para cada paso conserva tres columnas: evidencia utilizada, alternativa descartada y razón. Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado y evita reescribir la historia después de conocer el desenlace.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla señala el lente que debes buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Nigel Slack & Alistair Brandon-Jones — *Operations Management* | capacidad, procesos, variabilidad, calidad y estrategia de operaciones | ¿Qué supuesto de **continuidad operacional** ayuda a desafiar? |
| Eliyahu M. Goldratt & Jeff Cox — *The Goal* | restricciones, throughput, inventario y pensamiento de flujo | ¿Qué supuesto de **continuidad operacional** ayuda a desafiar? |
| Jeffrey K. Liker — *The Toyota Way* | perspectiva de Operaciones aplicada al problema de la clase | ¿Qué supuesto de **continuidad operacional** ayuda a desafiar? |
| ISO — *ISO 22301 Business continuity management systems* | sistema de gestión de continuidad y preparación ante disrupciones | ¿Qué supuesto de **continuidad operacional** ayuda a desafiar? |
| James P. Womack & Daniel T. Jones — *Lean Thinking* | valor, flujo, pull, desperdicio y mejora continua | ¿Qué supuesto de **continuidad operacional** ayuda a desafiar? |

En **continuidad operacional**, la lectura se evalúa por **uso**, no por cantidad de páginas. La nota debe indicar qué tesis de las fuentes modifica tu lectura de **BIA**, qué evidencia del caso tensiona esa tesis y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación:** Un incendio deja inaccesible una oficina. Sistemas están en cloud, pero el proceso crítico depende de dos personas y firmas físicas guardadas en el lugar.

**Paso 1 — identificar servicios críticos.** La gerencia escribe primero el supuesto asociado a **BIA** y evita convertirlo en hecho. Luego busca **RTO alcanzado** para contrastarlo en el caso de **continuidad operacional**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 2 — hacer BIA y dependencias.** La gerencia escribe primero el supuesto asociado a **RTO** y evita convertirlo en hecho. Luego busca **RPO alcanzado** para contrastarlo en el caso de **continuidad operacional**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 3 — definir RTO/RPO.** La gerencia escribe primero el supuesto asociado a **RPO** y evita convertirlo en hecho. Luego busca **servicios sin plan** para contrastarlo en el caso de **continuidad operacional**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 4 — diseñar estrategias y playbooks.** La gerencia escribe primero el supuesto asociado a **BCP** y evita convertirlo en hecho. Luego busca **ejercicios** para contrastarlo en el caso de **continuidad operacional**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 5 — ejercitar y corregir brechas.** La gerencia escribe primero el supuesto asociado a **DR** y evita convertirlo en hecho. Luego busca **dependencias no documentadas** para contrastarlo en el caso de **continuidad operacional**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Síntesis del caso.** La recomendación debe terminar con responsable, fecha, evidencia de éxito y señal de stop. En **continuidad operacional**, omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo |
|---|---|---|---|
| **BIA** | análisis de impacto que prioriza procesos y tiempos críticos | Cuando RTO alcanzado es observable y accionable. | Sobrerreaccionar a una señal parcial. |
| **RTO** | tiempo objetivo para restaurar una capacidad | Cuando la primera explicación no distingue mecanismo o responsabilidad. | Convertir el concepto en etiqueta. |
| **Experimento/revisión** | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar eternamente y no decidir. |
| **Escalamiento** | Elevar autoridad o especialidad | Cuando hay derechos, capital material, regulación o irreversibilidad. | Delegar hacia arriba lo que sí corresponde decidir. |

**Frontera de aplicación:** Continuidad total es imposible y costosa. Prioriza por impacto y tiempos; los objetivos deben estar aprobados por negocio, no elegidos solo por tecnología.

## 🪜 De profesional a owner

| Nivel | Responsabilidad sobre continuidad operacional |
|---|---|
| **Profesional** | usa **continuidad operacional** para mejorar una contribución propia y explicar sus supuestos con evidencia. |
| **Jefe / Team Lead** | aplica **BIA** y **RTO** para coordinar personas sin sustituir conversación por métricas. |
| **Manager / Gerente** | conecta RTO alcanzado con capacidad, presupuesto, dependencias y riesgo interáreas. |
| **CEO / Director** | decide si continuidad operacional cambia estrategia, economía o riesgo de empresa y qué debe llegar al comité o directorio. |
| **Founder / Owner** | pregunta si la solución de continuidad operacional reduce dependencia del fundador, preserva caja y puede operar como sistema repetible. |

El cambio de nivel en **continuidad operacional** aumenta el número de personas, dinero, dependencias y consecuencias que quedan dentro de la decisión. Por eso la misma herramienta debe volverse más explícita en evidencia, gobernanza y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Un incendio deja inaccesible una oficina. Sistemas están en cloud, pero el proceso crítico depende de dos personas y firmas físicas guardadas en el lugar.

Entrega un **decision brief de continuidad operacional** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre personas, cliente, operación, caja y riesgo; (e) recomendación; (f) condición que haría cambiarla; (g) dueño y fecha de revisión. Utiliza al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica

1. Reconstruye el caso de **continuidad operacional** con una tabla `hecho / interpretación / hipótesis / decisión`.
2. Ejecuta **1. identificar servicios críticos → 2. hacer BIA y dependencias → 3. definir RTO/RPO → 4. diseñar estrategias y playbooks → 5. ejercitar y corregir brechas** y adjunta evidencia para cada transición entre pasos.
3. Calcula o documenta RTO alcanzado, RPO alcanzado; si no existe dato, diseña cómo obtenerlo.
4. Escribe una alternativa que contradiga tu preferencia inicial y haz un *pre-mortem* específico del caso.
5. Lee dos referencias, registra una coincidencia y una tensión, y modifica el brief si corresponde.
6. Repite la decisión desde el rol de CEO/owner: identifica qué cambia al aumentar el alcance y la irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar BIA y RTO como sinónimos | Se pierde la distinción entre “análisis de impacto que prioriza procesos y tiempos críticos” y “tiempo objetivo para restaurar una capacidad” | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por “ejercitar y corregir brechas” | Se saltó “identificar servicios críticos” y la solución llegó antes que el diagnóstico | Reconstruye la cadena 1. identificar servicios críticos → 2. hacer BIA y dependencias → 3. definir RTO/RPO → 4. diseñar estrategias y playbooks → 5. ejercitar y corregir brechas y marca el primer supuesto no demostrado. |
| Optimizar solo RTO alcanzado | La métrica local sustituyó al resultado del sistema | Contrástala con RPO alcanzado y explicita el costo de oportunidad. |
| Generalizar desde un caso favorable | Se confundió evidencia local con una regla universal sobre continuidad operacional | Continuidad total es imposible y costosa. Prioriza por impacto y tiempos; los objetivos deben estar aprobados por negocio, no elegidos solo por tecnología. |
| No fijar revisión | Una decisión sobre continuidad operacional se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de stop. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **BIA** y **RTO** usando un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **RPO** y qué observación obligaría a rechazar tu interpretación?
3. Aplica **identificar servicios críticos → hacer BIA y dependencias** al caso de la clase. ¿Qué dato todavía falta?
4. ¿Por qué **RTO alcanzado** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la tabla de lectura. ¿Dónde podrían llevar a recomendaciones distintas para **continuidad operacional**?
6. ¿Qué decisión equivocada podría producirse si se ignora este límite: **Continuidad total es imposible y costosa. Prioriza por impacto y tiempos; los objetivos deben estar aprobados por negocio, no elegidos solo por tecnología.**?

## 📥 Entregable

Guarda en `portfolio/094-continuidad-operacional/`:

- `operating-improvement-brief.md` con el problema específico de **continuidad operacional**, evidencia, alternativas, decisión y gobernanza;
- `reading-note.md` contrastando las fuentes de **continuidad operacional** con edición/páginas consultadas;
- `decision-journal.md` registrando los supuestos de **BIA**, confianza, responsable y revisión;
- `red-team.md` con la objeción más fuerte al caso **Un incendio deja inaccesible una oficina. Sistemas están en cloud, pero el proceso crítico depende de dos personas y firmas físicas guardadas en el lugar.** y el dato que podría invalidar la recomendación.

## 📗 Fuentes y verificación

- Nigel Slack & Alistair Brandon-Jones — *Operations Management*. **Uso en esta clase:** capacidad, procesos, variabilidad, calidad y estrategia de operaciones. Lectura selectiva: índice/capítulos pertinentes a **continuidad operacional**; registra edición y páginas consultadas.
- Eliyahu M. Goldratt & Jeff Cox — *The Goal*. **Uso en esta clase:** restricciones, throughput, inventario y pensamiento de flujo. Lectura selectiva: índice/capítulos pertinentes a **continuidad operacional**; registra edición y páginas consultadas.
- Jeffrey K. Liker — *The Toyota Way*. **Uso en esta clase:** perspectiva de Operaciones aplicada al problema de la clase. Lectura selectiva: índice/capítulos pertinentes a **continuidad operacional**; registra edición y páginas consultadas.
- ISO — *ISO 22301 Business continuity management systems*. **Uso en esta clase:** sistema de gestión de continuidad y preparación ante disrupciones. Lectura selectiva: índice/capítulos pertinentes a **continuidad operacional**; registra edición y páginas consultadas.
- James P. Womack & Daniel T. Jones — *Lean Thinking*. **Uso en esta clase:** valor, flujo, pull, desperdicio y mejora continua. Lectura selectiva: índice/capítulos pertinentes a **continuidad operacional**; registra edición y páginas consultadas.
- W. Edwards Deming — *Out of the Crisis*. **Uso en esta clase:** variación, sistemas, aprendizaje y responsabilidad gerencial por la calidad. Lectura selectiva: índice/capítulos pertinentes a **continuidad operacional**; registra edición y páginas consultadas.
- Susan A. Ambrose et al. — *How Learning Works*. Diseño de objetivos, práctica y feedback.
- Peter C. Brown, Henry L. Roediger III & Mark A. McDaniel — *Make It Stick*. Recuperación, elaboración y transferencia.
- Grant Wiggins & Jay McTighe — *Understanding by Design*. Diseño inverso desde desempeño observable.
- Anders Ericsson & Robert Pool — *Peak*. Práctica deliberada con criterios y retroalimentación.
- William Ellet — *The Case Study Handbook*. Análisis de problema/decisión, evidencia y recomendación.

> **Regla de fuentes para Continuidad operacional:** las obras anteriores estructuran las perspectivas de esta materia; cualquier norma, ley, impuesto o estándar vivo mencionado en **continuidad operacional** debe comprobarse nuevamente en su fuente primaria vigente. El desarrollo es original y no reproduce capítulos protegidos.
