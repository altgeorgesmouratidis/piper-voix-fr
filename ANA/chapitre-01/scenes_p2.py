"""Partie 2 : données continues + qualitatives."""
from style import *
from matplotlib.patches import Rectangle as R

CL = [(50, 65), (65, 75), (75, 85), (85, 100)]
NI = [20, 28, 20, 12]
NC = [20, 48, 68, 80]
FI = [0.25, 0.35, 0.25, 0.15]
FC = [0.25, 0.60, 0.85, 1.0]
DN = [20 / 15, 2.8, 2.0, 0.8]
DF = [0.25 / 15, 0.035, 0.025, 0.01]
CLS = ["[50, 65[", "[65, 75[", "[75, 85[", "[85, 100["]


def fr(v, d=2):
    return f"{v:.{d}f}".replace(".", ",")


def F(x):
    acc = 0
    for (a, b), f in zip(CL, FI):
        if x < a:
            return acc
        if x < b:
            return acc + f * (x - a) / (b - a)
        acc += f
    return 1.0


SCENES = []


def scene(id, notion, beats):
    def deco(fn):
        SCENES.append(dict(id=id, part=2, notion=notion, beats=beats, draw=fn))
        return fn
    return deco


def poly(c, x=140, y=250, w=1000, h=620, vmarks=(), hmarks=(), hl_class=None, seg=None, full=True):
    a = c.chart(x, y, w, h, (45, 105), (0, 1.08), xticks=[50, 65, 75, 85, 100],
                yticks=[0, 0.25, 0.6, 0.85, 1], yticklabels=["0", "0,25", "0,60", "0,85", "1"],
                xlabel=r"$x$ (kg)", ylabel=r"$F(x)$")
    xs = [45, 50, 65, 75, 85, 100, 105]
    ys = [F(v) for v in xs]
    if full:
        a.plot(xs, ys, color=PRIMARY, lw=6, zorder=4)
        a.plot([50, 65, 75, 85, 100], [0, .25, .6, .85, 1], "o", ms=12, color=PRIMARY, zorder=5)
    if seg is not None:
        (x0, x1) = CL[seg]
        a.plot([x0, x1], [F(x0), F(x1)], color=ACCENT, lw=8, zorder=6)
    if hl_class is not None:
        x0, x1 = CL[hl_class]
        a.axvspan(x0, x1, color=ACCENT, alpha=0.12, zorder=1)
    for (xv, yv) in vmarks:
        a.plot([xv, xv], [0, yv], ls="--", color=ACCENT, lw=3, zorder=6)
        a.plot([45, xv], [yv, yv], ls="--", color=ACCENT, lw=3, zorder=6)
        a.plot(xv, yv, "o", ms=16, color=ACCENT, zorder=7)
    return a


# ------------------------------------------------------------------ titre / intro
@scene("p2_00_titre", "Introduction", [
    "Analyse de données, chapitre 1, deuxième partie : les données continues et les données qualitatives.",
])
def _(c, s):
    c.text(960, 330, "5ANA1D · Analyse de données", size=44, color=PRIMARY, ha="center")
    c.text(960, 450, "Chapitre 1", size=60, color=MUTED, ha="center")
    c.text(960, 560, "Statistique descriptive", size=96, weight="bold", ha="center")
    c.line([860, 1060], [640, 640], color=PRIMARY, lw=6)
    c.text(960, 730, "Partie 2 — Données continues et qualitatives", size=48, ha="center")


@scene("p2_01_intro", "Introduction", [
    "Cette fois, Alice pèse 80 étudiants, avec une balance précise au dixième de gramme.",
    "Problème : deux mesures identiques, c'est presque impossible. Le tableau aurait 80 lignes, avec uniquement des 1 dans la colonne n i.",
    "La solution : regrouper les valeurs en classes. Au programme : les classes, la densité, le polygone des fréquences cumulées, ses usages, et les données qualitatives.",
])
def _(c, s):
    c.title("80 étudiants sur la balance")
    vals = ["72,3184", "65,0412", "81,7765", "58,2209", "77,9031", "69,4458"]
    for k, v in enumerate(vals):
        c.chip(330 + k * 252, 300, v, size=40, minw=230, padx=8)
    if s >= 1:
        c.table(300, 400, [r"$x_i$", r"$n_i$"], [["58,2209", "1"], ["65,0412", "1"], ["69,4458", "1"]],
                [300, 180], hl_cols=(1,), total=["… 80 lignes", ""])
    if s >= 2:
        c.arrow(860, 560, 980, 560, color=PRIMARY)
        items = ["Classes", "Densité", "Polygone des fréq. cumulées", "Usages de F(x)", "Qualitatif"]
        for k, it in enumerate(items):
            c.text(1030, 420 + k * 72, f"{k+1}  {it}", size=42)


# ------------------------------------------------------------------ N6 classes
@scene("p2_02_classes", "Classes", [
    "Pense à un magasin de vêtements. Personne ne range les pulls au centimètre près : on fait des tailles S, M, L.",
    "En statistique, une classe est un intervalle : de x i moins 1 inclus, à x i exclu.",
    "Fermé à gauche, ouvert à droite. Ainsi, chaque valeur tombe dans une seule classe, même pile sur une limite.",
    "Voici les poids d'Alice, en 4 classes. Les fréquences gardent le même sens qu'avant.",
    "Une précision : grand N i compte maintenant les observations inférieures au bord droit de la classe. Par exemple, 48 étudiants pèsent moins de 75 kilos.",
])
def _(c, s):
    c.title("Regrouper en classes")
    if s == 0:
        for k, t in enumerate(["S", "M", "L"]):
            c.chip(660 + k * 300, 450, t, size=90, minw=200, h=200, ec=PRIMARY, weight="bold")
        c.text(960, 680, "on range par tailles, pas au cm près", size=46, color=MUTED, ha="center")
        return
    if s <= 2:
        c.formula([r"$[\,x_{i-1}$", r"$,$", r"$x_i\,[$"], 960, 440, size=110, hl={2: (0, 2)}.get(s, ()))
        if s >= 1:
            c.text(700, 600, "inclus", size=46, color=ACCENT if s == 2 else FG, ha="center")
            c.text(1220, 600, "exclu", size=46, color=ACCENT if s == 2 else FG, ha="center")
        if s >= 2:
            c.text(960, 760, "chaque valeur → une seule classe", size=48, color=FG, ha="center")
        return
    hl_cells = tuple((1, j) for j in [2]) if s == 4 else ()
    c.table(260, 280, ["Classe (kg)", r"$n_i$", r"$N_i$", r"$f_i$", r"$F_i$"],
            [[CLS[k], str(NI[k]), str(NC[k]), fr(FI[k]), fr(FC[k])] for k in range(4)],
            [330, 160, 160, 190, 190], rowh=80, size=44, hl_cells=hl_cells,
            hl_rows=(1,) if s == 4 else (), total=["Total", "80", "", "1", ""])
    if s == 4:
        c.text(960, 860, r"$N_2 = 48$ : 48 étudiants pèsent moins de 75 kg", size=46, color=ACCENT, ha="center")


@scene("p2_03_sturges", "Classes", [
    "Combien de classes choisir ? Ni trop peu, ni trop. La règle de Sturges donne un ordre de grandeur.",
    "Le nombre de classes vaut environ 1 plus 10 tiers, fois logarithme en base 10 de n.",
    "Pour n égale 80, on trouve environ 7,3. Donc environ 7 classes.",
    "Le cours en a choisi 4 : c'est permis. Le choix reste au flair du statisticien. Et les classes n'ont pas forcément toutes la même largeur.",
    "Regrouper fait perdre de l'information. 68, 72 et 74 kilos finissent tous dans la même classe.",
    "On fait donc une hypothèse : dans une classe, les valeurs sont réparties uniformément. De 65 à 75 kilos, 28 étudiants sur 10 kilos : 2,8 étudiants par kilo.",
    "À retenir : en continu, on regroupe en classes fermées à gauche et ouvertes à droite. Et on suppose les valeurs uniformément réparties dans chaque classe.",
])
def _(c, s):
    if s == 6:
        c.retenir([r"Classes $[\,x_{i-1},\, x_i\,[$  fermées à gauche",
                   "Valeurs réparties uniformément dans la classe"])
        return
    c.title("Combien de classes ?", "Règle de Sturges")
    if s <= 3:
        c.formula([r"$k$", r"$\approx$", r"$1 + \dfrac{10}{3}\,\log_{10} n$"], 960, 420, size=88,
                  hl=(2,) if s == 1 else ())
        if s >= 2:
            c.text(960, 590, r"$n = 80$ :  $1 + \dfrac{10}{3} \times 1{,}903 \approx 7{,}3$", size=54, ha="center",
                   color=ACCENT if s == 2 else FG)
        if s >= 3:
            c.text(960, 760, "un ordre de grandeur, pas une obligation", size=46, color=MUTED, ha="center")
        return
    # s 4-5 : uniformité
    c.ax.add_patch(R((360, 420), 1200, 160, fc=PANEL, ec=PRIMARY, lw=3, zorder=2))
    c.text(360, 640, "65 kg", size=44, ha="center", color=MUTED)
    c.text(1560, 640, "75 kg", size=44, ha="center", color=MUTED)
    if s == 4:
        for v in (68, 72, 74):
            xx = 360 + (v - 65) * 120
            c.ax.add_patch(Circle((xx, 500), 22, fc=ACCENT, zorder=4))
            c.text(xx, 360, f"{v}", size=44, ha="center", color=ACCENT)
        c.text(960, 800, "→ tous dans la classe [65, 75[", size=48, ha="center")
    if s == 5:
        for k in range(28):
            xx = 360 + (k + 0.5) * 1200 / 28
            c.ax.add_patch(Circle((xx, 500), 13, fc=ACCENT, zorder=4))
        c.text(960, 800, "28 étudiants / 10 kg = 2,8 par kg", size=52, ha="center", color=ACCENT)


# ------------------------------------------------------------------ N7 densité
def hist(c, heights, ylim, yticks, ylabel, x=170, y=260, w=900, h=560, color=PRIMARY, labels=None, hl=()):
    a = c.chart(x, y, w, h, (45, 105), ylim, xticks=[50, 65, 75, 85, 100], yticks=yticks,
                xlabel=r"$x$ (kg)", ylabel=ylabel)
    for k, ((x0, x1), hh) in enumerate(zip(CL, heights)):
        ec = ACCENT if k in hl else color
        a.add_patch(R((x0, 0), x1 - x0, hh, fc=color, alpha=0.35 if k not in hl else 0.55, ec=ec, lw=4, zorder=3))
        if labels:
            a.text((x0 + x1) / 2, hh / 2, labels[k], ha="center", va="center", color=FG if k not in hl else ACCENT,
                   fontsize=40 * PT, zorder=5, fontweight="bold")
    return a


@scene("p2_04_densite_pb", "Densité", [
    "Comment dessiner ces classes ? L'idée naturelle : un rectangle par classe, de hauteur n i.",
    "Mais ton œil ne compare pas les hauteurs. Il compare les surfaces. Comme quand tu choisis la plus grosse part de pizza.",
    "Regarde : la première et la troisième classe ont le même effectif, 20. Pourtant, le premier rectangle est une fois et demie plus grand.",
    "Et les deux derniers ont presque la même surface, 200 et 180. Alors que la dernière classe est bien moins peuplée.",
])
def _(c, s):
    c.title("Un piège visuel")
    labels = None
    hl = ()
    if s == 2:
        labels, hl = ["aire 300", "", "aire 200", ""], (0, 2)
    if s == 3:
        labels, hl = ["", "", "aire 200", "aire 180"], (2, 3)
    hist(c, NI, (0, 32), [0, 10, 20, 30], r"$n_i$", labels=labels, hl=hl)
    X = 1500
    if s == 0:
        c.text(X, 470, r"hauteur $= n_i$", size=56, ha="center", color=ACCENT)
    if s == 1:
        c.text(X, 440, "l'œil compare", size=48, ha="center", color=MUTED)
        c.text(X, 530, "les surfaces", size=60, ha="center", color=ACCENT, weight="bold")
    if s == 2:
        c.text(X, 430, "même effectif : 20", size=46, ha="center")
        c.text(X, 520, "300 contre 200", size=54, ha="center", color=ACCENT)
    if s == 3:
        c.text(X, 430, "20 contre 12", size=46, ha="center")
        c.text(X, 520, "mais 200 ≈ 180", size=54, ha="center", color=ACCENT)


@scene("p2_05_densite", "Densité", [
    "La solution : prendre comme hauteur la densité de fréquence absolue, d n i.",
    "d n i égale n i divisé par l i.",
    "l i, c'est la largeur de la classe : x i moins x i moins 1.",
    "La densité, c'est le nombre moyen d'observations par unité. Ici, par kilo.",
    "Première classe : 20 divisé par 15, environ 1,33. Le cours arrondit à 1,3.",
    "Vérifions : la hauteur fois la largeur, 1,33 fois 15, redonne 20. L'aire du rectangle, c'est bien n i.",
    "Ce graphique s'appelle l'histogramme des densités de fréquence absolue. Son aire totale vaut l'effectif, 80.",
    "Même chose en relatif : d f i égale f i divisé par l i. L'aire de chaque rectangle vaut alors f i, et l'aire totale vaut 1.",
    "Par exemple, pour la deuxième classe : 0,35 divisé par 10, ça donne 0,035.",
    "À retenir : dans un histogramme, c'est l'aire qui compte. La hauteur est une densité, n i sur l i, pour que l'aire égale l'effectif.",
])
def _(c, s):
    if s == 9:
        c.retenir([r"Hauteur = densité :  $dn_i = n_i / l_i$",
                   r"Aire du rectangle = $n_i$   (ou $f_i$)"])
        return
    c.title("Densité de fréquence")
    if s <= 3:
        c.formula([r"$dn_i$", r"$=$", r"$\dfrac{n_i}{l_i}$"], 960, 420, size=110,
                  hl={0: (0,), 1: (2,), 2: (2,)}.get(s, ()))
        if s >= 2:
            c.text(960, 620, r"$l_i = x_i - x_{i-1}$  : largeur de la classe", size=50, ha="center",
                   color=ACCENT if s == 2 else FG)
        if s >= 3:
            c.text(960, 760, "= nombre moyen d'observations par kg", size=50, ha="center", color=ACCENT)
        return
    if s <= 6:
        c.table(1150, 260, ["Classe", r"$n_i$", r"$dn_i$"],
                [[CLS[k], str(NI[k]), fr(DN[k])] for k in range(4)], [260, 140, 170],
                hl_rows=(0,) if s in (4, 5) else ())
        labels = ["20", "28", "20", "12"] if s >= 5 else None
        hist(c, DN, (0, 3.2), [0, 1, 2, 3], r"$dn_i$", w=860, labels=labels, hl=(0,) if s in (4, 5) else ())
        if s == 4:
            c.text(1435, 700, r"$dn_1 = 20 / 15 \approx 1{,}33$", size=50, ha="center", color=ACCENT)
        if s == 5:
            c.text(1435, 700, r"$1{,}33 \times 15 = 20 = n_1$", size=50, ha="center", color=ACCENT)
        if s == 6:
            c.text(1435, 700, "aire totale = n = 80", size=50, ha="center", color=ACCENT)
        return
    # relatif
    c.formula([r"$df_i$", r"$=$", r"$\dfrac{f_i}{l_i}$"], 1435, 420, size=90, hl=(2,) if s == 7 else ())
    c.text(1435, 580, "aire totale = 1", size=48, ha="center", color=FG)
    hist(c, DF, (0, 0.04), [0, 0.01, 0.02, 0.03], r"$df_i$", w=860,
         labels=["0,25", "0,35", "0,25", "0,15"], hl=(1,) if s == 8 else ())
    if s == 8:
        c.text(1435, 720, r"$df_2 = 0{,}35 / 10 = 0{,}035$", size=50, ha="center", color=ACCENT)


# ------------------------------------------------------------------ N8 polygone (ralenti)
@scene("p2_06_polygone", "Polygone des fréquences cumulées", [
    "En discret, la fonction de répartition était un escalier. En continu, on remplace les marches par des rampes.",
    "Pourquoi ? Parce qu'on suppose les valeurs réparties uniformément dans chaque classe. Le pourcentage cumulé monte donc régulièrement.",
    "Prenons une classe, de x i moins 1 à x i. En fin de classe, la hauteur est grand F i : la part des observations inférieures à x i.",
    "En début de classe, la hauteur est grand F i moins 1. On relie ces deux points par un segment.",
    "La montée vaut f i. La largeur vaut l i. Donc la pente vaut f i sur l i : c'est exactement la densité d f i.",
    "Voici l'équation du segment. y égale d f i fois, x moins x i moins 1, plus grand F i moins 1.",
    "On part de la hauteur grand F i moins 1, celle du début de la classe.",
    "Puis on monte de d f i pour chaque unité parcourue depuis le début de la classe.",
])
def _(c, s):
    c.title("Polygone des fréquences cumulées", "Le cas continu")
    if s <= 1:
        a = c.chart(200, 300, 650, 480, (0, 4), (0, 1.1), xticks=[], yticks=[])
        a.step([0, 1, 2, 3, 4], [0.1, 0.4, 0.7, 1.0, 1.0], where="post", color=MUTED, lw=6)
        c.text(525, 860, "discret : escalier", size=44, ha="center", color=MUTED)
        b = c.chart(1070, 300, 650, 480, (0, 4), (0, 1.1), xticks=[], yticks=[])
        b.plot([0, 1, 2, 3, 4], [0, 0.35, 0.7, 0.95, 1.0], color=PRIMARY, lw=6)
        c.text(1395, 860, "continu : rampes", size=44, ha="center", color=PRIMARY)
        if s == 1:
            c.text(960, 230, "valeurs uniformes dans la classe → montée régulière", size=44, ha="center", color=ACCENT)
        return
    # generic segment diagram on the left
    a = c.chart(150, 270, 820, 600, (0, 10), (0, 1), xticks=[3, 8], yticks=[0.3, 0.75],
                xticklabels=[r"$x_{i-1}$", r"$x_i$"], yticklabels=[r"$F_{i-1}$", r"$F_i$"])
    a.grid(False)
    a.plot([8, 8], [0, 0.75], ls=":", color=MUTED, lw=2)
    a.plot([0, 8], [0.75, 0.75], ls=":", color=MUTED, lw=2)
    a.plot(8, 0.75, "o", ms=18, color=PRIMARY, zorder=5)
    if s >= 3:
        a.plot([3, 3], [0, 0.3], ls=":", color=MUTED, lw=2)
        a.plot([0, 3], [0.3, 0.3], ls=":", color=MUTED, lw=2)
        a.plot(3, 0.3, "o", ms=18, color=PRIMARY, zorder=5)
        a.plot([3, 8], [0.3, 0.75], color=PRIMARY, lw=6)
    if s >= 4:
        a.annotate("", xy=(8.6, 0.75), xytext=(8.6, 0.3), arrowprops=dict(arrowstyle="<->", color=ACCENT, lw=3))
        a.text(8.9, 0.52, r"$f_i$", color=ACCENT, fontsize=48 * PT, va="center")
        a.annotate("", xy=(8, 0.2), xytext=(3, 0.2), arrowprops=dict(arrowstyle="<->", color=ACCENT, lw=3))
        a.text(5.5, 0.13, r"$l_i$", color=ACCENT, fontsize=48 * PT, ha="center")
    X = 1450
    if s == 2:
        c.text(X, 470, r"fin de classe :  $F_i$", size=50, ha="center", color=ACCENT)
        c.text(X, 550, r"part $< x_i$", size=44, ha="center", color=MUTED)
    if s == 3:
        c.text(X, 470, r"début :  $F_{i-1}$", size=50, ha="center", color=ACCENT)
        c.text(X, 550, "on relie par un segment", size=44, ha="center", color=MUTED)
    if s == 4:
        c.text(X, 470, r"pente $= \dfrac{f_i}{l_i} = df_i$", size=56, ha="center", color=ACCENT)
    if s >= 5:
        c.formula([r"$y$", r"$=$", r"$df_i\,(x - x_{i-1})$", r"$+$", r"$F_{i-1}$"], X, 470, size=58,
                  hl={6: (4,), 7: (2,)}.get(s, ()))
    if s == 6:
        c.text(X, 600, "hauteur de départ", size=44, ha="center", color=ACCENT)
    if s == 7:
        c.text(X, 600, "on monte de la pente", size=44, ha="center", color=ACCENT)
        c.text(X, 670, "× distance parcourue", size=44, ha="center", color=ACCENT)


@scene("p2_07_polygone_ex", "Polygone des fréquences cumulées", [
    "Exemple avec la deuxième classe, de 65 à 75 kilos. d f 2 vaut 0,035, et grand F 1 vaut 0,25.",
    "L'équation devient : y égale 0,035 fois, x moins 65, plus 0,25.",
    "Vérifions en fin de classe, à 75. 0,035 fois 10, plus 0,25 : on trouve 0,6. C'est bien grand F 2.",
    "Deuxième exemple, la troisième classe. y égale 0,025 fois, x moins 75, plus 0,6. À 85, on trouve 0,85 : c'est grand F 3.",
    "En assemblant tous les segments, on obtient le polygone des fréquences cumulées. C'est le graphique de F de x.",
    "Avant 50, F vaut 0. Après 100, F vaut 1. Entre les deux, un segment par classe.",
    "En continu, inférieur ou inférieur ou égal, c'est pareil : une valeur précise a une fréquence nulle.",
    "À retenir : sur chaque classe, F de x est un segment. On part de grand F i moins 1, et on monte de d f i par unité.",
])
def _(c, s):
    if s == 7:
        c.retenir([r"Sur la classe $[\,x_{i-1}, x_i\,[$ :",
                   r"$F(x) = df_i\,(x - x_{i-1}) + F_{i-1}$"])
        return
    c.title("Polygone : exemples")
    if s <= 3:
        seg = 1 if s <= 2 else 2
        poly(c, w=900, seg=seg, full=s >= 2, vmarks=[(75, 0.6)] if s == 2 else ([(85, 0.85)] if s == 3 else []))
        X = 1450
        if s <= 2:
            c.text(X, 330, "Classe [65, 75[", size=46, ha="center", color=MUTED)
            c.text(X, 420, r"$df_2 = 0{,}035$    $F_1 = 0{,}25$", size=48, ha="center")
        if s >= 1 and s <= 2:
            c.text(X, 540, r"$y = 0{,}035\,(x - 65) + 0{,}25$", size=48, ha="center", color=ACCENT if s == 1 else FG)
        if s == 2:
            c.text(X, 660, r"$0{,}035 \times 10 + 0{,}25$", size=48, ha="center")
            c.text(X, 750, r"$= 0{,}60 = F_2$", size=56, ha="center", color=ACCENT)
        if s == 3:
            c.text(X, 330, "Classe [75, 85[", size=46, ha="center", color=MUTED)
            c.text(X, 440, r"$y = 0{,}025\,(x - 75) + 0{,}6$", size=48, ha="center")
            c.text(X, 560, r"$0{,}025 \times 10 + 0{,}6$", size=48, ha="center")
            c.text(X, 650, r"$= 0{,}85 = F_3$", size=56, ha="center", color=ACCENT)
        return
    poly(c, w=760)
    rows = [("0", r"$x < 50$"), (r"$0{,}017\,(x-50)$", r"$50 \leq x < 65$"),
            (r"$0{,}035\,(x-65) + 0{,}25$", r"$65 \leq x < 75$"), (r"$0{,}025\,(x-75) + 0{,}6$", r"$75 \leq x < 85$"),
            (r"$0{,}01\,(x-85) + 0{,}85$", r"$85 \leq x < 100$"), ("1", r"$x \geq 100$")]
    c.text(1010, 560, r"$F(x)=$", size=46, color=PRIMARY)
    for k, (e, d) in enumerate(rows):
        y = 300 + k * 104
        hl = s == 5 and k in (0, 5)
        c.text(1170, y, e, size=40, color=ACCENT if hl else FG)
        c.text(1600, y, d, size=38, color=ACCENT if hl else MUTED)
    if s == 6:
        c.box(960, 900 - 45, 900, 90, fc=PANEL, ec=ACCENT, lw=3)
        c.text(1410, 900, r"continu :  $< x$  ou  $\leq x$  →  même valeur", size=40, ha="center", color=ACCENT)


# ------------------------------------------------------------------ N9 usages
@scene("p2_08_usages", "Utilité de F(x)", [
    "À quoi sert tout ça ? F de x répond à toutes les questions de pourcentage. Il y a trois cas à connaître.",
    "En dessous de x : F de x.",
    "Au-dessus de x : 1 moins F de x.",
    "Entre x 1 et x 2 : F de x 2 moins F de x 1.",
    "Et pour un nombre d'étudiants, on multiplie le pourcentage par l'effectif n.",
    "Exemple a. Quelle part des étudiants pèse moins de 73 kilos ? 73 est dans la deuxième classe.",
    "F de 73 égale 0,035 fois 8, plus 0,25. Soit 0,53 : 53 %.",
    "Exemple b. Plus de 73 kilos ? C'est le complément : 1 moins 0,53, soit 47 %.",
    "Exemple c. Combien d'étudiants pèsent moins de 73 kilos ? 80 fois 0,53 : 42,4. Donc environ 42 étudiants.",
])
def _(c, s):
    c.title("Utilité de la fonction de répartition")
    if s <= 4:
        rows = [("En dessous de x", r"$F(x)$"), ("Au-dessus de x", r"$1 - F(x)$"),
                (r"Entre $x_1$ et $x_2$", r"$F(x_2) - F(x_1)$"), ("Nombre d'observations", r"$n \times$ pourcentage")]
        for k, (a, b) in enumerate(rows):
            if s >= k + 1:
                y = 300 + k * 140
                c.box(260, y - 55, 1400, 110, fc=PANEL, ec=ACCENT if s == k + 1 else None, lw=3)
                c.text(320, y, a, size=46)
                c.text(1600, y, b, size=52, ha="right", color=ACCENT if s == k + 1 else PRIMARY)
        return
    poly(c, w=900, vmarks=[(73, 0.53)], hl_class=1 if s == 5 else None)
    X = 1460
    c.text(X, 300, "Moins de 73 kg ?", size=46, ha="center", color=MUTED if s > 6 else FG)
    if s >= 6:
        c.text(X, 390, r"$F(73) = 0{,}035 \times 8 + 0{,}25$", size=46, ha="center")
        c.text(X, 470, r"$= 0{,}53$  → 53 %", size=52, ha="center", color=ACCENT if s == 6 else FG)
    if s >= 7:
        c.text(X, 590, r"Plus de 73 kg : $1 - 0{,}53$ = 47 %", size=44, ha="center", color=ACCENT if s == 7 else FG)
    if s >= 8:
        c.text(X, 700, r"$80 \times 0{,}53 = 42{,}4$", size=48, ha="center", color=ACCENT)
        c.text(X, 780, "≈ 42 étudiants", size=48, ha="center", color=ACCENT)


@scene("p2_09_exemple_d", "Utilité de F(x)", [
    "Exemple d. On va le faire lentement, étape par étape. Quelle part des étudiants pèse entre 73 et 81 kilos ?",
    "Étape 1 : on traduit la question. Entre deux valeurs, c'est F de 81 moins F de 73.",
    "Étape 2 : F de 73, on l'a déjà calculé. 0,53.",
    "Étape 3 : dans quelle classe tombe 81 ? Entre 75 et 85 : la troisième classe.",
    "On prend donc l'équation de la troisième classe : 0,025 fois, x moins 75, plus 0,6.",
    "81 moins 75, ça fait 6. 0,025 fois 6, ça fait 0,15. Plus 0,6 : on obtient 0,75.",
    "Étape 4 : on soustrait. 0,75 moins 0,53, égale 0,22.",
    "Donc 22 % des étudiants pèsent entre 73 et 81 kilos. Sur le graphique, c'est l'écart vertical entre les deux hauteurs.",
    "Attention au piège : ne recopie pas les grands F i du tableau. 0,60 ou 0,85 sont les valeurs en fin de classe, pas en 73 ou en 81.",
])
def _(c, s):
    c.title("Exemple d : entre 73 et 81 kg")
    marks = []
    if s >= 2:
        marks.append((73, 0.53))
    if s >= 5:
        marks.append((81, 0.75))
    a = poly(c, w=880, vmarks=marks, hl_class=2 if s in (3, 4) else None)
    if s == 7:
        a.annotate("", xy=(60, 0.75), xytext=(60, 0.53), arrowprops=dict(arrowstyle="<->", color=ACCENT, lw=4))
        a.text(57, 0.64, "0,22", color=ACCENT, fontsize=44 * PT, ha="right", va="center", fontweight="bold")
    if s == 8:
        for yv in (0.6, 0.85):
            a.axhline(yv, color=MUTED, lw=3, ls=":")
    X = 1470
    steps = [
        (1, r"1.  $F(81) - F(73)$"),
        (2, r"2.  $F(73) = 0{,}53$"),
        (3, r"3.  81 dans [75, 85[ → classe 3"),
        (5, r"     $0{,}025 \times 6 + 0{,}6 = 0{,}75$"),
        (6, r"4.  $0{,}75 - 0{,}53 = 0{,}22$"),
    ]
    for k, (st, t) in enumerate(steps):
        if s >= st:
            cur = (s == st) or (st == 3 and s == 4)
            c.text(1060, 300 + k * 105, t, size=42, color=ACCENT if cur else FG)
    if s == 4:
        c.text(1060, 615, r"     $y = 0{,}025\,(x - 75) + 0{,}6$", size=42, color=ACCENT)
    if s >= 7:
        c.box(1040, 790, 820, 100, fc=PANEL, ec=ACCENT, lw=3)
        c.text(1450, 840, "22 % entre 73 et 81 kg", size=48, ha="center", color=ACCENT, weight="bold")
    if s == 8:
        c.text(1450, 935, "pas 0,60 ni 0,85 (fins de classe)", size=40, ha="center", color=ACCENT)


@scene("p2_10_inverse", "Utilité de F(x)", [
    "Dernier usage : le chemin inverse. On connaît un pourcentage, on cherche la valeur de x.",
    "Exemple e. Quel poids sépare les 30 % d'étudiants les plus légers ? On résout F de x égale 0,3.",
    "Sur le graphique, 0,3 est entre 0,25 et 0,6. Donc on est dans la deuxième classe.",
    "On résout : 0,035 fois, x moins 65, plus 0,25, égale 0,3.",
    "x moins 65 égale 0,05 divisé par 0,035, environ 1,43. Donc x vaut environ 66,4 kilos.",
    "Exemple bonus. Quel poids coupe le groupe en deux moitiés ? On résout F de x égale 0,5.",
    "Toujours la deuxième classe. x moins 65 égale 0,25 divisé par 0,035, environ 7,14. Donc x vaut environ 72,1 kilos. Cette valeur s'appelle la médiane.",
    "À retenir : en dessous, F de x. Au-dessus, 1 moins F de x. Entre deux valeurs, la différence. Et pour le chemin inverse, on résout F de x égale p.",
])
def _(c, s):
    if s == 7:
        c.retenir([r"$\leq x$ : $F(x)$     $\geq x$ : $1 - F(x)$",
                   r"Entre $x_1$ et $x_2$ : $F(x_2) - F(x_1)$",
                   r"Chemin inverse : résoudre $F(x) = p$"])
        return
    c.title("Le chemin inverse")
    if s == 0:
        c.text(1470, 420, "on connaît le %", size=48, ha="center", color=FG)
        c.text(1470, 510, "on cherche x", size=48, ha="center", color=ACCENT)
    marks = []
    if s >= 2 and s <= 4:
        marks = [(66.43, 0.3)]
    if s >= 5:
        marks = [(72.14, 0.5)]
    poly(c, w=880, vmarks=marks if s not in (1, 5) else [], hl_class=1 if s in (2, 6) else None)
    X = 1470
    if 1 <= s <= 4:
        c.text(X, 300, "30 % les plus légers", size=44, ha="center", color=MUTED)
        c.text(X, 390, r"$F(x) = 0{,}3$", size=54, ha="center", color=ACCENT if s == 1 else FG)
    if 2 <= s <= 4:
        c.text(X, 480, r"$0{,}25 < 0{,}3 < 0{,}6$ → classe 2", size=42, ha="center", color=ACCENT if s == 2 else FG)
    if 3 <= s <= 4:
        c.text(X, 580, r"$0{,}035\,(x - 65) + 0{,}25 = 0{,}3$", size=42, ha="center", color=ACCENT if s == 3 else FG)
    if s == 4:
        c.text(X, 680, r"$x - 65 = 0{,}05 / 0{,}035 \approx 1{,}43$", size=42, ha="center")
        c.text(X, 780, r"$x \approx 66{,}4$ kg", size=56, ha="center", color=ACCENT, weight="bold")
    if s >= 5:
        c.text(X, 300, "Bonus : couper en deux", size=44, ha="center", color=MUTED)
        c.text(X, 390, r"$F(x) = 0{,}5$", size=54, ha="center", color=ACCENT if s == 5 else FG)
    if s == 6:
        c.text(X, 500, r"$x - 65 = 0{,}25 / 0{,}035 \approx 7{,}14$", size=42, ha="center")
        c.text(X, 610, r"$x \approx 72{,}1$ kg", size=56, ha="center", color=ACCENT, weight="bold")
        c.text(X, 710, "= la médiane", size=46, ha="center", color=MUTED)


# ------------------------------------------------------------------ N10 qualitatif
AV = ["Très satisfait", "Satisfait", "Moyennement", "Peu satisfait", "Pas du tout"]
AN = [13, 42, 17, 6, 2]


@scene("p2_11_qualitatif", "Données qualitatives", [
    "Dernière famille : les données qualitatives. On garde les fréquences absolues et relatives, exactement comme avant.",
    "Par contre, pas de fréquences cumulées. Ces valeurs ne sont pas des nombres : les ranger sur un axe n'a pas de sens mathématique.",
    "Le contexte peut quand même suggérer un ordre. Par exemple, des avis de clients, du plus satisfait au moins satisfait.",
    "80 clients ont répondu. Satisfait : 42 réponses, donc 42 sur 80, soit 52,5 %.",
    "Sans ordre naturel, on classe par fréquence décroissante, ou par ordre alphabétique.",
    "Le graphique classique, c'est le diagramme en camembert. Chaque part a une surface proportionnelle à sa fréquence.",
    "L'angle d'une part vaut f i fois 360 degrés. Pour Satisfait : 0,525 fois 360, soit 189 degrés.",
    "À retenir : en qualitatif, on utilise n i et f i, mais pas de cumul. Et en camembert, l'angle vaut f i fois 360 degrés.",
])
def _(c, s):
    if s == 7:
        c.retenir([r"Qualitatif : $n_i$ et $f_i$, pas de cumul",
                   r"Camembert : angle $= f_i \times 360°$"])
        return
    c.title("Données qualitatives")
    if s <= 1:
        c.text(960, 380, r"$n_i$  et  $f_i$  :  comme avant", size=60, ha="center", color=PRIMARY)
        if s == 1:
            c.text(960, 540, r"$N_i$, $F_i$ :  pas de sens", size=60, ha="center", color=ACCENT)
            c.text(960, 650, "les valeurs ne sont pas des nombres", size=44, ha="center", color=MUTED)
        return
    if s <= 4:
        c.table(200, 260, ["Avis", r"$n_i$", r"$f_i$"],
                [[AV[k], str(AN[k]), fr(AN[k] / 80 * 100, 2 if k in (0, 2) else 1) + " %"] for k in range(5)],
                [420, 140, 220], hl_rows=(1,) if s == 3 else (), total=["Total", "80", "100 %"])
        X = 1380
        if s == 2:
            c.text(X, 450, "ordre suggéré", size=48, ha="center", color=ACCENT)
            c.text(X, 530, "du plus au moins satisfait", size=44, ha="center", color=MUTED)
        if s == 3:
            c.text(X, 450, r"$42 / 80 = 0{,}525$", size=54, ha="center", color=ACCENT)
            c.text(X, 540, "soit 52,5 %", size=48, ha="center")
        if s == 4:
            c.text(X, 450, "sans ordre naturel :", size=46, ha="center", color=MUTED)
            c.text(X, 530, "par fréquence", size=48, ha="center")
            c.text(X, 600, "ou alphabétique", size=48, ha="center")
        return
    a = c.fig.add_axes([150 / W, 1 - 930 / H, 700 / W, 700 / H])
    cols = ["#0EA5E9", ACCENT if s == 6 else PRIMARY, "#7DD3FC", "#0369A1", "#475569"]
    a.pie(AN, colors=cols, startangle=90, counterclock=False,
          wedgeprops=dict(edgecolor=BG, linewidth=4))
    for k, t in enumerate(AV):
        y = 330 + k * 80
        c.box(990, y - 20, 40, 40, fc=cols[k], r=6)
        c.text(1060, y, f"{t}  ({AN[k]})", size=40, color=ACCENT if (s == 6 and k == 1) else FG)
    if s == 6:
        c.text(1380, 800, r"$0{,}525 \times 360° = 189°$", size=54, ha="center", color=ACCENT)


# ------------------------------------------------------------------ récap 2
@scene("p2_12_recap", "Récapitulatif", [
    "Récapitulons la partie 2.",
    "En continu, on regroupe en classes, fermées à gauche, ouvertes à droite. La règle de Sturges donne un ordre de grandeur du nombre de classes.",
    "Dans un histogramme, la hauteur est une densité, n i sur l i. Comme ça, l'aire égale la fréquence.",
    "Sur chaque classe, F de x est un segment. y égale d f i fois, x moins x i moins 1, plus grand F i moins 1.",
    "En dessous de x, F de x. Au-dessus, 1 moins F de x. Entre deux valeurs, la différence.",
    "En qualitatif, pas de cumul, et l'angle d'une part vaut f i fois 360 degrés. Tu as maintenant tout le chapitre 1. Bon courage pour les exercices !",
])
def _(c, s):
    c.title("Fiche récap — Partie 2")
    lines = [
        r"Classes $[\,x_{i-1}, x_i\,[$     Sturges : $k \approx 1 + (10/3)\,\log_{10} n$",
        r"$dn_i = n_i / l_i$      $df_i = f_i / l_i$      aire = fréquence",
        r"$F(x) = df_i\,(x - x_{i-1}) + F_{i-1}$",
        r"$\leq x$ : $F(x)$     $\geq x$ : $1 - F(x)$     entre : $F(x_2) - F(x_1)$",
        r"Qualitatif : pas de cumul     angle $= f_i \times 360°$",
    ]
    for k, l in enumerate(lines):
        if s >= k + 1:
            y = 270 + k * 140
            c.box(150, y - 55, 1620, 110, fc=PANEL, ec=ACCENT if s == k + 1 else None, lw=3)
            c.text(200, y, l, size=44)
