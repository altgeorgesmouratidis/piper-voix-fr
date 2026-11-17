# Script de la voix off — 5ANA1D chapitre 1 partie 1

## Introduction  ·  00:00:00

Analyse de données, chapitre 1 : la statistique descriptive.

Dans cette première partie, on pose le vocabulaire, puis on range des données discrètes.

## Des données en vrac  ·  00:00:11

Tu demandes leur âge aux étudiants d'une classe, un par un. Tu obtiens ces seize nombres.

Comme ça, en vrac, c'est indigeste. Quel est l'âge le plus courant ? Combien ont moins de vingt ans ?

La statistique descriptive sert à ça : trier, compter, puis présenter les données en tableaux et en graphiques.

On va voir le vocabulaire, les fréquences, les fréquences cumulées et la fonction de répartition.

## Population et échantillon  ·  00:00:39

Pense à un cuisinier qui goûte sa soupe. Une cuillère suffit, pas besoin de boire toute la marmite.

La marmite, c'est la population : l'ensemble des individus qu'on veut étudier.

Attention, un individu, ce n'est pas forcément une personne. Ça peut être une voiture, un oiseau ou une commune.

Souvent, on ne peut pas interroger tout le monde. On prend un échantillon assez grand pour être représentatif. C'est la cuillère.

Le nombre d'individus de l'échantillon s'appelle l'effectif. On le note n.

## Trois familles d'observations  ·  00:01:15

Les informations récoltées s'appellent des observations. Il en existe deux grandes familles.

Si ce n'est pas un nombre, l'observation est qualitative. Par exemple, la marque de ton GSM.

Si c'est un nombre, elle est quantitative. Et là, il y a encore deux cas.

Discrète : des valeurs isolées, qu'on peut compter. Le nombre d'enfants d'une famille : 0, 1, 2, 3.

Continue : toutes les valeurs réelles d'un intervalle. Le poids d'un œuf peut valoir 52,375 grammes.

## Deux pièges  ·  00:01:52

Premier piège : une observation discrète n'est pas forcément un nombre entier.

Une interro sur 20 avec des demi-points : 0, 0,5, 1, et ainsi de suite jusqu'à 20. Ça fait 41 valeurs isolées. C'est discret.

Deuxième piège : le poids d'un œuf est continu. Mais si tu l'arrondis au gramme près, il redevient discret.

On parle alors de continu discrétisé.

Dernier mot de vocabulaire. Des mesures prises chaque jour à la même heure forment une série chronologique. Des mesures prises toutes au même moment forment une série statistique.

## Effectif et valeurs observées  ·  00:02:34

Revenons aux âges. Ce sont des données brutes : non triées, telles qu'on les a récoltées.

Premier réflexe : les compter. Il y en a seize, donc l'effectif n vaut 16.

Ensuite, on relève les valeurs différentes, toujours dans l'ordre croissant. On les note x 1, x 2, jusqu'à x k.

Ici, il y a cinq âges différents, de 17 à 21. Donc k vaut 5.

x 1 vaut 17, x 2 vaut 18, et ainsi de suite jusqu'à x 5, qui vaut 21.

## Fréquence absolue $n_i$  ·  00:03:12

Pour chaque valeur x i, on compte combien de fois elle apparaît. C'est sa fréquence absolue, notée n i.

Par exemple, 19 ans apparaît 6 fois. Donc n 3 vaut 6.

On range tout dans un tableau à deux colonnes. On l'appelle le tableau des fréquences absolues, ou tableau recensé.

Propriété fondamentale : si on additionne tous les n i, on retrouve l'effectif total.

La formule se lit : la somme des n i, pour i allant de 1 à k, égale n.

Ici, 2 plus 4 plus 6 plus 2 plus 2, ça fait bien 16.

## Fréquence relative $f_i$  ·  00:03:55

Dire 6 étudiants sur 16, c'est bien. Mais pour comparer deux classes de tailles différentes, un pourcentage est plus parlant.

La fréquence relative f i, c'est la fréquence absolue divisée par l'effectif.

Au numérateur, n i : le nombre d'apparitions. Au dénominateur, n : l'effectif total.

Pour 19 ans : 6 divisé par 16, ça donne 0,375. Soit 37,5 pour cent.

Une fréquence relative est donc toujours un réel entre 0 et 1. On la retrouvera dans la partie probabilités du cours.

## La somme des $f_i$ vaut 1  ·  00:04:37

Voici le tableau avec les fréquences relatives. Le total fait cent pour cent.

Ce n'est pas un hasard. On le démontre. La somme des f i, c'est la somme des n i divisés par n.

n est le même pour toutes les valeurs. On peut donc le sortir de la somme : un sur n, fois la somme des n i.

Or la somme des n i, c'est n. Il reste n divisé par n, donc 1.

Ce tableau a un avantage : on compare facilement. Son inconvénient : on ne voit plus l'effectif, 16 étudiants.

## Diagramme en bâtonnets  ·  00:05:15

On peut dessiner ce tableau. En abscisse, les valeurs x i. En hauteur, les n i.

Le bâton de 19 ans est le plus haut : c'est l'âge le plus fréquent.

Avec les f i en hauteur, l'allure est exactement la même. Seule la graduation de l'axe vertical change.

Petite remarque. Si les valeurs sont très différentes, par exemple 90 656 contre 8, on utilise une échelle logarithmique.

## Cumuler, c'est additionner au fur et à mesure  ·  00:05:45

Imagine que tu ranges les étudiants par âge, du plus jeune au plus vieux, et que tu comptes en avançant.

Arrivé au bout des 17 ans, tu en as compté 2. Après les 18 ans, 2 plus 4, donc 6.

Après les 19 ans, 6 plus 6, donc 12. Ce compteur qui ne fait que monter, c'est la fréquence cumulée.

Elle répond directement à la question : combien d'observations sont inférieures ou égales à une valeur ?

## Fréquence absolue cumulée $N_i$  ·  00:06:16

La fréquence absolue cumulée se note N i, avec un grand N. C'est le nombre d'observations inférieures ou égales à x i.

La formule : grand N i égale la somme des petits n j, pour j allant de 1 à i. On additionne les fréquences de toutes les valeurs jusqu'à x i.

En pratique, on calcule ligne par ligne. Grand N i, c'est le précédent, plus le n i de la ligne.

La première ligne recopie n 1, ici 2. La dernière donne toujours l'effectif total, ici 16.

## Fréquence relative cumulée $F_i$  ·  00:06:54

Même idée en pourcentage. La fréquence relative cumulée, grand F i, c'est la somme des f j jusqu'à i.

Autre façon de la calculer : grand N i divisé par l'effectif n.

Pour 19 ans : 12 divisé par 16, ça donne 0,75. Donc 75 pour cent.

La première ligne recopie f 1. La dernière vaut toujours 1, c'est-à-dire cent pour cent.

## Lire le tableau complet  ·  00:07:25

Avec ce tableau complet, on répond à trois types de questions.

Combien ont 19 ans ou moins ? On lit grand N i : 12 étudiants. Ou grand F i : 75 pour cent.

Combien ont plus de 19 ans ? On prend le complément : 100 moins 75, donc 25 pour cent. Autrement dit, 20 ans ou plus.

Combien ont entre 18 et 20 ans ? On prend grand F de 20, moins grand F de 17. Attention : de 17, pas de 18 !

87,5 moins 12,5, ça fait 75 pour cent. On soustrait la valeur juste avant 18, sinon on enlève les 18 ans du compte.

## La fonction de répartition $F(x)$  ·  00:08:15

Pour représenter les fréquences relatives cumulées, on dessine un graphique en escalier.

C'est le graphe de la fonction de répartition. F de x, c'est le pourcentage des observations inférieures ou égales à x.

Tu peux déjà l'écrire comme une probabilité : F de x égale P de X inférieur ou égal à x. Tu verras ça dans la partie probabilités.

Chaque palier commence à une valeur observée et monte d'une marche. Le point plein, à gauche, appartient au palier.

Le palier est fermé à gauche et ouvert à droite. Au bout, le point est exclu : à 20 pile, on est déjà sur la marche suivante.

## $F(x)$ existe pour tout réel $x$  ·  00:08:58

Contrairement aux bâtonnets, F a une valeur pour n'importe quel x, pas seulement pour les âges observés.

F de 16 vaut 0. Personne n'a 16 ans, mais il est vrai que zéro pour cent ont 16 ans ou moins.

F de 19,5 égale F de 19, donc 0,75. Les âges sont entiers : 75 pour cent ont au plus dix-neuf ans et demi.

Et F de 25 vaut 1. Tout le monde a 25 ans ou moins. Au-delà de 21, F vaut toujours 1.

À retenir : F de x monte de 0 à 1, par marches, et ne redescend jamais.

## Récap de la partie 1  ·  00:09:42

Récapitulons. L'effectif n, c'est le nombre d'observations. n i compte les apparitions de x i, et leur somme fait n.

La fréquence relative f i, c'est n i sur n. Leur somme fait 1.

Grand N i et grand F i cumulent : ils comptent les observations inférieures ou égales à x i.

Pour un intervalle, on soustrait : grand F de la borne haute, moins grand F de la valeur juste avant la borne basse.

Et la fonction de répartition F de x est un escalier qui monte de 0 à 1. Dans la partie 2, on passe aux données continues.

