"""Render the article's figures from the checked-in aggregates.

Run from any directory: MPLCONFIGDIR=/tmp/matplotlib python3 path/to/generate.py
Requires matplotlib. No network requests or npm dependencies.
"""
import csv
import re
from collections import defaultdict
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SLUG = "costa-rica-crime"
OUT = ROOT / "public/images/blog" / SLUG
POST = ROOT / "src/content/blog/datos-criminalidad-costa-rica-dos-historias.md"
OUT.mkdir(parents=True, exist_ok=True)

BG, TEXT, MUTED, GRID = "#111827", "#f8fafc", "#b5c3d7", "#273244"
BLUE, CYAN, GRAY, DIM, VIOLET = "#4f8cff", "#35d6ff", "#7187a5", "#46556b", "#a78bfa"
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 12,
    "text.color": TEXT, "axes.labelcolor": MUTED,
    "xtick.color": MUTED, "ytick.color": MUTED,
    "axes.facecolor": BG, "figure.facecolor": BG,
    "axes.edgecolor": GRID, "grid.color": GRID,
    "svg.fonttype": "none", "svg.hashsalt": "costa-rica-crime-2026",
})
SOURCE = "Fuente: Poder Judicial de Costa Rica, Estadísticas Policiales (datos abiertos) · consultado el 9 oct 2026"
NAMES = {
    "HOMICIDIO": "Homicidio", "ASALTO": "Asalto", "ROBO": "Robo",
    "HURTO": "Hurto", "ROBO DE VEHICULO": "Robo de vehículo", "TACHA DE VEHICULO": "Tacha de vehículo",
}
PROVINCES = {"SAN JOSE": "San José", "ALAJUELA": "Alajuela", "CARTAGO": "Cartago", "HEREDIA": "Heredia",
             "GUANACASTE": "Guanacaste", "PUNTARENAS": "Puntarenas", "LIMON": "Limón"}

def read(name):
    with open(HERE / name, newline="") as fh:
        return list(csv.DictReader(fh))

monthly, province, subtype = read("monthly.csv"), read("province.csv"), read("subtype.csv")

def number(value):
    # Costa Rican convention: period for thousands.
    return f"{value:,.0f}".replace(",", ".")

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
             f'<figure class="fig chart-figure">\n'
             f'<img src="/images/blog/{SLUG}/{slug}.svg" alt="{alt}" loading="lazy" />\n'
             f'<figcaption>{caption}</figcaption>\n</figure>\n'
             f'<!-- chart:{slug}:end -->')
    post = POST.read_text()
    pattern = rf'<!-- chart:{slug}:start -->.*?<!-- chart:{slug}:end -->'
    updated, count = re.subn(pattern, lambda _: block, post, flags=re.S)
    if count != 1:
        raise ValueError(f"Expected one chart placeholder for {slug}, got {count}")
    POST.write_text(updated)

# Figure 1: every category against its own 2015 level, January to September.
jan_sep = defaultdict(int)
for r in monthly:
    if int(r["month"][5:7]) <= 9:
        jan_sep[(int(r["year"]), r["crime"])] += int(r["records"])
years = sorted({y for y, _ in jan_sep})
order = ["TACHA DE VEHICULO", "HURTO", "ROBO", "ASALTO", "ROBO DE VEHICULO", "HOMICIDIO"]
colors = {"HOMICIDIO": CYAN, "ROBO DE VEHICULO": BLUE}
fig, ax = canvas("Los homicidios subieron mientras casi todo lo demás bajó",
                 "Registros de enero a septiembre de cada año · 2015 = 100", 6.2)
fig.subplots_adjust(left=.08, right=.74, top=.79, bottom=.16)
ends = []
for crime in order:
    index = [jan_sep[(y, crime)] / jan_sep[(2015, crime)] * 100 for y in years]
    color = colors.get(crime, GRAY)
    ax.plot(years, index, color=color, linewidth=2.6 if crime in colors else 1.6, zorder=3 if crime in colors else 2,
            solid_capstyle="round", solid_joinstyle="round")
    if crime in colors:
        ax.scatter(years, index, color=color, s=22, zorder=4)
    ends.append([index[-1], index[-1], crime, color])
ax.axhline(100, color=MUTED, linewidth=1, linestyle=(0, (4, 3)), zorder=1)
# Spread the end labels so none overlap.
ends.sort()
for _ in range(50):
    for i in range(1, len(ends)):
        gap = ends[i][1] - ends[i - 1][1]
        if gap < 9:
            ends[i][1] += (9 - gap) / 2
            ends[i - 1][1] -= (9 - gap) / 2
for value, y, crime, color in ends:
    ax.text(years[-1] + .35, y, f"{NAMES[crime]} {value:.0f}", va="center", fontsize=12,
            color=TEXT if crime in colors else MUTED, weight="bold" if crime in colors else "normal", clip_on=False)
ax.set_xticks(years, [str(y) if y % 2 == 1 or y == years[-1] else "" for y in years])
ax.set_xlim(years[0] - .3, years[-1] + .3)
ax.set_ylim(40, 190)
ax.set_yticks(range(50, 191, 25))
ax.grid(axis="y", alpha=.85)
fig.text(.08, .065, "Comparar enero a septiembre permite incluir 2026, con datos hasta el 30 de septiembre.", fontsize=11, color=MUTED)
fig.text(.08, .025, SOURCE, fontsize=10, color=MUTED)
summary = "; ".join(f"{NAMES[c]} {jan_sep[(years[-1], c)] / jan_sep[(2015, c)] * 100:.0f}" for c in reversed(order))
save(fig, "index", f"Índice de registros de enero a septiembre, 2015 = 100, valor en 2026: {summary}.",
     "<strong>Figura 1.</strong> Cada línea compara los registros de una categoría con su propio nivel de 2015, para que categorías de tamaños muy distintos compartan una escala.")

# Figure 2: homicides by recorded motive, complete years.
groups = [
    ("Ajuste de cuentas o venganza", {"AJUSTE DE CUENTAS/VENGANZA"}, CYAN),
    ("Discusión o riña", {"DISCUSION/RIÑA"}, BLUE),
    ("Al cometer otro delito", {"POR LA COMISION DE OTRO DELITO"}, VIOLET),
    ("Otros móviles registrados", {"VIOLENCIA DOMESTICA", "FEMICIDIO", "REPELIENDO ACTIVIDAD CRIMINAL", "PROFESIONAL", "IDEOLOGICO"}, GRAY),
    ("Indeterminado", {"OTRO O INDETERMINADO", "NO DETERMINADO", "DESCONOCIDO"}, DIM),
]
full_years = list(range(2015, 2026))
by_group = {name: [0] * len(full_years) for name, _, _ in groups}
for r in subtype:
    y = int(r["year"])
    if r["crime"] != "HOMICIDIO" or y not in full_years:
        continue
    for name, members, _ in groups:
        if r["subtype"] in members:
            by_group[name][full_years.index(y)] += int(r["records"])
fig, ax = canvas("La mayor parte del aumento viene de un solo móvil", "Registros de homicidio por año, según el móvil anotado por los investigadores", 6.2)
fig.subplots_adjust(left=.08, right=.97, top=.70, bottom=.16)
bottom = [0] * len(full_years)
for name, _, color in groups:
    ax.bar(full_years, by_group[name], bottom=bottom, width=.62, color=color, edgecolor=BG, linewidth=1.2, label=name)
    bottom = [b + v for b, v in zip(bottom, by_group[name])]
for x, total in zip(full_years, bottom):
    ax.text(x, total + 18, number(total), ha="center", fontsize=11, color=MUTED)
for i in (0, len(full_years) - 1):
    v = by_group["Ajuste de cuentas o venganza"][i]
    ax.text(full_years[i], v / 2, number(v), ha="center", va="center", fontsize=12, color=BG, weight="bold")
ax.legend(loc="lower left", bbox_to_anchor=(0, 1.0), ncol=3, frameon=False, fontsize=11, labelcolor=MUTED,
          handlelength=1, handleheight=1, borderaxespad=.3, columnspacing=1.4)
ax.set_xticks(full_years, [str(y) for y in full_years])
ax.set_ylim(0, 1150)
ax.set_yticks(range(0, 1001, 250))
ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: number(v)))
ax.grid(axis="y", alpha=.85)
fig.text(.08, .065, "Registros de los datos abiertos, que superan los totales anunciados por el OIJ (ver texto).", fontsize=11, color=MUTED)
fig.text(.08, .025, SOURCE, fontsize=10, color=MUTED)
s = by_group["Ajuste de cuentas o venganza"]
u = by_group["Indeterminado"]
save(fig, "homicide-motives",
     f"Registros de homicidio por móvil, 2015 a 2025. Ajuste de cuentas o venganza: {s[0]} en 2015, {s[-1]} en 2025. Indeterminado: {u[0]} en 2015, {u[-1]} en 2025. Totales: {bottom[0]} en 2015, {bottom[-1]} en 2025.",
     "<strong>Figura 2.</strong> Solo años completos. «Indeterminado» agrupa tres etiquetas que el archivo usa para un móvil desconocido.")

# Figure 3: homicides by province, 2015 against 2025.
hom = {(r["province"], int(r["year"])): int(r["records"]) for r in province if r["crime"] == "HOMICIDIO"}
provs = sorted(PROVINCES, key=lambda p: hom.get((p, 2025), 0))
fig, ax = canvas("Todas las provincias menos Heredia cerraron 2025 más arriba", "Registros de homicidio por año, 2015 y 2025", 5.8)
fig.subplots_adjust(left=.17, right=.93, top=.73, bottom=.16)
for i, p in enumerate(provs):
    a, b = hom.get((p, 2015), 0), hom.get((p, 2025), 0)
    ax.plot([a, b], [i, i], color=GRAY, linewidth=2, zorder=2, solid_capstyle="round")
    ax.scatter([a], [i], s=70, color=BG, edgecolor=GRAY, linewidth=2, zorder=3)
    ax.scatter([b], [i], s=70, color=CYAN, zorder=4)
    if a == b:
        ax.text(b + 7, i, f"{number(b)} en ambos años", ha="left", va="center", fontsize=11, color=TEXT)
        continue
    lo, hi = (a, b) if a < b else (b, a)
    ax.text(lo - 7, i, number(lo), ha="right", va="center", fontsize=11, color=MUTED if lo == a else TEXT)
    ax.text(hi + 7, i, number(hi), ha="left", va="center", fontsize=11, color=TEXT if hi == b else MUTED)
ax.set_yticks(range(len(provs)), [PROVINCES[p] for p in provs], fontsize=12)
ax.set_xlim(0, 380)
ax.set_xticks(range(0, 351, 50))
ax.grid(axis="x", alpha=.85)
ax.scatter([], [], s=70, color=BG, edgecolor=GRAY, linewidth=2, label="2015")
ax.scatter([], [], s=70, color=CYAN, label="2025")
ax.legend(loc="lower left", bbox_to_anchor=(0, 1.0), ncol=2, frameon=False, fontsize=11, labelcolor=MUTED, borderaxespad=.3)
fig.text(.17, .065, "Registros de los datos abiertos. La provincia es donde se registró el homicidio.", fontsize=11, color=MUTED)
fig.text(.05, .025, SOURCE, fontsize=10, color=MUTED)
save(fig, "homicide-provinces",
     "Registros de homicidio por provincia, 2015 a 2025: " + "; ".join(f"{PROVINCES[p]} de {hom.get((p, 2015), 0)} a {hom.get((p, 2025), 0)}" for p in reversed(provs)) + ".",
     "<strong>Figura 3.</strong> Solo años completos. Los círculos vacíos son 2015 y los llenos, 2025.")

# Figure 4: homicides per month with a 12-month average.
series = sorted((r["month"], int(r["records"])) for r in monthly if r["crime"] == "HOMICIDIO")
values = [v for _, v in series]
avg = [sum(values[i - 11:i + 1]) / 12 if i >= 11 else None for i in range(len(values))]
x = list(range(len(series)))
fig, ax = canvas("El salto de 2023 y un 2026 más bajo hasta ahora", "Registros de homicidio por mes · línea: promedio de los últimos 12 meses", 5.8)
fig.subplots_adjust(left=.08, right=.97, top=.79, bottom=.16)
ax.bar(x, values, width=.75, color=CYAN, alpha=.35, linewidth=0)
ax.plot([i for i in x if avg[i] is not None], [a for a in avg if a is not None], color=CYAN, linewidth=2.4,
        solid_capstyle="round", solid_joinstyle="round")
jan = [i for i, (m, _) in enumerate(series) if m.endswith("-01")]
ax.set_xticks(jan, [series[i][0][:4] for i in jan])
ax.set_xlim(-1, len(series))
ax.set_ylim(0, 135)
ax.set_yticks(range(0, 126, 25))
ax.grid(axis="y", alpha=.85)
peak = max(range(len(values)), key=values.__getitem__)
ax.annotate(f"{number(values[peak])} en feb 2024", (peak, values[peak]), xytext=(peak - 30, values[peak] + 4),
            fontsize=11, color=MUTED, va="center", arrowprops=dict(arrowstyle="-", color=MUTED, lw=1))
fig.text(.08, .065, "2026 llega hasta el 30 de septiembre.", fontsize=11, color=MUTED)
fig.text(.08, .025, SOURCE, fontsize=10, color=MUTED)
save(fig, "homicides-monthly",
     f"Registros mensuales de homicidio, enero 2015 a septiembre 2026. El promedio de 12 meses es {avg[-1]:.0f} en septiembre de 2026, frente a {avg[series.index(next(s for s in series if s[0] == '2024-09'))]:.0f} en septiembre de 2024. Máximo: {values[peak]} en febrero de 2024.",
     "<strong>Figura 4.</strong> Cada barra es un mes. La línea suaviza la variación de un mes a otro.")

print(f"Generated four SVG figures in {OUT} and updated {POST.name}")
