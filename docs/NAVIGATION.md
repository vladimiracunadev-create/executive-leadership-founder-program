# Cómo se navega el programa

El programa tiene cuatro niveles y cada página dice en cuál está, de dónde viene
y adónde sigue. Esta guía fija las reglas para que quien llega a cualquier
página sepa qué hacer a continuación.

## Los cuatro niveles

| Nivel | Qué es | Dónde vive | Qué responde |
|---|---|---|---|
| **Programa** | Las 24 partes en 6 etapas | [README](../README.md) y [temario](../SYLLABUS.md) | ¿Qué recorrido hay y en qué punto estoy? |
| **Parte** | 12 clases, 4 laboratorios y un proyecto | `modules/NN-…/README.md` | ¿De qué trata, con qué debo llegar y qué me llevo? |
| **Clase** | Una unidad de 150 minutos | `modules/NN-…/classes/NNN-…/README.md` | ¿Qué aprendo, cómo lo practico y cómo me evalúan? |
| **Práctica** | Laboratorios y proyecto de la parte | `modules/NN-…/labs/` y `project.md` | ¿Cómo demuestro que lo sé hacer? |

## Reglas de recorrido

1. **El orden importa.** Las clases son secuenciales: cada una supone la anterior.
   Se puede acelerar una clase con una prueba de dominio, pero la competencia
   debe demostrarse (véase la [ruta de aprendizaje](LEARNING_PATH.md)).
2. **Entra por la portada de la parte.** Antes de la primera clase de una parte,
   lee su portada: explica el tema, lo que hay que traer, los resultados y cómo se
   encadenan las clases.
3. **Cada clase se recorre igual.** Propósito, resultados, agenda, conceptos,
   desarrollo, práctica, errores frecuentes, preguntas de comprobación, entregable
   y fuentes. El entregable es una [plantilla](../templates/README.md).
4. **Cada página tiene miga y pie.** Arriba, la parte y la posición; abajo,
   `Anterior · Índice · Siguiente`. El «Índice» siempre lleva a la portada de la
   parte y al temario.
5. **Los laboratorios van después de las clases** que los alimentan y el proyecto
   cierra la parte. El último laboratorio enlaza al proyecto, y el proyecto, a la
   parte siguiente.
6. **Una parte se aprueba con su proyecto**, no solo leyendo. Los criterios están
   en el final de cada portada de parte.
7. **Las referencias cruzadas se declaran.** Cuando un tema se profundiza en otra
   parte, la clase lo dice; no se repite el contenido.

## Qué contiene la portada de una parte

| Sección | Para qué sirve |
|---|---|
| De qué trata | Por qué importa y cuál es su eje. |
| Con qué hay que llegar | Qué partes previas se suponen. |
| Resultados | Qué serás capaz de hacer al terminar. |
| Mapa | Cómo se relacionan clases, laboratorios y proyecto. |
| Cómo se encadenan las clases | El recorrido, en prosa. |
| Las clases | Tabla con enlace, conceptos clave, entregable y duración. |
| Riesgos característicos | Dónde suele fallar quien trabaja esta materia. |
| Glosario | Las definiciones operacionales de la parte. |
| Evidencia | Lo que queda como entregable. |
| Cómo se conecta | Qué partes alimenta. |

## Qué se genera y qué se edita a mano

La navegación **se genera**; no se edita a mano.

- `tools/build_navigation.py` escribe la portada de cada parte (entre
  `<!-- parte:inicio -->` y `<!-- parte:fin -->`), la miga y el pie de cada clase,
  y el pie de los laboratorios y proyectos. Con `--check` falla si algo está
  desfasado, y la CI lo ejecuta.
- `tools/build_diagrams.py` dibuja el **modelo mental** de cada clase como SVG
  (`modelo-mental.svg`, junto a su README) a partir de la secuencia de pasos y de
  las `evidence_signals` de `lesson.yaml`. Con `--check` falla si algo está
  desfasado.
- El contenido pedagógico propio de cada parte (de qué trata, qué se necesita,
  resultados, riesgos y evidencia) está en `curriculum/part_pedagogy.py`.
- Títulos, duraciones, entregables y conceptos salen de cada clase: se cambian
  en `lesson.yaml` o en el README de la clase y se vuelven a generar.
- Si regeneras una clase con `tools/deep_curriculum_builder.py`, ejecuta después
  `tools/build_diagrams.py` y `tools/build_navigation.py`: el generador de clases no conoce las marcas.
- Los laboratorios, el proyecto, la bibliografía y el criterio de aprobación
  de cada parte, que van después de `<!-- parte:fin -->`, sí se editan a mano.
