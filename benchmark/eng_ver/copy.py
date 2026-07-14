import random
from theorems import THEOREMS
from hypotheses import HYPOTHESES, text
from implications import satisfies, IMPLICATIONS_LIST, INVALID_IMPLICATIONS

ERROR_TYPES = [
    "correct",
    "missing_hypothesis",
    "multiple_missing",
    "misformulated_hypothesis",
    "invented_hypothesis",
    "erroneous_interval",
    "valid_implication",
    "invalid_implication",
]

def generate_copy(theorem_id, error_type=None):
    if theorem_id not in THEOREMS:
        raise ValueError(f"Theorem '{theorem_id}' unknown.")
    th = THEOREMS[theorem_id]
    gold = th["hypotheses"]
    common_errors = th["common_errors"]

    if error_type is None:
        error_type = random.choice(ERROR_TYPES)

    # Start with a correct copy that will be degraded according to the error type
    cited_hypotheses = list(gold)
    labels = {h: "present" for h in gold}
    applied_error = error_type

    # Correct copy
    if error_type == "correct":
        pass

    # One missing hypothesis
    elif error_type == "missing_hypothesis" and len(gold) > 1:
        forgotten_h = random.choice(gold)
        cited_hypotheses.remove(forgotten_h)
        labels[forgotten_h] = "absent"

    # Multiple missing hypotheses
    elif error_type == "multiple_missing" and len(gold) > 2:
        n_forgotten = random.randint(2, len(gold) - 1)
        for h in random.sample(gold, n_forgotten):
            cited_hypotheses.remove(h)
            labels[h] = "absent"

    # Misformulated hypothesis
    elif error_type == "misformulated_hypothesis" and "common_errors":
        idx = random.randint(0, len(gold) - 1)
        cited_hypotheses[idx] = random.choice(common_errors)
        labels[gold[idx]] = "misformulated"

    # Invented hypothesis
    elif error_type == "invented_hypothesis" and "common_errors":
        invented_h = random.choice(common_errors)
        cited_hypotheses.append(invented_h)
        labels["[invented] " + invented_h] = "invented"

    # Open/closed interval inversion
    elif error_type == "erroneous_interval":
        modified = False
        for i, h in enumerate(cited_hypotheses):
            if h in ["F_CONTINUE_FERME", "F_DERIVABLE_FERME"] and not modified:
                cited_hypotheses[i] = h.replace("FERME", "OUVERT")
                labels[gold[i]] = "misformulated"
                modified = True
            elif h in ["F_CONTINUE_OUVERT", "F_DERIVABLE_OUVERT"] and not modified:
                cited_hypotheses[i] = h.replace("OUVERT", "FERME")
                labels[gold[i]] = "misformulated"
                modified = True
        if not modified:
            applied_error = "correct"
        
    elif error_type == "valid_implication" and IMPLICATIONS_LIST:
        # Replacement by a stronger hypothesis is valid
        for stronger, weaker in IMPLICATIONS_LIST:
            if weaker in gold and stronger not in cited_hypotheses:
                idx = cited_hypotheses.index(weaker)
                cited_hypotheses[idx] = stronger
                labels[weaker] = "satisfied_by_implication"
                break
    
    elif error_type == "invalid_implication" and INVALID_IMPLICATIONS:
        # Replacement by a weaker hypothesis is INVALID
        for false_stronger, false_weaker in INVALID_IMPLICATIONS:
            if false_weaker in gold and false_stronger not in cited_hypotheses:
                idx = cited_hypotheses.index(false_weaker)
                cited_hypotheses[idx] = false_stronger
                labels[false_weaker] = "invalid_implication"
                break

    else:
        applied_error = "correct"

# Verdict    
    is_correct = True
    reasons = []
    
    for h in gold:
        if satisfies(cited_hypotheses, h):
            continue
        else:
            is_correct = False
            # Find justifications
            if labels.get(h) == "absent":
                reasons.append(f"missing: {text(h)}")
            elif labels.get(h) == "misformulated":
                reasons.append(f"misformulated: {text(h)}")
            elif labels.get(h) == "invalid_implication":
                reasons.append(f"invalid_implication: {text(h)}")
            elif labels.get(h) == "invented":
                reasons.append(f"invented: {h}")
            else:
                reasons.append(f"unsatisfied: {text(h)}")
    
    # Inventions
    for label_key, label_val in labels.items():
        if label_val == "invented":
            is_correct = False
            # Already added the reason
            reasons.append(f"invented: {label_key}")

    if error_type == "misformulated_hypothesis" and is_correct:
        applied_error = "valid_implication"

    reasons = list(set(reasons))
    if not reasons and is_correct:
        reason = "OK"
    elif not reasons and not is_correct:
        reason = "unknown_error"
    else:
        reason = "; ".join(reasons[:2])  # max 2 reasons

    return {
    "theorem_id": theorem_id,
    "name": th["name"],
    "copy": [text(h) if h in HYPOTHESES else h for h in cited_hypotheses],
    "expected": [text(h) for h in gold],
    "is_correct": is_correct,
    "reason": reason,
    "error_type": applied_error,
    }

if __name__ == "__main__":
    print("Generating copies:\n")
    
    for err_type in ERROR_TYPES[:5]:  # 5 examples
        copy = generate_copy("T01", err_type)
        print(f"Copy: {copy['copy']}")
        print(f"Verdict: {'TRUE' if copy['is_correct'] else 'FALSE'}")
        print(f"Reason: {copy['reason']}")
        print("-----------------------------------------------")