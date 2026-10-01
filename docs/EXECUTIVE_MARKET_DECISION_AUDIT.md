# Auditoría de decisión ejecutiva integrada

**Fecha de corte:** 2026-10-01
**Alcance:** mercado, cliente, modelo de negocio, economía, alianzas, capital y
proyección financiera.
**Restricción de diseño:** ampliar la capacidad de interrogación y decisión sin
duplicar las clases disciplinares ni alterar la arquitectura de 288 clases, 24
partes y 96 laboratorios.

## Fuentes de verdad y archivos derivados

La auditoría comprobó la arquitectura real antes de modificar contenido:

- Las clases publicadas viven en `modules/*/classes/*/`. En cada carpeta,
  `README.md` contiene el desarrollo, `assessment.md` la evaluación y
  `lesson.yaml` los metadatos, objetivos, entregable, referencias, límites y
  señales. Esas tríadas son artefactos versionados y validados, pero pueden
  regenerarse por clase desde `curriculum/deep_specs.py`,
  `curriculum/topic_notes.py` y `tools/deep_curriculum_builder.py`; una mejora
  durable debe actualizar también esas entradas.
- Los README de parte y los laboratorios en `modules/*/` son también contenido
  canónico. No se reemplazan con una nueva clase o una segunda ruta paralela.
- `curriculum/curriculum.yaml` y `curriculum/curriculum.json` fijan la
  arquitectura de 6 etapas, 24 partes, 288 clases y 720 horas.
- `SYLLABUS.md`, `STATUS.md`, `MANIFEST.md` y `FILE_INDEX.md` son derivados
  versionados. Los generan respectivamente `tools/build_syllabus.py`,
  `tools/build_status.py`, `tools/build_manifest.py` y
  `tools/build_file_index.py`.
- `site/` es un derivado no versionado que `tools/build_site.py` reconstruye
  desde el Markdown canónico.
- `tools/deep_curriculum_builder.py` es el generador de las tríadas. Admite
  `--class N`, por lo que la verificación correcta de una mejora localizada es
  regenerar solo las clases afectadas; nunca reescribir las 288 a ciegas.

## Mapa previo: cobertura y brecha ejecutiva

| Tema | Existente | Nivel de responsabilidad actual | Brecha ejecutiva real | Cambio mínimo |
|---|---|---|---|---|
| Mercado | Clases 133–135; diagnóstico e industria en 158–159 | Marketing y estrategia analizan demanda, segmentación y competencia | No hay un control ejecutivo compacto que detecte TAM inflado, sustitutos omitidos, benchmark no comparable, datos vencidos o inferencias tratadas como hechos | Añadir una puerta de calidad a la clase 133 y evaluarla en su tríada |
| Cliente | Customer discovery en 147 y 243; problema, JTBD, primeros clientes y PMF en 146–155 y 242–250 | Producto y founder aprenden a descubrir y validar | Los estados “descrito / entrevistado / intención / pagó / repitió” no funcionan como escalera obligatoria de evidencia para quien autoriza recursos | Incorporar la escalera de evidencia en la clase 147 sin volver a enseñar cómo entrevistar |
| Modelo de negocio | Clase 163; Business Model Canvas preservado en la clase 246 y sus laboratorios | Estrategia y founder diseñan y comparan modelos | Falta obligar al decisor a priorizar el bloque más incierto, la hipótesis que puede destruir el sistema y la evidencia que habilita la siguiente inversión | Extender la lectura ejecutiva de la clase 163; no alterar el laboratorio de Canvas |
| Economía del negocio | Parte 09 completa: ingresos, margen, costos, caja, capital de trabajo, forecast, unit economics, ROI y comité de inversión | Gerencia interpreta estados y decide con economía | La cobertura disciplinar es fuerte, pero sus resultados no son una condición obligatoria de un caso que cruce mercado, cliente, modelo y alianzas | Reutilizar esas salidas como evidencia de entrada en el capstone 204; no duplicar las clases financieras |
| Alianzas | Clase 166 sobre partnerships; clase 236 sobre build/buy/partner/retire; stakeholders y negociación en partes 02, 06, 10 y 17 | Estrategia y tecnología comparan ecosistemas y sourcing | Aporte, dependencia, poder negociador, alineación, exclusividad, riesgo, gobierno y salida no se exigen juntos en una recomendación estratégica | Completar la ficha de decisión de la clase 166 y conectarla con build/buy/partner |
| Proyección | Forecast en 115 y 126; escenarios en 164; flujos y capital en 220 y 228 | Finanzas, ventas y estrategia proyectan desde drivers y escenarios | En una decisión empresarial integrada todavía puede sobrevivir una cifra única sin rango, sensibilidad ni trigger | Endurecer la salida ejecutiva de 115 y exigirla en el caso 204 |
| Capital e inversión | ROI e inversión en 118–120; asignación en 198; estructura, costo y comité de capital en 217–228 | Gerente, CEO y comité asignan recursos | Los capstones especializados deciden bien dentro de su disciplina, pero no existe una decisión única que conecte evidencia comercial, economía, alianza y capital requerido | Usar el capstone 204 como foro integrador y mantener intactos los comités especializados |
| Gobierno de la decisión | Clases 196, 199, 204, 211–213; briefs con owner y revisión en todo el estándar | CEO y directorio gobiernan decisiones, stakeholders y riesgo | El patrón existe, pero no está formulado como ocho preguntas comunes para interrogar artefactos de mercado, cliente, modelo, economía, alianza y proyección | Añadir el protocolo transversal a la clase 196 y reutilizarlo en el capstone 204 |
| Caso integrado | Capstones de inversión, GTM, producto, estrategia, capital, launch readiness y 100 días | Cada foro resuelve un dominio o transición concreta | Ningún caso entrega conjuntamente resumen de mercado, evidencia de clientes, costos, modelo, aliados y proyección; por tanto no prueba síntesis ejecutiva | Ampliar el caso existente de la clase 204, admitiendo más de una decisión defendible y exigiendo decisión, argumentos, supuestos, riesgos, faltantes, owner y revisión |

## Decisión de alcance

La brecha no justifica nuevas clases, renumeración ni un segundo programa de
marketing, finanzas o venture creation. La intervención se limita a seis
tríadas existentes:

1. clase 115 para la presentación ejecutiva de proyecciones;
2. clase 133 para la prueba de calidad del mercado;
3. clase 147 para la madurez de evidencia del cliente;
4. clase 163 para incertidumbre del modelo de negocio;
5. clase 166 para build/buy/partner y gobierno de alianzas;
6. clases 196 y 204 para el protocolo común y el caso integrado.

Los cambios deben conservar las 16 secciones pedagógicas de cada README,
actualizar el objetivo o señal correspondiente en `lesson.yaml` y hacer que la
competencia nueva sea observable en `assessment.md`.

## Línea base verificable

Antes de cambiar las clases se ejecutó:

- `python tools/validate_repository.py --strict`: 24 partes, 288 clases, 96
  laboratorios y 48 escenarios;
- `pytest -q`: 42 pruebas aprobadas;
- inventario de `.github/workflows/`: `ci.yml`, `pages.yml`, `security.yml` y
  `sources.yml`.

Esta línea base es el control contra el que se comparará la arquitectura final.
