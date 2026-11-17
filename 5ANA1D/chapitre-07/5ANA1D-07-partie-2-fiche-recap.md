# 5ANA1D – Chapitre 7, partie 2 : la distribution normale (de X à Z, et les valeurs typiques)

## Points à retenir
- Il n'existe qu'une table, celle de $Z \sim N(0, 1)$. Pour une normale quelconque $X \sim N(\mu, \sigma)$, on centre et on réduit.
- Centrer, c'est soustraire $\mu$ : changement d'origine, car $\mu - \mu = 0$. Réduire, c'est diviser par $\sigma$ : changement d'unité, car $\sigma/\sigma = 1$.
- La valeur $z$ indique à combien d'écarts-types de la moyenne on se trouve.
- C'est un simple changement d'échelle. La moyenne correspond au 0 de $Z$, et un écart-type correspond à une unité de $Z$.
- Le $F$ des formules est toujours la fonction de répartition de la normale réduite, celle de la table.
- Pour une variable continue, $P[X \le b] = P[X < b]$.
- Valeurs typiques : environ 68 % des valeurs sont à moins de $1\sigma$ de la moyenne, 95 % à moins de $2\sigma$ et 99,7 % à moins de $3\sigma$.

## Formules
- $Z = \dfrac{X - \mu}{\sigma} \sim N(0, 1)$
  - Exemple, avec des œufs tels que $X \sim N(60, 5)$ : pour 67 g, $z = \dfrac{67-60}{5} = 1{,}4$, donc $P[X \le 67] = F(1{,}4) = 0{,}9192$.
- $P[a \le X \le b] = F\!\left(\dfrac{b-\mu}{\sigma}\right) - F\!\left(\dfrac{a-\mu}{\sigma}\right)$
  - Exemple : $P[52 \le X \le 67] = F(1{,}4) - F(-1{,}6) = 0{,}9192 - 0{,}0548 = 0{,}8644$.
- $P[X > b] = 1 - F\!\left(\dfrac{b-\mu}{\sigma}\right)$ (déduit du fait que l'aire totale vaut 1)
  - Exemple : $P[X > 70] = 1 - F(2) = 1 - 0{,}9772 = 0{,}0228$.
- $P[\mu - k\sigma \le X \le \mu + k\sigma] = F(k) - F(-k) = 2F(k) - 1$
  - $k = 1$ : $2 \times 0{,}8413 - 1 = 0{,}6826$ (œufs entre 55 et 65 g)
  - $k = 2$ : $2 \times 0{,}9772 - 1 = 0{,}9544$ (œufs entre 50 et 70 g). Au-delà de $2\sigma$ : $0{,}0456$.
  - $k = 3$ : $2 \times 0{,}9987 - 1 = 0{,}9974$ (œufs entre 45 et 75 g)

Pour aller plus loin (lien noté dans le cours) : https://www.geogebra.org/m/uRZ5DKGn
