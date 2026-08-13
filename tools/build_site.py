"""Genera el portal de estudio en HTML a partir del Markdown del repositorio.

El programa se puede recorrer entero leyendo los archivos en GitHub. El portal
existe para quien prefiere leerlo como un sitio: navegación entre clases,
buscador del temario, diagramas renderizados y lectura sin conexión.

El sitio **espeja** la estructura del repositorio: cada `X.md` produce un
`X.html` en la misma ruta relativa. Así los enlaces entre documentos siguen
funcionando cambiando solo la extensión, sin recalcular rutas.

Uso:
    python tools/build_site.py            # genera site/
    python tools/build_site.py --check    # genera y verifica sus enlaces
"""

from __future__ import annotations

import argparse
import html
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import portal_extra  # noqa: E402

try:
    import markdown
except ImportError:  # pragma: no cover - solo ocurre sin requirements-site
    print("Falta la dependencia 'markdown'. Instala: pip install -r requirements-site.txt")
    raise SystemExit(1)

ROOT = Path(__file__).resolve().parents[1]
SALIDA = ROOT / "site"

EXCLUIDOS = {".git", ".github", "node_modules", ".venv", "site",
             "__pycache__", ".pytest_cache", ".ruff_cache"}

TITULO = "Executive Leadership & Founder Program"
REPO = "https://github.com/vladimiracunadev-create/executive-leadership-founder-program"
DESCRIPCION = (
    "Programa abierto de 288 clases que recorre el camino de profesional "
    "individual a líder, gerente, CEO, founder y business owner, con "
    "bibliografía verificable y una ruta de creación de empresa en Chile."
)

# Enlaces relativos a un archivo .md, con ancla opcional.
ENLACE_MD = re.compile(r'(href=")(?!https?://|mailto:|#)([^"]+?)\.md((?:#[^"]*)?)(")')

# Bloques mermaid del origen. Se apartan antes de convertir, porque el
# resaltador de código los envolvería y el navegador ya no los reconocería.
MERMAID = re.compile(r"^```mermaid[ \t]*\n(.*?)^```[ \t]*$", re.S | re.M)

# Python-Markdown trata cualquier bloque HTML de nivel de bloque como HTML en
# crudo y no convierte lo que hay dentro. El README y los documentos usan
# `<div align="center">` para la portada, así que sin esto el portal serviría
# las insignias y las tablas como texto plano. La extensión `md_in_html` sí
# convierte el interior, pero solo cuando el elemento declara `markdown="1"`;
# ese atributo se pone aquí y no en el Markdown, porque en GitHub no hace falta.
ABRIR_HTML = re.compile(r"<(div|td|th|details|summary)((?:\s[^>]*)?)>")

# Avisos de GitHub (> [!IMPORTANT]) que el conversor no conoce.
AVISO = re.compile(r"^>\s*\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*$", re.M)
ETIQUETA_AVISO = {
    "NOTE": "📘 Nota", "TIP": "💡 Consejo", "IMPORTANT": "❗ Importante",
    "WARNING": "⚠️ Advertencia", "CAUTION": "🛑 Precaución",
}

# Igual que en `check_links.py`: se busca el destino sin exigir cómo es la
# etiqueta, para alcanzar también los `[![insignia](url)](destino-local)`.
ENLACE_RELATIVO = re.compile(r"\]\((?!https?://|mailto:|#)([^)\s]+)\)")

# Lo que va dentro de un bloque cercado o entre acentos ilustra la forma de un
# enlace; no es un destino que haya que resolver ni copiar.
BLOQUE_CERCADO = re.compile(r"^```.*?^```", re.S | re.M)
CODIGO_EN_LINEA = re.compile(r"`[^`\n]*`")


def archivos_markdown() -> list[Path]:
    return sorted(
        ruta for ruta in ROOT.rglob("*.md")
        if not any(parte in EXCLUIDOS for parte in ruta.relative_to(ROOT).parts)
    )


def adjuntos_enlazados() -> list[Path]:
    """Archivos que no son Markdown y que algún documento enlaza.

    El portal convierte cada `.md` en `.html`, pero un enlace a un `lesson.yaml`,
    a un conjunto de datos o a una herramienta apunta a un archivo que hay que
    copiar tal cual. Descubrirlos leyendo los enlaces evita mantener una lista a
    mano que se desactualiza en el primer enlace nuevo.
    """
    encontrados: set[Path] = set()
    for ruta in archivos_markdown():
        texto = CODIGO_EN_LINEA.sub("`` ", BLOQUE_CERCADO.sub("", ruta.read_text(encoding="utf-8")))
        for destino in ENLACE_RELATIVO.findall(texto):
            destino = destino.strip().split("#", 1)[0]
            if not destino or destino.endswith(".md"):
                continue
            resuelto = (ruta.parent / destino).resolve()
            if not resuelto.is_file():
                continue
            try:
                relativa = resuelto.relative_to(ROOT)
            except ValueError:
                continue
            if any(parte in EXCLUIDOS for parte in relativa.parts):
                continue
            encontrados.add(relativa)
    return sorted(encontrados)


def titulo_de(cuerpo: str, ruta: Path) -> str:
    for linea in cuerpo.splitlines():
        if linea.startswith("# "):
            return re.sub(r"^[^\w¿¡]+\s*", "", linea[2:].strip())
    return ruta.stem


def convertir(cuerpo: str) -> str:
    diagramas: list[str] = []

    def apartar(coincidencia: re.Match[str]) -> str:
        diagramas.append(coincidencia.group(1))
        return f"\nMERMAIDMARCA{len(diagramas) - 1}FIN\n"

    cuerpo = MERMAID.sub(apartar, cuerpo)
    cuerpo = AVISO.sub(lambda m: f"> **{ETIQUETA_AVISO[m.group(1)]}**  ", cuerpo)
    cuerpo = ABRIR_HTML.sub(r'<\1 markdown="1"\2>', cuerpo)

    md = markdown.Markdown(
        extensions=["tables", "fenced_code", "codehilite", "sane_lists",
                    "attr_list", "toc", "md_in_html"],
        extension_configs={"codehilite": {"guess_lang": False, "noclasses": False}},
    )
    contenido = md.convert(cuerpo)

    for indice, diagrama in enumerate(diagramas):
        contenido = contenido.replace(
            f"<p>MERMAIDMARCA{indice}FIN</p>",
            f'<pre class="mermaid">{html.escape(diagrama)}</pre>',
        )

    return ENLACE_MD.sub(
        lambda m: f"{m.group(1)}{m.group(2)}.html{m.group(3)}{m.group(4)}", contenido
    )


def directorios_con_indice() -> set[Path]:
    indices = {Path(".")}
    for ruta in archivos_markdown():
        if ruta.name == "README.md":
            indices.add(ruta.parent.relative_to(ROOT))
    return indices


def migas(relativa: Path, indices: set[Path]) -> str:
    partes = list(relativa.parts[:-1])
    if not partes:
        return ""
    subir = "../" * len(partes)
    trozos = [f'<a href="{subir}index.html">Inicio</a>']
    for indice, parte in enumerate(partes):
        directorio = Path(*partes[: indice + 1])
        etiqueta = html.escape(parte)
        # Solo se enlaza un directorio si tiene índice propio; el resto es una
        # etiqueta de ubicación, no un destino.
        if directorio in indices:
            restante = "../" * (len(partes) - indice - 1)
            trozos.append(f'<a href="{restante}index.html">{etiqueta}</a>')
        else:
            trozos.append(f"<span>{etiqueta}</span>")
    return " / ".join(trozos)


PLANTILLA = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo} · {sitio}</title>
<meta name="description" content="{descripcion}">
<link rel="stylesheet" href="{css}">
<link rel="manifest" href="{manifiesto}">
<meta name="theme-color" content="#0969da">
<link rel="icon" href="{icono}" type="image/png">
</head>
<body>
<a class="saltar" href="#contenido">Saltar al contenido</a>
<header class="cabecera">
  <a class="marca" href="{inicio}">Executive Leadership<br><span>&amp; Founder Program</span></a>
  <nav class="navegacion">
    <a href="{temario}">Temario</a>
    <a href="{syllabus}">Programa</a>
    <a href="{estado}">Estado</a>
    <a href="{docs}">Documentación</a>
    <a href="{repositorio}" rel="noopener">GitHub</a>
  </nav>
</header>
<div class="migas">{migas}</div>
<main id="contenido" class="contenido">
{cuerpo}
</main>
<footer class="pie">
  <p><strong>{sitio}</strong> · {clases} clases · {partes} partes · Licencia MIT</p>
  <p>Material formativo. No constituye asesoría legal, tributaria, financiera ni laboral.
     Verifica siempre la norma vigente antes de aplicar nada.</p>
  <p><a href="{repositorio}" rel="noopener">Ver en GitHub</a></p>
</footer>
<script>
if ("serviceWorker" in navigator) {{
  window.addEventListener("load", function () {{
    navigator.serviceWorker.register("{sw}").catch(function () {{}});
  }});
}}
</script>
<script type="module">
import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";
const oscuro = window.matchMedia("(prefers-color-scheme: dark)").matches;
mermaid.initialize({{ startOnLoad: true, theme: oscuro ? "dark" : "default" }});
</script>
</body>
</html>
"""

CSS = """:root {
  --fondo: #ffffff;
  --texto: #1f2328;
  --suave: #59636e;
  --borde: #d1d9e0;
  --acento: #0969da;
  --codigo: #f6f8fa;
  --destacado: #f6f8fa;
  --ancho: 62rem;
}
@media (prefers-color-scheme: dark) {
  :root {
    --fondo: #0d1117;
    --texto: #e6edf3;
    --suave: #9198a1;
    --borde: #3d444d;
    --acento: #4493f8;
    --codigo: #151b23;
    --destacado: #151b23;
  }
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  background: var(--fondo);
  color: var(--texto);
  font: 16px/1.65 -apple-system, BlinkMacSystemFont, "Segoe UI", Inter, Roboto,
        "Helvetica Neue", Arial, sans-serif;
}
.saltar {
  position: absolute; left: -999px;
  background: var(--acento); color: #fff; padding: .6rem 1rem; z-index: 10;
}
.saltar:focus { left: 1rem; top: 1rem; }
.cabecera {
  display: flex; flex-wrap: wrap; gap: 1rem;
  align-items: center; justify-content: space-between;
  max-width: var(--ancho); margin: 0 auto; padding: 1.25rem 1.5rem;
  border-bottom: 1px solid var(--borde);
}
.marca {
  font-weight: 700; font-size: .95rem; line-height: 1.25;
  color: var(--texto); text-decoration: none; letter-spacing: -.01em;
}
.marca span { font-weight: 400; color: var(--suave); }
.navegacion { display: flex; flex-wrap: wrap; gap: 1.25rem; }
.navegacion a {
  color: var(--suave); text-decoration: none; font-size: .9rem; font-weight: 500;
}
.navegacion a:hover { color: var(--acento); }
.migas {
  max-width: var(--ancho); margin: 0 auto; padding: .85rem 1.5rem 0;
  font-size: .82rem; color: var(--suave);
}
.migas a { color: var(--suave); }
.contenido {
  max-width: var(--ancho); margin: 0 auto; padding: 1.5rem 1.5rem 4rem;
}
.contenido h1 {
  font-size: 2rem; line-height: 1.25; letter-spacing: -.02em;
  margin: 1.5rem 0 1rem; padding-bottom: .5rem; border-bottom: 1px solid var(--borde);
}
.contenido h2 {
  font-size: 1.4rem; margin: 2.5rem 0 .85rem;
  padding-bottom: .35rem; border-bottom: 1px solid var(--borde);
}
.contenido h3 { font-size: 1.15rem; margin: 2rem 0 .75rem; }
.contenido h4 { font-size: 1rem; margin: 1.5rem 0 .5rem; }
.contenido a { color: var(--acento); text-decoration: none; }
.contenido a:hover { text-decoration: underline; }
.contenido p, .contenido li { overflow-wrap: break-word; }
.contenido ul, .contenido ol { padding-left: 1.4rem; }
.contenido li { margin: .3rem 0; }
.contenido blockquote {
  margin: 1.25rem 0; padding: .75rem 1.1rem;
  border-left: 4px solid var(--acento); background: var(--destacado);
  border-radius: 0 6px 6px 0;
}
.contenido blockquote > :first-child { margin-top: 0; }
.contenido blockquote > :last-child { margin-bottom: 0; }
.contenido code {
  background: var(--codigo); border: 1px solid var(--borde);
  border-radius: 5px; padding: .12em .4em; font-size: .875em;
  font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace;
}
.contenido pre {
  background: var(--codigo); border: 1px solid var(--borde);
  border-radius: 8px; padding: 1rem; overflow-x: auto; line-height: 1.45;
}
.contenido pre code { background: none; border: 0; padding: 0; font-size: .84rem; }
.contenido pre.mermaid {
  background: transparent; border: 0; text-align: center; padding: 1rem 0;
}
.contenido table {
  width: 100%; border-collapse: collapse; margin: 1.25rem 0;
  font-size: .92rem; display: block; overflow-x: auto;
}
.contenido th, .contenido td {
  border: 1px solid var(--borde); padding: .5rem .7rem; text-align: left;
  vertical-align: top;
}
.contenido th { background: var(--destacado); font-weight: 600; }
.contenido tr:nth-child(even) td {
  background: color-mix(in srgb, var(--destacado) 45%, transparent);
}
.contenido hr { border: 0; border-top: 1px solid var(--borde); margin: 2.5rem 0; }
.contenido img { max-width: 100%; }
.pie {
  max-width: var(--ancho); margin: 0 auto; padding: 2rem 1.5rem 3rem;
  border-top: 1px solid var(--borde); color: var(--suave); font-size: .85rem;
}
.pie p { margin: .4rem 0; }
.pie a { color: var(--acento); }
@media (max-width: 640px) {
  .cabecera { flex-direction: column; align-items: flex-start; }
  .contenido h1 { font-size: 1.6rem; }
}

/* ── Portada ─────────────────────────────────────────────────────── */
.hero { padding: 3.5rem 0 2.5rem; border-bottom: 1px solid var(--borde); text-align: center; }
.hero-cinta {
  display: inline-block; margin: 0 0 1.2rem; padding: .3rem .85rem; border-radius: 999px;
  background: var(--destacado); border: 1px solid var(--borde);
  font-size: .8rem; letter-spacing: .04em; text-transform: uppercase; color: var(--suave);
}
.hero h1 {
  margin: 0 0 1rem; font-size: clamp(1.9rem, 5.2vw, 3.1rem);
  line-height: 1.15; letter-spacing: -.02em;
}
.hero h1 span { color: var(--acento); }
.hero-bajada { max-width: 46rem; margin: 0 auto 2rem; font-size: 1.08rem; color: var(--suave); }
.hero-acciones { display: flex; flex-wrap: wrap; gap: .75rem; justify-content: center; }
.contenido .boton {
  display: inline-block; padding: .7rem 1.35rem; border-radius: 8px;
  background: var(--acento); color: #fff; font-weight: 600; text-decoration: none;
  border: 1px solid transparent;
}
.contenido .boton:hover { filter: brightness(1.08); text-decoration: none; }
.contenido .boton.secundario {
  background: transparent; color: var(--texto); border-color: var(--borde);
}
.contenido .boton.secundario:hover {
  border-color: var(--acento); color: var(--acento); text-decoration: none;
}
.cifras {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(7rem, 1fr));
  gap: 1rem; margin: 2.5rem 0 0; padding: 0;
}
.cifras div { margin: 0; }
.cifras dt { font-size: 1.65rem; font-weight: 700; letter-spacing: -.02em; }
.cifras dd {
  margin: .15rem 0 0; font-size: .82rem; color: var(--suave);
  text-transform: uppercase; letter-spacing: .05em;
}

.bloque { padding: 2.75rem 0; border-bottom: 1px solid var(--borde); }
.bloque > h2 { margin: 0 0 .6rem; font-size: 1.45rem; border: 0; padding: 0; }
.bloque-intro { margin: 0 0 1.5rem; color: var(--suave); max-width: 52rem; }
.bloque.aviso { border-bottom: 0; }
.bloque.aviso p {
  padding: 1rem 1.15rem; border-left: 4px solid var(--acento);
  background: var(--destacado); border-radius: 0 8px 8px 0; color: var(--suave);
}

.escalera {
  display: flex; flex-wrap: wrap; gap: .5rem; align-items: center;
  margin: 0 0 1.5rem; padding: 0; list-style: none;
}
.escalera li {
  padding: .35rem .8rem; border: 1px solid var(--borde); border-radius: 999px;
  font-size: .85rem; font-weight: 600; background: var(--destacado);
}
.escalera li::after { content: " →"; color: var(--suave); font-weight: 400; }
.escalera li:last-child::after { content: ""; }

.etapas { display: grid; gap: 1rem; grid-template-columns: repeat(auto-fit, minmax(15rem, 1fr)); }
.etapa {
  padding: 1.1rem 1.2rem; border: 1px solid var(--borde);
  border-top: 4px solid var(--color, var(--acento)); border-radius: 10px; background: var(--fondo);
}
.etapa h3 { margin: 0 0 .2rem; font-size: 1.05rem; }
.etapa-meta {
  margin: 0 0 .55rem; font-size: .8rem; color: var(--suave);
  text-transform: uppercase; letter-spacing: .04em;
}
.etapa p { margin: 0; font-size: .92rem; color: var(--suave); }

.rejilla { display: grid; gap: .85rem; grid-template-columns: repeat(auto-fill, minmax(16rem, 1fr)); }
.contenido .tarjeta {
  display: flex; flex-direction: column; gap: .3rem;
  padding: 1rem 1.1rem; border: 1px solid var(--borde);
  border-left: 4px solid var(--color, var(--acento)); border-radius: 10px;
  text-decoration: none; color: inherit; background: var(--fondo);
  transition: border-color .15s, transform .15s;
}
.contenido .tarjeta:hover {
  border-color: var(--acento); transform: translateY(-2px); text-decoration: none;
}
.tarjeta-numero, .tarjeta-nota { font-size: .78rem; color: var(--suave); }
.tarjeta-numero { text-transform: uppercase; letter-spacing: .06em; }
.tarjeta strong { font-size: 1rem; line-height: 1.3; }
.tarjeta-emoji { font-size: 1.5rem; }

/* ── Temario ─────────────────────────────────────────────────────── */
.temario-cabecera { padding: 2rem 0 1.5rem; border-bottom: 1px solid var(--borde); }
.temario-cabecera h1 { margin: 0 0 .4rem; }
.temario-cabecera p { margin: 0 0 1rem; color: var(--suave); }
#buscador {
  width: 100%; padding: .75rem 1rem; font-size: 1rem; color: var(--texto);
  background: var(--fondo); border: 1px solid var(--borde); border-radius: 8px;
}
#buscador:focus { outline: 2px solid var(--acento); outline-offset: 1px; }
.resultado { margin: .6rem 0 0 !important; font-size: .85rem; }
.vacio { padding: 2rem 0; color: var(--suave); text-align: center; }
.grupo { padding: 1.75rem 0 .5rem; border-bottom: 1px solid var(--borde); }
.grupo h2 { margin: 0 0 .2rem; font-size: 1.15rem; border: 0; padding: 0; }
.grupo-meta { margin: 0 0 .9rem; font-size: .82rem; color: var(--suave); }
.clases { display: grid; gap: .35rem; }
.contenido .clase {
  display: grid; grid-template-columns: 2.9rem 1fr auto; gap: .75rem;
  align-items: baseline; padding: .5rem .7rem; border-radius: 7px;
  text-decoration: none; color: inherit; border: 1px solid transparent;
}
.contenido .clase:hover {
  background: var(--destacado); border-color: var(--borde); text-decoration: none;
}
.clase-n { font-variant-numeric: tabular-nums; color: var(--color, var(--acento)); font-weight: 700; }
.clase-nivel {
  font-size: .75rem; color: var(--suave); text-transform: uppercase; letter-spacing: .04em;
}
@media (max-width: 34rem) {
  .clase { grid-template-columns: 2.6rem 1fr; }
  .clase-nivel { display: none; }
  .cifras { grid-template-columns: repeat(3, 1fr); }
}
"""


def _pagina(relativa: Path, titulo: str, cuerpo: str, migas_html: str,
            clases: int, partes: int) -> str:
    subir = "../" * (len(relativa.parts) - 1)
    return PLANTILLA.format(
        titulo=html.escape(titulo), sitio=TITULO, descripcion=html.escape(DESCRIPCION),
        css=f"{subir}assets/estilo.css", manifiesto=f"{subir}manifest.webmanifest",
        icono=f"{subir}assets/icono-192.png", sw=f"{subir}sw.js",
        temario=f"{subir}temario.html", inicio=f"{subir}index.html",
        syllabus=f"{subir}SYLLABUS.html", estado=f"{subir}STATUS.html",
        docs=f"{subir}docs/index.html", repositorio=REPO, migas=migas_html,
        cuerpo=cuerpo, clases=clases, partes=partes,
    )


def generar() -> int:
    if SALIDA.exists():
        shutil.rmtree(SALIDA)
    SALIDA.mkdir(parents=True)
    (SALIDA / "assets").mkdir()
    (SALIDA / "assets" / "estilo.css").write_text(CSS, encoding="utf-8", newline="\n")
    # Evita que GitHub Pages procese el sitio con Jekyll.
    (SALIDA / ".nojekyll").write_text("", encoding="utf-8")

    for relativa in adjuntos_enlazados():
        destino = SALIDA / relativa
        destino.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / relativa, destino)

    datos = portal_extra.inventario.partes()
    resumen = portal_extra.inventario.resumen(datos)
    indices = directorios_con_indice()
    paginas = 0

    for origen in archivos_markdown():
        relativa = origen.relative_to(ROOT)
        destino = SALIDA / relativa.with_suffix(".html")
        destino.parent.mkdir(parents=True, exist_ok=True)

        cuerpo = origen.read_text(encoding="utf-8")
        pagina = _pagina(
            relativa, titulo_de(cuerpo, origen), convertir(cuerpo),
            migas(relativa, indices), resumen.clases, resumen.partes,
        )
        destino.write_text(pagina, encoding="utf-8", newline="\n")
        paginas += 1

        # Un README.md también responde como índice de su directorio. El de la
        # raíz no: la entrada del portal es la portada, no el README volcado.
        if origen.name == "README.md" and relativa.parent != Path("."):
            (destino.parent / "index.html").write_text(pagina, encoding="utf-8", newline="\n")
            paginas += 1

    # Portada y temario: las dos páginas que no existen como archivo del
    # repositorio, porque solo tienen sentido dentro del portal.
    for nombre, cuerpo, titulo in (
        ("index.html", portal_extra.portada(datos, resumen), TITULO),
        ("temario.html", portal_extra.temario(datos, resumen), "Temario completo"),
    ):
        (SALIDA / nombre).write_text(
            _pagina(Path(nombre), titulo, cuerpo, "", resumen.clases, resumen.partes),
            encoding="utf-8", newline="\n",
        )
        paginas += 1

    portal_extra.escribir_pwa(SALIDA, portal_extra.inventario.version())
    return paginas


def verificar() -> int:
    """Comprueba que el sitio se genere y que sus enlaces internos resuelvan."""
    paginas = generar()

    faltantes: list[str] = []
    patron = re.compile(r'href="(?!https?://|mailto:|#)([^"#]+)')
    for pagina in SALIDA.rglob("*.html"):
        for destino in patron.findall(pagina.read_text(encoding="utf-8")):
            if not (pagina.parent / destino).exists():
                faltantes.append(f"{pagina.relative_to(SALIDA).as_posix()} -> {destino}")

    peso = sum(p.stat().st_size for p in SALIDA.rglob("*") if p.is_file())
    print(f"páginas generadas:  {paginas}")
    print(f"peso del sitio:     {peso / 1_048_576:.1f} MB")

    if faltantes:
        print(f"\n{len(faltantes)} enlace(s) roto(s) en el sitio:")
        for item in sorted(set(faltantes))[:40]:
            print(f"  - {item}")
        return 1

    print("\nEl portal se genera y todos sus enlaces internos resuelven")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="genera y verifica los enlaces sin publicar")
    args = parser.parse_args()

    if args.check:
        return verificar()

    paginas = generar()
    print(f"Portal generado en site/: {paginas} páginas")
    return 0


if __name__ == "__main__":
    sys.exit(main())
