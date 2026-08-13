<!-- portada:inicio -->
<div align="center">

# 📋 Changelog

**Qué cambió en cada versión y por qué.**

[![Versión](https://img.shields.io/badge/versión-2.1.0-e67e22?style=flat-square)](CHANGELOG.md)
[![Formato](https://img.shields.io/badge/formato-Keep%20a%20Changelog-007c83?style=flat-square)](https://keepachangelog.com/es-ES/1.1.0/)
[![Versionado](https://img.shields.io/badge/versionado-SemVer-2e8b57?style=flat-square)](https://semver.org/lang/es/)

[🏠 Inicio](README.md) ·
[📊 Estado](STATUS.md) ·
[🗺️ Roadmap](ROADMAP.md)

</div>
<!-- portada:fin -->

---

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
