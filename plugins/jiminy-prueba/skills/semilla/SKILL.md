---
name: semilla
description: >
  Prueba de Jiminy. Usar cuando la persona dice "activá la semilla de prueba".
  Comprueba si se puede copiar un archivo del plugin a la carpeta del proyecto.
---

# Semilla de prueba

El archivo a copiar es `semilla-de-prueba.md`, que está en la misma carpeta que
estas instrucciones.

1. Encontrar el archivo. Probar en este orden y anotar cuál funcionó:
   1. `${CLAUDE_PLUGIN_ROOT}/skills/semilla/semilla-de-prueba.md`
   2. La carpeta de esta habilidad, si sabés cuál es.
   3. Buscar `semilla-de-prueba.md` en el disco, fuera de la carpeta de trabajo.
2. Copiarlo a `frentes/prueba/habilidades/ejemplo/v1.md` dentro de la carpeta de
   trabajo. Crear las carpetas que falten. No modificar el contenido.
3. Comprobar que la copia es idéntica al original.
4. Responder en dos líneas: si funcionó y dónde quedó la copia.
5. Agregar al final de `informe-pruebas.md`, en la raíz de la carpeta de trabajo
   (crearlo si no existe):

   `- <fecha y hora> · Prueba 4 · <copió | no pudo> · origen: <ruta que funcionó> · método: <1 | 2 | 3> · idéntica: <sí | no>`
