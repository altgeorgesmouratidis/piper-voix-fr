# 5ANA1D – Chapitre 6, partie 1 : Variables aléatoires discrètes

## Points à retenir

- **Variable aléatoire** $X$ : associe une valeur réelle au résultat d'une expérience aléatoire, donc $X : \Omega \to \mathbb{R}$.
- **Discrète** : ensemble de valeurs fini (dé, jeu, nombre de 6 en 3 lancers) ou infini dénombrable (lancers jusqu'au premier 6). **Continue** : un intervalle de réels (taille) → partie 2.
- **Distribution de probabilité** : les valeurs $x_i$ avec leurs probabilités $p_i = P[X = x_i]$, dessinées en diagramme en bâtonnets.
- **Fonction de répartition** : $F(x) = P[X \le x]$, avec **inférieur OU égal** (la valeur $x$ est comprise). Graphe en escalier, de 0 à gauche à 1 à droite. Définie pour **tout** réel $x$.
- **Lien avec la statistique descriptive** : $f_i \leftrightarrow p_i$, $F_i \leftrightarrow F(x_i)$. Avant : des observations existantes. Ici : des valeurs théoriques.
- **Écart-type** (ordre de grandeur) : environ 68 % des valeurs dans $[\mu - \sigma, \mu + \sigma]$, 95 % dans $[\mu - 2\sigma, \mu + 2\sigma]$, à peine 1 % au-delà de $3\sigma$. Ce sont des indications, la vraie proportion dépend de la distribution.

## Formules

Exemple suivi : le jeu de dé (6 → +3 €, 2 ou 4 → −2 €, sinon 0 €).

| $x_i$ | $-2$ | $0$ | $3$ |
|---|---|---|---|
| $p_i$ | $\frac13$ | $\frac12$ | $\frac16$ |
| $F(x_i)$ | $\frac13$ | $\frac56$ | $1$ |

$$\sum_{i=1}^{n} p_i = 1$$
Exemple : $\frac13 + \frac12 + \frac16 = \frac26 + \frac36 + \frac16 = 1$.

$$F(x) = P[X \le x]$$
Exemple : $F(1) = \frac56$, alors que $P[X = 1] = 0$ (gagner **au plus** 1 €).

$$\mu = E[X] = \sum_{i=1}^{n} p_i x_i$$
Exemple : $(-2)\cdot\frac13 + 0\cdot\frac12 + 3\cdot\frac16 = -\frac16 \approx -0{,}17$ € par partie. Vérification sur 600 parties : $\frac{-400 + 300}{600} = -\frac16$.

$$\sigma^2 = \sum_{i=1}^{n} p_i (x_i - \mu)^2 = \sum_{i=1}^{n} p_i x_i^2 - \mu^2$$
Exemple : $\frac{17}{6} - \frac{1}{36} = \frac{101}{36} \approx 2{,}81$, donc $\sigma \approx 1{,}67$ €. La formule de définition donne le même résultat.
