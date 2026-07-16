# Cross-Domain Synthesis

*What seventy New York City government domains reveal, assessed the same way — and what a citywide API modernization would actually take.*

Companion to the 70 domain assessments. Interactive version, with the aggregate scorecard, at **[nyc.apievangelist.com/synthesis.html](https://nyc.apievangelist.com/synthesis.html)**.

---

## The corpus

Seventy NYC government domains — mayoral agencies, elected offices, the five borough presidents, the five district attorneys, oversight boards, public authorities (CUNY, H+H, EDC, SCA), and the three library systems — each run through the identical seven-step method (assess → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schema per object → OpenAPI → MCP). The totals: **2,681 Open Data assets mapped, 439 JSON Schemas, 752 API operations, 653 MCP tools** — all design-first artifacts. Every falsifiable claim was re-verified (**69 of 70 high confidence**; sampled Open Data assets all resolve; one confirmed defect — the Public Advocate's site is down). See [QA / verification](https://nyc.apievangelist.com/qa.html).

## The definitive finding: two flat columns

Every domain is scored 0–3 on seven dimensions by **one deterministic rule-based function** applied uniformly ([data/scorecard.json](data/scorecard.json); see `scoring_method`) — Open Data asset counts, the observed-API inventory, and platform fingerprints, *not* the earlier per-subagent self-scores, so the numbers are comparable across all 70. The result is inescapable — two columns are flat across the **entire** city government:

| Dimension | Mean | Domains scoring 0 | Domains scoring ≥2 |
|---|---|---|---|
| Platform modernity | 2.1 | 0 / 70 | **62 / 70** |
| Vendor independence | 2.1 | 0 / 70 | 54 / 70 |
| Core data machine-readable | 2.1 | 6 / 70 | 50 / 70 |
| Open Data breadth | 1.5 | 8 / 70 | 36 / 70 |
| Site / content API | 1.2 | **17 / 70** | 19 / 70 |
| **Transactional (write) API** | **0.03** | **68 / 70** | **0 / 70** |
| **Agent-readiness** | **0.00** | **70 / 70** | **0 / 70** |

Open data is broad and platforms are mostly maintained. But **not one of 70 domains scores above a 1 on having a transactional write API, and every single one scores 0 on agent-readiness.** 68 of 70 have *no* citizen write API at all; 70 of 70 have *no* agent surface. These two gaps are independent of platform, budget, or open-data maturity. They are the citywide condition.

## The taxonomy: ~40 verbs, five families

The method assigns each domain a one-word *modernization verb*. Seventy assessments produced **~40 distinct verbs** — proliferation that is itself a finding: there is no single fix. But they collapse into **five families**:

1. **Digitize** *(the data isn't machine-readable at all).* Elections, DOI, OCME, Tax Commission, BSA, CCHR, the DAs. Results, candidates, appeals, complaints trapped in PDFs, Power BI iframes, or prose. The original 2013 low-hanging-fruit case, still alive.
2. **Expose** *(a private, hidden, or undocumented API already exists — publish and document it).* HPD (WSO2 REST), IBO (Content API v2), CFB (FTMSearchWebAPI), DSNY (pickup backends), NYPD (Azure Gov), plus the dozens of **accidental APIs** — undocumented WordPress REST and Drupal JSON:APIs leaking from Council, MOCJ, the DAs, BPL. *The dominant move across the corpus is Expose, not Build.*
3. **Unify / Federate** *(fragmented sources or near-identical offices — one shared contract).* Council's three APIs; DOT's 267 scattered datasets; and most strikingly the **five Borough Presidents, five District Attorneys, and three libraries** — each running bespoke thin sites for identical functions. They beg for one shared *Borough President API*, *District Attorney API*, and *Library API*.
4. **Transact** *(reporting data is open, but the citizen transaction is locked behind a vendor or legacy app — build the write API).* The largest family: DOB, DOHMH, DEP, NYCHA, FDNY, DHS, DCAS, SBS, City Clerk, MOME, OATH, BIC, SCA, HRA. Permits, enrollments, licenses, appointments, marriage licenses, ballots — locked in Accela, Salesforce, Siebel, Unqork, Dynamics, PeopleSoft, Struts.
5. **Standardize / Lead** *(an open or industry standard exists — adopt, extend, or model it).* NYC311 should revive **Open311**; H+H has a live **FHIR** endpoint to extend; DCP is the **geography anchor**; OTI runs the **gateway**; **NYPL leads** with three real public APIs. The capability exists in-house — it just isn't generalized.

## Cross-cutting findings

1. **The service layer is the universal gap, not the data.** Reporting data is broadly open; the transactional service layer is missing, hidden, or vendor-locked almost everywhere. This is the meta-finding of all 70.
2. **A citizen write-workflow with no API — in nearly every domain.** 69 net-new write objects across the corpus (permit, enrollment, ballot, 311 request, vital record, marriage license, film permit, work order, tip, hold…). Open data liberated reporting; it never touched transactions.
3. **Agent-readiness is zero — all 70.** Not one domain ships a meaningful agent surface. Every MCP artifact in this project is net-new.
4. **"Accidental APIs" are everywhere.** Dozens of agencies unknowingly expose a WordPress REST or Drupal JSON:API; several run real private APIs. The machine-readable surface often already exists — undocumented and unowned.
5. **Near-identical offices multiply cost.** Five BPs, five DAs, three libraries, ~25 CUNY campuses — each a bespoke build of the same thing. Consolidation into shared, templated APIs is the clearest efficiency win.
6. **Vendor sprawl, uncoordinated.** Accela, Salesforce, Siebel, Unqork, Kaseware, Dynamics 365, Epic, BiblioCommons, PeopleSoft, Struts, Everbridge, Combined Arms — a different SaaS per agency, no shared strategy; sometimes the vendor *is* the only API (Legistar, Checkbook, FHIR).
7. **Platform sprawl — ~20 distinct stacks, zero shared API layer.** Smarty, Sitefinity, WordPress, Drupal, Dynamics, Oracle WebCenter, DotNetNuke, Weebly, Revize, Next.js, and more. Consistency must be imposed *above* the platforms.
8. **The standards made for NYC's problems go unadopted.** NYC pioneered **Open311** and let it lapse; **FHIR** runs at H+H but read-only; the **geography spine** recurs in all 70 but has no shared schema. The city keeps declining the standards built for exactly this: seven sector standards (Open311, FHIR, OpenReferral/HSDS, OCDS, GTFS, iCalendar, Popolo) apply across ~51 domain-slots and **exactly one is adopted** (H+H's FHIR). See [standards](https://nyc.apievangelist.com/standards.html).
9. **The counter-examples prove it's achievable.** NYPL (three owned public APIs), H+H (live FHIR), OTI (the api.nyc.gov gateway + Open Data), DCP (open-source geocoder). The talent and pattern exist inside the city already.
10. **Digital assets are decaying.** `brooklyn-usa.org` lapsed and now redirects off-site; the Public Advocate's site returned 502 during the crawl; `rcda.nyc.gov` is dead. Ungoverned surfaces rot.
11. **The shared geography spine recurs in all 70.** Borough · Community Board · Council District · Census Tract/NTA · BBL/BIN — every schema's `_common.json`. City Planning is its authoritative source: the basis for **`nyc-commons`**.
12. **No cross-domain identity.** Every domain has its own join key (gisPropNum, DBN, matterId, service_request_id…). A resident is the same person across all 70, but nothing links them.
13. **The stack is majority-proprietary — but the exits exist.** Of the 79 distinct technologies detected, **58 are commercial, 4 open-core, 17 open source**; the median domain's detected stack is **71% strictly-commercial** and **60 of 70 domains are majority-proprietary** (four are entirely proprietary in what we could see). Yet **every one of the 62 commercial/open-core tools has a credible open-source alternative** — Socrata→CKAN, Esri ArcGIS→QGIS+GeoServer+PostGIS, Salesforce/Siebel→SuiteCRM/Odoo, Accela→Form.io+Camunda, Google Analytics→Matomo, New Relic/Dynatrace→OpenTelemetry+Grafana, Azure APIM→Kong/Tyk/APISIX. Vendor lock-in is a choice the city re-makes by default, not a constraint. See [technology.html](https://nyc.apievangelist.com/technology.html).

## Recommendations — the NYC API playbook

1. **Run the five plays, per domain:** *Digitize* the PDF/iframe data; *Expose* the private and accidental APIs; *Unify/Federate* fragmented sources and duplicate offices; *Transact* — build the missing write APIs; *Standardize* on Open311, FHIR, and `nyc-commons`.
2. **Prioritize the write layer citywide.** 68 of 70 have no transactional API; it is the highest-value, most-uniform gap.
3. **Mandate agent-native by default.** Zero of 70 are agent-ready today; make an MCP surface a standard deliverable.
4. **Build the shared APIs for duplicate offices** — one Borough President API, one District Attorney API, one Library API — instead of 13 bespoke sites.
5. **Publish `nyc-commons`** (the geography spine + `Address`/`Place` identity) and have every agency `$ref` it. City Planning anchors it.
6. **Own the vendor-held and accidental APIs.** Front Legistar, Checkbook, FHIR, and the leaking WordPress/Drupal APIs with owned, documented contracts.
7. **Adopt the standards already made for the problem** — revive Open311, extend FHIR, model NYPL.
8. **Register everything** in an [APIs.json](https://apisjson.org) index so the citywide surface is navigable by humans and agents — the connective tissue open data never had.
9. **Govern the surface.** Lapsed domains and 502s are a security and trust problem; inventory and monitor what the city runs.

## Turning the assessment into a roadmap

Three analyses mine the collected data to move from "what's broken" to "what to do":

**Priority — where to start** ([opportunity.html](https://nyc.apievangelist.com/opportunity.html)). Every domain scored **demand × gap × feasibility** — demand from Open Data page-views and the reach of its locked citizen transaction, feasibility from whether an API/open data already exists (cheap) vs. data that must be digitized (expensive). The top of the list is high-demand agencies with a locked high-value transaction and data already in hand: **DCAS, DOB, NYPD, DOF, Parks, DOHMH, HPD, 311**. **25 domains are "quick wins"** — high impact and already feasible.

**Linkage — the connective tissue** ([linkage.html](https://nyc.apievangelist.com/linkage.html)). The shared join keys, detected across all 70 schemas: **Borough and Coordinates appear in every one of the 70**; Council District (17), Community Board (17), Census Tract / NTA (9). The **property keys — BBL and BIN** — are the real connectors that would stitch Buildings ↔ Finance ↔ Housing ↔ Planning ↔ 311 into one addressable graph. This is the `nyc-commons` case in data.

**Transactions — build these once** ([transactions.html](https://nyc.apievangelist.com/transactions.html)). The 69 net-new write workflows collapse into a handful of primitives: **Apply (31)**, Report/Complain (17), Request-records (5), Schedule/Reserve (4), Register (2), Dispute/File (2), Pay (1). The city doesn't need 69 bespoke builds — it needs one excellent "Apply" pattern (permits, enrollment, benefits, licenses, lottery) and a "Report" pattern (complaints, tips, 311), reused across agencies.

**Standards — adopt what exists** ([standards.html](https://nyc.apievangelist.com/standards.html)). Most of what NYC builds bespoke already has an open standard — Open311 for service requests, FHIR for health, OpenReferral/HSDS for human-service directories, OCDS for procurement, GTFS for mobility, Popolo for legislative people. Adoption is ~1 of 51 applicable slots. And the project's own contracts — **JSON Schema → OpenAPI → MCP → APIs.json** — are the standards that make the whole thing interoperable.

## Coda

Seventy domains, ~20 platforms, dozens of vendors, ~40 verbs — and one flat truth: NYC largely *published* its data and almost never made itself *programmable*. The write layer and the agent layer are empty across the whole city. The counter-examples — NYPL, H+H, OTI, DCP — show the way, and the shared spine and the five plays show the path.

The goal was never more datasets. It's a city you can **program**.

---
*70 domains assessed 2026 · [nyc.apievangelist.com](https://nyc.apievangelist.com) · [api-evangelist/nyc](https://github.com/api-evangelist/nyc). All APIs and MCP servers referenced are design-first artifacts, not deployments.*
