# Evaluación — Clase 237: Arquitectura y deuda técnica para ejecutivos

Esta evaluación exige haber estudiado la clase y sus fuentes; respuestas genéricas sin evidencia no cumplen el criterio.

## A. Comprensión conceptual — 25 %

1. ¿Qué es un atributo de calidad y cómo se relaciona con la estrategia?
2. ¿Qué propone Parnas sobre la modularidad?
3. ¿Qué es la deuda técnica y qué tipos hay?

## B. Caso de decisión — 30 %

**Caso:** Una empresa de servicios financieros con 1.700 personas y un núcleo de sistemas de 18 años tiene 90 ingenieros en tecnología (costo de 4.300 millones al año). Hechos: un cambio simple en tarifas toma 11 semanas y requiere coordinar a seis equipos; hubo 17 incidentes en el año (costo medio de 45 millones y uno de 400 millones con sanción del regulador); el 52 % del tiempo de los equipos se va en retrabajo, pruebas manuales y coordinación; hay 63 componentes con versiones sin soporte, algunos con vulnerabilidades conocidas; dos ingenieros con 20 años de antigüedad son los únicos que conocen módulos críticos; el costo de los sistemas antiguos es de 3.100 millones al año en licencias. El área de tecnología propone una reescritura completa de 14.000 millones en cuatro años; el área de negocio quiere congelar el sistema y construir encima; el director de riesgos advierte la exposición; el regulador pide un plan.

Construye dos alternativas plausibles. Para cada una indica beneficio esperado, costo de oportunidad, riesgo, reversibilidad y qué actor asume la consecuencia. Después recomienda una y declara qué nueva información cambiaría tu decisión.

## C. Método y evidencia — 30 %

Entrega un **plan de arquitectura y deuda técnica** que contenga: (a) los atributos de calidad que exige la estrategia y el estado actual; (b) el mapa de dependencias y cuellos de botella con el costo de cambio; (c) la cuantificación de la deuda en tiempo, riesgo y costo; (d) la comparación de remediar, estabilizar, aislar, reescribir y retirar según el horizonte de vida; (e) la priorización, el financiamiento por etapas con criterios de liberación y la prevención de nueva deuda; (f) las métricas de salud técnica y las verificaciones regulatorias, de seguridad y contractuales pendientes. Separa hechos, inferencias y supuestos.

## D. Fuentes, límites y red team — 15 %

Contrasta dos de las fuentes de la clase: qué aporta cada una, qué tensión hay entre ellas y cómo cambia tu recomendación. Luego responde al límite de la clase: No toda deuda debe pagarse.

## Criterios de aprobación

| Criterio | Peso | Evidencia esperada |
|---|---:|---|
| Precisión conceptual | 25 % | Definiciones correctas, con la fuente y con un ejemplo propio. |
| Diagnóstico y evidencia | 30 % | Cada afirmación del caso respaldada por un hecho y separada de la suposición. |
| Decisión y trade-offs | 30 % | Dos opciones defendibles, costo de oportunidad, riesgo y condición de revisión. |
| Fuentes y comunicación | 15 % | Dos lecturas realmente utilizadas, trazabilidad y argumento claro. |

**Aprobación sugerida:** 80/100 y ningún criterio bajo 60 %. Una respuesta que podría copiarse sin cambiar nada a otra clase se considera insuficiente.
