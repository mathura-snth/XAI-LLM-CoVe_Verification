# Implications Admises

## 1. Régularité des fonctions (Analyse)
```
f dérivable en a  ⟹  f continue en a
f dérivable sur I  ⟹  f continue sur I
f dérivable sur ]a, b[  ⟹  f continue sur ]a, b[
f dérivable sur [a, b]  ⟹  f continue sur [a, b]
f de classe C1 sur I  ⟹  f dérivable sur I
f de classe C1 sur I  ⟹  f continue sur I
f de classe C2 sur I  ⟹  f de classe C1 sur I
f de classe C2 sur I  ⟹  f dérivable sur I
f de classe Cn sur I  ⟹  f de classe Ck sur I  (pour tout k ≤ n)
f de classe C∞ sur I  ⟹  f de classe Cn sur I  (pour tout n)
f continue sur [a, b]  ⟹  f continue sur ]a, b[
f dérivable sur [a, b]  ⟹  f dérivable sur ]a, b[
f lipschitzienne sur I  ⟹  f uniformément continue sur I
f uniformément continue sur I  ⟹  f continue sur I
f monotone sur [a, b]  ⟹  f intégrable sur [a, b]
f continue sur [a, b]  ⟹  f intégrable sur [a, b]
f de classe C1 sur [a, b]  ⟹  f à variation bornée sur [a, b]
f dérivable sur [a, b]  ⟹  f dérivable sur ]a, b[    ← implication utile pour Rolle/Lagrange
f continue sur ℝ  ⟹  f continue sur [a, b]  (pour tout a, b)
f continue sur ℝ  ⟹  f continue sur ]a, b[  (pour tout a, b)
f dérivable sur ℝ  ⟹  f dérivable sur ]a, b[  (pour tout a, b)
[a, b] est compact  ⟹  [a, b] est fermé et borné    ← équivalent dans ℝ
[a, b] est fermé et borné  ⟹  [a, b] est compact    ← équivalent dans ℝ
f admet n valeurs propres distinctes (n = dim E)  ⟹  f est diagonalisable
f est symétrique réelle  ⟹  f est diagonalisable
f est diagonalisable  ⟹  le polynôme minimal est scindé à racines simples
le polynôme caractéristique est scindé à racines simples  ⟹  f est diagonalisable
f est un isomorphisme  ⟹  f est injective
f est un isomorphisme  ⟹  f est surjective
f injective et dim E = dim F (finis)  ⟹  f est un isomorphisme
f surjective et dim E = dim F (finis)  ⟹  f est un isomorphisme
F est une base de E  ⟹  F est une famille libre
F est une base de E  ⟹  F est une famille génératrice
F libre avec card(F) = dim E  ⟹  F est une base de E
F génératrice avec card(F) = dim E  ⟹  F est une base de E
E euclidien (produit scalaire)  ⟹  E est un espace normé
E de Hilbert  ⟹  E est un espace de Banach
E de Hilbert  ⟹  E est un espace de Hilbert (complet + produit scalaire)
u et v orthogonaux  ⟹  ⟨u,v⟩ = 0
(uₙ) converge  ⟹  (uₙ) est bornée
(uₙ) converge  ⟹  (uₙ) est de Cauchy  (dans un espace complet)
(uₙ) est de Cauchy dans un espace complet  ⟹  (uₙ) converge
(uₙ) converge  ⟹  uₙ → 0
(uₙ) croissante et bornée  ⟹  (uₙ) converge
(uₙ) décroissante et minorée  ⟹  (uₙ) converge
(uₙ) croissante et majorée  ⟹  (uₙ) converge    ← Théorème de convergence monotone
Σuₙ converge absolument  ⟹  Σuₙ converge
uₙ ≥ 0 et Σuₙ converge  ⟹  uₙ → 0
Σuₙ converge  ⟹  uₙ → 0  (condition nécessaire)
f continue sur [a, b]  ⟹  f intégrable sur [a, b]
f monotone sur [a, b]  ⟹  f intégrable sur [a, b]
f bornée et continue p.p. sur [a, b]  ⟹  f intégrable sur [a, b]
fₙ → f uniformément sur [a,b]  ⟹  fₙ → f presque partout
fₙ bornées par une constante M  ⟹  fₙ dominées par g = M · 1_{[a,b]} (intégrable)
X admet un moment d'ordre 2  ⟹  X admet un moment d'ordre 1  (E[|X|] < ∞)
Var(X) < ∞  ⟹  E[X2] < ∞
E[X2] < ∞  ⟹  E[|X|] < ∞
X et Y indépendantes  ⟹  X et Y non corrélées  (mais pas l'inverse en général)
X ~ N(μ, σ2)  ⟹  E[X] = μ et Var(X) = σ2 existent et sont finies
(Xₙ) i.i.d. avec E[X₁2] < ∞  ⟹  E[|X₁|] < ∞    ← utile pour TCL et LGN
[a, b] compact dans ℝ  ⟹  [a, b] fermé et borné
f continue sur un compact K  ⟹  f uniformément continue sur K   ← Heine
f continue sur un compact K  ⟹  f bornée sur K
f continue sur un compact K  ⟹  f atteint ses bornes sur K      ← Weierstrass
espace complet + précompact  ⟹  compact
```

## Utilisation dans le benchmark

Quand le LLM (ou l'étudiant) cite une hypothèse P alors que l'hypothèse requise est Q :

- Si `P ⟹ Q` figure dans cette table → la copie est **acceptée** (hypothèse plus forte mais valide)
- Si `P ⟹ Q` ne figure pas → la copie est **rejetée** (hypothèse incorrecte ou insuffisante)

**Exemple**

| Hypothèse requise | Hypothèse citée | Verdict |
|---|---|---|
| f continue sur [a, b] | f de classe C1 sur [a, b] | acceptée (C1 ⟹ continue) |
| f dérivable sur ]a, b[ | f dérivable sur [a, b] | acceptée (fermé ⟹ ouvert) |
| f continue sur [a, b] | f continue sur ]a, b[ | rejetée (ouvert ⊄ fermé) |
| E[X] finie | Var(X) finie | acceptée (Var finie ⟹ E[X] finie) |
| f continue sur [a, b] | f monotone sur [a, b] | rejetée (monotone ⊄ continue) |