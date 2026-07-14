# Low-Hanging Fruit Index — DOI

**Agency:** New York City Department of Investigation (DOI)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt — `nyc.gov/robots.txt` only disallows `/html/misc/`). Fingerprinted the informational site `nyc.gov/site/doi` (Akamai + nginx + NYC.gov "Livesite" v22 + Dynatrace). Followed "Report Corruption" → "Submit Report Online" to its host — a third-party **Kaseware** intake portal (`app.kaseware.us/public/#NYCDOI/…`, Cloudflare-fronted, title "Kaseware Portal"). Confirmed the public reports are **PDFs** under `/assets/doi/reports/pdf/<year>/`. Verified the NYC Open Data agency label `Department of Investigation (DOI)` via the Socrata Discovery API and pulled all **4** assets with column schemas.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-doi.md](opendata-doi.md).

## Headline findings

1. **DOI is New York City's Inspector General — but its core output is unstructured.** Public investigation reports and reform recommendations are published **only as PDFs** (`/assets/doi/reports/pdf/<year>/`), with no structured Open Data twin and no content API.
2. **Its Open Data is oversight, not investigations.** The **4 datasets** are dominated by **City Marshal oversight** — executed **Evictions** (`6z8x-wfk4`, ~237k views, DOI's most-viewed asset) and **City Marshals Revenue** — plus the **PPR recommendations** tracker and monthly performance indicators.
3. **The core transaction runs on a vendor.** Reporting fraud, waste, or corruption — the tip that starts every investigation — runs through a **third-party Kaseware** intake form (`app.kaseware.us`) with phone/fax/mail fallbacks. No API.
4. **One structured bridge exists.** The **PPR Portal** (`jstn-jaut`) publishes DOI's recommendations to agencies with acceptance and implementation status — proof the reports could be digitized too.

> **Reframe (a distinct pattern):** DORIS = *retrieve* records from a vendor DAMS; OCME = *instrument* a bare agency; DVS = *coordinate* a referral off a vendor form; **DOI = digitize the outputs and the intake.** Here the oversight data is already open — the work is least about liberating datasets and most about giving DOI's **investigative reports** (PDF-only) and its **corruption-complaint intake** (a Kaseware form) an owned, structured, agent-native API.

## The fruit

| # | Name | Entity | Where the data lives | Open Data twin |
|---|---|---|---|---|
| 1 | Public Investigation Reports | `PublicReport` | PDFs on nyc.gov | ❌ gap (PDF only) |
| 2 | Policy & Procedure Recommendations | `PolicyRecommendation` | SODA | 🟡 PPR Portal (`jstn-jaut`, 7c) |
| 3 | Evictions (City Marshal oversight) | `Eviction` | SODA + geography | ✅ Evictions (`6z8x-wfk4`, 20c) |
| 4 | City Marshals Revenue | `MarshalRevenue` | SODA | ✅ City Marshals Revenue (`7ewi-9cdf`, 5c) |
| 5 | Monthly Performance Reports | `PerformanceIndicator` | SODA | ✅ Perf. Mgmt Reports (`i8ua-bnkj`, 3c) |
| 6 | **Report Corruption (complaint)** | `CorruptionComplaint` | Kaseware portal + phone | ❌ **net-new** |
| 7 | Whistleblower / EO-16 obligation | `CorruptionComplaint` | Kaseware + phone/fax/mail | ❌ gap (no API) |
| 8 | OIG-NYPD complaint | `CorruptionComplaint` | Kaseware + phone | ❌ gap (no API) |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **Socrata SODA** — 4 DOI datasets (the one real, open API; oversight data, not investigations).
- **Kaseware** — the "Submit Report Online" corruption-complaint intake; a third-party case-management SaaS, client-rendered SPA, Cloudflare-fronted, no API.
- Platform: informational site on the **NYC.gov shared "Livesite" platform** (Akamai edge, nginx, Dynatrace RUM); public reports as static PDFs under `/assets/doi/reports/pdf/`.

## Reverse-engineered entities

`PublicReport` (PDF-only; net gap) · `PolicyRecommendation` (structured twin) · `Eviction` · `MarshalRevenue` · `PerformanceIndicator` · `CorruptionComplaint` (net-new write; also stands in for the whistleblower/EO-16 and OIG-NYPD intake flavors) — join keys: **Court Index / Docket Number**, **Marshal Last Name + Year**, **BBL/BIN** (evictions geography spine).

## Next

1. **JSON Schema** per entity, reconciling real Open Data column names and the PDF-report metadata — done ([schemas/](schemas/)).
2. **OpenAPI** publishing the open oversight data + a `PublicReport` index as clean resources + the net-new `POST /complaints` (report corruption) — done ([openapi/doi.yaml](openapi/doi.yaml)).
3. **MCP** artifact: `find_reports`, `get_report`, `find_recommendations`, `find_evictions`, `find_marshal_revenue`, `find_performance_indicators`, `list_my_complaints`, `file_complaint` — done ([mcp/doi-mcp.json](mcp/doi-mcp.json)).
