# 5ANA1D – Chapitre 1, partie 2 : Statistique descriptive (observations continues et qualitatives)

## Classes
- En continu, chaque valeur est presque unique : on groupe les données en **classes** $[x_{i-1}, x_i[$ contiguës, fermées à gauche et ouvertes à droite.
- Le choix des classes est arbitraire. La **règle de Sturge** donne un ordre de grandeur : $k \approx 1 + \frac{10}{3}\log_{10} n$. Exemple : $n = 80$ donne $k \approx 7{,}3$. C'est une indication, pas une obligation.
- Les classes peuvent avoir des largeurs différentes.
- **Hypothèse d'uniformité** : on suppose que les observations sont réparties régulièrement dans chaque classe. Exemple : 28 étudiants sur 10 kg, soit 2,8 par kilo.
- Dans le tableau par classes :
  - $n_i$ est le nombre d'observations dans la classe ;
  - $N_i$ est le nombre d'observations $< x_i$ (le bord droit) ;
  - $f_i = n_i / n$ et $F_i = N_i / n$.
  - Note : le cours écrit « $f_i$ est le nombre d'observations inférieures à $x_i$ » à la page 10. Il faut lire $N_i$.

| Classe (kg) | $n_i$ | $N_i$ | $f_i$ | $F_i$ | $dn_i$ | $df_i$ |
|---|---|---|---|---|---|---|
| [50, 65[ | 20 | 20 | 0,25 | 0,25 | ≈ 1,3 | ≈ 0,017 |
| [65, 75[ | 28 | 48 | 0,35 | 0,60 | 2,8 | 0,035 |
| [75, 85[ | 20 | 68 | 0,25 | 0,85 | 2 | 0,025 |
| [85, 100[ | 12 | 80 | 0,15 | 1 | 0,8 | 0,010 |

(≈ : valeurs arrondies, comme dans le cours.)

## Histogramme des densités
- Avec des rectangles de hauteur $n_i$, l'œil compare les aires $n_i \times l_i$, ce qui trompe. Exemple : les classes 1 et 3 ont toutes deux 20 étudiants, mais leurs aires valent 300 et 200.
- **Densité de fréquence absolue** : $dn_i = \dfrac{n_i}{l_i}$, avec $dn_i \times l_i = n_i$ = aire. L'aire totale vaut $n$. Exemple : $28/10 = 2{,}8$.
- **Densité de fréquence relative** : $df_i = \dfrac{f_i}{l_i}$, avec $df_i \times l_i = f_i$. L'aire totale vaut 1. Exemple : $0{,}35/10 = 0{,}035$.

## Polygone des fréquences cumulées ⚠
- On relie le point $(x_{i-1}\,;\,F_{i-1})$ au point $(x_i\,;\,F_i)$ par un segment. Grâce à l'hypothèse d'uniformité, $F$ est linéaire dans chaque classe.
- La pente du segment vaut $\dfrac{f_i}{l_i} = df_i$.
- L'équation du segment est $y = df_i\,(x - x_{i-1}) + F_{i-1}$. Exemple : pour $[65, 75[$, $y = 0{,}035(x-65) + 0{,}25$, et on retrouve $0{,}60$ en 75.
- $F(x)$ s'écrit par morceaux : 0 avant la première classe, 1 après la dernière. En continu, « $<$ » ou « $\le$ » donnent le même résultat, car la fréquence d'une valeur ponctuelle est 0.

## Utiliser $F(x)$
- Observations $< x$ : $F(x)$.
- Observations $> x$ : $1 - F(x)$.
- Observations entre $x_1$ et $x_2$ : $F(x_2) - F(x_1)$.
- Pour obtenir un effectif, on multiplie le pourcentage par $n$.
- Lecture inverse : on résout $F(x) = p$.
- Exemples :
  - $F(73) = 0{,}035 \times 8 + 0{,}25 = 0{,}53$, soit 53 % ;
  - $1 - 0{,}53 = 47\,\%$ ;
  - $80 \times 0{,}53 \approx 42$ étudiants ;
  - $F(81) - F(73) = 0{,}75 - 0{,}53 = 22\,\%$ ;
  - $F(x) = 0{,}3$ donne $x = 65 + 0{,}05/0{,}035 \approx 66{,}4$ kg.

## Qualitatif
- On utilise $n_i$ et $f_i$, mais **pas de fréquences cumulées** : les valeurs n'ont pas d'ordre numérique.
- Ordre de présentation : selon le contexte (avis du plus positif au moins positif), par fréquences décroissantes ou par ordre alphabétique.
- **Diagramme en fromage** : la surface de chaque part est proportionnelle à $f_i$, et son angle vaut $f_i \times 360°$. Exemple : « Satisfait » vaut $42/80 = 52{,}5\,\%$, soit un angle de 189°.
