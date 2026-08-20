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

## 4. Génération des copies (`generer_copie.py`)

Une copie part toujours d'une version **100% correcte** de la vérité terrain, puis est dégradée selon un **mécanisme d'erreur initial** (omission, ajout, substitution, inversion d'intervalle) :

```text
gold
 ↓
mécanisme de dégradation
 ↓
copie synthétique
 ↓
recalcul du verdict
```

Les mécanismes de génération peuvent produire :

- une omission ;
- plusieurs omissions ;
- un ajout d'hypothèse ;
- une substitution ;
- une implication valide ;
- une implication invalide ;
- une inversion d'intervalle.

### 4.1 Le label dépend de la copie finale

Le benchmark ne doit pas supposer que le LLM connaît la manière dont la copie a été générée. Il ne voit que :
```text
le théorème
+
la copie finale de l'étudiant
```

Il ne voit pas :
```text
"cette copie a été générée par le mécanisme substitution"
```

Donc le label de référence doit être recalculé à partir de la copie finale observable.
C'est cette propriété qui garantit que le benchmark mesure réellement la capacité du LLM à diagnostiquer la copie.

### 4.2 Recalibrage des labels
Pour ne pas biaiser l'évaluation du LLM (qui ne voit que le texte final et non
l'intention du mécanisme d'erreur initial), le générateur conserve certaines
informations sur la transformation effectivement appliquée :

- `removed_hypotheses` : hypothèses du gold explicitement supprimées ;
- `invented_entries` : hypothèses incorrectes ajoutées ou substituées à une
  hypothèse du gold ;
- `implication_swaps` : hypothèses du gold remplacées par une hypothèse plus
  forte qui l'implique.

Ces informations permettent de distinguer les différents cas.

#### 1. Omission pure

Si une hypothèse est simplement supprimée :

```text
Gold  : [A, B, C]
Copie : [A, C]
```
le générateur enregistre :

```python
removed_hypotheses = [B]
invented_entries = []
```

La copie est alors classée : `missing_hypothesis` ou, si plusieurs hypothèses ont été supprimées : `multiple_missing`.

#### 2. Substitution par une hypothèse incorrecte

Si une hypothèse est remplacée :

```text
Gold  : [A, B, C]
Copie : [A, D, C]
```
Il ne s'agit pas d'une simple omission. Le générateur enregistre la substitution dans `invented_entries` :

```python
invented_entries.append({
    "invented": D,
    "instead_of": B
})
```

La copie finale contient donc une hypothèse incorrecte à la place d'une hypothèse attendue. Elle est classée : `invented_hypothesis`. Le fait que le nombre total d'hypothèses reste identique ne change pas cette
classification : l'opération réalisée est une substitution B → D.

#### 3. Ajout d'une hypothèse en plus

Si une hypothèse est ajoutée sans remplacer une hypothèse existante :
```text
Gold  : [A, B, C]
Copie : [A, B, C, D]
```
le générateur enregistre :
```python
invented_entries.append({
    "invented": D,
    "instead_of": None
})
```

La copie est également classée : `invented_hypothesis`.

#### 4. Remplacement par une hypothèse plus forte

Si une hypothèse requise est remplacée par une hypothèse différente mais mathématiquement plus forte :
```text
Gold  : [A, B, C]
Copie : [A, D, C]

D ⇒ B
```
le générateur enregistre cette opération dans implication_swaps : `implication_swaps.append((D, B))`. Comme D satisfait B, la copie reste correcte. Elle reçoit alors :
```text
validation_type = "stronger_hypothesis"
is_correct = True
```
#### 5. Aucune modification

Si aucune dégradation n'est effectivement possible, le générateur remet :
```python
applied_error = "correct"
```
et si la copie finale est identique au gold :
```python
validation_type = "exact_match"
is_correct = True
```
**Distinction importante entre génération et validation**

Il faut distinguer le type d'erreur demandé au générateur du type de validation attribué à la copie finale.

`error_type` est utilisé en interne par `generate_copy()` pour choisir le mécanisme de dégradation :

- correct
- missing_hypothesis
- multiple_missing
- invented_hypothesis
- valid_implication

Le résultat final utilise en revanche `validation_type`, qui décrit la nature de la copie effectivement produite :

- exact_match
- stronger_hypothesis
- missing_hypothesis
- multiple_missing
- invented_hypothesis
- unknown_error

Ainsi, `error_type` décrit l'opération demandée au générateur, tandis que `validation_type` décrit le verdict obtenu après génération.

#### **Éviter les faux positifs d'Implication Valide :**
Certains mécanismes de génération peuvent ne produire aucune modification effective.
Si le générateur tente d'inverser un intervalle sur un théorème qui n'en contient pas, la copie reste identique au gold. Donc j'ai mis en place un test qui vérifie si la copie a réellement été modifiée (`if cited_hypotheses != gold`) avant d'autoriser l'étiquette `valid_implication`. Dans le cas contraire, la copie est marquée comme `correct`.

#### **Unification des sous-mécanismes d'invention :**
Plusieurs mécanismes internes peuvent produire une hypothèse qui n'est pas acceptable dans la copie finale.

Par exemple :

- une hypothèse mal formulée ;
- une implication invalide ;
- une hypothèse explicitement inventée ;
- une substitution par une variante incorrecte.

Ces mécanismes peuvent être différents du point de vue du générateur, mais ils ont un point commun du point de vue du LLM : **la copie contient une hypothèse qui ne satisfait pas correctement les exigences du théorème.**

Ils sont donc regroupés sous : `invented_hypothesis`.

Cela permet de garder une sortie suffisamment simple et stable pour l'évaluation du LLM.

Ainsi, le benchmark utilise les catégories suivantes :

| Type | Signification |
|---|---|
| **`correct`** | Toutes les hypothèses requises sont satisfaites |
| **`missing_hypothesis`** | Une seule hypothèse requise est absente |
| **`multiple_missing`** | Plusieurs hypothèses requises sont absentes |
| **`invented_hypothesis`** | Une hypothèse incorrecte, étrangère ou remplaçant une hypothèse attendue est présente |
| **`valid_implication`** | Une hypothèse différente de la gold satisfait néanmoins l'exigence car elle est logiquement plus forte |

### Priorité des catégories

Quand plusieurs descriptions sont possibles, les règles suivantes sont appliquées dans l'ordre :

1. Copie identique au gold → `correct`
2. Une hypothèse étrangère/incorrecte est présente → `invented_hypothesis`
3. Aucune hypothèse étrangère, une seule hypothèse gold manque → `missing_hypothesis`
4. Aucune hypothèse étrangère, plusieurs hypothèses gold manquent → `multiple_missing`
5. Une hypothèse plus forte satisfait une hypothèse gold → `valid_implication`

Cette hiérarchie permet de rendre les labels **déterministes**.

### Résultat final de la génération

Chaque copie produite est représentée sous la forme :
```python
{
    {
    "theoreme_id": "T01",
    "nom": "Théorème de Rolle",

    "copie": [...], # textes français affichés
    "attendu": [...], # textes français de la vérité terrain

    "est_correcte": True/False,

    "raison": (
        "OK"
        | "missing: ..."
        | "multiple_missing: ..."
        | "invented_hypothesis: ..."
        | "valid_implication: ..."
    ),

    "type_erreur": (
        "missing_hypothesis"
        | "multiple_missing"
        | "invented_hypothesis"
        | "valid_implication"
        | "correct"
    )
}
}
```

---

## 5. Génération du dataset (`run_benchmark.py`)

Le benchmark complet peut être généré avec :
```bash
python3 run_benchmark.py
```
Le script :
 - utilise une seed fixe (pour garantir la reproductibilité)
 - sélectionne aléatoirement un théorème
 - sélectionne un mécanisme d'erreur
 - génère une copie
 - recalcule son verdict à partir de la copie finale
 - répète l'opération N fois (100 fois par défaut)
 - écrit le résultat dans benchmark_data.json
  
#### Structure du dataset JSON

Le fichier : `benchmark_data.json` contient une liste de dictionnaires.

Exemple :
```json
[
  {
    "theoreme_id": "T01",
    "nom": "Théorème de Rolle",
    "copie": [
      "f est continue sur [a, b]",
      "f est dérivable sur ]a, b[",
      "f(a) = f(b)"
    ],
    "attendu": [
      "f est continue sur [a, b]",
      "f est dérivable sur ]a, b[",
      "f(a) = f(b)"
    ],
    "est_correcte": true,
    "raison": "OK",
    "type_erreur": "correct"
  }
]
```
---

## 6. Exportation sous d'autres formats (`exporter_tableau.py`)

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