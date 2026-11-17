# Script de la voix off — 5ANA1D chapitre 6 partie 2

## Introduction  ·  00:00:00

Analyse de données, chapitre 6, deuxième partie : les variables aléatoires continues.

On y voit les classes, la densité de probabilité, la fonction de répartition, et enfin la fonction de densité avec ses intégrales.

## Mesurer au lieu de compter  ·  00:00:16

Dans la partie 1, X prenait des valeurs qu'on pouvait compter : moins 2, 0, 3.

Maintenant, X sera une mesure : une taille, un poids, un temps d'attente.

Question piège : quelle est la probabilité qu'une personne mesure exactement 175 centimètres, avec une infinité de zéros après la virgule ?

La réponse est 0. Avec une variable continue, on ne parle plus de probabilité en un point, mais de probabilité sur un intervalle.

## Une variable aléatoire continue  ·  00:00:51

Une variable aléatoire continue peut prendre n'importe quelle valeur réelle dans un intervalle. Cet intervalle n'est pas forcément borné.

C'est l'équivalent des données quantitatives continues en statistique descriptive.

Le cours donne trois exemples. On choisit une personne au hasard et on note son poids.

On lance une pierre dans une direction donnée, et on mesure la distance parcourue.

On va à un arrêt de bus, et on note le temps d'attente. On retrouvera ce bus à la fin de la vidéo.

## Une distribution par classes  ·  00:01:24

Comme en statistique descriptive, on donne les probabilités pour des classes, c'est-à-dire des intervalles de valeurs.

p i est la probabilité que X soit entre x i moins 1 compris et x i non compris.

Exemple du cours : la taille d'une personne choisie au hasard dans une grande population. Les probabilités viennent par exemple d'observations statistiques.

Entre 150 et 170 centimètres : 0,3. Entre 170 et 180 : 0,45. Entre 180 et 200 : 0,25.

La somme fait bien 1.

## Le principe d'uniformité  ·  00:02:08

Le tableau dit que la probabilité d'être entre 150 et 170 vaut 0,3. Mais il ne dit pas comment elle se répartit dans la classe.

Y a-t-il plus de monde entre 150 et 160, ou entre 160 et 170 ? On ne le sait pas.

On suppose donc que la probabilité est uniforme dans la classe : elle est étalée de façon égale.

Chaque moitié reçoit donc 0,15.

Imagine 30 centilitres de sirop versés dans un bac plat de 20 centimètres de large : il s'étale à la même hauteur partout.

## La densité de probabilité  ·  00:02:46

Cette idée mène à la densité de probabilité, notée d p i.

C'est la probabilité p i de la classe, divisée par la largeur de la classe, notée l i.

Elle donne la probabilité par intervalle d'une unité, ici par centimètre.

Première classe : 0,3 divisé par 20 centimètres, ça fait 0,015.

Deuxième classe : 0,45 divisé par 10, ça fait 0,045. Troisième classe : 0,25 divisé par 20, ça fait 0,0125.

Donc la probabilité qu'une personne mesure entre 150 et 151 centimètres vaut 0,015. Et c'est pareil pour chaque tranche d'un centimètre de cette classe.

## L'histogramme des densités  ·  00:03:42

On dessine la distribution avec un histogramme : la hauteur de chaque rectangle est la densité d p i.

Regarde l'aire d'un rectangle : hauteur fois largeur, donc d p i fois l i. Et ça redonne p i.

Pour la classe du milieu : 0,045 fois 10, ça fait bien 0,45.

Comme la somme des p i vaut 1, l'aire totale de l'histogramme vaut 1.

Et la probabilité d'un intervalle, c'est l'aire des rectangles, ou des morceaux de rectangles, au-dessus de cet intervalle.

## La fonction de répartition  ·  00:04:21

La fonction de répartition garde la même définition : F de x est la probabilité que X soit inférieure ou égale à x, pour n'importe quel réel x.

Son graphe n'est plus un escalier, mais une ligne continue faite de segments.

À la borne droite d'une classe, F vaut la somme des probabilités des classes à gauche : 0,3 en 170, 0,75 en 180, et 1 en 200.

Dans chaque classe, la probabilité s'accumule régulièrement, grâce à l'uniformité. D'où les segments droits.

La pente d'un segment est la densité de la classe. Le segment le plus raide est celui de la classe 170 à 180, celle qui a la plus grande densité.

## L'équation d'un segment  ·  00:05:10

Pour un x dans la classe x i moins 1, x i, le segment a pour équation : y égale d p i fois x moins x i moins 1, plus F de x i moins 1.

Ce y, c'est F de x. On part de la valeur cumulée au début de la classe, et on ajoute la densité fois la distance parcourue dans la classe.

Calculons F de 175. Le début de la classe est 170, où F vaut 0,3. On ajoute 0,045 fois 5 centimètres, soit 0,225.

F de 175 vaut donc 0,525.

Même chose pour F de 190 : on part de 0,75 en 180, et on ajoute 0,0125 fois 10, soit 0,125. F de 190 vaut 0,875.

## La probabilité d'un intervalle  ·  00:06:12

Voici la propriété la plus utile : la probabilité que X soit entre a et b vaut F de b moins F de a.

F de b compte tout ce qui est à gauche de b. On retire F de a, tout ce qui est à gauche de a. Il reste ce qui est entre les deux.

Avec a égal 175 et b égal 190 : 0,875 moins 0,525. La probabilité d'avoir une taille entre 175 et 190 centimètres vaut 0,35.

Vérifions avec les aires de l'histogramme : 0,045 fois 5, plus 0,0125 fois 10. Ça fait 0,225 plus 0,125, donc 0,35. Les deux méthodes donnent le même résultat.

Dernière propriété : la probabilité en un point est toujours nulle. P de X égale a vaut 0. Avec une largeur nulle, l'aire est nulle.

## Espérance avec des classes  ·  00:07:22

Pour calculer l'espérance d'une distribution par classes, on remplace chaque classe par son centre, noté c i.

Le centre, c'est la moyenne des deux bornes : x i moins 1 plus x i, divisé par 2.

Ici, les centres valent 160, 175 et 190.

La formule est celle du cas discret, avec c i à la place de x i : la somme des p i fois c i.

0,3 fois 160 donne 48. 0,45 fois 175 donne 78,75. 0,25 fois 190 donne 47,5.

Au total, l'espérance vaut 174,25 centimètres : c'est la taille moyenne.

## Variance avec des classes  ·  00:08:14

Pour la variance, même idée : on prend la formule du cas discret avec les centres. Sigma au carré égale la somme des p i fois c i au carré, moins mu au carré.

0,3 fois 160 au carré donne 7680. 0,45 fois 175 au carré donne 13781,25. 0,25 fois 190 au carré donne 9025.

La somme vaut 30486,25.

On retire mu au carré, 174,25 au carré, c'est-à-dire 30363,06. La variance vaut environ 123,19.

L'écart-type est la racine : environ 11,10 centimètres. Les tailles s'écartent typiquement d'une dizaine de centimètres de la moyenne.

## Des classes de plus en plus fines  ·  00:09:14

Imagine maintenant des classes de 1 centimètre. Au lieu de 3 classes, on en aurait 50, chacune avec une toute petite probabilité.

Si on réduit encore la largeur, les probabilités des classes se rapprochent de 0. Les densités, elles, se stabilisent.

À la limite, quand la largeur tend vers 0, la probabilité en un point disparaît. Seule la densité garde un sens.

On définit alors la variable par une fonction de densité de probabilité, notée f de x. Elle est positive partout.

Et l'aire totale sous sa courbe vaut 1 : l'intégrale de f, de moins l'infini à plus l'infini, égale 1.

## Des aires sous la courbe  ·  00:10:00

Comme pour l'histogramme, une probabilité est une aire. La probabilité que X soit entre a et b, c'est l'aire sous la courbe entre a et b.

Cette aire se calcule avec une intégrale : l'intégrale de f de x, de a à b.

La fonction de répartition s'écrit aussi avec une intégrale : F de x est l'intégrale de f de t, de moins l'infini jusqu'à x.

F est donc une primitive de f. On retrouve la règle : P de a inférieur ou égal à X inférieur ou égal à b, égale F de b moins F de a.

Pourquoi ça marche ? F de b, c'est l'intégrale de moins l'infini à b. On lui retire l'intégrale de moins l'infini à a. Il reste l'intégrale de a à b.

## L'attente du bus  ·  00:10:52

Un exemple inventé, avec le bus du cours. Un bus passe toutes les 10 minutes, et tu arrives à l'arrêt au hasard.

Ton attente X est entre 0 et 10 minutes, et aucune durée n'est favorisée. La densité vaut 1 sur 10 sur cet intervalle, et 0 ailleurs.

Vérifions l'aire totale : un rectangle de largeur 10 et de hauteur 1 sur 10. L'aire vaut bien 1.

Probabilité d'attendre entre 2 et 5 minutes : l'intégrale de 1 sur 10, de 2 à 5. Ça fait 3 sur 10, soit 0,3.

Avec la fonction de répartition : F de x vaut x sur 10 entre 0 et 10. F de 5 moins F de 2, c'est 0,5 moins 0,2 : encore 0,3.

## Espérance et variance continues  ·  00:11:47

Pour une variable définie par une densité, les paramètres suivent les mêmes formules, mais les signes somme deviennent des intégrales.

L'espérance est l'intégrale de x fois f de x, de moins l'infini à plus l'infini.

Compare avec le discret : x i devient x, et p i devient f de x d x.

La variance suit la même logique, avec sa formule de définition et sa formule pratique : l'intégrale de x carré fois f de x, moins mu au carré.

## L'attente moyenne du bus  ·  00:12:21

Reprenons le bus, avec f de x égale 1 sur 10 entre 0 et 10.

L'espérance est l'intégrale de x sur 10, de 0 à 10. La primitive est x carré sur 20, et ça donne 100 sur 20, donc 5 minutes.

C'est logique : en moyenne, tu attends la moitié de l'intervalle entre deux bus.

Pour la variance, on intègre x carré sur 10 : la primitive est x cube sur 30. De 0 à 10, ça donne 1000 sur 30, soit 100 sur 3.

On retire mu au carré, donc 25. La variance vaut 25 sur 3, environ 8,33.

L'écart-type vaut environ 2,89 minutes.

## À retenir  ·  00:13:10

Récapitulons. Une variable continue prend ses valeurs dans un intervalle. La probabilité en un point vaut toujours 0.

Avec des classes, on suppose l'uniformité. La densité est p i divisé par la largeur, et chaque probabilité est une aire de l'histogramme.

La fonction de répartition est faite de segments, et la probabilité d'un intervalle vaut F de b moins F de a.

Pour l'espérance et la variance par classes, on utilise les centres c i.

Avec une fonction de densité, l'aire totale vaut 1, les probabilités sont des intégrales, et les sommes deviennent des intégrales dans les formules de mu et sigma.

