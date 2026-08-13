# Estándar pedagógico de profundidad

Este repositorio no considera una clase "completa" por tener una plantilla con encabezados. Una clase se considera completa cuando su contenido es **específico del tema**, deriva de fuentes identificables y permite demostrar una competencia observable.

## Contrato obligatorio de una clase

Cada clase debe contener, como mínimo:

1. **Propósito conectado con la clase anterior y la siguiente.** Debe explicar qué problema profesional resuelve el tema.
2. **Resultados de aprendizaje verificables.** Verbos observables: diagnosticar, calcular, diseñar, comparar, decidir, defender, auditar o construir.
3. **Agenda pedagógica.** Recuperación, explicación, ejemplo trabajado, práctica, comprobación y cierre.
4. **Conceptos centrales propios.** Al menos cinco conceptos específicos, definidos con criterios que permitan distinguirlos de conceptos cercanos.
5. **Modelo mental o marco operativo.** Debe permitir razonar, no memorizar una definición.
6. **Desarrollo profundo.** Al menos cinco subsecciones sustantivas y específicas del tema; cuando corresponda, fórmulas, matrices, secuencias, tablas o criterios de decisión.
7. **Ejemplo trabajado.** Resuelto paso a paso. No basta con describir un caso.
8. **Comparación o límites.** Cuándo usar el enfoque, cuándo no y qué alternativa existe.
9. **Aplicación ejecutiva.** Cómo cambia el uso del concepto al pasar de profesional a jefe, gerente, CEO, founder u owner.
10. **Caso de decisión.** Con restricciones, datos, stakeholders, incertidumbre y consecuencias.
11. **Práctica y entregable.** Evidencia tangible para el portafolio.
12. **Errores frecuentes.** Formato síntoma → causa → corrección cuando sea útil.
13. **Preguntas de comprobación.** Deben depender del contenido concreto de la clase.
14. **Fuentes y verificación.** Mínimo cinco referencias pertinentes; se priorizan libros de referencia, papers, estándares y fuentes oficiales. Para regulación o datos variables se registra fecha de verificación.

## Principios de diseño instruccional

El programa combina cuatro ideas pedagógicas:

- **Diseño inverso:** primero se define la competencia que se quiere observar y luego el contenido y la evaluación que permiten demostrarla. Referencia: Wiggins & McTighe, *Understanding by Design*.
- **Ejemplos trabajados y práctica deliberada:** la explicación culmina en una resolución visible antes de pedir desempeño autónomo. Referencias: Ericsson & Pool, *Peak*; Ambrose et al., *How Learning Works*.
- **Recuperación y transferencia:** cada clase recupera conceptos previos y los usa en una situación nueva. Referencia: Brown, Roediger & McDaniel, *Make It Stick*.
- **Método de casos:** en management no basta saber una definición; se debe decidir con información incompleta, restricciones y consecuencias. Se separan hechos, supuestos, análisis, decisión y revisión.

## Qué está prohibido

- Párrafos genéricos repetidos en varias clases.
- Cambiar solo el título dentro de la misma explicación.
- Referencias idénticas en todas las clases de una parte sin justificar su relación con el tema.
- Casos donde siempre se pide "formular tres hipótesis" independientemente de la materia.
- Evaluaciones que puedan responderse sin haber leído la clase.
- Presentar una ley, porcentaje, umbral, trámite o estándar variable sin fuente oficial y fecha de verificación.

## Umbrales automáticos

`tools/validate_depth.py` controla:

- profundidad mínima de texto;
- número de subsecciones y referencias;
- presencia de ejemplo trabajado;
- preguntas específicas;
- repetición de párrafos largos;
- similitud léxica anormal entre clases;
- referencias oficiales en las clases regulatorias de Chile.

El validador no reemplaza la revisión humana de exactitud, pero impide volver al patrón de "plantilla rellenada".
