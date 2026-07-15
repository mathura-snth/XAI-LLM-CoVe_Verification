from hypotheses import HYPOTHESES

# Liste des implications directes (plus_fort, plus_faible)
IMPLICATIONS_LIST = [
    ("F_DERIVABLE_EN_A", "F_CONTINUE_EN_A"),
    ("F_DERIVABLE_OUVERT", "F_CONTINUE_OUVERT"),
    ("F_DERIVABLE_FERME", "F_DERIVABLE_OUVERT"),
    ("F_CLASSE_C1", "F_DERIVABLE_OUVERT"),
    ("F_CLASSE_C1", "F_CONTINUE_FERME"),
    ("F_CLASSE_C2", "F_CLASSE_C1"),
    ("F_CLASSE_C2", "F_DERIVABLE_OUVERT"),
    ("F_CLASSE_C3", "F_CLASSE_C2"),
    ("F_CLASSE_C3", "F_CLASSE_C1"),
    ("F_DERIVABLE_FERME", "F_CONTINUE_FERME"),
    
    # Continuité sur différents intervalles
    ("F_CONTINUE_FERME", "F_CONTINUE_OUVERT"),
    ("F_CONTINUE_R", "F_CONTINUE_FERME"),
    ("F_CONTINUE_R", "F_CONTINUE_OUVERT"),
    ("F_DERIVABLE_R", "F_DERIVABLE_OUVERT"),
    
    # Compacité
    ("INTERVALLE_COMPACT", "INTERVALLE_FERME_BORNE"),
    ("INTERVALLE_FERME_BORNE", "INTERVALLE_COMPACT"),
        
    # Base et famille libre
    ("FAMILLE_EST_BASE", "FAMILLE_LIBRE_K_LEQ_N"),
    ("FAMILLE_EST_BASE", "FAMILLE_GENERATRICE_E"),
    
    # Espaces
    ("E_HILBERT", "E_BANACH"),
    ("E_PRODUIT_SCALAIRE", "E_NORME"),
    ("UV_ORTHOGONAUX", "UV_VECTEURS_E"), # simplification
    
    # Suites
    ("UN_CROISSANTE", "UN_MONOTONE"),
    ("UN_CAUCHY", "UN_BORNEE"), # suite de Cauchy ⟹ bornée
    
    # Convergence
    ("UN_DECROISSANTE_MAJOREE", "UN_MAJOREE"),
    
    # Suites adjacentes
    ("UN_CROISS_VN_DECROISS", "UN_CROISSANTE"),
    
    # Intégrabilité
    ("F_CONTINUE_FERME", "F_INTEGRABLE_FERME"),
    ("F_CONTINUE_FERME", "F_BORNEE_FERME"), # Weierstrass
    ("UV_CLASSE_C1_FERME", "UV_CONTINUES_FERME"),
    ("UV_CLASSE_C1_FERME", "UPRIME_V_CONTINUES_FERME"),
    ("UV_CLASSE_C2_FERME", "UV_CLASSE_C1_FERME"),
    
    # Changement de variable
    ("PHI_CLASSE_C1", "PHI_CONTINUE"),
    
    # Probabilités
    ("VAR_X1_FINIE_POSITIVE", "E_X1_FINIE"),
    ("VAR_X1_FINIE", "E_X1_CARRE_FINIE"),
    ("E_X1_CARRE_FINIE", "E_ABS_X1_FINIE"),
    ("E_X1_FINIE", "E_ABS_X1_FINIE"),
    ("XN_INDEPENDANTES", "XN_INDEP_UNIQUEMENT"),
    ("XN_IID", "XN_INDEPENDANTES"),
        
    # Compacité (Weierstrass, Heine)
    ("F_LIPSCHITZIENNE_FERME", "F_UNIF_CONTINUE_FERME"),
    ("F_UNIF_CONTINUE_FERME", "F_CONTINUE_FERME"),
]

def satisfait(hypotheses_citees, hypothese_requise):
    if hypothese_requise in hypotheses_citees:
        return True

    # Recherche récursive dans les implications
    visites = set()

    def implique(h):
        if h in visites:
            return False
        visites.add(h)
        
        # Si l'hypothèse h est citée directement
        if h in hypotheses_citees:
            return True
            
        # Parcours des implications
        for plus_fort, plus_faible in IMPLICATIONS_LIST:
            if plus_faible == h:
                # La propriété plus forte est citée
                if plus_fort in hypotheses_citees:
                    return True
                # Ou elle est elle-même impliquée par une autre propriété citée
                if implique(plus_fort):
                    return True
        return False
    return implique(hypothese_requise)

# Mauvaises implications (invalides)
MAUVAISES_IMPLICATIONS = [
    ("F_CONTINUE_OUVERT", "F_CONTINUE_FERME"),  # ouvert ≠ fermé
    ("F_DERIVABLE_OUVERT", "F_DERIVABLE_FERME"),  # ouvert ≠ fermé
    ("F_CLASSE_CN_UNIQUEMENT", "F_N_FOIS_DERIVABLE_FERME"),  # Cn ne suffit pas pour Lagrange
    ("F_INTEGRABLE_FERME", "F_CONTINUE_FERME"),  # intégrable n'implique pas continue
    ("F_BORNEE_FERME", "F_CONTINUE_FERME"),  # bornée n'implique pas continue
    ("FN_CONVERGE_PP", "FN_CONVERGE_UNIFORMEMENT"),  # pp ⟹ uniforme, FAUX !
]

if __name__ == "__main__":
    print(" Tests des implications")
    
    # Test 1: C1 implique continue (vrai)
    result = satisfait(["F_CLASSE_C1"], "F_CONTINUE_FERME")
    print(f"C1 sur I ⟹ continue sur I: {result}")
    
    # Test 2: C1 implique dérivable sur l'ouvert (vrai)
    result = satisfait(["F_CLASSE_C1"], "F_DERIVABLE_OUVERT")
    print(f"C1 sur I ⟹ dérivable sur l'ouvert: {result}")
    
    # Test 3 : Dérivable sur [a,b] implique continue sur ]a,b[
    result = satisfait(["F_DERIVABLE_FERME"], "F_CONTINUE_OUVERT")
    print(f"Dérivable sur [a,b] ⟹ continue sur ]a,b[: {result}")    
    
    # Vérification des IDs dans les implications
    print("\nVérification des IDs dans IMPLICATIONS_LIST")
    ids_set = set(HYPOTHESES.keys())
    missing_ids = []
    for plus_fort, plus_faible in IMPLICATIONS_LIST:
        if plus_fort not in ids_set:
            missing_ids.append(plus_fort)
        if plus_faible not in ids_set:
            missing_ids.append(plus_faible)
    if missing_ids:
        print(f"IDs manquants dans HYPOTHESES: {set(missing_ids)}")
    else:
        print("Tous les IDs sont valides")
    
    # Affichage d'un échantillon
    print("\nÉchantillon d'implications vérifiées")
    for i, (fort, faible) in enumerate(IMPLICATIONS_LIST[:5]):
        print(f"{i+1}. {HYPOTHESES.get(fort, fort)} ⟹ {HYPOTHESES.get(faible, faible)}")