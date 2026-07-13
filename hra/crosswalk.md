# Crosswalk — Website/Portal Fruit ↔ APIs ↔ NYC Open Data (HRA / DSS)

Maps the low-hanging fruit on **nyc.gov/site/hra**, the **ACCESS NYC** screener, and the **ACCESS HRA** portal to (a) the **existing APIs** (Socrata SODA; the open-source ACCESS NYC rules; the Siebel-less React portal) and (b) the **49 HRA datasets** on NYC Open Data. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-hra.json](opendata-hra.json).

## The reframe — fifth distinct pattern

- **Parks:** data-rich HTML on a legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned → *consolidate + own.*
- **NYCHA:** reference data wide open, every resident transaction locked in a vendor CRM → *unlock the service layer.*
- **HRA:** the caseload data is open **and** the eligibility engine is open-sourced (a public Drools rules engine), but nothing binds the screener, the rules, and the closed application step into one callable API → **connect the benefits journey.**

HRA is the first domain where the hard, agency-specific *logic* — who qualifies for which benefit — is already public and city-owned. Yet the ACCESS NYC screener returns HTML, and the thing a resident actually *does* — apply for SNAP/Cash Assistance/Medicaid and track the case — lives only behind the login-walled, JavaScript-only ACCESS HRA React portal. A resident or agent asking "what do I qualify for, where do I apply, and what's my case status?" has to cross three disconnected surfaces and has no API to call for the last one.

Coverage: ✅ strong open twin · 🟡 partial/aggregate · ❌ gap (no API).

## Entity crosswalk

| Entity | Website / Portal | API today | Open Data | Cov. |
|---|---|---|---|---|
| `Program` | ACCESS NYC catalog | SODA | HRA Facts, Programs & Services (`np6w-pies`); NYC Benefits Platform (`kvhd-5fmu`) | ✅ |
| `Center` | `/site/hra/locations` | SODA | Benefits Access Centers (`9d9t-bmk7`), SNAP Centers (`tc6u-8rnp`), Medicaid Offices (`ibs4-k445`), Homebase (`ntcm-2w4k`), wait times (`fq4m-vjs9`, `gqk4-hny9`) | ✅ |
| `CaseloadStatistic` | dashboards | SODA | SNAP (`5c4s-jwtq`), Cash Assistance (`qtrj-g3nm`), Medicaid (`33db-aeds`), Borough/CD (`5awp-wfkt`), DRS (`au2c-rs69`), Fair Fares (`3tw8-6si8`) | 🟡 aggregate |
| `CaseAction` | — | SODA | Rejections (`g6pg-qint`), Closed (`5fs5-yi3e`), Reopenings (`5uf6-jjmy`, `28gm-7ump`) — all ~75c | 🟡 aggregate |
| `BenefitsEligibility` | ACCESS NYC screener | **Drools rules (open source), no hosted API** | — (rules in `NYCOpportunity/ACCESS-NYC-Rules`) | ❌ no result API |
| **`BenefitsApplication`** (apply / case status) | ACCESS HRA portal + centers | **React SPA / in-person only** | — (aggregate case actions are the only twin) | ❌ **net-new** |

## The mismatch, concretely

| Source | Strength | Weakness |
|---|---|---|
| **Socrata SODA (49 datasets)** | Open, machine-readable; strong on caseloads, program/center directories, and case-action reporting | Reference/aggregate data only; static snapshots; nothing about a live individual application |
| **ACCESS NYC rules (Drools, open source)** | The eligibility logic is public and city-owned — the hardest, most agency-specific part | No hosted endpoint; the screener returns HTML, not a machine-readable determination |
| **ACCESS HRA portal (React SPA)** | The real transaction system — apply, upload documents, track case status | Login-walled, JavaScript-only, Akamai-gated; no API, no OpenAPI, no JSON; not agent-accessible; an in-person visit is the fallback |

## Implications for the API-first + MCP proposal

1. **Publish the open reference data as one clean resource model.** Programs, centers, caseloads, and case actions behind one owned HRA contract ([OpenAPI](openapi/hra.yaml)) — so consumers learn one model, not 49 Socrata IDs.
2. **Expose the open rules as an endpoint.** Wrap the ACCESS NYC Drools rules as `POST /eligibility` so a household profile returns machine-readable determinations — the logic is already public; only the API is missing.
3. **Unlock the service layer.** Front the ACCESS HRA portal with an API so the core resident transaction — submitting and tracking a **benefits application** — has a machine-readable, agent-native contract.
4. **Add the one net-new write workflow** — `apply_for_benefits` (submit a SNAP/Cash Assistance/Medicaid application), with an emergency flag that routes immediate needs (no food, eviction, no heat) to expedited handling.
5. **Keep cases private.** Caseloads and case actions stay aggregate-only; the API never exposes an individual case except to the authenticated resident who owns it.
6. **MCP server** so an agent can answer "what benefits do I qualify for?", "where is my nearest SNAP center and what's the wait?", and — the point — "apply for SNAP for me and tell me the status."
