"""Shared visual style + drawing helpers. All coordinates in pixels (1920x1080, y downward)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, FancyArrowPatch, Circle, Wedge
import numpy as np

W, H = 1920, 1080
BG = "#0F172A"      # fond sombre unique
PANEL = "#1E293B"
FG = "#E2E8F0"      # texte
MUTED = "#94A3B8"
PRIMARY = "#38BDF8" # couleur principale
ACCENT = "#FBBF24"  # couleur d'accent (surbrillance)
GRID = "#334155"

COURSE = "5ANA1D – Analyse de données – Ch. 1"

plt.rcParams.update({
    "font.family": "Inter",
    "mathtext.fontset": "custom",
    "mathtext.rm": "Inter",
    "mathtext.it": "Inter:italic",
    "mathtext.bf": "Inter:bold",
    "mathtext.sf": "Inter",
    "axes.unicode_minus": True,
})

PT = 72 / 100  # px -> pt at dpi 100


class Canvas:
    def __init__(self, notion=None, part=None):
        self.fig = plt.figure(figsize=(W / 100, H / 100), dpi=100, facecolor=BG)
        self.ax = self.fig.add_axes([0, 0, 1, 1])
        self.ax.set_xlim(0, W)
        self.ax.set_ylim(H, 0)
        self.ax.axis("off")
        self.ax.set_facecolor(BG)
        self._r = None
        if notion is not None:
            self.banner(notion, part)

    # ---------- basics
    @property
    def renderer(self):
        if self._r is None:
            self._r = self.fig.canvas.get_renderer()
        return self._r

    def text(self, x, y, s, size=40, color=FG, ha="left", va="center", weight="normal", alpha=1, z=5, style="normal"):
        assert size >= 36, f"text too small: {s}"
        return self.ax.text(x, y, s, fontsize=size * PT, color=color, ha=ha, va=va,
                            fontweight=weight, alpha=alpha, zorder=z, fontstyle=style)

    def width(self, artist):
        bb = artist.get_window_extent(renderer=self.renderer)
        return bb.width  # pixels (dpi 100, figure px == data px horizontally)

    def title(self, s, sub=None):
        self.text(80, 85, s, size=60, weight="bold", color=FG)
        self.ax.plot([80, 200], [130, 130], color=PRIMARY, lw=5, solid_capstyle="round")
        if sub:
            self.text(80, 175, sub, size=38, color=MUTED)

    def banner(self, notion, part=None):
        self.ax.plot([0, W], [1012, 1012], color=GRID, lw=1.5)
        label = COURSE + (f" – Partie {part}" if part else "")
        self.text(60, 1047, label, size=36, color=MUTED)
        if notion:
            self.text(W - 60, 1047, notion, size=36, color=MUTED, ha="right")

    def box(self, x, y, w, h, fc=PANEL, ec=None, lw=3, r=18, z=2, alpha=1):
        p = FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}",
                           fc=fc, ec=ec or fc, lw=lw, zorder=z, alpha=alpha)
        self.ax.add_patch(p)
        return p

    def chip(self, cx, cy, s, size=44, fc=PANEL, ec=None, color=FG, padx=26, h=None, weight="normal", minw=0):
        t = self.text(cx, cy, s, size=size, color=color, ha="center", weight=weight, z=6)
        w = max(self.width(t) + 2 * padx, minw)
        h = h or size * 1.7
        self.box(cx - w / 2, cy - h / 2, w, h, fc=fc, ec=ec, z=3)
        return w

    def arrow(self, x1, y1, x2, y2, color=MUTED, lw=3, head=22, z=4, style="-|>"):
        a = FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=f"{style},head_length={head*0.04},head_width={head*0.025}",
                            mutation_scale=40, color=color, lw=lw, zorder=z, shrinkA=0, shrinkB=0)
        self.ax.add_patch(a)

    def line(self, xs, ys, color=MUTED, lw=3, ls="-", z=4):
        self.ax.plot(xs, ys, color=color, lw=lw, ls=ls, zorder=z, solid_capstyle="round")

    # ---------- formulas made of parts, so a part can be highlighted
    def formula(self, parts, x, y, size=64, hl=(), ha="center", color=FG, hlcolor=ACCENT, gap=10):
        """parts: list of strings (mathtext allowed). hl: indices of parts to highlight."""
        arts, widths = [], []
        for p in parts:
            t = self.ax.text(0, y, p, fontsize=size * PT, color=color, ha="left", va="baseline", zorder=6)
            arts.append(t)
            widths.append(self.width(t))
        total = sum(widths) + gap * (len(parts) - 1)
        x0 = {"center": x - total / 2, "left": x, "right": x - total}[ha]
        cur = x0
        for i, (t, w) in enumerate(zip(arts, widths)):
            t.set_x(cur)
            if i in hl:
                t.set_color(hlcolor)
                bb = t.get_window_extent(renderer=self.renderer)
                # window coords -> data coords (y flipped)
                y_top = H - bb.y1
                y_bot = H - bb.y0
                self.box(cur - 10, y_top - 10, w + 20, (y_bot - y_top) + 20, fc="#3B2F0B", ec=hlcolor, lw=2, r=12, z=3)
            cur += w + gap
        return x0, total

    def retenir(self, s_lines, title="À retenir"):
        """Centered key-takeaway box (lines: list of str, may contain mathtext)."""
        n = len(s_lines)
        h = 150 + n * 80
        y0 = 540 - h / 2 - 20
        self.box(260, y0, 1400, h, fc=PANEL, ec=ACCENT, lw=4, r=28)
        self.text(W / 2, y0 + 70, title, size=46, color=ACCENT, ha="center", weight="bold")
        for i, s in enumerate(s_lines):
            self.text(W / 2, y0 + 155 + i * 80, s, size=44, color=FG, ha="center")

    # ---------- table
    def table(self, x, y, headers, rows, colw, rowh=66, size=40, hl_rows=(), hl_cols=(), hl_cells=(),
              show_cols=None, show_rows=None, total=None, header_color=PRIMARY):
        """Draw a clean table. headers/rows contain strings (mathtext ok)."""
        ncol = len(headers)
        show_cols = range(ncol) if show_cols is None else show_cols
        nrow = len(rows) if show_rows is None else show_rows
        tw = sum(colw)
        th = rowh * (1 + len(rows) + (1 if total else 0))
        self.box(x - 10, y - 10, tw + 20, th + 20, fc=PANEL, r=14, z=1)
        xs = np.cumsum([0] + colw) + x
        # header
        for j, hd in enumerate(headers):
            if j in show_cols:
                self.text((xs[j] + xs[j + 1]) / 2, y + rowh / 2, hd, size=size, color=header_color, ha="center", weight="bold")
        self.line([x, x + tw], [y + rowh, y + rowh], color=GRID, lw=2)
        for i, r in enumerate(rows):
            yy = y + rowh * (i + 1)
            if i in hl_rows:
                self.box(x - 4, yy + 4, tw + 8, rowh - 8, fc="#3B2F0B", ec=ACCENT, lw=2, r=10, z=2)
            for j, c in enumerate(r):
                if j not in show_cols or i >= nrow:
                    continue
                col = FG
                if j in hl_cols or (i, j) in hl_cells or i in hl_rows:
                    col = ACCENT
                if (i, j) in hl_cells:
                    self.box(xs[j] + 6, yy + 6, colw[j] - 12, rowh - 12, fc="#3B2F0B", ec=ACCENT, lw=2, r=10, z=2)
                self.text((xs[j] + xs[j + 1]) / 2, yy + rowh / 2, c, size=size, color=col, ha="center")
        if total:
            yy = y + rowh * (len(rows) + 1)
            self.line([x, x + tw], [yy, yy], color=GRID, lw=2)
            for j, c in enumerate(total):
                if j in show_cols and c:
                    self.text((xs[j] + xs[j + 1]) / 2, yy + rowh / 2, c, size=size, color=MUTED, ha="center")
        for j in range(1, ncol):
            self.line([xs[j], xs[j]], [y + 8, y + th - 8], color=GRID, lw=1.5)
        return xs

    # ---------- chart axes in pixel rect
    def chart(self, x, y, w, h, xlim, ylim, xticks=None, yticks=None, xlabel=None, ylabel=None,
              xticklabels=None, yticklabels=None):
        a = self.fig.add_axes([x / W, 1 - (y + h) / H, w / W, h / H])
        a.set_facecolor(BG)
        a.set_xlim(*xlim)
        a.set_ylim(*ylim)
        for s in ["top", "right"]:
            a.spines[s].set_visible(False)
        for s in ["left", "bottom"]:
            a.spines[s].set_color(MUTED)
            a.spines[s].set_linewidth(2.5)
        a.tick_params(colors=MUTED, labelsize=36 * PT, width=2, length=8)
        if xticks is not None:
            a.set_xticks(xticks)
        if yticks is not None:
            a.set_yticks(yticks)
        if xticklabels is not None:
            a.set_xticklabels(xticklabels)
        if yticklabels is not None:
            a.set_yticklabels(yticklabels)
        for lab in a.get_xticklabels() + a.get_yticklabels():
            lab.set_color(FG)
        if xlabel:
            a.set_xlabel(xlabel, color=FG, fontsize=38 * PT, loc="right")
        if ylabel:
            a.set_ylabel(ylabel, color=FG, fontsize=38 * PT, rotation=0, loc="top", labelpad=-10)
            a.yaxis.set_label_coords(-0.02, 1.06)
        a.grid(axis="y", color=GRID, lw=1, alpha=0.6)
        a.set_axisbelow(True)
        return a

    def save(self, path):
        self.fig.savefig(path, dpi=100, facecolor=BG)
        plt.close(self.fig)
