# Clase 248 — MVP y concierge tests

**Parte:** 20 — Founder y creación de empresas  
**Nivel:** Etapa 6 — Founder  
**Duración sugerida:** 150–180 minutos · **Estándar:** deep-class-v2

## 🎯 Propósito

MVP y concierge tests permiten aprender el flujo de valor manualmente antes de automatizar. El founder actúa como sistema para descubrir excepciones, lenguaje, datos y willingness to pay; luego automatiza las partes repetibles con mejor evidencia.

La salida de esta parte es **descubrir, validar y lanzar una empresa antes de escalarla**. En esta clase, esa progresión se concreta al exigir que cada afirmación sobre **mVP y concierge tests** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

## 📚 Resultados de aprendizaje

Al finalizar podrás:

1. **Distinguir** `concierge MVP`, `Wizard of Oz`, `manual-first`, `service blueprint`, `automation candidate` mediante observables, no por memoria verbal.
2. **Explicar** por qué esas distinciones cambian una decisión de founder.
3. **Aplicar** la secuencia **1. definir outcome a entregar → 2. operar manualmente para pocos clientes → 3. registrar steps y exceptions → 4. medir value y willingness → 5. automatizar solo patrón estable** conservando supuestos, alternativas y trazabilidad.
4. **Interpretar** time-to-value, manual hours per customer, exception rate sin confundir señal, explicación y causalidad.
5. **Resolver** el caso ejecutivo con al menos dos opciones plausibles y un criterio explícito de stop/revisión.
6. **Contrastar** dos obras de referencia y explicar dónde sus lentes son complementarias o entran en tensión.

## 🧭 Agenda

| Tramo | Evidencia de aprendizaje |
|---|---|
| 0–20 min | Recuperación: define concierge MVP y Wizard of Oz sin mirar la tabla; corrige con la fuente. |
| 20–70 min | Lectura guiada de conceptos + contraste de dos referencias. |
| 70–115 min | Ejemplo trabajado con time-to-value y trazabilidad de supuestos. |
| 115–155 min | Caso ejecutivo: dos alternativas, trade-offs y decisión provisional. |
| 155–180 min | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar comprensión |
|---|---|---|
| **concierge MVP** | servicio manual que entrega valor prometido a pocos clientes | Distingue un hecho compatible y otro que lo refute. |
| **Wizard of Oz** | interfaz que aparenta automatización mientras procesos internos son manuales | Distingue un hecho compatible y otro que lo refute. |
| **manual-first** | estrategia de aprendizaje que pospone automatización | Distingue un hecho compatible y otro que lo refute. |
| **service blueprint** | mapa frontstage y backstage del servicio | Distingue un hecho compatible y otro que lo refute. |
| **automation candidate** | tarea repetible y estable apta para automatizar | Distingue un hecho compatible y otro que lo refute. |

## 🧠 Modelo mental

```text
1. definir outcome a entregar → 2. operar manualmente para pocos clientes → 3. registrar steps y exceptions → 4. medir value y willingness → 5. automatizar solo patrón estable
```

La secuencia nace del problema de esta clase: **MVP y concierge tests permiten aprender el flujo de valor manualmente antes de automatizar. El founder actúa como sistema para descubrir excepciones, lenguaje, datos y willingness to pay; luego automatiza las partes repetibles con mejor evidencia.** El método es útil mientras las condiciones permitan observar las señales requeridas. No elimina incertidumbre; la hace visible y obliga a decidir proporcionalmente a la evidencia. Límite principal: **Concierge no prueba escalabilidad. Sirve para aprender demanda y workflow; antes de escalar, modela costos y automatización necesaria.**

## 📖 Desarrollo

### 1. concierge MVP: mecanismo central

**concierge MVP** se entiende aquí como **servicio manual que entrega valor prometido a pocos clientes**. Esta es la pieza causal o estructural desde la que se inicia **mVP y concierge tests**: antes de definir outcome a entregar, el gerente debe poder señalar qué cambia en el sistema si el concepto está presente y qué debería observar si no lo está. Una definición que no produce predicciones observables todavía es demasiado vaga para dirigir.

La lectura rectora de este bloque es Steve Blank — *The Four Steps to the Epiphany*. Su aporte se usa para examinar **customer development y búsqueda sistemática de un modelo de negocio**. Aplica esa lente al caso sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **time-to-value**; regístrala con periodo, unidad, población y baseline.

Relaciona el mecanismo con **Wizard of Oz**. Si ambos cambian juntos, no concluyas causalidad automáticamente: identifica una tercera variable o mecanismo alternativo que también pueda explicar el patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Wizard of Oz: frontera conceptual y error de clasificación

**Definición operacional:** interfaz que aparenta automatización mientras procesos internos son manuales. Su valor está en distinguirlo de **concierge MVP** y **manual-first**. En una decisión real, clasificar una situación en la categoría equivocada cambia la intervención: puedes asignar autoridad donde faltaba información, medir un output cuando debías observar un proceso o tratar una restricción como si fuera una preferencia.

Contrasta el problema con Alexander Osterwalder & Yves Pigneur — *Business Model Generation*, que aporta una mirada sobre **diseño de modelos de negocio mediante propuesta, clientes, recursos y economía**. Formula dos mini-casos: uno que sí satisface la definición de **Wizard of Oz** y otro que solo se parece superficialmente. Luego pregunta qué señal distinguiría ambos; para esta clase, **manual hours per customer** es una candidata, pero debe combinarse con evidencia cualitativa o documental cuando el fenómeno no sea directamente medible.

Antes de operar manualmente para pocos clientes, registra explícitamente qué decisión sería errónea si esta frontera conceptual se ignora. Esa frase convierte el vocabulario en criterio gerencial.

### 3. manual-first: operacionalización y medición

**manual-first** significa **estrategia de aprendizaje que pospone automatización**. El problema ya no es definirlo, sino **operacionalizarlo**: qué contar, durante qué ventana, con qué denominador, contra qué baseline y con qué segmentación. Una métrica útil conserva suficiente contexto para no confundir mejora local con mejora del sistema.

Peter F. Drucker — *The Effective Executive* orienta este bloque mediante **efectividad ejecutiva, contribución, prioridades y uso consciente del tiempo**. Usa esa perspectiva para diseñar una ficha de medición: `señal → fórmula/criterio → fuente → frecuencia → owner → interpretación permitida → interpretación prohibida`. La señal asignada es **exception rate**. Si no existe un dato confiable, la salida correcta no es inventar precisión: diseña el mecanismo de captura y declara la incertidumbre.

Al llegar a registrar steps y exceptions, compara tendencia, distribución y casos atípicos. Pregunta además si el indicador es *leading* o *lagging* y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; nunca convertirse en el objetivo que reemplaza al fenómeno.

### 4. service blueprint: trade-offs y efectos de segundo orden

**Definición:** mapa frontstage y backstage del servicio. Este concepto obliga a abandonar la idea de que **mVP y concierge tests** tiene una solución gratuita. Toda intervención consume autonomía, tiempo, caja, capacidad, atención, reputación o tolerancia al riesgo. Por eso, antes de medir value y willingness, se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Bill Aulet — *Disciplined Entrepreneurship* aporta una lente sobre **secuencia disciplinada desde mercado inicial hasta economía y diseño del negocio**. Úsala para construir una matriz `beneficio / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **paid retention** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la necesidad de observar efectos laterales fuera del KPI principal.

Haz un *pre-mortem* de **mVP y concierge tests**: supone que la opción recomendada fracasó seis meses después y enumera tres mecanismos que podrían explicarlo. Al menos uno debe provenir de un efecto de segundo orden asociado a **service blueprint** y otro de una hipótesis del caso que nunca fue validada.

### 5. automation candidate: gobernanza, límites e integración

**automation candidate** se define como **tarea repetible y estable apta para automatizar** y cierra el circuito porque traduce análisis en responsabilidad. La pregunta ejecutiva es quién decide, quién ejecuta, quién debe ser consultado, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar.

Eric Ries — *The Lean Startup* se utiliza para estudiar **build-measure-learn, MVP y aprendizaje validado** y contrastar la recomendación final. Al ejecutar automatizar solo patrón estable, deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento. Esa trazabilidad protege contra el sesgo retrospectivo y mejora las revisiones posteriores.

La frontera de esta clase es explícita: **Concierge no prueba escalabilidad. Sirve para aprender demanda y workflow; antes de escalar, modela costos y automatización necesaria.**. Conviértela en una regla operativa: `si ocurre X → no aplicar automáticamente → consultar/escalar/revalidar`. Integrar **concierge MVP**, **Wizard of Oz**, **manual-first**, **service blueprint** y **automation candidate** significa poder explicar qué parte del diagnóstico sostiene la decisión y cuál sigue siendo una apuesta.

### 6. Integración: de conceptos a una decisión defendible

La síntesis de **mVP y concierge tests** no consiste en sumar cinco definiciones. Empieza por **concierge MVP**, contrasta **Wizard of Oz** con **manual-first**, incorpora **service blueprint** como restricción o mecanismo y usa **automation candidate** para cerrar el ciclo. Si el análisis no puede explicar cuál de esas piezas cambió la recomendación, todavía no hay comprensión transferible.

Aplica ahora la secuencia **1. definir outcome a entregar → 2. operar manualmente para pocos clientes → 3. registrar steps y exceptions → 4. medir value y willingness → 5. automatizar solo patrón estable**. Para cada paso conserva tres columnas: evidencia utilizada, alternativa descartada y razón. Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado y evita reescribir la historia después de conocer el desenlace.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla señala el lente que debes buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Steve Blank — *The Four Steps to the Epiphany* | customer development y búsqueda sistemática de un modelo de negocio | ¿Qué supuesto de **mVP y concierge tests** ayuda a desafiar? |
| Alexander Osterwalder & Yves Pigneur — *Business Model Generation* | diseño de modelos de negocio mediante propuesta, clientes, recursos y economía | ¿Qué supuesto de **mVP y concierge tests** ayuda a desafiar? |
| Peter F. Drucker — *The Effective Executive* | efectividad ejecutiva, contribución, prioridades y uso consciente del tiempo | ¿Qué supuesto de **mVP y concierge tests** ayuda a desafiar? |
| Bill Aulet — *Disciplined Entrepreneurship* | secuencia disciplinada desde mercado inicial hasta economía y diseño del negocio | ¿Qué supuesto de **mVP y concierge tests** ayuda a desafiar? |
| Eric Ries — *The Lean Startup* | build-measure-learn, MVP y aprendizaje validado | ¿Qué supuesto de **mVP y concierge tests** ayuda a desafiar? |

En **mVP y concierge tests**, la lectura se evalúa por **uso**, no por cantidad de páginas. La nota debe indicar qué tesis de las fuentes modifica tu lectura de **concierge MVP**, qué evidencia del caso tensiona esa tesis y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación:** Una startup ofrece reportes de riesgo generados manualmente a cinco clientes pagos. Aprende que 70% del trabajo está en limpieza de datos, no en el modelo esperado.

**Paso 1 — definir outcome a entregar.** La gerencia escribe primero el supuesto asociado a **concierge MVP** y evita convertirlo en hecho. Luego busca **time-to-value** para contrastarlo en el caso de **mVP y concierge tests**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 2 — operar manualmente para pocos clientes.** La gerencia escribe primero el supuesto asociado a **Wizard of Oz** y evita convertirlo en hecho. Luego busca **manual hours per customer** para contrastarlo en el caso de **mVP y concierge tests**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 3 — registrar steps y exceptions.** La gerencia escribe primero el supuesto asociado a **manual-first** y evita convertirlo en hecho. Luego busca **exception rate** para contrastarlo en el caso de **mVP y concierge tests**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 4 — medir value y willingness.** La gerencia escribe primero el supuesto asociado a **service blueprint** y evita convertirlo en hecho. Luego busca **paid retention** para contrastarlo en el caso de **mVP y concierge tests**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 5 — automatizar solo patrón estable.** La gerencia escribe primero el supuesto asociado a **automation candidate** y evita convertirlo en hecho. Luego busca **automation potential** para contrastarlo en el caso de **mVP y concierge tests**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Síntesis del caso.** La recomendación debe terminar con responsable, fecha, evidencia de éxito y señal de stop. En **mVP y concierge tests**, omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo |
|---|---|---|---|
| **concierge MVP** | servicio manual que entrega valor prometido a pocos clientes | Cuando time-to-value es observable y accionable. | Sobrerreaccionar a una señal parcial. |
| **Wizard of Oz** | interfaz que aparenta automatización mientras procesos internos son manuales | Cuando la primera explicación no distingue mecanismo o responsabilidad. | Convertir el concepto en etiqueta. |
| **Experimento/revisión** | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar eternamente y no decidir. |
| **Escalamiento** | Elevar autoridad o especialidad | Cuando hay derechos, capital material, regulación o irreversibilidad. | Delegar hacia arriba lo que sí corresponde decidir. |

**Frontera de aplicación:** Concierge no prueba escalabilidad. Sirve para aprender demanda y workflow; antes de escalar, modela costos y automatización necesaria.

## 🪜 De profesional a owner

| Nivel | Responsabilidad sobre mVP y concierge tests |
|---|---|
| **Profesional** | usa **mVP y concierge tests** para mejorar una contribución propia y explicar sus supuestos con evidencia. |
| **Jefe / Team Lead** | aplica **concierge MVP** y **Wizard of Oz** para coordinar personas sin sustituir conversación por métricas. |
| **Manager / Gerente** | conecta time-to-value con capacidad, presupuesto, dependencias y riesgo interáreas. |
| **CEO / Director** | decide si mVP y concierge tests cambia estrategia, economía o riesgo de empresa y qué debe llegar al comité o directorio. |
| **Founder / Owner** | pregunta si la solución de mVP y concierge tests reduce dependencia del fundador, preserva caja y puede operar como sistema repetible. |

El cambio de nivel en **mVP y concierge tests** aumenta el número de personas, dinero, dependencias y consecuencias que quedan dentro de la decisión. Por eso la misma herramienta debe volverse más explícita en evidencia, gobernanza y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Una startup ofrece reportes de riesgo generados manualmente a cinco clientes pagos. Aprende que 70% del trabajo está en limpieza de datos, no en el modelo esperado.

Entrega un **decision brief de mVP y concierge tests** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre personas, cliente, operación, caja y riesgo; (e) recomendación; (f) condición que haría cambiarla; (g) dueño y fecha de revisión. Utiliza al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica

1. Reconstruye el caso de **mVP y concierge tests** con una tabla `hecho / interpretación / hipótesis / decisión`.
2. Ejecuta **1. definir outcome a entregar → 2. operar manualmente para pocos clientes → 3. registrar steps y exceptions → 4. medir value y willingness → 5. automatizar solo patrón estable** y adjunta evidencia para cada transición entre pasos.
3. Calcula o documenta time-to-value, manual hours per customer; si no existe dato, diseña cómo obtenerlo.
4. Escribe una alternativa que contradiga tu preferencia inicial y haz un *pre-mortem* específico del caso.
5. Lee dos referencias, registra una coincidencia y una tensión, y modifica el brief si corresponde.
6. Repite la decisión desde el rol de CEO/owner: identifica qué cambia al aumentar el alcance y la irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar concierge MVP y Wizard of Oz como sinónimos | Se pierde la distinción entre “servicio manual que entrega valor prometido a pocos clientes” y “interfaz que aparenta automatización mientras procesos internos son manuales” | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por “automatizar solo patrón estable” | Se saltó “definir outcome a entregar” y la solución llegó antes que el diagnóstico | Reconstruye la cadena 1. definir outcome a entregar → 2. operar manualmente para pocos clientes → 3. registrar steps y exceptions → 4. medir value y willingness → 5. automatizar solo patrón estable y marca el primer supuesto no demostrado. |
| Optimizar solo time-to-value | La métrica local sustituyó al resultado del sistema | Contrástala con manual hours per customer y explicita el costo de oportunidad. |
| Generalizar desde un caso favorable | Se confundió evidencia local con una regla universal sobre mVP y concierge tests | Concierge no prueba escalabilidad. Sirve para aprender demanda y workflow; antes de escalar, modela costos y automatización necesaria. |
| No fijar revisión | Una decisión sobre mVP y concierge tests se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de stop. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **concierge MVP** y **Wizard of Oz** usando un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **manual-first** y qué observación obligaría a rechazar tu interpretación?
3. Aplica **definir outcome a entregar → operar manualmente para pocos clientes** al caso de la clase. ¿Qué dato todavía falta?
4. ¿Por qué **time-to-value** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la tabla de lectura. ¿Dónde podrían llevar a recomendaciones distintas para **mVP y concierge tests**?
6. ¿Qué decisión equivocada podría producirse si se ignora este límite: **Concierge no prueba escalabilidad. Sirve para aprender demanda y workflow; antes de escalar, modela costos y automatización necesaria.**?

## 📥 Entregable

Guarda en `portfolio/248-mvp-y-concierge-tests/`:

- `product-evidence-brief.md` con el problema específico de **mVP y concierge tests**, evidencia, alternativas, decisión y gobernanza;
- `reading-note.md` contrastando las fuentes de **mVP y concierge tests** con edición/páginas consultadas;
- `decision-journal.md` registrando los supuestos de **concierge MVP**, confianza, responsable y revisión;
- `red-team.md` con la objeción más fuerte al caso **Una startup ofrece reportes de riesgo generados manualmente a cinco clientes pagos. Aprende que 70% del trabajo está en limpieza de datos, no en el modelo esperado.** y el dato que podría invalidar la recomendación.

## 📗 Fuentes y verificación

- Steve Blank — *The Four Steps to the Epiphany*. **Uso en esta clase:** customer development y búsqueda sistemática de un modelo de negocio. Lectura selectiva: índice/capítulos pertinentes a **mVP y concierge tests**; registra edición y páginas consultadas.
- Alexander Osterwalder & Yves Pigneur — *Business Model Generation*. **Uso en esta clase:** diseño de modelos de negocio mediante propuesta, clientes, recursos y economía. Lectura selectiva: índice/capítulos pertinentes a **mVP y concierge tests**; registra edición y páginas consultadas.
- Peter F. Drucker — *The Effective Executive*. **Uso en esta clase:** efectividad ejecutiva, contribución, prioridades y uso consciente del tiempo. Lectura selectiva: índice/capítulos pertinentes a **mVP y concierge tests**; registra edición y páginas consultadas.
- Bill Aulet — *Disciplined Entrepreneurship*. **Uso en esta clase:** secuencia disciplinada desde mercado inicial hasta economía y diseño del negocio. Lectura selectiva: índice/capítulos pertinentes a **mVP y concierge tests**; registra edición y páginas consultadas.
- Eric Ries — *The Lean Startup*. **Uso en esta clase:** build-measure-learn, MVP y aprendizaje validado. Lectura selectiva: índice/capítulos pertinentes a **mVP y concierge tests**; registra edición y páginas consultadas.
- Rob Fitzpatrick — *The Mom Test*. **Uso en esta clase:** perspectiva de Customer discovery aplicada al problema de la clase. Lectura selectiva: índice/capítulos pertinentes a **mVP y concierge tests**; registra edición y páginas consultadas.
- Susan A. Ambrose et al. — *How Learning Works*. **Uso en esta clase:** diseñar los objetivos, la práctica y el feedback de **mvp y concierge tests** sobre conocimiento previo verificable.
- Peter C. Brown, Henry L. Roediger III & Mark A. McDaniel — *Make It Stick*. **Uso en esta clase:** justificar la recuperación inicial y las preguntas de comprobación de **mvp y concierge tests**.
- Grant Wiggins & Jay McTighe — *Understanding by Design*. **Uso en esta clase:** derivar el entregable de **mvp y concierge tests** desde el desempeño observable y no desde el temario.
- Anders Ericsson & Robert Pool — *Peak*. **Uso en esta clase:** convertir la práctica de **mvp y concierge tests** en práctica deliberada con criterios explícitos.
- William Ellet — *The Case Study Handbook*. **Uso en esta clase:** estructurar el caso ejecutivo de **mvp y concierge tests** como problema, evidencia, alternativas y recomendación.

> **Regla de fuentes para MVP y concierge tests:** las obras anteriores estructuran las perspectivas de esta materia; cualquier norma, ley, impuesto o estándar vivo mencionado en **mVP y concierge tests** debe comprobarse nuevamente en su fuente primaria vigente. El desarrollo es original y no reproduce capítulos protegidos.
