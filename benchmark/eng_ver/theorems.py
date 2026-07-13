from hypotheses import HYPOTHESES

THEOREMS = {
    "T01": {
        "name": "Rolle's Theorem",
        "hypotheses": [
            "F_CONTINUE_FERME",
            "F_DERIVABLE_OUVERT",
            "F_EGAL_BORNES"
        ],
        "conclusion": "∃ c ∈ ]a, b[ such that f'(c) = 0",
        "common_errors": [
            "F_CONTINUE_OUVERT",
            "F_DERIVABLE_FERME",
            "F_DERIVABLE_BORNES"
        ]
    },

    "T02": {
        "name": "Mean Value Theorem (Lagrange)",
        "hypotheses": [
            "F_CONTINUE_FERME",
            "F_DERIVABLE_OUVERT"
        ],
        "conclusion": "∃ c ∈ ]a, b[ such that f(b) − f(a) = f'(c)(b − a)",
        "common_errors": [
            "F_CONTINUE_OUVERT",
            "F_DERIVABLE_FERME",
            "F_EGAL_BORNES"
        ]
    },

    "T03": {
        "name": "Intermediate Value Theorem",
        "hypotheses": [
            "F_CONTINUE_FERME",
            "Y_ENTRE_BORNES"
        ],
        "conclusion": "∃ c ∈ ]a, b[ such that f(c) = y",
        "common_errors": [
            "F_CONTINUE_OUVERT",
            "F_DERIVABLE_FERME",
            "SIGNES_OPPOSES"
        ]
    },

    "T04": {
        "name": "Weierstrass Theorem",
        "hypotheses": [
            "F_CONTINUE_FERME",
            "INTERVALLE_COMPACT"
        ],
        "conclusion": "f attains its maximum and minimum on [a, b]",
        "common_errors": [
            "F_CONTINUE_OUVERT",
            "F_CONTINUE_R",
            "F_BORNEE_FERME"
        ]
    },

    "T05": {
        "name": "L'Hôpital's Rule",
        "hypotheses": [
            "FG_DERIVABLES_VOISINAGE_A",
            "G_PRIME_NON_NULLE_VOIS_A",
            "FG_LIMITE_ZERO_OU_INFINI",
            "LIM_FPRIME_GPRIME_EXISTE"
        ],
        "conclusion": "lim_{x→a} f(x)/g(x) = ℓ",
        "common_errors": [
            "G_NON_NULLE_VOIS_A",
            "FG_CONTINUES_EN_A",
            "FG_CLASSE_C2_EN_A"
        ]
    },

    "T06": {
        "name": "Taylor-Young Formula",
        "hypotheses": [
            "F_N_FOIS_DERIVABLE_EN_A"
        ],
        "conclusion": "f(x) = Σ_{k=0}^{n} f^(k)(a)/k! · (x−a)^k + o((x−a)^n)",
        "common_errors": [
            "F_CLASSE_CN_VOISINAGE_A",
            "F_NPLUS1_FOIS_DERIVABLE_A",
            "F_ANALYTIQUE_EN_A"
        ]
    },

    "T07": {
        "name": "Fundamental Theorem of Calculus",
        "hypotheses": [
            "F_CONTINUE_FERME"
        ],
        "conclusion": "F(x) = ∫_a^x f(t)dt is differentiable and F'(x) = f(x)",
        "common_errors": [
            "F_INTEGRABLE_FERME",
            "F_CLASSE_C1",
            "F_CONTINUE_OUVERT"
        ]
    },

    "T08": {
        "name": "Integration by Parts",
        "hypotheses": [
            "UV_CLASSE_C1_FERME"
        ],
        "conclusion": "∫_a^b u'v = [uv]_a^b − ∫_a^b uv'",
        "common_errors": [
            "UV_CONTINUES_FERME",
            "UV_CLASSE_C2_FERME",
            "UPRIME_V_CONTINUES_FERME"
        ]
    },

    "T09": {
        "name": "Change of Variable in Integrals",
        "hypotheses": [
            "PHI_CLASSE_C1",
            "F_CONTINUE_PHI_IMAGE"
        ],
        "conclusion": "∫_α^β f(φ(t))φ'(t)dt = ∫_{φ(α)}^{φ(β)} f(x)dx",
        "common_errors": [
            "PHI_CONTINUE",
            "F_DERIVABLE_PHI_IMAGE",
            "PHI_BIJECTIVE"
        ]
    },

    "T10": {
        "name": "d'Alembert's Criterion (series)",
        "hypotheses": [
            "UN_POSITIF_GRAND_N",
            "LIM_RATIO_EXISTE"
        ],
        "conclusion": "ℓ < 1 ⟹ convergence ; ℓ > 1 ⟹ divergence ; ℓ = 1 inconclusive",
        "common_errors": [
            "UN_NON_NUL",
            "LIM_UN_ZERO",
            "SERIE_TERMES_POSITIFS"
        ]
    },

    "T11": {
        "name": "Rank Theorem",
        "hypotheses": [
            "F_LINEAIRE_E_F",
            "E_DIM_FINIE"
        ],
        "conclusion": "dim(Ker f) + dim(Im f) = dim(E)",
        "common_errors": [
            "EF_DIM_FINIE",
            "F_INJECTIVE",
            "F_SURJECTIVE"
        ]
    },

    "T12": {
        "name": "Incomplete Basis Theorem",
        "hypotheses": [
            "E_DIM_FINIE",
            "FAMILLE_LIBRE_K_LEQ_N"
        ],
        "conclusion": "F can be extended to a basis of E",
        "common_errors": [
            "FAMILLE_GENERATRICE_E",
            "K_EGAL_N",
            "FAMILLE_EST_BASE"
        ]
    },

    "T13": {
        "name": "Diagonalizability (distinct eigenvalues)",
        "hypotheses": [
            "F_ENDOMORPHISME_DIM_FINIE",
            "F_N_VP_DISTINCTES"
        ],
        "conclusion": "f is diagonalizable",
        "common_errors": [
            "F_N_VP_NON_DISTINCTES",
            "POLY_CARAC_SCINDE",
            "F_MATRICE_TRIANGULAIRE"
        ]
    },

    "T14": {
        "name": "Cayley-Hamilton Theorem",
        "hypotheses": [
            "A_MATRICE_CARREE_N",
            "CHI_A_POLY_CARACTERISTIQUE"
        ],
        "conclusion": "χ_A(A) = 0",
        "common_errors": [
            "A_DIAGONALISABLE",
            "CHI_A_POLY_MINIMAL",
            "A_SYMETRIQUE"
        ]
    },

    "T15": {
        "name": "Spectral Theorem (real symmetric matrices)",
        "hypotheses": [
            "A_MATRICE_REELLE",
            "A_SYMETRIQUE_EGALE_AT"
        ],
        "conclusion": "A is diagonalizable in an orthonormal basis; eigenvalues are real",
        "common_errors": [
            "A_MATRICE_COMPLEXE",
            "A_ANTISYMETRIQUE",
            "A_ORTHOGONALE"
        ]
    },

    "T16": {
        "name": "Cauchy-Schwarz Inequality",
        "hypotheses": [
            "E_PRODUIT_SCALAIRE",
            "UV_VECTEURS_E"
        ],
        "conclusion": "|⟨u, v⟩|² ≤ ⟨u, u⟩ · ⟨v, v⟩",
        "common_errors": [
            "E_NORME",
            "UV_ORTHOGONAUX",
            "E_DIM_FINIE"
        ]
    },

    "T17": {
        "name": "Orthogonal Projection Theorem (Hilbert)",
        "hypotheses": [
            "E_HILBERT",
            "F_SEV_FERME_E"
        ],
        "conclusion": "Every x ∈ E has a unique decomposition x = p + q with p ∈ F and q ∈ F⊥",
        "common_errors": [
            "F_SEV_E",
            "E_BANACH",
            "F_DIM_FINIE"
        ]
    },

    "T18": {
        "name": "Heine's Theorem (uniform continuity)",
        "hypotheses": [
            "F_CONTINUE_FERME",
            "INTERVALLE_COMPACT"
        ],
        "conclusion": "f is uniformly continuous on [a, b]",
        "common_errors": [
            "F_CONTINUE_OUVERT",
            "F_LIPSCHITZIENNE_FERME",
            "F_UNIF_CONTINUE_R"
        ]
    },

    "T19": {
        "name": "Bolzano-Weierstrass Theorem",
        "hypotheses": [
            "UN_SUITE_BORNEE"
        ],
        "conclusion": "(uₙ) has at least one convergent subsequence",
        "common_errors": [
            "UN_CROISSANTE",
            "UN_CAUCHY",
            "UN_MONOTONE"
        ]
    },

    "T20": {
        "name": "Monotone Convergence Theorem (sequences)",
        "hypotheses": [
            "UN_CROISSANTE",
            "UN_MAJOREE"
        ],
        "conclusion": "(uₙ) converges",
        "common_errors": [
            "UN_DECROISSANTE_MAJOREE",
            "UN_BORNEE",
            "UN_CAUCHY"
        ]
    },

    "T21": {
        "name": "Adjacent Sequences Theorem",
        "hypotheses": [
            "UN_CROISS_VN_DECROISS",
            "VN_MOINS_UN_TEND_ZERO"
        ],
        "conclusion": "(uₙ) and (vₙ) converge to the same limit",
        "common_errors": [
            "UN_VN_TOUTES_CROISSANTES",
            "UN_LEQ_VN",
            "UN_BORNEE"
        ]
    },

    "T22": {
        "name": "Cauchy Criterion (sequences)",
        "hypotheses": [
            "UN_ESPACE_COMPLET"
        ],
        "conclusion": "(uₙ) converges ⟺ (uₙ) is a Cauchy sequence",
        "common_errors": [
            "UN_BORNEE",
            "UN_ESPACE_NORME_SANS_COMPLET",
            "UN_MONOTONE"
        ]
    },

    "T23": {
        "name": "Dominated Convergence Theorem",
        "hypotheses": [
            "FN_MESURABLES",
            "FN_CONVERGE_PP",
            "FN_DOMINEE_INTEGRABLE"
        ],
        "conclusion": "∫fₙ → ∫f",
        "common_errors": [
            "FN_CONVERGE_UNIFORMEMENT",
            "FN_DOMINEE_CONSTANTE",
            "FN_INTEGRABLE_TOUT_N"
        ]
    },

    "T24": {
        "name": "Cauchy-Lipschitz Theorem",
        "hypotheses": [
            "F_CONTINUE_EN_T",
            "F_LIPSCHITZIENNE_EN_Y",
            "CONDITION_INITIALE"
        ],
        "conclusion": "There exists a unique maximal solution to y' = f(t, y)",
        "common_errors": [
            "F_CONTINUE_EN_Y",
            "F_CLASSE_C1_EN_T",
            "F_BORNEE"
        ]
    },

    "T25": {
        "name": "Superposition Principle (linear ODEs)",
        "hypotheses": [
            "L_OPERATEUR_LINEAIRE",
            "Y1_SOLUTION_F1",
            "Y2_SOLUTION_F2"
        ],
        "conclusion": "y₁ + y₂ is a solution of L(y) = f₁ + f₂",
        "common_errors": [
            "Y1_Y2_SOLUTIONS_HOMOGENE",
            "L_OPERATEUR_SANS_LINEAIRE",
            "L_CONTINU"
        ]
    },

    "T26": {
        "name": "Central Limit Theorem",
        "hypotheses": [
            "XN_INDEPENDANTES",
            "XN_IID",
            "E_X1_FINIE",
            "VAR_X1_FINIE_POSITIVE"
        ],
        "conclusion": "√n · (X̄ₙ − μ)/σ → N(0,1) in distribution",
        "common_errors": [
            "XN_INDEP_SANS_IID",
            "SIGMA2_POSITIF_SANS_FINI",
            "XN_LOI_NORMALE"
        ]
    },

    "T27": {
        "name": "Weak Law of Large Numbers",
        "hypotheses": [
            "XN_INDEPENDANTES",
            "XN_IID",
            "E_ABS_X1_FINIE"
        ],
        "conclusion": "X̄ₙ → E[X₁] in probability",
        "common_errors": [
            "E_X1_CARRE_FINIE",
            "XN_INDEP_UNIQUEMENT",
            "VAR_X1_FINIE"
        ]
    },

    "T28": {
        "name": "Jensen's Inequality",
        "hypotheses": [
            "PHI_CONVEXE",
            "X_VA_INTEGRABLE"
        ],
        "conclusion": "φ(E[X]) ≤ E[φ(X)]",
        "common_errors": [
            "PHI_CONCAVE",
            "X_BORNEE",
            "PHI_CROISSANTE"
        ]
    },

    "T29": {
        "name": "Jordan Normal Form (existence)",
        "hypotheses": [
            "A_MATRICE_COMPLEXE_NXN"
        ],
        "conclusion": "A is similar to a Jordan matrix",
        "common_errors": [
            "A_MATRICE_REELLE",
            "A_DIAGONALISABLE",
            "POLY_CARAC_SCINDE_R"
        ]
    },

    "T30": {
        "name": "Taylor's Formula with Lagrange Remainder",
        "hypotheses": [
            "F_N_FOIS_DERIVABLE_FERME",
            "F_NPLUS1_FOIS_DERIVABLE_OUVERT"
        ],
        "conclusion": "∃ c ∈ ]a, b[ such that f(b) = Σ f^(k)(a)/k!·(b-a)^k + f^(n+1)(c)/(n+1)!·(b-a)^(n+1)",
        "common_errors": [
            "F_NPLUS1_FOIS_DERIVABLE_FERME",
            "F_CLASSE_CN_UNIQUEMENT",
            "F_ANALYTIQUE"
        ]
    },
}

# Function to get the text of a hypothesis from its ID
def get_hypothesis_text(hyp_id):
    return HYPOTHESES.get(hyp_id, hyp_id)

# Function to get all hypotheses of a theorem as text
def get_hypotheses_text(theorem_id):
    if theorem_id not in THEOREMS:
        return []
    return [HYPOTHESES.get(h, h) for h in THEOREMS[theorem_id]["hypotheses"]]

if __name__ == "__main__":
    # Check if hypothesis IDs exist
    for t_id, th in THEOREMS.items():
        for h in th["hypotheses"]:
            if h not in HYPOTHESES:
                print(f"Hypothesis '{h}' of theorem {t_id} not found in HYPOTHESES")
        for e in th["common_errors"]:
            if e not in HYPOTHESES:
                print(f"Common error '{e}' of theorem {t_id} not found in HYPOTHESES")
    print("verification complete")