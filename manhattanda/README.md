# manhattanda — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **Manhattan District Attorney's Office** (New York County District Attorney), through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (newsroom, bureaus/initiatives, victim resources, offices, aggregate prosecution reporting, and the un-built tip intake).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (**WordPress** + "dany" theme behind **Sucuri CloudProxy**; **Jetpack Search**; FOIL delegated to **NYC OpenRecords**).
- [apis-observed.md](apis-observed.md) — the **one accidental API** (WordPress REST over the newsroom) vs. everything the office *does* having no API.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping with coverage verdicts.
- [opendata-manhattanda.md](opendata-manhattanda.md) / [opendata-manhattanda.json](opendata-manhattanda.json) — the verified **zero** NYC Open Data assets (and how that was confirmed).
- [schemas/](schemas/) — individual JSON Schema per object: `press-release` · `program` · `victim-service` · `office` · `prosecution` · `tip-submission` (+ shared `_common`).
- [openapi/manhattanda.yaml](openapi/manhattanda.yaml) — OpenAPI 3.1 contract `$ref`ing each object, with the net-new `POST /tips`.
- [mcp/manhattanda-mcp.json](mcp/manhattanda-mcp.json) — design-first MCP server definition (9 agent tools; artifact, not a deployment).

## What was found — the fifth distinct pattern

The Manhattan DA **inverts NYCHA**. NYCHA had too much open data and a locked service layer; the DA has almost **no structured surface at all**:

1. **No open data.** As an independently elected county prosecutor, the office is outside the mayoral NYC Open Data program. Four agency-label queries against the Socrata Discovery API return **zero** datasets.
2. **The only machine-readable object is accidental.** The newsroom (~3,029 posts) is JSON solely because WordPress ships a REST API. Everything the office *does* — prosecute, run bureaus and diversion programs, help victims, take tips — is HTML or prose.
3. **Core workflows are outsourced or un-built.** **FOIL is delegated to NYC OpenRecords** (off the DA's own domain); **tip intake is un-built** (a generic reCAPTCHA contact form is the only write path).

**The gap here is contracts, not liberation.** There is little to free from open data because there is no open data — the work is to *define* machine-readable objects where none exist.

**Reframe (vs. the earlier domains):**

| | Parks | DOE | Council | NYCHA | **Manhattan DA** |
|---|---|---|---|---|---|
| Platform | Smarty/PHP (legacy) | Sitefinity (.NET) | WordPress | Livesite + Oracle Siebel | **WordPress + Sucuri** |
| Core problem | data as HTML, no API | search rented, backend hidden | three APIs, none owned | data open, service layer locked | **no open data; only an accidental WP feed; FOIL delegated; tips un-built** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** | **unlock** | **standardize** |

**All five NYC District Attorneys share the same functions** — newsroom, bureaus, victim services, FOIL, tips. This is a candidate for **one shared DA API**: design the contract once (as here) and let Bronx, Brooklyn (Kings), Queens, and Staten Island (Richmond) adopt it, rather than building five silos.

## Reverse-engineered entities

`PressRelease` · `Program` (bureaus/units/initiatives; diversion, conviction integrity) · `VictimService` · `Office` · `Prosecution` (aggregate only; never an individual case) · `TipSubmission` (net-new write) — organizing keys: **crime category**, **bureau**.

## Method & caveats

Outside-in crawl (browser UA; no `robots.txt` served). The stack was fingerprinted from headers and markup (Sucuri, WordPress, the "dany" theme, Jetpack/Tribe/WPForms REST namespaces); the newsroom volume is from the live `x-wp-total` header. The absence of open data was verified with four exact agency-label queries plus keyword searches against the Socrata Discovery API. Because there are no Open Data columns to reconcile, the schemas are **design-first** — reverse-engineered from the site's own structure, with only `PressRelease` backed by a real feed. FOIL is documented from the Contact page's own text.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (verified zero) ✅ · JSON Schemas (6 + common) ✅ · OpenAPI 3.1 (7 paths / 9 ops) ✅ · MCP artifact (9 tools) ✅.
- **Next:** generalize this into **one shared DA API** across the other four borough District Attorneys; then the next domain from [../domains.md](../domains.md).
