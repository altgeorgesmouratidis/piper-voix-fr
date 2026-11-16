# 5ANA1D – Chapitre 3, partie 1 : Couples discrets, corrélation et régression

Dans une distribution à deux dimensions, on mesure **deux caractéristiques** sur chaque individu, par exemple une taille $X$ et un poids $Y$. Le but est de savoir s'il existe un **lien** entre les deux, c'est-à-dire si connaître $X$ permet d'estimer $Y$.

Exemple suivi tout au long de la fiche : les cotes de maths ($x_i$) et de stat ($y_i$) de 10 étudiants.

(12, 14) · (10, 8) · (16, 14) · (14, 10) · (11, 13) · (8, 9) · (12, 10) · (15, 12) · (13, 11) · (7, 10)

## Nuage de points
- Chaque couple $(x_i ; y_i)$ devient un point d'un plan : $X$ sur l'axe horizontal, $Y$ sur l'axe vertical.
- L'ensemble de ces points forme le **nuage de points**. Ici, on voit une tendance : en gros, quand la cote de maths monte, la cote de stat monte aussi.

## Moyennes et écarts-types
- Chaque variable garde ses propres paramètres, calculés comme au chapitre 2 :
  - $\bar{x} = 11{,}8$ et $s_x = 2{,}75$ ;
  - $\bar{y} = 11{,}1$ et $s_y = 1{,}97$.
- Ces quatre nombres ne disent **rien du lien** entre $X$ et $Y$.

## Covariance $s_{xy}$
- **Idée** : les droites $x = \bar{x}$ et $y = \bar{y}$ découpent le nuage en quatre zones. Pour chaque point, on calcule le produit $(x_i - \bar{x})(y_i - \bar{y})$.
  - Ce produit est **positif** en haut à droite et en bas à gauche, **négatif** dans les deux autres zones.
  - Exemple : le point (16 ; 14) donne $4{,}2 \times 2{,}9 = +12{,}18$.
- **Définition** : $s_{xy} = \dfrac{1}{n}\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})$
- **Formule pratique** : $s_{xy} = \dfrac{1}{n}\sum_{i=1}^{n} x_i y_i - \bar{x}\,\bar{y}$
  - Exemple : $\sum x_i y_i = 1340$, donc $s_{xy} = 134 - 11{,}8 \times 11{,}1 = 3{,}02$. La définition donne la même valeur.
- Si $s_{xy} > 0$, $X$ et $Y$ ont tendance à varier dans le même sens. Si $s_{xy} < 0$, ils varient en sens inverse.

## Coefficient de corrélation $r$
- La covariance dépend des **unités** (cm ou m, par exemple). On la divise donc par les deux écarts-types pour obtenir un nombre sans unité :

$$r = \frac{s_{xy}}{s_x\, s_y}$$

- On a toujours $-1 \le r \le 1$.
  - Plus $|r|$ est proche de 1, plus le lien est **fort**.
  - Plus $|r|$ est proche de 0, plus le lien est **faible**.
- Exemple : $r = \dfrac{3{,}02}{2{,}75 \times 1{,}97} = 0{,}557$. C'est un lien positif d'intensité moyenne.

## Lire un nuage selon $r$
- $r = 1$ : les points sont alignés sur une droite qui monte. $r = -1$ : ils sont alignés sur une droite qui descend.
- $0 < r < 1$ : le nuage est allongé et monte. $-1 < r < 0$ : quand $X$ augmente, $Y$ diminue.
- $r = 0$ : le nuage n'a pas de direction, il n'y a pas de lien **linéaire**.
- Le **signe** de $r$ donne le sens du lien, sa **valeur absolue** en donne la force.
- ⚠ $r$ mesure l'**alignement** des points, pas la pente. La forme du nuage (écrasé ou étiré) dépend de la comparaison entre $s_x$ et $s_y$ :
  - si $s_x > s_y$, le nuage est écrasé et la pente est faible ;
  - si $s_x < s_y$, le nuage est étiré vers le haut et la pente est forte.

## Droite de régression (droite des moindres carrés)
- C'est la droite $y = ax + b$ qui rend **minimale** la somme des carrés des écarts verticaux entre les points et la droite :

$$\min_{a,\,b}\ \sum_{i=1}^{n}(a x_i + b - y_i)^2$$

- On prend des carrés pour que les écarts au-dessus et en dessous de la droite ne s'annulent pas.
- Coefficients :

$$a = \frac{s_{xy}}{s_x^2} \qquad b = \bar{y} - a\,\bar{x}$$

- Exemple :
  - $a = \dfrac{3{,}02}{2{,}75^2} \approx 0{,}399$ ;
  - $b = 11{,}1 - 0{,}399 \times 11{,}8 \approx 6{,}39$ ;
  - la droite est donc $y \approx 0{,}4\,x + 6{,}4$.
- Lecture de la droite :
  - la pente $a = \Delta y / \Delta x \approx 0{,}4$ : un point de plus en maths donne, en moyenne, 0,4 point de plus en stat ;
  - $b \approx 6{,}4$ est la valeur de $y$ quand $x = 0$.
- Prédiction : avec 14 en maths, on obtient $0{,}4 \times 14 + 6{,}4 = 12$ en stat. C'est une estimation, pas une certitude.

## Démonstration (en résumé)
1. On pose $S(a, b) = \sum (a x_i + b - y_i)^2$. Au minimum, les dérivées partielles par rapport à $a$ et à $b$ s'annulent.
2. On applique la règle $(u^n)' = n\,u'\,u^{n-1}$ avec $u = a x_i + b - y_i$ et $n = 2$. Selon $a$, $u' = x_i$ ; selon $b$, $u' = 1$.
3. On obtient deux équations :
   - (1) : $\sum 2(a x_i + b - y_i)\,x_i = 0$ ;
   - (2) : $\sum 2(a x_i + b - y_i) = 0$.
4. De (2), après division par $n$ : $a\bar{x} + b - \bar{y} = 0$, donc $b = \bar{y} - a\bar{x}$.
5. On remplace $b$ dans (1), puis on divise par $n$ : $a\left(\frac{1}{n}\sum x_i^2 - \bar{x}^2\right) = \frac{1}{n}\sum x_i y_i - \bar{x}\,\bar{y}$. On a donc $a\,s_x^2 = s_{xy}$, d'où $a = \dfrac{s_{xy}}{s_x^2}$.

## Signe de la pente
- Comme $s_x^2 > 0$, la pente $a$ a **toujours le même signe que $s_{xy}$**.
- Si $s_{xy} = 0$, la droite est horizontale : $y = \bar{y}$.
