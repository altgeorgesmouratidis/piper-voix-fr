"""Partie 1 : vocabulaire + données discrètes. Each scene: id, notion, beats (narration), draw(c, s)."""
from style import *

AGES = [18, 19, 20, 18, 17, 21, 19, 19, 18, 20, 17, 19, 21, 19, 18, 19]
XI = [17, 18, 19, 20, 21]
NI = [2, 4, 6, 2, 2]
NC = [2, 6, 12, 14, 16]
FI = ["12,5 %", "25 %", "37,5 %", "12,5 %", "12,5 %"]
FC = ["12,5 %", "37,5 %", "75 %", "87,5 %", "100 %"]

SCENES = []


def scene(id, notion, beats):
    def deco(fn):
        SCENES.append(dict(id=id, part=1, notion=notion, beats=beats, draw=fn))
        return fn
    return deco


def raw_ages(c, y, hl=None, size=44):
    x0 = 1920 / 2 - 16 * 104 / 2 + 52
    for k, a in enumerate(AGES):
        ec = ACCENT if (hl and a == hl) else None
        col = ACCENT if (hl and a == hl) else FG
        c.chip(x0 + k * 104, y, str(a), size=size, minw=88, padx=10, ec=ec, color=col)


# ------------------------------------------------------------------ titre
@scene("p1_00_titre", "Introduction", [
    "Analyse de données, chapitre 1 : la statistique descriptive. "
    "Dans cette première partie, on voit le vocabulaire et les données discrètes.",
])
def _(c, s):
    c.text(960, 330, "5ANA1D · Analyse de données", size=44, color=PRIMARY, ha="center")
    c.text(960, 450, "Chapitre 1", size=60, color=MUTED, ha="center")
    c.text(960, 560, "Statistique descriptive", size=96, weight="bold", ha="center")
    c.line([860, 1060], [640, 640], color=PRIMARY, lw=6)
    c.text(960, 730, "Partie 1 — Vocabulaire et données discrètes", size=48, color=FG, ha="center")


# ------------------------------------------------------------------ intro
@scene("p1_01_intro", "Introduction", [
    "Imagine Alice. Elle demande leur âge aux 16 étudiants de sa classe.",
    "Elle obtient cette liste. En vrac, comme ça, elle ne raconte pas grand-chose.",
    "Le but de ce chapitre : ranger ces données dans des tableaux et des graphiques qui parlent.",
    "Au programme : le vocabulaire, les fréquences, les fréquences cumulées, et la fonction de répartition.",
])
def _(c, s):
    c.title("Une liste en vrac", "L'âge des 16 étudiants d'Alice")
    if s >= 1:
        raw_ages(c, 330)
    if s == 1:
        c.text(960, 470, "?", size=110, color=ACCENT, ha="center", weight="bold")
    if s >= 2:
        c.arrow(960, 400, 960, 500, color=PRIMARY)
        c.chip(700, 570, "Tableaux", size=44, ec=PRIMARY)
        c.chip(1220, 570, "Graphiques", size=44, ec=PRIMARY)
    if s >= 3:
        items = ["1  Vocabulaire", "2  Fréquences absolues et relatives",
                 "3  Fréquences cumulées", "4  Fonction de répartition"]
        for k, it in enumerate(items):
            c.text(560, 690 + k * 72, it, size=42, color=FG if k else FG)


# ------------------------------------------------------------------ N1 vocabulaire
@scene("p1_02_vocab", "Vocabulaire", [
    "Commençons par le vocabulaire. Pense à un cuisinier qui goûte sa soupe.",
    "Il ne boit pas toute la marmite. Une cuillère suffit, si la soupe est bien mélangée.",
    "En statistique, c'est pareil. La marmite, c'est la population : tout le groupe qu'on veut étudier.",
    "Chaque élément de ce groupe s'appelle un individu. Ça peut être une personne, un animal ou un objet.",
    "La cuillère, c'est l'échantillon : la partie du groupe qu'on interroge vraiment.",
    "Le nombre d'observations récoltées s'appelle l'effectif. On le note n.",
])
def _(c, s):
    c.title("Vocabulaire", "Population, échantillon, effectif")
    # soup analogy on the left
    if s <= 1:
        c.ax.add_patch(Wedge((700, 520), 230, 0, 180, fc=PANEL, ec=MUTED, lw=4, zorder=2))
        c.line([470, 930], [520, 520], color=MUTED, lw=4)
        c.text(700, 640, "la marmite", size=44, color=MUTED, ha="center")
        c.text(700, 460, "~ ~ ~", size=60, color=PRIMARY, ha="center")
    if s == 1:
        c.ax.add_patch(Circle((1250, 470), 70, fc=PANEL, ec=ACCENT, lw=4, zorder=3))
        c.line([1320, 1500], [470, 400], color=ACCENT, lw=6)
        c.text(1250, 600, "une cuillère suffit", size=44, color=ACCENT, ha="center")
    if s >= 2:
        c.ax.add_patch(Circle((640, 560), 270, fc=PANEL, ec=PRIMARY, lw=4, zorder=2))
        c.text(640, 250, "Population", size=48, color=PRIMARY, ha="center", weight="bold")
        rng = np.random.default_rng(3)
        pts = []
        while len(pts) < 34:
            p = rng.uniform(-240, 240, 2)
            if np.hypot(*p) < 235:
                pts.append(p)
        for p in pts:
            inside = np.hypot(p[0] - 70, p[1] - 40) < 110
            col = ACCENT if (s >= 4 and inside) else FG
            c.ax.add_patch(Circle((640 + p[0], 560 + p[1]), 11, fc=col, ec="none", zorder=4))
    if s >= 3:
        c.text(1080, 380, "Individu", size=46, color=FG, weight="bold")
        c.text(1080, 445, "personne, animal ou objet", size=40, color=MUTED)
    if s >= 4:
        c.ax.add_patch(Circle((710, 600), 115, fc="none", ec=ACCENT, lw=4, zorder=5))
        c.text(1080, 560, "Échantillon", size=46, color=ACCENT, weight="bold")
        c.text(1080, 625, "la partie qu'on interroge", size=40, color=MUTED)
    if s >= 5:
        c.text(1080, 740, "Effectif  $n$", size=46, color=PRIMARY, weight="bold")
        c.text(1080, 805, "nombre d'observations", size=40, color=MUTED)


@scene("p1_03_types", "Vocabulaire", [
    "Les informations récoltées s'appellent des observations. Il en existe deux grandes familles.",
    "Si ce ne sont pas des nombres, elles sont qualitatives. Par exemple, une couleur ou une marque de téléphone.",
    "Si ce sont des nombres, elles sont quantitatives. Et là, il y a encore deux cas.",
    "Discrètes : les valeurs sont isolées, on peut les compter une à une. Comme le nombre d'enfants : 0, 1, 2, 3.",
    "Continues : toutes les valeurs réelles d'un intervalle sont possibles. Comme le poids d'un œuf : 52 grammes, ou 52,375 grammes.",
])
def _(c, s):
    c.title("Les types d'observations")
    c.chip(960, 270, "Observations", size=48, ec=PRIMARY, weight="bold")
    if s >= 1:
        c.line([960, 520], [305, 420], color=MUTED)
        c.chip(520, 460, "Qualitatives", size=46, ec=PRIMARY)
        c.text(520, 560, "pas des nombres", size=40, color=MUTED, ha="center")
        c.text(520, 640, "couleur, marque de GSM", size=40, color=FG, ha="center")
    if s >= 2:
        c.line([960, 1300], [305, 420], color=MUTED)
        c.chip(1300, 460, "Quantitatives", size=46, ec=PRIMARY)
        c.text(1300, 560, "des nombres", size=40, color=MUTED, ha="center")
    if s >= 3:
        c.line([1300, 1060], [600, 700], color=MUTED)
        hl = s == 3
        c.chip(1060, 740, "Discrètes", size=44, ec=ACCENT if hl else PRIMARY)
        c.text(1060, 830, "valeurs isolées", size=40, color=MUTED, ha="center")
        c.text(1060, 900, "enfants : 0, 1, 2, 3…", size=40, color=FG, ha="center")
    if s >= 4:
        c.line([1300, 1560], [600, 700], color=MUTED)
        c.chip(1560, 740, "Continues", size=44, ec=ACCENT)
        c.text(1560, 830, "tout un intervalle", size=40, color=MUTED, ha="center")
        c.text(1560, 900, "œuf : 52,375 g", size=40, color=FG, ha="center")


@scene("p1_04_alice", "Vocabulaire", [
    "Classons le questionnaire d'Alice. Elle demande l'âge, la taille et le langage de programmation préféré.",
    "L'âge, en années entières, est quantitatif discret.",
    "La taille peut prendre n'importe quelle valeur réelle : c'est quantitatif continu.",
    "Le langage préféré, Python ou Java, n'est pas un nombre : c'est qualitatif.",
    "Attention au piège. Si Alice arrondit la taille au centimètre, les valeurs redeviennent isolées. On parle alors de continu discrétisé.",
    "Dernier mot. Des mesures répétées dans le temps forment une série chronologique. Des mesures prises au même moment forment une série statistique.",
    "À retenir : qualitatif, discret ou continu. Le type de données décide des tableaux et des graphiques à utiliser.",
])
def _(c, s):
    if s == 6:
        c.retenir(["Qualitatif  ·  Discret  ·  Continu",
                   "Le type décide du tableau et du graphique"])
        return
    c.title("Exemple : le questionnaire d'Alice")
    rows = [("Âge (années)", "Quantitatif discret", 1),
            ("Taille", "Quantitatif continu", 2),
            ("Langage préféré", "Qualitatif", 3)]
    for k, (q, t, step) in enumerate(rows):
        y = 300 + k * 130
        c.chip(460, y, q, size=46, minw=560)
        if s >= step:
            c.arrow(770, y, 900, y, color=MUTED)
            c.chip(1240, y, t, size=46, ec=ACCENT if s == step else PRIMARY, minw=560)
        else:
            c.text(1240, y, "?", size=56, color=MUTED, ha="center")
    if s >= 4:
        c.box(240, 650, 1440, 110, fc=PANEL, ec=ACCENT, lw=3)
        c.text(960, 705, "Taille arrondie au cm  →  continu discrétisé", size=44, color=ACCENT, ha="center")
    if s >= 5:
        c.text(960, 840, "Dans le temps : série chronologique  ·  Au même moment : série statistique",
               size=38, color=MUTED, ha="center")


# ------------------------------------------------------------------ N2 fréquence absolue
@scene("p1_05_freq_abs", "Fréquence absolue", [
    "Revenons aux âges d'Alice. Imagine un vote à main levée : on compte combien de mains se lèvent pour chaque âge.",
    "D'abord, on repère les valeurs différentes, rangées dans l'ordre croissant. On les note x 1, x 2, jusqu'à x k.",
    "Ici, il y a 5 âges différents, de 17 à 21. Donc k vaut 5.",
    "Ensuite, on compte. Le nombre de fois que la valeur x i apparaît s'appelle sa fréquence absolue. On la note n i.",
    "On range tout dans un tableau. On l'appelle le tableau des fréquences absolues, ou tableau recensé.",
    "Par exemple, 19 ans apparaît 6 fois. Donc n 3 vaut 6.",
    "Si on additionne toutes les fréquences absolues, on retrouve l'effectif total.",
    "La formule se lit : la somme des n i, pour i allant de 1 à k, égale n. Ici, 2 plus 4 plus 6 plus 2 plus 2, ça fait 16.",
    "À retenir : n i compte combien de fois la valeur x i apparaît. Et la somme des n i donne toujours l'effectif n.",
])
def _(c, s):
    if s == 8:
        c.retenir([r"$n_i$ = nombre de fois où $x_i$ apparaît",
                   r"$\sum\, n_i = n$  (l'effectif)"])
        return
    c.title("Fréquence absolue", r"Combien de fois chaque valeur apparaît")
    if s == 0:
        raw_ages(c, 400)
        c.text(960, 560, "1 vote à main levée par âge", size=44, color=MUTED, ha="center")
        return
    if s in (1, 2, 3):
        for k, (x) in enumerate(XI):
            cx = 560 + k * 200
            c.chip(cx, 380, str(x), size=52, minw=140, ec=PRIMARY)
            c.text(cx, 470, f"$x_{k+1}$", size=44, color=PRIMARY, ha="center")
            if s >= 3:
                c.text(cx, 570, f"$n_{k+1}$ = {NI[k]}", size=44, color=ACCENT, ha="center")
        if s >= 2:
            c.text(960, 700, r"$k = 5$  valeurs différentes", size=48, color=FG, ha="center")
        if s >= 3:
            c.text(960, 800, r"$n_i$ : fréquence absolue de $x_i$", size=48, color=ACCENT, ha="center")
        return
    # s >= 4: table + formula
    hl = (2,) if s == 5 else ()
    c.text(400, 255, "Tableau recensé", size=42, color=MUTED, ha="center")
    c.table(250, 300, [r"$x_i$", r"$n_i$"], [[str(x), str(n)] for x, n in zip(XI, NI)], [150, 150],
            hl_rows=hl, total=["Total", "16"])
    if s == 5:
        c.text(1200, 480, r"19 ans : 6 fois  →  $n_3 = 6$", size=52, color=ACCENT, ha="center")
    if s >= 6:
        c.formula([r"$\sum_{i=1}^{k}$", r"$n_i$", r"$=$", r"$n$"], 1200, 500, size=84,
                  hl=(0, 1) if s == 7 else ())
    if s >= 7:
        c.text(1200, 680, "2 + 4 + 6 + 2 + 2 = 16", size=52, color=FG, ha="center")


# ------------------------------------------------------------------ N3 fréquence relative
@scene("p1_06_freq_rel", "Fréquence relative", [
    "6 étudiants ont 19 ans. Mais 6 sur combien ? C'est comme une note : 18 points, ça ne veut rien dire sans le sur 20.",
    "La fréquence relative répond à ça. C'est la fréquence absolue divisée par l'effectif.",
    "f i, c'est la fréquence relative de la valeur x i.",
    "On divise n i, la fréquence absolue, par n, l'effectif total.",
    "Pour 19 ans : 6 divisé par 16, ça donne 0,375. Soit 37,5 %.",
    "Une fréquence relative est toujours comprise entre 0 et 1. Et la somme des f i vaut toujours 1, c'est-à-dire 100 %.",
    "Pourquoi ? Parce que la somme des n i sur n, c'est n sur n. Donc 1.",
])
def _(c, s):
    c.title("Fréquence relative", "La même information, en pourcentage")
    if s == 0:
        c.text(960, 400, "6 étudiants… sur combien ?", size=60, color=FG, ha="center")
        c.text(960, 540, "18 points  →  18 / 20", size=56, color=ACCENT, ha="center")
        return
    c.formula([r"$f_i$", r"$=$", r"$\dfrac{n_i}{n}$"], 560, 420, size=96,
              hl={2: (0,), 3: (2,)}.get(s, ()))
    if s >= 2:
        c.text(560, 600, "fréquence relative", size=40, color=ACCENT if s == 2 else MUTED, ha="center")
    if s >= 3:
        c.text(560, 670, "fréq. absolue / effectif", size=40, color=ACCENT if s == 3 else MUTED, ha="center")
    if s >= 4:
        c.table(1100, 250, [r"$x_i$", r"$n_i$", r"$f_i$"],
                [[str(x), str(n), f] for x, n, f in zip(XI, NI, FI)], [150, 150, 220],
                hl_rows=(2,) if s == 4 else (), total=["Total", "16", "100 %"])
    if s == 4:
        c.text(1360, 790, r"$f_3 = 6 / 16 = 0{,}375$", size=48, color=ACCENT, ha="center")
    if s >= 5:
        c.text(560, 790, r"$0 \leq f_i \leq 1$      $\sum f_i = 1$", size=50, color=FG, ha="center")
    if s >= 6:
        c.text(1360, 830, r"$\sum \dfrac{n_i}{n} = \dfrac{n}{n} = 1$", size=50, color=ACCENT, ha="center")


@scene("p1_07_batonnets", "Fréquence relative", [
    "Pour visualiser, on utilise un diagramme en bâtonnets. Les valeurs x i en abscisse, les fréquences en ordonnée.",
    "À gauche, les fréquences absolues. À droite, les fréquences relatives. Les deux diagrammes ont exactement la même allure.",
    "Seule la graduation de l'axe vertical change : un nombre d'étudiants d'un côté, un pourcentage de l'autre.",
    "Petite remarque : si les fréquences sont très éloignées, certains bâtonnets deviennent invisibles. On gradue alors l'axe en échelle logarithmique.",
    "À retenir : f i égale n i sur n. C'est une part entre 0 et 1, et la somme des f i vaut 1.",
])
def _(c, s):
    if s == 4:
        c.retenir([r"$f_i = n_i\,/\,n$     entre 0 et 1",
                   r"$\sum f_i = 1$  (100 %)"])
        return
    c.title("Diagramme en bâtonnets")
    a = c.chart(170, 250, 700, 520, (16, 22), (0, 7), xticks=XI, yticks=[0, 2, 4, 6], ylabel=r"$n_i$", xlabel=r"$x_i$")
    a.vlines(XI, 0, NI, color=PRIMARY, lw=14)
    if s >= 1:
        b = c.chart(1080, 250, 700, 520, (16, 22), (0, 0.42), xticks=XI, yticks=[0, 0.125, 0.25, 0.375],
                    yticklabels=["0", "12,5 %", "25 %", "37,5 %"], ylabel=r"$f_i$", xlabel=r"$x_i$")
        b.vlines(XI, 0, [n / 16 for n in NI], color=PRIMARY, lw=14)
    if s == 2:
        for ax_ in (a, b):
            ax_.tick_params(axis="y", labelcolor=ACCENT)
            ax_.spines["left"].set_color(ACCENT)
        c.text(960, 930, "seule la graduation verticale change", size=44, color=ACCENT, ha="center")
    if s == 3:
        c.text(960, 930, r"fréquences très éloignées  →  axe en $\log_{10} n_i$", size=44, color=ACCENT, ha="center")


# ------------------------------------------------------------------ N4 fréquences cumulées
@scene("p1_08_cumul_def", "Fréquences cumulées", [
    "Nouvelle question : combien d'étudiants ont 19 ans ou moins ? Pour répondre, on cumule.",
    "Pense au compteur à l'entrée d'une salle. À chaque groupe qui entre, le total grimpe.",
    "La fréquence absolue cumulée, notée grand N i, compte les observations inférieures ou égales à x i.",
    "Grand N i égale la somme des n j, pour j allant de 1 à i.",
    "En pratique, on ajoute simplement la ligne suivante : grand N i égale grand N i moins 1, plus n i.",
    "Même idée en pourcentage : grand F i, la fréquence relative cumulée. C'est grand N i divisé par n.",
])
def _(c, s):
    c.title("Fréquences cumulées", "Combien d'observations jusqu'à une valeur ?")
    if s <= 1:
        c.text(960, 380, "Combien ont 19 ans ou moins ?", size=60, ha="center")
        if s == 1:
            for k, v in enumerate([2, 6, 12, 14, 16]):
                c.chip(560 + k * 200, 560, str(v), size=56, minw=130, ec=ACCENT if k == 2 else PRIMARY)
                if k:
                    c.arrow(560 + (k - 1) * 200 + 70, 560, 560 + k * 200 - 70, 560, color=MUTED, head=16)
            c.text(960, 690, "le compteur grimpe à chaque groupe", size=44, color=MUTED, ha="center")
        return
    c.text(960, 290, r"$N_i$ = nombre d'observations  $\leq x_i$", size=50, ha="center",
           color=ACCENT if s == 2 else FG)
    if s >= 3:
        c.formula([r"$N_i$", r"$=$", r"$\sum_{j=1}^{i}\, n_j$"], 560, 500, size=80, hl=(2,) if s == 3 else ())
    if s >= 4:
        c.formula([r"$N_i$", r"$=$", r"$N_{i-1}$", r"$+$", r"$n_i$"], 1360, 500, size=72,
                  hl=(2, 4) if s == 4 else ())
    if s >= 5:
        c.formula([r"$F_i$", r"$=$", r"$\sum_{j=1}^{i}\, f_j$", r"$=$", r"$\dfrac{N_i}{n}$"], 960, 760, size=72,
                  hl=(0, 4) if s == 5 else ())


@scene("p1_09_cumul_tab", "Fréquences cumulées", [
    "Construisons le tableau. 2, puis 2 plus 4 égale 6, puis 6 plus 6 égale 12, puis 14, puis 16.",
    "Dernière ligne : grand N k vaut toujours n, et grand F k vaut toujours 1.",
    "Que peut-on lire ? Grand N 3 vaut 12 : 12 étudiants ont 19 ans ou moins. Soit 75 %.",
    "Le complément donne le reste : 1 moins 0,75. Donc 25 % des étudiants ont plus de 19 ans.",
    "Pour un intervalle, on soustrait. Entre 18 et 20 ans inclus : grand F de 20 moins grand F de 17.",
    "On retire 17, et pas 18, car on veut garder les étudiants de 18 ans. 87,5 moins 12,5 : ça fait 75 %.",
    "À retenir : grand F i est la part des observations inférieures ou égales à x i. Pour un intervalle, on soustrait deux F.",
])
def _(c, s):
    if s == 6:
        c.retenir([r"$F_i$ = part des observations $\leq x_i$",
                   r"Entre deux valeurs : on soustrait deux $F$"])
        return
    c.title("Fréquences cumulées : le tableau")
    hl_rows, hl_cells = (), ()
    if s == 0:
        hl_cells = tuple((i, 2) for i in range(5))
    if s == 1:
        hl_rows = (4,)
    if s == 2:
        hl_cells = ((2, 2), (2, 4))
    if s == 3:
        hl_cells = ((2, 4),)
    if s >= 4:
        hl_cells = ((3, 4), (0, 4))
    c.table(140, 230, [r"$x_i$", r"$n_i$", r"$N_i$", r"$f_i$", r"$F_i$"],
            [[str(x), str(n), str(N), f, F] for x, n, N, f, F in zip(XI, NI, NC, FI, FC)],
            [130, 130, 130, 200, 200], hl_rows=hl_rows, hl_cells=hl_cells)
    X = 1390
    if s == 0:
        c.text(X, 420, "2", size=52, ha="center", color=ACCENT)
        c.text(X, 500, "2 + 4 = 6", size=52, ha="center", color=ACCENT)
        c.text(X, 580, "6 + 6 = 12", size=52, ha="center", color=ACCENT)
        c.text(X, 660, "… 14, 16", size=52, ha="center", color=ACCENT)
    if s == 1:
        c.text(X, 460, r"$N_k = n = 16$", size=56, ha="center", color=ACCENT)
        c.text(X, 560, r"$F_k = 1$  (100 %)", size=56, ha="center", color=ACCENT)
    if s == 2:
        c.text(X, 420, r"$N_3 = 12$", size=56, ha="center", color=ACCENT)
        c.text(X, 520, "12 étudiants ≤ 19 ans", size=46, ha="center")
        c.text(X, 600, "soit 75 %", size=46, ha="center")
    if s == 3:
        c.text(X, 440, "Plus de 19 ans :", size=46, ha="center")
        c.text(X, 540, "1 − 0,75 = 25 %", size=56, ha="center", color=ACCENT)
    if s >= 4:
        c.text(X, 360, "Entre 18 et 20 ans :", size=46, ha="center")
        c.text(X, 460, r"$F(20) - F(17)$", size=60, ha="center", color=ACCENT)
    if s >= 5:
        c.text(X, 570, "87,5 % − 12,5 %", size=52, ha="center")
        c.text(X, 660, "= 75 %", size=60, ha="center", color=ACCENT, weight="bold")
        c.text(X, 780, "on retire 17, pas 18", size=42, ha="center", color=MUTED)


# ------------------------------------------------------------------ N5 fonction de répartition
def stair(c, marks=(), zoom20=False):
    a = c.chart(150, 250, 1000, 620, (15, 23), (0, 1.1), xticks=[16, 17, 18, 19, 20, 21, 22],
                yticks=[0, 0.25, 0.5, 0.75, 1], yticklabels=["0", "0,25", "0,5", "0,75", "1"],
                xlabel=r"$x$", ylabel=r"$F(x)$")
    F = [0, 0.125, 0.375, 0.75, 0.875, 1]
    edges = [15, 17, 18, 19, 20, 21, 23]
    for k in range(6):
        a.plot([edges[k], edges[k + 1]], [F[k], F[k]], color=PRIMARY, lw=6, solid_capstyle="butt")
        if k >= 1:
            a.plot(edges[k], F[k], "o", ms=16, color=PRIMARY, zorder=5)            # fermé à gauche
        if 1 <= k + 1 <= 5:
            a.plot(edges[k + 1], F[k], "o", ms=16, mfc=BG, mec=PRIMARY, mew=3, zorder=5)  # ouvert à droite
    for (x, y) in marks:
        a.plot([x, x], [0, y], ls="--", color=ACCENT, lw=3)
        a.plot([15, x], [y, y], ls="--", color=ACCENT, lw=3)
        a.plot(x, y, "o", ms=18, color=ACCENT, zorder=6)
    if zoom20:
        from matplotlib.patches import Ellipse
        a.add_patch(Ellipse((20, 0.81), 0.7, 0.26, fc="none", ec=ACCENT, lw=4, zorder=7))
    return a


@scene("p1_10_repartition", "Fonction de répartition", [
    "Les grands F i ne sont définis que pour les valeurs observées. Mais quelle est la part des étudiants de 19 ans et demi ou moins ?",
    "Pour répondre pour n'importe quel x, on définit la fonction de répartition, F de x.",
    "F de x égale la part des observations inférieures ou égales à x. Dans la partie probabilités, tu l'écriras : probabilité que X soit inférieur ou égal à x.",
    "Son graphique est un escalier. Comme un vrai escalier : tant que tu n'atteins pas la marche suivante, tu restes au même niveau.",
    "Avant 17 ans, personne. F de 16 vaut 0.",
    "Entre 19 et 20, on reste sur la même marche. F de 19 et demi égale F de 19, soit 0,75.",
    "Après 21 ans, tout le monde est compté. F de 25 vaut 1.",
    "Regarde bien le bord des marches. Le point plein est à gauche : la marche est fermée à gauche et ouverte à droite.",
    "Donc en x égale 20, on est déjà sur la nouvelle marche. F de 20 vaut 0,875, et pas 0,75.",
    "À retenir : F de x est la part des observations inférieures ou égales à x. En discret, c'est un escalier, fermé à gauche, ouvert à droite.",
])
def _(c, s):
    if s == 9:
        c.retenir([r"$F(x)$ = part des observations $\leq x$",
                   "Discret : escalier fermé à gauche, ouvert à droite"])
        return
    c.title("Fonction de répartition", "Le cas discret" if s <= 2 else None)
    if s <= 2:
        c.text(960, 380, "Part des étudiants de 19,5 ans ou moins ?", size=54, ha="center",
               color=ACCENT if s == 0 else FG)
        if s >= 1:
            c.formula([r"$F(x)$", r"$=$", r"part des observations $\leq x$"], 960, 560, size=64,
                      hl=(0,) if s == 1 else ())
        if s >= 2:
            c.text(960, 720, r"plus tard :  $F(x) = P(X \leq x)$", size=48, color=MUTED, ha="center")
        return
    marks = {4: [(16, 0)], 5: [(19.5, 0.75)], 6: [(22, 1)], 8: [(20, 0.875)]}.get(s, [])
    stair(c, marks=marks, zoom20=s in (7, 8))
    X = 1520
    if s == 3:
        c.text(X, 450, "un escalier", size=50, ha="center", color=ACCENT)
        c.text(X, 530, "défini pour tout x", size=44, ha="center", color=MUTED)
    if s == 4:
        c.text(X, 500, r"$F(16) = 0$", size=60, ha="center", color=ACCENT)
    if s == 5:
        c.text(X, 460, r"$F(19{,}5) = F(19)$", size=56, ha="center", color=ACCENT)
        c.text(X, 550, r"$= 0{,}75$", size=56, ha="center", color=ACCENT)
    if s == 6:
        c.text(X, 500, r"$F(25) = 1$", size=60, ha="center", color=ACCENT)
        c.text(X, 580, "(hors graphique)", size=40, ha="center", color=MUTED)
    if s in (7, 8):
        c.text(X, 400, "●  fermé à gauche", size=44, ha="center", color=PRIMARY)
        c.text(X, 480, "○  ouvert à droite", size=44, ha="center", color=PRIMARY)
    if s == 8:
        c.text(X, 620, r"$F(20) = 0{,}875$", size=56, ha="center", color=ACCENT)
        c.text(X, 700, r"et pas $0{,}75$", size=46, ha="center", color=MUTED)


# ------------------------------------------------------------------ récap 1
@scene("p1_11_recap", "Récapitulatif", [
    "Récapitulons la partie 1.",
    "Une observation est qualitative, quantitative discrète, ou quantitative continue.",
    "La fréquence relative f i vaut n i sur n. Les n i ont pour somme n, et les f i ont pour somme 1.",
    "La fréquence cumulée grand N i additionne les n j jusqu'à i. Et grand F i vaut grand N i sur n.",
    "La fonction de répartition F de x donne la part des observations inférieures ou égales à x. En discret, c'est un escalier.",
    "Pour la part entre deux valeurs, on soustrait deux F. Dans la partie 2, on passe aux données continues.",
])
def _(c, s):
    c.title("Fiche récap — Partie 1")
    lines = [
        "Qualitatif · Quantitatif discret · Quantitatif continu",
        r"$f_i = n_i / n$        $\sum n_i = n$        $\sum f_i = 1$",
        r"$N_i = n_1 + \dots + n_i$        $F_i = N_i / n$",
        r"$F(x)$ = part des observations $\leq x$  (escalier)",
        r"Entre $a$ et $b$ :  $F(b) - F(a)$",
    ]
    for k, l in enumerate(lines):
        if s >= k + 1:
            y = 270 + k * 140
            c.box(150, y - 55, 1620, 110, fc=PANEL, ec=ACCENT if s == k + 1 else None, lw=3)
            c.text(200, y, l, size=46, color=FG)
