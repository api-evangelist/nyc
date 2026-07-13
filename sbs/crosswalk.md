# Crosswalk — Website/Portal Fruit ↔ APIs ↔ NYC Open Data (SBS)

Maps the low-hanging fruit on **nyc.gov/site/sbs** and the **MyCity Business portal** to (a) the **existing APIs** (Socrata SODA; the portal) and (b) the **28 SBS datasets** on NYC Open Data. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-sbs.json](opendata-sbs.json).

## The reframe — fifth distinct pattern

- **Parks:** data-rich HTML on a legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned → *consolidate + own.*
- **NYCHA:** reference data wide open, but every resident transaction locked in an Oracle Siebel CRM → *unlock the service layer.*
- **SBS:** program data reasonably open (28 Socrata datasets), but the agency's **guidance and eligibility engine — the Step-by-Step wizard, certification, and enrollment — locked inside a stateful Spring/AEM portal** with no API → **navigate.**

SBS is a *navigator* agency. Its whole reason to exist is routing: which licenses do I need to open, which incentives do I qualify for, how do I get certified, where do I hire. The directories behind that routing are open — certified businesses, BIDs, Workforce1 events, service centers, incentive rolls are all on Open Data. But the *routing itself* — the Step-by-Step wizard and the certification/enrollment transactions — lives only behind the login-walled, JavaScript-only MyCity Business portal. A business or agent asking "what do I need to do to become an M/WBE?" has no API to call.

Coverage: ✅ strong open twin · 🟡 partial/derived · ❌ gap (no API).

## Entity crosswalk

| Entity | Website / Portal | API today | Open Data | Cov. |
|---|---|---|---|---|
| `CertifiedBusiness` | `/businesses/mwbe` | SODA | SBS Certified Business List (`ci93-uc8s`, 56c); EO50 (`5vi6-xdpy`) | ✅ |
| `BusinessImprovementDistrict` | `/neighborhoods/bids` | SODA | Directory of BIDs (`qpm9-j523`); maps (`ejxk-d93y`, `7jdm-inj8`); Trends FY24 (`hzd8-k2vv`, 64c) | ✅ |
| `WorkforceEvent` | `/careers/hiring-events` | SODA | Workforce1 Recruitment Events (`kf2b-aeh5`) | ✅ |
| `JobListing` | `/careers` | SODA | Workforce1 Job Listing (`ay9k-vznm`, 22c) | ✅ |
| `ServiceLocation` | center finder | SODA | Center & Service Locations (`6smc-7mk6`, 19c) | ✅ |
| `BusinessIncentive` | `/businesses/business-incentives` | SODA | Energy Cost Savings (`bug8-9f3g`, 30c) + jobs (`yqky-aebb`); ICAP EO50 (`9a87-6m4x`); Acceleration (`9b9u-8989`) | ✅ |
| Step-by-Step licensing wizard | MyCity Business `/wizard` | **Portal UI only** | — | ❌ gap |
| Workforce1 enrollment | MyCity Business | **Portal UI only** | — | ❌ gap |
| **`MWBECertificationApplication`** (apply for M/WBE) | MyCity Business / PASSPort | **Portal UI only** | — (public *output* only) | ❌ **net-new** |

## The mismatch, concretely

| Source | Strength | Weakness |
|---|---|---|
| **Socrata SODA (28 datasets)** | Open, machine-readable; strong on certified vendors, BIDs, Workforce1 events/jobs, service centers, incentive rolls | Directory/outcome data only; static snapshots; nothing about the guidance or the live application flows |
| **MyCity Business portal** | The real system — Step-by-Step licensing, incentive eligibility, certification and enrollment | Session-walled, JavaScript-only Spring/AEM app; no API, no OpenAPI, no JSON; not agent-accessible |

## Implications for the API-first + MCP proposal

1. **Publish the open program data as one clean resource model.** Certified businesses, BIDs, Workforce1 events and jobs, service centers, and incentives behind one owned SBS contract ([OpenAPI](openapi/sbs.yaml)) — so consumers learn one model, not 28 Socrata IDs.
2. **Navigate the service layer.** Front MyCity Business with an API so the core business transaction — applying for and tracking **M/WBE certification** — has a machine-readable, agent-native contract.
3. **Add the one net-new write workflow** — `apply_for_mwbe_certification` (submit an M/WBE / EBE / LBE application); approved applicants then surface in the public certified business list.
4. **Fold the parallel programs.** Model the three incentive programs (Energy Cost Savings, ICAP, Acceleration) as one `BusinessIncentive` keyed by `program`, and the six BID assets as one `BusinessImprovementDistrict`.
5. **MCP server** so an agent can answer "which M/WBE electricians are certified in the Bronx?", "what BIDs are in my neighborhood?", and — the point — "help me apply for women-owned business certification and tell me the status."
