# Evaluación — Clase 231: Economía de cloud y plataformas

Esta evaluación exige haber estudiado la clase y sus fuentes; respuestas genéricas sin evidencia no cumplen el criterio.

## A. Comprensión conceptual — 25 %

1. Distingue **cloud economics** de **elasticity** y crea un ejemplo donde confundirlos cambie la acción gerencial.
2. Explica **unit cost** a partir de su definición operacional y señala una observación que la refutaría.
3. Relaciona **FinOps** con **vendor lock-in**: ¿son causa, restricción, resultado o lentes distintos? Justifica.

## B. Caso de decisión — 30 %

**Caso:** Una SaaS crece revenue 30% pero cloud spend 70%. Nadie conoce costo por tenant y equipos sobredimensionan instancias para evitar incidentes.

Construye dos alternativas plausibles. Para cada una indica beneficio esperado, costo de oportunidad, riesgo, reversibilidad y qué actor asume la consecuencia. Después recomienda una y declara qué nueva información cambiaría tu decisión.

## C. Método y evidencia — 30 %

Aplica **mapear workloads y value drivers → calcular unit cost → identificar waste y commitments → modelar resilience y lock-in → optimizar arquitectura y governance**. Debes utilizar o diseñar cómo obtener **cloud cost per transaction, utilization, commitment coverage**. Separa hechos, inferencias y supuestos; una métrica sin baseline o periodo no cuenta como evidencia suficiente.

## D. Fuentes, límites y red team — 15 %

Contrasta dos referencias de la clase. Resume con tus palabras qué lente aporta cada una, identifica una tensión y explica cómo modifica tu recomendación. Luego responde al límite: **Optimizar costo no significa migrar todo on-premise ni eliminar managed services. Considera velocidad, talento, riesgo y costo total, no solo factura mensual.**

## Criterios de aprobación

| Criterio | Peso | Evidencia esperada |
|---|---:|---|
| Precisión conceptual | 25 % | Distinciones correctas y observables; no definiciones memorizadas. |
| Diagnóstico y evidencia | 30 % | Datos/señales pertinentes, baseline, alternativas causales y supuestos explícitos. |
| Decisión y trade-offs | 30 % | Dos opciones defendibles, costo de oportunidad, riesgo y condición de revisión. |
| Fuentes y comunicación | 15 % | Dos lecturas realmente utilizadas, trazabilidad y argumento ejecutivo claro. |

**Aprobación sugerida:** 80/100 y ningún criterio bajo 60 %. Una respuesta que podría copiarse sin cambiar nada a otra clase se considera insuficiente.
