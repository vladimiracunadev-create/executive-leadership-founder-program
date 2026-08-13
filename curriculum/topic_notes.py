# Profundizaciones técnicas/disciplinarias que no deben reducirse a la plantilla general.
TOPIC_NOTES = {}

def note(cid, text):
    TOPIC_NOTES[cid] = text.strip()

note(109, r'''
### Ecuación contable y tres preguntas del gerente

La contabilidad conecta decisiones con tres estados. La identidad base es `Activos = Pasivos + Patrimonio`. El estado de resultados explica desempeño durante un periodo; el balance muestra recursos y obligaciones a una fecha; el flujo de efectivo explica movimientos de caja. Un gerente debe poder reconciliar las tres vistas: utilidad no equivale a caja, crecimiento de ventas puede consumir capital de trabajo y una compra de activo puede deteriorar caja sin ser gasto inmediato.

Usa una transacción simple para comprobarlo: comprar una máquina por 100 con 40 de caja y 60 de deuda reduce caja 40, aumenta PPE 100 y pasivos 60; no crea de inmediato un gasto de 100. La depreciación aparecerá después en resultados. Esta separación entre **reconocimiento económico, posición financiera y caja** es la base de las clases 110–119.
''')
note(110, r'''
### Cascada, márgenes y normalización

Lee el estado de resultados en niveles, porque cada nivel responde una pregunta distinta:

```text
Ventas
- Costo de ventas                  = Margen bruto
- Gastos operativos               = Resultado operativo (EBIT, según presentación)
+ Depreciación y amortización      -> puente aproximado hacia EBITDA
± Resultado no operativo
- Intereses
- Impuestos                       = Resultado neto
```

Métricas mínimas: `margen bruto = (ventas - costo de ventas) / ventas`; `margen operativo = resultado operativo / ventas`; `margen neto = resultado neto / ventas`. EBITDA **no es caja**: omite inversiones, capital de trabajo, intereses e impuestos.

Con el caso de la clase, si el año 3 reporta utilidad neta de 2,8 millones pero incluye 1,75 millones por venta de una planta, primero separa ese ingreso no recurrente. Si el margen operativo cayó de 9,7 % a 6,4 %, el negocio operativo se deterioró aunque el resultado neto haya mejorado. Penman y Palepu justifican reformular y analizar la capacidad recurrente; Schilit aporta la disciplina de desconfiar de “otros ingresos” y ajustes oportunistas. Una normalización válida documenta **qué se elimina, por qué no es recurrente y cuál es su efecto tributario**.
''')
note(111, r'''
### Lectura estructurada del balance

Organiza el balance por **liquidez, exigibilidad y permanencia**. Calcula al menos `capital de trabajo neto = activos corrientes - pasivos corrientes` y, cuando sea útil, `current ratio = activos corrientes / pasivos corrientes`. Después mira composición: caja, cuentas por cobrar, inventarios, PPE, deuda, proveedores y patrimonio.

Dos balances con el mismo total pueden tener riesgos opuestos. Si cuentas por cobrar crecen mucho más rápido que ventas, la liquidez aparente puede depender de cobros dudosos. Si inventario crece mientras ventas se estancan, puede existir obsolescencia. Si deuda de corto plazo financia activos largos, aparece riesgo de refinanciamiento. El análisis no termina en ratios: reconcilia variaciones con resultados y flujo de caja.
''')
note(112, r'''
### CFO, CFI, CFF y flujo libre

El estado de flujo separa `CFO` (operación), `CFI` (inversión) y `CFF` (financiación). Por método indirecto, CFO parte del resultado y ajusta partidas no monetarias y cambios en capital de trabajo. Una forma gerencial simplificada de flujo libre es `FCF ≈ CFO - CAPEX`, siempre aclarando definición y propósito.

Ejemplo: una empresa puede reportar utilidad de 10, aumentar cuentas por cobrar en 8 e inventario en 4 y terminar con CFO mucho menor. El crecimiento “rentable” consume caja cuando se financia a clientes o inventario. Por eso el gerente debe rastrear la conversión de beneficio a efectivo y distinguir un problema operativo de una decisión de inversión o financiación.
''')
note(113, r'''
### Árbol de márgenes

No existe “el margen” como cifra única. `Margen bruto` observa economía de producto/servicio antes de estructura; `margen de contribución` suele restar costos variables relevantes para decisiones; `margen operativo` incorpora estructura operativa. Define siempre qué costos entran.

Para una venta de 100 con costo de producto 55 y costo variable comercial/logístico 10: margen bruto = 45 %, contribución = 35 si se define sobre esos costos variables. Esa diferencia importa para pricing, promociones, capacidad y break-even. Analiza cambios por **precio, volumen, mix y costo**, no solo el porcentaje final.
''')
note(114, r'''
### Ciclo de conversión de caja

Capital de trabajo operativo puede analizarse con `DSO` (días de cobro), `DIO` (días de inventario) y `DPO` (días de pago). Una aproximación común es `CCC = DSO + DIO - DPO`. No compares días entre industrias sin contexto.

Si DSO sube de 35 a 60 días mientras ventas crecen, el crecimiento exige más financiación. Si DIO sube por stock preventivo, puede reducir riesgo de quiebre pero aumentar caja inmovilizada y obsolescencia. Gestionar capital de trabajo exige coordinar ventas, operaciones, compras y finanzas; no es tarea exclusiva de tesorería.
''')
note(115, r'''
### Presupuesto, forecast y análisis de variaciones

Presupuesto fija una intención/plan; forecast actualiza la mejor estimación con información reciente. No “corrijas” el forecast para proteger el presupuesto. Separa variaciones en drivers: precio, volumen, mix, costo unitario, headcount, tipo de cambio u otros que correspondan.

Ejemplo: ventas presupuestadas 1.000 = 100 unidades × 10. Si se venden 90 a 11, ventas reales 990. La variación total es -10, pero precio aportó positivamente y volumen negativamente. El análisis driver-based evita respuestas equivocadas, como recortar marketing cuando el problema real fue capacidad de entrega.
''')
note(116, r'''
### Break-even y margen de seguridad

Con un producto simple, `margen de contribución unitario = precio - costo variable unitario` y `unidades de equilibrio = costos fijos / margen de contribución unitario`. Si precio = 100, variable = 60 y costos fijos = 200.000, el punto de equilibrio es 5.000 unidades.

Agrega `margen de seguridad = ventas esperadas - ventas de equilibrio`. En negocios multiproducto, el mix importa; en SaaS, los costos “variables” pueden comportarse distinto por etapa. El break-even no predice demanda: solo muestra qué volumen exige una estructura de costos dada.
''')
note(117, r'''
### Unit economics coherentes

Define cohortes y periodos antes de calcular. `CAC = gasto atribuible de adquisición / nuevos clientes adquiridos` (declarando qué gastos incluyes). Una aproximación de `LTV` puede usar `ARPA × margen bruto × vida esperada`, pero la vida derivada de churn exige supuestos; no uses `1/churn` mecánicamente si la retención no es estacionaria. `Payback = CAC / margen bruto mensual por cliente` es una aproximación útil.

Un ratio LTV/CAC alto no salva un negocio si el payback supera el runway. Complementa con churn logo, churn revenue, expansión, margen bruto y cohortes. El objetivo es entender **economía marginal y recuperación de caja**, no optimizar una cifra de presentación.
''')
note(118, r'''
### ROI, ROIC y creación de valor

`ROI` es una familia de cocientes y debe declarar numerador, denominador y horizonte. `ROIC` busca relacionar beneficio operativo después de impuestos con capital invertido en la operación. Una forma aproximada: `ROIC = NOPAT / capital invertido promedio`.

La comparación gerencial clave es `ROIC` contra costo de capital: crecer con ROIC persistentemente inferior al costo de capital puede destruir valor. Pero no uses ROIC de un año aislado para negocios en inversión temprana; analiza cohorte de inversiones, madurez y retorno incremental.
''')
note(119, r'''
### Valor presente y DCF como máquina de supuestos

El principio es `PV = CF_t / (1+r)^t`. Una valoración DCF suma flujos explícitos y valor terminal. No empieces por Excel: primero define **qué flujo** valoras y quién tiene derecho a él. Para FCFF, la tasa suele relacionarse con WACC; para equity cash flow, con costo de equity.

El valor terminal suele dominar el resultado, por lo que crecimiento terminal y tasa de descuento requieren sensibilidad. Presenta al menos un rango de `r` y `g`, no un único decimal. Damodaran y Koller son útiles precisamente porque obligan a conectar narrativa, drivers operativos y valoración.
''')
note(120, r'''
### Contrato de un comité de inversión

Una propuesta debe mostrar: problema/oportunidad, alternativa base (“no hacer”), desembolsos, flujos incrementales, supuestos, escenarios, NPV/IRR cuando correspondan, riesgos, reversibilidad, owner y post-audit. Nunca atribuyas beneficios hundidos o corporativos sin causalidad al proyecto.

La pregunta de comité no es “¿el NPV es positivo?” sino “¿qué supuesto explica mayor parte del valor, qué evidencia lo respalda y qué haremos si falla?”. Incluye sensibilidad y *pre-mortem* antes de aprobar capital.
''')

note(126, r'''
### Matemática mínima del pipeline

Pipeline es una distribución de oportunidades por etapa, no una lista de deseos. Calcula conversiones entre etapas, ciclo de venta y cobertura. Un forecast simple puede ser `Σ(valor oportunidad × probabilidad calibrada)`, pero las probabilidades deben provenir de históricos por etapa/segmento, no de optimismo del vendedor.

Separa **pipeline coverage** de forecast: tener 3× cuota en pipeline no implica 3× probabilidad de éxito si la calidad es baja. Revisa aging, slippage y concentración por cuenta.
''')
note(129, r'''
### Precio, valor y concesión

Pricing no comienza en costo + margen. Nagle propone pensar en valor económico y segmentación; el costo actúa como restricción, no como único ancla. Calcula el impacto de descuento: con margen bruto de 40 %, un descuento de 10 % puede exigir un aumento de volumen mucho mayor que 10 % para conservar beneficio bruto.

Toda concesión debe intercambiarse por algo: plazo, volumen, compromiso, referencia, pago anticipado o reducción de alcance. Registra *give/get* para evitar que negociar se convierta en regalar margen.
''')
note(141, r'''
### Funnel como sistema de tasas

Modela etapas con numeradores y denominadores coherentes: visita → lead → oportunidad → compra. La conversión total es producto de conversiones parciales cuando las cohortes y ventanas son compatibles. Una mejora grande en una etapa pequeña puede impactar menos que una mejora modesta en el cuello principal.

Segmenta por canal, cohorte y tipo de cliente; una tasa agregada puede esconder mix. No optimices conversión sacrificando calidad, devoluciones, churn o margen.
''')
note(155, r'''
### Product-market fit como conjunto de señales

PMF no es una encuesta aislada. Combina retención/cohortes, intensidad de uso, crecimiento orgánico/referidos, willingness to pay y evidencia cualitativa de que el producto resuelve un problema importante. En productos de distinta frecuencia, la ventana de retención debe ajustarse al hábito esperado.

Una señal útil es que cohortes de retención dejan de caer hacia cero, pero no existe un umbral universal. El error frecuente es escalar adquisición antes de comprobar retención, multiplicando un embudo con fuga.
''')
note(159, r'''
### Cinco fuerzas como estructura de rentabilidad

El marco de Porter analiza rivalidad, amenaza de entrantes, sustitutos, poder de compradores y poder de proveedores. No es una checklist de “alto/medio/bajo”: cada fuerza debe conectarse con un mecanismo que presione precios, costos o inversión requerida.

Distingue **industria** de competidores individuales. Una empresa puede ejecutar bien dentro de una estructura poco atractiva; estrategia exige decidir cómo posicionarse frente a esas fuerzas o cambiar la estructura mediante actividades, contratos, switching costs u otros mecanismos legítimos.
''')
note(160, r'''
### VRIO y capacidad real

Un recurso/capacidad produce ventaja sostenible solo si es valioso, relativamente raro, difícil de imitar/sustituir y la organización está preparada para capturar valor. “Tenemos buenos ingenieros” no es análisis VRIO: debes explicar qué sistema de contratación, aprendizaje, arquitectura, datos o relaciones produce una capacidad repetible.

La O de organización evita romantizar recursos: una patente sin go-to-market o datos sin derechos/procesos no capturan valor.
''')
note(174, r'''
### Los tres niveles de cultura de Schein

Schein distingue **artefactos** visibles, **valores declarados** y **supuestos básicos** difíciles de observar directamente. Un póster “customer first” es artefacto/valor declarado; si los incentivos castigan reportar problemas, la conducta revela un supuesto operativo distinto.

Diagnostica cultura comparando lo que la organización dice, recompensa, tolera y sanciona. No etiquetes “cultura tóxica” como explicación final: identifica mecanismos concretos —incentivos, selección, historias, decisiones de líderes, sistemas de información— que reproducen el patrón.
''')
note(181, r'''
### ERM: riesgo ligado a objetivos

Un registro de riesgos sin estrategia es inventario, no ERM. Parte del objetivo, identifica eventos/incertidumbres, evalúa impacto/probabilidad/velocidad cuando corresponda, define respuesta y owner, y monitorea riesgo residual. COSO ERM integra estrategia y desempeño; ISO 31000 enfatiza principios, marco y proceso.

Distingue riesgo inherente de residual y control preventivo de detectivo/correctivo. Una matriz 5×5 ayuda a priorizar, pero su precisión es ordinal; no conviertas colores en falsa matemática.
''')
note(187, r'''
### NIST CSF 2.0 desde gobierno

CSF 2.0 organiza outcomes en **Govern, Identify, Protect, Detect, Respond, Recover**. Para un ejecutivo, `Govern` es crucial: contexto, roles, políticas, riesgo de terceros y supervisión. El objetivo no es “cumplir un framework” sino traducir riesgo cibernético a decisiones de negocio y resiliencia.

Pide evidencia de cobertura de activos críticos, identidad/acceso, backups probados, detección, respuesta ejercitada y recuperación. Una herramienta comprada no equivale a una capacidad operativa.
''')
note(188, r'''
### NIST AI RMF y ciclo de riesgo

AI RMF organiza trabajo en **Govern, Map, Measure, Manage**. `Map` obliga a comprender contexto y afectados; `Measure` evalúa propiedades/riesgos con métodos apropiados; `Manage` prioriza respuestas; `Govern` atraviesa el ciclo.

Para cada caso de IA registra propósito, datos, modelo/proveedor, decisiones que afecta, supervisión humana, métricas de calidad, fallos previsibles, privacidad/seguridad, sesgo y plan de incidentes. “Tiene human-in-the-loop” no basta si la persona no tiene información, tiempo o autoridad real para intervenir.
''')
note(205, r'''
### Separar propiedad, dirección y supervisión

Gobierno corporativo responde quién posee, quién administra y quién supervisa. Accionistas no gestionan cada operación; el directorio supervisa, orienta y nombra/evalúa alta dirección según el marco aplicable; el management ejecuta. En empresas pequeñas los roles pueden recaer en las mismas personas, pero conviene separar **sombreros** para reducir conflictos.

La pregunta práctica es: ¿esta decisión corresponde al owner, al board o al management? Documentar reserved matters evita tanto microgestión del directorio como concentración opaca en el CEO.
''')
note(206, r'''
### Un directorio no es un comité operativo

Un buen directorio dedica atención a estrategia, desempeño, capital, riesgo, CEO/talento, controles y sostenibilidad del negocio según contexto. Su información debe ser suficiente para desafiar management sin administrar por detalle.

Diseña un board calendar anual y un board pack que diferencie `información`, `discusión` y `decisión`. La calidad de preguntas importa más que el número de diapositivas.
''')
note(209, r'''
### Conflictos, independencia y deberes

Gobierno exige identificar conflictos antes de votar, declarar intereses y aplicar mecanismos de abstención/recusación o aprobación según norma y estatutos. “Independencia” no significa ausencia de experiencia o relación humana; se refiere a capacidad de juicio libre de relaciones que comprometan objetividad bajo el marco aplicable.

Distingue un conflicto real, potencial y percibido. En materias legales concretas, usa estatutos y legislación vigente; el curso entrena el mapa de decisión, no reemplaza asesoría jurídica.
''')

note(217, r'''
### Estructura de capital como trade-off

Deuda ofrece prioridad contractual y puede tener ventajas fiscales según jurisdicción; equity absorbe riesgo residual y diluye propiedad/control. No existe ratio universal óptimo. Evalúa estabilidad de caja, activos, covenants, flexibilidad, riesgo de refinanciamiento y etapa.

Usa escenarios de downside: una estructura que maximiza ROE en el caso base puede destruir opcionalidad cuando ventas caen. La capacidad de sobrevivir importa junto al costo promedio de capital.
''')
note(218, r'''
### WACC, CAPM y spread de creación de valor

Una forma estándar es `WACC = E/(D+E) × Ke + D/(D+E) × Kd × (1-T)`, con ponderaciones a valor económico/mercado cuando sea posible. En CAPM, `Ke = Rf + β × ERP` (más ajustes solo si están justificados). `Kd` debe reflejar costo marginal de deuda, no necesariamente el cupón histórico.

Si `WACC = 9 %` y un proyecto con riesgo comparable tiene `IRR = 12 %`, el spread parece positivo; pero si el proyecto opera en otra tecnología/país/riesgo, usar el WACC corporativo puede inflar NPV. Ejecuta sensibilidad de `WACC`, beta/ERP y flujos; la precisión de la tasa nunca debe superar la calidad de los inputs.
''')
note(219, r'''
### Deuda versus equity: costo total, no solo tasa

Compara coste financiero, vencimiento, garantías, covenants, dilución, derechos de control, flexibilidad y riesgo de insolvencia. Equity suele ser más caro económicamente porque asume riesgo residual, aunque no tenga una cuota contractual mensual.

Construye una tabla de escenarios base/downside/upside y prueba si la empresa conserva liquidez bajo deuda. Una ronda de equity que evita insolvencia puede crear más valor que deuda “barata” imposible de servir.
''')
note(220, r'''
### DCF paso a paso

Para FCFF, una formulación común es `FCFF = NOPAT + D&A - CAPEX - ΔNWC`. Descuenta cada periodo por una tasa coherente con riesgo y flujo. Valor terminal por perpetuidad: `TV = FCF_(n+1)/(WACC-g)`, con `g < WACC` y crecimiento sostenible.

Después calcula sensibilidad WACC/g y de drivers operativos. Si 70–90 % del enterprise value viene del terminal, dilo explícitamente: la valoración depende más de supuestos lejanos que del forecast cercano.
''')
note(221, r'''
### Múltiplos y comparables

`EV/EBITDA`, `EV/Revenue` y `P/E` comparan cosas distintas. Enterprise-value multiples usan métricas antes de efectos de financiación; equity multiples corresponden a valor para accionistas. Selecciona comparables por economía, crecimiento, margen, riesgo y modelo, no solo por industria nominal.

Normaliza EBITDA/earnings y explica mediana, rango y diferencias estructurales. Un múltiplo no “valora solo”: resume expectativas incorporadas por mercado y requiere una narrativa de por qué la empresa merece prima o descuento.
''')
note(222, r'''
### Fundraising como necesidad de capital + hitos

Parte de runway y milestones: cuánto capital se necesita para alcanzar qué evidencia de reducción de riesgo. Una ronda más grande reduce riesgo de liquidez pero puede aumentar dilución y expectativas. Modela base/downside y un buffer explícito.

La narrativa financiera debe reconciliar uso de fondos, contratación, crecimiento, unit economics y siguiente hito financiable. “18 meses de runway” sin plan de hitos es solo una duración.
''')
note(223, r'''
### Cap table y dilución

Trabaja siempre en base fully diluted cuando corresponda y distingue pre-money/post-money. Si una empresa vale 8 pre-money y recibe 2, post-money = 10; el nuevo inversor tendría 20 % antes de considerar otros ajustes. Una ampliación de option pool pre-money puede diluir principalmente a founders existentes.

Modela rondas sucesivas, options, convertibles/SAFEs según términos reales y escenarios de salida. Porcentajes sin número de acciones y derechos pueden ocultar errores.
''')
note(224, r'''
### Term sheet: economics y control

Separa términos económicos (valuation, liquidation preference, participation, anti-dilution, dividends) de control/gobierno (board, voting, protective provisions, information rights). Un precio alto puede venir acompañado de términos de control costosos.

Modela al menos tres outcomes de salida para entender preferencias. No negocies cláusulas legales desde un resumen educativo: term sheets reales requieren abogado especializado y revisión del documento completo.
''')
note(225, r'''
### M&A: tesis antes del precio

La lógica debe explicar fuente de valor: sinergias de ingresos/costos, activos/capacidades, acceso a mercado, consolidación u opciones estratégicas. Separa valor standalone de sinergias y del precio pagado; pagar toda la sinergia al vendedor deja poco valor al comprador.

Escribe la tesis en hipótesis verificables y asigna un owner de integración antes del cierre. El fracaso de integración puede destruir una tesis financieramente atractiva.
''')
note(226, r'''
### Due diligence como prueba de hipótesis

No es una carpeta de documentos; es un proceso para comprobar qué debe ser verdad para sostener precio y términos. Organiza workstreams financiero, legal, comercial, producto/tech, personas, impuestos, ciber/datos y operaciones según transacción.

Cada hallazgo debe mapearse a una acción: ajustar precio, cambiar contrato, crear indemnity/escrow, exigir condición precedente, diseñar integración o abandonar. “Riesgo identificado” sin respuesta no cierra diligence.
''')
note(227, r'''
### Integración: valor y continuidad

Antes de Day 1 define decisiones sobre liderazgo, customer continuity, sistemas críticos, talento clave y controles. Distingue integración necesaria de áreas que conviene mantener separadas para proteger valor.

Usa un synergy tracker con baseline, owner, fecha y costo de captura. Medir solo “sinergias prometidas” incentiva reetiquetar ahorro existente; exige incrementalidad.
''')
note(228, r'''
### Comité de capital

El comité compara usos alternativos del capital: reinversión orgánica, deuda, adquisiciones, dividendos/buybacks cuando correspondan, liquidez y opciones futuras. Toda propuesta compite con una tasa mínima y con el costo de oportunidad de perder flexibilidad.

El memo final debe incluir retorno esperado, distribución de outcomes, downside, liquidez, covenants/dilución, riesgos no financieros y post-audit. Capital allocation es un sistema de aprendizaje, no un evento anual.
''')

note(260, r'''
### Mapa laboral chileno: tipo, realidad de la relación y obligaciones

Empieza por los **hechos**, no por el nombre del documento. Si existen prestación personal, subordinación/dependencia y remuneración en los términos que determine el marco legal, llamar “honorarios” a la relación no neutraliza el riesgo laboral. Para trabajo dependiente, distingue contrato indefinido, plazo fijo y obra/faena; después agrega modalidad de jornada/teletrabajo u otros regímenes aplicables.

Como control ejecutivo, separa cinco capas: `1) naturaleza de la relación; 2) tipo de contrato; 3) jornada y remuneraciones; 4) cotizaciones, seguridad y prevención; 5) modificación/término y documentación`. A agosto de 2026, la DT confirma que desde **26-04-2026** la jornada ordinaria máxima general se redujo de 44 a **42 horas**; no confundas ese estado vigente con la meta final de 40 horas. Ley Karin exige prevención e investigación/sanción dentro de su marco, y el DS 44 moderniza la gestión preventiva de riesgos laborales. Verifica siempre DT, BCN/LeyChile, SUSESO y Subsecretaría de Previsión Social antes de ejecutar una decisión real.
''')
