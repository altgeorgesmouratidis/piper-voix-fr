# 5ANA1D – Chapitre 2, partie 2 : Dispersion, transformations et autres moyennes

La moyenne ne suffit pas à décrire une série : 9, 10, 10, 11 et 0, 5, 15, 20 ont la même moyenne (10), mais la seconde série est beaucoup plus étalée. Les paramètres de dispersion mesurent cet étalement autour de $\bar{x}$. Ils ne s'appliquent qu'aux données quantitatives.

## Étendue $E_t$
- Définition : $E_t = x_{\max} - x_{\min}$. En continu, on prend la borne supérieure de la dernière classe moins la borne inférieure de la première.
- Exemples :
  - série A : $11 - 9 = 2$ ;
  - série B : $20 - 0 = 20$ ;
  - poids : $100 - 50 = 50$ kg.
- ⚠ Elle ne regarde que les valeurs extrêmes, ce qui la rend peu informative.

## Écart-moyen $E_m$
- Définition : $E_m = \dfrac{1}{n}\sum_{i=1}^{n} |x_i - \bar{x}|$. C'est la distance moyenne à la moyenne. La valeur absolue empêche les écarts de s'annuler.
- Exemple avec 4, 6, 8, 10, 12 : $\bar{x} = 8$, les écarts valent 4, 2, 0, 2, 4, et donc $E_m = 12/5 = 2{,}4$.

## Variance $s^2$ et écart-type $s$ ⚠
- Formule de base : $s^2 = \dfrac{1}{n}\sum_{i=1}^{n} (x_i - \bar{x})^2$, et $s = \sqrt{s^2}$.
- **Formule pratique** (à retenir) : $s^2 = \dfrac{1}{n}\sum_{i=1}^{n} x_i^2 - \bar{x}^2$, c'est-à-dire la moyenne des carrés moins le carré de la moyenne.
- Exemple avec 4, 6, 8, 10, 12 :
  - formule de base : $s^2 = 40/5 = 8$ ;
  - formule pratique : $360/5 - 8^2 = 72 - 64 = 8$, on trouve le même résultat ;
  - $s = \sqrt{8} \approx 2{,}83$.
- $s$ est toujours proche de $E_m$ et légèrement plus grand (ici 2,83 contre 2,4).
- L'écart-type est préféré à l'écart-moyen pour deux raisons : sa formule est plus maniable (pas de valeur absolue) et il joue un rôle central en probabilité. $s^2$ s'exprime en unités au carré, alors que $s$ est dans l'unité des données.
- En classes : $s^2 = \sum f_i\,c_i^2 - \bar{x}^2$. Exemple avec les poids : $5425 - 72{,}75^2 \approx 132{,}44$, donc $s \approx 11{,}51$ kg.

## Règle 68 – 95 – 99
- L'intervalle $[\bar{x} - s\,;\,\bar{x} + s]$ contient environ 68 % des valeurs, $[\bar{x} - 2s\,;\,\bar{x} + 2s]$ environ 95 % et $[\bar{x} - 3s\,;\,\bar{x} + 3s]$ environ 99 %.
- Exemple avec un trajet de 30 min en moyenne et $s = 5$ min : $[25\,;\,35]$ contient environ 68 % des trajets, $[20\,;\,40]$ environ 95 % et $[15\,;\,45]$ environ 99 %.
- Ce sont des approximations : elles supposent une distribution à peu près symétrique et beaucoup d'observations (loi normale, vue plus tard dans le cours).

## Changement d'origine et d'unité : $u_i = a\,x_i + b$
- Un changement d'origine ajoute $+\,b$ à chaque valeur (+50 € sur chaque salaire, −1 point sur chaque copie). Un changement d'unité multiplie chaque valeur par $a \neq 0$ (×1,05, conversion € → $, note sur 30 ramenée sur 20).
- La **position** subit tout : $\bar{u} = a\bar{x} + b$, $u_M = a\,x_M + b$, $u_{1/2} = a\,x_{1/2} + b$.
- La **dispersion** ignore $+\,b$ : $s_u = |a|\,s_x$, $E_t(u) = |a|\,E_t(x)$, $E_m(u) = |a|\,E_m(x)$.
- ⚠ Le cours écrit $s_u = a\,s_x$, ce qui n'est vrai que si $a > 0$. Un écart-type est toujours positif, la formule exacte est donc celle avec $|a|$.
- Exemple : une interro sur 30 a $\bar{x} = 18$ et $s = 6$.
  - Ramenée sur 20 ($a = 2/3$) : $\bar{u} = 12$ et $s = 4$.
  - Avec +1 point de bonus : $\bar{u} = 13$, et $s$ reste égal à 4.

## Autres moyennes
- **Pondérée** : $\bar{x} = \dfrac{P_1x_1 + \dots + P_nx_n}{P_1 + \dots + P_n}$.
  - Exemple avec les pondérations ESI 8, 8, 2 et les notes 12, 14, 17 : $242/18 \approx 13{,}44$.
  - C'est la même formule qu'avec les $n_i$ ou que pour une réunion de groupes. En physique, elle donne le centre de gravité.
- **Géométrique** : $\bar{x}_G = \sqrt[n]{x_1x_2\cdots x_n}$, et $\log\bar{x}_G = \frac{1}{n}\sum\log x_i$. Elle sert pour les taux moyens.
  - Exemple avec +10 % puis +30 % : $\sqrt{1{,}10 \times 1{,}30} = \sqrt{1{,}43} \approx 1{,}1958$, soit environ 19,58 %/an.
  - ⚠ Ce n'est pas 20 %, car $1{,}2^2 = 1{,}44$.
- **Harmonique** : $\dfrac{1}{\bar{x}_H} = \dfrac{1}{n}\left(\dfrac{1}{x_1} + \dots + \dfrac{1}{x_n}\right)$. Elle sert pour des vitesses sur une même distance.
  - Exemple avec 60 et 40 km/h sur 120 km chacun : 240 km en 5 h, soit $\bar{x}_H = 48$ km/h, et non 50.

## Coefficient de variation $C_v$ ⚠
- Définition : $C_v = \dfrac{s}{\bar{x}}$. C'est un paramètre hybride, qui combine position et dispersion. Il mesure la dispersion relative à l'ordre de grandeur et permet de comparer des séries sur des **échelles différentes**.
- Exemple :
  - action A (200 €, $s = 10$) : $C_v = 0{,}05$ ;
  - action B (20 €, $s = 4$) : $C_v = 0{,}20$.
  - B a l'écart-type le plus petit, mais elle est 4 fois plus volatile par rapport à son prix.

## Tableau récapitulatif (logique)

| | Brutes | Recensées | Classes |
|---|---|---|---|
| $\bar{x}$ | $\frac{1}{n}\sum x_i$ | $\sum f_i x_i$ | $\sum f_i c_i$ |
| $E_m$ | $\frac{1}{n}\sum \lvert x_i - \bar{x}\rvert$ | $\sum f_i \lvert x_i - \bar{x}\rvert$ | $\sum f_i \lvert c_i - \bar{x}\rvert$ |
| $s^2$ | $\frac{1}{n}\sum x_i^2 - \bar{x}^2$ | $\sum f_i x_i^2 - \bar{x}^2$ | $\sum f_i c_i^2 - \bar{x}^2$ |

Avec les $n_i$, on remplace $f_i$ par $n_i/n$.
