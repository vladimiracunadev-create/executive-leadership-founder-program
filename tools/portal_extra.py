"""Portada, temario y capa instalable del portal de estudio.

`build_site.py` convierte cada archivo del repositorio a HTML, y eso basta para
leerlo. Pero la entrada del portal no puede ser el README volcado: quien llega
por primera vez necesita ver de un vistazo de qué va el programa, cuántas
clases tiene y por dónde entrar.

Este módulo produce las tres piezas que faltan:

* la **portada**, con las cifras reales, las seis etapas y las 24 partes;
* el **temario**, con las 288 clases y un buscador que filtra sin recargar;
* el **manifiesto y el trabajador de servicio**, que permiten instalar el
  portal en el teléfono y consultarlo después sin conexión.

Todo se calcula leyendo el repositorio: ninguna cifra está escrita a mano.
"""

from __future__ import annotations

import html
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import inventario  # noqa: E402

PORTADA = """<section class="hero">
  <p class="hero-cinta">Programa abierto · español · licencia MIT</p>
  <h1>De profesional individual<br><span>a founder y business owner</span></h1>
  <p class="hero-bajada">{clases} clases en {partes} partes y seis etapas, cada una con su caso
     ejecutivo, su práctica deliberada y su bibliografía verificable. Sin registro,
     sin coste y sin publicidad.</p>
  <div class="hero-acciones">
    <a class="boton" href="{primera}">Empezar por la clase 001</a>
    <a class="boton secundario" href="temario.html">Ver las {clases} clases</a>
    <a class="boton secundario" href="docs/LEARNING_PATH.html">Ruta de aprendizaje</a>
  </div>
  <dl class="cifras">
    <div><dt>{clases}</dt><dd>clases</dd></div>
    <div><dt>{partes}</dt><dd>partes</dd></div>
    <div><dt>{horas}</dt><dd>horas</dd></div>
    <div><dt>{labs}</dt><dd>laboratorios</dd></div>
    <div><dt>{casos}</dt><dd>casos</dd></div>
    <div><dt>{bibliografia}</dt><dd>obras citadas</dd></div>
  </dl>
</section>

<section class="bloque">
  <h2>La escalera de responsabilidad</h2>
  <p class="bloque-intro">El recorrido es acumulativo: cada nivel añade una unidad de
     responsabilidad sobre la anterior, y ninguna se salta.</p>
  <ul class="escalera">
    <li>Profesional</li><li>Líder</li><li>Jefe</li><li>Manager</li><li>Gerente</li>
    <li>Director</li><li>CEO</li><li>Founder</li><li>Owner</li>
  </ul>
  <p class="bloque-intro">Dicho en términos de qué se administra:
     <strong>yo → equipo → sistema → unidad de negocio → empresa → capital → propiedad</strong>.</p>
</section>

<section class="bloque">
  <h2>Las seis etapas</h2>
  <p class="bloque-intro">Cada etapa supone la anterior. Primero se aprende a responder por
     uno mismo, después por un equipo, después por una unidad de negocio, después por una
     empresa completa y, por último, a crear la propia.</p>
  <div class="etapas">{etapas}</div>
</section>

<section class="bloque">
  <h2>Las {partes} partes</h2>
  <p class="bloque-intro">Cada parte trae sus 12 clases, sus 4 laboratorios, su caso
     integrador y su proyecto. Pulsa una para abrir su índice.</p>
  <div class="rejilla">{tarjetas}</div>
</section>

<section class="bloque">
  <h2>Para consultar</h2>
  <div class="rejilla">
    <a class="tarjeta" href="SYLLABUS.html"><span class="tarjeta-emoji">🗂️</span>
      <strong>Temario maestro</strong>
      <span class="tarjeta-nota">Las {clases} clases con sus horas, etapas y proyectos</span></a>
    <a class="tarjeta" href="docs/LEARNING_PATH.html"><span class="tarjeta-emoji">🧭</span>
      <strong>Ruta de aprendizaje</strong>
      <span class="tarjeta-nota">Por dónde entrar según tu punto de partida</span></a>
    <a class="tarjeta" href="docs/BOOKS.html"><span class="tarjeta-emoji">📚</span>
      <strong>Bibliografía</strong>
      <span class="tarjeta-nota">{bibliografia} obras en tres capas: núcleo, complemento y fuente oficial</span></a>
    <a class="tarjeta" href="docs/CHILE_FOUNDER_TRACK.html"><span class="tarjeta-emoji">🇨🇱</span>
      <strong>Founder Track Chile</strong>
      <span class="tarjeta-nota">Formalización, laboral y operación con fuentes oficiales</span></a>
    <a class="tarjeta" href="docs/ASSESSMENT_FRAMEWORK.html"><span class="tarjeta-emoji">🧪</span>
      <strong>Marco de evaluación</strong>
      <span class="tarjeta-nota">Cómo se puntúa cada clase, caso, laboratorio y proyecto</span></a>
    <a class="tarjeta" href="STATUS.html"><span class="tarjeta-emoji">📊</span>
      <strong>Estado del programa</strong>
      <span class="tarjeta-nota">Las cifras reales, contadas archivo por archivo</span></a>
  </div>
</section>

<section class="bloque aviso">
  <h2>Antes de aplicar nada</h2>
  <p>Este material es <strong>formativo</strong>. No constituye asesoría legal, tributaria,
     financiera, laboral ni de inversión, y completar clases no concede un cargo ni una
     certificación profesional. Las normas citadas —en particular las chilenas—
     <strong>cambian con la fecha</strong>: cada clase cierra con sus fuentes y con la
     obligación de verificarlas en origen antes de ejecutar un trámite o una decisión real.</p>
</section>
"""

TEMARIO = """<section class="temario-cabecera">
  <h1>Temario completo</h1>
  <p>Las {clases} clases del programa, en orden. Escribe para filtrar por título, parte,
     etapa o concepto.</p>
  <input id="buscador" type="search" placeholder="Buscar entre las {clases} clases…"
         autocomplete="off" aria-label="Buscar una clase">
  <p id="resultado" class="resultado" role="status">{clases} clases</p>
</section>
<div id="listado">{listado}</div>
<p id="vacio" class="vacio" hidden>Ninguna clase coincide con esa búsqueda.<br>
  El buscador mira los títulos y los conceptos centrales de cada clase.
  Para recorrer el programa por orden, prueba el <a href="SYLLABUS.html">temario maestro</a>.</p>
<script>
(function () {{
  var caja = document.getElementById("buscador");
  var filas = Array.prototype.slice.call(document.querySelectorAll("#listado .clase"));
  var grupos = Array.prototype.slice.call(document.querySelectorAll("#listado .grupo"));
  var contador = document.getElementById("resultado");
  var vacio = document.getElementById("vacio");
  function normaliza(t) {{
    return t.normalize("NFD").replace(/[\\u0300-\\u036f]/g, "").toLowerCase();
  }}
  filas.forEach(function (f) {{ f.dataset.busca = normaliza(f.dataset.texto); }});
  caja.addEventListener("input", function () {{
    var q = normaliza(caja.value.trim());
    var vistas = 0;
    filas.forEach(function (f) {{
      var ok = !q || f.dataset.busca.indexOf(q) !== -1;
      f.hidden = !ok;
      if (ok) vistas++;
    }});
    grupos.forEach(function (g) {{
      g.hidden = g.querySelectorAll(".clase:not([hidden])").length === 0;
    }});
    contador.textContent = vistas === filas.length
      ? filas.length + " clases"
      : vistas + " de " + filas.length + " clases";
    vacio.hidden = vistas !== 0;
  }});
}})();
</script>
"""


def _html(ruta: str) -> str:
    return ruta[:-3] + ".html" if ruta.endswith(".md") else ruta


def _tono(etapa: inventario.Etapa) -> str:
    """Los dos tonos de la etapa, para que la hoja de estilo elija según el tema.

    Se emiten las dos variables y **no** `--color` directamente: un estilo en
    línea gana a cualquier regla de la hoja, así que si aquí se fijara `--color`
    la consulta de tema oscuro no podría cambiarlo. La hoja resuelve
    `--color: var(--color-claro)` o `var(--color-oscuro)` según corresponda.
    """
    return f"--color-claro:{etapa.color_claro};--color-oscuro:{etapa.color_oscuro}"


def portada(datos: list[inventario.Parte], resumen: inventario.Resumen) -> str:
    bloques_etapa = []
    for indice, etapa in enumerate(inventario.ETAPAS, start=1):
        propias = [p for p in datos if etapa.desde <= p.numero <= etapa.hasta]
        clases = sum(len(p.clases) for p in propias)
        bloques_etapa.append(
            f'<article class="etapa" style="{_tono(etapa)}">'
            f'<h3><span aria-hidden="true">{etapa.emoji}</span> Etapa {indice} · '
            f"{html.escape(etapa.nombre)}</h3>"
            f'<p class="etapa-meta">Partes {etapa.desde:02d}–{etapa.hasta:02d} · '
            f"{clases} clases · {html.escape(etapa.salida)}</p>"
            f"<p>{html.escape(etapa.idea)}</p></article>"
        )

    tarjetas = []
    for parte in datos:
        etapa = inventario.etapa_de(parte.numero)
        tarjetas.append(
            f'<a class="tarjeta" href="{_html(parte.ruta_md)}" style="{_tono(etapa)}">'
            f'<span class="tarjeta-numero">{etapa.emoji} Parte {parte.numero:02d}</span>'
            f"<strong>{html.escape(parte.titulo)}</strong>"
            f'<span class="tarjeta-nota">{len(parte.clases)} clases · '
            f"{len(parte.labs)} laboratorios · {parte.horas} h</span></a>"
        )

    primera = _html(datos[0].clases[0].ruta_md)
    return PORTADA.format(
        clases=resumen.clases, partes=resumen.partes, horas=resumen.horas,
        labs=resumen.labs, casos=resumen.casos, bibliografia=resumen.bibliografia,
        primera=primera, etapas="".join(bloques_etapa), tarjetas="".join(tarjetas),
    )


def temario(datos: list[inventario.Parte], resumen: inventario.Resumen) -> str:
    piezas = []
    for parte in datos:
        etapa = inventario.etapa_de(parte.numero)
        numero_etapa = inventario.numero_de_etapa(etapa)

        filas = []
        for clase in parte.clases:
            texto = " ".join([
                f"{parte.numero:02d}", parte.titulo, clase.titulo,
                clase.nivel, etapa.nombre, *clase.conceptos,
            ])
            filas.append(
                f'<a class="clase" href="{_html(clase.ruta_md)}" '
                f'data-texto="{html.escape(texto, quote=True)}">'
                f'<span class="clase-n">{clase.numero:03d}</span>'
                f"<span class=\"clase-t\">{html.escape(clase.titulo)}</span>"
                f'<span class="clase-nivel">{html.escape(clase.nivel)}</span></a>'
            )

        piezas.append(
            f'<section class="grupo" style="{_tono(etapa)}">'
            f'<h2><span aria-hidden="true">{etapa.emoji}</span> Parte {parte.numero:02d} · '
            f"{html.escape(parte.titulo)}</h2>"
            f'<p class="grupo-meta">Etapa {numero_etapa} · {html.escape(etapa.nombre)} · '
            f"{len(parte.clases)} clases · {parte.horas} h · "
            f'<a href="{_html(parte.ruta_md)}">índice de la parte</a></p>'
            f'<div class="clases">{"".join(filas)}</div></section>'
        )

    return TEMARIO.format(clases=resumen.clases, listado="".join(piezas))


MANIFIESTO = {
    "name": "Executive Leadership & Founder Program",
    "short_name": "Liderazgo Ejecutivo",
    "description": "288 clases de liderazgo, gestión, dirección y creación de empresas.",
    "start_url": "./index.html",
    "scope": "./",
    "display": "standalone",
    "background_color": "#0d1117",
    "theme_color": "#0969da",
    "lang": "es",
    "categories": ["education", "business"],
    "icons": [
        {"src": "assets/icono-192.png", "sizes": "192x192", "type": "image/png",
         "purpose": "any maskable"},
        {"src": "assets/icono-512.png", "sizes": "512x512", "type": "image/png",
         "purpose": "any maskable"},
    ],
}

# Cachea lo que se visita, de modo que una clase leída una vez se pueda releer
# sin conexión. No se precachea el sitio entero: son varios megabytes y casi
# nadie los quiere todos.
TRABAJADOR = """const CACHE = "elfp-v{version}";
const ESENCIALES = ["./", "./index.html", "./temario.html", "./assets/estilo.css"];

self.addEventListener("install", (evento) => {
  evento.waitUntil(caches.open(CACHE).then((c) => c.addAll(ESENCIALES)));
  self.skipWaiting();
});

self.addEventListener("activate", (evento) => {
  evento.waitUntil(
    caches.keys().then((claves) =>
      Promise.all(claves.filter((k) => k !== CACHE).map((k) => caches.delete(k)))
    )
  );
  self.clients.claim();
});

self.addEventListener("fetch", (evento) => {
  const peticion = evento.request;
  if (peticion.method !== "GET" || !peticion.url.startsWith(self.location.origin)) return;
  evento.respondWith(
    fetch(peticion)
      .then((respuesta) => {
        const copia = respuesta.clone();
        caches.open(CACHE).then((c) => c.put(peticion, copia));
        return respuesta;
      })
      .catch(() => caches.match(peticion).then((r) => r || caches.match("./index.html")))
  );
});
"""


def icono_png(lado: int, color: tuple[int, int, int] = (9, 105, 218)) -> bytes:
    """Genera un PNG cuadrado de un color, sin dependencias.

    El portal necesita un icono para poder instalarse en el teléfono. Dibujar un
    logotipo pediría una librería de imagen; un cuadrado del color de marca
    cumple el requisito y no añade dependencias al flujo.
    """
    import struct
    import zlib

    fila = bytes(color) * lado
    crudo = b"".join(b"\x00" + fila for _ in range(lado))

    def trozo(etiqueta: bytes, datos: bytes) -> bytes:
        return (struct.pack(">I", len(datos)) + etiqueta + datos
                + struct.pack(">I", zlib.crc32(etiqueta + datos) & 0xFFFFFFFF))

    return (b"\x89PNG\r\n\x1a\n"
            + trozo(b"IHDR", struct.pack(">IIBBBBB", lado, lado, 8, 2, 0, 0, 0))
            + trozo(b"IDAT", zlib.compress(crudo, 9))
            + trozo(b"IEND", b""))


def escribir_pwa(salida: Path, version: str) -> None:
    (salida / "manifest.webmanifest").write_text(
        json.dumps(MANIFIESTO, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n"
    )
    (salida / "sw.js").write_text(
        TRABAJADOR.replace("{version}", version), encoding="utf-8", newline="\n"
    )
    for lado in (192, 512):
        (salida / "assets" / f"icono-{lado}.png").write_bytes(icono_png(lado))
