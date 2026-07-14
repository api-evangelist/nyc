# NYC Open Data — MOME Datasets

All NYC Open Data assets whose **Dataset-Information_Agency = "Mayor's Office of Media And Entertainment (MOME)"** (verified via the Socrata Discovery API, 2026-07-13 — note the label capitalizes "And"). Just **2 assets**, sorted by lifetime page views. Machine-readable: [opendata-mome.json](opendata-mome.json).

The shape of the corpus is the story: MOME publishes almost nothing *except* the one thing that matters, and it publishes it heroically. **Film Permits** (`tg4x-b46p`) is one of the most-viewed datasets in the entire NYC Open Data catalog (~530k lifetime views), automated and updated **daily** — every location shoot the Film Office greenlights, as a public record. The only other MOME-labeled asset is the nightlife-enforcement **MARCH Inspections** log. There is **no dataset for the permit *application*** — the intake workflow lives only in the login-walled "MOME E-Apply" event-permit portal. See [crosswalk.md](crosswalk.md).

| Views | Type | ID | Name | Cols |
|--:|---|---|---|--:|
| 530,471 | dataset | `tg4x-b46p` | Film Permits | 14 |
| 1,534 | dataset | `b84a-xy2t` | Multi Agency Response to Community Hotspot (MARCH) Inspections | 35 |

## Film Permits (`tg4x-b46p`) — the flagship

The famous dataset. One row per issued permit event, keyed on **`EventID`**, joined to the citywide geography spine (borough, community board, police precinct, ZIP) and typed by production **`Category`** / **`SubCategoryName`**:

- **Identity & timing:** `EventID`, `EventType` (Shooting Permit, Theater Load in and Load Out, Rigging Permit, DCAS Prep/Shoot/Wrap Permit), `StartDateTime`, `EndDateTime`, `EnteredOn`, `EventAgency`.
- **Where (ScreenActivity / held location):** `ParkingHeld` (the exact street segments reserved), `Borough`, `CommunityBoard(s)`, `PolicePrecinct(s)`, `ZipCode(s)`, `Country`.
- **What (production type):** `Category` (Film, Television, Commercial, Still Photography, WEB, Music Video, Theater, Documentary, Student), `SubCategoryName` (Feature, Episodic series, Cable-episodic, Signed Not Aired, etc.).

Notably absent: the **applicant / production company**, the fee, and lat/long — the permit is published as a public geography record, not as an application file.

## MARCH Inspections (`b84a-xy2t`)

The Multi-Agency Response to Community Hotspots log — joint NYPD/FDNY/DOB/DOHMH/DEP inspections of nightlife establishments. Sits under the MOME label because MOME runs the **Office of Nightlife**. One row per inspection: precinct, borough, council district, ZIP, duration, whether the establishment was closed, inspectors present and summonses issued per agency, and the conduct/complaint that triggered the operation.

## Related (other agencies' labels)

The film-permit story spills across agency labels — several high-traffic datasets describe the same permits from a different owner's angle:

- **Filming Permits – Transportation Department** (`c2az-nhru`, ~90k views) + its map (`k3tc-fe6r`) — DOT's street-work view of film permits, with applicant contacts, fees, milestones, and lat/long.
- **NYC Permitted Event Information** (`tvpp-9vvx`) + Historical (`bkfu-528j`) — the Office of Citywide Event Coordination and Management (CECM) feed that shares the same `nyceventpermits.nyc.gov` platform.
- **Number of Film Partnerships and Permits – Department KPI** (`bxm5-b7zs`) — a MOME KPI rollup.
