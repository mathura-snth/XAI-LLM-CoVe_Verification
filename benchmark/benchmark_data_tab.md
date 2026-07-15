# Benchmark des théorèmes mathématiques

**Total:** 100 copies

**Correctes:** 32

**Fausses:** 68

## Détail des copies

| # | Théorème | Copie | Attendu | Verdict | Raison | Type_erreur |
|---|----------|-------|---------|---------|--------|-------------|
| 1 | Théorème des suites adjacentes | (uₙ) est croissante et (vₙ) est décroissante; vₙ − uₙ → 0 | (uₙ) est croissante et (vₙ) est décroissante; vₙ − uₙ → 0 | VRAI | OK | correcte |
| 2 | Théorème de Rolle | f est dérivable sur ]a, b[ | f est continue sur [a, b]; f est dérivable sur ]a, b[; f(a) ... | FAUX | manquante: f(a) = f(b); manquante: f est... | plusieurs_manquantes |
| 3 | Théorème de Cauchy-Lipschitz | f est continue en t; f est lipschitzienne en y; une conditio... | f est continue en t; f est lipschitzienne en y; une conditio... | VRAI | OK | correcte |
| 4 | Critère de Cauchy (suites) | (uₙ) est une suite dans un espace complet | (uₙ) est une suite dans un espace complet | VRAI | OK | correcte |
| 5 | Théorème des Valeurs Intermédiaires | f est continue sur [a, b]; y est compris entre f(a) et f(b) | f est continue sur [a, b]; y est compris entre f(a) et f(b) | VRAI | OK | correcte |
| 6 | Théorème de Cayley-Hamilton | A est une matrice carrée n×n; χ_A est le polynôme caractéris... | A est une matrice carrée n×n; χ_A est le polynôme caractéris... | VRAI | OK | correcte |
| 7 | Théorème de Rolle | f est continue sur [a, b]; f est dérivable sur ]a, b[; f(a) ... | f est continue sur [a, b]; f est dérivable sur ]a, b[; f(a) ... | VRAI | OK | correcte |
| 8 | Théorème Fondamental de l'Analyse | f est continue sur [a, b] | f est continue sur [a, b] | VRAI | OK | correcte |
| 9 | Projection orthogonale (Hilbert) | E est un espace de Hilbert; F est un sous-espace vectoriel f... | E est un espace de Hilbert; F est un sous-espace vectoriel f... | VRAI | OK | correcte |
| 10 | Théorème de Cayley-Hamilton | A est une matrice carrée n×n | A est une matrice carrée n×n; χ_A est le polynôme caractéris... | FAUX | manquante: χ_A est le polynôme caractéri... | hypothese_manquante |
| 11 | Théorème de Bolzano-Weierstrass | (uₙ) est une suite bornée de réels | (uₙ) est une suite bornée de réels | VRAI | OK | correcte |
| 12 | Théorème Central Limite | (Xₙ) est une suite de variables aléatoires indépendantes; le... | (Xₙ) est une suite de variables aléatoires indépendantes; le... | VRAI | OK | correcte |
| 13 | Principe de superposition (EDO linéaires) | L est un opérateur différentiel linéaire; y₁ est solution de... | L est un opérateur différentiel linéaire; y₁ est solution de... | FAUX | manquante: y₂ est solution de L(y) = f₂ | hypothese_manquante |
| 14 | Changement de variable dans une intégrale | f est continue sur φ([α, β]) | φ est de classe C¹ sur [α, β]; f est continue sur φ([α, β]) | FAUX | manquante: φ est de classe C¹ sur [α, β] | hypothese_manquante |
| 15 | Principe de superposition (EDO linéaires) | y₂ est solution de L(y) = f₂ | L est un opérateur différentiel linéaire; y₁ est solution de... | FAUX | manquante: L est un opérateur différenti... | plusieurs_manquantes |
| 16 | Théorème de Weierstrass | f est continue sur [a, b]; [a, b] est un intervalle fermé et... | f est continue sur [a, b]; [a, b] est un intervalle fermé et... | VRAI | OK | correcte |
| 17 | Inégalité de Jensen | φ est une fonction convexe; X est une variable aléatoire rée... | φ est une fonction convexe; X est une variable aléatoire rée... | VRAI | OK | correcte |
| 18 | Théorème de convergence monotone (suites) | (uₙ) est une suite croissante; (uₙ) est majorée | (uₙ) est une suite croissante; (uₙ) est majorée | VRAI | OK | correcte |
| 19 | Théorème de Cauchy-Lipschitz | f est continue en t; f est continue en y; une condition init... | f est continue en t; f est lipschitzienne en y; une conditio... | FAUX | hypothese_inventee: f est lipschitzienne... | hypothese_inventee |
| 20 | Théorème de Heine (continuité uniforme) | f est continue sur [a, b]; [a, b] est un intervalle fermé et... | f est continue sur [a, b]; [a, b] est un intervalle fermé et... | VRAI | OK | correcte |
| 21 | Loi des Grands Nombres (faible) | (Xₙ) est une suite de variables aléatoires indépendantes; le... | (Xₙ) est une suite de variables aléatoires indépendantes; le... | VRAI | OK | correcte |
| 22 | Réduction de Jordan (existence) | A est une matrice carrée n×n à coefficients complexes | A est une matrice carrée n×n à coefficients complexes | VRAI | OK | correcte |
| 23 | Théorème de convergence dominée | (fₙ) est une suite de fonctions mesurables; fₙ → f presque p... | (fₙ) est une suite de fonctions mesurables; fₙ → f presque p... | VRAI | OK | correcte |
| 24 | Théorème des Accroissements Finis (Lagrange) | f est continue sur [a, b] | f est continue sur [a, b]; f est dérivable sur ]a, b[ | FAUX | manquante: f est dérivable sur ]a, b[ | hypothese_manquante |
| 25 | Théorème des Valeurs Intermédiaires | y est compris entre f(a) et f(b) | f est continue sur [a, b]; y est compris entre f(a) et f(b) | FAUX | manquante: f est continue sur [a, b] | hypothese_manquante |
| 26 | Diagonalisabilité (valeurs propres distinctes) | f est un endomorphisme de E (dim finie n); f admet n valeurs... | f est un endomorphisme de E (dim finie n); f admet n valeurs... | VRAI | OK | correcte |
| 27 | Théorème spectral (matrices symétriques réelles) | A est une matrice carrée réelle; A est symétrique (A = Aᵀ) | A est une matrice carrée réelle; A est symétrique (A = Aᵀ) | VRAI | OK | correcte |
| 28 | Formule de Taylor-Young | f est n fois dérivable en a | f est n fois dérivable en a | VRAI | OK | correcte |
| 29 | Théorème de la base incomplète | E est un espace vectoriel de dimension finie n | E est un espace vectoriel de dimension finie n; F = (f₁, ...... | FAUX | manquante: F = (f₁, ..., fₖ) est une fam... | hypothese_manquante |
| 30 | Théorème de convergence monotone (suites) | (uₙ) est majorée | (uₙ) est une suite croissante; (uₙ) est majorée | FAUX | manquante: (uₙ) est une suite croissante | hypothese_manquante |
| 31 | Changement de variable dans une intégrale | φ est de classe C¹ sur [α, β]; f est continue sur φ([α, β]) | φ est de classe C¹ sur [α, β]; f est continue sur φ([α, β]) | VRAI | OK | correcte |
| 32 | Intégration par parties | u et v sont de classe C¹ sur [a, b] | u et v sont de classe C¹ sur [a, b] | VRAI | OK | correcte |
| 33 | Théorème Central Limite | les Xₙ sont identiquement distribuées | (Xₙ) est une suite de variables aléatoires indépendantes; le... | FAUX | manquante: Var(X₁) = σ² est finie et str... | plusieurs_manquantes |
| 34 | Formule de Taylor avec reste de Lagrange | f est n fois dérivable sur [a, b] (continue); f est n+1 fois... | f est n fois dérivable sur [a, b] (continue); f est n+1 fois... | VRAI | OK | correcte |
| 35 | Réduction de Jordan (existence) | A est une matrice carrée n×n à coefficients complexes; A est... | A est une matrice carrée n×n à coefficients complexes | FAUX | inventee: [inventee] A_DIAGONALISABLE | hypothese_inventee |
| 36 | Règle de L'Hôpital | f et g sont dérivables au voisinage de a; g'(x) ≠ 0 au voisi... | f et g sont dérivables au voisinage de a; g'(x) ≠ 0 au voisi... | FAUX | manquante: f(a) = g(a) = 0 ou f et g ten... | hypothese_manquante |
| 37 | Projection orthogonale (Hilbert) | F est un sous-espace vectoriel de E (sans fermé); F est un s... | E est un espace de Hilbert; F est un sous-espace vectoriel f... | FAUX | hypothese_inventee: E est un espace de H... | hypothese_inventee |
| 38 | Règle de L'Hôpital | f et g sont dérivables au voisinage de a; g'(x) ≠ 0 au voisi... | f et g sont dérivables au voisinage de a; g'(x) ≠ 0 au voisi... | FAUX | manquante: lim_{x→a} f'(x)/g'(x) = ℓ existe | hypothese_manquante |
| 39 | Théorème de la base incomplète | F = (f₁, ..., fₖ) est une famille libre de E avec k ≤ n | E est un espace vectoriel de dimension finie n; F = (f₁, ...... | FAUX | manquante: E est un espace vectoriel de ... | hypothese_manquante |
| 40 | Inégalité de Cauchy-Schwarz | E est un espace vectoriel muni d'un produit scalaire; u et v... | E est un espace vectoriel muni d'un produit scalaire; u et v... | VRAI | OK | correcte |
| 41 | Théorème de Cauchy-Lipschitz | f est continue en t; f est lipschitzienne en y; f est contin... | f est continue en t; f est lipschitzienne en y; une conditio... | FAUX | hypothese_inventee: une condition initia... | hypothese_inventee |
| 42 | Règle de L'Hôpital | f et g sont dérivables au voisinage de a; g'(x) ≠ 0 au voisi... | f et g sont dérivables au voisinage de a; g'(x) ≠ 0 au voisi... | FAUX | inventee: [inventee] FG_CONTINUES_EN_A | hypothese_inventee |
| 43 | Théorème de Cayley-Hamilton | χ_A est le polynôme caractéristique de A | A est une matrice carrée n×n; χ_A est le polynôme caractéris... | FAUX | manquante: A est une matrice carrée n×n | hypothese_manquante |
| 44 | Théorème de convergence dominée | (fₙ) est une suite de fonctions mesurables | (fₙ) est une suite de fonctions mesurables; fₙ → f presque p... | FAUX | manquante: ∃ g intégrable telle que |fₙ|... | plusieurs_manquantes |
| 45 | Théorème de Heine (continuité uniforme) | [a, b] est un intervalle fermé et borné | f est continue sur [a, b]; [a, b] est un intervalle fermé et... | FAUX | manquante: f est continue sur [a, b] | hypothese_manquante |
| 46 | Critère de Cauchy (suites) | (uₙ) est une suite dans un espace complet; (uₙ) est une suit... | (uₙ) est une suite dans un espace complet | FAUX | inventee: [inventee] UN_MONOTONE | hypothese_inventee |
| 47 | Règle de L'Hôpital | f et g sont dérivables au voisinage de a; g'(x) ≠ 0 au voisi... | f et g sont dérivables au voisinage de a; g'(x) ≠ 0 au voisi... | VRAI | OK | correcte |
| 48 | Théorème de Bolzano-Weierstrass | (uₙ) est une suite bornée de réels; (uₙ) est une suite de Ca... | (uₙ) est une suite bornée de réels | FAUX | inventee: [inventee] UN_CAUCHY | hypothese_inventee |
| 49 | Théorème Central Limite | (Xₙ) est une suite de variables aléatoires indépendantes; le... | (Xₙ) est une suite de variables aléatoires indépendantes; le... | FAUX | inventee: [inventee] XN_INDEP_SANS_IID | hypothese_inventee |
| 50 | Théorème de Weierstrass | f est continue sur ]a, b[; [a, b] est un intervalle fermé et... | f est continue sur [a, b]; [a, b] est un intervalle fermé et... | FAUX | hypothese_inventee: f est continue sur [... | hypothese_inventee |
| 51 | Théorème des Accroissements Finis (Lagrange) | f est continue sur ]a, b[; f est dérivable sur ]a, b[ | f est continue sur [a, b]; f est dérivable sur ]a, b[ | FAUX | hypothese_inventee: f est continue sur [... | hypothese_inventee |
| 52 | Théorème spectral (matrices symétriques réelles) | A est une matrice carrée réelle | A est une matrice carrée réelle; A est symétrique (A = Aᵀ) | FAUX | manquante: A est symétrique (A = Aᵀ) | hypothese_manquante |
| 53 | Théorème spectral (matrices symétriques réelles) | A est symétrique (A = Aᵀ) | A est une matrice carrée réelle; A est symétrique (A = Aᵀ) | FAUX | manquante: A est une matrice carrée réelle | hypothese_manquante |
| 54 | Théorème Fondamental de l'Analyse | f est de classe C¹ sur I | f est continue sur [a, b] | VRAI | OK | hypothese_inventee |
| 55 | Théorème de Rolle | f est continue sur ]a, b[; f est dérivable sur ]a, b[; f(a) ... | f est continue sur [a, b]; f est dérivable sur ]a, b[; f(a) ... | FAUX | hypothese_inventee: f est continue sur [... | hypothese_inventee |
| 56 | Critère de Cauchy (suites) | (uₙ) est une suite dans un espace complet; (uₙ) est bornée | (uₙ) est une suite dans un espace complet | FAUX | inventee: [inventee] UN_BORNEE | hypothese_inventee |
| 57 | Critère de d'Alembert (séries) | lim_{n→∞} u_{n+1}/uₙ = ℓ existe | uₙ > 0 pour tout n suffisamment grand; lim_{n→∞} u_{n+1}/uₙ ... | FAUX | manquante: uₙ > 0 pour tout n suffisamme... | hypothese_manquante |
| 58 | Théorème des Accroissements Finis (Lagrange) | f est continue sur [a, b]; f est dérivable sur ]a, b[ | f est continue sur [a, b]; f est dérivable sur ]a, b[ | VRAI | OK | correcte |
| 59 | Théorème de Bolzano-Weierstrass | (uₙ) est une suite bornée de réels; (uₙ) est une suite crois... | (uₙ) est une suite bornée de réels | FAUX | inventee: [inventee] UN_CROISSANTE | hypothese_inventee |
| 60 | Inégalité de Jensen | X est une variable aléatoire réelle intégrable | φ est une fonction convexe; X est une variable aléatoire rée... | FAUX | manquante: φ est une fonction convexe | hypothese_manquante |
| 61 | Théorème du rang | f est une application linéaire de E vers F; E est un espace ... | f est une application linéaire de E vers F; E est un espace ... | VRAI | OK | correcte |
| 62 | Diagonalisabilité (valeurs propres distinctes) | f est un endomorphisme de E (dim finie n) | f est un endomorphisme de E (dim finie n); f admet n valeurs... | FAUX | manquante: f admet n valeurs propres dis... | hypothese_manquante |
| 63 | Théorème de Rolle | f est dérivable en a et b; f est dérivable sur ]a, b[; f(a) ... | f est continue sur [a, b]; f est dérivable sur ]a, b[; f(a) ... | FAUX | hypothese_inventee: f est continue sur [... | hypothese_inventee |
| 64 | Changement de variable dans une intégrale | φ est de classe C¹ sur [α, β] | φ est de classe C¹ sur [α, β]; f est continue sur φ([α, β]) | FAUX | manquante: f est continue sur φ([α, β]) | hypothese_manquante |
| 65 | Théorème de la base incomplète | E est un espace vectoriel de dimension finie n; F = (f₁, ...... | E est un espace vectoriel de dimension finie n; F = (f₁, ...... | VRAI | OK | correcte |
| 66 | Critère de d'Alembert (séries) | uₙ > 0 pour tout n suffisamment grand; lim_{n→∞} u_{n+1}/uₙ ... | uₙ > 0 pour tout n suffisamment grand; lim_{n→∞} u_{n+1}/uₙ ... | VRAI | OK | correcte |
| 67 | Règle de L'Hôpital | f et g sont dérivables au voisinage de a | f et g sont dérivables au voisinage de a; g'(x) ≠ 0 au voisi... | FAUX | manquante: lim_{x→a} f'(x)/g'(x) = ℓ exi... | plusieurs_manquantes |
| 68 | Théorème des Valeurs Intermédiaires | f est continue sur ]a, b[; y est compris entre f(a) et f(b) | f est continue sur [a, b]; y est compris entre f(a) et f(b) | FAUX | hypothese_inventee: f est continue sur [... | hypothese_inventee |
| 69 | Théorème du rang | f est une application linéaire de E vers F | f est une application linéaire de E vers F; E est un espace ... | FAUX | manquante: E est un espace vectoriel de ... | hypothese_manquante |
| 70 | Loi des Grands Nombres (faible) | E[|X₁|] est finie | (Xₙ) est une suite de variables aléatoires indépendantes; le... | FAUX | manquante: (Xₙ) est une suite de variabl... | plusieurs_manquantes |
| 71 | Réduction de Jordan (existence) | A est une matrice carrée n×n à coefficients complexes; A est... | A est une matrice carrée n×n à coefficients complexes | FAUX | inventee: [inventee] A_MATRICE_REELLE | hypothese_inventee |
| 72 | Réduction de Jordan (existence) | le polynôme caractéristique de A est scindé sur ℝ | A est une matrice carrée n×n à coefficients complexes | FAUX | hypothese_inventee: A est une matrice ca... | hypothese_inventee |
| 73 | Théorème Central Limite | (Xₙ) est une suite de variables aléatoires indépendantes; le... | (Xₙ) est une suite de variables aléatoires indépendantes; le... | FAUX | inventee: [inventee] SIGMA2_POSITIF_SANS... | hypothese_inventee |
| 74 | Inégalité de Jensen | φ est une fonction convexe; X est une variable aléatoire rée... | φ est une fonction convexe; X est une variable aléatoire rée... | FAUX | inventee: [inventee] PHI_CONCAVE | hypothese_inventee |
| 75 | Théorème de Rolle | f est continue sur [a, b]; f(a) = f(b) | f est continue sur [a, b]; f est dérivable sur ]a, b[; f(a) ... | FAUX | manquante: f est dérivable sur ]a, b[ | hypothese_manquante |
| 76 | Principe de superposition (EDO linéaires) | L est un opérateur différentiel linéaire | L est un opérateur différentiel linéaire; y₁ est solution de... | FAUX | manquante: y₂ est solution de L(y) = f₂;... | plusieurs_manquantes |
| 77 | Théorème de Cauchy-Lipschitz | f est lipschitzienne en y | f est continue en t; f est lipschitzienne en y; une conditio... | FAUX | manquante: f est continue en t; manquant... | plusieurs_manquantes |
| 78 | Théorème des Accroissements Finis (Lagrange) | f est dérivable sur [a, b]; f est dérivable sur ]a, b[ | f est continue sur [a, b]; f est dérivable sur ]a, b[ | VRAI | OK | hypothese_inventee |
| 79 | Théorème de Cauchy-Lipschitz | f est continue en t | f est continue en t; f est lipschitzienne en y; une conditio... | FAUX | manquante: f est lipschitzienne en y; ma... | plusieurs_manquantes |
| 80 | Théorème de Cayley-Hamilton | A est une matrice carrée n×n; χ_A est le polynôme caractéris... | A est une matrice carrée n×n; χ_A est le polynôme caractéris... | FAUX | inventee: [inventee] A_SYMETRIQUE | hypothese_inventee |
| 81 | Théorème Fondamental de l'Analyse | f est continue sur ]a, b[ | f est continue sur [a, b] | FAUX | hypothese_inventee: f est continue sur [... | hypothese_inventee |
| 82 | Projection orthogonale (Hilbert) | E est un espace de Hilbert; F est un sous-espace vectoriel f... | E est un espace de Hilbert; F est un sous-espace vectoriel f... | FAUX | inventee: [inventee] F_DIM_FINIE | hypothese_inventee |
| 83 | Loi des Grands Nombres (faible) | (Xₙ) est une suite de variables aléatoires indépendantes; le... | (Xₙ) est une suite de variables aléatoires indépendantes; le... | FAUX | manquante: E[|X₁|] est finie | hypothese_manquante |
| 84 | Théorème spectral (matrices symétriques réelles) | A est une matrice carrée réelle; A est symétrique (A = Aᵀ); ... | A est une matrice carrée réelle; A est symétrique (A = Aᵀ) | FAUX | inventee: [inventee] A_ORTHOGONALE | hypothese_inventee |
| 85 | Diagonalisabilité (valeurs propres distinctes) | f admet n valeurs propres distinctes | f est un endomorphisme de E (dim finie n); f admet n valeurs... | FAUX | manquante: f est un endomorphisme de E (... | hypothese_manquante |
| 86 | Principe de superposition (EDO linéaires) | L est un opérateur différentiel linéaire; y₁ est solution de... | L est un opérateur différentiel linéaire; y₁ est solution de... | FAUX | inventee: [inventee] Y1_Y2_SOLUTIONS_HOM... | hypothese_inventee |
| 87 | Inégalité de Cauchy-Schwarz | E est un espace vectoriel muni d'un produit scalaire | E est un espace vectoriel muni d'un produit scalaire; u et v... | FAUX | manquante: u et v sont deux vecteurs de E | hypothese_manquante |
| 88 | Intégration par parties | u et v sont de classe C¹ sur [a, b]; u' et v sont continues ... | u et v sont de classe C¹ sur [a, b] | FAUX | inventee: [inventee] UPRIME_V_CONTINUES_... | hypothese_inventee |
| 89 | Diagonalisabilité (valeurs propres distinctes) | f est un endomorphisme de E (dim finie n); le polynôme carac... | f est un endomorphisme de E (dim finie n); f admet n valeurs... | FAUX | hypothese_inventee: f admet n valeurs pr... | hypothese_inventee |
| 90 | Principe de superposition (EDO linéaires) | L est un opérateur différentiel linéaire; y₁ est solution de... | L est un opérateur différentiel linéaire; y₁ est solution de... | VRAI | OK | correcte |
| 91 | Théorème de Cayley-Hamilton | A est une matrice carrée n×n; χ_A est le polynôme minimal de A | A est une matrice carrée n×n; χ_A est le polynôme caractéris... | FAUX | hypothese_inventee: χ_A est le polynôme ... | hypothese_inventee |
| 92 | Critère de Cauchy (suites) | (uₙ) est une suite dans un espace complet; (uₙ) est dans un ... | (uₙ) est une suite dans un espace complet | FAUX | inventee: [inventee] UN_ESPACE_NORME_SAN... | hypothese_inventee |
| 93 | Formule de Taylor avec reste de Lagrange | f est n+1 fois dérivable sur ]a, b[ | f est n fois dérivable sur [a, b] (continue); f est n+1 fois... | FAUX | manquante: f est n fois dérivable sur [a... | hypothese_manquante |
| 94 | Formule de Taylor avec reste de Lagrange | f est analytique; f est n+1 fois dérivable sur ]a, b[ | f est n fois dérivable sur [a, b] (continue); f est n+1 fois... | FAUX | hypothese_inventee: f est n fois dérivab... | hypothese_inventee |
| 95 | Règle de L'Hôpital | f et g sont dérivables au voisinage de a; f et g sont contin... | f et g sont dérivables au voisinage de a; g'(x) ≠ 0 au voisi... | FAUX | hypothese_inventee: g'(x) ≠ 0 au voisina... | hypothese_inventee |
| 96 | Théorème de convergence dominée | fₙ → f presque partout | (fₙ) est une suite de fonctions mesurables; fₙ → f presque p... | FAUX | manquante: ∃ g intégrable telle que |fₙ|... | plusieurs_manquantes |
| 97 | Principe de superposition (EDO linéaires) | L est un opérateur différentiel linéaire; y₂ est solution de... | L est un opérateur différentiel linéaire; y₁ est solution de... | FAUX | manquante: y₁ est solution de L(y) = f₁ | hypothese_manquante |
| 98 | Théorème de Rolle | f(a) = f(b) | f est continue sur [a, b]; f est dérivable sur ]a, b[; f(a) ... | FAUX | manquante: f est dérivable sur ]a, b[; m... | plusieurs_manquantes |
| 99 | Théorème de convergence dominée | fₙ → f presque partout; ∃ g intégrable telle que |fₙ| ≤ g p.... | (fₙ) est une suite de fonctions mesurables; fₙ → f presque p... | FAUX | manquante: (fₙ) est une suite de fonctio... | hypothese_manquante |
| 100 | Théorème des suites adjacentes | (uₙ) est croissante et (vₙ) est décroissante; vₙ − uₙ → 0; u... | (uₙ) est croissante et (vₙ) est décroissante; vₙ − uₙ → 0 | FAUX | inventee: [inventee] UN_LEQ_VN | hypothese_inventee |
