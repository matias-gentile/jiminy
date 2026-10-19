# Actualizar la biblioteca

Procedimiento de la Fase 5. **Todavía no está activo:** se activa después del piloto
(decisión 11 de `docs/diseno.md`). Hasta entonces se puede correr a mano.

## Qué hace

Las semillas de Jiminy salen de fuentes externas fijadas a un commit
(`biblioteca/fuentes.json`). Esas fuentes cambian seguido. La actualización revisa
qué cambió, decide si vale la pena y propone el cambio en el repo para que Matías
lo apruebe. Nada llega a las personas sin esa aprobación.

## Pasos

1. **Ver qué cambió.**

   ```
   python3 scripts/revisar_fuentes.py --salida /tmp/cambios-fuentes.md
   ```

   El informe lista, por fuente, los cambios en las rutas que usamos, los archivos
   nuevos junto a ellas y si cambió la licencia.

2. **Decidir, cambio por cambio.** Un cambio entra solo si pasa las cinco preguntas
   de *Biblioteca curada* en `docs/diseno.md`: le sirve a alguien sin experiencia
   técnica, funciona en Cowork sin instalar nada, suma al ciclo de mejora, no agrega
   riesgo y su licencia permite copiarlo. Si cambió la licencia, no se adapta nada de
   esa fuente hasta revisarla.

3. **Adaptar.** Para cada cambio que entra:
   - editar `plugins/jiminy/semillas/<semilla>/habilidad.md` (y `preguntas.md` o
     `controles.md` si hace falta) en el formato de Jiminy;
   - subir el número en la línea `**Origen:** semilla: <semilla> · versión <N>` de
     `habilidad.md`, para que `puerta` ofrezca la comparación a quienes ya la usan;
   - anotar en `origen.md` el commit nuevo y qué se cambió;
   - actualizar el commit y la fecha en `biblioteca/fuentes.json` y en
     `biblioteca/indice.md`.

   Lo que pasó de largo también se registra: se actualiza el commit fijado, y en
   `biblioteca/indice.md` queda por qué no entró.

4. **Fuentes nuevas.** Si un archivo nuevo parece útil, se agrega como fila *Sin
   revisar* en `biblioteca/indice.md`. No se adapta en la misma pasada.

5. **Validar y proponer.** Correr `python3 scripts/validar.py`, subir la `version`
   en `plugins/jiminy/.claude-plugin/plugin.json`, y abrir un pull request con el
   resumen: qué cambió en cada fuente, qué entró, qué no y por qué.

6. **Aprobación.** Matías revisa y une el pull request. Cowork lo trae con *Sync
   automatically*. Las personas que ya personalizaron una habilidad no pierden nada:
   `puerta` les ofrece comparar la versión nueva de la semilla con la suya.

## La tarea semanal

Cuando se active, se crea una tarea programada de Claude que abre una sesión nueva
con este repo cada lunes y le da este pedido:

> En el repo matias-gentile/jiminy, seguí `docs/actualizar-biblioteca.md`. Corré
> `scripts/revisar_fuentes.py`. Si no hay cambios, terminá sin hacer nada. Si hay,
> evaluá cada uno con las cinco preguntas de la biblioteca curada, adaptá solo lo
> que pase, actualizá `fuentes.json`, `biblioteca/indice.md` y los `origen.md`,
> subí la versión de la semilla y del plugin, corré `scripts/validar.py` y abrí un
> pull request contra `main` con el resumen. No unas el pull request: lo aprueba Matías.
