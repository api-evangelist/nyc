# @api-common/nyc-mcp — The Programmable City

A **design-first MCP server over New York City government** — the agent-native front door to all 67 agencies from the [NYC Modernization](https://nyc.apievangelist.com) study. Browse the agencies, the ten common government-process skills, and the cross-agency prompts and resources, all backed by reference example data synthesized from the agency JSON Schemas.

> **Design-first / reference.** Reads return **example data** (synthesized from the schemas). Write workflows are described in each agency's OpenAPI but not executed here. This is the installable demonstration of the [experience layer](https://nyc.apievangelist.com/experience.html), not a production gateway.

## Install

One click via [install.apicommons.org](https://install.apicommons.org/?server=https://raw.githubusercontent.com/api-evangelist/nyc/main/experience/mcp-server/server.json), or run directly:

```bash
npx -y @api-common/nyc-mcp
```

Add to any MCP client (Claude Desktop, Cursor, VS Code, …):

```json
{ "mcpServers": { "nyc": { "command": "npx", "args": ["-y", "@api-common/nyc-mcp"] } } }
```

## What it exposes

**Tools** — `list_agencies`, `get_agency`, `search_city_data`, `look_up_place` (nyc-commons Place), `list_government_processes`, `find_agency_for_task`.

**Resources** — `nyc://catalog`, `nyc://commons/geography`, `nyc://skills`, and templated `nyc://agency/{slug}`, `nyc://place/{bbl}`.

**Prompts** — the cross-agency whole-task entry points: `who_represents_this_address`, `everything_about_this_place`, `how_do_i_apply_for`, `report_a_problem_at`, `whats_the_status_of_my`, `what_agency_handles`, `find_a_service_near_me`.

## Rebuild the bundled data

`data.json` is generated from the repo by `python3 scripts/build-gateway.py` (catalog + example records + skills + geography spine).

---
*Part of [api-evangelist/nyc](https://github.com/api-evangelist/nyc) · [nyc.apievangelist.com/experience.html](https://nyc.apievangelist.com/experience.html). MIT.*
