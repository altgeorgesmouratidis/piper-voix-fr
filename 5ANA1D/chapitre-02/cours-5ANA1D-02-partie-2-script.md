# Script de la voix off — 5ANA1D chapitre 2 partie 2

## Introduction  ·  00:00:00

Analyse de données, chapitre 2, deuxième partie.

On mesure maintenant l'étalement des données : étendue, écart-moyen, écart-type. Puis on voit les changements d'unité, et d'autres moyennes.

## La moyenne ne suffit pas  ·  00:00:12

Une interro donne une moyenne de 11 dans un groupe, et de 15 dans un autre. Le second groupe semble meilleur.

Mais rien ne dit où est le meilleur étudiant. Il peut avoir 20 dans le premier groupe, alors que le second plafonne à 18.

Encore plus frappant : deux séries peuvent avoir la même moyenne. Ici, 9, 10, 10 et 11 ont une moyenne de 10.

Et 0, 5, 15 et 20 aussi ! Pourtant, la deuxième série est beaucoup plus étalée.

Les paramètres de dispersion mesurent cet étalement autour de la moyenne. Ils n'ont de sens que pour des données quantitatives.

## L'étendue $E_t$  ·  00:00:48

Le paramètre le plus naturel : l'étendue, notée E t. C'est la plus grande valeur moins la plus petite.

Série A : 11 moins 9, égale 2. Série B : 20 moins 0, égale 20. On voit tout de suite que B est plus étalée.

En continu, on prend la borne supérieure de la dernière classe, moins la borne inférieure de la première. Pour les poids : 100 moins 50, égale 50 kilos.

Mais l'étendue est assez pauvre. Elle ne regarde que les deux valeurs extrêmes. Une seule valeur aberrante suffit à la gonfler.

Les paramètres suivants, eux, utilisent toutes les observations.

## L'écart-moyen $E_m$  ·  00:01:26

Intuition : des amis attendent le bus. En moyenne, à quelle distance de l'arrêt se trouvent-ils ? C'est l'idée de l'écart-moyen.

L'écart-moyen, E m, c'est la moyenne des écarts entre chaque observation et la moyenne. Un sur n, fois la somme des valeurs absolues de x i moins x barre.

La valeur absolue est indispensable : sans elle, les écarts positifs et négatifs s'annuleraient.

Exemple : 4, 6, 8, 10, 12. La moyenne vaut 8. Les écarts, en valeur absolue : 4, 2, 0, 2 et 4.

Leur somme vaut 12. On divise par 5 : l'écart-moyen vaut 2,4. En moyenne, une valeur est à 2,4 de la moyenne.

## Variance $s^2$ et écart-type $s$  ·  00:02:12

Les statisticiens préfèrent l'écart-type, noté s. On définit d'abord son carré, la variance, s carré.

s carré, c'est un sur n, fois la somme des x i moins x barre, au carré. Au lieu de la valeur absolue, on élève les écarts au carré.

C'est la moyenne des écarts quadratiques. Et l'écart-type, c'est la racine carrée de la variance.

Même série : les écarts sont moins 4, moins 2, 0, 2 et 4. Au carré : 16, 4, 0, 4 et 16. Total : 40.

La variance vaut 40 sur 5, donc 8. L'écart-type vaut racine de 8, environ 2,83.

Compare avec l'écart-moyen, 2,4 : même ordre de grandeur, et s est un peu plus grand. C'est toujours le cas.

## Pourquoi préférer l'écart-type ?  ·  00:03:02

Pourquoi cette préférence ? D'abord, la formule est plus maniable. Les valeurs absolues de l'écart-moyen sont peu pratiques en calcul.

Ensuite, l'écart-type joue un rôle central dans la suite du cours : les probabilités et les distributions.

Attention aux unités. La variance est en unités au carré : des kilos carrés, par exemple.

L'écart-type, grâce à la racine, revient dans l'unité des données. C'est lui qu'on interprète.

## La formule de calcul pratique  ·  00:03:30

Pour calculer s carré, on retiendra une deuxième formule, équivalente mais plus rapide.

s carré égale un sur n, fois la somme des x i au carré, moins x barre au carré. La moyenne des carrés, moins le carré de la moyenne.

Plus besoin de calculer chaque écart. On élève directement les valeurs au carré.

Même série : 16, 36, 64, 100 et 144. La somme vaut 360. Divisée par 5 : 72.

On retire x barre au carré : 8 au carré, 64. 72 moins 64, égale 8. On retrouve bien la même variance.

Le cours démontre l'égalité en développant le carré. Ici, on l'a vérifiée sur un exemple.

## Écart-type de données en classes  ·  00:04:15

Comme pour la moyenne, la formule s'adapte. Avec un tableau, on pondère par f i. En continu, on remplace x i par le centre de classe c i.

Formule pratique en continu : s carré égale la somme des f i fois c i au carré, moins x barre au carré.

Reprenons les poids. Pour la deuxième classe : 0,35 fois 70 au carré, ça donne 1715. Sur les quatre classes, le total vaut 5425.

La moyenne vaut 72,75. Au carré, environ 5292,56.

s carré égale 5425 moins 5292,56, environ 132,44. L'écart-type vaut environ 11,51 kilos.

## La règle 68 – 95 – 99  ·  00:05:04

Avec la moyenne et l'écart-type, on peut estimer où se trouvent les observations.

Exemple : ton trajet dure en moyenne 30 minutes, avec un écart-type de 5 minutes.

Entre x barre moins s et x barre plus s, donc entre 25 et 35 minutes : environ 68 pour cent des trajets.

Entre x barre moins 2 s et x barre plus 2 s, donc entre 20 et 40 minutes : environ 95 pour cent.

Et à 3 écarts-types, entre 15 et 45 minutes : environ 99 pour cent.

Attention : ce sont des approximations. Elles supposent une distribution à peu près symétrique, et beaucoup d'observations. On y reviendra avec la loi normale.

## Changement d'origine et d'unité  ·  00:05:47

Un changement d'origine ajoute la même quantité b à chaque observation. Par exemple, le patron augmente tous les salaires de 50 euros.

Ou le prof retire 1 point sur chaque copie. Chaque x i devient x i plus b.

Un changement d'unité multiplie chaque observation par un même nombre a, non nul. Par exemple, une augmentation de 5 pour cent : on multiplie par 1,05.

Ou une interro sur 30 ramenée sur 20 : on multiplie par 2 tiers. Chaque x i devient a fois x i.

Les deux ensemble, c'est une transformation linéaire : u i égale a fois x i, plus b. Question : faut-il tout recalculer ? Non !

## Ce que deviennent les paramètres  ·  00:06:30

Intuition : déplace tout un nuage de points vers la droite. Son centre bouge, mais son étalement ne change pas. Par contre, si tu l'étires, l'étalement change.

Les paramètres de position subissent tout, comme les observations. Le mode, la médiane et la moyenne deviennent a fois l'ancien paramètre, plus b.

Les paramètres de dispersion subissent le changement d'unité, mais pas le changement d'origine. Le plus b disparaît.

Attention, le cours écrit s u égale a fois s x. C'est une erreur : c'est vrai seulement si a est positif.

Un écart-type est toujours positif. La formule exacte est donc : s u égale valeur absolue de a, fois s x. Pareil pour l'étendue et l'écart-moyen.

## Exemple : une interro ramenée sur 20  ·  00:07:14

Une interro est notée sur 30. La moyenne vaut 18, l'écart-type 6.

Le prof la ramène sur 20 : il multiplie chaque note par 2 tiers. La moyenne devient 2 tiers de 18, donc 12. L'écart-type, 2 tiers de 6, donc 4.

Puis il ajoute 1 point de bonus à tout le monde. C'est un changement d'origine, avec b égale 1.

La moyenne monte à 13. Mais l'écart-type reste 4 : les notes sont décalées, pas plus étalées.

## La moyenne pondérée  ·  00:07:45

Quand on parle de moyenne sans préciser, c'est la moyenne arithmétique. Mais il en existe d'autres. D'abord, la moyenne pondérée.

Chaque observation x i reçoit un poids P i, qui indique son importance. Tu connais ça : ta note finale à l'ESI.

Dans l'exemple du cours, les maths et la logique ont une pondération de 8, la statistique de 2. Les deux premiers cours pèsent 4 fois plus.

On multiplie chaque valeur par son poids, et on divise par la somme des poids.

Avec 12 en maths, 14 en logique et 17 en stat : 8 fois 12, plus 8 fois 14, plus 2 fois 17, ça fait 242. Divisé par 18 : environ 13,44.

C'est la même formule que la moyenne avec les n i, ou que la réunion de groupes. En physique, elle donne le centre de gravité.

## La moyenne géométrique $\bar{x}_G$  ·  00:08:35

En finance, on utilise la moyenne géométrique pour trouver le taux moyen d'un placement.

C'est la racine n-ième du produit des n valeurs. La somme est remplacée par un produit, et la division par n par une racine n-ième.

Exemple : ton épargne gagne 10 pour cent la première année, puis 30 pour cent la deuxième. On multiplie donc par 1,10, puis par 1,30.

Au total, le capital est multiplié par 1,43. La moyenne géométrique vaut racine de 1,43, environ 1,1958. Soit un taux moyen d'environ 19,58 pour cent.

Piège : la moyenne arithmétique donnerait 20 pour cent. Mais 1,20 au carré, ça fait 1,44, pas 1,43.

Enfin, le log de la moyenne géométrique, c'est la moyenne des log des valeurs.

## La moyenne harmonique $\bar{x}_H$  ·  00:09:30

La moyenne harmonique sert en physique. Par exemple, pour la vitesse moyenne sur plusieurs trajets de même distance.

C'est l'inverse de la moyenne arithmétique des inverses. Un sur x barre H, égale un sur n, fois la somme des un sur x i.

Exemple : tu fais 120 kilomètres à l'aller à 60 kilomètres par heure, et le retour à 40 kilomètres par heure.

L'aller prend 2 heures, le retour 3 heures. Au total, 240 kilomètres en 5 heures : 48 kilomètres par heure.

C'est exactement la moyenne harmonique de 60 et 40. Et pas 50, car tu passes plus de temps à rouler lentement.

## Le coefficient de variation $C_v$  ·  00:10:09

Dernier paramètre, surligné dans ton cours : le coefficient de variation, C v.

C'est un paramètre hybride : il combine un paramètre de position et un de dispersion. C v égale s divisé par x barre.

Il mesure la dispersion par rapport à l'ordre de grandeur des valeurs. Il sert à comparer des groupes sur des échelles différentes.

Exemple : l'action A vaut en moyenne 200 euros, avec un écart-type de 10. Son C v vaut 10 sur 200, donc 0,05.

L'action B vaut 20 euros en moyenne, avec un écart-type de 4. Son C v vaut 4 sur 20, donc 0,20.

B a le plus petit écart-type, mais elle est 4 fois plus volatile par rapport à son prix.

## Le tableau récapitulatif  ·  00:10:54

Le cours termine par un grand tableau. Retiens la logique, pas chaque case.

Données brutes : on divise la somme par n.

Tableau recensé : on pondère chaque x i par sa fréquence f i.

Données en classes : on garde les f i, et on remplace x i par le centre c i.

C'est vrai pour la moyenne, l'écart-moyen et la variance. Et avec les n i, on remplace simplement f i par n i sur n.

## Récap de la partie 2  ·  00:11:22

Récapitulons. L'étendue est simple, mais elle ne regarde que les extrêmes.

L'écart-moyen est la moyenne des écarts en valeur absolue. La variance est la moyenne des écarts au carré, et l'écart-type sa racine.

Pour calculer, on utilise la formule pratique : la moyenne des carrés, moins le carré de la moyenne.

Environ 68, 95 et 99 pour cent des valeurs sont à 1, 2 ou 3 écarts-types de la moyenne.

Si u i égale a x i plus b : la position subit tout, la dispersion seulement valeur absolue de a.

Enfin : pondérée pour des importances, géométrique pour des taux, harmonique pour des vitesses, et C v pour comparer des échelles.

