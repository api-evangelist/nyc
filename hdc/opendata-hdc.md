# NYC Open Data — HDC Datasets

All NYC Open Data assets whose owning agency is the **New York City Housing Development Corporation (HDC)** (verified via the Socrata Discovery API, 2026-07-16). The count is the story: **zero.** Machine-readable: [opendata-hdc.json](opendata-hdc.json).

Filtering `data.cityofnewyork.us` for an attribution/agency of *Housing Development Corporation* returns **0 assets**. HDC — one of the nation's largest municipal affordable-housing bond issuers — **publishes no Open Data of its own and exposes no API**. This is thinner than [DDC](../ddc/) (which at least owns four Socrata datasets): HDC owns none.

Its machine-readable record instead lives entirely on **systems it does not own**:

| Views/role | Type | ID | Name | Owner | Cols |
|---|---|---|---|---|--:|
| HDC's deals | dataset | `p8i7-ix2s` | LIHTC Awarded by HPD: Project-Level (4% Awards) | **HPD** | 26 |
| HDC's deals | dataset | `h9ws-rfd9` | LIHTC Awarded by HPD: Building-Level (4% Awards) | **HPD** | 3 |
| adjacent | dataset | `frre-6z6q` | LIHTC Awarded by HPD: Project-Level (9% Awards) | **HPD** | 26 |
| adjacent | dataset | `kmtx-45c9` | LIHTC Awarded by HPD: Building-Level (9% Awards) | **HPD** | 3 |
| HDC as a value | dataset | `n5n4-5k5r` | Debt Issuance by Issuer | **OMB** | 7 |

## Where HDC's record actually lives

- **HPD's LIHTC award datasets are HDC's development record.** HPD's own dataset description is explicit: it allocates 4% Low-Income Housing Tax Credits "to projects receiving tax exempt bonds through New York City Housing Development Corporation." So the **4% awards** (`p8i7-ix2s`, `h9ws-rfd9`) *are* the deals HDC bond-financed — but they are published under the **HPD** label, keyed on **BBL/BIN**, with Project Name, Total Units, borough, construction/rehab, and the developer as `Applicant Name`. The 9% awards are HPD's own competitive credits (not bond-financed) and are included only as adjacent context.
- **OMB owns the debt trace.** The only City open-data record of HDC's bonds is OMB's **Debt Issuance by Issuer** (`n5n4-5k5r`), where HDC is merely one **`Issuer Name`** value among many, with Series Name, Issue Date, and tax-exempt/taxable par amounts.
- **Investor disclosure is federal, not City.** HDC's Official Statements, combined financial statements, and Sustainable Development Bond annual reports are disclosed on the **MSRB EMMA** platform (`emma.msrb.org`) as PDFs — a federal system, outside NYC Open Data entirely.

## What is missing

- **No HDC dataset of any kind** — not for developments, programs, term sheets, bonds, or borrowers.
- **No program/term-sheet catalog** — New Construction, ELLA, Mix and Match, Preservation, and PACT Preservation exist only as HTML pages and PDF term sheets.
- **No developer-intake data** — the Developer Intake Portal is the one HDC-owned transaction, and it emits nothing machine-readable.
- **No live pipeline** — even the HPD LIHTC datasets are annual, after-the-fact award records, not a live financing pipeline.
