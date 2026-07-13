# Low-Hanging Fruit Index — DEP

**Agency:** New York City Department of Environmental Protection (DEP)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt — `nyc.gov/robots.txt` only disallows `/html/misc/`). Fingerprinted the informational site `nyc.gov/site/dep` (Akamai + nginx + NYC.gov "Livesite" platform v22 + Dynatrace) and the customer **My DEP Account** portal at `a826-umax.dep.nyc.gov`, identified as the **uMAX** utility Customer Information System on **ASP.NET / ASP.NET Core** behind **Azure AD B2C** (`umaxazprodb2c.b2clogin.com`) on Azure App Service. Verified the NYC Open Data agency label `Department of Environmental Protection (DEP)` via the Socrata Discovery API and pulled all **57** assets with column schemas.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-dep.md](opendata-dep.md).

## Headline findings

1. **DEP is a split, data-rich but transaction-poor domain.** An informational site on the shared NYC.gov chassis, and a customer **My DEP Account portal running the uMAX utility CIS** (`a826-umax.dep.nyc.gov`, ASP.NET + Azure AD B2C) with **no API**.
2. **The reference/telemetry data is unusually open.** **57 NYC Open Data datasets** cover water consumption (DEP's most-viewed asset), reservoir levels, harbor/drinking/watershed/lead-copper water quality, green infrastructure, hydrants & catch basins, and water/air/asbestos permits.
3. **But that data is sprawling and inconsistently typed.** Harbor Water Quality is **100 free-text columns**; reservoir levels are cryptic SCADA tags; there are ~a dozen near-duplicate Watershed tables. Open ≠ usable.
4. **And the service layer is split and locked.** Bill payment and account management live only in the uMAX portal; street conditions — a water-main break, no water, or a **sewer backup** — are funneled into generic **NYC311**. Neither is a DEP-owned API.

> **Reframe (fifth distinct pattern):** Parks = *replatform* a legacy site; DOE = *reclaim* rented search + a hidden backend; Council = *consolidate + own* three fragmented APIs; NYCHA = *unlock* a service layer locked in one CRM; **DEP = transact.** Here the data is already open (if messy) — the work is to give the **customer transaction layer** (pay a bill, manage an account, and above all report a water-main break or sewer backup) an owned, well-typed, agent-native API instead of a billing portal plus a generic 311 form.

## The fruit

| # | Name | Entity | Where the data lives | Open Data twin |
|---|---|---|---|---|
| 1 | Water Consumption (citywide) | `WaterConsumption` | SODA | 🟡 Water Consumption (`ia2d-e54m`) — citywide only |
| 2 | Reservoir Levels | `ReservoirLevel` | SODA | 🟡 Current Reservoir Levels (`zkky-n5j3`) — cryptic SCADA |
| 3 | Water Quality | `WaterQualitySample` | SODA (×many) | 🟡 Harbor (`5uug-f49n`, 100c) + drinking/watershed/lead |
| 4 | Green Infrastructure | `GreenInfrastructure` | SODA (×4) | ✅ Point Layer (`df32-vzax`, 35c) + regulated/porous/medians |
| 5 | Hydrants & Catch Basins | `Hydrant` | SODA + map | ✅ Citywide Hydrants (`6pui-xhxz`) + Hydrants (`5bgh-vtsn`) |
| 6 | Permits (water/sewer, CATS air, asbestos) | `Permit` | SODA | ✅ read (`hphy-6g7m`…) · ❌ apply/renew |
| 7 | Pay water/sewer bill | — (portal) | uMAX portal | ❌ gap (no API) |
| 8 | Manage account | — (portal) | uMAX portal | ❌ gap (no API) |
| 9 | Report a sewer backup / catch-basin flooding | `WaterServiceRequest` | NYC311 | ❌ gap (no DEP API) |
| 10 | **Report a water problem (main break / no water / leak)** | `WaterServiceRequest` | NYC311 + phone | ❌ **net-new** |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **Socrata SODA** — 57 DEP datasets (the one real, open API; reference/telemetry data only, and inconsistently typed).
- **uMAX (Advanced Utility Systems) CIS** — the My DEP Account portal; login-walled ASP.NET SPA behind Azure AD B2C, no API.
- **NYC311** — where DEP street conditions are actually reported; generic, not DEP-owned.
- Platform: informational site on the **NYC.gov shared "Livesite" platform** (Akamai edge, nginx, Dynatrace RUM) — the same chassis behind Parks, DOE, Council, and NYCHA's informational surfaces.

## Reverse-engineered entities

`WaterConsumption` (citywide only) · `ReservoirLevel` · `WaterQualitySample` (analytes as a measurements map) · `GreenInfrastructure` · `Hydrant` · `Permit` (read-only) · `WaterServiceRequest` (net-new write; also stands in for the uMAX-locked bill-pay / account transactions and the 311-routed sewer backup) — join keys: **tax Block/Lot/BBL**, **UNITID**, **GI_ID**, the **geography spine**.

## Next

1. **JSON Schema** per entity, reconciling real Open Data column names and normalizing the messy ones (SCADA tags → reservoir fields; 100 text columns → a `measurements` map) — done ([schemas/](schemas/)).
2. **OpenAPI** publishing the open reference data as clean resources + the net-new `POST /water-service-requests` (report a water/sewer problem) — done ([openapi/dep.yaml](openapi/dep.yaml)).
3. **MCP** artifact: `find_reservoir_levels`, `find_water_consumption`, `find_water_quality`, `find_green_infrastructure`, `get_green_infrastructure`, `find_hydrants`, `get_hydrant`, `find_permits`, `list_my_service_requests`, `get_service_request`, `report_water_problem` — done ([mcp/dep-mcp.json](mcp/dep-mcp.json)).
