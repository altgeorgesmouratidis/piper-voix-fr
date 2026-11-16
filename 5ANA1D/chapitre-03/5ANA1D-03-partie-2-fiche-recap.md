# 5ANA1D – Chapitre 3, partie 2 : Données continues et indépendance

Avec des données continues (une taille en cm, un poids en kg), presque toutes les valeurs sont différentes. On regroupe donc chaque variable **en classes**, puis on range les individus dans un **tableau à deux dimensions**.

## Tableau à deux dimensions
| $X \backslash Y$ | [50 ; 65[ | [65 ; 75[ | [75 ; 85[ | [85 ; 100[ | $f_{i.}$ |
|---|---|---|---|---|---|
| [140 ; 160[ | 0,05 | 0,10 | 0,05 | 0 | 0,20 |
| [160 ; 170[ | 0,05 | 0,12 | 0,08 | 0,05 | 0,30 |
| [170 ; 180[ | 0 | 0,08 | **0,17** | 0,08 | 0,33 |
| [180 ; 200[ | 0 | 0,05 | 0,10 | 0,02 | 0,17 |
| $f_{.j}$ | 0,10 | 0,35 | 0,40 | 0,15 | 1 |

- $f_{ij}$ est la proportion d'individus qui sont **à la fois** dans la classe $i$ de $X$ et dans la classe $j$ de $Y$. Exemple : $f_{33} = 0{,}17$, donc 17 % des individus mesurent entre 170 et 180 cm **et** pèsent entre 75 et 85 kg.
- Pour que la distribution soit correcte, il faut $\sum_i\sum_j f_{ij} = 1$.

## Fréquences marginales
- $f_{i.}$ est le total de la **ligne** $i$. Ces totaux forment la distribution de $X$ seule. Exemple : $f_{1.} = 0{,}05 + 0{,}10 + 0{,}05 + 0 = 0{,}20$.
- $f_{.j}$ est le total de la **colonne** $j$. Ces totaux forment la distribution de $Y$ seule. Exemple : $f_{.1} = 0{,}05 + 0{,}05 + 0 + 0 = 0{,}10$.
- Dans la notation, le **point** remplace l'indice sur lequel on a additionné.

## Paramètres par classes
Chaque classe est représentée par son **centre** : $x_i$ pour les lignes, $y_j$ pour les colonnes. Par exemple, $[140 ; 160[$ a pour centre 150 et $[50 ; 65[$ a pour centre 57,5.

- **Moyennes** : $\bar{x} = \sum_{i=1}^{m} f_{i.}\,x_i$ et $\bar{y} = \sum_{j=1}^{n} f_{.j}\,y_j$
  - On peut aussi écrire $\bar{x} = \sum_i\sum_j f_{ij}\,x_i$ : c'est la même chose, puisque additionner une ligne redonne $f_{i.}$.
  - Exemple : $\bar{x} = 150 \times 0{,}2 + 165 \times 0{,}3 + 175 \times 0{,}33 + 190 \times 0{,}17 = 169{,}55$ cm, et $\bar{y} = 76{,}125$ kg.
- **Variances** : $s_x^2 = \sum_{i} f_{i.}\,x_i^2 - \bar{x}^2$ et $s_y^2 = \sum_{j} f_{.j}\,y_j^2 - \bar{y}^2$
  - Exemple : $s_x = 12{,}789$ cm et $s_y = 9{,}698$ kg.
- **Covariance** : il faut parcourir toutes les cases du tableau, d'où une double somme.

$$s_{xy} = \sum_{i=1}^{m}\sum_{j=1}^{n} f_{ij}\,(x_i - \bar{x})(y_j - \bar{y}) = \sum_{i=1}^{m}\sum_{j=1}^{n} f_{ij}\,x_i\,y_j - \bar{x}\,\bar{y}$$

  - Pour chaque case, on multiplie la fréquence par le centre de la ligne et par le centre de la colonne. Exemple : la case 0,17 donne $0{,}17 \times 175 \times 80 = 2380$.
  - Exemple complet : $s_{xy} = 12\,952{,}25 - 169{,}55 \times 76{,}125 \approx 45{,}256$.
- **Corrélation** : la formule ne change pas. $r = \dfrac{s_{xy}}{s_x s_y} = \dfrac{45{,}256}{12{,}789 \times 9{,}698} \approx 0{,}365$, soit un lien positif plutôt faible.
- La **droite de régression** se calcule avec les mêmes formules que dans le cas discret.

## Indépendance
- $X$ et $Y$ sont **indépendants** si l'un n'a aucune influence sur l'autre. Exemple : la cote d'une interro de maths et la taille de l'élève.
- Dans le tableau, cela se traduit par : $f_{ij} = f_{i.} \cdot f_{.j}$ **pour chaque case**.
- Test sur notre tableau : $f_{1.} \cdot f_{.1} = 0{,}20 \times 0{,}10 = 0{,}02$, alors que $f_{11} = 0{,}05$. La taille et le poids ne sont donc **pas** indépendants.
- **Conséquence** : si $X$ et $Y$ sont indépendants, alors $s_{xy} = 0$ et $r = 0$. En effet :

$$s_{xy} = \Big(\sum_i f_{i.}\,x_i\Big)\Big(\sum_j f_{.j}\,y_j\Big) - \bar{x}\,\bar{y} = \bar{x}\,\bar{y} - \bar{x}\,\bar{y} = 0$$

- ⚠ **La réciproque est fausse.** Le cours écrit au début du paragraphe que les variables sont indépendantes « lorsque leur coefficient de corrélation est nul ». C'est inexact.
  - Contre-exemple : $x$ vaut −1, 0 et 1, et $y = x^2$ (donc $y$ vaut 1, 0 et 1).
  - On a $\bar{x} = 0$ et $\frac{1}{n}\sum x_i y_i = 0$, donc $s_{xy} = 0$ et $r = 0$.
  - Pourtant, $y$ dépend complètement de $x$ : $r$ ne détecte que les liens **linéaires**.
- À retenir : l'indépendance entraîne $r = 0$, mais $r = 0$ n'entraîne pas l'indépendance.
