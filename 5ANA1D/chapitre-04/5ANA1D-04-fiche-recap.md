# 5ANA1D – Chapitre 4 : Analyse en composantes principales (ACP)

## Points à retenir

- Au-delà de 3 variables, on ne peut plus dessiner le nuage de points : il faut **réduire** le nombre de dimensions.
- **Matrice des corrélations** : la case $(i, j)$ contient $r(X_i, X_j)$. Elle est symétrique, avec des 1 sur la diagonale. Deux variables très corrélées apportent presque la même information.
- **Réduire ≠ supprimer** : on remplace les variables par des **combinaisons linéaires** (somme de variables multipliées par des nombres).
- **Idée de l'ACP** : représenter les données en dimension réduite (idéalement 2) en les déformant le moins possible, c'est-à-dire choisir l'axe où les projections sont **le plus dispersées**.
- **Dispersion maximale ⇔ somme des écarts² minimale** (écarts **perpendiculaires** à la droite, Pythagore). Cet axe est proche de la droite de régression, mais pas identique : la régression mesure les écarts **verticaux**.
- Le meilleur axe n'est ni X ni Y, mais une **combinaison linéaire** de X et Y.
- **Matrice des variances-covariances** : la case $(i, j)$ contient $\sigma(X_i, X_j)$. La diagonale contient les variances.
- Ses **vecteurs propres** donnent les nouveaux axes. Chaque **valeur propre** est égale à la **variance des données projetées** sur l'axe de son vecteur propre.
- **En 2D** : on garde les 2 vecteurs propres des **2 plus grandes valeurs propres** (plan de dispersion maximale).

## Formules

| Formule | Sens | Mini-exemple |
|---|---|---|
| $S = \tfrac12\,\text{math} + \tfrac12\,\text{phys}$ | combinaison linéaire | élève 3 : $\tfrac12 \cdot 6 + \tfrac12 \cdot 7 = 6{,}5$ |
| $M_{ij} = \sigma(X_i, X_j)$ | matrice des variances-covariances | points A à F : $M = \begin{pmatrix} 11{,}67 & 3{,}33 \\ 3{,}33 & 6{,}67 \end{pmatrix}$ |
| $M u = \lambda u$ | vecteur propre $u$, valeur propre $\lambda$ | $M \binom{2}{1} = \binom{26{,}67}{13{,}33} = 13{,}33 \binom{2}{1}$ donc $\lambda_1 = 13{,}33$ |
| $\lambda = $ variance des projections sur l'axe de $u$ | propriété clé | $\frac{121+36+9+1+64+169}{5 \times 6} = \frac{400}{30} = 13{,}33$ |
| part gardée $= \dfrac{\lambda}{\sum \lambda}$ | information conservée par un axe | $\frac{13{,}33}{18{,}33} = 73\,\%$ (axe X seul : 64 %) |

## Exemple fil rouge (points A à F)

A(1;1), B(0;8), C(2;7), D(4;5), E(8;6), F(9;9), centre (4 ; 6).

- Projection sur X : ordre B A C D E F. Sur Y : A D E C B F. Sur le meilleur axe $z = \frac{2(x-4) + (y-6)}{\sqrt5}$ : A B C D E F.
- Étalement / Σ écarts² : horizontale 70 / 40, verticale 40 / 70, **meilleur axe 80 / 30**. Total toujours 110.
- $\lambda_1 = 13{,}33$, $\lambda_2 = 5$, $\lambda_1 + \lambda_2 = 18{,}33 = 11{,}67 + 6{,}67$.

## Exemple des 9 élèves (4 cotes)

- Corrélations : math–phys 0,98 ; angl–néer 0,95 ; math–angl 0,23.
- Valeurs propres : 28,71 ; 12,08 ; 0,04 ; 0,01. Les deux premières gardent 70,3 % + 29,6 % = **99,9 %**.
- $u_1 \approx (0{,}51 ; 0{,}50 ; 0{,}49 ; 0{,}50)$ : niveau général. $u_2 \approx (-0{,}58 ; -0{,}38 ; 0{,}65 ; 0{,}32)$ : langues − sciences.
