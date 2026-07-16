# Low-Hanging Fruit Index — MOER/OER

**Agency:** New York City Mayor's Office of Environmental Remediation (MOER/OER)
**Assessed:** 2026-07-16
**Method:** Outside-in crawl (browser UA — `nyc.gov` returns Akamai `403` to non-browser agents). Fingerprinted three surfaces: the informational site `nyc.gov/site/oer` (Akamai + nginx + NYC.gov "Livesite" platform + AWS ALB + Dynatrace + Webtrends), the public **SPEED** map `speed.cityofnewyork.us` (CARTO/cartodb.js v3.15 + Leaflet, on Google Cloud, a JSONP `clientData.json` feed), and OER's login-walled **EPIC** project portal `a002-epic.nyc.gov` (Microsoft-IIS/10.0 + ASP.NET 4.0 + AngularJS). Read the Remediation and E-Designation pages for the OER Remedial Process and its determinations (Notice to Proceed, Notice of Satisfaction, Notice of No Objection). Verified the NYC Open Data agency label `Mayor's Office of Environmental Remediation (OER)` via the Socrata Discovery API and pulled all **10** assets with column schemas; noted the authoritative **E-Designation** datasets are published under the **DCP** label.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-moer.md](opendata-moer.md).

## Headline findings

1. **OER's reference data is open — and, at its core, live.** The flagship **OER Cleanup Sites** dataset (`3279-pp7v`) is updated **Daily** and carries a full BBL/BIN geography spine, and the public **SPEED** map lets anyone look up a parcel. **10** OER-labeled Open Data datasets in all (cleanup sites, historic land use, Clean Soil Bank, a six-layer brownfield-planning suite).
2. **But there is no OER-owned REST API.** The data reaches consumers only as Socrata dataset IDs plus SPEED — a CARTO/Leaflet **map app**, not a documented API. An agent can't call it.
3. **The regulatory workflow is trapped in EPIC.** OER's own login-walled portal (`a002-epic.nyc.gov`) runs the OER Remedial Process, holds every determination (**Notice to Proceed / Decision Document**, **Notice of Satisfaction / Completion**, **Notice of No Objection**), and is where intake happens. Unlike DDC, OER *owns* this system — but it is a legacy .NET/AngularJS portal with no API.
4. **The authoritative (E)-designation inventory belongs to DCP.** The most-demanded environmental record — whether a parcel carries an (E) — is published under the **Department of City Planning** label (`hxm3-23vy`, `mzjp-98aw`, `jsrs-ggnx`), not OER, even though OER is the office that clears the (E) requirement.

> **Reframe:** DDC = a vendor-facing agency whose data is thin and historical and whose transactions run on citywide systems it doesn't own → *surface.* **OER = an agency whose cleanup data is open and even daily, but whose whole regulatory workflow is trapped in a login-walled legacy portal, and whose authoritative (E) inventory is published by another agency → expose.** Expose the site data as one clean, BBL-keyed API *and* expose the workflow — status and the net-new request — as an owned contract.

## The fruit

| # | Name | Entity | Where the data lives | Open Data twin |
|---|---|---|---|---|
| 1 | Environmental / Cleanup Sites | `EnvironmentalSite` | SODA + SPEED (CARTO) | ✅ OER Cleanup Sites (`3279-pp7v`, Daily) |
| 2 | E-Designations (Do I Have an E?) | `EDesignation` | DCP SODA only | 🟡 DCP (`hxm3-23vy`, `mzjp-98aw`, `jsrs-ggnx`) |
| 3 | Cleanup Projects (VCP) | `CleanupProject` | EPIC portal | 🟡 coarse phase/class from `3279-pp7v` |
| 4 | OER Determinations (NTP / NOS / NNO) | `NoticeToProceed` | EPIC portal | ❌ gap (no API) |
| 5 | Remediation Status | `RemediationStatus` | EPIC portal | ❌ gap (reconstruct from docs) |
| 6 | **Request a Notice to Proceed / enroll in the VCP** | `NoticeToProceedRequest` | EPIC + email | ❌ **net-new (B2G)** |

Supporting: Historic Land Use (`r9ca-6t4q`), Clean Soil Bank (`b4dv-8mq4` + `hywf-9b6t`), and the six-layer BOA/community brownfield planning suite — all open (annual) due-diligence context.

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **Socrata SODA** — 10 OER datasets; flagship cleanup feed is daily and BBL-keyed (the real, open data surface).
- **SPEED** (`speed.cityofnewyork.us`) — public CARTO/Leaflet site-lookup map; a JSONP feed, not an API; OER-owned, on Google Cloud.
- **EPIC** (`a002-epic.nyc.gov`) — OER's login-walled ASP.NET/AngularJS project portal; where the workflow, documents, and determinations live; no API.
- **DCP E-Designations** — the authoritative (E) inventory, published by City Planning, not OER.
- Platform: informational site on the **NYC.gov shared "Livesite" platform** (Akamai edge, nginx, AWS ALB, Dynatrace, Webtrends) — the same chassis as DDC and peers.

## Reverse-engineered entities

`EnvironmentalSite` · `EDesignation` (DCP-published, OER-resolved) · `CleanupProject` (VCP) · `NoticeToProceed` (issued determination) · `RemediationStatus` (derived; `getRemediationStatus`) · `NoticeToProceedRequest` (net-new B2G write; `requestNoticeToProceed`) — join keys: **BBL** (leaning on nyc-commons) and **OER Project Number**.

## Next

1. **JSON Schema** per entity, reconciling the OER Cleanup Sites columns (OER Project Numbers, Project Name, OER Program, Class, Phase, BBL/BIN, geography) with the remedial-process concepts (phases, determinations) and the (E)-designation record — done ([schemas/](schemas/)).
2. **OpenAPI** exposing sites + (E)-designations + cleanup projects as clean BBL-keyed resources, `getRemediationStatus`, and the net-new `POST /notice-to-proceed-requests` (`requestNoticeToProceed`) — done ([openapi/moer.yaml](openapi/moer.yaml)).
3. **MCP** artifact: `find_environmental_sites`, `get_environmental_site`, `find_e_designations`, `get_e_designation`, `find_cleanup_projects`, `get_cleanup_project`, `get_remediation_status`, `find_notices`, `list_my_notice_to_proceed_requests`, `request_notice_to_proceed` — done ([mcp/moer-mcp.json](mcp/moer-mcp.json)).
