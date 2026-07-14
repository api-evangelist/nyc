# brooklynda — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **Kings County (Brooklyn) District Attorney's Office**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (press releases, programs, resources, victim services, the absent case statistics, and the net-new tip submission).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (self-hosted **WordPress 6.8.5** on Apache; GeneratePress; Wordfence/Yoast/MonsterInsights; the accidental **WordPress REST API**).
- [apis-observed.md](apis-observed.md) — the **one accidental API** (WordPress `wp/v2` over ~911 press releases) vs. **zero Open Data** and **no inbound surface**.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping, with the honest verdict that no DA Open Data exists.
- [opendata-brooklynda.md](opendata-brooklynda.md) / [opendata-brooklynda.json](opendata-brooklynda.json) — the Socrata verification: **zero** assets under any Brooklyn/Kings County DA label (empty JSON, documented honestly).
- [schemas/](schemas/) — individual JSON Schema per object: `press-release` · `program` · `community-resource` · `victim-service` · `case-statistics` · `tip-submission` (+ shared `_common`).
- [openapi/brooklynda.yaml](openapi/brooklynda.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/brooklynda-mcp.json](mcp/brooklynda-mcp.json) — design-first MCP server definition (9 agent tools; artifact, not a deployment).

## What was found — the fifth distinct pattern

The Brooklyn DA is a **content-only domain with no data**, and that absence is the finding:

1. **One WordPress brochure site.** `brooklynda.org` is self-hosted **WordPress 6.8.5** (GeneratePress, Wordfence, Yoast) on Apache — no portal, no application, no data platform, and *not* on the shared NYC.gov chassis.
2. **The only machine-readable surface is accidental.** The **WordPress REST API** (`/wp-json/wp/v2`) exposes ~911 press releases plus programs and resources. It is the CMS default, not a designed contract.
3. **Zero open data, anywhere.** No NYC Open Data asset exists for any DA office (verified). The office's core justice information — caseloads, dispositions, diversions, conviction-review outcomes — is published **nowhere as data**, only as prose in press releases.
4. **No inbound surface.** Submitting a **tip** has only a captcha web form, a phone hotline, or a bureau email.

**The gap here is that there is barely any data, and it belongs to five identical offices.** A resident or agent asking "how many DV cases were declined last year?" or "let me send in a tip about deed fraud" has nothing to call.

**Reframe (vs. the earlier domains):**

| | Parks | DOE | Council | NYCHA | **Brooklyn DA** |
|---|---|---|---|---|---|
| Platform | Smarty/PHP (legacy) | Sitefinity (.NET) | WordPress | NYC.gov Livesite + Oracle Siebel | **Self-hosted WordPress 6.8.5** |
| Core problem | data as HTML, no API | search rented, backend hidden | three APIs, none owned | data open, service layer locked | **no data at all; accidental content API; five identical offices** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** | **unlock** | **template** |

## The bigger opportunity — one shared DA API

All five NYC county District Attorney offices — **New York, Bronx, Kings (Brooklyn), Queens, and Richmond (Staten Island)** — share the same functions: bureaus, diversion and re-entry programs, conviction review, victim services, press, and tip intake. Each runs its own brochure site with no data and no API. The right modernization move is not five bespoke builds but **one shared DA API** — a single owned contract and [MCP server](mcp/brooklynda-mcp.json) (office id `io.nyc.brooklynda`) the five offices adopt. This assessment's schemas and OpenAPI are deliberately office-neutral to serve as that template.

## Reverse-engineered entities

`PressRelease` · `Program` · `CommunityResource` · `VictimService` · `CaseStatistics` (aggregate only; never individual cases) · `TipSubmission` (net-new write) — organizing key **Bureau**.

## Method & caveats

Outside-in crawl (browser UA; `brooklynda.org/robots.txt` is a Yoast block with no disallows). The site was fingerprinted from response headers (`Server: Apache`, WordPress generator meta, `Link` rel to `wp-json`) and markup (theme/plugin paths); the REST namespaces and content-category counts were read from `/wp-json`. Open Data absence verified via the Socrata Discovery API across every plausible agency label. A sample, not a full spider; program/victim-service structure is inferred from the site's information architecture, and `CaseStatistics` is a *proposed* surface — the office publishes no such data today.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (verified zero) ✅ · JSON Schemas (6 + common) ✅ · OpenAPI 3.1 (9 paths/9 ops) ✅ · MCP artifact (9 tools) ✅.
- **Next:** propose the **shared five-office DA API**; an example implementation fronting the WordPress REST API and the tip form for `submit_tip`; then the next domain from [../domains.md](../domains.md).
