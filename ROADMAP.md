# Roadmap

Where the NYC — API & Agent Modernization project is headed. Derived from the [cross-domain synthesis](SYNTHESIS.md) and its NYC API playbook. Status: 🟢 done · 🟡 in progress · ⚪ planned.

## Now / next

### 🟢 The Programmable City — API · MCP · Skills experience layer — **shipped**
The design-first payoff, assembled: the **REST operation → MCP tool → Agent Skill** chain across all 67 agencies in one place ([experience.html](https://nyc.apievangelist.com/experience.html)), built on the [API Experience](https://experience.apicommons.org) model. **721 operations, 624 MCP tools**, mapped to **ten common government processes** (Apply, Report, Request-records, Schedule, Register, Dispute, Pay + look-up-a-place, check-status, search-data), plus **7 cross-agency MCP prompts** and **7 resources** anchored on nyc-commons. Machine artifacts (`experience/`): one unified OpenAPI with `x-mcp-tool`/`x-agent-skill` on every operation, a NYC-wide MCP definition, an APIs.json descriptor (opens in experience.apicommons.org), and the ten Agent Skills. `scripts/build-experience.py` regenerates it all. **Shipped since:** per-agency MCP prompts + resources (167 prompts / 208 resources); a **static reference API** with GET-callable example data (`experience/api/`, `scripts/build-gateway.py`); and a **working, installable MCP server** [`@api-common/nyc-mcp`](experience/mcp-server/) with an [install.apicommons.org](https://install.apicommons.org) button on the page. **Next:** publish `@api-common/nyc-mcp` to npm to activate one-click install; optional AWS deploy for live writes.

### 🟢 `nyc-commons` — the shared schema set (HIGH priority) — **shipped v0.1.0**
The synthesis's clearest structural finding: writing one `_common.json` per domain surfaced the **same fields in every domain** — `Borough` (all 67), `Coordinates` (all 67), a geography spine (56), `Address` (15), `Money` (13). Parks facilities, DOE schools, Council funding, and BOE poll sites all carry them.

**Shipped:** a single, versioned, referenceable **[`nyc-commons/`](nyc-commons/README.md)** schema set — 21 canonical definitions across six files, factored from [DCP](dcp/) as the authoritative source, browsable at [commons.html](https://nyc.apievangelist.com/commons.html):
- `nyc-commons/geography.json` — `Borough`, `BoroCode`, `Coordinates`, `CommunityDistrict`, `CouncilDistrict`, `CensusTract`, `NTA`, `AdminBoundaries`, `GeographySpine`. ✅
- `nyc-commons/identifiers.json` — `BBL`, `BIN`, `GISPropNum`, `DBN`, `BoroBlockLot`, `CrossAgencyKey`. ✅
- `nyc-commons/place.json`, `nyc-commons/address.json`, `nyc-commons/party.json`, `nyc-commons/money.json` — the join objects + recurring party/money shapes. ✅
- **All 66 consumer domains migrated** to `$ref` the canonical set (every domain except DCP, the source), back-compatible — unchanged `$defs` names, so every object schema still resolves. Each keeps its agency-specific definitions local. ✅

**Next:** publish the `$id` base at a stable host (versioned), and add the party/contact/organization shapes to the shared set as their per-domain variants converge.

### 🟢 Cross-domain identity — `Address` / `Place` / `Person` — **shipped with nyc-commons**
Synthesis finding: every domain has its own join key (`gisPropNum`, `DBN`, `matterId`, election-district) and nothing links them. **Shipped** as [`nyc-commons/place.json`](nyc-commons/place.json) (`Place`, keyed on BBL/BIN + coordinates + the geography spine, carrying a list of other agencies' `CrossAgencyKey`s), [`address.json`](nyc-commons/address.json) (`Address`), and [`party.json`](nyc-commons/party.json) (`PersonName`/`PartyReference`) so cross-domain questions — "what's near me?", "who represents this block?" — become answerable.

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
