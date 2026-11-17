# Script de la voix off — 5ANA1D chapitre 7 partie 1

## Introduction  ·  00:00:00

Analyse de données, chapitre 7, première partie : la distribution normale.

On y découvre la courbe en cloche, la normale réduite, et comment lire sa table.

## Une forme qui revient partout  ·  00:00:12

Pèse mille œufs d'un même élevage, et dessine l'histogramme de leurs poids.

Tu obtiendras presque toujours la même forme : une cloche, haute au milieu et basse sur les bords.

Cette forme a un nom : la distribution normale, aussi appelée distribution de Gauss, du nom du mathématicien Carl Friedrich Gauss.

On la retrouve partout : la taille des individus, le poids des œufs, la température, le quotient intellectuel, la durée de vie.

C'est la loi continue la plus utilisée. Et elle sera au centre des chapitres sur les échantillons et l'estimation.

## La fonction de densité  ·  00:00:51

La courbe en cloche est le graphique d'une fonction de densité de probabilité. La voici.

Elle n'a que deux paramètres. D'abord mu : l'espérance, c'est-à-dire la moyenne.

Ensuite sigma : l'écart-type.

Le reste, ce sont des constantes : pi, et e, la base de l'exponentielle.

Si X suit cette loi, on écrit : X suit une normale de paramètres mu et sigma.

Le cours ne démontre pas que mu et sigma sont bien la moyenne et l'écart-type : les intégrales sont trop ardues. On l'admet.

## Les œufs d'un élevage  ·  00:01:29

Prenons un exemple inventé. Le poids des œufs d'un élevage suit une normale de moyenne 60 grammes et d'écart-type 5 grammes.

On note : X suit N de 60 et 5.

Calculons la hauteur de la courbe au sommet, en x égale 60. Le terme x moins mu vaut 0, donc l'exponentielle vaut e exposant 0, c'est-à-dire 1.

Il reste 1 divisé par 5 fois racine de 2 pi. Ça fait environ 0,0798.

Attention : ce n'est pas une probabilité. C'est une hauteur de courbe, une densité. Les probabilités, ce seront des aires.

## Le profil de la courbe  ·  00:02:14

Regardons le graphique de f. C'est la fameuse courbe en cloche, aussi appelée courbe de Gauss, ou gaussienne.

Elle est symétrique par rapport à mu : elle a la même allure à gauche et à droite de la moyenne.

Son sommet est en x égale mu. C'est là que la densité est la plus grande. On peut le montrer en dérivant f.

Quand x s'éloigne beaucoup de mu, l'exponentielle tend vers 0. L'axe des x est une asymptote horizontale : la courbe s'en approche sans jamais le toucher.

Enfin, l'aire totale sous la courbe vaut 1, quels que soient mu et sigma. C'est obligatoire pour une densité. Le cours l'admet sans démonstration.

## Les points d'inflexion  ·  00:03:00

Sur le schéma, on marque deux points : P I, les points d'inflexion.

En un point d'inflexion, la courbe change de concavité. Au milieu, elle est bombée comme un dôme. Après ces points, elle se creuse et s'aplatit.

Pour la normale, ils sont à un écart-type du sommet : en mu moins sigma et en mu plus sigma. On le montre avec la dérivée seconde.

Avec nos œufs, le sommet est à 60 grammes. Les points d'inflexion sont donc à 55 et 65 grammes.

Sigma se lit donc sur le graphique : c'est la distance entre le sommet et un point d'inflexion. Plus sigma est grand, plus la cloche est large.

## Une probabilité, c'est une aire  ·  00:03:46

Rappel du chapitre 6. Pour une variable continue, la probabilité que X soit entre a et b, c'est l'aire sous la courbe entre a et b.

Cette aire est l'intégrale de f, de a à b. Elle vaut F de b moins F de a, où F est la fonction de répartition, une primitive de f.

Par exemple, la probabilité qu'un œuf pèse entre 55 et 65 grammes, c'est cette aire-ci.

Mais il y a un problème. On ne sait pas intégrer f par les techniques habituelles : la fonction e exposant moins x carré n'a pas de primitive élémentaire.

La solution : une table de valeurs. Mais elle est établie pour une seule normale particulière : la normale réduite.

## La normale réduite  ·  00:04:35

La normale réduite, c'est la normale de moyenne 0 et d'écart-type 1.

On dit qu'elle est centrée, parce que mu vaut 0. Et réduite, parce que sigma vaut 1.

Pour la distinguer d'une normale quelconque, on la note Z plutôt que X. On écrit : Z suit N de 0 et 1.

En remplaçant mu par 0 et sigma par 1, sa densité se simplifie : 1 sur racine de 2 pi, fois e exposant moins un demi x carré.

Son graphique est centré en 0. Ses points d'inflexion sont en moins 1 et 1. Et l'aire totale vaut toujours 1.

## La fonction de répartition  ·  00:05:18

La fonction de répartition F de x donne la probabilité que Z soit inférieur ou égal à x.

Sur le graphique, c'est toute l'aire à gauche de x, depuis moins l'infini.

Elle s'écrit avec une intégrale : 1 sur racine de 2 pi, fois l'intégrale de moins l'infini à x, de e exposant moins un demi t carré, d t.

Ici, t est juste la variable d'intégration. Et x, c'est la borne jusqu'où on accumule l'aire.

Cette intégrale ne se calcule pas par les méthodes classiques. Les valeurs de F sont donc obtenues par approximation, puis rangées dans une table.

## Approcher F(x)  ·  00:06:00

Comment approcher F ? Le plus simple est de remplacer l'exponentielle par un polynôme : son développement en série de Mac Laurin.

En s'arrêtant à l'ordre 6, puis en intégrant, on obtient cette formule.

Testons-la en x égale 0,5. Elle donne 0,6915. La table donne aussi 0,6915 : parfait.

Mais en x égale 2, elle donne 0,9331, alors que la table donne 0,9772. C'est beaucoup trop loin.

C'est pourquoi le cours précise que cette formule n'est satisfaisante que pour x entre moins 1 et 1. En pratique, on utilisera la table.

## Lire la table  ·  00:06:48

La table du cours donne F de x, arrondie à 4 décimales, pour x positif, de 0 à 3, par pas de 0,01. Voici un extrait.

On découpe x en deux morceaux. L'unité et le premier chiffre après la virgule donnent la ligne.

Le deuxième chiffre après la virgule donne la colonne.

Exemple : F de 1,25. On prend la ligne 1,2, puis la colonne 0,05.

À l'intersection, on lit 0,8944. La probabilité que Z soit inférieur ou égal à 1,25 vaut donc 0,8944.

Au-delà de 3, F vaut presque 1 : 0,9987 en 3, et 1 en 4, à 4 décimales près.

## Et pour x négatif ?  ·  00:07:46

La table ne donne que des x positifs. Comment trouver F de moins 1 ?

F de moins 1, c'est l'aire à gauche de moins 1 : la queue de gauche.

Comme la courbe est symétrique par rapport à 0, cette queue est égale à la queue de droite, l'aire à droite de 1.

Or l'aire à droite de 1, c'est l'aire totale, qui vaut 1, moins l'aire à gauche de 1. C'est donc 1 moins F de 1.

D'où la formule : F de moins x égale 1 moins F de x. Le cours l'écrit dans l'autre sens : F de x égale 1 moins F de moins x. C'est la même chose.

Ici, F de 1 vaut 0,8413. Donc F de moins 1 vaut 1 moins 0,8413, soit 0,1587.

## F(−1,25)  ·  00:08:42

Entraînons-nous avec F de moins 1,25.

On applique la formule : F de moins 1,25 égale 1 moins F de 1,25.

On a lu F de 1,25 dans la table : 0,8944.

Donc F de moins 1,25 vaut 0,1056. Un peu plus de 10 % de l'aire se trouve à gauche de moins 1,25.

Petit réflexe de vérification : pour x négatif, F de x est toujours plus petit que 0,5, car on est à gauche du centre.

## À retenir  ·  00:09:25

Récapitulons. Une normale, X suit N de mu et sigma, c'est une courbe en cloche, symétrique, avec son sommet en mu.

Ses points d'inflexion sont en mu moins sigma et mu plus sigma, et l'aire totale sous la courbe vaut 1.

Une probabilité est une aire. Mais f n'a pas de primitive élémentaire : on passe par une table.

Cette table est celle de la normale réduite, Z suit N de 0 et 1. Elle donne F de x, l'aire à gauche de x.

Pour x négatif, F de moins x égale 1 moins F de x. Dans la partie 2, on verra comment utiliser cette table pour n'importe quelle normale.

