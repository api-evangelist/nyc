# pubadvocate — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **New York City Public Advocate (Office of the Public Advocate)**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (Worst Landlord Watchlist, sponsored legislation, reports, public interest requests, and the net-new ombudsman intake).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (self-hosted **nginx/Ubuntu** main site, **502 during crawl**; the **Next.js/Vercel** Worst Landlord Watchlist).
- [apis-observed.md](apis-observed.md) — the **one undocumented API** (`landlordwatchlist.com/api/landlords`) vs. a **down main site** and **no intake API**.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping with coverage verdicts.
- [opendata-pubadvocate.md](opendata-pubadvocate.md) / [opendata-pubadvocate.json](opendata-pubadvocate.json) — the Open Data footprint: **zero** assets (verified), documented honestly.
- [schemas/](schemas/) — individual JSON Schema per object: `worst-landlord` · `watchlist-building` · `legislation` · `report` · `public-interest-request` · `ombudsman-complaint` (+ shared `_common`).
- [openapi/pubadvocate.yaml](openapi/pubadvocate.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/pubadvocate-mcp.json](mcp/pubadvocate-mcp.json) — design-first MCP server definition (10 agent tools; artifact, not a deployment).

## What was found — the fifth distinct pattern

The Public Advocate is the city's ombudsman, and the finding is how **little of it is machine-readable**:

1. **Zero Open Data.** No NYC Open Data asset carries a Public Advocate label (verified across four label variants). Where NYCHA publishes 24 datasets, the PA contributes nothing.
2. **The main site was down.** `advocate.nyc.gov` runs on the office's own **nginx/1.18.0 (Ubuntu)** origin — not the shared NYC.gov platform — and returned **502 Bad Gateway** on every path during the crawl.
3. **One orphan API.** The flagship **Worst Landlord Watchlist** (`landlordwatchlist.com`) is a **Next.js/Vercel** app with an **undocumented** `/api/landlords` endpoint (99 ranked landlords) — real data, no docs, off-platform.
4. **No intake API.** "Help with a city agency" is a web form / phone / email only. There is no way to file or track an `OmbudsmanComplaint` by machine.

**The gap here is almost everything.** A resident or agent has an undocumented endpoint for the Watchlist, a PDF for reports, and a web form for help.

**Reframe (vs. the earlier domains):**

| | Parks | DOE | Council | NYCHA | **Public Advocate** |
|---|---|---|---|---|---|
| Platform | Smarty/PHP (legacy) | Sitefinity (.NET) | WordPress | Livesite + Oracle Siebel | **Self-hosted nginx/Ubuntu (down) + orphan Next.js/Vercel** |
| Core problem | data as HTML, no API | search rented, backend hidden | three APIs, none owned | data open, service layer locked | **no open data, site down, one undocumented API, no intake** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** | **unlock** | **respond** |

## Reverse-engineered entities

`WorstLandlord` · `WatchlistBuilding` · `Legislation` · `Report` · `PublicInterestRequest` · `OmbudsmanComplaint` (net-new write) — join keys **landlord id**, **BBL/BIN**, **Legistar file / Intro #**, **agency**.

## Method & caveats

Outside-in crawl (browser UA; robots-respecting). The main site returned 502 throughout, so its stack was fingerprinted only from redirect/error headers (`nginx/1.18.0 (Ubuntu)`); reports/legislation/public-interest content could not be enumerated and their schemas are proposed from the office's documented functions, not scraped. The Watchlist was fingerprinted from live markup (`__NEXT_DATA__`, `/_next/`, Vercel headers) and its undocumented `/api/landlords` endpoint was read directly (99 records). Open Data absence verified via the Socrata Discovery API across four agency-label variants. A sample, not a full spider.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (zero assets, documented) ✅ · JSON Schemas (6 + common) ✅ · OpenAPI 3.1 (7 paths / 10 ops) ✅ · MCP artifact (10 tools) ✅.
- **Next:** an example implementation promoting the undocumented Watchlist route to an owned contract and standing up `file_complaint`; then the next domain from [../domains.md](../domains.md).
