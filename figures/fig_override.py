#!/usr/bin/env python3
"""
Figure 1 - Override-direction agreement for number-transparent quantificational nouns.

One panel, x-axis = proportion plural agreement (0 = all singular, 1 = all plural).
Each row is a QN+complement combination, coloured by predicted direction. 95% Wilson
binomial CIs as horizontal bars. Reference line at 0.5 (chance). Sample sizes
annotated.

Data: COCA pilot, May 2026. See paper/data/coca-pilot.md.
"""

from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np

HOUSE = Path(__file__).resolve().parents[3] / '.house-style'
sys.path.insert(0, str(HOUSE))
from plot_style import setup, COLORS, save_figure


def wilson_ci(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    """Wilson score interval for a binomial proportion."""
    if n == 0:
        return (0.0, 0.0)
    p = k / n
    denom = 1.0 + z**2 / n
    centre = (p + z**2 / (2 * n)) / denom
    half = (z / denom) * np.sqrt(p * (1 - p) / n + z**2 / (4 * n**2))
    return (centre - half, centre + half)


# (label, plural_count, singular_count, predicted_direction)
# Predicted-singular rows on the bottom; predicted-plural rows on the top.
# Counter-direction cells are KWIC-filtered where contexts were checked. The
# large *a lot of people is/was* cell remains raw and conservative.
DATA = [
    # Predicted singular (non-count complement)
    ('the rest of the money',   0,    19,  'sg'),
    ('plenty of money',         0,    6,   'sg'),
    ('lots of money',           0,    24,  'sg'),
    ('a lot of money',          1,    90,  'sg'),
    # Predicted plural (plural complement)
    ('a number of people',      100,  0,   'pl'),
    ('a lot of people',         4195, 85,  'pl'),
    ('lots of people',          348,  0,   'pl'),
    ('plenty of people',        79,   0,   'pl'),
    ('the rest of the people',  19,   0,   'pl'),
]


def make_figure() -> plt.Figure:
    setup(font_size=10, title_size=11, tick_size=9, legend_size=9)
    # Match math text to body serif (otherwise mathtext defaults to DejaVu Sans)
    plt.rcParams['mathtext.fontset'] = 'custom'
    plt.rcParams['mathtext.rm'] = 'serif'
    plt.rcParams['mathtext.it'] = 'serif:italic'
    plt.rcParams['mathtext.bf'] = 'serif:bold'

    fig, ax = plt.subplots(figsize=(7.0, 4.5))

    labels = [r[0] for r in DATA]
    pl_counts = [r[1] for r in DATA]
    sg_counts = [r[2] for r in DATA]
    predicted = [r[3] for r in DATA]
    ns = [p + s for p, s in zip(pl_counts, sg_counts)]
    prop_pl = [p / n for p, n in zip(pl_counts, ns)]
    cis = [wilson_ci(p, n) for p, n in zip(pl_counts, ns)]

    ys = np.arange(len(DATA))

    # Predicted-direction zone shading
    ax.axvspan(0.0, 0.5, color=COLORS['light'], alpha=0.4, zorder=0)
    ax.axvspan(0.5, 1.0, color=COLORS['light'], alpha=0.0, zorder=0)
    ax.axvline(0.5, color=COLORS['dark'], linewidth=0.6, zorder=1)

    # CI error bars and points, coloured by predicted direction
    colour_map = {'sg': COLORS['secondary'], 'pl': COLORS['primary']}
    for y, prop, (lo, hi), pred in zip(ys, prop_pl, cis, predicted):
        c = colour_map[pred]
        ax.plot([lo, hi], [y, y], color=c, linewidth=1.4, zorder=2)
    for y, prop, pred in zip(ys, prop_pl, predicted):
        c = colour_map[pred]
        ax.scatter(prop, y, s=36, color=c, edgecolor='white', linewidths=0.6, zorder=3)

    # Sample-size annotations to the right (math mode)
    for y, n in zip(ys, ns):
        n_str = f'{n:,}'.replace(',', '{,}')
        ax.text(1.04, y, f'$n = {n_str}$',
                ha='left', va='center', fontsize=8.5, color=COLORS['dark'])

    # Y labels (italic)
    ax.set_yticks(ys)
    ax.set_yticklabels(labels)
    for tick in ax.get_yticklabels():
        tick.set_fontstyle('italic')
    ax.set_ylim(-0.7, len(DATA) - 0.3)

    # Group separator between predicted-singular and predicted-plural rows
    n_sg = sum(1 for p in predicted if p == 'sg')
    ax.axhline(n_sg - 0.5, color=COLORS['light'], linewidth=0.6, zorder=1)

    # X axis
    ax.set_xlabel('Proportion plural agreement')
    ax.set_xlim(0.0, 1.18)
    ax.set_xticks([0.0, 0.25, 0.5, 0.75, 1.0])
    ax.set_xticklabels(['0', '0.25', '0.5', '0.75', '1.0'])

    # Zone labels above the plot
    ax.text(0.25, len(DATA) - 0.2, 'predicted singular',
            ha='center', va='bottom', fontsize=8.5,
            color=COLORS['secondary'])
    ax.text(0.75, len(DATA) - 0.2, 'predicted plural',
            ha='center', va='bottom', fontsize=8.5,
            color=COLORS['primary'])

    fig.subplots_adjust(left=0.24, right=0.96, top=0.92, bottom=0.12)
    return fig


if __name__ == '__main__':
    fig = make_figure()
    out_dir = Path(__file__).resolve().parent
    save_figure(fig, out_dir / 'fig_override')
