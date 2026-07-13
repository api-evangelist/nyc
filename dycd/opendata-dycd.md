# NYC Open Data — DYCD Datasets

All NYC Open Data assets whose **Dataset-Information_Agency = "Department of Youth and Community Development (DYCD)"** (verified via the Socrata Discovery API, 2026-07-13). 15 assets, sorted by lifetime page views. Machine-readable: [opendata-dycd.json](opendata-dycd.json).

The shape of the corpus is the story: it is **supply-side and provider-heavy** — DYCD is a *funder/intermediary* that contracts hundreds of community-based organizations to run programs at physical sites, and the data documents that supply chain: **program sites** (`ebkm-iyma`, 34 columns, the richest asset), **contracts** (`graj-69em`), **contractors/providers** (`75e9-fg2t`), **Neighborhood Development Areas** (`vd7c-qjsx` + map), and aggregate **participant demographics** (`k9kq-67vm`, 52 columns). What is **not** here is a clean catalog of the program *offerings* themselves (SYEP, COMPASS, Beacon, SONYC) — that lives inside the **DiscoverDYCD** program-finder app — and there is **no dataset for applying** to a program. See [crosswalk.md](crosswalk.md).

| Views | Type | ID | Name | Cols |
|--:|---|---|---|--:|
| 6,401 | dataset | `ebkm-iyma` | DYCD Program Sites | 34 |
| 4,408 | dataset | `75e9-fg2t` | DYCD Contractors | 5 |
| 4,359 | dataset | `graj-69em` | Department of Youth and Community Development (DYCD) Contracts | 15 |
| 4,121 | map | `p57r-4v4f` | Neighborhood Development Areas Map | 0 |
| 2,951 | dataset | `vd7c-qjsx` | Neighborhood Development Areas | 3 |
| 2,183 | dataset | `5rw7-99k7` | Runaway and Homeless Youth (RHY) Daily Census | 5 |
| 2,100 | dataset | `qx6a-vcwx` | Youth Count | 9 |
| 1,500 | dataset | `x4x8-m3ds` | Summer Youth Employment Program (SYEP) for NYCHA Residents by Borough - Local Law 163 | 8 |
| 1,492 | dataset | `acek-a5z6` | Summer Youth Employment Program (SYEP) for NYCHA Residents by NYCHA development - Local Law 163 | 8 |
| 1,462 | dataset | `9f5n-qdib` | Evaluation and Monitoring Reports for Program Sites | 22 |
| 1,412 | dataset | `73rz-5b7x` | Summer Youth Employment Program (SYEP) for NYCHA Residents by Council District - Local Law 163 | 8 |
| 1,260 | dataset | `39et-rijq` | DYCD Runaway and Homeless Youth (RHY) Demographics and Services (Local Law 86) | 7 |
| 1,045 | dataset | `tg2n-zp58` | Runaway and Homeless Youth (RHY) Shelter Access Report (Local Law 79) | 3 |
| 685 | dataset | `denm-3mvn` | Runaway and Homeless Youth (RHY) Streamlined Referrals (Local Law 81) | 4 |
| 282 | dataset | `k9kq-67vm` | DYCD Participant Demographics | 52 |

## Groupings

- **Program sites (the core supply unit):** DYCD Program Sites (`ebkm-iyma`, 34c) — every funded site with provider, program area/type, service category, slots, participants, and a full NYC geography spine (BBL/BIN, council/community district, NTA, census tract, NDA, lat/long).
- **Providers & contracts:** DYCD Contractors (`75e9-fg2t`), DYCD Contracts (`graj-69em`, 15c — provider, major program, solicitation, funded amounts, registration).
- **Service geography:** Neighborhood Development Areas (`vd7c-qjsx`) + map (`p57r-4v4f`) — the community-district-level catchments for community-development programs.
- **Participants (aggregate only):** DYCD Participant Demographics (`k9kq-67vm`, 52c) — race/ethnicity and gender-identity counts and percentages by geography/program type. No individual participant is ever published.
- **Runaway & Homeless Youth (RHY) reporting:** Daily Census (`5rw7-99k7`), Demographics & Services / LL86 (`39et-rijq`), Shelter Access / LL79 (`tg2n-zp58`), Streamlined Referrals / LL81 (`denm-3mvn`), Youth Count (`qx6a-vcwx`).
- **SYEP for NYCHA residents (Local Law 163):** by borough (`x4x8-m3ds`), by NYCHA development (`acek-a5z6`), by council district (`73rz-5b7x`).
- **Oversight:** Evaluation and Monitoring Reports for Program Sites (`9f5n-qdib`, 22c) — site ratings and workscope.
