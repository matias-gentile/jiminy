# Fase 0: pruebas en Cowork

Estas pruebas responden las preguntas de *Sin confirmar* en `docs/diseno.md`
antes de escribir el núcleo. Nada de esto es para la primera usuaria todavía.

## Antes de empezar

- Usá una **cuenta personal Pro**, no la de Jam City: la de empresa tiene ajustes
  de organización que un usuario común no tiene.
- El plugin `jiminy-prueba` queda instalado en tu cuenta y aparece también en el
  chat y en Claude Code. **Al terminar, quitalo:** *Customize > Plugins >
  jiminy-prueba > Remove*.
- Las habilidades de prueba solo escriben dentro de la carpeta del proyecto de prueba.
- Cada prueba deja una línea en `informe-pruebas.md`, en esa carpeta. Al final,
  pasame ese archivo, `informe-entorno.md`, `registro-de-activacion.md` y la tabla
  de resultados completa.

## Preparación (una vez)

1. Creá una carpeta vacía llamada `Jiminy prueba`, por ejemplo en Documentos.
2. Poné adentro un PDF cualquiera sin datos personales (se usa en la prueba 3).
3. En Cowork: *Projects* > **+** > *Use an existing folder* > elegí `Jiminy prueba`.
   Nombre: "Jiminy prueba". Dejá las instrucciones vacías por ahora.

## Prueba 0. ¿Corre Cowork en esta compu?

En la MacBook Neo y en una Windows x64:

1. Instalá Claude Desktop, entrá con una cuenta Pro y abrí Cowork.
2. Pedí: "Creá un archivo hola.txt que diga hola" en una carpeta de prueba.
3. Fijate:
   - ¿Abre Cowork, o aparece un mensaje del tipo "Apple Silicon required"?
   - ¿Cuánto tarda en arrancar la primera vez?
   - ¿Cómo queda la memoria mientras trabaja? En Mac: *Monitor de Actividad >
     Memoria > Presión de memoria* (verde, amarilla o roja). En Windows:
     *Administrador de tareas > Rendimiento > Memoria*.

**Decide:** si el piloto puede hacerse en la compu de la primera usuaria. Si
Cowork no corre ahí, hay que diseñar un plan B: Jiminy en el chat de Claude, con
otro mecanismo de memoria.

## Prueba 1. Instalación y actualizaciones

1. *Customize > Plugins > Add marketplace* y pegá `matias-gentile/jiminy`.
2. Instalá `jiminy-prueba`. Contá los clics y sacá capturas: son la base de la
   guía de instalación para la usuaria.
3. En una sesión nueva preguntá: "¿Qué versión de la prueba de Jiminy tenés?".
   Tiene que contestar "versión 1".
4. Pasá a la versión 2. Editá en GitHub dos archivos:
   - `plugins/jiminy-prueba/skills/version/SKILL.md`: cambiá las dos apariciones
     de "versión 1" por "versión 2".
   - `plugins/jiminy-prueba/.claude-plugin/plugin.json`: cambiá `0.1.0` por `0.2.0`.

   Si preferís, avisame y lo subo yo.
5. En el marketplace, activá *Sync automatically* o tocá *Check for updates*. Abrí
   una sesión nueva y repetí la pregunta.

Fijate: ¿cuánto tardó en llegar? ¿Hizo falta reiniciar la app o abrir una sesión
nueva? Si no llegó, ¿llega cambiando solo el texto, sin subir la versión del plugin?

**Decide:** la guía de instalación y cómo llegan las mejoras del núcleo.

## Prueba 2. ¿Escribe y lee en la carpeta del proyecto entre sesiones?

1. Abrí una sesión nueva en el proyecto "Jiminy prueba" y pedí: "Anotá en mi
   cuaderno de prueba: me gusta el café cortado".
2. Cerrá la sesión. Abrí otra en el mismo proyecto y preguntá: "¿Qué hay en mi
   cuaderno de prueba?".
3. Buscá `cuaderno-de-prueba.md` en la carpeta desde Finder o el Explorador.

Fijate: ¿lo encontró en la segunda sesión? ¿El archivo está en la carpeta que
elegiste? ¿Qué ruta informó Claude? Anotá la forma de esa ruta: va al contrato de la
carpeta.

4. Abrí una conversación **fuera** del proyecto y pedí: "Anotá en mi cuaderno de
   prueba: hola". ¿Puede escribir en la carpeta del proyecto, o hay que abrir una
   conversación nueva adentro? ¿Una conversación de afuera se puede pasar al proyecto?
5. Repetí el paso 1 con una carpeta dentro de Documentos sincronizada con iCloud (en
   Mac) u OneDrive (en Windows), si la compu la tiene. ¿Funciona igual?

**Decide:** si funciona guardar las habilidades de la persona como archivos en su carpeta.

## Prueba 3. ¿Se activa la puerta sin nombrar a Jiminy?

La habilidad `puerta` de prueba anota cada activación en
`registro-de-activacion.md` y avisa con una línea. Solo actúa si la carpeta tiene
el archivo `jiminy.md`.

1. Creá `jiminy.md` en la raíz de la carpeta. Puede decir solo "Carpeta de
   Jiminy", o pedile a Claude que lo cree.
2. Hacé estos cinco pedidos en sesiones nuevas dentro del proyecto, sin nombrar a Jiminy:
   - "resumime el PDF que está en la carpeta"
   - "escribime un mail para reprogramar un turno"
   - "ordená esta lista de compras: leche, pan, café, manzanas"
   - "dame ideas para un posteo sobre el ojo seco"
   - "¿qué dice el PDF sobre el tema principal?"
3. Anotá cuántas veces apareció "(Prueba: la puerta de Jiminy se activó.)".
4. Creá en la raíz de la carpeta un archivo `CLAUDE.md` con este texto, sin tocar
   las instrucciones del proyecto, y repetí los cinco pedidos:
   "Este es un proyecto de Jiminy. Para cualquier pedido en este proyecto, usá primero
   la habilidad «puerta» de Jiminy (jiminy-prueba:puerta), antes que cualquier otra
   habilidad, y seguí sus pasos aunque también uses las de PDF, Word o Excel."
   ¿Cowork lo carga solo?
5. Borrá `CLAUDE.md`, pegá ese mismo texto en las instrucciones del proyecto y repetí
   los cinco pedidos.
6. Fuera del proyecto, en una sesión común de Cowork o en el chat, pedí: "resumime
   este texto: el café es una bebida que se hace con granos tostados". La puerta no
   tiene que activarse ni anotar nada.
7. En el pedido del PDF, fijate si se usó la habilidad de PDF que trae Claude en lugar
   de la puerta, o las dos.

**Decide:** cuál de las tres capas de activación funciona (descripción sola,
`CLAUDE.md`, instrucciones del proyecto). Si `CLAUDE.md` alcanza, pegar las
instrucciones pasa a ser opcional; si ninguna de las dos funciona sola, `empezar`
tiene que insistir con pegarlas. También decide si Jiminy queda quieto fuera de su
proyecto.

## Prueba 4. ¿Puede copiar una semilla del plugin a la carpeta?

1. En el proyecto pedí: "Activá la semilla de prueba".
2. Fijate si apareció `frentes/prueba/habilidades/ejemplo/v1.md` en la carpeta. La
   ruta del plugin que funcionó queda anotada en el informe.

**Decide:** cómo se activan las semillas.

## Prueba 5. ¿Qué guarda la memoria del proyecto?

Después de las pruebas 2 a 4:

1. Abrí la memoria del proyecto, en la configuración del proyecto.
2. Anotá qué guardó sola, si se puede editar o borrar (y dónde, paso a paso: Jiminy
   se lo explica a la persona cuando le pide olvidar algo), y si se puede apagar.

**Decide:** si usamos la memoria del proyecto, solo nuestros archivos o las dos; y
si conviene un proyecto para todo o uno por frente.

## Prueba 6. ¿Qué trae la máquina virtual?

1. En el proyecto pedí: "Revisá el entorno de prueba de Jiminy".
2. Se genera `informe-entorno.md` en la carpeta. Incluye el sistema, Python, las
   librerías para Excel, PDF, Word e imágenes, los programas disponibles, la
   memoria, el disco y a qué sitios llega.

**Decide:** si planillas y PDFs funcionan sin instalar nada, y qué semillas
necesitan otra estrategia.

## Prueba 7. Privacidad

1. En Claude, entrá a *Settings > Privacy* (o como se llame hoy). Buscá si las
   conversaciones se usan para entrenar y cómo se apaga.
2. Sacá una captura y anotá el nombre exacto de cada opción.

**Decide:** el texto del paso de privacidad de `empezar`.

## Prueba 7b. Archivos adjuntos y opciones para tocar

1. En el proyecto, arrastrá un PDF a la conversación (no a la carpeta) y pedí:
   "Guardá una copia de este archivo en la carpeta Entrada". ¿Dónde quedó el adjunto?
   ¿Claude lo pudo leer y copiar?
2. Pedí: "Haceme una pregunta con opciones para tocar". ¿Aparecen botones? ¿Hay un
   botón para saltear?
3. Pedí: "Creá un Word que diga hola en la carpeta Entregables". ¿Aparece el archivo
   como enlace en la conversación? ¿Se abre al tocarlo?

**Decide:** cómo `empezar` pide el primer archivo, si Jiminy pregunta con botones y
cómo le dice a la persona dónde quedó lo que preparó.

## Prueba 8. Windows

Repetí las pruebas 0, 1, 2, 4 y 6 en una compu Windows x64.

## Resultados

| # | Mac | Windows | Notas | ¿Cambia el diseño? |
|---|---|---|---|---|
| 0 | | | | |
| 1 | | | | |
| 2 | | | | |
| 3 | | — | | |
| 4 | | | | |
| 5 | | — | | |
| 6 | | | | |
| 7 | | — | | |
| 7b | | | | |

Al terminar, quitá `jiminy-prueba` de tu cuenta.
