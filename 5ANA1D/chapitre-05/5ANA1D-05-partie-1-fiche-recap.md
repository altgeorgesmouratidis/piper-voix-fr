# 5ANA1D – Chapitre 5, partie 1 : Introduction au calcul des probabilités

*Vocabulaire, probabilité a priori et a posteriori, opérations sur les événements*

## Points à retenir

- **Expérience aléatoire** : une action et ce que l'on note, dont le résultat est imprévisible. Exemple : jeter un dé et noter le point.
- **Ensemble des possibilités $\Omega$** : tous les résultats possibles. Pour un dé, $\Omega = \{1, 2, 3, 4, 5, 6\}$.
- **Événement** : un sous-ensemble de $\Omega$. Exemple : « au moins 5 » = $\{5, 6\}$.
- **Probabilité** : $0 \le P(A) \le 1$. $P = 0$ veut dire impossible ($\varnothing$), $P = 1$ veut dire certain ($\Omega$).
- **Équiprobables** : même probabilité (pièce équilibrée, dé normal). Ce n'est plus le cas avec un dé pipé.
- **Probabilité a priori** : compter des cas, à condition qu'ils soient **équiprobables**.
- **Piège des deux dés** : les 11 sommes possibles ne sont pas équiprobables. Il faut compter les 36 couples.
- **Probabilité a posteriori** : la limite de la fréquence relative quand on répète l'expérience. La fréquence est expérimentale, la probabilité est théorique.
- **Événements et ensembles** : ET = $\cap$, OU = $\cup$, NON = $\overline{A}$.
- **Incompatibles** (disjoints) : $A \cap B = \varnothing$.
- **Astuce** : quand un événement est compliqué à compter, on calcule son contraire.

## Formules

$$P(A) = \frac{\text{nombre de cas favorables}}{\text{nombre de cas équiprobables possibles}}$$
Exemple : P(somme de deux dés $\ge 10$) $= \frac{6}{36} = \frac16$, et non $\frac{3}{11}$.

$$f_n(A) = \frac{\text{nb de fois où } A \text{ se réalise}}{n} \qquad P(A) = \lim_{n \to \infty} f_n(A)$$
Exemple : sur 20 lancers de pièce, 9 piles donnent $f_{20} = 0{,}45$. La fréquence se stabilise vers $\frac12$.

$$\frac{S_{\text{cercle}}}{S_{\text{carré}}} = \frac{\pi r^2}{(2r)^2} = \frac{\pi}{4}$$
Exemple : on tire des points au hasard dans le carré, puis $4 \times f_n \to \pi$. Une simulation donne 3,12 avec 100 points et 3,140 avec 100 000 points.

$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$
Exemple avec un dé, pair OU au moins 5 : $\frac36 + \frac26 - \frac16 = \frac46 = \frac23$.

$$\text{Si } A, B \text{ incompatibles : } P(A \cup B) = P(A) + P(B)$$
Exemple, « 1 » OU « au moins 5 » : $\frac16 + \frac26 = \frac12$.

$$P(\overline{A}) = 1 - P(A)$$
Exemple : P(somme de deux dés $< 10$) $= 1 - \frac16 = \frac56$.
