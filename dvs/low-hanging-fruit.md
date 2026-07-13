# Low-Hanging Fruit Index — DVS

**Agency:** NYC Department of Veterans' Services (DVS)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt — `nyc.gov/robots.txt` only disallows `/html/misc/`). Fingerprinted the informational site `nyc.gov/site/veterans` (Akamai + nginx + NYC.gov "Livesite" platform v22 + Dynatrace) and resolved the **VetConnectNYC** intake to a third-party host, `nyc.veteranportal.combinedarms.us` — the **Combined Arms** "Military Resource Portal" (Next.js on CloudFront, `x-powered-by: Next.js`). Verified the NYC Open Data agency label `Department of Veterans' Services (DVS)` via the Socrata Discovery API and pulled all **7** assets with column schemas.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-dvs.md](opendata-dvs.md).

## Headline findings

1. **DVS is a connective agency with a vendor service layer.** An informational site on the shared NYC.gov chassis, and a care-coordination intake — **VetConnectNYC** — that runs on a **third-party platform, Combined Arms** (`nyc.veteranportal.combinedarms.us`), with **no API**.
2. **DVS is unusually open.** **7 NYC Open Data datasets** cover not only reference directories (DVS Resource Map, NYC Veteran Owned Businesses) but **de-identified service analytics** — assistance requests (with a `VetConnectNYC (Y/N)` flag), cases, client demographics, and historical request processing.
3. **But the live referral is locked.** The thing a veteran actually *does* — submit a VetConnectNYC request and get connected to services — has no machine-readable contract; it lives only in the Combined Arms web form and a manual **3–5 business-day** DVS Care Coordinator queue.
4. **Veterans stay private by design.** Client demographics are published only de-identified/aggregate; no identifiable veteran record is ever exposed.

> **Reframe:** Parks = *replatform* a legacy site; DOE = *reclaim* rented search; Council = *consolidate + own* fragmented APIs; NYCHA = *unlock* a vendor CRM; DFTA = *connect* through a phone contact center; **DVS = coordinate — own the referral.** Here even the service data is already open — the work is least about liberating datasets and most about giving the **VetConnectNYC referral** an owned, agent-native API instead of an out-of-city vendor form.
>
> **Vendor correction:** the assignment guessed VetConnectNYC was the Unite Us platform; the crawl shows it is **Combined Arms**. See [tech-stack.md](tech-stack.md).

## The fruit

| # | Name | Entity | Where the data lives | Open Data twin |
|---|---|---|---|---|
| 1 | DVS Resource Map | `VeteranResource` | SODA | ✅ Resource Map (`af2s-4k4p`, 15c) |
| 2 | NYC Veteran Owned Businesses | `VeteranOwnedBusiness` | SODA | ✅ Veteran Owned Businesses (`ybdk-jmnn`, 27c) |
| 3 | Assistance Requests | `AssistanceRequest` | SODA | 🟡 Assistance Requests (`jup5-7fik`, 22c) — de-identified |
| 4 | Cases | `Case` | SODA | 🟡 DVS Cases (`pw4e-vms3`, 9c) — de-identified |
| 5 | Client demographics | `ClientStatistics` | SODA | 🟡 DVS Clients (`idat-aemv`, 12c) — aggregate only |
| 6 | Historical request processing | `AssistanceRequest` | SODA | ✅ Historical Client Requests (`44f4-mjxy`); VPC Moves (`davn-rbxj`) |
| 7 | Connect to services / VA claims | `ServiceReferral` | VetConnectNYC (Combined Arms) | ❌ gap (no API) |
| 8 | Housing / homelessness help | `ServiceReferral` | VetConnectNYC (Combined Arms) | ❌ gap (no API) |
| 9 | **Make a VetConnectNYC referral** | `ServiceReferral` | VetConnectNYC Request Form + Care Coordinators | ❌ **net-new** |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **Socrata SODA** — 7 DVS datasets (the one real, open API; reference *and* de-identified service data).
- **Combined Arms — VetConnectNYC** — the "Military Resource Portal"; registration-gated web form, Next.js on CloudFront, no API; DVS Care Coordinators process within 3–5 business days.
- Platform: informational site on the **NYC.gov shared "Livesite" platform** (Akamai edge, nginx, Dynatrace RUM) — the same chassis as Parks/DOE/Council/NYCHA/DFTA.

## Reverse-engineered entities

`VeteranResource` · `VeteranOwnedBusiness` · `AssistanceRequest` (de-identified) · `Case` (de-identified) · `ClientStatistics` (aggregate; never individual) · `ServiceReferral` (net-new write; the VetConnectNYC referral) — join key: **DVS_RES_ID** for resources/businesses; the service records are de-identified, keyed only on record/request numbers.

## Next

1. **JSON Schema** per entity, reconciling real Open Data column names (DVS_RES_ID, the geography spine, branch/discharge/service-era vocabularies, the `VetConnectNYC (Y/N)` flag) — done ([schemas/](schemas/)).
2. **OpenAPI** publishing the open reference and service data as clean resources + the net-new `POST /referrals` (make a VetConnectNYC referral) — done ([openapi/dvs.yaml](openapi/dvs.yaml)).
3. **MCP** artifact: `find_veteran_resources`, `get_veteran_resource`, `find_veteran_owned_businesses`, `find_assistance_requests`, `find_cases`, `find_client_statistics`, `list_my_referrals`, `make_referral` — done ([mcp/dvs-mcp.json](mcp/dvs-mcp.json)).
