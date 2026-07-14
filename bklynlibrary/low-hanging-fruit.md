# Low-Hanging Fruit Index — Brooklyn Public Library

**Agency:** Brooklyn Public Library (BPL) — an independent nonprofit
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt — `bklynlibrary.org/robots.txt` is a standard Drupal robots.txt disallowing `/core/`, `/admin/`, `/search/`, `/user/register`; nothing crawled was disallowed). Fingerprinted `www.bklynlibrary.org` as **Drupal behind Cloudflare** and discovered the **Drupal JSON:API is fully public** at `/jsonapi` (289 resource links, ~22 node types), enumerating `node--branch/event/book_profile/eres/digital_asset` field schemas from live records. Identified the catalog as **BiblioCommons** (`bklynlibrary.bibliocommons.com`) and the events calendar as `discover.bklynlibrary.org`. Verified the NYC Open Data agency label `Brooklyn Public Library (BPL)` via the Socrata Discovery API — only **2** assets, both `type=href` external links.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-bklynlibrary.md](opendata-bklynlibrary.md).

## Headline findings

1. **BPL is an independent nonprofit**, not a city agency — so it has almost no Open Data footprint (2 file-link datasets) and runs its own stack: **Drupal** (Cloudflare) + the **BiblioCommons** catalog + a `discover` events calendar.
2. **A full, public content API already exists.** The Drupal **JSON:API** is open at `www.bklynlibrary.org/jsonapi` — ~22 content types (`branch`, `event`, `book_profile`, `digital_asset`, `eres`, finding aids…) served as read-only JSON. Real and comprehensive, but **undocumented and unadvertised**.
3. **The catalog transaction layer is locked.** Catalog search, the patron account/library card, and — the everyday transaction — **placing a hold** live only inside the login-walled **BiblioCommons** ILS. None has an owned public API.
4. **Applying for a card is a webform**, not an API (`webform_submission--library_card_access`, the `/card` flow).

> **Reframe (fifth distinct pattern):** Parks = *replatform*; DOE = *reclaim*; Council = *consolidate + own*; NYCHA = *unlock*; **BPL = formalize.** Here a public content API already exists — the work is least about liberating data and most about **naming, versioning, documenting, and owning** the accidental JSON:API, fronting the vendor catalog, and giving the core patron transaction (placing a **hold**) an owned, agent-native contract.

## The fruit

| # | Name | Entity | Where the data lives | Machine-readable today |
|---|---|---|---|---|
| 1 | Library Branches | `Branch` | Drupal JSON:API `node--branch` | ✅ full address/hours/geo/services |
| 2 | Events & Programs | `Event` | Drupal JSON:API `node--event` + `discover` | ✅ content (🟡 registration) |
| 3 | Catalog (books) | `CatalogItem` | BiblioCommons ILS | ❌ gap (no owned API) |
| 4 | Digital Collections | `DigitalCollection` | Drupal JSON:API `node--digital_asset` / `finding_aid` | ✅ |
| 5 | Electronic Resources | `ElectronicResource` | Drupal JSON:API `node--eres` | ✅ |
| 6 | Get a library card | `LibraryCard` | Drupal webform + BiblioCommons account | ❌ gap (no API) |
| 7 | **Place a hold (reservation)** | `BookHold` | BiblioCommons catalog | ❌ **net-new** |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **Drupal JSON:API** — `www.bklynlibrary.org/jsonapi`, fully public, ~22 content types (the accidental API to formalize).
- **BiblioCommons ILS** — the catalog/holds/account; login-walled, no documented API.
- **discover.bklynlibrary.org** — the events calendar (PHP/Cloudflare).
- Platform: **Drupal behind Cloudflare** — the fifth distinct platform after Parks' Smarty/PHP, DOE's Sitefinity/.NET, Council's WordPress, and NYCHA's NYC.gov Livesite + Oracle Siebel.
- NYC Open Data: only **2** BPL assets, both external file links (no SODA) — nonprofit, no mandate.

## Reverse-engineered entities

`Branch` · `Event` · `CatalogItem` (BiblioCommons; net-new read) · `DigitalCollection` · `ElectronicResource` · `LibraryCard` (net-new write; also the webform-locked card application) · `BookHold` (net-new write; the hold locked in BiblioCommons) — join keys: **Branch ID**, ISBN/BiblioCommons item id.

## Next

1. **JSON Schema** per entity, reconciling real JSON:API field names (`field_branchid`, `field_hours_*`, `field_position`, `field_eres_*`, `field_da_*`) and the BiblioCommons catalog record — done ([schemas/](schemas/)).
2. **OpenAPI** documenting the open content as clean resources + fronting the catalog + the net-new `POST /holds` (place a hold) and `POST /library-card/applications` — done ([openapi/bklynlibrary.yaml](openapi/bklynlibrary.yaml)).
3. **MCP** artifact: `find_branches`, `get_branch`, `find_events`, `get_event`, `search_catalog`, `get_catalog_item`, `find_digital_collections`, `find_electronic_resources`, `get_my_library_card`, `apply_for_library_card`, `list_my_holds`, `place_hold`, `get_hold` — done ([mcp/bklynlibrary-mcp.json](mcp/bklynlibrary-mcp.json)).
