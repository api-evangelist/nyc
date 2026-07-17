# NYC — API & Agent Modernization

Mapping the digital surface of New York City government — every public table, form, dataset, and portal — and turning it into an **API-first, agent-native** layer: individual JSON Schema per object, an OpenAPI contract that `$ref`s those objects, and an MCP server so the same resources are usable by both applications and AI agents.

This is the working project. It grew out of an [API Evangelist low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) — the same outside-in method used for the [University of Oklahoma](https://apievangelist.com/2014/10/12/an-outsidein-approach-to-jumpstarting-an-api-effort-at-the-university-of-oklahoma/) and the [Department of Veterans Affairs](https://skylight-hq.github.io/va-api-landscape/report/).

## Why this is *not* another data-liberation project

From roughly **2010 to 2018**, the open-data movement — led by **Socrata** (now Tyler), the Obama-era open-government directives, and NYC's own Open Data law — pushed cities to publish their data. NYC did: `data.cityofnewyork.us` hosts tens of thousands of datasets, and NYC Parks alone publishes **237 assets** there today.

**It only partially worked.** Publishing datasets is not the same as making a government programmable. What that era left us with:

- **Data without product.** Each dataset got a raw SODA endpoint, but there is no *resource-oriented* API — no "a Park has facilities, events, monuments, trees, and capital projects" model. Consumers get tables, not services.
- **Disconnected from the front door.** The public websites (e.g. `nycgovparks.org`) render their **own** parallel HTML and **never consume** the open-data twin. Two worlds, separately maintained, free to drift.
- **Read-only.** Open data liberated *reporting* data. The transactional workflows citizens actually need — permits, applications, registrations — stayed locked behind login-gated HTML forms with no API at all.
- **Not agent-ready.** None of it is exposed as tools an AI agent can call. In 2026 that is the gap that matters.

**This project is the next version.** Not "publish more CSVs." Instead:

> **Unify** what already exists behind coherent, resource-oriented APIs → **productize** with one JSON Schema per object and an OpenAPI contract → **complete** the missing write workflows (permits) → **expose** all of it through **MCP** so agents are first-class consumers.

Data liberation was step one, and it half-happened. This is step two: **making the city programmable.**

All **70 agencies** have been assessed this way, and the design-first artifacts are assembled into a full stack: a cross-domain **synthesis**, an **opportunity** ranking, the **`nyc-commons`** shared schema set, a **QA** verification pass, **standards** conformance, and **the Programmable City** — the REST → MCP → Agent-Skill chain across every agency, with a callable reference API and an installable MCP server. On top of it all sits a **strategy** aimed at New York's new [Public Interest Technology (PIT) Crew](https://nyc.apievangelist.com/strategy.html).

## Explore the site

This repo doubles as an explorable, data-driven website (**[nyc.apievangelist.com](https://nyc.apievangelist.com)**, GitHub Pages):

- `index.html` — project overview: thesis, cross-domain stats, the five verb families, the method, and cards for all 70 domains.
- `domain.html?d=<domain>` — per-domain explorer: interactive fruit index, searchable Open Data index, JSON Schema browser, OpenAPI operations, MCP tools, and rendered docs.
- `strategy.html` · `references.html` — **the strategic case** for why this work matters, aimed at NYC's [Public Interest Technology (PIT) Crew](https://www.nyc.gov/content/pitcrew/pages/), plus a growing library of references (`data/references.json`).
- `synthesis.html` — the **cross-domain synthesis**: the five verb families, the thirteen cross-cutting findings, and the aggregate maturity scorecard (the "two flat columns" — no write API, no agent surface).
- `opportunity.html` · `linkage.html` · `transactions.html` — the assessment layer: priority ranking (demand×gap×feasibility), the cross-domain join-key graph, and the citizen-transaction taxonomy.
- `experience.html` — **the Programmable City**: the REST operation → MCP tool → Agent Skill chain across all 70 agencies, organized by ten common government processes, with per-agency + cross-agency MCP prompts and resources. It's **runnable** — a GET-callable static **reference API** (`experience/api/`, example data off Pages) and an installable **MCP server** ([`@api-common/nyc-mcp`](experience/mcp-server/), one-click via [install.apicommons.org](https://install.apicommons.org)). Machine artifacts under `experience/` (unified OpenAPI with `x-` extensions, NYC-wide MCP, [APIs.json](https://apisjson.org) descriptor, Skills).
- `commons.html` — the **[`nyc-commons`](nyc-commons/README.md)** shared schema set: 21 canonical definitions (borough, BBL, address, place, party, dollar), the per-definition adoption report (all 69 consumer domains migrated), and the cross-agency key registry.
- `standards.html` · `qa.html` — the standards NYC agencies should adopt (and the standards this project is built on), and the verification pass (69/70 high confidence).
- `entities.html` · `technology.html` — master cross-domain inventories (344 entities; 79 technologies tagged commercial/open-source with an OSS alternative for each proprietary tool).
- `docs.html?f=…` — in-browser Markdown viewer (also serves the [CHANGELOG](CHANGELOG.md), [SYNTHESIS](SYNTHESIS.md), [STRATEGY](STRATEGY.md), and the per-analysis writeups).
- `data/manifest.json` — generated from the repo artifacts; the site reads it, so it stays accurate as domains are added. Regenerate after adding a domain: `python3 scripts/build-manifest.py && python3 scripts/build-scorecard.py` (then `build-analysis.py`, `build-inventories.py`, `build-qa.py`, `build-standards.py`; `build-commons.py` after touching any `_common.json`; `build-experience.py` then `build-gateway.py` rebuild the experience layer + reference API; `build-overlays.py` regenerates the localization overlays; `build-schemas.py` regenerates the per-schema index behind `schema.html`; `build-references.py` after editing references).

The site is dependency-free static HTML/CSS/JS — no build step.

**Enabling Pages:** Settings → Pages → *Deploy from a branch* → `main` / root. The custom domain is set via the `CNAME` file (`nyc.apievangelist.com`); add a DNS `CNAME` record `nyc → api-evangelist.github.io`. `.nojekyll` is present so files serve as-is.

See the **[CHANGELOG](CHANGELOG.md)** for the full project history, and the **[cross-domain SYNTHESIS](SYNTHESIS.md)** (interactive: `synthesis.html`) for the five-family taxonomy, the thirteen cross-cutting findings, and the aggregate maturity scorecard.

## Method (per domain)

1. **Low-hanging-fruit assessment** — outside-in crawl of the domain; index every table (>10 rows), form, and **downloadable data file — CSV, Excel (`.xlsx`/`.xls`), XML, JSON, PDF, or other** — as `name · type · URL · entity`. Excel/spreadsheet exports are one of the most common ways agencies share data that should be an API; capture them explicitly, not just on-page HTML tables.
2. **Technology & vendor inventory** — fingerprint the CMS, hosting, CDN, analytics, and any outsourced capabilities (search, maps, identity) from headers and page markup. Vendor lock-in is a modernization constraint.
3. **APIs-observed inventory** — document every backend/service API the site itself calls while crawling (internal REST, vendor APIs, blob stores, the open-data SODA endpoints). The *existing* programmatic surface.
4. **Open Data crosswalk** — match each resource to any existing `data.cityofnewyork.us` dataset; separate real gaps from already-published-but-disconnected data.
5. **JSON Schema per object** — one canonical schema file per entity, reconciling the website's columns with the Open Data column schemas.
6. **OpenAPI** — a resource-oriented contract that `$ref`s each object schema; reads over unified data, writes for the missing transactional workflows.
7. **MCP** — expose the same resources as agent tools (design artifact, not a deployment).

## Contents

> **All 70 assessed domains are browsable at [nyc.apievangelist.com](https://nyc.apievangelist.com)** — this Contents list highlights the first five deep-dives; every other agency folder follows the identical structure.

- [domains.md](domains.md) — master inventory of NYC government domains (umbrella `nyc.gov`, distinct-domain agencies, `aNNN-*.nyc.gov` app hosts, public authorities, adjacent state/regional).
- [nycgovparks.org/](nycgovparks.org/) — **first domain, taken through the full method:**
  - [low-hanging-fruit.md](nycgovparks.org/low-hanging-fruit.md) / [fruit.json](nycgovparks.org/fruit.json) — the fruit index.
  - [crosswalk.md](nycgovparks.org/crosswalk.md) — fruit ↔ Open Data mapping (the reframe, in evidence).
  - [opendata-parks.md](nycgovparks.org/opendata-parks.md) / [opendata-parks.json](nycgovparks.org/opendata-parks.json) — all 237 DPR Open Data assets + column schemas.
  - [tech-stack.md](nycgovparks.org/tech-stack.md) (vendors) · [apis-observed.md](nycgovparks.org/apis-observed.md) (backend APIs).
  - [schemas/](nycgovparks.org/schemas/) — individual JSON Schema per object: `park` · `facility` · `capital-project` · `event` · `monument` · `tree` · `permit-application` (+ shared `_common`).
  - [openapi/nyc-parks.yaml](nycgovparks.org/openapi/nyc-parks.yaml) — OpenAPI 3.1 contract `$ref`ing every object schema.
  - [mcp/nyc-parks-mcp.json](nycgovparks.org/mcp/nyc-parks-mcp.json) — design-first MCP server definition (15 agent tools mapped to the OpenAPI ops, `$ref`ing the same objects).
- [schools.nyc.gov/](schools.nyc.gov/) — **second domain (NYC Public Schools / DOE), full method + inventories:**
  - [low-hanging-fruit.md](schools.nyc.gov/low-hanging-fruit.md) / [fruit.json](schools.nyc.gov/fruit.json), [crosswalk.md](schools.nyc.gov/crosswalk.md), [opendata-doe.md](schools.nyc.gov/opendata-doe.md) (638 DOE assets).
  - [tech-stack.md](schools.nyc.gov/tech-stack.md) (vendors) · [apis-observed.md](schools.nyc.gov/apis-observed.md) (backend APIs).
  - [schemas/](schools.nyc.gov/schemas/) (DBN-keyed: `school` · `school-demographics` · `calendar-event` · `test-result` · `enrollment-application`) · [openapi/nyc-schools.yaml](schools.nyc.gov/openapi/nyc-schools.yaml) · [mcp/nyc-schools-mcp.json](schools.nyc.gov/mcp/nyc-schools-mcp.json).
- [council.nyc.gov/](council.nyc.gov/) — **third domain (NYC Council), full method + inventories:**
  - [low-hanging-fruit.md](council.nyc.gov/low-hanging-fruit.md) / [fruit.json](council.nyc.gov/fruit.json), [crosswalk.md](council.nyc.gov/crosswalk.md), [opendata-nycc.md](council.nyc.gov/opendata-nycc.md) (11 NYCC datasets).
  - [tech-stack.md](council.nyc.gov/tech-stack.md) (WordPress/WP Engine, Legistar) · [apis-observed.md](council.nyc.gov/apis-observed.md) (three existing APIs).
  - [schemas/](council.nyc.gov/schemas/) (`council-member` · `district` · `committee` · `legislation` · `meeting` · `discretionary-funding` · `testimony-registration`) · [openapi/nyc-council.yaml](council.nyc.gov/openapi/nyc-council.yaml) · [mcp/nyc-council-mcp.json](council.nyc.gov/mcp/nyc-council-mcp.json).
- [vote.nyc/](vote.nyc/) — **fourth domain (NYC Board of Elections), full method + inventories:**
  - [low-hanging-fruit.md](vote.nyc/low-hanging-fruit.md) / [fruit.json](vote.nyc/fruit.json), [crosswalk.md](vote.nyc/crosswalk.md), [opendata-boeny.md](vote.nyc/opendata-boeny.md) (2 assets).
  - [tech-stack.md](vote.nyc/tech-stack.md) (Drupal 9) · [apis-observed.md](vote.nyc/apis-observed.md) (near-absent).
  - [schemas/](vote.nyc/schemas/) (`poll-site` · `election-district` · `election` · `contest` · `candidate` · `election-result` · `ballot-request`) · [openapi/nyc-elections.yaml](vote.nyc/openapi/nyc-elections.yaml) · [mcp/nyc-elections-mcp.json](vote.nyc/mcp/nyc-elections-mcp.json).
- [nyc311/](nyc311/) — **fifth domain (NYC311), full method + Open311 alignment:**
  - [low-hanging-fruit.md](nyc311/low-hanging-fruit.md) / [fruit.json](nyc311/fruit.json), [crosswalk.md](nyc311/crosswalk.md) (incl. `erm2-nwe9` → Open311 mapping), [opendata-311.md](nyc311/opendata-311.md).
  - [tech-stack.md](nyc311/tech-stack.md) (Dynamics 365, api.nyc.gov gateway) · [apis-observed.md](nyc311/apis-observed.md) (retired Open311).
  - [schemas/](nyc311/schemas/) (Open311-aligned: `service-request` · `service-type` · `service-definition` · `agency`) · [openapi/nyc-311.yaml](nyc311/openapi/nyc-311.yaml) · [mcp/nyc-311-mcp.json](nyc311/mcp/nyc-311-mcp.json).
- **Batch of ten** (same full method — assessment, tech/vendor + APIs inventories, Open Data crosswalk, JSON Schemas, OpenAPI, MCP — each in its own folder):
  - [dob/](dob/) Buildings · **Transact** — the `aNNN-*` app layer; nightly one-way batch dump; net-new `PermitApplication`.
  - [hpd/](hpd/) Housing · **Expose** — a private owned REST API behind WSO2; net-new `HousingLotteryApplication`.
  - [dot/](dot/) Transportation · **Unify** — 267 assets as flat/map-only snapshots; net-new `StreetWorkPermit`.
  - [dohmh/](dohmh/) Health · **Transact** — 81 datasets, transactions on Accela; net-new `VitalRecordRequest`.
  - [dsny/](dsny/) Sanitation · **Expose** — live undocumented pickup APIs; net-new `BulkPickupRequest`.
  - [nypd/](nypd/) Police · **Expose** — snapshots + Angular apps on Azure Gov; net-new `PoliceReportRequest`.
  - [tlc/](tlc/) Taxi & Limousine · **Operationalize** — parquet trip dumps; net-new `LicenseApplication`.
  - [dcp/](dcp/) City Planning · **Anchor** — the geography source for `nyc-commons`; owned `/geocode`.
  - [comptroller.nyc.gov/](comptroller.nyc.gov/) Comptroller · **Consolidate & Own** — Checkbook is a live XML API; net-new `ClaimFiling`.
  - [nycha/](nycha/) Housing Authority · **Unlock** — resident service locked in a Siebel CRM; net-new `WorkOrder`.

## Status

**All 70 domains assessed** — the full NYC government surface: **2,681 Open Data assets** mapped, **439 JSON Schemas**, **752 API operations**, **653 MCP tools**. The assessment is verified ([69/70 high confidence](https://nyc.apievangelist.com/qa.html)). One flat truth across the entire city: open data is broad, but **68 of 70 agencies have no transactional write API and all 70 have no agent surface.** The ~40 modernization verbs collapse into five families — Digitize · Expose · Unify/Federate · Transact · Standardize.

Five of the domains, illustrating five distinct verbs:

| Domain | Platform | Machine-readable coverage | Verb |
|---|---|---|---|
| nycgovparks.org | Smarty/PHP | 237 Open Data assets | **replatform** |
| schools.nyc.gov | Sitefinity/.NET | 638 assets; rented search, hidden backend | **reclaim** |
| council.nyc.gov | WordPress | 3 APIs, none owned | **consolidate + own** |
| vote.nyc | Drupal 9 | 2 assets; results/candidates PDF-only | **digitize** |
| portal.311.nyc.gov | Dynamics 365 | flagship dataset; Open311 standard retired | **standardize** |

### Built on top of the 70 assessments

- **[Synthesis](SYNTHESIS.md)** — five verb families, thirteen cross-cutting findings, the aggregate maturity scorecard (`synthesis.html`).
- **Opportunity / Linkage / Transactions** — priority ranking, the cross-domain join-key graph, and the citizen-transaction taxonomy.
- **[`nyc-commons`](nyc-commons/README.md)** — a versioned shared schema set (geography · identifiers · address · place · party · money), factored from City Planning; **all 69 consumer domains migrated** to `$ref` it.
- **QA** — every claim re-verified; **Standards** — the sector standards NYC should adopt (Open311, FHIR, …) and the standards this project is built on.
- **Inventories** — 344 entities and 79 technologies, each tagged commercial / open-source with a named OSS alternative for every proprietary tool.
- **[The Programmable City](https://nyc.apievangelist.com/experience.html)** — the REST → MCP → Agent-Skill chain across all 70 agencies, ten common government-process skills, per- and cross-agency MCP prompts/resources, a **callable reference API**, and an **installable MCP server** ([`@api-common/nyc-mcp`](experience/mcp-server/)).
- **[Strategy](STRATEGY.md) + [References](REFERENCES.md)** — the case for the work, aimed at NYC's Public Interest Technology (PIT) Crew.
- **[Cross-agency workflows](experience/workflows/)** — multi-agency journeys as open [Arazzo](https://spec.openapis.org/arazzo/latest.html) documents, starting with **[Build Affordable Housing in NYC](experience/workflows/build-affordable-housing.arazzo.yaml)** — the ~40-permit chain across twelve agencies as one BBL-keyed thread — and the **[housing brief](HOUSING.md)** on making affordable-housing permitting programmable.
- **[Interface localization](experience/overlays/)** — [OpenAPI Overlays](https://spec.openapis.org/overlay/latest.html) that translate the API/agent **interface** (not the data) into the **ten citywide languages of Local Law 30**, from one base contract — yielding a localized OpenAPI *and* MCP server per language. Worked example: the HPD Housing Connect lottery in all ten languages.

**Next** — see the [ROADMAP](ROADMAP.md): the DCWP "Click to Cancel" worked example for PIT Crew, a forkable "civic API kit" so other cities can run the method, OSS-migration playbooks, and publishing `@api-common/nyc-mcp` to npm.

---
*Part of [API Evangelist](https://apievangelist.com). Repo: [api-evangelist/nyc](https://github.com/api-evangelist/nyc).*
