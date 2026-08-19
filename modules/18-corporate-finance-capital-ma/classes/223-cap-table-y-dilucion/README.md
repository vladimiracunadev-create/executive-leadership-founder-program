# Clase 223 — Cap table y dilución

**Parte:** 18 — Finanzas corporativas, capital y M&A  
**Nivel:** Etapa 5 — CEO → Capital allocator  
**Duración sugerida:** 150–180 minutos · **Estándar:** deep-class-v2

## 🎯 Propósito

Cap table muestra quién posee qué y cómo opciones, convertibles y nuevas rondas alteran propiedad. El founder debe comprender fully diluted ownership, option pool y escenarios de dilución antes de firmar; porcentajes nominales sin waterfall pueden engañar.

La salida de esta parte es **decidir estructura de capital, valoración, fundraising y transacciones**. En esta clase, esa progresión se concreta al exigir que cada afirmación sobre **cap table y dilución** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

## 📚 Resultados de aprendizaje

Al finalizar podrás:

1. **Distinguir** `cap table`, `fully diluted`, `option pool`, `pre-money valuation`, `post-money valuation` mediante observables, no por memoria verbal.
2. **Explicar** por qué esas distinciones cambian una decisión de ceo → capital allocator.
3. **Aplicar** la secuencia **1. limpiar cap table actual → 2. convertir a fully diluted → 3. modelar nueva emisión y pool → 4. calcular ownership post-money → 5. simular rondas y exits** conservando supuestos, alternativas y trazabilidad.
4. **Interpretar** founder ownership, investor ownership, option pool sin confundir señal, explicación y causalidad.
5. **Resolver** el caso ejecutivo con al menos dos opciones plausibles y un criterio explícito de stop/revisión.
6. **Contrastar** dos obras de referencia y explicar dónde sus lentes son complementarias o entran en tensión.

## 🧭 Agenda

| Tramo | Evidencia de aprendizaje |
|---|---|
| 0–20 min | Recuperación: define cap table y fully diluted sin mirar la tabla; corrige con la fuente. |
| 20–70 min | Lectura guiada de conceptos + contraste de dos referencias. |
| 70–115 min | Ejemplo trabajado con founder ownership y trazabilidad de supuestos. |
| 115–155 min | Caso ejecutivo: dos alternativas, trade-offs y decisión provisional. |
| 155–180 min | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar comprensión |
|---|---|---|
| **cap table** | registro de ownership y securities de una compañía | Distingue un hecho compatible y otro que lo refute. |
| **fully diluted** | propiedad asumiendo ejercicio o conversión de instrumentos relevantes | Distingue un hecho compatible y otro que lo refute. |
| **option pool** | acciones reservadas para incentivos de empleados | Distingue un hecho compatible y otro que lo refute. |
| **pre-money valuation** | valor antes del nuevo capital | Distingue un hecho compatible y otro que lo refute. |
| **post-money valuation** | pre-money más inversión nueva | Distingue un hecho compatible y otro que lo refute. |

## 🧠 Modelo mental

```text
1. limpiar cap table actual → 2. convertir a fully diluted → 3. modelar nueva emisión y pool → 4. calcular ownership post-money → 5. simular rondas y exits
```

La secuencia nace del problema de esta clase: **Cap table muestra quién posee qué y cómo opciones, convertibles y nuevas rondas alteran propiedad. El founder debe comprender fully diluted ownership, option pool y escenarios de dilución antes de firmar; porcentajes nominales sin waterfall pueden engañar.** El método es útil mientras las condiciones permitan observar las señales requeridas. No elimina incertidumbre; la hace visible y obliga a decidir proporcionalmente a la evidencia. Límite principal: **Cap tables legales pueden incluir preferencias y derechos complejos. Usa modelo para comprender economía, pero valida documentos y conversiones con asesoría legal o financiera.**

## 📖 Desarrollo

### 1. cap table: mecanismo central

**cap table** se entiende aquí como **registro de ownership y securities de una compañía**. Esta es la pieza causal o estructural desde la que se inicia **cap table y dilución**: antes de limpiar cap table actual, el gerente debe poder señalar qué cambia en el sistema si el concepto está presente y qué debería observar si no lo está. Una definición que no produce predicciones observables todavía es demasiado vaga para dirigir.

La lectura rectora de este bloque es Richard Brealey, Stewart Myers & Franklin Allen — *Principles of Corporate Finance*. Su aporte se usa para examinar **valor del dinero, riesgo, costo de capital, inversión y financiación**. Aplica esa lente al caso sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **founder ownership**; regístrala con periodo, unidad, población y baseline.

Relaciona el mecanismo con **fully diluted**. Si ambos cambian juntos, no concluyas causalidad automáticamente: identifica una tercera variable o mecanismo alternativo que también pueda explicar el patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. fully diluted: frontera conceptual y error de clasificación

**Definición operacional:** propiedad asumiendo ejercicio o conversión de instrumentos relevantes. Su valor está en distinguirlo de **cap table** y **option pool**. En una decisión real, clasificar una situación en la categoría equivocada cambia la intervención: puedes asignar autoridad donde faltaba información, medir un output cuando debías observar un proceso o tratar una restricción como si fuera una preferencia.

Contrasta el problema con Stephen Ross, Randolph Westerfield et al. — *Corporate Finance*, que aporta una mirada sobre **decisiones de inversión, financiación, capital de trabajo y valoración**. Formula dos mini-casos: uno que sí satisface la definición de **fully diluted** y otro que solo se parece superficialmente. Luego pregunta qué señal distinguiría ambos; para esta clase, **investor ownership** es una candidata, pero debe combinarse con evidencia cualitativa o documental cuando el fenómeno no sea directamente medible.

Antes de convertir a fully diluted, registra explícitamente qué decisión sería errónea si esta frontera conceptual se ignora. Esa frase convierte el vocabulario en criterio gerencial.

### 3. option pool: operacionalización y medición

**option pool** significa **acciones reservadas para incentivos de empleados**. El problema ya no es definirlo, sino **operacionalizarlo**: qué contar, durante qué ventana, con qué denominador, contra qué baseline y con qué segmentación. Una métrica útil conserva suficiente contexto para no confundir mejora local con mejora del sistema.

Brad Feld & Jason Mendelson — *Venture Deals* orienta este bloque mediante **term sheets, economics/control y negociación de venture capital**. Usa esa perspectiva para diseñar una ficha de medición: `señal → fórmula/criterio → fuente → frecuencia → owner → interpretación permitida → interpretación prohibida`. La señal asignada es **option pool**. Si no existe un dato confiable, la salida correcta no es inventar precisión: diseña el mecanismo de captura y declara la incertidumbre.

Al llegar a modelar nueva emisión y pool, compara tendencia, distribución y casos atípicos. Pregunta además si el indicador es *leading* o *lagging* y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; nunca convertirse en el objetivo que reemplaza al fenómeno.

### 4. pre-money valuation: trade-offs y efectos de segundo orden

**Definición:** valor antes del nuevo capital. Este concepto obliga a abandonar la idea de que **cap table y dilución** tiene una solución gratuita. Toda intervención consume autonomía, tiempo, caja, capacidad, atención, reputación o tolerancia al riesgo. Por eso, antes de calcular ownership post-money, se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

OECD — *G20/OECD Principles of Corporate Governance 2023* aporta una lente sobre **derechos de accionistas, directorio, disclosure, sostenibilidad y buen gobierno**. Úsala para construir una matriz `beneficio / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **dilution per round** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la necesidad de observar efectos laterales fuera del KPI principal.

Haz un *pre-mortem* de **cap table y dilución**: supone que la opción recomendada fracasó seis meses después y enumera tres mecanismos que podrían explicarlo. Al menos uno debe provenir de un efecto de segundo orden asociado a **pre-money valuation** y otro de una hipótesis del caso que nunca fue validada.

### 5. post-money valuation: gobernanza, límites e integración

**post-money valuation** se define como **pre-money más inversión nueva** y cierra el circuito porque traduce análisis en responsabilidad. La pregunta ejecutiva es quién decide, quién ejecuta, quién debe ser consultado, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar.

Noam Wasserman — *The Founder's Dilemmas* se utiliza para estudiar **dilemas de fundador, equity, control, equipo y decisiones tempranas** y contrastar la recomendación final. Al ejecutar simular rondas y exits, deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento. Esa trazabilidad protege contra el sesgo retrospectivo y mejora las revisiones posteriores.

La frontera de esta clase es explícita: **Cap tables legales pueden incluir preferencias y derechos complejos. Usa modelo para comprender economía, pero valida documentos y conversiones con asesoría legal o financiera.**. Conviértela en una regla operativa: `si ocurre X → no aplicar automáticamente → consultar/escalar/revalidar`. Integrar **cap table**, **fully diluted**, **option pool**, **pre-money valuation** y **post-money valuation** significa poder explicar qué parte del diagnóstico sostiene la decisión y cuál sigue siendo una apuesta.

### 6. Integración: de conceptos a una decisión defendible

La síntesis de **cap table y dilución** no consiste en sumar cinco definiciones. Empieza por **cap table**, contrasta **fully diluted** con **option pool**, incorpora **pre-money valuation** como restricción o mecanismo y usa **post-money valuation** para cerrar el ciclo. Si el análisis no puede explicar cuál de esas piezas cambió la recomendación, todavía no hay comprensión transferible.

Aplica ahora la secuencia **1. limpiar cap table actual → 2. convertir a fully diluted → 3. modelar nueva emisión y pool → 4. calcular ownership post-money → 5. simular rondas y exits**. Para cada paso conserva tres columnas: evidencia utilizada, alternativa descartada y razón. Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado y evita reescribir la historia después de conocer el desenlace.

## 🔧 Profundización específica

### Cap table y dilución

Trabaja siempre en base fully diluted cuando corresponda y distingue pre-money/post-money. Si una empresa vale 8 pre-money y recibe 2, post-money = 10; el nuevo inversor tendría 20 % antes de considerar otros ajustes. Una ampliación de option pool pre-money puede diluir principalmente a founders existentes.

Modela rondas sucesivas, options, convertibles/SAFEs según términos reales y escenarios de salida. Porcentajes sin número de acciones y derechos pueden ocultar errores.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla señala el lente que debes buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Richard Brealey, Stewart Myers & Franklin Allen — *Principles of Corporate Finance* | valor del dinero, riesgo, costo de capital, inversión y financiación | ¿Qué supuesto de **cap table y dilución** ayuda a desafiar? |
| Stephen Ross, Randolph Westerfield et al. — *Corporate Finance* | decisiones de inversión, financiación, capital de trabajo y valoración | ¿Qué supuesto de **cap table y dilución** ayuda a desafiar? |
| Brad Feld & Jason Mendelson — *Venture Deals* | term sheets, economics/control y negociación de venture capital | ¿Qué supuesto de **cap table y dilución** ayuda a desafiar? |
| OECD — *G20/OECD Principles of Corporate Governance 2023* | derechos de accionistas, directorio, disclosure, sostenibilidad y buen gobierno | ¿Qué supuesto de **cap table y dilución** ayuda a desafiar? |
| Noam Wasserman — *The Founder's Dilemmas* | dilemas de fundador, equity, control, equipo y decisiones tempranas | ¿Qué supuesto de **cap table y dilución** ayuda a desafiar? |

En **cap table y dilución**, la lectura se evalúa por **uso**, no por cantidad de páginas. La nota debe indicar qué tesis de las fuentes modifica tu lectura de **cap table**, qué evidencia del caso tensiona esa tesis y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación:** Dos fundadores creen conservar 70% tras ronda. El term sheet exige option pool 15% creado pre-money y un convertible convierte con descuento antes de la ronda.

**Paso 1 — limpiar cap table actual.** La gerencia escribe primero el supuesto asociado a **cap table** y evita convertirlo en hecho. Luego busca **founder ownership** para contrastarlo en el caso de **cap table y dilución**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 2 — convertir a fully diluted.** La gerencia escribe primero el supuesto asociado a **fully diluted** y evita convertirlo en hecho. Luego busca **investor ownership** para contrastarlo en el caso de **cap table y dilución**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 3 — modelar nueva emisión y pool.** La gerencia escribe primero el supuesto asociado a **option pool** y evita convertirlo en hecho. Luego busca **option pool** para contrastarlo en el caso de **cap table y dilución**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 4 — calcular ownership post-money.** La gerencia escribe primero el supuesto asociado a **pre-money valuation** y evita convertirlo en hecho. Luego busca **dilution per round** para contrastarlo en el caso de **cap table y dilución**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 5 — simular rondas y exits.** La gerencia escribe primero el supuesto asociado a **post-money valuation** y evita convertirlo en hecho. Luego busca **proceeds waterfall** para contrastarlo en el caso de **cap table y dilución**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Síntesis del caso.** La recomendación debe terminar con responsable, fecha, evidencia de éxito y señal de stop. En **cap table y dilución**, omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo |
|---|---|---|---|
| **cap table** | registro de ownership y securities de una compañía | Cuando founder ownership es observable y accionable. | Sobrerreaccionar a una señal parcial. |
| **fully diluted** | propiedad asumiendo ejercicio o conversión de instrumentos relevantes | Cuando la primera explicación no distingue mecanismo o responsabilidad. | Convertir el concepto en etiqueta. |
| **Experimento/revisión** | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar eternamente y no decidir. |
| **Escalamiento** | Elevar autoridad o especialidad | Cuando hay derechos, capital material, regulación o irreversibilidad. | Delegar hacia arriba lo que sí corresponde decidir. |

**Frontera de aplicación:** Cap tables legales pueden incluir preferencias y derechos complejos. Usa modelo para comprender economía, pero valida documentos y conversiones con asesoría legal o financiera.

## 🪜 De profesional a owner

| Nivel | Responsabilidad sobre cap table y dilución |
|---|---|
| **Profesional** | usa **cap table y dilución** para mejorar una contribución propia y explicar sus supuestos con evidencia. |
| **Jefe / Team Lead** | aplica **cap table** y **fully diluted** para coordinar personas sin sustituir conversación por métricas. |
| **Manager / Gerente** | conecta founder ownership con capacidad, presupuesto, dependencias y riesgo interáreas. |
| **CEO / Director** | decide si cap table y dilución cambia estrategia, economía o riesgo de empresa y qué debe llegar al comité o directorio. |
| **Founder / Owner** | pregunta si la solución de cap table y dilución reduce dependencia del fundador, preserva caja y puede operar como sistema repetible. |

El cambio de nivel en **cap table y dilución** aumenta el número de personas, dinero, dependencias y consecuencias que quedan dentro de la decisión. Por eso la misma herramienta debe volverse más explícita en evidencia, gobernanza y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Dos fundadores creen conservar 70% tras ronda. El term sheet exige option pool 15% creado pre-money y un convertible convierte con descuento antes de la ronda.

Entrega un **decision brief de cap table y dilución** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre personas, cliente, operación, caja y riesgo; (e) recomendación; (f) condición que haría cambiarla; (g) dueño y fecha de revisión. Utiliza al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica

1. Reconstruye el caso de **cap table y dilución** con una tabla `hecho / interpretación / hipótesis / decisión`.
2. Ejecuta **1. limpiar cap table actual → 2. convertir a fully diluted → 3. modelar nueva emisión y pool → 4. calcular ownership post-money → 5. simular rondas y exits** y adjunta evidencia para cada transición entre pasos.
3. Calcula o documenta founder ownership, investor ownership; si no existe dato, diseña cómo obtenerlo.
4. Escribe una alternativa que contradiga tu preferencia inicial y haz un *pre-mortem* específico del caso.
5. Lee dos referencias, registra una coincidencia y una tensión, y modifica el brief si corresponde.
6. Repite la decisión desde el rol de CEO/owner: identifica qué cambia al aumentar el alcance y la irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar cap table y fully diluted como sinónimos | Se pierde la distinción entre “registro de ownership y securities de una compañía” y “propiedad asumiendo ejercicio o conversión de instrumentos relevantes” | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por “simular rondas y exits” | Se saltó “limpiar cap table actual” y la solución llegó antes que el diagnóstico | Reconstruye la cadena 1. limpiar cap table actual → 2. convertir a fully diluted → 3. modelar nueva emisión y pool → 4. calcular ownership post-money → 5. simular rondas y exits y marca el primer supuesto no demostrado. |
| Optimizar solo founder ownership | La métrica local sustituyó al resultado del sistema | Contrástala con investor ownership y explicita el costo de oportunidad. |
| Generalizar desde un caso favorable | Se confundió evidencia local con una regla universal sobre cap table y dilución | Cap tables legales pueden incluir preferencias y derechos complejos. Usa modelo para comprender economía, pero valida documentos y conversiones con asesoría legal o financiera. |
| No fijar revisión | Una decisión sobre cap table y dilución se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de stop. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **cap table** y **fully diluted** usando un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **option pool** y qué observación obligaría a rechazar tu interpretación?
3. Aplica **limpiar cap table actual → convertir a fully diluted** al caso de la clase. ¿Qué dato todavía falta?
4. ¿Por qué **founder ownership** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la tabla de lectura. ¿Dónde podrían llevar a recomendaciones distintas para **cap table y dilución**?
6. ¿Qué decisión equivocada podría producirse si se ignora este límite: **Cap tables legales pueden incluir preferencias y derechos complejos. Usa modelo para comprender economía, pero valida documentos y conversiones con asesoría legal o financiera.**?

## 📥 Entregable

Guarda en `portfolio/223-cap-table-y-dilucion/`:

- `leadership-decision-brief.md` con el problema específico de **cap table y dilución**, evidencia, alternativas, decisión y gobernanza;
- `reading-note.md` contrastando las fuentes de **cap table y dilución** con edición/páginas consultadas;
- `decision-journal.md` registrando los supuestos de **cap table**, confianza, responsable y revisión;
- `red-team.md` con la objeción más fuerte al caso **Dos fundadores creen conservar 70% tras ronda. El term sheet exige option pool 15% creado pre-money y un convertible convierte con descuento antes de la ronda.** y el dato que podría invalidar la recomendación.

## 📗 Fuentes y verificación

- Richard Brealey, Stewart Myers & Franklin Allen — *Principles of Corporate Finance*. **Uso en esta clase:** valor del dinero, riesgo, costo de capital, inversión y financiación. Lectura selectiva: índice/capítulos pertinentes a **cap table y dilución**; registra edición y páginas consultadas.
- Stephen Ross, Randolph Westerfield et al. — *Corporate Finance*. **Uso en esta clase:** decisiones de inversión, financiación, capital de trabajo y valoración. Lectura selectiva: índice/capítulos pertinentes a **cap table y dilución**; registra edición y páginas consultadas.
- Brad Feld & Jason Mendelson — *Venture Deals*. **Uso en esta clase:** term sheets, economics/control y negociación de venture capital. Lectura selectiva: índice/capítulos pertinentes a **cap table y dilución**; registra edición y páginas consultadas.
- OECD — *G20/OECD Principles of Corporate Governance 2023*. **Uso en esta clase:** derechos de accionistas, directorio, disclosure, sostenibilidad y buen gobierno. Lectura selectiva: índice/capítulos pertinentes a **cap table y dilución**; registra edición y páginas consultadas.
- Noam Wasserman — *The Founder's Dilemmas*. **Uso en esta clase:** dilemas de fundador, equity, control, equipo y decisiones tempranas. Lectura selectiva: índice/capítulos pertinentes a **cap table y dilución**; registra edición y páginas consultadas.
- Tim Koller, Marc Goedhart & David Wessels — *Valuation: Measuring and Managing the Value of Companies*. **Uso en esta clase:** drivers de valor, ROIC, crecimiento y valoración por flujo descontado. Lectura selectiva: índice/capítulos pertinentes a **cap table y dilución**; registra edición y páginas consultadas.
- Susan A. Ambrose et al. — *How Learning Works*. **Uso en esta clase:** diseñar los objetivos, la práctica y el feedback de **cap table y dilución** sobre conocimiento previo verificable.
- Peter C. Brown, Henry L. Roediger III & Mark A. McDaniel — *Make It Stick*. **Uso en esta clase:** justificar la recuperación inicial y las preguntas de comprobación de **cap table y dilución**.
- Grant Wiggins & Jay McTighe — *Understanding by Design*. **Uso en esta clase:** derivar el entregable de **cap table y dilución** desde el desempeño observable y no desde el temario.
- Anders Ericsson & Robert Pool — *Peak*. **Uso en esta clase:** convertir la práctica de **cap table y dilución** en práctica deliberada con criterios explícitos.
- William Ellet — *The Case Study Handbook*. **Uso en esta clase:** estructurar el caso ejecutivo de **cap table y dilución** como problema, evidencia, alternativas y recomendación.

> **Regla de fuentes para Cap table y dilución:** las obras anteriores estructuran las perspectivas de esta materia; cualquier norma, ley, impuesto o estándar vivo mencionado en **cap table y dilución** debe comprobarse nuevamente en su fuente primaria vigente. El desarrollo es original y no reproduce capítulos protegidos.
