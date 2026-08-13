# 🤝 Contribuir

Gracias por querer mejorar el programa. Este documento explica **qué se acepta,
qué no y por qué**, para que no dediques tiempo a un cambio que va a rechazarse
por una regla que no conocías.

Las contribuciones más valiosas, por orden: **una corrección de exactitud**, **una
norma citada que cambió**, **una fuente mejor que la actual** y **un enlace roto**.

## 🧭 Antes de escribir código o contenido

Ejecuta las comprobaciones. Son rápidas y usan solo la biblioteca estándar:

```bash
python tools/validate_repository.py --strict
python tools/validate_depth.py
python tools/check_links.py
pytest
```

Si tu cambio toca clases, plantillas o datos, además hay que regenerar los
documentos que dependen de ellos:

```bash
python tools/build_syllabus.py
python tools/build_status.py
python tools/build_manifest.py
python tools/build_file_index.py
```

La CI ejecuta esos mismos generadores con `--check` y **falla si el documento
del repositorio no coincide** con lo que produce el generador. No es una
formalidad: es lo que impide que el temario diga 288 clases cuando hay 289.

## ✍️ Reglas del contenido

1. **Originalidad.** No se copian capítulos, tablas extensas, ejercicios ni
   figuras de obras protegidas. Los libros son *andamios conceptuales*: se citan,
   se contrastan y se aplican, no se reproducen. El método está en
   [docs/READING_METHOD.md](docs/READING_METHOD.md).
2. **El contrato de clase es obligatorio.** Las 16 secciones de `deep-class-v2`,
   en su orden, con sus tres archivos (`README.md`, `assessment.md`,
   `lesson.yaml`). El validador rechaza lo que falte.
3. **Densidad real, no plantilla rellenada.** `validate_depth.py` exige un mínimo
   de palabras, al menos cinco referencias, cinco subsecciones de desarrollo y
   cinco preguntas de comprobación, y rechaza párrafos largos copiados entre
   clases o similitud léxica anormal dentro de una parte.
4. **Un título, tres sitios.** El título de `lesson.yaml` debe encabezar el
   README y la evaluación. Si cambias uno, cambia los tres.
5. **Normativa con fecha.** Todo contenido legal, tributario, regulatorio,
   laboral o de mercado se cita con **fuente primaria y fecha de verificación**.
   Una norma sin fecha es una afirmación que no caduca, y eso es exactamente lo
   que se quiere evitar en material chileno que cambia cada año.
6. **Sin datos personales reales.** Empresas, personas, RUT, montos y contratos
   son sintéticos. `tools/detect_pii.py` lo comprueba en `data/`, `templates/`,
   `portfolio/`, `academy/` y `cases/`.
7. **Español, con sus tildes.** El material está en español y se revisa como tal.

## 🧱 Reglas del código

- Las herramientas de `tools/` usan **solo la biblioteca estándar**. Validar el
  programa no puede exigir instalar nada. La única excepción es el portal
  (`build_site.py`), cuyas dependencias viven en `requirements-site.txt`.
- Cada herramienta lleva un docstring que explica **qué problema resuelve**, no
  solo qué hace.
- Los comentarios explican el porqué de una decisión no obvia. Un comentario que
  repite el código sobra.
- Nada de cifras escritas a mano en documentos generados: se cuentan desde
  `tools/inventario.py`.

## 🔀 Pull requests

- Una rama por cambio, con un asunto que diga qué cambia y para quién.
- Descripción con el **motivo**: qué estaba mal o qué faltaba.
- Si corriges una norma, incluye el enlace a la fuente oficial y su fecha.
- Todos los jobs de CI en verde. Un PR rojo no se revisa.

## 🐛 Issues

Usa las plantillas. Para un error de contenido, indica la clase concreta
(`modules/XX-.../classes/NNN-.../README.md`) y qué es incorrecto; para una norma
desactualizada, la fuente oficial vigente y su fecha.

## 🔐 Seguridad

Las vulnerabilidades **no** se reportan en un issue público. El procedimiento
está en [SECURITY.md](SECURITY.md).

## 📄 Licencia de tu aportación

Al contribuir aceptas que tu aportación se publique bajo la licencia
[MIT](LICENSE) del repositorio.
