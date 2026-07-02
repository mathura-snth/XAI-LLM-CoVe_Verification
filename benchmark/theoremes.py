from hypotheses import HYPOTHESES

THEOREMES = {
    "T01": {
        "nom": "Théorème de Rolle",
        "hypotheses": [
            "F_CONTINUE_FERME",
            "F_DERIVABLE_OUVERT",
            "F_EGAL_BORNES"
        ],
        "conclusion": "∃ c ∈ ]a, b[ tel que f'(c) = 0",
        "erreurs_courantes": [
            "F_CONTINUE_OUVERT",
            "F_DERIVABLE_FERME",
            "F_DERIVABLE_BORNES"
        ]
    },

    "T02": {
        "nom": "Théorème des Accroissements Finis (Lagrange)",
        "hypotheses": [
            "F_CONTINUE_FERME",
            "F_DERIVABLE_OUVERT"
        ],
        "conclusion": "∃ c ∈ ]a, b[ tel que f(b) − f(a) = f'(c)(b − a)",
        "erreurs_courantes": [
            "F_CONTINUE_OUVERT",
            "F_DERIVABLE_FERME",
            "F_EGAL_BORNES"
        ]
    },

    "T03": {
        "nom": "Théorème des Valeurs Intermédiaires",
        "hypotheses": [
            "F_CONTINUE_FERME",
            "Y_ENTRE_BORNES"
        ],
        "conclusion": "∃ c ∈ ]a, b[ tel que f(c) = y",
        "erreurs_courantes": [
            "F_CONTINUE_OUVERT",
            "F_DERIVABLE_FERME",
            "SIGNES_OPPOSES"
        ]
    },

    "T04": {
        "nom": "Théorème de Weierstrass",
        "hypotheses": [
            "F_CONTINUE_FERME",
            "INTERVALLE_COMPACT"
        ],
        "conclusion": "f atteint son maximum et son minimum sur [a, b]",
        "erreurs_courantes": [
            "F_CONTINUE_OUVERT",
            "F_CONTINUE_R",
            "F_BORNEE_FERME"
        ]
    },

    "T05": {
        "nom": "Règle de L'Hôpital",
        "hypotheses": [
            "FG_DERIVABLES_VOISINAGE_A",
            "G_PRIME_NON_NULLE_VOIS_A",
            "FG_LIMITE_ZERO_OU_INFINI",
            "LIM_FPRIME_GPRIME_EXISTE"
        ],
        "conclusion": "lim_{x→a} f(x)/g(x) = ℓ",
        "erreurs_courantes": [
            "G_NON_NULLE_VOIS_A",
            "FG_CONTINUES_EN_A",
            "FG_CLASSE_C2_EN_A"
        ]
    },

    "T06": {
        "nom": "Formule de Taylor-Young",
        "hypotheses": [
            "F_N_FOIS_DERIVABLE_EN_A"
        ],
        "conclusion": "f(x) = Σ_{k=0}^{n} f^(k)(a)/k! · (x−a)^k + o((x−a)^n)",
        "erreurs_courantes": [
            "F_CLASSE_CN_VOISINAGE_A",
            "F_NPLUS1_FOIS_DERIVABLE_A",
            "F_ANALYTIQUE_EN_A"
        ]
    },

    "T07": {
        "nom": "Théorème Fondamental de l'Analyse",
        "hypotheses": [
            "F_CONTINUE_FERME"
        ],
        "conclusion": "F(x) = ∫_a^x f(t)dt est dérivable et F'(x) = f(x)",
        "erreurs_courantes": [
            "F_INTEGRABLE_FERME",
            "F_CLASSE_C1",
            "F_CONTINUE_OUVERT"
        ]
    },

    "T08": {
        "nom": "Intégration par parties",
        "hypotheses": [
            "UV_CLASSE_C1_FERME"
        ],
        "conclusion": "∫_a^b u'v = [uv]_a^b − ∫_a^b uv'",
        "erreurs_courantes": [
            "UV_CONTINUES_FERME",
            "UV_CLASSE_C2_FERME",
            "UPRIME_V_CONTINUES_FERME"
        ]
    },

    "T09": {
        "nom": "Changement de variable dans une intégrale",
        "hypotheses": [
            "PHI_CLASSE_C1",
            "F_CONTINUE_PHI_IMAGE"
        ],
        "conclusion": "∫_α^β f(φ(t))φ'(t)dt = ∫_{φ(α)}^{φ(β)} f(x)dx",
        "erreurs_courantes": [
            "PHI_CONTINUE",
            "F_DERIVABLE_PHI_IMAGE",
            "PHI_BIJECTIVE"
        ]
    },

    "T10": {
        "nom": "Critère de d'Alembert (séries)",
        "hypotheses": [
            "UN_POSITIF_GRAND_N",
            "LIM_RATIO_EXISTE"
        ],
        "conclusion": "ℓ < 1 ⟹ convergence ; ℓ > 1 ⟹ divergence ; ℓ = 1 non concluant",
        "erreurs_courantes": [
            "UN_NON_NUL",
            "LIM_UN_ZERO",
            "SERIE_TERMES_POSITIFS"
        ]
    },

    "T11": {
        "nom": "Théorème du rang",
        "hypotheses": [
            "F_LINEAIRE_E_F",
            "E_DIM_FINIE"
        ],
        "conclusion": "dim(Ker f) + dim(Im f) = dim(E)",
        "erreurs_courantes": [
            "EF_DIM_FINIE",
            "F_INJECTIVE",
            "F_SURJECTIVE"
        ]
    },

    "T12": {
        "nom": "Théorème de la base incomplète",
        "hypotheses": [
            "E_DIM_FINIE",
            "FAMILLE_LIBRE_K_LEQ_N"
        ],
        "conclusion": "On peut compléter F en une base de E",
        "erreurs_courantes": [
            "FAMILLE_GENERATRICE_E",
            "K_EGAL_N",
            "FAMILLE_EST_BASE"
        ]
    },

    "T13": {
        "nom": "Diagonalisabilité (valeurs propres distinctes)",
        "hypotheses": [
            "F_ENDOMORPHISME_DIM_FINIE",
            "F_N_VP_DISTINCTES"
        ],
        "conclusion": "f est diagonalisable",
        "erreurs_courantes": [
            "F_N_VP_NON_DISTINCTES",
            "POLY_CARAC_SCINDE",
            "F_MATRICE_TRIANGULAIRE"
        ]
    },

    "T14": {
        "nom": "Théorème de Cayley-Hamilton",
        "hypotheses": [
            "A_MATRICE_CARREE_N",
            "CHI_A_POLY_CARACTERISTIQUE"
        ],
        "conclusion": "χ_A(A) = 0",
        "erreurs_courantes": [
            "A_DIAGONALISABLE",
            "CHI_A_POLY_MINIMAL",
            "A_SYMETRIQUE"
        ]
    },

    "T15": {
        "nom": "Théorème spectral (matrices symétriques réelles)",
        "hypotheses": [
            "A_MATRICE_REELLE",
            "A_SYMETRIQUE_EGALE_AT"
        ],
        "conclusion": "A est diagonalisable dans une base orthonormée ; valeurs propres réelles",
        "erreurs_courantes": [
            "A_MATRICE_COMPLEXE",
            "A_ANTISYMETRIQUE",
            "A_ORTHOGONALE"
        ]
    },

    "T16": {
        "nom": "Inégalité de Cauchy-Schwarz",
        "hypotheses": [
            "E_PRODUIT_SCALAIRE",
            "UV_VECTEURS_E"
        ],
        "conclusion": "|⟨u, v⟩|² ≤ ⟨u, u⟩ · ⟨v, v⟩",
        "erreurs_courantes": [
            "E_NORME",
            "UV_ORTHOGONAUX",
            "E_DIM_FINIE"
        ]
    },

    "T17": {
        "nom": "Projection orthogonale (Hilbert)",
        "hypotheses": [
            "E_HILBERT",
            "F_SEV_FERME_E"
        ],
        "conclusion": "Tout x ∈ E s'écrit de façon unique x = p + q avec p ∈ F et q ∈ F⊥",
        "erreurs_courantes": [
            "F_SEV_E",
            "E_BANACH",
            "F_DIM_FINIE"
        ]
    },

    "T18": {
        "nom": "Théorème de Heine (continuité uniforme)",
        "hypotheses": [
            "F_CONTINUE_FERME",
            "INTERVALLE_COMPACT"
        ],
        "conclusion": "f est uniformément continue sur [a, b]",
        "erreurs_courantes": [
            "F_CONTINUE_OUVERT",
            "F_LIPSCHITZIENNE_FERME",
            "F_UNIF_CONTINUE_R"
        ]
    },

    "T19": {
        "nom": "Théorème de Bolzano-Weierstrass",
        "hypotheses": [
            "UN_SUITE_BORNEE"
        ],
        "conclusion": "(uₙ) admet au moins une sous-suite convergente",
        "erreurs_courantes": [
            "UN_CROISSANTE",
            "UN_CAUCHY",
            "UN_MONOTONE"
        ]
    },

    "T20": {
        "nom": "Théorème de convergence monotone (suites)",
        "hypotheses": [
            "UN_CROISSANTE",
            "UN_MAJOREE"
        ],
        "conclusion": "(uₙ) converge",
        "erreurs_courantes": [
            "UN_DECROISSANTE_MAJOREE",
            "UN_BORNEE",
            "UN_CAUCHY"
        ]
    },

    "T21": {
        "nom": "Théorème des suites adjacentes",
        "hypotheses": [
            "UN_CROISS_VN_DECROISS",
            "VN_MOINS_UN_TEND_ZERO"
        ],
        "conclusion": "(uₙ) et (vₙ) convergent vers la même limite",
        "erreurs_courantes": [
            "UN_VN_TOUTES_CROISSANTES",
            "UN_LEQ_VN",
            "UN_BORNEE"
        ]
    },

    "T22": {
        "nom": "Critère de Cauchy (suites)",
        "hypotheses": [
            "UN_ESPACE_COMPLET"
        ],
        "conclusion": "(uₙ) converge ⟺ (uₙ) est une suite de Cauchy",
        "erreurs_courantes": [
            "UN_BORNEE",
            "UN_ESPACE_NORME_SANS_COMPLET",
            "UN_MONOTONE"
        ]
    },

    "T23": {
        "nom": "Théorème de convergence dominée",
        "hypotheses": [
            "FN_MESURABLES",
            "FN_CONVERGE_PP",
            "FN_DOMINEE_INTEGRABLE"
        ],
        "conclusion": "∫fₙ → ∫f",
        "erreurs_courantes": [
            "FN_CONVERGE_UNIFORMEMENT",
            "FN_DOMINEE_CONSTANTE",
            "FN_INTEGRABLE_TOUT_N"
        ]
    },

    "T24": {
        "nom": "Théorème de Cauchy-Lipschitz",
        "hypotheses": [
            "F_CONTINUE_EN_T",
            "F_LIPSCHITZIENNE_EN_Y",
            "CONDITION_INITIALE"
        ],
        "conclusion": "Il existe une unique solution maximale au problème y' = f(t, y)",
        "erreurs_courantes": [
            "F_CONTINUE_EN_Y",
            "F_CLASSE_C1_EN_T",
            "F_BORNEE"
        ]
    },

    "T25": {
        "nom": "Principe de superposition (EDO linéaires)",
        "hypotheses": [
            "L_OPERATEUR_LINEAIRE",
            "Y1_SOLUTION_F1",
            "Y2_SOLUTION_F2"
        ],
        "conclusion": "y₁ + y₂ est solution de L(y) = f₁ + f₂",
        "erreurs_courantes": [
            "Y1_Y2_SOLUTIONS_HOMOGENE",
            "L_OPERATEUR_SANS_LINEAIRE",
            "L_CONTINU"
        ]
    },

    "T26": {
        "nom": "Théorème Central Limite",
        "hypotheses": [
            "XN_INDEPENDANTES",
            "XN_IID",
            "E_X1_FINIE",
            "VAR_X1_FINIE_POSITIVE"
        ],
        "conclusion": "√n · (X̄ₙ − μ)/σ → N(0,1) en loi",
        "erreurs_courantes": [
            "XN_INDEP_SANS_IID",
            "SIGMA2_POSITIF_SANS_FINI",
            "XN_LOI_NORMALE"
        ]
    },

    "T27": {
        "nom": "Loi des Grands Nombres (faible)",
        "hypotheses": [
            "XN_INDEPENDANTES",
            "XN_IID",
            "E_ABS_X1_FINIE"
        ],
        "conclusion": "X̄ₙ → E[X₁] en probabilité",
        "erreurs_courantes": [
            "E_X1_CARRE_FINIE",
            "XN_INDEP_UNIQUEMENT",
            "VAR_X1_FINIE"
        ]
    },

    "T28": {
        "nom": "Inégalité de Jensen",
        "hypotheses": [
            "PHI_CONVEXE",
            "X_VA_INTEGRABLE"
        ],
        "conclusion": "φ(E[X]) ≤ E[φ(X)]",
        "erreurs_courantes": [
            "PHI_CONCAVE",
            "X_BORNEE",
            "PHI_CROISSANTE"
        ]
    },

    "T29": {
        "nom": "Réduction de Jordan (existence)",
        "hypotheses": [
            "A_MATRICE_COMPLEXE_NXN"
        ],
        "conclusion": "A est semblable à une matrice de Jordan",
        "erreurs_courantes": [
            "A_MATRICE_REELLE",
            "A_DIAGONALISABLE",
            "POLY_CARAC_SCINDE_R"
        ]
    },

    "T30": {
        "nom": "Formule de Taylor avec reste de Lagrange",
        "hypotheses": [
            "F_N_FOIS_DERIVABLE_FERME",
            "F_NPLUS1_FOIS_DERIVABLE_OUVERT"
        ],
        "conclusion": "∃ c ∈ ]a, b[ tel que f(b) = Σ f^(k)(a)/k!·(b-a)^k + f^(n+1)(c)/(n+1)!·(b-a)^(n+1)",
        "erreurs_courantes": [
            "F_NPLUS1_FOIS_DERIVABLE_FERME",
            "F_CLASSE_CN_UNIQUEMENT",
            "F_ANALYTIQUE"
        ]
    },
}

# Fonction pour obtenir le texte d'une hypothèse à partir de son ID
def get_hypothese_texte(hyp_id):
    return HYPOTHESES.get(hyp_id, hyp_id)

# Fonction pour avoir toutes les hypothèses d'un théorème en texte
def get_hypotheses_texte(theoreme_id):
    if theoreme_id not in THEOREMES:
        return []
    return [HYPOTHESES.get(h, h) for h in THEOREMES[theoreme_id]["hypotheses"]]

if __name__ == "__main__":
    # on vérifie si les IDs d'hypothèses existent
    for t_id, th in THEOREMES.items():
        for h in th["hypotheses"]:
            if h not in HYPOTHESES:
                print(f"Hypothèse '{h}' du théorème {t_id} non trouvée dans HYPOTHESES")
        for e in th["erreurs_courantes"]:
            if e not in HYPOTHESES:
                print(f"Erreur courante '{e}' du théorème {t_id} non trouvée dans HYPOTHESES")
    print("Vérification terminée.")