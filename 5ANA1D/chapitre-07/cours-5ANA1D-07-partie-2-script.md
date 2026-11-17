# Script de la voix off — 5ANA1D chapitre 7 partie 2

## Introduction  ·  00:00:00

Analyse de données, chapitre 7, deuxième partie : calculer une probabilité pour n'importe quelle normale.

On passe de X à Z, puis on retrouve les fameuses valeurs 68 % et 95 %.

## Une seule table pour toutes les normales  ·  00:00:15

Dans la partie 1, on a appris à lire la table de la normale réduite, Z suit N de 0 et 1.

Mais nos œufs suivent N de 60 et 5. Et il existe une infinité de normales : une pour chaque couple mu, sigma.

Pas question de faire une table pour chacune ! L'idée : transformer X en Z, pour se ramener à la seule table qu'on a.

C'est comme dire : cet œuf est à deux écarts-types au-dessus de la moyenne, au lieu de dire : il pèse 70 grammes.

## Centrer et réduire  ·  00:00:49

La transformation s'écrit : Z égale X moins mu, divisé par sigma.

D'abord, on soustrait mu : c'est un changement d'origine. La moyenne vient se placer en 0, car mu moins mu égale 0.

Ensuite, on divise par sigma : c'est un changement d'unité. Un écart-type devient une unité, car sigma divisé par sigma égale 1.

Tu as vu au chapitre 2 qu'un tel changement linéaire transforme la moyenne de la même façon, alors que l'écart-type ne subit que le changement d'unité.

Résultat : Z a une moyenne 0 et un écart-type 1. Z suit la normale réduite, N de 0 et 1.

Concrètement, la valeur z dit à combien d'écarts-types de la moyenne on se trouve.

## Un simple changement d'échelle  ·  00:01:41

Visualisons. Voici la courbe de nos œufs, avec son axe en grammes.

Sous cet axe, on ajoute celui de Z. La moyenne, 60 grammes, correspond au 0 de Z.

Un écart-type, 5 grammes, correspond à une unité de Z. Donc 65 grammes correspond à 1, et 70 grammes à 2.

De l'autre côté, 55 grammes correspond à moins 1, et 50 grammes à moins 2.

La courbe ne change pas de forme. On change seulement les graduations.

## Un œuf de 67 grammes  ·  00:02:18

Quelle est la probabilité qu'un œuf pèse au plus 67 grammes ?

On centre-réduit : z égale 67 moins 60, divisé par 5.

Ça fait 7 divisé par 5, soit 1,4. Un œuf de 67 grammes est à 1,4 écart-type au-dessus de la moyenne.

Donc P de X inférieur ou égal à 67 égale P de Z inférieur ou égal à 1,4 : c'est F de 1,4.

Dans la table, ligne 1,4, colonne 0,00 : on lit 0,9192. Environ 92 % des œufs pèsent au plus 67 grammes.

## Probabilité sur un intervalle  ·  00:03:07

Pour un intervalle de a à b, on applique la même transformation aux trois membres de l'inégalité.

A inférieur ou égal à X inférieur ou égal à b devient : a moins mu sur sigma, inférieur ou égal à Z, inférieur ou égal à b moins mu sur sigma.

Ensuite, comme au chapitre 6 : c'est F de la borne de droite, moins F de la borne de gauche.

Attention : ce F, c'est toujours la fonction de répartition de la normale réduite, celle de la table.

## Entre 52 et 67 grammes  ·  00:03:42

Quelle proportion des œufs pèse entre 52 et 67 grammes ?

Borne de gauche : 52 moins 60, divisé par 5, égale moins 1,6.

Borne de droite : on l'a déjà calculée, c'est 1,4.

La probabilité vaut donc F de 1,4 moins F de moins 1,6.

F de 1,4 vaut 0,9192. Et F de moins 1,6 vaut 1 moins F de 1,6, soit 1 moins 0,9452 : 0,0548.

Résultat : 0,9192 moins 0,0548 égale 0,8644. Environ 86 % des œufs.

## Au-dessus d'un seuil  ·  00:04:38

Et la probabilité qu'un œuf pèse plus de 70 grammes ? La table donne l'aire à gauche, pas l'aire à droite.

Comme l'aire totale vaut 1, l'aire à droite égale 1 moins l'aire à gauche.

On centre-réduit : 70 moins 60, divisé par 5, égale 2.

Donc P de X supérieur à 70 égale 1 moins F de 2, soit 1 moins 0,9772.

Ça fait 0,0228 : à peine 2 % des œufs dépassent 70 grammes.

Rappel du chapitre 6 : pour une variable continue, la probabilité d'un point vaut 0. Inférieur ou strictement inférieur, c'est donc la même probabilité.

## À un écart-type de la moyenne  ·  00:05:28

Terminons par des valeurs à connaître. Quelle est la probabilité de tomber à moins d'un écart-type de la moyenne ?

On centre-réduit les bornes. Mu moins sigma, moins mu, divisé par sigma, ça donne moins 1. Et mu plus sigma, moins mu, divisé par sigma, ça donne 1.

C'est donc F de 1 moins F de moins 1.

Or F de moins 1, c'est 1 moins F de 1. On obtient F de 1, moins 1, plus F de 1 : c'est 2 F de 1 moins 1.

Avec la table : 2 fois 0,8413, moins 1, égale 0,6826.

Environ 68 % des valeurs sont à moins d'un écart-type de la moyenne, quels que soient mu et sigma.

## Deux et trois écarts-types  ·  00:06:20

Même raisonnement à deux écarts-types : la probabilité vaut 2 F de 2 moins 1.

Avec la table : 2 fois 0,9772, moins 1, égale 0,9544. Environ 95 %.

Au-delà de deux écarts-types, il ne reste que 1 moins 0,9544, soit 0,0456. C'est très faible.

À trois écarts-types : 2 fois 0,9987, moins 1, égale 0,9974. Au-delà, c'est quasi nul.

Tu reconnais la règle des 68 et 95 % du chapitre 6 : maintenant, tu sais d'où elle vient.

## Les œufs en trois zones  ·  00:07:12

Appliquons ça à nos œufs, de moyenne 60 grammes et d'écart-type 5 grammes.

À un écart-type : entre 55 et 65 grammes, on trouve environ 68 % des œufs.

À deux écarts-types : entre 50 et 70 grammes, environ 95 %.

À trois écarts-types : entre 45 et 75 grammes, presque tous : 99,7 %.

Un œuf de 80 grammes serait donc très étonnant : il est à 4 écarts-types de la moyenne.

## À retenir  ·  00:07:48

Récapitulons. Pour utiliser la table avec X qui suit N de mu et sigma, on centre-réduit : Z égale X moins mu, sur sigma.

La valeur z dit à combien d'écarts-types de la moyenne on se trouve, et Z suit N de 0 et 1.

Sur un intervalle, la probabilité vaut F de b moins mu sur sigma, moins F de a moins mu sur sigma.

Au-dessus d'un seuil, c'est 1 moins F. Et pour un z négatif, F de moins x égale 1 moins F de x.

Enfin, les valeurs typiques : 68 % à un écart-type, 95 % à deux, 99,7 % à trois.

