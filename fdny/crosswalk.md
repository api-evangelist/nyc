# Crosswalk — Website/Portal Fruit ↔ APIs ↔ NYC Open Data (FDNY)

Maps the low-hanging fruit on **nyc.gov/site/fdny** and the **FDNY Business** portal to (a) the **existing APIs** (Socrata SODA; the Accela portal) and (b) the **17 FDNY datasets** on NYC Open Data. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-fdny.json](opendata-fdny.json).

## The reframe — fifth distinct pattern

- **Parks:** data-rich HTML on a legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned → *consolidate + own.*
- **NYCHA:** reference data wide open, resident transactions locked in an in-house vendor CRM (Siebel) → *unlock the service layer.*
- **FDNY:** the **reference and incident data is already wide open** (17 Socrata datasets), but every **business transaction is rented out to a commercial SaaS** (Accela Civic Platform) with no API → **front the rented portal with an owned API.**

FDNY inverts the usual problem in the same direction NYCHA did, but the lock is different in kind. It is not that the data is trapped in HTML — firehouses, Fire/EMS dispatch, inspections, violations, and certificates are all machine-readable on Open Data. It is that the things a business *does* — apply for a permit, hold a Certificate of Fitness, schedule an inspection, answer a violation — live only behind the login-walled, JavaScript-only **FDNY Business** portal, which is a **rented Accela** application, not an in-house system. And the open data is a **historical snapshot**: it shows outcomes, never live status. A business or agent asking "what's the status of my permit?" has no API to call.

Coverage: ✅ strong open twin · 🟡 partial/historical-snapshot · ❌ gap (no API).

## Entity crosswalk

| Entity | Website / Portal | API today | Open Data | Cov. |
|---|---|---|---|---|
| `Firehouse` | `/about/.../find-a-firehouse` | SODA | FDNY Firehouse Listing (`hc8x-tcnd`, 12c) | ✅ |
| `IncidentDispatch` | — | SODA | Fire Dispatch (`8m42-w767`, 29c); EMS Dispatch (`76xm-jjuj`, 31c); Fire Companies (`tm6d-hbzd`); Fire Causes (`ii3r-svjz`) | ✅ |
| `Inspection` | FDNY Business | SODA (read) | BFP Inspections (`ssq6-fkht`); RBIS (`itd7-gx3g`); Mandatory (`kfgh-h6re`) | 🟡 historical |
| `Violation` | FDNY Business | SODA (read) | Active Violation Orders (`bi53-yph3`); Vacate List (`n5xc-7jfa`); Building Summary (`nvgj-hbht`) | 🟡 historical |
| `CertificateOfFitness` | FDNY Business | SODA (read) | Certificates of Fitness (`pdiy-9ae5`, 18c) | 🟡 historical |
| Apply for a fire permit | FDNY Business | **Accela UI only** | — | ❌ gap |
| Hold / renew a Certificate of Fitness | FDNY Business | **Accela UI only** | — | ❌ gap |
| Schedule an inspection | FDNY Business | **Accela UI only** | — | ❌ gap |
| **`FirePermitApplication`** (submit + track) | FDNY Business + paper | **Accela UI / paper only** | — | ❌ **net-new** |

## The mismatch, concretely

| Source | Strength | Weakness |
|---|---|---|
| **Socrata SODA (17 datasets)** | Open, machine-readable; strong on firehouses, minute-level Fire/EMS dispatch, inspections, violations, certificates | Reference/operational data only; **historical snapshots** of the regulatory records; nothing about live business transactions |
| **FDNY Business (Accela)** | The real transaction system — permits, certificates, inspections, violations, fees | Login-walled, JavaScript-only, **rented commercial SaaS**; no API, no OpenAPI, no JSON; not agent-accessible; paper is the fallback |

## Implications for the API-first + MCP proposal

1. **Publish the open reference/operational data as one clean resource model.** Firehouses, incidents, inspections, violations, and certificates behind one owned FDNY contract ([OpenAPI](openapi/fdny.yaml)) — so consumers learn one model, not 17 Socrata IDs.
2. **Front the rented portal.** Put an owned API in front of the Accela FDNY Business system so the core business transaction — submitting and tracking a **fire permit application** — has a machine-readable, agent-native contract.
3. **Add the one net-new write workflow** — `apply_for_permit` (submit a fire permit / Certificate of Operation / inspection request), with permit types spanning general fire permits, Place of Assembly, hot-work, fireworks, and storage.
4. **Close the historical gap.** The read resources should serve *live* inspection/violation/certificate status, not just the historical snapshots Open Data publishes.
5. **MCP server** so an agent can answer "which firehouse covers this address?", "what violations are open on this building?", and — the point — "apply for a Place of Assembly certificate and tell me the status."
