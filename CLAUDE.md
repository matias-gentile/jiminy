# Jiminy: guía para trabajar en este repo

Jiminy es un plugin de Cowork para personas sin experiencia técnica. Antes de
cambiar algo, leé `docs/diseno.md` (decisiones) y `docs/plan-desarrollo.md`
(especificación de cada componente).

## Dónde está cada cosa

- `plugins/jiminy/`: el plugin. `reglas.md`, `referencias/` y `plantillas/` son los
  contratos compartidos; `skills/` es el núcleo; `semillas/`, los módulos por situación.
- `plugins/jiminy-prueba/`: solo para la Fase 0. Se borra cuando terminen las pruebas.
- `biblioteca/`: fuentes externas curadas y fijadas a un commit.
- `docs/`: diseño, plan, Fase 0, piloto, escenarios y guías.
- `scripts/validar.py`: validación. Corre en cada push.

## Reglas para cambiar el plugin

- **Los contratos mandan.** `plugins/jiminy/referencias/carpeta.md` define los
  archivos de la carpeta de la persona, su formato y quién escribe cada uno. Si un
  cambio necesita algo nuevo, primero se cambia el contrato y después las habilidades.
- **No romper carpetas existentes.** Hay personas con carpetas creadas por versiones
  anteriores. Un cambio de formato tiene que leer el formato viejo, o subir
  `Versión de la carpeta` en `plantillas/jiminy.md` y explicar en `empezar` cómo
  actualizarla.
- **Lo que Jiminy le dice a la persona** sigue `plugins/jiminy/referencias/estilo.md`:
  una pregunta por vez, sin jerga.
- **Nada depende de conectores, de internet ni de instalar algo.**
- **Nombres de archivo válidos en Windows**, en minúsculas, sin tildes, con guiones.
- **Lo adaptado de otros proyectos** conserva su licencia en `origen.md` y en
  `plugins/jiminy/AVISOS-DE-TERCEROS.md`, y se registra en `biblioteca/indice.md`.
- Cada cambio del plugin que llega a las personas sube la `version` de
  `plugins/jiminy/.claude-plugin/plugin.json`.

## Antes de subir

```
python3 scripts/validar.py
```

Tiene que terminar sin errores.

## Idioma

Todo en español. Los mensajes de commit también.
