# Crosswalk — Website/Catalog Fruit ↔ APIs ↔ NYC Open Data (Brooklyn Public Library)

Maps the low-hanging fruit on **bklynlibrary.org**, the **BiblioCommons catalog**, and the **discover** events calendar to (a) the **existing APIs** (the public Drupal JSON:API; the BiblioCommons ILS) and (b) BPL's **2** NYC Open Data assets. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-bklynlibrary.json](opendata-bklynlibrary.json).

## The reframe — fifth distinct pattern

- **Parks:** data-rich HTML on a legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned → *consolidate + own.*
- **NYCHA:** reference data wide open, service layer locked in a vendor CRM → *unlock.*
- **BPL:** a **full, public content API already exists** (an accidental Drupal JSON:API), but it is undocumented, and every **catalog transaction is locked inside the BiblioCommons ILS** → **formalize** (name/own/document the content API, front the catalog, add the hold write).

BPL inverts the usual problem twice over. First, unlike a city agency, this **nonprofit has almost no Open Data footprint** — just two file-link datasets. Second, and more surprising, its real content data is **already a working public API**: the Drupal JSON:API serves branches, events, digital collections, and e-resources as clean JSON to anyone. What is missing is (a) any documentation or ownership of that API as a product, and (b) an owned contract for the things a patron *does* — search the catalog, get a card, and above all **place a hold** — which live only behind the login-walled BiblioCommons ILS. A patron or agent asking "reserve this book for pickup at my branch" has no API to call.

Coverage: ✅ open JSON:API twin · 🟡 partial · ❌ gap (no owned API).

## Entity crosswalk

| Entity | Website / Catalog | API today | Open Data | Cov. |
|---|---|---|---|---|
| `Branch` | `/locations` | **Drupal JSON:API** `node--branch` | BPL Branches (`xmzf-uf2w`, href only) | ✅ |
| `Event` | `discover.bklynlibrary.org` | **Drupal JSON:API** `node--event` / `node--external_event` | — | ✅ (content) 🟡 (registration) |
| `CatalogItem` (book) | BiblioCommons catalog | **BiblioCommons UI only** | — | ❌ gap |
| `DigitalCollection` | `/digitalcollections` | **Drupal JSON:API** `node--digital_asset` / `finding_aid` | — | ✅ |
| `ElectronicResource` | `/eresources` | **Drupal JSON:API** `node--eres` | BPL Electronic Resources (`b7t4-zm44`, href only) | ✅ |
| `LibraryCard` | `/card` + BiblioCommons account | **webform + BiblioCommons UI** | — | ❌ gap |
| **`BookHold`** (place a hold) | BiblioCommons catalog | **BiblioCommons UI only** | — | ❌ **net-new** |

## The mismatch, concretely

| Source | Strength | Weakness |
|---|---|---|
| **Drupal JSON:API (~22 types)** | Open, machine-readable, comprehensive; strong on branches, events, collections, e-resources | Undocumented, unversioned, unadvertised; read-only; not the catalog (no bibliographic records or holds) |
| **BiblioCommons ILS** | The real catalog + transaction system — search, account, library card, holds | Login-walled vendor UI; no documented API, no OpenAPI, no JSON; not agent-accessible |

## Implications for the API-first + MCP proposal

1. **Formalize the accidental API.** Document, version, and own the JSON:API content — branches, events, digital collections, electronic resources — behind one clean BPL contract ([OpenAPI](openapi/bklynlibrary.yaml)), so consumers learn one model instead of scraping raw `node--*` endpoints.
2. **Front the catalog.** Publish catalog search + item availability from BiblioCommons as owned read resources.
3. **Add the net-new write workflows** — `place_hold` (reserve a catalog item, choose a pickup branch) and `apply_for_library_card` — that today exist only behind the vendor login or a Drupal webform.
4. **Keep patron data behind auth.** Card status, fines, and a patron's own holds are read only for the authenticated patron; the public content API stays anonymous.
5. **MCP server** so an agent can answer "which branch near me does holds pickup and is open now?", "what kids' programs are on this Saturday?", and — the point — "place a hold on this book for pickup at Central Library and tell me my queue position." BPL is one of three separate NYC library systems (NYPL, BPL, Queens); a shared library API is the larger opportunity this contract opens.
