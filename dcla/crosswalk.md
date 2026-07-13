# Crosswalk — Website/Portal Fruit ↔ APIs ↔ NYC Open Data (DCLA)

Maps the low-hanging fruit on **nyc.gov/site/dcla** and the **Grants Management System** to (a) the **existing APIs** (Socrata SODA; the Salesforce portal) and (b) the **9 DCLA datasets** on NYC Open Data. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-dcla.json](opendata-dcla.json).

## The reframe — the grantmaker pattern

- **Parks:** data-rich HTML on a legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned → *consolidate + own.*
- **NYCHA:** reference data open, resident transactions locked in an Oracle Siebel CRM → *unlock.*
- **DCWP:** whole regulated-business lifecycle open across 37 datasets, no owned contract, two citizen writes locked → *bind + add the writes.*
- **DCLA:** the funding **outcomes** are open (9 datasets — who was funded, the org directory, public art, MFTA), but the grant **application** is locked in a Salesforce Experience Cloud portal, and no owned API binds an organization to its funding → **open the grant pipeline.**

DCLA is a grantmaker. It publishes the *results* of its grantmaking generously — awards, the geocoded cultural-organization directory, Cultural Institutions Group support, completed Percent for Art commissions, and Materials for the Arts summaries. But the thing an organization actually *does* — **apply** to the Cultural Development Fund — lives only behind the login-walled Salesforce Grants Management System. An organization or agent asking "what's the status of my application?" or "apply for this grant" has no API to call.

Coverage: ✅ strong open twin · 🟡 partial/aggregate · ❌ gap (no API).

## Entity crosswalk

| Entity | Website / Portal | API today | Open Data | Cov. |
|---|---|---|---|---|
| `CulturalOrganization` | `/` directory | SODA | Cultural Organizations (`u35m-9t32`, 16c); Cultural Organization Resources (`rb2h-bgai`) | ✅ |
| `ProgramFunding` (grant award) | `/cultural-funding/programs-funding` | SODA | Programs Funding (`y6fv-k6p7`); FY11 (`rskq-5bfv`); FY2010 (`j8p3-8ufc`) | ✅ |
| `CapitalFunding` | `/cultural-funding/capital-funding` | SODA | Capital Funding (`7hgn-sgmk`, 6c) | ✅ |
| `CulturalInstitution` (CIG) | `/cultural-funding/city-owned-institutions` | SODA | Cultural Institutions Group Funding (`ka27-qx5k`) | ✅ |
| `PublicArtwork` (Percent for Art) | `/publicart/percent-for-art` | SODA | Completed Percent for Art projects (`gzdv-qiga`, 7c) | ✅ |
| `MaterialsForTheArts` | `/programs/materials-for-the-arts` | SODA | MFTA Donor Information (`vhtt-kpwy`) — **aggregate only** | 🟡 aggregate |
| **`GrantApplication`** (apply for a grant) | Grants Management System | **Salesforce UI only** | — | ❌ **net-new** |

## The mismatch, concretely

| Source | Strength | Weakness |
|---|---|---|
| **Socrata SODA (9 datasets)** | Open, machine-readable; strong on funding outcomes, the geocoded org directory, public art, and MFTA | Publishes only the *outcome* (who was funded); thin join keys (organization name + application #, no stable org id); nothing about the live application pipeline |
| **Salesforce Grants Management System** | The real transaction system — register, apply, submit, and track a Cultural Development Fund grant | Login-walled Salesforce Experience Cloud community; no public API, no OpenAPI, no JSON; not agent-accessible |

## Implications for the API-first + MCP proposal

1. **Publish the open funding data as one clean resource model.** Cultural organizations, program and capital funding, CIG support, public artworks, and MFTA behind one owned DCLA contract ([OpenAPI](openapi/dcla.yaml)) — so consumers learn one model, not 9 Socrata IDs.
2. **Open the grant pipeline.** Front the Salesforce portal with an API so the core transaction — submitting and tracking a **grant application** — has a machine-readable, agent-native contract.
3. **Add the one net-new write workflow** — `apply_for_grant` (create a Cultural Development Fund application), with the requested amount, program, and project narrative.
4. **Keep donors private.** Materials for the Arts stays aggregate-only; the API never exposes an individual donor.
5. **MCP server** so an agent can answer "which Bronx dance organizations did DCLA fund last year?", "what has this museum received in capital funding?", and — the point — "apply for a Cultural Development Fund grant and tell me the status."
