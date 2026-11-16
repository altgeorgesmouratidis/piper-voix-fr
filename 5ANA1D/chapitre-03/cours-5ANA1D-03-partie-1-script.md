# Script de la voix off — 5ANA1D chapitre 3 partie 1

## Introduction  ·  00:00:00

Analyse de données, chapitre 3 : les distributions à deux dimensions.

Dans cette première partie, on étudie des couples de données discrètes : la covariance, la corrélation et la droite de régression.

## Deux mesures à la fois  ·  00:00:14

Jusqu'ici, on étudiait une seule caractéristique à la fois : le poids, ou la taille.

Dans ce chapitre, on mesure deux choses sur chaque individu. Par exemple, sa taille X et son poids Y.

La grande question : y a-t-il un lien entre les deux ? Si je connais la taille, puis-je estimer le poids ?

Pour mesurer ce lien, on va construire un nombre : le coefficient de corrélation.

Ensuite, on tracera la droite qui résume le mieux ce lien : la droite de régression.

## Couple de données et nuage de points  ·  00:00:45

Prenons dix étudiants. Pour chacun, on note sa cote de maths, x i, et sa cote de stat, y i.

Chaque couple devient un point dans un plan : la cote de maths à l'horizontale, la cote de stat à la verticale.

Par exemple, le couple 12, 14 : 12 en maths et 14 en stat. C'est ce point-ci.

L'ensemble de ces points s'appelle un nuage de points.

On voit déjà une tendance : en gros, quand la cote de maths monte, la cote de stat monte aussi.

## Moyennes et écarts-types  ·  00:01:14

Chaque variable garde ses propres paramètres, calculés comme au chapitre 2.

Les moyennes : x barre vaut 11,8 en maths, et y barre vaut 11,1 en stat. On les trace en pointillés.

Les écarts-types : s x vaut 2,75, et s y vaut 1,97. Les cotes de maths sont un peu plus dispersées.

Mais ces quatre nombres décrivent chaque variable séparément. Ils ne disent rien du lien entre les deux.

## La covariance : l'idée  ·  00:01:43

Pour mesurer le lien, on découpe le nuage avec les deux moyennes. Ça fait quatre zones.

Pour chaque point, on calcule deux écarts : x i moins x barre, et y i moins y barre. Puis on les multiplie.

En haut à droite, les deux écarts sont positifs : le produit est positif. En bas à gauche, les deux sont négatifs : le produit est encore positif.

Dans les deux autres zones, un écart est positif et l'autre négatif : le produit est négatif.

Par exemple, le point 16, 14. Ses écarts valent 4,2 et 2,9. Leur produit vaut plus 12,18.

Si la plupart des points sont dans les zones positives, X et Y montent ensemble.

## La covariance $s_{xy}$  ·  00:02:28

La covariance, notée s x y, est la moyenne de ces produits.

Un sur n, fois la somme, pour i allant de 1 à n, de x i moins x barre, fois y i moins y barre.

Pour calculer à la main, le cours donne une formule équivalente, plus rapide.

La moyenne des produits x i fois y i, moins le produit des moyennes, x barre fois y barre.

Dans notre exemple, la somme des produits x i fois y i vaut 1340. Divisée par 10, ça fait 134.

On retire 11,8 fois 11,1, soit 130,98. La covariance vaut 3,02.

Avec la définition, on trouve exactement la même valeur. Les deux formules sont bien équivalentes.

À retenir : une covariance positive signifie que X et Y ont tendance à varier dans le même sens.

## Le coefficient de corrélation $r$  ·  00:03:22

La covariance a un défaut : sa valeur dépend des unités. En centimètres ou en mètres, on n'obtient pas le même nombre.

On la divise donc par les deux écarts-types. On obtient le coefficient de corrélation r : s x y, divisé par s x fois s y.

Ce nombre est toujours compris entre moins 1 et 1.

Plus sa valeur absolue est proche de 1, plus le lien est fort. Plus elle est proche de 0, plus il est faible.

Dans notre exemple : 3,02 divisé par 2,75 fois 1,97. On trouve r égale 0,557.

C'est une corrélation positive, d'intensité moyenne : les bons en maths ont plutôt de bonnes cotes en stat, mais pas toujours.

## Lire un nuage selon $r$  ·  00:04:07

Voyons à quoi ressemble un nuage selon la valeur de r.

Quand r vaut 1, tous les points sont parfaitement alignés sur une droite qui monte.

Entre 0 et 1, les points forment un nuage allongé qui monte. Plus r est proche de 1, plus il est serré.

Quand r vaut 0, le nuage n'a aucune direction : il n'y a pas de lien linéaire.

Si r est négatif, c'est l'inverse : quand X augmente, Y diminue. Pour r égal moins 1, les points sont alignés sur une droite qui descend.

À retenir : le signe de r donne le sens du lien. Sa valeur absolue donne sa force.

## La forme du nuage  ·  00:04:44

Attention : r mesure l'alignement des points, pas la pente.

Ces trois nuages ont la même corrélation. Dans le premier, s x est plus grand que s y : le nuage est écrasé, la pente est faible.

Si s x égale s y, le nuage suit la diagonale.

Si s x est plus petit que s y, le nuage est étiré vers le haut : la pente est forte.

La forme dépend donc des écarts-types. La force du lien, elle, ne dépend que de r.

## La droite de régression  ·  00:05:14

Quand la corrélation est forte, le nuage ressemble à une droite. L'idée : trouver la droite qui passe au plus près de tous les points.

Imagine que tu poses une règle sur le nuage. Tu la fais glisser et tourner jusqu'à ce qu'elle colle au mieux aux points.

Pour chaque point, on mesure l'écart vertical entre le point et la droite. Ce sont les traits jaunes.

La droite de régression est celle qui rend la somme des carrés de ces écarts la plus petite possible.

C'est pour ça qu'on l'appelle aussi la droite des moindres carrés.

Pourquoi des carrés ? Sans eux, les écarts au-dessus et en dessous de la droite s'annuleraient.

## Calculer $a$ et $b$  ·  00:05:50

La droite a pour équation y égale a x plus b. Le cours donne directement les deux coefficients.

La pente a vaut la covariance, divisée par la variance de X : s x y sur s x au carré.

L'ordonnée à l'origine b vaut y barre, moins a fois x barre.

Dans notre exemple : a égale 3,02, divisé par 2,75 au carré. On obtient environ 0,399, donc à peu près 0,4.

Et b égale 11,1, moins 0,399 fois 11,8. On obtient environ 6,39.

La droite de régression est donc : y égale 0,4 x, plus 6,4.

## Lire et utiliser la droite  ·  00:06:36

Comment lire cette droite ?

La pente a, c'est delta y sur delta x. Ici, 0,4 : un point de plus en maths donne, en moyenne, 0,4 point de plus en stat.

Le nombre 6,4, c'est la valeur de y quand x vaut 0. C'est là que la droite coupe l'axe vertical.

Surtout, la droite sert à prédire. Un étudiant a 14 en maths : 0,4 fois 14, plus 6,4, ça donne 12.

On estime donc sa cote de stat à environ 12. C'est une estimation, pas une certitude.

## D'où viennent ces formules ? (1/2)  ·  00:07:14

Pourquoi ces formules ? Tu as annoté cette démonstration, alors on la refait pas à pas, sans se presser.

On cherche a et b qui rendent la somme S la plus petite possible. S dépend de deux variables : a et b.

Au minimum, les dérivées partielles s'annulent. Dériver par rapport à a, c'est traiter b comme une constante. Et inversement.

On utilise la règle de dérivation d'une puissance : la dérivée de u exposant n, c'est n fois u prime, fois u exposant n moins 1.

Ici, u vaut a x i plus b moins y i, et n vaut 2. Par rapport à a, u prime vaut x i. Par rapport à b, u prime vaut 1.

On obtient deux équations. La première : la somme de 2 u fois x i égale 0. La deuxième : la somme de 2 u égale 0.

## D'où viennent ces formules ? (2/2)  ·  00:08:04

Commençons par l'équation 2. On simplifie par 2 et on sépare la somme : a fois la somme des x i, plus n fois b, moins la somme des y i, égale 0.

On divise tout par n. La somme des x i divisée par n, c'est x barre. Il reste : a x barre, plus b, moins y barre, égale 0.

D'où b égale y barre moins a x barre. Voilà la deuxième formule.

On remplace ce b dans l'équation 1, puis on divise encore par n.

On reconnaît la formule pratique de la variance de X d'un côté, et celle de la covariance de l'autre.

Donc a fois s x carré égale s x y, et a égale s x y sur s x carré. C'est démontré.

## Le signe de la pente  ·  00:08:48

Dernière remarque. Dans a égale s x y sur s x carré, le dénominateur est un carré : il est toujours positif.

Donc a a toujours le même signe que la covariance. Covariance positive : la droite monte.

Covariance négative : la droite descend.

Et si la covariance est nulle, a vaut 0 : la droite est horizontale. Son équation est y égale y barre.

À retenir : la pente de la droite et la covariance ont toujours le même signe.

## Récap de la partie 1  ·  00:09:20

Récapitulons cette première partie.

Un couple de données se représente par un nuage de points.

La covariance mesure si X et Y varient ensemble. En pratique : la moyenne des produits, moins le produit des moyennes.

Le coefficient de corrélation r divise la covariance par les deux écarts-types. Il est toujours compris entre moins 1 et 1.

La droite de régression minimise la somme des carrés des écarts verticaux. Sa pente vaut s x y sur s x carré, et b vaut y barre moins a x barre.

Dans la deuxième partie, on passe aux données continues, regroupées en classes, et à l'indépendance.

