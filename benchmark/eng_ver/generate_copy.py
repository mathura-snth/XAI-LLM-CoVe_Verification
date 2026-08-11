import random
from theorems import THEOREMS
from hypotheses import HYPOTHESES, text
from implications import satisfies, IMPLICATIONS_LIST, INVALID_IMPLICATIONS

ERROR_TYPES = [
    "correct",
    "missing_hypothesis",
    "multiple_missing",
    "invented_hypothesis",
    "valid_implication",
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

    removed_hypotheses = []
    invented_entries = []
    implication_swaps = []

    applied_error = error_type

    # Correct copy
    if error_type == "correct":
        pass

    # One missing hypothesis
    elif error_type == "missing_hypothesis" and len(gold) > 1:
        forgotten_h = random.choice(gold)
        cited_hypotheses.remove(forgotten_h)
        # on mémorise la vraie suppression
        removed_hypotheses.append(forgotten_h)

    # Multiple missing hypotheses
    elif error_type == "multiple_missing" and len(gold) > 2:
        n_forgotten = random.randint(2, len(gold) - 1)
        forgotten = random.sample(gold, n_forgotten)
        for h in forgotten:
            cited_hypotheses.remove(h)
            removed_hypotheses.append(h)

    # invented hypothesis has multiple sub_errors ()
    elif error_type == "invented_hypothesis":

        sub_type = random.choice(["misformulated", "invented", "interval", "invalid_implication"])
        
        # misformulated hypothesis
        if sub_type == "misformulated" and common_errors:
            idx = random.randint(0, len(gold) - 1)
            original = cited_hypotheses[idx]
            replacement = random.choice(common_errors)
            cited_hypotheses[idx] = replacement

            invented_entries.append({ "invented": replacement, "instead_of": original })

        # invented hypothesis added
        elif sub_type == "invented" and common_errors:
            candidates = [
                h for h in common_errors
                if h not in cited_hypotheses
            ]
            if candidates:
                invented_h = random.choice(candidates)
                cited_hypotheses.append(invented_h)
                invented_entries.append({ "invented": invented_h, "instead_of": None })

        # interval inversion
        elif sub_type == "interval":
            modified = False
            for i, h in enumerate(cited_hypotheses):
                if h in ["F_CONTINUE_FERME", "F_DERIVABLE_FERME"] and not modified:
                    new_h = h.replace("FERME", "OUVERT")
                    cited_hypotheses[i] = new_h
                    invented_entries.append({ "invented": new_h, "instead_of": h })
                    modified = True
                elif h in ["F_CONTINUE_OUVERT", "F_DERIVABLE_OUVERT"] and not modified:
                    new_h = h.replace("OUVERT", "FERME")
                    cited_hypotheses[i] = new_h
                    invented_entries.append({ "invented": new_h, "instead_of": h })
                    modified = True
            if not modified:
                applied_error = "correct"
        
        elif sub_type == "invalid_implication" and INVALID_IMPLICATIONS:
            modified = False
            # Replacement by a weaker hypothesis is INVALID
            for false_stronger, false_weaker in INVALID_IMPLICATIONS:
                if false_weaker in gold and false_stronger not in cited_hypotheses:
                    idx = cited_hypotheses.index(false_weaker)
                    cited_hypotheses[idx] = false_stronger
                    # replacement memorisation
                    invented_entries.append({ "invented": false_stronger, "instead_of": false_weaker })
                    modified = True
                    break
            if not modified:
                applied_error = "correct"

    elif error_type == "valid_implication" and IMPLICATIONS_LIST:
        implication_found = False
        # Replacement by a stronger hypothesis is valid
        for stronger, weaker in IMPLICATIONS_LIST:
            if weaker in gold and weaker in cited_hypotheses and stronger not in cited_hypotheses:
                idx = cited_hypotheses.index(weaker)
                cited_hypotheses[idx] = stronger
                implication_swaps.append((stronger, weaker))
                implication_found = True
                break
        if not implication_found:
            applied_error = "correct"
    else:
        applied_error = "correct"
    if cited_hypotheses == gold:
        applied_error = "correct"

# Verdict    
    is_correct = True
    reasons = []
    
    for h in gold:
        if not satisfies(cited_hypotheses, h):
            is_correct = False
    if invented_entries:
        is_correct = False

    # justifications : missing hypothesis
    for h in removed_hypotheses:
        reasons.append( f"missing: {text(h)}" )

    # justifications : invented -> hypothesis added / replacement
    for entry in invented_entries:
        invented = entry["invented"]
        instead_of = entry["instead_of"]

        invented_text = (
            text(invented)
            if invented in HYPOTHESES
            else invented
        )
        # replacement
        if instead_of is not None:
            instead_text = (
                text(instead_of)
                if instead_of in HYPOTHESES
                else instead_of
            )
            reasons.append(
                f"invented_hypothesis: "
                f"{invented_text} "
                f"(instead of {instead_text})"
            )
        # hypothesis added (no replacmeent)
        else:
            reasons.append( f"invented_hypothesis: {invented_text}" )

    # justifications : implications valides
    if is_correct and implication_swaps:
        descriptions = []
        for stronger, weaker in implication_swaps:
            descriptions.append(
                f"{text(stronger)} implies {text(weaker)}"
            )
        reasons.append("stronger_hypothesis: " + "; ".join(descriptions[:2]))

    # validation type
    if is_correct:
        if implication_swaps:
            validation_type = "stronger_hypothesis"
            reason = "; ".join(reasons)
        else:
            validation_type = "exact_match"
            reason = "hypotheses match exactly."

    else:
        if invented_entries:
            validation_type = "invented_hypothesis"
            reason = "; ".join(reasons)

        elif removed_hypotheses:
            if len(removed_hypotheses) > 1:
                validation_type = "multiple_missing"
            else:
                validation_type = "missing_hypothesis"

            reason = "; ".join(reasons)

        else:
            validation_type = "unknown_error"
            reason = "unable to determine the exact error."

    return {
    "theorem_id": theorem_id,
    "name": th["name"],
    "copy": [text(h) if h in HYPOTHESES else h for h in cited_hypotheses],
    "expected": [text(h) for h in gold],
    "is_correct": is_correct,
    "reason": reason,
    "validation_type": validation_type,
    }

if __name__ == "__main__":
    print("Generating copies:\n")
    
    for err_type in ERROR_TYPES[:5]:  # 5 examples
        copy = generate_copy("T01", err_type)
        print(f"Copy: {copy['copy']}")
        print(f"Verdict: {'TRUE' if copy['is_correct'] else 'FALSE'}")
        print(f"Reason: {copy['reason']}")
        print("-----------------------------------------------")