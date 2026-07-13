# acs — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **NYC Administration for Children's Services (ACS)**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (the Community Partners provider directory, the aggregate child-welfare/prevention/foster-care/youth-justice reports, and the delegated intake channels).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (NYC.gov "Livesite" + Akamai + Dynatrace + Google Maps; the **delegated** intakes: NY State Central Register and NYC 311).
- [apis-observed.md](apis-observed.md) — the **one useful open API** (Socrata SODA over a single address-level dataset) vs. a service layer **delegated** to the State and 311.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (21 ACS assets) with coverage verdicts.
- [opendata-acs.md](opendata-acs.md) / [opendata-acs.json](opendata-acs.json) — all 21 ACS Open Data assets + column schemas, sorted by page views.
- [schemas/](schemas/) — individual JSON Schema per object: `provider` · `child-welfare-indicator` · `prevention-service` · `foster-care-statistics` · `juvenile-justice-statistics` · `child-care-complaint` (+ shared `_common`).
- [openapi/acs.yaml](openapi/acs.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/acs-mcp.json](mcp/acs-mcp.json) — design-first MCP server definition (9 agent tools; artifact, not a deployment).

## What was found — the fifth distinct pattern

ACS is a **confidentiality-bound, delegated-intake** domain, and that is the finding:

1. **Its operational data is confidential by statute.** Abuse/neglect investigations, foster care, and juvenile detention are published **only in aggregate** — never per case, correctly.
2. **What is public is thin and mostly files.** Of **21** ACS Open Data assets, **16 are `file` attachments** (uploaded reports, not queryable) and only **5 are tabular**. Exactly **one** — the **ACS Community Partners** directory (`9hyh-zkx9`, 39 columns) — is address-level and machine-readable.
3. **Its public actions are delegated.** Reporting abuse goes to the **NY State Central Register** (1-800-342-3720); complaining about a **child care provider** goes to **NYC 311**. ACS owns neither intake and exposes no API of its own.

**The gap here is ownership, not a hidden backend.** There is no CRM to unlock — the data is confidential or dumped as files, and the two public actions belong to the State and to 311.

**Reframe (vs. the earlier domains):**

| | Parks | DOE | Council | NYCHA | **ACS** |
|---|---|---|---|---|---|
| Platform | Smarty/PHP (legacy) | Sitefinity (.NET) | WordPress | NYC.gov Livesite + Oracle Siebel | **NYC.gov Livesite (no owned app)** |
| Core problem | data as HTML, no API | search rented, backend hidden | three APIs, none owned | data open, service layer in a CRM | **data confidential or file-dumped; actions delegated to State + 311** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** | **unlock** | **insource** |

## Reverse-engineered entities

`Provider` (Community Partner; the one machine-readable object) · `ChildWelfareIndicator` · `PreventionService` · `FosterCareStatistics` · `JuvenileJusticeStatistics` (all aggregate-only; never an individual case) · `ChildCareComplaint` (net-new write; a **provider** concern, delegated today to 311) — shared spines: **NYC geography** (BBL/BIN, council district, community board, NTA) and **reporting period**.

## Method & caveats

Outside-in crawl (browser UA; `nyc.gov/robots.txt` only disallows `/html/misc/`). The informational site was fingerprinted from headers (Akamai, nginx, Livesite, Dynatrace, Google Maps JS); the abuse-report and complaint paths were traced from the site's own outbound links (`ocfs.ny.gov`, `portal.311.nyc.gov`) without submitting anything. Open Data agency label verified via the Socrata Discovery API; all 21 assets pulled with columns (16 are non-tabular `file` attachments). A sample, not a full spider; the State SCR (CONNECTIONS) and 311 internals are inferred from their public role, not scraped. Child care *licensing* data lives under **DOHMH**, not ACS.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (21 assets) ✅ · JSON Schemas (6 + common) ✅ · OpenAPI 3.1 (9 paths/ops) ✅ · MCP artifact (9 tools) ✅.
- **Next:** an example implementation fronting NYC 311 for `report_child_care_concern` with a hard redirect to the State Central Register for any suspected abuse; then the next domain from [../domains.md](../domains.md).
