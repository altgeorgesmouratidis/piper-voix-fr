# Script de la voix off — 5ANA1D chapitre 5 partie 1

## Introduction  ·  00:00:00

Analyse de données, chapitre 5 : introduction au calcul des probabilités.

Dans cette première partie, on apprend le vocabulaire, deux façons de calculer une probabilité, et les opérations sur les événements.

## Chiffrer le hasard  ·  00:00:15

Calculer une probabilité, c'est chiffrer la chance qu'un événement soumis au hasard se réalise.

Tout a commencé avec les jeux de hasard : les joueurs voulaient estimer leurs chances de gagner.

L'exemple type, c'est le pile ou face. Tout le monde sait qu'on a une chance sur deux d'obtenir pile.

Mais le hasard est partout : un tirage au sort, croiser quelqu'un dans la rue, la météo du week-end prochain.

Un dicton résume bien l'enjeu : la loterie est une taxe sur ceux qui ne comprennent rien aux probabilités.

## Expérience aléatoire et Ω  ·  00:00:48

Une expérience aléatoire, c'est un processus dont on ne peut pas connaître le résultat à l'avance.

Pour être complète, elle décrit une action, et ce qu'on note comme résultat.

Par exemple, jeter un dé et noter le point. Les résultats possibles sont 1, 2, 3, 4, 5 et 6.

Avec la même action, on peut noter autre chose : la parité du point. Les résultats deviennent pair ou impair. C'est une autre expérience.

L'ensemble de tous les résultats possibles s'appelle l'ensemble des possibilités. On le note oméga.

Il peut être discret, comme pour le dé, continu, comme la longueur d'un saut entre 0 et 10 mètres, ou qualitatif, comme pile ou face.

## Événement aléatoire  ·  00:01:39

Un événement aléatoire, c'est une des issues possibles de l'expérience.

Techniquement, c'est un sous-ensemble de oméga : on y met tous les résultats pour lesquels l'événement est réalisé.

Exemple avec le dé : l'événement, le point est au moins 5, correspond au sous-ensemble 5, 6.

Et l'événement, le point est pair, correspond au sous-ensemble 2, 4, 6.

On note les événements avec des lettres majuscules : A, B, C.

## La probabilité P(A)  ·  00:02:13

La probabilité d'un événement A se note P de A. C'est un nombre réel entre 0 et 1, bornes comprises.

Plus elle est proche de 1, plus l'événement a de chances de se réaliser. Plus elle est proche de 0, moins il en a.

Deux cas extrêmes. Une probabilité nulle : l'événement est impossible. Une probabilité de 1 : il est certain.

Avec la pièce : P de pile vaut 1 sur 2, et P de face aussi.

P de, la pièce tombe sur pile ou sur face, vaut 1 : c'est certain. P de, la pièce ne retombe pas, vaut 0 : c'est impossible.

Une probabilité, c'est donc une fonction qui associe à chaque événement un nombre entre 0 et 1.

## Événements équiprobables  ·  00:03:05

Deux événements sont équiprobables s'ils ont la même probabilité de se réaliser.

Avec une pièce bien équilibrée, pile et face sont équiprobables : 1 sur 2 chacun.

Avec un dé normal, chaque point a la même probabilité : 1 sur 6.

Mais avec un dé pipé, le 6 sort plus souvent que les autres. Les points ne sont plus équiprobables.

Retiens bien cette notion : elle est cruciale pour la suite.

## Probabilité a priori  ·  00:03:36

Il existe deux façons de calculer une probabilité. La première, la probabilité a priori, est mathématique : on compte des cas.

C'est la formule bien connue : P de A égale le nombre de cas favorables, divisé par le nombre de cas possibles.

Un cas favorable, c'est un cas où l'événement A se réalise, parmi les cas possibles envisagés.

La pièce : 2 cas possibles, pile ou face. Un seul est favorable. P de pile vaut 1 sur 2.

Le dé, avec l'événement, au moins 5 : 6 cas possibles, et 2 favorables, le 5 et le 6. P vaut 2 sur 6, donc 1 sur 3.

## Le piège des deux dés  ·  00:04:21

Attention, voici le piège du cours. On jette deux dés, et on veut la probabilité que la somme soit au moins 10.

Oméga contient les sommes de 2 à 12 : ça fait 11 résultats. Trois sont favorables : 10, 11 et 12.

On serait tenté de répondre 3 sur 11. Mais ce résultat est faux !

Pourquoi ? Parce que ces 11 sommes ne sont pas équiprobables.

Pour faire 12, il faut que les deux dés tombent sur 6 : une seule façon.

Pour faire 7, il y a six façons : 1 plus 6, 2 plus 5, 3 plus 4, et aussi 4 plus 3, 5 plus 2, 6 plus 1.

## La bonne méthode : 36 couples  ·  00:05:07

La solution, c'est de remonter plus loin dans l'expérience, jusqu'à des cas qui sont vraiment équiprobables.

Ici, ce sont les couples dé 1, dé 2. Chaque dé a 6 valeurs, donc il y a 6 fois 6, soit 36 couples équiprobables.

Le tableau donne la somme pour chaque couple. On repère les cases qui valent 10, 11 ou 12.

Il y en a 6. La probabilité vaut donc 6 sur 36, soit 1 sur 6. C'est exactement ce que tu avais noté.

D'où la formule améliorée : le nombre de cas favorables, divisé par le nombre de cas possibles équiprobables.

Et cette formule suppose un dé parfait. Avec un dé truqué, elle ne s'applique plus.

## Probabilité a posteriori  ·  00:05:55

Mais souvent, on ne peut pas compter de cas. Quelle est la probabilité de réussir un examen, ou que ton ordinateur plante ?

La seconde méthode, la probabilité a posteriori, se base sur l'expérience. On répète l'expérience n fois.

On calcule la fréquence relative f n de A : le nombre de fois où A s'est réalisé, divisé par n.

Plus n est grand, plus cette fréquence est fiable. La probabilité, c'est la limite de f n de A, quand n tend vers l'infini.

Attention : la fréquence est expérimentale, la probabilité est théorique. On ne fait que s'en approcher.

Le chapitre 7 le justifiera avec la loi des grands nombres.

## Exemple : 20 lancers de pièce  ·  00:06:43

Exemple du cours : on lance une pièce 20 fois, et on suit la fréquence de pile après chaque lancer.

Au début, ça varie beaucoup : 1, puis 0,5, puis 0,67, puis 0,8 après cinq lancers.

Ensuite, les variations diminuent. Après 20 lancers, on a 9 piles : la fréquence vaut 9 sur 20, soit 0,45.

En continuant, la fréquence devrait se stabiliser autour de 0,5, ou d'une autre valeur si la pièce est truquée.

Remarque : aux lancers 2, 14 et 16, la fréquence vaut pile 0,5. C'est un hasard. Seul le comportement à long terme compte.

## Exemple : calculer π avec le hasard  ·  00:07:32

Deuxième exemple, plus surprenant : calculer pi grâce au hasard.

On dessine un cercle de rayon 1 dans un carré de côté 2, centré sur l'origine.

On lance des points au hasard dans le carré : x et y sont choisis au hasard entre moins 1 et 1. Certains tombent dans le cercle, d'autres non.

La probabilité de tomber dans le cercle, c'est le rapport des surfaces : la surface du cercle, divisée par celle du carré.

Comme tu l'avais écrit : pi r carré, divisé par 2 r au carré, ça donne pi sur 4.

Donc la fréquence des points dans le cercle tend vers pi sur 4. Il suffit de la multiplier par 4 pour approcher pi.

## L'algorithme ApproximationPi  ·  00:08:19

Voici l'algorithme du cours. On initialise un compteur à 0.

Pour chacun des n points, on tire x et y au hasard entre moins 1 et 1. Rnd renvoie un réel aléatoire entre 0 et 1, donc 2 fois Rnd moins 1 tombe entre moins 1 et 1.

Si x carré plus y carré est inférieur ou égal à 1, le point est dans le cercle : on augmente le compteur.

À la fin, on renvoie 4 fois le compteur, divisé par n.

J'ai exécuté cet algorithme. Avec 100 points, on obtient 3,12. Avec 100 000 points, on obtient 3,14.

Ce n'est pas la méthode la plus rapide pour calculer pi. Mais c'est étonnant : le hasard construit une suite qui converge vers une valeur exacte.

## Événements et ensembles  ·  00:09:13

Plus précisément, un événement est une proposition booléenne, comme, le dé tombe sur un point pair. Elle est vraie ou fausse selon le résultat.

Comme en logique, c'est un prédicat. Et le sous-ensemble 2, 4, 6 est sa classe de vérité.

C'est pourquoi on confond événements et ensembles. Les opérateurs logiques deviennent des opérations sur les ensembles.

ET devient l'intersection. OU devient l'union. NON devient le complémentaire, noté avec une barre au-dessus.

Et l'événement certain correspond à oméga tout entier. L'événement impossible correspond à l'ensemble vide.

## Le théorème d'addition  ·  00:09:56

Le théorème d'addition donne la probabilité de A union B, c'est-à-dire A ou B, au sens non exclusif.

P de A union B égale P de A, plus P de B, moins P de A inter B.

Pourquoi la soustraction ? Regarde le dessin. Quand on additionne A et B, la zone commune est comptée deux fois.

On la retire donc une fois. C'est tout le théorème.

## Exemple : pair OU au moins 5  ·  00:10:25

Exemple avec un dé. A : le point est pair. B : le point est au moins 5.

P de A vaut 3 sur 6, avec 2, 4 et 6. P de B vaut 2 sur 6, avec 5 et 6.

A inter B, c'est pair et au moins 5 : seulement le 6. Donc P de A inter B vaut 1 sur 6.

On applique : 3 sur 6, plus 2 sur 6, moins 1 sur 6. Ça fait 4 sur 6, donc 2 sur 3.

Vérifions en comptant directement : A union B, c'est 2, 4, 5, 6. Quatre cas sur six. C'est bien 2 sur 3.

## Événements incompatibles  ·  00:11:15

Deux événements sont incompatibles s'ils ne peuvent pas se produire en même temps.

En ensembles, leur intersection est vide. On dit aussi qu'ils sont mutuellement exclusifs, ou disjoints.

Dans ce cas, P de A inter B vaut 0. Le théorème d'addition se simplifie : P de A union B égale P de A plus P de B.

Exemple avec le dé. A : le point est 1. B : le point est au moins 5. Ils ne peuvent pas arriver ensemble.

Donc P de A union B vaut 1 sur 6, plus 2 sur 6, c'est-à-dire 3 sur 6, soit 1 sur 2.

## L'événement complémentaire  ·  00:12:01

Le complémentaire de A, c'est sa négation. On le note A barre.

Par exemple, le complémentaire de, le point est au moins 5, c'est, le point est au plus 4.

En ensembles, c'est tout ce qui est dans oméga, mais pas dans A.

Propriété : P de A barre égale 1 moins P de A.

Pourquoi ? A et A barre sont incompatibles, et leur union, c'est oméga, dont la probabilité vaut 1. Donc P de A plus P de A barre vaut 1.

## Exemples : passer par le contraire  ·  00:12:37

Premier exemple : P de, au moins 5, vaut 1 sur 3. Donc P de, au plus 4, vaut 1 moins 1 sur 3, soit 2 sur 3.

Deuxième exemple, avec nos deux dés : quelle est la probabilité que la somme soit inférieure à 10 ?

Compter les 30 cases serait long. Mais c'est le contraire de, la somme est au moins 10, qui vaut 1 sur 6.

Donc la réponse est 1 moins 1 sur 6, soit 5 sur 6.

À retenir : quand un événement est compliqué à compter, calcule son contraire.

## Récap de la partie 1  ·  00:13:17

Récapitulons. Une expérience aléatoire a un ensemble de possibilités oméga. Un événement est une partie de oméga, et sa probabilité est entre 0 et 1.

La probabilité a priori compte les cas favorables, sur les cas possibles, à condition qu'ils soient équiprobables.

La probabilité a posteriori est la limite de la fréquence relative, quand on répète l'expérience.

Le théorème d'addition donne le OU. Pour des événements incompatibles, on additionne simplement.

Et la probabilité du contraire vaut 1 moins P de A. Dans la partie 2, on verra les probabilités conditionnelles.

