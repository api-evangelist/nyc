# Low-Hanging Fruit Index — NYCHA

**Agency:** New York City Housing Authority (NYCHA)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt — `nyc.gov/robots.txt` only disallows `/html/misc/`). Fingerprinted the informational site `nyc.gov/site/nycha` (Akamai + nginx + NYC.gov "Livesite" platform + Dynatrace) and the resident **Self Service Portal** at `selfserve.nycha.info/nycha/app/eservice/enu`, identified as **Oracle Siebel CRM** (`SWECmd`, `OracleSiebel_logo.gif`, page title). Verified the NYC Open Data agency label `New York City Housing Authority (NYCHA)` via the Socrata Discovery API and pulled all **24** assets with column schemas.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-nycha.md](opendata-nycha.md).

## Headline findings

1. **NYCHA is a split domain.** An informational site on the shared NYC.gov chassis, and a resident **Self Service Portal running Oracle Siebel CRM** (`selfserve.nycha.info`) with **no API**.
2. **The reference data is unusually open.** **24 NYC Open Data datasets** cover developments (Development Data Book, 55 columns), residential addresses, community facilities, **six** streams of utility consumption-and-cost metering, and aggregate resident demographics.
3. **But the service layer is locked.** Rent, recertification, waitlist applications, and repair **work orders** — the things residents actually *do* — live only inside a login-walled, JavaScript-only Siebel portal or a phone call. None has a machine-readable contract.
4. **Households stay private by design.** Resident demographics are published only in aggregate (Resident Data Book); no individual `HouseholdRecord` is ever exposed.

> **Reframe (fourth distinct pattern):** Parks = *replatform* a legacy site; DOE = *reclaim* rented search + a hidden backend; Council = *consolidate + own* three fragmented APIs; **NYCHA = unlock the service layer.** Here the data is already open — the work is least about liberating datasets and most about giving the **resident transaction layer** (above all, reporting a repair) an owned, agent-native API instead of a vendor CRM screen.

## The fruit

| # | Name | Entity | Where the data lives | Open Data twin |
|---|---|---|---|---|
| 1 | Public Housing Developments | `Development` | SODA + map | ✅ Development Data Book (`evjd-dqpz`, 55c) |
| 2 | Residential Addresses | `ResidentialAddress` | SODA | ✅ Residential Addresses (`3ub5-4ph8`, 26c) |
| 3 | Community Facilities & Service Centers | `CommunityFacility` | SODA + map | ✅ Community Facilities (`crns-fw6u`) |
| 4 | Utility Consumption & Cost | `UtilityConsumption` | SODA (×6) | ✅ Electric (`jr24-e7cr`) + water/gas/steam/oil |
| 5 | Resident Demographics | `ResidentStatistics` | SODA | 🟡 Resident Data Book (`5r5y-pvs3`) — aggregate only |
| 6 | REES / Jobs (Local Law 163) | `ResidentStatistics` | SODA | ✅ REES by dev/borough/council (`dggd-3jfu`…) |
| 7 | Pay rent | — (portal) | Siebel portal | ❌ gap (no API) |
| 8 | Annual recertification | — (portal) | Siebel portal | ❌ gap (no API) |
| 9 | Waitlist application | `WaitlistApplication` | Siebel portal | ❌ gap (no API) |
| 10 | **Report a repair (work order)** | `WorkOrder` | Siebel portal + Contact Center | ❌ **net-new** |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **Socrata SODA** — 24 NYCHA datasets (the one real, open API; reference data only).
- **Oracle Siebel CRM** — the Self Service Portal; login-walled, JavaScript-only, no API.
- Platform: informational site on the **NYC.gov shared "Livesite" platform** (Akamai edge, nginx, Dynatrace RUM) — the fourth distinct platform after Parks' Smarty/PHP, DOE's Sitefinity/.NET, and Council's WordPress.

## Reverse-engineered entities

`Development` · `ResidentialAddress` · `CommunityFacility` · `UtilityConsumption` (PropertyMeter) · `ResidentStatistics` (aggregate; never individual household) · `WorkOrder` (net-new write; also stands in for the Siebel-locked WaitlistApplication / rent / recertification transactions) — join keys: **TDS #**, **EDP #**, **HUD AMP #**, **BIN/BBL**.

## Next

1. **JSON Schema** per entity, reconciling real Open Data column names (TDS #, UMIS Bill ID, BBL/BIN, the geography spine) — done ([schemas/](schemas/)).
2. **OpenAPI** publishing the open reference data as clean resources + the net-new `POST /work-orders` (report a repair) — done ([openapi/nycha.yaml](openapi/nycha.yaml)).
3. **MCP** artifact: `find_developments`, `get_development`, `find_facilities`, `find_utility_consumption`, `find_resident_statistics`, `list_my_work_orders`, `report_repair` — done ([mcp/nycha-mcp.json](mcp/nycha-mcp.json)).
