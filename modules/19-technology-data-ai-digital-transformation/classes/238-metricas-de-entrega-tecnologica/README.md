# Clase 238 — Métricas de entrega tecnológica

**Parte:** 19 — Tecnología, datos, IA y transformación digital para ejecutivos  
**Nivel:** Etapa 5 — CEO → Transformador digital  
**Duración sugerida:** 150–180 minutos · **Estándar:** deep-class-v2

## 🎯 Propósito

Métricas de entrega tecnológica deben conectar velocidad y estabilidad. DORA popularizó deployment frequency, lead time, change failure rate y recovery; ninguna métrica aislada define productividad y comparaciones entre contextos distintos requieren cautela.

La salida de esta parte es **gobernar tecnología, datos e IA como capacidades económicas y organizacionales**. En esta clase, esa progresión se concreta al exigir que cada afirmación sobre **métricas de entrega tecnológica** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

## 📚 Resultados de aprendizaje

Al finalizar podrás:

1. **Distinguir** `deployment frequency`, `lead time for changes`, `change failure rate`, `time to restore`, `developer experience` mediante observables, no por memoria verbal.
2. **Explicar** por qué esas distinciones cambian una decisión de ceo → transformador digital.
3. **Aplicar** la secuencia **1. definir flujo de valor de software → 2. instrumentar velocidad y estabilidad → 3. segmentar por producto y contexto → 4. identificar constraint → 5. experimentar mejora y medir outcome** conservando supuestos, alternativas y trazabilidad.
4. **Interpretar** deployment frequency, lead time, change failure rate sin confundir señal, explicación y causalidad.
5. **Resolver** el caso ejecutivo con al menos dos opciones plausibles y un criterio explícito de stop/revisión.
6. **Contrastar** dos obras de referencia y explicar dónde sus lentes son complementarias o entran en tensión.

## 🧭 Agenda

| Tramo | Evidencia de aprendizaje |
|---|---|
| 0–20 min | Recuperación: define deployment frequency y lead time for changes sin mirar la tabla; corrige con la fuente. |
| 20–70 min | Lectura guiada de conceptos + contraste de dos referencias. |
| 70–115 min | Ejemplo trabajado con deployment frequency y trazabilidad de supuestos. |
| 115–155 min | Caso ejecutivo: dos alternativas, trade-offs y decisión provisional. |
| 155–180 min | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar comprensión |
|---|---|---|
| **deployment frequency** | frecuencia con que cambios llegan a producción | Distingue un hecho compatible y otro que lo refute. |
| **lead time for changes** | tiempo desde cambio hasta producción | Distingue un hecho compatible y otro que lo refute. |
| **change failure rate** | proporción de cambios que causan degradación o incidente | Distingue un hecho compatible y otro que lo refute. |
| **time to restore** | tiempo para recuperar servicio tras fallo | Distingue un hecho compatible y otro que lo refute. |
| **developer experience** | condiciones que afectan capacidad de entregar software de forma efectiva | Distingue un hecho compatible y otro que lo refute. |

## 🧠 Modelo mental

```text
1. definir flujo de valor de software → 2. instrumentar velocidad y estabilidad → 3. segmentar por producto y contexto → 4. identificar constraint → 5. experimentar mejora y medir outcome
```

La secuencia nace del problema de esta clase: **Métricas de entrega tecnológica deben conectar velocidad y estabilidad. DORA popularizó deployment frequency, lead time, change failure rate y recovery; ninguna métrica aislada define productividad y comparaciones entre contextos distintos requieren cautela.** El método es útil mientras las condiciones permitan observar las señales requeridas. No elimina incertidumbre; la hace visible y obliga a decidir proporcionalmente a la evidencia. Límite principal: **No conviertas DORA en cuota individual. Son señales de sistema y deben interpretarse con calidad, seguridad, customer outcomes y contexto.**

## 📖 Desarrollo

### 1. deployment frequency: mecanismo central

**deployment frequency** se entiende aquí como **frecuencia con que cambios llegan a producción**. Esta es la pieza causal o estructural desde la que se inicia **métricas de entrega tecnológica**: antes de definir flujo de valor de software, el gerente debe poder señalar qué cambia en el sistema si el concepto está presente y qué debería observar si no lo está. Una definición que no produce predicciones observables todavía es demasiado vaga para dirigir.

La lectura rectora de este bloque es Marco Iansiti & Karim R. Lakhani — *Competing in the Age of AI*. Su aporte se usa para examinar **modelo operativo AI-first, escala digital, redes y arquitectura de decisión**. Aplica esa lente al caso sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **deployment frequency**; regístrala con periodo, unidad, población y baseline.

Relaciona el mecanismo con **lead time for changes**. Si ambos cambian juntos, no concluyas causalidad automáticamente: identifica una tercera variable o mecanismo alternativo que también pueda explicar el patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. lead time for changes: frontera conceptual y error de clasificación

**Definición operacional:** tiempo desde cambio hasta producción. Su valor está en distinguirlo de **deployment frequency** y **change failure rate**. En una decisión real, clasificar una situación en la categoría equivocada cambia la intervención: puedes asignar autoridad donde faltaba información, medir un output cuando debías observar un proceso o tratar una restricción como si fuera una preferencia.

Contrasta el problema con Thomas H. Davenport & Nitin Mittal — *All-In on AI*, que aporta una mirada sobre **casos empresariales, estrategia y organización para inteligencia artificial**. Formula dos mini-casos: uno que sí satisface la definición de **lead time for changes** y otro que solo se parece superficialmente. Luego pregunta qué señal distinguiría ambos; para esta clase, **lead time** es una candidata, pero debe combinarse con evidencia cualitativa o documental cuando el fenómeno no sea directamente medible.

Antes de instrumentar velocidad y estabilidad, registra explícitamente qué decisión sería errónea si esta frontera conceptual se ignora. Esa frase convierte el vocabulario en criterio gerencial.

### 3. change failure rate: operacionalización y medición

**change failure rate** significa **proporción de cambios que causan degradación o incidente**. El problema ya no es definirlo, sino **operacionalizarlo**: qué contar, durante qué ventana, con qué denominador, contra qué baseline y con qué segmentación. Una métrica útil conserva suficiente contexto para no confundir mejora local con mejora del sistema.

NIST — *AI Risk Management Framework (AI RMF 1.0)* orienta este bloque mediante **gobierno y gestión de riesgos de IA confiable a lo largo del ciclo de vida**. Usa esa perspectiva para diseñar una ficha de medición: `señal → fórmula/criterio → fuente → frecuencia → owner → interpretación permitida → interpretación prohibida`. La señal asignada es **change failure rate**. Si no existe un dato confiable, la salida correcta no es inventar precisión: diseña el mecanismo de captura y declara la incertidumbre.

Al llegar a segmentar por producto y contexto, compara tendencia, distribución y casos atípicos. Pregunta además si el indicador es *leading* o *lagging* y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; nunca convertirse en el objetivo que reemplaza al fenómeno.

### 4. time to restore: trade-offs y efectos de segundo orden

**Definición:** tiempo para recuperar servicio tras fallo. Este concepto obliga a abandonar la idea de que **métricas de entrega tecnológica** tiene una solución gratuita. Toda intervención consume autonomía, tiempo, caja, capacidad, atención, reputación o tolerancia al riesgo. Por eso, antes de identificar constraint, se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

George Westerman, Didier Bonnet & Andrew McAfee — *Leading Digital* aporta una lente sobre **transformación digital desde capacidades de liderazgo y capacidades digitales**. Úsala para construir una matriz `beneficio / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **recovery time** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la necesidad de observar efectos laterales fuera del KPI principal.

Haz un *pre-mortem* de **métricas de entrega tecnológica**: supone que la opción recomendada fracasó seis meses después y enumera tres mecanismos que podrían explicarlo. Al menos uno debe provenir de un efecto de segundo orden asociado a **time to restore** y otro de una hipótesis del caso que nunca fue validada.

### 5. developer experience: gobernanza, límites e integración

**developer experience** se define como **condiciones que afectan capacidad de entregar software de forma efectiva** y cierra el circuito porque traduce análisis en responsabilidad. La pregunta ejecutiva es quién decide, quién ejecuta, quién debe ser consultado, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar.

Nicole Forsgren, Jez Humble & Gene Kim — *Accelerate* se utiliza para estudiar **métricas de entrega, capacidades técnicas y desempeño organizacional** y contrastar la recomendación final. Al ejecutar experimentar mejora y medir outcome, deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento. Esa trazabilidad protege contra el sesgo retrospectivo y mejora las revisiones posteriores.

La frontera de esta clase es explícita: **No conviertas DORA en cuota individual. Son señales de sistema y deben interpretarse con calidad, seguridad, customer outcomes y contexto.**. Conviértela en una regla operativa: `si ocurre X → no aplicar automáticamente → consultar/escalar/revalidar`. Integrar **deployment frequency**, **lead time for changes**, **change failure rate**, **time to restore** y **developer experience** significa poder explicar qué parte del diagnóstico sostiene la decisión y cuál sigue siendo una apuesta.

### 6. Integración: de conceptos a una decisión defendible

La síntesis de **métricas de entrega tecnológica** no consiste en sumar cinco definiciones. Empieza por **deployment frequency**, contrasta **lead time for changes** con **change failure rate**, incorpora **time to restore** como restricción o mecanismo y usa **developer experience** para cerrar el ciclo. Si el análisis no puede explicar cuál de esas piezas cambió la recomendación, todavía no hay comprensión transferible.

Aplica ahora la secuencia **1. definir flujo de valor de software → 2. instrumentar velocidad y estabilidad → 3. segmentar por producto y contexto → 4. identificar constraint → 5. experimentar mejora y medir outcome**. Para cada paso conserva tres columnas: evidencia utilizada, alternativa descartada y razón. Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado y evita reescribir la historia después de conocer el desenlace.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla señala el lente que debes buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Marco Iansiti & Karim R. Lakhani — *Competing in the Age of AI* | modelo operativo AI-first, escala digital, redes y arquitectura de decisión | ¿Qué supuesto de **métricas de entrega tecnológica** ayuda a desafiar? |
| Thomas H. Davenport & Nitin Mittal — *All-In on AI* | casos empresariales, estrategia y organización para inteligencia artificial | ¿Qué supuesto de **métricas de entrega tecnológica** ayuda a desafiar? |
| NIST — *AI Risk Management Framework (AI RMF 1.0)* | gobierno y gestión de riesgos de IA confiable a lo largo del ciclo de vida | ¿Qué supuesto de **métricas de entrega tecnológica** ayuda a desafiar? |
| George Westerman, Didier Bonnet & Andrew McAfee — *Leading Digital* | transformación digital desde capacidades de liderazgo y capacidades digitales | ¿Qué supuesto de **métricas de entrega tecnológica** ayuda a desafiar? |
| Nicole Forsgren, Jez Humble & Gene Kim — *Accelerate* | métricas de entrega, capacidades técnicas y desempeño organizacional | ¿Qué supuesto de **métricas de entrega tecnológica** ayuda a desafiar? |

En **métricas de entrega tecnológica**, la lectura se evalúa por **uso**, no por cantidad de páginas. La nota debe indicar qué tesis de las fuentes modifica tu lectura de **deployment frequency**, qué evidencia del caso tensiona esa tesis y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación:** Un CTO presiona por más deployments; el equipo divide cambios artificialmente y sube frecuencia 3x mientras incidentes y lead time total empeoran.

**Paso 1 — definir flujo de valor de software.** La gerencia escribe primero el supuesto asociado a **deployment frequency** y evita convertirlo en hecho. Luego busca **deployment frequency** para contrastarlo en el caso de **métricas de entrega tecnológica**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 2 — instrumentar velocidad y estabilidad.** La gerencia escribe primero el supuesto asociado a **lead time for changes** y evita convertirlo en hecho. Luego busca **lead time** para contrastarlo en el caso de **métricas de entrega tecnológica**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 3 — segmentar por producto y contexto.** La gerencia escribe primero el supuesto asociado a **change failure rate** y evita convertirlo en hecho. Luego busca **change failure rate** para contrastarlo en el caso de **métricas de entrega tecnológica**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 4 — identificar constraint.** La gerencia escribe primero el supuesto asociado a **time to restore** y evita convertirlo en hecho. Luego busca **recovery time** para contrastarlo en el caso de **métricas de entrega tecnológica**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 5 — experimentar mejora y medir outcome.** La gerencia escribe primero el supuesto asociado a **developer experience** y evita convertirlo en hecho. Luego busca **developer satisfaction** para contrastarlo en el caso de **métricas de entrega tecnológica**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Síntesis del caso.** La recomendación debe terminar con responsable, fecha, evidencia de éxito y señal de stop. En **métricas de entrega tecnológica**, omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo |
|---|---|---|---|
| **deployment frequency** | frecuencia con que cambios llegan a producción | Cuando deployment frequency es observable y accionable. | Sobrerreaccionar a una señal parcial. |
| **lead time for changes** | tiempo desde cambio hasta producción | Cuando la primera explicación no distingue mecanismo o responsabilidad. | Convertir el concepto en etiqueta. |
| **Experimento/revisión** | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar eternamente y no decidir. |
| **Escalamiento** | Elevar autoridad o especialidad | Cuando hay derechos, capital material, regulación o irreversibilidad. | Delegar hacia arriba lo que sí corresponde decidir. |

**Frontera de aplicación:** No conviertas DORA en cuota individual. Son señales de sistema y deben interpretarse con calidad, seguridad, customer outcomes y contexto.

## 🪜 De profesional a owner

| Nivel | Responsabilidad sobre métricas de entrega tecnológica |
|---|---|
| **Profesional** | usa **métricas de entrega tecnológica** para mejorar una contribución propia y explicar sus supuestos con evidencia. |
| **Jefe / Team Lead** | aplica **deployment frequency** y **lead time for changes** para coordinar personas sin sustituir conversación por métricas. |
| **Manager / Gerente** | conecta deployment frequency con capacidad, presupuesto, dependencias y riesgo interáreas. |
| **CEO / Director** | decide si métricas de entrega tecnológica cambia estrategia, economía o riesgo de empresa y qué debe llegar al comité o directorio. |
| **Founder / Owner** | pregunta si la solución de métricas de entrega tecnológica reduce dependencia del fundador, preserva caja y puede operar como sistema repetible. |

El cambio de nivel en **métricas de entrega tecnológica** aumenta el número de personas, dinero, dependencias y consecuencias que quedan dentro de la decisión. Por eso la misma herramienta debe volverse más explícita en evidencia, gobernanza y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Un CTO presiona por más deployments; el equipo divide cambios artificialmente y sube frecuencia 3x mientras incidentes y lead time total empeoran.

Entrega un **decision brief de métricas de entrega tecnológica** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre personas, cliente, operación, caja y riesgo; (e) recomendación; (f) condición que haría cambiarla; (g) dueño y fecha de revisión. Utiliza al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica

1. Reconstruye el caso de **métricas de entrega tecnológica** con una tabla `hecho / interpretación / hipótesis / decisión`.
2. Ejecuta **1. definir flujo de valor de software → 2. instrumentar velocidad y estabilidad → 3. segmentar por producto y contexto → 4. identificar constraint → 5. experimentar mejora y medir outcome** y adjunta evidencia para cada transición entre pasos.
3. Calcula o documenta deployment frequency, lead time; si no existe dato, diseña cómo obtenerlo.
4. Escribe una alternativa que contradiga tu preferencia inicial y haz un *pre-mortem* específico del caso.
5. Lee dos referencias, registra una coincidencia y una tensión, y modifica el brief si corresponde.
6. Repite la decisión desde el rol de CEO/owner: identifica qué cambia al aumentar el alcance y la irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar deployment frequency y lead time for changes como sinónimos | Se pierde la distinción entre “frecuencia con que cambios llegan a producción” y “tiempo desde cambio hasta producción” | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por “experimentar mejora y medir outcome” | Se saltó “definir flujo de valor de software” y la solución llegó antes que el diagnóstico | Reconstruye la cadena 1. definir flujo de valor de software → 2. instrumentar velocidad y estabilidad → 3. segmentar por producto y contexto → 4. identificar constraint → 5. experimentar mejora y medir outcome y marca el primer supuesto no demostrado. |
| Optimizar solo deployment frequency | La métrica local sustituyó al resultado del sistema | Contrástala con lead time y explicita el costo de oportunidad. |
| Generalizar desde un caso favorable | Se confundió evidencia local con una regla universal sobre métricas de entrega tecnológica | No conviertas DORA en cuota individual. Son señales de sistema y deben interpretarse con calidad, seguridad, customer outcomes y contexto. |
| No fijar revisión | Una decisión sobre métricas de entrega tecnológica se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de stop. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **deployment frequency** y **lead time for changes** usando un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **change failure rate** y qué observación obligaría a rechazar tu interpretación?
3. Aplica **definir flujo de valor de software → instrumentar velocidad y estabilidad** al caso de la clase. ¿Qué dato todavía falta?
4. ¿Por qué **deployment frequency** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la tabla de lectura. ¿Dónde podrían llevar a recomendaciones distintas para **métricas de entrega tecnológica**?
6. ¿Qué decisión equivocada podría producirse si se ignora este límite: **No conviertas DORA en cuota individual. Son señales de sistema y deben interpretarse con calidad, seguridad, customer outcomes y contexto.**?

## 📥 Entregable

Guarda en `portfolio/238-metricas-de-entrega-tecnologica/`:

- `leadership-decision-brief.md` con el problema específico de **métricas de entrega tecnológica**, evidencia, alternativas, decisión y gobernanza;
- `reading-note.md` contrastando las fuentes de **métricas de entrega tecnológica** con edición/páginas consultadas;
- `decision-journal.md` registrando los supuestos de **deployment frequency**, confianza, responsable y revisión;
- `red-team.md` con la objeción más fuerte al caso **Un CTO presiona por más deployments; el equipo divide cambios artificialmente y sube frecuencia 3x mientras incidentes y lead time total empeoran.** y el dato que podría invalidar la recomendación.

## 📗 Fuentes y verificación

- Marco Iansiti & Karim R. Lakhani — *Competing in the Age of AI* (Harvard Business Review Press, 2020). **Uso en esta clase:** modelo operativo AI-first, escala digital, redes y arquitectura de decisión. Lectura selectiva sobre **métricas de entrega tecnológica**. **Localizador:** [ISBN-13 9781633697621](https://openlibrary.org/isbn/9781633697621).
- Thomas H. Davenport & Nitin Mittal — *All-In on AI* (Harvard Business Review Press, 2022). **Uso en esta clase:** casos empresariales, estrategia y organización para inteligencia artificial. Lectura selectiva sobre **métricas de entrega tecnológica**. **Localizador:** [ISBN-13 9781647824693](https://openlibrary.org/isbn/9781647824693).
- NIST — *AI Risk Management Framework (AI RMF 1.0)*. **Uso en esta clase:** gobierno y gestión de riesgos de IA confiable a lo largo del ciclo de vida. **Fuente primaria:** <https://www.nist.gov/itl/ai-risk-management-framework>.
- George Westerman, Didier Bonnet & Andrew McAfee — *Leading Digital* (Harvard Business Review Press, 2014). **Uso en esta clase:** transformación digital desde capacidades de liderazgo y capacidades digitales. Lectura selectiva sobre **métricas de entrega tecnológica**. **Localizador:** [ISBN-13 9781625272478](https://openlibrary.org/isbn/9781625272478).
- Nicole Forsgren, Jez Humble & Gene Kim — *Accelerate* (IT Revolution Press, 2018). **Uso en esta clase:** métricas de entrega, capacidades técnicas y desempeño organizacional. Lectura selectiva sobre **métricas de entrega tecnológica**. **Localizador:** [ISBN-13 9781942788379](https://openlibrary.org/isbn/9781942788379).
- Thomas H. Davenport & Jeanne G. Harris — *Competing on Analytics* (Harvard Business School Press, 2007). **Uso en esta clase:** perspectiva de Datos aplicada al problema de la clase. Lectura selectiva sobre **métricas de entrega tecnológica**. **Localizador:** [ISBN-13 9781422103326](https://openlibrary.org/isbn/9781422103326).
- Susan A. Ambrose et al. — *How Learning Works* (John Wiley & Sons, Incorporated, 2010). **Uso en esta clase:** diseñar los objetivos, la práctica y el feedback de **métricas de entrega tecnológica** sobre conocimiento previo verificable. **Localizador:** [ISBN-13 9780470617601](https://openlibrary.org/isbn/9780470617601).
- Peter C. Brown, Henry L. Roediger III & Mark A. McDaniel — *Make It Stick* (Harvard University Press, 2014). **Uso en esta clase:** justificar la recuperación inicial y las preguntas de comprobación de **métricas de entrega tecnológica**. **Localizador:** [ISBN-13 9780674986572](https://openlibrary.org/isbn/9780674986572).
- Grant Wiggins & Jay McTighe — *Understanding by Design* (Pearson Education, Inc., 2006). **Uso en esta clase:** derivar el entregable de **métricas de entrega tecnológica** desde el desempeño observable y no desde el temario. **Localizador:** [ISBN-13 9780131950849](https://openlibrary.org/isbn/9780131950849).
- Anders Ericsson & Robert Pool — *Peak* (Penguin Random House, 2016). **Uso en esta clase:** convertir la práctica de **métricas de entrega tecnológica** en práctica deliberada con criterios explícitos. **Localizador:** [ISBN-13 9781473513143](https://openlibrary.org/isbn/9781473513143).
- William Ellet — *The Case Study Handbook* (Harvard Business Review Press, 2018). **Uso en esta clase:** estructurar el caso ejecutivo de **métricas de entrega tecnológica** como problema, evidencia, alternativas y recomendación. **Localizador:** [ISBN-13 9781633696150](https://openlibrary.org/isbn/9781633696150).

> **Regla de fuentes para Métricas de entrega tecnológica:** las obras anteriores estructuran las perspectivas de esta materia; cualquier norma, ley, impuesto o estándar vivo mencionado en **métricas de entrega tecnológica** debe comprobarse nuevamente en su fuente primaria vigente. El desarrollo es original y no reproduce capítulos protegidos.
