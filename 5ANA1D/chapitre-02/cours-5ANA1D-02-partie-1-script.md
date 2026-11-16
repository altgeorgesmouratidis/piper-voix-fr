# Script de la voix off — 5ANA1D chapitre 2 partie 1

## Introduction  ·  00:00:00

Analyse de données, chapitre 2 : les paramètres statistiques. Première partie.

Dans cette partie, on résume une série de données par une seule valeur : le mode, la médiane, les quartiles et la moyenne.

## Trois familles de paramètres  ·  00:00:14

Un paramètre statistique, c'est une valeur caractéristique calculée à partir d'une série d'observations.

Première famille : les paramètres de position. Ils situent les observations sur l'axe des abscisses.

Par exemple, pour comparer les résultats d'une interro dans deux groupes d'étudiants : lequel a des notes plus élevées ?

Deuxième famille : les paramètres de dispersion. Ils mesurent l'étalement des observations autour d'une valeur centrale. Ce sera la partie 2.

La troisième famille, les paramètres de forme, mesure la dissymétrie. Elle n'est pas au programme de ce cours.

## Le mode $x_M$  ·  00:00:50

Intuition : au resto universitaire, le plat du jour le plus commandé, c'est le mode des commandes.

Le mode d'une série, noté x M, c'est l'observation la plus fréquente.

En discret, ou en qualitatif, c'est la valeur qui a le plus grand n i, ou le plus grand f i.

Sur un diagramme en bâtonnets, c'est l'abscisse du plus grand bâtonnet. Ici, la valeur 50, avec 6 observations.

Le mode existe aussi en qualitatif : c'est le seul paramètre de position qui ne demande pas de nombres.

## Les limites du mode  ·  00:01:23

Attention, le mode a des limites. D'abord, il n'est pas toujours unique : deux valeurs peuvent être ex aequo.

Si toutes les valeurs apparaissent le même nombre de fois, elles sont toutes modales. On peut aussi dire qu'il n'y a pas de mode.

Surtout, le mode ne regarde qu'une seule valeur. Il peut tomber sur une valeur aberrante.

Exemple : dix copies d'examen. Trois étudiants ont rendu une feuille blanche, donc 0.

Les sept autres ont tous une note différente, entre 11 et 17. Le mode vaut donc 0 !

Pourtant, la plupart des notes sont au-dessus de 10. Le mode n'est pas un paramètre très représentatif.

## La classe modale  ·  00:02:02

En continu, les données sont groupées en classes. On parle alors de classe modale.

C'est la classe qui a la plus forte densité de fréquence, d n i ou d f i. Rappel : d f i, c'est f i divisé par la largeur de la classe.

Reprenons les poids du chapitre 1. La première classe a une densité d'environ 0,017. La deuxième : 0,35 divisé par 10, donc 0,035.

La plus forte densité est 0,035. La classe modale est donc 65 à 75 kilos.

Si toutes les classes ont la même largeur, c'est plus simple : il suffit de prendre la classe qui a la plus grande fréquence.

## La médiane $x_{1/2}$  ·  00:02:44

Intuition : range des élèves par taille. Celui qui est pile au milieu de la file, c'est la médiane.

La médiane, notée x un demi, partage les observations en deux groupes de même effectif. 50 pour cent en dessous, 50 pour cent au-dessus.

Il faut pouvoir ranger les valeurs dans l'ordre. La médiane n'existe donc pas en qualitatif.

Données brutes, n impair : on prend l'observation de rang n plus 1, sur 2. Pour 2, 3, 5, 5, 6, 7, 9, n vaut 7. On prend la quatrième : 5.

n pair : on fait la moyenne des deux valeurs centrales, de rang n sur 2 et n sur 2 plus 1.

On ajoute 10 à la série. n vaut 8, on prend les rangs 4 et 5 : 5 et 6. La médiane vaut 5,5.

## Médiane d'un tableau recensé  ·  00:03:31

Passage important, on va lentement. Les données sont dans un tableau recensé : chaque valeur x i avec son effectif n i.

La règle : on cherche le premier effectif cumulé grand N i qui est supérieur ou égal à n sur 2.

Ici, n vaut 20. Donc n sur 2 vaut 10.

On descend la colonne des N i : 2, c'est trop petit. 6, encore trop petit. 12, c'est le premier qui dépasse 10.

12 est strictement supérieur à 10. Dans ce cas, la médiane est simplement la valeur x i de cette ligne : 50.

Pourquoi ? Les observations de rang 7 à 12 valent toutes 50. La dixième et la onzième, celles du milieu, valent donc 50.

## Le cas de l'égalité  ·  00:04:16

Autre exemple du cours, avec les fréquences relatives : on cherche le premier grand F i supérieur ou égal à 0,5.

Ici : 0,10, puis 0,25, puis 0,50. On tombe pile sur 0,5.

C'est le deuxième cas. Il ne peut arriver que si n est pair.

Exactement la moitié des observations vaut 50 ou moins. L'autre moitié vaut 60 ou plus.

Il y a donc deux valeurs centrales différentes. La médiane est leur moyenne : 50 plus 60, divisé par 2, égale 55.

À retenir : supérieur strict, on prend x i. Égalité, on prend la moyenne de x i et de la valeur suivante.

## Médiane en continu  ·  00:05:00

Cas quantitatif continu. La médiane, c'est la valeur x telle que 50 pour cent des observations lui sont inférieures.

Autrement dit, on résout l'équation F de x égale 0,5, avec la fonction de répartition du chapitre 1.

Reprenons les poids des étudiants. On part de 0,5 sur l'axe vertical, on va jusqu'à la courbe, et on descend.

0,5 est entre 0,25 et 0,60. La médiane est donc dans la classe 65 à 75, où F de x vaut 0,035 fois x moins 65, plus 0,25.

On résout : 0,035 fois x moins 65 égale 0,25. Donc x moins 65 égale 0,25 divisé par 0,035, environ 7,14.

La médiane vaut environ 72,14 kilos.

## Sans équation : la règle de trois  ·  00:05:59

Tu n'as pas écrit l'équation du segment ? Pas de problème : une règle de trois suffit.

Sur le segment, les abscisses 65, x un demi et 75 sont en proportion avec les ordonnées 0,25, 0,5 et 0,60.

On avance de x moins 65 sur une largeur de 10. On monte de 0,25 sur une hauteur de 0,35.

Donc x moins 65, sur 10, égale 0,25 sur 0,35. On trouve à nouveau x environ égal à 72,14 kilos.

C'est la même chose : la règle de trois utilise simplement la pente du segment.

## Quartiles, déciles, centiles  ·  00:06:41

La médiane coupe les observations en deux. Les quartiles les coupent en quatre groupes de même effectif.

Il y en a trois. Le premier quartile, x un quart, résout F de x égale 0,25. Le deuxième, c'est la médiane. Le troisième, x trois quarts, résout F de x égale 0,75.

Pour les poids, F de 65 vaut exactement 0,25. Le premier quartile est donc 65 kilos.

Pour 0,75, on est dans la classe 75 à 85. On résout 0,025 fois x moins 75, plus 0,6, égale 0,75. On trouve 81 kilos.

Même principe pour les déciles, qui coupent en 10 groupes : il y en a 9. Et pour les centiles, qui coupent en 100 : il y en a 99.

Ces paramètres ont surtout du sens en continu, avec beaucoup d'observations.

## La moyenne $\bar{x}$  ·  00:07:38

La moyenne arithmétique, notée x barre, n'existe que pour des observations quantitatives.

Sur des données brutes : on additionne toutes les observations et on divise par n. Un sur n, fois la somme des x i, pour i allant de 1 à n.

Dans un tableau recensé, chaque valeur x i compte n i fois. On fait la somme des n i fois x i, divisée par n.

Ou, ce qui revient au même, la somme des f i fois x i. Ici, i va de 1 à k, le nombre de valeurs différentes.

Exemple avec notre tableau : 30 fois 2, plus 40 fois 4, et ainsi de suite. On obtient 1030.

On divise par 20 : la moyenne vaut 51,5. Proche de la médiane, qui valait 50.

## Moyenne de données en classes  ·  00:08:26

En continu, on ne connaît pas les valeurs exactes dans chaque classe. On les remplace par le centre de classe, c i.

Le centre, c'est la moyenne des deux bornes : x i moins 1, plus x i, divisé par 2. Pour 65 à 75, le centre vaut 70.

Grâce à l'hypothèse d'uniformité, le centre représente bien la moyenne des observations de la classe.

La formule devient : la somme des f i fois c i. C'est une moyenne des moyennes de chaque classe.

Pour les poids : 0,25 fois 57,5, plus 0,35 fois 70, plus 0,25 fois 80, plus 0,15 fois 92,5.

On obtient 72,75 kilos. Très proche de la médiane, 72,14.

## Moyenne d'une réunion de groupes  ·  00:09:16

Deux groupes passent la même interro. Groupe A : 30 étudiants, moyenne 12. Groupe B : 20 étudiants, moyenne 15.

Quelle est la moyenne de tous les étudiants ? Le piège, c'est de faire 12 plus 15, divisé par 2, donc 13,5. C'est faux.

Le groupe A est plus nombreux, il doit peser plus. On multiplie chaque moyenne par l'effectif de son groupe.

30 fois 12, plus 20 fois 15, ça fait 660. C'est la somme de toutes les notes.

On divise par l'effectif total, 50. La moyenne globale vaut 13,2.

La formule se généralise à k groupes : la somme des n i fois x barre i, divisée par la somme des n i.

## Récap de la partie 1  ·  00:10:01

Récapitulons. Le mode est la valeur la plus fréquente. En continu, c'est la classe de plus forte densité. Attention aux valeurs aberrantes.

La médiane coupe les observations en deux moitiés. Données brutes : la valeur du milieu, ou la moyenne des deux valeurs centrales.

Tableau recensé : le premier N i supérieur ou égal à n sur 2. En cas d'égalité, la moyenne de x i et de la valeur suivante.

En continu : on résout F de x égale 0,5. Et 0,25 ou 0,75 pour les quartiles.

La moyenne : la somme des f i fois x i, avec les centres de classe c i en continu. Pour réunir des groupes, on pondère par les effectifs.

Dans la partie 2 : la dispersion, et d'autres types de moyennes.

