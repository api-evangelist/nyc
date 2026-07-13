# Crosswalk — Website/Intake Fruit ↔ APIs ↔ NYC Open Data (NYC Aging / DFTA)

Maps the low-hanging fruit on **nyc.gov/site/dfta** and the **Aging Connect** intake to (a) the **existing APIs** (Socrata SODA; the phone-based Aging Connect) and (b) the **11 DFTA datasets** on NYC Open Data. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-dfta.json](opendata-dfta.json).

## The reframe — fifth distinct pattern

- **Parks:** data-rich HTML on a legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned → *consolidate + own.*
- **NYCHA:** reference data open, every resident transaction locked inside an Oracle Siebel CRM → *unlock the service layer.*
- **DFTA:** the **provider-network reference data is already wide open** (11 Socrata datasets), but every **resident transaction is a phone call to Aging Connect** — there is no system to unlock, only a referral process to give an API → **connect the older adult to services.**

DFTA is a further twist on NYCHA. NYCHA at least had a vendor application (Siebel) behind its transactions; DFTA's transaction layer is a **contact center**. A caseworker takes the call and routes the older adult into the very provider network that is fully published on Open Data. A resident or agent asking "connect my mother to home-delivered meals in the Bronx" has no API to call — only 212-AGING-NYC.

Coverage: ✅ strong open twin · 🟡 partial/aggregate · ❌ gap (no API).

## Entity crosswalk

| Entity | Website / Intake | API today | Open Data | Cov. |
|---|---|---|---|---|
| `ServiceProvider` | find-help / center finder | SODA | All Contracted Providers (`cqc8-am9x`, 38c); Public Sites (`u7wp-np5k`); Social Adult Day Care (`32cj-z7va`) | ✅ |
| `OlderAdultCenter` | center finder | SODA | Senior Center LL140 Provider Data (`ygfr-ij6t`, 49c); Client Data (`hm83-bdp7`) | ✅ |
| `ProgramActivity` | center activity listings | SODA | Older Adult Center (OAC) Activities (`fzy4-e84j`, 26c) | ✅ |
| `ServiceUnit` | — | SODA | Reported Service Units (`exaw-9qnu`); Budgeted Services (`nxrs-2ci5`); Reported Expenditures (`tt8e-a9vn`); Bottom Line Budget (`u845-acue`) | ✅ |
| `Participation` (client) | — | SODA | Number of Participants (`2td3-mfek`, 18c) — **aggregate only** | 🟡 aggregate |
| Apply for home-delivered meals | Aging Connect | **phone only** | — | ❌ gap |
| Request case management | Aging Connect | **phone only** | — | ❌ gap |
| Report suspected elder abuse | Aging Connect / APS | **phone only** | — | ❌ gap |
| **`ServiceReferral`** (connect to services) | Aging Connect (212-AGING-NYC) | **phone / 311 only** | — | ❌ **net-new** |

## The mismatch, concretely

| Source | Strength | Weakness |
|---|---|---|
| **Socrata SODA (11 datasets)** | Open, machine-readable; strong on the provider network, senior-center operations, activities, and contract spend | Reference/contract data only; static snapshots; nothing about a live resident intake |
| **Aging Connect (phone I&R)** | The real intake — case management, meals, benefits, caregiver, elder abuse, enrollment | Phone / walk-in only; no API, no OpenAPI, no JSON; not agent-accessible; a phone queue is the only channel |

## Implications for the API-first + MCP proposal

1. **Publish the open provider network as one clean resource model.** Providers, older adult centers, activities, service units, and aggregate participation behind one owned DFTA contract ([OpenAPI](openapi/dfta.yaml)) — so consumers learn one model, not 11 Socrata IDs.
2. **Connect the service layer.** Front Aging Connect with an API so the core resident transaction — making and tracking a **service referral** — has a machine-readable, agent-native contract.
3. **Add the one net-new write workflow** — `make_referral` (connect an older adult to services), with an urgent flag that routes suspected elder abuse / no-food / unsafe-at-home to Aging Connect / Adult Protective Services.
4. **Keep clients private.** Participation stays aggregate-only; the API never exposes an individual older adult record.
5. **MCP server** so an agent can answer "which older adult centers are in my council district?", "what did this program serve?", and — the point — "connect my mother to home-delivered meals and tell me the status."
