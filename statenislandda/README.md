# statenislandda — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **Office of the District Attorney, Richmond County (Staten Island DA)**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (press releases, programs, victim services, scam advisories, the dark caseload data, and the tip forms).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (self-hosted **WordPress** / Themeco "Pro" on **SiteGround**; Contact Form 7; a bot-protection captcha).
- [apis-observed.md](apis-observed.md) — the **no-API** finding: a bot-walled WordPress `/wp-json`, two Contact Form 7 email forms, and zero Open Data.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (all gaps) with coverage verdicts.
- [opendata-statenislandda.md](opendata-statenislandda.md) / [opendata-statenislandda.json](opendata-statenislandda.json) — the honest **zero** — no Socrata assets under any DA label.
- [schemas/](schemas/) — individual JSON Schema per object: `press-release` · `program` · `victim-service` · `community-resource` · `prosecution-statistics` · `tip-submission` (+ shared `_common`).
- [openapi/statenislandda.yaml](openapi/statenislandda.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/statenislandda-mcp.json](mcp/statenislandda-mcp.json) — design-first MCP server definition (9 agent tools; artifact, not a deployment).

## What was found — the emptiest domain yet

The Staten Island DA is an **off-platform, data-dark** domain, and that emptiness is the finding:

1. **Wrong address, dead legacy.** The expected `rcda.nyc.gov` no longer resolves; the office runs its own site at **`statenislandda.org`** — self-hosted WordPress (Themeco "Pro") on **SiteGround**, off the NYC.gov chassis entirely.
2. **No data.** **Zero** NYC Open Data datasets. The core prosecution data — caseloads, dispositions, diversions — is **dark**, surfacing only as prose in press releases.
3. **No API.** The only latent API (WordPress `/wp-json`) is undocumented and **bot-walled** by a SiteGround captcha that also blocks agents from reading the content at all.
4. **One transaction, as email.** Submitting a confidential tip is a pair of **Contact Form 7** forms (`/drug-tip-form/`, `/scam-tip-form/`) — no ticket, no status, no contract.

**The gap here is everything.** A resident or agent asking "how many gun cases did the DA prosecute?" or "file a scam tip and give me a reference number" has nothing to call.

**Reframe (vs. the earlier domains):**

| | Council | NYCHA | **Staten Island DA** |
|---|---|---|---|
| Platform | WordPress | NYC.gov Livesite + Oracle Siebel | **Self-hosted WordPress on SiteGround (off-platform)** |
| Core problem | three APIs, none owned | data open, service layer locked in a CRM | **no data, no API, bot-walled; core case data dark** |
| Modernization verb | **consolidate + own** | **unlock** | **surface** |

## The strategic prize — one shared five-borough DA API

All five NYC District Attorney offices — Manhattan, Brooklyn, Queens, the Bronx, and Staten Island — do the **same things**: publish press releases, run prosecution bureaus and community programs, offer victim services, take confidential tips, and (should) report aggregate caseload statistics. Yet each runs a separate stack on a separate domain (`manhattanda.org`, `brooklynda.gov`, `queensda.org`, `bronxda.nyc.gov`, `statenislandda.org`), and none publishes structured data. The schemas and OpenAPI here are deliberately **generic** — a template for a single shared **five-borough DA API** rather than five one-off builds. Surfacing Staten Island is step one; the reusable model is the point.

## Reverse-engineered entities

`PressRelease` · `Program` · `VictimService` · `CommunityResource` · `ProsecutionStatistics` (aggregate only) · `TipSubmission` (net-new write) — no natural join keys beyond WordPress slugs and the NYC geography spine (Richmond County = Staten Island; Council districts 49-51).

## Method & caveats

Outside-in crawl (browser UA). `rcda.nyc.gov` does not resolve; `statenislandda.org` is bot-walled by a SiteGround captcha, so the stack was fingerprinted from response headers (nginx, `x-sg-cdn`, SiteGround `nevercache` cookie) and a decompressed Wayback Machine snapshot (2026-07-01), with pages enumerated via Wayback CDX. Tip-form fields are the real Contact Form 7 field names read from the archived pages. Open Data absence was verified via the Socrata Discovery API across five candidate agency labels. A sample, not a full spider; the aggregate prosecution-statistics schema is a design-first proposal for data that does not yet exist in any machine-readable form.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (zero datasets, documented) ✅ · JSON Schemas (6 + common) ✅ · OpenAPI 3.1 (9 paths/ops) ✅ · MCP artifact (9 tools) ✅.
- **Next:** an example implementation fronting the Contact Form 7 tip forms with `POST /tips`; then generalize the schemas into a shared five-borough DA API, and the next domain from [../domains.md](../domains.md).
