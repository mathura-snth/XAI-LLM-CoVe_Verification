# Benchmark Synthétique

Mathematical theorems have **formal and verifiable** assumptions — like the rules of a decision tree.

We synthetically generate student answers applying a theorem (correctly or incorrectly), and measure whether the LLM detects missing, misquoted, or invented assumptions.

The goal is not just to check for an exact equality between lists of assumptions, but to test the LLM's reasoning about the presence, absence, replacement, and logical implications of assumptions.

The objective is therefore to distinguish several different situations:

- all required assumptions are present → `correct`
- one or more required assumptions are missing → `missing_hypothesis` or `multiple_missing`
- an expected assumption has been replaced by an incorrect assumption or one unrelated to the theorem → `invented_hypothesis`
- a different assumption is **stronger** than a required assumption and therefore allows it to be satisfied → `valid_implication`.

*N.B.: a stronger assumption that allows a required assumption to be satisfied by a valid implication is considered **correct**. This is a deliberate choice in order to test the LLM's ability to perform logical reasoning, rather than merely checking the textual identity of assumptions.*

**Important rule:** when an expected assumption is replaced by another assumption that does not satisfy the former, it is considered an `invented_hypothesis`, and not a combination of `missing_hypothesis` + `invented_hypothesis`. The mechanism's intent is therefore interpreted as a **substitution**.

---

## General Principle

Each theorem has a list of mandatory assumptions, the **ground truth** (gold standard).
A synthetic copy is then generated from this ground truth. It may be:

- correct;
- missing an assumption;
- missing several assumptions;
- enriched or modified with an incorrect assumption;
- constructed with a stronger assumption that implies a required assumption;
- constructed with an assumption that looks like a valid implication but is not.

Each copy is associated with a verdict:

- `TRUE` if all necessary assumptions are satisfied;
- `FALSE` otherwise.

When a copy is false, a **reason** and a precise **error type** are also associated with it.

### Comparison by identifiers

Note that comparisons are made using identifiers *(e.g. F_CONTINUE_FERME)*. The French text exists only for display.

*N.B.: The goal is to eliminate ***false negatives*** caused by differences in wording ("f continuous" instead of "f is continuous").*

---

## Directory Architecture

| File | Purpose |
|---|---|
| **`hypotheses.py`** | Catalogue of all assumptions associated with their id: id → displayed text |
| **`theoremes.py`** | Defines the 30 theorems: mandatory assumptions (ids), conclusion, common errors (ids) |
| **`implications.py`** | Set of **valid** and **invalid** logical implications and the `satisfait()` function |
| **`generer_copie.py`** | Generates a degraded synthetic copy according to a given error type (or without error) and computes the verdict |
| **`run_benchmark.py`** | Generates N copies (100 by default) |
| **`exporter_tableau.py`** | Converts the .json into .csv and .md |

---

## 1. The Set of Assumptions (`hypotheses.py`)

The hypotheses.py file is the central catalogue of assumptions.

```python
HYPOTHESES = {
    "F_CONTINUE_FERME":  "f est continue sur [a, b]",
    "F_DERIVABLE_OUVERT": "f est dérivable sur ]a, b[",
    "F_EGAL_BORNES":      "f(a) = f(b)",
    # etc
}
```

Each assumption has:

1. a stable identifier, used throughout the benchmark;
2. French text, used only for display and for generating the copy presented to the LLM.

The file contains two functions:

- `texte(hyp_id)` → returns the French text for an id
- `textes(hyp_ids)` → returns the list of texts for a list of ids

---

## 2. Theorems (`theoremes.py`)

Each theorem is defined solely in terms of ids:

```python
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
    ],
},
```

- **`hypotheses`**: the ground truth, the exhaustive and mandatory list of assumptions of the theorem.
- **`conclusion`**: the expected result when all assumptions are satisfied.
- **`erreurs_courantes`**: **plausible but incorrect** assumption ids used to simulate poorly worded or invented copies.

**Important rule:** These are **never** valid assumptions for this theorem — a common error must never appear as `stronger` in a valid implication toward a gold assumption of the same theorem.

---

## 3. Implications (`implications.py`)

The `implications.py` file formalizes logical relationships between assumptions.

It makes it possible to determine whether a cited assumption, even if different from the required assumption, **nevertheless satisfies it** because it is logically stronger.

For example:
```text
f est de classe C¹
        ↓
f est dérivable
```
Therefore, if the theorem only requires f to be differentiable and the student states that f is of class C¹, the assumption is satisfied.

### 3.1 Valid implications — IMPLICATIONS_LIST

List of pairs (stronger, weaker) that are mathematically true:

```python
IMPLICATIONS_LIST = [
    ("F_DERIVABLE_OUVERT", "F_CONTINUE_OUVERT"),
    ("F_CLASSE_C1", "F_DERIVABLE_OUVERT"),
    ("F_CONTINUE_FERME", "F_CONTINUE_OUVERT"),
    # ...
]
```

### 3.2 Validation rules for each pair added to the table

- The implication must be **true in isolation**, without any additional assumption being implicitly understood. ("increasing ⟹ bounded" is **false**; "bounded above" is missing; a conjunction of two assumptions is not encoded as a single-term implication)

- A `common_error` id of a theorem **must never** appear as `stronger` implying a gold assumption of that same theorem, otherwise the common error will pass as valid

- No duplicate pairs

- Each id used must exist in `HYPOTHESES` (a function performs the verification)

### 3.3 Invalid implications — `MAUVAISES_IMPLICATIONS`

List of pairs that **look like** valid implications but are false (this is the kind of trap the LLM must detect)

```python
MAUVAISES_IMPLICATIONS = [
    ("F_CONTINUE_OUVERT", "F_CONTINUE_FERME"),   # ouvert n'implique PAS fermé
    ("F_DERIVABLE_OUVERT", "F_DERIVABLE_FERME"), # idem
    ("F_INTEGRABLE_FERME", "F_CONTINUE_FERME"),  # intégrable n'implique pas continue
    # ...
]
```

These pairs are used to generate the `implication_invalide` error type; they are never used by `satisfait()`.

``` text
IMPLICATIONS_LIST
        ↓
raisonnement logique autorisé

MAUVAISES_IMPLICATIONS
        ↓
erreurs volontairement générées
```

### 3.4 The `satisfait(hypotheses_citees, hypothese_requise)` function

It answers the question: **Is a theorem assumption satisfied by the assumptions actually cited in the copy?*

It returns `True` in two cases:

1. the required assumption is cited directly
2. a cited assumption is stronger and implies the required assumption through a chain of valid implications

```python
def satisfait(hypotheses_citees, hypothese_requise):
```

Searches **recursively** in `IMPLICATIONS_LIST` (a `visites` set is used to avoid cycles), never in `MAUVAISES_IMPLICATIONS`.
---

## 4. Copy Generation (`generer_copie.py`)

A copy always starts from a **100% correct** version of the ground truth, and is then degraded according to an **initial error mechanism** (omission, addition, substitution, interval reversal):

```text
gold
 ↓
degradation mechanism
 ↓
synthetic copy
 ↓
verdict recalculation
```

The generation mechanisms can produce:

- an omission;
- multiple omissions;
- an added assumption;
- a substitution;
- a valid implication;
- an invalid implication;
- an interval reversal.

### 4.1 The label depends on the final copy

The benchmark must not assume that the LLM knows how the copy was generated. It only sees:

```text
the theorem
+
the student's final copy
```

It does not see:
```text
"this copy was generated by the substitution mechanism"
```

Therefore, the reference label must be recalculated from the observable final copy.
It is this property that ensures that the benchmark actually measures the LLM's ability to diagnose the copy.

### 4.2 Label recalibration

In order not to bias the evaluation of the LLM (which only sees the final text and not the intent of the initial error mechanism), the generator retains certain information about the transformation actually applied:

- `removed_hypotheses`: gold assumptions explicitly removed;
- `invented_entries`: incorrect assumptions added or substituted for a gold assumption;
- `implication_swaps`: gold assumptions replaced by a stronger assumption that implies them.

This information makes it possible to distinguish the different cases.

#### 1. Pure omission

If an assumption is simply removed:

```text
Gold  : [A, B, C]
Copy : [A, C]
```
the generator records:

```python
removed_hypotheses = [B]
invented_entries = []
```

The copy is then classified as: `missing_hypothesis` or, if several assumptions have been removed: `multiple_missing`.

#### 2. Substitution by an incorrect assumption

If an assumption is replaced:

```text
Gold  : [A, B, C]
Copy : [A, D, C]
```
This is not a simple omission. The generator records the substitution in `invented_entries`:

```python
invented_entries.append({
    "invented": D,
    "instead_of": B
})
```

The final copy therefore contains an incorrect assumption in place of an expected assumption. It is classified as: `invented_hypothesis`. The fact that the total number of assumptions remains identical does not change this classification: the operation performed is a substitution B → D.

#### 3. Adding an extra assumption

If an assumption is added without replacing an existing assumption:
```text
Gold  : [A, B, C]
Copy : [A, B, C, D]
```
the generator records:
```python
invented_entries.append({
    "invented": D,
    "instead_of": None
})
```

The copy is also classified as: `invented_hypothesis`.

#### 4. Replacement by a stronger assumption

If a required assumption is replaced by a different but mathematically stronger assumption:
```text
Gold  : [A, B, C]
Copy : [A, D, C]

D ⇒ B
```
the generator records this operation in implication_swaps: `implication_swaps.append((D, B))`. Since D satisfies B, the copy remains correct. It then receives:
```text
validation_type = "stronger_hypothesis"
is_correct = True
```
*N.B.: When an assumption is replaced by substitution (`invented_hypothesis`), it may happen that the replacement assumption is stronger than the original assumption. Therefore, to avoid penalizing a copy that remains logically correct, a filtering block iterates through the list of `invented_entries`: if the substitution satisfies the original assumption (via `satisfait()`), the entry is removed from the errors and reclassified as a valid implication in `implication_swaps`.*

#### 5. No modification

If no degradation is actually possible, the generator sets:
```python
applied_error = "correct"
```
and if the final copy is identical to the gold:
```python
validation_type = "exact_match"
is_correct = True
```
**Important distinction between generation and validation**

The error type requested from the generator must be distinguished from the validation type assigned to the final copy.

`error_type` is used internally by `generate_copy()` to choose the degradation mechanism:

- correct
- missing_hypothesis
- multiple_missing
- invented_hypothesis
- valid_implication

The final result instead uses `validation_type`, which describes the nature of the copy actually produced:

- exact_match
- stronger_hypothesis
- missing_hypothesis
- multiple_missing
- invented_hypothesis
- unknown_error

Thus, `error_type` describes the operation requested from the generator, while `validation_type` describes the verdict obtained after generation.

#### **Avoiding Valid Implication False Positives:**

Some generation mechanisms may produce no effective modification.

If the generator attempts to reverse an interval on a theorem that contains none, the copy remains identical to the gold. Therefore, I have implemented a test that checks whether the copy was actually modified (if `cited_hypotheses` != gold) before allowing the `valid_implication` label. Otherwise, the copy is marked as `correct`.

#### **Unification of Invention Sub-mechanisms:**

Several internal mechanisms may produce an assumption that is not acceptable in the final copy.

For example:

- a poorly worded assumption;
- an invalid implication;
- an explicitly invented assumption;
- a substitution with an incorrect variant.

These mechanisms may be different from the generator's point of view, but they have one thing in common from the LLM's point of view: **the copy contains an assumption that does not correctly satisfy the theorem's requirements.**

They are therefore grouped under: `invented_hypothesis`.

This keeps the output sufficiently simple and stable for LLM evaluation.

Thus, the benchmark uses the following categories:

|Type | Meaning |
|---|---|
| **`correct`** | All required assumptions are satisfied |
| **`missing_hypothesis`** | A single required assumption is missing |
| **`multiple_missing`** | Several required assumptions are missing |
| **`invented_hypothesis`** | An incorrect, unrelated, or replacement assumption is present |
| **`valid_implication`** | An assumption different from the gold nevertheless satisfies the requirement because it is logically stronger |

### Category Priority

When several descriptions are possible, the following rules are applied in order:

1. Copy identical to gold → `correct`
2. An unrelated/incorrect assumption is present → `invented_hypothesis`
3. No unrelated assumption, a single gold assumption is missing → `missing_hypothesis`
4. No unrelated assumption, several gold assumptions are missing → `multiple_missing`
5. A stronger assumption satisfies a gold assumption → `valid_implication`

This hierarchy makes the labels **deterministic**.

### Final Generation Result

Each generated copy is represented as:
```python
{
    {
    "theorem_id": "T01",
    "name": "Rolle's Theorem",
    "copy": [...], # texts of the cited assumptions
    "expected": [...], # texts of the ground truth

    "is_correct": True/False,

    "reason": (
        "hypotheses match exactly"
        | "missing: ..."
        | "multiple_missing: ..."
        | "invented_hypothesis: ..."
        | "valid_implication: ..."
        | "unable to determine the exact error."
    ),

   "validation_type": (
        "exact\_match"
        | "stronger\_hypothesis"
        | "missing\_hypothesis"
        | "multiple\_missing"
        | "invented\_hypothesis"
        | "unknown\_error"
    )
}
}
```

---

## 5. Dataset Generation (`run_benchmark.py`)

The complete benchmark can be generated with:
```bash
python3 run_benchmark.py
```
The script:

- uses a fixed seed (to guarantee reproducibility)
- randomly selects a theorem
- selects an error mechanism
- generates a copy
- recalculates its verdict from the final copy
- repeats the operation N times (100 times by default)
- writes the result to benchmark_data.json

#### JSON Dataset Structure

The file: `benchmark_data.json` contains a list of dictionaries.

Example:
```json
[
  {
    "theorem_id": "T01",
    "name": "Rolle's Theorem",
    "copy": [
      "f is continuous on [a, b]",
      "f is differentiable on [a, b]",
      "f(a) = f(b)"
    ],
    "expected": [
      "f is continuous on [a, b]",
      "f is differentiable on ]a, b[",
      "f(a) = f(b)"
    ],
    "is_correct": true,
    "reason": "stronger_hypothesis: f is differentiable on [a, b] implies f is differentiable on ]a, b[",
    "validation_type": "stronger_hypothesis"
  }
]
```
---

## 6. Exporting to Other Formats (`exporter_tableau.py`)

```bash
python3 exporter_tableau.py
```

Transforme `benchmark_data.json` en :

- **`benchmark_data_tab.csv`** — colonnes : `ID`, `Théorème`, `Copie`, `Attendu`, `Correct (bool)`, `Correct (texte)`, `Raison`, `Type_erreur`
- **`benchmark_data_tab.md`** — même contenu en tableau Markdown, avec statistiques globales (total, correctes, fausses, répartition par type d'erreur, top 5 des raisons d'échec)

**Structure finale à 2 colonnes :**

| Colonne | Contenu |
|---|---|
| **Copie** | La liste des hypothèses citées par l'étudiant synthétique (texte français) |
| **Verdict** | `VRAI` / `FAUX` + raison précise si `FAUX` |

---

## 7. Vue finale du benchmark

Pour le LLM évalué, la structure conceptuelle est volontairement simple. Il reçoit :
```text
THÉORÈME
↓
Hypothèses attendues

COPIE DE L'ÉTUDIANT
↓
Hypothèses citées

QUESTION
↓
La copie est-elle correcte ?
Si non : pourquoi ?
```
Le LLM doit donc reconstruire le raisonnement logique.

---

## 8. Validation du benchmark

Avant de générer un dataset final, il est recommandé de valider les tables internes.

1. Pour les théorèmes : `python3 theoremes.py`

2. Pour les implications : `python3 implications.py`

Ces vérifications doivent notamment détecter :

- les ids inexistants ;
- les ids dupliqués lorsque cela est interdit ;
- les références à des hypothèses non présentes dans HYPOTHESES ;
- les incohérences dans les tables d'implications.

---

## 9. Extensibilité

Ajouter un nouveau théorème ne nécessite pas de modifier le pipeline général.

Il suffit de :

1. ajouter les nouveaux ids d'hypothèses nécessaires dans hypotheses.py
2. ajouter l'entrée du théorème dans theoremes.py
3. renseigner ses hypothèses gold
4. renseigner ses erreurs courantes
5. ajouter les implications valides correspondantes dans implications.py
6. ajouter éventuellement les fausses implications correspondantes
7. exécuter les scripts de validation
8. régénérer le dataset

| Domaine | Théorèmes couverts |
|---|---|
| Analyse | Rolle, Lagrange, TVI, Weierstrass, L'Hôpital, Taylor-Young, Taylor-Lagrange, TFA, IPP, Changement de variable |
| Séries | Critère de d'Alembert |
| Algèbre Linéaire | Rang, Base incomplète, Diagonalisabilité, Cayley-Hamilton, Spectral, Cauchy-Schwarz, Jordan |
| Topologie | Heine, Bolzano-Weierstrass |
| Suites | Convergence monotone, Suites adjacentes, Critère de Cauchy |
| Intégration | Convergence dominée |
| Équations Différentielles | Cauchy-Lipschitz, Superposition |
| Probabilités | TCL, LGN faible, Jensen |

---

## 10. Résumé du pipeline

Le benchmark génère des copies mathématiques synthétiques, puis demande à un LLM de déterminer si les hypothèses d'un théorème sont correctement satisfaites, en tenant compte des omissions, des hypothèses inventées et des implications logiques valides, avec une vérité terrain calculée indépendamment du mécanisme de génération.

Le fonctionnement global peut être résumé ainsi :
```text
                         ┌──────────────────┐
                         │   HYPOTHESES     │
                         │  id → texte      │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │    THEOREMES     │
                         │ gold hypotheses  │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │   IMPLICATIONS   │
                         │  valides/fausses │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ GENERER_COPIE    │
                         │ gold → erreur    │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ COPIE FINALE     │
                         │ observable       │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ RECALCUL LABEL   │
                         │ sur contenu réel │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ DATASET JSON     │
                         └────────┬─────────┘
                                  │
                         ┌────────┴────────┐
                         ▼                 ▼
                  ┌──────────────┐  ┌──────────────┐
                  │     CSV      │  │  Markdown    │
                  └──────────────┘  └──────────────┘
```