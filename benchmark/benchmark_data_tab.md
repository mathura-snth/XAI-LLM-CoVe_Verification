# Benchmark des théorèmes mathématiques

**Total:** 100 copies

**Correctes:** 52

**Fausses:** 48

## Détail des copies

| # | Théorème | Copie | Attendu | Verdict | Raison | Type_erreur |
|---|----------|-------|---------|---------|--------|-------------|
| 1 | Théorème des suites adjacentes | vₙ − uₙ → 0 | (uₙ) est croissante et (vₙ) est décroissante; vₙ − uₙ → 0 | FAUX | manquante: (uₙ) est croissante et (vₙ) e... | hypothese_manquante |
| 2 | Théorème de Cauchy-Lipschitz | f est continue en t; f est lipschitzienne en y; une conditio... | f est continue en t; f est lipschitzienne en y; une conditio... | FAUX | inventee: [inventee] F_CONTINUE_EN_Y | hypothese_inventee |
| 3 | Intégration par parties | u et v sont de classe C¹ sur [a, b] | u et v sont de classe C¹ sur [a, b] | VRAI | OK | correcte |
| 4 | Théorème de Cauchy-Lipschitz | f est continue en t; f est lipschitzienne en y | f est continue en t; f est lipschitzienne en y; une conditio... | FAUX | manquante: une condition initiale y(t₀) ... | hypothese_manquante |
| 5 | Théorème de Cauchy-Lipschitz | f est continue en t; f est lipschitzienne en y | f est continue en t; f est lipschitzienne en y; une conditio... | FAUX | manquante: une condition initiale y(t₀) ... | hypothese_manquante |
| 6 | Théorème de Cayley-Hamilton | A est une matrice carrée n×n; χ_A est le polynôme caractéris... | A est une matrice carrée n×n; χ_A est le polynôme caractéris... | VRAI | OK | correcte |
| 7 | Théorème de Rolle | f est dérivable sur ]a, b[; f(a) = f(b) | f est continue sur [a, b]; f est dérivable sur ]a, b[; f(a) ... | FAUX | manquante: f est continue sur [a, b] | hypothese_manquante |
| 8 | Intégration par parties | u et v sont de classe C¹ sur [a, b] | u et v sont de classe C¹ sur [a, b] | VRAI | OK | correcte |
| 9 | Théorème de Heine (continuité uniforme) | f est continue sur [a, b]; f est continue sur ]a, b[ | f est continue sur [a, b]; [a, b] est un intervalle fermé et... | FAUX | mal_formulee: [a, b] est un intervalle f... | hypothese_mal_formulee |
| 10 | Théorème spectral (matrices symétriques réelles) | A est une matrice carrée réelle; A est symétrique (A = Aᵀ); ... | A est une matrice carrée réelle; A est symétrique (A = Aᵀ) | FAUX | inventee: [inventee] A_MATRICE_COMPLEXE | hypothese_inventee |
| 11 | Principe de superposition (EDO linéaires) | L est un opérateur différentiel linéaire | L est un opérateur différentiel linéaire; y₁ est solution de... | FAUX | manquante: y₂ est solution de L(y) = f₂;... | plusieurs_manquantes |
| 12 | Règle de L'Hôpital | f et g sont dérivables au voisinage de a; g'(x) ≠ 0 au voisi... | f et g sont dérivables au voisinage de a; g'(x) ≠ 0 au voisi... | FAUX | mal_formulee: f(a) = g(a) = 0 ou f et g ... | hypothese_mal_formulee |
| 13 | Théorème des Valeurs Intermédiaires | f est dérivable sur [a, b]; y est compris entre f(a) et f(b) | f est continue sur [a, b]; y est compris entre f(a) et f(b) | VRAI | OK | implication_valide |
| 14 | Théorème de Weierstrass | f est continue sur ]a, b[; [a, b] est un intervalle fermé et... | f est continue sur [a, b]; [a, b] est un intervalle fermé et... | FAUX | mal_formulee: f est continue sur [a, b] | intervalle_errone |
| 15 | Inégalité de Jensen | φ est une fonction convexe; X est une variable aléatoire rée... | φ est une fonction convexe; X est une variable aléatoire rée... | VRAI | OK | correcte |
| 16 | Théorème de convergence monotone (suites) | (uₙ) est une suite croissante; (uₙ) est majorée; (uₙ) est un... | (uₙ) est une suite croissante; (uₙ) est majorée | FAUX | inventee: [inventee] UN_DECROISSANTE_MAJ... | hypothese_inventee |
| 17 | Théorème de Cauchy-Lipschitz | f est continue en t; f est lipschitzienne en y; une conditio... | f est continue en t; f est lipschitzienne en y; une conditio... | VRAI | OK | implication_invalide |
| 18 | Théorème de Heine (continuité uniforme) | f est continue sur [a, b] | f est continue sur [a, b]; [a, b] est un intervalle fermé et... | FAUX | manquante: [a, b] est un intervalle ferm... | hypothese_manquante |
| 19 | Théorème des Valeurs Intermédiaires | f est continue sur [a, b]; y est compris entre f(a) et f(b);... | f est continue sur [a, b]; y est compris entre f(a) et f(b) | FAUX | inventee: [inventee] SIGNES_OPPOSES | hypothese_inventee |
| 20 | Théorème de convergence monotone (suites) | (uₙ) est une suite croissante; (uₙ) est majorée | (uₙ) est une suite croissante; (uₙ) est majorée | VRAI | OK | correcte |
| 21 | Théorème de Bolzano-Weierstrass | (uₙ) est une suite croissante | (uₙ) est une suite bornée de réels | FAUX | mal_formulee: (uₙ) est une suite bornée ... | hypothese_mal_formulee |
| 22 | Critère de Cauchy (suites) | (uₙ) est bornée | (uₙ) est une suite dans un espace complet | FAUX | mal_formulee: (uₙ) est une suite dans un... | hypothese_mal_formulee |
| 23 | Inégalité de Jensen | X est bornée; X est une variable aléatoire réelle intégrable | φ est une fonction convexe; X est une variable aléatoire rée... | FAUX | mal_formulee: φ est une fonction convexe | hypothese_mal_formulee |
| 24 | Changement de variable dans une intégrale | φ est de classe C¹ sur [α, β]; f est continue sur φ([α, β]) | φ est de classe C¹ sur [α, β]; f est continue sur φ([α, β]) | VRAI | OK | implication_invalide |
| 25 | Théorème des suites adjacentes | (uₙ) est croissante et (vₙ) est décroissante; vₙ − uₙ → 0 | (uₙ) est croissante et (vₙ) est décroissante; vₙ − uₙ → 0 | VRAI | OK | correcte |
| 26 | Formule de Taylor-Young | f est n fois dérivable en a | f est n fois dérivable en a | VRAI | OK | correcte |
| 27 | Théorème de la base incomplète | E est un espace vectoriel de dimension finie n; F est une ba... | E est un espace vectoriel de dimension finie n; F = (f₁, ...... | VRAI | OK | hypothese_mal_formulee |
| 28 | Formule de Taylor avec reste de Lagrange | f est n+1 fois dérivable sur ]a, b[ | f est n fois dérivable sur [a, b] (continue); f est n+1 fois... | FAUX | manquante: f est n fois dérivable sur [a... | hypothese_manquante |
| 29 | Théorème de Heine (continuité uniforme) | f est lipschitzienne sur [a, b]; [a, b] est un intervalle fe... | f est continue sur [a, b]; [a, b] est un intervalle fermé et... | VRAI | OK | hypothese_mal_formulee |
| 30 | Diagonalisabilité (valeurs propres distinctes) | f est un endomorphisme de E (dim finie n); f admet n valeurs... | f est un endomorphisme de E (dim finie n); f admet n valeurs... | FAUX | inventee: [inventee] F_MATRICE_TRIANGULAIRE | hypothese_inventee |
| 31 | Théorème de convergence dominée | (fₙ) est une suite de fonctions mesurables; fₙ → f presque p... | (fₙ) est une suite de fonctions mesurables; fₙ → f presque p... | FAUX | mal_formulee: ∃ g intégrable telle que |... | hypothese_mal_formulee |
| 32 | Loi des Grands Nombres (faible) | (Xₙ) est une suite de variables aléatoires indépendantes; le... | (Xₙ) est une suite de variables aléatoires indépendantes; le... | VRAI | OK | correcte |
| 33 | Intégration par parties | u et v sont de classe C¹ sur [a, b] | u et v sont de classe C¹ sur [a, b] | VRAI | OK | correcte |
| 34 | Théorème Central Limite | (Xₙ) est une suite de variables aléatoires indépendantes; le... | (Xₙ) est une suite de variables aléatoires indépendantes; le... | VRAI | OK | correcte |
| 35 | Diagonalisabilité (valeurs propres distinctes) | f est un endomorphisme de E (dim finie n); f admet n valeurs... | f est un endomorphisme de E (dim finie n); f admet n valeurs... | FAUX | inventee: [inventee] F_N_VP_NON_DISTINCTES | hypothese_inventee |
| 36 | Théorème Fondamental de l'Analyse | f est continue sur ]a, b[ | f est continue sur [a, b] | FAUX | mal_formulee: f est continue sur [a, b] | intervalle_errone |
| 37 | Théorème Fondamental de l'Analyse | f est continue sur ]a, b[ | f est continue sur [a, b] | FAUX | implication_invalide: f est continue sur... | implication_invalide |
| 38 | Diagonalisabilité (valeurs propres distinctes) | f est un endomorphisme de E (dim finie n); f admet n valeurs... | f est un endomorphisme de E (dim finie n); f admet n valeurs... | VRAI | OK | implication_invalide |
| 39 | Règle de L'Hôpital | f et g sont dérivables au voisinage de a; g'(x) ≠ 0 au voisi... | f et g sont dérivables au voisinage de a; g'(x) ≠ 0 au voisi... | FAUX | inventee: [inventee] G_NON_NULLE_VOIS_A | hypothese_inventee |
| 40 | Intégration par parties | u et v sont de classe C¹ sur [a, b]; u' et v sont continues ... | u et v sont de classe C¹ sur [a, b] | FAUX | inventee: [inventee] UPRIME_V_CONTINUES_... | hypothese_inventee |
| 41 | Théorème de Bolzano-Weierstrass | (uₙ) est une suite bornée de réels | (uₙ) est une suite bornée de réels | VRAI | OK | implication_valide |
| 42 | Réduction de Jordan (existence) | A est une matrice carrée n×n à coefficients complexes | A est une matrice carrée n×n à coefficients complexes | VRAI | OK | implication_valide |
| 43 | Théorème de la base incomplète | F est une base de E; F = (f₁, ..., fₖ) est une famille libre... | E est un espace vectoriel de dimension finie n; F = (f₁, ...... | FAUX | mal_formulee: E est un espace vectoriel ... | hypothese_mal_formulee |
| 44 | Inégalité de Cauchy-Schwarz | u et v sont deux vecteurs de E | E est un espace vectoriel muni d'un produit scalaire; u et v... | FAUX | manquante: E est un espace vectoriel mun... | hypothese_manquante |
| 45 | Inégalité de Jensen | X est une variable aléatoire réelle intégrable | φ est une fonction convexe; X est une variable aléatoire rée... | FAUX | manquante: φ est une fonction convexe | hypothese_manquante |
| 46 | Théorème des suites adjacentes | (uₙ) est croissante et (vₙ) est décroissante; vₙ − uₙ → 0 | (uₙ) est croissante et (vₙ) est décroissante; vₙ − uₙ → 0 | VRAI | OK | correcte |
| 47 | Théorème Central Limite | (Xₙ) est une suite de variables aléatoires indépendantes; le... | (Xₙ) est une suite de variables aléatoires indépendantes; le... | VRAI | OK | implication_valide |
| 48 | Théorème de convergence monotone (suites) | (uₙ) est une suite croissante | (uₙ) est une suite croissante; (uₙ) est majorée | FAUX | manquante: (uₙ) est majorée | hypothese_manquante |
| 49 | Diagonalisabilité (valeurs propres distinctes) | f est un endomorphisme de E (dim finie n); f admet n valeurs... | f est un endomorphisme de E (dim finie n); f admet n valeurs... | VRAI | OK | implication_invalide |
| 50 | Projection orthogonale (Hilbert) | E est un espace de Hilbert; F est un sous-espace vectoriel f... | E est un espace de Hilbert; F est un sous-espace vectoriel f... | FAUX | inventee: [inventee] F_DIM_FINIE | hypothese_inventee |
| 51 | Inégalité de Jensen | φ est une fonction convexe; X est une variable aléatoire rée... | φ est une fonction convexe; X est une variable aléatoire rée... | VRAI | OK | correcte |
| 52 | Critère de Cauchy (suites) | (uₙ) est une suite dans un espace complet | (uₙ) est une suite dans un espace complet | VRAI | OK | correcte |
| 53 | Critère de Cauchy (suites) | (uₙ) est une suite dans un espace complet; (uₙ) est une suit... | (uₙ) est une suite dans un espace complet | FAUX | inventee: [inventee] UN_MONOTONE | hypothese_inventee |
| 54 | Théorème du rang | f est une application linéaire de E vers F | f est une application linéaire de E vers F; E est un espace ... | FAUX | manquante: E est un espace vectoriel de ... | hypothese_manquante |
| 55 | Théorème de Cayley-Hamilton | A est une matrice carrée n×n; χ_A est le polynôme caractéris... | A est une matrice carrée n×n; χ_A est le polynôme caractéris... | VRAI | OK | correcte |
| 56 | Théorème spectral (matrices symétriques réelles) | A est une matrice carrée réelle; A est symétrique (A = Aᵀ) | A est une matrice carrée réelle; A est symétrique (A = Aᵀ) | VRAI | OK | correcte |
| 57 | Théorème de Cauchy-Lipschitz | f est continue en t; f est lipschitzienne en y; une conditio... | f est continue en t; f est lipschitzienne en y; une conditio... | FAUX | inventee: [inventee] F_BORNEE | hypothese_inventee |
| 58 | Principe de superposition (EDO linéaires) | L est un opérateur différentiel linéaire | L est un opérateur différentiel linéaire; y₁ est solution de... | FAUX | manquante: y₂ est solution de L(y) = f₂;... | plusieurs_manquantes |
| 59 | Loi des Grands Nombres (faible) | les Xₙ sont indépendantes uniquement; les Xₙ sont identiquem... | (Xₙ) est une suite de variables aléatoires indépendantes; le... | VRAI | OK | hypothese_mal_formulee |
| 60 | Principe de superposition (EDO linéaires) | L est un opérateur différentiel linéaire | L est un opérateur différentiel linéaire; y₁ est solution de... | FAUX | manquante: y₂ est solution de L(y) = f₂;... | plusieurs_manquantes |
| 61 | Inégalité de Cauchy-Schwarz | E est un espace vectoriel muni d'un produit scalaire; u et v... | E est un espace vectoriel muni d'un produit scalaire; u et v... | VRAI | OK | correcte |
| 62 | Théorème de Weierstrass | f est continue sur ]a, b[; [a, b] est un intervalle fermé et... | f est continue sur [a, b]; [a, b] est un intervalle fermé et... | FAUX | mal_formulee: f est continue sur [a, b] | intervalle_errone |
| 63 | Réduction de Jordan (existence) | A est une matrice carrée n×n à coefficients complexes; A est... | A est une matrice carrée n×n à coefficients complexes | FAUX | inventee: [inventee] A_MATRICE_REELLE | hypothese_inventee |
| 64 | Théorème des Accroissements Finis (Lagrange) | f est continue sur ]a, b[; f est dérivable sur ]a, b[ | f est continue sur [a, b]; f est dérivable sur ]a, b[ | FAUX | mal_formulee: f est continue sur [a, b] | hypothese_mal_formulee |
| 65 | Théorème de Cauchy-Lipschitz | f est continue en t; f est lipschitzienne en y; une conditio... | f est continue en t; f est lipschitzienne en y; une conditio... | VRAI | OK | implication_invalide |
| 66 | Loi des Grands Nombres (faible) | (Xₙ) est une suite de variables aléatoires indépendantes; le... | (Xₙ) est une suite de variables aléatoires indépendantes; le... | FAUX | manquante: E[|X₁|] est finie | hypothese_manquante |
| 67 | Principe de superposition (EDO linéaires) | L est un opérateur différentiel linéaire | L est un opérateur différentiel linéaire; y₁ est solution de... | FAUX | manquante: y₂ est solution de L(y) = f₂;... | plusieurs_manquantes |
| 68 | Théorème de Heine (continuité uniforme) | f est continue sur [a, b]; [a, b] est un intervalle fermé et... | f est continue sur [a, b]; [a, b] est un intervalle fermé et... | VRAI | OK | correcte |
| 69 | Changement de variable dans une intégrale | φ est de classe C¹ sur [α, β]; f est continue sur φ([α, β]) | φ est de classe C¹ sur [α, β]; f est continue sur φ([α, β]) | VRAI | OK | implication_valide |
| 70 | Théorème Fondamental de l'Analyse | f est de classe C¹ sur I | f est continue sur [a, b] | FAUX | mal_formulee: f est continue sur [a, b] | hypothese_mal_formulee |
| 71 | Critère de Cauchy (suites) | (uₙ) est une suite dans un espace complet | (uₙ) est une suite dans un espace complet | VRAI | OK | correcte |
| 72 | Théorème spectral (matrices symétriques réelles) | A est une matrice carrée réelle; A est symétrique (A = Aᵀ) | A est une matrice carrée réelle; A est symétrique (A = Aᵀ) | VRAI | OK | implication_invalide |
| 73 | Théorème de Weierstrass | f est continue sur ]a, b[; [a, b] est un intervalle fermé et... | f est continue sur [a, b]; [a, b] est un intervalle fermé et... | FAUX | mal_formulee: f est continue sur [a, b] | hypothese_mal_formulee |
| 74 | Théorème du rang | f est une application linéaire de E vers F; E est un espace ... | f est une application linéaire de E vers F; E est un espace ... | VRAI | OK | correcte |
| 75 | Théorème de Bolzano-Weierstrass | (uₙ) est une suite croissante | (uₙ) est une suite bornée de réels | FAUX | mal_formulee: (uₙ) est une suite bornée ... | hypothese_mal_formulee |
| 76 | Théorème des Valeurs Intermédiaires | f est continue sur [a, b]; y est compris entre f(a) et f(b) | f est continue sur [a, b]; y est compris entre f(a) et f(b) | VRAI | OK | correcte |
| 77 | Intégration par parties | u et v sont de classe C¹ sur [a, b] | u et v sont de classe C¹ sur [a, b] | VRAI | OK | correcte |
| 78 | Réduction de Jordan (existence) | A est une matrice carrée n×n à coefficients complexes | A est une matrice carrée n×n à coefficients complexes | VRAI | OK | correcte |
| 79 | Inégalité de Jensen | φ est une fonction convexe; X est une variable aléatoire rée... | φ est une fonction convexe; X est une variable aléatoire rée... | VRAI | OK | correcte |
| 80 | Théorème des Valeurs Intermédiaires | f est continue sur [a, b]; f(a) et f(b) sont de signes stric... | f est continue sur [a, b]; y est compris entre f(a) et f(b) | FAUX | mal_formulee: y est compris entre f(a) e... | hypothese_mal_formulee |
| 81 | Inégalité de Cauchy-Schwarz | E est un espace vectoriel de dimension finie n; u et v sont ... | E est un espace vectoriel muni d'un produit scalaire; u et v... | FAUX | mal_formulee: E est un espace vectoriel ... | hypothese_mal_formulee |
| 82 | Formule de Taylor avec reste de Lagrange | f est de classe Cⁿ uniquement; f est n+1 fois dérivable sur ... | f est n fois dérivable sur [a, b] (continue); f est n+1 fois... | FAUX | implication_invalide: f est n fois dériv... | implication_invalide |
| 83 | Intégration par parties | u et v sont de classe C¹ sur [a, b] | u et v sont de classe C¹ sur [a, b] | VRAI | OK | implication_invalide |
| 84 | Théorème Central Limite | (Xₙ) est une suite de variables aléatoires indépendantes; le... | (Xₙ) est une suite de variables aléatoires indépendantes; le... | VRAI | OK | implication_valide |
| 85 | Théorème Fondamental de l'Analyse | f est continue sur [a, b] | f est continue sur [a, b] | VRAI | OK | correcte |
| 86 | Théorème de Weierstrass | f est dérivable sur [a, b]; [a, b] est un intervalle fermé e... | f est continue sur [a, b]; [a, b] est un intervalle fermé et... | VRAI | OK | implication_valide |
| 87 | Théorème de la base incomplète | E est un espace vectoriel de dimension finie n; F est une ba... | E est un espace vectoriel de dimension finie n; F = (f₁, ...... | VRAI | OK | implication_valide |
| 88 | Théorème de Cayley-Hamilton | A est une matrice carrée n×n; χ_A est le polynôme caractéris... | A est une matrice carrée n×n; χ_A est le polynôme caractéris... | VRAI | OK | implication_invalide |
| 89 | Inégalité de Jensen | φ est une fonction convexe; X est une variable aléatoire rée... | φ est une fonction convexe; X est une variable aléatoire rée... | VRAI | OK | correcte |
| 90 | Critère de Cauchy (suites) | (uₙ) est une suite dans un espace complet | (uₙ) est une suite dans un espace complet | VRAI | OK | correcte |
| 91 | Théorème des Accroissements Finis (Lagrange) | f est continue sur [a, b]; f est dérivable sur [a, b] | f est continue sur [a, b]; f est dérivable sur ]a, b[ | VRAI | OK | implication_valide |
| 92 | Théorème de Cauchy-Lipschitz | f est continue en t; f est lipschitzienne en y; une conditio... | f est continue en t; f est lipschitzienne en y; une conditio... | VRAI | OK | correcte |
| 93 | Théorème Central Limite | (Xₙ) est une suite de variables aléatoires indépendantes; E[... | (Xₙ) est une suite de variables aléatoires indépendantes; le... | FAUX | manquante: les Xₙ sont identiquement dis... | hypothese_manquante |
| 94 | Théorème Fondamental de l'Analyse | f est intégrable sur [a, b] | f est continue sur [a, b] | FAUX | mal_formulee: f est continue sur [a, b] | hypothese_mal_formulee |
| 95 | Théorème de Cayley-Hamilton | A est une matrice carrée n×n; χ_A est le polynôme caractéris... | A est une matrice carrée n×n; χ_A est le polynôme caractéris... | VRAI | OK | correcte |
| 96 | Changement de variable dans une intégrale | φ est de classe C¹ sur [α, β]; f est continue sur φ([α, β]) | φ est de classe C¹ sur [α, β]; f est continue sur φ([α, β]) | VRAI | OK | implication_invalide |
| 97 | Intégration par parties | u et v sont de classe C¹ sur [a, b] | u et v sont de classe C¹ sur [a, b] | VRAI | OK | correcte |
| 98 | Théorème spectral (matrices symétriques réelles) | A est symétrique (A = Aᵀ) | A est une matrice carrée réelle; A est symétrique (A = Aᵀ) | FAUX | manquante: A est une matrice carrée réelle | hypothese_manquante |
| 99 | Théorème des suites adjacentes | (uₙ) est croissante et (vₙ) est décroissante; vₙ − uₙ → 0 | (uₙ) est croissante et (vₙ) est décroissante; vₙ − uₙ → 0 | VRAI | OK | correcte |
| 100 | Théorème des Valeurs Intermédiaires | f est dérivable sur [a, b]; y est compris entre f(a) et f(b) | f est continue sur [a, b]; y est compris entre f(a) et f(b) | VRAI | OK | hypothese_mal_formulee |
