# NYC Open Data — DVS Datasets

All NYC Open Data assets whose **Dataset-Information_Agency = "Department of Veterans' Services (DVS)"** (verified via the Socrata Discovery API, 2026-07-13). 7 assets, sorted by lifetime page views. Machine-readable: [opendata-dvs.json](opendata-dvs.json).

The shape of the corpus is the story, and DVS is unusual: unlike most NYC agencies, it publishes **its own service-layer analytics** as open data — de-identified assistance requests, cases, client demographics, and historical request processing — alongside two reference directories (the DVS Resource Map and NYC Veteran Owned Businesses). What it does **not** publish, and what has no machine-readable surface at all, is the live intake itself: a **VetConnectNYC** care-coordination referral, which runs on a third-party vendor portal (Combined Arms) and is worked by DVS Care Coordinators by hand. See [crosswalk.md](crosswalk.md).

| Views | Type | ID | Name | Cols |
|--:|---|---|---|--:|
| 2,539 | dataset | `ybdk-jmnn` | NYC Veteran Owned Businesses | 27 |
| 1,231 | dataset | `jup5-7fik` | DVS Assistance Requests | 22 |
| 1,078 | dataset | `davn-rbxj` | Historical Veteran Peer Coordinator (VPC) Program Moves | 15 |
| 831 | dataset | `44f4-mjxy` | Historical DVS Client Requests Received and Processed | 14 |
| 803 | dataset | `af2s-4k4p` | DVS Resource Map | 15 |
| 774 | dataset | `idat-aemv` | Department of Veterans' Services Clients | 12 |
| 668 | dataset | `pw4e-vms3` | Department of Veterans' Services Cases | 9 |

## Groupings

- **Reference directories (VeteranResource / VeteranOwnedBusiness):** DVS Resource Map (`af2s-4k4p`, 15c — the curated directory of veteran-serving resources, keyed on `DVS_RES_ID`), NYC Veteran Owned Businesses (`ybdk-jmnn`, 27c — geocoded business directory with the full NYC geography spine, certifications, also keyed on `DVS_RES_ID`).
- **Service records — de-identified (AssistanceRequest / Case):** DVS Assistance Requests (`jup5-7fik`, 22c — intake records with a `VetConnectNYC (Y/N)` flag, `Referral Made To?`, engagement level/method), DVS Cases (`pw4e-vms3`, 9c — case outcomes, service type/subtype, "Started as Assistance Request", "Case is Referred").
- **Historical service records:** Historical Veteran Peer Coordinator (VPC) Program Moves (`davn-rbxj`, 15c — housing/homelessness service requests and moves), Historical DVS Client Requests Received and Processed (`44f4-mjxy`, 14c — de-identified client requests by category/sub-category).
- **Clients (aggregate / de-identified only):** Department of Veterans' Services Clients (`idat-aemv`, 12c — demographics: service era, branch, discharge type, race/ethnicity, gender, marital status, gross monthly income). No individual veteran record is ever published; the row grain is de-identified counts.

## The one thing missing

There is **no dataset — and no API — for the live referral**. When a veteran fills out the **VetConnectNYC Request Form**, it goes into the **Combined Arms "Military Resource Portal"** (`nyc.veteranportal.combinedarms.us`), where DVS Care Coordinators receive and process it within 3–5 business days. That transaction is the net-new write surface ([service-referral.json](schemas/service-referral.json)); the open datasets above are its downstream, de-identified exhaust.
