#!/usr/bin/env python3
"""Valida el repo de Jiminy antes de subir cambios.

Solo usa la biblioteca estándar. Uso:

    python3 scripts/validar.py

Sale con código 1 si encuentra errores. Las advertencias no cortan la validación.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

NOMBRE_VALIDO = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
CARACTERES_WINDOWS = set('\\:*?"<>|')
NOMBRES_RESERVADOS_WINDOWS = {
    "con", "prn", "aux", "nul",
    *(f"com{i}" for i in range(1, 10)),
    *(f"lpt{i}" for i in range(1, 10)),
}
SECCIONES_HABILIDAD = [
    "## Para qué sirve",
    "## Qué recibe",
    "## Pasos",
    "## Lo que tiene que tener el resultado",
    "## Errores graves",
    "## Formato del entregable",
    "## Controles antes de entregar",
    "## Ejemplo",
]
ARCHIVOS_SEMILLA = ["habilidad.md", "preguntas.md", "controles.md", "origen.md"]
# Marcas que completa nueva-habilidad sin preguntar (salen del perfil o de la conversación).
MARCAS_PROPIAS = {"frente", "v1"}
# Contratos que se leen en cada conversación: tienen que ser livianos.
CONTRATOS_SIEMPRE = ["reglas.md", "referencias/estilo.md", "referencias/rutas.md"]
MAX_BYTES_CONTRATOS = 20 * 1024
BYTES_CONTRATOS_RECOMENDADOS = 16 * 1024
ENCABEZADO_EXACTO = re.compile(r"^---\nname: ([a-z0-9-]+)\ndescription: >\n((?:  \S.*\n)+)---\n")
JERGA = ["plugin", "skill", "markdown", "prompt", "token", "repositorio", "yaml", "json", "terminal", "frontmatter"]
PREFIJOS_DEL_PLUGIN = ("referencias/", "plantillas/", "semillas/", "skills/")
MAX_LINEAS_SKILL = 500
LINEAS_SKILL_RECOMENDADAS = 300
MAX_ARCHIVOS_PLUGIN = 5000
MAX_BYTES_PLUGIN = 200 * 1024 * 1024
IGNORAR = {".git", "__pycache__"}


class Informe:
    def __init__(self) -> None:
        self.errores: list[str] = []
        self.advertencias: list[str] = []

    def error(self, ruta: Path | str, mensaje: str) -> None:
        self.errores.append(f"{_rel(ruta)}: {mensaje}")

    def advertencia(self, ruta: Path | str, mensaje: str) -> None:
        self.advertencias.append(f"{_rel(ruta)}: {mensaje}")


def _rel(ruta: Path | str) -> str:
    ruta = Path(ruta)
    try:
        return str(ruta.relative_to(RAIZ))
    except ValueError:
        return str(ruta)


def archivos(base: Path) -> list[Path]:
    return sorted(
        p for p in base.rglob("*")
        if p.is_file() and not any(parte in IGNORAR for parte in p.relative_to(RAIZ).parts)
    )


def leer_json(ruta: Path, informe: Informe) -> dict | None:
    try:
        return json.loads(ruta.read_text(encoding="utf-8"))
    except FileNotFoundError:
        informe.error(ruta, "no existe")
    except json.JSONDecodeError as error:
        informe.error(ruta, f"JSON inválido: {error}")
    return None


def encabezado(texto: str) -> tuple[dict[str, str], str] | None:
    """Lee el encabezado YAML simple de un SKILL.md: claves de una línea y bloques `>`."""
    if not texto.startswith("---\n"):
        return None
    fin = texto.find("\n---\n", 4)
    if fin == -1:
        return None
    campos: dict[str, str] = {}
    clave = None
    bloque: list[str] = []
    for linea in texto[4:fin].splitlines():
        if clave and (linea.startswith("  ") or not linea.strip()):
            bloque.append(linea.strip())
            continue
        if clave:
            campos[clave] = " ".join(p for p in bloque if p)
            clave, bloque = None, []
        nombre, _, valor = linea.partition(":")
        valor = valor.strip()
        if valor in (">", "|", ">-", "|-"):
            clave = nombre.strip()
        else:
            campos[nombre.strip()] = valor.strip("\"'")
    if clave:
        campos[clave] = " ".join(p for p in bloque if p)
    return campos, texto[fin + 5:]


def validar_catalogo(informe: Informe) -> list[Path]:
    catalogo = RAIZ / ".claude-plugin" / "marketplace.json"
    datos = leer_json(catalogo, informe)
    if not datos:
        return []
    plugins = []
    for entrada in datos.get("plugins", []):
        nombre = entrada.get("name", "")
        if not NOMBRE_VALIDO.match(nombre):
            informe.error(catalogo, f"nombre de plugin inválido: {nombre!r}")
        origen = entrada.get("source")
        if not isinstance(origen, str):
            informe.error(catalogo, f"{nombre}: 'source' tiene que ser una ruta del repo")
            continue
        carpeta = (RAIZ / origen).resolve()
        manifiesto = leer_json(carpeta / ".claude-plugin" / "plugin.json", informe)
        if manifiesto is None:
            continue
        if manifiesto.get("name") != nombre:
            informe.error(carpeta, f"plugin.json dice {manifiesto.get('name')!r} y el catálogo {nombre!r}")
        if not re.match(r"^\d+\.\d+\.\d+$", str(manifiesto.get("version", ""))):
            informe.error(carpeta, "plugin.json necesita una 'version' del tipo 1.2.3")
        plugins.append(carpeta)
    return plugins


def validar_limites(plugin: Path, informe: Informe) -> None:
    lista = archivos(plugin)
    if len(lista) > MAX_ARCHIVOS_PLUGIN:
        informe.error(plugin, f"{len(lista)} archivos; Cowork admite hasta {MAX_ARCHIVOS_PLUGIN}")
    total = sum(p.stat().st_size for p in lista)
    if total > MAX_BYTES_PLUGIN:
        informe.error(plugin, f"{total} bytes; Cowork admite hasta {MAX_BYTES_PLUGIN}")


def validar_skills(plugin: Path, informe: Informe, exacto: bool) -> None:
    for skill in sorted((plugin / "skills").glob("*/SKILL.md")):
        texto = skill.read_text(encoding="utf-8")
        if exacto and not ENCABEZADO_EXACTO.match(texto):
            informe.error(skill, "el encabezado tiene que ser exactamente 'name: …', 'description: >' y el texto con dos espacios de sangría")
        leido = encabezado(texto)
        if not leido:
            informe.error(skill, "falta el encabezado YAML entre líneas '---'")
            continue
        campos, cuerpo = leido
        nombre = campos.get("name", "")
        if nombre != skill.parent.name:
            informe.error(skill, f"'name' es {nombre!r} y la carpeta es {skill.parent.name!r}")
        if not NOMBRE_VALIDO.match(nombre) or len(nombre) > 64:
            informe.error(skill, f"'name' inválido: {nombre!r}")
        descripcion = campos.get("description", "")
        if not descripcion:
            informe.error(skill, "falta 'description'")
        elif len(descripcion) > 1024:
            informe.error(skill, f"'description' tiene {len(descripcion)} caracteres; el máximo es 1024")
        if re.search(r"<[a-zA-Z/][^>]*>", descripcion):
            informe.error(skill, "'description' no puede tener etiquetas XML")
        lineas = cuerpo.count("\n")
        if lineas > MAX_LINEAS_SKILL:
            informe.error(skill, f"{lineas} líneas; el máximo es {MAX_LINEAS_SKILL}")
        elif lineas > LINEAS_SKILL_RECOMENDADAS:
            informe.advertencia(skill, f"{lineas} líneas; conviene menos de {LINEAS_SKILL_RECOMENDADAS}")
        validar_jerga(skill, cuerpo, informe)


def validar_jerga(ruta: Path, cuerpo: str, informe: Informe) -> None:
    """Busca jerga en lo que Jiminy le dice a la persona (texto entre comillas dobles)."""
    for frase in re.findall(r"[\"“]([^\"”\n]{3,})[\"”]", cuerpo):
        for palabra in JERGA:
            if re.search(rf"\b{palabra}\b", frase, re.IGNORECASE):
                informe.advertencia(ruta, f"posible jerga para la persona ({palabra}): \"{frase[:80]}\"")


def validar_rutas_del_plugin(plugin: Path, informe: Informe) -> None:
    """Las rutas del plugin que se nombran entre comillas invertidas tienen que existir.

    Las relativas (`../../reglas.md`, `../revisar/SKILL.md`) se resuelven desde la
    carpeta de la habilidad (la que tiene el SKILL.md), también en sus referencias;
    las demás, desde la raíz del plugin.
    """
    for ruta in archivos(plugin):
        if ruta.suffix != ".md":
            continue
        for citada in re.findall(r"`([^`\s]+)`", ruta.read_text(encoding="utf-8")):
            if re.search(r"[<>{}*…]|\.\.\.(?!/)", citada):
                continue
            if citada.startswith("../"):
                partes = ruta.relative_to(plugin).parts
                if partes[0] != "skills" or len(partes) < 3:
                    continue  # fuera de una habilidad, `../` es solo un ejemplo
                destino = (plugin / "skills" / partes[1] / citada).resolve()
                if not destino.exists():
                    informe.error(ruta, f"nombra `{citada}`, que no existe desde su carpeta")
                elif plugin.resolve() not in destino.parents and destino != plugin.resolve():
                    informe.error(ruta, f"`{citada}` sale de la carpeta del plugin")
                continue
            citada = citada.removeprefix("${CLAUDE_PLUGIN_ROOT}/")
            if not citada.startswith(PREFIJOS_DEL_PLUGIN) and citada != "reglas.md":
                continue
            if not (plugin / citada.rstrip("/")).exists():
                informe.error(ruta, f"nombra `{citada}`, que no existe en el plugin")


def validar_semillas(plugin: Path, informe: Informe) -> None:
    base = plugin / "semillas"
    if not base.is_dir():
        return
    for semilla in sorted(p for p in base.iterdir() if p.is_dir()):
        for nombre in ARCHIVOS_SEMILLA:
            if not (semilla / nombre).is_file():
                informe.error(semilla, f"falta {nombre}")
        habilidad = semilla / "habilidad.md"
        preguntas = semilla / "preguntas.md"
        if not habilidad.is_file() or not preguntas.is_file():
            continue
        texto = habilidad.read_text(encoding="utf-8")
        for seccion in SECCIONES_HABILIDAD:
            if seccion not in texto:
                informe.error(habilidad, f"falta la sección '{seccion}' de plantillas/habilidad.md")
        origen_linea = re.search(rf"^- \*\*Origen:\*\* semilla: {re.escape(semilla.name)} · versión (\d+)$", texto, re.MULTILINE)
        if not origen_linea:
            informe.error(habilidad, f"falta la línea fija '- **Origen:** semilla: {semilla.name} · versión <N>'")
        origen = semilla / "origen.md"
        if origen.is_file():
            texto_origen = origen.read_text(encoding="utf-8")
            if "## Cambios" not in texto_origen:
                informe.error(origen, "falta la sección '## Cambios'")
            elif origen_linea and not re.search(rf"^- versión {origen_linea.group(1)} \(", texto_origen, re.MULTILINE):
                informe.error(origen, f"'## Cambios' no tiene la entrada de la versión {origen_linea.group(1)}")
        texto_preguntas = preguntas.read_text(encoding="utf-8")
        numeradas = re.findall(r"^\d+\.\s", texto_preguntas, re.MULTILINE)
        if not 3 <= len(numeradas) <= 5:
            informe.error(preguntas, f"tiene {len(numeradas)} preguntas; tienen que ser de 3 a 5")
        cubiertas = set(re.findall(r"\{\{([^}]+)\}\}", texto_preguntas))
        for marca in sorted(set(re.findall(r"\{\{([^}]+)\}\}", texto))):
            if marca not in cubiertas and marca not in MARCAS_PROPIAS and not marca.startswith("Nombre"):
                informe.advertencia(habilidad, f"la marca {{{{{marca}}}}} no la completa ninguna pregunta")


def validar_marcas_sueltas(plugin: Path, informe: Informe) -> None:
    for ruta in archivos(plugin):
        relativa = ruta.relative_to(plugin).parts
        if ruta.suffix != ".md" or relativa[0] in ("plantillas", "semillas"):
            continue
        texto = re.sub(r"`[^`]*`", "", ruta.read_text(encoding="utf-8"))
        for marca in re.findall(r"\{\{[^}]*\}\}", texto):
            if marca != "{{…}}":
                informe.advertencia(ruta, f"marca sin completar fuera de plantillas y semillas: {marca}")


def validar_contratos(plugin: Path, informe: Informe) -> None:
    presentes = [plugin / c for c in CONTRATOS_SIEMPRE if (plugin / c).is_file()]
    if not presentes:
        return
    total = sum(p.stat().st_size for p in presentes)
    if total > MAX_BYTES_CONTRATOS:
        informe.error(plugin, f"reglas, estilo y rutas pesan {total} bytes; el máximo es {MAX_BYTES_CONTRATOS}")
    elif total > BYTES_CONTRATOS_RECOMENDADOS:
        informe.advertencia(plugin, f"reglas, estilo y rutas pesan {total} bytes; conviene menos de {BYTES_CONTRATOS_RECOMENDADOS}")
    carpeta = plugin / "referencias" / "carpeta.md"
    plantilla = plugin / "plantillas" / "jiminy.md"
    migraciones = plugin / "referencias" / "migraciones.md"
    if not (carpeta.is_file() and plantilla.is_file()):
        return
    contrato = re.search(r"Versión del contrato: (\d+)", carpeta.read_text(encoding="utf-8"))
    de_carpeta = re.search(r"Versión de la carpeta: (\d+)", plantilla.read_text(encoding="utf-8"))
    if not contrato or not de_carpeta:
        informe.error(carpeta, "faltan 'Versión del contrato: N' o 'Versión de la carpeta: N' en la plantilla jiminy.md")
        return
    if contrato.group(1) != de_carpeta.group(1):
        informe.error(plantilla, f"la carpeta nueva dice versión {de_carpeta.group(1)} y el contrato {contrato.group(1)}")
    version = int(contrato.group(1))
    if version > 1:
        texto = migraciones.read_text(encoding="utf-8") if migraciones.is_file() else ""
        if f"{version - 1} → {version}" not in texto:
            informe.error(migraciones, f"falta la migración '{version - 1} → {version}'")


def validar_nombres(informe: Informe) -> None:
    vistos: dict[str, Path] = {}
    for ruta in archivos(RAIZ):
        for parte in ruta.relative_to(RAIZ).parts:
            if CARACTERES_WINDOWS & set(parte):
                informe.error(ruta, f"'{parte}' tiene caracteres que Windows no acepta")
            if parte.endswith((" ", ".")):
                informe.error(ruta, f"'{parte}' termina en espacio o punto")
            if parte.split(".")[0].lower() in NOMBRES_RESERVADOS_WINDOWS:
                informe.error(ruta, f"'{parte}' es un nombre reservado en Windows")
        clave = str(ruta.relative_to(RAIZ)).lower()
        if clave in vistos:
            informe.error(ruta, f"choca con {_rel(vistos[clave])} en sistemas que no distinguen mayúsculas")
        vistos[clave] = ruta


def validar_enlaces(informe: Informe) -> None:
    for ruta in archivos(RAIZ):
        if ruta.suffix != ".md":
            continue
        for destino in re.findall(r"\]\(([^)\s]+)\)", ruta.read_text(encoding="utf-8")):
            if re.match(r"^[a-z]+:", destino) or destino.startswith("#"):
                continue
            if not (ruta.parent / destino.split("#")[0]).exists():
                informe.error(ruta, f"enlace roto: {destino}")


def validar_fuentes(informe: Informe) -> None:
    ruta = RAIZ / "biblioteca" / "fuentes.json"
    if not ruta.exists():
        return
    datos = leer_json(ruta, informe)
    if datos is None:
        return
    for fuente in datos.get("fuentes", []):
        for campo in ("repo", "commit", "licencia", "rutas"):
            if campo not in fuente:
                informe.error(ruta, f"a la fuente {fuente.get('repo', '?')} le falta '{campo}'")
        if not re.match(r"^[0-9a-f]{40}$", str(fuente.get("commit", ""))):
            informe.error(ruta, f"{fuente.get('repo', '?')}: 'commit' tiene que ser un SHA completo")


def main() -> int:
    informe = Informe()
    plugins = validar_catalogo(informe)
    for plugin in plugins:
        validar_limites(plugin, informe)
        validar_skills(plugin, informe, exacto=plugin.name == "jiminy")
        validar_contratos(plugin, informe)
        validar_rutas_del_plugin(plugin, informe)
        validar_semillas(plugin, informe)
        validar_marcas_sueltas(plugin, informe)
    validar_nombres(informe)
    validar_enlaces(informe)
    validar_fuentes(informe)

    for advertencia in informe.advertencias:
        print(f"advertencia  {advertencia}")
    for error in informe.errores:
        print(f"ERROR        {error}")
    print(f"\n{len(plugins)} plugins · {len(informe.errores)} errores · {len(informe.advertencias)} advertencias")
    return 1 if informe.errores else 0


if __name__ == "__main__":
    sys.exit(main())
