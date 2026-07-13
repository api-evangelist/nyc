# Crosswalk — Website/Vendor-System Fruit ↔ APIs ↔ NYC Open Data (DDC)

Maps the low-hanging fruit on **nyc.gov/site/ddc** and DDC's vendor/procurement flow to (a) the **existing APIs** (Socrata SODA; the citywide PASSPort/City Record/Checkbook systems) and (b) the **4 DDC datasets** on NYC Open Data. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-ddc.json](opendata-ddc.json).

## The reframe — sixth distinct pattern

- **Parks:** data-rich HTML on a legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned → *consolidate + own.*
- **NYCHA:** reference data wide open, resident transactions locked in a vendor CRM → *unlock.*
- **DFTA:** provider network open, the connecting act is a phone call → *connect.*
- **DDC:** a **vendor-facing agency** whose own data is **thin and historical** and whose transactions all run on **citywide systems it doesn't own** → **surface** the live portfolio and front the citywide vendor flow.

DDC is the business-to-government inversion. There is no citizen and no citizen transaction — DDC builds for other agencies. Its published data is just four Socrata datasets (three of them `(Historical)`), and everything a vendor actually *does* — search solicitations, register, prequalify, respond, get award notices — happens in **PASSPort (MOCS)**, the **City Record**, and **Checkbook NYC (Comptroller)**. DDC owns neither a live data API nor a write surface. A firm or agent asking "what DDC solicitations are open in the Public Buildings division and how do I prequalify?" has no DDC API to call.

Coverage: ✅ open twin (even if stale) · 🟡 partial/derived · ❌ gap (no API).

## Entity crosswalk

| Entity | Website / System | API today | Open Data | Cov. |
|---|---|---|---|---|
| `CapitalProject` | `/projects` | SODA (snapshots) | Active Projects (`3ss8-m844`, 8c); Infrastructure Historical (`rukc-mmqu`, 9c); Public Buildings Historical (`g9ub-hrve`, 9c) | 🟡 historical/snapshot |
| `AwardedContract` | `/contracts/work-with-ddc` | SODA + Checkbook | Directory Of Awarded Construction Contracts (`j7gw-gcxi`, 4c) | ✅ (thin: 4 cols) |
| `Vendor` (firm/consultant) | Work With DDC / MWBE | **PASSPort UI only** | derived from `j7gw-gcxi` SELECTED FIRM | 🟡 derived |
| `Division` | `/about` | — | derived from `Division` column | 🟡 derived |
| `Solicitation` | Work With DDC → PASSPort | **PASSPort / City Record only** | — | ❌ gap (no DDC API) |
| **`VendorPrequalification`** (submit / express interest) | PASSPort (MOCS) | **PASSPort UI only** | — | ❌ **net-new** (B2G; no citizen write exists) |

## The mismatch, concretely

| Source | Strength | Weakness |
|---|---|---|
| **Socrata SODA (4 datasets)** | Open, machine-readable; covers the project portfolio and awarded contracts | Very thin (4–9 columns each); three of four are `(Historical)` snapshots; no live status; the live capital-commitment data lives under OMB/Comptroller, not DDC |
| **PASSPort / City Record / Checkbook** | The real transaction + transparency systems for solicitation, onboarding, prequalification, awards | Citywide, **not DDC-owned**; PASSPort is login-walled with no public API; no DDC-scoped contract or agent surface |

## Implications for the API-first + MCP proposal

1. **Surface the portfolio live.** Present capital projects, awarded contracts, vendors, and divisions behind one owned DDC contract ([OpenAPI](openapi/ddc.yaml)) — keyed on Project ID and PIN — instead of stale snapshots and four Socrata IDs.
2. **Front the citywide vendor flow.** Expose solicitations and a DDC-owned write path so a firm can prequalify / express interest without living inside PASSPort's UI.
3. **Add the one net-new write workflow** — `submit_prequalification` (vendor prequalification / expression of interest), with an optional City Record notification subscription. Be honest: this is **B2G**; there is **no citizen write** in this domain.
4. **Name the ownership gap.** The finding is that DDC owns neither its data API nor its transaction layer; modernization here is as much about *reclaiming ownership* of surfaces MOCS/Comptroller currently hold as about publishing.
5. **MCP server** so an agent can answer "which Public Buildings projects for DOE are in construction?", "what's the value of contract PIN X and who won it?", and — the point — "prequalify my engineering firm and alert me to matching solicitations."
