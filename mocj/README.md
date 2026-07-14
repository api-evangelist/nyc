# mocj — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **NYC Mayor's Office of Criminal Justice (MOCJ)**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (programs, the one Supervised Release dataset, jail-population analysis, publications, procurement, and the net-new referral).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (a thin **NYC.gov Livesite** stub + the real site on **WordPress / WP Engine / Cloudflare**, with an accidental `wp/v2` REST API).
- [apis-observed.md](apis-observed.md) — the **one real API is accidental** (the WordPress REST API) vs. the jail numbers MOCJ links to but does not own.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (1 dataset) with coverage verdicts.
- [opendata-mocj.md](opendata-mocj.md) / [opendata-mocj.json](opendata-mocj.json) — the single MOCJ Open Data asset + column schema.
- [schemas/](schemas/) — individual JSON Schema per object: `program` · `supervised-release-docket` · `jail-population-metric` · `data-report` · `solicitation` · `program-referral` (+ shared `_common`).
- [openapi/mocj.yaml](openapi/mocj.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/mocj-mcp.json](mcp/mocj-mcp.json) — design-first MCP server definition (9 agent tools; artifact, not a deployment).

## What was found — the fifth distinct pattern

MOCJ is a **coordination office that owns almost no data**, and that is the finding:

1. **It owns almost no data.** NYC Open Data carries exactly **one** MOCJ dataset — Supervised Release Dockets (`atne-2dki`, 6 columns), unchanged since 2023.
2. **Its headline numbers belong to other agencies.** The jail-population and re-arrest figures MOCJ is known for are DOC's / NYPD's / DCJS's; the office publishes PDF *explainers* and links out.
3. **Its only real API is accidental.** The real site (`criminaljustice.cityofnewyork.us`) runs on WordPress, whose default `wp/v2` REST API exposes programs, publications, and solicitations as JSON — undocumented, unintended, unsupported.

**The gap here is ownership, not just format.** A resident, provider, or agent asking "which reentry programs serve the Bronx?" or "refer this client to supervised release" has, at best, an undocumented plugin default to scrape and no write surface at all.

**Reframe (vs. the earlier domains):**

| | Parks | DOE | Council | NYCHA | **MOCJ** |
|---|---|---|---|---|---|
| Platform | Smarty/PHP (legacy) | Sitefinity (.NET) | WordPress | Livesite + Oracle Siebel | **WordPress / WP Engine / Cloudflare** |
| Core problem | data as HTML, no API | search rented, backend hidden | three APIs, none owned | data open, service layer locked in a CRM | **owns almost no data; only an accidental WP API; jail numbers belong to others** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** | **unlock** | **route** |

## Reverse-engineered entities

`Program` · `SupervisedReleaseDocket` · `JailPopulationMetric` (aggregate; owned by other agencies) · `DataReport` · `Solicitation` · `ProgramReferral` (net-new write) — organizing vocabularies: the **Sequential Intercept Model (0-5)** and **Programs by Issue**.

## Method & caveats

Outside-in crawl (browser UA; `nyc.gov/robots.txt` only disallows `/html/misc/`). The NYC.gov stub was fingerprinted from headers (Akamai, nginx, Livesite, Dynatrace/mPulse); the real site was fingerprinted as WordPress/WP Engine/Cloudflare from headers and markup, and its content model enumerated via the public `wp/v2` REST API (counts from `x-wp-total`) without authenticating. Open Data agency label verified via the Socrata Discovery API; the one asset pulled with columns. The `JailPopulationMetric` schema is a *proposed* shape for metrics that today live only in PDF explainers and other agencies' dashboards — not a scraped dataset. The `ProgramReferral` write surface is net-new and, in any real deployment, must be authenticated, consent-gated, and minimized because it concerns justice-involved individuals.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (1 dataset) ✅ · JSON Schemas (6 + common) ✅ · OpenAPI 3.1 (9 paths/9 ops) ✅ · MCP artifact (9 tools) ✅.
- **Next:** an example implementation promoting the accidental WordPress API to an intentional one and standing up `refer_to_program`; then the next domain from [../domains.md](../domains.md).
