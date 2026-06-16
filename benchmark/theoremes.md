# Benchmark Synthétique — Liste des Théorèmes

30 théorèmes de niveau L3, avec leurs hypothèses formalisées.
Chaque hypothèse est une proposition booléenne indépendante (présente / absente).

---

## Analyse Réelle

### T01 — Théorème de Rolle
| # | Hypothèse |
|---|---|
| H1 | f est continue sur [a, b] |
| H2 | f est dérivable sur ]a, b[ |
| H3 | f(a) = f(b) |

**Conclusion :** ∃ c ∈ ]a, b[ tel que f'(c) = 0

---

### T02 — Théorème des Accroissements Finis (Lagrange)
| # | Hypothèse |
|---|---|
| H1 | f est continue sur [a, b] |
| H2 | f est dérivable sur ]a, b[ |

**Conclusion :** ∃ c ∈ ]a, b[ tel que f(b) − f(a) = f'(c)(b − a)

---

### T03 — Théorème des Valeurs Intermédiaires (TVI)
| # | Hypothèse |
|---|---|
| H1 | f est continue sur [a, b] |
| H2 | f(a) et f(b) sont de signes opposés (ou y est compris entre f(a) et f(b)) |

**Conclusion :** ∃ c ∈ ]a, b[ tel que f(c) = y

---

### T04 — Théorème de Weierstrass (existence de extrema)
| # | Hypothèse |
|---|---|
| H1 | f est continue sur [a, b] |
| H2 | [a, b] est un intervalle fermé et borné |

**Conclusion :** f atteint son maximum et son minimum sur [a, b]

---

### T05 — Théorème de la limite de la dérivée
| # | Hypothèse |
|---|---|
| H1 | f est continue sur [a, b] |
| H2 | f est dérivable sur ]a, b[ |
| H3 | lim_{x→a⁺} f'(x) = ℓ existe (finie) |

**Conclusion :** f est dérivable en a et f'(a) = ℓ

---

### T06 — Règle de L'Hôpital
| # | Hypothèse |
|---|---|
| H1 | f et g sont dérivables au voisinage de a (sauf peut-être en a) |
| H2 | g'(x) ≠ 0 au voisinage de a |
| H3 | f(a) = g(a) = 0 (forme 0/0) ou f et g → ±∞ (forme ∞/∞) |
| H4 | lim_{x→a} f'(x)/g'(x) = ℓ existe |

**Conclusion :** lim_{x→a} f(x)/g(x) = ℓ

---

### T07 — Théorème de Cauchy (accroissements finis généralisés)
| # | Hypothèse |
|---|---|
| H1 | f et g sont continues sur [a, b] |
| H2 | f et g sont dérivables sur ]a, b[ |
| H3 | g'(x) ≠ 0 sur ]a, b[ |

**Conclusion :** ∃ c ∈ ]a, b[ tel que [f(b)−f(a)]g'(c) = [g(b)−g(a)]f'(c)

---

### T08 — Théorème de développement limité (Taylor-Young)
| # | Hypothèse |
|---|---|
| H1 | f est n fois dérivable en a |

**Conclusion :** f(x) = Σ_{k=0}^{n} f^(k)(a)/k! · (x−a)^k + o((x−a)^n)

---

### T09 — Formule de Taylor avec reste de Lagrange
| # | Hypothèse |
|---|---|
| H1 | f est n+1 fois dérivable sur ]a, b[ |
| H2 | f est n fois dérivable sur [a, b] (continue) |

**Conclusion :** ∃ c ∈ ]a, b[ tel que f(b) = Σ_{k=0}^{n} f^(k)(a)/k! · (b−a)^k + f^(n+1)(c)/(n+1)! · (b−a)^(n+1)

---

### T10 — Critère de convergence des séries (d'Alembert)
| # | Hypothèse |
|---|---|
| H1 | uₙ > 0 pour tout n suffisamment grand |
| H2 | lim_{n→∞} u_{n+1}/uₙ = ℓ existe |

**Conclusion :** Si ℓ < 1 la série converge ; si ℓ > 1 elle diverge ; si ℓ = 1 le critère est non concluant

---

## Algèbre Linéaire

### T11 — Théorème du rang (dimension)
| # | Hypothèse |
|---|---|
| H1 | f est une application linéaire de E vers F |
| H2 | E est un espace vectoriel de dimension finie n |

**Conclusion :** dim(Ker f) + dim(Im f) = dim(E)

---

### T12 — Théorème de la base incomplète
| # | Hypothèse |
|---|---|
| H1 | E est un espace vectoriel de dimension finie n |
| H2 | F = (f₁, ..., fₖ) est une famille libre de E avec k ≤ n |

**Conclusion :** On peut compléter F en une base de E

---

### T13 — Diagonalisabilité (condition suffisante)
| # | Hypothèse |
|---|---|
| H1 | f est un endomorphisme de E (dim finie) |
| H2 | f admet n valeurs propres distinctes (n = dim E) |

**Conclusion :** f est diagonalisable

---

### T14 — Théorème de Cayley-Hamilton
| # | Hypothèse |
|---|---|
| H1 | A est une matrice carrée n×n |
| H2 | χ_A est le polynôme caractéristique de A |

**Conclusion :** χ_A(A) = 0

---

### T15 — Théorème spectral (matrices symétriques réelles)
| # | Hypothèse |
|---|---|
| H1 | A est une matrice carrée réelle |
| H2 | A est symétrique (A = Aᵀ) |

**Conclusion :** A est diagonalisable dans une base orthonormée ; toutes ses valeurs propres sont réelles

---

### T16 — Réduction de Jordan (existence)
| # | Hypothèse |
|---|---|
| H1 | A est une matrice carrée n×n à coefficients complexes |

**Conclusion :** A est semblable à une matrice de Jordan

---

### T17 — Inégalité de Cauchy-Schwarz
| # | Hypothèse |
|---|---|
| H1 | E est un espace vectoriel muni d'un produit scalaire ⟨·,·⟩ |
| H2 | u et v sont deux vecteurs de E |

**Conclusion :** |⟨u, v⟩|² ≤ ⟨u, u⟩ · ⟨v, v⟩

---

### T18 — Théorème de projection orthogonale
| # | Hypothèse |
|---|---|
| H1 | E est un espace de Hilbert (ou espace euclidien) |
| H2 | F est un sous-espace vectoriel fermé de E |

**Conclusion :** Tout vecteur x ∈ E s'écrit de façon unique x = p + q avec p ∈ F et q ∈ F⊥

---

## Topologie / Analyse

### T19 — Théorème de Heine (continuité uniforme)
| # | Hypothèse |
|---|---|
| H1 | f est continue sur [a, b] |
| H2 | [a, b] est un compact (fermé borné de ℝ) |

**Conclusion :** f est uniformément continue sur [a, b]

---

### T20 — Théorème de Bolzano-Weierstrass
| # | Hypothèse |
|---|---|
| H1 | (uₙ) est une suite bornée de réels (ou de ℝⁿ) |

**Conclusion :** (uₙ) admet au moins une sous-suite convergente

---

### T21 — Théorème de convergence monotone (suites)
| # | Hypothèse |
|---|---|
| H1 | (uₙ) est une suite croissante |
| H2 | (uₙ) est majorée |

**Conclusion :** (uₙ) converge

---

### T22 — Théorème des suites adjacentes
| # | Hypothèse |
|---|---|
| H1 | (uₙ) est croissante et (vₙ) est décroissante |
| H2 | vₙ − uₙ → 0 |

**Conclusion :** (uₙ) et (vₙ) convergent vers la même limite

---

### T23 — Critère de Cauchy (suites)
| # | Hypothèse |
|---|---|
| H1 | (uₙ) est une suite de réels (ou dans un espace complet) |

**Conclusion :** (uₙ) converge ⟺ (uₙ) est une suite de Cauchy

*N.B. : La complétude de l'espace est une hypothèse implicite souvent omise par les étudiants.*

---

### T24 — Théorème de convergence dominée (intégrales)
| # | Hypothèse |
|---|---|
| H1 | (fₙ) est une suite de fonctions mesurables |
| H2 | fₙ → f presque partout |
| H3 | ∃ g intégrable telle que \|fₙ\| ≤ g p.p. pour tout n |

**Conclusion :** ∫fₙ → ∫f et lim ∫fₙ = ∫ lim fₙ

---

## Équations Différentielles

### T25 — Existence et unicité (Cauchy-Lipschitz)
| # | Hypothèse |
|---|---|
| H1 | f est continue en t |
| H2 | f est lipschitzienne en y (ou C¹ en y suffit) |
| H3 | Une condition initiale y(t₀) = y₀ est donnée |

**Conclusion :** Il existe une unique solution maximale au problème de Cauchy y' = f(t, y)

---

### T26 — Principe de superposition (EDO linéaires)
| # | Hypothèse |
|---|---|
| H1 | L est un opérateur différentiel linéaire |
| H2 | y₁ est solution de L(y) = f₁ et y₂ est solution de L(y) = f₂ |

**Conclusion :** y₁ + y₂ est solution de L(y) = f₁ + f₂

---

## Intégration

### T27 — Théorème fondamental de l'analyse (TFA)
| # | Hypothèse |
|---|---|
| H1 | f est continue sur [a, b] |

**Conclusion :** La fonction F(x) = ∫_a^x f(t)dt est dérivable sur [a, b] et F'(x) = f(x)

---

### T28 — Intégration par parties
| # | Hypothèse |
|---|---|
| H1 | u et v sont de classe C¹ sur [a, b] |

**Conclusion :** ∫_a^b u'v = [uv]_a^b − ∫_a^b uv'

---

### T29 — Changement de variable dans une intégrale
| # | Hypothèse |
|---|---|
| H1 | φ est de classe C¹ sur [α, β] |
| H2 | f est continue sur φ([α, β]) |

**Conclusion :** ∫_α^β f(φ(t))φ'(t)dt = ∫_{φ(α)}^{φ(β)} f(x)dx

---

## Probabilités

### T30 — Théorème Central Limite (TCL)
| # | Hypothèse |
|---|---|
| H1 | (Xₙ) est une suite de variables aléatoires indépendantes |
| H2 | Les Xₙ sont identiquement distribuées |
| H3 | E[X₁] = μ existe et est finie |
| H4 | Var(X₁) = σ² existe, est finie et strictement positive |

**Conclusion :** √n · (X̄ₙ − μ)/σ → N(0,1) en loi

---

## Récapitulatif

| # | Théorème | Domaine | Nb hypothèses |
|---|---|---|---|
| T01 | Rolle | Analyse | 3 |
| T02 | Lagrange (TAF) | Analyse | 2 |
| T03 | TVI | Analyse | 2 |
| T04 | Weierstrass | Analyse | 2 |
| T05 | Limite de la dérivée | Analyse | 3 |
| T06 | L'Hôpital | Analyse | 4 |
| T07 | Cauchy (TAF généralisé) | Analyse | 3 |
| T08 | Taylor-Young | Analyse | 1 |
| T09 | Taylor-Lagrange | Analyse | 2 |
| T10 | D'Alembert | Séries | 2 |
| T11 | Théorème du rang | Algèbre | 2 |
| T12 | Base incomplète | Algèbre | 2 |
| T13 | Diagonalisabilité | Algèbre | 2 |
| T14 | Cayley-Hamilton | Algèbre | 2 |
| T15 | Théorème spectral | Algèbre | 2 |
| T16 | Réduction de Jordan | Algèbre | 1 |
| T17 | Cauchy-Schwarz | Algèbre | 2 |
| T18 | Projection orthogonale | Algèbre | 2 |
| T19 | Heine | Topologie | 2 |
| T20 | Bolzano-Weierstrass | Topologie | 1 |
| T21 | Convergence monotone | Suites | 2 |
| T22 | Suites adjacentes | Suites | 2 |
| T23 | Cauchy (suites) | Suites | 1 |
| T24 | Convergence dominée | Intégration | 3 |
| T25 | Cauchy-Lipschitz | EDO | 3 |
| T26 | Superposition | EDO | 2 |
| T27 | TFA | Intégration | 1 |
| T28 | Intégration par parties | Intégration | 1 |
| T29 | Changement de variable | Intégration | 2 |
| T30 | TCL | Probabilités | 4 |