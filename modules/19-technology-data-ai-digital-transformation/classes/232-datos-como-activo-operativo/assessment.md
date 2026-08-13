# Evaluación — Clase 232: Datos como activo operativo

Esta evaluación exige haber estudiado la clase y sus fuentes; respuestas genéricas sin evidencia no cumplen el criterio.

## A. Comprensión conceptual — 25 %

1. Distingue **data product** de **data quality** y crea un ejemplo donde confundirlos cambie la acción gerencial.
2. Explica **data owner** a partir de su definición operacional y señala una observación que la refutaría.
3. Relaciona **lineage** con **single source of truth**: ¿son causa, restricción, resultado o lentes distintos? Justifica.

## B. Caso de decisión — 30 %

**Caso:** Ventas y finanzas reportan ARR distinto porque cada una define renovación y FX de forma diferente. Ambos dashboards son técnicamente correctos según su lógica.

Construye dos alternativas plausibles. Para cada una indica beneficio esperado, costo de oportunidad, riesgo, reversibilidad y qué actor asume la consecuencia. Después recomienda una y declara qué nueva información cambiaría tu decisión.

## C. Método y evidencia — 30 %

Aplica **identificar decisiones y productos de datos → definir dominios y owners → establecer calidad y contracts → habilitar acceso con governance → medir uso incidents y value**. Debes utilizar o diseñar cómo obtener **data quality SLA, time-to-data, duplicate definitions**. Separa hechos, inferencias y supuestos; una métrica sin baseline o periodo no cuenta como evidencia suficiente.

## D. Fuentes, límites y red team — 15 %

Contrasta dos referencias de la clase. Resume con tus palabras qué lente aporta cada una, identifica una tensión y explica cómo modifica tu recomendación. Luego responde al límite: **Una única fuente física no siempre es necesaria; lo crítico es semántica y governance. Evita centralización total si destruye velocidad sin mejorar consistencia.**

## Criterios de aprobación

| Criterio | Peso | Evidencia esperada |
|---|---:|---|
| Precisión conceptual | 25 % | Distinciones correctas y observables; no definiciones memorizadas. |
| Diagnóstico y evidencia | 30 % | Datos/señales pertinentes, baseline, alternativas causales y supuestos explícitos. |
| Decisión y trade-offs | 30 % | Dos opciones defendibles, costo de oportunidad, riesgo y condición de revisión. |
| Fuentes y comunicación | 15 % | Dos lecturas realmente utilizadas, trazabilidad y argumento ejecutivo claro. |

**Aprobación sugerida:** 80/100 y ningún criterio bajo 60 %. Una respuesta que podría copiarse sin cambiar nada a otra clase se considera insuficiente.
