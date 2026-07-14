# NYC — Programmable City (the experience layer)

*Every NYC government API, MCP server, and Agent Skill in one place — the API → MCP → Agent-Skill chain across all 67 agencies.*

Interactive: **[nyc.apievangelist.com/experience.html](https://nyc.apievangelist.com/experience.html)**. Machine artifacts: [unified OpenAPI](experience/nyc-openapi.json) · [NYC-wide MCP](experience/nyc-mcp.json) · [APIs.json descriptor](experience/nyc.apis.json) · [Skills](experience/skills/).

## The opportunity in one number set

| Surface | Count |
|---|---|
| Agency APIs | 67 |
| REST operations | 721 |
| — of which net-new write operations | 77 |
| MCP tools | 624 |
| MCP prompts (cross-agency + per-agency) | 7 + 160 = **167** |
| MCP resources (cross-agency + per-agency) | 7 + 201 = **208** |
| Common government-process skills | 10 |

Built on the [API Experience](https://experience.apicommons.org) chain — **REST operation → MCP tool → Agent Skill** — minus the free/pro tiering and AI enrichment: a clean view of the whole programmable surface the city could have.

## Call it. Install it.

The experience layer is not just documentation — it's runnable:

- **Static reference API** — example data at stable URLs, served off GitHub Pages, GET-callable: `curl https://nyc.apievangelist.com/experience/api/dob/building.json`. Catalog at [`/experience/api/index.json`](https://nyc.apievangelist.com/experience/api/index.json). Reads only; write workflows are documented in the OpenAPI, not executed. 422 example collections, 844 records synthesized from the agency JSON Schemas.
- **Installable MCP server** — [`@api-common/nyc-mcp`](experience/mcp-server/), a working stdio server (`npx -y @api-common/nyc-mcp`) with tools (`list_agencies`, `get_agency`, `search_city_data`, `look_up_place`, `find_agency_for_task`), the 7 prompts, and `nyc://` resources — installable one-click via [install.apicommons.org](https://install.apicommons.org/?server=https://raw.githubusercontent.com/api-evangelist/nyc/main/experience/mcp-server/server.json). The install button is embedded on [experience.html](https://nyc.apievangelist.com/experience.html).

## Ten common government processes (Agent Skills)

| Skill | Group | Agencies | Operations |
|---|---|---|---|
| [Apply for a permit, license, or benefit](experience/skills/apply-for-a-permit-license-or-benefit.md) | Act | 35 | 38 |
| [Report a problem or file a complaint](experience/skills/report-a-problem-or-file-a-complaint.md) | Act | 20 | 20 |
| [Request public records](experience/skills/request-public-records.md) | Act | 2 | 2 |
| [Schedule or reserve](experience/skills/schedule-or-reserve.md) | Act | 7 | 7 |
| [Register or enroll](experience/skills/register-or-enroll.md) | Act | 6 | 6 |
| [Dispute or appeal](experience/skills/dispute-or-appeal.md) | Act | 3 | 3 |
| [Pay a city charge](experience/skills/pay-a-city-charge.md) | Act | 1 | 1 |
| [Look up a property or place](experience/skills/look-up-a-property-or-place.md) | Know | 35 | 93 |
| [Check application or case status](experience/skills/check-application-or-case-status.md) | Know | 20 | 20 |
| [Search city data and records](experience/skills/search-city-data-and-records.md) | Know | 67 | 531 |

## Cross-agency MCP prompts & resources

**Prompts** — whole-task entry points: `who_represents_this_address`, `everything_about_this_place`, `how_do_i_apply_for`, `report_a_problem_at`, `whats_the_status_of_my`, `what_agency_handles`, `find_a_service_near_me`.

**Resources** — shared context: `nyc://catalog`, `nyc://commons/geography`, `nyc://transactions`, `nyc://linkage`, `nyc://skills`, `nyc://place/{bbl}`, `nyc://agency/{slug}`.

---
*Design-first artifacts, not deployments. Part of the [NYC Modernization](README.md) study.*
