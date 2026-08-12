# Benchmark Synthétique

Les théorèmes mathématiques ont des hypothèses **formelles et vérifiables** — comme les règles d'un arbre de décision.

On génère synthétiquement des réponses d'étudiants appliquant un théorème (correctement ou non), et on mesure si le LLM détecte les hypothèses manquantes, mal citées, ou inventées.

Il ne s'agit pas que de vérifier une égalité exacte entre listes d'hypothèses, mais de tester le raisonnement du LLM sur la présence, l'absence, le remplacement et les implications logiques.

L'objectif est donc de distinguer plusieurs situations différentes :

- toutes les hypothèses requises sont présentes → `correct`
- une ou plusieurs hypothèses requises sont absentes → `missing_hypothesis` ou `multiple_missing`
- une hypothèse attendue a été remplacée par une hypothèse incorrecte ou étrangère au théorème → `invented_hypothesis`
- une hypothèse différente est **plus forte** qu'une hypothèse requise et permet donc de la satisfaire → `valid_implication`.

*N.B. : une hypothèse plus forte qui permet de satisfaire une hypothèse requise par une implication valide est considérée comme **correcte**. Il s'agit d'un choix volontaire afin de tester la capacité du LLM à effectuer un raisonnement logique, plutôt qu'à vérifier uniquement l'identité textuelle des hypothèses.*

**Règle importante :** lorsqu'une hypothèse attendue est remplacée par une autre hypothèse qui ne satisfait pas la première, on considère qu'il s'agit d'une `invented_hypothesis`, et non d'une combinaison `missing_hypothesis` + `invented_hypothesis`. L'intention du mécanisme est donc interprétée comme une **substitution**.

---

## Principe général

Chaque théorème a une liste d'hypothèses obligatoires, **la vérité terrain** (gold standard).

Une copie synthétique est ensuite générée à partir de cette vérité terrain. Elle peut être :

- correcte ;
- privée d'une hypothèse ;
- privée de plusieurs hypothèses ;
- enrichie ou modifiée par une hypothèse incorrecte ;
- construite avec une hypothèse plus forte qui implique une hypothèse requise ;
- construite avec une hypothèse qui ressemble à une implication valide mais qui ne l'est pas.

À chaque copie est associé un verdict :

- `VRAI` si toutes les hypothèses nécessaires sont satisfaites ;
- `FAUX` sinon.

Lorsqu'une copie est fausse, une raison et un type d'erreur précis sont également associés.

### Comparaison par identifiants

À noter que le benchmark ne compare **jamais** du texte en toutes lettres : les comparaisons se font sur des identifiants *(ex : F_CONTINUE_FERME)*. Le texte français n'existe que pour l'affichage.

*N.B. : Le but étant d'éliminer les faux négatifs dus aux différences de formulation ("f continue" au lieu de "f est continue").*

---

## Architecture du dossier

| Fichier | But |
|---|---|
| **`hypotheses.py`** | Catalogue de toutes les hypothèses associées à leur id : `id → texte affiché` |
| **`theoremes.py`** | Définit les 30 théorèmes : hypothèses obligatoires (ids), conclusion, erreurs courantes (ids) |
| **`implications.py`** | Ensemble d'implications logiques **valides** et **invalides** et la fonction `satisfait()` |
| **`generer_copie.py`** | Génère une copie synthétique dégradée selon un type d'erreur donné (ou sans erreur) et calcule du verdict |
| **`run_benchmark.py`** | Génère N copies (par défaut 100) |
| **`exporter_tableau.py`** | Convertit le .json en .csv et .md |

---

## 1. L'ensemble des hypothèses (`hypotheses.py`)

Le fichier hypotheses.py constitue le catalogue central des hypothèses.

```python
HYPOTHESES = {
    "F_CONTINUE_FERME":  "f est continue sur [a, b]",
    "F_DERIVABLE_OUVERT": "f est dérivable sur ]a, b[",
    "F_EGAL_BORNES":      "f(a) = f(b)",
    # etc
}
```

Chaque hypothèse possède :
1. un identifiant stable, utilisé par tout le benchmark ;
2. un texte français, utilisé uniquement pour l'affichage et la génération de la copie présentée au LLM.

Le fichier contient deux fonctions :
  - `texte(hyp_id)` → renvoie le texte français d'un id
  - `textes(hyp_ids)` → renvoie la liste des textes pour une liste d'ids

---

## 2. Les théorèmes (`theoremes.py`)

Chaque théorème est défini uniquement en termes d'ids :

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

- **`hypotheses`** : la vérité terrain, la liste exhaustive et obligatoire des hypothèses du théorème.
- **`conclusion`** : c'est le résultat attendu lorsque toutes les hypothèses sont satisfaites.
- **`erreurs_courantes`** : des ids d'hypothèses **plausibles mais incorrectes** pour simuler des copies mal formulées ou inventées.

**Règle importante :** Ce ne sont **jamais** des hypothèses valides pour ce théorème — une erreur courante ne doit jamais apparaître comme `plus_fort` d'une implication valide vers une hypothèse gold du même théorème.

---

## 3. Les implications (`implications.py`)

Le fichier implications.py formalise les relations logiques entre hypothèses.

Elle permet de déterminer si une hypothèse citée, même différente de l'hypothèse requise, la **satisfait tout de même** parce qu'elle est logiquement plus forte.

Par exemple :
```text
f est de classe C¹
        ↓
f est dérivable
```
Donc si le théorème exige seulement que f soit dérivable et que l'étudiant indique que f est de classe C¹, l'hypothèse est satisfaite.

### 3.1 Implications valides — `IMPLICATIONS_LIST`

Liste de paires `(plus_fort, plus_faible)` mathématiquement vraies :

```python
IMPLICATIONS_LIST = [
    ("F_DERIVABLE_OUVERT", "F_CONTINUE_OUVERT"),
    ("F_CLASSE_C1", "F_DERIVABLE_OUVERT"),
    ("F_CONTINUE_FERME", "F_CONTINUE_OUVERT"),
    # ...
]
```

### 3.2 Règles de validation pour chaque paire ajoutée à la table

- L'implication doit être **vraie isolément**, sans hypothèse supplémentaire sous-entendue. (`"croissante ⟹ bornée"` est **faux** il manque "majorée" ; une conjonction de deux hypothèses ne se code pas comme une implication à un seul terme)
- Un id d'`erreurs_courantes` d'un théorème **ne doit jamais** apparaître comme `plus_fort` impliquant une hypothèse `gold` de ce même théorème, sinon l'erreur courante passera comme valide
- Pas de doublons de paires
- Chaque id utilisé doit exister dans `HYPOTHESES` (une fonction en fait la vérificatin)

### 3.3 Implications invalides — `MAUVAISES_IMPLICATIONS`

Liste de paires qui **ressemblent** à des implications valides mais sont fausses (c'est le genre de piège que le LLM doit détecter)

```python
MAUVAISES_IMPLICATIONS = [
    ("F_CONTINUE_OUVERT", "F_CONTINUE_FERME"),   # ouvert n'implique PAS fermé
    ("F_DERIVABLE_OUVERT", "F_DERIVABLE_FERME"), # idem
    ("F_INTEGRABLE_FERME", "F_CONTINUE_FERME"),  # intégrable n'implique pas continue
    # ...
]
```

Ces paires servent à générer le type d'erreur `implication_invalide`, elles ne sont jamais utilisées par `satisfait()`.

``` text
IMPLICATIONS_LIST
        ↓
raisonnement logique autorisé

MAUVAISES_IMPLICATIONS
        ↓
erreurs volontairement générées
```

### 3.4 La fonction `satisfait(hypotheses_citees, hypothese_requise)`

Elle répond à la question : *Une hypothèse requise par le théorème est-elle satisfaite par les hypothèses effectivement citées dans la copie ?*

Elle retourne `True` dans deux cas :

1. l'hypothèse requise est citée directement
2. une hypothèse citée est plus forte et implique l'hypothèse requise par une chaîne d'implications valides

```python
def satisfait(hypotheses_citees, hypothese_requise):
    """
    True si hypothese_requise est citée directement,
    ou si elle est déduite par une chaîne d'implications valides
    à partir d'une hypothèse présente dans hypotheses_citees.
    """
```

Recherche **récursive** dans `IMPLICATIONS_LIST` (on utilise un ensemble `visites` pour éviter les cycles), jamais dans `MAUVAISES_IMPLICATIONS`.

---

## 4.Génération des copies (`generer_copie.py`)

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

## Génération du dataset (`run_benchmark.py`)

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

## Exportation sous d'autres formats (`exporter_tableau.py`)

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

## Extensibilité

Ajouter un théorème ne modifie pas le pipeline d'évaluation :

1. Ajouter les nouveaux ids d'hypothèses nécessaires dans `hypotheses.py`
2. Ajouter l'entrée du théorème dans `theoremes.py` (`hypotheses` + `erreurs_courantes`, en ids)
3. Ajouter les nouvelles implications valides et invalides correspondantes dans `implications.py`
4. Relancer `python3 theoremes.py` et `python3 implications.py` pour vérifier qu'aucun id n'est manquant ou dupliqué avant de régénérer le dataset

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