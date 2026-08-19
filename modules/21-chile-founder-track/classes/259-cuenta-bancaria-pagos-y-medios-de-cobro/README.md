# Clase 259 — Cuenta bancaria, pagos y medios de cobro

**Parte:** 21 — Founder Track Chile: formalización y operación  
**Nivel:** Etapa 6 — Founder en Chile  
**Duración sugerida:** 150–180 minutos · **Estándar:** deep-class-v2

## 🎯 Propósito

Cuenta bancaria, adquirencia y medios de cobro son parte del diseño de caja y control. El founder debe separar fondos empresariales, conocer settlement, chargebacks, comisiones y conciliación, y evitar que una sola credencial concentre toda capacidad de pago.

La salida de esta parte es **formalizar y operar una empresa chilena con comprensión ejecutiva de obligaciones y escalamiento profesional**. En esta clase, esa progresión se concreta al exigir que cada afirmación sobre **cuenta bancaria, pagos y medios de cobro** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

## 📚 Resultados de aprendizaje

Al finalizar podrás:

1. **Distinguir** `business bank account`, `merchant acquiring`, `settlement`, `chargeback`, `payment approval` mediante observables, no por memoria verbal.
2. **Explicar** por qué esas distinciones cambian una decisión de founder en chile.
3. **Aplicar** la secuencia **1. seleccionar medios por cliente y costo → 2. definir cuentas y roles → 3. mapear settlement y fees → 4. implementar approvals y reconciliation → 5. monitorear fraude y chargebacks** conservando supuestos, alternativas y trazabilidad.
4. **Interpretar** settlement delay, payment fees, chargeback rate sin confundir señal, explicación y causalidad.
5. **Resolver** el caso ejecutivo con al menos dos opciones plausibles y un criterio explícito de stop/revisión.
6. **Contrastar** dos obras de referencia y explicar dónde sus lentes son complementarias o entran en tensión.

## 🧭 Agenda

| Tramo | Evidencia de aprendizaje |
|---|---|
| 0–20 min | Recuperación: define business bank account y merchant acquiring sin mirar la tabla; corrige con la fuente. |
| 20–70 min | Lectura guiada de conceptos + contraste de dos referencias. |
| 70–115 min | Ejemplo trabajado con settlement delay y trazabilidad de supuestos. |
| 115–155 min | Caso ejecutivo: dos alternativas, trade-offs y decisión provisional. |
| 155–180 min | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar comprensión |
|---|---|---|
| **business bank account** | cuenta usada por entidad para separar y gestionar flujos | Distingue un hecho compatible y otro que lo refute. |
| **merchant acquiring** | servicio que procesa pagos con tarjetas u otros medios | Distingue un hecho compatible y otro que lo refute. |
| **settlement** | abono final de fondos procesados | Distingue un hecho compatible y otro que lo refute. |
| **chargeback** | reverso o disputa de una transacción según reglas del medio | Distingue un hecho compatible y otro que lo refute. |
| **payment approval** | control que autoriza desembolsos | Distingue un hecho compatible y otro que lo refute. |

## 🧠 Modelo mental

```text
1. seleccionar medios por cliente y costo → 2. definir cuentas y roles → 3. mapear settlement y fees → 4. implementar approvals y reconciliation → 5. monitorear fraude y chargebacks
```

La secuencia nace del problema de esta clase: **Cuenta bancaria, adquirencia y medios de cobro son parte del diseño de caja y control. El founder debe separar fondos empresariales, conocer settlement, chargebacks, comisiones y conciliación, y evitar que una sola credencial concentre toda capacidad de pago.** El método es útil mientras las condiciones permitan observar las señales requeridas. No elimina incertidumbre; la hace visible y obliga a decidir proporcionalmente a la evidencia. Límite principal: **Productos bancarios y condiciones cambian por proveedor. Compara contratos, seguridad y costos vigentes y no dependas de una sola persona para accesos críticos.**

## 📖 Desarrollo

### 1. business bank account: mecanismo central

**business bank account** se entiende aquí como **cuenta usada por entidad para separar y gestionar flujos**. Esta es la pieza causal o estructural desde la que se inicia **cuenta bancaria, pagos y medios de cobro**: antes de seleccionar medios por cliente y costo, el gerente debe poder señalar qué cambia en el sistema si el concepto está presente y qué debería observar si no lo está. Una definición que no produce predicciones observables todavía es demasiado vaga para dirigir.

La lectura rectora de este bloque es Comisión para el Mercado Financiero (Chile) — *Normativa e información del mercado financiero*. Su aporte se usa para examinar **regulación e información financiera y de mercados en Chile**. Aplica esa lente al caso sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **settlement delay**; regístrala con periodo, unidad, población y baseline.

Relaciona el mecanismo con **merchant acquiring**. Si ambos cambian juntos, no concluyas causalidad automáticamente: identifica una tercera variable o mecanismo alternativo que también pueda explicar el patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. merchant acquiring: frontera conceptual y error de clasificación

**Definición operacional:** servicio que procesa pagos con tarjetas u otros medios. Su valor está en distinguirlo de **business bank account** y **settlement**. En una decisión real, clasificar una situación en la categoría equivocada cambia la intervención: puedes asignar autoridad donde faltaba información, medir un output cuando debías observar un proceso o tratar una restricción como si fuera una preferencia.

Contrasta el problema con Servicio de Impuestos Internos (Chile) — *Guías, normativa y servicios oficiales*, que aporta una mirada sobre **obligaciones tributarias y ciclo de vida del contribuyente en Chile**. Formula dos mini-casos: uno que sí satisface la definición de **merchant acquiring** y otro que solo se parece superficialmente. Luego pregunta qué señal distinguiría ambos; para esta clase, **payment fees** es una candidata, pero debe combinarse con evidencia cualitativa o documental cuando el fenómeno no sea directamente medible.

Antes de definir cuentas y roles, registra explícitamente qué decisión sería errónea si esta frontera conceptual se ignora. Esa frase convierte el vocabulario en criterio gerencial.

### 3. settlement: operacionalización y medición

**settlement** significa **abono final de fondos procesados**. El problema ya no es definirlo, sino **operacionalizarlo**: qué contar, durante qué ventana, con qué denominador, contra qué baseline y con qué segmentación. Una métrica útil conserva suficiente contexto para no confundir mejora local con mejora del sistema.

Registro de Empresas y Sociedades (Chile) — *Portal y documentación oficial* orienta este bloque mediante **constitución y modificaciones societarias en el Registro de Empresas y Sociedades**. Usa esa perspectiva para diseñar una ficha de medición: `señal → fórmula/criterio → fuente → frecuencia → owner → interpretación permitida → interpretación prohibida`. La señal asignada es **chargeback rate**. Si no existe un dato confiable, la salida correcta no es inventar precisión: diseña el mecanismo de captura y declara la incertidumbre.

Al llegar a mapear settlement y fees, compara tendencia, distribución y casos atípicos. Pregunta además si el indicador es *leading* o *lagging* y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; nunca convertirse en el objetivo que reemplaza al fenómeno.

### 4. chargeback: trade-offs y efectos de segundo orden

**Definición:** reverso o disputa de una transacción según reglas del medio. Este concepto obliga a abandonar la idea de que **cuenta bancaria, pagos y medios de cobro** tiene una solución gratuita. Toda intervención consume autonomía, tiempo, caja, capacidad, atención, reputación o tolerancia al riesgo. Por eso, antes de implementar approvals y reconciliation, se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Peter F. Drucker — *Management: Tasks, Responsibilities, Practices* aporta una lente sobre **responsabilidad gerencial, propósito, organización y resultados**. Úsala para construir una matriz `beneficio / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **cash concentration** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la necesidad de observar efectos laterales fuera del KPI principal.

Haz un *pre-mortem* de **cuenta bancaria, pagos y medios de cobro**: supone que la opción recomendada fracasó seis meses después y enumera tres mecanismos que podrían explicarlo. Al menos uno debe provenir de un efecto de segundo orden asociado a **chargeback** y otro de una hipótesis del caso que nunca fue validada.

### 5. payment approval: gobernanza, límites e integración

**payment approval** se define como **control que autoriza desembolsos** y cierra el circuito porque traduce análisis en responsabilidad. La pregunta ejecutiva es quién decide, quién ejecuta, quién debe ser consultado, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar.

INAPI (Chile) — *Propiedad industrial y orientación oficial* se utiliza para estudiar **propiedad industrial, marcas, patentes y activos intangibles en Chile** y contrastar la recomendación final. Al ejecutar monitorear fraude y chargebacks, deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento. Esa trazabilidad protege contra el sesgo retrospectivo y mejora las revisiones posteriores.

La frontera de esta clase es explícita: **Productos bancarios y condiciones cambian por proveedor. Compara contratos, seguridad y costos vigentes y no dependas de una sola persona para accesos críticos.**. Conviértela en una regla operativa: `si ocurre X → no aplicar automáticamente → consultar/escalar/revalidar`. Integrar **business bank account**, **merchant acquiring**, **settlement**, **chargeback** y **payment approval** significa poder explicar qué parte del diagnóstico sostiene la decisión y cuál sigue siendo una apuesta.

### 6. Integración: de conceptos a una decisión defendible

La síntesis de **cuenta bancaria, pagos y medios de cobro** no consiste en sumar cinco definiciones. Empieza por **business bank account**, contrasta **merchant acquiring** con **settlement**, incorpora **chargeback** como restricción o mecanismo y usa **payment approval** para cerrar el ciclo. Si el análisis no puede explicar cuál de esas piezas cambió la recomendación, todavía no hay comprensión transferible.

Aplica ahora la secuencia **1. seleccionar medios por cliente y costo → 2. definir cuentas y roles → 3. mapear settlement y fees → 4. implementar approvals y reconciliation → 5. monitorear fraude y chargebacks**. Para cada paso conserva tres columnas: evidencia utilizada, alternativa descartada y razón. Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado y evita reescribir la historia después de conocer el desenlace.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla señala el lente que debes buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Comisión para el Mercado Financiero (Chile) — *Normativa e información del mercado financiero* | regulación e información financiera y de mercados en Chile | ¿Qué supuesto de **cuenta bancaria, pagos y medios de cobro** ayuda a desafiar? |
| Servicio de Impuestos Internos (Chile) — *Guías, normativa y servicios oficiales* | obligaciones tributarias y ciclo de vida del contribuyente en Chile | ¿Qué supuesto de **cuenta bancaria, pagos y medios de cobro** ayuda a desafiar? |
| Registro de Empresas y Sociedades (Chile) — *Portal y documentación oficial* | constitución y modificaciones societarias en el Registro de Empresas y Sociedades | ¿Qué supuesto de **cuenta bancaria, pagos y medios de cobro** ayuda a desafiar? |
| Peter F. Drucker — *Management: Tasks, Responsibilities, Practices* | responsabilidad gerencial, propósito, organización y resultados | ¿Qué supuesto de **cuenta bancaria, pagos y medios de cobro** ayuda a desafiar? |
| INAPI (Chile) — *Propiedad industrial y orientación oficial* | propiedad industrial, marcas, patentes y activos intangibles en Chile | ¿Qué supuesto de **cuenta bancaria, pagos y medios de cobro** ayuda a desafiar? |

En **cuenta bancaria, pagos y medios de cobro**, la lectura se evalúa por **uso**, no por cantidad de páginas. La nota debe indicar qué tesis de las fuentes modifica tu lectura de **business bank account**, qué evidencia del caso tensiona esa tesis y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación:** Una startup cobra por tres pasarelas. Finanzas compara ventas con saldo bancario sin considerar fees ni settlement; cada mes aparecen diferencias que nadie puede explicar.

**Paso 1 — seleccionar medios por cliente y costo.** La gerencia escribe primero el supuesto asociado a **business bank account** y evita convertirlo en hecho. Luego busca **settlement delay** para contrastarlo en el caso de **cuenta bancaria, pagos y medios de cobro**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 2 — definir cuentas y roles.** La gerencia escribe primero el supuesto asociado a **merchant acquiring** y evita convertirlo en hecho. Luego busca **payment fees** para contrastarlo en el caso de **cuenta bancaria, pagos y medios de cobro**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 3 — mapear settlement y fees.** La gerencia escribe primero el supuesto asociado a **settlement** y evita convertirlo en hecho. Luego busca **chargeback rate** para contrastarlo en el caso de **cuenta bancaria, pagos y medios de cobro**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 4 — implementar approvals y reconciliation.** La gerencia escribe primero el supuesto asociado a **chargeback** y evita convertirlo en hecho. Luego busca **cash concentration** para contrastarlo en el caso de **cuenta bancaria, pagos y medios de cobro**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 5 — monitorear fraude y chargebacks.** La gerencia escribe primero el supuesto asociado a **payment approval** y evita convertirlo en hecho. Luego busca **approval exceptions** para contrastarlo en el caso de **cuenta bancaria, pagos y medios de cobro**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Síntesis del caso.** La recomendación debe terminar con responsable, fecha, evidencia de éxito y señal de stop. En **cuenta bancaria, pagos y medios de cobro**, omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo |
|---|---|---|---|
| **business bank account** | cuenta usada por entidad para separar y gestionar flujos | Cuando settlement delay es observable y accionable. | Sobrerreaccionar a una señal parcial. |
| **merchant acquiring** | servicio que procesa pagos con tarjetas u otros medios | Cuando la primera explicación no distingue mecanismo o responsabilidad. | Convertir el concepto en etiqueta. |
| **Experimento/revisión** | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar eternamente y no decidir. |
| **Escalamiento** | Elevar autoridad o especialidad | Cuando hay derechos, capital material, regulación o irreversibilidad. | Delegar hacia arriba lo que sí corresponde decidir. |

**Frontera de aplicación:** Productos bancarios y condiciones cambian por proveedor. Compara contratos, seguridad y costos vigentes y no dependas de una sola persona para accesos críticos.

## 🪜 De profesional a owner

| Nivel | Responsabilidad sobre cuenta bancaria, pagos y medios de cobro |
|---|---|
| **Profesional** | usa **cuenta bancaria, pagos y medios de cobro** para mejorar una contribución propia y explicar sus supuestos con evidencia. |
| **Jefe / Team Lead** | aplica **business bank account** y **merchant acquiring** para coordinar personas sin sustituir conversación por métricas. |
| **Manager / Gerente** | conecta settlement delay con capacidad, presupuesto, dependencias y riesgo interáreas. |
| **CEO / Director** | decide si cuenta bancaria, pagos y medios de cobro cambia estrategia, economía o riesgo de empresa y qué debe llegar al comité o directorio. |
| **Founder / Owner** | pregunta si la solución de cuenta bancaria, pagos y medios de cobro reduce dependencia del fundador, preserva caja y puede operar como sistema repetible. |

El cambio de nivel en **cuenta bancaria, pagos y medios de cobro** aumenta el número de personas, dinero, dependencias y consecuencias que quedan dentro de la decisión. Por eso la misma herramienta debe volverse más explícita en evidencia, gobernanza y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Una startup cobra por tres pasarelas. Finanzas compara ventas con saldo bancario sin considerar fees ni settlement; cada mes aparecen diferencias que nadie puede explicar.

Entrega un **decision brief de cuenta bancaria, pagos y medios de cobro** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre personas, cliente, operación, caja y riesgo; (e) recomendación; (f) condición que haría cambiarla; (g) dueño y fecha de revisión. Utiliza al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica

1. Reconstruye el caso de **cuenta bancaria, pagos y medios de cobro** con una tabla `hecho / interpretación / hipótesis / decisión`.
2. Ejecuta **1. seleccionar medios por cliente y costo → 2. definir cuentas y roles → 3. mapear settlement y fees → 4. implementar approvals y reconciliation → 5. monitorear fraude y chargebacks** y adjunta evidencia para cada transición entre pasos.
3. Calcula o documenta settlement delay, payment fees; si no existe dato, diseña cómo obtenerlo.
4. Escribe una alternativa que contradiga tu preferencia inicial y haz un *pre-mortem* específico del caso.
5. Lee dos referencias, registra una coincidencia y una tensión, y modifica el brief si corresponde.
6. Repite la decisión desde el rol de CEO/owner: identifica qué cambia al aumentar el alcance y la irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar business bank account y merchant acquiring como sinónimos | Se pierde la distinción entre “cuenta usada por entidad para separar y gestionar flujos” y “servicio que procesa pagos con tarjetas u otros medios” | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por “monitorear fraude y chargebacks” | Se saltó “seleccionar medios por cliente y costo” y la solución llegó antes que el diagnóstico | Reconstruye la cadena 1. seleccionar medios por cliente y costo → 2. definir cuentas y roles → 3. mapear settlement y fees → 4. implementar approvals y reconciliation → 5. monitorear fraude y chargebacks y marca el primer supuesto no demostrado. |
| Optimizar solo settlement delay | La métrica local sustituyó al resultado del sistema | Contrástala con payment fees y explicita el costo de oportunidad. |
| Generalizar desde un caso favorable | Se confundió evidencia local con una regla universal sobre cuenta bancaria, pagos y medios de cobro | Productos bancarios y condiciones cambian por proveedor. Compara contratos, seguridad y costos vigentes y no dependas de una sola persona para accesos críticos. |
| No fijar revisión | Una decisión sobre cuenta bancaria, pagos y medios de cobro se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de stop. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **business bank account** y **merchant acquiring** usando un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **settlement** y qué observación obligaría a rechazar tu interpretación?
3. Aplica **seleccionar medios por cliente y costo → definir cuentas y roles** al caso de la clase. ¿Qué dato todavía falta?
4. ¿Por qué **settlement delay** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la tabla de lectura. ¿Dónde podrían llevar a recomendaciones distintas para **cuenta bancaria, pagos y medios de cobro**?
6. ¿Qué decisión equivocada podría producirse si se ignora este límite: **Productos bancarios y condiciones cambian por proveedor. Compara contratos, seguridad y costos vigentes y no dependas de una sola persona para accesos críticos.**?

## 📥 Entregable

Guarda en `portfolio/259-cuenta-bancaria-pagos-y-medios-de-cobro/`:

- `risk-governance-brief.md` con el problema específico de **cuenta bancaria, pagos y medios de cobro**, evidencia, alternativas, decisión y gobernanza;
- `reading-note.md` contrastando las fuentes de **cuenta bancaria, pagos y medios de cobro** con edición/páginas consultadas;
- `decision-journal.md` registrando los supuestos de **business bank account**, confianza, responsable y revisión;
- `red-team.md` con la objeción más fuerte al caso **Una startup cobra por tres pasarelas. Finanzas compara ventas con saldo bancario sin considerar fees ni settlement; cada mes aparecen diferencias que nadie puede explicar.** y el dato que podría invalidar la recomendación.

## 📗 Fuentes y verificación

- Comisión para el Mercado Financiero (Chile) — *Normativa e información del mercado financiero*. **Uso en esta clase:** verificar qué instituciones y productos financieros están regulados y supervisados. **Fuente primaria:** <https://www.cmfchile.cl/>.
- Servicio de Impuestos Internos (Chile) — *Guías, normativa y servicios oficiales*. **Uso en esta clase:** obligaciones tributarias y ciclo de vida del contribuyente en Chile. **Fuente primaria:** <https://www.sii.cl/>.
- Registro de Empresas y Sociedades (Chile) — *Portal y documentación oficial*. **Uso en esta clase:** constitución y modificaciones societarias en el Registro de Empresas y Sociedades. **Fuente primaria:** <https://www.registrodeempresasysociedades.cl/>.
- Peter F. Drucker — *Management: Tasks, Responsibilities, Practices* (Harper & Row, 1974). **Uso en esta clase:** responsabilidad gerencial, propósito, organización y resultados. Lectura selectiva sobre **cuenta bancaria, pagos y medios de cobro**. **Localizador:** [ISBN-13 9780060110925](https://openlibrary.org/isbn/9780060110925).
- INAPI (Chile) — *Propiedad industrial y orientación oficial*. **Uso en esta clase:** propiedad industrial, marcas, patentes y activos intangibles en Chile. **Fuente primaria:** <https://www.inapi.cl/>.
- Corporación de Fomento de la Producción (Chile) — *Programas, instrumentos y apoyo empresarial*. **Uso en esta clase:** instrumentos de desarrollo productivo, innovación y financiamiento empresarial. **Fuente primaria:** <https://www.corfo.cl/>.
- Servicio de Impuestos Internos (Chile) — *Acreditación de inicio de actividades y obligaciones tributarias*. **Uso en esta clase:** comprobar qué acredita el banco al abrir la cuenta de la empresa. **Fuente primaria:** <https://www.sii.cl/destacados/ley_cumplimiento_obligaciones_tributarias/inicio_actividades.html>.
- Susan A. Ambrose et al. — *How Learning Works* (John Wiley & Sons, Incorporated, 2010). **Uso en esta clase:** diseñar los objetivos, la práctica y el feedback de **cuenta bancaria, pagos y medios de cobro** sobre conocimiento previo verificable. **Localizador:** [ISBN-13 9780470617601](https://openlibrary.org/isbn/9780470617601).
- Peter C. Brown, Henry L. Roediger III & Mark A. McDaniel — *Make It Stick* (Harvard University Press, 2014). **Uso en esta clase:** justificar la recuperación inicial y las preguntas de comprobación de **cuenta bancaria, pagos y medios de cobro**. **Localizador:** [ISBN-13 9780674986572](https://openlibrary.org/isbn/9780674986572).
- Grant Wiggins & Jay McTighe — *Understanding by Design* (Pearson Education, Inc., 2006). **Uso en esta clase:** derivar el entregable de **cuenta bancaria, pagos y medios de cobro** desde el desempeño observable y no desde el temario. **Localizador:** [ISBN-13 9780131950849](https://openlibrary.org/isbn/9780131950849).
- Anders Ericsson & Robert Pool — *Peak* (Penguin Random House, 2016). **Uso en esta clase:** convertir la práctica de **cuenta bancaria, pagos y medios de cobro** en práctica deliberada con criterios explícitos. **Localizador:** [ISBN-13 9781473513143](https://openlibrary.org/isbn/9781473513143).
- William Ellet — *The Case Study Handbook* (Harvard Business Review Press, 2018). **Uso en esta clase:** estructurar el caso ejecutivo de **cuenta bancaria, pagos y medios de cobro** como problema, evidencia, alternativas y recomendación. **Localizador:** [ISBN-13 9781633696150](https://openlibrary.org/isbn/9781633696150).

> **Regla de fuentes para Cuenta bancaria, pagos y medios de cobro:** las obras anteriores estructuran las perspectivas de esta materia; cualquier norma, ley, impuesto o estándar vivo mencionado en **cuenta bancaria, pagos y medios de cobro** debe comprobarse nuevamente en su fuente primaria vigente. El desarrollo es original y no reproduce capítulos protegidos.
