# Benchmark des théorèmes mathématiques

**Total:** 100 copies

**Correctes:** 58

**Fausses:** 42

## Détail des copies

| # | Théorème | Copie | Attendu | Verdict | Raison | Type_erreur |
|---|----------|-------|---------|---------|--------|-------------|
| 1 | Théorème des suites adjacentes | vₙ − uₙ → 0 | (uₙ) est croissante et (vₙ) est décroissante; vₙ − uₙ → 0 | FAUX | manquante: (uₙ) est croissante et (vₙ) e... | hypothese_manquante |
| 2 | Théorème de Cauchy-Lipschitz | f est continue en t; f est lipschitzienne en y; une conditio... | f est continue en t; f est lipschitzienne en y; une conditio... | FAUX | erreur_inconnue | hypothese_inventee |
| 3 | Intégration par parties | u et v sont de classe C¹ sur [a, b] | u et v sont de classe C¹ sur [a, b] | VRAI | OK | correcte |
| 4 | Théorème de Cauchy-Lipschitz | f est continue en t; f est lipschitzienne en y | f est continue en t; f est lipschitzienne en y; une conditio... | FAUX | manquante: une condition initiale y(t₀) ... | hypothese_manquante |
| 5 | Théorème de Cauchy-Lipschitz | f est continue en t; f est lipschitzienne en y; une conditio... | f est continue en t; f est lipschitzienne en y; une conditio... | VRAI | OK | implication_invalide |
| 6 | Théorème des Valeurs Intermédiaires | f est de classe C¹ sur I; y est compris entre f(a) et f(b) | f est continue sur [a, b]; y est compris entre f(a) et f(b) | VRAI | OK | renforcement_abusif |
| 7 | Théorème des Accroissements Finis (Lagrange) | f est continue sur [a, b]; f est dérivable sur ]a, b[ | f est continue sur [a, b]; f est dérivable sur ]a, b[ | VRAI | OK | correcte |
| 8 | Théorème des Valeurs Intermédiaires | s; y est compris entre f(a) et f(b) | f est continue sur [a, b]; y est compris entre f(a) et f(b) | FAUX | mal_formulee: f est continue sur [a, b] | hypothese_mal_formulee |
| 9 | Théorème de convergence monotone (suites) | (uₙ) est une suite croissante; (uₙ) est majorée | (uₙ) est une suite croissante; (uₙ) est majorée | VRAI | OK | correcte |
| 10 | Théorème de Heine (continuité uniforme) | f est continue sur [a, b]; _ | f est continue sur [a, b]; [a, b] est un intervalle fermé et... | VRAI | OK | hypothese_mal_formulee |
| 11 | Théorème spectral (matrices symétriques réelles) | A est une matrice carrée réelle; A est symétrique (A = Aᵀ); e | A est une matrice carrée réelle; A est symétrique (A = Aᵀ) | FAUX | erreur_inconnue | hypothese_inventee |
| 12 | Principe de superposition (EDO linéaires) | L est un opérateur différentiel linéaire | L est un opérateur différentiel linéaire; y₁ est solution de... | FAUX | manquante: y₂ est solution de L(y) = f₂;... | plusieurs_manquantes |
| 13 | Règle de L'Hôpital | f et g sont dérivables au voisinage de a; g'(x) ≠ 0 au voisi... | f et g sont dérivables au voisinage de a; g'(x) ≠ 0 au voisi... | FAUX | mal_formulee: f(a) = g(a) = 0 ou f et g ... | hypothese_mal_formulee |
| 14 | Théorème des Valeurs Intermédiaires | f est de classe C¹ sur I; y est compris entre f(a) et f(b) | f est continue sur [a, b]; y est compris entre f(a) et f(b) | VRAI | OK | renforcement_abusif |
| 15 | Théorème de Weierstrass | f est continue sur ]a, b[; [a, b] est un intervalle fermé et... | f est continue sur [a, b]; [a, b] est un intervalle fermé et... | FAUX | mal_formulee: f est continue sur [a, b] | intervalle_errone |
| 16 | Inégalité de Jensen | φ est une fonction convexe; X est une variable aléatoire rée... | φ est une fonction convexe; X est une variable aléatoire rée... | VRAI | OK | correcte |
| 17 | Théorème de convergence monotone (suites) | (uₙ) est une suite croissante; (uₙ) est majorée; r | (uₙ) est une suite croissante; (uₙ) est majorée | FAUX | erreur_inconnue | hypothese_inventee |
| 18 | Théorème de Cauchy-Lipschitz | f est continue en t; f est lipschitzienne en y; une conditio... | f est continue en t; f est lipschitzienne en y; une conditio... | VRAI | OK | implication_valide |
| 19 | Théorème de Heine (continuité uniforme) | f est continue sur [a, b] | f est continue sur [a, b]; [a, b] est un intervalle fermé et... | VRAI | OK | hypothese_manquante |
| 20 | Théorème des Valeurs Intermédiaires | f est continue sur ]a, b[; y est compris entre f(a) et f(b) | f est continue sur [a, b]; y est compris entre f(a) et f(b) | FAUX | implication_invalide: f est continue sur... | implication_invalide |
| 21 | Critère de d'Alembert (séries) | uₙ > 0 pour tout n suffisamment grand; lim_{n→∞} u_{n+1}/uₙ ... | uₙ > 0 pour tout n suffisamment grand; lim_{n→∞} u_{n+1}/uₙ ... | VRAI | OK | correcte |
| 22 | Théorème de Bolzano-Weierstrass | r | (uₙ) est une suite bornée de réels | FAUX | mal_formulee: (uₙ) est une suite bornée ... | hypothese_mal_formulee |
| 23 | Critère de Cauchy (suites) | r | (uₙ) est une suite dans un espace complet | FAUX | mal_formulee: (uₙ) est une suite dans un... | hypothese_mal_formulee |
| 24 | Inégalité de Jensen | a; X est une variable aléatoire réelle intégrable | φ est une fonction convexe; X est une variable aléatoire rée... | FAUX | mal_formulee: φ est une fonction convexe | hypothese_mal_formulee |
| 25 | Changement de variable dans une intégrale | φ est bijective sur [α, β]; f est continue sur φ([α, β]) | φ est de classe C¹ sur [α, β]; f est continue sur φ([α, β]) | VRAI | OK | implication_valide |
| 26 | Théorème des suites adjacentes | (uₙ) est croissante et (vₙ) est décroissante; vₙ − uₙ → 0 | (uₙ) est croissante et (vₙ) est décroissante; vₙ − uₙ → 0 | VRAI | OK | correcte |
| 27 | Formule de Taylor-Young | f est n fois dérivable en a | f est n fois dérivable en a | VRAI | OK | correcte |
| 28 | Théorème de la base incomplète | E est un espace vectoriel de dimension finie n; r | E est un espace vectoriel de dimension finie n; F = (f₁, ...... | FAUX | mal_formulee: F = (f₁, ..., fₖ) est une ... | hypothese_mal_formulee |
| 29 | Théorème de convergence monotone (suites) | (uₙ) est une suite croissante; (uₙ) est majorée | (uₙ) est une suite croissante; (uₙ) est majorée | VRAI | OK | correcte |
| 30 | Théorème de Heine (continuité uniforme) | t; [a, b] est un intervalle fermé et borné | f est continue sur [a, b]; [a, b] est un intervalle fermé et... | FAUX | mal_formulee: f est continue sur [a, b] | hypothese_mal_formulee |
| 31 | Diagonalisabilité (valeurs propres distinctes) | f est un endomorphisme de E (dim finie n); f admet n valeurs... | f est un endomorphisme de E (dim finie n); f admet n valeurs... | FAUX | erreur_inconnue | hypothese_inventee |
| 32 | Critère de Cauchy (suites) | (uₙ) est une suite dans un espace complet | (uₙ) est une suite dans un espace complet | VRAI | OK | correcte |
| 33 | Loi des Grands Nombres (faible) | (Xₙ) est une suite de variables aléatoires indépendantes; le... | (Xₙ) est une suite de variables aléatoires indépendantes; le... | VRAI | OK | correcte |
| 34 | Intégration par parties | u et v sont de classe C¹ sur [a, b] | u et v sont de classe C¹ sur [a, b] | VRAI | OK | correcte |
| 35 | Théorème Central Limite | (Xₙ) est une suite de variables aléatoires indépendantes; le... | (Xₙ) est une suite de variables aléatoires indépendantes; le... | VRAI | OK | correcte |
| 36 | Diagonalisabilité (valeurs propres distinctes) | f est un endomorphisme de E (dim finie n); f admet n valeurs... | f est un endomorphisme de E (dim finie n); f admet n valeurs... | FAUX | erreur_inconnue | hypothese_inventee |
| 37 | Théorème Fondamental de l'Analyse | f est continue sur ]a, b[ | f est continue sur [a, b] | FAUX | mal_formulee: f est continue sur [a, b] | intervalle_errone |
| 38 | Théorème Fondamental de l'Analyse | f est de classe C¹ sur I | f est continue sur [a, b] | VRAI | OK | implication_valide |
| 39 | Diagonalisabilité (valeurs propres distinctes) | le polynôme caractéristique est scindé; f admet n valeurs pr... | f est un endomorphisme de E (dim finie n); f admet n valeurs... | VRAI | OK | implication_valide |
| 40 | Règle de L'Hôpital | f et g sont dérivables au voisinage de a; g'(x) ≠ 0 au voisi... | f et g sont dérivables au voisinage de a; g'(x) ≠ 0 au voisi... | FAUX | erreur_inconnue | hypothese_inventee |
| 41 | Intégration par parties | u et v sont de classe C¹ sur [a, b] | u et v sont de classe C¹ sur [a, b] | VRAI | OK | implication_invalide |
| 42 | Théorème de Heine (continuité uniforme) | f est continue sur [a, b]; [a, b] est un intervalle fermé et... | f est continue sur [a, b]; [a, b] est un intervalle fermé et... | FAUX | erreur_inconnue | hypothese_inventee |
| 43 | Réduction de Jordan (existence) | A est une matrice carrée n×n à coefficients complexes | A est une matrice carrée n×n à coefficients complexes | VRAI | OK | correcte |
| 44 | Théorème de la base incomplète | s; F = (f₁, ..., fₖ) est une famille libre de E avec k ≤ n | E est un espace vectoriel de dimension finie n; F = (f₁, ...... | VRAI | OK | hypothese_mal_formulee |
| 45 | Inégalité de Cauchy-Schwarz | u et v sont deux vecteurs de E | E est un espace vectoriel muni d'un produit scalaire; u et v... | FAUX | manquante: E est un espace vectoriel mun... | hypothese_manquante |
| 46 | Inégalité de Jensen | X est une variable aléatoire réelle intégrable | φ est une fonction convexe; X est une variable aléatoire rée... | FAUX | manquante: φ est une fonction convexe | hypothese_manquante |
| 47 | Théorème des suites adjacentes | (uₙ) est croissante et (vₙ) est décroissante; vₙ − uₙ → 0 | (uₙ) est croissante et (vₙ) est décroissante; vₙ − uₙ → 0 | VRAI | OK | correcte |
| 48 | Théorème Central Limite | (Xₙ) est une suite de variables aléatoires indépendantes; le... | (Xₙ) est une suite de variables aléatoires indépendantes; le... | VRAI | OK | correcte |
| 49 | Théorème de convergence monotone (suites) | (uₙ) est une suite croissante | (uₙ) est une suite croissante; (uₙ) est majorée | VRAI | OK | hypothese_manquante |
| 50 | Diagonalisabilité (valeurs propres distinctes) | le polynôme caractéristique est scindé; f admet n valeurs pr... | f est un endomorphisme de E (dim finie n); f admet n valeurs... | VRAI | OK | implication_valide |
| 51 | Projection orthogonale (Hilbert) | E est un espace de Hilbert; F est un sous-espace vectoriel f... | E est un espace de Hilbert; F est un sous-espace vectoriel f... | FAUX | erreur_inconnue | hypothese_inventee |
| 52 | Critère de Cauchy (suites) | (uₙ) est une suite dans un espace complet | (uₙ) est une suite dans un espace complet | VRAI | OK | correcte |
| 53 | Critère de Cauchy (suites) | (uₙ) est une suite dans un espace complet | (uₙ) est une suite dans un espace complet | VRAI | OK | implication_invalide |
| 54 | Principe de superposition (EDO linéaires) | L est un opérateur différentiel linéaire; y₁ est solution de... | L est un opérateur différentiel linéaire; y₁ est solution de... | FAUX | erreur_inconnue | hypothese_inventee |
| 55 | Théorème de Weierstrass | f est continue sur [a, b]; [a, b] est un intervalle fermé et... | f est continue sur [a, b]; [a, b] est un intervalle fermé et... | FAUX | erreur_inconnue | hypothese_inventee |
| 56 | Formule de Taylor-Young | f est n fois dérivable en a | f est n fois dérivable en a | VRAI | OK | implication_valide |
| 57 | Théorème de Rolle | f est continue sur [a, b]; f est dérivable sur ]a, b[; f(a) ... | f est continue sur [a, b]; f est dérivable sur ]a, b[; f(a) ... | FAUX | erreur_inconnue | hypothese_inventee |
| 58 | Principe de superposition (EDO linéaires) | L est un opérateur différentiel linéaire | L est un opérateur différentiel linéaire; y₁ est solution de... | FAUX | manquante: y₂ est solution de L(y) = f₂;... | plusieurs_manquantes |
| 59 | Loi des Grands Nombres (faible) | (Xₙ) est une suite de variables aléatoires indépendantes; le... | (Xₙ) est une suite de variables aléatoires indépendantes; le... | VRAI | OK | implication_invalide |
| 60 | Théorème de convergence monotone (suites) | r; (uₙ) est majorée | (uₙ) est une suite croissante; (uₙ) est majorée | FAUX | mal_formulee: (uₙ) est une suite croissante | hypothese_mal_formulee |
| 61 | Principe de superposition (EDO linéaires) | L est un opérateur différentiel linéaire | L est un opérateur différentiel linéaire; y₁ est solution de... | FAUX | manquante: y₂ est solution de L(y) = f₂;... | plusieurs_manquantes |
| 62 | Inégalité de Cauchy-Schwarz | E est un espace vectoriel muni d'un produit scalaire; u et v... | E est un espace vectoriel muni d'un produit scalaire; u et v... | VRAI | OK | correcte |
| 63 | Théorème de Weierstrass | f est continue sur ]a, b[; [a, b] est un intervalle fermé et... | f est continue sur [a, b]; [a, b] est un intervalle fermé et... | FAUX | mal_formulee: f est continue sur [a, b] | intervalle_errone |
| 64 | Réduction de Jordan (existence) | A est une matrice carrée n×n à coefficients complexes; _ | A est une matrice carrée n×n à coefficients complexes | FAUX | erreur_inconnue | hypothese_inventee |
| 65 | Théorème des Accroissements Finis (Lagrange) | r; f est dérivable sur ]a, b[ | f est continue sur [a, b]; f est dérivable sur ]a, b[ | FAUX | mal_formulee: f est continue sur [a, b] | hypothese_mal_formulee |
| 66 | Théorème de Cauchy-Lipschitz | f est continue en t; f est lipschitzienne en y; une conditio... | f est continue en t; f est lipschitzienne en y; une conditio... | VRAI | OK | implication_valide |
| 67 | Loi des Grands Nombres (faible) | (Xₙ) est une suite de variables aléatoires indépendantes; le... | (Xₙ) est une suite de variables aléatoires indépendantes; le... | FAUX | manquante: E[|X₁|] est finie | hypothese_manquante |
| 68 | Principe de superposition (EDO linéaires) | L est un opérateur différentiel linéaire | L est un opérateur différentiel linéaire; y₁ est solution de... | FAUX | manquante: y₂ est solution de L(y) = f₂;... | plusieurs_manquantes |
| 69 | Théorème de Heine (continuité uniforme) | f est continue sur [a, b]; [a, b] est un intervalle fermé et... | f est continue sur [a, b]; [a, b] est un intervalle fermé et... | VRAI | OK | correcte |
| 70 | Changement de variable dans une intégrale | φ est de classe C¹ sur [α, β]; f est continue sur φ([α, β]) | φ est de classe C¹ sur [α, β]; f est continue sur φ([α, β]) | VRAI | OK | implication_invalide |
| 71 | Inégalité de Jensen | φ est une fonction convexe; X est une variable aléatoire rée... | φ est une fonction convexe; X est une variable aléatoire rée... | VRAI | OK | correcte |
| 72 | Théorème Fondamental de l'Analyse | f est continue sur ]a, b[ | f est continue sur [a, b] | FAUX | implication_invalide: f est continue sur... | implication_invalide |
| 73 | Principe de superposition (EDO linéaires) | L est un opérateur différentiel linéaire; y₁ est solution de... | L est un opérateur différentiel linéaire; y₁ est solution de... | FAUX | mal_formulee: y₂ est solution de L(y) = f₂ | hypothese_mal_formulee |
| 74 | Diagonalisabilité (valeurs propres distinctes) | f est un endomorphisme de E (dim finie n); f admet n valeurs... | f est un endomorphisme de E (dim finie n); f admet n valeurs... | VRAI | OK | correcte |
| 75 | Théorème spectral (matrices symétriques réelles) | A est une matrice carrée réelle; A est symétrique (A = Aᵀ) | A est une matrice carrée réelle; A est symétrique (A = Aᵀ) | VRAI | OK | implication_invalide |
| 76 | Théorème spectral (matrices symétriques réelles) | A est symétrique (A = Aᵀ) | A est une matrice carrée réelle; A est symétrique (A = Aᵀ) | VRAI | OK | hypothese_manquante |
| 77 | Intégration par parties | u et v sont de classe C¹ sur [a, b] | u et v sont de classe C¹ sur [a, b] | VRAI | OK | correcte |
| 78 | Théorème du rang | f est une application linéaire de E vers F; E est un espace ... | f est une application linéaire de E vers F; E est un espace ... | VRAI | OK | correcte |
| 79 | Théorème de Bolzano-Weierstrass | (uₙ) est une suite bornée de réels | (uₙ) est une suite bornée de réels | VRAI | OK | implication_invalide |
| 80 | Intégration par parties | r | u et v sont de classe C¹ sur [a, b] | FAUX | mal_formulee: u et v sont de classe C¹ s... | hypothese_mal_formulee |
| 81 | Théorème de convergence dominée | (fₙ) est une suite de fonctions mesurables; fₙ → f presque p... | (fₙ) est une suite de fonctions mesurables; fₙ → f presque p... | VRAI | OK | correcte |
| 82 | Intégration par parties | u et v sont de classe C¹ sur [a, b] | u et v sont de classe C¹ sur [a, b] | VRAI | OK | correcte |
| 83 | Réduction de Jordan (existence) | A est une matrice carrée n×n à coefficients complexes | A est une matrice carrée n×n à coefficients complexes | VRAI | OK | correcte |
| 84 | Inégalité de Jensen | φ est une fonction convexe; X est une variable aléatoire rée... | φ est une fonction convexe; X est une variable aléatoire rée... | VRAI | OK | correcte |
| 85 | Théorème des Valeurs Intermédiaires | f est continue sur ]a, b[; y est compris entre f(a) et f(b) | f est continue sur [a, b]; y est compris entre f(a) et f(b) | FAUX | implication_invalide: f est continue sur... | implication_invalide |
| 86 | Intégration par parties | u et v sont de classe C¹ sur [a, b]; e | u et v sont de classe C¹ sur [a, b] | FAUX | erreur_inconnue | hypothese_inventee |
| 87 | Théorème Fondamental de l'Analyse | f est continue sur ]a, b[ | f est continue sur [a, b] | FAUX | implication_invalide: f est continue sur... | implication_invalide |
| 88 | Règle de L'Hôpital | f et g sont dérivables au voisinage de a; g'(x) ≠ 0 au voisi... | f et g sont dérivables au voisinage de a; g'(x) ≠ 0 au voisi... | VRAI | OK | implication_valide |
| 89 | Intégration par parties | u et v sont de classe C² sur [a, b] | u et v sont de classe C¹ sur [a, b] | VRAI | OK | implication_valide |
| 90 | Théorème Central Limite | (Xₙ) est une suite de variables aléatoires indépendantes; le... | (Xₙ) est une suite de variables aléatoires indépendantes; le... | VRAI | OK | correcte |
| 91 | Théorème Fondamental de l'Analyse | f est continue sur [a, b] | f est continue sur [a, b] | VRAI | OK | correcte |
| 92 | Théorème de Weierstrass | f est de classe C¹ sur I; [a, b] est un intervalle fermé et ... | f est continue sur [a, b]; [a, b] est un intervalle fermé et... | VRAI | OK | renforcement_abusif |
| 93 | Théorème de la base incomplète | E est un espace vectoriel de dimension finie n; F = (f₁, ...... | E est un espace vectoriel de dimension finie n; F = (f₁, ...... | VRAI | OK | correcte |
| 94 | Théorème de Cayley-Hamilton | A est une matrice carrée n×n; χ_A est le polynôme caractéris... | A est une matrice carrée n×n; χ_A est le polynôme caractéris... | VRAI | OK | implication_valide |
| 95 | Inégalité de Jensen | φ est une fonction convexe; X est une variable aléatoire rée... | φ est une fonction convexe; X est une variable aléatoire rée... | VRAI | OK | correcte |
| 96 | Critère de Cauchy (suites) | (uₙ) est une suite dans un espace complet | (uₙ) est une suite dans un espace complet | VRAI | OK | correcte |
| 97 | Théorème des Accroissements Finis (Lagrange) | f est de classe C¹ sur I; f est dérivable sur ]a, b[ | f est continue sur [a, b]; f est dérivable sur ]a, b[ | VRAI | OK | renforcement_abusif |
| 98 | Théorème de Cauchy-Lipschitz | f est continue en t; f est lipschitzienne en y; une conditio... | f est continue en t; f est lipschitzienne en y; une conditio... | VRAI | OK | correcte |
| 99 | Théorème Central Limite | (Xₙ) est une suite de variables aléatoires indépendantes; E[... | (Xₙ) est une suite de variables aléatoires indépendantes; le... | FAUX | manquante: les Xₙ sont identiquement dis... | hypothese_manquante |
| 100 | Théorème Fondamental de l'Analyse | u | f est continue sur [a, b] | FAUX | mal_formulee: f est continue sur [a, b] | hypothese_mal_formulee |
