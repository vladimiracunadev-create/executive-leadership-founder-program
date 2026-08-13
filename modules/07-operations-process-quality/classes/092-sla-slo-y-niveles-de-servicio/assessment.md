# Evaluación — Clase 092: SLA, SLO y niveles de servicio

Esta evaluación exige haber estudiado la clase y sus fuentes; respuestas genéricas sin evidencia no cumplen el criterio.

## A. Comprensión conceptual — 25 %

1. Distingue **SLI** de **SLO** y crea un ejemplo donde confundirlos cambie la acción gerencial.
2. Explica **SLA** a partir de su definición operacional y señala una observación que la refutaría.
3. Relaciona **error budget** con **availability**: ¿son causa, restricción, resultado o lentes distintos? Justifica.

## B. Caso de decisión — 30 %

**Caso:** Un servicio promete 99,9% SLA y usa exactamente 99,9% como objetivo interno. Cualquier desviación rompe contrato porque no existe margen operacional.

Construye dos alternativas plausibles. Para cada una indica beneficio esperado, costo de oportunidad, riesgo, reversibilidad y qué actor asume la consecuencia. Después recomienda una y declara qué nueva información cambiaría tu decisión.

## C. Método y evidencia — 30 %

Aplica **seleccionar experiencia crítica y SLI → definir SLO según usuario y costo → crear buffer antes del SLA → medir error budget → tocar capacidad o cambios cuando se consume**. Debes utilizar o diseñar cómo obtener **availability, latency percentiles, error budget burn**. Separa hechos, inferencias y supuestos; una métrica sin baseline o periodo no cuenta como evidencia suficiente.

## D. Fuentes, límites y red team — 15 %

Contrasta dos referencias de la clase. Resume con tus palabras qué lente aporta cada una, identifica una tensión y explica cómo modifica tu recomendación. Luego responde al límite: **Más nueves cuestan mucho y pueden no crear valor. La confiabilidad objetivo debe responder al impacto del usuario, no al deseo abstracto de perfección.**

## Criterios de aprobación

| Criterio | Peso | Evidencia esperada |
|---|---:|---|
| Precisión conceptual | 25 % | Distinciones correctas y observables; no definiciones memorizadas. |
| Diagnóstico y evidencia | 30 % | Datos/señales pertinentes, baseline, alternativas causales y supuestos explícitos. |
| Decisión y trade-offs | 30 % | Dos opciones defendibles, costo de oportunidad, riesgo y condición de revisión. |
| Fuentes y comunicación | 15 % | Dos lecturas realmente utilizadas, trazabilidad y argumento ejecutivo claro. |

**Aprobación sugerida:** 80/100 y ningún criterio bajo 60 %. Una respuesta que podría copiarse sin cambiar nada a otra clase se considera insuficiente.
