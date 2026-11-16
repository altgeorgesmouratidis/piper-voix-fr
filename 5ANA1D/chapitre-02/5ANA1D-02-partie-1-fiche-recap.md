# 5ANA1D – Chapitre 2, partie 1 : Les paramètres de position

Il existe trois familles de paramètres statistiques :
- **position** : où se trouvent les valeurs ;
- **dispersion** : à quel point elles sont étalées (partie 2) ;
- **forme** : hors programme.

## Mode $x_M$
- Le mode est l'observation **la plus fréquente**. En discret ou en qualitatif, c'est le $x_i$ qui a le plus grand $n_i$ (ou $f_i$). Exemple : le premier tableau de la section Médiane a pour mode $x_M = 50$ ($n_i = 6$).
- En continu, on parle de **classe modale** : c'est la classe qui a la plus forte densité $df_i = f_i / l_i$. Si toutes les classes ont la même largeur, on peut prendre directement le plus grand $f_i$.
  - Exemple avec les poids : les densités valent 0,017 / **0,035** / 0,025 / 0,010, donc la classe modale est $[65, 75[$.
- Limites :
  - le mode peut avoir des ex aequo ;
  - si toutes les valeurs ont le même effectif, on considère qu'il n'y a pas de mode ;
  - ⚠ il peut tomber sur une **valeur aberrante**. Exemple : avec les notes 0, 0, 0, 11, 12, 13, 14, 15, 16, 17, on obtient $x_M = 0$ à cause des feuilles blanches, alors que la médiane vaut 12,5.

## Médiane $x_{1/2}$
- La médiane est l'« observation du milieu » : 50 % des valeurs sont en dessous, 50 % au-dessus. Elle n'existe pas en qualitatif, car il faut pouvoir classer les valeurs.
- **Données brutes** (classées dans l'ordre croissant) :
  - si $n$ est impair, $x_{1/2} = x_{(n+1)/2}$. Exemple : la médiane de 2, 3, 5, 5, 6, 7, 9 vaut 5 ;
  - si $n$ est pair, $x_{1/2} = \frac{1}{2}\left(x_{n/2} + x_{n/2+1}\right)$. Exemple : en ajoutant 10 à la série précédente, on obtient $\frac{5+6}{2} = 5{,}5$.
- **Tableau recensé** : on cherche le premier $N_i \geq n/2$ (ou le premier $F_i \geq 0{,}5$).
  - Si $N_i > n/2$ (strictement), alors $x_{1/2} = x_i$.
  - Si $N_i = n/2$ exactement (ce qui n'arrive que si $n$ est pair), alors $x_{1/2} = \frac{1}{2}(x_i + x_{i+1})$.

Les deux exemples du cours portent sur deux séries différentes.

| $x_i$ | $n_i$ | $N_i$ |
|---|---|---|
| 30 | 2 | 2 |
| 40 | 4 | 6 |
| 50 | 6 | **12** |
| 60 | 5 | 17 |
| 70 | 3 | 20 |

Ici $n/2 = 10$ et $12 > 10$, donc $x_{1/2} = 50$.

| $x_i$ | $f_i$ | $F_i$ |
|---|---|---|
| 30 | 0,10 | 0,10 |
| 40 | 0,15 | 0,25 |
| 50 | 0,25 | **0,50** |
| 60 | 0,30 | 0,80 |
| 70 | 0,20 | 1 |

Ici $F_3 = 0{,}5$ pile, donc $x_{1/2} = \frac{50+60}{2} = 55$.

- **Continu** : on résout $F(x) = 0{,}5$. Pour les poids, la médiane est dans $[65, 75[$ : $0{,}035(x - 65) + 0{,}25 = 0{,}5$ donne $x_{1/2} \approx 72{,}14$ kg.
  - On trouve le même résultat par une règle de trois : $\dfrac{x - 65}{10} = \dfrac{0{,}25}{0{,}35}$.

## Quartiles, déciles, centiles
- Les **quartiles** partagent les observations en 4 groupes d'effectif égal. On a $F(x_{1/4}) = 0{,}25$, $x_{2/4} = x_{1/2}$ et $F(x_{3/4}) = 0{,}75$.
  - Exemple avec les poids : $x_{1/4} = 65$ kg, car $F(65) = 0{,}25$ pile.
  - $0{,}025(x - 75) + 0{,}6 = 0{,}75$ donne $x_{3/4} = 81$ kg.
- Il existe aussi 9 **déciles** ($x_{1/10}, \dots, x_{9/10}$) et 99 **centiles**, calculés de la même façon. Ces paramètres ont surtout du sens en continu, avec beaucoup d'observations.

## Moyenne $\bar{x}$
- Elle n'existe que pour des données quantitatives.
- Données brutes : $\bar{x} = \dfrac{1}{n}\sum_{i=1}^{n} x_i$.
- Tableau recensé : $\bar{x} = \dfrac{1}{n}\sum_{i=1}^{k} n_i\,x_i = \sum_{i=1}^{k} f_i\,x_i$. Exemple avec le premier tableau ci-dessus : $\dfrac{1030}{20} = 51{,}5$.
- Classes : $\bar{x} = \sum_{i=1}^{k} f_i\,c_i$, où le centre de classe vaut $c_i = \dfrac{x_{i-1} + x_i}{2}$.
  - Exemple avec les poids : $0{,}25 \times 57{,}5 + 0{,}35 \times 70 + 0{,}25 \times 80 + 0{,}15 \times 92{,}5 = 72{,}75$ kg.

## Moyenne d'une réunion de groupes
- Formule : $\bar{x} = \dfrac{n_1\bar{x}_1 + n_2\bar{x}_2 + \dots + n_k\bar{x}_k}{n_1 + n_2 + \dots + n_k}$.
- Exemple : le groupe A compte 30 étudiants (moyenne 12) et le groupe B 20 étudiants (moyenne 15). On obtient $\dfrac{360 + 300}{50} = 13{,}2$.
- ⚠ Ce n'est pas $\frac{12+15}{2} = 13{,}5$, car les groupes n'ont pas le même effectif.
