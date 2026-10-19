# Plan de desarrollo

Fecha: 2026-10-19 · Rama: `jiminy-0.1` · Versión del plugin: 0.1.0

Este plan cubre todo lo que se puede construir sin Cowork: el núcleo (Fase 1), el
ciclo de mejora (Fase 2), las semillas (Fase 3), la documentación para la persona y
para el piloto, la validación automática y las herramientas de la actualización de
la biblioteca (Fase 5), listas pero sin activar. La Fase 0 y el piloto (Fase 4) se
hacen en Cowork, con personas, y quedan para Matías.

Cada componente se diseñó para funcionar aunque la Fase 0 dé resultados distintos a
los esperados. Ver *Cómo cubre cada duda de la Fase 0*.

## Entregables

| Componente | Archivos | Fase |
|---|---|---|
| Contratos compartidos | `plugins/jiminy/reglas.md`, `plugins/jiminy/referencias/*.md`, `plugins/jiminy/plantillas/*.md` | 1 |
| Puerta de entrada | `plugins/jiminy/skills/puerta/` | 1 |
| Empezar | `plugins/jiminy/skills/empezar/` | 1 |
| Revisar | `plugins/jiminy/skills/revisar/` | 1 |
| Nueva habilidad | `plugins/jiminy/skills/nueva-habilidad/` | 2 |
| Recordar criterio | `plugins/jiminy/skills/recordar-criterio/` | 2 |
| Mejorar habilidad (incluye volver atrás) | `plugins/jiminy/skills/mejorar-habilidad/` | 2 |
| Seis semillas | `plugins/jiminy/semillas/<semilla>/` | 3 |
| Avisos de licencia | `plugins/jiminy/AVISOS-DE-TERCEROS.md` | 3 |
| Guía de instalación para la persona | `docs/guia-instalacion.md` | 4 |
| Protocolo del piloto | `docs/piloto.md` | 4 |
| Escenarios de aceptación en Cowork | `docs/escenarios.md` | 4 |
| Validación automática | `scripts/validar.py`, `.github/workflows/validar.yml` | todas |
| Guía para desarrollar | `CLAUDE.md` | todas |
| Actualización de la biblioteca (sin activar) | `biblioteca/fuentes.json`, `scripts/revisar_fuentes.py`, `docs/actualizar-biblioteca.md` | 5 |

## Contratos compartidos

Todo componente los respeta. Ninguno los contradice ni los duplica: los cita.

- `plugins/jiminy/reglas.md`: las once reglas que valen siempre.
- `plugins/jiminy/referencias/carpeta.md`: la estructura de la carpeta de la persona,
  el formato de cada archivo y **quién puede escribir cada uno**.
- `plugins/jiminy/referencias/estilo.md`: cómo habla Jiminy y las palabras prohibidas.
- `plugins/jiminy/referencias/rutas.md`: cómo encontrar los archivos del plugin y
  cómo una habilidad usa a otra.
- `plugins/jiminy/referencias/semillas.md`: el catálogo de semillas y cómo proponerlas.
- `plugins/jiminy/plantillas/`: los archivos de la persona en blanco.

## Convenciones para escribir habilidades

- Formato Cowork: `skills/<nombre>/SKILL.md` con encabezado YAML de `name` (igual a la
  carpeta, minúsculas y guiones, hasta 64 caracteres) y `description` (hasta 1024
  caracteres, sin etiquetas XML). Material largo en `skills/<nombre>/referencias/`.
- La `description` dice, en tercera persona, cuándo usarla, con las frases reales
  que dice la gente entre comillas. Toda habilidad salvo `empezar` aclara que es
  "dentro de una carpeta de Jiminy (la que tiene jiminy.md)".
- El cuerpo está escrito como instrucciones para Claude, en español e imperativo. Lo
  que se le dice a la persona va entre comillas y respeta `estilo.md`.
- Primer paso de toda habilidad salvo `empezar`: comprobar `jiminy.md` (regla 1).
- Cuerpo de menos de 300 líneas. Nada de rutas absolutas: todo se resuelve con `rutas.md`.
- Ningún componente depende de conectores, de internet ni de instalar algo. Para
  crear Word, Excel, PowerPoint o PDF se usan las herramientas de documentos que
  Claude tenga disponibles. Si no hay, se entrega en un formato más simple y se avisa.

## Especificación por componente

### `puerta`

**Para qué:** es la puerta de entrada. Recibe cualquier pedido dentro de la carpeta
de Jiminy, elige la habilidad de la persona que corresponde y hace la tarea con sus
criterios. Es lo que hace que Jiminy funcione sin que la persona sepa nombres.

**Se activa con:** cualquier pedido de trabajo (resumir, escribir, contestar,
ordenar, revisar, planificar, buscar ideas, explicar) dentro de una carpeta de
Jiminy; "Jiminy", "Jimini", "Yimini", "Pepe Grillo" o "Grillo" cuando la carpeta ya
existe; preguntas como "¿qué sabés hacer?", "¿qué habilidades tengo?".

**Lee:** `jiminy.md`, `indice.md`, `yo/perfil.md`, `yo/criterios.md`, los
`criterios.md` y `registro.md` del frente, la versión actual de la habilidad.
**Escribe:** solo `frentes/<f>/registro.md` y los entregables.

**Pasos:**

1. Sin `jiminy.md`: si la persona nombró a Jiminy o pidió empezar, seguir `empezar`;
   si no, no hacer nada propio.
2. Leer las reglas y el estilo una vez por sesión, el índice, el perfil y los
   criterios generales.
3. Decidir qué es el pedido, en este orden:
   - corrige o define cómo quiere las cosas → seguir `recordar-criterio`;
   - quiere cambiar cómo hace algo una habilidad, o volver a como estaba → seguir `mejorar-habilidad`;
   - quiere enseñarle algo nuevo → seguir `nueva-habilidad`;
   - quiere un tema nuevo o revisar su perfil → seguir `empezar`;
   - pregunta qué sabe hacer o qué aprendió → contestar desde el índice y los criterios, en simple;
   - es una tarea → paso 4.
4. Elegir **una** habilidad del índice por sus frases y su sentido. Si dudás entre
   dos, una pregunta. Si no hay ninguna, mirar el catálogo de semillas: si una
   sirve, proponer probarla ("Tengo una forma armada para esto. ¿La probamos?") y,
   si dice que sí, seguir `nueva-habilidad` desde esa semilla. Si tampoco, hacer la
   tarea igual, con cuidado general.
5. Elegir el frente: el de la habilidad, o el que corresponda; si no está claro,
   `general`. Leer sus criterios. Si un criterio del frente choca con uno general,
   gana el del frente; si dos del mismo nivel chocan, preguntar.
6. Antes de abrir archivos, aplicar las reglas 3 y 4 (privado y datos de terceros).
7. Hacer la tarea siguiendo la versión actual de la habilidad y los criterios.
8. Antes de entregar, seguir `revisar`.
9. Guardar el entregable en `entregables/` con el nombre del contrato y decir dónde quedó.
10. Agregar una línea al `registro.md` del frente.
11. Si la persona corrige algo, seguir `recordar-criterio`. Si en el registro hay
    tres o más tareas parecidas sin habilidad, proponer una vez crear una con
    `nueva-habilidad`. Si dice que no, anotarlo en el registro y no volver a
    proponerlo esa semana.

**Aceptación:** con una carpeta armada, "resumime este PDF" usa la habilidad
correcta, lee sus criterios, pasa por `revisar`, guarda `_v1` sin pisar nada y anota
el registro. Fuera de una carpeta de Jiminy no hace nada. Nunca nombra habilidades
por su carpeta ni usa jerga.

### `empezar`

**Para qué:** la primera sesión, y volver a ella para retomar, sumar un frente o
revisar el perfil.

**Se activa con:** "empezar", "empecemos", "primer día", "configurame", "no sé por
dónde arrancar", "¿cómo empiezo?"; "Jiminy" (y sus variantes) cuando la carpeta
todavía no tiene `jiminy.md`; "quiero usarte también para…", "agregá un tema";
"revisemos mi perfil".

**Escribe:** `jiminy.md`, `indice.md`, `yo/perfil.md`, `yo/criterios.md`, los
frentes (`criterios.md` y `registro.md`), las carpetas `entrada/`, `entregables/`,
`privado/` y `frentes/general/`.

**Modos:**

- **Primera vez** (no hay `jiminy.md`):
  1. Apertura: tres líneas sobre qué va a pasar y cuánto tarda (unos 20 minutos); después "¿Arrancamos?".
  2. Carpeta: comprobar que la sesión tiene una carpeta de trabajo. Si no, guiar a
     crear un proyecto de Cowork con una carpeta nueva llamada "Jiminy", paso a paso
     (Mac y Windows), con los nombres de pantalla de la documentación y la
     aclaración "o como aparezca en tu idioma". Si la carpeta elegida ya tiene
     archivos, no tocarlos nunca.
  3. Crear la estructura (avisando en dos líneas): `jiminy.md`, `indice.md`, `yo/`,
     `entrada/`, `entregables/`, `privado/` y el frente `general` ("Otras cosas").
  4. Instrucciones del proyecto: mostrar el texto de
     `plantillas/instrucciones-proyecto.md` y guiar a pegarlo, de a un paso. Es
     recomendado; si se complica, se saltea.
  5. Privacidad: en dos líneas, que lo que lee Jiminy se procesa en los servidores
     de Anthropic; dónde está el ajuste de privacidad; y la pregunta "¿Qué cosas no
     deberían entrar nunca a esta carpeta?".
  6. Entrevista, de a una pregunta (ver `skills/empezar/referencias/entrevista.md`):
     tener una hipótesis de qué necesita y seguir preguntando hasta estar seguro de
     sus frentes, sus tareas repetidas, cuánta autonomía quiere, el formato y el
     tono. Como mucho ocho preguntas. Siempre se puede decir "seguimos otro día".
  7. Resumen de lo que entendió y confirmación. Recién ahí escribir `yo/perfil.md`,
     los frentes y la tabla de frentes del índice.
  8. Proponer dos o tres habilidades desde el catálogo de semillas, con nombres en
     sus palabras. Por cada una que elija, seguir `nueva-habilidad` desde la
     semilla. Las que queden para otro día se anotan en `## Pendiente` del índice.
  9. Primera tarea real: pedirle que ponga un archivo suyo en Entrada (explicar cómo
     arrastrarlo) y hacerla con la habilidad nueva, como la haría `puerta`.
  10. Cierre: qué quedó armado, cómo pedir cosas, cómo enseñarle algo nuevo y que
      si algo no le gusta, lo diga.
- **Retomar** (hay `jiminy.md` pero falta el perfil o hay algo en `## Pendiente`):
  ofrecer seguir donde quedó.
- **Sumar un frente:** dos o tres preguntas, crear la carpeta del frente, agregarlo
  al índice y ofrecer una semilla.
- **Revisar el perfil:** mostrarlo en simple, preguntar qué cambió y escribir solo
  eso, después de confirmarlo.

**Referencias propias:** `skills/empezar/referencias/entrevista.md`,
`skills/empezar/referencias/proyecto.md` (crear el proyecto y pegar las
instrucciones, en Mac y Windows) y `skills/empezar/referencias/privacidad.md`. Lo que
dependa de la Fase 0 se marca como "[confirmar en Fase 0]".

**Aceptación:** una persona sin experiencia termina con la carpeta armada, el
perfil confirmado, dos o tres habilidades y un entregable real, sin que se le pida
nada técnico más allá de crear el proyecto y pegar un texto.

### `nueva-habilidad`

**Para qué:** crear una habilidad de la persona, desde una semilla o desde cero.

**Se activa con:** "quiero que aprendas a…", "te quiero enseñar a…", "siempre hago
esto…", "hacé una habilidad para…", "armemos una forma de…"; y cuando `empezar` o
`puerta` la llaman con una semilla.

**Escribe:** `habilidades/<h>/v1.md`, `historial.md` y una fila en el índice.

**Pasos:**

- **Desde una semilla:** leer su `habilidad.md` y `preguntas.md`; hacer las
  preguntas de a una, salteando las que ya contestó en el perfil; completar todas
  las marcas `{{…}}` (si algo no se sabe todavía, se saca la línea o se deja una
  regla razonable; nunca queda una marca); ponerle el nombre en sus palabras.
- **Desde cero:** "Contame una tarea que hacés seguido"; los pasos como los haría
  la persona (cómo se trabaja); lo que no puede faltar en el resultado y los
  errores graves (qué sabe un experto); un ejemplo de lo que recibe, en Entrada; un
  ejemplo de buen resultado o cómo se ve; el formato del entregable; y cómo lo
  pediría (de ahí salen las frases del índice).
- **En los dos casos:** elegir el frente; si ya existe una habilidad parecida,
  proponer `mejorar-habilidad` en lugar de crear otra; probar el borrador con el
  ejemplo, mostrar el resultado y ajustar; recién cuando la persona está conforme,
  escribir `v1.md`, la primera entrada del historial y la fila del índice.
- La persona no ve el archivo de la habilidad, salvo que lo pida.

**Aceptación:** la `v1.md` sigue `plantillas/habilidad.md`, no tiene marcas sin
completar, tiene frases reales en el índice y se probó con un ejemplo.

### `revisar`

**Para qué:** el control antes de entregar. También se usa a pedido.

**Se activa con:** antes de cada entrega de `puerta` y de las habilidades de la
persona; "revisá esto", "¿está bien?", "fijate si hay errores", "controlá los números".

**Controles:**

1. **Entrega:** está todo lo pedido, en el formato y con el nombre del contrato.
2. **Fidelidad:** cada dato concreto (número, nombre, fecha, cita, referencia)
   coincide con la fuente; lo que no está en la fuente se marca **[verificar]**; no
   hay citas, autores ni enlaces inventados.
3. **Consistencia:** los totales cierran con sus filas, los resúmenes con sus
   tablas, las cantidades con lo que hay.
4. **Uso:** quien lo recibe lo puede usar tal cual.
5. **Terminación:** no quedan marcas `{{…}}`, pendientes, secciones vacías ni texto de relleno.
6. **Criterios:** se aplicaron los generales y los del frente.
7. **Controles propios:** los de la habilidad y, si viene de una semilla, los de su `controles.md`.
8. **Privacidad:** no se copiaron datos de terceros sensibles al entregable.

Si algo falla: arreglarlo y, si importa, decirlo en una línea; si no se puede
arreglar, decirlo con claridad. Nunca esconderlo. Cuando revisa un archivo de la
persona a pedido, nunca lo modifica: entrega las observaciones o una copia
corregida en Entregables.

**Aceptación:** detecta un total que no cierra, una cita que no está en la fuente y
una marca sin completar.

### `recordar-criterio`

**Para qué:** que Jiminy aprenda de cada corrección sin llenarse de ruido.

**Se activa con:** "no, así no", "no me gusta", "siempre que…", "nunca…",
"acordate que…", "la próxima vez…", "prefiero…"; "olvidate de…", "ya no hagas…";
"¿qué aprendiste de mí?", "¿qué criterios tenés?".

**Escribe:** solo los `criterios.md` (generales y de cada frente).

**Pasos:**

1. Proponer el criterio en una línea, *cuándo aplica / qué hacer*, en las palabras de la persona.
2. **Filtro de datos del caso:** si es un dato de esta tarea ("este mes la consulta
   cuesta X"), no va a la memoria permanente; decirlo. Nunca se guardan datos de
   terceros, contraseñas ni datos de salud de nadie.
3. **Habilidad o criterio:** si cambia cómo hace algo una habilidad siempre, proponer
   `mejorar-habilidad` en lugar de guardar un criterio suelto.
4. **Alcance:** general o del frente. Si no es obvio, una pregunta.
5. **Duplicados y choques:** si ya hay uno parecido, archivar el viejo y guardar el
   nuevo; si se contradicen, preguntar cuál vale.
6. Con la confirmación, guardarlo con la fecha y el ejemplo que lo originó, y
   aplicarlo enseguida a la tarea en curso.
7. **Presupuesto:** con más de 30 vigentes en un archivo, proponer juntar algunos o
   convertirlos en habilidad.
8. "Olvidate de…": pasarlo a Archivados con el motivo.
9. "¿Qué aprendiste?": listar los vigentes en simple, por frente.

**Aceptación:** "acordate que siempre firmo como Dra. X" queda como criterio
general; "este paciente se llama Y" no se guarda; "los resúmenes de paper tienen que
traer el tamaño de la muestra" propone `mejorar-habilidad`.

### `mejorar-habilidad`

**Para qué:** cambiar una habilidad probando la forma nueva contra la actual, y
volver atrás cuando haga falta.

**Se activa con:** "cambiá cómo hacés…", "la próxima hacelo así…" (cuando es sobre
cómo trabaja una habilidad), "quiero que el resumen tenga…", "probá si queda
mejor…"; "volvé a como estaba antes", "deshacé el cambio", "usá la versión
anterior"; "¿qué le cambiaste a…?"; y cuando la llaman `puerta` o `recordar-criterio`.

**Escribe:** `vN+1.md`, `pruebas/`, el historial y la versión actual en el índice.

**Pasos para mejorar:**

1. Identificar la habilidad por el índice y leer la versión actual.
2. Escribir `vN+1.md` con **un** cambio, sin tocar el resto. Si pide varios a la vez,
   sugerir de a uno; si prefiere todos juntos, el veredicto será "no se puede saber".
3. Elegir el ejemplo: un archivo que ella indique, o el último que usó con esa habilidad.
4. Hacer la tarea con las dos versiones sobre el mismo ejemplo y guardar los
   resultados en `pruebas/`. Asignar A y B sin que la persona sepa cuál es cuál
   (si el historial tiene una cantidad par de entradas, A es la nueva; si es impar,
   A es la actual) y anotar en el historial cuál fue cuál.
5. Mostrar las dos (o un resumen de cada una y dónde están) y preguntar: "¿Cuál te
   sirve más, A o B?".
6. Si elige la nueva, pasa a ser la actual en el índice. Si elige la actual, la
   nueva queda guardada, pero no se usa.
7. Anotar en el historial: cambio, por qué, comparación, elección y veredicto
   (ayudó, empeoró, sin diferencia, no se puede saber).
8. Si no hay ejemplo para comparar, ofrecer adoptarla sin comparar, con veredicto
   "no se puede saber".

**Pasos para volver atrás:** contar en simple las versiones, con su fecha y lo que
cambió cada una; la persona elige; cambiar la versión actual en el índice; anotar
"volvió a vN" en el historial. Nunca se borra una versión.

**Aceptación:** después de un cambio hay `v2.md`, dos archivos en `pruebas/`, una
entrada completa en el historial y el índice apunta a la versión elegida; "volvé a
como estaba" deja el índice en `v1` sin borrar nada.

### Semillas

Cada semilla en `plugins/jiminy/semillas/<semilla>/` tiene:

- `habilidad.md`: sigue `plantillas/habilidad.md`, con marcas `{{…}}` donde va lo que
  cuenta la persona. Es instrucción para Claude, en español.
- `preguntas.md`: de tres a cinco preguntas, de a una, que completan esas marcas.
  Formato: `1. <pregunta> → completa {{marca}}`.
- `controles.md`: de cinco a diez controles que `revisar` suma.
- `origen.md`: fuentes (repo, commit fijado, ruta), licencia y qué se cambió.

Todas respetan las reglas, funcionan sin conectores y sin internet, nunca modifican
la Entrada y no dependen de librerías que haya que instalar.

| Semilla | Base | Puntos clave |
|---|---|---|
| `papeles-pdfs` | Propia | Resumir y pasar datos a una tabla; montos y fechas exactos; lo ilegible queda **[verificar]**; PDFs escaneados sin texto se avisan. |
| `mails` | `inbox-manager` (Anthropic), camino sin conectores | La persona pega el mail o lo pone en Entrada; borrador con su tono y firma; contesta todas las preguntas; nunca se manda. |
| `planillas` | Propia | Archivo nuevo en Entregables; no se pierden filas (contar entrada y salida); totales que cierran; formato de fechas y moneda; plan B si no hay herramientas de Excel. |
| `escribir` | `avoid-ai-writing` (wshobson), adaptado al español | Su voz a partir de ejemplos suyos; lista de muletillas de IA en español; nada de relleno. |
| `aprender` | `research-synthesist` (agency-agents) | Resumen de paper con pregunta, diseño, muestra, resultados con números y límites; diez citas del mismo estudio son una sola prueba; solo lo que está en el PDF; preguntas de repaso; plan de estudio. |
| `redes` | `social-content-engine` (Anthropic), `instagram-curator` y `carousel-growth-engine` (agency-agents) | Plan del mes, textos con su voz, ideas de imagen y carruseles; deja todo listo para que ella publique; las reglas de su profesión salen de la entrevista, no se asumen; sin llamados comerciales por defecto; nunca imágenes de pacientes sin consentimiento. |

Las fuentes están en `biblioteca/indice.md`, fijadas a un commit. Lo adaptado
conserva el aviso de licencia en `origen.md` y en `plugins/jiminy/AVISOS-DE-TERCEROS.md`.

### Documentación

- **`docs/guia-instalacion.md`**, para la persona, sin jerga: qué necesita (plan con
  Cowork, compu compatible), instalar Claude, agregar Jiminy (*Customize > Plugins >
  Add marketplace* con `matias-gentile/jiminy` e instalar "Jiminy"), crear el
  proyecto o dejar que Jiminy la guíe, decir "Jiminy, empecemos", privacidad, qué
  hacer si algo no anda y cómo quitarlo.
- **`docs/piloto.md`**, para Matías: antes, durante la primera sesión (qué observar,
  cuándo ayudar y anotar cada ayuda), las dos semanas, qué juntar (registro,
  historial, criterios, entregables), las preguntas del cierre y cómo traer los resultados.
- **`docs/escenarios.md`**: escenarios de aceptación para correr en Cowork después
  de la Fase 0. Cada uno con preparación, qué decir, qué tiene que pasar, qué no
  tiene que pasar y qué archivos tienen que quedar.

### Herramientas

- **`scripts/validar.py`** (solo biblioteca estándar): manifiestos JSON válidos; cada
  plugin del catálogo existe; cada `SKILL.md` con `name` igual a su carpeta y
  `description` dentro de los límites; las rutas del plugin que nombran las
  habilidades existen; nombres de archivo válidos en Windows; cada semilla tiene
  sus cuatro archivos; no quedan marcas `{{…}}` fuera de plantillas y semillas;
  límites de tamaño de Cowork. Sale con error si algo falla.
- **`.github/workflows/validar.yml`**: corre el validador en cada push y pull request.
- **`CLAUDE.md`**: cómo trabajar en este repo (contratos, convenciones, validar antes
  de subir, no romper la carpeta de quienes ya lo usan).
- **`biblioteca/fuentes.json`** y **`scripts/revisar_fuentes.py`**: las fuentes fijadas
  y un script que, para cada una, trae la versión nueva y lista qué cambió en las
  rutas que usamos desde el commit fijado. **`docs/actualizar-biblioteca.md`**: el
  procedimiento y el texto de la tarea semanal, para activarla después del piloto.

## Cómo cubre cada duda de la Fase 0

| Duda | Cómo se cubre en esta versión |
|---|---|
| 1. MacBook Neo | Nada del plugin depende de la compu. Si Cowork no corre ahí, el plan B se diseña con los resultados. |
| 2. Escribir y leer en la carpeta | Todo vive en archivos de la carpeta. Si no persistiera, la Fase 0 lo muestra antes del piloto. |
| 3. Activación sin nombrar a Jiminy | Tres capas: la descripción de `puerta`, las instrucciones del proyecto que pega `empezar` y el nombre "Jiminy" como palabra para llamarlo. |
| 4. Copiar semillas | `rutas.md` prueba tres caminos para encontrar el plugin. |
| 5. Memoria nativa | Nuestros archivos son la fuente de verdad; no se depende de la memoria del proyecto. |
| 6. Librerías de la máquina | Las semillas usan las herramientas de documentos de Claude y tienen un plan B en formatos simples. |
| 7. Privacidad | `empezar` explica el tema y marca la ubicación exacta del ajuste como "[confirmar en Fase 0]". |
| 8. Actualizaciones | La guía pide activar *Sync automatically*. |
| 9. Windows | Nombres de archivo válidos en Windows (lo controla el validador) y guías con pasos para los dos sistemas. |

## Verificación

1. **Validador** en cada cambio.
2. **Revisión independiente** de cada componente, contra la especificación, los
   contratos, el estilo y las reglas.
3. **Simulaciones de punta a punta** con tres personas inventadas (una médica que
   también usa Instagram, un contador independiente que no confía en la
   tecnología y una jubilada que quiere ordenar papeles). Siguen las habilidades al
   pie de la letra en una carpeta de prueba. Cada problema que aparece se corrige.
4. **Crítica de seguridad y privacidad** sobre todo el plugin.
5. **Escenarios en Cowork** (`docs/escenarios.md`) después de la Fase 0, a cargo de Matías.

## Fuera de esta etapa

- Correr la Fase 0 y el piloto: los hace Matías en Cowork.
- Activar la tarea semanal de la biblioteca: después del piloto (decisión 11).
- Conectores, publicar automáticamente y datos de pacientes (ver *Fuera de alcance*
  en `docs/diseno.md`).
