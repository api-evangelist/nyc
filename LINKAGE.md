# Cross-Domain Linkage

The join keys that connect agencies — the basis for `nyc-commons` and cross-domain interoperability. Detected in each domain's JSON Schemas. Interactive: [linkage.html](https://nyc.apievangelist.com/linkage.html).

## Shared keys, by reach

| Key | Category | # domains |
|--|--|--|
| `Borough` | geography | 70 |
| `Coordinates (lat/long)` | geography | 70 |
| `BBL` | property | 23 |
| `BIN` | property | 23 |
| `Community Board` | geography | 17 |
| `Council District` | geography | 17 |
| `Census Tract` | geography | 9 |
| `NTA (neighborhood)` | geography | 9 |
| `Police Precinct` | geography | 5 |
| `GISPropNum` | property | 2 |
| `DBN (school)` | identity | 2 |
| `Matter ID (Legistar)` | identity | 2 |
| `Election District` | identity | 2 |
| `Council Member ID` | identity | 1 |

## The property spine (BBL/BIN — the strongest connectors)

- **BBL** (23): NYC Standards & Appeals (BSA), NYC Citywide Admin Services (DCAS), NYC City Planning (DCP), NYC Environmental Protection (DEP), NYC Homeless Services (DHS), NYC Buildings (DOB), NYC Finance (DOF), NYC Health (DOHMH), NYC Economic Development (EDC), NYC Fire (FDNY), NYC Housing Development Corp (HDC), NYC Housing (HPD), NYC Law Department, NYC Landmarks (LPC), Manhattan District Attorney, NYC Environmental Remediation (OER), NYC Emergency Management (NYCEM), NYPD, NYC Technology & Innovation (OTI), NYC Public Design Commission (PDC), NYC Public Advocate, NYC School Construction Authority (SCA), NYC Tax Commission
- **BIN** (23): NYC Standards & Appeals (BSA), NYC Citywide Admin Services (DCAS), NYC Cultural Affairs (DCLA), NYC City Planning (DCP), NYC Homeless Services (DHS), NYC Buildings (DOB), NYC Finance (DOF), NYC Health (DOHMH), NYC Transportation (DOT), NYC Sanitation (DSNY), NYC Economic Development (EDC), NYC Fire (FDNY), NYC Housing Development Corp (HDC), NYC Housing (HPD), NYC Landmarks (LPC), Manhattan District Attorney, NYC Environmental Remediation (OER), NYC Emergency Management (NYCEM), NYC Housing Authority (NYCHA), NYPD, NYC Technology & Innovation (OTI), NYC Public Advocate, NYC School Construction Authority (SCA)
- **GISPropNum** (2): NYC City Planning (DCP), NYC Parks & Recreation
