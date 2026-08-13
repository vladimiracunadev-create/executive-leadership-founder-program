# Clase 086 — Mapeo de procesos end-to-end

**Parte:** 07 — Operaciones, procesos y calidad  
**Nivel:** Etapa 2 — Jefe → Manager  
**Duración sugerida:** 150–180 minutos · **Estándar:** deep-class-v2

## 🎯 Propósito

Mapear procesos end-to-end sigue el resultado desde la demanda del cliente hasta su cierre, atravesando silos. El mapa debe mostrar handoffs, esperas, decisiones, rework y sistemas, porque la mayoría de demoras vive entre funciones más que dentro de una tarea individual.

La salida de esta parte es **operar procesos end-to-end con capacidad, calidad, continuidad y mejora**. En esta clase, esa progresión se concreta al exigir que cada afirmación sobre **mapeo de procesos end-to-end** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

## 📚 Resultados de aprendizaje

Al finalizar podrás:

1. **Distinguir** `end-to-end process`, `handoff`, `touch time`, `wait time`, `rework` mediante observables, no por memoria verbal.
2. **Explicar** por qué esas distinciones cambian una decisión de jefe → manager.
3. **Aplicar** la secuencia **1. definir inicio, fin y cliente → 2. recorrer casos reales → 3. registrar pasos, handoffs y tiempos → 4. marcar rework y decisiones → 5. calcular lead time versus touch time** conservando supuestos, alternativas y trazabilidad.
4. **Interpretar** lead time, touch-time ratio, handoffs sin confundir señal, explicación y causalidad.
5. **Resolver** el caso ejecutivo con al menos dos opciones plausibles y un criterio explícito de stop/revisión.
6. **Contrastar** dos obras de referencia y explicar dónde sus lentes son complementarias o entran en tensión.

## 🧭 Agenda

| Tramo | Evidencia de aprendizaje |
|---|---|
| 0–20 min | Recuperación: define end-to-end process y handoff sin mirar la tabla; corrige con la fuente. |
| 20–70 min | Lectura guiada de conceptos + contraste de dos referencias. |
| 70–115 min | Ejemplo trabajado con lead time y trazabilidad de supuestos. |
| 115–155 min | Caso ejecutivo: dos alternativas, trade-offs y decisión provisional. |
| 155–180 min | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar comprensión |
|---|---|---|
| **end-to-end process** | flujo completo que produce un outcome para un cliente interno o externo | Distingue un hecho compatible y otro que lo refute. |
| **handoff** | transferencia entre roles o sistemas | Distingue un hecho compatible y otro que lo refute. |
| **touch time** | tiempo de trabajo activo | Distingue un hecho compatible y otro que lo refute. |
| **wait time** | tiempo sin procesamiento | Distingue un hecho compatible y otro que lo refute. |
| **rework** | trabajo repetido por error, cambio o criterio incumplido | Distingue un hecho compatible y otro que lo refute. |

## 🧠 Modelo mental

```text
1. definir inicio, fin y cliente → 2. recorrer casos reales → 3. registrar pasos, handoffs y tiempos → 4. marcar rework y decisiones → 5. calcular lead time versus touch time
```

La secuencia nace del problema de esta clase: **Mapear procesos end-to-end sigue el resultado desde la demanda del cliente hasta su cierre, atravesando silos. El mapa debe mostrar handoffs, esperas, decisiones, rework y sistemas, porque la mayoría de demoras vive entre funciones más que dentro de una tarea individual.** El método es útil mientras las condiciones permitan observar las señales requeridas. No elimina incertidumbre; la hace visible y obliga a decidir proporcionalmente a la evidencia. Límite principal: **Un mapa detallado no cambia nada por sí mismo. Debe terminar en hipótesis de mejora y owner; evita documentar cada excepción antes de entender el flujo dominante.**

## 📖 Desarrollo

### 1. end-to-end process: mecanismo central

**end-to-end process** se entiende aquí como **flujo completo que produce un outcome para un cliente interno o externo**. Esta es la pieza causal o estructural desde la que se inicia **mapeo de procesos end-to-end**: antes de definir inicio, fin y cliente, el gerente debe poder señalar qué cambia en el sistema si el concepto está presente y qué debería observar si no lo está. Una definición que no produce predicciones observables todavía es demasiado vaga para dirigir.

La lectura rectora de este bloque es Nigel Slack & Alistair Brandon-Jones — *Operations Management*. Su aporte se usa para examinar **capacidad, procesos, variabilidad, calidad y estrategia de operaciones**. Aplica esa lente al caso sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **lead time**; regístrala con periodo, unidad, población y baseline.

Relaciona el mecanismo con **handoff**. Si ambos cambian juntos, no concluyas causalidad automáticamente: identifica una tercera variable o mecanismo alternativo que también pueda explicar el patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. handoff: frontera conceptual y error de clasificación

**Definición operacional:** transferencia entre roles o sistemas. Su valor está en distinguirlo de **end-to-end process** y **touch time**. En una decisión real, clasificar una situación en la categoría equivocada cambia la intervención: puedes asignar autoridad donde faltaba información, medir un output cuando debías observar un proceso o tratar una restricción como si fuera una preferencia.

Contrasta el problema con Eliyahu M. Goldratt & Jeff Cox — *The Goal*, que aporta una mirada sobre **restricciones, throughput, inventario y pensamiento de flujo**. Formula dos mini-casos: uno que sí satisface la definición de **handoff** y otro que solo se parece superficialmente. Luego pregunta qué señal distinguiría ambos; para esta clase, **touch-time ratio** es una candidata, pero debe combinarse con evidencia cualitativa o documental cuando el fenómeno no sea directamente medible.

Antes de recorrer casos reales, registra explícitamente qué decisión sería errónea si esta frontera conceptual se ignora. Esa frase convierte el vocabulario en criterio gerencial.

### 3. touch time: operacionalización y medición

**touch time** significa **tiempo de trabajo activo**. El problema ya no es definirlo, sino **operacionalizarlo**: qué contar, durante qué ventana, con qué denominador, contra qué baseline y con qué segmentación. Una métrica útil conserva suficiente contexto para no confundir mejora local con mejora del sistema.

ISO — *ISO 9001 Quality management systems* orienta este bloque mediante **gestión de calidad basada en procesos, evidencia y mejora**. Usa esa perspectiva para diseñar una ficha de medición: `señal → fórmula/criterio → fuente → frecuencia → owner → interpretación permitida → interpretación prohibida`. La señal asignada es **handoffs**. Si no existe un dato confiable, la salida correcta no es inventar precisión: diseña el mecanismo de captura y declara la incertidumbre.

Al llegar a registrar pasos, handoffs y tiempos, compara tendencia, distribución y casos atípicos. Pregunta además si el indicador es *leading* o *lagging* y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; nunca convertirse en el objetivo que reemplaza al fenómeno.

### 4. wait time: trade-offs y efectos de segundo orden

**Definición:** tiempo sin procesamiento. Este concepto obliga a abandonar la idea de que **mapeo de procesos end-to-end** tiene una solución gratuita. Toda intervención consume autonomía, tiempo, caja, capacidad, atención, reputación o tolerancia al riesgo. Por eso, antes de marcar rework y decisiones, se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

James P. Womack & Daniel T. Jones — *Lean Thinking* aporta una lente sobre **valor, flujo, pull, desperdicio y mejora continua**. Úsala para construir una matriz `beneficio / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **rework** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la necesidad de observar efectos laterales fuera del KPI principal.

Haz un *pre-mortem* de **mapeo de procesos end-to-end**: supone que la opción recomendada fracasó seis meses después y enumera tres mecanismos que podrían explicarlo. Al menos uno debe provenir de un efecto de segundo orden asociado a **wait time** y otro de una hipótesis del caso que nunca fue validada.

### 5. rework: gobernanza, límites e integración

**rework** se define como **trabajo repetido por error, cambio o criterio incumplido** y cierra el circuito porque traduce análisis en responsabilidad. La pregunta ejecutiva es quién decide, quién ejecuta, quién debe ser consultado, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar.

Geary A. Rummler & Alan P. Brache — *Improving Performance* se utiliza para estudiar **perspectiva de Procesos aplicada al problema de la clase** y contrastar la recomendación final. Al ejecutar calcular lead time versus touch time, deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento. Esa trazabilidad protege contra el sesgo retrospectivo y mejora las revisiones posteriores.

La frontera de esta clase es explícita: **Un mapa detallado no cambia nada por sí mismo. Debe terminar en hipótesis de mejora y owner; evita documentar cada excepción antes de entender el flujo dominante.**. Conviértela en una regla operativa: `si ocurre X → no aplicar automáticamente → consultar/escalar/revalidar`. Integrar **end-to-end process**, **handoff**, **touch time**, **wait time** y **rework** significa poder explicar qué parte del diagnóstico sostiene la decisión y cuál sigue siendo una apuesta.

### 6. Integración: de conceptos a una decisión defendible

La síntesis de **mapeo de procesos end-to-end** no consiste en sumar cinco definiciones. Empieza por **end-to-end process**, contrasta **handoff** con **touch time**, incorpora **wait time** como restricción o mecanismo y usa **rework** para cerrar el ciclo. Si el análisis no puede explicar cuál de esas piezas cambió la recomendación, todavía no hay comprensión transferible.

Aplica ahora la secuencia **1. definir inicio, fin y cliente → 2. recorrer casos reales → 3. registrar pasos, handoffs y tiempos → 4. marcar rework y decisiones → 5. calcular lead time versus touch time**. Para cada paso conserva tres columnas: evidencia utilizada, alternativa descartada y razón. Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado y evita reescribir la historia después de conocer el desenlace.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla señala el lente que debes buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Nigel Slack & Alistair Brandon-Jones — *Operations Management* | capacidad, procesos, variabilidad, calidad y estrategia de operaciones | ¿Qué supuesto de **mapeo de procesos end-to-end** ayuda a desafiar? |
| Eliyahu M. Goldratt & Jeff Cox — *The Goal* | restricciones, throughput, inventario y pensamiento de flujo | ¿Qué supuesto de **mapeo de procesos end-to-end** ayuda a desafiar? |
| ISO — *ISO 9001 Quality management systems* | gestión de calidad basada en procesos, evidencia y mejora | ¿Qué supuesto de **mapeo de procesos end-to-end** ayuda a desafiar? |
| James P. Womack & Daniel T. Jones — *Lean Thinking* | valor, flujo, pull, desperdicio y mejora continua | ¿Qué supuesto de **mapeo de procesos end-to-end** ayuda a desafiar? |
| Geary A. Rummler & Alan P. Brache — *Improving Performance* | perspectiva de Procesos aplicada al problema de la clase | ¿Qué supuesto de **mapeo de procesos end-to-end** ayuda a desafiar? |

En **mapeo de procesos end-to-end**, la lectura se evalúa por **uso**, no por cantidad de páginas. La nota debe indicar qué tesis de las fuentes modifica tu lectura de **end-to-end process**, qué evidencia del caso tensiona esa tesis y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación:** Emitir una propuesta tarda nueve días aunque el trabajo activo suma tres horas. La solicitud cruza ventas, legal, finanzas y dirección con esperas no visibles.

**Paso 1 — definir inicio, fin y cliente.** La gerencia escribe primero el supuesto asociado a **end-to-end process** y evita convertirlo en hecho. Luego busca **lead time** para contrastarlo en el caso de **mapeo de procesos end-to-end**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 2 — recorrer casos reales.** La gerencia escribe primero el supuesto asociado a **handoff** y evita convertirlo en hecho. Luego busca **touch-time ratio** para contrastarlo en el caso de **mapeo de procesos end-to-end**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 3 — registrar pasos, handoffs y tiempos.** La gerencia escribe primero el supuesto asociado a **touch time** y evita convertirlo en hecho. Luego busca **handoffs** para contrastarlo en el caso de **mapeo de procesos end-to-end**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 4 — marcar rework y decisiones.** La gerencia escribe primero el supuesto asociado a **wait time** y evita convertirlo en hecho. Luego busca **rework** para contrastarlo en el caso de **mapeo de procesos end-to-end**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 5 — calcular lead time versus touch time.** La gerencia escribe primero el supuesto asociado a **rework** y evita convertirlo en hecho. Luego busca **queue time** para contrastarlo en el caso de **mapeo de procesos end-to-end**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Síntesis del caso.** La recomendación debe terminar con responsable, fecha, evidencia de éxito y señal de stop. En **mapeo de procesos end-to-end**, omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo |
|---|---|---|---|
| **end-to-end process** | flujo completo que produce un outcome para un cliente interno o externo | Cuando lead time es observable y accionable. | Sobrerreaccionar a una señal parcial. |
| **handoff** | transferencia entre roles o sistemas | Cuando la primera explicación no distingue mecanismo o responsabilidad. | Convertir el concepto en etiqueta. |
| **Experimento/revisión** | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar eternamente y no decidir. |
| **Escalamiento** | Elevar autoridad o especialidad | Cuando hay derechos, capital material, regulación o irreversibilidad. | Delegar hacia arriba lo que sí corresponde decidir. |

**Frontera de aplicación:** Un mapa detallado no cambia nada por sí mismo. Debe terminar en hipótesis de mejora y owner; evita documentar cada excepción antes de entender el flujo dominante.

## 🪜 De profesional a owner

| Nivel | Responsabilidad sobre mapeo de procesos end-to-end |
|---|---|
| **Profesional** | usa **mapeo de procesos end-to-end** para mejorar una contribución propia y explicar sus supuestos con evidencia. |
| **Jefe / Team Lead** | aplica **end-to-end process** y **handoff** para coordinar personas sin sustituir conversación por métricas. |
| **Manager / Gerente** | conecta lead time con capacidad, presupuesto, dependencias y riesgo interáreas. |
| **CEO / Director** | decide si mapeo de procesos end-to-end cambia estrategia, economía o riesgo de empresa y qué debe llegar al comité o directorio. |
| **Founder / Owner** | pregunta si la solución de mapeo de procesos end-to-end reduce dependencia del fundador, preserva caja y puede operar como sistema repetible. |

El cambio de nivel en **mapeo de procesos end-to-end** aumenta el número de personas, dinero, dependencias y consecuencias que quedan dentro de la decisión. Por eso la misma herramienta debe volverse más explícita en evidencia, gobernanza y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Emitir una propuesta tarda nueve días aunque el trabajo activo suma tres horas. La solicitud cruza ventas, legal, finanzas y dirección con esperas no visibles.

Entrega un **decision brief de mapeo de procesos end-to-end** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre personas, cliente, operación, caja y riesgo; (e) recomendación; (f) condición que haría cambiarla; (g) dueño y fecha de revisión. Utiliza al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica

1. Reconstruye el caso de **mapeo de procesos end-to-end** con una tabla `hecho / interpretación / hipótesis / decisión`.
2. Ejecuta **1. definir inicio, fin y cliente → 2. recorrer casos reales → 3. registrar pasos, handoffs y tiempos → 4. marcar rework y decisiones → 5. calcular lead time versus touch time** y adjunta evidencia para cada transición entre pasos.
3. Calcula o documenta lead time, touch-time ratio; si no existe dato, diseña cómo obtenerlo.
4. Escribe una alternativa que contradiga tu preferencia inicial y haz un *pre-mortem* específico del caso.
5. Lee dos referencias, registra una coincidencia y una tensión, y modifica el brief si corresponde.
6. Repite la decisión desde el rol de CEO/owner: identifica qué cambia al aumentar el alcance y la irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar end-to-end process y handoff como sinónimos | Se pierde la distinción entre “flujo completo que produce un outcome para un cliente interno o externo” y “transferencia entre roles o sistemas” | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por “calcular lead time versus touch time” | Se saltó “definir inicio, fin y cliente” y la solución llegó antes que el diagnóstico | Reconstruye la cadena 1. definir inicio, fin y cliente → 2. recorrer casos reales → 3. registrar pasos, handoffs y tiempos → 4. marcar rework y decisiones → 5. calcular lead time versus touch time y marca el primer supuesto no demostrado. |
| Optimizar solo lead time | La métrica local sustituyó al resultado del sistema | Contrástala con touch-time ratio y explicita el costo de oportunidad. |
| Generalizar desde un caso favorable | Se confundió evidencia local con una regla universal sobre mapeo de procesos end-to-end | Un mapa detallado no cambia nada por sí mismo. Debe terminar en hipótesis de mejora y owner; evita documentar cada excepción antes de entender el flujo dominante. |
| No fijar revisión | Una decisión sobre mapeo de procesos end-to-end se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de stop. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **end-to-end process** y **handoff** usando un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **touch time** y qué observación obligaría a rechazar tu interpretación?
3. Aplica **definir inicio, fin y cliente → recorrer casos reales** al caso de la clase. ¿Qué dato todavía falta?
4. ¿Por qué **lead time** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la tabla de lectura. ¿Dónde podrían llevar a recomendaciones distintas para **mapeo de procesos end-to-end**?
6. ¿Qué decisión equivocada podría producirse si se ignora este límite: **Un mapa detallado no cambia nada por sí mismo. Debe terminar en hipótesis de mejora y owner; evita documentar cada excepción antes de entender el flujo dominante.**?

## 📥 Entregable

Guarda en `portfolio/086-mapeo-de-procesos-end-to-end/`:

- `operating-improvement-brief.md` con el problema específico de **mapeo de procesos end-to-end**, evidencia, alternativas, decisión y gobernanza;
- `reading-note.md` contrastando las fuentes de **mapeo de procesos end-to-end** con edición/páginas consultadas;
- `decision-journal.md` registrando los supuestos de **end-to-end process**, confianza, responsable y revisión;
- `red-team.md` con la objeción más fuerte al caso **Emitir una propuesta tarda nueve días aunque el trabajo activo suma tres horas. La solicitud cruza ventas, legal, finanzas y dirección con esperas no visibles.** y el dato que podría invalidar la recomendación.

## 📗 Fuentes y verificación

- Nigel Slack & Alistair Brandon-Jones — *Operations Management*. **Uso en esta clase:** capacidad, procesos, variabilidad, calidad y estrategia de operaciones. Lectura selectiva: índice/capítulos pertinentes a **mapeo de procesos end-to-end**; registra edición y páginas consultadas.
- Eliyahu M. Goldratt & Jeff Cox — *The Goal*. **Uso en esta clase:** restricciones, throughput, inventario y pensamiento de flujo. Lectura selectiva: índice/capítulos pertinentes a **mapeo de procesos end-to-end**; registra edición y páginas consultadas.
- ISO — *ISO 9001 Quality management systems*. **Uso en esta clase:** gestión de calidad basada en procesos, evidencia y mejora. Lectura selectiva: índice/capítulos pertinentes a **mapeo de procesos end-to-end**; registra edición y páginas consultadas.
- James P. Womack & Daniel T. Jones — *Lean Thinking*. **Uso en esta clase:** valor, flujo, pull, desperdicio y mejora continua. Lectura selectiva: índice/capítulos pertinentes a **mapeo de procesos end-to-end**; registra edición y páginas consultadas.
- Geary A. Rummler & Alan P. Brache — *Improving Performance*. **Uso en esta clase:** perspectiva de Procesos aplicada al problema de la clase. Lectura selectiva: índice/capítulos pertinentes a **mapeo de procesos end-to-end**; registra edición y páginas consultadas.
- W. Edwards Deming — *Out of the Crisis*. **Uso en esta clase:** variación, sistemas, aprendizaje y responsabilidad gerencial por la calidad. Lectura selectiva: índice/capítulos pertinentes a **mapeo de procesos end-to-end**; registra edición y páginas consultadas.
- Susan A. Ambrose et al. — *How Learning Works*. Diseño de objetivos, práctica y feedback.
- Peter C. Brown, Henry L. Roediger III & Mark A. McDaniel — *Make It Stick*. Recuperación, elaboración y transferencia.
- Grant Wiggins & Jay McTighe — *Understanding by Design*. Diseño inverso desde desempeño observable.
- Anders Ericsson & Robert Pool — *Peak*. Práctica deliberada con criterios y retroalimentación.
- William Ellet — *The Case Study Handbook*. Análisis de problema/decisión, evidencia y recomendación.

> **Regla de fuentes para Mapeo de procesos end-to-end:** las obras anteriores estructuran las perspectivas de esta materia; cualquier norma, ley, impuesto o estándar vivo mencionado en **mapeo de procesos end-to-end** debe comprobarse nuevamente en su fuente primaria vigente. El desarrollo es original y no reproduce capítulos protegidos.
