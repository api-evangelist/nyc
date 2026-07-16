# hdc — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **New York City Housing Development Corporation (HDC)**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

HDC is the City's affordable-housing **bond financier** — a public benefit corporation, sibling to [HPD](../hpd/). It was previously only lightly covered (folded into the `hpd/` notes); this folder gives it a first-class assessment.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (developments, financing programs/term sheets, bond issues, borrowers, and the net-new financing-application write).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (Drupal 10 on Pantheon + Fastly CDN + nginx + GTM/GA — *not* the shared NYC.gov Livesite chassis; the Developer Intake Portal, PDF term sheets, and the federal MSRB EMMA disclosure platform).
- [apis-observed.md](apis-observed.md) — the finding that HDC exposes **no API and owns no Open Data at all**; its record lives on HPD, OMB, and federal EMMA.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (adjacent, non-HDC-owned datasets) with coverage verdicts.
- [opendata-hdc.md](opendata-hdc.md) / [opendata-hdc.json](opendata-hdc.json) — the **zero** HDC-owned assets, plus the adjacent HPD/OMB datasets that carry HDC's record + column schemas.
- [schemas/](schemas/) — individual JSON Schema per object: `development` · `financing-program` · `bond-issue` · `borrower` · `financing-application` (the net-new write) (+ shared `_common`).
- [openapi/hdc.yaml](openapi/hdc.yaml) — OpenAPI 3.1 contract `$ref`ing each object; includes `applyForFinancing` (POST) and `getFinancingStatus` (GET).
- [mcp/hdc-mcp.json](mcp/hdc-mcp.json) — design-first MCP server definition (9 agent tools; artifact, not a deployment).

## What was found — a new distinct pattern

HDC is a **bond financier**, and that is the finding:

1. **HDC owns nothing machine-readable.** Verified: **zero** NYC Open Data datasets are attributed to HDC, and there is **no HDC API** of any kind. This is thinner than [DDC](../ddc/), which at least owns four Socrata datasets.
2. **Its record is dispersed across three owners it doesn't control.** Developments are published by **HPD** (the LIHTC **4%** awards are precisely HDC's tax-exempt-bond-financed deals); its debt is published by **OMB** ("Debt Issuance by Issuer", HDC as an `Issuer Name` value); and its investor disclosure lives on the **federal MSRB EMMA** platform as documents.
3. **Its own surfaces publish nothing structured.** The website (Drupal on Pantheon) is a marketing site with no content API; the programs are PDF term sheets; and the one transaction HDC owns — the **Developer Intake Portal** — has no API.

**The gap here is ownership.** A developer or agent asking "which HDC program fits a 60%-AMI new-construction deal, and how do I apply?" has no HDC API to call — only PDFs and an intake portal.

**Reframe (vs. sibling B2G domains):**

| | DDC | LPC | **HDC** |
|---|---|---|---|
| Platform | NYC.gov Livesite + citywide PASSPort/City Record/Checkbook | NYC.gov Livesite + Socrata + Esri + Salesforce Portico | **nychdc.com (Drupal/Pantheon/Fastly) + Developer Intake Portal + PDF term sheets + federal MSRB EMMA** |
| Owned Open Data | 4 datasets (thin/historical) | 15 datasets (open, scattered) | **0 datasets** |
| Core problem | data thin & on systems DDC doesn't own | data open but scattered, write locked in Salesforce | **owns no data or API at all; record is HPD's / OMB's / the MSRB's** |
| Modernization verb | **surface** | **bind** | **originate** |

## Reverse-engineered entities

`Development` · `FinancingProgram` (term sheet) · `BondIssue` (HRB/SDB) · `Borrower` (developer; derived) · `FinancingApplication` (net-new B2G write — the Developer Intake Form) — join keys **BBL**, **BIN**, **Project Name**, **Applicant Name**, bond **Series Name**.

## Method & caveats

Outside-in crawl (browser UA). The informational site was fingerprinted from headers and markup (Drupal 10, Pantheon `x-pantheon-styx-*`, Fastly `via: varnish` / `x-served-by`, nginx, GTM/gtag). The financing programs and term sheets were read from the Develop section; the bond/disclosure surfaces from the Invest section (Debt Issuance, Sustainable Development Bonds, EMMA, credit ratings). The **zero** Open Data count was verified via the Socrata Discovery API (`attribution`/agency = "Housing Development Corporation" → 0), and the adjacent HPD/OMB datasets were pulled with columns. Where a dataset carries HDC's record but belongs to another agency (HPD LIHTC 4% awards; OMB Debt Issuance by Issuer), that is stated explicitly. The net-new write is quoted from the Develop page ("All new project proposals must be submitted through HDC Developer Intake Portal"); its internal workflow is inferred, not scraped behind login. There is **no citizen write** in this domain — the net-new write is honestly B2G/developer, and (per HDC) submission does not indicate acceptance.

## Status & next

- **Done (2026-07-16):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (0 owned; adjacent HPD/OMB) ✅ · JSON Schemas (5 + common) ✅ · OpenAPI 3.1 (8 paths/ops) ✅ · MCP artifact (9 tools) ✅.
- **Next:** an example implementation fronting the Developer Intake Portal for `applyForFinancing`, and reconciling `Development` against HPD's LIHTC 4% datasets by BBL; then the next domain from [../domains.md](../domains.md).
