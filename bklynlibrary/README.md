# bklynlibrary — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of **Brooklyn Public Library (BPL)** — an independent nonprofit — through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (branches, events, catalog, digital collections, e-resources, and the locked catalog transactions).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (**Drupal** + Cloudflare; the accidental public **JSON:API**; the **BiblioCommons** catalog; the `discover` events calendar).
- [apis-observed.md](apis-observed.md) — the **already-open content API** (Drupal JSON:API, ~22 types) vs. the **BiblioCommons ILS with no documented API**.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping with coverage verdicts.
- [opendata-bklynlibrary.md](opendata-bklynlibrary.md) / [opendata-bklynlibrary.json](opendata-bklynlibrary.json) — BPL's 2 NYC Open Data assets (both external file links — no SODA).
- [schemas/](schemas/) — individual JSON Schema per object: `branch` · `event` · `catalog-item` · `digital-collection` · `electronic-resource` · `library-card` · `book-hold` (+ shared `_common`).
- [openapi/bklynlibrary.yaml](openapi/bklynlibrary.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/bklynlibrary-mcp.json](mcp/bklynlibrary-mcp.json) — design-first MCP server definition (13 agent tools; artifact, not a deployment).

## What was found — the fifth distinct pattern

BPL inverts the usual problem, and that inversion is the finding:

1. **A public content API already exists.** The Drupal **JSON:API** is open at `www.bklynlibrary.org/jsonapi` — ~22 content types (`node--branch` with full address/hours/geo/services, `node--event`, `node--digital_asset`, `node--eres`, finding aids, and more) served as read-only JSON. It is real and comprehensive, but **undocumented, unversioned, and unadvertised**.
2. **The catalog transaction layer is locked.** The **BiblioCommons** ILS (`bklynlibrary.bibliocommons.com`) holds the bibliographic catalog, patron account, library card, and **holds** — login-walled, **no documented API**. Applying for a card is a Drupal webform.

**The gap here is transactions and documentation, not raw data.** A patron or agent asking "reserve this book at my branch" or "what's my hold's queue position?" has nothing owned to call — while, ironically, the branch and event data is already open.

**Reframe (vs. the earlier domains):**

| | Parks | DOE | Council | NYCHA | **BPL** |
|---|---|---|---|---|---|
| Platform | Smarty/PHP | Sitefinity (.NET) | WordPress | NYC.gov Livesite + Oracle Siebel | **Drupal (Cloudflare) + BiblioCommons ILS** |
| Core problem | data as HTML, no API | search rented, backend hidden | three APIs, none owned | data open, service layer locked in a CRM | **content API exists but accidental; catalog locked in a vendor ILS** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** | **unlock** | **formalize** |

## Reverse-engineered entities

`Branch` · `Event` · `CatalogItem` (BiblioCommons) · `DigitalCollection` · `ElectronicResource` · `LibraryCard` (net-new write) · `BookHold` (net-new write) — join keys **Branch ID**, ISBN / BiblioCommons item id.

## Method & caveats

Outside-in crawl (browser UA; `bklynlibrary.org/robots.txt` is a standard Drupal file). The site was fingerprinted from headers and markup (Cloudflare, `drupal-settings-json`); the JSON:API was enumerated from its own public resource index and live records without authenticating. The catalog was identified as BiblioCommons from redirect/cookie evidence; its internal hold/account workflows are inferred from BPL's documented patron services, not scraped behind login. Open Data agency label verified via the Socrata Discovery API — only 2 BPL assets, both `type=href`. A sample, not a full spider.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (2 assets) ✅ · JSON Schemas (7 + common) ✅ · OpenAPI 3.1 (13 paths/ops) ✅ · MCP artifact (13 tools) ✅.
- **Next:** an example implementation documenting the JSON:API and fronting BiblioCommons for `place_hold`; then converge NYPL / BPL / Queens toward a shared library API; then the next domain from [../domains.md](../domains.md).
