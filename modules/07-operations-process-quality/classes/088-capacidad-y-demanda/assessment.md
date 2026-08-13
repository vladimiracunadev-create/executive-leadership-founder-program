# Evaluación — Clase 088: Capacidad y demanda

Esta evaluación exige haber estudiado la clase y sus fuentes; respuestas genéricas sin evidencia no cumplen el criterio.

## A. Comprensión conceptual — 25 %

1. Distingue **demand rate** de **capacity rate** y crea un ejemplo donde confundirlos cambie la acción gerencial.
2. Explica **utilization** a partir de su definición operacional y señala una observación que la refutaría.
3. Relaciona **queue** con **buffer**: ¿son causa, restricción, resultado o lentes distintos? Justifica.

## B. Caso de decisión — 30 %

**Caso:** Un equipo procesa en promedio 100 solicitudes semanales y recibe 98. Dirección concluye que hay capacidad suficiente, pero la llegada varía entre 70 y 140 y la cola crece cada fin de mes.

Construye dos alternativas plausibles. Para cada una indica beneficio esperado, costo de oportunidad, riesgo, reversibilidad y qué actor asume la consecuencia. Después recomienda una y declara qué nueva información cambiaría tu decisión.

## C. Método y evidencia — 30 %

Aplica **medir demanda por tipo y periodo → medir capacidad efectiva → segmentar variabilidad y picos → diseñar buffer o flex capacity → regular ingreso cuando supera sistema**. Debes utilizar o diseñar cómo obtener **utilization, queue length, wait time**. Separa hechos, inferencias y supuestos; una métrica sin baseline o periodo no cuenta como evidencia suficiente.

## D. Fuentes, límites y red team — 15 %

Contrasta dos referencias de la clase. Resume con tus palabras qué lente aporta cada una, identifica una tensión y explica cómo modifica tu recomendación. Luego responde al límite: **Más buffer cuesta dinero. La meta no es baja utilización universal, sino equilibrar costo de capacidad con costo de espera, pérdida de demanda y criticidad.**

## Criterios de aprobación

| Criterio | Peso | Evidencia esperada |
|---|---:|---|
| Precisión conceptual | 25 % | Distinciones correctas y observables; no definiciones memorizadas. |
| Diagnóstico y evidencia | 30 % | Datos/señales pertinentes, baseline, alternativas causales y supuestos explícitos. |
| Decisión y trade-offs | 30 % | Dos opciones defendibles, costo de oportunidad, riesgo y condición de revisión. |
| Fuentes y comunicación | 15 % | Dos lecturas realmente utilizadas, trazabilidad y argumento ejecutivo claro. |

**Aprobación sugerida:** 80/100 y ningún criterio bajo 60 %. Una respuesta que podría copiarse sin cambiar nada a otra clase se considera insuficiente.
