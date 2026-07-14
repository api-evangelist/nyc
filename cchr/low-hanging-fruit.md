# Low-Hanging Fruit Index — CCHR

**Agency:** NYC Commission on Human Rights (CCHR)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt — `nyc.gov/robots.txt` only disallows `/html/misc/`). Fingerprinted the site `nyc.gov/site/cchr` (Akamai + nginx + AWS ALB + NYC.gov "Livesite" platform + Dynatrace + Akamai mPulse) and inspected the **Report Discrimination** intake form (`/about/report-discrimination.page`), identified as a native server-rendered Livesite HTML form with no machine-readable contract. Verified the NYC Open Data agency label `Commission on Human Rights (CCHR)` via the Socrata Discovery API — only **3** assets, all pulled with column schemas.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-cchr.md](opendata-cchr.md).

## Headline findings

1. **CCHR is the thinnest domain yet.** NYC Open Data carries only **3** CCHR datasets — Inquiries Received, Office of Mediation cases, Pre-Complaint Resolutions — and all three are **aggregate operational counts**. There is no case data, no law-as-data, no guidance catalog, no outreach calendar.
2. **The core transaction is an untyped web form.** Reporting discrimination — the single most important thing a person does with CCHR — runs on the shared NYC.gov "Livesite" platform as a plain HTML `<form>` that posts to an opaque Law Enforcement Bureau backend. **No API, no OpenAPI, no JSON, no documented POST schema.**
3. **The law itself is not data.** Protected classes and legal enforcement guidance exist only as prose and PDF. "Is X protected in housing?" has no machine-readable answer.
4. **Complaints stay private by design.** Individual complaint/respondent/case data is never published; the intake form's typed structure is discarded and re-surfaces only as an annual tally whose columns match the form's category choices.

> **Reframe (fifth distinct pattern):** Parks = *replatform* a legacy site; DOE = *reclaim* rented search + a hidden backend; Council = *consolidate + own* three fragmented APIs; NYCHA = *unlock* a service layer trapped in a vendor CRM; **CCHR = structure.** Here almost nothing is machine-readable — the work is least about liberating datasets (there are barely any) and most about giving the **intake form and the Human Rights Law** typed, agent-native contracts.

## The fruit

| # | Name | Entity | Where it lives | Open Data twin |
|---|---|---|---|---|
| 1 | **Report Discrimination** | `DiscriminationComplaint` | Report Discrimination form + phone/LEB | ❌ **net-new** |
| 2 | Protected classes (the Law) | `ProtectedClass` | `/law/the-law`, legal library | ❌ gap (prose/PDF) |
| 3 | Legal enforcement guidance | `LegalGuidance` | `/law/legal-library`, `/media/publications` | ❌ gap (prose/PDF) |
| 4 | Trainings & workshops | `TrainingEvent` | `/community/events-workshops`, SHA training | ❌ gap (HTML) |
| 5 | Inquiries received | `InquiryStatistic` | Open Data | 🟡 Inquiries Received (`395v-hkhg`) — aggregate |
| 6 | Mediation / pre-complaint resolutions | `ResolutionStatistic` | Open Data | 🟡 Mediation (`tmha-56pf`) + Pre-Complaint (`6ayi-8khd`) — aggregate |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **Socrata SODA** — 3 CCHR datasets (the only open, machine-readable surface; aggregate counts only).
- **Report Discrimination HTML form** — the core transaction; native Livesite form, no API.
- Platform: the site sits on the **NYC.gov shared "Livesite" platform** (Akamai edge, nginx, AWS ALB, Dynatrace + mPulse RUM) — the same chassis as the NYCHA informational site; no CCHR-specific application platform and, notably, **no vendor CRM** (unlike NYCHA's Siebel).

## Reverse-engineered entities

`DiscriminationComplaint` (net-new write; from the intake form) · `ProtectedClass` (NYC Human Rights Law) · `LegalGuidance` · `TrainingEvent` (outreach; also stands in for bias-testing/education programs) · `InquiryStatistic` (aggregate) · `ResolutionStatistic` (aggregate; never individual case) — organizing vocabularies: the **protected classes** and **protected areas** (employment, housing, public accommodations, lending, discriminatory harassment, bias-based profiling) of Title 8 of the NYC Administrative Code.

## Next

1. **JSON Schema** per entity, reconciling the live intake-form fields and the three datasets' columns to the NYC Human Rights Law vocabulary — done ([schemas/](schemas/)).
2. **OpenAPI** typing the net-new `POST /complaints` (report discrimination) + publishing protected classes, guidance, outreach, and aggregate statistics as clean resources — done ([openapi/cchr.yaml](openapi/cchr.yaml)).
3. **MCP** artifact: `find_protected_classes`, `find_legal_guidance`, `find_training_events`, `find_inquiry_statistics`, `find_resolution_statistics`, `list_my_complaints`, `get_complaint`, `report_discrimination` — done ([mcp/cchr-mcp.json](mcp/cchr-mcp.json)).
