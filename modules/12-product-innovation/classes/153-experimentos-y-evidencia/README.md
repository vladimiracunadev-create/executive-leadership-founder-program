# Clase 153 — Experimentos y evidencia

**Parte:** 12 — Producto e innovación  
**Nivel:** Etapa 3 — Manager → Gerente  
**Duración sugerida:** 150–180 minutos · **Estándar:** deep-class-v2

## 🎯 Propósito

Los experimentos de producto convierten incertidumbre en evidencia mediante hipótesis, tratamiento, comparación y criterio de decisión. Un A/B test es solo una forma; smoke tests, fake doors, concierge, prototipos y pilotos responden preguntas distintas. El diseño debe evitar confundir correlación con efecto causal.

La salida de esta parte es **convertir problemas de clientes en productos validados y outcomes medibles**. En esta clase, esa progresión se concreta al exigir que cada afirmación sobre **experimentos y evidencia** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

## 📚 Resultados de aprendizaje

Al finalizar podrás:

1. **Distinguir** `experiment`, `control`, `metric guardrail`, `sample size`, `external validity` mediante observables, no por memoria verbal.
2. **Explicar** por qué esas distinciones cambian una decisión de manager → gerente.
3. **Aplicar** la secuencia **1. formular hipótesis causal o conductual → 2. elegir diseño proporcional → 3. predefinir métrica y guardrails → 4. ejecutar sin cambiar reglas a mitad → 5. interpretar efecto incertidumbre y transferencia** conservando supuestos, alternativas y trazabilidad.
4. **Interpretar** primary metric, guardrail metrics, effect size sin confundir señal, explicación y causalidad.
5. **Resolver** el caso ejecutivo con al menos dos opciones plausibles y un criterio explícito de stop/revisión.
6. **Contrastar** dos obras de referencia y explicar dónde sus lentes son complementarias o entran en tensión.

## 🧭 Agenda

| Tramo | Evidencia de aprendizaje |
|---|---|
| 0–20 min | Recuperación: define experiment y control sin mirar la tabla; corrige con la fuente. |
| 20–70 min | Lectura guiada de conceptos + contraste de dos referencias. |
| 70–115 min | Ejemplo trabajado con primary metric y trazabilidad de supuestos. |
| 115–155 min | Caso ejecutivo: dos alternativas, trade-offs y decisión provisional. |
| 155–180 min | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar comprensión |
|---|---|---|
| **experiment** | intervención diseñada para aprender sobre una hipótesis | Distingue un hecho compatible y otro que lo refute. |
| **control** | condición de comparación que permite atribución | Distingue un hecho compatible y otro que lo refute. |
| **metric guardrail** | señal que no debe deteriorarse al optimizar otra | Distingue un hecho compatible y otro que lo refute. |
| **sample size** | tamaño requerido para detectar un efecto relevante con error controlado | Distingue un hecho compatible y otro que lo refute. |
| **external validity** | grado en que el aprendizaje se transfiere a otros contextos | Distingue un hecho compatible y otro que lo refute. |

## 🧠 Modelo mental

```text
1. formular hipótesis causal o conductual → 2. elegir diseño proporcional → 3. predefinir métrica y guardrails → 4. ejecutar sin cambiar reglas a mitad → 5. interpretar efecto incertidumbre y transferencia
```

La secuencia nace del problema de esta clase: **Los experimentos de producto convierten incertidumbre en evidencia mediante hipótesis, tratamiento, comparación y criterio de decisión. Un A/B test es solo una forma; smoke tests, fake doors, concierge, prototipos y pilotos responden preguntas distintas. El diseño debe evitar confundir correlación con efecto causal.** El método es útil mientras las condiciones permitan observar las señales requeridas. No elimina incertidumbre; la hace visible y obliga a decidir proporcionalmente a la evidencia. Límite principal: **No todo puede o debe randomizarse. Experimentos pequeños, B2B enterprise o cambios irreversibles requieren métodos alternativos y mucha cautela al atribuir causalidad.**

## 📖 Desarrollo

### 1. experiment: mecanismo central

**experiment** se entiende aquí como **intervención diseñada para aprender sobre una hipótesis**. Esta es la pieza causal o estructural desde la que se inicia **experimentos y evidencia**: antes de formular hipótesis causal o conductual, el gerente debe poder señalar qué cambia en el sistema si el concepto está presente y qué debería observar si no lo está. Una definición que no produce predicciones observables todavía es demasiado vaga para dirigir.

La lectura rectora de este bloque es Marty Cagan — *Inspired*. Su aporte se usa para examinar **equipos de producto, discovery, riesgos de producto y outcomes**. Aplica esa lente al caso sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **primary metric**; regístrala con periodo, unidad, población y baseline.

Relaciona el mecanismo con **control**. Si ambos cambian juntos, no concluyas causalidad automáticamente: identifica una tercera variable o mecanismo alternativo que también pueda explicar el patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. control: frontera conceptual y error de clasificación

**Definición operacional:** condición de comparación que permite atribución. Su valor está en distinguirlo de **experiment** y **metric guardrail**. En una decisión real, clasificar una situación en la categoría equivocada cambia la intervención: puedes asignar autoridad donde faltaba información, medir un output cuando debías observar un proceso o tratar una restricción como si fuera una preferencia.

Contrasta el problema con Teresa Torres — *Continuous Discovery Habits*, que aporta una mirada sobre **discovery continuo, oportunidades, experimentos y decisiones basadas en evidencia**. Formula dos mini-casos: uno que sí satisface la definición de **control** y otro que solo se parece superficialmente. Luego pregunta qué señal distinguiría ambos; para esta clase, **guardrail metrics** es una candidata, pero debe combinarse con evidencia cualitativa o documental cuando el fenómeno no sea directamente medible.

Antes de elegir diseño proporcional, registra explícitamente qué decisión sería errónea si esta frontera conceptual se ignora. Esa frase convierte el vocabulario en criterio gerencial.

### 3. metric guardrail: operacionalización y medición

**metric guardrail** significa **señal que no debe deteriorarse al optimizar otra**. El problema ya no es definirlo, sino **operacionalizarlo**: qué contar, durante qué ventana, con qué denominador, contra qué baseline y con qué segmentación. Una métrica útil conserva suficiente contexto para no confundir mejora local con mejora del sistema.

Eric Ries — *The Lean Startup* orienta este bloque mediante **build-measure-learn, MVP y aprendizaje validado**. Usa esa perspectiva para diseñar una ficha de medición: `señal → fórmula/criterio → fuente → frecuencia → owner → interpretación permitida → interpretación prohibida`. La señal asignada es **effect size**. Si no existe un dato confiable, la salida correcta no es inventar precisión: diseña el mecanismo de captura y declara la incertidumbre.

Al llegar a predefinir métrica y guardrails, compara tendencia, distribución y casos atípicos. Pregunta además si el indicador es *leading* o *lagging* y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; nunca convertirse en el objetivo que reemplaza al fenómeno.

### 4. sample size: trade-offs y efectos de segundo orden

**Definición:** tamaño requerido para detectar un efecto relevante con error controlado. Este concepto obliga a abandonar la idea de que **experimentos y evidencia** tiene una solución gratuita. Toda intervención consume autonomía, tiempo, caja, capacidad, atención, reputación o tolerancia al riesgo. Por eso, antes de ejecutar sin cambiar reglas a mitad, se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Rob Fitzpatrick — *The Mom Test* aporta una lente sobre **perspectiva de Customer discovery aplicada al problema de la clase**. Úsala para construir una matriz `beneficio / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **confidence interval** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la necesidad de observar efectos laterales fuera del KPI principal.

Haz un *pre-mortem* de **experimentos y evidencia**: supone que la opción recomendada fracasó seis meses después y enumera tres mecanismos que podrían explicarlo. Al menos uno debe provenir de un efecto de segundo orden asociado a **sample size** y otro de una hipótesis del caso que nunca fue validada.

### 5. external validity: gobernanza, límites e integración

**external validity** se define como **grado en que el aprendizaje se transfiere a otros contextos** y cierra el circuito porque traduce análisis en responsabilidad. La pregunta ejecutiva es quién decide, quién ejecuta, quién debe ser consultado, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar.

Clayton M. Christensen — *The Innovator's Dilemma* se utiliza para estudiar **perspectiva de Innovación aplicada al problema de la clase** y contrastar la recomendación final. Al ejecutar interpretar efecto incertidumbre y transferencia, deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento. Esa trazabilidad protege contra el sesgo retrospectivo y mejora las revisiones posteriores.

La frontera de esta clase es explícita: **No todo puede o debe randomizarse. Experimentos pequeños, B2B enterprise o cambios irreversibles requieren métodos alternativos y mucha cautela al atribuir causalidad.**. Conviértela en una regla operativa: `si ocurre X → no aplicar automáticamente → consultar/escalar/revalidar`. Integrar **experiment**, **control**, **metric guardrail**, **sample size** y **external validity** significa poder explicar qué parte del diagnóstico sostiene la decisión y cuál sigue siendo una apuesta.

### 6. Integración: de conceptos a una decisión defendible

La síntesis de **experimentos y evidencia** no consiste en sumar cinco definiciones. Empieza por **experiment**, contrasta **control** con **metric guardrail**, incorpora **sample size** como restricción o mecanismo y usa **external validity** para cerrar el ciclo. Si el análisis no puede explicar cuál de esas piezas cambió la recomendación, todavía no hay comprensión transferible.

Aplica ahora la secuencia **1. formular hipótesis causal o conductual → 2. elegir diseño proporcional → 3. predefinir métrica y guardrails → 4. ejecutar sin cambiar reglas a mitad → 5. interpretar efecto incertidumbre y transferencia**. Para cada paso conserva tres columnas: evidencia utilizada, alternativa descartada y razón. Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado y evita reescribir la historia después de conocer el desenlace.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla señala el lente que debes buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Marty Cagan — *Inspired* | equipos de producto, discovery, riesgos de producto y outcomes | ¿Qué supuesto de **experimentos y evidencia** ayuda a desafiar? |
| Teresa Torres — *Continuous Discovery Habits* | discovery continuo, oportunidades, experimentos y decisiones basadas en evidencia | ¿Qué supuesto de **experimentos y evidencia** ayuda a desafiar? |
| Eric Ries — *The Lean Startup* | build-measure-learn, MVP y aprendizaje validado | ¿Qué supuesto de **experimentos y evidencia** ayuda a desafiar? |
| Rob Fitzpatrick — *The Mom Test* | perspectiva de Customer discovery aplicada al problema de la clase | ¿Qué supuesto de **experimentos y evidencia** ayuda a desafiar? |
| Clayton M. Christensen — *The Innovator's Dilemma* | perspectiva de Innovación aplicada al problema de la clase | ¿Qué supuesto de **experimentos y evidencia** ayuda a desafiar? |

En **experimentos y evidencia**, la lectura se evalúa por **uso**, no por cantidad de páginas. La nota debe indicar qué tesis de las fuentes modifica tu lectura de **experiment**, qué evidencia del caso tensiona esa tesis y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación:** Un A/B test sube clics 12%, pero también aumenta cancelaciones y el grupo experimental recibió una campaña distinta. El equipo declara victoria mirando solo CTR.

**Paso 1 — formular hipótesis causal o conductual.** La gerencia escribe primero el supuesto asociado a **experiment** y evita convertirlo en hecho. Luego busca **primary metric** para contrastarlo en el caso de **experimentos y evidencia**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 2 — elegir diseño proporcional.** La gerencia escribe primero el supuesto asociado a **control** y evita convertirlo en hecho. Luego busca **guardrail metrics** para contrastarlo en el caso de **experimentos y evidencia**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 3 — predefinir métrica y guardrails.** La gerencia escribe primero el supuesto asociado a **metric guardrail** y evita convertirlo en hecho. Luego busca **effect size** para contrastarlo en el caso de **experimentos y evidencia**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 4 — ejecutar sin cambiar reglas a mitad.** La gerencia escribe primero el supuesto asociado a **sample size** y evita convertirlo en hecho. Luego busca **confidence interval** para contrastarlo en el caso de **experimentos y evidencia**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 5 — interpretar efecto incertidumbre y transferencia.** La gerencia escribe primero el supuesto asociado a **external validity** y evita convertirlo en hecho. Luego busca **segment heterogeneity** para contrastarlo en el caso de **experimentos y evidencia**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Síntesis del caso.** La recomendación debe terminar con responsable, fecha, evidencia de éxito y señal de stop. En **experimentos y evidencia**, omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo |
|---|---|---|---|
| **experiment** | intervención diseñada para aprender sobre una hipótesis | Cuando primary metric es observable y accionable. | Sobrerreaccionar a una señal parcial. |
| **control** | condición de comparación que permite atribución | Cuando la primera explicación no distingue mecanismo o responsabilidad. | Convertir el concepto en etiqueta. |
| **Experimento/revisión** | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar eternamente y no decidir. |
| **Escalamiento** | Elevar autoridad o especialidad | Cuando hay derechos, capital material, regulación o irreversibilidad. | Delegar hacia arriba lo que sí corresponde decidir. |

**Frontera de aplicación:** No todo puede o debe randomizarse. Experimentos pequeños, B2B enterprise o cambios irreversibles requieren métodos alternativos y mucha cautela al atribuir causalidad.

## 🪜 De profesional a owner

| Nivel | Responsabilidad sobre experimentos y evidencia |
|---|---|
| **Profesional** | usa **experimentos y evidencia** para mejorar una contribución propia y explicar sus supuestos con evidencia. |
| **Jefe / Team Lead** | aplica **experiment** y **control** para coordinar personas sin sustituir conversación por métricas. |
| **Manager / Gerente** | conecta primary metric con capacidad, presupuesto, dependencias y riesgo interáreas. |
| **CEO / Director** | decide si experimentos y evidencia cambia estrategia, economía o riesgo de empresa y qué debe llegar al comité o directorio. |
| **Founder / Owner** | pregunta si la solución de experimentos y evidencia reduce dependencia del fundador, preserva caja y puede operar como sistema repetible. |

El cambio de nivel en **experimentos y evidencia** aumenta el número de personas, dinero, dependencias y consecuencias que quedan dentro de la decisión. Por eso la misma herramienta debe volverse más explícita en evidencia, gobernanza y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Un A/B test sube clics 12%, pero también aumenta cancelaciones y el grupo experimental recibió una campaña distinta. El equipo declara victoria mirando solo CTR.

Entrega un **decision brief de experimentos y evidencia** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre personas, cliente, operación, caja y riesgo; (e) recomendación; (f) condición que haría cambiarla; (g) dueño y fecha de revisión. Utiliza al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica

1. Reconstruye el caso de **experimentos y evidencia** con una tabla `hecho / interpretación / hipótesis / decisión`.
2. Ejecuta **1. formular hipótesis causal o conductual → 2. elegir diseño proporcional → 3. predefinir métrica y guardrails → 4. ejecutar sin cambiar reglas a mitad → 5. interpretar efecto incertidumbre y transferencia** y adjunta evidencia para cada transición entre pasos.
3. Calcula o documenta primary metric, guardrail metrics; si no existe dato, diseña cómo obtenerlo.
4. Escribe una alternativa que contradiga tu preferencia inicial y haz un *pre-mortem* específico del caso.
5. Lee dos referencias, registra una coincidencia y una tensión, y modifica el brief si corresponde.
6. Repite la decisión desde el rol de CEO/owner: identifica qué cambia al aumentar el alcance y la irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar experiment y control como sinónimos | Se pierde la distinción entre “intervención diseñada para aprender sobre una hipótesis” y “condición de comparación que permite atribución” | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por “interpretar efecto incertidumbre y transferencia” | Se saltó “formular hipótesis causal o conductual” y la solución llegó antes que el diagnóstico | Reconstruye la cadena 1. formular hipótesis causal o conductual → 2. elegir diseño proporcional → 3. predefinir métrica y guardrails → 4. ejecutar sin cambiar reglas a mitad → 5. interpretar efecto incertidumbre y transferencia y marca el primer supuesto no demostrado. |
| Optimizar solo primary metric | La métrica local sustituyó al resultado del sistema | Contrástala con guardrail metrics y explicita el costo de oportunidad. |
| Generalizar desde un caso favorable | Se confundió evidencia local con una regla universal sobre experimentos y evidencia | No todo puede o debe randomizarse. Experimentos pequeños, B2B enterprise o cambios irreversibles requieren métodos alternativos y mucha cautela al atribuir causalidad. |
| No fijar revisión | Una decisión sobre experimentos y evidencia se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de stop. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **experiment** y **control** usando un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **metric guardrail** y qué observación obligaría a rechazar tu interpretación?
3. Aplica **formular hipótesis causal o conductual → elegir diseño proporcional** al caso de la clase. ¿Qué dato todavía falta?
4. ¿Por qué **primary metric** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la tabla de lectura. ¿Dónde podrían llevar a recomendaciones distintas para **experimentos y evidencia**?
6. ¿Qué decisión equivocada podría producirse si se ignora este límite: **No todo puede o debe randomizarse. Experimentos pequeños, B2B enterprise o cambios irreversibles requieren métodos alternativos y mucha cautela al atribuir causalidad.**?

## 📥 Entregable

Guarda en `portfolio/153-experimentos-y-evidencia/`:

- `product-evidence-brief.md` con el problema específico de **experimentos y evidencia**, evidencia, alternativas, decisión y gobernanza;
- `reading-note.md` contrastando las fuentes de **experimentos y evidencia** con edición/páginas consultadas;
- `decision-journal.md` registrando los supuestos de **experiment**, confianza, responsable y revisión;
- `red-team.md` con la objeción más fuerte al caso **Un A/B test sube clics 12%, pero también aumenta cancelaciones y el grupo experimental recibió una campaña distinta. El equipo declara victoria mirando solo CTR.** y el dato que podría invalidar la recomendación.

## 📗 Fuentes y verificación

- Marty Cagan — *Inspired*. **Uso en esta clase:** equipos de producto, discovery, riesgos de producto y outcomes. Lectura selectiva: índice/capítulos pertinentes a **experimentos y evidencia**; registra edición y páginas consultadas.
- Teresa Torres — *Continuous Discovery Habits*. **Uso en esta clase:** discovery continuo, oportunidades, experimentos y decisiones basadas en evidencia. Lectura selectiva: índice/capítulos pertinentes a **experimentos y evidencia**; registra edición y páginas consultadas.
- Eric Ries — *The Lean Startup*. **Uso en esta clase:** build-measure-learn, MVP y aprendizaje validado. Lectura selectiva: índice/capítulos pertinentes a **experimentos y evidencia**; registra edición y páginas consultadas.
- Rob Fitzpatrick — *The Mom Test*. **Uso en esta clase:** perspectiva de Customer discovery aplicada al problema de la clase. Lectura selectiva: índice/capítulos pertinentes a **experimentos y evidencia**; registra edición y páginas consultadas.
- Clayton M. Christensen — *The Innovator's Dilemma*. **Uso en esta clase:** perspectiva de Innovación aplicada al problema de la clase. Lectura selectiva: índice/capítulos pertinentes a **experimentos y evidencia**; registra edición y páginas consultadas.
- David J. Bland & Alexander Osterwalder — *Testing Business Ideas*. **Uso en esta clase:** hipótesis de negocio, experimentos, evidencia y reducción de riesgo. Lectura selectiva: índice/capítulos pertinentes a **experimentos y evidencia**; registra edición y páginas consultadas.
- Susan A. Ambrose et al. — *How Learning Works*. Diseño de objetivos, práctica y feedback.
- Peter C. Brown, Henry L. Roediger III & Mark A. McDaniel — *Make It Stick*. Recuperación, elaboración y transferencia.
- Grant Wiggins & Jay McTighe — *Understanding by Design*. Diseño inverso desde desempeño observable.
- Anders Ericsson & Robert Pool — *Peak*. Práctica deliberada con criterios y retroalimentación.
- William Ellet — *The Case Study Handbook*. Análisis de problema/decisión, evidencia y recomendación.

> **Regla de fuentes para Experimentos y evidencia:** las obras anteriores estructuran las perspectivas de esta materia; cualquier norma, ley, impuesto o estándar vivo mencionado en **experimentos y evidencia** debe comprobarse nuevamente en su fuente primaria vigente. El desarrollo es original y no reproduce capítulos protegidos.
