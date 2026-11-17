# 5ANA1D – Chapitre 5, partie 2 : Probabilités conditionnelles, totales et Bayes

## Points à retenir

- **Dépendants** : savoir que B est réalisé change la probabilité de A.
- **$P(A/B)$** se lit « probabilité de A sachant B ». On ne garde que les cas où B est réalisé.
- **Indépendants** : $P(A/B) = P(A)$. Un tirage **sans remise** donne des tirages dépendants, un tirage **avec remise** des tirages indépendants.
- **Arbre de probabilités** :
  - les branches qui partent d'un même sommet ont une somme égale à 1 ;
  - on **multiplie** le long d'un chemin ;
  - on **additionne** les chemins qui mènent à l'événement.
- **Système exhaustif** $\{E_1, \dots, E_n\}$ :
  - aucun événement n'est impossible ;
  - ils sont incompatibles deux à deux ;
  - leur union est $\Omega$.

  Exemples : {cœurs, carreaux, noires} est exhaustif. {cœurs, noires} ne l'est pas : il y a un trou. {images, rouges, noires} non plus : il y a un chevauchement.
- **Bayes** : on remonte de la conséquence à la cause, ce qui donne l'arbre inverse.
- **Correction du cours p. 50** : le dernier terme concerne mardi, mercredi ou jeudi (et non « mercredi, jeudi ou vendredi »).

## Formules

$$P(A/B) = \frac{P(A \cap B)}{P(B)}$$
Exemple avec un dé : P(6 / pair) $= \frac{1/6}{1/2} = \frac13$.

$$P(A \cap B) = P(A) \cdot P(B/A) = P(B) \cdot P(A/B)$$
Exemple : P(pair et 6) $= \frac12 \times \frac13 = \frac16$.

$$\text{Si } A, B \text{ indépendants : } P(A \cap B) = P(A) \cdot P(B)$$
Exemple avec l'urne (5 blanches, 5 noires) : deux blanches sans remise donnent $\frac{5}{10} \times \frac49 = \frac29 \approx 0{,}222$. Avec remise, on obtient $\frac{5}{10} \times \frac{5}{10} = \frac14$.

$$P(A \cap B \cap C) = P(A) \cdot P(B/A) \cdot P(C/(A \cap B))$$
Exemple : trois blanches sans remise donnent $\frac{5}{10} \times \frac49 \times \frac38 = \frac1{12}$.

$$P(A) = \sum_{i=1}^{n} P(E_i) \cdot P(A/E_i)$$
Exemple du bus : P(à l'heure) $= \frac27 \cdot 0{,}9 + \frac27 \cdot 0{,}6 + \frac37 \cdot 0{,}8 \approx 0{,}771$.

$$P(E_k/A) = \frac{P(E_k) \cdot P(A/E_k)}{\sum_{i} P(E_i) \cdot P(A/E_i)}$$
Exemple : P(week-end / à l'heure) $= \frac{\frac27 \times 0{,}9}{0{,}771} = \frac13$.

Arbre inverse :
- sachant « à l'heure » : week-end $\frac13$, lu/ve $\frac29$, ma/me/je $\frac49$ ;
- sachant « en retard » : week-end $\frac18$, lu/ve $\frac12$, ma/me/je $\frac38$.
