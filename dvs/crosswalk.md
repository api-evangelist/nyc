# Crosswalk — Website/Portal Fruit ↔ APIs ↔ NYC Open Data (DVS)

Maps the low-hanging fruit on **nyc.gov/site/veterans** and the **VetConnectNYC** intake to (a) the **existing APIs** (Socrata SODA; the Combined Arms portal) and (b) the **7 DVS datasets** on NYC Open Data. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-dvs.json](opendata-dvs.json).

## The reframe — a connective agency with a vendor service layer

- **Parks:** data-rich HTML on a legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned → *consolidate + own.*
- **NYCHA:** reference data wide open, every transaction locked in an Oracle Siebel CRM → *unlock the service layer.*
- **DFTA:** provider network open, service layer is a phone contact center (Aging Connect) → *connect.*
- **DVS:** reference data **and de-identified service data** are open, but the live care-coordination **referral runs on a third-party vendor portal** (Combined Arms / VetConnectNYC) with no API → **coordinate — own the referral.**

DVS is the most open small agency in this project so far: it publishes not just a resource directory but its own de-identified service analytics — assistance requests, cases, and client demographics. What it does **not** publish, and what has no machine-readable surface, is the live intake: a **VetConnectNYC** referral. A veteran fills out the VetConnectNYC Request Form on `nyc.veteranportal.combinedarms.us`, and DVS Care Coordinators work it by hand within 3–5 business days. A veteran or agent asking "connect me to housing help in the Bronx and tell me the status" has no API to call.

Coverage: ✅ strong open twin · 🟡 partial/aggregate · ❌ gap (no API).

## Entity crosswalk

| Entity | Website / Portal | API today | Open Data | Cov. |
|---|---|---|---|---|
| `VeteranResource` | `/services` resource lists | SODA | DVS Resource Map (`af2s-4k4p`, 15c) | ✅ |
| `VeteranOwnedBusiness` | — | SODA | NYC Veteran Owned Businesses (`ybdk-jmnn`, 27c) | ✅ |
| `AssistanceRequest` | VetConnectNYC (after the fact) | SODA | DVS Assistance Requests (`jup5-7fik`, 22c); Historical Client Requests (`44f4-mjxy`); VPC Moves (`davn-rbxj`) | 🟡 de-identified |
| `Case` | — | SODA | DVS Cases (`pw4e-vms3`, 9c) | 🟡 de-identified |
| `ClientStatistics` | — | SODA | DVS Clients (`idat-aemv`, 12c) — aggregate only | 🟡 aggregate |
| **`ServiceReferral`** (VetConnectNYC) | VetConnectNYC Request Form | **Combined Arms portal only** | — (de-identified twin: `jup5-7fik`) | ❌ **net-new** |

## The mismatch, concretely

| Source | Strength | Weakness |
|---|---|---|
| **Socrata SODA (7 datasets)** | Open, machine-readable; unusually deep — reference directories *and* de-identified service analytics (assistance requests, cases, client demographics) | Everything is downstream/de-identified snapshots; nothing about a live, individual referral you can act on |
| **VetConnectNYC (Combined Arms)** | The real intake system — connects a veteran to housing, benefits, VA claims, health, employment, food, legal | Third-party out-of-city vendor web form; no API, no OpenAPI, no JSON; registration-gated; a manual 3–5 business-day DVS Care Coordinator queue; not agent-accessible |

## Implications for the API-first + MCP proposal

1. **Publish the open reference and service data as one clean resource model.** Resource Map, veteran-owned businesses, assistance requests, cases, and aggregate client statistics behind one owned DVS contract ([OpenAPI](openapi/dvs.yaml)) — so consumers learn one model, not 7 Socrata IDs.
2. **Coordinate the referral.** Front VetConnectNYC with an owned API so the core veteran transaction — making and tracking a **ServiceReferral** — has a machine-readable, agent-native contract instead of an out-of-city vendor form.
3. **Add the one net-new write workflow** — `make_referral` (create a VetConnectNYC referral), with an urgent flag that escalates imminent-homelessness / no-food / crisis to a DVS Veteran Resource Center rather than the standard 3–5 day queue.
4. **Keep veterans private.** Client data stays de-identified/aggregate-only; the API never exposes an identifiable veteran record.
5. **MCP server** so an agent can answer "which veteran-serving resources take walk-ins in Brooklyn?", "how many assistance requests came through VetConnectNYC last fiscal year?", and — the point — "connect this veteran to housing help and tell me the status."
