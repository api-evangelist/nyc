# Crosswalk — Website/Intake Fruit ↔ APIs ↔ NYC Open Data (CCHR)

Maps the low-hanging fruit on **nyc.gov/site/cchr** and the **Report Discrimination** intake to (a) the **existing APIs** (Socrata SODA; the untyped intake form) and (b) the **3 CCHR datasets** on NYC Open Data. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-cchr.json](opendata-cchr.json).

## The reframe — fifth distinct pattern

- **Parks:** data-rich HTML on a legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned → *consolidate + own.*
- **NYCHA:** reference data wide open, every resident transaction locked in a vendor CRM → *unlock the service layer.*
- **CCHR:** **almost nothing is machine-readable** — the law is prose, the guidance is PDF, the intake is an untyped web form, Open Data is three aggregate tallies → **structure the intake and the law into typed contracts.**

CCHR is the thinnest domain yet. NYCHA at least published its physical stock generously; CCHR publishes only three small operational-metrics tables. And where NYCHA's transactions were trapped in a vendor CRM, CCHR's core transaction — **reporting discrimination** — runs on the city's own platform as a plain HTML form. The problem isn't lock-in; it's that nothing has a **type**. A person (or agent) asking "am I protected against this?" or "help me file a report" has no contract to call, and the data they enter is only ever seen again as an annual count.

Coverage: ✅ strong open twin · 🟡 partial/aggregate · ❌ gap (no API).

## Entity crosswalk

| Entity | Website / Intake | API today | Open Data | Cov. |
|---|---|---|---|---|
| **`DiscriminationComplaint`** (report discrimination) | Report Discrimination form + phone/LEB | **HTML form only** | — (aggregated away into inquiry counts) | ❌ **net-new** |
| `ProtectedClass` (the Human Rights Law) | `/law/the-law`, legal library | — | — | ❌ gap (prose/PDF only) |
| `LegalGuidance` (enforcement guidance) | `/law/legal-library`, `/media/publications` | — | — | ❌ gap (prose/PDF only) |
| `TrainingEvent` (workshops, SHA training) | `/community/events-workshops`, `/law/sexual-harassment-training` | — | — | ❌ gap (HTML only) |
| `InquiryStatistic` | (published metric) | SODA | Inquiries Received (`395v-hkhg`, 9c) | 🟡 aggregate |
| `ResolutionStatistic` | (published metric) | SODA | Mediation Cases (`tmha-56pf`); Pre-Complaint Resolutions (`6ayi-8khd`) | 🟡 aggregate |
| Individual complaint / case data | — | LEB backend (opaque) | — (never published, by design) | ❌ private by design |

## The mismatch, concretely

| Source | Strength | Weakness |
|---|---|---|
| **Socrata SODA (3 datasets)** | Open, machine-readable | Only three aggregate operational tallies; nothing about the law, guidance, outreach, or any individual matter |
| **Report Discrimination form** | The real intake — captures category, respondent, incident, description | Untyped HTML form; no API, no OpenAPI, no JSON; data is discarded as structure the moment it's submitted and re-surfaces only as an annual count |
| **The Human Rights Law + guidance** | The Commission's core reference value | Published only as prose and PDF; not queryable; "is X protected in housing?" has no machine answer |

## Implications for the API-first + MCP proposal

1. **Type the intake.** Turn the Report Discrimination form into a typed `POST /complaints` ([OpenAPI](openapi/cchr.yaml)) that captures protected class(es), protected area, respondent, incident, and description as structured data — the net-new **write** surface, `report_discrimination`. Preserve the form's affordances: anonymous reports allowed, and a report may be filed whether or not the person wants a formal complaint.
2. **Publish the law as data.** Expose `ProtectedClass` and `LegalGuidance` as resources so an agent can answer "am I protected against this?" and cite the guidance — instead of a person reading PDFs.
3. **Publish outreach.** `TrainingEvent` makes workshops and the Stop Sexual Harassment Act training discoverable.
4. **Keep complaints private.** Individual complaint/case data stays private by design; the API never exposes another person's report. Aggregate statistics (`InquiryStatistic`, `ResolutionStatistic`) stay aggregate.
5. **MCP server** so a person can, in one place, ask "is my landlord allowed to reject my voucher?", "what does the law say about gender identity at work?", and — the point — "help me report this discrimination and tell me what happens next."
