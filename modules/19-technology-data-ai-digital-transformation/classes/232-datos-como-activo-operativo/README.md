# Clase 232 — Datos como activo operativo

**Parte:** 19 — Tecnología, datos, IA y transformación digital para ejecutivos  
**Nivel:** Etapa 5 — CEO → Transformador digital  
**Duración sugerida:** 150–180 minutos · **Estándar:** deep-class-v2

## 🎯 Propósito

Tratar datos como activo operativo requiere calidad, ownership, arquitectura, semántica, acceso y lineage. Su valor aparece cuando reducen incertidumbre o habilitan decisiones y productos; acumular datos sin propósito aumenta costo, privacidad y superficie de ataque.

La salida de esta parte es **gobernar tecnología, datos e IA como capacidades económicas y organizacionales**. En esta clase, esa progresión se concreta al exigir que cada afirmación sobre **datos como activo operativo** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

## 📚 Resultados de aprendizaje

Al finalizar podrás:

1. **Distinguir** `data product`, `data quality`, `data owner`, `lineage`, `single source of truth` mediante observables, no por memoria verbal.
2. **Explicar** por qué esas distinciones cambian una decisión de ceo → transformador digital.
3. **Aplicar** la secuencia **1. identificar decisiones y productos de datos → 2. definir dominios y owners → 3. establecer calidad y contracts → 4. habilitar acceso con governance → 5. medir uso incidents y value** conservando supuestos, alternativas y trazabilidad.
4. **Interpretar** data quality SLA, time-to-data, duplicate definitions sin confundir señal, explicación y causalidad.
5. **Resolver** el caso ejecutivo con al menos dos opciones plausibles y un criterio explícito de stop/revisión.
6. **Contrastar** dos obras de referencia y explicar dónde sus lentes son complementarias o entran en tensión.

## 🧭 Agenda

| Tramo | Evidencia de aprendizaje |
|---|---|
| 0–20 min | Recuperación: define data product y data quality sin mirar la tabla; corrige con la fuente. |
| 20–70 min | Lectura guiada de conceptos + contraste de dos referencias. |
| 70–115 min | Ejemplo trabajado con data quality SLA y trazabilidad de supuestos. |
| 115–155 min | Caso ejecutivo: dos alternativas, trade-offs y decisión provisional. |
| 155–180 min | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar comprensión |
|---|---|---|
| **data product** | conjunto gestionado de datos con usuarios owner SLA y propósito | Distingue un hecho compatible y otro que lo refute. |
| **data quality** | grado de exactitud completitud oportunidad y consistencia | Distingue un hecho compatible y otro que lo refute. |
| **data owner** | rol accountable por definición y uso de un dominio | Distingue un hecho compatible y otro que lo refute. |
| **lineage** | trazabilidad desde origen a transformación y consumo | Distingue un hecho compatible y otro que lo refute. |
| **single source of truth** | fuente autorizada para una definición específica | Distingue un hecho compatible y otro que lo refute. |

## 🧠 Modelo mental

```text
1. identificar decisiones y productos de datos → 2. definir dominios y owners → 3. establecer calidad y contracts → 4. habilitar acceso con governance → 5. medir uso incidents y value
```

La secuencia nace del problema de esta clase: **Tratar datos como activo operativo requiere calidad, ownership, arquitectura, semántica, acceso y lineage. Su valor aparece cuando reducen incertidumbre o habilitan decisiones y productos; acumular datos sin propósito aumenta costo, privacidad y superficie de ataque.** El método es útil mientras las condiciones permitan observar las señales requeridas. No elimina incertidumbre; la hace visible y obliga a decidir proporcionalmente a la evidencia. Límite principal: **Una única fuente física no siempre es necesaria; lo crítico es semántica y governance. Evita centralización total si destruye velocidad sin mejorar consistencia.**

## 📖 Desarrollo

### 1. data product: mecanismo central

**data product** se entiende aquí como **conjunto gestionado de datos con usuarios owner SLA y propósito**. Esta es la pieza causal o estructural desde la que se inicia **datos como activo operativo**: antes de identificar decisiones y productos de datos, el gerente debe poder señalar qué cambia en el sistema si el concepto está presente y qué debería observar si no lo está. Una definición que no produce predicciones observables todavía es demasiado vaga para dirigir.

La lectura rectora de este bloque es Marco Iansiti & Karim R. Lakhani — *Competing in the Age of AI*. Su aporte se usa para examinar **modelo operativo AI-first, escala digital, redes y arquitectura de decisión**. Aplica esa lente al caso sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **data quality SLA**; regístrala con periodo, unidad, población y baseline.

Relaciona el mecanismo con **data quality**. Si ambos cambian juntos, no concluyas causalidad automáticamente: identifica una tercera variable o mecanismo alternativo que también pueda explicar el patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. data quality: frontera conceptual y error de clasificación

**Definición operacional:** grado de exactitud completitud oportunidad y consistencia. Su valor está en distinguirlo de **data product** y **data owner**. En una decisión real, clasificar una situación en la categoría equivocada cambia la intervención: puedes asignar autoridad donde faltaba información, medir un output cuando debías observar un proceso o tratar una restricción como si fuera una preferencia.

Contrasta el problema con Thomas H. Davenport & Nitin Mittal — *All-In on AI*, que aporta una mirada sobre **casos empresariales, estrategia y organización para inteligencia artificial**. Formula dos mini-casos: uno que sí satisface la definición de **data quality** y otro que solo se parece superficialmente. Luego pregunta qué señal distinguiría ambos; para esta clase, **time-to-data** es una candidata, pero debe combinarse con evidencia cualitativa o documental cuando el fenómeno no sea directamente medible.

Antes de definir dominios y owners, registra explícitamente qué decisión sería errónea si esta frontera conceptual se ignora. Esa frase convierte el vocabulario en criterio gerencial.

### 3. data owner: operacionalización y medición

**data owner** significa **rol accountable por definición y uso de un dominio**. El problema ya no es definirlo, sino **operacionalizarlo**: qué contar, durante qué ventana, con qué denominador, contra qué baseline y con qué segmentación. Una métrica útil conserva suficiente contexto para no confundir mejora local con mejora del sistema.

Andrew McAfee & Erik Brynjolfsson — *Machine, Platform, Crowd* orienta este bloque mediante **perspectiva de Economía digital aplicada al problema de la clase**. Usa esa perspectiva para diseñar una ficha de medición: `señal → fórmula/criterio → fuente → frecuencia → owner → interpretación permitida → interpretación prohibida`. La señal asignada es **duplicate definitions**. Si no existe un dato confiable, la salida correcta no es inventar precisión: diseña el mecanismo de captura y declara la incertidumbre.

Al llegar a establecer calidad y contracts, compara tendencia, distribución y casos atípicos. Pregunta además si el indicador es *leading* o *lagging* y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; nunca convertirse en el objetivo que reemplaza al fenómeno.

### 4. lineage: trade-offs y efectos de segundo orden

**Definición:** trazabilidad desde origen a transformación y consumo. Este concepto obliga a abandonar la idea de que **datos como activo operativo** tiene una solución gratuita. Toda intervención consume autonomía, tiempo, caja, capacidad, atención, reputación o tolerancia al riesgo. Por eso, antes de habilitar acceso con governance, se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Thomas H. Davenport & Jeanne G. Harris — *Competing on Analytics* aporta una lente sobre **perspectiva de Datos aplicada al problema de la clase**. Úsala para construir una matriz `beneficio / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **data incidents** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la necesidad de observar efectos laterales fuera del KPI principal.

Haz un *pre-mortem* de **datos como activo operativo**: supone que la opción recomendada fracasó seis meses después y enumera tres mecanismos que podrían explicarlo. Al menos uno debe provenir de un efecto de segundo orden asociado a **lineage** y otro de una hipótesis del caso que nunca fue validada.

### 5. single source of truth: gobernanza, límites e integración

**single source of truth** se define como **fuente autorizada para una definición específica** y cierra el circuito porque traduce análisis en responsabilidad. La pregunta ejecutiva es quién decide, quién ejecuta, quién debe ser consultado, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar.

NIST — *Cybersecurity Framework (CSF) 2.0* se utiliza para estudiar **gobierno, identificación, protección, detección, respuesta y recuperación en ciberseguridad** y contrastar la recomendación final. Al ejecutar medir uso incidents y value, deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento. Esa trazabilidad protege contra el sesgo retrospectivo y mejora las revisiones posteriores.

La frontera de esta clase es explícita: **Una única fuente física no siempre es necesaria; lo crítico es semántica y governance. Evita centralización total si destruye velocidad sin mejorar consistencia.**. Conviértela en una regla operativa: `si ocurre X → no aplicar automáticamente → consultar/escalar/revalidar`. Integrar **data product**, **data quality**, **data owner**, **lineage** y **single source of truth** significa poder explicar qué parte del diagnóstico sostiene la decisión y cuál sigue siendo una apuesta.

### 6. Integración: de conceptos a una decisión defendible

La síntesis de **datos como activo operativo** no consiste en sumar cinco definiciones. Empieza por **data product**, contrasta **data quality** con **data owner**, incorpora **lineage** como restricción o mecanismo y usa **single source of truth** para cerrar el ciclo. Si el análisis no puede explicar cuál de esas piezas cambió la recomendación, todavía no hay comprensión transferible.

Aplica ahora la secuencia **1. identificar decisiones y productos de datos → 2. definir dominios y owners → 3. establecer calidad y contracts → 4. habilitar acceso con governance → 5. medir uso incidents y value**. Para cada paso conserva tres columnas: evidencia utilizada, alternativa descartada y razón. Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado y evita reescribir la historia después de conocer el desenlace.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla señala el lente que debes buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Marco Iansiti & Karim R. Lakhani — *Competing in the Age of AI* | modelo operativo AI-first, escala digital, redes y arquitectura de decisión | ¿Qué supuesto de **datos como activo operativo** ayuda a desafiar? |
| Thomas H. Davenport & Nitin Mittal — *All-In on AI* | casos empresariales, estrategia y organización para inteligencia artificial | ¿Qué supuesto de **datos como activo operativo** ayuda a desafiar? |
| Andrew McAfee & Erik Brynjolfsson — *Machine, Platform, Crowd* | perspectiva de Economía digital aplicada al problema de la clase | ¿Qué supuesto de **datos como activo operativo** ayuda a desafiar? |
| Thomas H. Davenport & Jeanne G. Harris — *Competing on Analytics* | perspectiva de Datos aplicada al problema de la clase | ¿Qué supuesto de **datos como activo operativo** ayuda a desafiar? |
| NIST — *Cybersecurity Framework (CSF) 2.0* | gobierno, identificación, protección, detección, respuesta y recuperación en ciberseguridad | ¿Qué supuesto de **datos como activo operativo** ayuda a desafiar? |

En **datos como activo operativo**, la lectura se evalúa por **uso**, no por cantidad de páginas. La nota debe indicar qué tesis de las fuentes modifica tu lectura de **data product**, qué evidencia del caso tensiona esa tesis y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación:** Ventas y finanzas reportan ARR distinto porque cada una define renovación y FX de forma diferente. Ambos dashboards son técnicamente correctos según su lógica.

**Paso 1 — identificar decisiones y productos de datos.** La gerencia escribe primero el supuesto asociado a **data product** y evita convertirlo en hecho. Luego busca **data quality SLA** para contrastarlo en el caso de **datos como activo operativo**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 2 — definir dominios y owners.** La gerencia escribe primero el supuesto asociado a **data quality** y evita convertirlo en hecho. Luego busca **time-to-data** para contrastarlo en el caso de **datos como activo operativo**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 3 — establecer calidad y contracts.** La gerencia escribe primero el supuesto asociado a **data owner** y evita convertirlo en hecho. Luego busca **duplicate definitions** para contrastarlo en el caso de **datos como activo operativo**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 4 — habilitar acceso con governance.** La gerencia escribe primero el supuesto asociado a **lineage** y evita convertirlo en hecho. Luego busca **data incidents** para contrastarlo en el caso de **datos como activo operativo**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 5 — medir uso incidents y value.** La gerencia escribe primero el supuesto asociado a **single source of truth** y evita convertirlo en hecho. Luego busca **decision adoption** para contrastarlo en el caso de **datos como activo operativo**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Síntesis del caso.** La recomendación debe terminar con responsable, fecha, evidencia de éxito y señal de stop. En **datos como activo operativo**, omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo |
|---|---|---|---|
| **data product** | conjunto gestionado de datos con usuarios owner SLA y propósito | Cuando data quality SLA es observable y accionable. | Sobrerreaccionar a una señal parcial. |
| **data quality** | grado de exactitud completitud oportunidad y consistencia | Cuando la primera explicación no distingue mecanismo o responsabilidad. | Convertir el concepto en etiqueta. |
| **Experimento/revisión** | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar eternamente y no decidir. |
| **Escalamiento** | Elevar autoridad o especialidad | Cuando hay derechos, capital material, regulación o irreversibilidad. | Delegar hacia arriba lo que sí corresponde decidir. |

**Frontera de aplicación:** Una única fuente física no siempre es necesaria; lo crítico es semántica y governance. Evita centralización total si destruye velocidad sin mejorar consistencia.

## 🪜 De profesional a owner

| Nivel | Responsabilidad sobre datos como activo operativo |
|---|---|
| **Profesional** | usa **datos como activo operativo** para mejorar una contribución propia y explicar sus supuestos con evidencia. |
| **Jefe / Team Lead** | aplica **data product** y **data quality** para coordinar personas sin sustituir conversación por métricas. |
| **Manager / Gerente** | conecta data quality SLA con capacidad, presupuesto, dependencias y riesgo interáreas. |
| **CEO / Director** | decide si datos como activo operativo cambia estrategia, economía o riesgo de empresa y qué debe llegar al comité o directorio. |
| **Founder / Owner** | pregunta si la solución de datos como activo operativo reduce dependencia del fundador, preserva caja y puede operar como sistema repetible. |

El cambio de nivel en **datos como activo operativo** aumenta el número de personas, dinero, dependencias y consecuencias que quedan dentro de la decisión. Por eso la misma herramienta debe volverse más explícita en evidencia, gobernanza y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Ventas y finanzas reportan ARR distinto porque cada una define renovación y FX de forma diferente. Ambos dashboards son técnicamente correctos según su lógica.

Entrega un **decision brief de datos como activo operativo** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre personas, cliente, operación, caja y riesgo; (e) recomendación; (f) condición que haría cambiarla; (g) dueño y fecha de revisión. Utiliza al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica

1. Reconstruye el caso de **datos como activo operativo** con una tabla `hecho / interpretación / hipótesis / decisión`.
2. Ejecuta **1. identificar decisiones y productos de datos → 2. definir dominios y owners → 3. establecer calidad y contracts → 4. habilitar acceso con governance → 5. medir uso incidents y value** y adjunta evidencia para cada transición entre pasos.
3. Calcula o documenta data quality SLA, time-to-data; si no existe dato, diseña cómo obtenerlo.
4. Escribe una alternativa que contradiga tu preferencia inicial y haz un *pre-mortem* específico del caso.
5. Lee dos referencias, registra una coincidencia y una tensión, y modifica el brief si corresponde.
6. Repite la decisión desde el rol de CEO/owner: identifica qué cambia al aumentar el alcance y la irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar data product y data quality como sinónimos | Se pierde la distinción entre “conjunto gestionado de datos con usuarios owner SLA y propósito” y “grado de exactitud completitud oportunidad y consistencia” | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por “medir uso incidents y value” | Se saltó “identificar decisiones y productos de datos” y la solución llegó antes que el diagnóstico | Reconstruye la cadena 1. identificar decisiones y productos de datos → 2. definir dominios y owners → 3. establecer calidad y contracts → 4. habilitar acceso con governance → 5. medir uso incidents y value y marca el primer supuesto no demostrado. |
| Optimizar solo data quality SLA | La métrica local sustituyó al resultado del sistema | Contrástala con time-to-data y explicita el costo de oportunidad. |
| Generalizar desde un caso favorable | Se confundió evidencia local con una regla universal sobre datos como activo operativo | Una única fuente física no siempre es necesaria; lo crítico es semántica y governance. Evita centralización total si destruye velocidad sin mejorar consistencia. |
| No fijar revisión | Una decisión sobre datos como activo operativo se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de stop. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **data product** y **data quality** usando un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **data owner** y qué observación obligaría a rechazar tu interpretación?
3. Aplica **identificar decisiones y productos de datos → definir dominios y owners** al caso de la clase. ¿Qué dato todavía falta?
4. ¿Por qué **data quality SLA** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la tabla de lectura. ¿Dónde podrían llevar a recomendaciones distintas para **datos como activo operativo**?
6. ¿Qué decisión equivocada podría producirse si se ignora este límite: **Una única fuente física no siempre es necesaria; lo crítico es semántica y governance. Evita centralización total si destruye velocidad sin mejorar consistencia.**?

## 📥 Entregable

Guarda en `portfolio/232-datos-como-activo-operativo/`:

- `leadership-decision-brief.md` con el problema específico de **datos como activo operativo**, evidencia, alternativas, decisión y gobernanza;
- `reading-note.md` contrastando las fuentes de **datos como activo operativo** con edición/páginas consultadas;
- `decision-journal.md` registrando los supuestos de **data product**, confianza, responsable y revisión;
- `red-team.md` con la objeción más fuerte al caso **Ventas y finanzas reportan ARR distinto porque cada una define renovación y FX de forma diferente. Ambos dashboards son técnicamente correctos según su lógica.** y el dato que podría invalidar la recomendación.

## 📗 Fuentes y verificación

- Marco Iansiti & Karim R. Lakhani — *Competing in the Age of AI*. **Uso en esta clase:** modelo operativo AI-first, escala digital, redes y arquitectura de decisión. Lectura selectiva: índice/capítulos pertinentes a **datos como activo operativo**; registra edición y páginas consultadas.
- Thomas H. Davenport & Nitin Mittal — *All-In on AI*. **Uso en esta clase:** casos empresariales, estrategia y organización para inteligencia artificial. Lectura selectiva: índice/capítulos pertinentes a **datos como activo operativo**; registra edición y páginas consultadas.
- Andrew McAfee & Erik Brynjolfsson — *Machine, Platform, Crowd*. **Uso en esta clase:** perspectiva de Economía digital aplicada al problema de la clase. Lectura selectiva: índice/capítulos pertinentes a **datos como activo operativo**; registra edición y páginas consultadas.
- Thomas H. Davenport & Jeanne G. Harris — *Competing on Analytics*. **Uso en esta clase:** perspectiva de Datos aplicada al problema de la clase. Lectura selectiva: índice/capítulos pertinentes a **datos como activo operativo**; registra edición y páginas consultadas.
- NIST — *Cybersecurity Framework (CSF) 2.0*. **Uso en esta clase:** gobierno, identificación, protección, detección, respuesta y recuperación en ciberseguridad. Lectura selectiva: índice/capítulos pertinentes a **datos como activo operativo**; registra edición y páginas consultadas.
- George Westerman, Didier Bonnet & Andrew McAfee — *Leading Digital*. **Uso en esta clase:** transformación digital desde capacidades de liderazgo y capacidades digitales. Lectura selectiva: índice/capítulos pertinentes a **datos como activo operativo**; registra edición y páginas consultadas.
- Susan A. Ambrose et al. — *How Learning Works*. **Uso en esta clase:** diseñar los objetivos, la práctica y el feedback de **datos como activo operativo** sobre conocimiento previo verificable.
- Peter C. Brown, Henry L. Roediger III & Mark A. McDaniel — *Make It Stick*. **Uso en esta clase:** justificar la recuperación inicial y las preguntas de comprobación de **datos como activo operativo**.
- Grant Wiggins & Jay McTighe — *Understanding by Design*. **Uso en esta clase:** derivar el entregable de **datos como activo operativo** desde el desempeño observable y no desde el temario.
- Anders Ericsson & Robert Pool — *Peak*. **Uso en esta clase:** convertir la práctica de **datos como activo operativo** en práctica deliberada con criterios explícitos.
- William Ellet — *The Case Study Handbook*. **Uso en esta clase:** estructurar el caso ejecutivo de **datos como activo operativo** como problema, evidencia, alternativas y recomendación.

> **Regla de fuentes para Datos como activo operativo:** las obras anteriores estructuran las perspectivas de esta materia; cualquier norma, ley, impuesto o estándar vivo mencionado en **datos como activo operativo** debe comprobarse nuevamente en su fuente primaria vigente. El desarrollo es original y no reproduce capítulos protegidos.
