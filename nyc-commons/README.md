# nyc-commons — the shared schema set

*One canonical definition of a borough, a BBL, an address, a place, a party, and a dollar — for all of NYC government.*

Across the [67 domain assessments](../SYNTHESIS.md) the same objects are re-declared over and over: **`Borough` appears in all 67** domains' `_common.json`, `Coordinates` in all 67, a `Geography`/`GeographySpine` block in 53, `Address` in 12, `Money` in 13. Every agency invents its own copy. That is the fragmentation the [synthesis](../SYNTHESIS.md) calls out as finding 11–12: a shared geography spine recurs everywhere, and yet **nothing links one agency's records to another's**.

`nyc-commons` is the fix: a single, versioned, referenceable schema set that every domain schema can [`$ref`](https://json-schema.org/understanding-json-schema/structuring) instead of maintaining a private definition. Resolve two records to the same `BBL` and they are provably about the same place.

## Factored from City Planning

The Department of City Planning (**[DCP](../dcp/)**) is the authoritative source of the city's geography — BBL (via PLUTO/MapPLUTO), community districts, Neighborhood Tabulation Areas, census tracts, and council/borough boundaries. `nyc-commons` is factored **from** DCP, not invented alongside it. `dcp/schemas/_common.json` carries an `x-nyc-commons: { role: "authoritative-source" }` marker; these files carry `role: "canonical"` and point back to it.

## The files

| File | What it defines |
|---|---|
| [`geography.json`](geography.json) | `Borough`, `BoroCode`, `Coordinates`, `CommunityDistrict`, `CouncilDistrict`, `CensusTract`, `NTA`, `AdminBoundaries`, and the **`GeographySpine`** — the recurring location block of NYC government. |
| [`identifiers.json`](identifiers.json) | The cross-agency join keys: **`BBL`**, **`BIN`**, `GISPropNum` (Parks), `DBN` (schools), `BoroBlockLot`, and `CrossAgencyKey` (a typed reference to another agency's primary key). |
| [`address.json`](address.json) | `Address` — a NYC street address decomposed the way city datasets store it (house-number range + street + borough + ZIP), resolving to BBL/BIN and coordinates. |
| [`place.json`](place.json) | **`Place`** — the missing cross-domain join object: one location resolved to its identifiers, geography spine, address, and coordinates, plus the other agencies' keys that resolve to it. |
| [`party.json`](party.json) | `PersonName`, `ContactPoint`, `AgencyReference`, `OrganizationReference`, `PartyReference` — the people/orgs/agencies that recur on records. |
| [`money.json`](money.json) | `MoneyUSD`, `FiscalYear` (NYC FY = Jul 1–Jun 30), `FiscalPeriod`. |
| [`nyc-commons.json`](nyc-commons.json) | Root index / manifest that re-exports the headline defs and lists every file. |

## How a domain uses it

A domain's `_common.json` keeps its `#/$defs/Borough` name (so existing object schemas that reference `_common.json#/$defs/Borough` keep resolving) and redirects the body to the canonical source:

```json
{
  "$defs": {
    "Borough": { "$ref": "https://raw.githubusercontent.com/api-evangelist/nyc/main/nyc-commons/geography.json#/$defs/Borough" },
    "Coordinates": { "$ref": "https://raw.githubusercontent.com/api-evangelist/nyc/main/nyc-commons/geography.json#/$defs/Coordinates" },
    "GeographySpine": { "$ref": "https://raw.githubusercontent.com/api-evangelist/nyc/main/nyc-commons/geography.json#/$defs/GeographySpine" }
  }
}
```

This is **back-compatible**: the `$defs` names are unchanged, so no object schema breaks — the definition simply now comes from one canonical place. **DCP** is the authoritative source and is *not* redirected; the consumer anchor domains **dob, dof, hpd, nyc311** are migrated this way as the reference implementation; the [adoption report](../commons.html) tracks the rest.

## Versioning

`x-nyc-commons.version` is `0.1.0`. These `$id`s are the stable base for the eventual published set; treat additions as backward-compatible and any field removal or `enum`/`pattern` tightening as a minor/major bump.

---
*Part of the [NYC Modernization](../README.md) study · [nyc.apievangelist.com/commons.html](https://nyc.apievangelist.com/commons.html). Design-first artifacts, not deployments.*
