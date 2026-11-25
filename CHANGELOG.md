<!-- portada:inicio -->
<div align="center">

# 📋 Changelog

**Qué cambió en cada versión y por qué.**

[![Versión](https://img.shields.io/badge/versión-2.3.0-e67e22?style=flat-square)](CHANGELOG.md)
[![Formato](https://img.shields.io/badge/formato-Keep%20a%20Changelog-007c83?style=flat-square)](https://keepachangelog.com/es-ES/1.1.0/)
[![Versionado](https://img.shields.io/badge/versionado-SemVer-2e8b57?style=flat-square)](https://semver.org/lang/es/)

[🏠 Inicio](README.md) ·
[📊 Estado](STATUS.md) ·
[🗺️ Roadmap](ROADMAP.md)

</div>
<!-- portada:fin -->

---

## Sin publicar

### Clases escritas como conocimiento, con fuente y diagrama a medida

- **Cuatro clases se reescriben a mano** (034, 137, 190, 200): definiciones con su
  autor, un marco real por clase (prominencia de interesados de Mitchell, Agle y
  Wood; confianza de Mayer, Davis y Schoorman y reparación de Kim et al.; mando de
  incidentes de Beyer et al. y comunicación de crisis de Coombs), ejemplo con
  datos, claves de respuesta y límites declarados.
- **Cada una lleva un diagrama SVG propio** que dibuja ese marco (diagrama de Venn
  de tres atributos, escalera de escalamiento con roles, modelo causal de
  confianza, matriz de atribución de responsabilidad).
- **Las otras 284 clases llevan una ficha visual** en lugar del esquema idéntico
  anterior: muestra los conceptos reales de la clase con su definición, la
  secuencia del método en cuatro diseños distintos, las señales a observar y el
  límite. Se regenera con la clase.
- **La parte 02 completa se reescribe a mano** (025–036, con la 034 ya hecha): cada clase
  con su marco atribuido, ejemplo con datos, claves de respuesta, límites y un
  diagrama a medida (riqueza del canal, tipos de pregunta, pirámide, lámina de
  decisión, SUCCES, niveles de feedback, camino a la acción, conflicto de tarea y
  relación, persuasión y coerción, ajuste de contexto, cuatro justicias).
- **La parte 06 completa** (073–084): tipos de trabajo, alcance y éxito, descomposición, estimación con visión
  desde afuera (Buehler, Flyvbjerg), riesgos, Agile, Scrum, Kanban y ley de Little, gobernanza, calidad y
  recuperación de proyectos; cada clase con fuentes verificadas y un diagrama a medida.
- **La parte 05 completa** (061–072): diseño de cargos (Hackman y Oldham), dotación (Cappelli),
  selección (Schmidt y Hunter; Sackett et al.), entrevistas estructuradas (Levashina et
  al.), onboarding (Bauer et al.), desempeño, plan de mejora, compensación (Adams; Deci et
  al.; Gneezy y Rustichini), aprendizaje (Ericsson), sucesión (Charan et al.),
  desvinculación responsable y el capstone del sistema de talento.
- **La parte 04 completa** (049–060): equipo real (Katzenbach y Smith; Hackman), propósito
  y metas (Locke y Latham), roles (Rizzo et al.), confianza (Lencioni), delegación
  (Grove), coaching (Whitmore), uno a uno, reuniones (Rogelberg), reconocimiento,
  rendición de cuentas, equipos distribuidos (Cramton; Hinds y Bailey) y el
  capstone de recuperación de un equipo, con diagramas a medida.
- **La parte 03 completa también** (037–048): autoconciencia (Goleman), regulación (Gross),
  empatía y exigencia (Scott), motivación (Ryan y Deci), resiliencia (Masten y
  Bonanno), seguridad psicológica (Edmondson), técnico y adaptativo (Heifetz),
  construcción de sentido (Weick), dilemas (Kidder), inmunidad al cambio (Kegan y
  Lahey), agotamiento y recuperación (Maslach; Sonnentag y Fritz) y el capstone de
  crisis humana, cada una con su diagrama a medida.
- **Veintisiete fuentes verificadas** (DOI e ISBN comprobados) entran al registro.
- Una clase con `authoring: manual` en su `lesson.yaml` no la regenera
  `deep_curriculum_builder.py`.
- Nuevos `tools/diagramas_clase.py` y `tools/build_diagrams.py` (con `--check` en
  la CI).

### Navegación y portadas de parte

- **Cada parte tiene portada pedagógica**: de qué trata, con qué hay que llegar,
  resultados, mapa, cómo se encadenan las clases, **tabla con enlace a cada clase**,
  riesgos, glosario derivado de las clases, evidencia y conexiones.
- **Cada clase, laboratorio y proyecto** lleva miga bajo el título y pie
  `Anterior · Índice · Siguiente`, también entre partes.
- **Nuevo** `tools/build_navigation.py` (con `--check` en la CI), el contenido
  propio de cada parte en `curriculum/part_pedagogy.py` y la guía
  `docs/NAVIGATION.md` con las reglas de recorrido.
- `tools/build_site.py` normaliza las rutas al comprobar enlaces, para no fallar
  en Windows con nombres largos.

### Reputación, comunicación ejecutiva y liderazgo en crisis

- **Nueve clases existentes se amplían** (010, 025, 034, 048, 137, 190, 200, 202,
  286): reputación y su evolución por rol, comunicación interna y externa,
  legitimidad y asuntos corporativos, conflicto con trabajadores, reparación de
  confianza, comité de crisis, vocería, intereses en conflicto, IA con
  responsabilidad humana y recuperación reputacional.
- **Cuatro plantillas nuevas**: acta del comité de crisis, manual de vocería,
  mapa de interesados y legitimidad, plan de reparación de confianza.
- **Nuevo documento** `docs/REPUTATION_AND_CRISIS_LEADERSHIP.md`: diagnóstico,
  matriz de brechas, ocho simulaciones con tres decisiones defendibles y
  rúbrica de decisiones bajo presión.
- Sin clases nuevas: sigue en 288 clases, 24 partes y 96 laboratorios.

### Inteligencia humana, influencia y protección del liderazgo

- **Siete clases existentes se amplían** (016, 045, 189, 190, 202, 209, 213):
  sesgos como vías de influencia indebida, lealtades y relaciones del cargo,
  declaración de conflictos, protocolo de 72 horas ante una alegación, escenarios
  sobre personas clave, casos históricos y contrainteligencia ejecutiva defensiva.
- **Nueva plantilla** `influence-and-conflict-disclosure-brief.md`.
- **Nuevo documento** `docs/HUMAN_INTELLIGENCE_AND_LEADERSHIP_PROTECTION.md`:
  diagnóstico, matriz de brechas, progresión por rol, glosario y el caso NVIDIA
  con hechos separados de alegaciones.
- Sin clases nuevas ni herramientas de vigilancia: la arquitectura sigue en
  288 clases, 24 partes y 96 laboratorios.

## 2.3.0 — 2026-08-19

### Las fuentes se ven, y se pueden comprobar

La versión anterior dejó el registro correcto pero ilegible: para saber de dónde
salía una clase había que abrir un JSON. Ahora la fuente se ve donde se usa.

- **Cada cita de clase muestra la edición y el localizador.** Las 3 200 citas de
  las 288 clases pasan a la forma
  `Autor — *Obra* (Editorial, año). **Uso en esta clase:** … **Localizador:**
  [ISBN-13 …](https://openlibrary.org/isbn/…)`. Editorial y año no se escriben a
  mano: salen de la ficha de la edición que resolvió el ISBN.
- **[docs/FUENTES.md](docs/FUENTES.md)** — la página de lectura del registro:
  cómo leer una cita, las 164 obras de gestión con autor, editorial, año, enlace
  y número de clases que las usan, las 41 fuentes oficiales con su URL y fecha de
  consulta, y la lista de pendientes con su motivo. Se genera desde el registro.
- El README deja de ser un tablero de cifras: una tabla compacta, las obras
  rectoras **con su enlace** y el puntero al catálogo completo.
- `scripts/verify-sources --write` escribe las citas de clase desde el registro, y
  el CI falla si alguna se desvía: una clase ya no puede decir que cita una obra
  distinta de la que el registro declara.
- Cuatro ediciones corregidas a mano tras comprobarlas contra su ficha: *The Lean
  Startup* apuntaba a la traducción alemana y *Atomic Habits* a una edición
  self-published; *The Effective Executive* y *The Innovator's Dilemma* no tenían
  ISBN-13 resoluble en la edición que devolvía la búsqueda.

## 2.2.0 — 2026-08-19

### Trazabilidad de fuentes

- Crea [`sources/bibliography.json`](sources/bibliography.json), **el registro
  único de fuentes**. Cada entrada exige un localizador resoluble: libro por
  **ISBN-13** con dígito de control válido, artículo por **DOI**, norma o
  documentación oficial por **URL https** de la fuente primaria. Lo que no
  resuelve se marca `pendiente` con el motivo; no se borra ni se rellena a ojo.
- Declara la **obra transversal** que faltaba: William Ellet — *The Case Study
  Handbook*, citada en las 288 clases porque el método de caso vertebra el
  programa, y hasta ahora no aparecía en ningún registro.
- Fusiona `data/official_sources.json` y la tabla escrita a mano de
  [`docs/OFFICIAL_SOURCES.md`](docs/OFFICIAL_SOURCES.md) en ese registro único.
  El documento pasa a **generarse** desde él; `data/official_sources.json`
  desaparece.
- Normaliza el bloque de fuentes de **las 288 clases** a una forma canónica:
  `- <emisor> — *<obra>*. **Uso en esta clase:** <uso>.`. Cada cita declara
  ahora **el uso que esa clase hace de la obra**, no solo la obra. El desarrollo
  de las clases no se toca.
- Separa en el README la **bibliografía de gestión** de las **fuentes oficiales
  y normas**: son dos cosas distintas y caducan distinto.

### Verificación

- `scripts/verify-sources` — **offline, determinista, bloquea en CI**: esquema
  del registro, dígito de control del ISBN-13, forma canónica del localizador,
  toda obra citada declarada, ninguna entrada sin usar, ningún bloque de fuentes
  repetido entre clases y las cifras publicadas cuadrando con el registro.
- `scripts/refresh-sources` — **en red, manual o programada, no bloquea**:
  resuelve ISBN en `openlibrary.org` y DOI en `api.crossref.org` comparando
  título y autores, hace GET a cada URL de norma, actualiza `verified_on` y
  `accessed`, e informa de lo que dejó de resolver sin borrarlo.
- Las cifras del README **las produce el verificador**, no una persona: viven
  entre marcadores y el CI falla si dejan de coincidir con el registro.
- `.github/workflows/sources.yml` revalida contra la red el día 1 de cada mes y
  publica el informe en el resumen del job, separado del CI a propósito: la red
  no es determinista y un CI intermitente se acaba ignorando.

## 2.1.0 — 2026-08-13

### Contenido

- Repara los **195 títulos de clase** que habían perdido sus tildes en
  `lesson.yaml`, en el H1 del README y en el de la evaluación; `SYLLABUS.md`
  conservaba el título correcto y se toma como fuente.
- Corrige la cabecera de las **288 clases**, que citaba el slug en inglés
  (`Professional To Leader`) en lugar del título en español de su parte.
- Añade [`docs/README.md`](docs/README.md) como índice de la documentación,
  agrupado por para qué sirve cada documento.

### Portal

- Publica el programa como **portal HTML en GitHub Pages**, generado con
  `tools/build_site.py`: espeja la estructura del repositorio, así que cada
  enlace del material sigue funcionando dentro del sitio.
- Portada con las cifras reales, las seis etapas y las 24 partes; **temario con
  buscador** que filtra por título, parte, etapa y concepto sin recargar.
- Diagramas Mermaid renderizados, tema claro y oscuro, y capa instalable (PWA)
  para consultar sin conexión lo ya visitado.
- Retira el `site/` escrito a mano —cuatro archivos con un JSON de módulos
  mantenido aparte— y lo saca del control de versiones: ahora se genera.

### Documentos generados

- `SYLLABUS.md`, `STATUS.md`, `MANIFEST.md` y `FILE_INDEX.md` pasan a generarse
  desde el repositorio con `tools/build_*.py`, cada uno con modo `--check` que
  la CI ejecuta. Dos fuentes de verdad para el mismo dato acaban siempre
  discrepando; ahora hay una.
- Añade [`MANIFEST.md`](MANIFEST.md): qué garantiza cada comprobación y, sobre
  todo, qué no garantiza.
- `tools/inventario.py` centraliza el recuento: ninguna cifra se escribe a mano.

### Herramientas

- Renombra `scripts/` a `tools/`, en línea con el resto de los programas.
- Reescribe `validate_repository.py`: verifica además los campos de
  `lesson.yaml`, la numeración continua 001–288, la coherencia del título entre
  los tres archivos de la clase y la cabecera de parte.
- Añade `check_links.py`, `detect_secrets.py` y `detect_pii.py`.
- Corrige el patrón de enlaces, que no alcanzaba la forma
  `[![insignia](url)](destino)`: los enlaces de las portadas no se comprobaban.
- Migra las pruebas a **pytest** y amplía su cobertura al simulador y a los datos.

### Integración continua

- Reescribe `ci.yml` en cinco trabajos con puerta de calidad final, acciones
  **pineadas por SHA**, `permissions: contents: read`, `persist-credentials:
  false`, `concurrency` y `timeout-minutes`.
- Añade `pages.yml`, que genera el portal, lo publica y **comprueba que
  responda** tras el despliegue.
- Añade `security.yml`: `pip-audit`, `bandit`, `gitleaks` sobre el historial y
  los detectores propios, con ejecución semanal.
- Audita los propios workflows con `actionlint` y `zizmor`.
- Añade lint de Markdown, comprobación de codificación UTF-8 sin BOM y matriz de
  3 sistemas × 3 versiones de Python.

### Repositorio

- Publica el repositorio y activa GitHub Pages.
- Amplía `SECURITY.md`, `CONTRIBUTING.md` y `CODE_OF_CONDUCT.md`, que eran
  párrafos sueltos.
- Añade `.gitattributes`, `.markdownlint-cli2.jsonc`, `requirements.txt`,
  `requirements-site.txt`, `pyproject.toml` y plantillas de issue y de PR.
- Reconcilia la versión: `VERSION` decía `1.1.0` mientras el README y el
  changelog decían `2.0.0`.

## 2.0.0 — 2026-08-12

- Reescribe las 288 clases bajo `deep-class-v2`; se elimina el patrón de contenido superficial replicado.
- Define 288 especificaciones temáticas distintas: concepto central, cinco conceptos, método, evidencia, caso y límites.
- Eleva la profundidad a 3.168–3.987 palabras por clase (mediana ~3.379) sin aceptar párrafos largos repetidos.
- Vincula fuentes al desarrollo mediante una sección de lectura comparada y lentes de lectura por concepto.
- Amplía el catálogo a 229 referencias e incorpora Kieso, Penman, Palepu y Schilit para contabilidad/análisis financiero.
- Incorpora explícitamente *How Learning Works*, *Make It Stick*, *Understanding by Design*, *Peak* y *The Case Study Handbook* como fuentes pedagógicas.
- Reescribe 288 `assessment.md` específicos; cada evaluación usa conceptos, método, métricas, caso y límite propios.
- Reescribe `lesson.yaml` con objetivos, evidencias y referencias específicas por clase.
- Agrega `docs/PEDAGOGICAL_STANDARD.md`, `docs/READING_METHOD.md` y `docs/REFERENCE_MAP.md`.
- Agrega `scripts/validate_depth.py`: mínimos de profundidad/fuentes, detector de párrafos replicados y similitud anormal.
- Prioriza fuentes por tema: contabilidad financiera usa Kieso/Penman/Palepu/Schilit; laboral Chile usa DT, BCN, SUSESO y Previsión Social.
- Añade 38 profundizaciones técnicas/regulatorias con fórmulas, marcos y reglas disciplinares cuando la materia lo exige.
- Mantiene 24 partes, 288 clases, 96 labs y 48 escenarios; todos los validadores y tests pasan.

## 1.2.0 — 2026-08-12

- Agrega mapa completo de tipos contractuales laborales en Chile: indefinido, plazo fijo y obra/faena.
- Distingue tipo por duración de modalidades como jornada parcial, teletrabajo/híbrido y turnos.
- Incorpora contratos/regímenes especiales: aprendizaje, servicios transitorios, temporada, casa particular y advertencia de estatutos sectoriales.
- Incorpora figuras afines no laborales: honorarios, proveedor, práctica profesional y subcontratación.
- Documenta transformación de plazo fijo a indefinido y controles de renovación.
- Añade checklist de selección contractual y expande la clase 260.

## 1.1.0 — 2026-08-12

- Incorpora guía completa de derecho laboral chileno para jefaturas, gerencia y founders.
- Profundiza la clase 260 con contratación, honorarios, jornada, previsión, seguridad, Ley Karin, teletrabajo, inclusión y término.
- Agrega mapa JSON de 17 normas/marcos laborales y previsionales.
- Actualiza la referencia temporal de jornada a 42 horas desde 26-04-2026 y la transición a 40 horas en 2028.
- Añade DS 44, Ley 21.735 y preparación para Ley 21.719 (vigencia 01-12-2026).
- Añade 5 plantillas laborales de auditoría y compliance.
- Amplía fuentes oficiales con Mintrab, SUSESO, Superintendencia de Pensiones, AFC, SERMIG y ChileAtiende.

## 1.0.0 — 2026-08-12

- Primera versión completa.
- 24 partes, 288 clases y 720 horas.
- 96 laboratorios ejecutivos.
- Bibliografía, fuentes oficiales y Founder Track Chile.
- Simulador ejecutivo y validación estructural.

---

<div align="center">

[🏠 Inicio](README.md) · [📊 Estado](STATUS.md) · [🗺️ Roadmap](ROADMAP.md) · [📚 Temario](SYLLABUS.md)

</div>
