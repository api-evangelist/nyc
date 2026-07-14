# Crosswalk — Website Fruit ↔ APIs ↔ NYC Open Data (MOCJ)

Maps the low-hanging fruit on **criminaljustice.cityofnewyork.us** (and the nyc.gov stub) to (a) the **existing APIs** (the accidental WordPress REST API; SODA; Contact Form 7) and (b) the **single MOCJ dataset** on NYC Open Data. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-mocj.json](opendata-mocj.json).

## The reframe — fifth distinct pattern

- **Parks:** data-rich HTML on a legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned → *consolidate + own.*
- **NYCHA:** reference data wide open, service layer locked in a vendor CRM → *unlock.*
- **MOCJ:** a **coordination office that owns almost no data** — one stale dataset, an *accidental* WordPress API, and jail numbers that belong to other agencies → **route** its programs, publications, and referrals through one owned contract.

MOCJ inverts the NYCHA finding again. NYCHA's data was open but its transactions were locked; MOCJ has neither much open data *nor* a real service API. What it has is a WordPress site whose default REST API happens to expose everything as JSON, and a convening role — analyzing other agencies' numbers and routing people to community programs — that has no machine-readable surface at all.

Coverage: ✅ strong open twin · 🟢 accidental JSON (WordPress REST) · 🟡 partial/aggregate · ❌ gap (no API).

## Entity crosswalk

| Entity | Website | API today | Open Data | Cov. |
|---|---|---|---|---|
| `Program` | `/programs/` | Accidental `wp/v2/programs` (26) | — | 🟢 accidental JSON |
| `SupervisedReleaseDocket` | `/programs/supervised-release/` | SODA | Supervised Release Dockets (`atne-2dki`, 6c) | ✅ (stale 2023) |
| `JailPopulationMetric` | `/system-data/` | **External links only** (DOC/NYPD/DCJS/BOC) | — (not MOCJ's) | 🟡 aggregate, not owned |
| `DataReport` (reports/briefs/data reports/stories) | `/publications/` | Accidental `wp/v2` (26+54+109+6) | — | 🟢 accidental JSON (PDF content) |
| `Solicitation` (procurement) | `/notices-solicitations/` | Accidental `wp/v2/solicitation` (25) + `notice` (26) | — | 🟢 accidental JSON |
| Vendor enrollment / contact | `/vendor-enrollment/` | **Contact Form 7 only** | — | ❌ gap (form-to-email) |
| **`ProgramReferral`** (route to a program) | `/programs/` | **offline / web form only** | — | ❌ **net-new** |

## The mismatch, concretely

| Source | Strength | Weakness |
|---|---|---|
| **WordPress `wp/v2` REST (accidental)** | Already returns programs, publications, solicitations as JSON; free, live | Undocumented, unintended, no auth model, no data guarantees; a plugin default, not a product |
| **Socrata SODA** | Open, machine-readable | Exactly one MOCJ dataset, 6 columns, unchanged since 2023 |
| **DOC/NYPD/DCJS/BOC dashboards** | The real jail/crime numbers | Owned by other agencies; MOCJ only links and narrates |
| **Contact Form 7** | The one write path | Generic form-to-email; not a referral or procurement API |

## Implications for the API-first + MCP proposal

1. **Promote the accidental API to an intentional one.** Programs, publications, and solicitations already come back as JSON — an owned [OpenAPI](openapi/mocj.yaml) turns that into a documented, stable resource model instead of a WordPress default nobody supports.
2. **Aggregate and cite the metrics MOCJ analyzes.** A `JailPopulationMetric` resource can carry the jail-population / re-arrest numbers *with* their `sourceAgency`, so an agent gets the figure and its provenance instead of a PDF and a hyperlink.
3. **Add the one net-new write workflow** — `refer_to_program` (create a `ProgramReferral`), routing a person or case to a coordinated program along the Sequential Intercept Model, with an `urgent` flag and an explicit `consentGiven` requirement.
4. **Treat referral data as sensitive.** Justice-involved individuals: the referral surface is authenticated, consent-gated, and minimized — never an open dataset.
5. **MCP server** so an agent can answer "which reentry programs serve the Bronx at Intercept 5?", "what did MOCJ's jail-population explainer conclude?", and — the point — "refer this client to a supervised-release program and tell me the status."
