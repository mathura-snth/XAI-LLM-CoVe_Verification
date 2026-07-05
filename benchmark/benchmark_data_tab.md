# Benchmark des théorèmes mathématiques

**Total:** 100 copies

**Correctes:** 60

**Fausses:** 40

## Détail des copies

| # | Théorème | Copie | Attendu | Verdict | Raison | Type_erreur |
|---|----------|-------|---------|---------|--------|-------------|
| 1 | Théorème des suites adjacentes | vₙ − uₙ → 0 | (uₙ) est croissante et (vₙ) est décroissante; vₙ − uₙ → 0 | FAUX | manquante: (uₙ) est croissante et (vₙ) e... | hypothese_manquante |
| 2 | Théorème de Cauchy-Lipschitz | f est continue en t; f est lipschitzienne en y; une conditio... | f est continue en t; f est lipschitzienne en y; une conditio... | FAUX | inventee: [inventee] F_CONTINUE_EN_Y | hypothese_inventee |
| 3 | Intégration par parties | u et v sont de classe C¹ sur [a, b] | u et v sont de classe C¹ sur [a, b] | VRAI | OK | correcte |
| 4 | Théorème de Cauchy-Lipschitz | f est continue en t; f est lipschitzienne en y | f est continue en t; f est lipschitzienne en y; une conditio... | FAUX | manquante: une condition initiale y(t₀) ... | hypothese_manquante |
| 5 | Théorème de Cauchy-Lipschitz | f est continue en t; f est lipschitzienne en y; une conditio... | f est continue en t; f est lipschitzienne en y; une conditio... | VRAI | OK | implication_invalide |
| 6 | Théorème des Valeurs Intermédiaires | f est de classe C¹ sur I; y est compris entre f(a) et f(b) | f est continue sur [a, b]; y est compris entre f(a) et f(b) | VRAI | OK | renforcement_abusif |
| 7 | Théorème des Accroissements Finis (Lagrange) | f est continue sur [a, b]; f est dérivable sur ]a, b[ | f est continue sur [a, b]; f est dérivable sur ]a, b[ | VRAI | OK | correcte |
| 8 | Théorème des Valeurs Intermédiaires | f(a) et f(b) sont de signes strictement opposés; y est compr... | f est continue sur [a, b]; y est compris entre f(a) et f(b) | FAUX | mal_formulee: f est continue sur [a, b] | hypothese_mal_formulee |
| 9 | Théorème de convergence monotone (suites) | (uₙ) est une suite croissante; (uₙ) est majorée | (uₙ) est une suite croissante; (uₙ) est majorée | VRAI | OK | correcte |
| 10 | Théorème de Heine (continuité uniforme) | f est continue sur [a, b]; f est continue sur ]a, b[ | f est continue sur [a, b]; [a, b] est un intervalle fermé et... | VRAI | OK | hypothese_mal_formulee |
| 11 | Théorème spectral (matrices symétriques réelles) | A est une matrice carrée réelle; A est symétrique (A = Aᵀ); ... | A est une matrice carrée réelle; A est symétrique (A = Aᵀ) | FAUX | inventee: [inventee] A_MATRICE_COMPLEXE | hypothese_inventee |
| 12 | Principe de superposition (EDO linéaires) | L est un opérateur différentiel linéaire | L est un opérateur différentiel linéaire; y₁ est solution de... | FAUX | manquante: y₁ est solution de L(y) = f₁;... | plusieurs_manquantes |
| 13 | Règle de L'Hôpital | f et g sont dérivables au voisinage de a; g'(x) ≠ 0 au voisi... | f et g sont dérivables au voisinage de a; g'(x) ≠ 0 au voisi... | FAUX | mal_formulee: f(a) = g(a) = 0 ou f et g ... | hypothese_mal_formulee |
| 14 | Théorème des Valeurs Intermédiaires | f est de classe C¹ sur I; y est compris entre f(a) et f(b) | f est continue sur [a, b]; y est compris entre f(a) et f(b) | VRAI | OK | renforcement_abusif |
| 15 | Théorème de Weierstrass | f est continue sur ]a, b[; [a, b] est un intervalle fermé et... | f est continue sur [a, b]; [a, b] est un intervalle fermé et... | FAUX | mal_formulee: f est continue sur [a, b] | intervalle_errone |
| 16 | Inégalité de Jensen | φ est une fonction convexe; X est une variable aléatoire rée... | φ est une fonction convexe; X est une variable aléatoire rée... | VRAI | OK | correcte |
| 17 | Théorème de convergence monotone (suites) | (uₙ) est une suite croissante; (uₙ) est majorée; (uₙ) est un... | (uₙ) est une suite croissante; (uₙ) est majorée | FAUX | inventee: [inventee] UN_DECROISSANTE_MAJ... | hypothese_inventee |
| 18 | Théorème de Cauchy-Lipschitz | f est continue en t; f est lipschitzienne en y; une conditio... | f est continue en t; f est lipschitzienne en y; une conditio... | VRAI | OK | implication_valide |
| 19 | Théorème de Heine (continuité uniforme) | f est continue sur [a, b] | f est continue sur [a, b]; [a, b] est un intervalle fermé et... | VRAI | OK | hypothese_manquante |
| 20 | Théorème des Valeurs Intermédiaires | f est continue sur ]a, b[; y est compris entre f(a) et f(b) | f est continue sur [a, b]; y est compris entre f(a) et f(b) | FAUX | implication_invalide: f est continue sur... | implication_invalide |
| 21 | Critère de d'Alembert (séries) | uₙ > 0 pour tout n suffisamment grand; lim_{n→∞} u_{n+1}/uₙ ... | uₙ > 0 pour tout n suffisamment grand; lim_{n→∞} u_{n+1}/uₙ ... | VRAI | OK | correcte |
| 22 | Théorème de Bolzano-Weierstrass | (uₙ) est une suite croissante | (uₙ) est une suite bornée de réels | FAUX | mal_formulee: (uₙ) est une suite bornée ... | hypothese_mal_formulee |
| 23 | Critère de Cauchy (suites) | (uₙ) est bornée | (uₙ) est une suite dans un espace complet | FAUX | mal_formulee: (uₙ) est une suite dans un... | hypothese_mal_formulee |
| 24 | Inégalité de Jensen | X est bornée; X est une variable aléatoire réelle intégrable | φ est une fonction convexe; X est une variable aléatoire rée... | FAUX | mal_formulee: φ est une fonction convexe | hypothese_mal_formulee |
| 25 | Changement de variable dans une intégrale | φ est de classe C¹ sur [α, β]; f est continue sur φ([α, β]) | φ est de classe C¹ sur [α, β]; f est continue sur φ([α, β]) | VRAI | OK | implication_valide |
| 26 | Théorème des suites adjacentes | (uₙ) est croissante et (vₙ) est décroissante; vₙ − uₙ → 0 | (uₙ) est croissante et (vₙ) est décroissante; vₙ − uₙ → 0 | VRAI | OK | correcte |
| 27 | Formule de Taylor-Young | f est n fois dérivable en a | f est n fois dérivable en a | VRAI | OK | correcte |
| 28 | Théorème de la base incomplète | E est un espace vectoriel de dimension finie n; F est une ba... | E est un espace vectoriel de dimension finie n; F = (f₁, ...... | VRAI | OK | hypothese_mal_formulee |
| 29 | Formule de Taylor avec reste de Lagrange | f est n+1 fois dérivable sur ]a, b[ | f est n fois dérivable sur [a, b] (continue); f est n+1 fois... | FAUX | manquante: f est n fois dérivable sur [a... | hypothese_manquante |
| 30 | Théorème de Heine (continuité uniforme) | f est lipschitzienne sur [a, b]; [a, b] est un intervalle fe... | f est continue sur [a, b]; [a, b] est un intervalle fermé et... | VRAI | OK | hypothese_mal_formulee |
| 31 | Diagonalisabilité (valeurs propres distinctes) | f est un endomorphisme de E (dim finie n); f admet n valeurs... | f est un endomorphisme de E (dim finie n); f admet n valeurs... | FAUX | inventee: [inventee] F_MATRICE_TRIANGULAIRE | hypothese_inventee |
| 32 | Théorème de convergence dominée | (fₙ) est une suite de fonctions mesurables; fₙ → f presque p... | (fₙ) est une suite de fonctions mesurables; fₙ → f presque p... | VRAI | OK | implication_invalide |
| 33 | Intégration par parties | u et v sont de classe C¹ sur [a, b] | u et v sont de classe C¹ sur [a, b] | VRAI | OK | correcte |
| 34 | Loi des Grands Nombres (faible) | (Xₙ) est une suite de variables aléatoires indépendantes; le... | (Xₙ) est une suite de variables aléatoires indépendantes; le... | VRAI | OK | correcte |
| 35 | Intégration par parties | u et v sont de classe C¹ sur [a, b] | u et v sont de classe C¹ sur [a, b] | VRAI | OK | correcte |
| 36 | Théorème Central Limite | (Xₙ) est une suite de variables aléatoires indépendantes; le... | (Xₙ) est une suite de variables aléatoires indépendantes; le... | VRAI | OK | correcte |
| 37 | Diagonalisabilité (valeurs propres distinctes) | f est un endomorphisme de E (dim finie n); f admet n valeurs... | f est un endomorphisme de E (dim finie n); f admet n valeurs... | FAUX | inventee: [inventee] F_N_VP_NON_DISTINCTES | hypothese_inventee |
| 38 | Théorème Fondamental de l'Analyse | f est continue sur ]a, b[ | f est continue sur [a, b] | FAUX | mal_formulee: f est continue sur [a, b] | intervalle_errone |
| 39 | Théorème Fondamental de l'Analyse | f est de classe C¹ sur I | f est continue sur [a, b] | VRAI | OK | implication_valide |
| 40 | Diagonalisabilité (valeurs propres distinctes) | le polynôme caractéristique est scindé; f admet n valeurs pr... | f est un endomorphisme de E (dim finie n); f admet n valeurs... | VRAI | OK | implication_valide |
| 41 | Règle de L'Hôpital | f et g sont dérivables au voisinage de a; g'(x) ≠ 0 au voisi... | f et g sont dérivables au voisinage de a; g'(x) ≠ 0 au voisi... | FAUX | inventee: [inventee] G_NON_NULLE_VOIS_A | hypothese_inventee |
| 42 | Intégration par parties | u et v sont de classe C¹ sur [a, b] | u et v sont de classe C¹ sur [a, b] | VRAI | OK | implication_invalide |
| 43 | Théorème de Heine (continuité uniforme) | f est continue sur [a, b]; [a, b] est un intervalle fermé et... | f est continue sur [a, b]; [a, b] est un intervalle fermé et... | FAUX | inventee: [inventee] F_UNIF_CONTINUE_R | hypothese_inventee |
| 44 | Théorème de Bolzano-Weierstrass | (uₙ) est une suite bornée de réels | (uₙ) est une suite bornée de réels | VRAI | OK | correcte |
| 45 | Réduction de Jordan (existence) | A est une matrice carrée n×n à coefficients complexes | A est une matrice carrée n×n à coefficients complexes | VRAI | OK | correcte |
| 46 | Théorème de la base incomplète | F est une base de E; F = (f₁, ..., fₖ) est une famille libre... | E est un espace vectoriel de dimension finie n; F = (f₁, ...... | VRAI | OK | hypothese_mal_formulee |
| 47 | Inégalité de Cauchy-Schwarz | u et v sont deux vecteurs de E | E est un espace vectoriel muni d'un produit scalaire; u et v... | FAUX | manquante: E est un espace vectoriel mun... | hypothese_manquante |
| 48 | Inégalité de Jensen | X est une variable aléatoire réelle intégrable | φ est une fonction convexe; X est une variable aléatoire rée... | FAUX | manquante: φ est une fonction convexe | hypothese_manquante |
| 49 | Théorème des suites adjacentes | (uₙ) est croissante et (vₙ) est décroissante; vₙ − uₙ → 0 | (uₙ) est croissante et (vₙ) est décroissante; vₙ − uₙ → 0 | VRAI | OK | correcte |
| 50 | Théorème Central Limite | (Xₙ) est une suite de variables aléatoires indépendantes; le... | (Xₙ) est une suite de variables aléatoires indépendantes; le... | VRAI | OK | correcte |
| 51 | Théorème de convergence monotone (suites) | (uₙ) est une suite croissante | (uₙ) est une suite croissante; (uₙ) est majorée | FAUX | manquante: (uₙ) est majorée | hypothese_manquante |
| 52 | Diagonalisabilité (valeurs propres distinctes) | le polynôme caractéristique est scindé; f admet n valeurs pr... | f est un endomorphisme de E (dim finie n); f admet n valeurs... | VRAI | OK | implication_valide |
| 53 | Projection orthogonale (Hilbert) | E est un espace de Hilbert; F est un sous-espace vectoriel f... | E est un espace de Hilbert; F est un sous-espace vectoriel f... | FAUX | inventee: [inventee] F_DIM_FINIE | hypothese_inventee |
| 54 | Inégalité de Jensen | φ est une fonction convexe; X est une variable aléatoire rée... | φ est une fonction convexe; X est une variable aléatoire rée... | VRAI | OK | correcte |
| 55 | Critère de Cauchy (suites) | (uₙ) est une suite dans un espace complet | (uₙ) est une suite dans un espace complet | VRAI | OK | correcte |
| 56 | Critère de Cauchy (suites) | (uₙ) est une suite dans un espace complet | (uₙ) est une suite dans un espace complet | VRAI | OK | implication_invalide |
| 57 | Principe de superposition (EDO linéaires) | L est un opérateur différentiel linéaire; y₁ est solution de... | L est un opérateur différentiel linéaire; y₁ est solution de... | FAUX | inventee: [inventee] L_CONTINU | hypothese_inventee |
| 58 | Théorème du rang | f est une application linéaire de E vers F | f est une application linéaire de E vers F; E est un espace ... | FAUX | manquante: E est un espace vectoriel de ... | hypothese_manquante |
| 59 | Théorème de Cayley-Hamilton | A est une matrice carrée n×n; χ_A est le polynôme caractéris... | A est une matrice carrée n×n; χ_A est le polynôme caractéris... | VRAI | OK | correcte |
| 60 | Théorème spectral (matrices symétriques réelles) | A est une matrice carrée réelle; A est symétrique (A = Aᵀ) | A est une matrice carrée réelle; A est symétrique (A = Aᵀ) | VRAI | OK | correcte |
| 61 | Théorème de Cauchy-Lipschitz | f est continue en t; f est lipschitzienne en y; une conditio... | f est continue en t; f est lipschitzienne en y; une conditio... | FAUX | inventee: [inventee] F_BORNEE | hypothese_inventee |
| 62 | Principe de superposition (EDO linéaires) | L est un opérateur différentiel linéaire | L est un opérateur différentiel linéaire; y₁ est solution de... | FAUX | manquante: y₁ est solution de L(y) = f₁;... | plusieurs_manquantes |
| 63 | Loi des Grands Nombres (faible) | (Xₙ) est une suite de variables aléatoires indépendantes; le... | (Xₙ) est une suite de variables aléatoires indépendantes; le... | VRAI | OK | implication_invalide |
| 64 | Théorème de convergence monotone (suites) | (uₙ) est bornée; (uₙ) est majorée | (uₙ) est une suite croissante; (uₙ) est majorée | FAUX | mal_formulee: (uₙ) est une suite croissante | hypothese_mal_formulee |
| 65 | Principe de superposition (EDO linéaires) | L est un opérateur différentiel linéaire | L est un opérateur différentiel linéaire; y₁ est solution de... | FAUX | manquante: y₁ est solution de L(y) = f₁;... | plusieurs_manquantes |
| 66 | Inégalité de Cauchy-Schwarz | E est un espace vectoriel muni d'un produit scalaire; u et v... | E est un espace vectoriel muni d'un produit scalaire; u et v... | VRAI | OK | correcte |
| 67 | Théorème de Weierstrass | f est continue sur ]a, b[; [a, b] est un intervalle fermé et... | f est continue sur [a, b]; [a, b] est un intervalle fermé et... | FAUX | mal_formulee: f est continue sur [a, b] | intervalle_errone |
| 68 | Réduction de Jordan (existence) | A est une matrice carrée n×n à coefficients complexes; A est... | A est une matrice carrée n×n à coefficients complexes | FAUX | inventee: [inventee] A_MATRICE_REELLE | hypothese_inventee |
| 69 | Théorème des Accroissements Finis (Lagrange) | f est continue sur ]a, b[; f est dérivable sur ]a, b[ | f est continue sur [a, b]; f est dérivable sur ]a, b[ | FAUX | mal_formulee: f est continue sur [a, b] | hypothese_mal_formulee |
| 70 | Théorème de Cauchy-Lipschitz | f est continue en t; f est lipschitzienne en y; une conditio... | f est continue en t; f est lipschitzienne en y; une conditio... | VRAI | OK | implication_valide |
| 71 | Loi des Grands Nombres (faible) | (Xₙ) est une suite de variables aléatoires indépendantes; le... | (Xₙ) est une suite de variables aléatoires indépendantes; le... | FAUX | manquante: E[|X₁|] est finie | hypothese_manquante |
| 72 | Principe de superposition (EDO linéaires) | L est un opérateur différentiel linéaire | L est un opérateur différentiel linéaire; y₁ est solution de... | FAUX | manquante: y₁ est solution de L(y) = f₁;... | plusieurs_manquantes |
| 73 | Théorème de Heine (continuité uniforme) | f est continue sur [a, b]; [a, b] est un intervalle fermé et... | f est continue sur [a, b]; [a, b] est un intervalle fermé et... | VRAI | OK | correcte |
| 74 | Changement de variable dans une intégrale | φ est de classe C¹ sur [α, β]; f est continue sur φ([α, β]) | φ est de classe C¹ sur [α, β]; f est continue sur φ([α, β]) | VRAI | OK | implication_invalide |
| 75 | Inégalité de Jensen | φ est une fonction convexe; X est une variable aléatoire rée... | φ est une fonction convexe; X est une variable aléatoire rée... | VRAI | OK | correcte |
| 76 | Théorème Fondamental de l'Analyse | f est continue sur ]a, b[ | f est continue sur [a, b] | FAUX | implication_invalide: f est continue sur... | implication_invalide |
| 77 | Principe de superposition (EDO linéaires) | L est un opérateur différentiel linéaire; y₁ est solution de... | L est un opérateur différentiel linéaire; y₁ est solution de... | FAUX | mal_formulee: y₂ est solution de L(y) = f₂ | hypothese_mal_formulee |
| 78 | Diagonalisabilité (valeurs propres distinctes) | f est un endomorphisme de E (dim finie n); f admet n valeurs... | f est un endomorphisme de E (dim finie n); f admet n valeurs... | VRAI | OK | correcte |
| 79 | Théorème spectral (matrices symétriques réelles) | A est une matrice carrée réelle; A est symétrique (A = Aᵀ) | A est une matrice carrée réelle; A est symétrique (A = Aᵀ) | VRAI | OK | implication_invalide |
| 80 | Théorème spectral (matrices symétriques réelles) | A est symétrique (A = Aᵀ) | A est une matrice carrée réelle; A est symétrique (A = Aᵀ) | VRAI | OK | hypothese_manquante |
| 81 | Intégration par parties | u et v sont de classe C¹ sur [a, b] | u et v sont de classe C¹ sur [a, b] | VRAI | OK | correcte |
| 82 | Théorème du rang | f est une application linéaire de E vers F; E est un espace ... | f est une application linéaire de E vers F; E est un espace ... | VRAI | OK | correcte |
| 83 | Théorème de Bolzano-Weierstrass | (uₙ) est une suite bornée de réels | (uₙ) est une suite bornée de réels | VRAI | OK | implication_invalide |
| 84 | Intégration par parties | u et v sont continues sur [a, b] | u et v sont de classe C¹ sur [a, b] | FAUX | mal_formulee: u et v sont de classe C¹ s... | hypothese_mal_formulee |
| 85 | Théorème de convergence dominée | (fₙ) est une suite de fonctions mesurables; fₙ → f presque p... | (fₙ) est une suite de fonctions mesurables; fₙ → f presque p... | VRAI | OK | correcte |
| 86 | Intégration par parties | u et v sont de classe C¹ sur [a, b] | u et v sont de classe C¹ sur [a, b] | VRAI | OK | correcte |
| 87 | Réduction de Jordan (existence) | A est une matrice carrée n×n à coefficients complexes | A est une matrice carrée n×n à coefficients complexes | VRAI | OK | correcte |
| 88 | Inégalité de Jensen | φ est une fonction convexe; X est une variable aléatoire rée... | φ est une fonction convexe; X est une variable aléatoire rée... | VRAI | OK | correcte |
| 89 | Théorème des Valeurs Intermédiaires | f est continue sur ]a, b[; y est compris entre f(a) et f(b) | f est continue sur [a, b]; y est compris entre f(a) et f(b) | FAUX | implication_invalide: f est continue sur... | implication_invalide |
| 90 | Intégration par parties | u et v sont de classe C¹ sur [a, b]; u' et v sont continues ... | u et v sont de classe C¹ sur [a, b] | FAUX | inventee: [inventee] UPRIME_V_CONTINUES_... | hypothese_inventee |
| 91 | Inégalité de Cauchy-Schwarz | E est un espace vectoriel de dimension finie n; u et v sont ... | E est un espace vectoriel muni d'un produit scalaire; u et v... | FAUX | mal_formulee: E est un espace vectoriel ... | hypothese_mal_formulee |
| 92 | Formule de Taylor avec reste de Lagrange | f est n fois dérivable sur [a, b] (continue); f est n+1 fois... | f est n fois dérivable sur [a, b] (continue); f est n+1 fois... | VRAI | OK | implication_valide |
| 93 | Intégration par parties | u et v sont de classe C² sur [a, b] | u et v sont de classe C¹ sur [a, b] | VRAI | OK | implication_valide |
| 94 | Théorème Central Limite | (Xₙ) est une suite de variables aléatoires indépendantes; le... | (Xₙ) est une suite de variables aléatoires indépendantes; le... | VRAI | OK | correcte |
| 95 | Théorème Fondamental de l'Analyse | f est continue sur [a, b] | f est continue sur [a, b] | VRAI | OK | correcte |
| 96 | Théorème de Weierstrass | f est de classe C¹ sur I; [a, b] est un intervalle fermé et ... | f est continue sur [a, b]; [a, b] est un intervalle fermé et... | VRAI | OK | renforcement_abusif |
| 97 | Théorème de la base incomplète | E est un espace vectoriel de dimension finie n; F = (f₁, ...... | E est un espace vectoriel de dimension finie n; F = (f₁, ...... | VRAI | OK | correcte |
| 98 | Théorème de Cayley-Hamilton | A est une matrice carrée n×n; χ_A est le polynôme caractéris... | A est une matrice carrée n×n; χ_A est le polynôme caractéris... | VRAI | OK | implication_valide |
| 99 | Inégalité de Jensen | φ est une fonction convexe; X est une variable aléatoire rée... | φ est une fonction convexe; X est une variable aléatoire rée... | VRAI | OK | correcte |
| 100 | Critère de Cauchy (suites) | (uₙ) est une suite dans un espace complet | (uₙ) est une suite dans un espace complet | VRAI | OK | correcte |
