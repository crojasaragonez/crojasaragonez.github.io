"""Render the article's four figures from the checked-in source observations.

Run from any directory: MPLCONFIGDIR=/tmp/matplotlib python3 path/to/generate.py
Requires matplotlib. No network requests or npm dependencies.
"""
import json
import re
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
OUT = ROOT / "public/images/blog/apple-silicon"
POST = ROOT / "src/content/blog/from-m1-to-m6-apple-silicon.md"
DATA = json.loads((HERE / "measurements.json").read_text())
OUT.mkdir(parents=True, exist_ok=True)

BG, TEXT, MUTED, GRID = "#111827", "#f8fafc", "#b5c3d7", "#273244"
BLUE, CYAN, GRAY = "#4f8cff", "#35d6ff", "#7187a5"
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 12,
    "text.color": TEXT, "axes.labelcolor": MUTED,
    "xtick.color": MUTED, "ytick.color": MUTED,
    "axes.facecolor": BG, "figure.facecolor": BG,
    "axes.edgecolor": GRID, "grid.color": GRID,
    "svg.fonttype": "none", "svg.hashsalt": "apple-silicon-2026",
})

def number(value):
    return f"{value:,.0f}"

def canvas(title, subtitle, height=5.6):
    fig, ax = plt.subplots(figsize=(10, height), dpi=100)
    fig.text(.05, .93, title, fontsize=19, weight="bold")
    fig.text(.05, .875, subtitle, fontsize=12, color=MUTED)
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.set_axisbelow(True)
    ax.tick_params(length=0)
    return fig, ax

def save(fig, slug, alt, caption):
    # Retain editable text and fixed dimensions for standalone export.
    fig.savefig(OUT / f"{slug}.svg", metadata={"Date": None, "Description": alt})
    plt.close(fig)
    block = (f'<!-- chart:{slug}:start -->\n'
             f'<figure class="fig silicon-figure">\n'
             f'<img src="/images/blog/apple-silicon/{slug}.svg" alt="{alt}" loading="lazy" />\n'
             f'<figcaption>{caption}</figcaption>\n</figure>\n'
             f'<!-- chart:{slug}:end -->')
    post = POST.read_text()
    pattern = rf'<!-- chart:{slug}:start -->.*?<!-- chart:{slug}:end -->'
    updated, count = re.subn(pattern, lambda _: block, post, flags=re.S)
    if count != 1:
        raise ValueError(f"Expected one chart placeholder for {slug}, got {count}")
    POST.write_text(updated)

rows = DATA["evolution"]["rows"]
evolution_source = DATA["evolution"]["source"]
for metric, title, limit, ticks, figure in [
    ("single", "Single-thread progress, M1 to M6", 1000, range(0,1001,200), 1),
    ("multi", "Multicore progress, M1 to M6", 6500, range(0,6001,1000), 2),
]:
    fig, ax = canvas(title, "Cinebench 2026.1 · base chips · higher scores are better")
    fig.subplots_adjust(left=.09, right=.95, top=.77, bottom=.25)
    positions = [r["year"] for r in rows]
    values = [r[metric] for r in rows]
    ax.plot(positions, values, color=CYAN, linewidth=2, zorder=3)
    for x, r in zip(positions, rows):
        y = r[metric]
        ax.errorbar(x, y, yerr=[[y-r[f"{metric}_min"]], [r[f"{metric}_max"]-y]],
                    color=CYAN, capsize=5, elinewidth=2, fmt="o", markersize=7,
                    markerfacecolor=BG if r["chip"] == "M6" else CYAN, zorder=4)
        label_y = r[f"{metric}_max"] + limit*.045
        ax.text(x, label_y, number(y), ha="center", fontsize=12, color=TEXT)
    ax.set_xticks(positions, [f'{r["chip"]}\n{r["year"]} · n={r[f"{metric}_n"]}' for r in rows])
    ax.tick_params(axis="x", pad=14)
    ax.set_yticks(list(ticks))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: number(v)))
    ax.set_ylim(0, limit)
    ax.set_xlim(2019.6, 2026.4)
    ax.grid(axis="y", alpha=.85)
    fig.text(.09, .09, "Whiskers: observed minimum–maximum. n: number of results.", fontsize=11, color=MUTED)
    fig.text(.09, .045, "Source: ComputerBase · Sep 21, 2026 · configurations vary", fontsize=10, color=MUTED)
    alt = (f'Cinebench 2026.1, {"single-thread" if metric == "single" else "multicore"}: '
           + "; ".join(f'{r["chip"]}: {number(r[metric])}' for r in rows)
           + ". Only one M6 observation.")
    save(fig, f"evolution-{metric}", alt,
         f'<strong>Figure {figure}.</strong> Community aggregates from '
         f'<a href="{evolution_source}">ComputerBase</a>. '
         'Ranges are not confidence intervals. Lines guide the eye, without measurements between generations.')

source = DATA["comparison"]["source"]
selected = DATA["comparison"]["rows"][:5]
fig, ax = canvas("Single-core performance", "Cinebench 2024 · selected systems · higher is better", 5.8)
fig.subplots_adjust(left=.39, right=.93, top=.77, bottom=.18)
labels = ["Apple M6\nMac mini", "Apple M5\nMacBook Pro 14", "Snapdragon X2 Elite Extreme\nAsus Zenbook A16", "Core Ultra X7 358H\nMinisforum M2 Pro", "Ryzen AI 9 HX 470\nMinisforum AI X1 Pro"]
values = [r["single"] for r in selected]
ax.barh(range(5), values, height=.5, color=[CYAN, BLUE, GRAY, GRAY, GRAY])
ax.set_yticks(range(5), labels, fontsize=12)
ax.tick_params(axis="y", pad=14)
ax.invert_yaxis()
ax.set_xlim(0, 250)
ax.set_xticks(range(0,251,50))
ax.grid(axis="x", alpha=.85)
for i, v in enumerate(values):
    ax.text(v+4, i, str(v), va="center", fontsize=13)
fig.text(.39, .09, "Points", fontsize=11, color=MUTED)
fig.text(.05, .035, "Source: Notebookcheck · Sep 21, 2026", fontsize=10, color=MUTED)
save(fig, "comparison-single", "Single-core scores: M6 221; M5 200; Snapdragon 151; Intel 123; AMD 119 points.",
     f'<strong>Figure 3.</strong> <a href="{source}">Notebookcheck</a>, Cinebench 2024. '
     'Selected systems. Snapdragon variant: X2E-94-100.')

selected = sorted(DATA["comparison"]["rows"], key=lambda r: -r["multi_points_per_watt"])
label_map = {r["chip"]: label for r, label in zip(DATA["comparison"]["rows"][:5], labels)}
label_map["Apple M4 (10-core)"] = "Apple M4\nMacBook Air 13"
fig, ax = canvas("How much work each watt delivers", "Cinebench 2024 multicore · whole-system power", 6.5)
fig.subplots_adjust(left=.39, right=.93, top=.79, bottom=.18)
values = [r["multi_points_per_watt"] for r in selected]
colors = [CYAN if r["chip"] == "Apple M6" else BLUE if r["chip"].startswith("Apple") else GRAY for r in selected]
ax.barh(range(6), values, height=.5, color=colors)
ax.set_yticks(range(6), [label_map[r["chip"]] for r in selected], fontsize=12)
ax.tick_params(axis="y", pad=14)
ax.invert_yaxis()
ax.set_xlim(0, 45)
ax.set_xticks(range(0,41,10))
ax.grid(axis="x", alpha=.85)
for i,v in enumerate(values):
    ax.text(v+.6, i, f"{v:.1f}", va="center", fontsize=13)
fig.text(.39, .10, "Points per watt · higher is better", fontsize=11, color=MUTED)
fig.text(.05, .055, "External-display setup. Not isolated CPU power.", fontsize=11, color=MUTED)
fig.text(.05, .02, "Source: Notebookcheck · Sep 21, 2026", fontsize=10, color=MUTED)
save(fig, "comparison-efficiency", "Multicore points per watt: Air M4 39; M6 32.5; M5 27.5; Snapdragon 22.2; Intel 17.8; AMD 13.4.",
     f'<strong>Figure 4.</strong> <a href="{source}">Notebookcheck</a>. '
     'Cooling, memory, and configuration affect results. This does not measure battery life.')

print(f"Generated four SVG figures in {OUT} and updated {POST.name}")
