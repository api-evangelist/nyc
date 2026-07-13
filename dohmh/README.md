# DOHMH (nyc.gov/site/doh) — Low-Hanging Fruit Assessment

Fourth domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **NYC Department of Health and Mental Hygiene (DOHMH)**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (restaurants, inspections, rodents, childcare, clinics, complaints, permits, vital records).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (LiveSite WCM/Akamai/Dynatrace; ABC Eats AngularJS+ASP.NET; eVital VRRTS; Accela Citizen Access; VitalChek; 311…).
- [apis-observed.md](apis-observed.md) — the observed systems: a private ABC Eats Web API, open Socrata SODA, and the transactional apps (eVital, Accela) with no open API.
- [crosswalk.md](crosswalk.md) — fruit ↔ systems ↔ Open Data mapping (81 DOHMH datasets) with coverage verdicts.
- [opendata-dohmh.md](opendata-dohmh.md) / [opendata-dohmh.json](opendata-dohmh.json) — all 81 DOHMH Open Data datasets sorted by page views, with column schemas for the key ones.
- [schemas/](schemas/) — individual JSON Schema per object: `food-establishment` · `inspection` · `rodent-inspection` · `childcare-center` · `health-facility` · `environmental-complaint` · `vital-record-request` (+ shared `_common`).
- [openapi/dohmh.yaml](openapi/dohmh.yaml) — OpenAPI 3.1 contract `$ref`ing each object (10 paths / 12 operations, incl. the net-new write).
- [mcp/dohmh-mcp.json](mcp/dohmh-mcp.json) — design-first MCP server definition (10 agent tools; artifact, not a deployment).

## What was found — the fourth distinct pattern

DOHMH is the **most data-rich** domain in the project, and that is precisely the finding. Its data is thoroughly liberated — **81 datasets** on NYC Open Data, led by the city's single most-viewed dataset — but its **transactions** are siloed:

1. **NYC Open Data (SODA)** — 81 open, machine-readable datasets (restaurant/rodent/childcare inspections, complaints, and much more). Reads are solved.
2. **ABC Eats** (`a816-health.nyc.gov/ABCEatsRestaurants`) — a public restaurant-grade lookup that is an **AngularJS SPA over a private, undocumented Web API** — duplicating the open dataset without offering a contract.
3. **eVital VRRTS + VitalChek** — the birth/death **certificate ordering** transaction, locked in a session-gated ASP.NET app and a third-party vendor portal, with **no open API**.
4. **Accela Citizen Access** — health permits & licenses as a **vendor COTS** app, no open API.

**None lets an agent *act*.** A resident asking "what's this restaurant's grade, and can you order my birth certificate?" can read the grade three ways but cannot transact at all.

**Reframe (vs. the first three domains):**

| | Parks | DOE | Council | **DOHMH** |
|---|---|---|---|---|
| Platform | Smarty/PHP | Sitefinity (.NET) | WordPress | **LiveSite WCM + a fleet of ASP.NET/COTS apps** |
| Core problem | data as HTML | search rented | three APIs, none owned | **data liberated, transactions siloed** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** | **transact** |

## Reverse-engineered entities

`FoodEstablishment` · `Inspection` (with `Violation[]`) · `RodentInspection` · `ChildcareCenter` · `HealthFacility` · `EnvironmentalComplaint` · `VitalRecordRequest` (net-new write) — join keys **camis**, **bbl/bin**, **dc_id**, plus the shared NYC geography spine.

## Method & caveats

Outside-in crawl (browser UA; `www.nyc.gov` robots.txt only disallows `/html/misc/`). DOH pages on the shared LiveSite WCM (`/site/doh/*.page`); transactional apps on `a816-*.nyc.gov` fingerprinted from headers (not exercised — no orders placed, no forms submitted). Open Data enumerated and agency-verified via the Socrata Discovery API (81 assets). A sample, not a full spider; the vital-records and permit flows are documented from their landing pages, not driven.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (81 datasets) ✅ · JSON Schemas (7 + `_common`) ✅ · OpenAPI 3.1 (10 paths / 12 ops) ✅ · MCP artifact (10 tools) ✅.
- **Next:** promote the ABC Eats backend to a documented API; stand up the net-new vital-records ordering write in front of eVital/VitalChek; publish `HealthFacility` as a resource; then the next domain from [../domains.md](../domains.md).
