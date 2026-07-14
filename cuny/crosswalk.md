# Crosswalk — Website/Portal Fruit ↔ APIs ↔ NYC Open Data (CUNY)

Maps the low-hanging fruit on **cuny.edu** and **CUNYfirst** to (a) the **existing APIs** (there are none public; PeopleSoft; wp-json) and (b) the **NYC Open Data corpus** (which, for CUNY, is essentially empty). Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-cuny.json](opendata-cuny.json).

## The reframe — fifth distinct pattern

- **Parks:** data-rich HTML on a legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned → *consolidate + own.*
- **NYCHA:** reference data wide open, every transaction locked in a vendor CRM → *unlock the service layer.*
- **CUNY:** a **federated system** — ~25 campuses on one WordPress Multisite and one shared PeopleSoft ERP, publishing **nothing** to NYC Open Data → **federate** the campuses behind one owned contract and unlock the application.

CUNY inverts NYCHA. NYCHA's reference data was wide open and only the transactions were locked. CUNY has **neither**: no open-data twin for any entity (it is a state public benefit corporation, not a city publisher), and every transaction is hidden in CUNYfirst. The reference data exists — it is just scattered across 25 college websites, a client-rendered program finder, and PDF/Excel data books, with no single machine-readable model. A student or agent asking "which CUNY colleges offer a BS in Nursing, and how do I apply?" has nothing to call.

Coverage: ✅ strong open twin · 🟡 partial/aggregate/non-NYC · ❌ gap (no API, no open data).

## Entity crosswalk

| Entity | Website / Portal | API today | Open Data | Cov. |
|---|---|---|---|---|
| `Campus` | `/about/colleges-schools` | — (HTML) | none (CUNY not a NYC OD publisher) | ❌ gap |
| `DegreeProgram` | `/academics/programs` (Explore Programs) | — (client-rendered) | none | ❌ gap |
| `Course` | CUNYfirst catalog browse | **PeopleSoft UI only** | none | ❌ gap |
| `EnrollmentStatistics` | OIRA data books | — (PDF/Excel) | 🟡 state tables on `data.ny.gov`; **aggregate only** | 🟡 non-NYC / aggregate |
| `FacultyResearch` | college directories + Academic Works | **OAI-PMH only** | none | 🟡 OAI-PMH |
| Community-college budget | — | SODA | 🟡 `wusu-mzmq` (tagged **OMB**, not CUNY) | 🟡 wrong agency |
| Apply to CUNY | CUNYfirst | **PeopleSoft UI only** | none | ❌ gap |
| Check application status | CUNYfirst | **PeopleSoft UI only** | none | ❌ gap |
| Register for classes | CUNYfirst | **PeopleSoft UI only** | none | ❌ gap |
| **`AdmissionsApplication`** (submit) | CUNYfirst | **PeopleSoft UI only** | none | ❌ **net-new** |

## The mismatch, concretely

| Source | Strength | Weakness |
|---|---|---|
| **NYC Open Data** | Open, machine-readable | **Empty for CUNY** — the agency label returns one external link; CUNY is a state entity, not a city publisher |
| **cuny.edu (WordPress Multisite)** | Rich reference content across ~25 college sites | Federated and inconsistent; `wp-json` is content-only; program finder is client-rendered; enrollment is PDF/Excel |
| **CUNYfirst (PeopleSoft)** | The real transaction system — apply, catalog, enroll, aid | Guest/login PeopleSoft screens; no API, no OpenAPI, no JSON; not agent-accessible |

## Implications for the API-first + MCP proposal

1. **Federate the reference data into one clean resource model.** Campuses, degree programs, courses, aggregate enrollment, and faculty/research behind one owned CUNY contract ([OpenAPI](openapi/cuny.yaml)) — so consumers learn one model, not 25 college sites and a PeopleSoft catalog.
2. **Unlock the transaction layer.** Front CUNYfirst with an API so the core prospective-student transaction — submitting and tracking a **CUNY admissions application** (one application, multiple campuses) — has a machine-readable, agent-native contract.
3. **Add the one net-new write workflow** — `submit_application` (create a CUNY admissions application), with a fee-waiver flag.
4. **Keep students private.** Enrollment stays aggregate-only; the API never exposes an individual `StudentRecord` (FERPA).
5. **MCP server** so an agent can answer "which CUNY colleges offer a BS in Nursing?", "what's the Fall enrollment at Hunter?", and — the point — "start my CUNY application to these three campuses and tell me the status."
