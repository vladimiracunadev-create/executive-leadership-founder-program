# Clase 091 — Calidad y variabilidad

**Parte:** 07 — Operaciones, procesos y calidad  
**Nivel:** Etapa 2 — Jefe → Manager  
**Duración sugerida:** 150–180 minutos · **Estándar:** deep-class-v2

## 🎯 Propósito

Calidad es la capacidad de producir resultados conformes y útiles con variación controlada. Deming desplaza la mirada desde culpar individuos hacia comprender procesos y causas comunes versus especiales. Mejorar calidad exige medición estable, aprendizaje y diseño preventivo.

La salida de esta parte es **operar procesos end-to-end con capacidad, calidad, continuidad y mejora**. En esta clase, esa progresión se concreta al exigir que cada afirmación sobre **calidad y variabilidad** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

## 📚 Resultados de aprendizaje

Al finalizar podrás:

1. **Distinguir** `quality`, `variation`, `common cause`, `special cause`, `first-pass yield` mediante observables, no por memoria verbal.
2. **Explicar** por qué esas distinciones cambian una decisión de jefe → manager.
3. **Aplicar** la secuencia **1. definir características críticas → 2. medir proceso en el tiempo → 3. distinguir causas comunes y especiales → 4. corregir causa adecuada → 5. estandarizar mejora y monitorear** conservando supuestos, alternativas y trazabilidad.
4. **Interpretar** defect rate, first-pass yield, rework sin confundir señal, explicación y causalidad.
5. **Resolver** el caso ejecutivo con al menos dos opciones plausibles y un criterio explícito de stop/revisión.
6. **Contrastar** dos obras de referencia y explicar dónde sus lentes son complementarias o entran en tensión.

## 🧭 Agenda

| Tramo | Evidencia de aprendizaje |
|---|---|
| 0–20 min | Recuperación: define quality y variation sin mirar la tabla; corrige con la fuente. |
| 20–70 min | Lectura guiada de conceptos + contraste de dos referencias. |
| 70–115 min | Ejemplo trabajado con defect rate y trazabilidad de supuestos. |
| 115–155 min | Caso ejecutivo: dos alternativas, trade-offs y decisión provisional. |
| 155–180 min | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar comprensión |
|---|---|---|
| **quality** | grado de conformidad con requisitos y aptitud para uso | Distingue un hecho compatible y otro que lo refute. |
| **variation** | diferencia natural o especial entre resultados del proceso | Distingue un hecho compatible y otro que lo refute. |
| **common cause** | variación inherente al sistema actual | Distingue un hecho compatible y otro que lo refute. |
| **special cause** | evento identificable fuera del patrón estable | Distingue un hecho compatible y otro que lo refute. |
| **first-pass yield** | porcentaje que cumple sin rework | Distingue un hecho compatible y otro que lo refute. |

## 🧠 Modelo mental

```text
1. definir características críticas → 2. medir proceso en el tiempo → 3. distinguir causas comunes y especiales → 4. corregir causa adecuada → 5. estandarizar mejora y monitorear
```

La secuencia nace del problema de esta clase: **Calidad es la capacidad de producir resultados conformes y útiles con variación controlada. Deming desplaza la mirada desde culpar individuos hacia comprender procesos y causas comunes versus especiales. Mejorar calidad exige medición estable, aprendizaje y diseño preventivo.** El método es útil mientras las condiciones permitan observar las señales requeridas. No elimina incertidumbre; la hace visible y obliga a decidir proporcionalmente a la evidencia. Límite principal: **No conviertas calidad en solo conformidad interna. Un proceso estable puede producir consistentemente algo que el cliente no necesita; conecta control con valor y outcome.**

## 📖 Desarrollo

### 1. quality: mecanismo central

**quality** se entiende aquí como **grado de conformidad con requisitos y aptitud para uso**. Esta es la pieza causal o estructural desde la que se inicia **calidad y variabilidad**: antes de definir características críticas, el gerente debe poder señalar qué cambia en el sistema si el concepto está presente y qué debería observar si no lo está. Una definición que no produce predicciones observables todavía es demasiado vaga para dirigir.

La lectura rectora de este bloque es Nigel Slack & Alistair Brandon-Jones — *Operations Management*. Su aporte se usa para examinar **capacidad, procesos, variabilidad, calidad y estrategia de operaciones**. Aplica esa lente al caso sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **defect rate**; regístrala con periodo, unidad, población y baseline.

Relaciona el mecanismo con **variation**. Si ambos cambian juntos, no concluyas causalidad automáticamente: identifica una tercera variable o mecanismo alternativo que también pueda explicar el patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. variation: frontera conceptual y error de clasificación

**Definición operacional:** diferencia natural o especial entre resultados del proceso. Su valor está en distinguirlo de **quality** y **common cause**. En una decisión real, clasificar una situación en la categoría equivocada cambia la intervención: puedes asignar autoridad donde faltaba información, medir un output cuando debías observar un proceso o tratar una restricción como si fuera una preferencia.

Contrasta el problema con Eliyahu M. Goldratt & Jeff Cox — *The Goal*, que aporta una mirada sobre **restricciones, throughput, inventario y pensamiento de flujo**. Formula dos mini-casos: uno que sí satisface la definición de **variation** y otro que solo se parece superficialmente. Luego pregunta qué señal distinguiría ambos; para esta clase, **first-pass yield** es una candidata, pero debe combinarse con evidencia cualitativa o documental cuando el fenómeno no sea directamente medible.

Antes de medir proceso en el tiempo, registra explícitamente qué decisión sería errónea si esta frontera conceptual se ignora. Esa frase convierte el vocabulario en criterio gerencial.

### 3. common cause: operacionalización y medición

**common cause** significa **variación inherente al sistema actual**. El problema ya no es definirlo, sino **operacionalizarlo**: qué contar, durante qué ventana, con qué denominador, contra qué baseline y con qué segmentación. Una métrica útil conserva suficiente contexto para no confundir mejora local con mejora del sistema.

James P. Womack & Daniel T. Jones — *Lean Thinking* orienta este bloque mediante **valor, flujo, pull, desperdicio y mejora continua**. Usa esa perspectiva para diseñar una ficha de medición: `señal → fórmula/criterio → fuente → frecuencia → owner → interpretación permitida → interpretación prohibida`. La señal asignada es **rework**. Si no existe un dato confiable, la salida correcta no es inventar precisión: diseña el mecanismo de captura y declara la incertidumbre.

Al llegar a distinguir causas comunes y especiales, compara tendencia, distribución y casos atípicos. Pregunta además si el indicador es *leading* o *lagging* y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; nunca convertirse en el objetivo que reemplaza al fenómeno.

### 4. special cause: trade-offs y efectos de segundo orden

**Definición:** evento identificable fuera del patrón estable. Este concepto obliga a abandonar la idea de que **calidad y variabilidad** tiene una solución gratuita. Toda intervención consume autonomía, tiempo, caja, capacidad, atención, reputación o tolerancia al riesgo. Por eso, antes de corregir causa adecuada, se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Jeffrey K. Liker — *The Toyota Way* aporta una lente sobre **perspectiva de Operaciones aplicada al problema de la clase**. Úsala para construir una matriz `beneficio / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **control limits** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la necesidad de observar efectos laterales fuera del KPI principal.

Haz un *pre-mortem* de **calidad y variabilidad**: supone que la opción recomendada fracasó seis meses después y enumera tres mecanismos que podrían explicarlo. Al menos uno debe provenir de un efecto de segundo orden asociado a **special cause** y otro de una hipótesis del caso que nunca fue validada.

### 5. first-pass yield: gobernanza, límites e integración

**first-pass yield** se define como **porcentaje que cumple sin rework** y cierra el circuito porque traduce análisis en responsabilidad. La pregunta ejecutiva es quién decide, quién ejecuta, quién debe ser consultado, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar.

ISO — *ISO 9001 Quality management systems* se utiliza para estudiar **gestión de calidad basada en procesos, evidencia y mejora** y contrastar la recomendación final. Al ejecutar estandarizar mejora y monitorear, deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento. Esa trazabilidad protege contra el sesgo retrospectivo y mejora las revisiones posteriores.

La frontera de esta clase es explícita: **No conviertas calidad en solo conformidad interna. Un proceso estable puede producir consistentemente algo que el cliente no necesita; conecta control con valor y outcome.**. Conviértela en una regla operativa: `si ocurre X → no aplicar automáticamente → consultar/escalar/revalidar`. Integrar **quality**, **variation**, **common cause**, **special cause** y **first-pass yield** significa poder explicar qué parte del diagnóstico sostiene la decisión y cuál sigue siendo una apuesta.

### 6. Integración: de conceptos a una decisión defendible

La síntesis de **calidad y variabilidad** no consiste en sumar cinco definiciones. Empieza por **quality**, contrasta **variation** con **common cause**, incorpora **special cause** como restricción o mecanismo y usa **first-pass yield** para cerrar el ciclo. Si el análisis no puede explicar cuál de esas piezas cambió la recomendación, todavía no hay comprensión transferible.

Aplica ahora la secuencia **1. definir características críticas → 2. medir proceso en el tiempo → 3. distinguir causas comunes y especiales → 4. corregir causa adecuada → 5. estandarizar mejora y monitorear**. Para cada paso conserva tres columnas: evidencia utilizada, alternativa descartada y razón. Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado y evita reescribir la historia después de conocer el desenlace.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla señala el lente que debes buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Nigel Slack & Alistair Brandon-Jones — *Operations Management* | capacidad, procesos, variabilidad, calidad y estrategia de operaciones | ¿Qué supuesto de **calidad y variabilidad** ayuda a desafiar? |
| Eliyahu M. Goldratt & Jeff Cox — *The Goal* | restricciones, throughput, inventario y pensamiento de flujo | ¿Qué supuesto de **calidad y variabilidad** ayuda a desafiar? |
| James P. Womack & Daniel T. Jones — *Lean Thinking* | valor, flujo, pull, desperdicio y mejora continua | ¿Qué supuesto de **calidad y variabilidad** ayuda a desafiar? |
| Jeffrey K. Liker — *The Toyota Way* | perspectiva de Operaciones aplicada al problema de la clase | ¿Qué supuesto de **calidad y variabilidad** ayuda a desafiar? |
| ISO — *ISO 9001 Quality management systems* | gestión de calidad basada en procesos, evidencia y mejora | ¿Qué supuesto de **calidad y variabilidad** ayuda a desafiar? |

En **calidad y variabilidad**, la lectura se evalúa por **uso**, no por cantidad de páginas. La nota debe indicar qué tesis de las fuentes modifica tu lectura de **quality**, qué evidencia del caso tensiona esa tesis y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación:** Un call center sanciona agentes cada vez que el tiempo medio sube, aunque el patrón aumenta simultáneamente en todos por un sistema lento. Se trata una causa común como problema individual.

**Paso 1 — definir características críticas.** La gerencia escribe primero el supuesto asociado a **quality** y evita convertirlo en hecho. Luego busca **defect rate** para contrastarlo en el caso de **calidad y variabilidad**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 2 — medir proceso en el tiempo.** La gerencia escribe primero el supuesto asociado a **variation** y evita convertirlo en hecho. Luego busca **first-pass yield** para contrastarlo en el caso de **calidad y variabilidad**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 3 — distinguir causas comunes y especiales.** La gerencia escribe primero el supuesto asociado a **common cause** y evita convertirlo en hecho. Luego busca **rework** para contrastarlo en el caso de **calidad y variabilidad**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 4 — corregir causa adecuada.** La gerencia escribe primero el supuesto asociado a **special cause** y evita convertirlo en hecho. Luego busca **control limits** para contrastarlo en el caso de **calidad y variabilidad**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 5 — estandarizar mejora y monitorear.** La gerencia escribe primero el supuesto asociado a **first-pass yield** y evita convertirlo en hecho. Luego busca **customer complaints** para contrastarlo en el caso de **calidad y variabilidad**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Síntesis del caso.** La recomendación debe terminar con responsable, fecha, evidencia de éxito y señal de stop. En **calidad y variabilidad**, omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo |
|---|---|---|---|
| **quality** | grado de conformidad con requisitos y aptitud para uso | Cuando defect rate es observable y accionable. | Sobrerreaccionar a una señal parcial. |
| **variation** | diferencia natural o especial entre resultados del proceso | Cuando la primera explicación no distingue mecanismo o responsabilidad. | Convertir el concepto en etiqueta. |
| **Experimento/revisión** | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar eternamente y no decidir. |
| **Escalamiento** | Elevar autoridad o especialidad | Cuando hay derechos, capital material, regulación o irreversibilidad. | Delegar hacia arriba lo que sí corresponde decidir. |

**Frontera de aplicación:** No conviertas calidad en solo conformidad interna. Un proceso estable puede producir consistentemente algo que el cliente no necesita; conecta control con valor y outcome.

## 🪜 De profesional a owner

| Nivel | Responsabilidad sobre calidad y variabilidad |
|---|---|
| **Profesional** | usa **calidad y variabilidad** para mejorar una contribución propia y explicar sus supuestos con evidencia. |
| **Jefe / Team Lead** | aplica **quality** y **variation** para coordinar personas sin sustituir conversación por métricas. |
| **Manager / Gerente** | conecta defect rate con capacidad, presupuesto, dependencias y riesgo interáreas. |
| **CEO / Director** | decide si calidad y variabilidad cambia estrategia, economía o riesgo de empresa y qué debe llegar al comité o directorio. |
| **Founder / Owner** | pregunta si la solución de calidad y variabilidad reduce dependencia del fundador, preserva caja y puede operar como sistema repetible. |

El cambio de nivel en **calidad y variabilidad** aumenta el número de personas, dinero, dependencias y consecuencias que quedan dentro de la decisión. Por eso la misma herramienta debe volverse más explícita en evidencia, gobernanza y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Un call center sanciona agentes cada vez que el tiempo medio sube, aunque el patrón aumenta simultáneamente en todos por un sistema lento. Se trata una causa común como problema individual.

Entrega un **decision brief de calidad y variabilidad** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre personas, cliente, operación, caja y riesgo; (e) recomendación; (f) condición que haría cambiarla; (g) dueño y fecha de revisión. Utiliza al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica

1. Reconstruye el caso de **calidad y variabilidad** con una tabla `hecho / interpretación / hipótesis / decisión`.
2. Ejecuta **1. definir características críticas → 2. medir proceso en el tiempo → 3. distinguir causas comunes y especiales → 4. corregir causa adecuada → 5. estandarizar mejora y monitorear** y adjunta evidencia para cada transición entre pasos.
3. Calcula o documenta defect rate, first-pass yield; si no existe dato, diseña cómo obtenerlo.
4. Escribe una alternativa que contradiga tu preferencia inicial y haz un *pre-mortem* específico del caso.
5. Lee dos referencias, registra una coincidencia y una tensión, y modifica el brief si corresponde.
6. Repite la decisión desde el rol de CEO/owner: identifica qué cambia al aumentar el alcance y la irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar quality y variation como sinónimos | Se pierde la distinción entre “grado de conformidad con requisitos y aptitud para uso” y “diferencia natural o especial entre resultados del proceso” | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por “estandarizar mejora y monitorear” | Se saltó “definir características críticas” y la solución llegó antes que el diagnóstico | Reconstruye la cadena 1. definir características críticas → 2. medir proceso en el tiempo → 3. distinguir causas comunes y especiales → 4. corregir causa adecuada → 5. estandarizar mejora y monitorear y marca el primer supuesto no demostrado. |
| Optimizar solo defect rate | La métrica local sustituyó al resultado del sistema | Contrástala con first-pass yield y explicita el costo de oportunidad. |
| Generalizar desde un caso favorable | Se confundió evidencia local con una regla universal sobre calidad y variabilidad | No conviertas calidad en solo conformidad interna. Un proceso estable puede producir consistentemente algo que el cliente no necesita; conecta control con valor y outcome. |
| No fijar revisión | Una decisión sobre calidad y variabilidad se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de stop. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **quality** y **variation** usando un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **common cause** y qué observación obligaría a rechazar tu interpretación?
3. Aplica **definir características críticas → medir proceso en el tiempo** al caso de la clase. ¿Qué dato todavía falta?
4. ¿Por qué **defect rate** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la tabla de lectura. ¿Dónde podrían llevar a recomendaciones distintas para **calidad y variabilidad**?
6. ¿Qué decisión equivocada podría producirse si se ignora este límite: **No conviertas calidad en solo conformidad interna. Un proceso estable puede producir consistentemente algo que el cliente no necesita; conecta control con valor y outcome.**?

## 📥 Entregable

Guarda en `portfolio/091-calidad-y-variabilidad/`:

- `operating-improvement-brief.md` con el problema específico de **calidad y variabilidad**, evidencia, alternativas, decisión y gobernanza;
- `reading-note.md` contrastando las fuentes de **calidad y variabilidad** con edición/páginas consultadas;
- `decision-journal.md` registrando los supuestos de **quality**, confianza, responsable y revisión;
- `red-team.md` con la objeción más fuerte al caso **Un call center sanciona agentes cada vez que el tiempo medio sube, aunque el patrón aumenta simultáneamente en todos por un sistema lento. Se trata una causa común como problema individual.** y el dato que podría invalidar la recomendación.

## 📗 Fuentes y verificación

- Nigel Slack & Alistair Brandon-Jones — *Operations Management* (Pearson Education, Limited, 2019). **Uso en esta clase:** capacidad, procesos, variabilidad, calidad y estrategia de operaciones. Lectura selectiva sobre **calidad y variabilidad**. **Localizador:** [ISBN-13 9781292254036](https://openlibrary.org/isbn/9781292254036).
- Eliyahu M. Goldratt & Jeff Cox — *The Goal* (HighBridge Audio, 2014). **Uso en esta clase:** restricciones, throughput, inventario y pensamiento de flujo. Lectura selectiva sobre **calidad y variabilidad**. **Localizador:** [ISBN-13 9781622313945](https://openlibrary.org/isbn/9781622313945).
- James P. Womack & Daniel T. Jones — *Lean Thinking* (Free Press, 2003). **Uso en esta clase:** valor, flujo, pull, desperdicio y mejora continua. Lectura selectiva sobre **calidad y variabilidad**. **Localizador:** [ISBN-13 9780743231640](https://openlibrary.org/isbn/9780743231640).
- Jeffrey K. Liker — *The Toyota Way* (American Media International, 2005). **Uso en esta clase:** perspectiva de Operaciones aplicada al problema de la clase. Lectura selectiva sobre **calidad y variabilidad**. **Localizador:** [ISBN-13 9781932378702](https://openlibrary.org/isbn/9781932378702).
- ISO — *ISO 9001 Quality management systems*. **Uso en esta clase:** gestión de calidad basada en procesos, evidencia y mejora. **Localizador pendiente:** ver [el registro de fuentes](../../../../docs/FUENTES.md).
- Michael Hammer & James Champy — *Reengineering the Corporation* (HarperBusiness, 2001). **Uso en esta clase:** perspectiva de Procesos aplicada al problema de la clase. Lectura selectiva sobre **calidad y variabilidad**. **Localizador:** [ISBN-13 9780066621128](https://openlibrary.org/isbn/9780066621128).
- Susan A. Ambrose et al. — *How Learning Works* (John Wiley & Sons, Incorporated, 2010). **Uso en esta clase:** diseñar los objetivos, la práctica y el feedback de **calidad y variabilidad** sobre conocimiento previo verificable. **Localizador:** [ISBN-13 9780470617601](https://openlibrary.org/isbn/9780470617601).
- Peter C. Brown, Henry L. Roediger III & Mark A. McDaniel — *Make It Stick* (Harvard University Press, 2014). **Uso en esta clase:** justificar la recuperación inicial y las preguntas de comprobación de **calidad y variabilidad**. **Localizador:** [ISBN-13 9780674986572](https://openlibrary.org/isbn/9780674986572).
- Grant Wiggins & Jay McTighe — *Understanding by Design* (Pearson Education, Inc., 2006). **Uso en esta clase:** derivar el entregable de **calidad y variabilidad** desde el desempeño observable y no desde el temario. **Localizador:** [ISBN-13 9780131950849](https://openlibrary.org/isbn/9780131950849).
- Anders Ericsson & Robert Pool — *Peak* (Penguin Random House, 2016). **Uso en esta clase:** convertir la práctica de **calidad y variabilidad** en práctica deliberada con criterios explícitos. **Localizador:** [ISBN-13 9781473513143](https://openlibrary.org/isbn/9781473513143).
- William Ellet — *The Case Study Handbook* (Harvard Business Review Press, 2018). **Uso en esta clase:** estructurar el caso ejecutivo de **calidad y variabilidad** como problema, evidencia, alternativas y recomendación. **Localizador:** [ISBN-13 9781633696150](https://openlibrary.org/isbn/9781633696150).

> **Regla de fuentes para Calidad y variabilidad:** las obras anteriores estructuran las perspectivas de esta materia; cualquier norma, ley, impuesto o estándar vivo mencionado en **calidad y variabilidad** debe comprobarse nuevamente en su fuente primaria vigente. El desarrollo es original y no reproduce capítulos protegidos.
