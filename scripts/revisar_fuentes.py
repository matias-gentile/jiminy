#!/usr/bin/env python3
"""Lista qué cambió en las fuentes de la biblioteca desde el commit fijado.

Para cada fuente de `biblioteca/fuentes.json` trae la versión más nueva de su rama
principal y compara, solo en las rutas que usa Jiminy, contra el commit fijado.
También avisa si cambió la licencia o si aparecieron archivos nuevos junto a las
rutas que usamos. No modifica nada del repo de Jiminy.

Uso:

    python3 scripts/revisar_fuentes.py [--trabajo CARPETA] [--salida INFORME.md]

Necesita git y acceso a github.com.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
FUENTES = RAIZ / "biblioteca" / "fuentes.json"


def git(carpeta: Path, *argumentos: str) -> str:
    resultado = subprocess.run(
        ["git", "-C", str(carpeta), *argumentos],
        check=True, capture_output=True, text=True,
    )
    return resultado.stdout.strip()


def traer(repo: str, destino: Path) -> Path:
    carpeta = destino / repo.replace("/", "__")
    if (carpeta / ".git").is_dir():
        git(carpeta, "fetch", "--quiet", "origin")
    else:
        subprocess.run(
            ["git", "clone", "--quiet", "--filter=blob:none", "--no-checkout",
             f"https://github.com/{repo}", str(carpeta)],
            check=True, capture_output=True, text=True,
        )
    return carpeta


def revisar(fuente: dict, destino: Path) -> list[str]:
    repo, fijado = fuente["repo"], fuente["commit"]
    lineas = [f"## {repo}", ""]
    try:
        carpeta = traer(repo, destino)
        nuevo = git(carpeta, "rev-parse", "origin/HEAD")
    except subprocess.CalledProcessError as error:
        return lineas + [f"No se pudo traer: {error.stderr.strip() or error}", ""]

    fecha = git(carpeta, "log", "-1", "--format=%cs", nuevo)
    lineas += [f"- Commit fijado: `{fijado}` ({fuente.get('fecha', '?')})",
               f"- Más nuevo: `{nuevo}` ({fecha})", ""]
    if nuevo == fijado:
        return lineas + ["Sin cambios.", ""]

    licencias = git(carpeta, "diff", "--name-only", fijado, nuevo, "--", "LICENSE*", "COPYING*")
    if licencias:
        lineas += [f"**Atención: cambió la licencia** ({licencias.replace(chr(10), ', ')}).", ""]

    for entrada in fuente["rutas"]:
        ruta, uso = entrada["ruta"], entrada.get("uso", "")
        cambios = git(carpeta, "diff", "--stat=100", fijado, nuevo, "--", ruta)
        lineas.append(f"### `{ruta}` ({uso})")
        lineas.append("")
        if cambios:
            lineas += ["```", cambios, "```"]
        else:
            lineas.append("Sin cambios.")
        vecina = str(Path(ruta).parent)
        nuevos = git(carpeta, "diff", "--name-only", "--diff-filter=A", fijado, nuevo, "--", vecina)
        if nuevos:
            lineas += ["", f"Archivos nuevos en `{vecina}`:", ""]
            lineas += [f"- `{archivo}`" for archivo in nuevos.splitlines()[:30]]
        lineas.append("")
    return lineas


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--trabajo", type=Path, help="carpeta donde guardar las copias de las fuentes")
    parser.add_argument("--salida", type=Path, help="archivo donde escribir el informe")
    argumentos = parser.parse_args()

    datos = json.loads(FUENTES.read_text(encoding="utf-8"))
    with tempfile.TemporaryDirectory() as temporal:
        destino = argumentos.trabajo or Path(temporal)
        destino.mkdir(parents=True, exist_ok=True)
        lineas = ["# Cambios en las fuentes de la biblioteca", "",
                  f"Fijadas el {datos.get('revisado', '?')}.", ""]
        for fuente in datos["fuentes"]:
            lineas += revisar(fuente, destino)

    informe = "\n".join(lineas) + "\n"
    if argumentos.salida:
        argumentos.salida.write_text(informe, encoding="utf-8")
    print(informe)
    return 0


if __name__ == "__main__":
    sys.exit(main())
