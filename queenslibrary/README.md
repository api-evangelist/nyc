# queenslibrary — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of **Queens Public Library (QPL)** — an independent nonprofit — through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (branches, catalog, events, digital collections, and the login-walled patron transactions).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (**Drupal** behind an **F5 BIG-IP** WAF; **BiblioCommons** catalog; **Communico** events; **OverDrive/Libby + Axis 360 + hoopla** digital; **Springshare** help).
- [apis-observed.md](apis-observed.md) — the **one open API** (Socrata SODA, a single dataset) vs. **five vendor SaaS silos**, none an owned QPL API.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping with coverage verdicts.
- [opendata-queenslibrary.md](opendata-queenslibrary.md) / [opendata-queenslibrary.json](opendata-queenslibrary.json) — the sole QPL Open Data asset + column schema.
- [schemas/](schemas/) — individual JSON Schema per object: `branch` · `catalog-item` · `event` · `digital-collection` · `library-card` · `book-hold` (+ shared `_common`).
- [openapi/queenslibrary.yaml](openapi/queenslibrary.yaml) — OpenAPI 3.1 contract `$ref`ing each object, with the net-new `POST /holds` and `POST /library-cards`.
- [mcp/queenslibrary-mcp.json](mcp/queenslibrary-mcp.json) — design-first MCP server definition (9 agent tools; artifact, not a deployment).

## What was found — the fifth distinct pattern

QPL is the first **non-agency** domain, and that is the finding:

1. **It's a nonprofit, so almost nothing is on Open Data.** Verified via the Socrata Discovery API: agency label `Queens Library (QBPL)` holds **exactly one** dataset — Queens Library Branches (`kh3d-xhq7`, 21c).
2. **Every patron surface is a different vendor SaaS silo.** The catalog is **BiblioCommons**, events are **Communico**, digital lending is **OverDrive/Libby + Axis 360 + hoopla**, help is **Springshare** — each with its own login and vendor API, **none an owned QPL contract**. The Drupal site itself sits behind an **F5 BIG-IP** WAF that rejects browser-UA crawls.

**The gap here is federation, not liberation.** QPL's data mostly *is* machine-readable — just scattered across five vendor systems with five models and logins, and the patron transactions (holds, cards) are trapped behind a BiblioCommons account.

**Reframe (vs. the earlier domains):**

| | Parks | DOE | Council | NYCHA | **QPL** |
|---|---|---|---|---|---|
| Platform | Smarty/PHP (legacy) | Sitefinity (.NET) | WordPress | Livesite + Oracle Siebel | **Drupal (F5 WAF) + BiblioCommons + Communico + OverDrive/Axis 360/hoopla + Springshare** |
| Core problem | data as HTML, no API | search rented, backend hidden | three APIs, none owned | data open, service layer locked in a CRM | **nonprofit; every surface a separate vendor silo, only branches open** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** | **unlock** | **federate** |

## Reverse-engineered entities

`Branch` · `CatalogItem` · `Event` · `DigitalCollection` · `LibraryCard` (net-new write) · `BookHold` (net-new write; place a hold) — join key **branch** + the NYC geography spine on branches.

## Method & caveats

Outside-in crawl (browser UA). The `queenslibrary.org` site is behind an **F5 BIG-IP ASM** WAF that returns a 244-byte "Request Rejected / support ID" page to curl and WebFetch on content paths, so the **Drupal** platform is inferred from the site's `taxonomy/term` URL scheme and `/core/` paths rather than a header. The vendor platforms were fingerprinted directly from their own hosts and headers (BiblioCommons `x-version nerf15`, Communico `Server:` header, OverDrive host, Springshare `x-backend-server`). Open Data agency label and its single asset verified via the Socrata Discovery API. Vendor internal APIs (BiblioCommons/Communico/OverDrive) are documented as *existing* but were not exercised behind login; the patron workflows are inferred from QPL's public help pages, not scraped.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (1 dataset) ✅ · JSON Schemas (6 + common) ✅ · OpenAPI 3.1 (9 paths / 10 ops) ✅ · MCP artifact (9 tools) ✅.
- **Next:** an example implementation federating BiblioCommons + Communico + OverDrive behind `place_hold`; and — the bigger prize — a **shared NYC library API** across Queens, Brooklyn (BPL), and The New York Public Library (NYPL), which are three separate nonprofits with separate catalogs, cards, and vendor stacks. Then the next domain from [../domains.md](../domains.md).
