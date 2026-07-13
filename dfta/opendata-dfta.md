# NYC Open Data — NYC Aging (DFTA) Datasets

All NYC Open Data assets whose **Dataset-Information_Agency = "Department for the Aging (NYC Aging)"** (verified via the Socrata Discovery API, 2026-07-13). 11 assets, sorted by lifetime page views. Machine-readable: [opendata-dfta.json](opendata-dfta.json).

The shape of the corpus is the story: it is **provider- and contract-centric** — who the funded providers are, where their public sites are, what senior centers do (Local Law 140), what activities they run, and the budgeted-vs-reported service units and expenditures behind them — plus aggregate participation. There is **no dataset for the intake/referral service layer** (connecting an older adult to case management, meals, benefits, or center enrollment); that lives only in the phone-based Aging Connect information-and-referral center. See [crosswalk.md](crosswalk.md).

| Views | Type | ID | Name | Cols |
|--:|---|---|---|--:|
| 6,477 | dataset | `32cj-z7va` | Department for the Aging (NYC Aging) - Social Adult Day Care Services | 33 |
| 5,089 | dataset | `cqc8-am9x` | Department for the Aging (NYC Aging) - All Contracted Providers | 38 |
| 2,169 | dataset | `ygfr-ij6t` | Senior Center Local Law 140 Provider Data - FY 2020 | 49 |
| 1,421 | dataset | `u845-acue` | Department for the Aging (NYC Aging) - Bottom Line Budget | 7 |
| 1,308 | dataset | `hm83-bdp7` | Senior Center Local Law 140 Client Data - FY 2020 | 12 |
| 1,159 | dataset | `exaw-9qnu` | Department for the Aging (NYC Aging) - Reported Service Units | 10 |
| 1,129 | dataset | `u7wp-np5k` | List of NYC Aging Providers with Sites Open to the Public | 21 |
| 804 | dataset | `nxrs-2ci5` | Department for the Aging (NYC Aging) - Budgeted Services | 8 |
| 759 | dataset | `tt8e-a9vn` | Department for the Aging (NYC Aging) - Reported Expenditures | 9 |
| 678 | dataset | `fzy4-e84j` | Older Adult Center (OAC) Activities | 26 |
| 564 | dataset | `2td3-mfek` | Number of Participants in NYC Aging funded Programs | 18 |

## Groupings

- **Provider network / directory:** All Contracted Providers (`cqc8-am9x`, 38c), List of Providers with Sites Open to the Public (`u7wp-np5k`, 21c), Social Adult Day Care Services (`32cj-z7va`, 33c). Provider types include Older Adult Center, Case Management, Home-Delivered Meal, Caregiver, Homecare, NORC, Elder Abuse, Geriatric Mental Health, Legal, Transportation, and New York Connects.
- **Older adult centers (senior centers, Local Law 140):** Senior Center LL140 Provider Data (`ygfr-ij6t`, 49c) + Client Data (`hm83-bdp7`) — utilization, meals, staffing, budget/expenditures.
- **Activities:** Older Adult Center (OAC) Activities (`fzy4-e84j`, 26c) — events, classes, virtual/in-person programming.
- **Contract budget & performance:** Bottom Line Budget (`u845-acue`), Budgeted Services (`nxrs-2ci5`), Reported Service Units (`exaw-9qnu`), Reported Expenditures (`tt8e-a9vn`).
- **Participation (aggregate only):** Number of Participants in NYC Aging funded Programs (`2td3-mfek`, 18c) — unduplicated client counts, never an individual older adult.
