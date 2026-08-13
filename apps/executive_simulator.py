#!/usr/bin/env python3
"""Simulador de decisiones ejecutivas.

48 escenarios con informacion incompleta. No hay respuesta correcta: cada
opcion mueve seis dimensiones que compiten entre si, y el aprendizaje esta en
declarar que se sacrifica.
"""
import argparse, json, random, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCENARIOS = json.loads((ROOT / "data" / "scenarios.json").read_text(encoding="utf-8"))

# Los escenarios estan en espanol y llevan tildes y el separador «·». La consola
# de Windows usa cp1252 por defecto y revienta al imprimirlos, asi que la salida
# se fuerza a UTF-8 en cuanto el flujo lo permite.
for flujo in (sys.stdout, sys.stderr):
    if hasattr(flujo, "reconfigure"):
        flujo.reconfigure(encoding="utf-8", errors="replace")

def show(s):
    print(f"\n{s['id']} · Parte {s['part']:02d} · {s['title']}")
    print("-"*72)
    print(s["prompt"])
    for o in s["options"]:
        print(f"  {o['key']}) {o['text']}")
    return s

def run(s):
    show(s)
    choice = input("\nDecisión [A/B/C]: ").strip().upper()
    opt = next((o for o in s["options"] if o["key"] == choice), None)
    if not opt:
        print("Opción inválida.")
        return 2
    print("\nImpacto pedagógico estimado:")
    for k,v in opt["effects"].items():
        print(f"  {k:10s} {v:+d}")
    print("\nDebrief:")
    print(s["debrief"])
    print("\nPreguntas:")
    print("1. ¿Qué supuesto fue más importante?")
    print("2. ¿Qué dato cambiaría tu decisión?")
    print("3. ¿Qué riesgo aceptarías explícitamente?")
    return 0

def main():
    ap=argparse.ArgumentParser(description="Executive Leadership decision simulator")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--scenario")
    ap.add_argument("--random", action="store_true")
    args=ap.parse_args()
    if args.list:
        for s in SCENARIOS:
            print(f"{s['id']}  P{s['part']:02d}  {s['title']}")
        return 0
    if args.scenario:
        s=next((x for x in SCENARIOS if x["id"].upper()==args.scenario.upper()), None)
        if not s:
            raise SystemExit("Escenario no encontrado")
        return run(s)
    return run(random.choice(SCENARIOS))

if __name__=="__main__":
    raise SystemExit(main())
