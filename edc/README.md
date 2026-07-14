# edc — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **New York City Economic Development Corporation (EDC)**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (projects, real estate, solicitations, the company map, ferry ridership, WiredNYC, and the net-new solicitation-response write).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (**Drupal behind a Cloudflare bot challenge**; NYC Ferry on Cloudflare + CloudFront).
- [apis-observed.md](apis-observed.md) — the **near-absence** of APIs (5 peripheral Socrata datasets, a bot-walled Drupal site, no EDC API).
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (5 EDC datasets) with coverage verdicts.
- [opendata-edc.md](opendata-edc.md) / [opendata-edc.json](opendata-edc.json) — all 5 EDC Open Data assets + column schemas, sorted by page views.
- [schemas/](schemas/) — individual JSON Schema per object: `development-project` · `property-asset` · `solicitation` · `mapped-company` · `ferry-ridership` · `wired-building` · `rfp-response` (+ shared `_common`).
- [openapi/edc.yaml](openapi/edc.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/edc-mcp.json](mcp/edc-mcp.json) — design-first MCP server definition (11 agent tools; artifact, not a deployment).

## What was found — the fifth distinct pattern

EDC is a **public benefit corporation**, and the finding is how little of it is machine-readable:

1. **Only peripheral data is published.** Just **5 NYC Open Data datasets** carry the EDC label — a marketing company map (**Mapped In NY**, `f4yq-wry5`), **NYC Ferry ridership** (`t5n6-gx8c`), and three **WiredNYC** broadband-certification tables. None touches EDC's mission.
2. **The core business is dark.** EDC's **~60M sq ft real-estate portfolio**, its **development projects**, and its **solicitations (RFPs/RFEIs)** have no Open Data twin and no API. They live only as Drupal pages on edc.nyc — and that site is **sealed behind a Cloudflare bot challenge** (403 to non-browser clients), so even the pages can't be reliably scraped.

**The gap here is coverage, not format or transactions.** A partner or agent asking "what is EDC soliciting?" or "what EDC property is available?" has nothing to call and nothing to scrape.

**Reframe (vs. the earlier domains):**

| | Parks | DOE | Council | NYCHA | **EDC** |
|---|---|---|---|---|---|
| Platform | Smarty/PHP (legacy) | Sitefinity (.NET) | WordPress | NYC.gov Livesite + Oracle Siebel | **Drupal behind Cloudflare (bot-walled)** |
| Core problem | data as HTML, no API | search rented, backend hidden | three APIs, none owned | data open, service layer locked | **core business not published at all** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** | **unlock** | **surface** |

## Reverse-engineered entities

`DevelopmentProject` · `PropertyAsset` (EDC-managed real estate) · `Solicitation` (RFP/RFEI/RFQ/RFI) · `MappedCompany` · `FerryRidership` · `WiredBuilding` · `RFPResponse` (net-new write) — join keys **BBL**, **BIN**, neighborhood, and the NYC geography spine.

## Method & caveats

Outside-in crawl (browser UA; `edc.nyc/robots.txt` fetches, but page HTML is Cloudflare-challenged with a 403). The platform was fingerprinted from `robots.txt` (Drupal) and response headers (Cloudflare, CloudFront on ferry.nyc). Open Data agency label verified via the Socrata Discovery API; all 5 assets pulled with columns. Because the site is bot-walled, the **core entities (projects, assets, solicitations) are modeled from EDC's documented site structure, not scraped** — treat them as an owned-API proposal, not a live feed.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (5 datasets) ✅ · JSON Schemas (7 + common) ✅ · OpenAPI 3.1 (11 paths/12 ops) ✅ · MCP artifact (11 tools) ✅.
- **Next:** an example implementation surfacing EDC's projects/assets/solicitations and fronting the solicitation-response workflow; then the next domain from [../domains.md](../domains.md).
