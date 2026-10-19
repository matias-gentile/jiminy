# Migraciones de carpetas

Cuando cambia el contrato de la carpeta (`referencias/carpeta.md`), sube su
`Versión del contrato` y acá se agrega cómo pasar una carpeta de la versión anterior
a la nueva.

## Cómo se usa

1. Leer la línea `Versión de la carpeta: N` de `jiminy.md`. Si no está, es la 1.
2. Si N es menor que la `Versión del contrato`, aplicar en orden cada migración desde
   N hasta la actual.
3. Cada migración crea o mueve solo lo que dice, nunca borra lo que dejó la persona y
   al terminar actualiza la línea de `jiminy.md`.
4. Avisar en una línea: "Acomodé tu carpeta a una versión nueva de Jiminy. No se
   perdió nada."

## Migraciones

Sin migraciones: la versión actual del contrato es la 1.
