---
name: entorno
description: >
  Prueba de Jiminy. Usar cuando la persona dice "revisá el entorno de prueba de
  Jiminy". Revisa qué programas y librerías trae la máquina de Cowork, sin
  instalar nada.
---

# Entorno de prueba

No instalar nada en ningún paso.

1. Correr el script `sondeo.py`, que está en la carpeta `scripts` junto a estas
   instrucciones, y pasarle la ruta del informe:

   `python3 <ruta de sondeo.py> <carpeta de trabajo>/informe-entorno.md`

   Para encontrar el script, probar
   `${CLAUDE_PLUGIN_ROOT}/skills/entorno/scripts/sondeo.py`; si no existe,
   buscar `sondeo.py` en el disco, fuera de la carpeta de trabajo.
2. Si no hay `python3`, correr estos comandos y guardar la salida en
   `informe-entorno.md`, en la raíz de la carpeta de trabajo:
   `uname -a`, `cat /etc/os-release`, `free -m`, `df -h` y
   `command -v python3 python pip3 node soffice pandoc pdftotext tesseract git curl`.
3. Responder con un resumen de cinco líneas: sistema, Python, librerías que
   faltan, programas disponibles y a qué sitios llega.
4. Agregar al final de `informe-pruebas.md`, en la raíz de la carpeta de trabajo
   (crearlo si no existe):

   `- <fecha y hora> · Prueba 6 · informe-entorno.md <generado | no generado> · método: <script | comandos>`
