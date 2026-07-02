# Ensemble des hypothèses sous forme d'identifiant.
# id -> texte affiché dans les copies générées / prompts LLM
# comparaison ne doit jamais se faire sur le texte, que sur l'id.

HYPOTHESES = {
    "F_CONTINUE_EN_A":            "f est continue en a",
    "F_DERIVABLE_EN_A":           "f est dérivable en a",
    "F_CONTINUE_FERME":           "f est continue sur [a, b]",
    "F_CONTINUE_OUVERT":          "f est continue sur ]a, b[",
    "F_CONTINUE_R":               "f est continue sur ℝ",
    "F_DERIVABLE_FERME":          "f est dérivable sur [a, b]",
    "F_DERIVABLE_OUVERT":         "f est dérivable sur ]a, b[",
    "F_DERIVABLE_BORNES":         "f est dérivable en a et b",
    "F_CLASSE_C1":                "f est de classe C¹ sur I",
    "F_CLASSE_C2":                "f est de classe C² sur I",
    "F_CLASSE_CN":                "f est de classe Cⁿ sur I",
    "F_BORNEE_FERME":             "f est bornée sur [a, b]",
    "F_INTEGRABLE_FERME":         "f est intégrable sur [a, b]",
    "F_LIPSCHITZIENNE_FERME":     "f est lipschitzienne sur [a, b]",
    "F_UNIF_CONTINUE_FERME":      "f est uniformément continue sur [a, b]",
    "F_UNIF_CONTINUE_R":          "f est uniformément continue sur ℝ",

    # Rolle / Lagrange / TVI
    "F_EGAL_BORNES":              "f(a) = f(b)",
    "Y_ENTRE_BORNES":             "y est compris entre f(a) et f(b)",
    "SIGNES_OPPOSES":             "f(a) et f(b) sont de signes strictement opposés",

    # Weierstrass
    "INTERVALLE_COMPACT":         "[a, b] est un intervalle fermé et borné",

    # Règle de L'Hôpital
    "FG_DERIVABLES_VOISINAGE_A":  "f et g sont dérivables au voisinage de a",
    "G_PRIME_NON_NULLE_VOIS_A":   "g'(x) ≠ 0 au voisinage de a",
    "G_NON_NULLE_VOIS_A":         "g(x) ≠ 0 au voisinage de a",
    "FG_LIMITE_ZERO_OU_INFINI":   "f(a) = g(a) = 0 ou f et g tendent vers ±∞",
    "LIM_FPRIME_GPRIME_EXISTE":   "lim_{x→a} f'(x)/g'(x) = ℓ existe",
    "FG_CONTINUES_EN_A":          "f et g sont continues en a",
    "FG_CLASSE_C2_EN_A":          "f et g sont de classe C² en a",

    # Taylor-Young
    "F_N_FOIS_DERIVABLE_EN_A":    "f est n fois dérivable en a",
    "F_CLASSE_CN_VOISINAGE_A":    "f est de classe Cⁿ au voisinage de a",
    "F_NPLUS1_FOIS_DERIVABLE_A":  "f est n+1 fois dérivable en a",
    "F_ANALYTIQUE_EN_A":          "f est analytique en a",

    # Intégration par parties
    "UV_CLASSE_C1_FERME":         "u et v sont de classe C¹ sur [a, b]",
    "UV_CONTINUES_FERME":         "u et v sont continues sur [a, b]",
    "UV_CLASSE_C2_FERME":         "u et v sont de classe C² sur [a, b]",
    "UPRIME_V_CONTINUES_FERME":   "u' et v sont continues sur [a, b]",

    # Changement de variable
    "PHI_CLASSE_C1":              "φ est de classe C¹ sur [α, β]",
    "F_CONTINUE_PHI_IMAGE":       "f est continue sur φ([α, β])",
    "PHI_CONTINUE":               "φ est continue sur [α, β]",
    "F_DERIVABLE_PHI_IMAGE":      "f est dérivable sur φ([α, β])",
    "PHI_BIJECTIVE":              "φ est bijective sur [α, β]",

    # Critère de d'Alembert
    "UN_POSITIF_GRAND_N":         "uₙ > 0 pour tout n suffisamment grand",
    "LIM_RATIO_EXISTE":           "lim_{n→∞} u_{n+1}/uₙ = ℓ existe",
    "UN_NON_NUL":                 "uₙ ≠ 0 pour tout n",
    "LIM_UN_ZERO":                "lim uₙ = 0",
    "SERIE_TERMES_POSITIFS":      "la série est à termes positifs uniquement",

    # Théorème du rang
    "F_LINEAIRE_E_F":             "f est une application linéaire de E vers F",
    "E_DIM_FINIE":                "E est un espace vectoriel de dimension finie n",
    "EF_DIM_FINIE":                "E et F sont de dimension finie",
    "F_INJECTIVE":                "f est injective",
    "F_SURJECTIVE":               "f est surjective",

    # Base incomplète
    "FAMILLE_LIBRE_K_LEQ_N":      "F = (f₁, ..., fₖ) est une famille libre de E avec k ≤ n",
    "FAMILLE_GENERATRICE_E":      "F est une famille génératrice de E",
    "K_EGAL_N":                   "k = n",
    "FAMILLE_EST_BASE":           "F est une base de E",

    # Diagonalisabilité (valeurs propres distinctes)
    "F_ENDOMORPHISME_DIM_FINIE":  "f est un endomorphisme de E (dim finie n)",
    "F_N_VP_DISTINCTES":          "f admet n valeurs propres distinctes",
    "F_N_VP_NON_DISTINCTES":      "f admet n valeurs propres (pas nécessairement distinctes)",
    "POLY_CARAC_SCINDE":          "le polynôme caractéristique est scindé",
    "F_MATRICE_TRIANGULAIRE":     "f est une matrice triangulaire",

    # Cayley-Hamilton
    "A_MATRICE_CARREE_N":         "A est une matrice carrée n×n",
    "CHI_A_POLY_CARACTERISTIQUE": "χ_A est le polynôme caractéristique de A",
    "A_DIAGONALISABLE":           "A est une matrice diagonalisable",
    "CHI_A_POLY_MINIMAL":         "χ_A est le polynôme minimal de A",
    "A_SYMETRIQUE":               "A est une matrice symétrique",

    # Théorème spectral
    "A_MATRICE_REELLE":           "A est une matrice carrée réelle",
    "A_SYMETRIQUE_EGALE_AT":      "A est symétrique (A = Aᵀ)",
    "A_MATRICE_COMPLEXE":         "A est une matrice carrée complexe",
    "A_ANTISYMETRIQUE":           "A est antisymétrique",
    "A_ORTHOGONALE":              "A est orthogonale",

    # Cauchy-Schwarz
    "E_PRODUIT_SCALAIRE":         "E est un espace vectoriel muni d'un produit scalaire",
    "UV_VECTEURS_E":              "u et v sont deux vecteurs de E",
    "E_NORME":                    "E est un espace vectoriel normé",
    "UV_ORTHOGONAUX":             "u et v sont orthogonaux",

    # Projection orthogonale (Hilbert)
    "E_HILBERT":                  "E est un espace de Hilbert",
    "F_SEV_FERME_E":              "F est un sous-espace vectoriel fermé de E",
    "F_SEV_E":                    "F est un sous-espace vectoriel de E (sans fermé)",
    "E_BANACH":                   "E est un espace de Banach",
    "F_DIM_FINIE":                "F est de dimension finie",

    # Bolzano-Weierstrass / suites
    "UN_SUITE_BORNEE":            "(uₙ) est une suite bornée de réels",
    "UN_CROISSANTE":              "(uₙ) est une suite croissante",
    "UN_CAUCHY":                  "(uₙ) est une suite de Cauchy",
    "UN_MONOTONE":                "(uₙ) est une suite monotone",

    # Convergence monotone
    "UN_MAJOREE":                 "(uₙ) est majorée",
    "UN_DECROISSANTE_MAJOREE":    "(uₙ) est une suite décroissante et majorée",
    "UN_BORNEE":                  "(uₙ) est bornée",

    # Suites adjacentes
    "UN_CROISS_VN_DECROISS":      "(uₙ) est croissante et (vₙ) est décroissante",
    "VN_MOINS_UN_TEND_ZERO":      "vₙ − uₙ → 0",
    "UN_VN_TOUTES_CROISSANTES":   "(uₙ) et (vₙ) sont toutes deux croissantes",
    "UN_LEQ_VN":                  "uₙ ≤ vₙ pour tout n",

    # Critère de Cauchy
    "UN_ESPACE_COMPLET":          "(uₙ) est une suite dans un espace complet",
    "UN_ESPACE_NORME_SANS_COMPLET": "(uₙ) est dans un espace vectoriel normé (sans complet)",

    # Convergence dominée
    "FN_MESURABLES":              "(fₙ) est une suite de fonctions mesurables",
    "FN_CONVERGE_PP":             "fₙ → f presque partout",
    "FN_DOMINEE_INTEGRABLE":      "∃ g intégrable telle que |fₙ| ≤ g p.p. pour tout n",
    "FN_CONVERGE_UNIFORMEMENT":   "fₙ → f uniformément",
    "FN_DOMINEE_CONSTANTE":       "|fₙ| ≤ M (constante)",
    "FN_INTEGRABLE_TOUT_N":       "fₙ est intégrable pour tout n",

    # Cauchy-Lipschitz
    "F_CONTINUE_EN_T":            "f est continue en t",
    "F_LIPSCHITZIENNE_EN_Y":      "f est lipschitzienne en y",
    "CONDITION_INITIALE":         "une condition initiale y(t₀) = y₀ est donnée",
    "F_CONTINUE_EN_Y":            "f est continue en y",
    "F_CLASSE_C1_EN_T":           "f est de classe C¹ en t",
    "F_BORNEE":                   "f est bornée",

    # Principe de superposition
    "L_OPERATEUR_LINEAIRE":       "L est un opérateur différentiel linéaire",
    "Y1_SOLUTION_F1":             "y₁ est solution de L(y) = f₁",
    "Y2_SOLUTION_F2":             "y₂ est solution de L(y) = f₂",
    "Y1_Y2_SOLUTIONS_HOMOGENE":   "y₁ et y₂ sont solutions de L(y) = 0",
    "L_OPERATEUR_SANS_LINEAIRE":  "L est un opérateur différentiel (sans linéaire)",
    "L_CONTINU":                  "L est continu",

    # Théorème Central Limite
    "XN_INDEPENDANTES":           "(Xₙ) est une suite de variables aléatoires indépendantes",
    "XN_IID":                     "les Xₙ sont identiquement distribuées",
    "E_X1_FINIE":                 "E[X₁] = μ est finie",
    "VAR_X1_FINIE_POSITIVE":      "Var(X₁) = σ² est finie et strictement positive",
    "XN_INDEP_SANS_IID":          "les Xₙ sont indépendantes (sans identiquement distribuées)",
    "SIGMA2_POSITIF_SANS_FINI":   "σ² > 0 sans mentionner que σ² est finie",
    "XN_LOI_NORMALE":             "les Xₙ suivent une loi normale",

    # Loi des Grands Nombres (faible)
    "E_ABS_X1_FINIE":             "E[|X₁|] est finie",
    "E_X1_CARRE_FINIE":           "E[X₁²] est finie",
    "XN_INDEP_UNIQUEMENT":        "les Xₙ sont indépendantes uniquement",
    "VAR_X1_FINIE":               "Var(X₁) est finie",

    # Inégalité de Jensen
    "PHI_CONVEXE":                "φ est une fonction convexe",
    "X_VA_INTEGRABLE":            "X est une variable aléatoire réelle intégrable",
    "PHI_CONCAVE":                "φ est une fonction concave",
    "X_BORNEE":                   "X est bornée",
    "PHI_CROISSANTE":             "φ est une fonction croissante",

    # Réduction de Jordan
    "A_MATRICE_COMPLEXE_NXN":     "A est une matrice carrée n×n à coefficients complexes",
    "POLY_CARAC_SCINDE_R":        "le polynôme caractéristique de A est scindé sur ℝ",

    # Taylor avec reste de Lagrange
    "F_N_FOIS_DERIVABLE_FERME":   "f est n fois dérivable sur [a, b] (continue)",
    "F_NPLUS1_FOIS_DERIVABLE_OUVERT": "f est n+1 fois dérivable sur ]a, b[",
    "F_NPLUS1_FOIS_DERIVABLE_FERME":  "f est n+1 fois dérivable sur [a, b]",
    "F_CLASSE_CN_UNIQUEMENT":     "f est de classe Cⁿ uniquement",
    "F_ANALYTIQUE":               "f est analytique",
}


def texte(hyp_id):
    return HYPOTHESES[hyp_id]


def textes(hyp_ids):
    return [HYPOTHESES[h] for h in hyp_ids]


if __name__ == "__main__":
    # aucun id dupliqué, tous les ids ont un texte non vide
    assert len(HYPOTHESES) == len(set(HYPOTHESES.keys()))
    for k, v in HYPOTHESES.items():
        assert isinstance(v, str) and len(v) > 0, k
    print(f"{len(HYPOTHESES)} hypothèses cataloguées, OK.")