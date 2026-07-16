# NYC — Programmable City (the experience layer)

*Every NYC government API, MCP server, and Agent Skill in one place — the API → MCP → Agent-Skill chain across all 70 agencies.*

Interactive: **[nyc.apievangelist.com/experience.html](https://nyc.apievangelist.com/experience.html)**. Machine artifacts: [unified OpenAPI](experience/nyc-openapi.json) · [NYC-wide MCP](experience/nyc-mcp.json) · [APIs.json descriptor](experience/nyc.apis.json) · [Skills](experience/skills/).

## The opportunity in one number set

| Surface | Count |
|---|---|
| Agency APIs | 70 |
| REST operations | 752 |
| — of which net-new write operations | 80 |
| MCP tools | 653 |
| MCP prompts (cross-agency + per-agency) | 7 + 168 = **175** |
| MCP resources (cross-agency + per-agency) | 7 + 210 = **217** |
| Common government-process skills | 10 |

Built on the [API Experience](https://experience.apicommons.org) chain — **REST operation → MCP tool → Agent Skill** — minus the free/pro tiering and AI enrichment: a clean view of the whole programmable surface the city could have.

## Ten common government processes (Agent Skills)

| Skill | Group | Agencies | Operations |
|---|---|---|---|
| [Apply for a permit, license, or benefit](experience/skills/apply-for-a-permit-license-or-benefit.md) | Act | 38 | 41 |
| [Report a problem or file a complaint](experience/skills/report-a-problem-or-file-a-complaint.md) | Act | 20 | 20 |
| [Request public records](experience/skills/request-public-records.md) | Act | 2 | 2 |
| [Schedule or reserve](experience/skills/schedule-or-reserve.md) | Act | 7 | 7 |
| [Register or enroll](experience/skills/register-or-enroll.md) | Act | 6 | 6 |
| [Dispute or appeal](experience/skills/dispute-or-appeal.md) | Act | 3 | 3 |
| [Pay a city charge](experience/skills/pay-a-city-charge.md) | Act | 1 | 1 |
| [Look up a property or place](experience/skills/look-up-a-property-or-place.md) | Know | 36 | 94 |
| [Check application or case status](experience/skills/check-application-or-case-status.md) | Know | 23 | 23 |
| [Search city data and records](experience/skills/search-city-data-and-records.md) | Know | 70 | 555 |

## Cross-agency MCP prompts & resources

**Prompts** — whole-task entry points: `who_represents_this_address`, `everything_about_this_place`, `how_do_i_apply_for`, `report_a_problem_at`, `whats_the_status_of_my`, `what_agency_handles`, `find_a_service_near_me`.

**Resources** — shared context: `nyc://catalog`, `nyc://commons/geography`, `nyc://transactions`, `nyc://linkage`, `nyc://skills`, `nyc://place/{bbl}`, `nyc://agency/{slug}`.

---
*Design-first artifacts, not deployments. Part of the [NYC Modernization](README.md) study.*
