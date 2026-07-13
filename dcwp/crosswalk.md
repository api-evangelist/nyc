# Crosswalk — Website/Portal Fruit ↔ APIs ↔ NYC Open Data (DCWP)

Maps the low-hanging fruit on **nyc.gov/site/dca**, the **NYC Business portal**, and **311** to (a) the **existing APIs** (Socrata SODA; the portals) and (b) the **37 DCWP datasets** on NYC Open Data. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-dcwp.json](opendata-dcwp.json).

## The reframe — fifth distinct pattern

- **Parks:** data-rich HTML on a legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned → *consolidate + own.*
- **NYCHA:** reference data wide open, every transaction locked in a vendor CRM → *unlock the service layer.*
- **DCWP:** the **entire regulatory lifecycle is already open** (37 Socrata datasets), but it is **spread across 37 IDs with no owned contract**, and the two citizen writes (apply, complain) live in a Java portal / 311 → **bind the open lifecycle and add the writes.**

DCWP is the most-open domain yet. Apply → issue → inspect → charge → complain → revoke is all machine-readable, all joinable on `Business Unique ID` and `License Number`. The problem is not trapped data — it is that no owned API binds those 37 datasets into one model, and the two things a person *does* (apply for a license, file a complaint) have no write API at all.

Coverage: ✅ strong open twin · 🟡 partial/aggregate · ❌ gap (no API).

## Entity crosswalk

| Entity | Website / Portal | API today | Open Data | Cov. |
|---|---|---|---|---|
| `BusinessLicense` | `/businesses/licenses` | SODA | Issued Licenses (`w7w3-xahh`, 31c); Historical Licenses (`m4ph-grrm`); Revocations (`rpeq-j89e`); Licensed Vehicles (`9vpn-rpgs`) | ✅ |
| `LicenseApplication` (read) | NYC Business portal | SODA | License Applications (`ptev-4hud`, 35c); Historical (`vnz6-h2k4`) | ✅ |
| `Inspection` | — | SODA | DCWP Inspections (`jzhd-m6uv`, 28c); Archived (`kwss-yksz`); Weights & Measures (`8fei-z6rz`) | ✅ |
| `Charge` (violation) | — | SODA | DCWP Charges (`5fn4-dr26`, 18c); Archived (`wyj6-frpa`); Fines & Fees (`2k3g-r445`) | ✅ |
| `ConsumerComplaint` (read) | 311 / web form | SODA | DCWP Consumer Complaints (`nre2-6m2s`, 33c) | ✅ |
| `WorkerProtectionCase` | `/workers/workersrights` | SODA | OLPS Enforcement Matters (`c292-vzrn`); Workplace Inquiries (`2z24-2htf`) — **aggregate only** | 🟡 aggregate |
| **Apply for a license** | NYC Business portal | **Java portal only** | — (read twin exists) | ❌ **net-new write** |
| **File a consumer complaint** | 311 / web form | **311 UI only** | — (read twin exists) | ❌ **net-new write** |
| Pay a fine / fee | CityPay | **CityBase UI only** | Payments Received (`2xab-argn`) | ❌ gap |

## The mismatch, concretely

| Source | Strength | Weakness |
|---|---|---|
| **Socrata SODA (37 datasets)** | Open, machine-readable; the whole lifecycle — applications, licenses, inspections, charges, complaints, revocations, worker-protection matters | Spread across 37 IDs with no owned contract; static snapshots; nothing to *submit* against |
| **NYC Business portal / 311 / CityPay** | The real transaction systems — apply, complain, pay | Session-gated Java portal / 311 form / CityBase checkout; no API, no OpenAPI, no JSON; not agent-accessible |

## Implications for the API-first + MCP proposal

1. **Bind the open lifecycle into one clean resource model.** Licenses, applications, inspections, charges, complaints, and worker-protection matters behind one owned DCWP contract ([OpenAPI](openapi/dcwp.yaml)) keyed on `Business Unique ID` — so consumers learn one model, not 37 Socrata IDs.
2. **Add the two net-new writes.** `apply_for_license` (create a `LicenseApplication`, replacing the Java portal) and `file_complaint` (create a `ConsumerComplaint`, replacing the 311 form) — the two citizen transactions with no API today.
3. **Keep workers private.** OLPS worker-protection data stays aggregate-only; the API never exposes an individual worker.
4. **MCP server** so an agent can answer "is this contractor licensed and in good standing?", "what has DCWP charged this business with?", and — the point — "file a complaint that this shop overcharged me" or "apply for my home-improvement contractor license."
