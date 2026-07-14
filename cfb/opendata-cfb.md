# NYC Open Data — Campaign Finance Board (CFB) Datasets

All NYC Open Data assets whose **Dataset-Information_Agency = "Campaign Finance Board (CFB)"** (verified via the Socrata Discovery API, 2026-07-13). 16 assets, sorted by lifetime page views. Machine-readable: [opendata-cfb.json](opendata-cfb.json).

The shape of the corpus is the story: it is **campaign-finance and elections heavy** — contributions, expenditures, intermediaries, public matching-funds payments, and financial analysis, in parallel citywide and off-year/special-election streams — plus voter-analysis/turnout data from the NYC Votes side. But NYC Open Data is only *part* of the CFB's publishing: the same data (and more) is served live by the **Follow the Money Web API** (`nyccfb.info/FTMSearchWebAPI`) and as **bulk per-cycle CSVs** in the CFB Data Library (2001–2025). There is **no dataset for the write/submission layer** — filing a disclosure statement lives only in the C-SMART application. See [crosswalk.md](crosswalk.md).

| Views | Type | ID | Name | Cols |
|--:|---|---|---|--:|
| 4,537 | dataset | `psx2-aqx3` | Voter Analysis 2008-2018 | 175 |
| 3,240 | dataset | `rjkp-yttg` | Campaign Contributions | 54 |
| 2,531 | dataset | `rixx-fc37` | Historical Voter Turnout | 9 |
| 1,787 | dataset | `qxzj-vkn2` | Campaign Expenditures | 32 |
| 1,503 | dataset | `m3tj-a2pb` | Campaign Financial Analysis | 26 |
| 1,207 | dataset | `xrxs-qn95` | Enforcement Actions Board Determinations and Penalties | 6 |
| 1,050 | dataset | `u69g-mvrb` | Campaign Public Funds Payments | 12 |
| 981 | dataset | `tcwb-nry3` | Campaign Intermediaries | 24 |
| 916 | dataset | `x4w5-m7uh` | Enforcement Audit Determinations | 16 |
| 909 | dataset | `fbkk-n4e3` | Doing Business Contributions Summary | 52 |
| 811 | dataset | `yqhh-93zq` | Off-Year and Special Elections Intermediary | 24 |
| 722 | dataset | `kgzj-pjna` | Off-Year and Special Elections Contribution | 52 |
| 646 | dataset | `cgcg-w2ys` | Off-Year and Special Elections Campaign Expenditure | 32 |
| 628 | dataset | `7f4s-uwi7` | Off-Year and Special Elections Public Matching Fund Payments | 12 |
| 552 | dataset | `ups9-zwkm` | Off-Year and Special Elections Financial Analysis | 26 |
| 552 | dataset | `2ujk-6z7u` | Late/Missing Disclosure Statements | 6 |

## Groupings

- **Contributions & bundling:** Campaign Contributions (`rjkp-yttg`, 54c) + off-year (`kgzj-pjna`), Campaign Intermediaries (`tcwb-nry3`) + off-year (`yqhh-93zq`), Doing Business Contributions Summary (`fbkk-n4e3`, 52c).
- **Expenditures:** Campaign Expenditures (`qxzj-vkn2`, 32c) + off-year (`cgcg-w2ys`).
- **Public matching funds:** Campaign Public Funds Payments (`u69g-mvrb`) + off-year (`7f4s-uwi7`).
- **Candidate / campaign analysis:** Campaign Financial Analysis (`m3tj-a2pb`, 26c) + off-year (`ups9-zwkm`).
- **Compliance & enforcement:** Late/Missing Disclosure Statements (`2ujk-6z7u`), Enforcement Actions — Board Determinations and Penalties (`xrxs-qn95`), Enforcement Audit Determinations (`x4w5-m7uh`).
- **Voters / NYC Votes:** Voter Analysis 2008–2018 (`psx2-aqx3`, 175c), Historical Voter Turnout (`rixx-fc37`).

## Beyond Open Data

- **Follow the Money Web API** — `nyccfb.info/FTMSearchWebAPI` (ASP.NET Web API) returns live JSON for election cycles, offices, contributor/candidate/payee typeaheads, and search. Real and working, but undocumented and backend-only. See [apis-observed.md](apis-observed.md).
- **Data Library** — 56 bulk CSV files under `/DataLibrary/` (contribution, expenditure, payment, intermediary, analysis) per election cycle from **2001 through 2025**.
- **C-SMART** — the login-walled web application campaigns use to *submit* disclosure statements. This is the net-new write surface with no public API.
