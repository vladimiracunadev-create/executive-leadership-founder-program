# Auditoría de licenciamiento y metodología

**Repositorio:** `vladimiracunadev-create/executive-leadership-founder-program`

**Fecha de corte:** 22 de septiembre de 2026

**Autor del contenido original hasta el corte:** Vladimir Acuña

**Resultado:** separación prospectiva entre software MIT y contenido educativo
CC BY-NC-SA 4.0, con preservación expresa de las concesiones MIT anteriores.

Este inventario es una revisión de procedencia y licenciamiento, no una opinión
legal. La bibliografía exhaustiva está en [docs/FUENTES.md](docs/FUENTES.md).

## 1. Inventario del repositorio

| Familia de activos | Rutas principales | Titularidad o procedencia | Política actual |
|---|---|---|---|
| Software auxiliar | `apps/`, `scripts/`, `tools/`, `tests/`, `curriculum/*.py` | Código original de Vladimir Acuña; dependencias externas no incorporadas | MIT |
| Configuración de software y CI | `.github/workflows/`, `pyproject.toml`, requisitos y configuración técnica | Original, salvo acciones y herramientas externas referenciadas | MIT |
| Currículo y clases | `modules/`, `curriculum/*.json`, `curriculum/*.yaml`, `SYLLABUS.md` | Selección, secuencia y redacción original; conceptos externos citados | CC BY-NC-SA 4.0 actual; MIT histórico preservado |
| Ejercicios y evaluación | `assessment.md`, `labs/`, `project.md`, `cases/` | Expresión original del programa | CC BY-NC-SA 4.0 actual; MIT histórico preservado |
| Plantillas y frameworks propios | `templates/` y estructuras pedagógicas propias | Originales, sin apropiación de métodos externos citados | CC BY-NC-SA 4.0 actual; MIT histórico preservado |
| Datos didácticos | `data/scenarios.json`, mapas y catálogos propios | Datos sintéticos y compilaciones del programa; fuentes citadas separadamente | CC BY-NC-SA 4.0 salvo aviso específico |
| Documentación educativa | `docs/`, `academy/`, `portfolio/` y documentos curriculares de raíz | Original y generado desde fuentes del programa | CC BY-NC-SA 4.0 salvo archivos legales o aviso específico |
| Bibliografía y fuentes | `sources/bibliography.json`, `docs/FUENTES.md`, `docs/OFFICIAL_SOURCES.md` | Metadatos, enlaces y citas; las obras enlazadas no se incorporan | La licencia del repo cubre la compilación original, no las obras citadas |
| Identidad | Nombre del programa y presentación visual | Vladimir Acuña, en cuanto sea protegible | Derechos de marca reservados; sin licencia implícita |

## 2. Hallazgos

1. El archivo `LICENSE` original aplicaba MIT al software y a la documentación
   publicada. No existía una separación explícita por tipo de activo.
2. Todos los commits anteriores al corte registran un único autor, Vladimir
   Acuña. No se detectaron contribuciones de terceros en el historial de Git.
3. La redacción de clases, casos, evaluaciones y plantillas declara originalidad
   y usa obras externas como andamiaje conceptual, mediante cita y paráfrasis.
4. El repositorio contiene nombres de marcos, estándares y marcas externas,
   pero no se detectaron copias de libros o estándares completos ni binarios
   de terceros versionados.
5. La protección nueva solo puede operar prospectivamente: las copias ya
   publicadas bajo MIT mantienen los derechos recibidos bajo esa licencia.
6. El código de conducta reconoce su inspiración en Contributor Covenant; se
   normalizó el aviso y su licencia en los avisos de terceros.

## 3. Marcos, métodos y estándares de terceros

“Referencia” significa que el programa puede nombrar, explicar en palabras
propias y contrastar el concepto, pero no sublicencia la obra fuente ni sus
gráficos, tablas, textos o marcas.

| Marco o familia | Titular o fuente reconocida | Uso observado | Situación | Acción de cumplimiento |
|---|---|---|---|---|
| Método de casos | William Ellet y Harvard Business Review Press, entre otras tradiciones académicas | Estructura problema → evidencia → alternativas → recomendación | Referencia bibliográfica; no se reclama el método externo | Mantener cita; licenciar solo casos y expresión original del programa |
| Scrum | Ken Schwaber y Jeff Sutherland | Clases de entrega adaptativa | La [*Scrum Guide* 2020](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-US.pdf) se ofrece bajo CC BY-SA 4.0 | Citar guía y autores; no copiarla ni relicenciarla como contenido propio |
| Kanban | David J. Anderson y literatura citada | Flujo, WIP y políticas explícitas | Referencia a obra protegida y práctica de gestión | Mantener paráfrasis y cita; no reproducir tableros editoriales |
| Agile | Agile Manifesto y literatura posterior | Principios de entrega adaptativa | Término y conjunto de ideas de múltiples autores | No atribuir el campo al programa; enlazar fuentes cuando se cite texto |
| PMBOK® Guide | Project Management Institute, Inc. | Gobernanza y dominios de proyectos | Publicación protegida; PMBOK® es marca registrada según las [guías de PMI](https://www.pmi.org/-/media/pmi/documents/public/pdf/about/press-media/trademark-usage-guidelines-new.pdf) | Uso nominativo con marca y atribución; no reproducir tablas o estándares |
| Lean y Toyota Production System | Autores y organizaciones citados | Valor, flujo, desperdicio y mejora | Tradición externa con múltiples fuentes y marcas | Atribuir obras concretas; no presentar una variante como oficial |
| Theory of Constraints | Eliyahu M. Goldratt y fuentes citadas | Restricciones y throughput | Referencia bibliográfica externa | Mantener cita; no reproducir diagramas o texto editorial |
| OKR | Literatura de Drucker, Grove, Doerr y otros | Objetivos y resultados clave | Práctica externa; expresión de libros protegida | No reclamar invención; citar la fuente usada y escribir ejemplos propios |
| Balanced Scorecard | Robert S. Kaplan y David P. Norton | Traducción de estrategia a objetivos e indicadores | Marco externo desarrollado en obras protegidas | Citar autores; no copiar mapas o figuras oficiales |
| Cinco fuerzas, cadena de valor y estrategia competitiva | Michael E. Porter | Análisis de industria y ventaja | Marcos externos descritos en obras protegidas | Atribuir a Porter; mantener ejemplos y diagramas originales |
| Jobs to Be Done | Clayton Christensen y otros autores citados | Investigación causal de elección del cliente | Campo con varias formulaciones externas | Nombrar la fuente específica; no reclamar una definición única propia |
| Business Model Canvas | Alexander Osterwalder, Yves Pigneur y Strategyzer | Diseño de modelos de negocio | Strategyzer declara [uso con atribución](https://www.strategyzer.com/legal/usage-of-our-tools); el lienzo tiene condiciones propias | No incluir póster oficial; acreditar `Strategyzer.com` cuando se use el lienzo |
| Value Proposition Canvas | Strategyzer AG y autores acreditados | Diseño de propuesta de valor | Strategyzer [reserva adaptación, software y reventa](https://www.strategyzer.com/legal/usage-of-our-tools) del lienzo | No incorporar el lienzo; solicitar permiso para esos usos |
| Lean Startup | Eric Ries | Experimentos y aprendizaje validado | Referencia bibliográfica y denominación externa | Citar; no copiar tablas o capítulos |
| Design Thinking | Múltiples escuelas y organizaciones | Descubrimiento, prototipado y aprendizaje | Familia metodológica sin autoría única del programa | Atribuir la escuela o fuente concreta cuando sea relevante |
| RACI | Procedencia distribuida en literatura de gestión | Roles y responsabilidades | Acrónimo de uso extendido; fuentes concretas pueden estar protegidas | Usar explicación propia y evitar copiar matrices editoriales |
| RAPID® | Bain & Company, Inc. | Derechos de decisión | Marca registrada y modelo de Bain | Escribir RAPID® en su primera mención, atribuir a Bain y no copiar gráficos |
| COSO ERM | COSO | Riesgo integrado con estrategia y desempeño | Marco y materiales protegidos según las [reglas de COSO](https://www.coso.org/_files/ugd/3059fc_f7d01f2bbf7f46528d8fd2fe1207b5fd.pdf) | Citar y enlazar; no reproducir componentes gráficos o texto sustancial |
| ISO 9001, 22301 y 31000 | International Organization for Standardization | Calidad, continuidad y riesgo | Estándares protegidos conforme al [aviso de ISO](https://www.iso.org/copyright.html) | No reproducir requisitos; citar número y versión desde fuentes autorizadas |
| NIST CSF 2.0 y AI RMF 1.0 | NIST, Departamento de Comercio de EE. UU. | Ciberseguridad y gobierno de IA | En general, publicaciones federales de NIST son dominio público en EE. UU., salvo material marcado; véase su [aviso](https://www.nist.gov/copyrights-disclaimers) | Atribuir NIST y revisar avisos del documento concreto |
| Principios de IA y gobierno corporativo | OECD | Gobierno de IA y directorios | Publicaciones sujetas a las [condiciones de la OECD](https://www.oecd.org/en/about/terms-conditions.html) y al aviso de cada obra | Enlazar y resumir; no asumir que la licencia CC del programa las cubre |
| IFRS / NIIF | IFRS Foundation | Información financiera | Normas y marcas de la IFRS Foundation | Referencia nominativa; no reproducir estándares |
| SPIN Selling, Challenger, Getting to Yes y otras escuelas comerciales | Autores y editoriales registrados | Ventas y negociación | Obras externas protegidas | Citar cada obra; conservar ejemplos, casos y ejercicios originales |
| Leadership Pipeline, Five Dysfunctions y demás modelos de liderazgo | Autores y editoriales registrados | Liderazgo, talento y equipos | Obras externas protegidas | Citar, contrastar y no presentar el modelo como creación del programa |

## 4. Fuentes oficiales y normativa

Las leyes, decisiones administrativas, portales y guías oficiales no se
convierten en contenido propio por estar catalogados. La situación jurídica
varía por jurisdicción y por documento. El programa:

- enlaza la fuente primaria y registra la fecha de verificación;
- no concede bajo CC derechos que no posee;
- distingue una cita de una reproducción; y
- exige revalidar vigencia antes de una decisión real.

Los registros canónicos son
[sources/bibliography.json](sources/bibliography.json) y
[docs/OFFICIAL_SOURCES.md](docs/OFFICIAL_SOURCES.md).

## 5. Dependencias, fuentes y contributors

- `pytest`, `Python-Markdown` y `Pygments` se instalan como dependencias y no se
  incluyen en el repositorio. Sus licencias se registran en
  [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
- Las GitHub Actions se referencian por SHA y conservan sus repositorios y
  licencias de origen.
- El historial previo al corte muestra un solo contributor. Las contribuciones
  futuras deben declarar la licencia de entrada por tipo de aporte en
  [CONTRIBUTING.md](CONTRIBUTING.md).

## 6. Decisión sobre activos estratégicos

No se clasificó ningún ejercicio, plantilla o framework educativo original como
“todos los derechos reservados”. Se eligió CC BY-NC-SA 4.0 para todos ellos
porque protege atribución, uso no comercial y reciprocidad de adaptaciones. La
reserva se limita a marcas, identidad y derechos que una licencia de copyright
no debe conceder implícitamente.

Esta decisión puede revisarse para activos futuros antes de publicarlos. Un
aviso posterior no puede retirar derechos ya concedidos sobre versiones
anteriores.

## 7. Controles implementados

- separación de licencias por alcance;
- historia y punto de corte verificables;
- política de contribuciones por tipo de activo;
- aviso de terceros y marcas;
- guía de uso comercial;
- frase visible en el README;
- validación automatizada de archivos legales, frase y alcance; y
- verificación de enlaces internos, documentos generados, pruebas y CI.

## 8. Riesgos residuales y mantenimiento

1. Revisar permisos antes de incorporar cualquier imagen, diagrama, tabla,
   traducción o plantilla de terceros.
2. Mantener `THIRD_PARTY_NOTICES.md` al añadir dependencias o materiales.
3. Registrar por escrito cualquier licencia comercial.
4. Marcar de forma específica todo activo futuro que se reserve antes de
   publicarlo.
5. Repetir la auditoría cuando cambie el conjunto de fuentes o marcos.
6. Consultar asesoría jurídica en jurisdicciones o explotaciones de alto riesgo.
