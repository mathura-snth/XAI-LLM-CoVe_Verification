import random
from theoremes import THEOREMES

TYPES_ERREURS = [
    "correcte",
    "hypothese_manquante",
    "plusieurs_manquantes",
    "hypothese_mal_formulee",
    "hypothese_inventee",
    "intervalle_errone",
    "renforcement_abusif",
]

def generer_copie(theoreme_id, type_erreur=None):
    if theoreme_id not in THEOREMES:
        raise ValueError(f"Théorème '{theoreme_id}' inconnu.")

    th = THEOREMES[theoreme_id]
    gold = th["hypotheses"]

    if type_erreur is None:
        type_erreur = random.choice(TYPES_ERREURS)

    # on part d'une copie correcte qu'on va dégrader selon le type d'erreur
    hypotheses_citees = list(gold)
    labels = {h: "presente" for h in gold}
    erreur_appliquee = type_erreur

    # copie correcte
    if type_erreur == "correcte":
        pass

    # une hypothèse manquante
    elif type_erreur == "hypothese_manquante" and len(gold) > 1:
        h_oubliee = random.choice(gold)
        hypotheses_citees.remove(h_oubliee)
        labels[h_oubliee] = "absente"

    # plusieurs hypothèses manquantes
    elif type_erreur == "plusieurs_manquantes" and len(gold) > 2:
        n_oubliees = random.randint(2, len(gold) - 1)
        for h in random.sample(gold, n_oubliees):
            hypotheses_citees.remove(h)
            labels[h] = "absente"

    # hypothèse mal formulée
    elif type_erreur == "hypothese_mal_formulee" and th["erreurs_courantes"]:
        idx = random.randint(0, len(gold) - 1)
        hypotheses_citees[idx] = random.choice(th["erreurs_courantes"])
        labels[gold[idx]] = "mal_formulee"

    # hypothèse inventée
    elif type_erreur == "hypothese_inventee" and th["erreurs_courantes"]:
        h_inventee = random.choice(th["erreurs_courantes"])
        hypotheses_citees.append(h_inventee)
        labels["[inventee] " + h_inventee] = "inventee"

    # intervalle ouvert/fermé inversé
    elif type_erreur == "intervalle_errone":
        modifiee = False
        for i, h in enumerate(hypotheses_citees):
            if "[a, b]" in h and not modifiee:
                hypotheses_citees[i] = h.replace("[a, b]", "]a, b[")
                labels[gold[i]] = "mal_formulee"
                modifiee = True
            elif "]a, b[" in h and not modifiee:
                hypotheses_citees[i] = h.replace("]a, b[", "[a, b]")
                labels[gold[i]] = "mal_formulee"
                modifiee = True
        if not modifiee:
            erreur_appliquee = "correcte"

    # renforcement abusif
    elif type_erreur == "renforcement_abusif":
        renforcements = {
            "continue": "de classe C¹",
            "dérivable": "de classe C²",
            "intégrable": "continue",
            "mesurable": "continue",
        }
        modifiee = False
        for i, h in enumerate(hypotheses_citees):
            for mot, renfort in renforcements.items():
                if mot in h and not modifiee:
                    hypotheses_citees[i] = h.replace(mot, renfort)
                    labels[gold[i]] = "mal_formulee"
                    modifiee = True
                    break
        if not modifiee:
            erreur_appliquee = "correcte"

    else:
        erreur_appliquee = "correcte"

    # calcul du score
    n_correctes = sum(1 for h in gold if labels[h] == "presente")
    score = round(n_correctes / len(gold), 3)
    est_correcte = score == 1.0 and "inventee" not in labels.values()

    return {
        "theoreme_id": theoreme_id,
        "nom": th["nom"],
        "domaine": th["domaine"],
        "type_erreur": erreur_appliquee,
        "hypotheses_gold": gold,
        "hypotheses_citees": hypotheses_citees,
        "labels": labels,
        "conclusion": th["conclusion"],
        "score": score,
        "est_correcte": est_correcte,
    }


# test rapide
if __name__ == "__main__":
    print("3 exemples sur T01 (Rolle)\n")
    for type_erreur in ["correcte", "hypothese_manquante", "intervalle_errone"]:
        copie = generer_copie("T01", type_erreur)
        print(f"Type     : {copie['type_erreur']}")
        print(f"Gold     : {copie['hypotheses_gold']}")
        print(f"Citées   : {copie['hypotheses_citees']}")
        print(f"Labels   : {copie['labels']}")
        print(f"Score    : {copie['score']} | Correcte : {copie['est_correcte']}")
        print()