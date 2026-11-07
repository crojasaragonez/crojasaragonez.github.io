"""Illustrative fund simulation for the digital twins article.

This is a toy model written for the blog. It does NOT use Subaxa data,
parameters, or methods. Run: python3 generate.py  (writes *.svg.html snippets)
"""
import numpy as np
from pathlib import Path

OUT = Path(__file__).parent
RNG = np.random.default_rng(2026)
SIMS, HORIZON, CAPITAL = 2000, 48, 100.0


def simulate(n_props):
    """Return fund value index per month (SIMS x HORIZON+1)."""
    size = CAPITAL / n_props
    values = np.zeros((SIMS, HORIZON + 1))
    for s in range(SIMS):
        buy = np.sort(RNG.integers(0, 10, n_props))           # deploy over months 0-9
        legal = RNG.triangular(4, 10, 24, n_props)              # months to resolve
        sale = RNG.uniform(2, 8, n_props)                       # months to sell
        mult = RNG.lognormal(np.log(1.45), 0.28, n_props) - 0.10  # net of costs
        trouble = RNG.random(n_props) < 0.12                    # complications
        mult[trouble] *= 0.55
        legal[trouble] += 8
        exit_m = buy + legal + sale
        for t in range(HORIZON + 1):
            sold = exit_m <= t
            # cash not yet deployed + unsold at cost + proceeds of sold
            values[s, t] = size * ((buy > t).sum() + ((buy <= t) & ~sold).sum() + mult[sold].sum())
    return values


def fan_chart(v):
    W, H, L, R, T, B = 700, 430, 80, 640, 70, 340
    lo, hi = 90, 170
    x = lambda m: L + (R - L) * m / HORIZON
    y = lambda val: B - (B - T) * (val - lo) / (hi - lo)
    p = {q: np.percentile(v, q, axis=0) for q in (10, 25, 50, 75, 90)}
    months = range(HORIZON + 1)
    def band(a, b):
        top = " ".join(f"L{x(m):.1f} {y(p[b][m]):.1f}" for m in months)
        bot = " ".join(f"L{x(m):.1f} {y(p[a][m]):.1f}" for m in reversed(months))
        return "M" + top[1:] + " " + bot + " Z"
    med = "M" + " ".join(f"L{x(m):.1f} {y(p[50][m]):.1f}" for m in months)[1:]
    g = []
    for val in range(lo, hi + 1, 10):
        g.append(f'<line x1="{L}" y1="{y(val):.1f}" x2="{R}" y2="{y(val):.1f}" stroke="var(--border)"/>'
                 f'<text x="{L-12}" y="{y(val)+4:.1f}" text-anchor="end" font-size="11" fill="var(--text-muted)">{val}</text>')
    for m in range(0, HORIZON + 1, 12):
        g.append(f'<text x="{x(m):.1f}" y="{B+20}" text-anchor="middle" font-size="11" fill="var(--text-muted)">{m}</text>')
    end = {q: p[q][-1] for q in p}
    lab = (f'<text x="{R+6}" y="{y(end[90])+4:.1f}" font-size="10.5" fill="var(--text-muted)">P90</text>'
           f'<text x="{R+6}" y="{y(end[50])+4:.1f}" font-size="10.5" fill="var(--text)">Median</text>'
           f'<text x="{R+6}" y="{y(end[10])+4:.1f}" font-size="10.5" fill="var(--text-muted)">P10</text>')
    return f'''<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="dt3t dt3d">
<title id="dt3t">Range of simulated fund value paths</title>
<desc id="dt3d">Illustrative simulation of {SIMS} paths for a toy property fund over {HORIZON} months, indexed to 100 at launch. The median path ends near {end[50]:.0f}; 80% of paths end between {end[10]:.0f} and {end[90]:.0f}.</desc>
<text x="{W/2}" y="30" text-anchor="middle" font-size="16" font-weight="600" fill="var(--text)">{SIMS:,} simulated futures for one illustrative fund</text>
{"".join(g)}
<line x1="{L}" y1="{y(100):.1f}" x2="{R}" y2="{y(100):.1f}" stroke="var(--border-strong)" stroke-dasharray="4 4"/>
<path d="{band(10, 90)}" fill="var(--accent)" fill-opacity="0.2"/>
<path d="{band(25, 75)}" fill="var(--accent)" fill-opacity="0.32"/>
<path d="{med}" fill="none" stroke="var(--accent-soft)" stroke-width="2.5"/>
{lab}
<text x="{(L+R)/2}" y="{B+44}" text-anchor="middle" font-size="13" fill="var(--text-muted)">Months since launch →</text>
<text x="24" y="{(T+B)/2}" transform="rotate(-90 24 {(T+B)/2})" text-anchor="middle" font-size="13" fill="var(--text-muted)">Fund value (100 = capital invested) →</text>
<g font-size="11" fill="var(--text-muted)"><rect x="150" y="402" width="18" height="10" fill="var(--accent)" fill-opacity="0.2"/><text x="174" y="411">80% of paths</text><rect x="270" y="402" width="18" height="10" fill="var(--accent)" fill-opacity="0.32"/><text x="294" y="411">50% of paths</text><line x1="390" y1="407" x2="408" y2="407" stroke="var(--accent-soft)" stroke-width="2.5"/><text x="414" y="411">Median path</text></g>
</svg>''', end


def histogram(a, b):
    W, H, L, R, T, B = 700, 430, 80, 640, 70, 340
    bins = np.arange(0.8, 2.01, 0.1)
    clip = lambda v: np.clip(v, bins[0], bins[-1] - 1e-9)  # last bin holds the tail
    ha = np.histogram(clip(a), bins)[0] / len(a) * 100
    hb = np.histogram(clip(b), bins)[0] / len(b) * 100
    top = int(np.ceil(max(ha.max(), hb.max()) / 5) * 5)
    x = lambda v: L + (R - L) * (v - bins[0]) / (bins[-1] - bins[0])
    y = lambda pct: B - (B - T) * pct / top
    bw = (R - L) / (len(bins) - 1)
    g = []
    for pct in range(0, top + 1, 5):
        g.append(f'<line x1="{L}" y1="{y(pct):.1f}" x2="{R}" y2="{y(pct):.1f}" stroke="var(--border)"/>'
                 f'<text x="{L-12}" y="{y(pct)+4:.1f}" text-anchor="end" font-size="11" fill="var(--text-muted)">{pct}%</text>')
    for v in np.arange(0.8, 2.01, 0.2):
        g.append(f'<text x="{x(v):.1f}" y="{B+20}" text-anchor="middle" font-size="11" fill="var(--text-muted)">{v:.1f}×</text>')
    bars = []
    for i in range(len(bins) - 1):
        x0 = L + i * bw
        bars.append(f'<rect x="{x0+1:.1f}" y="{y(ha[i]):.1f}" width="{bw/2-1:.1f}" height="{B-y(ha[i]):.1f}" fill="var(--accent-deep)"/>')
        bars.append(f'<rect x="{x0+bw/2:.1f}" y="{y(hb[i]):.1f}" width="{bw/2-1:.1f}" height="{B-y(hb[i]):.1f}" fill="var(--accent-soft)"/>')
    stats = dict(a_med=np.median(a), b_med=np.median(b), a_loss=(a < 1).mean() * 100, b_loss=(b < 1).mean() * 100,
                 a_p10=np.percentile(a, 10), b_p10=np.percentile(b, 10))
    return f'''<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="dt4t dt4d">
<title id="dt4t">Outcome distributions for two strategies</title>
<desc id="dt4d">Illustrative simulation. Fund value multiple after {HORIZON} months. Concentrated path (6 properties): median {stats["a_med"]:.2f}x, {stats["a_loss"]:.0f}% of paths below 1.0x. Diversified path (24 properties): median {stats["b_med"]:.2f}x, {stats["b_loss"]:.1f}% of paths below 1.0x.</desc>
<text x="{W/2}" y="30" text-anchor="middle" font-size="16" font-weight="600" fill="var(--text)">Same capital, two paths, very different risk</text>
{"".join(g)}
<rect x="{L}" y="{T}" width="{x(1.0)-L:.1f}" height="{B-T}" fill="var(--text-muted)" fill-opacity="0.07"/>
<text x="{(L+x(1.0))/2:.1f}" y="{T+16}" text-anchor="middle" font-size="10.5" fill="var(--text-muted)">Lose money</text>
{"".join(bars)}
<line x1="{x(1.0):.1f}" y1="{T}" x2="{x(1.0):.1f}" y2="{B}" stroke="var(--border-strong)" stroke-dasharray="4 4"/>
<line x1="{L}" y1="{B}" x2="{R}" y2="{B}" stroke="var(--border-strong)"/>
<text x="{(L+R)/2}" y="{B+44}" text-anchor="middle" font-size="13" fill="var(--text-muted)">Fund value multiple after {HORIZON} months →</text>
<text x="24" y="{(T+B)/2}" transform="rotate(-90 24 {(T+B)/2})" text-anchor="middle" font-size="13" fill="var(--text-muted)">Share of simulated paths →</text>
<g font-size="11" fill="var(--text-muted)"><rect x="160" y="402" width="12" height="12" fill="var(--accent-deep)"/><text x="178" y="412">Path A: 6 larger properties</text><rect x="390" y="402" width="12" height="12" fill="var(--accent-soft)"/><text x="408" y="412">Path B: 24 smaller properties</text></g>
</svg>''', stats


# Illustrative cash distribution for ONE property sale (not Subaxa figures).
SALE = 150_000
COSTS = [("Auction price", 90_000), ("Legal and court costs", 6_000),
         ("Repairs and preparation", 10_000), ("Holding costs", 6_000),
         ("Closing costs and taxes", 7_500)]


def sankey():
    cost_total = sum(v for _, v in COSTS)
    profit = SALE - cost_total
    split = [("Investors (80%)", round(profit * 0.8)), ("Fund manager (20%)", round(profit * 0.2))]
    W, H, TOP, K, GAP3 = 700, 480, 78, 300 / SALE, 12
    X1, X2, X3, NW = 40, 270, 470, 14
    COST, PROF = "#fb7185", "#34d399"
    leaves = [(n, v, COST) for n, v in COSTS] + [(n, v, PROF) for n, v in split]
    col3_h = SALE * K + GAP3 * (len(leaves) - 1)
    y3, ys = TOP, []
    for _, v, _ in leaves:
        ys.append(y3); y3 += v * K + GAP3
    mid = TOP + col3_h / 2
    gap2 = 44
    y2c = mid - (SALE * K + gap2) / 2
    y2p = y2c + cost_total * K + gap2
    y1 = mid - SALE * K / 2

    def ribbon(xa, ya, xb, yb, h, color):
        cx = (xa + xb) / 2
        return (f'<path d="M{xa:.1f} {ya:.1f} C{cx:.1f} {ya:.1f} {cx:.1f} {yb:.1f} {xb:.1f} {yb:.1f} '
                f'L{xb:.1f} {yb+h:.1f} C{cx:.1f} {yb+h:.1f} {cx:.1f} {ya+h:.1f} {xa:.1f} {ya+h:.1f} Z" '
                f'fill="{color}" fill-opacity="0.32"/>')

    out = []
    # column 1 -> 2
    out.append(ribbon(X1 + NW, y1, X2, y2c, cost_total * K, COST))
    out.append(ribbon(X1 + NW, y1 + cost_total * K, X2, y2p, profit * K, PROF))
    # column 2 -> 3
    off = {COST: y2c, PROF: y2p}
    for (n, v, c), y in zip(leaves, ys):
        out.append(ribbon(X2 + NW, off[c], X3, y, v * K, c))
        off[c] += v * K
    # nodes
    out.append(f'<rect x="{X1}" y="{y1:.1f}" width="{NW}" height="{SALE*K:.1f}" fill="var(--accent)"/>')
    out.append(f'<rect x="{X2}" y="{y2c:.1f}" width="{NW}" height="{cost_total*K:.1f}" fill="{COST}"/>')
    out.append(f'<rect x="{X2}" y="{y2p:.1f}" width="{NW}" height="{profit*K:.1f}" fill="{PROF}"/>')
    for (n, v, c), y in zip(leaves, ys):
        out.append(f'<rect x="{X3}" y="{y:.1f}" width="{NW}" height="{v*K:.1f}" fill="{c}"/>')
        cy = y + v * K / 2 + 4
        out.append(f'<text x="{X3+NW+10}" y="{cy:.1f}" font-size="12" fill="var(--text)">{n} '
                   f'<tspan font-weight="600" fill="var(--text-muted)">${v:,}</tspan></text>')
    lab = lambda x, y, a, b: (f'<text x="{x}" y="{y:.1f}" font-size="12.5" font-weight="600" fill="var(--text)">{a}</text>'
                              f'<text x="{x}" y="{y+16:.1f}" font-size="12" fill="var(--text-muted)">{b}</text>')
    out.append(lab(X1, y1 - 26, "Sale price", f"${SALE:,}"))
    out.append(lab(X2, y2c - 26, "Costs recovered", f"${cost_total:,}"))
    out.append(lab(X2, y2p + profit * K + 18, "Net profit", f"${profit:,}"))
    desc = (f"Illustrative example, not Subaxa figures. A property sold for ${SALE:,}. "
            + "; ".join(f"{n}: ${v:,}" for n, v in COSTS)
            + f". Costs total ${cost_total:,}, leaving a net profit of ${profit:,}, split "
            + " and ".join(f"{n} ${v:,}" for n, v in split) + ".")
    svg = f"""<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="dt5t dt5d">
<title id="dt5t">Where the money from one property sale goes</title>
<desc id="dt5d">{desc}</desc>
<text x="{W/2}" y="30" text-anchor="middle" font-size="16" font-weight="600" fill="var(--text)">Where the money from one property sale goes</text>
{"".join(out)}
</svg>"""
    return svg, cost_total, profit, split


if __name__ == "__main__":
    a = simulate(6)
    b = simulate(24)
    svg, end = fan_chart(a)
    (OUT / "fan.svg.html").write_text(svg)
    svg, stats = histogram(a[:, -1] / 100, b[:, -1] / 100)
    (OUT / "paths.svg.html").write_text(svg)
    svg, ct, pr, sp = sankey()
    (OUT / "sankey.svg.html").write_text(svg)
    print("sankey:", ct, pr, sp)
    print("fan end percentiles (Path A):", {k: round(float(v), 1) for k, v in end.items()})
    print({k: round(float(v), 3) for k, v in stats.items()})
    med_month = lambda v: int(np.argmax(np.median(v, axis=0) >= 100 * 1.0 + 0.01))
    print("median time-in-value>100: A", med_month(a), "B", med_month(b))
