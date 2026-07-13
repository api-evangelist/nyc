# Crosswalk — Website/Portal Fruit ↔ APIs ↔ NYC Open Data (DEP)

Maps the low-hanging fruit on **nyc.gov/site/dep** and the **My DEP Account** portal to (a) the **existing APIs** (Socrata SODA; the uMAX portal; NYC311) and (b) the **57 DEP datasets** on NYC Open Data. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-dep.json](opendata-dep.json).

## The reframe — fifth distinct pattern

- **Parks:** data-rich HTML on a legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned → *consolidate + own.*
- **NYCHA:** reference data wide open, resident transactions locked in one Oracle Siebel CRM → *unlock.*
- **DEP:** reference data **very** open but sprawling and inconsistently typed (57 datasets), and the customer transaction layer **split** between a uMAX billing portal (Azure AD B2C) and generic NYC311 → **transact.**

DEP is the **data-rich, transaction-poor** case. Reservoirs, water quality, consumption, green infrastructure, hydrants, and permits are all machine-readable on Open Data — but *hard to use* (Harbor Water Quality = 100 free-text columns; reservoir levels = cryptic SCADA tags). And the things a customer *does* — pay a water bill, manage an account, and above all **report a water-main break or sewer backup** — have no single, owned, machine-readable contract. A resident or agent asking "report that my basement is flooding with sewage and tell me the status" has no DEP API to call; it goes to 311.

Coverage: ✅ strong open twin · 🟡 partial/inconsistent · ❌ gap (no API).

## Entity crosswalk

| Entity | Website / Portal | API today | Open Data | Cov. |
|---|---|---|---|---|
| `ReservoirLevel` | `/water/reservoir-levels` | SODA | Current Reservoir Levels (`zkky-n5j3`, 25c — cryptic SCADA tags) | 🟡 open but cryptic |
| `WaterConsumption` | `/water` | SODA | Water Consumption in NYC (`ia2d-e54m`, 4c — **citywide only**) | 🟡 aggregate only |
| `WaterQualitySample` | `/water/drinking-water` | SODA | Harbor (`5uug-f49n`, 100c text), Drinking Water Distribution (`bkwf-xfky`), Watershed (`y43c-5n92` + subtables), Lead/Copper (`k5us-nav4`) | 🟡 open but inconsistent |
| `GreenInfrastructure` | `/water/green-infrastructure` | SODA | Point (`df32-vzax`), Regulated (`fm4z-qud6`), Porous Pavement (`n7f2-dyvt`), Medians (`drep-uzs7`) | ✅ |
| `Hydrant` | — | SODA | Citywide Hydrants map (`6pui-xhxz`) + Hydrants (`5bgh-vtsn`); Catch Basins (`2w2g-fk3i`) | ✅ |
| `Permit` | `/environmental-education/…`, permit pages | SODA | Water & Sewer (`hphy-6g7m`, `4k4u-823g`), CATS Air (`f4rp-2kvy`), Asbestos ACP7 (`vq35-j9qm`) | ✅ (read); ❌ apply/renew |
| Water-bill payment | My DEP Account | **uMAX portal only** (Azure B2C) | — | ❌ gap |
| Account management | My DEP Account | **uMAX portal only** | — | ❌ gap |
| **`WaterServiceRequest`** (main break / no water / sewer backup / leak / catch basin / hydrant) | DEP site → NYC311 | **NYC311 / phone only** | Work Order Management Module (`4fvw-nn9c`) — read-only, after the fact | ❌ **net-new** |

## The mismatch, concretely

| Source | Strength | Weakness |
|---|---|---|
| **Socrata SODA (57 datasets)** | Open, machine-readable; broad — supply, quality, consumption, GI, assets, permits | Reference/telemetry only; sprawling and inconsistently typed (100-column text tables, cryptic SCADA tags, a dozen near-duplicate watershed tables); nothing about live customer transactions |
| **uMAX My DEP Account portal** | The real billing/account system — pay a water bill, manage an account | Login-walled ASP.NET SPA behind Azure AD B2C; no API, no OpenAPI, no JSON; not agent-accessible |
| **NYC311** | Where street conditions actually get reported | Generic, not DEP-owned; no DEP-specific contract; tracking is fragmented from the read-side Work Order data |

## Implications for the API-first + MCP proposal

1. **Publish the open reference data as one clean, well-typed resource model.** Reservoir levels, consumption, water quality, green infrastructure, hydrants, and permits behind one owned DEP contract ([OpenAPI](openapi/dep.yaml)) — so consumers learn one model, not 57 Socrata IDs and 100-column text tables.
2. **Give the service layer a transactional API.** Front uMAX and NYC311 with an owned contract so the core customer transaction — reporting and tracking a **water service request** — has a machine-readable, agent-native surface.
3. **Add the one net-new write workflow** — `report_water_problem` (create a water/sewer service request), with an emergency flag that routes water-main breaks, sewer backups, flooding, and no-water to DEP's 24-hour customer service.
4. **Type the analytes.** Normalize water-quality analytes into a `measurements` map so agents can read chlorine/turbidity/lead without decoding hundreds of free-text columns.
5. **MCP server** so an agent can answer "how full is the Cannonsville reservoir?", "what was the lead result at this address?", and — the point — "report that a water main broke on my street and tell me the status."
