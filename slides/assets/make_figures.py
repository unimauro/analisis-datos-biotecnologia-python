"""Genera figuras didácticas para el deck U2 (ADN/ARN/Proteínas). Estilo de marca teal."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import numpy as np

TEAL_DARK = "#08262e"
TEAL = "#158158"
TEAL_MID = "#0c4a50"
CYAN = "#24cbe5"
INK = "#0f2f33"
GREY = "#5b6b6e"

plt.rcParams.update({"font.family": "DejaVu Sans"})


def box(ax, x, y, w, h, label, fc, tc="white", fs=15, sub=None):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.08",
                                fc=fc, ec="none", mutation_scale=1))
    ax.text(x + w / 2, y + h / 2 + (0.06 if sub else 0), label, ha="center", va="center",
            color=tc, fontsize=fs, fontweight="bold")
    if sub:
        ax.text(x + w / 2, y + h / 2 - 0.12, sub, ha="center", va="center", color=tc, fontsize=10)


def arrow(ax, x1, y1, x2, y2, label=None, color=TEAL, lbl_color=INK):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=26,
                                 lw=3, color=color))
    if label:
        ax.text((x1 + x2) / 2, max(y1, y2) + 0.10, label, ha="center", va="bottom",
                color=lbl_color, fontsize=12, fontweight="bold")


# ===== FIG 1: Dogma central ADN -> ARN -> Proteína =====
fig, ax = plt.subplots(figsize=(11, 3.2), dpi=200)
ax.set_xlim(0, 11); ax.set_ylim(0, 3.2); ax.axis("off")
box(ax, 0.4, 1.0, 2.4, 1.2, "ADN", TEAL_DARK, sub="A C G T")
box(ax, 4.3, 1.0, 2.4, 1.2, "ARN", TEAL, sub="A C G U")
box(ax, 8.2, 1.0, 2.4, 1.2, "Proteína", CYAN, tc=INK, sub="20 aminoácidos")
arrow(ax, 2.85, 1.6, 4.25, 1.6, "Transcripción")
arrow(ax, 6.75, 1.6, 8.15, 1.6, "Traducción")
ax.text(5.5, 0.35, "El Dogma Central de la Biología Molecular",
        ha="center", color=GREY, fontsize=12, style="italic")
fig.savefig("fig_dogma.png", bbox_inches="tight", transparent=True)
plt.close(fig)


# ===== FIG 2: ADN como string / pares de bases =====
fig, ax = plt.subplots(figsize=(11, 3.0), dpi=200)
ax.set_xlim(0, 12); ax.set_ylim(0, 3); ax.axis("off")
seq = "A T G C T A G C T A"
comp = "T A C G A T C G A T"
pair = {"A": CYAN, "T": TEAL, "G": TEAL_DARK, "C": "#3a8f6f"}
for i, (a, b) in enumerate(zip(seq.split(), comp.split())):
    x = 0.8 + i * 1.08
    ax.add_patch(Circle((x, 2.2), 0.34, fc=pair[a], ec="white", lw=2))
    ax.text(x, 2.2, a, ha="center", va="center", color="white", fontsize=14, fontweight="bold")
    ax.add_patch(Circle((x, 0.7), 0.34, fc=pair[b], ec="white", lw=2))
    ax.text(x, 0.7, b, ha="center", va="center", color="white", fontsize=14, fontweight="bold")
    ax.plot([x, x], [1.86, 1.04], color=GREY, lw=2, ls=":")
ax.text(0.1, 2.2, "5'", ha="center", va="center", color=INK, fontsize=13, fontweight="bold")
ax.text(0.1, 0.7, "3'", ha="center", va="center", color=INK, fontsize=13, fontweight="bold")
ax.text(6.0, 0.05, "Cadena y su complementaria  ·  A–T   G–C",
        ha="center", color=GREY, fontsize=12, style="italic")
fig.savefig("fig_bases.png", bbox_inches="tight", transparent=True)
plt.close(fig)


# ===== FIG 3: Contenido GC (barra) =====
fig, ax = plt.subplots(figsize=(7.5, 4.2), dpi=200)
genes = ["Gen A", "Gen B", "Gen C", "Gen D"]
gc = [42, 61, 38, 55]
colors = [TEAL if v < 50 else CYAN for v in gc]
bars = ax.bar(genes, gc, color=colors, width=0.6, zorder=3)
ax.axhline(50, color=GREY, ls="--", lw=1.5, zorder=2)
ax.text(3.45, 51, "50%", color=GREY, fontsize=11, va="bottom", ha="right")
for b, v in zip(bars, gc):
    ax.text(b.get_x() + b.get_width() / 2, v + 1.5, f"{v}%", ha="center",
            color=INK, fontsize=13, fontweight="bold")
ax.set_ylim(0, 75); ax.set_ylabel("Contenido GC (%)", fontsize=12, color=INK)
ax.set_title("Contenido GC por gen", fontsize=15, fontweight="bold", color=TEAL_DARK)
ax.spines[["top", "right"]].set_visible(False)
ax.tick_params(colors=INK)
ax.grid(axis="y", alpha=0.25, zorder=0)
fig.savefig("fig_gc.png", bbox_inches="tight", transparent=True)
plt.close(fig)


# ===== FIG 4: Doble hélice estilizada =====
fig, ax = plt.subplots(figsize=(4.5, 6.5), dpi=200)
ax.set_xlim(-2, 2); ax.set_ylim(0, 12); ax.axis("off")
t = np.linspace(0, 4 * np.pi, 400)
x1 = np.sin(t); x2 = np.sin(t + np.pi); y = np.linspace(0, 12, 400)
ax.plot(x1, y, color=CYAN, lw=5, solid_capstyle="round")
ax.plot(x2, y, color=TEAL, lw=5, solid_capstyle="round")
for i in range(0, 400, 16):
    ax.plot([x1[i], x2[i]], [y[i], y[i]], color=GREY, lw=2, alpha=0.7)
fig.savefig("fig_helix.png", bbox_inches="tight", transparent=True)
plt.close(fig)


# ===== FIG 5: Codón -> aminoácido (tabla mini) =====
fig, ax = plt.subplots(figsize=(11, 3.0), dpi=200)
ax.set_xlim(0, 12); ax.set_ylim(0, 3); ax.axis("off")
codons = [("AUG", "Met\n(inicio)", TEAL_DARK), ("UUU", "Phe", TEAL),
          ("GGC", "Gly", "#3a8f6f"), ("UAA", "STOP", "#b23b3b")]
for i, (cod, aa, c) in enumerate(codons):
    x = 0.6 + i * 3.0
    box(ax, x, 1.3, 1.3, 1.1, cod, c, fs=16)
    arrow(ax, x + 1.35, 1.85, x + 2.05, 1.85, color=GREY)
    ax.text(x + 2.45, 1.85, aa, ha="center", va="center", color=INK, fontsize=12, fontweight="bold")
ax.text(6, 0.4, "El código genético: 3 bases (1 codón) → 1 aminoácido",
        ha="center", color=GREY, fontsize=12, style="italic")
fig.savefig("fig_codones.png", bbox_inches="tight", transparent=True)
plt.close(fig)


# ===== FIG 6: Pipeline mutación (caso salud) =====
fig, ax = plt.subplots(figsize=(11, 2.6), dpi=200)
ax.set_xlim(0, 12); ax.set_ylim(0, 2.6); ax.axis("off")
steps = [("FASTA\ngen", TEAL_DARK), ("Leer con\nBiopython", TEAL),
         ("Comparar\nvs. referencia", "#3a8f6f"), ("Detectar\nmutación", CYAN),
         ("Interpretar\nen salud", "#b23b3b")]
w = 1.9
for i, (lbl, c) in enumerate(steps):
    x = 0.3 + i * 2.35
    tc = "white" if c != CYAN else INK
    box(ax, x, 0.8, w, 1.1, lbl, c, tc=tc, fs=12)
    if i < len(steps) - 1:
        arrow(ax, x + w, 1.35, x + w + 0.45, 1.35, color=GREY)
fig.savefig("fig_pipeline.png", bbox_inches="tight", transparent=True)
plt.close(fig)

print("OK figuras: dogma, bases, gc, helix, codones, pipeline")
