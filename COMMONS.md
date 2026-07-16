# nyc-commons — the shared schema set

*One canonical definition of a borough, a BBL, an address, a place, a party, and a dollar — for all of NYC government.*

Full schema set and rationale: [`nyc-commons/`](nyc-commons/README.md). Interactive: **[nyc.apievangelist.com/commons.html](https://nyc.apievangelist.com/commons.html)**.

## The problem it solves

Across the 70 domain assessments the same objects were re-declared per agency — **Borough in all 70**, Coordinates in all 70, a geography spine in 59. `nyc-commons` factors them into 21 canonical definitions across 5 files, `$ref`'d from [DCP](dcp/README.md) as the authoritative source, and **every consumer domain is now migrated to reference them**. Two records that resolve to the same `BBL` are provably about the same place.

## Adoption — canonical definitions and how many domains declare a local equivalent

| Definition | File | Domains declaring | Migrated to `$ref` |
|---|---|---:|---:|
| `Borough` | `geography.json` | 70 | 69 |
| `Coordinates` | `geography.json` | 70 | 69 |
| `GeographySpine` | `geography.json` | 59 | 58 |
| `Address` | `address.json` | 16 | 16 |
| `MoneyUSD` | `money.json` | 15 | 15 |
| `ContactPoint` | `party.json` | 8 | 1 |
| `BoroCode` | `geography.json` | 7 | 6 |
| `BBL` | `identifiers.json` | 7 | 3 |
| `PartyReference` | `party.json` | 7 | 1 |
| `AgencyReference` | `party.json` | 7 | 6 |
| `OrganizationReference` | `party.json` | 6 | 1 |
| `FiscalYear` | `money.json` | 5 | 5 |
| `CommunityDistrict` | `geography.json` | 4 | 0 |
| `AdminBoundaries` | `geography.json` | 4 | 4 |
| `BIN` | `identifiers.json` | 3 | 2 |
| `CouncilDistrict` | `geography.json` | 1 | 0 |
| `CensusTract` | `geography.json` | 1 | 0 |
| `NTA` | `geography.json` | 1 | 0 |
| `DBN` | `identifiers.json` | 1 | 1 |
| `FiscalPeriod` | `money.json` | 1 | 0 |
| `GISPropNum` | `identifiers.json` | 0 | 0 |

**Migration status: complete.** All **69 consumer domains** (every domain except [`dcp`](dcp/README.md), the authoritative source) are migrated to `$ref` the canonical set — back-compatible, since the `$defs` names are unchanged so every object schema still resolves. Each keeps its own agency-specific definitions local; only the shared geography/identifier/address/money/agency shapes are redirected.

## Cross-agency key registry

The join keys that let one agency's records link to another's, ranked by how many domains carry them (from the [linkage analysis](LINKAGE.md)):

| Key | Category | Domains | Owner |
|---|---|---:|---|
| Borough | geography | 70 | — |
| Coordinates (lat/long) | geography | 70 | — |
| BBL | property | 23 | dcp |
| BIN | property | 23 | dcp |
| Community Board | geography | 17 | — |
| Council District | geography | 17 | — |
| Census Tract | geography | 9 | — |
| NTA (neighborhood) | geography | 9 | — |
| Police Precinct | geography | 5 | — |
| GISPropNum | property | 2 | nycgovparks.org |
| DBN (school) | identity | 2 | — |
| Matter ID (Legistar) | identity | 2 | — |
| Election District | identity | 2 | — |
| Council Member ID | identity | 1 | — |

---
*Part of the [NYC Modernization](README.md) study. Design-first artifacts, not deployments.*
