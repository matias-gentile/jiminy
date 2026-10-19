# Plan de desarrollo

Fecha: 2026-10-19 · Rama: `jiminy-0.1` · Versión del plugin: 0.1.0

Este plan cubre todo lo que se puede construir sin Cowork: el núcleo (Fase 1), el
ciclo de mejora (Fase 2), las semillas (Fase 3), la documentación para la persona y
para el piloto, la validación automática y las herramientas de la actualización de
la biblioteca (Fase 5), listas pero sin activar. La Fase 0 y el piloto (Fase 4) se
hacen en Cowork, con personas, y quedan para Matías.

Los contratos y este plan pasaron por una crítica independiente desde tres lentes
(persona sin experiencia, factibilidad en Cowork, consistencia y seguridad) antes de
implementar.

## Entregables

| Componente | Archivos | Fase |
|---|---|---|
| Contratos compartidos | `plugins/jiminy/reglas.md`, `plugins/jiminy/referencias/*.md`, `plugins/jiminy/plantillas/*.md` | 1 |
| Puerta de entrada | `plugins/jiminy/skills/puerta/` | 1 |
| Empezar | `plugins/jiminy/skills/empezar/` | 1 |
| Revisar | `plugins/jiminy/skills/revisar/` | 1 |
| Nueva habilidad | `plugins/jiminy/skills/nueva-habilidad/` | 2 |
| Recordar criterio | `plugins/jiminy/skills/recordar-criterio/` | 2 |
| Mejorar habilidad (incluye volver atrás y dejar de usar) | `plugins/jiminy/skills/mejorar-habilidad/` | 2 |
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

- `plugins/jiminy/reglas.md`: las trece reglas que valen siempre.
- `plugins/jiminy/referencias/carpeta.md`: la carpeta de la persona, el formato de
  cada archivo, **quién puede escribir cada uno**, el orden cuando dos cosas chocan y
  cómo reparar lo que falta.
- `plugins/jiminy/referencias/estilo.md`: cómo habla Jiminy y las palabras prohibidas.
- `plugins/jiminy/referencias/rutas.md`: cómo encontrar los archivos del plugin y
  cómo una habilidad usa a otra.
- `plugins/jiminy/referencias/semillas.md`: el catálogo de semillas.
- `plugins/jiminy/referencias/migraciones.md`: cómo actualizar carpetas viejas.
- `plugins/jiminy/plantillas/`: los archivos de la persona en blanco.

## Cómo se activa Jiminy

Tres capas, de la más confiable a la menos:

1. **Las instrucciones del proyecto** (`plantillas/instrucciones-proyecto.md`), que la
   persona pega con la guía de `empezar`.
2. **`CLAUDE.md` en la carpeta** (`plantillas/CLAUDE.md`), con el mismo texto, por si
   Cowork lo carga solo [confirmar en Fase 0, prueba 3].
3. **El nombre "Jiminy"** y la descripción de `puerta`, como respaldo.

La descripción de `puerta` reclama solo pedidos dentro de una carpeta de Jiminy o
con el nombre de Jiminy, y aclara que se combina con las habilidades de PDF, Word,
Excel y PowerPoint que trae Claude, no que las reemplaza. `empezar` solo se activa
cuando la persona nombra a Jiminy. Ninguna habilidad de Jiminy reclama pedidos
sueltos fuera de su carpeta: en el chat y en Claude Code, Jiminy no aparece.

## Convenciones para escribir habilidades

- **Encabezado con este formato exacto y nada más:** la línea `name: <nombre>` (igual a
  la carpeta, minúsculas y guiones, hasta 64 caracteres), la línea `description: >` y
  debajo el texto con dos espacios de sangría (hasta 1024 caracteres, sin `<` ni `>`).
  Sin `allowed-tools` ni otras claves.
- **La `description`** dice, en tercera persona, cuándo usarla, con las frases reales
  entre comillas. Las frases que cambian con el trato van también con tú y con usted:
  "resumime / resúmeme / resúmame". Toda habilidad salvo `empezar` aclara que es solo
  "cuando la carpeta de trabajo tiene jiminy.md". Termina con cuándo no usarla.
- **Todo `SKILL.md` empieza, después del título, con este bloque:**

  > **Archivos de Jiminy.** La raíz de Jiminy es la carpeta dos niveles arriba de esta
  > habilidad (`../../` desde la carpeta de este archivo). Si no tenés textuales en
  > esta conversación `../../reglas.md` y `../../referencias/estilo.md`, leelos antes
  > de seguir. Las reglas mandan sobre todo lo demás.

- **Primeros pasos de toda habilidad salvo `empezar`:** (1) comprobar que la carpeta
  de trabajo tiene `jiminy.md`; si no, no hacer nada propio y no mencionar a Jiminy;
  (2) si no está textual en la conversación, leer `yo/perfil.md` (trato y autonomía).
- El cuerpo está escrito como instrucciones para Claude, en español e imperativo. Lo
  que se le dice a la persona va entre comillas y respeta `estilo.md`: seis líneas
  como mucho, una pregunta por vez, sin jerga ni palabras internas, sin asumir género.
- Las referencias a archivos del plugin se escriben relativas a la carpeta de la
  habilidad (`../../referencias/carpeta.md`, `../revisar/SKILL.md`). Nada de rutas
  absolutas ni búsquedas en el disco.
- Cuerpo de menos de 300 líneas. Lo largo va en `skills/<nombre>/referencias/`.
- Los formatos de archivo se citan de `carpeta.md` por su sección; se copia solo la
  línea de formato que el paso necesita.
- **Ningún componente depende de conectores, de internet ni de instalar algo.**
- **Entregables:** archivos dentro de `entregables/` con la extensión que diga la
  habilidad. Para Word, Excel, PowerPoint o PDF, usar las habilidades de documentos
  de Claude que estén disponibles, nombrando la extensión de forma explícita. No crear
  documentos en la nube, páginas publicadas ni artefactos salvo que la persona lo
  pida. Si no hay herramientas para ese formato, el texto va en `.txt` y las tablas en
  `.csv`, y se avisa: "Te lo dejé como texto simple; si lo querés en Word, copialo y
  pegalo ahí." Nunca `.md` para algo que la persona va a abrir.

## Especificación por componente

### `puerta`

**Para qué:** la puerta de entrada. Recibe cualquier pedido dentro de la carpeta de
Jiminy, elige la habilidad de la persona que corresponde y hace la tarea con lo que
Jiminy aprendió.

**Descripción (base):** "Puerta de entrada de Jiminy. Usar SOLO cuando la carpeta de
trabajo tiene jiminy.md en la raíz (lo indican las instrucciones del proyecto o el
CLAUDE.md de la carpeta) o cuando la persona nombra a Jiminy ("Jiminy", "Jimini",
"Yimini", "Pepe Grillo"). En esos casos se usa antes que cualquier otra habilidad, para
cualquier pedido: "resumime este PDF", "contestame este mail", "ordená esta
planilla", "dame ideas para un posteo", "¿qué sabés hacer?". Se combina con las
habilidades de PDF, Word, Excel y PowerPoint; no las reemplaza. No usar en
programación ni en conversaciones sin carpeta de Jiminy."

**Lee**, en una sola tanda de lecturas en paralelo: `indice.md`, `yo/perfil.md`,
`yo/criterios.md`, el `criterios.md` del frente y la versión actual de la habilidad.
De `jiminy.md` solo comprueba que exista y su versión de carpeta. Del registro, solo
las últimas 50 líneas y solo para el paso 11. Reglas y estilo, una vez por
conversación. Tope: ocho lecturas antes de empezar la tarea.
**Escribe:** las líneas del `registro.md` del frente, frases nuevas en el índice (paso
4) y los entregables.

**Pasos:**

1. **Dónde estamos.** Si no hay carpeta de trabajo o no tiene `jiminy.md`: si la
   persona nombró a Jiminy, seguir `empezar` desde su paso 0; si no, no hacer nada
   propio y responder como si esta habilidad no existiera.
2. **Estado de la carpeta.** Si `jiminy.md` tiene una versión de carpeta menor que la
   del contrato, seguir `../../referencias/migraciones.md`. Si falta algo de la
   estructura, seguir `empezar` en modo Reparar. Si no hay `yo/perfil.md`, decir "Nos
   faltó terminar de conocernos. ¿Seguimos ahora?"; si dice que no, hacer la tarea
   con cuidado general.
3. **Qué es el pedido**, en este orden:
   - conversa, agradece o hace una pregunta que se contesta en pocas líneas (una duda,
     una explicación, ideas sueltas) → contestar en la conversación, sin archivo y sin
     registro, aplicando igual la regla 5;
   - corrige o define cómo quiere las cosas → seguir `recordar-criterio`;
   - quiere cambiar cómo hace algo una habilidad, volver a como estaba o dejar de usar
     una → seguir `mejorar-habilidad`;
   - quiere enseñarle algo nuevo → seguir `nueva-habilidad`;
   - quiere un tema nuevo o cambiar algo de lo que Jiminy sabe de ella → seguir `empezar`;
   - pregunta qué sabe hacer → contestar desde el índice, en simple; pregunta qué
     aprendió → seguir `recordar-criterio`, paso de "¿qué aprendiste?";
   - pide algo que Jiminy no puede hacer desde acá (mandar, publicar, mirar otras
     carpetas de la compu, abrir programas, entrar a una página) → decir en una línea
     qué no puede y ofrecer lo que sí: "No puedo mandarlo yo. Te lo dejo listo para
     que lo copies en tu correo." / "Solo veo tu carpeta Jiminy. Si lo ponés en
     Entrada, lo leo.";
   - pide borrar o mover algo → Jiminy no borra: explicar cómo hacerlo desde la carpeta;
   - trae varios pedidos → nombrarlos en una línea y hacerlos de a uno, en el orden
     en que los dijo;
   - es una tarea → paso 4.
4. **Qué habilidad.** Elegir **una** del índice por sus frases y su sentido. Si dudás
   entre dos, una pregunta; con la respuesta, sumar esa frase a la habilidad elegida
   en el índice. Si no hay ninguna, mirar el catálogo de semillas: si una sirve, hacer
   esta tarea con la semilla, completando sus marcas con el perfil y con una pregunta
   como mucho, y después de entregar preguntar: "¿Querés que la próxima vez lo haga
   igual? Lo guardo como tu forma de hacer <tarea en sus palabras>." Si dice que sí,
   seguir `nueva-habilidad` desde la semilla, usando esta tarea como prueba (no se
   vuelve a pedir un ejemplo). Si tampoco hay semilla, hacer la tarea con cuidado general.
5. **Qué tema.** El de la habilidad, o el que corresponda; si no está claro,
   `otras-cosas`. Leer lo aprendido para ese tema. Si dos cosas chocan, seguir el
   orden de `carpeta.md`.
6. **Antes de abrir archivos**, aplicar las reglas 3 y 4. Lo adjuntado o pegado se usa
   directamente; si conviene guardarlo, preguntar antes.
7. **Hacer la tarea** siguiendo la versión actual de la habilidad y lo aprendido, con
   la autonomía del perfil. Si el pedido lee o crea un PDF, Word, Excel o PowerPoint y
   hay una habilidad de documentos de Claude para eso, seguirla para el archivo: qué
   aplicar, el nombre y la carpeta los decide Jiminy.
8. **Antes de entregar**, seguir `revisar`.
9. **Entregar.** Si es un documento (lo pidió como archivo, la habilidad indica un
   formato de archivo o pasa de unas 20 líneas), guardarlo en `entregables/` con el
   nombre del contrato y decir dónde quedó con el lugar de `jiminy.md`. Si no, en la
   conversación. Si el formato es "en la conversación para copiar", mostrarlo ahí.
10. **Correcciones.** Si la persona corrige algo, seguir `recordar-criterio` y volver acá.
11. **Al terminar** (después de la última corrección), agregar la línea del registro.
    Después, como mucho una de estas ofertas, en este orden:
    - si la habilidad viene de una semilla con una versión más nueva en el plugin y el
      registro no tiene ` · nota: ofrecí semilla <carpeta> versión <N>`, ofrecer una vez
      comparar con `mejorar-habilidad` y agregar esa nota;
    - si en el registro hay dos `corregido` seguidos con la misma versión de una
      habilidad, ofrecer cambiarla con `mejorar-habilidad`;
    - si en las últimas 50 líneas hay tres o más tareas parecidas `sin habilidad` y
      ninguna nota de que no quiso, proponer una vez crear una con `nueva-habilidad`;
      si dice que no, agregar ` · nota: no quiso crear una habilidad para esto`.

**Aceptación:** con una carpeta armada, "resumime este PDF" usa la habilidad correcta,
lee lo aprendido, pasa por `revisar`, guarda `_v1` sin pisar nada y anota el registro
con la versión, la entrada y el entregable. "Gracias" no genera archivo ni registro.
Fuera de una carpeta de Jiminy no hace nada ni menciona a Jiminy. Nunca nombra
habilidades por su carpeta ni usa palabras internas.

### `empezar`

**Para qué:** la primera vez, y volver para retomar, sumar un tema, cambiar algo de lo
que Jiminy sabe de la persona, reparar la carpeta o actualizarla.

**Descripción (base):** "Usar cuando la persona nombra a Jiminy para empezar o
configurarlo ("Jiminy, empecemos", "empezar con Jiminy", "configurame Jiminy", "Pepe
Grillo, arranquemos", "Jiminy, sigamos", "ya creé el proyecto"), o cuando la carpeta
de trabajo ya tiene jiminy.md y dice "empecemos", "sigamos", "quiero usarte también
para…", "agregá un tema" o "revisemos lo que sabés de mí". Sin jiminy.md, las frases
que no nombran a Jiminy no cuentan."

**Escribe:** `jiminy.md`, `CLAUDE.md`, `indice.md` (frentes y pendientes),
`yo/perfil.md`, `yo/criterios.md`, los frentes (`criterios.md` y `registro.md`) y
las carpetas `entrada/`, `entregables/`, `privado/` y `frentes/otras-cosas/`.

**Paso 0 (siempre).** Si la carpeta no tiene `jiminy.md` y la persona no nombró a
Jiminy, no hacer nada. Si la carpeta ya tiene `jiminy.md`, el perfil está completo y
el pedido es una tarea (no empezar, retomar, sumar un tema ni cambiar el perfil),
seguir `puerta`. Si no hay carpeta de trabajo, o la carpeta no tiene `jiminy.md`,
preguntar primero, con opciones: "Es la primera vez que uso Jiminy" / "Ya tengo mi
carpeta de Jiminy".
- **Ya la tiene:** "Tus cosas están en el proyecto Jiminy. Buscalo en la lista de
  proyectos ("Projects"), abrí una conversación ahí y escribime: Jiminy, sigamos."
  Si la movió de lugar, guiar a elegir de nuevo esa carpeta para el proyecto
  [confirmar en Fase 0]. Si está en otra compu: "Lo que aprendí está en la carpeta de
  la otra compu y no viaja solo. Podemos seguir allá o armar una carpeta nueva acá."
  Nunca crear una carpeta nueva sin esta respuesta.
- **Primera vez:** modo Primera vez.

**Modo Primera vez:**

1. **Apertura** (solo si es la primera conversación): tres líneas sobre qué va a
   pasar y cuánto tarda ("entre media hora y una hora; podemos cortar cuando quieras y
   seguimos donde quedó"); después "¿Arrancamos?".
2. **Proyecto y carpeta.** Si la conversación no está dentro de un proyecto con una
   carpeta (si no se puede saber, preguntar una vez: "¿Abriste esta conversación
   adentro del proyecto Jiminy?"), no crear nada. Preguntar con opciones reconocibles:
   "¿Tu compu es una Mac, de Apple, o es de otra marca, como Lenovo, HP o Dell?".
   Guiar a crear el proyecto con una carpeta nueva y vacía llamada "Jiminy" en
   Documentos (`skills/empezar/referencias/proyecto.md`), de a un paso por mensaje,
   cada uno con las opciones "Listo" / "No lo encuentro". Cerrar con: "Listo. Ahora
   abrí una conversación nueva dentro del proyecto Jiminy y escribí: Jiminy, sigamos.
   Ahí sigo yo." y no hacer nada más en esta conversación.
   - En la conversación nueva (carpeta sin `jiminy.md` y la persona nombrando a
     Jiminy): saltear la apertura ("Ya estamos en tu carpeta. Sigo desde acá.").
   - Si la carpeta ya tiene archivos y no es de Jiminy: no crear nada, no listar ni
     abrir lo que tiene. "Esta carpeta ya tiene tus cosas. Para no mezclarlas,
     armemos una carpeta nueva solo para Jiminy." y guiar a crear el proyecto con una
     carpeta nueva y vacía.
3. **Crear la estructura**, avisando en dos líneas y confirmando el nombre de la
   carpeta: primero `jiminy.md` y `CLAUDE.md`, después `indice.md`, `yo/`, `entrada/`,
   `entregables/`, `privado/` y `frentes/otras-cosas/`. Comprobar listando la raíz que
   quedó todo. Completar en `jiminy.md` el lugar y la compu.
4. **Privacidad**, en dos líneas: lo que lee Jiminy se procesa en los servidores de
   Anthropic, y dónde está el ajuste de privacidad (`skills/empezar/referencias/privacidad.md`).
5. **Entrevista** (`skills/empezar/referencias/entrevista.md`), con las preguntas
   fijas y en este orden; cada una acepta "Prefiero no decirlo":
   1. "¿Cómo querés que te llame?"
   2. "¿A qué te dedicás?"
   3. Lo que nunca entra, con una propuesta según la respuesta anterior: "Por lo que
      me contás, propongo que nunca entren datos de tus pacientes, como el nombre
      junto a lo que tienen. ¿Agregarías algo?"
   4. "Además de eso, ¿para qué más te gustaría usarme? Por ejemplo: trámites, cosas
      de la casa, redes."
   5. "Contame qué hiciste el lunes pasado, o en un día común, sin nombres de otras personas."
   6. "¿Qué tarea te lleva más tiempo y es casi siempre igual?"
   7. "¿Qué archivo o mensaje armás todas las semanas?"
   8. Autonomía, con opciones: "Cuando te prepare algo, ¿preferís que te consulte en
      cada paso o que lo haga entero y te lo muestre?" (si no sabe: pregunta antes de
      cada paso).

   El trato no se pregunta: se deduce de cómo escribe. El tono y el formato se
   preguntan en la primera habilidad, con opciones. Ante "no sé", ofrecer dos o tres
   ejemplos una sola vez; si sigue sin saber, "todavía no lo sé". Después de cada
   respuesta, agregar en Pendiente la línea `- Entrevista: <dato> = <respuesta corta>`
   sin anunciarlo. Si no quiere entrevista ("vamos al grano"), preguntar solo el
   nombre y lo que nunca entra, escribir un perfil mínimo y pasar a: "¿Tenés algo
   para hacer hoy? Lo hacemos y voy aprendiendo." La primera tarea define la primera habilidad.
6. **Resumen y confirmación.** Recién ahí escribir `yo/perfil.md`, los temas (como
   mucho tres además de Otras cosas; el resto a Pendiente) con sus carpetas, y borrar
   las líneas `Entrevista:` de Pendiente.
7. **Habilidades.** Proponer dos o tres desde el catálogo de semillas, con nombres en
   sus palabras. Para la que va a usar primero, seguir `nueva-habilidad` desde la
   semilla: la prueba del borrador **es** la primera tarea real (paso 8). Para las
   otras, como mucho las dos primeras preguntas de su semilla; escribir `v1.md` con
   reglas razonables para lo que falte y "sin probar todavía" en su historial. Tope de
   la primera sesión: 15 preguntas en total, contando la entrevista y las semillas
   (no cuentan los "Listo / No lo encuentro").
8. **Primera tarea real.** Pedirle un archivo suyo: puede arrastrarlo a esta
   conversación o a la carpeta Entrada. Si no tiene ninguno a mano, un texto que pegue
   o escriba. Hacerla como la haría `puerta` (revisar, entregar, registrar).
9. **Instrucciones del proyecto.** Mostrar el texto de
   `../../plantillas/instrucciones-proyecto.md` solo, para copiar, y guiar de a un
   paso dónde pegarlo (Mac: Cmd+V; Windows: Ctrl+V; o clic derecho y "Pegar"). Si se
   complica, saltearlo y anotar en Pendiente `- Pegar las instrucciones del proyecto`.
10. **Cierre:** qué quedó armado, cómo pedir cosas, cómo enseñarle algo nuevo, que si
    algo no le gusta lo diga, dónde encontrarlo ("La próxima vez abrí el proyecto
    Jiminy y escribime ahí; si me escribís en otro lado, no tengo tus cosas.") y cómo
    deshacer ("Si un cambio no te gusta, decime: volvé a como estaba."). Si saltó las
    instrucciones: "Si alguna vez te contesto sin acordarme de tus cosas, empezá el
    mensaje con la palabra Jiminy."

**Otros modos:**

- **Retomar** (hay `jiminy.md` y falta el perfil o hay algo en Pendiente): mostrar en
  una línea lo que ya sabe y seguir con lo próximo que falte.
- **Sumar un tema:** dos preguntas como mucho, crear la carpeta del tema con su
  `criterios.md` y su `registro.md`, agregarlo al índice y ofrecer una semilla.
- **Cambiar el perfil:** mostrar en simple lo que sabe de ese dato, preguntar qué
  cambió y escribir solo eso, después de confirmarlo. Lo usa también
  `recordar-criterio` cuando una corrección cambia un dato del perfil.
- **Reparar:** crear solo lo que falta según *Si falta algo o no coincide* de
  `carpeta.md`, contarlo en una línea y volver a lo que se estaba haciendo.

**Referencias propias:**

- `skills/empezar/referencias/entrevista.md`: las preguntas, cómo reconocer las
  respuestas, cómo pasar de las respuestas al perfil y a los temas, y cómo elegir
  semillas.
- `skills/empezar/referencias/proyecto.md`: crear el proyecto y pegar las
  instrucciones, en Mac y en Windows, de a un paso, con qué hacer si no lo encuentra.
- `skills/empezar/referencias/privacidad.md`: las dos líneas sobre privacidad y
  respuestas de dos líneas a "¿quién ve esto?", "¿lo usan para entrenar?" y "¿lo
  puedo borrar?", sin afirmar nada que no esté confirmado.

Todo lo que depende de cómo se ve Cowork se marca "[confirmar en Fase 0]".

**Aceptación:** una persona sin experiencia termina con la carpeta armada, lo que
Jiminy sabe de ella confirmado, dos o tres habilidades y un entregable real, sin más
preguntas que el tope y sin hacer nada técnico por su cuenta: crear el proyecto, pegar
un texto y poner un archivo los hace siguiendo los pasos de Jiminy, de a uno. Si corta
en cualquier punto, en la conversación siguiente sigue donde quedó.

### `nueva-habilidad`

**Para qué:** crear una habilidad de la persona, desde una semilla o desde cero.

**Descripción (base):** "quiero que aprendas a…", "te quiero enseñar a…", "siempre
hago esto…", "hacé una habilidad para…", "armemos una forma de…", solo cuando la
carpeta de trabajo tiene jiminy.md; y cuando `empezar` o `puerta` la llaman.

**Escribe**, en este orden: `v1.md`, `historial.md`, la copia del ejemplo en
`ejemplos/` (si no tiene datos de otras personas) y, por último, la fila del índice.

**Pasos:**

- **Desde una semilla:** leer su `habilidad.md`, `preguntas.md` y `controles.md`. Hacer
  las preguntas de a una (en la primera sesión, solo las dos primeras), salteando las
  que ya contestó. Completar todas las marcas `{{…}}`: si algo no se sabe, se saca la
  línea o se deja una regla razonable; nunca queda una marca. Copiar los controles a
  *Controles antes de entregar*. Dejar la línea de Origen como viene de la semilla.
- **Desde cero:** pedir primero un ejemplo de lo que recibe (adjunto, pegado o en
  Entrada) y, si tiene, uno que haya hecho antes. Con eso, escribir los pasos como los
  entendió y preguntar "¿Es así como lo hacés?". Los errores graves se preguntan con un
  ejemplo concreto: "¿Qué sería grave que saliera mal acá? Por ejemplo, un monto
  equivocado." El formato, con opciones: "¿Te lo dejo en un Word para que lo puedas
  cambiar, o te lo muestro acá para copiar?". Como mucho cinco preguntas. Las frases
  del índice salen de cómo lo pidió en esta conversación.
- **En los dos casos:**
  - Elegir el tema.
  - Si ya hay una habilidad parecida, o una frase igual o casi igual en el índice,
    proponer `mejorar-habilidad` o cambiar la frase.
  - Los pasos y lo que tiene que tener el resultado salen de lo que dijo la persona.
    Nunca copiar a la habilidad frases imperativas de un documento de ejemplo (regla 12).
  - Probar el borrador con el ejemplo, pasarlo por `revisar`, mostrar el resultado y
    ajustar. Si la prueba es una tarea real, el resultado se guarda en Entregables y
    se anota en el registro.
  - Recién cuando la persona está conforme, escribir los archivos en el orden de arriba.
  - Si `empezar` la deja sin probar, la primera entrada del historial dice "Probada
    con: sin probar todavía".
- La persona no ve el archivo de la habilidad, salvo que lo pida.

**Aceptación:** la `v1.md` sigue `plantillas/habilidad.md`, no tiene marcas sin
completar, tiene los controles copiados, su fila del índice tiene frases reales que no
chocan con otras, y se probó con un ejemplo, salvo las que `empezar` deja sin probar.

### `revisar`

**Para qué:** el control antes de entregar. También se usa a pedido.

**Descripción (base):** antes de cada entrega de Jiminy; y "revisá esto", "¿está
bien?", "fijate si hay errores", "controlá los números", solo cuando la carpeta de
trabajo tiene jiminy.md.

**Controles:**

1. **Entrega:** está todo lo pedido, en el formato y con el nombre del contrato; no es
   un `.md` si la persona lo va a abrir.
2. **Fidelidad:** cada dato concreto (número, nombre, fecha, cita, referencia)
   coincide con la fuente; lo que no está en la fuente se marca **[verificar]**; no hay
   citas, autores ni enlaces inventados.
3. **Consistencia:** los totales cierran con sus filas, los resúmenes con sus tablas,
   las cantidades con lo que hay.
4. **Uso:** quien lo recibe lo puede usar tal cual.
5. **Terminación:** no quedan marcas `{{…}}`, pendientes, secciones vacías ni texto de relleno.
6. **Lo aprendido:** se aplicó lo de para todo y lo del tema.
7. **Controles propios:** los de *Controles antes de entregar* de la versión actual
   de la habilidad. Nunca leer el `controles.md` de una semilla.
8. **Privacidad:** no se copiaron datos de otras personas al entregable ni al nombre
   del archivo.

Si algo falla: arreglarlo y, si importa, decirlo en una línea; si no se puede
arreglar, decirlo con claridad. Nunca esconderlo. Cuando revisa un archivo de la
persona a pedido, nunca lo modifica: entrega las observaciones o una copia corregida
en Entregables.

**Aceptación:** detecta un total que no cierra, una cita que no está en la fuente, una
marca sin completar y un nombre de paciente en el nombre del archivo.

### `recordar-criterio`

**Para qué:** que Jiminy aprenda de cada corrección sin llenarse de ruido.

**Descripción (base):** "no, así no", "no me gusta", "más corto", "siempre que…",
"nunca…", "acordate que…", "la próxima vez…", "prefiero…"; "olvidate de…", "ya no
hagas…"; "¿qué aprendiste de mí?", solo cuando la carpeta de trabajo tiene jiminy.md.
Toda corrección entra por acá.

**Escribe:** solo los archivos de criterios (vigentes y archivados).

**Pasos:**

1. Si la corrección no dice qué cambiar ("no me gusta"), preguntar solo eso: "¿Qué le cambiarías?".
2. **Aplicar la corrección enseguida** y mostrar el resultado.
3. **En ese mismo mensaje, una sola pregunta** para guardarla, con el alcance ya
   propuesto: "Lo dejé más corto. ¿Querés que los posteos de Instagram sean siempre
   así de cortos?". El alcance se pregunta aparte solo si no se puede deducir. Si la
   corrección es claramente de este caso ("este más corto porque es una historia"), no
   proponer guardarla.
4. **Filtro de datos del caso:** si es un dato de esta tarea ("este mes la consulta
   cuesta X"), no va a la memoria permanente. Nunca se guardan datos de otras
   personas, contraseñas ni datos de salud de nadie. Solo se guarda lo que la persona
   escribió en la conversación (regla 12).
5. **Perfil, habilidad o criterio:** si cambia un dato del perfil (nombre, trato,
   idioma, autonomía, formato preferido, tono, lo que nunca entra), seguir `empezar`
   en modo Cambiar el perfil solo para ese dato. Si cambia cómo hace algo una
   habilidad siempre, proponer `mejorar-habilidad` en lugar de guardar un criterio suelto.
6. **Duplicados y choques:** si ya hay uno parecido, archivar el viejo y guardar el
   nuevo; si se contradicen, preguntar cuál vale.
7. Con el sí, guardarlo con la fecha y el ejemplo (en genérico) y decir en una línea
   qué aprendió.
8. **Presupuesto:** seguir los límites de `carpeta.md`. Si en un tema hay tres o más
   criterios que solo aplican a una misma habilidad, proponer una vez
   `mejorar-habilidad` para incorporarlos; si elige la nueva, archivarlos con el motivo
   "pasó a <habilidad> v<N>".
9. **"Olvidate de…":** pasarlo a los archivados con el motivo. Si la memoria del
   proyecto lo recuerda, decirle en simple dónde borrarlo [confirmar en Fase 0, prueba 5].
10. **"¿Qué aprendiste?":** listar lo vigente en simple, por tema.

**Aceptación:** "acordate que siempre firmo como Dra. X" queda como criterio para
todo; "este paciente se llama Y" no se guarda; "los resúmenes de paper tienen que
traer el tamaño de la muestra" propone `mejorar-habilidad`; "tratame de usted" cambia
el perfil; "más corto" se aplica antes de preguntar nada.

### `mejorar-habilidad`

**Para qué:** cambiar una habilidad probando la forma nueva contra la actual, volver
atrás y dejar de usar una.

**Descripción (base):** "cambiá cómo hacés…", "probá si queda mejor…", "volvé a como
estaba antes", "deshacé el cambio", "usá la versión anterior", "¿qué le cambiaste
a…?", "ya no uses…", "borrá la habilidad de…", solo cuando la carpeta de trabajo tiene
jiminy.md; y cuando la llaman `puerta` o `recordar-criterio`.

**Escribe:** la versión nueva, `ejemplos/`, `pruebas/`, el historial y, en el índice,
la versión actual, las frases y las archivadas.

**Pasos para mejorar:**

1. Identificar la habilidad por el índice y leer la versión actual.
2. **Un cambio por vez.** Si pide varios, sugerir de a uno; si prefiere todos juntos,
   el veredicto será "no se puede saber".
3. **Ejemplo**, en este orden: el que indique la persona; el último `entrada:` del
   registro con esa habilidad que siga en Entrada; el más nuevo de `ejemplos/`. Si no
   hay ninguno, pedirle uno o adoptar la versión nueva sin comparar.
4. **Resultado de la versión actual:** si el registro tiene el entregable de ese
   ejemplo con la versión actual y la persona no lo corrigió, usarlo, porque se hizo
   antes de conocer el cambio. Si no, hacer la tarea con la versión actual **antes** de
   escribir la nueva. Si hay una herramienta para delegar en un ayudante
   independiente, darle a cada versión su ayudante con solo esa versión, lo aprendido y
   el ejemplo.
5. **Versión nueva:** escribir `v<M+1>.md`, donde M es el número más alto que existe en
   la carpeta de la habilidad (no la versión actual), aplicando el cambio sobre la
   versión actual. Comprobar que no contradice las reglas.
6. Hacer la tarea con la versión nueva. Las dos pasan por `revisar`. Guardar los dos
   resultados y la clave en `pruebas/`. A es la nueva si la cantidad de archivos
   `_clave.md` que ya hay es par; si no, A es la actual.
7. **Mostrar:** "Lo hice de las dos formas con el mismo ejemplo. No te digo cuál es la
   nueva para que elijas sin que eso pese." Mostrar A y B en la conversación, completas
   o, si son largas, el mismo fragmento de cada una; nunca un resumen escrito por
   Jiminy. Si son archivos, mostrar su contenido como texto. Nunca mandar a la persona
   a buscar en `pruebas/`. Durante la comparación no decir "nueva" ni "anterior".
   Preguntar: "¿Cuál te sirve más, A o B?". Si pregunta cuál es cuál, decírselo y anotarlo.
8. **Veredicto:** elige la nueva → "ayudó", pasa a ser la actual. Elige la actual →
   "empeoró", no cambia nada. "Me da igual" → "sin diferencia", queda la actual.
   "Ninguna" → "empeoró", queda la actual y se pregunta qué le falta. Si fueron varios
   cambios juntos, no hubo ejemplo o viene de una semilla nueva → "no se puede saber",
   elija lo que elija.
9. Escribir la entrada del historial una sola vez, completa, y actualizar el índice.

**Desde una semilla nueva:** aplicar sobre la versión actual de la persona los
cambios de `## Cambios` del `origen.md` de la semilla entre su versión y la nueva, de a
uno si la persona quiere, y comparar como arriba. Actualizar la versión de la semilla
en la fila del índice.

**Pasos para volver atrás:** contar en simple las versiones, con su fecha y lo que
cambió cada una (del historial); la persona elige; cambiar la versión actual en el
índice; escribir la entrada "volvió a vN". Nunca se borra una versión.

**Pasos para dejar de usar:** pasar la fila a *Archivadas* con fecha y motivo, sin
borrar la carpeta, y escribir la entrada en el historial. Para volver a usarla,
devolver la fila.

**Aceptación:** después de un cambio hay `v2.md`, dos resultados y la clave en
`pruebas/`, una entrada completa en el historial y el índice apunta a la versión
elegida; "volvé a como estaba" deja el índice en `v1` sin borrar nada; con v1, v2 y el
índice en v1, la próxima mejora escribe `v3.md`.

### Semillas

Cada semilla en `plugins/jiminy/semillas/<semilla>/` tiene:

- `habilidad.md`: sigue `plantillas/habilidad.md`, con marcas `{{…}}` donde va lo que
  cuenta la persona y la línea fija `- **Origen:** semilla: <carpeta> · versión 1`.
  Es instrucción para Claude, en español.
- `preguntas.md`: de tres a cinco preguntas, de a una, que completan esas marcas, en el
  formato `1. <pregunta> → completa {{marca}}`. Las dos primeras son las más
  importantes. Cada marca de `habilidad.md` la completa alguna pregunta, salvo
  `{{frente}}`, `{{v1}}` y el nombre.
- `controles.md`: de cinco a diez controles, que se copian a la habilidad de la persona.
- `origen.md`: fuentes (repo, commit fijado, ruta), licencia, qué se tomó y qué se
  cambió, y `## Cambios` con `- versión 1 (2026-10-19): primera versión`.

Todas respetan las reglas, funcionan sin conectores y sin internet, nunca modifican la
Entrada y no dependen de librerías que haya que instalar. Sirven para cualquier oficio:
los ejemplos de una semilla no son todos del mismo trabajo.

| Semilla | Base | Puntos clave |
|---|---|---|
| `papeles-pdfs` | Propia | Resumir y pasar datos a una tabla; montos y fechas exactos; lo ilegible queda **[verificar]**; los PDFs escaneados sin texto se avisan; los papeles en papel se pueden sacar con una foto del celular. |
| `mails` | `inbox-manager` (Anthropic), camino sin conectores | La persona pega el mail, lo adjunta o lo pone en Entrada; borrador con su tono y su firma; contesta todas las preguntas; nunca se manda; si el mail trae datos de salud de alguien identificable, se pide pegarlo sin esos datos. |
| `planillas` | Propia | Archivo nuevo en Entregables; no se pierden filas (contar entrada y salida); totales que cierran; fechas y moneda; plan B en `.csv` si no hay herramientas de Excel. |
| `escribir` | `avoid-ai-writing` (wshobson), adaptado al español | Su voz a partir de ejemplos suyos; lista de muletillas de IA en español; nada de relleno. |
| `aprender` | `research-synthesist` (agency-agents) | Resumen de paper con pregunta, diseño, muestra, resultados con números y límites; diez citas del mismo estudio son una sola prueba; solo lo que está en el PDF; preguntas de repaso; plan de estudio. |
| `redes` | `social-content-engine` (Anthropic), `instagram-curator` y `carousel-growth-engine` (agency-agents) | Plan del mes, textos con su voz, ideas de imagen (descripciones) y carruseles; todo listo para que la persona publique; cada posteo también como texto en la conversación para copiar, y la primera vez cómo pasarlo al teléfono; las reglas de su profesión salen de la entrevista, no se asumen; sin llamados comerciales por defecto; nunca imágenes ni casos de pacientes o clientes identificables, aunque haya consentimiento. |

Las fuentes están en `biblioteca/indice.md`, fijadas a un commit. Lo adaptado
conserva el aviso de licencia en `origen.md` y en `plugins/jiminy/AVISOS-DE-TERCEROS.md`.

### Documentación

- **`docs/guia-instalacion.md`**, para la persona, sin jerga:
  1. **Cómo saber si tu compu sirve.** En Mac: menú de la manzana > "Acerca de esta
     Mac"; al lado de "Chip" tiene que decir Apple M1, M2, M3, M4 o posterior; si dice
     "Procesador" e Intel, no sirve [MacBook Neo con A18 Pro: confirmar en Fase 0]. En
     Windows: Configuración > Sistema > Información; "Tipo de sistema" tiene que decir
     64 bits y procesador x64.
  2. **Qué plan hace falta:** Pro o superior (el gratis no trae Cowork).
  3. Instalar Claude y entrar.
  4. Agregar Jiminy: "Customize" > "Plugins" > "Add marketplace" con
     `matias-gentile/jiminy`, instalar "Jiminy" y activar "Sync automatically".
  5. Crear el proyecto "Jiminy" con una carpeta nueva y vacía en Documentos (fuera de
     iCloud u OneDrive si se puede [confirmar en Fase 0]).
  6. Dentro del proyecto, escribir "Jiminy, empecemos".
  7. Privacidad, qué hacer si algo no anda (incluido el aviso de límite de uso: "no se
     rompió nada; esperá la hora que indica y escribí Jiminy, sigamos") y cómo quitarlo.
- **`docs/piloto.md`**, para Matías: antes (Fase 0 completa; sacar `jiminy-prueba` del
  catálogo y borrar `plugins/jiminy-prueba/` antes de dar la guía), durante la primera
  sesión (qué observar, cuándo ayudar y anotar cada ayuda), las dos semanas, qué
  juntar (registro, historial, criterios, entregables), las preguntas del cierre y
  cómo traer los resultados.
- **`docs/escenarios.md`**: escenarios de aceptación para correr en Cowork después de
  la Fase 0. Cada uno con preparación, qué decir, qué tiene que pasar, qué no tiene que
  pasar y qué archivos tienen que quedar.

### Herramientas

- **`scripts/validar.py`** (solo biblioteca estándar): manifiestos JSON válidos; cada
  plugin del catálogo existe; cada `SKILL.md` con el encabezado exacto, `name` igual a
  su carpeta y `description` dentro de los límites; las rutas del plugin que nombran
  las habilidades existen, resueltas desde la carpeta de cada habilidad; nombres de
  archivo válidos en Windows; cada semilla tiene sus cuatro archivos, las secciones de
  la plantilla, su línea de Origen con versión y `## Cambios`; no quedan marcas `{{…}}`
  fuera de plantillas y semillas; los contratos que se leen siempre no pasan de un
  tamaño; límites de Cowork. Sale con error si algo falla.
- **`.github/workflows/validar.yml`**: corre el validador en cada push y pull request.
- **`CLAUDE.md`**: cómo trabajar en este repo.
- **`biblioteca/fuentes.json`**, **`scripts/revisar_fuentes.py`** y
  **`docs/actualizar-biblioteca.md`**: la actualización de la biblioteca, para activar
  después del piloto.

## Cómo cubre cada duda de la Fase 0

| Duda | Cómo se cubre en esta versión |
|---|---|
| 1. MacBook Neo | Nada del plugin depende de la compu. La guía explica cómo ver el chip. Si Cowork no corre ahí, el plan B se diseña con los resultados. |
| 2. Escribir y leer en la carpeta | Todo vive en archivos de la carpeta; `empezar` comprueba que `jiminy.md` quedó en la carpeta que ve la persona. |
| 3. Activación | Tres capas: instrucciones del proyecto, `CLAUDE.md` en la carpeta y el nombre "Jiminy". |
| 4. Archivos del plugin | Rutas relativas `../../`, como en los plugins de Anthropic, y `${CLAUDE_PLUGIN_ROOT}` de respaldo. Sin búsquedas en el disco. |
| 5. Memoria nativa | Regla 13: valen los archivos. Las instrucciones lo dicen. |
| 6. Librerías de la máquina | Las habilidades de documentos de Claude y un plan B en `.txt` y `.csv`. |
| 7. Privacidad | `empezar` lo explica y marca la ubicación exacta del ajuste como "[confirmar en Fase 0]". |
| 8. Actualizaciones | La guía pide activar "Sync automatically". |
| 9. Windows | Nombres de archivo con `a-z`, `0-9` y guiones (lo controla el validador) y guías para los dos sistemas. |

## Verificación

1. **Validador** en cada cambio.
2. **Revisión independiente** de cada componente, contra la especificación, los
   contratos, el estilo y las reglas, con corrección en el lugar.
3. **Simulaciones de punta a punta** con tres personas inventadas: una médica que
   también maneja su Instagram, un contador independiente que desconfía de la
   tecnología y una jubilada que quiere ordenar papeles y escribirle a la familia.
   Siguen las habilidades al pie de la letra en una carpeta de prueba. Una simulación
   falla si:
   - la primera sesión pasa de 15 preguntas;
   - un mensaje de Jiminy (sin contar resultados) pasa de seis líneas o trae dos preguntas;
   - aparece una palabra de la columna "No" de `estilo.md` fuera de los nombres de pantalla;
   - se le pide algo técnico que no está en la aceptación de `empezar`;
   - queda en la carpeta el nombre de otra persona;
   - un archivo no sigue el contrato.

   Cada simulación anota cuántos intercambios tuvo la primera sesión.
4. **Crítica de seguridad y privacidad** sobre todo el plugin.
5. **Escenarios en Cowork** (`docs/escenarios.md`) después de la Fase 0, a cargo de Matías.

## Fuera de esta etapa

- Correr la Fase 0 y el piloto: los hace Matías en Cowork.
- Activar la tarea semanal de la biblioteca: después del piloto (decisión 11).
- Conectores, publicar automáticamente y datos de pacientes (ver *Fuera de alcance*
  en `docs/diseno.md`).
