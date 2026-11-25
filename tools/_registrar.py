"""Ayuda de trabajo: añade entradas verificadas al registro de fuentes (uso interno del autor)."""
import sys
sys.path.insert(0, 'tools')
import sources_registry as r


def registrar(nuevas):
    reg = r.cargar()
    ids = {e['id'] for e in reg['entries']}
    for tipo, aut, emisor, titulo, autoridad, anio, loc in nuevas:
        e = {"id": r.identificador(emisor, titulo), "type": tipo, "authors": aut, "title": titulo,
             "cited_as": r.cita(emisor, titulo), "authority": autoridad, "published": anio}
        e.update(loc)
        if 'isbn13' in loc:
            assert r.isbn13_valido(loc['isbn13']), loc
        e["locator"] = r.localizador_esperado(e)
        e["accessed"] = "2026-11-25"; e["used_in"] = []; e["status"] = "verificada"
        if e['id'] in ids:
            print('ya existe', e['id']); continue
        reg['entries'].append(e)
    r.guardar(reg)


def citas(*ids):
    reg = r.cargar()
    for e in reg['entries']:
        if e['id'] in ids:
            print(e['id'], '|', e['cited_as'].replace('—', '-'))
