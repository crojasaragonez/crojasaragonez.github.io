# Costa Rica crime: source data

Supports the draft `datos-criminalidad-costa-rica-dos-historias.md`. Retrieved 2026-10-09
from the Judicial Branch's open data portal,
<https://datosabiertospj.poder-judicial.go.cr/dataset/estadisticas-policiales>
(CC Attribution; dataset metadata last modified 2026-08-03, updated monthly).

- **Raw files:** twelve CSVs, `PJCROD_POLICIALES_V1-<year>.csv`, 2015 to 2026,
  577,310 rows, Latin-1, no header. They total ~90 MB and are not checked in;
  `aggregate.py` downloads them. Columns: category, subtype, date, victim
  type, victim subtype, age group, gender (empty in every year), nationality,
  province, canton, district.
- **Cutoff:** the 2026 file ends on 2026-10-01. The 36 rows dated October 1
  are dropped so 2026 covers January to September. Every comparison that
  includes 2026 uses January to September of each year (`records_jan_sep`).
- **Locations:** 18 rows have no valid province and are grouped as
  `DESCONOCIDO`. A few nationalities contain a comma, so the location
  columns are read from the end of the row.
- **Unit:** one row is one record. The files have no case or victim
  identifier, so the analysis counts rows.

## Known discrepancy with official homicide totals

The dataset's homicide rows run 10% to 16% above the totals the OIJ
announces (2019 to 2025), and above all seven 2025 provincial totals.
`oij-homicides.json` holds the announced figures with their sources. The
cause is unknown: about one homicide row in eight (2023 to 2025) is
identical to another row, which may be a second victim of the same event or a
duplicate. The article uses the dataset for composition and trend, and the
announced totals for levels. Do not present dataset homicide counts as the
official number of victims.

## Regenerating

```sh
python3 src/data/costa-rica-crime/aggregate.py [RAW_DIR]   # optional, rewrites the CSVs
MPLCONFIGDIR=/tmp/matplotlib python3 src/data/costa-rica-crime/generate.py
```

`generate.py` reads `monthly.csv`, `province.csv` and `subtype.csv`, writes
four SVGs to `public/images/blog/costa-rica-crime/` and refreshes the
article's figure blocks. Requires Python 3 and Matplotlib (tested with
3.11.0). Generation is offline and deterministic.

The article stays `draft: true`. Its route is available in Astro dev mode;
production routes, listings and the sitemap exclude it.
