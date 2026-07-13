# NYC Open Data — DOC Datasets

All NYC Open Data assets whose **Dataset-Information_Agency = "Department of Correction (DOC)"** (verified via the Socrata Discovery API, 2026-07-13). 15 assets, sorted by lifetime page views. Machine-readable: [opendata-doc.json](opendata-doc.json).

The shape of the corpus is the story: it is **accountability heavy** — one dominant daily in-custody snapshot, plus admissions/discharges, deaths, and five more parallel safety/security incident streams (slashings, stabbings, fights, assaults on staff, staff injuries, lock-ins), Local Law 33/85 security and visitation indicators, and staffing rollups. There is **no dataset for the live person-in-custody lookup** (that runs as a JSF web app at `a073-ils-web.nyc.gov`) and **no dataset for the resident-facing transactions** — scheduling a visit or filing a complaint/records request. See [crosswalk.md](crosswalk.md).

| Views | Type | ID | Name | Cols |
|--:|---|---|---|--:|
| 98,188 | dataset | `7479-ugqb` | Daily Inmates In Custody | 13 |
| 10,663 | dataset | `f64t-5yiv` | Inmate Deaths | 4 |
| 9,066 | dataset | `6teu-xtgp` | Inmate Admissions | 7 |
| 8,140 | dataset | `94ri-3ium` | Inmate Discharges | 8 |
| 6,249 | dataset | `f5mc-f3zp` | DOC Hart Island Burial Records | 5 |
| 4,909 | dataset | `gakf-suji` | Inmate Incidents - Slashing and Stabbing | 4 |
| 3,878 | dataset | `eddp-3v5g` | Aggregate Employee Statistics | 4 |
| 3,389 | dataset | `k548-32d3` | Inmate Incidents - Inmate Fights | 3 |
| 3,306 | dataset | `erra-pzy8` | Inmate Assault on Staff | 5 |
| 2,429 | dataset | `2wuc-x56b` | Local Law 33 - Security Indicators Report | 6 |
| 1,623 | dataset | `7hi3-kaps` | Staff Injuries - Class A Injuries | 5 |
| 995 | dataset | `b3eu-nmy6` | Local Law 85 – Visitation Quarterly | 5 |
| 583 | dataset | `9dab-x6kn` | Emergency Lock-In Data | 12 |
| 500 | dataset | `5n4h-km5r` | Medical Non-production for Clinic Appointments | 11 |
| 389 | dataset | `q9w2-yi4x` | Article 730 Transfer Waitlist | 7 |

## Groupings

- **People in custody:** Daily Inmates In Custody (`7479-ugqb`, 13c) — the dominant dataset — plus Inmate Admissions (`6teu-xtgp`) and Inmate Discharges (`94ri-3ium`). Anonymized per-person rows keyed on `INMATEID`.
- **Safety & security incidents:** Inmate Deaths (`f64t-5yiv`), Slashing and Stabbing (`gakf-suji`), Inmate Fights (`k548-32d3`), Assault on Staff (`erra-pzy8`), Staff Injuries - Class A (`7hi3-kaps`), Emergency Lock-In Data (`9dab-x6kn`, 12c) — parallel incident streams keyed on `INCIDENT_ID` per facility.
- **Population & indicators:** Local Law 33 - Security Indicators Report (`2wuc-x56b`, rate per 100 ADP), Article 730 Transfer Waitlist (`q9w2-yi4x`), Medical Non-production for Clinic Appointments (`5n4h-km5r`, 11c), Local Law 85 – Visitation Quarterly (`b3eu-nmy6`, aggregate).
- **Workforce:** Aggregate Employee Statistics (`eddp-3v5g`) — rank/gender/leave-status rollups.
- **Other:** DOC Hart Island Burial Records (`f5mc-f3zp`) — DOC-administered public burial records.
