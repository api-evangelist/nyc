# NYC Open Data — IBO Datasets

All NYC Open Data assets whose **Dataset-Information_Agency = "NYC Independent Budget Office (IBO)"** (verified via the Socrata Discovery API, 2026-07-13). **20 assets**, sorted by lifetime page views. Machine-readable: [opendata-ibo.json](opendata-ibo.json).

The shape of the corpus is the story: IBO publishes **wide, pivoted fiscal time-series** — one row per line-item/category, one **column per fiscal year** (`FY 1980` … `FY 2020`) — plus distributional tax/income tables keyed on AGI range. This is Excel-on-Socrata, not a normalized data model; a modern API would pivot these to long-form `(series, category, fiscalYear, value)` observations. IBO’s analysis itself (revenue forecasts, fiscal briefs, testimony) is **not** in Open Data — it lives as **1,145 publications** behind the NYC.gov Content API and as PDFs/interactives. See [crosswalk.md](crosswalk.md).

| Views | Type | ID | Name | Cols |
|--:|---|---|---|--:|
| 12,077 | dataset | `gffu-ps8j` | Income By Type Of Income And AGI Range | 7 |
| 8,499 | dataset | `ipc3-2nbm` | Personal Income By AGI Range | 7 |
| 3,344 | file | `29nk-6u2k` | NYC Public School Indicators | 0 |
| 2,808 | dataset | `hdnu-nbrh` | NYC Independent Budget Office (IBO) Tax Revenue FY 1980 - FY 2020 | 14 |
| 2,690 | dataset | `7zhs-43jt` | NYC Independent Budget Office (IBO) Revenue And Spending Summary FY 1980 - FY 2020 | 42 |
| 2,170 | dataset | `5i9t-mvdt` | NYC Independent Budget Office (IBO) Debt Outstanding Since FY 2000 | 22 |
| 1,931 | dataset | `uaj7-9szf` | NYC Independent Budget Office (IBO) Full Time Positions in city government, by fiscal year | 42 |
| 1,875 | dataset | `p26e-k6k9` | School Spending Since 1990 | 29 |
| 1,853 | dataset | `hukm-snmq` | NYC Independent Budget Office (IBO) Capital Expenditures Since 1985 | 38 |
| 1,804 | file | `mric-ye48` | Annual Tax Effort in NYC since 1929 | 0 |
| 1,762 | dataset | `fu34-wamz` | NYC Independent Budget Office (IBO) State And Federal Categorical Aid, FY 1980 - 2020 | 43 |
| 1,712 | dataset | `cwjy-rrh3` | NYC Independent Budget Office (IBO) Agency Expenditures FY 1980 - 2018 | 40 |
| 1,565 | dataset | `sg72-pis5` | IBO Federal Stimulus Budget and Spending Tracker (ARPA and CRRSAA) | 12 |
| 1,552 | dataset | `6ggx-itps` | NYC Independent Budget Office (IBO) Debt Service Since FY 2000 | 22 |
| 1,543 | dataset | `ke6f-vhnd` | Independent Budget Office: NYC COVID 19 Spending by Date - Citywide and by Agency | 48 |
| 1,517 | dataset | `3vvi-fwjs` | Tax Liability By AGI Range | 4 |
| 1,361 | dataset | `ypbd-r4kg` | NYC Independent Budget Office (IBO) Non- Tax Revenues FY 1980 - FY 2020 | 42 |
| 1,098 | dataset | `nwet-nc6h` | Tax Credits By Agi Range | 3 |
| 797 | dataset | `khqt-g67n` | Independent Budget Office: NYC COVID 19 Cumulative Spending by Expense Type | 2 |
| 766 | dataset | `duk5-k5fk` | NYC COVID 19 Spending by Agency by Expense Description | 3 |

## Groupings

- **City revenue & spending (wide FY tables):** Revenue And Spending Summary (`7zhs-43jt`, 42c), Non-Tax Revenues (`ypbd-r4kg`), State & Federal Categorical Aid (`fu34-wamz`), Agency Expenditures (`cwjy-rrh3`), Full-Time Positions by agency (`uaj7-9szf`).
- **Capital & debt:** Capital Expenditures by purpose (`hukm-snmq`), Debt Outstanding (`5i9t-mvdt`), Debt Service (`6ggx-itps`).
- **Education / schools:** School Spending Since 1990 (`p26e-k6k9`, 29c), NYC Public School Indicators (`29nk-6u2k`, file).
- **Taxes & income distribution (by AGI range):** Tax Revenue since FY1980 (`hdnu-nbrh`), Personal Income by AGI Range (`ipc3-2nbm`), Income by Type and AGI Range (`gffu-ps8j`), Tax Liability by AGI Range (`3vvi-fwjs`), Tax Credits/EITC by AGI Range (`nwet-nc6h`), Annual Tax Effort since 1929 (`mric-ye48`, file).
- **COVID / federal stimulus trackers:** COVID-19 Spending by Date (`ke6f-vhnd`), Cumulative Spending (`khqt-g67n`), Spending by Agency by Expense (`duk5-k5fk`), Federal Stimulus / ARPA Tracker (`sg72-pis5`).
