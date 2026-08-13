# Evaluación — Clase 019: Análisis de causa raíz

Esta evaluación exige haber estudiado la clase y sus fuentes; respuestas genéricas sin evidencia no cumplen el criterio.

## A. Comprensión conceptual — 25 %

1. Distingue **causa raíz** de **causa contribuyente** y crea un ejemplo donde confundirlos cambie la acción gerencial.
2. Explica **5 porqués** a partir de su definición operacional y señala una observación que la refutaría.
3. Relaciona **Ishikawa** con **contrafactual**: ¿son causa, restricción, resultado o lentes distintos? Justifica.

## B. Caso de decisión — 30 %

**Caso:** Un despliegue provoca una caída de dos horas. La explicación inicial es 'un desarrollador olvidó revisar un flag', pero el cambio pasó por un proceso sin checklist, revisión independiente ni prueba automatizada.

Construye dos alternativas plausibles. Para cada una indica beneficio esperado, costo de oportunidad, riesgo, reversibilidad y qué actor asume la consecuencia. Después recomienda una y declara qué nueva información cambiaría tu decisión.

## C. Método y evidencia — 30 %

Aplica **definir evento y alcance → reconstruir línea de tiempo → generar causas potenciales sin culpabilizar → buscar evidencia y contrafactuales → diseñar acciones sobre sistema y verificar recurrencia**. Debes utilizar o diseñar cómo obtener **reincidencia del incidente, tiempo entre fallos, acciones correctivas cerradas**. Separa hechos, inferencias y supuestos; una métrica sin baseline o periodo no cuenta como evidencia suficiente.

## D. Fuentes, límites y red team — 15 %

Contrasta dos referencias de la clase. Resume con tus palabras qué lente aporta cada una, identifica una tensión y explica cómo modifica tu recomendación. Luego responde al límite: **No todos los problemas justifican root-cause analysis profundo. En eventos pequeños y aislados puede costar más que el riesgo evitado; usa proporcionalidad y reserva análisis exhaustivo para recurrencia o severidad material.**

## Criterios de aprobación

| Criterio | Peso | Evidencia esperada |
|---|---:|---|
| Precisión conceptual | 25 % | Distinciones correctas y observables; no definiciones memorizadas. |
| Diagnóstico y evidencia | 30 % | Datos/señales pertinentes, baseline, alternativas causales y supuestos explícitos. |
| Decisión y trade-offs | 30 % | Dos opciones defendibles, costo de oportunidad, riesgo y condición de revisión. |
| Fuentes y comunicación | 15 % | Dos lecturas realmente utilizadas, trazabilidad y argumento ejecutivo claro. |

**Aprobación sugerida:** 80/100 y ningún criterio bajo 60 %. Una respuesta que podría copiarse sin cambiar nada a otra clase se considera insuficiente.
