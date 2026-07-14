# NYC Open Data — Staten Island DA Datasets

**Zero.** The Socrata Discovery API returns **no assets** for the Office of the District Attorney, Richmond County under any agency label (verified 2026-07-13). Machine-readable: [opendata-statenislandda.json](opendata-statenislandda.json) (an empty array — documented honestly).

## What was checked

Queried `https://api.us.socrata.com/api/catalog/v1` with `--data-urlencode "Dataset-Information_Agency=<LABEL>" --data-urlencode "limit=400"` for every plausible label:

| Agency label tried | Assets |
|---|--:|
| `Richmond County District Attorney` | 0 |
| `District Attorney Richmond County` | 0 |
| `Office of the District Attorney Richmond County` | 0 |
| `Richmond County District Attorney's Office` | 0 |
| `Staten Island District Attorney` | 0 |

A free-text `q=district attorney` search returns 71 datasets, but **none are owned by any DA office** — they are DA *mentions* inside other agencies' data (IBO budget lines, HRA/OTI/DCP reference tables). A NYC-domain-scoped `q=richmond county district attorney` returns 76 spurious keyword hits, again all owned by other agencies (IBO, OTI, NYCHA, DPR, HRA, OPA, DCAS, DCP, SCA).

## The finding

The Staten Island DA has **no Open Data footprint at all** — not one dataset, not one Socrata endpoint. This is the opposite of NYCHA (24 datasets). The office is entirely **off** NYC Open Data, and its public presence is a self-hosted WordPress marketing site (statenislandda.org), not the NYC.gov chassis. The core prosecution data — cases, dispositions, diversions — is **dark**: it lives in an internal case-management system and never reaches the public as structured data. See [crosswalk.md](crosswalk.md) and [tech-stack.md](tech-stack.md).

> Prosecutorial-transparency data (caseloads, declinations, dispositions) is exactly the kind of accountability data a DA's office should publish, and here there is none. The proposed [aggregate prosecution-statistics schema](schemas/prosecution-statistics.json) is a design-first placeholder for data that does not yet exist in any machine-readable form.
