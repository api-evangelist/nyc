# Crosswalk — Website/Portal Fruit ↔ APIs ↔ NYC Open Data (DCAS)

Maps the low-hanging fruit on **nyc.gov/site/dcas** and the **aNNN application layer** to (a) the **existing APIs** (Socrata SODA; the vendor portals) and (b) the **32 DCAS datasets** on NYC Open Data. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-dcas.json](opendata-dcas.json).

## The reframe — fifth distinct pattern

- **Parks:** data-rich HTML on a legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned → *consolidate + own.*
- **NYCHA:** reference data wide open, every resident transaction locked in one vendor CRM → *unlock.*
- **DCAS:** the **reference data is broadly open** (32 Socrata datasets) and the careers front door is even replatformed onto modern .NET/Azure, but every **citizen transaction is scattered across separate rented apps** (Azure/.NET City Jobs, PeopleSoft self-service, Shopify store) with no API → **transact.**

DCAS is the reference-data-rich, transaction-poor pattern taken to its logical end. It publishes the civil-service machine generously — the Civil Service List (Active) alone has 3.5M lifetime views — yet the one thing a citizen most wants to *do*, **register for a civil-service exam**, has no API. You can read the exam schedule (`4ptz-hmtc`) as open data, but to apply you must log into OASys and pay a fee inside a vendor portal. A resident or agent asking "register me for the next Sanitation Worker exam" has nothing to call.

Coverage: ✅ strong open twin · 🟡 partial · ❌ gap (no API).

## Entity crosswalk

| Entity | Website / Portal | API today | Open Data | Cov. |
|---|---|---|---|---|
| `JobPosting` | `cityjobs.nyc.gov` | SODA | Jobs NYC Postings (`kpav-sd4t`, 30c) | ✅ |
| `CivilServiceTitle` | `/employees/salary-and-title-verification` | SODA | NYC Civil Service Titles (`nzjr-3966`, 11c) | ✅ |
| `EligibleListEntry` | `/employees` | SODA | Civil Service List Active (`vx8i-nprf`, 20c); Certification (`a9md-ynri`); Terminated (`qu8g-sxqf`); Civil List (`ye3c-m4ga`) | ✅ |
| `ExamSchedule` | `/employees/current-exams` | SODA | Annual Examination Schedule (`4ptz-hmtc`, 7c) | ✅ |
| `CityBuilding` | `/agencies/facilities-management` | SODA | DCAS Managed Public Buildings (`xx2p-4jnq`, 22c); Energy Usage (`ubdi-jgw2`); Benchmarking (`vvj6-d5qx`) | ✅ |
| `FleetVehicle` | `/agencies/fleet` | SODA | Fleet Daily Service (`5rzx-3686`); Vehicle Auction (`ynic-uz5i`); Fuel Efficiency (`mn2p-34if`); EV Stations (`fc53-9hrv`) | ✅ |
| CityStore purchase | `a856-citystore.nyc.gov` | **Shopify tenant only** | CityStore catalog (`mqdy-gu73`) | 🟡 catalog only |
| Employee self-service | `a127-ess.nyc.gov` | **PeopleSoft UI only** | — | ❌ gap |
| `JobApplication` (apply to a posting) | `cityjobs.nyc.gov` | **ASP.NET/OASys UI only** | — | ❌ gap |
| **`ExamRegistration`** (register for an exam) | OASys / `a127-jobs.nyc.gov` | **OASys UI only** | — | ❌ **net-new** |

## The mismatch, concretely

| Source | Strength | Weakness |
|---|---|---|
| **Socrata SODA (32 datasets)** | Open, machine-readable; strong on civil-service lists, titles, exam schedule, buildings, and fleet; some assets with millions of views | Reference/asset data only; static snapshots; nothing about live citizen transactions |
| **aNNN vendor apps (City Jobs, ESS, CityStore)** | The real transaction systems — job applications, exam registration, HR self-service, retail | Three separate rented tenants (Azure/.NET, PeopleSoft, Shopify); none exposes a DCAS-owned API, OpenAPI, or JSON; not agent-accessible |

## Implications for the API-first + MCP proposal

1. **Publish the open reference data as one clean resource model.** Postings, titles, eligible lists, exam schedule, buildings, and fleet behind one owned DCAS contract ([OpenAPI](openapi/dcas.yaml)) — so consumers learn one model, not 32 Socrata IDs.
2. **Transact.** Front the aNNN apps with an API so the core citizen transaction — **registering for a civil-service exam** — has a machine-readable, agent-native contract.
3. **Add the one net-new write workflow** — `register_for_exam` (create an exam registration), carrying veteran/residency-credit claims, fee-waiver, and accommodation requests. `JobApplication` is the obvious second write surface.
4. **Unify the three tenants.** One DCAS API in front of Azure City Jobs, PeopleSoft self-service, and the Shopify CityStore reduces the governance and continuity risk of three separate vendor relationships.
5. **MCP server** so an agent can answer "which exams are open now?", "what's the salary band for this title?", and — the point — "register me for exam 1234 and claim my residency credit."
