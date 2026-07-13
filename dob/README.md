# dob — Low-Hanging Fruit Assessment

Fourth domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **NYC Department of Buildings (DOB)**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (buildings, filings, permits, violations, complaints, C of O, the DOB NOW filing surface).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (citywide NYC.gov CMS + the `aNNN-*.nyc.gov` app layer: BIS Web, DOB NOW, eFiling; Akamai/Dynatrace/mPulse).
- [apis-observed.md](apis-observed.md) — the interfaces observed: the Open Data **nightly batch dump** and the browser-only, API-less app layer.
- [crosswalk.md](crosswalk.md) — fruit ↔ app layer ↔ Open Data mapping (44 DOB datasets) with coverage verdicts.
- [opendata-dob.md](opendata-dob.md) / [opendata-dob.json](opendata-dob.json) — all 44 DOB Open Data datasets + column schemas of the anchors.
- [schemas/](schemas/) — individual JSON Schema per object: `building` · `job-filing` · `permit` · `violation` · `complaint` · `certificate-of-occupancy` · `permit-application` (net-new) (+ shared `_common`).
- [openapi/dob.yaml](openapi/dob.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/dob-mcp.json](mcp/dob-mcp.json) — design-first MCP server definition (10 agent tools; artifact, not a deployment).

## What was found — the fourth distinct pattern

DOB is the project's proof that **the real legacy surface is the application layer, not the website.** `www.nyc.gov/site/buildings` is brochureware on the citywide NYC.gov CMS. Everything that matters lives in the numbered legacy applications:

1. **BIS Web** (`a810-bisweb.nyc.gov`) — the legacy **Building Information System**, per-building system of record. Browser-only, Akamai-gated.
2. **DOB NOW** (`a810-dobnow.nyc.gov`) — the modern filing/permitting portal (jobs, permits, C of O, elevator/boiler/facade safety). Browser-only, Akamai "Access Denied" to non-browser clients.
3. **eFiling** (`a810-efiling.nyc.gov`) — Apache Tomcat/9.0.117 (Java).

**None exposes a public API.** The single machine-readable DOB surface is **NYC Open Data** — 44 datasets — but every one is a **nightly one-way batch dump** (the `DOBRunDate` column proves it). You can read yesterday's filings; you cannot transact.

**The modernization verb: _Transact._** DOB is data-rich but transaction-closed. The work is to put an owned, live, two-way API in front of the app layer — and to add the one thing no interface offers today: **filing a permit application** through an API.

**The net-new write object: `PermitApplication`** — an API-first DOB NOW filing you can create, submit, and track programmatically.

**Reframe (vs. the first three domains):**

| | Parks | DOE | Council | **DOB** |
|---|---|---|---|---|
| Platform | Smarty/PHP (legacy) | Sitefinity (.NET) | WordPress / WP Engine | **NYC.gov CMS + `aNNN` app layer** |
| Core problem | data as HTML, no API | search rented, backend hidden | three APIs, none owned/unified | **transactional apps, no API; only a nightly dump** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** | **transact** |

## Reverse-engineered entities

`Building` (BIN/BBL — the join spine) · `JobFiling` · `Permit` · `Violation` (DOB + ECB) · `Complaint` · `CertificateOfOccupancy` · **`PermitApplication`** (net-new write) — join keys **BIN**, **BBL**, **Job #**, and the shared geography spine (community board, council district, census tract, NTA, bbl, bin).

## Method & caveats

Outside-in crawl (browser UA; nyc.gov robots.txt disallows only `/html/misc/`). The app-layer hosts (`a810-dobnow`, `a810-bisweb`) return Akamai "Access Denied" to non-browser clients, so they were characterized from headers, not spidered. Open Data verified via the Socrata catalog API (agency label "Department of Buildings (DOB)", 44 datasets). A sample and a design-first proposal, not a full spider or a deployment.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed (Open Data batch dump + API-less app layer) ✅ · Open Data crosswalk (44 datasets) ✅ · JSON Schemas (7) ✅ · OpenAPI 3.1 (17 ops) ✅ · MCP artifact (10 tools) ✅.
- **Next:** an example implementation fronting BIS/DOB NOW for live reads + the net-new `PermitApplication` write; then the next domain from [../domains.md](../domains.md).
