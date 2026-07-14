# Low-Hanging Fruit Index — CFB

**Agency:** NYC Campaign Finance Board (CFB)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA; `nyccfb.info` serves no robots.txt — 404). Fingerprinted the main site and Follow the Money search on `nyccfb.info` (Microsoft IIS 8.5 + ASP.NET MVC 5.2 + AngularJS 1.5), confirmed the **real JSON Web API** behind FTM at `nyccfb.info/FTMSearchWebAPI` (live JSON from `/api/Common/GetElectionCycle`), catalogued the bulk **Data Library** (`/DataLibrary/*.csv`, 56 files, 2001–2025), and identified the login-walled **C-SMART** / **IEDS** filing applications and the **NYC Votes** (Umbraco/Azure) voter site. Verified the NYC Open Data agency label `Campaign Finance Board (CFB)` via the Socrata Discovery API and pulled all **16** assets with column schemas.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-cfb.md](opendata-cfb.md).

## Headline findings

1. **CFB is the transparency leader — and *almost* API-first already.** It runs on its **own domain** (`nyccfb.info`, not nyc.gov), publishes **16 Open Data datasets**, ships a **bulk CSV Data Library** back to 2001, and its Follow the Money search is a single-page app backed by a **real, working JSON Web API** (`FTMSearchWebAPI`).
2. **But the API is undocumented and unowned.** No OpenAPI, no developer docs, no stable public contract, no agent-native surface. It is a de-facto API, not a published product.
3. **The data is published three uncoordinated ways** — Socrata, bulk CSV, and the live API — never as one clean, versioned resource model.
4. **The one write is locked.** Filing a **disclosure statement** happens only inside **C-SMART** (or **IEDS** for outside spenders); there is no submission API and no Open Data twin — only *filing status* leaks out via the Late/Missing Disclosure Statements dataset.

> **Reframe (fifth distinct pattern):** Parks = *replatform* a legacy site; DOE = *reclaim* rented search + a hidden backend; Council = *consolidate + own* three fragmented APIs; NYCHA = *unlock* a service layer locked in a vendor CRM; **CFB = document the API you already built, and give filing a contract.** Here the data is open *and* a search API exists — the work is least about liberating datasets and most about **maturing an existing API into an owned product** and adding the one net-new write (submitting a disclosure).

## The fruit

| # | Name | Entity | Where the data lives | Open Data twin |
|---|---|---|---|---|
| 1 | Campaign Contributions | `Contribution` | FTM API + SODA + CSV | ✅ Campaign Contributions (`rjkp-yttg`, 54c) |
| 2 | Campaign Expenditures | `Expenditure` | FTM API + SODA + CSV | ✅ Campaign Expenditures (`qxzj-vkn2`, 32c) |
| 3 | Campaign Intermediaries (bundlers) | `Contribution` | SODA + FTM API | ✅ Intermediaries (`tcwb-nry3`) |
| 4 | Public Funds Payments | `PublicMatchingFundsPayment` | SODA + CSV | ✅ Public Funds Payments (`u69g-mvrb`) |
| 5 | Campaign Financial Analysis | `Candidate` | SODA + FTM API | ✅ Financial Analysis (`m3tj-a2pb`, 26c) |
| 6 | Follow the Money search API | `Contribution` | **FTM Web API (undocumented)** | — (real API, not a dataset) |
| 7 | Late/Missing Disclosure Statements | `DisclosureFiling` | SODA | 🟡 Late/Missing (`2ujk-6z7u`) — status only |
| 8 | Enforcement & audit determinations | `DisclosureFiling` | SODA | ✅ Penalties (`xrxs-qn95`) + Audits (`x4w5-m7uh`) |
| 9 | Voter analysis & turnout (NYC Votes) | `Candidate` | SODA | ✅ Voter Analysis (`psx2-aqx3`, 175c) |
| 10 | **File a disclosure statement (C-SMART)** | `DisclosureFiling` | C-SMART / IEDS | ❌ **net-new** |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **FTM Web API** — `nyccfb.info/FTMSearchWebAPI` (ASP.NET Web API); the real, undocumented JSON backend of Follow the Money.
- **Socrata SODA** — 16 CFB datasets.
- **Data Library** — 56 bulk CSVs, 2001–2025.
- **C-SMART / IEDS** — login-walled disclosure filing applications; no API.
- Platform: **IIS 8.5 / ASP.NET MVC 5.2 + AngularJS 1.5** on the CFB's own domain; **Umbraco/ASP.NET on Azure** for `nycvotes.org` — the fifth distinct platform after Parks' Smarty/PHP, DOE's Sitefinity/.NET, Council's WordPress, and NYCHA's NYC.gov Livesite + Oracle Siebel.

## Reverse-engineered entities

`Candidate` · `Committee` (filer) · `Contribution` (with intermediary/bundler detail) · `Expenditure` · `PublicMatchingFundsPayment` · `DisclosureFiling` (net-new write; also carries the Late/Missing status read) — join keys: **CANDID / RECIPID**, **COMMITTEE**, **ELECTION cycle**, **OFFICECD**, **REFNO**.

## Next

1. **JSON Schema** per entity, reconciling real column names (CANDID, RECIPID, AMNT, MATCHAMNT, INTERMNAME, OFFICECD, the money/office/election spine) — done ([schemas/](schemas/)).
2. **OpenAPI** documenting the FTM search data as clean resources + the net-new `POST /disclosure-filings` (file a disclosure) — done ([openapi/cfb.yaml](openapi/cfb.yaml)).
3. **MCP** artifact: `find_candidates`, `get_candidate`, `find_committees`, `find_contributions`, `find_expenditures`, `find_public_funds_payments`, `find_disclosure_filings`, `get_disclosure_filing`, `file_disclosure` — done ([mcp/cfb-mcp.json](mcp/cfb-mcp.json)).
