# NYC Open Data — Brooklyn Public Library Datasets

All NYC Open Data assets whose **Dataset-Information_Agency = "Brooklyn Public Library (BPL)"** (verified via the Socrata Discovery API, 2026-07-13). **2 assets** — and both are `type=href` (external links), not live Socrata (SODA) tables. Machine-readable: [opendata-bklynlibrary.json](opendata-bklynlibrary.json).

The shape of the corpus is the story — or rather, the *absence* of one. **BPL is an independent nonprofit, not a city agency**, so it is under no Open Data mandate, and it shows: only two BPL-labeled assets exist on `data.cityofnewyork.us`, both simply **link out** to BPL-hosted files. There is **no live SODA endpoint, no column schema, no queryable table**. BPL's real, machine-readable data does not live on NYC Open Data at all — it lives on **BPL's own Drupal JSON:API** (`www.bklynlibrary.org/jsonapi`) and inside the **BiblioCommons catalog**. See [crosswalk.md](crosswalk.md) and [apis-observed.md](apis-observed.md).

| Views | Type | ID | Name | Cols |
|--:|---|---|---|--:|
| 6,501 | href | `xmzf-uf2w` | BPL Branches | 0 |
| 2,378 | href | `b7t4-zm44` | BPL Electronic Resources | 0 |

## Where the data actually is

- **Branches** (`xmzf-uf2w` on Open Data is just a file link) → live on the Drupal JSON:API as **`node--branch`** with full address, weekly hours, geo, subway lines, holds-pickup flag, and ~40 service fields.
- **Electronic resources** (`b7t4-zm44`) → live on the JSON:API as **`node--eres`** (link, vendor, status, language).
- **Events / programs** → `node--event` + `node--external_event` (power `discover.bklynlibrary.org`).
- **Digital collections** → `node--digital_asset`, `node--feature_collection_digcoll`, `node--finding_aid`.
- **The catalog (books) and holds** → **not on the site's API at all**; they live in the **BiblioCommons ILS** (`bklynlibrary.bibliocommons.com`), which has no documented public API.

## Caveat

A handful of BPL-*mentioning* assets exist under **other** agencies' labels (e.g. "BP Appointments – Brooklyn Public Library (BPL) Board" under the Brooklyn Borough President; citywide public-computer-center and Wi-Fi datasets under OTI). Those are not BPL-owned and are excluded here.
