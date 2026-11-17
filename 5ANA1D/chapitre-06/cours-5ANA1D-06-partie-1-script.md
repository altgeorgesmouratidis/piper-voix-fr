# Script de la voix off — 5ANA1D chapitre 6 partie 1

## Introduction  ·  00:00:00

Analyse de données, chapitre 6 : les variables aléatoires.

Dans cette première partie, on étudie les variables aléatoires discrètes : leur distribution, leur fonction de répartition, leur espérance et leur écart-type.

## Mettre un nombre sur le hasard  ·  00:00:16

On te propose un jeu : tu lances un dé. Si tu fais 6, tu gagnes 3 euros. Si tu fais 2 ou 4, tu perds 2 euros. Sinon, il ne se passe rien.

Question : est-ce que tu as intérêt à jouer ?

Pour répondre, on va transformer chaque résultat du dé en un nombre : ton gain. Ce nombre, c'est une variable aléatoire.

On verra ensuite comment décrire ses valeurs avec leurs probabilités, puis comment calculer le gain moyen et la dispersion.

## Une variable aléatoire  ·  00:00:49

Une variable aléatoire associe une valeur numérique au résultat d'une expérience aléatoire.

On la note en général avec une majuscule : X.

Reprenons le jeu. L'ensemble des résultats, oméga, contient les six faces du dé.

X envoie chaque face sur ton gain : le 6 vers 3, le 2 et le 4 vers moins 2, et les faces 1, 3 et 5 vers 0.

X est donc une fonction de oméga dans l'ensemble des réels. Elle prend ici trois valeurs possibles : moins 2, 0 et 3.

## Cinq exemples du cours  ·  00:01:27

Le cours donne cinq exemples. Regarde à chaque fois les valeurs que X peut prendre.

a : on jette un dé et on note le point. X vaut 1, 2, 3, 4, 5 ou 6.

b : notre jeu de dé. X vaut moins 2, 0 ou 3.

c : on jette trois fois un dé et on compte les 6. X vaut 0, 1, 2 ou 3.

d : on lance un dé jusqu'à obtenir un 6, et on compte les lancers. X peut valoir 1, 2, 3, et ainsi de suite, sans limite.

e : on mesure la taille d'une personne prise au hasard dans la rue. X peut prendre n'importe quelle valeur entre 0 et 2 mètres 50.

## Discrète ou continue ?  ·  00:02:19

Ces exemples se rangent en deux familles.

Une variable est discrète si ses valeurs forment un ensemble fini, comme dans les exemples a, b et c.

Elle est aussi discrète si l'ensemble est infini mais dénombrable, c'est-à-dire qu'on peut numéroter les valeurs une par une. C'est l'exemple d.

Une variable est continue si ses valeurs remplissent tout un intervalle de réels. C'est l'exemple e, la taille.

Pense à un escalier et à une rampe. Sur l'escalier, tu poses le pied sur des marches précises. Sur la rampe, tu peux t'arrêter n'importe où.

Cette partie traite les variables discrètes. Les continues viennent dans la partie 2.

## La distribution de probabilité  ·  00:03:04

Pour décrire une variable aléatoire discrète, on donne sa distribution de probabilité.

C'est la liste des valeurs possibles, notées x i, avec leur probabilité, notée p i.

Par définition, p i est la probabilité que X prenne la valeur x i.

Dans le jeu : X vaut moins 2 quand on fait 2 ou 4, donc 2 faces sur 6. Ça fait 1 sur 3.

X vaut 0 pour les faces 1, 3 et 5 : 3 faces sur 6, soit 1 sur 2. Et X vaut 3 seulement pour le 6 : 1 sur 6.

Comme en statistique descriptive, on dessine cette distribution avec un diagramme en bâtonnets.

## La somme des pᵢ vaut 1  ·  00:03:51

Une propriété à retenir : la somme des probabilités de toutes les valeurs vaut toujours 1.

La lettre sigma veut dire : on additionne les p i, pour i allant de 1 à n. Et n est le nombre de valeurs possibles.

C'est logique : X prend forcément une de ses valeurs. L'événement, X prend une valeur, est certain.

Vérifions sur le jeu. 1 sur 3 plus 1 sur 2 plus 1 sur 6. En sixièmes, ça fait 2 plus 3 plus 1, donc 6 sixièmes.

On trouve bien 1. Si tu ne trouves pas 1, il y a une erreur dans ta distribution.

## La fonction de répartition  ·  00:04:33

Deuxième outil : la fonction de répartition, notée F.

F de x, c'est la probabilité que X soit inférieure ou égale à x.

Attention au signe : c'est inférieur ou égal. La valeur x elle-même est comptée.

Pour une valeur x i, F de x i est donc la somme des probabilités de toutes les valeurs inférieures ou égales à x i. On cumule.

Dans le jeu : F de moins 2 vaut 1 sur 3. C'est la seule valeur jusque-là.

F de 0 vaut 1 sur 3 plus 1 sur 2, donc 5 sur 6.

Et F de 3 vaut 5 sur 6 plus 1 sur 6, donc 1.

## Un graphe en escalier  ·  00:05:21

Le graphe de F a la forme d'un escalier. Il monte d'une marche à chaque valeur x i, et la hauteur de la marche vaut p i.

Tout à gauche, F vaut 0 : X ne peut pas être plus petite que moins 2. Tout à droite, F vaut 1.

Important : F existe pour tout réel x, pas seulement pour les valeurs de X. Par exemple, F de 1 vaut 5 sur 6.

Pourtant, la probabilité de gagner exactement 1 euro est nulle : 1 n'est pas une valeur du jeu.

F de 1, c'est la probabilité de gagner au plus 1 euro, donc 1 euro ou moins. Et ça, c'est 5 sur 6.

## Un air de déjà-vu  ·  00:06:06

Tout ça doit te rappeler la statistique descriptive. Les deux mondes se correspondent.

Les fréquences relatives f i deviennent les probabilités p i.

Les fréquences relatives cumulées, grand F i, deviennent la fonction de répartition, F de x i.

Les graphiques sont les mêmes : bâtonnets et escalier.

La vraie différence est le sens des valeurs. En statistique, elles viennent d'observations qui existent déjà.

Ici, ce sont des probabilités : des valeurs théoriques, pour une expérience dont on ne connaît pas encore le résultat.

## L'espérance mathématique  ·  00:06:45

Le parallèle continue : à la moyenne de la statistique correspond l'espérance mathématique.

L'espérance de X se note E de X, ou plus simplement mu. C'est la valeur moyenne que prend X.

Si X est le gain d'un jeu, E de X est le gain moyen par partie : ce que tu peux espérer gagner en jouant.

La formule ressemble à celle de la moyenne : on additionne chaque valeur x i multipliée par sa probabilité p i.

Chaque valeur pèse donc selon sa probabilité. Une valeur rare compte peu, une valeur fréquente compte beaucoup.

## Le jeu est-il rentable ?  ·  00:07:25

Calculons l'espérance du jeu de dé.

Moins 2 fois 1 sur 3, ça fait moins 2 sur 3. 0 fois 1 sur 2, ça fait 0. Et 3 fois 1 sur 6, ça fait 1 sur 2.

On additionne : moins 4 sixièmes plus 3 sixièmes, donc moins 1 sur 6 euro.

En moyenne, tu perds environ 0,17 euro par partie. Le jeu n'est pas rentable pour toi.

Vérifions avec 600 parties. Tu perds 2 euros environ 200 fois, et tu gagnes 3 euros environ 100 fois.

Bilan : moins 400 plus 300, donc moins 100 euros. Divisé par 600 parties, on retrouve bien moins 1 sur 6.

## Variance et écart-type  ·  00:08:14

L'espérance ne dit pas tout. Deux jeux peuvent avoir le même gain moyen, mais des gains très différents d'une partie à l'autre.

Comme en statistique, l'écart-type, noté sigma, mesure la dispersion des valeurs autour de la moyenne mu.

Sa formule donne d'abord sigma au carré : la somme des p i fois x i moins mu, au carré.

x i moins mu, c'est l'écart d'une valeur à la moyenne. On le met au carré, puis on le pondère par sa probabilité.

Sigma au carré s'appelle la variance. L'écart-type est sa racine carrée.

## La variance du jeu  ·  00:08:52

Appliquons la définition au jeu, avec mu égal à moins 1 sur 6.

Pour moins 2 : l'écart vaut moins 11 sixièmes. Au carré, 121 sur 36, multiplié par 1 sur 3.

Pour 0 : l'écart vaut 1 sixième. Au carré, 1 sur 36, multiplié par 1 sur 2.

Pour 3 : l'écart vaut 19 sixièmes. Au carré, 361 sur 36, multiplié par 1 sur 6.

On additionne les trois termes : la variance vaut 101 sur 36, environ 2,81.

Ça marche, mais il faut calculer tous les écarts, et les fractions deviennent vite pénibles.

## La formule pratique  ·  00:09:41

Le cours donne une formule de calcul plus rapide, à retenir : sigma au carré égale la somme des p i fois x i au carré, moins mu au carré.

On ne calcule plus aucun écart : on met juste chaque valeur au carré.

Pour le jeu : 1 sur 3 fois 4, plus 1 sur 2 fois 0, plus 1 sur 6 fois 9. Ça fait 17 sur 6.

On retire mu au carré, c'est-à-dire 1 sur 36. 17 sur 6, c'est 102 sur 36. Il reste 101 sur 36.

C'est exactement le résultat de la définition. Le cours le démontre, ici on l'a vérifié sur l'exemple.

L'écart-type vaut la racine de 101 sur 36 : environ 1,67 euro.

## Que veut dire σ ?  ·  00:10:33

Comment interpréter l'écart-type ? Le cours rappelle une propriété déjà vue en statistique.

Environ 68 % des valeurs de X se trouvent à au plus un écart-type de la moyenne : entre mu moins sigma et mu plus sigma.

Environ 95 % se trouvent à au plus deux écarts-types.

Et à peine 1 % des valeurs s'écartent de plus de trois écarts-types.

Exemple inventé : un examen avec une moyenne de 12 sur 20 et un écart-type de 3. Environ deux tiers des notes seraient entre 9 et 15, et 95 % entre 6 et 18.

Garde ces pourcentages comme un ordre de grandeur : selon la forme de la distribution, la vraie proportion peut s'en écarter.

## À retenir  ·  00:11:23

Récapitulons. Une variable aléatoire X associe un nombre à chaque résultat d'une expérience. Elle est discrète si on peut compter ses valeurs.

Sa distribution donne chaque valeur x i avec sa probabilité p i, et la somme des p i vaut toujours 1.

La fonction de répartition, F de x, est la probabilité que X soit inférieure ou égale à x. Son graphe est un escalier.

L'espérance, c'est la somme des p i fois x i : le gain moyen.

La variance se calcule plus vite avec la somme des p i fois x i au carré, moins mu au carré. L'écart-type est sa racine.

Dans la partie 2, on passe aux variables continues.

