# 5ANA1D – Chapitre 7, partie 1 : la distribution normale (courbe en cloche et table)

## Points à retenir
- La distribution normale (ou de Gauss) est la loi continue la plus utilisée : tailles, poids des œufs, températures, QI, durées de vie.
- Elle a deux paramètres : $\mu$ (espérance, moyenne) et $\sigma$ (écart-type). Notation : $X \sim N(\mu, \sigma)$.
- La courbe en cloche est symétrique en $\mu$, a son sommet en $x = \mu$, et l'axe des $x$ est une asymptote horizontale.
- Les points d'inflexion sont en $\mu - \sigma$ et $\mu + \sigma$ : $\sigma$ se lit comme la distance entre le sommet et un point d'inflexion.
- L'aire totale sous la courbe vaut 1 (admis).
- Une probabilité est une aire, mais $e^{-x^2}$ n'a pas de primitive élémentaire : on utilise une table.
- La normale réduite $Z \sim N(0, 1)$ est centrée ($\mu = 0$) et réduite ($\sigma = 1$). Ses points d'inflexion sont en $-1$ et $1$.
- La table donne $F(x) = P[Z \le x]$, l'aire à gauche de $x$, pour $x$ de 0 à 3 (pas de 0,01, 4 décimales).
- Pour lire la table, la ligne donne l'unité et la 1re décimale, la colonne donne la 2e décimale.
- Pour $x$ négatif, on utilise la symétrie.

## Formules
- Densité : $f(x) = \dfrac{1}{\sigma\sqrt{2\pi}}\, e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}$
  - Exemple, avec des œufs tels que $X \sim N(60, 5)$ : $f(60) = \dfrac{1}{5\sqrt{2\pi}} \approx 0{,}0798$. C'est une hauteur de courbe, pas une probabilité.
- $P[a \le X \le b] = \displaystyle\int_a^b f(x)\,dx = F(b) - F(a)$
- Normale réduite : $f(x) = \dfrac{1}{\sqrt{2\pi}}\, e^{-\frac{1}{2}x^2}$
- Répartition : $F(x) = P[Z \le x] = \dfrac{1}{\sqrt{2\pi}} \displaystyle\int_{-\infty}^{x} e^{-\frac{1}{2}t^2}\,dt$
  - Exemple : $F(1{,}25) = 0{,}8944$ (ligne 1,2, colonne 0,05).
- Approximation de Mac Laurin, valable pour $|x| < 1$ : $F(x) \approx \dfrac{1}{2} + \dfrac{1}{\sqrt{2\pi}}\left(x - \dfrac{x^3}{6} + \dfrac{x^5}{40} - \dfrac{x^7}{336}\right)$
  - Exemple : en $x = 0{,}5$, elle donne $0{,}6915$, comme la table. En $x = 2$, elle donne $0{,}9331$ au lieu de $0{,}9772$.
- Symétrie : $F(-x) = 1 - F(x)$
  - Exemples : $F(-1) = 1 - 0{,}8413 = 0{,}1587$ et $F(-1{,}25) = 1 - 0{,}8944 = 0{,}1056$.

Pour aller plus loin (lien noté dans le cours) : https://www.geogebra.org/m/uRZ5DKGn
