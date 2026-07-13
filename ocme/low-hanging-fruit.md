# Low-Hanging Fruit Index — OCME

**Agency:** NYC Office of Chief Medical Examiner (OCME)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt — `nyc.gov/robots.txt` only disallows `/html/misc/`). Fingerprinted the informational site `nyc.gov/site/ocme` (Akamai + nginx + AWS ALB + NYC.gov "Livesite" platform + Dynatrace) and confirmed OCME runs **no agency-specific application** — its records-request service layer is paper forms plus NYC **311** (`portal.311.nyc.gov`). Verified the NYC Open Data agency label `Office of Chief Medical Examiner (OCME)` via the Socrata Discovery API: **exactly one** asset.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-ocme.md](opendata-ocme.md).

## Headline findings

1. **OCME is the most data-dark agency assessed.** A single dataset carries its Open Data label — 'Monthly Indicators' (`8r6c-ydwk`), a Mayor's Management Report passthrough whose real months run only **July 2015 - May 2016**. It is not casework.
2. **There is no OCME application at all.** No portal, no CRM, no login to fingerprint. The records-request service layer is a **notarized paper form and NYC 311**, with a **three-to-six-month** turnaround.
3. **The core object is confidential by law.** A **death investigation** is never published — not per-decedent, not in aggregate. Any responsible surface must stay non-identifying.
4. **What little is public is federated elsewhere.** Missing-persons visibility lives in federal **NamUs**; death *certificates* are issued by **DOHMH**, not OCME. OCME owns almost none of its own digital footprint.

> **Reframe (fifth distinct pattern):** Parks = *replatform* a legacy site; DOE = *reclaim* rented search; Council = *consolidate + own* fragmented APIs; NYCHA = *unlock* a locked service layer; **OCME = instrument** it. Here there is almost nothing to liberate and nothing to unlock — the work is *first, careful instrumentation* of the least-instrumented, most privacy-constrained agency: publish the few responsibly-public resources, and give grieving families one dignified digital path to request a decedent's record.

## The fruit

| # | Name | Entity | Where the data lives | Open Data twin |
|---|---|---|---|---|
| 1 | Monthly performance indicators | `MonthlyIndicator` | SODA | 🟡 Monthly Indicators (`8r6c-ydwk`, 16c) — stale 2015-16 |
| 2 | Death-investigation statistics (aggregate) | `CaseStatistics` | reporting-a-case (HTML) | ❌ no data (net-new, aggregate only) |
| 3 | Forensic services / disciplines | `ForensicService` | services pages (HTML) | ❌ gap |
| 4 | Family services centers | `FamilyServicesCenter` | locations pages (HTML + phone) | ❌ gap |
| 5 | Missing persons / unidentified | `MissingPerson` | NamUs (federal) | 🟡 federated (not OCME) |
| 6 | **Request a casefile record** | `DeathRecordRequest` | paper forms + 311 | ❌ **net-new** |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **Socrata SODA** — one OCME dataset (stale MMR passthrough); the only OCME-labeled machine-readable asset.
- **NYC 311** (`portal.311.nyc.gov`) — the de facto records-request channel; not an OCME system, no OCME API.
- **Federal NamUs** — where OCME missing-persons/unidentified cases surface; owned by US DOJ.
- Platform: informational site on the **NYC.gov shared "Livesite" platform** (Akamai edge, nginx, AWS ALB, Dynatrace RUM) — the same chassis as NYCHA's informational site, but here it is the *only* digital surface OCME has.

## Reverse-engineered entities

`MonthlyIndicator` · `CaseStatistics` (aggregate; never an individual death investigation) · `ForensicService` · `FamilyServicesCenter` · `MissingPerson` (public NamUs listing) · `DeathRecordRequest` (net-new write; also the read/status surface for a submitted request) — the deliberately non-identifying join key is an OCME **case number**, never a decedent's clinical record.

## Next

1. **JSON Schema** per entity, keeping casework at a respectful, non-identifying altitude — done ([schemas/](schemas/)).
2. **OpenAPI** publishing the responsibly-public resources as clean reads + the net-new `POST /record-requests` (request a casefile record) — done ([openapi/ocme.yaml](openapi/ocme.yaml)).
3. **MCP** artifact: `list_indicators`, `find_case_statistics`, `find_services`, `find_family_services_centers`, `find_missing_persons`, `list_my_record_requests`, `get_record_request`, `request_record` — done ([mcp/ocme-mcp.json](mcp/ocme-mcp.json)).
