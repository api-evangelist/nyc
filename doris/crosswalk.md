# Crosswalk — Website/Portal Fruit ↔ APIs ↔ NYC Open Data (DORIS)

Maps the low-hanging fruit on **nyc.gov/site/records**, the **Municipal Archives collections** (archives.nyc / Preservica DAMS), the **Historical Vital Records portal**, and the **OpenRecords FOIL** system to (a) the **existing APIs** (Socrata SODA; the token-gated Preservica content API) and (b) the **13 DORIS datasets** on NYC Open Data. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-doris.json](opendata-doris.json).

## The reframe — fifth distinct pattern

- **Parks:** data-rich HTML on a legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned → *consolidate + own.*
- **NYCHA:** the reference data is open, every resident transaction is locked in a vendor CRM → *unlock the service layer.*
- **DORIS:** the **indexes/finding aids are open** (13 Socrata datasets), but the **objects are locked in a vendor DAMS** (Preservica/LUNA) and **retrieving** a record is a manual order across three portals → **retrieve** — bind the open index to the closed object and make ordering an API.

DORIS is the "discovery is solved, retrieval isn't" pattern. You can *find* a 1920 death certificate, a WPA-era photograph, or a mandated agency report in seconds — the indexes are open. But the scan lives behind the DAMS, and *getting* it means an order on the vital-records portal, an email/form to the Archives, or a FOIL request on OpenRecords. A researcher or agent asking "get me a copy of this certificate" has no API to call.

Coverage: ✅ strong open index · 🟡 partial/blob/token-gated · ❌ gap (no API).

## Entity crosswalk

| Entity | Website / Portal | API today | Open Data | Cov. |
|---|---|---|---|---|
| `ArchivalCollection` | archives.nyc / Preservica | SODA (index); Preservica (token) | Resources & Instances (`bk7g-bhsz`, 11c); Accessions (`vfa7-chs9`) | 🟡 index open, object gated |
| `DigitalItem` | Archives online collections | SODA (index); **Preservica token-gated** | Digital Objects (`28et-rv7b`, 5c) | 🟡 metadata open, asset in DAMS |
| `HistoricalVitalRecord` | Historical Vital Records portal | SODA (index); **portal, no API** | Death (`797j-9xvg`), Marriage Cert (`j62e-7maa`), Birth (`5gq7-rgmv`), Marriage License (`d8dr-nyhw`) | 🟡 index open, scan behind portal |
| `GovernmentPublication` | City Hall Library / publications | SODA | Library Catalog (`gysc-yn4h`, blob); Publications Listing (`xip9-pe9k`, 18c); Required Reports (`9azj-tmjp`) | ✅ / 🟡 (catalog is a blob) |
| `HonoraryStreetName` | records site / maps | SODA | Street Line (`xesp-yqsx`, 14c); Intersection (`ig76-wwag`, 18c) | ✅ |
| Order a vital-record copy | Historical Vital Records portal | **portal only** | — | ❌ gap |
| Request an archival reproduction | archives.nyc / email / form | **email/form only** | — | ❌ gap |
| File a FOIL request | OpenRecords | **portal only** (read-only rollup) | rollup `kegn-anvq` | ❌ gap (write) |
| **`RecordsRequest`** (retrieve/order a record) | portals + forms | **portals only** | — | ❌ **net-new** |

## The mismatch, concretely

| Source | Strength | Weakness |
|---|---|---|
| **Socrata SODA (13 datasets)** | Open, machine-readable; strong indexes for vital records, archives, publications, honorary streets | Indexes/metadata only; the catalog is a delimited blob; nothing that retrieves an object or files a request |
| **Preservica content API (DAMS)** | A real REST/JSON API holding the actual digitized assets | Token-gated for the public catalog; no OpenAPI, no open/bulk access, not agent-accessible |
| **Vital-records + OpenRecords portals** | The real retrieval systems — order a certified copy, file a FOIL | Akamai/portal UIs; no API, no OpenAPI, no JSON; each a separate silo; email/form is the fallback |

## Implications for the API-first + MCP proposal

1. **Publish the open indexes as one clean resource model.** Archival collections, digital items, vital-record indexes, publications, and honorary street names behind one owned DORIS contract ([OpenAPI](openapi/doris.yaml)) — so consumers learn one model, not 13 Socrata IDs across five systems.
2. **Bind the index to the object.** Every `DigitalItem` / `ArchivalCollection` carries a `provenance` link into the DAMS (Preservica/LUNA), turning an index hit into a resolvable object reference.
3. **Add the one net-new write workflow** — `request_record` (retrieve/order a record): a certified vital-record copy, an archival reproduction, a library publication, or a FOIL request, with the restricted-record eligibility path noted as offline.
4. **Normalize the catalog blob.** The most-viewed dataset (`gysc-yn4h`) is a single `#`-delimited column — a clean win to structure into `GovernmentPublication`.
5. **MCP server** so an agent can answer "find my great-grandfather's 1918 death certificate in Kings County", "show me WPA photographs of this block", and — the point — "order a certified copy and tell me the status."
