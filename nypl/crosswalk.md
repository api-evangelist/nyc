# Crosswalk — Website/APIs Fruit ↔ APIs ↔ NYC Open Data (NYPL)

Maps the low-hanging fruit on **nypl.org** and NYPL's developer surfaces to (a) the **existing NYPL-owned APIs** (Digital Collections, Locations, Research Catalog) and (b) the **6 NYPL datasets** on NYC Open Data. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-nypl.json](opendata-nypl.json).

## The reframe — the counter-example

- **Parks:** data-rich HTML on a legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned → *consolidate + own.*
- **NYCHA:** reference data open, resident transactions locked in a vendor CRM → *unlock.*
- **BIC:** open registry, business transactions behind a Salesforce portal → *transact.*
- **NYPL:** an independent nonprofit that has **already built and open-sourced genuinely good public APIs** for its collections, locations, and catalog → **lead.**

NYPL inverts the usual problem. For every city agency, the frustration is that the good data is trapped in HTML or a vendor system. For NYPL, the good data is **already on real, documented, NYPL-owned APIs** — the Digital Collections API, the open Locations API, and the Research Catalog `discovery-api` — and NYPL open-sources the code. What is *not* here is (1) a single unified contract across those three APIs, and (2) a clean, documented, agent-native **write** surface for the everyday transaction: placing a hold.

Coverage: ✅ real owned API · 🟡 partial/stale · ❌ gap (no clean public API).

## Entity crosswalk

| Entity | Website / surface | API today | Open Data | Cov. |
|---|---|---|---|---|
| `DigitalItem` | digitalcollections.nypl.org | **Digital Collections API** (token) `items/*` | — | ✅ owned API |
| `Collection` | digitalcollections.nypl.org | **Digital Collections API** `collections/*` | — | ✅ owned API |
| `Branch` | nypl.org/locations | **Locations API** (open, hypermedia) | Library map `p4pf-fyc4`; LIBRARY layer `feuq-due4` (thin) | ✅ owned API |
| `Event` | nypl.org/events/calendar | **Locations API** `/events` HAL link | — | ✅ owned API |
| `CatalogItem` (Bib) | nypl.org/research/research-catalog | **discovery-api** (open source) + Sierra ILS | — | ✅ owned API |
| Branch-services stats | — | — | Branch Services ×4 (`3nja-bsch`, `pfys-fabf`, `wibz-uqui`, `ne9z-skhf`) | 🟡 stale (2010-2011) |
| **`Hold`** (place a reservation) | Research Catalog account | internal services only (`on-site-hold-request-service`, `patron-eligibility-service`) | — | ❌ **net-new** (no clean public API) |
| Library-card application | nypl.org/library-card | `nypl-library-card-app` (UI) + `dgx-patron-creator-service` | — | ❌ gap (UI, no public API) — already partially exists |

## The inversion, concretely

| Source | Strength | Weakness |
|---|---|---|
| **NYPL Digital Collections API** | Real, token-authenticated, versioned Rails API; search + MODS + captures + rights over millions of items | Requires a registered token; a separate contract from Locations and Catalog |
| **NYPL Locations API** | Open, hypermedia, self-describing; hours, amenities, access, events, exhibitions | Different host/shape from the other two APIs; no write surface |
| **Research Catalog (discovery-api)** | Open-source bibliographic search over the Sierra ILS | Yet another separate contract; holds live only in the account UI |
| **NYC Open Data (6 datasets)** | — | Thin and mostly stale (2010-2011 branch stats); not where NYPL's real data lives |

## Implications for the API-first + MCP proposal

1. **Unify the three good APIs under one resource model.** Digital items, collections, branches, events, and catalog bibs behind a single owned NYPL contract ([OpenAPI](openapi/nypl.yaml)) — one auth model, one shape, instead of three.
2. **Add the one net-new write** — `place_hold` (reserve a catalog item for pickup at a branch), backed by NYPL's existing internal hold/eligibility/Sierra services, with `list_my_holds` for status.
3. **Keep patron data private.** Collections, locations, and catalog are open; holds (read and write) require the authenticated patron. No other patron's data is ever exposed.
4. **Make it agent-native.** An [MCP server](mcp/nypl-mcp.json) so an agent can answer "find public-domain maps of Harlem", "is the Schwarzman Building open now?", "what kids' programs are at the 115th Street branch this week?", and — the point — "put the new Colson Whitehead novel on hold for pickup at my branch."
5. **Hold NYPL up as the model.** This is the exemplar the other domains should be measured against: own your APIs, open-source your stack, and the only work left is packaging.
