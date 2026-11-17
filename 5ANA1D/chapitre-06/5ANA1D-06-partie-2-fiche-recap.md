# 5ANA1D – Chapitre 6, partie 2 : Variables aléatoires continues

## Points à retenir

- **Variable continue** : valeurs réelles dans un intervalle (poids, distance d'une pierre, attente du bus).
- **Probabilité en un point** : toujours nulle, $P[X = a] = 0$. On raisonne sur des intervalles.
- **Distribution par classes** : $p_i = P[x_{i-1} \le X < x_i]$, avec le **principe d'uniformité** (la probabilité est étalée de façon égale dans la classe).
- **Histogramme des densités** : l'aire de chaque rectangle vaut $p_i$, l'aire totale vaut 1, et la probabilité d'un intervalle est l'aire au-dessus de cet intervalle.
- **Fonction de répartition** : $F(x) = P[X \le x]$. Ligne continue faite de segments, dont la pente vaut $dp_i$.
- **Fonction de densité** $f$ : le cas limite des classes infiniment fines. $f(x) \ge 0$ et l'aire totale vaut 1. $F$ est une primitive de $f$.
- **Passage au continu** : les $\sum$ deviennent des $\int$, $x_i$ devient $x$ et $p_i$ devient $f(x)\,dx$.

## Formules

Exemple suivi : la taille (cm). Classes $[150, 170[$ : 0,3 ; $[170, 180[$ : 0,45 ; $[180, 200[$ : 0,25.

$$dp_i = \frac{p_i}{l_i}$$
Exemple : 0,015 ; 0,045 ; 0,0125. Donc $P[150 \le X < 151] = 0{,}015$.

$$F(x) = dp_i\,(x - x_{i-1}) + F(x_{i-1})$$
Exemple : $F(175) = 0{,}045 \times 5 + 0{,}3 = 0{,}525$ et $F(190) = 0{,}0125 \times 10 + 0{,}75 = 0{,}875$.

$$P[a \le X \le b] = F(b) - F(a)$$
Exemple : $P[175 \le X \le 190] = 0{,}875 - 0{,}525 = 0{,}35$. Avec les aires : $0{,}225 + 0{,}125 = 0{,}35$.

$$E[X] = \sum_{i=1}^{n} p_i c_i \qquad c_i = \frac{x_{i-1} + x_i}{2}$$
Exemple : centres 160, 175, 190, donc $\mu = 48 + 78{,}75 + 47{,}5 = 174{,}25$ cm.

$$\sigma^2 = \sum_{i=1}^{n} p_i (c_i - \mu)^2 = \sum_{i=1}^{n} p_i c_i^2 - \mu^2$$
Exemple : $30\,486{,}25 - 174{,}25^2 \approx 123{,}19$, donc $\sigma \approx 11{,}10$ cm.

$$\int_{-\infty}^{+\infty} f(x)\,dx = 1 \qquad P[a \le X \le b] = \int_a^b f(x)\,dx \qquad F(x) = \int_{-\infty}^{x} f(t)\,dt$$
Exemple inventé : l'attente du bus, avec $f(x) = \frac{1}{10}$ sur $[0, 10]$ min. Aire totale $10 \times \frac{1}{10} = 1$. $P[2 \le X \le 5] = \frac{3}{10} = 0{,}3 = F(5) - F(2)$.

$$E[X] = \int_{-\infty}^{+\infty} x\,f(x)\,dx \qquad \sigma^2 = \int_{-\infty}^{+\infty} x^2 f(x)\,dx - \mu^2$$
Exemple du bus : $E[X] = \left[\frac{x^2}{20}\right]_0^{10} = 5$ min. $\sigma^2 = \frac{100}{3} - 25 = \frac{25}{3} \approx 8{,}33$, donc $\sigma \approx 2{,}89$ min.
