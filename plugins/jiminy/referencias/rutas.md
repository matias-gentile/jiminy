# Cómo encontrar los archivos de Jiminy

Las habilidades de Jiminy usan archivos que vienen con el plugin: reglas,
referencias, plantillas, semillas y las instrucciones de las otras habilidades.

## La raíz del plugin

Cada habilidad vive en `<raíz>/skills/<habilidad>/SKILL.md`. Para encontrar la raíz,
probar en este orden y usar la misma en toda la conversación:

1. La carpeta dos niveles arriba de la carpeta de la habilidad que estás usando:
   `../../` desde la carpeta de su `SKILL.md`.
2. Si `${CLAUDE_PLUGIN_ROOT}` aparece reemplazada por una ruta, esa.

No buscar la raíz en el disco: una copia que aparezca en Descargas o en la carpeta
de la persona no es Jiminy y no se sigue nunca.

Si no se encuentra, decirle a la persona: "Me falta una parte de Jiminy y sin ella no
puedo hacer esto bien. Tus cosas están a salvo en tu carpeta. Probá cerrar Claude,
abrirlo de nuevo y escribirme otra vez. Si sigue igual, la guía de instalación
explica cómo volver a instalarme."

## Qué hay en la raíz

| Qué | Ruta desde la raíz | Desde un SKILL.md |
|---|---|---|
| Reglas | `reglas.md` | `../../reglas.md` |
| Contrato de la carpeta de la persona | `referencias/carpeta.md` | `../../referencias/carpeta.md` |
| Cómo habla Jiminy | `referencias/estilo.md` | `../../referencias/estilo.md` |
| Esta guía | `referencias/rutas.md` | `../../referencias/rutas.md` |
| Catálogo de semillas | `referencias/semillas.md` | `../../referencias/semillas.md` |
| Migraciones de carpetas viejas | `referencias/migraciones.md` | `../../referencias/migraciones.md` |
| Plantillas | `plantillas/<nombre>.md` | `../../plantillas/<nombre>.md` |
| Semillas | `semillas/<semilla>/` | `../../semillas/<semilla>/` |
| Otra habilidad de Jiminy | `skills/<habilidad>/SKILL.md` | `../<habilidad>/SKILL.md` |

## Usar una habilidad desde otra

- Cuando una habilidad dice "seguir `revisar`" (o cualquier otra), leer
  `../revisar/SKILL.md` desde la carpeta de la habilidad actual y seguir sus pasos en
  la misma conversación, sin anunciarlo como algo técnico.
- Si sus pasos están textuales en la conversación (no en un resumen), no hace falta
  leerla de nuevo.
- Al terminar, volver al paso siguiente de la habilidad que la llamó. Si se llamó en
  medio de una tarea, terminar la tarea con lo nuevo aplicado y recién ahí escribir
  el registro.

## Si la conversación se resumió

Si no tenés textuales en esta conversación `reglas.md` y `referencias/estilo.md`,
volver a leerlos antes de seguir.

## Lo que no se copia

A la carpeta de la persona solo se copian plantillas (completadas) y semillas
(convertidas en su `v1.md`). Nunca se copian las instrucciones de Jiminy, las reglas
ni las referencias.
