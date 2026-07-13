# Crosswalk — Website/Service Fruit ↔ APIs ↔ NYC Open Data (OCME)

Maps the low-hanging fruit on **nyc.gov/site/ocme** and the paper/311 service channel to (a) the **existing APIs** (Socrata SODA; NYC 311; federal NamUs) and (b) the **one** OCME dataset on NYC Open Data. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-ocme.json](opendata-ocme.json).

## The reframe — fifth distinct pattern

- **Parks:** data-rich HTML on a legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned → *consolidate + own.*
- **NYCHA:** reference data wide open, but every resident transaction locked inside an Oracle Siebel CRM → *unlock the service layer.*
- **OCME:** **almost nothing is published, there is no application at all, and the core object is confidential by law** → **instrument** it — the least-instrumented, most privacy-constrained domain assessed.

OCME inverts NYCHA. NYCHA had a wealth of open reference data and a locked transaction system. OCME has **neither**: one stale MMR dataset, zero owned applications, and a core object — a death investigation — that can never be published per-decedent. The modernization work here is not liberation and not unlocking; it is *first instrumentation*, done carefully: publish the small set of things that can responsibly be public, and give families **one dignified digital write path** in place of a notarized form and a six-month wait.

Coverage: ✅ open twin · 🟡 partial/aggregate/federated · ❌ gap (no API, no data).

## Entity crosswalk

| Entity | Website / Service | API today | Open Data | Cov. |
|---|---|---|---|---|
| `MonthlyIndicator` | (MMR reporting) | SODA | Monthly Indicators (`8r6c-ydwk`, 16c) — stale 2015-16 | 🟡 stale |
| `CaseStatistics` (aggregate DeathInvestigation) | `/services/reporting-a-case` | — | **none** | ❌ no data (aggregate would be net-new) |
| `ForensicService` | `/services/services` | — | none (HTML only) | ❌ gap |
| `FamilyServicesCenter` | `/locations/family-services-centers` | — | none (HTML + phone only) | ❌ gap |
| `MissingPerson` | `/for-families/namus` | **NamUs (federal)** | none (OCME) | 🟡 federated |
| **`DeathRecordRequest`** (request a casefile record) | `/records-requests` + paper + 311 | **311 / paper only** | — | ❌ **net-new** |

## The absence, concretely

| Source | Strength | Weakness |
|---|---|---|
| **Socrata SODA (1 dataset)** | Open, machine-readable | A single stale MMR performance-indicator pivot (real months July 2015 - May 2016); not casework; not maintained |
| **NYC 311 + paper forms** | The real records-request channel | Not an OCME system; no API surfaced for OCME; notarization required for third-party delivery; three-to-six-month turnaround |
| **Federal NamUs** | Public, structured missing-persons/unidentified data | Owned by US DOJ, not OCME; OCME participates but exposes nothing itself |
| **Death investigation (core object)** | — | Confidential by law; correctly never published, even in aggregate |

## Implications for the API-first + MCP proposal

1. **Publish only what can responsibly be public — as one clean model.** Performance indicators, AGGREGATE case statistics (counts by manner of death, never individuals), the forensic-service catalog, family services centers, and NamUs listings behind one owned OCME contract ([OpenAPI](openapi/ocme.yaml)).
2. **Instrument the core object at a respectful altitude.** `CaseStatistics` proposes the *first* machine-readable OCME casework surface — aggregate only, small cells suppressed. There is no Open Data twin today; this is net-new and must stay non-identifying.
3. **Add the one net-new write workflow — dignified.** `request_record` (create a `DeathRecordRequest`) replaces the notarized-paper-and-311 process for a family requesting a decedent's casefile record, with eligibility, notarization, and a realistic turnaround expectation encoded in the contract.
4. **Privacy is the design.** The API never exposes an individual death investigation, cause of death against a person, or the contents of a casefile record. The [MCP artifact](mcp/ocme-mcp.json)'s instructions make that an explicit agent constraint and set a bereavement-appropriate tone.
5. **MCP server** so an agent can answer "where is the Bronx family services center?", "how many accident deaths were investigated in Queens last year?" (aggregate), and — the point — "help me request my father's autopsy report and tell me its status."
