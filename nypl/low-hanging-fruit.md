# Low-Hanging Fruit Index — NYPL

**Agency:** New York Public Library (NYPL) — an independent nonprofit serving Manhattan, the Bronx, and Staten Island
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA; `www.nypl.org` sits behind Imperva Incapsula, so its headers are edge-obscured). Probed NYPL's **own public APIs** directly — the **Digital Collections API** (`api.repo.nypl.org/api/v2`, returns `401 HTTP Basic: Access denied` without a token; Rails + Phusion Passenger) and the open, hypermedia **Locations API** (`refinery.nypl.org/api/nypl/locations/v1.0`; PHP Slim, `NYPL\Refinery\Server`). Enumerated the **github.com/NYPL** open-source org. Verified the NYC Open Data agency label `New York Public Library (NYPL)` via the Socrata Discovery API — only **6** assets, mostly stale.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-nypl.md](opendata-nypl.md).

## Headline findings

1. **NYPL is the counter-example of this whole project.** Where nearly every NYC agency traps its data in HTML or a vendor CRM, NYPL — a nonprofit, not a city agency — has already **built and operated genuinely good public APIs** for years, and open-sources the code.
2. **Three real, owned APIs.** The **Digital Collections API** (token-authenticated Rails, over millions of digitized items with MODS metadata, captures, and rights); the **Locations API** (open hypermedia, with hours, amenities, access, and links to events/exhibitions/alerts); and the **Research Catalog** behind the open-source `discovery-api` + Sierra ILS.
3. **Exemplary ownership.** Nearly the entire stack is on **github.com/NYPL** — the `nypl-core` ontology, an accessibility-first React design system, a web-based ebook reader, and patron/hold/Sierra microservices.
4. **NYC Open Data is a thin afterthought.** Only **6** NYPL datasets, mostly **stale 2010-2011** branch-services stats plus a facilities layer. NYPL's living data is on its own APIs, not Open Data.

> **Reframe (the counter-example):** Parks = *replatform*; DOE = *reclaim*; Council = *consolidate + own*; NYCHA = *unlock*; BIC = *transact*; **NYPL = lead.** Here the data is already on owned, open-sourced APIs. The work is least about liberating anything and most about (1) **unifying** three separate contracts into one resource model and (2) closing the single gap — a clean, agent-native **write** API for placing a hold.

## The fruit

| # | Name | Entity | Where the data lives | Owned API / Open Data |
|---|---|---|---|---|
| 1 | Digital Collections (items) | `DigitalItem` | Digital Collections API | ✅ owned API (token) |
| 2 | Digital Collections collections | `Collection` | Digital Collections API | ✅ owned API (token) |
| 3 | Branches, hours & amenities | `Branch` | Locations API | ✅ owned API (open) |
| 4 | Events, classes & exhibitions | `Event` | Locations API `/events` | ✅ owned API (open) |
| 5 | Research & circulating catalog | `CatalogItem` | discovery-api + Sierra | ✅ owned API (open source) |
| 6 | Branch-services statistics | `Branch` | NYC Open Data (×4) | 🟡 stale (2010-2011) |
| 7 | **Place a hold (reservation)** | `Hold` | Research Catalog account | ❌ **net-new** (internal services only) |
| 8 | Library-card application | `Hold` | nypl.org/library-card | ❌ gap (UI app; already partial) |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **Digital Collections API** (`api.repo.nypl.org/api/v2`) — token-authenticated Rails; the flagship owned API.
- **Locations API** (`refinery.nypl.org`) — open hypermedia PHP/Slim; hours, amenities, events, exhibitions.
- **discovery-api** — open-source Research Catalog API over the **Sierra** ILS (`ruby-sierra-api-client`).
- **github.com/NYPL** — `nypl-core` ontology, `nypl-design-system`, `web-reader`, and patron/hold microservices (`on-site-hold-request-service`, `patron-eligibility-service`, `nypl-hold-request-consumer`, `dgx-patron-creator-service`).
- Infra/vendors: **Imperva Incapsula** (edge), **AWS** (ALB), **New Relic** (monitoring). The only system-of-record vendor is the **Sierra ILS**.

## Reverse-engineered entities

`DigitalItem` · `Collection` · `Branch` (Location) · `Event` · `CatalogItem` (Bib/Book) · `Hold` (net-new write; also stands in for the library-card application workflow) — join keys: **UUID** (Digital Collections), Locations **slug**, and Sierra **bib id**. A `ResearchDivision` is carried as a field on items and collections.

## Next

1. **JSON Schema** per entity, reconciling real API payloads (Digital Collections UUID + MODS, Locations `hours_data`/`geolocation`, Sierra bib/item availability) — done ([schemas/](schemas/)).
2. **OpenAPI** unifying the three owned APIs as clean resources + the net-new `POST /holds` — done ([openapi/nypl.yaml](openapi/nypl.yaml)).
3. **MCP** artifact: `search_digital_collections`, `get_digital_item`, `list_collections`, `find_branches`, `get_branch`, `get_branch_events`, `find_events`, `search_catalog`, `get_catalog_item`, `list_my_holds`, `place_hold` — done ([mcp/nypl-mcp.json](mcp/nypl-mcp.json)).
