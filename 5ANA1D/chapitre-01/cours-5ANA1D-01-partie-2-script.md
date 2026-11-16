# Script de la voix off — 5ANA1D chapitre 1 partie 2

## Introduction  ·  00:00:00

Analyse de données, chapitre 1, deuxième partie.

On passe aux observations continues : classes, histogrammes, polygone et fonction de répartition. Puis on termine par le qualitatif.

## Pourquoi regrouper en classes ?  ·  00:00:12

Imagine que tu pèses 80 étudiants avec une balance précise au dixième de gramme.

Il y a peu de chances que deux mesures soient identiques. Un tableau recensé aurait 80 lignes.

Et sa colonne des n i ne contiendrait que des 1. Ça ne nous apprend rien.

La solution : grouper les données en classes. Ce sont des intervalles contigus, collés les uns aux autres, qui couvrent toutes les observations.

## Le tableau par classes  ·  00:00:38

Voici le tableau des poids, groupés en quatre classes.

n i, c'est maintenant le nombre d'observations dans la classe. Par exemple, 28 étudiants pèsent entre 65 et 75 kilos.

f i, c'est ce nombre en pourcentage de l'effectif. 28 sur 80, ça fait 0,35.

Grand N i, c'est le nombre d'observations inférieures à x i, le bord droit de la classe. 48 étudiants pèsent moins de 75 kilos.

Et grand F i, c'est ce même nombre en pourcentage : 48 sur 80, donc 0,60.

## Comment choisir les classes ?  ·  00:01:13

Le choix des classes est arbitraire. Il dépend du bon sens du statisticien.

Pas trop peu de classes, sinon on n'apprend rien. Pas trop, sinon c'est indigeste.

La règle de Sturge donne un ordre de grandeur : 1 plus dix tiers fois le logarithme en base 10 de n.

Pour 80 étudiants, ça donne environ 7 classes. C'est une indication, pas une obligation : le cours en prend 4.

Les classes peuvent avoir des largeurs différentes. Et elles sont fermées à gauche, ouvertes à droite : 65 kilos pile tombe dans une seule classe.

## Hypothèse d'uniformité  ·  00:01:48

Grouper en classes fait perdre de l'information. Des étudiants de 68, 72 et 74 kilos tombent tous dans la classe 65 à 75.

On ne sait plus où ils sont exactement dans la classe. Alors on fait une hypothèse.

On suppose que les observations sont réparties uniformément dans chaque classe.

Autrement dit, il y a le même nombre d'étudiants par tranche d'un kilo. Ici, 28 étudiants sur 10 kilos, donc 2,8 par kilo.

Cette hypothèse est la clé de toute la suite : densité, polygone et fonction de répartition.

## Le piège des rectangles  ·  00:02:23

Premier réflexe pour dessiner le tableau : des rectangles posés sur chaque classe, de hauteur n i.

Problème : ton œil ne compare pas les hauteurs. Il compare les surfaces. Et l'aire d'un rectangle, c'est n i fois la largeur l i.

Les classes 1 et 3 ont le même effectif, 20. Mais la première est plus large : 300 contre 200. Elle paraît 50 pour cent plus importante.

Pire : les deux dernières classes ont des aires proches, 200 et 180. Pourtant la dernière ne compte que 12 étudiants, contre 20.

C'est un défaut visuel majeur. Il faut des rectangles dont l'aire, et pas la hauteur, représente l'effectif.

## Densité de fréquence absolue $dn_i$  ·  00:03:03

La solution : prendre comme hauteur la densité de fréquence absolue, d n i. C'est n i divisé par l i, la largeur de la classe.

d n i, c'est le nombre moyen d'observations par unité. Ici, par kilo. Pour la classe 65 à 75 : 28 divisé par 10, donc 2,8 étudiants par kilo.

Pour la première classe : 20 divisé par 15, environ 1,3. C'est une valeur arrondie.

Et maintenant, l'aire de chaque rectangle vaut d n i fois l i, donc exactement n i. L'aire totale vaut l'effectif, 80.

Ce graphique s'appelle l'histogramme des densités de fréquence absolue.

## Densité de fréquence relative $df_i$  ·  00:03:44

Même idée avec les fréquences relatives. La densité de fréquence relative, d f i, c'est f i divisé par l i.

C'est le pourcentage moyen d'observations par unité. Pour la classe 65 à 75 : 0,35 divisé par 10, donc 0,035.

Pour la première classe : 0,25 divisé par 15, environ 0,017. Encore une valeur arrondie.

Cette fois, l'aire de chaque rectangle vaut f i, et l'aire totale vaut 1.

L'histogramme a exactement la même forme que le précédent. Seule l'échelle verticale change.

## Le polygone des fréquences cumulées  ·  00:04:24

On passe à un point très important. En discret, on dessinait un escalier. En continu, on dessine un polygone.

Prends une classe, de x i moins 1 à x i. Grand F i, c'est le pourcentage d'observations inférieures à x i.

Donc le point de hauteur grand F i se place en fin de classe, au-dessus de x i.

En début de classe, au-dessus de x i moins 1, la hauteur est grand F i moins 1 : le pourcentage des observations avant la classe.

Entre les deux, on trace un segment oblique. Pourquoi ? Grâce à l'hypothèse d'uniformité.

Les observations sont réparties régulièrement dans la classe. Donc le pourcentage cumulé augmente à vitesse constante, de façon linéaire.

## L'équation d'un segment  ·  00:05:08

Autre point très important : l'équation de ce segment.

Sa pente, c'est la montée divisée par l'avancée. La montée, c'est grand F i moins grand F i moins 1, donc f i. L'avancée, c'est la largeur l i.

La pente vaut donc f i sur l i. C'est exactement la densité d f i !

L'équation se lit : y égale d f i, fois x moins x i moins 1, plus grand F i moins 1.

On part de la hauteur de début de classe, et on monte de d f i par unité parcourue.

Pour la classe 65 à 75 : y égale 0,035 fois x moins 65, plus 0,25. En 75, on retrouve bien 0,60.

## $F(x)$ par morceaux  ·  00:05:53

En mettant les segments bout à bout, on obtient le polygone des fréquences cumulées. C'est le graphe de la fonction de répartition F de x.

On écrit F de x par morceaux, une ligne par classe. Avant 50, F vaut 0. Après 100, F vaut 1.

Les pentes sont les densités arrondies : 0,017, 0,035, 0,025, et 0,01.

La définition reste : le pourcentage des observations inférieures, ou égales, à x.

En continu, strictement inférieur ou inférieur ou égal, c'est pareil. La fréquence d'une valeur ponctuelle est toujours 0.

## À quoi sert $F(x)$ ?  ·  00:06:36

Avec F, tu trouves le pourcentage d'observations dans n'importe quel intervalle. Il y a trois cas.

Inférieures à x : F de x.

Supérieures à x : le complément, 1 moins F de x.

Entre x 1 et x 2 : F de x 2 moins F de x 1.

Pour un effectif, multiplie le pourcentage par n. Et dans l'autre sens, on peut chercher le x qui correspond à un pourcentage donné.

## Exemple : moins de 73 kilos  ·  00:07:04

Quel pourcentage d'étudiants pèse moins de 73 kilos ? 73 est dans la classe 65 à 75, donc on prend la troisième ligne de F.

F de 73 égale 0,035 fois 73 moins 65, plus 0,25. 0,035 fois 8, ça fait 0,28. Plus 0,25 : 0,53. Donc 53 pour cent.

Plus de 73 kilos ? Le complément : 1 moins 0,53, donc 47 pour cent.

Et combien d'étudiants pèsent moins de 73 kilos ? 80 fois 0,53, ça fait 42,4. Donc environ 42 étudiants.

## Exemple : un intervalle et la lecture inverse  ·  00:07:48

Entre 73 et 81 kilos ? On soustrait : F de 81 moins F de 73.

81 est dans la classe 75 à 85. F de 81 égale 0,025 fois 6, plus 0,6, donc 0,75. Moins 0,53, ça fait 0,22. Soit 22 pour cent.

Maintenant, à l'envers. Quel poids sépare les 30 pour cent d'étudiants les plus légers ? On cherche x tel que F de x égale 0,3.

Sur le graphique, 0,3 est entre 0,25 et 0,60. La solution est donc dans la deuxième classe.

On résout : 0,035 fois x moins 65, plus 0,25, égale 0,3. On trouve x environ égal à 66,4 kilos.

## Observations qualitatives  ·  00:08:43

Dernier cas : les observations qualitatives. On définit n i et f i exactement comme en discret.

Par contre, pas de fréquences cumulées. Les valeurs ne sont pas des nombres : les ordonner sur un axe n'a pas de sens mathématique.

On choisit quand même un ordre de présentation. Parfois, le contexte l'impose : des avis vont du plus positif au moins positif.

Sinon, on classe par fréquences décroissantes, comme les voitures les plus vendues. Ou par ordre alphabétique, pour éviter un classement arbitraire.

## Le diagramme en fromage  ·  00:09:15

Pour le qualitatif, on utilise souvent un diagramme en tarte, ou en fromage.

Chaque part a une surface proportionnelle à sa fréquence. Avec nos avis, 80 réponses au total.

Satisfait : 42 sur 80, donc 52,5 pour cent. C'est plus de la moitié du disque.

Pour l'angle d'une part, on multiplie la fréquence par 360 degrés. 0,525 fois 360, ça donne 189 degrés.

## Récap de la partie 2  ·  00:09:45

Récapitulons. En continu, on groupe en classes et on suppose les observations uniformes dans chaque classe.

L'histogramme se dessine avec les densités d n i ou d f i, pour que l'aire représente l'effectif.

Le polygone relie les points x i, grand F i. Chaque segment a pour pente d f i.

F de x donne les pourcentages : F de x, 1 moins F de x, ou une différence. Et on peut la lire à l'envers.

Enfin, en qualitatif, on garde n i et f i, sans cumul, et on dessine un fromage.

