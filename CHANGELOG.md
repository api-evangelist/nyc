# Changelog

All notable work on the NYC — API & Agent Modernization project. Newest first. Dates are absolute.

The format is loosely [Keep a Changelog](https://keepachangelog.com/). This project began as research and was activated into the [api-evangelist/nyc](https://github.com/api-evangelist/nyc) repository.

## 2026-07-13

### Added — Batch of ten domains (parallel)
- Ran the full 7-step method against ten more agencies in parallel, each in its own folder: **DOB, HPD, DOT, DOHMH, DSNY, NYPD, TLC, DCP, Comptroller, NYCHA**. Total assessed: **15 domains** (~1,700 Open Data assets mapped, 95 JSON Schemas, 142 MCP tools).
- **Taxonomy expanded** with new verbs — Transact (DOB, DOHMH), Expose (HPD, DSNY, NYPD), Unify (DOT), Operationalize (TLC), Anchor (DCP), Consolidate & Own (Comptroller), Unlock (NYCHA) — all clustering on one **meta-finding: the reporting data is open; the service/transaction layer is missing, hidden, or vendor-locked.**
- Notables: HPD already runs a private owned REST API (WSO2); DSNY/NYPD run live undocumented backends; Comptroller's **Checkbook NYC** is a live keyless XML API; DCP is the **geography anchor** for the planned `nyc-commons`. DOB confirms "the real legacy surface is the `aNNN-*` app layer." Across all 15, the write API is absent in 14/15 and agent-readiness is 0/15.
- Net-new write objects: `PermitApplication`, `HousingLotteryApplication`, `StreetWorkPermit`, `VitalRecordRequest`, `BulkPickupRequest`, `PoliceReportRequest`, `LicenseApplication`, `ClaimFiling`, `WorkOrder`.
- Manifest generator (`scripts/build-manifest.py`) extended to 15; manifest regenerated; scorecard, SYNTHESIS (new "batch of ten" section), home page, and synthesis page updated to fifteen domains.

### Added — Roadmap
- `ROADMAP.md` — near/soon/later plan led by **`nyc-commons`** (factor the recurring geography spine — Borough, Community Board, Council District, Census Tract/NTA, BBL/BIN — into one shared schema set every domain `$ref`s), plus cross-domain identity (`Address`/`Place`), more domains, open-standards conformance, an APIs.json registry, and a reference implementation. Added to site nav.

### Added — Domain 5: NYC311 (portal.311.nyc.gov)
- Full method run. **Fifth distinct platform: Microsoft Dynamics 365** (Power Apps Portals on Azure).
- Findings: the 311 dataset (`erm2-nwe9`) is the **most-used in the project** (1.26M views, 590k downloads); a real **API gateway exists** (`api.nyc.gov`, Azure APIM — GeoClient, key-gated); but the **Open311 (GeoReport v2) standard NYC once ran is retired**, and the service is a vendor CRM with no public write API. **Five-for-five** on the universal write-API gap.
- Artifacts: assessment + inventories + crosswalk (incl. `erm2-nwe9`→Open311 field mapping); **Open311-aligned** JSON Schemas (`service-request`, `service-type`, `service-definition`, `agency`); **OpenAPI** reviving Open311 GeoReport v2 (6 paths / 7 ops); **MCP** (6 tools). Net-new: `ServiceRequest` (revive Open311 `POST /requests`).
- Established the **fifth verb: Standardize**. Manifest regenerated (via new `scripts/build-manifest.py`); scorecard, synthesis, and home page updated to five domains.

### Added — Cross-domain synthesis
- `SYNTHESIS.md` — the project-level analysis: the four-verb diagnostic taxonomy (Replatform · Reclaim · Consolidate & Own · Digitize), **eight cross-cutting findings** (no shared API layer; website vs. open data as two worlds; uneven Open Data inversely related to stakes; a universal un-API'd citizen write-workflow; pervasive uncoordinated vendor outsourcing; zero agent-readiness; a recurring shared geography spine; per-domain join keys with no cross-domain identity), a **7-dimension maturity scorecard**, and a **NYC API playbook** (shared `nyc-commons` schemas, the three-contract chain, prioritize write workflows, agent-native by default, own vendor-held records, register everything, connect data to the front door).
- `data/scorecard.json` — per-domain maturity scores (0–3) with reasoning.
- `synthesis.html` — interactive page: verb cards, an at-a-glance **maturity heatmap** (hover for reasoning), the four net-new write objects, the shared geography spine, and the eight findings. Added to nav and the home page.

### Added — Explorable GitHub Pages site
- Built a self-contained, data-driven static site (no build step) to explore every artifact, intended for **nyc.apievangelist.com**.
  - `index.html` — project overview: thesis, cross-domain stats, four-verb pattern table, the seven-step method, domain cards, and the domains-inventory summary.
  - `domain.html` — per-domain explorer with tabs: Overview, **interactive Fruit index** (filter by coverage/search), APIs & tech, **searchable Open Data index**, **Schemas browser** (renders each JSON Schema), OpenAPI operations, MCP tools, and Documents.
  - `docs.html` — in-browser Markdown viewer (renders any repo `.md`, incl. this changelog); dependency-free renderer with table support.
  - `data/manifest.json` — generated from the repo artifacts so the site stays accurate as domains are added.
  - `assets/style.css`, `assets/app.js` — responsive, light/dark, brand-blue; zero external dependencies.
  - `CNAME`, `.nojekyll` for GitHub Pages custom-domain hosting.
- Added this `CHANGELOG.md`.

### Added — Domain 4: vote.nyc (NYC Board of Elections)
- Full method run. **Fourth distinct platform: Drupal 9** (JSON:API disabled — no site API), Cloudflare/Varnish, New Relic.
- Finding: the **least-modernized** domain — only **2** Open Data assets (poll sites); election **results, candidates, and contests are PDF-only** plus a legacy viewer (`enr.boenyc.gov`); ballot request/tracking siloed in `requestballot.vote.nyc`.
- Artifacts: `low-hanging-fruit.md`, `fruit.json`, `tech-stack.md`, `apis-observed.md`, `crosswalk.md`, `opendata-boeny.md/json`; **7 JSON Schemas** (`poll-site`, `election-district`, `election`, `contest`, `candidate`, `election-result`, `ballot-request` — several **aspirational**, defining data that doesn't exist yet); **OpenAPI** (10 paths / 11 ops); **MCP** (7 tools). Net-new: `BallotRequest`.
- Established the **fourth verb: Digitize**.

### Added — Domain 3: council.nyc.gov (NYC Council)
- Full method run. **Third distinct platform: WordPress on WP Engine.**
- Finding: the **most API-covered** domain — three existing APIs (vendor **Legistar Web API**, open **WordPress REST API**, **Socrata SODA** / 11 NYCC datasets), none owned/unified/agent-native.
- Artifacts: assessment + inventories + crosswalk; **7 JSON Schemas** (`council-member`, `district`, `committee`, `legislation`, `meeting`, `discretionary-funding`, `testimony-registration`); **OpenAPI** (14 paths / 15 ops); **MCP** (10 tools). Net-new: `TestimonyRegistration`.
- Established the **third verb: Consolidate & Own**.

### Added — Domain 2: schools.nyc.gov (NYC Public Schools / DOE)
- Full method run. **Second distinct platform: Progress Sitefinity (.NET).**
- Finding: 638 DOE Open Data assets (incl. 462-column directories); site **search rented to a vendor (HawkSearch)** and school pages driven by a hidden, robots-blocked internal `/CustomApi`. DBN is the join key.
- Artifacts: assessment + crosswalk; **6 JSON Schemas** (`school`, `school-demographics`, `calendar-event`, `test-result`, `enrollment-application`, `_common`); **OpenAPI** (9 paths / 11 ops); **MCP** (9 tools). Net-new: `EnrollmentApplication`.
- Established the **second verb: Reclaim**, and introduced two new standard method steps: **Technology & vendor inventory** and **APIs-observed inventory** (later back-filled to Parks).

### Added — Domain 1: nycgovparks.org (NYC Parks & Recreation)
- First full assessment. Platform: legacy **Smarty 2.6.2 / jQuery (PHP)** behind nginx + CloudFront; one modern island (the Next.js **Tree Map**).
- Low-hanging-fruit index: ~1,700 parks, ~42 facility directories (up to 1,275 rows), Capital Project Tracker, events, Historical Signs DB, Tree Map.
- **Open Data crosswalk** — the reframe: **237 DPR assets** already exist as machine-readable twins (27 of ~40 fruit items matched), just unlinked from the site. Sharpened the project thesis.
- Artifacts: `low-hanging-fruit.md`, `fruit.json`, `crosswalk.md`, `opendata-parks.md/json`; **7 JSON Schemas** (`park`, `facility`, `capital-project`, `event`, `monument`, `tree`, `permit-application`); **OpenAPI** (15 paths / 17 ops); **MCP** (15 tools). Net-new: `PermitApplication`.
- Back-filled `tech-stack.md` + `apis-observed.md` for parity with later domains.
- Established the **first verb: Replatform**.

### Added — Project activation & framing
- Cloned **api-evangelist/nyc** into `new-york/nyc/`; moved all work out of `research/` (removed `research/nyc-modernization/`).
- Root `README.md` frames the thesis: **not another data-liberation project.** 2010–2018 open data (Socrata, Obama-era, NYC Open Data law) only partially worked; this is step two — unify, productize, complete write workflows, expose via MCP. "Make the city programmable."
- Adopted the **design-first artifact chain**: individual JSON Schema per object → OpenAPI that `$ref`s them → MCP server that maps to the same operations. APIs/MCP are **design artifacts, not deployments**.

### Added — Inventory & scope
- `domains.md` — inventory of **~85 distinct NYC government domains/subdomains** across 11 categories (umbrella, open-data/API, mayoral agencies, elected offices, public authorities, libraries, community boards, app hosts, and adjacent state/regional). Noted the true surface is larger (~100 agencies mostly under `nyc.gov/site/*` paths + hundreds of `aNNN-*.nyc.gov` app hosts).

---

### Conventions
- **Verbs:** each domain gets a one-word modernization verb capturing its dominant gap — Replatform · Reclaim · Consolidate & Own · Digitize.
- **Per-domain method (7 steps):** assess → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schema per object → OpenAPI → MCP.
- **Status:** all APIs and MCP servers are design-first artifacts; nothing is deployed.
