# Digital twins: illustrative toy model

Supports `digital-twins-for-private-investment-funds.md`. Figures 3 and 4 come
from `generate.py`, a deliberately simple toy model written for the article.
It does not use Subaxa data, parameters, or methods.

Assumptions: 100 units of capital deployed over months 0 to 9 into 6 (Path A)
or 24 (Path B) equal properties. Legal resolution takes 4 to 24 months
(triangular, mode 10) and sale 2 to 8 months. Net multiple per property is
lognormal around 1.45 minus 0.10 for costs. 12% of properties hit
complications: multiple x0.55 and 8 extra months. Properties are independent
(no shared market shocks). Unsold properties are held at cost. 2,000 runs per
path, seed 2026, 48-month horizon.

`python3 generate.py` writes `fan.svg.html` and `paths.svg.html`; their SVG
is pasted inline into the post (replace the matching `<svg>` blocks). Figures 1 and 2 are hand-written diagrams.
