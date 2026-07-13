from hypotheses import HYPOTHESES

# List of direct implications (stronger, weaker)
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
    
    # Continuity on different intervals
    ("F_CONTINUE_FERME", "F_CONTINUE_OUVERT"),
    ("F_CONTINUE_R", "F_CONTINUE_FERME"),
    ("F_CONTINUE_R", "F_CONTINUE_OUVERT"),
    ("F_DERIVABLE_R", "F_DERIVABLE_OUVERT"),
    
    # Compactness
    ("INTERVALLE_COMPACT", "INTERVALLE_FERME_BORNE"),
    ("INTERVALLE_FERME_BORNE", "INTERVALLE_COMPACT"),
        
    # Basis and linearly independent family
    ("FAMILLE_EST_BASE", "FAMILLE_LIBRE_K_LEQ_N"),
    ("FAMILLE_EST_BASE", "FAMILLE_GENERATRICE_E"),
    
    # Spaces
    ("E_HILBERT", "E_BANACH"),
    ("E_PRODUIT_SCALAIRE", "E_NORME"),
    ("UV_ORTHOGONAUX", "UV_VECTEURS_E"), # simplification
    
    # Sequences
    ("UN_CROISSANTE", "UN_MONOTONE"),
    ("UN_CAUCHY", "UN_BORNEE"), # Cauchy sequence ⟹ bounded
    
    # Convergence
    ("UN_DECROISSANTE_MAJOREE", "UN_MAJOREE"),
    
    # Adjacent sequences
    ("UN_CROISS_VN_DECROISS", "UN_CROISSANTE"),
    
    # Integrability
    ("F_CONTINUE_FERME", "F_INTEGRABLE_FERME"),
    ("F_CONTINUE_FERME", "F_BORNEE_FERME"), # Weierstrass
    ("UV_CLASSE_C1_FERME", "UV_CONTINUES_FERME"),
    ("UV_CLASSE_C1_FERME", "UPRIME_V_CONTINUES_FERME"),
    ("UV_CLASSE_C2_FERME", "UV_CLASSE_C1_FERME"),
    
    # Change of variable
    ("PHI_CLASSE_C1", "PHI_CONTINUE"),
    
    # Probability
    ("VAR_X1_FINIE_POSITIVE", "E_X1_FINIE"),
    ("VAR_X1_FINIE", "E_X1_CARRE_FINIE"),
    ("E_X1_CARRE_FINIE", "E_ABS_X1_FINIE"),
    ("E_X1_FINIE", "E_ABS_X1_FINIE"),
    ("XN_INDEPENDANTES", "XN_INDEP_UNIQUEMENT"),
    ("XN_IID", "XN_INDEPENDANTES"),
        
    # Compactness (Weierstrass, Heine)
    ("F_LIPSCHITZIENNE_FERME", "F_UNIF_CONTINUE_FERME"),
    ("F_UNIF_CONTINUE_FERME", "F_CONTINUE_FERME"),
]

def satisfies(cited_hypotheses, required_hypothesis):
    if required_hypothesis in cited_hypotheses:
        return True

    # Recursive search through implications
    visited = set()

    def implies(h):
        if h in visited:
            return False
        visited.add(h)
        
        # If hypothesis h is cited directly
        if h in cited_hypotheses:
            return True
            
        # Traverse implications
        for stronger, weaker in IMPLICATIONS_LIST:
            if weaker == h:
                # The stronger property is cited
                if stronger in cited_hypotheses:
                    return True
                # Or it is itself implied by another cited property
                if implies(stronger):
                    return True
        return False
    return implies(required_hypothesis)

# Invalid implications
INVALID_IMPLICATIONS = [
    ("F_CONTINUE_OUVERT", "F_CONTINUE_FERME"),  # open ≠ closed
    ("F_DERIVABLE_OUVERT", "F_DERIVABLE_FERME"),  # open ≠ closed
    ("F_CLASSE_CN_UNIQUEMENT", "F_N_FOIS_DERIVABLE_FERME"),  # Cn not enough for Lagrange
    ("F_INTEGRABLE_FERME", "F_CONTINUE_FERME"),  # integrable doesn't imply continuous
    ("F_BORNEE_FERME", "F_CONTINUE_FERME"),  # bounded doesn't imply continuous
    ("FN_CONVERGE_PP", "FN_CONVERGE_UNIFORMEMENT"),  # pp ⟹ uniform, FALSE!
]

if __name__ == "__main__":
    print(" Testing implications")
    
    # Test 1: C1 implies continuous (true)
    result = satisfies(["F_CLASSE_C1"], "F_CONTINUE_FERME")
    print(f"C1 on I ⟹ continuous on I: {result}")
    
    # Test 2: C1 implies differentiable on the open interval (true)
    result = satisfies(["F_CLASSE_C1"], "F_DERIVABLE_OUVERT")
    print(f"C1 on I ⟹ differentiable on the open interval: {result}")
    
    # Test 3: Differentiable on [a,b] implies continuous on ]a,b[
    result = satisfies(["F_DERIVABLE_FERME"], "F_CONTINUE_OUVERT")
    print(f"Differentiable on [a,b] ⟹ continuous on ]a,b[: {result}")    
    
    # Check IDs in implications
    print("\nChecking IDs in IMPLICATIONS_LIST")
    ids_set = set(HYPOTHESES.keys())
    missing_ids = []
    for stronger, weaker in IMPLICATIONS_LIST:
        if stronger not in ids_set:
            missing_ids.append(stronger)
        if weaker not in ids_set:
            missing_ids.append(weaker)
    if missing_ids:
        print(f"Missing IDs in HYPOTHESES: {set(missing_ids)}")
    else:
        print("All IDs are valid")
    
    # Display a sample
    print("\nSample of verified implications")
    for i, (strong, weak) in enumerate(IMPLICATIONS_LIST[:5]):
        print(f"{i+1}. {HYPOTHESES.get(strong, strong)} ⟹ {HYPOTHESES.get(weak, weak)}")