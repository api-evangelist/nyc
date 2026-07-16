# Crosswalk — Website/System Fruit ↔ APIs ↔ NYC Open Data (HDC)

Maps the low-hanging fruit on **nychdc.com** and HDC's financing flow to (a) the **existing APIs** (none owned; HPD/OMB Socrata; the federal MSRB EMMA disclosure platform) and (b) the **datasets that carry HDC's record but belong to other agencies**. Built 2026-07-16 from [fruit.json](fruit.json) × [opendata-hdc.json](opendata-hdc.json).

## The reframe — a new distinct pattern

- **DDC:** a vendor-facing agency whose own data is thin/historical and whose transactions run on citywide systems it doesn't own → *surface.*
- **LPC:** open landmark data scattered across three vendor silos, no owned API, write locked in Salesforce → *bind.*
- **HDC:** a **bond financier** that owns **no Open Data and no API at all** — its development record is **HPD's**, its debt trace is **OMB's**, its investor disclosure is the **federal MSRB's (EMMA)**, and the one transaction it owns (Developer Intake) has no API → **originate** an owned contract where none exists.

HDC is the financier inversion. There is no citizen and no citizen transaction — HDC lends to developers and borrows from bond investors. It publishes **zero** datasets. The record of what it finances is published by **HPD** (the LIHTC 4% awards); the record of its borrowing is published by **OMB** (Debt Issuance by Issuer) and disclosed to investors on **federal EMMA**; the programs a developer would apply to are **PDF term sheets**. A developer or agent asking "what HDC programs fit a 60%-AMI new-construction deal in the Bronx, and how do I apply?" has **no HDC API to call** — only PDFs and an intake portal.

Coverage: ✅ open twin (even if another agency owns it) · 🟡 partial/derived/documents-only · ❌ gap (no API).

## Entity crosswalk

| Entity | Website / System | API today | Open Data | Cov. |
|---|---|---|---|---|
| `Development` | `/develop` | HPD SODA (not HDC's) | HPD LIHTC 4% Project-Level (`p8i7-ix2s`, 26c); Building-Level (`h9ws-rfd9`, 3c) | 🟡 HPD-owned |
| `FinancingProgram` (term sheet) | `/develop` | — | none (PDF term sheets only) | ❌ gap (documents) |
| `BondIssue` | `/invest` (Debt Issuance) | federal EMMA (documents) | OMB Debt Issuance by Issuer (`n5n4-5k5r`, 7c — HDC as an `Issuer Name` value) | 🟡 OMB/federal |
| `Borrower` (developer) | `/develop` | — | derived from HPD LIHTC `Applicant Name` | 🟡 derived |
| **`FinancingApplication`** (apply for financing) | HDC Developer Intake Portal | **Portal UI only** | — | ❌ **net-new** (B2G; no citizen write exists) |

## The mismatch, concretely

| Source | Strength | Weakness |
|---|---|---|
| **HPD LIHTC 4% datasets** (`p8i7-ix2s`, `h9ws-rfd9`) | Open, machine-readable, BBL/BIN-keyed; the real record of HDC-financed developments | **Owned by HPD, not HDC**; annual after-the-fact award records, not a live pipeline; the HDC financing structure (program, bond series, subsidy) is absent |
| **OMB Debt Issuance by Issuer** (`n5n4-5k5r`) | Open; shows HDC's issuance (par amounts, series, dates) | **Owned by OMB**; HDC is just one `Issuer Name` value; no link to the developments the debt funds |
| **MSRB EMMA** | Authoritative investor disclosure (Official Statements, financials, SDB reports) | **Federal, document-based**; PDFs, not data; not a City surface at all |
| **HDC Developer Intake Portal / term sheets** | The real developer-facing surfaces HDC owns | Portal is UI-only with no API; programs are **PDF** term sheets; nothing machine-readable |

## Implications for the API-first + MCP proposal

1. **Originate an owned contract.** Present HDC-financed developments, financing programs (from the term sheets), and bond issues behind one owned HDC contract ([OpenAPI](openapi/hdc.yaml)) — keyed on **BBL** — instead of an HPD dataset, an OMB dataset, and a pile of federal EMMA PDFs.
2. **Turn term sheets into a program catalog.** The New Construction / ELLA / Mix and Match / Preservation / PACT programs should be structured, queryable `FinancingProgram` resources, not PDFs.
3. **Add the one net-new write workflow** — `apply_for_financing` (the Developer Intake Form), fronting the Developer Intake Portal. Be honest: this is **B2G/developer**; there is **no citizen write** in this domain, and submission does not indicate acceptance.
4. **Name the ownership gap.** The finding is that HDC owns neither its data nor its disclosure surface — its development record is HPD's, its debt OMB's/federal EMMA's — so modernization here is as much about *reclaiming ownership* of HDC's own record as about publishing.
5. **MCP server** so an agent can answer "which HDC programs fit a 60%-AMI new-construction deal?", "what SDB series has HDC issued and at what rating?", and — the point — "start a Developer Intake for my project."
