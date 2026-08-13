# Evaluación — Clase 248: MVP y concierge tests

Esta evaluación exige haber estudiado la clase y sus fuentes; respuestas genéricas sin evidencia no cumplen el criterio.

## A. Comprensión conceptual — 25 %

1. Distingue **concierge MVP** de **Wizard of Oz** y crea un ejemplo donde confundirlos cambie la acción gerencial.
2. Explica **manual-first** a partir de su definición operacional y señala una observación que la refutaría.
3. Relaciona **service blueprint** con **automation candidate**: ¿son causa, restricción, resultado o lentes distintos? Justifica.

## B. Caso de decisión — 30 %

**Caso:** Una startup ofrece reportes de riesgo generados manualmente a cinco clientes pagos. Aprende que 70% del trabajo está en limpieza de datos, no en el modelo esperado.

Construye dos alternativas plausibles. Para cada una indica beneficio esperado, costo de oportunidad, riesgo, reversibilidad y qué actor asume la consecuencia. Después recomienda una y declara qué nueva información cambiaría tu decisión.

## C. Método y evidencia — 30 %

Aplica **definir outcome a entregar → operar manualmente para pocos clientes → registrar steps y exceptions → medir value y willingness → automatizar solo patrón estable**. Debes utilizar o diseñar cómo obtener **time-to-value, manual hours per customer, exception rate**. Separa hechos, inferencias y supuestos; una métrica sin baseline o periodo no cuenta como evidencia suficiente.

## D. Fuentes, límites y red team — 15 %

Contrasta dos referencias de la clase. Resume con tus palabras qué lente aporta cada una, identifica una tensión y explica cómo modifica tu recomendación. Luego responde al límite: **Concierge no prueba escalabilidad. Sirve para aprender demanda y workflow; antes de escalar, modela costos y automatización necesaria.**

## Criterios de aprobación

| Criterio | Peso | Evidencia esperada |
|---|---:|---|
| Precisión conceptual | 25 % | Distinciones correctas y observables; no definiciones memorizadas. |
| Diagnóstico y evidencia | 30 % | Datos/señales pertinentes, baseline, alternativas causales y supuestos explícitos. |
| Decisión y trade-offs | 30 % | Dos opciones defendibles, costo de oportunidad, riesgo y condición de revisión. |
| Fuentes y comunicación | 15 % | Dos lecturas realmente utilizadas, trazabilidad y argumento ejecutivo claro. |

**Aprobación sugerida:** 80/100 y ningún criterio bajo 60 %. Una respuesta que podría copiarse sin cambiar nada a otra clase se considera insuficiente.
