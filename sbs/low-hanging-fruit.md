# Low-Hanging Fruit Index — SBS

**Agency:** NYC Department of Small Business Services (SBS)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt — `nyc.gov/robots.txt` only disallows `/html/misc/`). Fingerprinted the informational site `nyc.gov/site/sbs` (Akamai + nginx + NYC.gov "Livesite" platform + Dynatrace) and the business **MyCity Business** portal at `nyc-business.nyc.gov/nycbusiness`, identified as a **Spring-session Java app** with **Adobe AEM** (Universal Editor) + jQuery/Handlebars + Akamai mPulse; the **Step-by-Step** licensing wizard confirmed at `/nycbusiness/wizard`. Verified the NYC Open Data agency label `Department of Small Business Services (SBS)` via the Socrata Discovery API and pulled all **28** assets with column schemas.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-sbs.md](opendata-sbs.md).

## Headline findings

1. **SBS is a split domain.** An informational site on the shared NYC.gov chassis, and a business **service portal — MyCity Business** (`nyc-business.nyc.gov`) on **Spring + Adobe AEM** with **no API**.
2. **The program data is reasonably open.** **28 NYC Open Data datasets** cover the **SBS Certified Business List** (M/WBE, 56 columns), **Business Improvement Districts** (directory, maps, 64-column FY24 trends), **Workforce1** recruitment events and job listings, service-center locations, and business-incentive rolls.
3. **But SBS is a navigator agency, and its navigation is locked.** The **Step-by-Step licensing wizard** (which licenses/permits does my business need?), incentive eligibility, and the M/WBE **certification** and Workforce1 **enrollment** flows — the things SBS actually *does* — live only inside the session-bound MyCity Business portal. None has a machine-readable contract.
4. **The public certified list is the shadow of a closed flow.** You can read who got certified (`ci93-uc8s`, 56c), but there is no API to apply.

> **Reframe (fifth distinct pattern):** Parks = *replatform* a legacy site; DOE = *reclaim* rented search + a hidden backend; Council = *consolidate + own* three fragmented APIs; NYCHA = *unlock* a service layer trapped in a vendor CRM; **SBS = navigate.** Here the directories are already open — the work is least about liberating datasets and most about giving the **guidance and eligibility engine** (the wizard, and above all certification) an owned, agent-native API instead of a stateful portal screen.

## The fruit

| # | Name | Entity | Where the data lives | Open Data twin |
|---|---|---|---|---|
| 1 | SBS Certified Businesses (M/WBE) | `CertifiedBusiness` | SODA + map | ✅ Certified Business List (`ci93-uc8s`, 56c) |
| 2 | Business Improvement Districts | `BusinessImprovementDistrict` | SODA + map | ✅ Directory of BIDs (`qpm9-j523`) + Trends (`hzd8-k2vv`, 64c) |
| 3 | Workforce1 Recruitment Events | `WorkforceEvent` | SODA | ✅ Recruitment Events (`kf2b-aeh5`) |
| 4 | Workforce1 Job Listings | `JobListing` | SODA | ✅ Job Listing (`ay9k-vznm`, 22c) |
| 5 | Center & Service Locations | `ServiceLocation` | SODA | ✅ Center & Service Locations (`6smc-7mk6`, 19c) |
| 6 | Business Incentives | `BusinessIncentive` | SODA (×4) | ✅ Energy Cost Savings (`bug8-9f3g`) + ICAP + Acceleration |
| 7 | Step-by-Step licensing wizard | — (portal) | MyCity Business | ❌ gap (no API) |
| 8 | Workforce1 enrollment | — (portal) | MyCity Business | ❌ gap (no API) |
| 9 | **Apply for M/WBE certification** | `MWBECertificationApplication` | MyCity Business / PASSPort | ❌ **net-new** |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **Socrata SODA** — 28 SBS datasets (the one real, open API; program data only).
- **MyCity Business** — the business service portal; **Spring** session + **Adobe AEM** + jQuery/Handlebars, login-walled, JavaScript-only, no API. Hosts the **Step-by-Step** wizard.
- Platform: informational site on the **NYC.gov shared "Livesite" platform** (Akamai edge, nginx, Dynatrace RUM) — the same chassis seen at Parks, DOE, Council, and NYCHA.

## Reverse-engineered entities

`CertifiedBusiness` · `BusinessImprovementDistrict` · `WorkforceEvent` · `JobListing` · `ServiceLocation` · `BusinessIncentive` (folds three incentive programs) · `MWBECertificationApplication` (net-new write; also stands in for the portal-locked Step-by-Step wizard and Workforce1 enrollment) — join keys: **Account_Number**, **NAICS**, **BBL/BIN**, and the borough/council/NTA geography spine.

## Next

1. **JSON Schema** per entity, reconciling real Open Data column names (Account_Number, NAICS, org_id, BBL/BIN, the geography spine) — done ([schemas/](schemas/)).
2. **OpenAPI** publishing the open program data as clean resources + the net-new `POST /mwbe-applications` (apply for M/WBE certification) — done ([openapi/sbs.yaml](openapi/sbs.yaml)).
3. **MCP** artifact: `find_certified_businesses`, `get_certified_business`, `find_business_improvement_districts`, `get_business_improvement_district`, `find_workforce_events`, `find_job_listings`, `find_service_locations`, `find_incentives`, `list_my_mwbe_applications`, `apply_for_mwbe_certification` — done ([mcp/sbs-mcp.json](mcp/sbs-mcp.json)).
