"""Aggregate the Judicial Branch's police statistics into the article's CSVs.

Usage: python3 aggregate.py [RAW_DIR]

RAW_DIR holds PJCROD_POLICIALES_V1-<year>.csv or <year>.csv for 2015-2026.
Missing files are downloaded into RAW_DIR (default: a temporary directory).
The raw files are ~90 MB in total, so they are not checked in.
"""
import csv
import sys
import tempfile
import urllib.request
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
URL = "https://pjcrdatosabiertos.blob.core.windows.net/datosabiertos/PJCROD_POLICIALES_V1/PJCROD_POLICIALES_V1-{year}.csv"
YEARS = range(2015, 2027)
CUTOFF = "2026-09-30"  # last complete month in the 2026 file
PROVINCES = {"SAN JOSE", "ALAJUELA", "CARTAGO", "HEREDIA", "GUANACASTE", "PUNTARENAS", "LIMON"}

raw = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(tempfile.mkdtemp())
raw.mkdir(parents=True, exist_ok=True)

monthly, province, motive = Counter(), Counter(), Counter()
for year in YEARS:
    path = next((p for p in (raw / f"PJCROD_POLICIALES_V1-{year}.csv", raw / f"{year}.csv") if p.exists()), None)
    if path is None:
        path = raw / f"PJCROD_POLICIALES_V1-{year}.csv"
        urllib.request.urlretrieve(URL.format(year=year), path)
    # No header row. Columns: delito, subdelito, fecha, victima, subvictima, edad,
    # genero (always empty), nacionalidad, provincia, canton, distrito. A few
    # nationalities contain a comma ("CONGO, REPUBLICA ..."), so location is
    # read from the end of the row.
    with open(path, encoding="latin-1", newline="") as fh:
        for row in csv.reader(fh):
            date = row[2]
            if date > CUTOFF:
                continue
            crime, sub = row[0].strip(), row[1].strip()
            y, m = int(date[:4]), int(date[5:7])
            prov = row[-3].strip()
            prov = prov if prov in PROVINCES else "DESCONOCIDO"
            monthly[(f"{y}-{m:02d}", y, crime)] += 1
            for counter, key in ((province, (y, prov, crime)), (motive, (y, crime, sub))):
                counter[key + ("all",)] += 1
                if m <= 9:
                    counter[key + ("jan_sep",)] += 1

with open(HERE / "monthly.csv", "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["month", "year", "crime", "records"])
    for (month, y, crime), n in sorted(monthly.items()):
        w.writerow([month, y, crime, n])

for name, header, counter in (("province.csv", ["year", "province", "crime"], province),
                              ("subtype.csv", ["year", "crime", "subtype"], motive)):
    keys = sorted({k[:-1] for k in counter})
    with open(HERE / name, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(header + ["records", "records_jan_sep"])
        for k in keys:
            w.writerow(list(k) + [counter[k + ("all",)], counter[k + ("jan_sep",)]])

print(f"Wrote monthly.csv, province.csv and subtype.csv to {HERE}")
