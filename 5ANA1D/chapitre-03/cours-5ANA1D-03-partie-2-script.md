# Script de la voix off — 5ANA1D chapitre 3 partie 2

## Introduction  ·  00:00:00

Analyse de données, chapitre 3, deuxième partie.

On passe aux données continues, rangées dans un tableau à deux dimensions. Puis on voit quand deux variables sont indépendantes.

## Des données continues  ·  00:00:11

Dans la première partie, chaque étudiant donnait un couple de cotes bien précis.

Avec des données continues, comme la taille en centimètres et le poids en kilos, presque toutes les valeurs sont différentes.

On regroupe donc chaque variable en classes, comme au chapitre 1.

Puis on range les individus dans une grille, un peu comme au jeu de la bataille navale : une ligne pour la classe de taille, une colonne pour la classe de poids.

## Le tableau à deux dimensions  ·  00:00:36

Voici l'exemple du cours : la taille X, en lignes, et le poids Y, en colonnes.

Chaque case contient une fréquence, notée f i j : la proportion d'individus qui sont dans la classe i de X, et dans la classe j de Y.

Par exemple, cette case vaut 0,17. Donc 17 % des individus mesurent entre 170 et 180 centimètres, et pèsent entre 75 et 85 kilos.

Pour que la distribution soit correcte, la somme de toutes les cases doit valoir 1.

## Les fréquences marginales  ·  00:01:09

Ce tableau contient aussi la distribution de chaque variable prise seule.

En additionnant une ligne, on obtient f i point : la fréquence de la classe i de X, tous poids confondus.

Pour la ligne 140 à 160 : 0,05 plus 0,10 plus 0,05 plus 0, ça fait 0,20. Donc 20 % des individus mesurent entre 140 et 160 centimètres.

En additionnant une colonne, on obtient f point j : la fréquence de la classe j de Y.

Pour la colonne 50 à 65 kilos : 0,05 plus 0,05 plus 0 plus 0, ça fait 0,10.

On les appelle fréquences marginales, parce qu'elles sont écrites dans la marge. Le point remplace l'indice sur lequel on a additionné.

## Moyennes et variances par classes  ·  00:02:00

Pour calculer les paramètres, chaque classe est représentée par son centre. Pour 140 à 160 centimètres, le centre vaut 150. Pour 50 à 65 kilos, il vaut 57,5.

La moyenne de X, c'est la somme des f i point fois x i, où x i est le centre de la classe i.

Tu l'avais noté : on peut aussi écrire une double somme avec les f i j. C'est pareil, car additionner une ligne redonne f i point.

Calculons : 150 fois 0,2, plus 165 fois 0,3, plus 175 fois 0,33, plus 190 fois 0,17. On obtient 169,55 centimètres.

De la même façon, avec les centres des colonnes, la moyenne de Y vaut 76,125 kilos.

La variance suit la formule pratique du chapitre 2 : la somme des f i point fois x i carré, moins x barre carré.

On trouve un écart-type de 12,789 centimètres pour X, et de 9,698 kilos pour Y.

## Covariance et corrélation par classes  ·  00:03:06

Pour la covariance, il faut parcourir toutes les cases du tableau. On utilise donc une double somme.

La formule pratique : la somme, sur toutes les lignes i et toutes les colonnes j, de f i j fois x i fois y j. Moins x barre fois y barre.

Concrètement : pour chaque case, on multiplie sa fréquence par le centre de sa ligne et par le centre de sa colonne. Puis on additionne les seize résultats.

Par exemple, la case 0,17 donne 0,17 fois 175 fois 80, soit 2380.

Le total vaut 12952,25. On retire 169,55 fois 76,125, et la covariance vaut 45,256.

Le coefficient de corrélation garde la même formule : 45,256 divisé par 12,789 fois 9,698. On trouve r égale 0,365.

Le lien entre taille et poids est positif, mais plutôt faible. Et la droite de régression se calcule avec les mêmes formules qu'en partie 1.

## Deux variables indépendantes  ·  00:04:18

Deux variables sont indépendantes quand l'une n'a aucune influence sur l'autre. Par exemple, la cote d'une interro de maths, et la taille de l'élève.

Dans chaque tranche de taille, on retrouverait alors la même proportion de réussites et d'échecs.

Dans le tableau, ça se traduit par une propriété simple : chaque f i j est égal au produit des fréquences marginales, f i point fois f point j.

Testons sur notre tableau. Première case : f 1 point vaut 0,20, et f point 1 vaut 0,10. Leur produit vaut 0,02.

Mais la case contient 0,05, pas 0,02. Une seule case suffit : la taille et le poids ne sont pas indépendants.

## Indépendance ⇒ $r = 0$  ·  00:05:02

Si X et Y sont indépendants, leur covariance est nulle. Voyons pourquoi.

Dans la double somme, on remplace f i j par f i point fois f point j.

La double somme se sépare alors en deux sommes simples : une qui ne parle que de X, une qui ne parle que de Y.

La première vaut x barre. La deuxième vaut y barre. Il reste x barre y barre, moins x barre y barre : zéro.

Donc deux variables indépendantes ont toujours une covariance nulle, et un coefficient de corrélation nul.

## Attention : la réciproque est fausse  ·  00:05:35

Attention, la réciproque est fausse. Au début de ce paragraphe, le cours dit que deux variables sont indépendantes lorsque r est nul. C'est inexact.

Contre-exemple : x vaut moins 1, 0 et 1, et y égale x au carré. Donc y vaut 1, 0 et 1.

La moyenne de x vaut 0. La moyenne des produits x i y i vaut moins 1 plus 0 plus 1, sur 3 : zéro aussi.

La covariance vaut donc 0 moins 0 fois deux tiers, c'est-à-dire 0. Et r vaut 0.

Pourtant, y dépend complètement de x ! Le coefficient r ne détecte que les liens en ligne droite.

À retenir : l'indépendance entraîne r égale 0. Mais r égale 0 n'entraîne pas l'indépendance.

## Récap de la partie 2  ·  00:06:22

Récapitulons.

Pour des données continues, on construit un tableau à deux dimensions. Chaque case contient une fréquence f i j, et le total vaut 1.

Les totaux des lignes et des colonnes sont les fréquences marginales : f i point pour X, f point j pour Y.

Les paramètres utilisent les centres des classes. La covariance devient une double somme. r et la droite de régression gardent les mêmes formules.

Enfin, si X et Y sont indépendants, chaque f i j vaut f i point fois f point j, et r vaut 0. Mais un r nul ne prouve pas l'indépendance.

