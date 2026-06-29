# Liste des implications directes (plus_fort, plus_faible)
IMPLICATIONS_LIST = [
    ("f dérivable en a", "f continue en a"),
    ("f dérivable sur I", "f continue sur I"),
    ("f dérivable sur [a, b]", "f dérivable sur ]a, b["),
    ("f de classe C1 sur I", "f dérivable sur I"),
    ("f de classe C1 sur I", "f continue sur I"),
    ("f de classe C2 sur I", "f de classe C1 sur I"),
    ("f de classe C2 sur I", "f dérivable sur I"),
    ("f de classe C2 sur I", "f de classe C1 sur I"),
    ("f de classe C3 sur I", "f de classe C2 sur I"),
    ("f de classe C3 sur I", "f de classe C1 sur I"),
    ("f de classe C∞ sur I", "f de classe Cn sur I"),
    ("f continue sur [a, b]", "f continue sur ]a, b["),
    ("f dérivable sur [a, b]", "f dérivable sur ]a, b["),
    ("f lipschitzienne sur I", "f uniformément continue sur I"),
    ("f uniformément continue sur I", "f continue sur I"),
    ("f monotone sur [a, b]", "f intégrable sur [a, b]"),
    ("f continue sur [a, b]", "f intégrable sur [a, b]"),
    ("f de classe C1 sur [a, b]", "f à variation bornée sur [a, b]"),
    ("f continue sur ℝ", "f continue sur [a, b]"),
    ("f continue sur [a, b]", "f continue sur ]a, b["),
    ("f dérivable sur ℝ", "f dérivable sur ]a, b["),
    ("[a, b] est compact dans ℝ", "[a, b] est fermé et borné"),
    ("[a,b] fermé et borné dans ℝ", "[a,b] compact"),
    ("f admet n valeurs propres distinctes", "f est diagonalisable"),
    ("f est symétrique réelle", "f est diagonalisable"),
    ("f est diagonalisable", "le polynôme minimal est scindé à racines simples"),
    ("le polynôme caractéristique est scindé à racines simples", "f est diagonalisable"),
    ("f est un isomorphisme", "f est injective"),
    ("f est un isomorphisme", "f est surjective"),
    ("f injective et dim E = dim F", "f est un isomorphisme"),
    ("f surjective et dim E = dim F", "f est un isomorphisme"),
    ("F est une base de E", "F est une famille libre"),
    ("F est une base de E", "F est une famille génératrice"),
    ("F libre avec card(F) = dim E", "F est une base de E"),
    ("F génératrice avec card(F) = dim E", "F est une base de E"),
    ("E euclidien", "E est un espace normé"),
    ("E de Hilbert", "E est un espace de Banach"),
    ("u et v orthogonaux", "⟨u,v⟩ = 0"),
    ("(un) converge", "(un) est bornée"),
    ("(un) converge", "(un) est de Cauchy"),
    ("(un) est de Cauchy dans un espace complet", "(un) converge"),
    ("(un) croissante et bornée", "(un) converge"),
    ("(un) décroissante et minorée", "(un) converge"),
    ("(un) croissante et majorée", "(un) converge"),
    ("Σun converge absolument", "Σun converge"),
    ("un ≥ 0 et Σun converge", "un → 0"),
    ("Σun converge", "un → 0"),
    ("f bornée et continue p.p. sur [a, b]", "f intégrable sur [a, b]"),
    ("fn → f uniformément sur [a,b]", "fn → f presque partout"),
    ("X admet un moment d'ordre 2", "X admet un moment d'ordre 1"),
    ("Var(X) < ∞", "E[X2] < ∞"),
    ("E[X2] < ∞", "E[|X|] < ∞"),
    ("X et Y indépendantes", "X et Y non corrélées"),
    ("X ~ N(μ,σ²)", "E[X]=μ"),
    ("X ~ N(μ,σ²)", "Var(X)=σ²"),
    ("f continue sur un compact K", "f uniformément continue sur K"),
    ("f continue sur un compact K", "f bornée sur K"),
    ("f continue sur un compact K", "f atteint ses bornes sur K"),
    ("espace complet + précompact", "compact")
]

def satisfait(hypotheses_citees, hypothese_requise):
    """
    Retourne True si l'hypothèse requise est satisfaite
    directement ou par implication.

    hypotheses_citees : liste de chaînes
    hypothese_requise : chaîne
    """

    # présente explicitement
    if hypothese_requise in hypotheses_citees:
        return True

    # recherche récursive dans les implications
    visites = set()

    def implique(h):
        if h in visites:
            return False

        visites.add(h)

        for plus_fort, plus_faible in IMPLICATIONS_LIST:

            if plus_faible == h:

                # la propriété plus forte est citée
                if plus_fort in hypotheses_citees:
                    return True

                # ou elle est elle-même impliquée
                if implique(plus_fort):
                    return True

        return False

    return implique(hypothese_requise)

if __name__ == "__main__":
    print(
        satisfait(
            ["f de classe C1 sur I"],
            "f continue sur I"
        )
    )