# Script de la voix off — 5ANA1D chapitre 5 partie 2

## Introduction  ·  00:00:00

Analyse de données, chapitre 5, deuxième partie.

On voit ce qui change quand on sait déjà quelque chose : les probabilités conditionnelles, les probabilités totales, et le théorème de Bayes.

## Quand on sait déjà quelque chose  ·  00:00:14

En général, les événements d'une même expérience s'influencent. On dit qu'ils sont dépendants.

Imagine : tu jettes un dé sous un gobelet. Un ami jette un œil et te dit seulement : c'est pair.

Prenons A : le point est 6, et B : le point est pair. Sans information, P de A vaut 1 sur 6.

Mais si on sait que B est réalisé, il ne reste que trois résultats possibles : 2, 4 et 6.

Le 6 est un cas sur trois. La probabilité de A sachant B vaut donc 1 sur 3.

On la note P de A barre oblique B, et on lit : probabilité de A sachant B.

## La formule de P(A / B)  ·  00:01:00

Voici la formule : P de A sachant B égale P de A inter B, divisé par P de B.

L'idée : on ne garde comme cas possibles que ceux où B est réalisé. Et au numérateur, ceux où A est aussi réalisé.

Autrement dit : les cas favorables à A et B, divisés par les cas favorables à B.

Vérifions avec le dé. A inter B, c'est 6 et pair : seulement le 6, donc 1 sur 6. Et P de B vaut 1 sur 2.

1 sur 6, divisé par 1 sur 2, ça fait bien 1 sur 3. On retrouve le résultat.

## Le théorème de multiplication  ·  00:01:42

Si on retourne la formule précédente, on obtient la probabilité de A inter B, c'est-à-dire A et B.

P de A inter B égale P de A, fois P de B sachant A.

Comme tu l'as noté, on peut aussi partir de B : P de B, fois P de A sachant B. Les deux écritures sont justes.

Exemple avec le dé : P de, pair et 6, égale P de pair, fois P de 6 sachant pair.

Ça fait 1 sur 2, fois 1 sur 3, donc 1 sur 6. C'est logique : pair et 6, c'est simplement le 6.

## Événements indépendants  ·  00:02:24

Deux événements sont indépendants quand la réalisation de l'un n'influence pas la probabilité de l'autre.

En formule : P de A sachant B égale P de A. Savoir que B est réalisé ne change rien.

Dans ce cas, le théorème de multiplication se simplifie : P de A inter B égale P de A fois P de B.

Exemple : on lance une pièce et un dé. Les deux n'ont aucun lien.

P de, pile et 6, égale 1 sur 2 fois 1 sur 6, soit 1 sur 12.

## L'urne : tirage sans remise  ·  00:03:02

Exemple du cours : une urne contient 5 boules blanches et 5 boules noires. On tire deux boules. Quelle est la probabilité de tirer deux blanches ?

On applique le théorème de multiplication : P de, première blanche, fois P de, deuxième blanche sachant que la première était blanche.

Au premier tirage, 5 blanches sur 10 boules : 5 sur 10.

On ne remet pas la boule. Il reste 9 boules, dont 4 blanches. Le deuxième tirage dépend donc du premier : 4 sur 9.

Résultat : 5 sur 10 fois 4 sur 9, ça fait 2 sur 9, environ 0,222.

## L'urne : tirage avec remise  ·  00:03:48

Même expérience, mais avec remise : on remet la première boule dans l'urne avant le deuxième tirage.

Cette fois, l'urne est identique au deuxième tirage. Les deux tirages sont indépendants.

On multiplie simplement : 5 sur 10, fois 5 sur 10, ça fait 1 sur 4, soit 0,25.

Compare : sans remise, 0,222. Avec remise, 0,25. Retirer une blanche diminue un peu les chances d'en retirer une.

À retenir : sans remise, les tirages sont dépendants. Avec remise, ils sont indépendants.

## Avec trois événements  ·  00:04:31

Le théorème se généralise à trois événements. P de A inter B inter C égale P de A, fois P de B sachant A, fois P de C sachant A inter B.

Chaque facteur tient compte de tout ce qui s'est passé avant.

Si les trois événements sont indépendants, on multiplie simplement les trois probabilités.

Exemple avec notre urne : trois blanches de suite, sans remise. 5 sur 10, puis 4 sur 9, puis 3 sur 8. Ça fait 1 sur 12.

Avec remise, les tirages sont indépendants : un demi, trois fois, soit 1 sur 8.

## Le bus arrive-t-il à l'heure ?  ·  00:05:13

Passons aux probabilités totales, avec l'exemple du bus. Sa ponctualité dépend du jour.

Le week-end, le trafic est calme : il est à l'heure avec une probabilité de 0,9. Le lundi et le vendredi, il y a beaucoup de trafic : 0,6. Les autres jours, 0,8.

Question : quelle est la probabilité que le bus soit à l'heure, un jour quelconque ?

On découpe selon les jours : week-end, lundi ou vendredi, et mardi, mercredi ou jeudi. Ces cas sont incompatibles, donc on additionne.

Chaque terme est un ET : on utilise la multiplication. Par exemple, 2 jours sur 7 fois 0,9 pour le week-end.

Au total : 2 sur 7 fois 0,9, plus 2 sur 7 fois 0,6, plus 3 sur 7 fois 0,8. On obtient environ 0,771 : 77 % de chances.

## L'arbre de probabilités  ·  00:06:22

Cette situation se dessine très bien en arbre. Au premier niveau, les jours, avec leurs probabilités.

Au deuxième niveau, à l'heure ou en retard, avec les probabilités conditionnelles. Par exemple, sachant week-end, 0,9 et 0,1.

Règle 1 : les branches qui partent d'un même sommet sont incompatibles, et couvrent tous les cas. Leur somme vaut donc 1.

Règle 2 : la probabilité d'un chemin, c'est le produit des probabilités de ses branches.

Règle 3 : pour un événement, on additionne tous les chemins qui y mènent. Les trois chemins à l'heure donnent 0,771.

Remarque : c'est une moyenne pondérée des probabilités, par la fréquence des jours.

## Système exhaustif d'événements  ·  00:07:13

Pour énoncer la formule générale, il faut un système exhaustif d'événements : on découpe oméga en morceaux disjoints.

Un ensemble d'événements E 1 à E n est un système exhaustif si trois conditions sont vraies.

Un : aucun événement n'est impossible. Chaque P de E i est strictement positif.

Deux : ils sont incompatibles deux à deux. Aucun chevauchement.

Trois : leur union recouvre tout oméga. Aucun trou.

Comme les pièces d'un puzzle : elles ne se chevauchent pas, et ensemble elles forment l'image complète.

## Exhaustif ou pas ?  ·  00:07:54

Testons avec un jeu de 52 cartes. Cœurs, carreaux, et cartes noires : c'est un système exhaustif. Pas de chevauchement, et toutes les cartes sont couvertes.

Cœurs et cartes noires : ce n'est pas exhaustif. Il manque les carreaux : il y a un trou.

Images, rouges, et noires : pas exhaustif non plus. Un roi de cœur est à la fois une image et une carte rouge : il y a un chevauchement.

Avec un dé, pairs et impairs forment un système exhaustif. Et en général, un événement et son contraire en forment toujours un.

Dernier point : les branches qui partent d'un même sommet d'un arbre forment toujours un système exhaustif.

## Le théorème des probabilités totales  ·  00:08:40

Soit un système exhaustif E 1 à E n, et un événement A de la même expérience.

Alors P de A égale la somme, pour i allant de 1 à n, de P de E i fois P de A sachant E i.

P de E i, c'est la probabilité de chaque cas. P de A sachant E i, la probabilité de A dans ce cas.

L'idée : A se découpe en morceaux, A inter E 1, A inter E 2, et ainsi de suite. Ces morceaux sont disjoints, donc on additionne leurs probabilités.

Et chaque morceau se calcule avec le théorème de multiplication. Pour le bus : E 1 le week-end, E 2 lundi ou vendredi, E 3 les trois autres jours.

## Le théorème de Bayes  ·  00:09:31

Jusqu'ici, on partait du cas, le jour, pour calculer la conséquence, le bus à l'heure.

Le théorème de Bayes inverse le point de vue. Sachant que A s'est produit, quelle est la probabilité qu'il se soit produit dans le cas E k ?

Pense à un détective : il voit la conséquence, et il remonte à la cause la plus probable.

La formule : P de E k sachant A égale P de E k fois P de A sachant E k, divisé par P de A.

Le numérateur vient du théorème de multiplication. Et le dénominateur, P de A, se calcule avec les probabilités totales.

## Exemple : c'était le week-end ?  ·  00:10:13

Reprenons le bus. On sait que le bus est arrivé à l'heure. Quelle est la probabilité que ce soit un jour de week-end ?

Au numérateur : P de week-end, fois P d'être à l'heure sachant week-end. 2 sur 7 fois 0,9, soit environ 0,257.

Au dénominateur : P d'être à l'heure, qu'on a déjà calculée : environ 0,771.

0,257 divisé par 0,771, ça fait exactement 1 sur 3.

Il y a donc une chance sur trois que ce soit le week-end. Sans cette information, on aurait dit 2 sur 7, soit environ 0,29.

## L'arbre inverse  ·  00:11:00

En calculant toutes les probabilités de ce type, on construit l'arbre inverse.

Au premier niveau, la conséquence : à l'heure, avec 0,771, ou en retard, avec 0,229.

Sachant que le bus est à l'heure : week-end 1 sur 3, lundi ou vendredi 2 sur 9, et les trois autres jours 4 sur 9.

Sachant qu'il est en retard : week-end 1 sur 8, lundi ou vendredi 1 sur 2, et les trois autres jours 3 sur 8.

Logique : quand le bus est en retard, il y a une chance sur deux que ce soit un lundi ou un vendredi, les jours de gros trafic.

## Récap de la partie 2  ·  00:11:45

Récapitulons. La probabilité de A sachant B, c'est P de A inter B, divisé par P de B.

Le théorème de multiplication donne le ET : P de A, fois P de B sachant A.

Si A et B sont indépendants, on multiplie simplement : P de A fois P de B. Sans remise, dépendants ; avec remise, indépendants.

Avec un système exhaustif, les probabilités totales : la somme des P de E i, fois P de A sachant E i. En arbre : on multiplie le long des chemins, et on additionne les chemins.

Et Bayes remonte de la conséquence à la cause. Voilà, tu as toutes les bases du calcul des probabilités.

