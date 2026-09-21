# Apple Silicon: source observations

Supports the draft `from-m1-to-m6-apple-silicon.md`. Retrieved 2026-09-21.
The article adapts the author's MIT assignment but replaces its estimated
package-power comparison with published measurements of whole systems.

`measurements.json` contains the selected values, sources and protocols.

- **Evolution:** ComputerBase's community Cinebench 2026.1 aggregates for
  base M1–M6 chips. The sample mixes memory configurations, OS versions,
  cooling and devices. The M6 observation uses 32 GB and macOS 27. M1 has
  8/16 GB; M2 8 GB; M3 16 GB; M4 16/24/32 GB; M5 16/24/32 GB, mostly
  macOS 26 with some older versions as listed by the source. The range
  markers show the observed extrema, not confidence intervals. The plotted
  averages are the source's rounded aggregates; do not recompute a different
  statistic or infer a controlled generational uplift. Only one M6 result.
- **Comparison:** Notebookcheck's own M6 SoC analysis, Cinebench 2024,
  selected Apple/Qualcomm/Intel/AMD devices. The additional Air M4 result
  illustrates why a newer generation need not maximize efficiency.
  Snapdragon is the X2E-94-100 variant. The M6 review unit has 24 GB RAM
  and 512 GB storage. Device identifiers are in the JSON. Efficiency is the
  publication's reported points per watt using system power with its
  external-display protocol, not a TDP or package-power estimate. This is
  not a price-matched or power-matched comparison.

Do not combine Cinebench 2024 and 2026.1 scores. Do not divide scores from
one test by power from another. No benchmark was run by the blog author.

Generate the standalone SVGs and refresh the article's figure blocks:

```sh
MPLCONFIGDIR=/tmp/matplotlib python3 src/data/apple-silicon/generate.py
```

Requires Python 3 and Matplotlib (tested with 3.11.0). The generated figures
use selectable text, a zero baseline, a time-scaled evolution axis, and
source/date labels. Their SVG files are in `public/images/blog/apple-silicon/`.
Generation is offline and deterministic (fixed SVG hash salt; no timestamp).

The article stays `draft: true`. Its direct route is available in Astro dev
mode; production routes, home/blog listings and the sitemap exclude it.
