# Informe de calidad pedagógica — v2.0.0

## Motivo de la reescritura

La versión 1.x cumplía estructuralmente con 288 clases, pero una auditoría interna mostró un problema: muchas clases compartían texto genérico y su profundidad mediana rondaba unas 600–650 palabras. El repositorio podía parecer completo por conteo sin ofrecer una experiencia equivalente a los programas maduros de IA y Finanzas/Banca.

La versión 2.0 cambia el criterio de “completo”: **una clase no aprueba por tener encabezados; debe contener materia específica, fuentes aplicadas, ejemplo, decisión, práctica y evaluación propia**.

## Métricas actuales

| Control | Resultado |
|---|---:|
| Clases | 288 |
| Palabras por clase | 3.168–3.987 |
| Mediana | 3.379 |
| Referencias por clase | 11–18 |
| Subsecciones de desarrollo | ≥ 6 |
| Evaluaciones | 288 |
| Evaluaciones con contenido idéntico | 0 |
| Catálogo bibliográfico/primario | 229 fuentes |
| Profundizaciones técnicas/regulatorias adicionales | 38 clases |
| Párrafos largos repetidos en ≥4 clases | 0 según validador |
| Pares con similitud anormal dentro de una parte | 0 según umbral automático |

## Qué se valida

`tools/validate_depth.py` falla si detecta:

- clase bajo el mínimo de profundidad;
- secciones pedagógicas ausentes;
- menos de cinco fuentes;
- menos de cinco bloques de desarrollo;
- preguntas insuficientes;
- párrafos largos copiados en cuatro o más clases;
- similitud léxica anormal entre clases de la misma parte;
- clases regulatorias Chile sin fuente oficial.

## Qué NO demuestra el validador

El conteo automático no certifica verdad conceptual, vigencia normativa ni calidad de una decisión real. Por eso el diseño agrega bibliografía, fuentes primarias y la obligación de registrar edición/páginas consultadas. Las materias vivas deben revalidarse antes de uso profesional.

## Estándar pedagógico

La estructura se inspira en:

- Ambrose et al. — *How Learning Works*;
- Brown, Roediger & McDaniel — *Make It Stick*;
- Wiggins & McTighe — *Understanding by Design*;
- Ericsson & Pool — *Peak*;
- William Ellet — *The Case Study Handbook*.

La **estructura** puede ser consistente; el **contenido** no puede ser intercambiable. Cada clase tiene una especificación propia con concepto central, cinco conceptos, método, evidencia, caso, límites y fuentes seleccionadas.

## Profundización disciplinaria

Además de las 288 especificaciones, 38 materias donde una explicación genérica sería particularmente dañina agregan un bloque técnico específico. Incluyen, entre otras:

- estados financieros, flujo de caja, márgenes, capital de trabajo, break-even, unit economics, ROI/ROIC y valoración;
- pipeline, pricing, funnel y product-market fit;
- Porter, VRIO y cultura según Schein;
- ERM, NIST CSF 2.0 y NIST AI RMF;
- directorios, conflictos e independencia;
- estructura de capital, WACC, DCF, múltiplos, cap table, term sheets, M&A y due diligence;
- contratación y obligaciones laborales en Chile con fuentes oficiales vigentes.
