# Low-Hanging Fruit Index — HRA / DSS

**Agency:** NYC Human Resources Administration / Department of Social Services (HRA/DSS)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt — `nyc.gov/robots.txt` only disallows `/html/misc/`). Fingerprinted the informational site `nyc.gov/site/hra` (Akamai + nginx + NYC.gov "Livesite" + Dynatrace), the **ACCESS NYC** eligibility screener `access.nyc.gov` (Cloudflare + WP Engine / WordPress), and the **ACCESS HRA** application portal `a069-access.nyc.gov/accesshra` (React SPA behind Akamai bot protection). Confirmed via GitHub that ACCESS NYC's eligibility logic is **open source** — `NYCOpportunity/ACCESS-NYC-Rules`, a Drools rules engine. Verified the NYC Open Data agency label `Human Resources Administration (HRA)` via the Socrata Discovery API (the alternate `Department of Social Services (DSS)` returns 0) and pulled all **49** assets with column schemas.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-hra.md](opendata-hra.md).

## Headline findings

1. **HRA is a three-surface benefits domain.** An informational NYC.gov/Livesite site, the **ACCESS NYC** eligibility screener (WordPress/WP Engine), and the **ACCESS HRA** application portal (a React SPA behind Akamai) with **no API**.
2. **The eligibility logic is open source.** `NYCOpportunity/ACCESS-NYC-Rules` is a public **Drools** business rules engine driving the screener at `access.nyc.gov/eligibility`, alongside a `benefits-screening-api`. The rules are public and city-owned — but no hosted API returns a determination to a caller.
3. **The caseload data is unusually open.** **49 NYC Open Data datasets** cover SNAP/Cash Assistance/Medicaid recipient and case counts, application-center directories (Benefits Access Centers, SNAP Centers, Medicaid Offices, Homebase), wait times, and 75-column case-action reports.
4. **But the service layer is locked.** Applying for and tracking a benefits case — the thing residents actually *do* — lives only inside the ACCESS HRA React portal or an in-person visit. None of it has a machine-readable contract, and no dataset exposes an individual application/case (aggregate case-action counts are the closest twin).

> **Reframe (fifth distinct pattern):** Parks = *replatform* a legacy site; DOE = *reclaim* rented search + a hidden backend; Council = *consolidate + own* three fragmented APIs; NYCHA = *unlock* a service layer trapped in a vendor CRM; **HRA = connect the benefits journey.** Here the data is open *and* the eligibility engine is already open-sourced — the work is least about liberating datasets or rebuilding logic and most about giving the **journey** (screen → determine eligibility → apply → track a case) one owned, agent-native API instead of three disconnected apps.

## The fruit

| # | Name | Entity | Where the data lives | Open Data twin |
|---|---|---|---|---|
| 1 | Benefit Programs & Services | `Program` | SODA + ACCESS NYC | ✅ HRA Facts (`np6w-pies`); NYC Benefits Platform (`kvhd-5fmu`) |
| 2 | Centers & Offices | `Center` | SODA + map | ✅ Benefits Access (`9d9t-bmk7`), SNAP (`tc6u-8rnp`), Medicaid (`ibs4-k445`), Homebase (`ntcm-2w4k`) |
| 3 | Caseload & Enrollment | `CaseloadStatistic` | SODA | 🟡 SNAP (`5c4s-jwtq`), CA (`qtrj-g3nm`), Medicaid (`33db-aeds`) — aggregate |
| 4 | Case Actions | `CaseAction` | SODA | 🟡 Rejections/Closed/Reopenings (`g6pg-qint`…) — aggregate |
| 5 | Eligibility screening | `BenefitsEligibility` | ACCESS NYC Drools rules | ❌ open source, but no hosted result API |
| 6 | Apply for benefits | `BenefitsApplication` | ACCESS HRA portal + centers | ❌ **net-new** (no API) |
| 7 | Check case status | `BenefitsApplication` | ACCESS HRA portal | ❌ gap (read side of net-new) |
| 8 | Emergency assistance | `BenefitsApplication` | ACCESS HRA portal | 🟡 aggregate requests (`5vgr-4tp3`) only |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **Socrata SODA** — 49 HRA datasets (the one real, open API; reference/caseload data only).
- **ACCESS NYC Drools rules** — `NYCOpportunity/ACCESS-NYC-Rules`; the eligibility logic is open source, but there is no hosted determination API.
- **ACCESS HRA React SPA** — the application portal; login-walled, JavaScript-only, Akamai-gated, no API.
- Platform: informational site on the **NYC.gov shared "Livesite" platform** (Akamai edge, nginx, Dynatrace RUM) — the same chassis as Parks/DOE/Council/NYCHA; ACCESS NYC adds WordPress/WP Engine + Cloudflare.

## Reverse-engineered entities

`Program` · `Center` · `CaseloadStatistic` (aggregate) · `CaseAction` (aggregate; never individual) · `BenefitsEligibility` (ACCESS NYC screening result) · `BenefitsApplication` (net-new write; the ACCESS-HRA-locked apply/case-status transaction, also standing in for emergency assistance) — join keys: **program code**, **center number**, the **BIN/BBL/NTA/council** geography spine.

## Next

1. **JSON Schema** per entity, reconciling real Open Data column names (program metadata, center directories, the 75-column case-action breakdowns, the geography spine) — done ([schemas/](schemas/)).
2. **OpenAPI** publishing the open reference data as clean resources + `POST /eligibility` (wrapping the open rules) + the net-new `POST /applications` (apply for benefits) — done ([openapi/hra.yaml](openapi/hra.yaml)).
3. **MCP** artifact: `find_programs`, `get_program`, `find_centers`, `find_caseload_statistics`, `find_case_actions`, `screen_eligibility`, `list_my_applications`, `get_application`, `apply_for_benefits` — done ([mcp/hra-mcp.json](mcp/hra-mcp.json)).
