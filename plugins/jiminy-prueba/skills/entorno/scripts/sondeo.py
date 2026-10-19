#!/usr/bin/env python3
"""Sondeo del entorno de Cowork para la Fase 0 de Jiminy.

Solo lee: no instala nada. Escribe un informe en Markdown en la ruta que recibe
como argumento, o lo muestra por pantalla si no recibe ninguna.
"""

from __future__ import annotations

import importlib.metadata
import importlib.util
import os
import platform
import shutil
import socket
import sys
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path

# (módulo que se importa, distribución que se instala, para qué sirve)
LIBRERIAS = [
    ("openpyxl", "openpyxl", "Excel (.xlsx)"),
    ("xlrd", "xlrd", "Excel viejo (.xls)"),
    ("pandas", "pandas", "tablas y datos"),
    ("numpy", "numpy", "cálculo"),
    ("pypdf", "pypdf", "PDF: leer, unir, separar"),
    ("pdfplumber", "pdfplumber", "PDF: texto y tablas"),
    ("fitz", "PyMuPDF", "PDF: texto e imágenes"),
    ("reportlab", "reportlab", "PDF: crear"),
    ("docx", "python-docx", "Word (.docx)"),
    ("pptx", "python-pptx", "PowerPoint (.pptx)"),
    ("PIL", "Pillow", "imágenes"),
    ("matplotlib", "matplotlib", "gráficos"),
    ("bs4", "beautifulsoup4", "páginas web"),
    ("requests", "requests", "descargas"),
]

PROGRAMAS = [
    "python3", "pip", "pip3", "node", "npm", "soffice", "libreoffice",
    "pandoc", "pdftotext", "tesseract", "git", "curl",
]

SITIOS = [
    "https://api.anthropic.com",
    "https://pypi.org",
    "https://github.com",
    "https://raw.githubusercontent.com",
    "https://www.google.com",
]


def version_de(modulo: str, distribucion: str) -> str:
    if importlib.util.find_spec(modulo) is None:
        return "no está"
    try:
        return importlib.metadata.version(distribucion)
    except importlib.metadata.PackageNotFoundError:
        return "está (versión desconocida)"


def memoria() -> str:
    meminfo = Path("/proc/meminfo")
    if not meminfo.is_file():
        return "desconocida"
    valores = {}
    for linea in meminfo.read_text().splitlines():
        clave, _, resto = linea.partition(":")
        if clave in ("MemTotal", "MemAvailable"):
            valores[clave] = int(resto.split()[0]) // 1024
    return f"{valores.get('MemTotal', '?')} MB en total, {valores.get('MemAvailable', '?')} MB libres"


def disco(ruta: Path) -> str:
    uso = shutil.disk_usage(ruta)
    return f"{uso.total // 2**30} GB en total, {uso.free // 2**30} GB libres (en {ruta})"


def llega(url: str) -> str:
    pedido = urllib.request.Request(url, method="HEAD")
    try:
        with urllib.request.urlopen(pedido, timeout=5) as respuesta:
            return f"sí ({respuesta.status})"
    except urllib.error.HTTPError as error:
        return f"sí ({error.code})"
    except (urllib.error.URLError, socket.timeout, OSError) as error:
        motivo = getattr(error, "reason", error)
        return f"no ({motivo})"


def informe(destino: Path | None) -> str:
    lineas = [
        "# Informe del entorno de Cowork",
        "",
        f"Generado: {datetime.now():%Y-%m-%d %H:%M}",
        "",
        "## Sistema",
        "",
        f"- Sistema: {platform.platform()}",
        f"- Arquitectura: {platform.machine()}",
        f"- Procesadores: {os.cpu_count()}",
        f"- Memoria: {memoria()}",
        f"- Disco: {disco(destino.parent if destino else Path.cwd())}",
        f"- Python: {sys.version.split()[0]} ({sys.executable})",
        f"- Este script está en: {Path(__file__).resolve()}",
        f"- CLAUDE_PLUGIN_ROOT: {os.environ.get('CLAUDE_PLUGIN_ROOT', 'no está definida')}",
        f"- Carpeta actual: {Path.cwd()}",
        "",
        "## Librerías de Python",
        "",
        "| Librería | Para qué | Versión |",
        "|---|---|---|",
    ]
    for modulo, distribucion, uso in LIBRERIAS:
        lineas.append(f"| {distribucion} | {uso} | {version_de(modulo, distribucion)} |")
    lineas += ["", "## Programas", "", "| Programa | Dónde está |", "|---|---|"]
    for programa in PROGRAMAS:
        lineas.append(f"| {programa} | {shutil.which(programa) or 'no está'} |")
    lineas += ["", "## Sitios a los que llega", "", "| Sitio | ¿Llega? |", "|---|---|"]
    for sitio in SITIOS:
        lineas.append(f"| {sitio} | {llega(sitio)} |")
    return "\n".join(lineas) + "\n"


def main() -> None:
    destino = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    texto = informe(destino)
    if destino:
        destino.write_text(texto, encoding="utf-8")
    print(texto)


if __name__ == "__main__":
    main()
