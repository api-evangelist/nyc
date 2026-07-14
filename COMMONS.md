# nyc-commons — the shared schema set

*One canonical definition of a borough, a BBL, an address, a place, a party, and a dollar — for all of NYC government.*

Full schema set and rationale: [`nyc-commons/`](nyc-commons/README.md). Interactive: **[nyc.apievangelist.com/commons.html](https://nyc.apievangelist.com/commons.html)**.

## The problem it solves

Across the 67 domain assessments the same objects were re-declared per agency — **Borough in all 67**, Coordinates in all 67, a geography spine in 56. `nyc-commons` factors them into 21 canonical definitions across 5 files, `$ref`'d from [DCP](dcp/README.md) as the authoritative source, and **every consumer domain is now migrated to reference them**. Two records that resolve to the same `BBL` are provably about the same place.

## Adoption — canonical definitions and how many domains declare a local equivalent

| Definition | File | Domains declaring | Migrated to `$ref` |
|---|---|---:|---:|
| `Borough` | `geography.json` | 67 | 66 |
| `Coordinates` | `geography.json` | 67 | 66 |
| `GeographySpine` | `geography.json` | 56 | 55 |
| `Address` | `address.json` | 15 | 15 |
| `MoneyUSD` | `money.json` | 13 | 13 |
| `BoroCode` | `geography.json` | 7 | 6 |
| `ContactPoint` | `party.json` | 7 | 0 |
| `PartyReference` | `party.json` | 6 | 0 |
| `AgencyReference` | `party.json` | 6 | 5 |
| `OrganizationReference` | `party.json` | 5 | 0 |
| `FiscalYear` | `money.json` | 5 | 5 |
| `CommunityDistrict` | `geography.json` | 4 | 0 |
| `AdminBoundaries` | `geography.json` | 4 | 4 |
| `BBL` | `identifiers.json` | 4 | 0 |
| `CouncilDistrict` | `geography.json` | 1 | 0 |
| `CensusTract` | `geography.json` | 1 | 0 |
| `NTA` | `geography.json` | 1 | 0 |
| `BIN` | `identifiers.json` | 1 | 0 |
| `DBN` | `identifiers.json` | 1 | 1 |
| `FiscalPeriod` | `money.json` | 1 | 0 |
| `GISPropNum` | `identifiers.json` | 0 | 0 |

**Migration status: complete.** All **66 consumer domains** (every domain except [`dcp`](dcp/README.md), the authoritative source) are migrated to `$ref` the canonical set — back-compatible, since the `$defs` names are unchanged so every object schema still resolves. Each keeps its own agency-specific definitions local; only the shared geography/identifier/address/money/agency shapes are redirected.

## Cross-agency key registry

The join keys that let one agency's records link to another's, ranked by how many domains carry them (from the [linkage analysis](LINKAGE.md)):

| Key | Category | Domains | Owner |
|---|---|---:|---|
| Borough | geography | 67 | — |
| Coordinates (lat/long) | geography | 67 | — |
| Council District | geography | 62 | — |
| Community Board | geography | 56 | — |
| Census Tract | geography | 53 | — |
| NTA (neighborhood) | geography | 53 | — |
| BBL | property | 52 | dcp |
| BIN | property | 50 | dcp |
| Police Precinct | geography | 23 | — |
| GISPropNum | property | 2 | nycgovparks.org |
| DBN (school) | identity | 2 | — |
| Matter ID (Legistar) | identity | 2 | — |
| Election District | identity | 2 | — |
| Council Member ID | identity | 1 | — |

---
*Part of the [NYC Modernization](README.md) study. Design-first artifacts, not deployments.*
