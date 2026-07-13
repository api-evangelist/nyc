# Roadmap

Where the NYC — API & Agent Modernization project is headed. Derived from the [cross-domain synthesis](SYNTHESIS.md) and its NYC API playbook. Status: 🟢 done · 🟡 in progress · ⚪ planned.

## Now / next

### ⚪ `nyc-commons` — the shared schema set (HIGH priority)
The synthesis's clearest structural finding: writing one `_common.json` per domain surfaced the **same fields in every domain** — `Borough`, `Community Board`, `Council District`, `Census Tract / NTA`, `BBL / BIN`. Parks facilities, DOE schools, Council funding, and BOE poll sites all carry them.

**Plan:** factor these into a single, versioned, referenceable **`nyc-commons`** schema set (its own directory / eventual published `$id` base) that every domain's schemas `$ref` instead of each maintaining a private `_common.json`. Deliverables:
- `nyc-commons/geography.json` — `Borough`, `CommunityBoard`, `CouncilDistrict`, `CensusTract`, `NTA`, `Coordinates`, `AdminBoundaries`.
- `nyc-commons/identifiers.json` — `BBL`, `BIN`, `GISPropNum`, `DBN` and other cross-agency keys.
- `nyc-commons/place.json`, `nyc-commons/address.json` — the missing cross-domain join objects (see identity item below).
- Migrate the four existing domains' `_common.json` to `$ref` `nyc-commons` (keep back-compat).

*Why it matters:* turns four isolated APIs into an interoperable set and gives future domains a running start.

### ⚪ Cross-domain identity — `Address` / `Place` / `Person`
Synthesis finding 8: every domain has its own join key (`gisPropNum`, `DBN`, `matterId`, election-district) and nothing links them. Define shared `Address` and `Place` objects (keyed on BBL/BIN + coordinates) so cross-domain questions — "what's near me?", "who represents this block?" — become answerable. Part of `nyc-commons`.

### 🟡 More domains
Continue the per-domain method to broaden coverage and stress-test the modernization-verb taxonomy.
- 🟢 Parks · DOE · Council · Elections · NYC311 (done)
- 🟡 **Batch of 10 in progress:** Buildings (DOB) · Housing (HPD) · Transportation (DOT) · Health (DOHMH) · Sanitation (DSNY) · Police (NYPD) · Taxi & Limousine (TLC) · City Planning (DCP) · Comptroller · Housing Authority (NYCHA). DOB tests "the real legacy surface is the `aNNN-*` app layer"; DCP is the source of the shared geography; Comptroller/Checkbook is another "partial API exists"; TLC/NYPD carry some of the largest open datasets.
- ⚪ Later candidates: DEP, DCWP, HRA/benefits (ACCESS NYC), DCAS, DOF, FDNY, DOE-adjacent (SCA), EDC.

## Soon

### ⚪ Prioritize the write workflows
The universal gap — four-for-four, the citizen action has no API (`PermitApplication`, `EnrollmentApplication`, `TestimonyRegistration`, `BallotRequest`). Build these out first as real read/write contracts; they're the highest citizen value.

### ⚪ Open-standards conformance
Where an open standard exists, measure against it and align the schema/OpenAPI — starting with **Open311 (GeoReport v2)** for NYC311. Add a "standards" dimension to the assessment.

### ⚪ APIs.json registry
Catalog every domain's schemas, OpenAPI, and MCP in a discoverable [APIs.json](https://apisjson.org) index so the citywide surface is navigable by humans and agents — the connective tissue open data never had.

### ⚪ Reference implementation
Stand up one read endpoint backed by the existing SODA/Open Data source (e.g. `GET /parks/{gisPropNum}` → Parks Properties) to prove the design-first contracts are buildable, not just aspirational.

## Later

- ⚪ **Agent-native by default** — ensure every domain ships a consistent MCP surface; add a shared auth/consent pattern for the write tools.
- ⚪ **Connect data to the front door** — demonstrate a public page consuming its own API instead of parallel HTML.
- ⚪ **Enumerate the `aNNN-*.nyc.gov` app layer** — the un-catalogued legacy application surface (open item from [domains.md](domains.md)).
- ⚪ **Own vendor-held records** — pattern for fronting vendor APIs (e.g. Legistar) with a city-owned contract.

## Done

- 🟢 Project activated in `api-evangelist/nyc`; thesis framed (not another data-liberation project).
- 🟢 `domains.md` inventory (~85 domains).
- 🟢 Four domain assessments through the full 7-step method.
- 🟢 Design-first artifact chain (JSON Schema → OpenAPI → MCP) per domain.
- 🟢 Explorable GitHub Pages site (nyc.apievangelist.com) + `CHANGELOG.md`.
- 🟢 Cross-domain [SYNTHESIS.md](SYNTHESIS.md) + maturity scorecard.
