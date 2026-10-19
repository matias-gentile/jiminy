# Estado del desarrollo

Fecha: 2026-10-19 · Rama: `jiminy-0.1`

Para retomar el trabajo. El diseño está en `docs/diseno.md` y la especificación de
cada componente, en `docs/plan-desarrollo.md`.

## Hecho

- **Contratos compartidos**, revisados por tres críticos independientes y corregidos:
  `plugins/jiminy/reglas.md`, `referencias/` (carpeta, estilo, rutas, semillas,
  migraciones) y `plantillas/`.
- **Plan de desarrollo** con la especificación y la aceptación de cada componente.
- **Las seis habilidades del núcleo**, escritas según el plan:
  `puerta`, `empezar` (con `referencias/entrevista.md`, `proyecto.md` y
  `privacidad.md`), `nueva-habilidad`, `mejorar-habilidad`, `revisar` y
  `recordar-criterio`.
- **Validador** (`scripts/validar.py`) e integración continua (`.github/workflows/validar.yml`).
- **Guía para desarrollar** (`CLAUDE.md`).
- **Herramientas de la biblioteca** para la Fase 5, sin activar:
  `biblioteca/fuentes.json`, `scripts/revisar_fuentes.py` y `docs/actualizar-biblioteca.md`.
- **Licencia y avisos de terceros** dentro del plugin.
- **Fase 0:** el protocolo (`docs/fase-0.md`) y el plugin de prueba (`plugins/jiminy-prueba/`),
  que ya están en `main`.

## Falta

En este orden:

1. **Revisión independiente de las seis habilidades.** Las escribió un agente cada una
   y todavía no las revisó otro. Revisar cada una contra su sección del plan, el
   contrato `carpeta.md`, las trece reglas y `estilo.md`, y recorrer a mano su caso de
   aceptación.
2. **Resolver los problemas que reportaron los agentes** (abajo) y actualizar los
   contratos o el plan donde haga falta.
3. **Las seis semillas** (`plugins/jiminy/semillas/`), según la sección *Semillas* del
   plan. Las fuentes están fijadas en `biblioteca/fuentes.json`. Hasta que existan, el
   validador falla porque `referencias/semillas.md` y `AVISOS-DE-TERCEROS.md` las nombran.
4. **`docs/guia-instalacion.md` y `docs/piloto.md`**, según *Documentación* en el plan.
5. **Simulaciones de punta a punta** con las tres personas inventadas y sus criterios
   de falla (*Verificación* en el plan), y corregir lo que aparezca.
6. **`docs/escenarios.md`**, los escenarios de aceptación para Cowork.
7. Actualizar `docs/diseno.md`, el `README.md` y los estados de `biblioteca/indice.md`.
8. **Correr la Fase 0 en Cowork** y ajustar lo marcado "[confirmar en Fase 0]".

Para instalar Jiminy desde Cowork, el catálogo se lee de `main`. Hasta unir esta rama,
en Cowork solo aparece lo que ya está en `main`: el plugin de prueba de la Fase 0.

## Problemas que reportaron los agentes que escribieron el núcleo

Cada agente resolvió estos casos de alguna forma dentro de su habilidad, pero el
contrato o el plan no los dicen, y conviene fijarlos en un solo lugar.

### Quién escribe el registro y los pendientes

- El contrato dice que solo `puerta` escribe `registro.md`, pero `empezar` (primera
  tarea), `nueva-habilidad` (prueba con una tarea real) y `revisar` (copia corregida a
  pedido) también terminan tareas. Hoy cada una "sigue el paso 11 de `puerta`". Conviene
  que el contrato diga que cualquier habilidad puede seguir ese paso, o sumarlas a la tabla.
- La línea del registro se escribe "después de la última corrección". Si la persona
  cierra la conversación sin contestar, la tarea no queda anotada. Propuesta: escribir
  `entregado` al entregar y, si corrige, agregar otra línea con `corregido`.
- El registro no tiene un valor de `entrada:` para una tarea sin fuente (hoy se usa
  `pegado`) ni de `entregable:` para una tarea frenada.
- Agregar una nota al final de una línea ya escrita no está permitido explícitamente.
  Hoy `puerta` la agrega. También inventó la nota ` · nota: no quiso cambiar <habilidad> v<N>`.
- La línea `- Crear habilidad:` de Pendiente la borran tanto `empezar` como
  `nueva-habilidad`. Hace falta un solo dueño.
- `- Pegar las instrucciones del proyecto` se anota al crear la estructura y se borra
  al pegarlas. El plan dice que se anota solo si se saltean.
- En Pendiente, `frente:` lleva la carpeta completa (`frentes/consultorio`). El contrato
  no lo aclara.

### Reparaciones

- *Si falta algo o no coincide*, puntos 3 a 5, no dice quién escribe la reparación
  cuando la detecta `puerta`: el historial es de `mejorar-habilidad` y del índice
  `puerta` solo agrega frases. Hoy: `nueva-habilidad` tiene *Registrar una que ya
  existe*, y una habilidad sin ninguna versión se recrea en una carpeta nueva.
- Avisar "la primera vez" que aparece algo ajeno en la raíz no tiene dónde quedar
  anotado. Hoy no se avisa: solo no se toca.

### Historial y comparaciones

- `Probada con:` no tiene valor para un ejemplo que tenía datos de otras personas y
  no se copió. Hoy: descripción genérica más "(sin copia: tenía datos de otras personas)".
- `Eligió:` no tiene valor para "adoptar sin comparar" (hoy: "la nueva, sin comparar")
  ni para anotar que la persona supo cuál era cuál (hoy: "(supo cuál era cuál)").
- Faltan los títulos fijos de "dejó de usarse" y "volvió a usarse". Hoy se usan esos mismos.
- Si la persona deja la elección A/B para otro día, la entrada no se escribe y la
  versión nueva queda sin usarse. No hay formato para dejar rastro.
- La tabla *Archivadas* pierde las frases, el origen y la versión actual. Conviene
  guardarlos ahí.
- `mejorar-habilidad` necesita cambiar la columna Origen del índice cuando adopta una
  semilla nueva; la tabla del contrato no se lo permite.
- El formato de criterio archivado pisa la fecha y el ejemplo originales.

### Activación y lectura

- El tope de ocho lecturas de `puerta` no alcanza con la versión del contrato
  (`carpeta.md` es largo) y el catálogo de semillas. Conviene llevar la versión del
  contrato a un lugar liviano. Además, `puerta` lee de `jiminy.md` el lugar y la compu,
  no solo la versión.
- `puerta` no manda "revisá esto" a `revisar`: hay que sumar esa rama a su paso 3.
- Si la persona dice "Jiminy, sigamos" en una carpeta sin perfil, `puerta` pregunta
  "¿Seguimos ahora?". Conviene que `puerta` mande primero a `empezar` los pedidos de
  empezar o retomar.
- El cierre del paso 2 de `empezar` ("escribí: Jiminy, sigamos") es la misma frase que
  se le da a quien ya tiene carpeta, y en la conversación nueva vuelve a preguntar
  "primera vez o ya tengo". Mejor: "Jiminy, ya creé el proyecto".

### Primera sesión

- El tope de 15 preguntas no dice cuáles cuentan. `entrevista.md` lo definió: cuentan
  las que piden un dato, una elección o algo de la persona; no cuentan las de pantalla
  ni los sí o no sobre algo que Jiminy acaba de mostrar. Hay que llevarlo al plan.
- El tono y el formato "se preguntan en la primera habilidad", pero nadie tiene esa
  tarea y quedan en "todavía no lo sé". Hay que decidir quién los pregunta y quién
  actualiza el perfil.
- El lugar de la carpeta y la compu se pierden al pasar de la conversación suelta a la
  del proyecto. Hoy se deducen de la ruta o se preguntan sin contar para el tope.

### Semillas usadas al vuelo

- Cuando `puerta` hace una tarea con una semilla sin guardarla, no corre ningún
  control propio de la semilla (`revisar` nunca lee `controles.md`). Hoy `revisar`
  mira "Errores graves" y "Lo que tiene que tener el resultado". Propuesta: que las
  semillas repitan en "Errores graves" sus controles críticos.

### Estilo y validador

- Las marcas "[confirmar en Fase 0]" aparecen dentro de textos que Jiminy le dice a la
  persona. Falta una regla global que diga que esas marcas no se dicen.
- El validador no revisa la jerga en `skills/<h>/referencias/*.md` ni comprueba las
  referencias propias de una habilidad (`./referencias/...`). En esas referencias,
  `../` se resuelve desde la carpeta de la habilidad, y `rutas.md` no lo dice.
- Un nombre de otra persona en el nombre de un entregable viejo: hoy, a pedido no se
  toca (se ofrece una copia con nombre genérico) y antes de entregar se cambia.
