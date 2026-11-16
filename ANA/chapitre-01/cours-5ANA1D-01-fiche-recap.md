# Fiche récap — 5ANA1D, chapitre 1 : Statistique descriptive

## Vocabulaire
- **Population** : tout le groupe étudié. **Individu** : un élément (personne, animal, objet).
- **Échantillon** : la partie qu'on interroge vraiment. **Effectif n** : nombre d'observations.
- **Types d'observations** :
  - qualitatives : pas des nombres (couleur, marque de GSM) ;
  - quantitatives discrètes : valeurs isolées, dénombrables (nombre d'enfants) ;
  - quantitatives continues : toutes les valeurs d'un intervalle (poids d'un œuf).
- Continu arrondi (taille au cm) = **continu discrétisé**.
- Mesures dans le temps = série chronologique ; au même moment = série statistique.

## Données discrètes
| Notion | Formule | Sens |
|---|---|---|
| Fréquence absolue | nᵢ | nombre de fois où xᵢ apparaît |
| Propriété | Σ nᵢ = n | la somme donne l'effectif |
| Fréquence relative | fᵢ = nᵢ / n | part entre 0 et 1, Σ fᵢ = 1 |
| Fréq. absolue cumulée | Nᵢ = n₁ + … + nᵢ = Nᵢ₋₁ + nᵢ | nombre d'observations ≤ xᵢ |
| Fréq. relative cumulée | Fᵢ = Nᵢ / n = f₁ + … + fᵢ | part des observations ≤ xᵢ ; Fₖ = 1 |

- Graphique des nᵢ ou fᵢ : **diagramme en bâtonnets** (même allure, seule l'échelle verticale change). Écarts énormes → échelle log₁₀.
- **Fonction de répartition** : F(x) = part des observations ≤ x, définie pour tout réel x.
  En discret : **escalier fermé à gauche, ouvert à droite** (ex. âges : F(20) = 0,875, pas 0,75).

## Données continues
- **Classes** [xᵢ₋₁, xᵢ[ : fermées à gauche, ouvertes à droite → chaque valeur dans une seule classe.
- Nᵢ, Fᵢ = observations **inférieures au bord droit** xᵢ.
- **Règle de Sturges** : k ≈ 1 + (10/3)·log₁₀ n (ordre de grandeur ; n = 80 → ≈ 7 classes).
- Hypothèse : valeurs **réparties uniformément** dans chaque classe.
- **Densités** (hauteurs de l'histogramme, pour que l'aire = la fréquence) :
  - dnᵢ = nᵢ / lᵢ, avec lᵢ = xᵢ − xᵢ₋₁ ; aire d'un rectangle = nᵢ, aire totale = n ;
  - dfᵢ = fᵢ / lᵢ ; aire d'un rectangle = fᵢ, aire totale = 1.
- **Polygone des fréquences cumulées** (graphe de F) : sur [xᵢ₋₁, xᵢ[,
  **F(x) = dfᵢ · (x − xᵢ₋₁) + Fᵢ₋₁** (pente = dfᵢ). F = 0 avant la 1ʳᵉ classe, 1 après la dernière.
- En continu, « < x » et « ≤ x » donnent la même valeur.

## Utiliser F(x)
| Question | Calcul |
|---|---|
| Part en dessous de x | F(x) |
| Part au-dessus de x | 1 − F(x) |
| Part entre x₁ et x₂ | F(x₂) − F(x₁) |
| Nombre d'observations | n × part |
| Valeur pour une part p (chemin inverse) | résoudre F(x) = p dans la bonne classe |

**Exemple (poids de 80 étudiants)** : F(73) = 0,035 × 8 + 0,25 = 0,53 ; F(81) = 0,025 × 6 + 0,6 = 0,75 ;
part entre 73 et 81 kg = 0,22. ⚠ Calcule F(x) avec l'équation de la classe, ne recopie pas les Fᵢ du tableau.
F(x) = 0,3 → x ≈ 66,4 kg ; F(x) = 0,5 → x ≈ 72,1 kg (médiane).

## Données qualitatives
- On garde nᵢ et fᵢ, **pas de fréquences cumulées** (pas d'ordre numérique).
- Ordre : celui du contexte (avis), sinon par fréquence ou alphabétique.
- **Camembert** : angle d'une part = fᵢ × 360° (ex. 42/80 = 0,525 → 189°).

## Points du PDF à vérifier
- p. 10 : « fᵢ est le nombre d'observations inférieures à xᵢ » → probablement une coquille pour **Nᵢ**.
- p. 10 : « Les classes ne doivent pas être toutes de même largeur » → compris comme « pas forcément ».
- p. 11 : dn₁ = 1,3 et df₁ = 0,017 sont des arrondis (valeurs exactes : 4/3 et 1/60).
