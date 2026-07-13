# Changelog

All notable work on the NYC — API & Agent Modernization project. Newest first. Dates are absolute.

The format is loosely [Keep a Changelog](https://keepachangelog.com/). This project began as research and was activated into the [api-evangelist/nyc](https://github.com/api-evangelist/nyc) repository.

## 2026-07-13

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
