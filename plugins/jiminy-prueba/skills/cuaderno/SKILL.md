---
name: cuaderno
description: >
  Prueba de Jiminy. Usar cuando la persona dice "anotá en mi cuaderno de
  prueba…" o pregunta "¿qué hay en mi cuaderno de prueba?".
---

# Cuaderno de prueba

Esta prueba comprueba si lo que se escribe en la carpeta del proyecto sigue ahí
en otra sesión.

La carpeta de trabajo es la que Cowork tiene abierta en esta sesión. Si no hay
ninguna, decirlo y no hacer nada más.

## Si pide anotar

1. Agregar al final de `cuaderno-de-prueba.md`, en la raíz de la carpeta de
   trabajo (crearlo si no existe), una línea:
   `- <fecha y hora>: <lo que pidió anotar>`
2. Responder "Anotado en cuaderno-de-prueba.md." y la ruta completa del archivo
   tal como la ves.

## Si pregunta qué hay

1. Leer `cuaderno-de-prueba.md` y mostrar su contenido tal cual.
2. Si no existe, decirlo y listar los archivos que sí hay en la raíz de la
   carpeta de trabajo.

## En los dos casos

Agregar al final de `informe-pruebas.md`, en la raíz de la carpeta de trabajo
(crearlo si no existe):

`- <fecha y hora> · Prueba 2 · <anotó | leyó | no encontró el cuaderno> · ruta: <ruta completa de la carpeta de trabajo>`
