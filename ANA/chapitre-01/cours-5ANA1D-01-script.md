# Script voix off — 5ANA1D, chapitre 1 : Statistique descriptive

## Partie 1 — Vocabulaire et données discrètes

### Scène 1 — Introduction  (`p1_00_titre`)

Analyse de données, chapitre 1 : la statistique descriptive. Dans cette première partie, on voit le vocabulaire et les données discrètes.

### Scène 2 — Introduction  (`p1_01_intro`)

Imagine Alice. Elle demande leur âge aux 16 étudiants de sa classe.

Elle obtient cette liste. En vrac, comme ça, elle ne raconte pas grand-chose.

Le but de ce chapitre : ranger ces données dans des tableaux et des graphiques qui parlent.

Au programme : le vocabulaire, les fréquences, les fréquences cumulées, et la fonction de répartition.

### Scène 3 — Vocabulaire  (`p1_02_vocab`)

Commençons par le vocabulaire. Pense à un cuisinier qui goûte sa soupe.

Il ne boit pas toute la marmite. Une cuillère suffit, si la soupe est bien mélangée.

En statistique, c'est pareil. La marmite, c'est la population : tout le groupe qu'on veut étudier.

Chaque élément de ce groupe s'appelle un individu. Ça peut être une personne, un animal ou un objet.

La cuillère, c'est l'échantillon : la partie du groupe qu'on interroge vraiment.

Le nombre d'observations récoltées s'appelle l'effectif. On le note n.

### Scène 4 — Vocabulaire  (`p1_03_types`)

Les informations récoltées s'appellent des observations. Il en existe deux grandes familles.

Si ce ne sont pas des nombres, elles sont qualitatives. Par exemple, une couleur ou une marque de téléphone.

Si ce sont des nombres, elles sont quantitatives. Et là, il y a encore deux cas.

Discrètes : les valeurs sont isolées, on peut les compter une à une. Comme le nombre d'enfants : 0, 1, 2, 3.

Continues : toutes les valeurs réelles d'un intervalle sont possibles. Comme le poids d'un œuf : 52 grammes, ou 52,375 grammes.

### Scène 5 — Vocabulaire  (`p1_04_alice`)

Classons le questionnaire d'Alice. Elle demande l'âge, la taille et le langage de programmation préféré.

L'âge, en années entières, est quantitatif discret.

La taille peut prendre n'importe quelle valeur réelle : c'est quantitatif continu.

Le langage préféré, Python ou Java, n'est pas un nombre : c'est qualitatif.

Attention au piège. Si Alice arrondit la taille au centimètre, les valeurs redeviennent isolées. On parle alors de continu discrétisé.

Dernier mot. Des mesures répétées dans le temps forment une série chronologique. Des mesures prises au même moment forment une série statistique.

À retenir : qualitatif, discret ou continu. Le type de données décide des tableaux et des graphiques à utiliser.

### Scène 6 — Fréquence absolue  (`p1_05_freq_abs`)

Revenons aux âges d'Alice. Imagine un vote à main levée : on compte combien de mains se lèvent pour chaque âge.

D'abord, on repère les valeurs différentes, rangées dans l'ordre croissant. On les note x 1, x 2, jusqu'à x k.

Ici, il y a 5 âges différents, de 17 à 21. Donc k vaut 5.

Ensuite, on compte. Le nombre de fois que la valeur x i apparaît s'appelle sa fréquence absolue. On la note n i.

On range tout dans un tableau. On l'appelle le tableau des fréquences absolues, ou tableau recensé.

Par exemple, 19 ans apparaît 6 fois. Donc n 3 vaut 6.

Si on additionne toutes les fréquences absolues, on retrouve l'effectif total.

La formule se lit : la somme des n i, pour i allant de 1 à k, égale n. Ici, 2 plus 4 plus 6 plus 2 plus 2, ça fait 16.

À retenir : n i compte combien de fois la valeur x i apparaît. Et la somme des n i donne toujours l'effectif n.

### Scène 7 — Fréquence relative  (`p1_06_freq_rel`)

6 étudiants ont 19 ans. Mais 6 sur combien ? C'est comme une note : 18 points, ça ne veut rien dire sans le sur 20.

La fréquence relative répond à ça. C'est la fréquence absolue divisée par l'effectif.

f i, c'est la fréquence relative de la valeur x i.

On divise n i, la fréquence absolue, par n, l'effectif total.

Pour 19 ans : 6 divisé par 16, ça donne 0,375. Soit 37,5 %.

Une fréquence relative est toujours comprise entre 0 et 1. Et la somme des f i vaut toujours 1, c'est-à-dire 100 %.

Pourquoi ? Parce que la somme des n i sur n, c'est n sur n. Donc 1.

### Scène 8 — Fréquence relative  (`p1_07_batonnets`)

Pour visualiser, on utilise un diagramme en bâtonnets. Les valeurs x i en abscisse, les fréquences en ordonnée.

À gauche, les fréquences absolues. À droite, les fréquences relatives. Les deux diagrammes ont exactement la même allure.

Seule la graduation de l'axe vertical change : un nombre d'étudiants d'un côté, un pourcentage de l'autre.

Petite remarque : si les fréquences sont très éloignées, certains bâtonnets deviennent invisibles. On gradue alors l'axe en échelle logarithmique.

À retenir : f i égale n i sur n. C'est une part entre 0 et 1, et la somme des f i vaut 1.

### Scène 9 — Fréquences cumulées  (`p1_08_cumul_def`)

Nouvelle question : combien d'étudiants ont 19 ans ou moins ? Pour répondre, on cumule.

Pense au compteur à l'entrée d'une salle. À chaque groupe qui entre, le total grimpe.

La fréquence absolue cumulée, notée grand N i, compte les observations inférieures ou égales à x i.

Grand N i égale la somme des n j, pour j allant de 1 à i.

En pratique, on ajoute simplement la ligne suivante : grand N i égale grand N i moins 1, plus n i.

Même idée en pourcentage : grand F i, la fréquence relative cumulée. C'est grand N i divisé par n.

### Scène 10 — Fréquences cumulées  (`p1_09_cumul_tab`)

Construisons le tableau. 2, puis 2 plus 4 égale 6, puis 6 plus 6 égale 12, puis 14, puis 16.

Dernière ligne : grand N k vaut toujours n, et grand F k vaut toujours 1.

Que peut-on lire ? Grand N 3 vaut 12 : 12 étudiants ont 19 ans ou moins. Soit 75 %.

Le complément donne le reste : 1 moins 0,75. Donc 25 % des étudiants ont plus de 19 ans.

Pour un intervalle, on soustrait. Entre 18 et 20 ans inclus : grand F de 20 moins grand F de 17.

On retire 17, et pas 18, car on veut garder les étudiants de 18 ans. 87,5 moins 12,5 : ça fait 75 %.

À retenir : grand F i est la part des observations inférieures ou égales à x i. Pour un intervalle, on soustrait deux F.

### Scène 11 — Fonction de répartition  (`p1_10_repartition`)

Les grands F i ne sont définis que pour les valeurs observées. Mais quelle est la part des étudiants de 19 ans et demi ou moins ?

Pour répondre pour n'importe quel x, on définit la fonction de répartition, F de x.

F de x égale la part des observations inférieures ou égales à x. Dans la partie probabilités, tu l'écriras : probabilité que X soit inférieur ou égal à x.

Son graphique est un escalier. Comme un vrai escalier : tant que tu n'atteins pas la marche suivante, tu restes au même niveau.

Avant 17 ans, personne. F de 16 vaut 0.

Entre 19 et 20, on reste sur la même marche. F de 19 et demi égale F de 19, soit 0,75.

Après 21 ans, tout le monde est compté. F de 25 vaut 1.

Regarde bien le bord des marches. Le point plein est à gauche : la marche est fermée à gauche et ouverte à droite.

Donc en x égale 20, on est déjà sur la nouvelle marche. F de 20 vaut 0,875, et pas 0,75.

À retenir : F de x est la part des observations inférieures ou égales à x. En discret, c'est un escalier, fermé à gauche, ouvert à droite.

### Scène 12 — Récapitulatif  (`p1_11_recap`)

Récapitulons la partie 1.

Une observation est qualitative, quantitative discrète, ou quantitative continue.

La fréquence relative f i vaut n i sur n. Les n i ont pour somme n, et les f i ont pour somme 1.

La fréquence cumulée grand N i additionne les n j jusqu'à i. Et grand F i vaut grand N i sur n.

La fonction de répartition F de x donne la part des observations inférieures ou égales à x. En discret, c'est un escalier.

Pour la part entre deux valeurs, on soustrait deux F. Dans la partie 2, on passe aux données continues.

## Partie 2 — Données continues et qualitatives

### Scène 1 — Introduction  (`p2_00_titre`)

Analyse de données, chapitre 1, deuxième partie : les données continues et les données qualitatives.

### Scène 2 — Introduction  (`p2_01_intro`)

Cette fois, Alice pèse 80 étudiants, avec une balance précise au dixième de gramme.

Problème : deux mesures identiques, c'est presque impossible. Le tableau aurait 80 lignes, avec uniquement des 1 dans la colonne n i.

La solution : regrouper les valeurs en classes. Au programme : les classes, la densité, le polygone des fréquences cumulées, ses usages, et les données qualitatives.

### Scène 3 — Classes  (`p2_02_classes`)

Pense à un magasin de vêtements. Personne ne range les pulls au centimètre près : on fait des tailles S, M, L.

En statistique, une classe est un intervalle : de x i moins 1 inclus, à x i exclu.

Fermé à gauche, ouvert à droite. Ainsi, chaque valeur tombe dans une seule classe, même pile sur une limite.

Voici les poids d'Alice, en 4 classes. Les fréquences gardent le même sens qu'avant.

Une précision : grand N i compte maintenant les observations inférieures au bord droit de la classe. Par exemple, 48 étudiants pèsent moins de 75 kilos.

### Scène 4 — Classes  (`p2_03_sturges`)

Combien de classes choisir ? Ni trop peu, ni trop. La règle de Sturges donne un ordre de grandeur.

Le nombre de classes vaut environ 1 plus 10 tiers, fois logarithme en base 10 de n.

Pour n égale 80, on trouve environ 7,3. Donc environ 7 classes.

Le cours en a choisi 4 : c'est permis. Le choix reste au flair du statisticien. Et les classes n'ont pas forcément toutes la même largeur.

Regrouper fait perdre de l'information. 68, 72 et 74 kilos finissent tous dans la même classe.

On fait donc une hypothèse : dans une classe, les valeurs sont réparties uniformément. De 65 à 75 kilos, 28 étudiants sur 10 kilos : 2,8 étudiants par kilo.

À retenir : en continu, on regroupe en classes fermées à gauche et ouvertes à droite. Et on suppose les valeurs uniformément réparties dans chaque classe.

### Scène 5 — Densité  (`p2_04_densite_pb`)

Comment dessiner ces classes ? L'idée naturelle : un rectangle par classe, de hauteur n i.

Mais ton œil ne compare pas les hauteurs. Il compare les surfaces. Comme quand tu choisis la plus grosse part de pizza.

Regarde : la première et la troisième classe ont le même effectif, 20. Pourtant, le premier rectangle est une fois et demie plus grand.

Et les deux derniers ont presque la même surface, 200 et 180. Alors que la dernière classe est bien moins peuplée.

### Scène 6 — Densité  (`p2_05_densite`)

La solution : prendre comme hauteur la densité de fréquence absolue, d n i.

d n i égale n i divisé par l i.

l i, c'est la largeur de la classe : x i moins x i moins 1.

La densité, c'est le nombre moyen d'observations par unité. Ici, par kilo.

Première classe : 20 divisé par 15, environ 1,33. Le cours arrondit à 1,3.

Vérifions : la hauteur fois la largeur, 1,33 fois 15, redonne 20. L'aire du rectangle, c'est bien n i.

Ce graphique s'appelle l'histogramme des densités de fréquence absolue. Son aire totale vaut l'effectif, 80.

Même chose en relatif : d f i égale f i divisé par l i. L'aire de chaque rectangle vaut alors f i, et l'aire totale vaut 1.

Par exemple, pour la deuxième classe : 0,35 divisé par 10, ça donne 0,035.

À retenir : dans un histogramme, c'est l'aire qui compte. La hauteur est une densité, n i sur l i, pour que l'aire égale l'effectif.

### Scène 7 — Polygone des fréquences cumulées  (`p2_06_polygone`)

En discret, la fonction de répartition était un escalier. En continu, on remplace les marches par des rampes.

Pourquoi ? Parce qu'on suppose les valeurs réparties uniformément dans chaque classe. Le pourcentage cumulé monte donc régulièrement.

Prenons une classe, de x i moins 1 à x i. En fin de classe, la hauteur est grand F i : la part des observations inférieures à x i.

En début de classe, la hauteur est grand F i moins 1. On relie ces deux points par un segment.

La montée vaut f i. La largeur vaut l i. Donc la pente vaut f i sur l i : c'est exactement la densité d f i.

L'équation du segment : y égale d f i fois, x moins x i moins 1, plus grand F i moins 1.

On part de la hauteur grand F i moins 1, celle du début de la classe.

Puis on monte de d f i pour chaque unité parcourue depuis le début de la classe.

### Scène 8 — Polygone des fréquences cumulées  (`p2_07_polygone_ex`)

Exemple avec la deuxième classe, de 65 à 75 kilos. d f 2 vaut 0,035, et grand F 1 vaut 0,25.

L'équation devient : y égale 0,035 fois, x moins 65, plus 0,25.

Vérifions en fin de classe, à 75. 0,035 fois 10, plus 0,25 : on trouve 0,6. C'est bien grand F 2.

Deuxième exemple, la troisième classe. y égale 0,025 fois, x moins 75, plus 0,6. À 85, on trouve 0,85 : c'est grand F 3.

En assemblant tous les segments, on obtient le polygone des fréquences cumulées. C'est le graphique de F de x.

Avant 50, F vaut 0. Après 100, F vaut 1. Entre les deux, un segment par classe.

En continu, inférieur ou inférieur ou égal, c'est pareil : une valeur précise a une fréquence nulle.

À retenir : sur chaque classe, F de x égale d f i fois, x moins x i moins 1, plus grand F i moins 1.

### Scène 9 — Utilité de F(x)  (`p2_08_usages`)

À quoi sert tout ça ? F de x répond à toutes les questions de pourcentage. Il y a trois cas à connaître.

En dessous de x : F de x.

Au-dessus de x : 1 moins F de x.

Entre x 1 et x 2 : F de x 2 moins F de x 1.

Et pour un nombre d'étudiants, on multiplie le pourcentage par l'effectif n.

Exemple a. Quelle part des étudiants pèse moins de 73 kilos ? 73 est dans la deuxième classe.

F de 73 égale 0,035 fois 8, plus 0,25. Soit 0,53 : 53 %.

Exemple b. Plus de 73 kilos ? C'est le complément : 1 moins 0,53, soit 47 %.

Exemple c. Combien d'étudiants pèsent moins de 73 kilos ? 80 fois 0,53 : 42,4. Donc environ 42 étudiants.

### Scène 10 — Utilité de F(x)  (`p2_09_exemple_d`)

Exemple d. On va le faire lentement, étape par étape. Quelle part des étudiants pèse entre 73 et 81 kilos ?

Étape 1 : on traduit la question. Entre deux valeurs, c'est F de 81 moins F de 73.

Étape 2 : F de 73, on l'a déjà calculé. 0,53.

Étape 3 : dans quelle classe tombe 81 ? Entre 75 et 85 : la troisième classe.

On prend donc l'équation de la troisième classe : 0,025 fois, x moins 75, plus 0,6.

81 moins 75, ça fait 6. 0,025 fois 6, ça fait 0,15. Plus 0,6 : on obtient 0,75.

Étape 4 : on soustrait. 0,75 moins 0,53, égale 0,22.

Donc 22 % des étudiants pèsent entre 73 et 81 kilos. Sur le graphique, c'est l'écart vertical entre les deux hauteurs.

Attention au piège : ne recopie pas les grands F i du tableau. 0,60 ou 0,85 sont les valeurs en fin de classe, pas en 73 ou en 81.

### Scène 11 — Utilité de F(x)  (`p2_10_inverse`)

Dernier usage : le chemin inverse. On connaît un pourcentage, on cherche la valeur de x.

Exemple e. Quel poids sépare les 30 % d'étudiants les plus légers ? On résout F de x égale 0,3.

Sur le graphique, 0,3 est entre 0,25 et 0,6. Donc on est dans la deuxième classe.

On résout : 0,035 fois, x moins 65, plus 0,25, égale 0,3.

x moins 65 égale 0,05 divisé par 0,035, environ 1,43. Donc x vaut environ 66,4 kilos.

Exemple bonus. Quel poids coupe le groupe en deux moitiés ? On résout F de x égale 0,5.

Toujours la deuxième classe. x moins 65 égale 0,25 divisé par 0,035, environ 7,14. Donc x vaut environ 72,1 kilos. Cette valeur s'appelle la médiane.

À retenir : en dessous, F de x. Au-dessus, 1 moins F de x. Entre deux valeurs, la différence. Et pour le chemin inverse, on résout F de x égale p.

### Scène 12 — Données qualitatives  (`p2_11_qualitatif`)

Dernière famille : les données qualitatives. On garde les fréquences absolues et relatives, exactement comme avant.

Par contre, pas de fréquences cumulées. Ces valeurs ne sont pas des nombres : les ranger sur un axe n'a pas de sens mathématique.

Le contexte peut quand même suggérer un ordre. Par exemple, des avis de clients, du plus satisfait au moins satisfait.

80 clients ont répondu. Satisfait : 42 réponses, donc 42 sur 80, soit 52,5 %.

Sans ordre naturel, on classe par fréquence décroissante, ou par ordre alphabétique.

Le graphique classique, c'est le diagramme en camembert. Chaque part a une surface proportionnelle à sa fréquence.

L'angle d'une part vaut f i fois 360 degrés. Pour Satisfait : 0,525 fois 360, soit 189 degrés.

À retenir : en qualitatif, on utilise n i et f i, mais pas de cumul. Et en camembert, l'angle vaut f i fois 360 degrés.

### Scène 13 — Récapitulatif  (`p2_12_recap`)

Récapitulons la partie 2.

En continu, on regroupe en classes, fermées à gauche, ouvertes à droite. La règle de Sturges donne un ordre de grandeur du nombre de classes.

Dans un histogramme, la hauteur est une densité, n i sur l i. Comme ça, l'aire égale la fréquence.

Sur chaque classe, F de x égale d f i fois, x moins x i moins 1, plus grand F i moins 1.

En dessous de x, F de x. Au-dessus, 1 moins F de x. Entre deux valeurs, la différence.

En qualitatif, pas de cumul, et l'angle d'une part vaut f i fois 360 degrés. Tu as maintenant tout le chapitre 1. Bon courage pour les exercices !
