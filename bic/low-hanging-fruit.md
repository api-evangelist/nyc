# Low-Hanging Fruit Index — BIC

**Agency:** New York City Business Integrity Commission (BIC)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt — `nyc.gov/robots.txt` only disallows `/html/misc/`). Fingerprinted the informational site `nyc.gov/site/bic` (Akamai + nginx + NYC.gov "Livesite" v22 + Dynatrace) and the transactional portal at `bicportal.nyc.gov`, identified as **Salesforce Experience Cloud** (`server: sfdcedge`, `x-sfdc-request-id`, Lightning `/s/` paths incl. `/s/viopay`). Verified the NYC Open Data agency label `Business Integrity Commission (BIC)` via the Socrata Discovery API and pulled all **9** assets with column schemas.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-bic.md](opendata-bic.md).

## Headline findings

1. **BIC is a split domain.** An informational site on the shared NYC.gov chassis, and a licensing/enforcement **portal running Salesforce Experience Cloud** (`bicportal.nyc.gov`) with **no API**.
2. **The regulatory registry is unusually open.** **9 NYC Open Data datasets** cover trade waste hauler licensees (`867j-5pgi`, ~78k views), broker/self-hauler/construction-and-demolition registrants, public wholesale-market businesses (Hunts Point, Fulton Fish), the licensee/registrant vehicle fleet, issued violations, complaints, and denied companies — all keyed on **BIC NUMBER**.
3. **But the transaction layer is locked.** Applying for and renewing a license/registration and paying a violation fine (`/s/viopay`) — the things businesses actually *do* — live only inside a login-walled Salesforce portal or on paper. None has a machine-readable contract.
4. **Open data publishes outputs, not the workflow.** The registry shows who *is* licensed and who was *denied* (`exsg-kpya`), but nothing of the apply → review → approve pipeline that produces those records.

> **Reframe (fifth distinct pattern):** Parks = *replatform* a legacy site; DOE = *reclaim* rented search + a hidden backend; Council = *consolidate + own* three fragmented APIs; NYCHA = *unlock* a resident service layer locked in a Siebel CRM; **BIC = transact.** Here the registry is the most open of any domain yet — the work is least about liberating datasets and most about giving the **licensing lifecycle** (apply, renew, pay) an owned, agent-native API instead of a vendor SaaS screen.

## The fruit

| # | Name | Entity | Where the data lives | Open Data twin |
|---|---|---|---|---|
| 1 | Trade Waste Hauler Licensees | `Licensee` | SODA | ✅ Licensees (`867j-5pgi`, 27c) |
| 2 | Registrants (Broker/Self-Hauler/C&D) | `Registrant` | SODA (×3) | ✅ Broker (`krx7-u82t`) + self-hauler + C&D |
| 3 | Public Wholesale Market Businesses | `MarketBusiness` | SODA | ✅ Wholesale Markets (`87fx-28ei`, 26c) |
| 4 | Licensee/Registrant Fleet | `Vehicle` | SODA | ✅ Fleet Information (`n84m-kx4j`, 18c) |
| 5 | BIC Issued Violations | `Violation` | SODA | ✅ Issued Violations (`upii-frjc`, 31c) |
| 6 | Complaints & Inquiries | `Complaint` | SODA + 311 | 🟡 Complaints (`p2d7-vcsb`) — intake via 311 |
| 7 | Denied Companies (decisions) | `TradeWasteLicenseApplication` | SODA | 🟡 Denials only (`exsg-kpya`, 22c) |
| 8 | Pay a violation fine | `Violation` | Salesforce portal `/s/viopay` | ❌ gap (no API) |
| 9 | Renew a license/registration | `TradeWasteLicenseApplication` | Salesforce portal | ❌ gap (no API) |
| 10 | **Apply for a trade waste license/registration** | `TradeWasteLicenseApplication` | Salesforce portal + paper | ❌ **net-new** |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **Socrata SODA** — 9 BIC datasets (the one real, open API; registry/outputs only).
- **Salesforce Experience Cloud** — the licensing/payment portal; login-walled, JavaScript-only, no API.
- Platform: informational site on the **NYC.gov shared "Livesite" platform** (Akamai edge, nginx, Dynatrace RUM) — the same chassis as NYCHA, but here the locked layer is a Salesforce SaaS rather than an Oracle Siebel CRM.

## Reverse-engineered entities

`Licensee` · `Registrant` (broker / self-hauler / C&D) · `MarketBusiness` (wholesale markets) · `Vehicle` (BIC-plated fleet) · `Violation` · `Complaint` · `TradeWasteLicenseApplication` (net-new write; also stands in for the Salesforce-locked renew / pay-a-fine transactions) — join key: **BIC NUMBER**, plus the full NYC geography spine.

## Next

1. **JSON Schema** per entity, reconciling real Open Data column names (BIC NUMBER, APPLICATION TYPE, VIOLATION NUMBER, BIC PLATE NUMBER, the geography spine) — done ([schemas/](schemas/)).
2. **OpenAPI** publishing the open registry as clean resources + the net-new `POST /applications` (apply for a license) — done ([openapi/bic.yaml](openapi/bic.yaml)).
3. **MCP** artifact: `find_licensees`, `get_licensee`, `find_registrants`, `find_market_businesses`, `find_vehicles`, `find_violations`, `find_complaints`, `list_my_applications`, `apply_for_license` — done ([mcp/bic-mcp.json](mcp/bic-mcp.json)).
