# Cómo encontrar los archivos de Jiminy

Las habilidades de Jiminy usan archivos que vienen con el plugin: reglas,
referencias, plantillas, semillas y las instrucciones de las otras habilidades.

## La raíz del plugin

Probar en este orden y quedarse con la primera que funcione. Una vez encontrada,
usar siempre la misma en toda la sesión.

1. Si `${CLAUDE_PLUGIN_ROOT}` está definida, o aparece ya reemplazada por una ruta,
   esa es la raíz.
2. Si no, la raíz está dos carpetas arriba de la carpeta de la habilidad que estás
   usando: las habilidades viven en `<raíz>/skills/<habilidad>/SKILL.md`.
3. Si tampoco, buscar en el disco, fuera de la carpeta de la persona, el archivo
   `referencias/rutas.md` que esté junto a `plantillas/` y `semillas/`. Por ejemplo:
   `find / -path '*/referencias/rutas.md' -not -path '/proc/*' 2>/dev/null`.
   Quedarse con la que tenga `.claude-plugin/plugin.json` con `"name": "jiminy"`.

Si no se encuentra la raíz: seguir con lo que estas instrucciones ya dicen, sin
inventar plantillas, y decirle a la persona en simple: "No encuentro una parte de
Jiminy. Puede que haya que volver a instalarlo."

## Qué hay en la raíz

| Qué | Ruta |
|---|---|
| Reglas | `reglas.md` |
| Contrato de la carpeta de la persona | `referencias/carpeta.md` |
| Cómo habla Jiminy | `referencias/estilo.md` |
| Catálogo de semillas | `referencias/semillas.md` |
| Plantillas de los archivos de la persona | `plantillas/<nombre>.md` |
| Semillas | `semillas/<semilla>/habilidad.md`, `preguntas.md`, `controles.md` |
| Instrucciones de las habilidades de Jiminy | `skills/<habilidad>/SKILL.md` |

## Usar una habilidad desde otra

Cuando una habilidad dice "seguir `revisar`" (o cualquier otra), leer
`skills/revisar/SKILL.md` en la raíz y seguir sus pasos en la misma conversación,
sin anunciarlo como algo técnico. Si esa habilidad ya está cargada, no hace falta
leerla de nuevo.

## Lo que no se copia

A la carpeta de la persona solo se copian plantillas (completadas) y semillas
(convertidas en su `v1.md`). Nunca se copian las instrucciones de Jiminy, las
reglas ni las referencias.
