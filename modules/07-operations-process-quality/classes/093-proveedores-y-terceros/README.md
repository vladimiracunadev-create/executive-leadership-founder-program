# Clase 093 — Proveedores y terceros

**Parte:** 07 — Operaciones, procesos y calidad  
**Nivel:** Etapa 2 — Jefe → Manager  
**Duración sugerida:** 150–180 minutos · **Estándar:** deep-class-v2

## 🎯 Propósito

Gestionar proveedores y terceros extiende responsabilidad más allá de la frontera legal de la empresa. Debe evaluar criticidad, concentración, contratos, niveles de servicio, seguridad, continuidad y salida. El proveedor ejecuta; la organización sigue siendo responsable de su propia promesa al cliente.

La salida de esta parte es **operar procesos end-to-end con capacidad, calidad, continuidad y mejora**. En esta clase, esa progresión se concreta al exigir que cada afirmación sobre **proveedores y terceros** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

## 📚 Resultados de aprendizaje

Al finalizar podrás:

1. **Distinguir** `third-party risk`, `criticality`, `concentration risk`, `exit plan`, `SLA` mediante observables, no por memoria verbal.
2. **Explicar** por qué esas distinciones cambian una decisión de jefe → manager.
3. **Aplicar** la secuencia **1. clasificar terceros por criticidad → 2. hacer due diligence proporcional → 3. definir contratos y controles → 4. monitorear performance y riesgo → 5. probar exit y continuidad** conservando supuestos, alternativas y trazabilidad.
4. **Interpretar** SLA breaches, concentración de gasto, incidentes de terceros sin confundir señal, explicación y causalidad.
5. **Resolver** el caso ejecutivo con al menos dos opciones plausibles y un criterio explícito de stop/revisión.
6. **Contrastar** dos obras de referencia y explicar dónde sus lentes son complementarias o entran en tensión.

## 🧭 Agenda

| Tramo | Evidencia de aprendizaje |
|---|---|
| 0–20 min | Recuperación: define third-party risk y criticality sin mirar la tabla; corrige con la fuente. |
| 20–70 min | Lectura guiada de conceptos + contraste de dos referencias. |
| 70–115 min | Ejemplo trabajado con SLA breaches y trazabilidad de supuestos. |
| 115–155 min | Caso ejecutivo: dos alternativas, trade-offs y decisión provisional. |
| 155–180 min | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar comprensión |
|---|---|---|
| **third-party risk** | riesgo introducido por dependencia de un proveedor o socio | Distingue un hecho compatible y otro que lo refute. |
| **criticality** | impacto si el tercero falla | Distingue un hecho compatible y otro que lo refute. |
| **concentration risk** | dependencia excesiva de un proveedor, región o tecnología | Distingue un hecho compatible y otro que lo refute. |
| **exit plan** | capacidad práctica de terminar o migrar la relación | Distingue un hecho compatible y otro que lo refute. |
| **SLA** | compromiso de nivel de servicio con medición y remedios | Distingue un hecho compatible y otro que lo refute. |

## 🧠 Modelo mental

```text
1. clasificar terceros por criticidad → 2. hacer due diligence proporcional → 3. definir contratos y controles → 4. monitorear performance y riesgo → 5. probar exit y continuidad
```

La secuencia nace del problema de esta clase: **Gestionar proveedores y terceros extiende responsabilidad más allá de la frontera legal de la empresa. Debe evaluar criticidad, concentración, contratos, niveles de servicio, seguridad, continuidad y salida. El proveedor ejecuta; la organización sigue siendo responsable de su propia promesa al cliente.** El método es útil mientras las condiciones permitan observar las señales requeridas. No elimina incertidumbre; la hace visible y obliga a decidir proporcionalmente a la evidencia. Límite principal: **Duplicar proveedores no siempre es económico ni reduce riesgo si comparten la misma infraestructura. Analiza concentración real y costo de salida, no solo número de contratos.**

## 📖 Desarrollo

### 1. third-party risk: mecanismo central

**third-party risk** se entiende aquí como **riesgo introducido por dependencia de un proveedor o socio**. Esta es la pieza causal o estructural desde la que se inicia **proveedores y terceros**: antes de clasificar terceros por criticidad, el gerente debe poder señalar qué cambia en el sistema si el concepto está presente y qué debería observar si no lo está. Una definición que no produce predicciones observables todavía es demasiado vaga para dirigir.

La lectura rectora de este bloque es Nigel Slack & Alistair Brandon-Jones — *Operations Management*. Su aporte se usa para examinar **capacidad, procesos, variabilidad, calidad y estrategia de operaciones**. Aplica esa lente al caso sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **SLA breaches**; regístrala con periodo, unidad, población y baseline.

Relaciona el mecanismo con **criticality**. Si ambos cambian juntos, no concluyas causalidad automáticamente: identifica una tercera variable o mecanismo alternativo que también pueda explicar el patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. criticality: frontera conceptual y error de clasificación

**Definición operacional:** impacto si el tercero falla. Su valor está en distinguirlo de **third-party risk** y **concentration risk**. En una decisión real, clasificar una situación en la categoría equivocada cambia la intervención: puedes asignar autoridad donde faltaba información, medir un output cuando debías observar un proceso o tratar una restricción como si fuera una preferencia.

Contrasta el problema con Eliyahu M. Goldratt & Jeff Cox — *The Goal*, que aporta una mirada sobre **restricciones, throughput, inventario y pensamiento de flujo**. Formula dos mini-casos: uno que sí satisface la definición de **criticality** y otro que solo se parece superficialmente. Luego pregunta qué señal distinguiría ambos; para esta clase, **concentración de gasto** es una candidata, pero debe combinarse con evidencia cualitativa o documental cuando el fenómeno no sea directamente medible.

Antes de hacer due diligence proporcional, registra explícitamente qué decisión sería errónea si esta frontera conceptual se ignora. Esa frase convierte el vocabulario en criterio gerencial.

### 3. concentration risk: operacionalización y medición

**concentration risk** significa **dependencia excesiva de un proveedor, región o tecnología**. El problema ya no es definirlo, sino **operacionalizarlo**: qué contar, durante qué ventana, con qué denominador, contra qué baseline y con qué segmentación. Una métrica útil conserva suficiente contexto para no confundir mejora local con mejora del sistema.

Geary A. Rummler & Alan P. Brache — *Improving Performance* orienta este bloque mediante **perspectiva de Procesos aplicada al problema de la clase**. Usa esa perspectiva para diseñar una ficha de medición: `señal → fórmula/criterio → fuente → frecuencia → owner → interpretación permitida → interpretación prohibida`. La señal asignada es **incidentes de terceros**. Si no existe un dato confiable, la salida correcta no es inventar precisión: diseña el mecanismo de captura y declara la incertidumbre.

Al llegar a definir contratos y controles, compara tendencia, distribución y casos atípicos. Pregunta además si el indicador es *leading* o *lagging* y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; nunca convertirse en el objetivo que reemplaza al fenómeno.

### 4. exit plan: trade-offs y efectos de segundo orden

**Definición:** capacidad práctica de terminar o migrar la relación. Este concepto obliga a abandonar la idea de que **proveedores y terceros** tiene una solución gratuita. Toda intervención consume autonomía, tiempo, caja, capacidad, atención, reputación o tolerancia al riesgo. Por eso, antes de monitorear performance y riesgo, se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

ISO — *ISO 9001 Quality management systems* aporta una lente sobre **gestión de calidad basada en procesos, evidencia y mejora**. Úsala para construir una matriz `beneficio / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **tiempo de reemplazo** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la necesidad de observar efectos laterales fuera del KPI principal.

Haz un *pre-mortem* de **proveedores y terceros**: supone que la opción recomendada fracasó seis meses después y enumera tres mecanismos que podrían explicarlo. Al menos uno debe provenir de un efecto de segundo orden asociado a **exit plan** y otro de una hipótesis del caso que nunca fue validada.

### 5. SLA: gobernanza, límites e integración

**SLA** se define como **compromiso de nivel de servicio con medición y remedios** y cierra el circuito porque traduce análisis en responsabilidad. La pregunta ejecutiva es quién decide, quién ejecuta, quién debe ser consultado, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar.

Michael Hammer & James Champy — *Reengineering the Corporation* se utiliza para estudiar **perspectiva de Procesos aplicada al problema de la clase** y contrastar la recomendación final. Al ejecutar probar exit y continuidad, deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento. Esa trazabilidad protege contra el sesgo retrospectivo y mejora las revisiones posteriores.

La frontera de esta clase es explícita: **Duplicar proveedores no siempre es económico ni reduce riesgo si comparten la misma infraestructura. Analiza concentración real y costo de salida, no solo número de contratos.**. Conviértela en una regla operativa: `si ocurre X → no aplicar automáticamente → consultar/escalar/revalidar`. Integrar **third-party risk**, **criticality**, **concentration risk**, **exit plan** y **SLA** significa poder explicar qué parte del diagnóstico sostiene la decisión y cuál sigue siendo una apuesta.

### 6. Integración: de conceptos a una decisión defendible

La síntesis de **proveedores y terceros** no consiste en sumar cinco definiciones. Empieza por **third-party risk**, contrasta **criticality** con **concentration risk**, incorpora **exit plan** como restricción o mecanismo y usa **SLA** para cerrar el ciclo. Si el análisis no puede explicar cuál de esas piezas cambió la recomendación, todavía no hay comprensión transferible.

Aplica ahora la secuencia **1. clasificar terceros por criticidad → 2. hacer due diligence proporcional → 3. definir contratos y controles → 4. monitorear performance y riesgo → 5. probar exit y continuidad**. Para cada paso conserva tres columnas: evidencia utilizada, alternativa descartada y razón. Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado y evita reescribir la historia después de conocer el desenlace.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla señala el lente que debes buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Nigel Slack & Alistair Brandon-Jones — *Operations Management* | capacidad, procesos, variabilidad, calidad y estrategia de operaciones | ¿Qué supuesto de **proveedores y terceros** ayuda a desafiar? |
| Eliyahu M. Goldratt & Jeff Cox — *The Goal* | restricciones, throughput, inventario y pensamiento de flujo | ¿Qué supuesto de **proveedores y terceros** ayuda a desafiar? |
| Geary A. Rummler & Alan P. Brache — *Improving Performance* | perspectiva de Procesos aplicada al problema de la clase | ¿Qué supuesto de **proveedores y terceros** ayuda a desafiar? |
| ISO — *ISO 9001 Quality management systems* | gestión de calidad basada en procesos, evidencia y mejora | ¿Qué supuesto de **proveedores y terceros** ayuda a desafiar? |
| Michael Hammer & James Champy — *Reengineering the Corporation* | perspectiva de Procesos aplicada al problema de la clase | ¿Qué supuesto de **proveedores y terceros** ayuda a desafiar? |

En **proveedores y terceros**, la lectura se evalúa por **uso**, no por cantidad de páginas. La nota debe indicar qué tesis de las fuentes modifica tu lectura de **third-party risk**, qué evidencia del caso tensiona esa tesis y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación:** El core de pagos depende de un único SaaS sin plan de exportación de datos. El precio sube 80% y la empresa descubre que migrar requiere nueve meses.

**Paso 1 — clasificar terceros por criticidad.** La gerencia escribe primero el supuesto asociado a **third-party risk** y evita convertirlo en hecho. Luego busca **SLA breaches** para contrastarlo en el caso de **proveedores y terceros**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 2 — hacer due diligence proporcional.** La gerencia escribe primero el supuesto asociado a **criticality** y evita convertirlo en hecho. Luego busca **concentración de gasto** para contrastarlo en el caso de **proveedores y terceros**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 3 — definir contratos y controles.** La gerencia escribe primero el supuesto asociado a **concentration risk** y evita convertirlo en hecho. Luego busca **incidentes de terceros** para contrastarlo en el caso de **proveedores y terceros**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 4 — monitorear performance y riesgo.** La gerencia escribe primero el supuesto asociado a **exit plan** y evita convertirlo en hecho. Luego busca **tiempo de reemplazo** para contrastarlo en el caso de **proveedores y terceros**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 5 — probar exit y continuidad.** La gerencia escribe primero el supuesto asociado a **SLA** y evita convertirlo en hecho. Luego busca **controles pendientes** para contrastarlo en el caso de **proveedores y terceros**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Síntesis del caso.** La recomendación debe terminar con responsable, fecha, evidencia de éxito y señal de stop. En **proveedores y terceros**, omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo |
|---|---|---|---|
| **third-party risk** | riesgo introducido por dependencia de un proveedor o socio | Cuando SLA breaches es observable y accionable. | Sobrerreaccionar a una señal parcial. |
| **criticality** | impacto si el tercero falla | Cuando la primera explicación no distingue mecanismo o responsabilidad. | Convertir el concepto en etiqueta. |
| **Experimento/revisión** | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar eternamente y no decidir. |
| **Escalamiento** | Elevar autoridad o especialidad | Cuando hay derechos, capital material, regulación o irreversibilidad. | Delegar hacia arriba lo que sí corresponde decidir. |

**Frontera de aplicación:** Duplicar proveedores no siempre es económico ni reduce riesgo si comparten la misma infraestructura. Analiza concentración real y costo de salida, no solo número de contratos.

## 🪜 De profesional a owner

| Nivel | Responsabilidad sobre proveedores y terceros |
|---|---|
| **Profesional** | usa **proveedores y terceros** para mejorar una contribución propia y explicar sus supuestos con evidencia. |
| **Jefe / Team Lead** | aplica **third-party risk** y **criticality** para coordinar personas sin sustituir conversación por métricas. |
| **Manager / Gerente** | conecta SLA breaches con capacidad, presupuesto, dependencias y riesgo interáreas. |
| **CEO / Director** | decide si proveedores y terceros cambia estrategia, economía o riesgo de empresa y qué debe llegar al comité o directorio. |
| **Founder / Owner** | pregunta si la solución de proveedores y terceros reduce dependencia del fundador, preserva caja y puede operar como sistema repetible. |

El cambio de nivel en **proveedores y terceros** aumenta el número de personas, dinero, dependencias y consecuencias que quedan dentro de la decisión. Por eso la misma herramienta debe volverse más explícita en evidencia, gobernanza y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

El core de pagos depende de un único SaaS sin plan de exportación de datos. El precio sube 80% y la empresa descubre que migrar requiere nueve meses.

Entrega un **decision brief de proveedores y terceros** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre personas, cliente, operación, caja y riesgo; (e) recomendación; (f) condición que haría cambiarla; (g) dueño y fecha de revisión. Utiliza al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica

1. Reconstruye el caso de **proveedores y terceros** con una tabla `hecho / interpretación / hipótesis / decisión`.
2. Ejecuta **1. clasificar terceros por criticidad → 2. hacer due diligence proporcional → 3. definir contratos y controles → 4. monitorear performance y riesgo → 5. probar exit y continuidad** y adjunta evidencia para cada transición entre pasos.
3. Calcula o documenta SLA breaches, concentración de gasto; si no existe dato, diseña cómo obtenerlo.
4. Escribe una alternativa que contradiga tu preferencia inicial y haz un *pre-mortem* específico del caso.
5. Lee dos referencias, registra una coincidencia y una tensión, y modifica el brief si corresponde.
6. Repite la decisión desde el rol de CEO/owner: identifica qué cambia al aumentar el alcance y la irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar third-party risk y criticality como sinónimos | Se pierde la distinción entre “riesgo introducido por dependencia de un proveedor o socio” y “impacto si el tercero falla” | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por “probar exit y continuidad” | Se saltó “clasificar terceros por criticidad” y la solución llegó antes que el diagnóstico | Reconstruye la cadena 1. clasificar terceros por criticidad → 2. hacer due diligence proporcional → 3. definir contratos y controles → 4. monitorear performance y riesgo → 5. probar exit y continuidad y marca el primer supuesto no demostrado. |
| Optimizar solo SLA breaches | La métrica local sustituyó al resultado del sistema | Contrástala con concentración de gasto y explicita el costo de oportunidad. |
| Generalizar desde un caso favorable | Se confundió evidencia local con una regla universal sobre proveedores y terceros | Duplicar proveedores no siempre es económico ni reduce riesgo si comparten la misma infraestructura. Analiza concentración real y costo de salida, no solo número de contratos. |
| No fijar revisión | Una decisión sobre proveedores y terceros se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de stop. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **third-party risk** y **criticality** usando un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **concentration risk** y qué observación obligaría a rechazar tu interpretación?
3. Aplica **clasificar terceros por criticidad → hacer due diligence proporcional** al caso de la clase. ¿Qué dato todavía falta?
4. ¿Por qué **SLA breaches** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la tabla de lectura. ¿Dónde podrían llevar a recomendaciones distintas para **proveedores y terceros**?
6. ¿Qué decisión equivocada podría producirse si se ignora este límite: **Duplicar proveedores no siempre es económico ni reduce riesgo si comparten la misma infraestructura. Analiza concentración real y costo de salida, no solo número de contratos.**?

## 📥 Entregable

Guarda en `portfolio/093-proveedores-y-terceros/`:

- `leadership-decision-brief.md` con el problema específico de **proveedores y terceros**, evidencia, alternativas, decisión y gobernanza;
- `reading-note.md` contrastando las fuentes de **proveedores y terceros** con edición/páginas consultadas;
- `decision-journal.md` registrando los supuestos de **third-party risk**, confianza, responsable y revisión;
- `red-team.md` con la objeción más fuerte al caso **El core de pagos depende de un único SaaS sin plan de exportación de datos. El precio sube 80% y la empresa descubre que migrar requiere nueve meses.** y el dato que podría invalidar la recomendación.

## 📗 Fuentes y verificación

- Nigel Slack & Alistair Brandon-Jones — *Operations Management* (Pearson Education, Limited, 2019). **Uso en esta clase:** capacidad, procesos, variabilidad, calidad y estrategia de operaciones. Lectura selectiva sobre **proveedores y terceros**. **Localizador:** [ISBN-13 9781292254036](https://openlibrary.org/isbn/9781292254036).
- Eliyahu M. Goldratt & Jeff Cox — *The Goal* (HighBridge Audio, 2014). **Uso en esta clase:** restricciones, throughput, inventario y pensamiento de flujo. Lectura selectiva sobre **proveedores y terceros**. **Localizador:** [ISBN-13 9781622313945](https://openlibrary.org/isbn/9781622313945).
- Geary A. Rummler & Alan P. Brache — *Improving Performance* (Jossey-Bass, 1995). **Uso en esta clase:** perspectiva de Procesos aplicada al problema de la clase. Lectura selectiva sobre **proveedores y terceros**. **Localizador:** [ISBN-13 9780787900908](https://openlibrary.org/isbn/9780787900908).
- ISO — *ISO 9001 Quality management systems*. **Uso en esta clase:** gestión de calidad basada en procesos, evidencia y mejora. **Localizador pendiente:** ver [el registro de fuentes](../../../../docs/FUENTES.md).
- Michael Hammer & James Champy — *Reengineering the Corporation* (HarperBusiness, 2001). **Uso en esta clase:** perspectiva de Procesos aplicada al problema de la clase. Lectura selectiva sobre **proveedores y terceros**. **Localizador:** [ISBN-13 9780066621128](https://openlibrary.org/isbn/9780066621128).
- James P. Womack & Daniel T. Jones — *Lean Thinking* (Free Press, 2003). **Uso en esta clase:** valor, flujo, pull, desperdicio y mejora continua. Lectura selectiva sobre **proveedores y terceros**. **Localizador:** [ISBN-13 9780743231640](https://openlibrary.org/isbn/9780743231640).
- Susan A. Ambrose et al. — *How Learning Works* (John Wiley & Sons, Incorporated, 2010). **Uso en esta clase:** diseñar los objetivos, la práctica y el feedback de **proveedores y terceros** sobre conocimiento previo verificable. **Localizador:** [ISBN-13 9780470617601](https://openlibrary.org/isbn/9780470617601).
- Peter C. Brown, Henry L. Roediger III & Mark A. McDaniel — *Make It Stick* (Harvard University Press, 2014). **Uso en esta clase:** justificar la recuperación inicial y las preguntas de comprobación de **proveedores y terceros**. **Localizador:** [ISBN-13 9780674986572](https://openlibrary.org/isbn/9780674986572).
- Grant Wiggins & Jay McTighe — *Understanding by Design* (Pearson Education, Inc., 2006). **Uso en esta clase:** derivar el entregable de **proveedores y terceros** desde el desempeño observable y no desde el temario. **Localizador:** [ISBN-13 9780131950849](https://openlibrary.org/isbn/9780131950849).
- Anders Ericsson & Robert Pool — *Peak* (Penguin Random House, 2016). **Uso en esta clase:** convertir la práctica de **proveedores y terceros** en práctica deliberada con criterios explícitos. **Localizador:** [ISBN-13 9781473513143](https://openlibrary.org/isbn/9781473513143).
- William Ellet — *The Case Study Handbook* (Harvard Business Review Press, 2018). **Uso en esta clase:** estructurar el caso ejecutivo de **proveedores y terceros** como problema, evidencia, alternativas y recomendación. **Localizador:** [ISBN-13 9781633696150](https://openlibrary.org/isbn/9781633696150).

> **Regla de fuentes para Proveedores y terceros:** las obras anteriores estructuran las perspectivas de esta materia; cualquier norma, ley, impuesto o estándar vivo mencionado en **proveedores y terceros** debe comprobarse nuevamente en su fuente primaria vigente. El desarrollo es original y no reproduce capítulos protegidos.
