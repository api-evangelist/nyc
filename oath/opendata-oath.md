# NYC Open Data — OATH Datasets

All NYC Open Data assets whose **Dataset-Information_Agency = "Office of Administrative Trials and Hearings (OATH)"** (verified via the Socrata Discovery API, 2026-07-13). 2 assets, sorted by lifetime page views. Machine-readable: [opendata-oath.json](opendata-oath.json).

The shape of the corpus is the story: it is **narrow but deep**. There are only two datasets, but the flagship — the Hearings Division Case Status — is one of the largest, most-viewed, and most-frequently-updated files in all of NYC Open Data (74 columns, refreshed **daily**, ~400k lifetime views), publishing essentially the entire ECB summons docket. There is **no dataset for the respondent service layer** (looking up and responding to / disputing a summons); that lives only in the legacy Apache Struts ECB Ticket Finder portal. See [crosswalk.md](crosswalk.md).

| Views | Type | ID | Name | Cols |
|--:|---|---|---|--:|
| 400,366 | dataset | `jz4z-kudi` | OATH Hearings Division Case Status | 74 |
| 11,971 | dataset | `y3hw-z6bm` | OATH Trials Division Case Status | 16 |

## The two datasets

### `jz4z-kudi` — OATH Hearings Division Case Status (74 columns, daily)

The ECB summons docket. Every summons OATH's Hearings Division adjudicates, with:

- **Identity & issuer:** Ticket Number, Issuing Agency, Violation Description, Violation Details, Violation Date/Time.
- **Charges (up to 10 parallel sets):** Charge #1–#10 Code, Code Section, Code Description, Infraction Amount.
- **Respondent:** Respondent Last Name, Respondent Address (House #, Zip Code, Borough), Respondent Address or Facility Number (For FDNY and DOB Tickets).
- **Violation location (tax-lot spine):** House #, Street Name, City, State Name, Zip Code, Borough, Floor, Block No., Lot No.
- **Hearing:** Hearing Date, Hearing Time, Hearing Status, Scheduled Hearing Location, Hearing Result.
- **Decision & money:** Decision Date, Decision Location (Borough), Penalty Imposed, Additional Penalties or Late Fees, Total Violation Amount, Paid Amount, Balance Due, Date Judgment Docketed, Compliance Status.

### `y3hw-z6bm` — OATH Trials Division Case Status (16 columns, monthly)

The tribunal side — formal adjudications referred by other agencies: Case Number, Name, Filing Agency Case ID, Type, Category, Subcategory, Premises, Opened, Original Conference, Original Trial Date, Trial Concluded, Report Issued, Dispo Code, Agency Head Decision, Appeal Action Date, Record Closed.

## Groupings

- **ECB summons adjudication (Hearings Division):** `jz4z-kudi` — the summons, its charges, hearing, decision, penalty, and balance.
- **Tribunal adjudication (Trials Division):** `y3hw-z6bm` — agency disciplinary/licensing cases.
- **Respondent service layer (no dataset):** looking up and **responding to / disputing** a summons lives only in the ECB Ticket Finder portal — the net-new write surface.
