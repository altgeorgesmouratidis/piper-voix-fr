# 5ANA1D – Chapitre 1, partie 1 : Statistique descriptive (vocabulaire et observations discrètes)

## Vocabulaire
- **Population** : l'ensemble des individus étudiés. Un individu n'est pas forcément une personne : ça peut être une voiture, un oiseau ou une commune.
- **Échantillon** : la partie de la population qu'on interroge vraiment. Il doit être représentatif.
- **Effectif** $n$ : le nombre d'observations.
- **Types d'observations** :
  - qualitatives (non numériques) : marque de GSM ;
  - quantitatives discrètes (valeurs isolées et dénombrables) : nombre d'enfants, interro sur 20 avec des demi-points (41 valeurs) ;
  - quantitatives continues (toutes les valeurs d'un intervalle) : poids d'un œuf. Arrondi au gramme, il devient du « continu discrétisé ».
- **Série chronologique** : des mesures à intervalles réguliers dans le temps. **Série statistique** : des mesures prises toutes au même moment.

## Exemple fil rouge
Âges de 16 étudiants : $n = 16$, $k = 5$ valeurs différentes, $x_1 = 17, \dots, x_5 = 21$.

| $x_i$ | $n_i$ | $N_i$ | $f_i$ | $F_i$ |
|---|---|---|---|---|
| 17 | 2 | 2 | 12,5 % | 12,5 % |
| 18 | 4 | 6 | 25 % | 37,5 % |
| 19 | 6 | 12 | 37,5 % | 75 % |
| 20 | 2 | 14 | 12,5 % | 87,5 % |
| 21 | 2 | 16 | 12,5 % | 100 % |

## Formules
- Fréquence absolue $n_i$ (tableau recensé) : $\sum_{i=1}^{k} n_i = n$. Exemple : $2+4+6+2+2 = 16$.
- Fréquence relative : $f_i = \dfrac{n_i}{n}$, avec $0 \le f_i \le 1$ et $\sum f_i = 1$. Exemple : $f_3 = 6/16 = 0{,}375$.
  - Démonstration : $\sum f_i = \sum \frac{n_i}{n} = \frac{1}{n}\sum n_i = \frac{n}{n} = 1$.
- Fréquence absolue cumulée : $N_i = \sum_{j=1}^{i} n_j = N_{i-1} + n_i$, avec $N_1 = n_1$ et $N_k = n$. C'est le nombre d'observations $\le x_i$. Exemple : $N_3 = 12$.
- Fréquence relative cumulée : $F_i = \sum_{j=1}^{i} f_j = \dfrac{N_i}{n}$, avec $F_1 = f_1$ et $F_k = 1$. Exemple : $F_3 = 12/16 = 0{,}75$.

## Lire le tableau
- Observations $\le x$ : $F(x)$. Exemple : 75 % ont 19 ans ou moins.
- Observations $> x$ : $1 - F(x)$. Exemple : 25 % ont plus de 19 ans.
- Observations entre $a$ et $b$ : $F(b) - F(\text{valeur juste avant } a)$. Exemple : entre 18 et 20 ans, $87{,}5\,\% - 12{,}5\,\% = 75\,\%$. On soustrait $F(17)$, pas $F(18)$.

## Graphiques
- **Diagramme en bâtonnets** : $x_i$ en abscisse, $n_i$ ou $f_i$ en ordonnée. L'allure est la même, seule l'échelle change. Si les valeurs sont très inégales, on utilise une échelle $\log_{10}$.
- **Fonction de répartition** : $F(x) = P(X \le x)$ est le pourcentage des observations $\le x$. Son graphique est un escalier, avec des paliers fermés à gauche et ouverts à droite. Elle est définie pour tout réel $x$ : $F(16) = 0$, $F(19{,}5) = F(19) = 0{,}75$, $F(25) = 1$.
