# Collection of hypotheses as identifiers.
# id -> text displayed in generated copies / LLM prompts
# Comparison should never be done on text, only on id.

HYPOTHESES = {
    "F_CONTINUE_EN_A":            "f is continuous at a",
    "F_DERIVABLE_EN_A":           "f is differentiable at a",
    "F_CONTINUE_FERME":           "f is continuous on [a, b]",
    "F_CONTINUE_OUVERT":          "f is continuous on ]a, b[",
    "F_CONTINUE_R":               "f is continuous on ℝ",
    "F_DERIVABLE_FERME":          "f is differentiable on [a, b]",
    "F_DERIVABLE_OUVERT":         "f is differentiable on ]a, b[",
    "F_DERIVABLE_BORNES":         "f is differentiable at a and b",
    "F_CLASSE_C1":                "f is of class C¹ on I",
    "F_CLASSE_C2":                "f is of class C² on I",
    "F_CLASSE_CN":                "f is of class Cⁿ on I",
    "F_BORNEE_FERME":             "f is bounded on [a, b]",
    "F_INTEGRABLE_FERME":         "f is integrable on [a, b]",
    "F_LIPSCHITZIENNE_FERME":     "f is Lipschitz on [a, b]",
    "F_UNIF_CONTINUE_FERME":      "f is uniformly continuous on [a, b]",
    "F_UNIF_CONTINUE_R":          "f is uniformly continuous on ℝ",

    # Rolle / Lagrange / IVT
    "F_EGAL_BORNES":              "f(a) = f(b)",
    "Y_ENTRE_BORNES":             "y is between f(a) and f(b)",
    "SIGNES_OPPOSES":             "f(a) and f(b) have strictly opposite signs",

    # Weierstrass
    "INTERVALLE_COMPACT":         "[a, b] is a closed and bounded interval",
    "INTERVALLE_FERME_BORNE":     "[a, b] is closed and bounded",
    
    # L'Hôpital's Rule
    "FG_DERIVABLES_VOISINAGE_A":  "f and g are differentiable in a neighborhood of a",
    "G_PRIME_NON_NULLE_VOIS_A":   "g'(x) ≠ 0 in a neighborhood of a",
    "G_NON_NULLE_VOIS_A":         "g(x) ≠ 0 in a neighborhood of a",
    "FG_LIMITE_ZERO_OU_INFINI":   "f(a) = g(a) = 0 or f and g tend to ±∞",
    "LIM_FPRIME_GPRIME_EXISTE":   "lim_{x→a} f'(x)/g'(x) = ℓ exists",
    "FG_CONTINUES_EN_A":          "f and g are continuous at a",
    "FG_CLASSE_C2_EN_A":          "f and g are of class C² at a",

    # Taylor-Young
    "F_N_FOIS_DERIVABLE_EN_A":    "f is n times differentiable at a",
    "F_CLASSE_CN_VOISINAGE_A":    "f is of class Cⁿ in a neighborhood of a",
    "F_NPLUS1_FOIS_DERIVABLE_A":  "f is n+1 times differentiable at a",
    "F_ANALYTIQUE_EN_A":          "f is analytic at a",

    # Integration by parts
    "UV_CLASSE_C1_FERME":         "u and v are of class C¹ on [a, b]",
    "UV_CONTINUES_FERME":         "u and v are continuous on [a, b]",
    "UV_CLASSE_C2_FERME":         "u and v are of class C² on [a, b]",
    "UPRIME_V_CONTINUES_FERME":   "u' and v are continuous on [a, b]",

    # Change of variable in integrals
    "PHI_CLASSE_C1":              "φ is of class C¹ on [α, β]",
    "F_CONTINUE_PHI_IMAGE":       "f is continuous on φ([α, β])",
    "PHI_CONTINUE":               "φ is continuous on [α, β]",
    "F_DERIVABLE_PHI_IMAGE":      "f is differentiable on φ([α, β])",
    "PHI_BIJECTIVE":              "φ is bijective on [α, β]",

    # d'Alembert's criterion (series)
    "UN_POSITIF_GRAND_N":         "uₙ > 0 for all n sufficiently large",
    "LIM_RATIO_EXISTE":           "lim_{n→∞} u_{n+1}/uₙ = ℓ exists",
    "UN_NON_NUL":                 "uₙ ≠ 0 for all n",
    "LIM_UN_ZERO":                "lim uₙ = 0",
    "SERIE_TERMES_POSITIFS":      "the series has only positive terms",

    # Rank theorem
    "F_LINEAIRE_E_F":             "f is a linear map from E to F",
    "E_DIM_FINIE":                "E is a finite-dimensional vector space of dimension n",
    "EF_DIM_FINIE":               "E and F are finite-dimensional",
    "F_INJECTIVE":                "f is injective",
    "F_SURJECTIVE":               "f is surjective",

    # Incomplete basis theorem
    "FAMILLE_LIBRE_K_LEQ_N":      "F = (f₁, ..., fₖ) is a linearly independent family in E with k ≤ n",
    "FAMILLE_GENERATRICE_E":      "F is a spanning family of E",
    "K_EGAL_N":                   "k = n",
    "FAMILLE_EST_BASE":           "F is a basis of E",

    # Diagonalizability (distinct eigenvalues)
    "F_ENDOMORPHISME_DIM_FINIE":  "f is an endomorphism of E (finite dimension n)",
    "F_N_VP_DISTINCTES":          "f has n distinct eigenvalues",
    "F_N_VP_NON_DISTINCTES":      "f has n eigenvalues (not necessarily distinct)",
    "POLY_CARAC_SCINDE":          "the characteristic polynomial is split",
    "F_MATRICE_TRIANGULAIRE":     "f is a triangular matrix",

    # Cayley-Hamilton
    "A_MATRICE_CARREE_N":         "A is an n×n square matrix",
    "CHI_A_POLY_CARACTERISTIQUE": "χ_A is the characteristic polynomial of A",
    "A_DIAGONALISABLE":           "A is a diagonalizable matrix",
    "CHI_A_POLY_MINIMAL":         "χ_A is the minimal polynomial of A",
    "A_SYMETRIQUE":               "A is a symmetric matrix",

    # Spectral theorem
    "A_MATRICE_REELLE":           "A is a real square matrix",
    "A_SYMETRIQUE_EGALE_AT":      "A is symmetric (A = Aᵀ)",
    "A_MATRICE_COMPLEXE":         "A is a complex square matrix",
    "A_ANTISYMETRIQUE":           "A is antisymmetric",
    "A_ORTHOGONALE":              "A is orthogonal",

    # Cauchy-Schwarz
    "E_PRODUIT_SCALAIRE":         "E is a vector space with an inner product",
    "UV_VECTEURS_E":              "u and v are two vectors in E",
    "E_NORME":                    "E is a normed vector space",
    "UV_ORTHOGONAUX":             "u and v are orthogonal",

    # Orthogonal projection (Hilbert)
    "E_HILBERT":                  "E is a Hilbert space",
    "F_SEV_FERME_E":              "F is a closed subspace of E",
    "F_SEV_E":                    "F is a subspace of E (not necessarily closed)",
    "E_BANACH":                   "E is a Banach space",
    "F_DIM_FINIE":                "F is finite-dimensional",

    # Bolzano-Weierstrass / sequences
    "UN_SUITE_BORNEE":            "(uₙ) is a bounded sequence of reals",
    "UN_CROISSANTE":              "(uₙ) is an increasing sequence",
    "UN_CAUCHY":                  "(uₙ) is a Cauchy sequence",
    "UN_MONOTONE":                "(uₙ) is a monotone sequence",

    # Monotone convergence
    "UN_MAJOREE":                 "(uₙ) is bounded above",
    "UN_DECROISSANTE_MAJOREE":    "(uₙ) is a decreasing and bounded above sequence",
    "UN_BORNEE":                  "(uₙ) is bounded",

    # Adjacent sequences
    "UN_CROISS_VN_DECROISS":      "(uₙ) is increasing and (vₙ) is decreasing",
    "VN_MOINS_UN_TEND_ZERO":      "vₙ − uₙ → 0",
    "UN_VN_TOUTES_CROISSANTES":   "(uₙ) and (vₙ) are both increasing",
    "UN_LEQ_VN":                  "uₙ ≤ vₙ for all n",

    # Cauchy criterion
    "UN_ESPACE_COMPLET":          "(uₙ) is a sequence in a complete space",
    "UN_ESPACE_NORME_SANS_COMPLET": "(uₙ) is in a normed vector space (not necessarily complete)",

    # Dominated convergence
    "FN_MESURABLES":              "(fₙ) is a sequence of measurable functions",
    "FN_CONVERGE_PP":             "fₙ → f almost everywhere",
    "FN_DOMINEE_INTEGRABLE":      "∃ g integrable such that |fₙ| ≤ g a.e. for all n",
    "FN_CONVERGE_UNIFORMEMENT":   "fₙ → f uniformly",
    "FN_DOMINEE_CONSTANTE":       "|fₙ| ≤ M (constant)",
    "FN_INTEGRABLE_TOUT_N":       "fₙ is integrable for all n",

    # Cauchy-Lipschitz
    "F_CONTINUE_EN_T":            "f is continuous in t",
    "F_LIPSCHITZIENNE_EN_Y":      "f is Lipschitz in y",
    "CONDITION_INITIALE":         "an initial condition y(t₀) = y₀ is given",
    "F_CONTINUE_EN_Y":            "f is continuous in y",
    "F_CLASSE_C1_EN_T":           "f is of class C¹ in t",
    "F_BORNEE":                   "f is bounded",

    # Superposition principle
    "L_OPERATEUR_LINEAIRE":       "L is a linear differential operator",
    "Y1_SOLUTION_F1":             "y₁ is a solution of L(y) = f₁",
    "Y2_SOLUTION_F2":             "y₂ is a solution of L(y) = f₂",
    "Y1_Y2_SOLUTIONS_HOMOGENE":   "y₁ and y₂ are solutions of L(y) = 0",
    "L_OPERATEUR_SANS_LINEAIRE":  "L is a differential operator (not necessarily linear)",
    "L_CONTINU":                  "L is continuous",

    # Central Limit Theorem
    "XN_INDEPENDANTES":           "(Xₙ) is a sequence of independent random variables",
    "XN_IID":                     "the Xₙ are identically distributed",
    "E_X1_FINIE":                 "E[X₁] = μ is finite",
    "VAR_X1_FINIE_POSITIVE":      "Var(X₁) = σ² is finite and strictly positive",
    "XN_INDEP_SANS_IID":          "the Xₙ are independent (not identically distributed)",
    "SIGMA2_POSITIF_SANS_FINI":   "σ² > 0 without mentioning that σ² is finite",
    "XN_LOI_NORMALE":             "the Xₙ follow a normal distribution",

    # Weak Law of Large Numbers
    "E_ABS_X1_FINIE":             "E[|X₁|] is finite",
    "E_X1_CARRE_FINIE":           "E[X₁²] is finite",
    "XN_INDEP_UNIQUEMENT":        "the Xₙ are independent only",
    "VAR_X1_FINIE":               "Var(X₁) is finite",

    # Jensen's inequality
    "PHI_CONVEXE":                "φ is a convex function",
    "X_VA_INTEGRABLE":            "X is an integrable real random variable",
    "PHI_CONCAVE":                "φ is a concave function",
    "X_BORNEE":                   "X is bounded",
    "PHI_CROISSANTE":             "φ is an increasing function",

    # Jordan normal form
    "A_MATRICE_COMPLEXE_NXN":     "A is an n×n complex square matrix",
    "POLY_CARAC_SCINDE_R":        "the characteristic polynomial of A splits over ℝ",

    # Taylor with Lagrange remainder
    "F_N_FOIS_DERIVABLE_FERME":   "f is n times differentiable on [a, b] (continuous)",
    "F_NPLUS1_FOIS_DERIVABLE_OUVERT": "f is n+1 times differentiable on ]a, b[",
    "F_NPLUS1_FOIS_DERIVABLE_FERME":  "f is n+1 times differentiable on [a, b]",
    "F_CLASSE_CN_UNIQUEMENT":     "f is of class Cⁿ only",
    "F_ANALYTIQUE":               "f is analytic",
}


def text(hyp_id):
    return HYPOTHESES[hyp_id]


def texts(hyp_ids):
    return [HYPOTHESES[h] for h in hyp_ids]


if __name__ == "__main__":
    # no duplicate ids, all ids have non-empty text
    assert len(HYPOTHESES) == len(set(HYPOTHESES.keys()))
    for k, v in HYPOTHESES.items():
        assert isinstance(v, str) and len(v) > 0, k
    print(f"{len(HYPOTHESES)} hypotheses catalogued, OK.")