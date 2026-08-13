# Evaluación — Clase 089: Cuellos de botella y teoría de restricciones

Esta evaluación exige haber estudiado la clase y sus fuentes; respuestas genéricas sin evidencia no cumplen el criterio.

## A. Comprensión conceptual — 25 %

1. Distingue **constraint** de **bottleneck** y crea un ejemplo donde confundirlos cambie la acción gerencial.
2. Explica **throughput** a partir de su definición operacional y señala una observación que la refutaría.
3. Relaciona **buffer** con **subordination**: ¿son causa, restricción, resultado o lentes distintos? Justifica.

## B. Caso de decisión — 30 %

**Caso:** Una línea tiene cinco etapas. Cuatro producen 120 unidades/día y una 70. El director financia automatización de una etapa que ya produce 120 porque es la más visible.

Construye dos alternativas plausibles. Para cada una indica beneficio esperado, costo de oportunidad, riesgo, reversibilidad y qué actor asume la consecuencia. Después recomienda una y declara qué nueva información cambiaría tu decisión.

## C. Método y evidencia — 30 %

Aplica **medir flujo y localizar restricción → explotar capacidad sin inversión → subordinar upstream y downstream → elevar restricción si el valor lo justifica → repetir cuando migra el cuello**. Debes utilizar o diseñar cómo obtener **throughput de restricción, idle time del cuello, buffer penetration**. Separa hechos, inferencias y supuestos; una métrica sin baseline o periodo no cuenta como evidencia suficiente.

## D. Fuentes, límites y red team — 15 %

Contrasta dos referencias de la clase. Resume con tus palabras qué lente aporta cada una, identifica una tensión y explica cómo modifica tu recomendación. Luego responde al límite: **No todos los sistemas tienen un único cuello estable; mix, demanda y políticas pueden moverlo. Observa datos y horizonte antes de convertir TOC en dogma.**

## Criterios de aprobación

| Criterio | Peso | Evidencia esperada |
|---|---:|---|
| Precisión conceptual | 25 % | Distinciones correctas y observables; no definiciones memorizadas. |
| Diagnóstico y evidencia | 30 % | Datos/señales pertinentes, baseline, alternativas causales y supuestos explícitos. |
| Decisión y trade-offs | 30 % | Dos opciones defendibles, costo de oportunidad, riesgo y condición de revisión. |
| Fuentes y comunicación | 15 % | Dos lecturas realmente utilizadas, trazabilidad y argumento ejecutivo claro. |

**Aprobación sugerida:** 80/100 y ningún criterio bajo 60 %. Una respuesta que podría copiarse sin cambiar nada a otra clase se considera insuficiente.
