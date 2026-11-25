# Evaluación — Clase 143: Growth loops y experimentación

Esta evaluación exige haber estudiado la clase y sus fuentes; respuestas genéricas sin evidencia no cumplen el criterio.

## A. Comprensión conceptual — 25 %

1. ¿Qué diferencia hay entre un embudo y un ciclo de crecimiento?
2. ¿Qué tipos de ciclo existen?
3. ¿Qué mide el coeficiente de ciclo y por qué importa el tiempo de vuelta?

## B. Caso de decisión — 30 %

**Caso:** Una aplicación de finanzas personales con 500.000 usuarios lanzó un programa de referidos con USD 10 por cada invitado que se registre. El equipo de crecimiento implementó un paso en que, al registrarse, la aplicación solicita acceso a los contactos y envía invitaciones preseleccionadas con el nombre del usuario. En dos meses, los registros subieron 38 %, pero el 41 % de los referidos son cuentas que nunca se activan, se detectaron redes de cuentas falsas que cobran el incentivo, las quejas por correos no solicitados se multiplicaron por cuatro y el proveedor de correo bloqueó parte del dominio. La retención a 90 días de los referidos es de 12 %, frente a 38 % de los otros canales. La gerencia de producto propone retirar el programa; la de crecimiento, mejorarlo con controles.

Construye dos alternativas plausibles. Para cada una indica beneficio esperado, costo de oportunidad, riesgo, reversibilidad y qué actor asume la consecuencia. Después recomienda una y declara qué nueva información cambiaría tu decisión.

## C. Método y evidencia — 30 %

Entrega un **diseño de ciclo y programa de experimentos** que contenga: (a) el ciclo actual, sus pasos, el coeficiente y los problemas de calidad; (b) un rediseño del ciclo basado en valor para el usuario y su invitado; (c) las métricas de ciclo y de protección; (d) un plan de experimentos priorizado con hipótesis, muestra y criterios; (e) los controles contra fraude y spam; (f) las verificaciones de comunicaciones comerciales, consentimiento y protección de datos y del dinero que se realizarán con asesoría y las normas vigentes. Separa hechos, inferencias y supuestos.

## D. Fuentes, límites y red team — 15 %

Contrasta dos de las fuentes de la clase: qué aporta cada una, qué tensión hay entre ellas y cómo cambia tu recomendación. Luego responde al límite de la clase: Los coeficientes típicos de ciclos son menores que 1, por lo que rara vez reemplazan la adquisición: la reducen.

## Criterios de aprobación

| Criterio | Peso | Evidencia esperada |
|---|---:|---|
| Precisión conceptual | 25 % | Definiciones correctas, con la fuente y con un ejemplo propio. |
| Diagnóstico y evidencia | 30 % | Cada afirmación del caso respaldada por un hecho y separada de la suposición. |
| Decisión y trade-offs | 30 % | Dos opciones defendibles, costo de oportunidad, riesgo y condición de revisión. |
| Fuentes y comunicación | 15 % | Dos lecturas realmente utilizadas, trazabilidad y argumento claro. |

**Aprobación sugerida:** 80/100 y ningún criterio bajo 60 %. Una respuesta que podría copiarse sin cambiar nada a otra clase se considera insuficiente.
