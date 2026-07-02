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
        
    elif type_erreur == "implication_valide" and IMPLICATIONS_LIST:
        # le remplacement par une hypothèse plus forte est valide
        for fort, faible in IMPLICATIONS_LIST:
            if faible in gold and fort not in hypotheses_citees:
                idx = hypotheses_citees.index(faible)
                hypotheses_citees[idx] = fort
                labels[faible] = "satisfaite_par_implication"
                break
    
    elif type_erreur == "implication_invalide" and MAUVAISES_IMPLICATIONS:
        # le remplacement par une hypothèse plus faible est INVALIDE
        for faux_fort, faux_faible in MAUVAISES_IMPLICATIONS:
            if faux_faible in gold and faux_fort not in hypotheses_citees:
                idx = hypotheses_citees.index(faux_faible)
                hypotheses_citees[idx] = faux_fort
                labels[faux_faible] = "implication_invalide"
                break

    else:
        erreur_appliquee = "correcte"

# verdict    
    est_correcte = True
    raisons = []
    
    for h in gold:
        if satisfait(hypotheses_citees, h):
            continue
        else:
            est_correcte = False
            # on cherche les justifications
            if labels.get(h) == "absente":
                raisons.append(f"manquante: {texte(h)}")
            elif labels.get(h) == "mal_formulee":
                raisons.append(f"mal_formulee: {texte(h)}")
            elif labels.get(h) == "implication_invalide":
                raisons.append(f"implication_invalide: {texte(h)}")
            elif labels.get(h) == "inventee":
                raisons.append(f"inventee: {h}")
            else:
                raisons.append(f"non_satisfaite: {texte(h)}")
    
    # les inventions
    for label in labels.values():
        if label == "inventee":
            est_correcte = False
            # car on a déjà ajouté la raison

    raisons = list(set(raisons))
    if not raisons and est_correcte:
        raison = "OK"
    elif not raisons and not est_correcte:
        raison = "erreur_inconnue"
    else:
        raison = "; ".join(raisons[:2])  # max 2 raisons

    return {
    "theoreme_id": theoreme_id,
    "nom": th["nom"],
    "copie": [texte(h) if h in HYPOTHESES else h for h in hypotheses_citees],
    "attendu": [texte(h) for h in gold],
    "est_correcte": est_correcte,
    "raison": raison,
    "type_erreur": erreur_appliquee,
    }

if __name__ == "__main__":
    print("Génération de copies :\n")
    
    for type_err in TYPES_ERREURS[:5]:  # 5 exemples
        copie = generer_copie("T01", type_err)
        print(f"Copie: {copie['copie']}")
        print(f"Verdict: {'VRAI' if copie['est_correcte'] else 'FAUX'}")
        print(f"Raison: {copie['raison']}")
        print("-----------------------------------------------")
