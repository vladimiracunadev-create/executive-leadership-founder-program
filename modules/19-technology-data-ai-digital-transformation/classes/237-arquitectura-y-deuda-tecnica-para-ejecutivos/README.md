# Clase 237 — Arquitectura y deuda técnica para ejecutivos

**Parte:** 19 — Tecnología, datos, IA y transformación digital para ejecutivos  
**Nivel:** Etapa 5 — CEO → Transformador digital  
**Duración sugerida:** 150–180 minutos · **Estándar:** deep-class-v2

## 🎯 Propósito

Arquitectura y deuda técnica importan al ejecutivo cuando afectan velocidad, disponibilidad, costo, seguridad o capacidad de cambiar. La deuda es un trade-off deliberado o acumulado, no código feo; debe gestionarse como riesgo y capital maintenance.

La salida de esta parte es **gobernar tecnología, datos e IA como capacidades económicas y organizacionales**. En esta clase, esa progresión se concreta al exigir que cada afirmación sobre **arquitectura y deuda técnica para ejecutivos** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

## 📚 Resultados de aprendizaje

Al finalizar podrás:

1. **Distinguir** `architecture`, `technical debt`, `coupling`, `legacy`, `architectural runway` mediante observables, no por memoria verbal.
2. **Explicar** por qué esas distinciones cambian una decisión de ceo → transformador digital.
3. **Aplicar** la secuencia **1. traducir estrategia a quality attributes → 2. mapear bottlenecks y dependencies → 3. cuantificar debt impact → 4. priorizar remediation por value y risk → 5. crear guardrails y evolución incremental** conservando supuestos, alternativas y trazabilidad.
4. **Interpretar** change failure rate, lead time, incident rate sin confundir señal, explicación y causalidad.
5. **Resolver** el caso ejecutivo con al menos dos opciones plausibles y un criterio explícito de stop/revisión.
6. **Contrastar** dos obras de referencia y explicar dónde sus lentes son complementarias o entran en tensión.

## 🧭 Agenda

| Tramo | Evidencia de aprendizaje |
|---|---|
| 0–20 min | Recuperación: define architecture y technical debt sin mirar la tabla; corrige con la fuente. |
| 20–70 min | Lectura guiada de conceptos + contraste de dos referencias. |
| 70–115 min | Ejemplo trabajado con change failure rate y trazabilidad de supuestos. |
| 115–155 min | Caso ejecutivo: dos alternativas, trade-offs y decisión provisional. |
| 155–180 min | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar comprensión |
|---|---|---|
| **architecture** | estructura de componentes interfaces y decisiones que condicionan sistemas | Distingue un hecho compatible y otro que lo refute. |
| **technical debt** | costo futuro creado al elegir soluciones que aumentan fricción o riesgo | Distingue un hecho compatible y otro que lo refute. |
| **coupling** | grado de dependencia entre componentes | Distingue un hecho compatible y otro que lo refute. |
| **legacy** | tecnología que sigue soportando valor pero impone restricciones | Distingue un hecho compatible y otro que lo refute. |
| **architectural runway** | capacidad técnica preparada para próximas necesidades | Distingue un hecho compatible y otro que lo refute. |

## 🧠 Modelo mental

```text
1. traducir estrategia a quality attributes → 2. mapear bottlenecks y dependencies → 3. cuantificar debt impact → 4. priorizar remediation por value y risk → 5. crear guardrails y evolución incremental
```

La secuencia nace del problema de esta clase: **Arquitectura y deuda técnica importan al ejecutivo cuando afectan velocidad, disponibilidad, costo, seguridad o capacidad de cambiar. La deuda es un trade-off deliberado o acumulado, no código feo; debe gestionarse como riesgo y capital maintenance.** El método es útil mientras las condiciones permitan observar las señales requeridas. No elimina incertidumbre; la hace visible y obliga a decidir proporcionalmente a la evidencia. Límite principal: **No toda deuda debe pagarse. Si un sistema está cerca de retiro o el costo de cambio supera beneficio, gestionar el riesgo puede ser mejor que reescribir.**

## 📖 Desarrollo

### 1. architecture: mecanismo central

**architecture** se entiende aquí como **estructura de componentes interfaces y decisiones que condicionan sistemas**. Esta es la pieza causal o estructural desde la que se inicia **arquitectura y deuda técnica para ejecutivos**: antes de traducir estrategia a quality attributes, el gerente debe poder señalar qué cambia en el sistema si el concepto está presente y qué debería observar si no lo está. Una definición que no produce predicciones observables todavía es demasiado vaga para dirigir.

La lectura rectora de este bloque es Marco Iansiti & Karim R. Lakhani — *Competing in the Age of AI*. Su aporte se usa para examinar **modelo operativo AI-first, escala digital, redes y arquitectura de decisión**. Aplica esa lente al caso sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **change failure rate**; regístrala con periodo, unidad, población y baseline.

Relaciona el mecanismo con **technical debt**. Si ambos cambian juntos, no concluyas causalidad automáticamente: identifica una tercera variable o mecanismo alternativo que también pueda explicar el patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. technical debt: frontera conceptual y error de clasificación

**Definición operacional:** costo futuro creado al elegir soluciones que aumentan fricción o riesgo. Su valor está en distinguirlo de **architecture** y **coupling**. En una decisión real, clasificar una situación en la categoría equivocada cambia la intervención: puedes asignar autoridad donde faltaba información, medir un output cuando debías observar un proceso o tratar una restricción como si fuera una preferencia.

Contrasta el problema con Thomas H. Davenport & Nitin Mittal — *All-In on AI*, que aporta una mirada sobre **casos empresariales, estrategia y organización para inteligencia artificial**. Formula dos mini-casos: uno que sí satisface la definición de **technical debt** y otro que solo se parece superficialmente. Luego pregunta qué señal distinguiría ambos; para esta clase, **lead time** es una candidata, pero debe combinarse con evidencia cualitativa o documental cuando el fenómeno no sea directamente medible.

Antes de mapear bottlenecks y dependencies, registra explícitamente qué decisión sería errónea si esta frontera conceptual se ignora. Esa frase convierte el vocabulario en criterio gerencial.

### 3. coupling: operacionalización y medición

**coupling** significa **grado de dependencia entre componentes**. El problema ya no es definirlo, sino **operacionalizarlo**: qué contar, durante qué ventana, con qué denominador, contra qué baseline y con qué segmentación. Una métrica útil conserva suficiente contexto para no confundir mejora local con mejora del sistema.

NIST — *Cybersecurity Framework (CSF) 2.0* orienta este bloque mediante **gobierno, identificación, protección, detección, respuesta y recuperación en ciberseguridad**. Usa esa perspectiva para diseñar una ficha de medición: `señal → fórmula/criterio → fuente → frecuencia → owner → interpretación permitida → interpretación prohibida`. La señal asignada es **incident rate**. Si no existe un dato confiable, la salida correcta no es inventar precisión: diseña el mecanismo de captura y declara la incertidumbre.

Al llegar a cuantificar debt impact, compara tendencia, distribución y casos atípicos. Pregunta además si el indicador es *leading* o *lagging* y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; nunca convertirse en el objetivo que reemplaza al fenómeno.

### 4. legacy: trade-offs y efectos de segundo orden

**Definición:** tecnología que sigue soportando valor pero impone restricciones. Este concepto obliga a abandonar la idea de que **arquitectura y deuda técnica para ejecutivos** tiene una solución gratuita. Toda intervención consume autonomía, tiempo, caja, capacidad, atención, reputación o tolerancia al riesgo. Por eso, antes de priorizar remediation por value y risk, se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Andrew McAfee & Erik Brynjolfsson — *Machine, Platform, Crowd* aporta una lente sobre **perspectiva de Economía digital aplicada al problema de la clase**. Úsala para construir una matriz `beneficio / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **maintenance share** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la necesidad de observar efectos laterales fuera del KPI principal.

Haz un *pre-mortem* de **arquitectura y deuda técnica para ejecutivos**: supone que la opción recomendada fracasó seis meses después y enumera tres mecanismos que podrían explicarlo. Al menos uno debe provenir de un efecto de segundo orden asociado a **legacy** y otro de una hipótesis del caso que nunca fue validada.

### 5. architectural runway: gobernanza, límites e integración

**architectural runway** se define como **capacidad técnica preparada para próximas necesidades** y cierra el circuito porque traduce análisis en responsabilidad. La pregunta ejecutiva es quién decide, quién ejecuta, quién debe ser consultado, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar.

Martin Kleppmann — *Designing Data-Intensive Applications* se utiliza para estudiar **perspectiva de Arquitectura tecnológica aplicada al problema de la clase** y contrastar la recomendación final. Al ejecutar crear guardrails y evolución incremental, deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento. Esa trazabilidad protege contra el sesgo retrospectivo y mejora las revisiones posteriores.

La frontera de esta clase es explícita: **No toda deuda debe pagarse. Si un sistema está cerca de retiro o el costo de cambio supera beneficio, gestionar el riesgo puede ser mejor que reescribir.**. Conviértela en una regla operativa: `si ocurre X → no aplicar automáticamente → consultar/escalar/revalidar`. Integrar **architecture**, **technical debt**, **coupling**, **legacy** y **architectural runway** significa poder explicar qué parte del diagnóstico sostiene la decisión y cuál sigue siendo una apuesta.

### 6. Integración: de conceptos a una decisión defendible

La síntesis de **arquitectura y deuda técnica para ejecutivos** no consiste en sumar cinco definiciones. Empieza por **architecture**, contrasta **technical debt** con **coupling**, incorpora **legacy** como restricción o mecanismo y usa **architectural runway** para cerrar el ciclo. Si el análisis no puede explicar cuál de esas piezas cambió la recomendación, todavía no hay comprensión transferible.

Aplica ahora la secuencia **1. traducir estrategia a quality attributes → 2. mapear bottlenecks y dependencies → 3. cuantificar debt impact → 4. priorizar remediation por value y risk → 5. crear guardrails y evolución incremental**. Para cada paso conserva tres columnas: evidencia utilizada, alternativa descartada y razón. Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado y evita reescribir la historia después de conocer el desenlace.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla señala el lente que debes buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Marco Iansiti & Karim R. Lakhani — *Competing in the Age of AI* | modelo operativo AI-first, escala digital, redes y arquitectura de decisión | ¿Qué supuesto de **arquitectura y deuda técnica para ejecutivos** ayuda a desafiar? |
| Thomas H. Davenport & Nitin Mittal — *All-In on AI* | casos empresariales, estrategia y organización para inteligencia artificial | ¿Qué supuesto de **arquitectura y deuda técnica para ejecutivos** ayuda a desafiar? |
| NIST — *Cybersecurity Framework (CSF) 2.0* | gobierno, identificación, protección, detección, respuesta y recuperación en ciberseguridad | ¿Qué supuesto de **arquitectura y deuda técnica para ejecutivos** ayuda a desafiar? |
| Andrew McAfee & Erik Brynjolfsson — *Machine, Platform, Crowd* | perspectiva de Economía digital aplicada al problema de la clase | ¿Qué supuesto de **arquitectura y deuda técnica para ejecutivos** ayuda a desafiar? |
| Martin Kleppmann — *Designing Data-Intensive Applications* | perspectiva de Arquitectura tecnológica aplicada al problema de la clase | ¿Qué supuesto de **arquitectura y deuda técnica para ejecutivos** ayuda a desafiar? |

En **arquitectura y deuda técnica para ejecutivos**, la lectura se evalúa por **uso**, no por cantidad de páginas. La nota debe indicar qué tesis de las fuentes modifica tu lectura de **architecture**, qué evidencia del caso tensiona esa tesis y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación:** Cada feature en billing requiere coordinación de cinco equipos y ventana nocturna. Negocio piensa que es lentitud de ingeniería; arquitectura monolítica crea el cuello.

**Paso 1 — traducir estrategia a quality attributes.** La gerencia escribe primero el supuesto asociado a **architecture** y evita convertirlo en hecho. Luego busca **change failure rate** para contrastarlo en el caso de **arquitectura y deuda técnica para ejecutivos**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 2 — mapear bottlenecks y dependencies.** La gerencia escribe primero el supuesto asociado a **technical debt** y evita convertirlo en hecho. Luego busca **lead time** para contrastarlo en el caso de **arquitectura y deuda técnica para ejecutivos**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 3 — cuantificar debt impact.** La gerencia escribe primero el supuesto asociado a **coupling** y evita convertirlo en hecho. Luego busca **incident rate** para contrastarlo en el caso de **arquitectura y deuda técnica para ejecutivos**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 4 — priorizar remediation por value y risk.** La gerencia escribe primero el supuesto asociado a **legacy** y evita convertirlo en hecho. Luego busca **maintenance share** para contrastarlo en el caso de **arquitectura y deuda técnica para ejecutivos**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Paso 5 — crear guardrails y evolución incremental.** La gerencia escribe primero el supuesto asociado a **architectural runway** y evita convertirlo en hecho. Luego busca **dependency count** para contrastarlo en el caso de **arquitectura y deuda técnica para ejecutivos**. El resultado del paso debe ser un artefacto revisable —dato, mapa, cálculo, registro o decisión— y una frase explícita: “cambiaríamos de rumbo si…”.

**Síntesis del caso.** La recomendación debe terminar con responsable, fecha, evidencia de éxito y señal de stop. En **arquitectura y deuda técnica para ejecutivos**, omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo |
|---|---|---|---|
| **architecture** | estructura de componentes interfaces y decisiones que condicionan sistemas | Cuando change failure rate es observable y accionable. | Sobrerreaccionar a una señal parcial. |
| **technical debt** | costo futuro creado al elegir soluciones que aumentan fricción o riesgo | Cuando la primera explicación no distingue mecanismo o responsabilidad. | Convertir el concepto en etiqueta. |
| **Experimento/revisión** | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar eternamente y no decidir. |
| **Escalamiento** | Elevar autoridad o especialidad | Cuando hay derechos, capital material, regulación o irreversibilidad. | Delegar hacia arriba lo que sí corresponde decidir. |

**Frontera de aplicación:** No toda deuda debe pagarse. Si un sistema está cerca de retiro o el costo de cambio supera beneficio, gestionar el riesgo puede ser mejor que reescribir.

## 🪜 De profesional a owner

| Nivel | Responsabilidad sobre arquitectura y deuda técnica para ejecutivos |
|---|---|
| **Profesional** | usa **arquitectura y deuda técnica para ejecutivos** para mejorar una contribución propia y explicar sus supuestos con evidencia. |
| **Jefe / Team Lead** | aplica **architecture** y **technical debt** para coordinar personas sin sustituir conversación por métricas. |
| **Manager / Gerente** | conecta change failure rate con capacidad, presupuesto, dependencias y riesgo interáreas. |
| **CEO / Director** | decide si arquitectura y deuda técnica para ejecutivos cambia estrategia, economía o riesgo de empresa y qué debe llegar al comité o directorio. |
| **Founder / Owner** | pregunta si la solución de arquitectura y deuda técnica para ejecutivos reduce dependencia del fundador, preserva caja y puede operar como sistema repetible. |

El cambio de nivel en **arquitectura y deuda técnica para ejecutivos** aumenta el número de personas, dinero, dependencias y consecuencias que quedan dentro de la decisión. Por eso la misma herramienta debe volverse más explícita en evidencia, gobernanza y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Cada feature en billing requiere coordinación de cinco equipos y ventana nocturna. Negocio piensa que es lentitud de ingeniería; arquitectura monolítica crea el cuello.

Entrega un **decision brief de arquitectura y deuda técnica para ejecutivos** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre personas, cliente, operación, caja y riesgo; (e) recomendación; (f) condición que haría cambiarla; (g) dueño y fecha de revisión. Utiliza al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica

1. Reconstruye el caso de **arquitectura y deuda técnica para ejecutivos** con una tabla `hecho / interpretación / hipótesis / decisión`.
2. Ejecuta **1. traducir estrategia a quality attributes → 2. mapear bottlenecks y dependencies → 3. cuantificar debt impact → 4. priorizar remediation por value y risk → 5. crear guardrails y evolución incremental** y adjunta evidencia para cada transición entre pasos.
3. Calcula o documenta change failure rate, lead time; si no existe dato, diseña cómo obtenerlo.
4. Escribe una alternativa que contradiga tu preferencia inicial y haz un *pre-mortem* específico del caso.
5. Lee dos referencias, registra una coincidencia y una tensión, y modifica el brief si corresponde.
6. Repite la decisión desde el rol de CEO/owner: identifica qué cambia al aumentar el alcance y la irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar architecture y technical debt como sinónimos | Se pierde la distinción entre “estructura de componentes interfaces y decisiones que condicionan sistemas” y “costo futuro creado al elegir soluciones que aumentan fricción o riesgo” | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por “crear guardrails y evolución incremental” | Se saltó “traducir estrategia a quality attributes” y la solución llegó antes que el diagnóstico | Reconstruye la cadena 1. traducir estrategia a quality attributes → 2. mapear bottlenecks y dependencies → 3. cuantificar debt impact → 4. priorizar remediation por value y risk → 5. crear guardrails y evolución incremental y marca el primer supuesto no demostrado. |
| Optimizar solo change failure rate | La métrica local sustituyó al resultado del sistema | Contrástala con lead time y explicita el costo de oportunidad. |
| Generalizar desde un caso favorable | Se confundió evidencia local con una regla universal sobre arquitectura y deuda técnica para ejecutivos | No toda deuda debe pagarse. Si un sistema está cerca de retiro o el costo de cambio supera beneficio, gestionar el riesgo puede ser mejor que reescribir. |
| No fijar revisión | Una decisión sobre arquitectura y deuda técnica para ejecutivos se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de stop. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **architecture** y **technical debt** usando un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **coupling** y qué observación obligaría a rechazar tu interpretación?
3. Aplica **traducir estrategia a quality attributes → mapear bottlenecks y dependencies** al caso de la clase. ¿Qué dato todavía falta?
4. ¿Por qué **change failure rate** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la tabla de lectura. ¿Dónde podrían llevar a recomendaciones distintas para **arquitectura y deuda técnica para ejecutivos**?
6. ¿Qué decisión equivocada podría producirse si se ignora este límite: **No toda deuda debe pagarse. Si un sistema está cerca de retiro o el costo de cambio supera beneficio, gestionar el riesgo puede ser mejor que reescribir.**?

## 📥 Entregable

Guarda en `portfolio/237-arquitectura-y-deuda-tecnica-para-ejecutivos/`:

- `leadership-decision-brief.md` con el problema específico de **arquitectura y deuda técnica para ejecutivos**, evidencia, alternativas, decisión y gobernanza;
- `reading-note.md` contrastando las fuentes de **arquitectura y deuda técnica para ejecutivos** con edición/páginas consultadas;
- `decision-journal.md` registrando los supuestos de **architecture**, confianza, responsable y revisión;
- `red-team.md` con la objeción más fuerte al caso **Cada feature en billing requiere coordinación de cinco equipos y ventana nocturna. Negocio piensa que es lentitud de ingeniería; arquitectura monolítica crea el cuello.** y el dato que podría invalidar la recomendación.

## 📗 Fuentes y verificación

- Marco Iansiti & Karim R. Lakhani — *Competing in the Age of AI* (Harvard Business Review Press, 2020). **Uso en esta clase:** modelo operativo AI-first, escala digital, redes y arquitectura de decisión. Lectura selectiva sobre **arquitectura y deuda técnica para ejecutivos**. **Localizador:** [ISBN-13 9781633697621](https://openlibrary.org/isbn/9781633697621).
- Thomas H. Davenport & Nitin Mittal — *All-In on AI* (Harvard Business Review Press, 2022). **Uso en esta clase:** casos empresariales, estrategia y organización para inteligencia artificial. Lectura selectiva sobre **arquitectura y deuda técnica para ejecutivos**. **Localizador:** [ISBN-13 9781647824693](https://openlibrary.org/isbn/9781647824693).
- NIST — *Cybersecurity Framework (CSF) 2.0*. **Uso en esta clase:** gobierno, identificación, protección, detección, respuesta y recuperación en ciberseguridad. **Fuente primaria:** <https://www.nist.gov/cyberframework>.
- Andrew McAfee & Erik Brynjolfsson — *Machine, Platform, Crowd* (Norton & Company, Incorporated, W. W., 2017). **Uso en esta clase:** perspectiva de Economía digital aplicada al problema de la clase. Lectura selectiva sobre **arquitectura y deuda técnica para ejecutivos**. **Localizador:** [ISBN-13 9780393254303](https://openlibrary.org/isbn/9780393254303).
- Martin Kleppmann — *Designing Data-Intensive Applications* (O'Reilly publications, 2017). **Uso en esta clase:** perspectiva de Arquitectura tecnológica aplicada al problema de la clase. Lectura selectiva sobre **arquitectura y deuda técnica para ejecutivos**. **Localizador:** [ISBN-13 9789352135240](https://openlibrary.org/isbn/9789352135240).
- George Westerman, Didier Bonnet & Andrew McAfee — *Leading Digital* (Harvard Business Review Press, 2014). **Uso en esta clase:** transformación digital desde capacidades de liderazgo y capacidades digitales. Lectura selectiva sobre **arquitectura y deuda técnica para ejecutivos**. **Localizador:** [ISBN-13 9781625272478](https://openlibrary.org/isbn/9781625272478).
- Susan A. Ambrose et al. — *How Learning Works* (John Wiley & Sons, Incorporated, 2010). **Uso en esta clase:** diseñar los objetivos, la práctica y el feedback de **arquitectura y deuda técnica para ejecutivos** sobre conocimiento previo verificable. **Localizador:** [ISBN-13 9780470617601](https://openlibrary.org/isbn/9780470617601).
- Peter C. Brown, Henry L. Roediger III & Mark A. McDaniel — *Make It Stick* (Harvard University Press, 2014). **Uso en esta clase:** justificar la recuperación inicial y las preguntas de comprobación de **arquitectura y deuda técnica para ejecutivos**. **Localizador:** [ISBN-13 9780674986572](https://openlibrary.org/isbn/9780674986572).
- Grant Wiggins & Jay McTighe — *Understanding by Design* (Pearson Education, Inc., 2006). **Uso en esta clase:** derivar el entregable de **arquitectura y deuda técnica para ejecutivos** desde el desempeño observable y no desde el temario. **Localizador:** [ISBN-13 9780131950849](https://openlibrary.org/isbn/9780131950849).
- Anders Ericsson & Robert Pool — *Peak* (Penguin Random House, 2016). **Uso en esta clase:** convertir la práctica de **arquitectura y deuda técnica para ejecutivos** en práctica deliberada con criterios explícitos. **Localizador:** [ISBN-13 9781473513143](https://openlibrary.org/isbn/9781473513143).
- William Ellet — *The Case Study Handbook* (Harvard Business Review Press, 2018). **Uso en esta clase:** estructurar el caso ejecutivo de **arquitectura y deuda técnica para ejecutivos** como problema, evidencia, alternativas y recomendación. **Localizador:** [ISBN-13 9781633696150](https://openlibrary.org/isbn/9781633696150).

> **Regla de fuentes para Arquitectura y deuda técnica para ejecutivos:** las obras anteriores estructuran las perspectivas de esta materia; cualquier norma, ley, impuesto o estándar vivo mencionado en **arquitectura y deuda técnica para ejecutivos** debe comprobarse nuevamente en su fuente primaria vigente. El desarrollo es original y no reproduce capítulos protegidos.
