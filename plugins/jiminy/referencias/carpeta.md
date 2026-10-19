# La carpeta de la persona

Este es el contrato de la carpeta donde Jiminy trabaja con cada persona. Todas las
habilidades de Jiminy leen y escriben estos archivos con este formato y respetan
quién puede escribir cada uno. Si una habilidad necesita algo que no está acá, no
lo inventa: primero se agrega a este contrato.

## Cómo se reconoce

La carpeta de Jiminy es la carpeta de trabajo del proyecto de Cowork que tiene
`jiminy.md` en la raíz. Sin ese archivo, Jiminy no hace nada, salvo `empezar`, que
es la que lo crea.

## Estructura

```
<raíz>/
  jiminy.md                          qué es esta carpeta (para la persona) y las reglas
  indice.md                          frentes y habilidades: lo que usa la puerta para elegir
  yo/
    perfil.md                        quién es y cómo le gusta trabajar
    criterios.md                     criterios que aplican a todo
  frentes/general/                   "Otras cosas": lo que no entra en otro frente (siempre existe)
  frentes/<frente>/
    criterios.md                     criterios de ese frente
    registro.md                      una línea por tarea
    habilidades/<habilidad>/
      v1.md, v2.md…                  versiones de la habilidad
      historial.md                   qué cambió, por qué y qué eligió la persona
      pruebas/                       resultados de las comparaciones
  entrada/                           lo que la persona quiere que Jiminy lea
  entregables/                       lo que Jiminy prepara
  privado/                           Jiminy no entra sin permiso
```

## Nombres de archivos y carpetas

- Minúsculas, sin tildes ni ñ, con guiones entre palabras. "Consultorio" →
  `consultorio`; "Diseño de posteos" → `diseno-de-posteos`.
- Nunca estos caracteres, que Windows no acepta: `\ / : * ? " < > |`.
- El nombre como lo dice la persona (con tildes y mayúsculas) va dentro de los
  archivos, no en el nombre del archivo.
- **Entregables:** `<nombre-corto>_v<N>.<extensión>`, por ejemplo
  `post-ojo-seco_v1.docx`. Si ya existe `_v1`, el nuevo es `_v2`. Nunca se pisa uno.
- **Fechas:** siempre `aaaa-mm-dd`.

## Quién escribe qué

| Archivo | Lo crea | Lo puede cambiar | Lo lee |
|---|---|---|---|
| `jiminy.md` | empezar | empezar | todas |
| `indice.md` | empezar | empezar (frentes), nueva-habilidad (agrega habilidades), mejorar-habilidad (versión actual) | puerta, todas |
| `yo/perfil.md` | empezar | empezar | todas |
| `yo/criterios.md` | empezar (vacío) | recordar-criterio | todas las que trabajan |
| `frentes/<f>/criterios.md` | empezar (vacío) | recordar-criterio | todas las que trabajan en ese frente |
| `frentes/<f>/registro.md` | empezar (vacío) | puerta (agrega líneas) | puerta |
| `habilidades/<h>/vN.md` | nueva-habilidad (v1), mejorar-habilidad (las siguientes) | nadie: una versión no se modifica | puerta, mejorar-habilidad |
| `habilidades/<h>/historial.md` | nueva-habilidad | mejorar-habilidad (agrega entradas) | mejorar-habilidad |
| `habilidades/<h>/pruebas/` | mejorar-habilidad | mejorar-habilidad | mejorar-habilidad |
| `entrada/` | empezar (vacía) | solo la persona | todas |
| `entregables/` | empezar (vacía) | todas las que trabajan (archivos nuevos, nunca pisar) | todas |
| `privado/` | empezar (vacía) | solo la persona | nadie sin permiso |

"Todas las que trabajan" incluye las habilidades de la persona cuando la puerta
las usa.

## Formato de cada archivo

### `jiminy.md`

Se crea desde `plantillas/jiminy.md`, ajustando el trato al de la persona. Termina
con la línea `Versión de la carpeta: 1 · Creada: aaaa-mm-dd`.

### `indice.md`

Se crea desde `plantillas/indice.md`. Tiene dos tablas.

**Frentes:**

| Frente | Carpeta | Para qué |
|---|---|---|
| Consultorio | `frentes/consultorio` | Papers, informes y clases |

**Habilidades:**

| Habilidad | Carpeta | Se usa cuando dice… | Versión actual | Origen |
|---|---|---|---|---|
| Resumen de paper | `frentes/consultorio/habilidades/resumen-de-paper` | "resumime este paper" · "qué dice este estudio" | v2 | semilla: aprender |

- **Habilidad:** el nombre en palabras de la persona.
- **Se usa cuando dice…:** de dos a cinco frases reales de la persona, entre
  comillas y separadas por ` · `.
- **Versión actual:** la que se usa. Volver atrás es cambiar este valor.
- **Origen:** `propia` o `semilla: <carpeta de la semilla>`. El encabezado de la habilidad
  (`vN.md`) guarda además la versión de la semilla de la que salió:
  `semilla: <carpeta> · versión <N>`. Cuando la semilla del plugin tiene una versión
  más nueva, `puerta` ofrece una vez compararla con la de la persona usando
  `mejorar-habilidad`. Nunca se reemplaza sola.

**Pendiente** (opcional; lo escribe `empezar` y lo vacía quien completa cada cosa):

```
## Pendiente

- Crear habilidad: <nombre en palabras de la persona> (semilla: <carpeta> | propia) · frente: <carpeta del frente>
```

Al crear la carpeta, la tabla de frentes ya tiene la fila de `general`:
`| Otras cosas | frentes/general | Lo que no entra en otro frente |`.

### `yo/perfil.md`

Se crea desde `plantillas/perfil.md` con lo que la persona contó en la entrevista.
Solo `empezar` lo cambia, y solo después de mostrarle el cambio a la persona.

### `criterios.md` (en `yo/` y en cada frente)

Se crea desde `plantillas/criterios.md`. Cada criterio vigente es una línea:

```
- **Cuándo:** <situación>. **Qué hacer:** <acción>. _(aaaa-mm-dd · de: <ejemplo breve que lo originó>)_
```

Un criterio que deja de valer no se borra: pasa a **Archivados**, tachado y con la
fecha y el motivo:

```
- ~~**Cuándo:** … **Qué hacer:** …~~ _(archivado aaaa-mm-dd: <motivo>)_
```

Como mucho 30 criterios vigentes por archivo.

### `frentes/<f>/registro.md`

Se crea desde `plantillas/registro.md`. Una línea por tarea terminada:

```
- aaaa-mm-dd · <pedido en hasta 12 palabras> · <nombre de la habilidad o "sin habilidad"> · <entregado | corregido | a medias>
```

Si hace falta, al final va una nota corta: ` · nota: <texto>`. Por ejemplo,
` · nota: no quiso crear una habilidad para esto`.

### `habilidades/<h>/vN.md`

Siguen `plantillas/habilidad.md`. `v1.md` sale de una semilla completada con lo que
contó la persona, o de `nueva-habilidad`. Cada versión nueva es un archivo nuevo.

### `habilidades/<h>/historial.md`

Se crea desde `plantillas/historial.md`. Una entrada por cambio, la más nueva abajo:

```
## aaaa-mm-dd · v2

- **Cambio:** <qué cambió, en una línea>
- **Por qué:** <qué pidió o corrigió la persona>
- **Comparación:** A = v1, B = v2 · ejemplo: <archivo usado> (o "sin comparar")
- **Eligió:** <A | B | ninguna>
- **Veredicto:** <ayudó | empeoró | sin diferencia | no se puede saber>
- **Versión actual:** v2
```

Volver a una versión anterior también es una entrada, con **Cambio:** `volvió a v1`.

### `habilidades/<h>/pruebas/`

Los dos resultados de cada comparación: `aaaa-mm-dd_A.<ext>` y `aaaa-mm-dd_B.<ext>`.
Si hay más de una comparación el mismo día: `aaaa-mm-dd-2_A.<ext>`.

### `entrada/`, `entregables/`, `privado/`

Carpetas. Ver *Quién escribe qué*.
