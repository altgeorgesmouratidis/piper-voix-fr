# Script de la voix off — 5ANA1D chapitre 4

## Introduction  ·  00:00:00

Analyse de données, chapitre 4 : l'analyse en composantes principales, qu'on appelle aussi l'ACP.

L'idée : représenter des données à beaucoup de variables sur un simple graphique, en perdant le moins d'information possible.

## Trop de dimensions  ·  00:00:16

Au chapitre 2, on étudiait une seule variable. Ses valeurs tiennent sur une droite.

Au chapitre 3, on en étudiait deux. Chaque individu devient un point dans un plan : c'est le nuage de points.

Avec trois variables, on obtient un nuage de points en trois dimensions. On peut encore l'imaginer.

Mais avec quatre variables ou plus, il faudrait un espace à quatre dimensions. Personne ne peut le dessiner.

L'analyse en composantes principales résout ce problème. Elle ramène les données à deux dimensions, en les déformant le moins possible.

## Un exemple à 4 variables  ·  00:00:54

Prenons les cotes de neuf élèves, dans quatre cours : math, physique, anglais et néerlandais.

Chaque élève est donc décrit par quatre nombres. C'est un point dans un espace à quatre dimensions.

Première idée : ne garder que deux cours sur les quatre. Mais lesquels choisir ?

Regarde les colonnes. Les cotes de math et de physique se ressemblent beaucoup.

Les cotes d'anglais et de néerlandais aussi. Un élève a un niveau proche dans les branches scientifiques, et proche dans les langues.

## La matrice des corrélations  ·  00:01:28

Pour le voir précisément, on range toutes les corrélations dans un tableau. Un peu comme le tableau des distances entre villes, sur une carte routière.

Les variables sont notées X 1, X 2, jusqu'à X n. Ici, n vaut 4.

Dans la matrice des corrélations, la case en ligne i et en colonne j contient le coefficient de corrélation r entre X i et X j. C'est le r du chapitre 3.

Cette matrice est forcément symétrique : la corrélation de X i avec X j est la même que celle de X j avec X i.

Et sa diagonale ne contient que des 1 : une variable est parfaitement corrélée avec elle-même.

## Lire la matrice des corrélations  ·  00:02:13

Voici la matrice des corrélations pour nos neuf élèves.

Math et physique : 0,98. C'est presque une corrélation parfaite.

Anglais et néerlandais : 0,95. Très forte aussi.

Par contre, math et anglais : seulement 0,23. Le lien est faible.

On voit donc deux groupes de cours : les sciences d'un côté, les langues de l'autre.

À retenir : garder math et physique n'aurait aucun sens. Ces deux cours disent presque la même chose.

## Combiner au lieu de supprimer  ·  00:02:48

Pour passer à deux dimensions, on pourrait garder un cours scientifique et un cours de langue. Par exemple math et anglais.

On peut faire mieux : créer deux nouvelles variables qui résument les quatre.

S est la moyenne de math et de physique : un demi de math, plus un demi de physique.

L est la moyenne d'anglais et de néerlandais : un demi d'anglais, plus un demi de néerlandais.

Exemple avec l'élève 3. Il a 6 en math et 7 en physique, donc S vaut 6,5.

Il a 11 en anglais et 9,5 en néerlandais, donc L vaut 10,25.

Une telle somme de variables multipliées par des nombres s'appelle une combinaison linéaire.

## Le graphique S–L  ·  00:03:38

Chaque élève n'a plus que deux nombres, S et L. On peut enfin le dessiner dans un plan.

Voici les neuf élèves. Chaque point est un élève.

En haut à droite, l'élève 4 : 14,5 en sciences et 15,25 en langues. Il est bon partout.

En bas à gauche, l'élève 1 : 6 et 5. Il est faible partout.

En haut à gauche, l'élève 7 : 6,25 en sciences mais 12,75 en langues. Il est plus à l'aise en langues.

À retenir : réduire le nombre de variables, ce n'est pas en supprimer. On les remplace par des combinaisons linéaires qui gardent l'image représentative.

## L'idée de l'ACP  ·  00:04:26

Revenons au principe. Imagine un nuage de points en trois dimensions, et tu veux le photographier.

Tu vas chercher l'angle de vue où les points sont le plus étalés. C'est là que tu les distingues le mieux.

Exemple : les sept étoiles de la Grande Ourse. Vues de la Terre, elles dessinent une sorte de casserole.

Vues depuis une autre galaxie, ces mêmes étoiles auraient sans doute une forme complètement différente.

L'ACP fait exactement ça : elle cherche l'angle de vue qui étale le plus les données.

## Projeter sur une droite  ·  00:04:59

Pour comprendre, prenons un cas plus simple : passer de deux dimensions à une seule.

Voici six points, de A à F, dans un plan. Je leur ai donné des coordonnées simples, comme A égale 1, 1, ou B égale 0, 8.

Projeter un point sur l'axe X, c'est le faire descendre verticalement jusqu'à l'axe. On garde seulement son x.

Sur l'axe X, l'ordre des points devient : B, A, C, D, E, F. B et A sont collés, alors qu'ils sont très loin dans le plan.

Projetons maintenant sur l'axe Y. On garde seulement le y de chaque point.

L'ordre change complètement : A, D, E, C, B, F. Chaque axe déforme l'image à sa façon.

## Le meilleur axe  ·  00:05:56

Et si on projetait sur une droite inclinée ? Voici celle qui passe au milieu du nuage, dans le sens où il s'allonge.

On projette chaque point perpendiculairement sur cette droite.

L'ordre obtenu est A, B, C, D, E, F. C'est l'ordre qui semble le plus naturel quand on regarde le plan.

Cette droite a une propriété importante : parmi toutes les inclinaisons possibles, c'est celle où les points projetés sont le plus dispersés.

À retenir : le meilleur axe de projection est celui de dispersion maximale.

## Étaler au max = coller au plus près  ·  00:06:34

Il y a une autre façon de voir ce meilleur axe. Mesurons l'écart de chaque point à la droite, perpendiculairement.

Pour chaque droite qui passe par le centre du nuage, on calcule deux sommes. L'étalement des projections, et la somme des écarts au carré.

Avec la droite horizontale : étalement 70, écarts 40. Avec la verticale : étalement 40, écarts 70.

Avec le meilleur axe : étalement 80, écarts seulement 30. C'est le minimum.

Remarque : la somme fait toujours 110. C'est Pythagore : chaque point se décompose en projection plus écart.

Donc étaler les projections au maximum, c'est la même chose que rendre la somme des écarts au carré minimale.

Attention : cet axe est proche de la droite de régression du chapitre 3, mais pas identique. La régression mesure les écarts verticaux, l'ACP les écarts perpendiculaires.

## Le nouvel axe mélange X et Y  ·  00:07:38

Sur le meilleur axe, la position d'un point n'est plus x, ni y. C'est un mélange des deux.

On place d'abord l'origine au centre du nuage : la moyenne, 4 pour x et 6 pour y. Puis la position vaut deux fois x plus y, le tout divisé par racine de 5.

Pour A : x moins 4 donne moins 3, y moins 6 donne moins 5. Deux fois moins 3, plus moins 5 : moins 11.

On fait pareil pour les autres points. On obtient moins 6, moins 3, moins 1, 8 et 13.

Ces valeurs sont bien rangées dans l'ordre A, B, C, D, E, F.

À retenir : le nouvel axe est une combinaison linéaire de X et de Y. L'ACP sert à choisir au mieux ces axes.

## La matrice des variances-covariances  ·  00:08:34

Comment l'ACP trouve-t-elle ces axes ? Elle part d'un tableau : la matrice des variances-covariances.

Pour n variables X 1 à X n, la case en ligne i et en colonne j contient la covariance de X i et X j, notée sigma de X i, X j.

C'est la covariance s x y du chapitre 3 : la moyenne des produits des écarts à la moyenne.

Sur la diagonale, i égale j : la covariance d'une variable avec elle-même, c'est sa variance.

Comme la matrice des corrélations, elle est symétrique.

## Exemple : les points A à F  ·  00:09:12

Calculons-la pour nos six points. Deux variables, donc une matrice deux sur deux.

Variance de X : la somme des x moins 4, au carré, vaut 70. Divisée par 6, ça donne 11,67.

Variance de Y : la somme des y moins 6, au carré, vaut 40. Divisée par 6 : 6,67.

Covariance de X et Y : la somme des produits des écarts vaut 20. Divisée par 6 : 3,33.

On range tout ça : les variances sur la diagonale, la covariance dans les deux autres cases.

## Valeurs et vecteurs propres  ·  00:09:55

Ensuite, on cherche les valeurs propres et les vecteurs propres de cette matrice.

Petit rappel d'algèbre : u est un vecteur propre de M si M fois u donne le même vecteur u, multiplié par un nombre lambda.

Ce nombre lambda est la valeur propre associée à u.

Les vecteurs propres donnent les nouveaux axes sur lesquels on va représenter les données.

Et voici la propriété clé : une valeur propre est égale à la variance des données projetées sur l'axe de son vecteur propre.

Donc la plus grande valeur propre donne l'axe où les données sont le plus dispersées.

## Exemple : vérifions sur A à F  ·  00:10:36

Testons le vecteur u 1 égale 2, 1 : c'est la direction de notre meilleur axe.

M fois u 1 : 11,67 fois 2 plus 3,33 donne 26,67. Et 3,33 fois 2 plus 6,67 donne 13,33.

Or 26,67 et 13,33, c'est exactement 13,33 fois 2, et 13,33 fois 1. Donc lambda 1 vaut 13,33.

Vérifions la propriété. Les positions sur l'axe étaient moins 11, moins 6, moins 3, moins 1, 8 et 13, divisées par racine de 5.

Leurs carrés font 400. Divisé par 5, puis par 6 points : 13,33. C'est bien la variance des projections.

L'autre vecteur propre, moins 1, 2, donne lambda 2 égale 5. Et 13,33 plus 5 donne 18,33 : la somme des deux variances.

## Combien d'information garde-t-on ?  ·  00:11:49

La variance totale, c'est la somme des variances : 18,33. C'est toute l'information du nuage.

Si on projette sur l'axe X, on garde sa variance : 11,67, soit 64 pour cent.

Sur l'axe Y : 6,67, soit 36 pour cent seulement.

Sur l'axe du premier vecteur propre : 13,33, soit 73 pour cent. C'est le meilleur score possible pour une seule droite.

À retenir : la part d'information gardée par un axe, c'est sa valeur propre divisée par la somme des valeurs propres.

## Passer en 2 dimensions  ·  00:12:29

Pour représenter les données dans un plan, on prend comme base les deux vecteurs propres des deux plus grandes valeurs propres.

Ce plan est celui où les données sont dispersées au maximum.

Revenons aux neuf élèves. Leur matrice des variances-covariances est une matrice quatre sur quatre. Elle a donc quatre valeurs propres.

Les voici : 28,71, puis 12,08, puis 0,04 et 0,01.

Les deux premières gardent 70,3 plus 29,6 pour cent : 99,9 pour cent de l'information.

À retenir : le plan des deux premiers vecteurs propres montre presque tout, en deux dimensions seulement.

## Que représentent ces 2 axes ?  ·  00:13:19

Regardons les deux vecteurs propres. Chacun donne une combinaison linéaire des quatre cotes.

Le premier donne presque le même poids, environ 0,5, aux quatre cours. Il mesure le niveau général de l'élève.

Le second donne des poids négatifs aux sciences et positifs aux langues. Il oppose les langues aux sciences.

On retrouve l'intuition du début avec S et L. Mais cette fois, c'est le calcul qui a choisi les meilleurs axes.

## Récap du chapitre 4  ·  00:13:50

Récapitulons.

Au-delà de trois variables, on ne peut plus dessiner les données. La matrice des corrélations montre déjà quelles variables se ressemblent.

Réduire le nombre de variables, c'est les remplacer par des combinaisons linéaires, pas les supprimer.

L'ACP cherche les axes où les projections sont le plus dispersées. Ça revient à rendre minimale la somme des écarts au carré.

On part de la matrice des variances-covariances. Ses vecteurs propres donnent les axes, et chaque valeur propre est la variance sur son axe.

Pour un plan, on garde les deux vecteurs propres des deux plus grandes valeurs propres.

