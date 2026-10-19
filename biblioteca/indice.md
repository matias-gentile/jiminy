# Biblioteca curada

Fuentes externas que Jiminy usa como base para sus semillas. Nada de esto se lee
en vivo: cada fuente queda fijada a una versión y se adapta al formato de Jiminy
antes de entrar al plugin. El porqué está en *Biblioteca curada*, en `docs/diseno.md`.

Última revisión: 2026-10-19.

## Fuentes y versión fijada

| Fuente | Autor | Licencia | Versión fijada |
|---|---|---|---|
| [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins/tree/33eeda1e8fd856455b05479d13a0f85b5f803744) | Anthropic | Apache-2.0 | `33eeda1e8fd856455b05479d13a0f85b5f803744` (2026-10-15) |
| [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents/tree/652b2692f8d8ec2b1f1a38e559073e287dfdc469) | AgentLand Contributors | MIT | `652b2692f8d8ec2b1f1a38e559073e287dfdc469` (2026-10-15) |
| [wshobson/agents](https://github.com/wshobson/agents/tree/0874a27b17a22e2b7c2e2bcd725768e0803cad06) | Seth Hobson | MIT | `0874a27b17a22e2b7c2e2bcd725768e0803cad06` (2026-10-17) |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills/tree/aeac41d4d005999432bb7312f7ff06383a91d59d) | Addy Osmani | MIT | `aeac41d4d005999432bb7312f7ff06383a91d59d` (2026-10-13) |

## Para adaptar

| Lo que dice la persona | Semilla | Fuente | Ruta | Estado | Notas |
|---|---|---|---|---|---|
| "armame los posteos del mes", "hace mucho que no publico" | Redes y contenido | knowledge-work-plugins | `small-business/skills/social-content-engine` | Pendiente | Deja los posteos listos para aprobar. Sin conectores, arma el calendario y los textos para publicar a mano. |
| "quiero que mi Instagram se vea mejor" | Redes y contenido | agency-agents | `marketing/marketing-instagram-curator.md` | Pendiente | Sacar lo comercial ("llamado a la acción fuerte", Shopping). |
| "armame un carrusel" | Redes y contenido | agency-agents | `marketing/marketing-carousel-growth-engine.md` | Sin revisar | |
| "que no suene a IA", "que suene a mí" | Escribir, Redes y contenido | wshobson/agents | `plugins/avoid-ai-writing/skills/avoid-ai-writing` | Pendiente | |
| "resumime este paper", "¿qué dice la evidencia?" | Aprender | agency-agents | `research/research-synthesist.md` | Pendiente | No cuenta diez citas del mismo estudio como diez pruebas. |
| "ayudame con los mails" | Mails y mensajes | knowledge-work-plugins | `small-business/skills/inbox-manager` | Sin revisar | |

## Referencias de diseño (no se copian)

| Para | Fuente | Ruta | Qué se toma |
|---|---|---|---|
| `empezar` | knowledge-work-plugins | `small-business/skills/smb-onboard` | Entrevista de a una pregunta; mostrar el perfil antes de guardarlo. |
| `puerta` | knowledge-work-plugins | `small-business/skills/smb-router` | Una sola recomendación por pedido; tabla de frases y habilidades. |
| Memoria | knowledge-work-plugins | `productivity/skills/memory-management`, `productivity/skills/start` | Memoria corta siempre a mano y el detalle aparte; copiar archivos del plugin con `${CLAUDE_PLUGIN_ROOT}`. |
| `empezar`, `nueva-habilidad` | addyosmani/agent-skills | `skills/interview-me` | Tener una hipótesis con nivel de confianza y preguntar hasta estar seguro. |
| Estructura del plugin | knowledge-work-plugins | `cowork-plugin-management/skills/create-cowork-plugin` | Formato de skills y plugins para Cowork. |

## Descartadas

| Fuente | Ruta | Por qué |
|---|---|---|
| agency-agents | `specialized/healthcare-marketing-compliance.md` | Es sobre la ley china de publicidad médica. |
| wshobson/agents | `plugins/social-publishing` | Publica a través de un servicio de terceros y pide una clave. |
| anthropics/claude-quickstarts | Todo | Son aplicaciones para programadores con clave de API. |
| wshobson/agents, addyosmani/agent-skills | El resto | Pensadas para programar. |
