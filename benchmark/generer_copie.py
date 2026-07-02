import random
from theoremes import THEOREMES
from hypotheses import HYPOTHESES, texte
from implications import satisfait, IMPLICATIONS_LIST, MAUVAISES_IMPLICATIONS

TYPES_ERREURS = [
    "correcte",
    "hypothese_manquante",
    "plusieurs_manquantes",
    "hypothese_mal_formulee",
    "hypothese_inventee",
    "intervalle_errone",
    "renforcement_abusif",
    "implication_valide",
    "implication_invalide",
]

def generer_copie(theoreme_id, type_erreur=None):
    if theoreme_id not in THEOREMES:
        raise ValueError(f"Théorème '{theoreme_id}' inconnu.")
    th = THEOREMES[theoreme_id]
    gold = th["hypotheses"]
    erreurs_courantes = th["erreurs_courantes"]

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
    elif type_erreur == "hypothese_mal_formulee" and "erreurs_courantes":
        idx = random.randint(0, len(gold) - 1)
        hypotheses_citees[idx] = random.choice("erreurs_courantes")
        labels[gold[idx]] = "mal_formulee"

    # hypothèse inventée
    elif type_erreur == "hypothese_inventee" and "erreurs_courantes":
        h_inventee = random.choice("erreurs_courantes")
        hypotheses_citees.append(h_inventee)
        labels["[inventee] " + h_inventee] = "inventee"

    # intervalle ouvert/fermé inversé
    elif type_erreur == "intervalle_errone":
        modifiee = False
        for i, h in enumerate(hypotheses_citees):
            if h in ["F_CONTINUE_FERME", "F_DERIVABLE_FERME"] and not modifiee:
                hypotheses_citees[i] = h.replace("FERME", "OUVERT")
                labels[gold[i]] = "mal_formulee"
                modifiee = True
            elif h in ["F_CONTINUE_OUVERT", "F_DERIVABLE_OUVERT"] and not modifiee:
                hypotheses_citees[i] = h.replace("OUVERT", "FERME")
                labels[gold[i]] = "mal_formulee"
                modifiee = True
        if not modifiee:
            erreur_appliquee = "correcte"

    # renforcement abusif
    elif type_erreur == "renforcement_abusif":
        renforcements = {
            "F_CONTINUE_FERME": "F_CLASSE_C1",
            "F_CONTINUE_OUVERT": "F_CLASSE_C1",
            "F_DERIVABLE_OUVERT": "F_CLASSE_C2",
            "F_INTEGRABLE_FERME": "F_CONTINUE_FERME",
        }
        modifiee = False
        for i, h in enumerate(hypotheses_citees):
            if h in renforcements and not modifiee:
                    hypotheses_citees[i] = renforcements[h]
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
        print(f"Type : {copie['type_erreur']}")
        print(f"Gold : {copie['hypotheses_gold']}")
        print(f"Citées : {copie['hypotheses_citees']}")
        print(f"Labels: {copie['labels']}")
        print(f"Score: {copie['score']} | Correcte : {copie['est_correcte']}")
        print()