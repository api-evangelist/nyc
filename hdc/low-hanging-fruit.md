# Low-Hanging Fruit Index — HDC

**Agency:** New York City Housing Development Corporation (HDC)
**Assessed:** 2026-07-16
**Method:** Outside-in crawl (browser UA). Fingerprinted the informational site `www.nychdc.com` (Drupal 10 on Pantheon + Fastly CDN + nginx + Google Tag Manager/GA) and read the **Develop** and **Invest** sections (financing programs + PDF term sheets; Debt Issuance / Sustainable Development Bonds / EMMA disclosure). Confirmed via the Socrata Discovery API that **zero** NYC Open Data assets are attributed to HDC, and identified the adjacent datasets that actually carry HDC's record (**HPD**'s LIHTC 4% awards; **OMB**'s Debt Issuance by Issuer). The net-new write (the **Developer Intake Portal** / Developer Intake Form) is quoted from `nychdc.com/develop`.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-hdc.md](opendata-hdc.md).

## Headline findings

1. **HDC is a public benefit corporation and affordable-housing bond financier.** One of the nation's largest municipal housing bond issuers — it lends to developers and borrows from bond investors. There is **no citizen and no citizen transaction** anywhere in the domain.
2. **HDC owns no NYC Open Data and no API — of any kind.** Verified via the Socrata Discovery API: **0** datasets are attributed to HDC. This is *thinner than DDC*, which at least owns four Socrata datasets; HDC owns none.
3. **The record is dispersed across three owners HDC doesn't control.** Developments → **HPD** (the LIHTC **4%** awards are precisely HDC's tax-exempt-bond-financed deals). Debt → **OMB** ("Debt Issuance by Issuer", where HDC is one `Issuer Name` value). Investor disclosure → the **federal MSRB EMMA** platform (Official Statements, financials, SDB annual reports — as documents).
4. **HDC's own surfaces publish nothing structured.** The website is a Drupal/Pantheon marketing site with no content API (`/developments`, `/where-we-fund` → 404); the programs (New Construction, ELLA, Mix and Match, Preservation, PACT Preservation, Sustainable Development Bonds) are HTML pages + **PDF term sheets**; and the one transaction HDC owns — the **Developer Intake Portal** — has no API.

> **Reframe (a new distinct pattern):** DDC = *surface* a thin/historical data set whose transactions run on citywide systems; LPC = *bind* open data scattered across vendor silos with the write locked in Salesforce; **HDC = originate.** HDC owns *no* Open Data and *no* API — its development record is HPD's, its debt OMB's, its investor disclosure the federal MSRB's — so the work is to *originate* an owned HDC contract where none exists: consolidate the dispersed financing record and front the one transaction HDC controls (developer financing intake) with an agent-native write.

## The fruit

| # | Name | Entity | Where the data lives | Open Data twin |
|---|---|---|---|---|
| 1 | HDC-Financed Developments | `Development` | HPD SODA (not HDC's) | 🟡 HPD LIHTC 4% (`p8i7-ix2s` 26c, `h9ws-rfd9` 3c) |
| 2 | Financing Programs (term sheets) | `FinancingProgram` | PDFs | ❌ gap (documents) |
| 3 | Bond Issues (HRB / SDB) | `BondIssue` | OMB SODA + federal EMMA | 🟡 OMB `n5n4-5k5r` (HDC as `Issuer Name`) |
| 4 | Developers / Borrowers | `Borrower` | derived | 🟡 derived from HPD `Applicant Name` |
| 5 | **Apply for HDC financing** | `FinancingApplication` | HDC Developer Intake Portal | ❌ **net-new (B2G)** |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **No HDC-owned API or Open Data** — verified 0 datasets attributed to HDC.
- **HPD LIHTC datasets (Socrata)** — the closest record of HDC-financed developments, but **HPD-owned**, keyed on BBL/BIN.
- **OMB "Debt Issuance by Issuer" (Socrata)** — HDC appears only as an `Issuer Name` value.
- **Federal MSRB EMMA** — HDC's investor disclosure, as PDFs on a federal platform.
- **HDC Developer Intake Portal** — the one HDC-owned transaction; no API.
- Platform: an independent **Drupal 10 on Pantheon** site behind **Fastly** — *not* the shared NYC.gov Livesite chassis, because HDC is a public benefit corporation.

## Reverse-engineered entities

`Development` (HDC-financed project; reconciled from HPD LIHTC 4% awards) · `FinancingProgram` (term-sheet programs) · `BondIssue` (HRB/SDB; OMB + federal EMMA) · `Borrower` (developer; derived) · `FinancingApplication` (net-new B2G write — the Developer Intake Form) — join keys: **BBL**, **BIN**, **Project Name**, **Applicant Name**, and bond **Series Name**.

## Next

1. **JSON Schema** per entity, reconciling the real adjacent columns (BBL, BIN, Project Name, Total Units, New Construction/Rehabilitation, Applicant Name; Series Name, par amounts, ratings) and HDC's own program concepts — done ([schemas/](schemas/)).
2. **OpenAPI** consolidating developments + programs + bond issues as clean resources + the net-new `POST /financing-applications` (`applyForFinancing`) and `GET /financing-applications/{id}` (`getFinancingStatus`) — done ([openapi/hdc.yaml](openapi/hdc.yaml)).
3. **MCP** artifact: `find_developments`, `get_development`, `find_financing_programs`, `get_financing_program`, `find_bond_issues`, `get_bond_issue`, `list_my_financing_applications`, `get_financing_status`, `apply_for_financing` — done ([mcp/hdc-mcp.json](mcp/hdc-mcp.json)).
