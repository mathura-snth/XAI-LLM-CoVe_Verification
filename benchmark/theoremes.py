THEOREMES = {
    "T01": {
        "nom": "Théorème de Rolle",
        "domaine": "Analyse",
        "hypotheses": [
            "f est continue sur [a, b]",
            "f est dérivable sur ]a, b[",
            "f(a) = f(b)"
        ],
        "conclusion": "∃ c ∈ ]a, b[ tel que f'(c) = 0",
        "erreurs_courantes": [
            "f est continue sur ]a, b[",
            "f est dérivable sur [a, b]",
            "f est dérivable en a et b",
        ]
    },

    "T02": {
        "nom": "Théorème des Accroissements Finis (Lagrange)",
        "domaine": "Analyse",
        "hypotheses": [
            "f est continue sur [a, b]",
            "f est dérivable sur ]a, b["
        ],
        "conclusion": "∃ c ∈ ]a, b[ tel que f(b) − f(a) = f'(c)(b − a)",
        "erreurs_courantes": [
            "f est continue sur ]a, b[",
            "f est dérivable sur [a, b]",
            "f(a) = f(b)",  # hypothèse de Rolle glissée ici
        ]
    },

    "T03": {
        "nom": "Théorème des Valeurs Intermédiaires",
        "domaine": "Analyse",
        "hypotheses": [
            "f est continue sur [a, b]",
            "y est compris entre f(a) et f(b)"
        ],
        "conclusion": "∃ c ∈ ]a, b[ tel que f(c) = y",
        "erreurs_courantes": [
            "f est continue sur ]a, b[",
            "f est dérivable sur [a, b]",
            "f(a) et f(b) sont de signes strictement opposés",
        ]
    },

    "T04": {
        "nom": "Théorème de Weierstrass",
        "domaine": "Analyse",
        "hypotheses": [
            "f est continue sur [a, b]",
            "[a, b] est un intervalle fermé et borné"
        ],
        "conclusion": "f atteint son maximum et son minimum sur [a, b]",
        "erreurs_courantes": [
            "f est continue sur ]a, b[",
            "f est continue sur ℝ",
            "f est bornée sur [a, b]",
        ]
    },

    "T05": {
        "nom": "Règle de L'Hôpital",
        "domaine": "Analyse",
        "hypotheses": [
            "f et g sont dérivables au voisinage de a",
            "g'(x) ≠ 0 au voisinage de a",
            "f(a) = g(a) = 0 ou f et g tendent vers ±∞",
            "lim_{x→a} f'(x)/g'(x) = ℓ existe"
        ],
        "conclusion": "lim_{x→a} f(x)/g(x) = ℓ",
        "erreurs_courantes": [
            "g(x) ≠ 0 au voisinage de a",
            "f et g sont continues en a",
            "f et g sont de classe C² en a",
        ]
    },

    "T06": {
        "nom": "Formule de Taylor-Young",
        "domaine": "Analyse",
        "hypotheses": [
            "f est n fois dérivable en a"
        ],
        "conclusion": "f(x) = Σ_{k=0}^{n} f^(k)(a)/k! · (x−a)^k + o((x−a)^n)",
        "erreurs_courantes": [
            "f est de classe Cⁿ au voisinage de a",
            "f est n+1 fois dérivable en a",
            "f est analytique en a",
        ]
    },

    "T07": {
        "nom": "Théorème Fondamental de l'Analyse",
        "domaine": "Analyse",
        "hypotheses": [
            "f est continue sur [a, b]"
        ],
        "conclusion": "F(x) = ∫_a^x f(t)dt est dérivable et F'(x) = f(x)",
        "erreurs_courantes": [
            "f est intégrable sur [a, b]",
            "f est de classe C¹ sur [a, b]",
            "f est continue sur ]a, b[",
        ]
    },

    "T08": {
        "nom": "Intégration par parties",
        "domaine": "Analyse",
        "hypotheses": [
            "u et v sont de classe C¹ sur [a, b]"
        ],
        "conclusion": "∫_a^b u'v = [uv]_a^b − ∫_a^b uv'",
        "erreurs_courantes": [
            "u et v sont continues sur [a, b]",
            "u et v sont de classe C² sur [a, b]",
            "u' et v sont continues sur [a, b]",
        ]
    },

    "T09": {
        "nom": "Changement de variable dans une intégrale",
        "domaine": "Analyse",
        "hypotheses": [
            "φ est de classe C¹ sur [α, β]",
            "f est continue sur φ([α, β])"
        ],
        "conclusion": "∫_α^β f(φ(t))φ'(t)dt = ∫_{φ(α)}^{φ(β)} f(x)dx",
        "erreurs_courantes": [
            "φ est continue sur [α, β]",
            "f est dérivable sur φ([α, β])",
            "φ est bijective sur [α, β]",
        ]
    },

    "T10": {
        "nom": "Critère de d'Alembert (séries)",
        "domaine": "Séries",
        "hypotheses": [
            "uₙ > 0 pour tout n suffisamment grand",
            "lim_{n→∞} u_{n+1}/uₙ = ℓ existe"
        ],
        "conclusion": "ℓ < 1 ⟹ convergence ; ℓ > 1 ⟹ divergence ; ℓ = 1 non concluant",
        "erreurs_courantes": [
            "uₙ ≠ 0 pour tout n",
            "lim uₙ = 0",
            "la série est à termes positifs uniquement",
        ]
    },

    "T11": {
        "nom": "Théorème du rang",
        "domaine": "Algèbre Linéaire",
        "hypotheses": [
            "f est une application linéaire de E vers F",
            "E est un espace vectoriel de dimension finie n"
        ],
        "conclusion": "dim(Ker f) + dim(Im f) = dim(E)",
        "erreurs_courantes": [
            "E et F sont de dimension finie",
            "f est injective",
            "f est surjective",
        ]
    },

    "T12": {
        "nom": "Théorème de la base incomplète",
        "domaine": "Algèbre Linéaire",
        "hypotheses": [
            "E est un espace vectoriel de dimension finie n",
            "F = (f₁, ..., fₖ) est une famille libre de E avec k ≤ n"
        ],
        "conclusion": "On peut compléter F en une base de E",
        "erreurs_courantes": [
            "F est une famille génératrice de E",
            "k = n",
            "F est une base de E",
        ]
    },

    "T13": {
        "nom": "Diagonalisabilité (valeurs propres distinctes)",
        "domaine": "Algèbre Linéaire",
        "hypotheses": [
            "f est un endomorphisme de E (dim finie n)",
            "f admet n valeurs propres distinctes"
        ],
        "conclusion": "f est diagonalisable",
        "erreurs_courantes": [
            "f admet n valeurs propres (pas nécessairement distinctes)",
            "le polynôme caractéristique est scindé",
            "f est une matrice triangulaire",
        ]
    },

    "T14": {
        "nom": "Théorème de Cayley-Hamilton",
        "domaine": "Algèbre Linéaire",
        "hypotheses": [
            "A est une matrice carrée n×n",
            "χ_A est le polynôme caractéristique de A"
        ],
        "conclusion": "χ_A(A) = 0",
        "erreurs_courantes": [
            "A est une matrice diagonalisable",
            "χ_A est le polynôme minimal de A",
            "A est une matrice symétrique",
        ]
    },

    "T15": {
        "nom": "Théorème spectral (matrices symétriques réelles)",
        "domaine": "Algèbre Linéaire",
        "hypotheses": [
            "A est une matrice carrée réelle",
            "A est symétrique (A = Aᵀ)"
        ],
        "conclusion": "A est diagonalisable dans une base orthonormée ; valeurs propres réelles",
        "erreurs_courantes": [
            "A est une matrice carrée complexe",
            "A est antisymétrique",
            "A est orthogonale",
        ]
    },

    "T16": {
        "nom": "Inégalité de Cauchy-Schwarz",
        "domaine": "Algèbre Linéaire",
        "hypotheses": [
            "E est un espace vectoriel muni d'un produit scalaire",
            "u et v sont deux vecteurs de E"
        ],
        "conclusion": "|⟨u, v⟩|² ≤ ⟨u, u⟩ · ⟨v, v⟩",
        "erreurs_courantes": [
            "E est un espace vectoriel normé",
            "u et v sont orthogonaux",
            "E est de dimension finie",
        ]
    },

    "T17": {
        "nom": "Projection orthogonale (Hilbert)",
        "domaine": "Algèbre Linéaire",
        "hypotheses": [
            "E est un espace de Hilbert",
            "F est un sous-espace vectoriel fermé de E"
        ],
        "conclusion": "Tout x ∈ E s'écrit de façon unique x = p + q avec p ∈ F et q ∈ F⊥",
        "erreurs_courantes": [
            "F est un sous-espace vectoriel de E (sans fermé)",
            "E est un espace de Banach",
            "F est de dimension finie",
        ]
    },

    "T18": {
        "nom": "Théorème de Heine (continuité uniforme)",
        "domaine": "Topologie",
        "hypotheses": [
            "f est continue sur [a, b]",
            "[a, b] est un compact (fermé borné de ℝ)"
        ],
        "conclusion": "f est uniformément continue sur [a, b]",
        "erreurs_courantes": [
            "f est continue sur ]a, b[",
            "f est lipschitzienne sur [a, b]",
            "f est uniformément continue sur ℝ",
        ]
    },

    "T19": {
        "nom": "Théorème de Bolzano-Weierstrass",
        "domaine": "Topologie",
        "hypotheses": [
            "(uₙ) est une suite bornée de réels"
        ],
        "conclusion": "(uₙ) admet au moins une sous-suite convergente",
        "erreurs_courantes": [
            "(uₙ) est une suite croissante",
            "(uₙ) est une suite de Cauchy",
            "(uₙ) est une suite monotone",
        ]
    },

    "T20": {
        "nom": "Théorème de convergence monotone (suites)",
        "domaine": "Suites",
        "hypotheses": [
            "(uₙ) est une suite croissante",
            "(uₙ) est majorée"
        ],
        "conclusion": "(uₙ) converge",
        "erreurs_courantes": [
            "(uₙ) est une suite décroissante et majorée",
            "(uₙ) est bornée",
            "(uₙ) est une suite de Cauchy",
        ]
    },

    "T21": {
        "nom": "Théorème des suites adjacentes",
        "domaine": "Suites",
        "hypotheses": [
            "(uₙ) est croissante et (vₙ) est décroissante",
            "vₙ − uₙ → 0"
        ],
        "conclusion": "(uₙ) et (vₙ) convergent vers la même limite",
        "erreurs_courantes": [
            "(uₙ) et (vₙ) sont toutes deux croissantes",
            "uₙ ≤ vₙ pour tout n",
            "(uₙ) est bornée",
        ]
    },

    "T22": {
        "nom": "Critère de Cauchy (suites)",
        "domaine": "Suites",
        "hypotheses": [
            "(uₙ) est une suite dans un espace complet"
        ],
        "conclusion": "(uₙ) converge ⟺ (uₙ) est une suite de Cauchy",
        "erreurs_courantes": [
            "(uₙ) est une suite bornée",
            "(uₙ) est dans un espace vectoriel normé (sans complet)",
            "(uₙ) est monotone",
        ]
    },

    "T23": {
        "nom": "Théorème de convergence dominée",
        "domaine": "Intégration",
        "hypotheses": [
            "(fₙ) est une suite de fonctions mesurables",
            "fₙ → f presque partout",
            "∃ g intégrable telle que |fₙ| ≤ g p.p. pour tout n"
        ],
        "conclusion": "∫fₙ → ∫f",
        "erreurs_courantes": [
            "fₙ → f uniformément",
            "|fₙ| ≤ M (constante)",
            "fₙ est intégrable pour tout n",
        ]
    },

    "T24": {
        "nom": "Théorème de Cauchy-Lipschitz",
        "domaine": "Équations Différentielles",
        "hypotheses": [
            "f est continue en t",
            "f est lipschitzienne en y",
            "Une condition initiale y(t₀) = y₀ est donnée"
        ],
        "conclusion": "Il existe une unique solution maximale au problème y' = f(t, y)",
        "erreurs_courantes": [
            "f est continue en y",
            "f est de classe C¹ en t",
            "f est bornée",
        ]
    },

    "T25": {
        "nom": "Principe de superposition (EDO linéaires)",
        "domaine": "Équations Différentielles",
        "hypotheses": [
            "L est un opérateur différentiel linéaire",
            "y₁ est solution de L(y) = f₁",
            "y₂ est solution de L(y) = f₂"
        ],
        "conclusion": "y₁ + y₂ est solution de L(y) = f₁ + f₂",
        "erreurs_courantes": [
            "y₁ et y₂ sont solutions de L(y) = 0",
            "L est un opérateur différentiel (sans linéaire)",
            "L est continu",
        ]
    },

    "T26": {
        "nom": "Théorème Central Limite",
        "domaine": "Probabilités",
        "hypotheses": [
            "(Xₙ) est une suite de variables aléatoires indépendantes",
            "Les Xₙ sont identiquement distribuées",
            "E[X₁] = μ est finie",
            "Var(X₁) = σ² est finie et strictement positive"
        ],
        "conclusion": "√n · (X̄ₙ − μ)/σ → N(0,1) en loi",
        "erreurs_courantes": [
            "les Xₙ sont indépendantes (sans identiquement distribuées)",
            "σ² > 0 sans mentionner que σ² est finie",
            "les Xₙ suivent une loi normale",
        ]
    },

    "T27": {
        "nom": "Loi des Grands Nombres (faible)",
        "domaine": "Probabilités",
        "hypotheses": [
            "(Xₙ) est une suite de variables aléatoires indépendantes",
            "Les Xₙ sont identiquement distribuées",
            "E[|X₁|] est finie"
        ],
        "conclusion": "X̄ₙ → E[X₁] en probabilité",
        "erreurs_courantes": [
            "E[X₁²] est finie",
            "les Xₙ sont indépendantes uniquement",
            "Var(X₁) est finie",
        ]
    },

    "T28": {
        "nom": "Inégalité de Jensen",
        "domaine": "Probabilités",
        "hypotheses": [
            "φ est une fonction convexe",
            "X est une variable aléatoire réelle intégrable"
        ],
        "conclusion": "φ(E[X]) ≤ E[φ(X)]",
        "erreurs_courantes": [
            "φ est une fonction concave",
            "X est bornée",
            "φ est une fonction croissante",
        ]
    },

    "T29": {
        "nom": "Réduction de Jordan (existence)",
        "domaine": "Algèbre Linéaire",
        "hypotheses": [
            "A est une matrice carrée n×n à coefficients complexes"
        ],
        "conclusion": "A est semblable à une matrice de Jordan",
        "erreurs_courantes": [
            "A est une matrice carrée réelle",
            "A est diagonalisable",
            "le polynôme caractéristique de A est scindé sur ℝ",
        ]
    },

    "T30": {
        "nom": "Formule de Taylor avec reste de Lagrange",
        "domaine": "Analyse",
        "hypotheses": [
            "f est n fois dérivable sur [a, b] (continue)",
            "f est n+1 fois dérivable sur ]a, b["
        ],
        "conclusion": "∃ c ∈ ]a, b[ tel que f(b) = Σ f^(k)(a)/k!·(b-a)^k + f^(n+1)(c)/(n+1)!·(b-a)^(n+1)",
        "erreurs_courantes": [
            "f est n+1 fois dérivable sur [a, b]",
            "f est de classe Cⁿ uniquement",
            "f est analytique",
        ]
    },
}