# Crosswalk — Website Fruit ↔ APIs ↔ NYC Open Data (DHS)

Maps the low-hanging fruit on **nyc.gov/site/dhs** and the NYC311 outreach channel to (a) the **existing APIs** (Socrata SODA; NYC311) and (b) the **23 DHS datasets** on NYC Open Data. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-dhs.json](opendata-dhs.json).

## The reframe — fifth distinct pattern

- **Parks:** data-rich HTML on a legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned → *consolidate + own.*
- **NYCHA:** reference data wide open, every transaction locked in a vendor CRM → *unlock the service layer.*
- **DHS:** the **observational data is wide open** (23 Socrata datasets, led by the daily census), but there is **no service layer at all** — the actions route through NYC311/phone/in-person → **connect the action to an owned API.**

DHS is the most extreme version of the pattern so far. It is not that a transaction system is hidden or vendor-locked — there is **no DHS transaction system to expose**. The things a New Yorker does — apply for shelter, or **report someone on the street for outreach** — happen on the phone (311, 911) or at a front desk. A resident or agent asking "can you get outreach to the person sleeping at this corner, and tell me what happened?" has no API to call.

Coverage: ✅ strong open twin · 🟡 partial/aggregate · ❌ gap (no API).

## Entity crosswalk

| Entity | Website / Channel | API today | Open Data | Cov. |
|---|---|---|---|---|
| `ShelterCensus` (DailyReport) | `/about/stats-and-reports` | SODA | DHS Daily Report (`k46n-sa2m`, 13c); Historical (`dwrg-kzni`); Intake (`sci4-yqgk`) | ✅ |
| `DropInCenter` | `/outreach` | SODA | Directory Of Homeless Drop-In Centers (`bmxf-3rd4`, 13c) | ✅ |
| `ShelterFacility` | — | SODA | Shelter Repair Scorecard (`dvaj-b7yx`, 55c); Buildings (`3qem-6v3v`); Individual Census (`veav-vj3r`) | ✅ |
| `DHSContact` (offices / intake centers) | `/shelter` | SODA | Directory Of DHS Contacts (`cete-9g3v`, 14c) | ✅ |
| `StreetHomelessCount` | `/outreach` | SODA | Unsheltered ratio 2009–2012 (`483x-fy9e`…); LL19 Quarterly (`7tu6-bcih`) — **aggregate only** | 🟡 aggregate |
| Apply for shelter | Intake center (PATH / adult intake) | **In-person only** | — | ❌ gap |
| **`OutreachRequest`** (report a person for outreach) | NYC311 "Homeless Person Assistance" | **NYC311 / phone only** | — | ❌ **net-new** |

## The mismatch, concretely

| Source | Strength | Weakness |
|---|---|---|
| **Socrata SODA (23 datasets)** | Open, machine-readable; strong on the daily census, directories, buildings, and street-count history | Observational only; aggregate snapshots; nothing about a live individual action |
| **NYC311 (Homeless Person Assistance)** | The real action channel — reporting a person for outreach, connecting to shelter | Not a DHS surface; a generic phone/webform, no API, no OpenAPI, no JSON; not agent-accessible; no owned tracking back to DHS |

## Implications for the API-first + MCP proposal

1. **Publish the open reference data as one clean resource model.** Census, drop-in centers, facilities, contacts, and street counts behind one owned DHS contract ([OpenAPI](openapi/dhs.yaml)) — so consumers learn one model, not 23 Socrata IDs.
2. **Connect the action.** Give the core human-services transaction — reporting a person on the street for **outreach** — a machine-readable, agent-native contract instead of a 311 phone menu.
3. **Add the one net-new write workflow** — `request_outreach` (create an outreach request), with an emergency flag that routes unresponsive/medical/extreme-weather cases to 911 while dispatching the borough outreach team.
4. **Keep people private.** Census and street data stay aggregate-only; the API never exposes an individual person.
5. **MCP server** so an agent can answer "how many people were in shelter last night?", "where's the nearest drop-in center?", and — the point — "get outreach to the person at this corner and tell me the status."
