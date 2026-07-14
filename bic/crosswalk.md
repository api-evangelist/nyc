# Crosswalk — Website/Portal Fruit ↔ APIs ↔ NYC Open Data (BIC)

Maps the low-hanging fruit on **nyc.gov/site/bic** and the **bicportal.nyc.gov** portal to (a) the **existing APIs** (Socrata SODA; the Salesforce portal) and (b) the **9 BIC datasets** on NYC Open Data. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-bic.json](opendata-bic.json).

## The reframe — fifth distinct pattern

- **Parks:** data-rich HTML on a legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned → *consolidate + own.*
- **NYCHA:** reference data open, resident transactions locked in an Oracle Siebel CRM → *unlock.*
- **BIC:** the **regulatory registry is the most open yet** (9 Socrata datasets — licensees, registrants, markets, fleet, violations, complaints, denials), but every **business transaction is locked inside a Salesforce Experience Cloud portal** → **transact.**

BIC is a **public registry with a private front counter.** The data publishes the *outputs* of the licensing lifecycle — who is licensed, who was denied, what violations issued — generously. But the things a business *does* — apply for a license, renew it, pay a fine — live only behind a login-walled Salesforce Lightning app. A business or agent asking "submit my trade waste license application" or "what's the status of my application?" has no API to call; the only public trace of that pipeline is the list of companies that were *denied* (`exsg-kpya`).

Coverage: ✅ strong open twin · 🟡 partial (outputs only / intake elsewhere) · ❌ gap (no API).

## Entity crosswalk

| Entity | Website / Portal | API today | Open Data | Cov. |
|---|---|---|---|---|
| `Licensee` | `/industries` | SODA | Trade Waste Hauler Licensees (`867j-5pgi`, 27c) | ✅ |
| `Registrant` | `/industries` | SODA | Broker (`krx7-u82t`), Self Hauler (`a8wp-rerh`), C&D (`cspg-yi7g`) | ✅ |
| `MarketBusiness` | `/industries` (wholesale markets) | SODA | Wholesale Markets (`87fx-28ei`, 26c) | ✅ |
| `Vehicle` (fleet) | side-guard requirement page | SODA | Licensees and Registrants Fleet Information (`n84m-kx4j`, 18c) | ✅ |
| `Violation` | `/complaints` | SODA | BIC Issued Violations (`upii-frjc`, 31c) | ✅ |
| `Complaint` | `/complaints` + 311 | SODA (closed records) | BIC Complaints Inquiries (`p2d7-vcsb`, 42c) | 🟡 intake via 311 |
| Pay a violation fine | Salesforce portal `/s/viopay` | **Salesforce UI only** | — | ❌ gap |
| Renew a license/registration | Salesforce portal | **Salesforce UI only** | — | ❌ gap |
| **`TradeWasteLicenseApplication`** (apply) | Salesforce portal + paper | **Salesforce UI only** | Denials only (`exsg-kpya`, 22c) | ❌ **net-new** |

## The mismatch, concretely

| Source | Strength | Weakness |
|---|---|---|
| **Socrata SODA (9 datasets)** | Open, machine-readable; strong on the full regulatory registry — licensees, registrants, markets, fleet, violations, complaints, denials; unified by BIC NUMBER | Snapshots of *outputs*; nothing about live applications, renewals, or payments in flight |
| **Salesforce portal** | The real transaction system — apply, renew, pay a fine | Login-walled, JavaScript-only vendor SaaS; no API, no OpenAPI, no JSON; not agent-accessible; system-of-record with no export contract |

## Implications for the API-first + MCP proposal

1. **Publish the open registry as one clean resource model.** Licensees, registrants, market businesses, fleet, violations, and complaints behind one owned BIC contract ([OpenAPI](openapi/bic.yaml)) — so consumers learn one model keyed on BIC NUMBER, not 9 Socrata IDs.
2. **Transact the service layer.** Front the Salesforce portal with an API so the core business transaction — submitting and tracking a **trade waste license application** — has a machine-readable, agent-native contract.
3. **Add the one net-new write workflow** — `apply_for_license` (submit a license/registration/exemption application), with the decision (approve/deny) reconciled back to the public registry and denials datasets.
4. **Close the loop.** A live application should resolve to the same BIC NUMBER-keyed record that later appears in the licensee/registrant registry, or in `exsg-kpya` if denied.
5. **MCP server** so an agent can answer "is this hauler licensed?", "what violations does this company have?", "which businesses operate in the Hunts Point Produce Market?", and — the point — "apply for a trade waste license and tell me the status."
