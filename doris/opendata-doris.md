# NYC Open Data — DORIS Datasets

All NYC Open Data assets whose **Dataset-Information_Agency = "Department of Records and Information Services (DORIS)"** (verified via the Socrata Discovery API, 2026-07-13). 13 assets, sorted by lifetime page views. Machine-readable: [opendata-doris.json](opendata-doris.json).

The shape of the corpus is the story: it is **index-and-catalog heavy**. DORIS publishes the *finding aids* generously — indexes to the historical vital records (birth, death, marriage), a listing of the Municipal Archives' digitized objects and collection resources, the City Hall Library catalog, government publications, and honorary street names. What it does **not** publish is the object itself: the scanned certificate, the archival photograph, the digitized report. Those live in the vendor DAMS (Preservica, formerly LUNA Imaging) and are retrieved through separate portals. See [crosswalk.md](crosswalk.md).

| Views | Type | ID | Name | Cols |
|--:|---|---|---|--:|
| 41,855 | dataset | `gysc-yn4h` | NYC City Hall Library Catalog | 1 |
| 22,622 | dataset | `797j-9xvg` | NYC Historical Vital Records: Index to Digitized Death Certificates | 9 |
| 19,075 | dataset | `j62e-7maa` | NYC Historical Vital Records: Index to Digitized Marriage Certificates | 8 |
| 14,527 | dataset | `5gq7-rgmv` | NYC Historical Vital Records: Index to Digitized Birth Certificates | 8 |
| 10,987 | dataset | `kegn-anvq` | OpenRecords FOIL Requests | 8 |
| 7,407 | dataset | `d8dr-nyhw` | NYC Historical Vital Records: Index to Digitized Marriage Licenses | 3 |
| 2,907 | dataset | `xesp-yqsx` | NYC Honorary Street Names Map (Street Line) | 14 |
| 2,372 | dataset | `28et-rv7b` | NYC Municipal Archives Data Collection: Digital Objects | 5 |
| 2,354 | dataset | `ig76-wwag` | NYC Honorary Street Names Map (Intersection) | 18 |
| 1,899 | dataset | `9azj-tmjp` | Government Publication - Required Reports | 8 |
| 1,757 | dataset | `bk7g-bhsz` | NYC Municipal Archives Data Collection: Resources and Instances List | 11 |
| 1,526 | dataset | `xip9-pe9k` | Government Publications Listing | 18 |
| 1,463 | dataset | `vfa7-chs9` | NYC Municipal Archives Data Collection: Acquisitions / Accessions List | 7 |

## Groupings

- **Historical vital records (indexes):** Death Certificates (`797j-9xvg`, 9c), Marriage Certificates (`j62e-7maa`), Birth Certificates (`5gq7-rgmv`), Marriage Licenses (`d8dr-nyhw`) — name/Soundex + county + certificate day/month/year + certificate number. Indexes only; the scan is behind the Historical Vital Records portal.
- **Municipal Archives collections:** Digital Objects (`28et-rv7b`, the digitized items), Resources and Instances List (`bk7g-bhsz`, the finding-aid/container level), Acquisitions / Accessions List (`vfa7-chs9`).
- **Publications & library:** City Hall Library Catalog (`gysc-yn4h` — the most-viewed DORIS dataset, but a single delimited blob column), Government Publications Listing (`xip9-pe9k`, 18c), Government Publication - Required Reports (`9azj-tmjp`, the Charter/Local Law mandate table).
- **Honorary street names:** Street Line (`xesp-yqsx`, 14c) and Intersection (`ig76-wwag`, 18c) — enactment number, present/new name, limits, honoree, geography spine, coordinates.
- **FOIL:** OpenRecords FOIL Requests (`kegn-anvq`) — request status, agency, submitted/due/close dates, submission method. The one dataset that describes a *request* workflow (read-only rollup of the OpenRecords system).

## Caveats

- The City Hall Library Catalog (`gysc-yn4h`) is technically one column — a `#`-delimited MARC-like blob (Corporate Name#Subordinate Unit#Title#…). Rich content, poor structure; a real modernization win is normalizing it.
- None of these datasets carries the digital asset itself. "Digitized" here means an index/listing points to an object held in the DAMS; retrieval is a separate, non-API step.
