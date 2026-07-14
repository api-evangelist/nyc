# Crosswalk — Website/Portal Fruit ↔ APIs ↔ NYC Open Data (DOI)

Maps the low-hanging fruit on **nyc.gov/site/doi** and the **Report Corruption** intake to (a) the **existing APIs** (Socrata SODA; the Kaseware portal) and (b) the **4 DOI datasets** on NYC Open Data. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-doi.json](opendata-doi.json).

## The reframe — a distinct pattern

- **DORIS:** open indexes, records trapped in a vendor DAMS → *retrieve.*
- **OCME:** one stale dataset, no application, paper forms → *instrument.*
- **DVS:** open service data, the referral runs through a third-party vendor form → *coordinate.*
- **DOI:** the **investigative reports exist only as PDFs** and the **corruption complaint runs on a third-party Kaseware form** → **digitize the outputs and the intake.**

DOI is New York City's Inspector General, yet the two things that define it have no structured surface. Its **public reports** — findings, subject agencies, recommendations — are published only as PDFs. Its **corruption complaint** — the tip that starts every investigation — is a client-rendered vendor form. What *is* open (evictions, marshal revenue, performance) is oversight of the City Marshals DOI regulates, not DOI's own casework. The one bridge is the **PPR Portal**, which publishes DOI's recommendations to agencies as structured data — proof the reports could be digitized too.

Coverage: ✅ strong open twin · 🟡 partial/structured-fragment · ❌ gap (no API).

## Entity crosswalk

| Entity | Website / Portal | API today | Open Data | Cov. |
|---|---|---|---|---|
| `PublicReport` | `/newsroom/public-reports-current` | **PDF only** | — | ❌ gap (PDF) |
| `PolicyRecommendation` | `/about/…ppr-portal` | SODA | Policy & Procedure Recommendations (`jstn-jaut`, 7c) | 🟡 structured twin |
| `Eviction` | marshals list | SODA | Evictions (`6z8x-wfk4`, 20c) — ~237k views | ✅ |
| `MarshalRevenue` | marshals list | SODA | City Marshals Revenue (`7ewi-9cdf`, 5c) | ✅ |
| `PerformanceIndicator` | — | SODA | Monthly Performance Management Reports (`i8ua-bnkj`, 3c) | ✅ |
| **`CorruptionComplaint`** (report corruption) | Kaseware intake + phone | **Kaseware form only** | — | ❌ **net-new** |

## The mismatch, concretely

| Source | Strength | Weakness |
|---|---|---|
| **Socrata SODA (4 datasets)** | Open, machine-readable; strong on City Marshal oversight (evictions is a ~237k-view asset) and structured on recommendations | It is *oversight* data, not DOI's investigations; no report content, no complaints |
| **PDF report library** | The real work product — findings, subject agencies, reform recommendations | Static PDFs; no metadata, no index API, nothing an agent can query |
| **Kaseware intake portal** | The real transaction system — filing a corruption complaint | Third-party vendor SaaS; client-rendered SPA, no API, no OpenAPI; not agent-accessible; phone/fax/mail fallback |

## Implications for the API-first + MCP proposal

1. **Index the reports.** Publish `PublicReport` metadata (title, date, unit/OIG, subject agency, `pdfUrl`, recommendation count) as one clean resource so the investigative corpus is searchable — the PPR dataset shows DOI can already publish structured recommendations ([OpenAPI](openapi/doi.yaml)).
2. **Publish the oversight data as one resource model.** Evictions, marshal revenue, recommendations, and performance behind one owned DOI contract — so consumers learn one model, not 4 Socrata IDs.
3. **Own the intake.** Add the net-new write workflow — `file_complaint` (report fraud/waste/corruption) — with anonymous filing, Whistleblower-Law protection, and the EO-16 employee reporting obligation, replacing the Kaseware-only form.
4. **MCP server** so an agent can answer "what did DOI recommend to NYCHA and did they implement it?", "which marshal executed the most evictions in the Bronx last year?", and — the point — "help me report corruption at my agency, anonymously."
