# NYC Open Data — Office of the City Clerk Datasets

All NYC Open Data assets whose **Dataset-Information_Agency = "Office of the City Clerk (OCC)"** (verified via the Socrata Discovery API, 2026-07-13). **2 assets**, sorted by lifetime page views. Machine-readable: [opendata-cityclerk.json](opendata-cityclerk.json).

The shape of the corpus is the story: it is **entirely lobbying**. Both City Clerk datasets come out of the Lobbying Bureau's e-Lobbyist filing system — periodic lobbying reports and lobbyist fundraising/political-consulting reports. There is **no dataset for the Marriage Bureau** — no marriage licenses, ceremonies, or applications. The only marriage data on Open Data is published by a different agency, **DORIS** (Department of Records & Information Services), and only as *historical* vital-records indexes (`j62e-7maa`, `d8dr-nyhw`). The live marriage side lives only inside Project Cupid. See [crosswalk.md](crosswalk.md).

| Views | Type | ID | Name | Cols |
|--:|---|---|---|--:|
| 6,589 | dataset | `fmf3-knd8` | City Clerk eLobbyist Data | 28 |
| 993 | dataset | `7arw-dbem` | Lobbyists' Fundraising and Political Consulting Reports | 24 |

## Groupings

- **Lobbying — periodic filings:** City Clerk eLobbyist Data (`fmf3-knd8`, 28c) — lobbyist/client identity (`LOBBYIST_ID`, `CLIENT_ID`, `REGISTRATION_ID`), reporting period, compensation and expense totals, activities, and targets.
- **Lobbying — fundraising / political consulting:** Lobbyists' Fundraising and Political Consulting Reports (`7arw-dbem`, 24c) — reporting entity, candidate, target office, amounts raised and spent.

## Not the City Clerk's (but adjacent)

- **Marriage records** — only DORIS publishes them, as historical indexes: NYC Historical Vital Records Index to Digitized Marriage Certificates (`j62e-7maa`) and Marriage Licenses (`d8dr-nyhw`). These are archival, not the live Marriage Bureau record.
