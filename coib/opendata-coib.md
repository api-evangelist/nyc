# NYC Open Data — COIB Datasets

All NYC Open Data assets whose **Dataset-Information_Agency = "Conflicts of Interest Board (COIB)"** (verified via the Socrata Discovery API, 2026-07-13). 8 assets, sorted by lifetime page views. Machine-readable: [opendata-coib.json](opendata-coib.json).

The shape of the corpus is the story: it is **transparency-and-enforcement heavy** — enforcement fines, three donation streams, the policymakers list, and three legal-defense-trust streams. There is **no dataset for the compliance input** (the annual financial disclosure filing, ethics training, waivers, or advisory opinions); the filing lives only in the login-gated COIB filing website. See [crosswalk.md](crosswalk.md).

| Views | Type | ID | Name | Cols |
|--:|---|---|---|--:|
| 5,278 | dataset | `p39r-nm7f` | Enforcement Fines | 13 |
| 2,969 | dataset | `dx8z-6nev` | Donations to Not-for-Profit Organizations Affiliated with Elected Officials | 12 |
| 2,285 | dataset | `aqs7-v55z` | Donations Received by City Agencies | 5 |
| 1,748 | dataset | `wf8t-6cqt` | Policymakers List | 7 |
| 714 | dataset | `basd-2jwn` | Official Fundraising by City Agencies | 3 |
| 474 | dataset | `mhyv-6iza` | Legal Defense Trust Expenditures | 20 |
| 309 | dataset | `jsiv-zh9r` | Legal Defense Trust Donations | 10 |
| 264 | dataset | `t3pj-3dgu` | Legal Defense Trust Refunded Donations | 11 |

## Groupings

- **Enforcement:** Enforcement Fines (`p39r-nm7f`, 13c) — resolved cases with fine paid to COIB / to agency / imposed-but-unpaid, other penalties, suspension days, and a narrative explanation. COIB's most-viewed asset.
- **Donations / transparency:** Donations to Not-for-Profit Organizations Affiliated with Elected Officials (`dx8z-6nev`, 12c), Donations Received by City Agencies (`aqs7-v55z`, 5c), Official Fundraising by City Agencies (`basd-2jwn`, 3c).
- **Policymakers:** Policymakers List (`wf8t-6cqt`, 7c) — the monthly designation list that triggers the annual disclosure obligation.
- **Legal defense trusts:** Expenditures (`mhyv-6iza`, 20c — the only COIB dataset with the full geography spine), Donations (`jsiv-zh9r`, 10c), Refunded Donations (`t3pj-3dgu`, 11c).

## What is *not* here

- **No financial disclosure filings.** The annual disclosure reports themselves are never published as data — confidential except for elected officials, whose reports are released only as PDFs on request.
- **No advisory opinions, ethics training, or waivers.** These are published as PDFs or handled through login-only/email workflows with no machine-readable index.

All 8 assets are categorized **City Government** on NYC Open Data.
