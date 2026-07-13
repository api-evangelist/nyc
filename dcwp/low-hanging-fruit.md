# Low-Hanging Fruit Index — DCWP

**Agency:** Department of Consumer and Worker Protection (DCWP, formerly the Department of Consumer Affairs / DCA)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt — `nyc.gov/robots.txt` only disallows `/html/misc/`). Fingerprinted the informational site `nyc.gov/site/dca` (Akamai + nginx + NYC.gov "Livesite" v22 + Dynatrace) and the **NYC Business licensing portal** at `nyc-business.nyc.gov/nycbusiness` (a Java/Spring web app — `SESSION` cookie, Akamai, Dynatrace). Verified the NYC Open Data agency label `Department of Consumer and Worker Protection (DCWP)` via the Socrata Discovery API and pulled all **37** assets with column schemas.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-dcwp.md](opendata-dcwp.md).

## Headline findings

1. **DCWP is the most-open domain in this project.** **37 NYC Open Data datasets** publish the entire regulated-business lifecycle — license applications, issued licenses (147k views), inspections, charges/violations, consumer complaints, revocations, and Office of Labor Policy & Standards worker-protection matters.
2. **But no owned contract binds it.** The whole lifecycle is joinable on `Business Unique ID` and `License Number`, yet a consumer or agent must stitch 37 Socrata IDs by hand. There is no single DCWP API.
3. **The two citizen writes have no API.** Applying for a business license lives only in the Java NYC Business portal; filing a consumer complaint lives only in 311 or a web form. Neither has a machine-readable contract.
4. **Workers stay private by design.** OLPS worker-protection data is published only in aggregate by topic/industry/geography; no individual worker is ever exposed.

> **Reframe (fifth distinct pattern):** Parks = *replatform* a legacy site; DOE = *reclaim* rented search; Council = *consolidate + own* three fragmented APIs; NYCHA = *unlock* a locked service layer; **DCWP = bind the open lifecycle and add the writes.** Here the data is already open *and* complete — the work is least about liberating datasets and most about giving the 37-dataset lifecycle one owned contract and giving the two citizen transactions (apply for a license, file a complaint) an API instead of a Java portal or a 311 form.

## The fruit

| # | Name | Entity | Where the data lives | Open Data twin |
|---|---|---|---|---|
| 1 | Issued Licenses | `BusinessLicense` | SODA | ✅ Issued Licenses (`w7w3-xahh`, 31c) |
| 2 | License Applications | `LicenseApplication` | SODA (read) / portal (write) | ✅ License Applications (`ptev-4hud`, 35c) |
| 3 | DCWP Inspections | `Inspection` | SODA | ✅ DCWP Inspections (`jzhd-m6uv`, 28c) |
| 4 | DCWP Charges (violations) | `Charge` | SODA | ✅ DCWP Charges (`5fn4-dr26`, 18c) |
| 5 | Consumer Complaints | `ConsumerComplaint` | SODA (read) / 311 (write) | ✅ Consumer Complaints (`nre2-6m2s`, 33c) |
| 6 | License Revocations & Suspensions | `BusinessLicense` | SODA | ✅ Revocations (`rpeq-j89e`, 7c) |
| 7 | Worker Protection (OLPS) | `WorkerProtectionCase` | SODA | 🟡 Enforcement/Inquiries (`c292-vzrn`, `2z24-2htf`) — aggregate only |
| 8 | DCWP Licensed Vehicles | `BusinessLicense` | SODA | ✅ Licensed Vehicles (`9vpn-rpgs`, 15c) |
| 9 | **Apply for a license** | `LicenseApplication` | NYC Business portal | ❌ **net-new write** |
| 10 | **File a consumer complaint** | `ConsumerComplaint` | 311 / web form | ❌ **net-new write** |
| 11 | Pay a fine / fee | `Charge` | CityPay | ❌ gap (no API) |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **Socrata SODA** — 37 DCWP datasets (the one real, open API; the whole lifecycle as reference data).
- **NYC Business portal** (`nyc-business.nyc.gov`) — a Java/Spring licensing app; session-gated, browser-only, no API.
- **CityPay** (CityBase) and **311** — payment and complaint intake; UI only, no public API.
- Platform: informational site on the **NYC.gov shared "Livesite" v22 platform** (Akamai edge, nginx, Dynatrace RUM) — the same chassis as NYCHA and every citywide agency site.

## Reverse-engineered entities

`BusinessLicense` · `LicenseApplication` (net-new write) · `Inspection` · `Charge` (violation) · `ConsumerComplaint` (net-new write) · `WorkerProtectionCase` (aggregate; never individual worker) — join keys: **Business Unique ID**, **License Number** / **DCWP License Number**, **Application ID**, **Inspection Number**, **NOH Number**, **BBL/BIN**.

## Next

1. **JSON Schema** per entity, reconciling real Open Data column names (Business Unique ID, License Number, NOH Number, the geography spine) — done ([schemas/](schemas/)).
2. **OpenAPI** binding the open lifecycle as clean resources + the net-new `POST /license-applications` (apply) and `POST /consumer-complaints` (file a complaint) — done ([openapi/dcwp.yaml](openapi/dcwp.yaml)).
3. **MCP** artifact: `find_licenses`, `get_license`, `find_applications`, `find_inspections`, `find_charges`, `find_consumer_complaints`, `find_worker_protection_cases`, `apply_for_license`, `file_complaint` — done ([mcp/dcwp-mcp.json](mcp/dcwp-mcp.json)).
