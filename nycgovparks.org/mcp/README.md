# NYC Parks — MCP Server (design artifact)

A **design-first** definition of a Model Context Protocol (MCP) server for NYC Parks. This is an **artifact, not a deployment** — it describes the agent-native tool surface the same way [../openapi/nyc-parks.yaml](../openapi/nyc-parks.yaml) describes the REST surface and [../schemas/](../schemas/) describe the objects. Nothing here runs; it's a contract.

- **File:** [nyc-parks-mcp.json](nyc-parks-mcp.json)
- **Why design-first:** the tool surface is derived from — and kept in lockstep with — the OpenAPI. Every tool carries `x-openapi-operation` pointing at the operation it fronts, and every tool's `inputSchema`/`outputSchema` `$ref`s the same object schema files the API uses. One object model, three contracts (JSON Schema → OpenAPI → MCP).

## Why an MCP surface at all

This is the piece the 2010–2018 open-data era never had (see the [project README](../../README.md)). Open Data made parks data *downloadable*; an MCP server makes it *callable by agents* — an assistant can find a dog run near a user, check whether a pool is open, surface a park's capital projects, or **submit and track a permit application** on the user's behalf. Same resources as the API, shaped as tools.

## Tool catalog (15 tools)

Read tools are anonymous/open. Permit tools require an authenticated applicant (`x-auth: applicant`) and, for writes, are annotated non-read-only so a host will gate them behind user confirmation.

| Tool | Reads/Writes | Resource | → OpenAPI op |
|---|---|---|---|
| `find_parks` | read | Park[] | `listParks` |
| `get_park` | read | Park | `getPark` |
| `list_park_facilities` | read | Facility[] | `listParkFacilities` |
| `find_facilities` | read | Facility[] | `listFacilities` |
| `find_events` | read | Event[] | `listEvents` |
| `get_event` | read | Event | `getEvent` |
| `find_monuments` | read | Monument[] | `listMonuments` |
| `get_monument` | read | Monument | `getMonument` |
| `find_trees` | read | Tree[] | `listTrees` |
| `find_capital_projects` | read | CapitalProject[] | `listCapitalProjects` |
| `get_capital_project` | read | CapitalProject | `getCapitalProject` |
| `submit_permit_application` | **write** 🔐 | PermitApplication | `createPermitApplication` |
| `check_permit_status` | read 🔐 | PermitApplication | `getPermitApplication` |
| `list_permit_applications` | read 🔐 | PermitApplication[] | `listPermitApplications` |
| `update_permit_application` | **write** 🔐 | PermitApplication | `updatePermitApplication` |

**Deliberate omissions:** the OpenAPI's `getFacility` and `getTree` (fetch-by-opaque-id) have no dedicated tool — agents reach individual facilities and trees through `find_facilities` / `list_park_facilities` / `find_trees` rather than guessing internal ids. Kept out to keep the tool list agent-friendly.

## Tool annotations

Each tool uses MCP [tool annotations](https://modelcontextprotocol.io/) as design hints for hosts:

- `readOnlyHint: true` on all `find_*`/`get_*`/`check_*` tools — safe to call without confirmation.
- `submit_permit_application` / `update_permit_application`: `readOnlyHint: false` (+ `idempotentHint: true` on update) — hosts should confirm with the user before invoking.
- `openWorldHint: true` throughout — these reach an external system of record.

## Example agent scenarios

- *"Find a dog run in Brooklyn near Prospect Park"* → `find_parks(q:"Prospect Park")` → `list_park_facilities(gisPropNum, type:"dog-area")`.
- *"Any free kids' events in Queens this weekend?"* → `find_events(borough:"Queens", from, to, category)`.
- *"What capital projects are underway in Central Park?"* → `find_parks` → `find_capital_projects(borough:"Manhattan")`.
- *"Apply for a tennis permit and tell me when it's approved"* → `submit_permit_application(...)` (confirmed) → later `check_permit_status(applicationId)`.

## Auth & tiering (design note)

- **Anonymous read** for the discovery tools (parks, facilities, events, monuments, trees, capital projects) — public data, no key.
- **Applicant auth** (bearer) for permit tools — tied to a person/org identity; writes gated behind host confirmation via annotations.
- If usage tiering is ever wanted, the natural line is **discovery free / transactional (permits) authenticated** — not metering the open data.

## Relationship to the other artifacts

```
schemas/*.json      ← one JSON Schema per object (source of truth)
   ↓ $ref
openapi/nyc-parks.yaml   ← REST contract ($ref objects)
   ↓ x-openapi-operation
mcp/nyc-parks-mcp.json   ← agent contract ($ref same objects, maps to same ops)
```
