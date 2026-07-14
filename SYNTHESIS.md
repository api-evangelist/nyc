# Cross-Domain Synthesis

*What sixty-seven New York City government domains reveal, assessed the same way — and what a citywide API modernization would actually take.*

Companion to the 67 domain assessments. Interactive version, with the aggregate scorecard, at **[nyc.apievangelist.com/synthesis.html](https://nyc.apievangelist.com/synthesis.html)**.

---

## The corpus

Sixty-seven NYC government domains — mayoral agencies, elected offices, the five borough presidents, the five district attorneys, oversight boards, public authorities (CUNY, H+H, EDC, SCA), and the three library systems — each run through the identical seven-step method (assess → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schema per object → OpenAPI → MCP). The totals: **2,666 Open Data assets mapped, 422 JSON Schemas, 721 API operations, 624 MCP tools** — all design-first artifacts.

## The definitive finding: two flat columns

Scoring every domain 0–3 across seven dimensions ([data/scorecard.json](data/scorecard.json)) produces one inescapable result. Two columns are flat across the **entire** city government:

| Dimension | Mean | Domains scoring 0 | Domains scoring ≥2 |
|---|---|---|---|
| Open Data breadth | 1.9 | 9 / 67 | **43 / 67** |
| Core data machine-readable | 1.8 | 7 / 67 | 44 / 67 |
| Platform modernity | 1.6 | 0 / 67 | 33 / 67 |
| Vendor independence | 1.5 | 1 / 67 | 30 / 67 |
| Site / content API | 0.8 | **33 / 67** | 16 / 67 |
| **Transactional (write) API** | **0.10** | **60 / 67** | **0 / 67** |
| **Agent-readiness** | **0.04** | **64 / 67** | **0 / 67** |

Open data is broad — 43 of 67 agencies publish substantially. But **not one of 67 domains scores above a 1 on having a transactional write API, and not one scores above a 1 on agent-readiness.** 60 of 67 have *no* citizen write API at all; 64 of 67 have *no* agent surface. These two gaps are independent of platform, budget, or open-data maturity. They are the citywide condition.

## The taxonomy: ~40 verbs, five families

The method assigns each domain a one-word *modernization verb*. Sixty-seven assessments produced **~40 distinct verbs** — proliferation that is itself a finding: there is no single fix. But they collapse into **five families**:

1. **Digitize** *(the data isn't machine-readable at all).* Elections, DOI, OCME, Tax Commission, BSA, CCHR, the DAs. Results, candidates, appeals, complaints trapped in PDFs, Power BI iframes, or prose. The original 2013 low-hanging-fruit case, still alive.
2. **Expose** *(a private, hidden, or undocumented API already exists — publish and document it).* HPD (WSO2 REST), IBO (Content API v2), CFB (FTMSearchWebAPI), DSNY (pickup backends), NYPD (Azure Gov), plus the dozens of **accidental APIs** — undocumented WordPress REST and Drupal JSON:APIs leaking from Council, MOCJ, the DAs, BPL. *The dominant move across the corpus is Expose, not Build.*
3. **Unify / Federate** *(fragmented sources or near-identical offices — one shared contract).* Council's three APIs; DOT's 267 scattered datasets; and most strikingly the **five Borough Presidents, five District Attorneys, and three libraries** — each running bespoke thin sites for identical functions. They beg for one shared *Borough President API*, *District Attorney API*, and *Library API*.
4. **Transact** *(reporting data is open, but the citizen transaction is locked behind a vendor or legacy app — build the write API).* The largest family: DOB, DOHMH, DEP, NYCHA, FDNY, DHS, DCAS, SBS, City Clerk, MOME, OATH, BIC, SCA, HRA. Permits, enrollments, licenses, appointments, marriage licenses, ballots — locked in Accela, Salesforce, Siebel, Unqork, Dynamics, PeopleSoft, Struts.
5. **Standardize / Lead** *(an open or industry standard exists — adopt, extend, or model it).* NYC311 should revive **Open311**; H+H has a live **FHIR** endpoint to extend; DCP is the **geography anchor**; OTI runs the **gateway**; **NYPL leads** with three real public APIs. The capability exists in-house — it just isn't generalized.

## Cross-cutting findings

1. **The service layer is the universal gap, not the data.** Reporting data is broadly open; the transactional service layer is missing, hidden, or vendor-locked almost everywhere. This is the meta-finding of all 67.
2. **A citizen write-workflow with no API — in nearly every domain.** 66 net-new write objects across the corpus (permit, enrollment, ballot, 311 request, vital record, marriage license, film permit, work order, tip, hold…). Open data liberated reporting; it never touched transactions.
3. **Agent-readiness is essentially zero — 64 of 67.** Not one domain ships a meaningful agent surface. Every MCP artifact in this project is net-new.
4. **"Accidental APIs" are everywhere.** Dozens of agencies unknowingly expose a WordPress REST or Drupal JSON:API; several run real private APIs. The machine-readable surface often already exists — undocumented and unowned.
5. **Near-identical offices multiply cost.** Five BPs, five DAs, three libraries, ~25 CUNY campuses — each a bespoke build of the same thing. Consolidation into shared, templated APIs is the clearest efficiency win.
6. **Vendor sprawl, uncoordinated.** Accela, Salesforce, Siebel, Unqork, Kaseware, Dynamics 365, Epic, BiblioCommons, PeopleSoft, Struts, Everbridge, Combined Arms — a different SaaS per agency, no shared strategy; sometimes the vendor *is* the only API (Legistar, Checkbook, FHIR).
7. **Platform sprawl — ~20 distinct stacks, zero shared API layer.** Smarty, Sitefinity, WordPress, Drupal, Dynamics, Oracle WebCenter, DotNetNuke, Weebly, Revize, Next.js, and more. Consistency must be imposed *above* the platforms.
8. **The standards made for NYC's problems go unadopted.** NYC pioneered **Open311** and let it lapse; **FHIR** runs at H+H but read-only; the **geography spine** recurs in all 67 but has no shared schema. The city keeps declining the standards built for exactly this.
9. **The counter-examples prove it's achievable.** NYPL (three owned public APIs), H+H (live FHIR), OTI (the api.nyc.gov gateway + Open Data), DCP (open-source geocoder). The talent and pattern exist inside the city already.
10. **Digital assets are decaying.** `brooklyn-usa.org` lapsed and now redirects off-site; the Public Advocate's site returned 502 during the crawl; `rcda.nyc.gov` is dead. Ungoverned surfaces rot.
11. **The shared geography spine recurs in all 67.** Borough · Community Board · Council District · Census Tract/NTA · BBL/BIN — every schema's `_common.json`. City Planning is its authoritative source: the basis for **`nyc-commons`**.
12. **No cross-domain identity.** Every domain has its own join key (gisPropNum, DBN, matterId, service_request_id…). A resident is the same person across all 67, but nothing links them.

## Recommendations — the NYC API playbook

1. **Run the five plays, per domain:** *Digitize* the PDF/iframe data; *Expose* the private and accidental APIs; *Unify/Federate* fragmented sources and duplicate offices; *Transact* — build the missing write APIs; *Standardize* on Open311, FHIR, and `nyc-commons`.
2. **Prioritize the write layer citywide.** 60 of 67 have no transactional API; it is the highest-value, most-uniform gap.
3. **Mandate agent-native by default.** Zero of 67 are agent-ready today; make an MCP surface a standard deliverable.
4. **Build the shared APIs for duplicate offices** — one Borough President API, one District Attorney API, one Library API — instead of 13 bespoke sites.
5. **Publish `nyc-commons`** (the geography spine + `Address`/`Place` identity) and have every agency `$ref` it. City Planning anchors it.
6. **Own the vendor-held and accidental APIs.** Front Legistar, Checkbook, FHIR, and the leaking WordPress/Drupal APIs with owned, documented contracts.
7. **Adopt the standards already made for the problem** — revive Open311, extend FHIR, model NYPL.
8. **Register everything** in an [APIs.json](https://apisjson.org) index so the citywide surface is navigable by humans and agents — the connective tissue open data never had.
9. **Govern the surface.** Lapsed domains and 502s are a security and trust problem; inventory and monitor what the city runs.

## Coda

Sixty-seven domains, ~20 platforms, dozens of vendors, ~40 verbs — and one flat truth: NYC largely *published* its data and almost never made itself *programmable*. The write layer and the agent layer are empty across the whole city. The counter-examples — NYPL, H+H, OTI, DCP — show the way, and the shared spine and the five plays show the path.

The goal was never more datasets. It's a city you can **program**.

---
*67 domains assessed 2026 · [nyc.apievangelist.com](https://nyc.apievangelist.com) · [api-evangelist/nyc](https://github.com/api-evangelist/nyc). All APIs and MCP servers referenced are design-first artifacts, not deployments.*
