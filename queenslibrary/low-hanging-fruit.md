# Low-Hanging Fruit Index — Queens Public Library (QPL)

**Agency:** Queens Public Library (QPL) — an independent nonprofit (queenslibrary.org / queenspubliclibrary.org)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA). `queenslibrary.org` sits behind an **F5 BIG-IP ASM WAF** (`TS` cookie + a "Request Rejected / support ID" interstitial) that blocks curl and WebFetch on content paths; the **Drupal** platform is inferred from the site's `taxonomy/term` URL scheme and `/core/` paths. Fingerprinted the vendor platforms directly: **BiblioCommons** catalog (`queenslibrary.bibliocommons.com`, `x-version nerf15 9.35.0`), **Communico** events (`queens.libnet.info`, `connect.queenslibrary.org`, `Server: Communico`), **OverDrive/Libby** (`queenslibrary.overdrive.com`), and **Springshare** LibAnswers (`qpl.libanswers.com`). Verified NYC Open Data via the Socrata Discovery API: agency label `Queens Library (QBPL)` holds **exactly one** asset.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-queenslibrary.md](opendata-queenslibrary.md).

## Headline findings

1. **QPL is an independent nonprofit, not a city agency.** So it publishes almost nothing to NYC Open Data — a **single dataset**, Queens Library Branches (`kh3d-xhq7`), under `Queens Library (QBPL)`.
2. **Every patron surface is a different vendor SaaS silo.** The catalog is **BiblioCommons**, events are **Communico**, digital lending is **OverDrive/Libby + Axis 360 + hoopla**, help is **Springshare** — each with its own login and vendor API, **none an owned QPL contract**.
3. **The site is WAF-locked.** The Drupal front door sits behind an **F5 BIG-IP** WAF that rejects even a polite browser-UA crawl of content pages. No content API.
4. **The patron transactions are login-walled.** Placing/tracking a **hold**, and applying for a **card**, have no owned public API — they live only inside the BiblioCommons account.

> **Reframe (fifth distinct pattern):** Parks = *replatform* a legacy site; DOE = *reclaim* rented search + a hidden backend; Council = *consolidate + own* three fragmented APIs; NYCHA = *unlock* a service layer locked in a CRM; **QPL = federate** a nonprofit whose every surface is a separate vendor silo. Here the work is least about liberating one dataset and most about giving branches, catalog, events, digital lending, and the patron **hold**/**card** transactions a single owned, agent-native contract.

## The fruit

| # | Name | Entity | Where the data lives | Open Data twin |
|---|---|---|---|---|
| 1 | Library Branches | `Branch` | SODA + site | ✅ Queens Library Branches (`kh3d-xhq7`, 21c) |
| 2 | Catalog (books & media) | `CatalogItem` | BiblioCommons | 🟡 vendor API only |
| 3 | Events & programs | `Event` | Communico | 🟡 vendor API only |
| 4 | Digital collections | `DigitalCollection` | OverDrive/Libby, Axis 360, hoopla | 🟡 vendor APIs (siloed) |
| 5 | Get a library card | `LibraryCard` | BiblioCommons (login) | ❌ gap (net-new write) |
| 6 | My account (holds/checkouts/fines) | `BookHold` | BiblioCommons (login) | ❌ gap |
| 7 | **Place a hold (book hold)** | `BookHold` | BiblioCommons (login) | ❌ **net-new** |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **Socrata SODA** — 1 QPL dataset (branches; the one open API).
- **BiblioCommons** — catalog + patron account/holds/card; vendor API, login-walled account, no owned QPL surface.
- **Communico** — events; vendor API.
- **OverDrive/Libby, Axis 360, hoopla** — digital lending; three separate vendor silos.
- **Springshare** — LibAnswers help/FAQ.
- Platform: **Drupal** behind an **F5 BIG-IP** WAF — the fifth distinct platform after Parks' Smarty/PHP, DOE's Sitefinity/.NET, Council's WordPress, and NYCHA's Livesite + Oracle Siebel.

## Reverse-engineered entities

`Branch` · `CatalogItem` · `Event` · `DigitalCollection` · `LibraryCard` (net-new write) · `BookHold` (net-new write; place a hold) — join key **branch** + the NYC geography spine (Borough, Community Board, Council District, BIN/BBL/NTA) on branches.

## Next

1. **JSON Schema** per entity, reconciling the branch dataset columns + the vendor object models — done ([schemas/](schemas/)).
2. **OpenAPI** federating branches (open) + catalog/events/digital (vendor-locked) as clean resources + the net-new `POST /holds` (place a hold) and `POST /library-cards` — done ([openapi/queenslibrary.yaml](openapi/queenslibrary.yaml)).
3. **MCP** artifact: `find_branches`, `get_branch`, `search_catalog`, `get_catalog_item`, `find_events`, `find_digital_collections`, `list_my_holds`, `place_hold`, `apply_for_library_card` — done ([mcp/queenslibrary-mcp.json](mcp/queenslibrary-mcp.json)).
4. **The bigger prize:** a shared NYC library API across Queens, Brooklyn, and NYPL.
