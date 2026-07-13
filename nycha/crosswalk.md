# Crosswalk — Website/Portal Fruit ↔ APIs ↔ NYC Open Data (NYCHA)

Maps the low-hanging fruit on **nyc.gov/site/nycha** and the **Self Service Portal** to (a) the **existing APIs** (Socrata SODA; the Siebel portal) and (b) the **24 NYCHA datasets** on NYC Open Data. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-nycha.json](opendata-nycha.json).

## The reframe — fourth distinct pattern

- **Parks:** data-rich HTML on a legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned → *consolidate + own.*
- **NYCHA:** the **reference data is already wide open** (24 Socrata datasets), but every **resident transaction is locked inside an Oracle Siebel CRM** with no API → **unlock the service layer.**

NYCHA inverts the usual problem. It is not that the data is trapped in HTML — the developments, addresses, facilities, utility metering, and aggregate demographics are all machine-readable on Open Data. It is that the things a resident *does* — pay rent, recertify income, check a waitlist application, and above all **report a repair** — live only behind a login-walled, JavaScript-only Siebel portal. A resident or agent asking "what's the status of my repair?" has no API to call.

Coverage: ✅ strong open twin · 🟡 partial/aggregate · ❌ gap (no API).

## Entity crosswalk

| Entity | Website / Portal | API today | Open Data | Cov. |
|---|---|---|---|---|
| `Development` | `/about/developments` | SODA | Development Data Book (`evjd-dqpz`, 55c); Public Housing Developments (`phvi-damg`); map (`npwq-dpkb`) | ✅ |
| `ResidentialAddress` | — | SODA | Residential Addresses (`3ub5-4ph8`, 26c) | ✅ |
| `CommunityFacility` | facility finder | SODA | Community Facilities (`crns-fw6u`); Service Centers (`d4iy-9uh7`); Contact Centers (`37fm-7uaa`) | ✅ |
| `UtilityConsumption` (PropertyMeter) | — | SODA | Electric (`jr24-e7cr`), Water (`66be-66yr`), Heating/Cooking Gas (`it56-eyq4`/`avhb-5jhc`), Steam (`smdw-73pj`), Oil (`bhwu-wuzu`) | ✅ |
| `ResidentStatistics` (household) | — | SODA | Resident Data Book Summary (`5r5y-pvs3`, 43c) — **aggregate only** | 🟡 aggregate |
| REES / jobs (Local Law 163) | `/residents/rees` | SODA | REES by dev/borough/council (`dggd-3jfu`, `snck-inhz`, `h65x-gk9r`); Jobs & Training (`an6v-iuem`) | ✅ |
| Rent payment | Self Service Portal | **Siebel UI only** | — | ❌ gap |
| Annual recertification | Self Service Portal | **Siebel UI only** | — | ❌ gap |
| `WaitlistApplication` (public housing / Section 8) | Self Service Portal | **Siebel UI only** | — | ❌ gap |
| **`WorkOrder`** (report a repair) | Self Service Portal + Contact Center | **Siebel UI / phone only** | — | ❌ **net-new** |

## The mismatch, concretely

| Source | Strength | Weakness |
|---|---|---|
| **Socrata SODA (24 datasets)** | Open, machine-readable; strong on physical stock, utilities, facilities, aggregate demographics | Reference/asset data only; static snapshots; nothing about live resident transactions |
| **Siebel Self Service Portal** | The real transaction system — rent, recertification, applications, work orders | Login-walled, JavaScript-only vendor CRM; no API, no OpenAPI, no JSON; not agent-accessible; a phone queue is the fallback |

## Implications for the API-first + MCP proposal

1. **Publish the open reference data as one clean resource model.** Developments, addresses, facilities, utilities, and aggregate statistics behind one owned NYCHA contract ([OpenAPI](openapi/nycha.yaml)) — so consumers learn one model, not 24 Socrata IDs.
2. **Unlock the service layer.** Front the Siebel portal with an API so the core resident transaction — reporting and tracking a **work order** — has a machine-readable, agent-native contract.
3. **Add the one net-new write workflow** — `report_repair` (create a maintenance work order), with an emergency flag that routes no-heat/hot-water/gas/flooding to the 24-hour Customer Contact Center.
4. **Keep households private.** Resident data stays aggregate-only; the API never exposes an individual `HouseholdRecord`.
5. **MCP server** so an agent can answer "which developments are in my council district?", "what did this development spend on electricity?", and — the point — "report that my radiator is broken and tell me the status."
