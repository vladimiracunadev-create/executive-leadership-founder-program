# Evaluación — Clase 259: Cuenta bancaria, pagos y medios de cobro

Esta evaluación exige haber estudiado la clase y sus fuentes; respuestas genéricas sin evidencia no cumplen el criterio.

## A. Comprensión conceptual — 25 %

1. Distingue **business bank account** de **merchant acquiring** y crea un ejemplo donde confundirlos cambie la acción gerencial.
2. Explica **settlement** a partir de su definición operacional y señala una observación que la refutaría.
3. Relaciona **chargeback** con **payment approval**: ¿son causa, restricción, resultado o lentes distintos? Justifica.

## B. Caso de decisión — 30 %

**Caso:** Una startup cobra por tres pasarelas. Finanzas compara ventas con saldo bancario sin considerar fees ni settlement; cada mes aparecen diferencias que nadie puede explicar.

Construye dos alternativas plausibles. Para cada una indica beneficio esperado, costo de oportunidad, riesgo, reversibilidad y qué actor asume la consecuencia. Después recomienda una y declara qué nueva información cambiaría tu decisión.

## C. Método y evidencia — 30 %

Aplica **seleccionar medios por cliente y costo → definir cuentas y roles → mapear settlement y fees → implementar approvals y reconciliation → monitorear fraude y chargebacks**. Debes utilizar o diseñar cómo obtener **settlement delay, payment fees, chargeback rate**. Separa hechos, inferencias y supuestos; una métrica sin baseline o periodo no cuenta como evidencia suficiente.

## D. Fuentes, límites y red team — 15 %

Contrasta dos referencias de la clase. Resume con tus palabras qué lente aporta cada una, identifica una tensión y explica cómo modifica tu recomendación. Luego responde al límite: **Productos bancarios y condiciones cambian por proveedor. Compara contratos, seguridad y costos vigentes y no dependas de una sola persona para accesos críticos.**

## Criterios de aprobación

| Criterio | Peso | Evidencia esperada |
|---|---:|---|
| Precisión conceptual | 25 % | Distinciones correctas y observables; no definiciones memorizadas. |
| Diagnóstico y evidencia | 30 % | Datos/señales pertinentes, baseline, alternativas causales y supuestos explícitos. |
| Decisión y trade-offs | 30 % | Dos opciones defendibles, costo de oportunidad, riesgo y condición de revisión. |
| Fuentes y comunicación | 15 % | Dos lecturas realmente utilizadas, trazabilidad y argumento ejecutivo claro. |

**Aprobación sugerida:** 80/100 y ningún criterio bajo 60 %. Una respuesta que podría copiarse sin cambiar nada a otra clase se considera insuficiente.
