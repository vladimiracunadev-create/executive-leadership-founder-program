# Clase 115 — Presupuesto y forecast

**Parte:** 09 — Finanzas y contabilidad para gerentes  
**Nivel:** Etapa 3 — Manager → Gerente  
**Duración sugerida:** 150–180 minutos · **Estándar:** deep-class-v2

## 🎯 Propósito

Presupuesto es una asignación y compromiso para un periodo; forecast es la mejor estimación actual del futuro. Confundirlos incentiva ocultar malas noticias para 'cumplir presupuesto'. Un gerente usa rolling forecast y escenarios para decidir, aunque el presupuesto siga siendo base de autorización.

La salida de esta parte es **leer la economía del negocio y decidir con estados, caja, márgenes, retorno y valoración**. En esta clase, esa progresión se concreta al exigir que cada afirmación sobre **presupuesto y forecast** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

## 📚 Resultados de aprendizaje

Al finalizar podrás:

1. **Distinguir** `budget`, `forecast`, `variance`, `driver-based model`, `scenario` mediante observables, no por memoria verbal.
2. **Explicar** por qué esas distinciones cambian una decisión de manager → gerente.
3. **Aplicar** la secuencia **1. definir drivers y baseline → 2. construir budget con recursos → 3. actualizar actuals → 4. reforecast sin manipular para alcanzar plan → 5. usar escenarios para decisiones de capacidad y caja** conservando supuestos, alternativas y trazabilidad.
4. **Interpretar** forecast error, budget variance, driver accuracy sin confundir señal, explicación y causalidad.
5. **Resolver** el caso ejecutivo con al menos dos opciones plausibles y un criterio explícito de stop/revisión.
6. **Contrastar** dos obras de referencia y explicar dónde sus lentes son complementarias o entran en tensión.

## 🧭 Agenda

| Tramo | Evidencia de aprendizaje |
|---|---|
| 0–20 min | Recuperación: define budget y forecast sin mirar la tabla; corrige con la fuente. |
| 20–70 min | Lectura guiada de conceptos + contraste de dos referencias. |
| 70–115 min | Ejemplo trabajado con forecast error y trazabilidad de supuestos. |
| 115–155 min | Caso ejecutivo: dos alternativas, trade-offs y decisión provisional. |
| 155–180 min | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar comprensión |
|---|---|---|
| **budget** | plan aprobado que asigna recursos y objetivos | Distingue un hecho compatible y otro que lo refute. |
| **forecast** | estimación actualizada basada en evidencia reciente | Distingue un hecho compatible y otro que lo refute. |
| **variance** | diferencia entre actual y referencia | Distingue un hecho compatible y otro que lo refute. |
| **driver-based model** | forecast construido desde variables causales del negocio | Distingue un hecho compatible y otro que lo refute. |
| **scenario** | conjunto coherente de supuestos alternativos | Distingue un hecho compatible y otro que lo refute. |

## 🧠 Modelo mental

```text
1. definir drivers y baseline → 2. construir budget con recursos → 3. actualizar actuals → 4. reforecast sin manipular para alcanzar plan → 5. usar escenarios para decisiones de capacidad y caja
```

La secuencia nace del problema de esta clase: **Presupuesto es una asignación y compromiso para un periodo; forecast es la mejor estimación actual del futuro. Confundirlos incentiva ocultar malas noticias para 'cumplir presupuesto'. Un gerente usa rolling forecast y escenarios para decidir, aunque el presupuesto siga siendo base de autorización.** El método es útil mientras las condiciones permitan observar las señales requeridas. No elimina incertidumbre; la hace visible y obliga a decidir proporcionalmente a la evidencia. Límite principal: **Forecast no debe convertirse en target que la gente tema cambiar. Si se usa para evaluar a quien lo produce, se incentiva precisión política en vez de económica.**

## 📖 Desarrollo

### 1. budget: mecanismo central

**budget** se entiende aquí como **plan aprobado que asigna recursos y objetivos**. Esta es la pieza causal o estructural desde la que se inicia **presupuesto y forecast**: antes de definir drivers y baseline, el gerente debe poder señalar qué cambia en el sistema si el concepto está presente y qué debería observar si no lo está. Una definición que no produce predicciones observables todavía es demasiado vaga para dirigir.

La lectura rectora de este bloque es Charles Horngren et al. — *Cost Accounting: A Managerial Emphasis*. Su aporte se usa para examinar **costos relevantes, presupuestos, variaciones y decisiones gerenciales**. Aplica esa lente al caso sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **forecast error**; regístrala con periodo, unidad, población y baseline.

Relaciona el mecanismo con **forecast**. Si ambos cambian juntos, no concluyas causalidad automáticamente: identifica una tercera variable o mecanismo alternativo que también pueda explicar el patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. forecast: frontera conceptual y error de clasificación

**Definición operacional:** estimación actualizada basada en evidencia reciente. Su valor está en distinguirlo de **budget** y **variance**. En una decisión real, clasificar una situación en la categoría equivocada cambia la intervención: puedes asignar autoridad donde faltaba información, medir un output cuando debías observar un proceso o tratar una restricción como si fuera una preferencia.

Contrasta el problema con Richard Brealey, Stewart Myers & Franklin Allen — *Principles of Corporate Finance*, que aporta una mirada sobre **valor del dinero, riesgo, costo de capital, inversión y financiación**. Formula dos mini-casos: uno que sí satisface la definición de **forecast** y otro que solo se parece superficialmente. Luego pregunta qué señal distinguiría ambos; para esta clase, **budget variance** es una candidata, pero debe combinarse con evidencia cualitativa o documental cuando el fenómeno no sea directamente medible.

Antes de construir budget con recursos, registra explícitamente qué decisión sería errónea si esta frontera conceptual se ignora. Esa frase convierte el vocabulario en criterio gerencial.

### 3. variance: operacionalización y medición

**variance** significa **diferencia entre actual y referencia**. El problema ya no es definirlo, sino **operacionalizarlo**: qué contar, durante qué ventana, con qué denominador, contra qué baseline y con qué segmentación. Una métrica útil conserva suficiente contexto para no confundir mejora local con mejora del sistema.

Stephen Ross, Randolph Westerfield et al. — *Corporate Finance* orienta este bloque mediante **decisiones de inversión, financiación, capital de trabajo y valoración**. Usa esa perspectiva para diseñar una ficha de medición: `señal → fórmula/criterio → fuente → frecuencia → owner → interpretación permitida → interpretación prohibida`. La señal asignada es **driver accuracy**. Si no existe un dato confiable, la salida correcta no es inventar precisión: diseña el mecanismo de captura y declara la incertidumbre.

Al llegar a actualizar actuals, compara tendencia, distribución y casos atípicos. Pregunta además si el indicador es *leading* o *lagging* y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; nunca convertirse en el objetivo que reemplaza al fenómeno.

### 4. driver-based model: trade-offs y efectos de segundo orden

**Definición:** forecast construido desde variables causales del negocio. Este concepto obliga a abandonar la idea de que **presupuesto y forecast** tiene una solución gratuita. Toda intervención consume autonomía, tiempo, caja, capacidad, atención, reputación o tolerancia al riesgo. Por eso, antes de reforecast sin manipular para alcanzar plan, se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Donald E. Kieso, Jerry J. Weygandt & Terry D. Warfield — *Intermediate Accounting* aporta una lente sobre **reconocimiento, medición y presentación de estados financieros y sus partidas**. Úsala para construir una matriz `beneficio / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **cash runway** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la necesidad de observar efectos laterales fuera del KPI principal.

Haz un *pre-mortem* de **presupuesto y forecast**: supone que la opción recomendada fracasó seis meses después y enumera tres mecanismos que podrían explicarlo. Al menos uno debe provenir de un efecto de segundo orden asociado a **driver-based model** y otro de una hipótesis del caso que nunca fue validada.

### 5. scenario: gobernanza, límites e integración

**scenario** se define como **conjunto coherente de supuestos alternativos** y cierra el circuito porque traduce análisis en responsabilidad. La pregunta ejecutiva es quién decide, quién ejecuta, quién debe ser consultado, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar.

Stephen H. Penman — *Financial Statement Analysis and Security Valuation* se utiliza para estudiar **reformulación de estados, calidad del resultado y análisis de rentabilidad para valoración** y contrastar la recomendación final. Al ejecutar usar escenarios para decisiones de capacidad y caja, deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento. Esa trazabilidad protege contra el sesgo retrospectivo y mejora las revisiones posteriores.

La frontera de esta clase es explícita: **Forecast no debe convertirse en target que la gente tema cambiar. Si se usa para evaluar a quien lo produce, se incentiva precisión política en vez de económica.**. Conviértela en una regla operativa: `si ocurre X → no aplicar automáticamente → consultar/escalar/revalidar`. Integrar **budget**, **forecast**, **variance**, **driver-based model** y **scenario** significa poder explicar qué parte del diagnóstico sostiene la decisión y cuál sigue siendo una apuesta.

### 6. Integración: de conceptos a una decisión defendible

La síntesis de **presupuesto y forecast** no consiste en sumar cinco definiciones. Empieza por **budget**, contrasta **forecast** con **variance**, incorpora **driver-based model** como restricción o mecanismo y usa **scenario** para cerrar el ciclo. Si el análisis no puede explicar cuál de esas piezas cambió la recomendación, todavía no hay comprensión transferible.

Aplica ahora la secuencia **1. definir drivers y baseline → 2. construir budget con recursos → 3. actualizar actuals → 4. reforecast sin manipular para alcanzar plan → 5. usar escenarios para decisiones de capacidad y caja**. Para cada paso conserva tres columnas: evidencia utilizada, alternativa descartada y razón. Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado y evita reescribir la historia después de conocer el desenlace.

## 🔧 Profundización específica

### Presupuesto, forecast y análisis de variaciones

Presupuesto fija una intención/plan; forecast actualiza la mejor estimación con información reciente. No “corrijas” el forecast para proteger el presupuesto. Separa variaciones en drivers: precio, volumen, mix, costo unitario, headcount, tipo de cambio u otros que correspondan.

Ejemplo: ventas presupuestadas 1.000 = 100 unidades × 10. Si se venden 90 a 11, ventas reales 990. La variación total es -10, pero precio aportó positivamente y volumen negativamente. El análisis driver-based evita respuestas equivocadas, como recortar marketing cuando el problema real fue capacidad de entrega.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla señala el lente que debes buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Charles Horngren et al. — *Cost Accounting: A Managerial Emphasis* | costos relevantes, presupuestos, variaciones y decisiones gerenciales | ¿Qué supuesto de **presupuesto y forecast** ayuda a desafiar? |
| Richard Brealey, Stewart Myers & Franklin Allen — *Principles of Corporate Finance* | valor del dinero, riesgo, costo de capital, inversión y financiación | ¿Qué supuesto de **presupuesto y forecast** ayuda a desafiar? |
| Stephen Ross, Randolph Westerfield et al. — *Corporate Finance* | decisiones de inversión, financiación, capital de trabajo y valoración | ¿Qué supuesto de **presupuesto y forecast** ayuda a desafiar? |
| Donald E. Kieso, Jerry J. Weygandt & Terry D. Warfield — *Intermediate Accounting* | reconocimiento, medición y presentación de estados financieros y sus partidas | ¿Qué supuesto de **presupuesto y forecast** ayuda a desafiar? |
| Stephen H. Penman — *Financial Statement Analysis and Security Valuation* | reformulación de estados, calidad del resultado y análisis de rentabilidad para valoración | ¿Qué supuesto de **presupuesto y forecast** ayuda a desafiar? |

En **presupuesto y forecast**, la lectura se evalúa por **uso**, no por cantidad de páginas. La nota debe indicar qué tesis de las fuentes modifica tu lectura de **budget**, qué evidencia del caso tensiona esa tesis y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación:** El presupuesto asume 25% crecimiento. A mitad de año los datos apuntan a 8%, pero el equipo mantiene el forecast original para no 'verse pesimista', retrasando ajustes de gasto.

**Paso 1 — definir drivers y baseline.** La gerencia escribe primero el supuesto asociado a **budget** y evita convertirlo en hecho. Luego busca **forecast error** para contrastarlo en el caso de **presupuesto y forecast**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 2 — construir budget con recursos.** La gerencia escribe primero el supuesto asociado a **forecast** y evita convertirlo en hecho. Luego busca **budget variance** para contrastarlo en el caso de **presupuesto y forecast**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 3 — actualizar actuals.** La gerencia escribe primero el supuesto asociado a **variance** y evita convertirlo en hecho. Luego busca **driver accuracy** para contrastarlo en el caso de **presupuesto y forecast**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 4 — reforecast sin manipular para alcanzar plan.** La gerencia escribe primero el supuesto asociado a **driver-based model** y evita convertirlo en hecho. Luego busca **cash runway** para contrastarlo en el caso de **presupuesto y forecast**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 5 — usar escenarios para decisiones de capacidad y caja.** La gerencia escribe primero el supuesto asociado a **scenario** y evita convertirlo en hecho. Luego busca **reforecast frequency** para contrastarlo en el caso de **presupuesto y forecast**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Síntesis del caso.** La recomendación debe terminar con responsable, fecha, evidencia de éxito y señal de stop. En **presupuesto y forecast**, omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo |
|---|---|---|---|
| **budget** | plan aprobado que asigna recursos y objetivos | Cuando forecast error es observable y accionable. | Sobrerreaccionar a una señal parcial. |
| **forecast** | estimación actualizada basada en evidencia reciente | Cuando la primera explicación no distingue mecanismo o responsabilidad. | Convertir el concepto en etiqueta. |
| **Experimento/revisión** | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar eternamente y no decidir. |
| **Escalamiento** | Elevar autoridad o especialidad | Cuando hay derechos, capital material, regulación o irreversibilidad. | Delegar hacia arriba lo que sí corresponde decidir. |

**Frontera de aplicación:** Forecast no debe convertirse en target que la gente tema cambiar. Si se usa para evaluar a quien lo produce, se incentiva precisión política en vez de económica.

## 🪜 De profesional a owner

| Nivel | Responsabilidad sobre presupuesto y forecast |
|---|---|
| **Profesional** | usa **presupuesto y forecast** para mejorar una contribución propia y explicar sus supuestos con evidencia. |
| **Jefe / Team Lead** | aplica **budget** y **forecast** para coordinar personas sin sustituir conversación por métricas. |
| **Manager / Gerente** | conecta forecast error con capacidad, presupuesto, dependencias y riesgo interáreas. |
| **CEO / Director** | decide si presupuesto y forecast cambia estrategia, economía o riesgo de empresa y qué debe llegar al comité o directorio. |
| **Founder / Owner** | pregunta si la solución de presupuesto y forecast reduce dependencia del fundador, preserva caja y puede operar como sistema repetible. |

El cambio de nivel en **presupuesto y forecast** aumenta el número de personas, dinero, dependencias y consecuencias que quedan dentro de la decisión. Por eso la misma herramienta debe volverse más explícita en evidencia, gobernanza y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

El presupuesto asume 25% crecimiento. A mitad de año los datos apuntan a 8%, pero el equipo mantiene el forecast original para no 'verse pesimista', retrasando ajustes de gasto.

Entrega un **decision brief de presupuesto y forecast** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre personas, cliente, operación, caja y riesgo; (e) recomendación; (f) condición que haría cambiarla; (g) dueño y fecha de revisión. Utiliza al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica

1. Reconstruye el caso de **presupuesto y forecast** con una tabla `hecho / interpretación / hipótesis / decisión`.
2. Ejecuta **1. definir drivers y baseline → 2. construir budget con recursos → 3. actualizar actuals → 4. reforecast sin manipular para alcanzar plan → 5. usar escenarios para decisiones de capacidad y caja** y adjunta evidencia para cada transición entre pasos.
3. Calcula o documenta forecast error, budget variance; si no existe dato, diseña cómo obtenerlo.
4. Escribe una alternativa que contradiga tu preferencia inicial y haz un *pre-mortem* específico del caso.
5. Lee dos referencias, registra una coincidencia y una tensión, y modifica el brief si corresponde.
6. Repite la decisión desde el rol de CEO/owner: identifica qué cambia al aumentar el alcance y la irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar budget y forecast como sinónimos | Se pierde la distinción entre “plan aprobado que asigna recursos y objetivos” y “estimación actualizada basada en evidencia reciente” | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por “usar escenarios para decisiones de capacidad y caja” | Se saltó “definir drivers y baseline” y la solución llegó antes que el diagnóstico | Reconstruye la cadena 1. definir drivers y baseline → 2. construir budget con recursos → 3. actualizar actuals → 4. reforecast sin manipular para alcanzar plan → 5. usar escenarios para decisiones de capacidad y caja y marca el primer supuesto no demostrado. |
| Optimizar solo forecast error | La métrica local sustituyó al resultado del sistema | Contrástala con budget variance y explicita el costo de oportunidad. |
| Generalizar desde un caso favorable | Se confundió evidencia local con una regla universal sobre presupuesto y forecast | Forecast no debe convertirse en target que la gente tema cambiar. Si se usa para evaluar a quien lo produce, se incentiva precisión política en vez de económica. |
| No fijar revisión | Una decisión sobre presupuesto y forecast se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de stop. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **budget** y **forecast** usando un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **variance** y qué observación obligaría a rechazar tu interpretación?
3. Aplica **definir drivers y baseline → construir budget con recursos** al caso de la clase. ¿Qué dato todavía falta?
4. ¿Por qué **forecast error** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la tabla de lectura. ¿Dónde podrían llevar a recomendaciones distintas para **presupuesto y forecast**?
6. ¿Qué decisión equivocada podría producirse si se ignora este límite: **Forecast no debe convertirse en target que la gente tema cambiar. Si se usa para evaluar a quien lo produce, se incentiva precisión política en vez de económica.**?

## 📥 Entregable

Guarda en `portfolio/115-presupuesto-y-forecast/`:

- `modelo-financiero-y-memo-de-decision.md` con el problema específico de **presupuesto y forecast**, evidencia, alternativas, decisión y gobernanza;
- `reading-note.md` contrastando las fuentes de **presupuesto y forecast** con edición/páginas consultadas;
- `decision-journal.md` registrando los supuestos de **budget**, confianza, responsable y revisión;
- `red-team.md` con la objeción más fuerte al caso **El presupuesto asume 25% crecimiento. A mitad de año los datos apuntan a 8%, pero el equipo mantiene el forecast original para no 'verse pesimista', retrasando ajustes de gasto.** y el dato que podría invalidar la recomendación.

## 📗 Fuentes y verificación

- Charles Horngren et al. — *Cost Accounting: A Managerial Emphasis* (Prentice Hall College Div, 2002). **Uso en esta clase:** costos relevantes, presupuestos, variaciones y decisiones gerenciales. Lectura selectiva sobre **presupuesto y forecast**. **Localizador:** [ISBN-13 9780130650061](https://openlibrary.org/isbn/9780130650061).
- Richard Brealey, Stewart Myers & Franklin Allen — *Principles of Corporate Finance* (McGraw-Hill International Book Co, 1984). **Uso en esta clase:** valor del dinero, riesgo, costo de capital, inversión y financiación. Lectura selectiva sobre **presupuesto y forecast**. **Localizador:** [ISBN-13 9780070662025](https://openlibrary.org/isbn/9780070662025).
- Stephen Ross, Randolph Westerfield et al. — *Corporate Finance* (McGraw-Hill Education, 2018). **Uso en esta clase:** decisiones de inversión, financiación, capital de trabajo y valoración. Lectura selectiva sobre **presupuesto y forecast**. **Localizador:** [ISBN-13 9781259918940](https://openlibrary.org/isbn/9781259918940).
- Donald E. Kieso, Jerry J. Weygandt & Terry D. Warfield — *Intermediate Accounting* (John Wiley & Sons, Incorporated, 2006). **Uso en esta clase:** reconocimiento, medición y presentación de estados financieros y sus partidas. Lectura selectiva sobre **presupuesto y forecast**. **Localizador:** [ISBN-13 9780470098189](https://openlibrary.org/isbn/9780470098189).
- Stephen H. Penman — *Financial Statement Analysis and Security Valuation* (McGraw-Hill/Irwin, 2001). **Uso en esta clase:** reformulación de estados, calidad del resultado y análisis de rentabilidad para valoración. Lectura selectiva sobre **presupuesto y forecast**. **Localizador:** [ISBN-13 9780072903331](https://openlibrary.org/isbn/9780072903331).
- Tim Koller, Marc Goedhart & David Wessels — *Valuation: Measuring and Managing the Value of Companies* (Wiley, 2005). **Uso en esta clase:** drivers de valor, ROIC, crecimiento y valoración por flujo descontado. Lectura selectiva sobre **presupuesto y forecast**. **Localizador:** [ISBN-13 9780471702191](https://openlibrary.org/isbn/9780471702191).
- Susan A. Ambrose et al. — *How Learning Works* (John Wiley & Sons, Incorporated, 2010). **Uso en esta clase:** diseñar los objetivos, la práctica y el feedback de **presupuesto y forecast** sobre conocimiento previo verificable. **Localizador:** [ISBN-13 9780470617601](https://openlibrary.org/isbn/9780470617601).
- Peter C. Brown, Henry L. Roediger III & Mark A. McDaniel — *Make It Stick* (Harvard University Press, 2014). **Uso en esta clase:** justificar la recuperación inicial y las preguntas de comprobación de **presupuesto y forecast**. **Localizador:** [ISBN-13 9780674986572](https://openlibrary.org/isbn/9780674986572).
- Grant Wiggins & Jay McTighe — *Understanding by Design* (Pearson Education, Inc., 2006). **Uso en esta clase:** derivar el entregable de **presupuesto y forecast** desde el desempeño observable y no desde el temario. **Localizador:** [ISBN-13 9780131950849](https://openlibrary.org/isbn/9780131950849).
- Anders Ericsson & Robert Pool — *Peak* (Penguin Random House, 2016). **Uso en esta clase:** convertir la práctica de **presupuesto y forecast** en práctica deliberada con criterios explícitos. **Localizador:** [ISBN-13 9781473513143](https://openlibrary.org/isbn/9781473513143).
- William Ellet — *The Case Study Handbook* (Harvard Business Review Press, 2018). **Uso en esta clase:** estructurar el caso ejecutivo de **presupuesto y forecast** como problema, evidencia, alternativas y recomendación. **Localizador:** [ISBN-13 9781633696150](https://openlibrary.org/isbn/9781633696150).

> **Regla de fuentes para Presupuesto y forecast:** las obras anteriores estructuran las perspectivas de esta materia; cualquier norma, ley, impuesto o estándar vivo mencionado en **presupuesto y forecast** debe comprobarse nuevamente en su fuente primaria vigente. El desarrollo es original y no reproduce capítulos protegidos.
