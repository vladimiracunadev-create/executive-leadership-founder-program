# Evaluación — Clase 237: Arquitectura y deuda técnica para ejecutivos

Esta evaluación exige haber estudiado la clase y sus fuentes; respuestas genéricas sin evidencia no cumplen el criterio.

## A. Comprensión conceptual — 25 %

1. Distingue **architecture** de **technical debt** y crea un ejemplo donde confundirlos cambie la acción gerencial.
2. Explica **coupling** a partir de su definición operacional y señala una observación que la refutaría.
3. Relaciona **legacy** con **architectural runway**: ¿son causa, restricción, resultado o lentes distintos? Justifica.

## B. Caso de decisión — 30 %

**Caso:** Cada feature en billing requiere coordinación de cinco equipos y ventana nocturna. Negocio piensa que es lentitud de ingeniería; arquitectura monolítica crea el cuello.

Construye dos alternativas plausibles. Para cada una indica beneficio esperado, costo de oportunidad, riesgo, reversibilidad y qué actor asume la consecuencia. Después recomienda una y declara qué nueva información cambiaría tu decisión.

## C. Método y evidencia — 30 %

Aplica **traducir estrategia a quality attributes → mapear bottlenecks y dependencies → cuantificar debt impact → priorizar remediation por value y risk → crear guardrails y evolución incremental**. Debes utilizar o diseñar cómo obtener **change failure rate, lead time, incident rate**. Separa hechos, inferencias y supuestos; una métrica sin baseline o periodo no cuenta como evidencia suficiente.

## D. Fuentes, límites y red team — 15 %

Contrasta dos referencias de la clase. Resume con tus palabras qué lente aporta cada una, identifica una tensión y explica cómo modifica tu recomendación. Luego responde al límite: **No toda deuda debe pagarse. Si un sistema está cerca de retiro o el costo de cambio supera beneficio, gestionar el riesgo puede ser mejor que reescribir.**

## Criterios de aprobación

| Criterio | Peso | Evidencia esperada |
|---|---:|---|
| Precisión conceptual | 25 % | Distinciones correctas y observables; no definiciones memorizadas. |
| Diagnóstico y evidencia | 30 % | Datos/señales pertinentes, baseline, alternativas causales y supuestos explícitos. |
| Decisión y trade-offs | 30 % | Dos opciones defendibles, costo de oportunidad, riesgo y condición de revisión. |
| Fuentes y comunicación | 15 % | Dos lecturas realmente utilizadas, trazabilidad y argumento ejecutivo claro. |

**Aprobación sugerida:** 80/100 y ningún criterio bajo 60 %. Una respuesta que podría copiarse sin cambiar nada a otra clase se considera insuficiente.
