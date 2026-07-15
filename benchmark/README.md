# Benchmark Synthétique

Les théorèmes mathématiques ont des hypothèses **formelles et vérifiables** — comme les règles d'un arbre de décision.

On génère synthétiquement des réponses d'étudiants appliquant un théorème (correctement ou non), et on mesure si le LLM détecte les hypothèses manquantes, mal citées, ou inventées.

---
## Principe général
Chaque théorème a une liste d'hypothèses obligatoires (la vérité terrain). Une copie est une version dégradée ou correcte de cette liste, à laquelle est associé un verdict : VRAI / FAUX et, si FAUX, une raison précise.

À noter que le benchmark ne compare **jamais** du texte en toute lettre : les comparaisons se font sur des identifiants *(ex : F_CONTINUE_FERME)*. Le texte français n'existe que pour l'affichage. C'est pour éliminer les faux négatifs dus aux différences de formulation ("f continue" au lieu de "f est continue").

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

## 3. L'ensemble des hypothèses (`hypotheses.py`)

```python
HYPOTHESES = {
    "F_CONTINUE_FERME":  "f est continue sur [a, b]",
    "F_DERIVABLE_OUVERT": "f est dérivable sur ]a, b[",
    "F_EGAL_BORNES":      "f(a) = f(b)",
    # etc
}
```
- Le fichier contient deux fonctions :
  - `texte(hyp_id)` → renvoie le texte français d'un id
  - `textes(hyp_ids)` → renvoie la liste des textes pour une liste d'ids

---

## Les théorèmes (`theoremes.py`)

Chaque théorème est défini uniquement en termes d'ids :

```python
"T01": {
    "nom": "Théorème de Rolle",
    "hypotheses": ["F_CONTINUE_FERME", "F_DERIVABLE_OUVERT", "F_EGAL_BORNES"],
    "conclusion": "∃ c ∈ ]a, b[ tel que f'(c) = 0",
    "erreurs_courantes": ["F_CONTINUE_OUVERT", "F_DERIVABLE_FERME", "F_DERIVABLE_BORNES"],
},
```

- **`hypotheses`** : la vérité terrain, la liste exhaustive et obligatoire des hypothèses du théorème.
- **`erreurs_courantes`** : des ids d'hypothèses **plausibles mais incorrectes** pour simuler des copies mal formulées ou inventées. Ce ne sont **jamais** des hypothèses valides pour ce théorème — une erreur courante ne doit jamais apparaître comme `plus_fort` d'une implication valide vers une hypothèse gold du même théorème.

**30 théorèmes** du niveau L3 mathématiques : Analyse, Algèbre Linéaire, Topologie, Probabilités.

---

## Les implications (`implications.py`)

Pour déterminer si une hypothèse citée, même différente de la hypothèse requise, la **satisfait tout de même** parce qu'elle est logiquement plus forte.

### Implications valides — `IMPLICATIONS_LIST`

Liste de paires `(plus_fort, plus_faible)` mathématiquement vraies :

```python
IMPLICATIONS_LIST = [
    ("F_DERIVABLE_OUVERT", "F_CONTINUE_OUVERT"),
    ("F_CLASSE_C1", "F_DERIVABLE_OUVERT"),
    ("F_CONTINUE_FERME", "F_CONTINUE_OUVERT"),
    # ...
]
```

**Règle de validation pour chaque paire ajoutée à la table :**
- L'implication doit être **vraie isolément**, sans hypothèse supplémentaire sous-entendue. (`"croissante ⟹ bornée"` est **faux** il manque "majorée" ; une conjonction de deux hypothèses ne se code pas comme une implication à un seul terme)
- Un id d'`erreurs_courantes` d'un théorème **ne doit jamais** apparaître comme `plus_fort` impliquant une hypothèse `gold` de ce même théorème, sinon l'erreur courante passera comme valide
- Pas de doublons de paires
- Chaque id utilisé doit exister dans `HYPOTHESES` (une fonction en fait la vérificatin)

### Implications invalides — `MAUVAISES_IMPLICATIONS`

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

### La fonction `satisfait()`

```python
def satisfait(hypotheses_citees, hypothese_requise):
    """
    True si hypothese_requise est citée directement,
    ou si elle est déduite par une chaîne d'implications valides
    à partir d'une hypothèse présente dans hypotheses_citees.
    """
```

Recherche **récursive** dans `IMPLICATIONS_LIST` (on utimose une ensemble `visites` pour éviter les cycles), jamais dans `MAUVAISES_IMPLICATIONS`.

---

## Génération des copies (`generer_copie.py`)

Une copie part toujours d'une version **100% correcte** de la vérité terrain, puis est dégradée selon un **type d'erreur** :

| Type d'erreur | Effet |
|---|---|
| **`correcte`** | Aucune dégradation |
| **`hypothese_manquante`** | Une hypothèse gold est retirée |
| **`plusieurs_manquantes`** | Entre 2 et n−1 hypothèses gold sont retirées |
| **`hypothese_inventee`** | Tire au sort un sous-type : remplace une hypothèse gold par une erreur courante, ajoute une erreur courante en plus, ou inverse un intervalle (FERME ↔ OUVERT) |
| **`implication_valide`** | Une hypothèse gold est remplacée par une hypothèse **plus forte et valide** (tirée de `IMPLICATIONS_LIST`) → doit rester `VRAI` |
| **`implication_invalide`** | Une hypothèse gold est remplacée par une hypothèse **invalide** (tirée de `MAUVAISES_IMPLICATIONS`) → doit être `FAUX` |

### Calcul du verdict

Pour chaque hypothèse `h` de la vérité terrain :
1. Si `satisfait(hypotheses_citees, h)` est vrai → hypothèse validée (directement ou par implication)
2. Sinon → copie fausse, raison enregistrée (`manquante`, `mal_formulee`, `implication_invalide`, `inventee`, etc)

Le résultat final contient :

```python
{
    "theoreme_id": "T01",
    "nom": "Théorème de Rolle",
    "copie": [...],              # textes français affichés
    "attendu": [...],            # textes français de la vérité terrain
    "est_correcte": True/False,
    "raison": "OK" | "manquante: ..." | "mal_formulee: ..." | ...,
    "type_erreur": "hypothese_manquante" | ...,
}
```

---

## Génération du dataset (`run_benchmark.py`)

```bash
python3 run_benchmark.py
```

- Tire aléatoirement (seed fixée pour reproductibilité) un théorème et un type d'erreur, `N` fois (défaut 100)
- Exporte `benchmark_data.json` : une liste de dictionnaires
- Affiche un résumé en 2 colonnes (`COPIE` / `VERDICT`) et des statistiques globales (total, correctes, incorrectes)

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

## Version anglaise

Une version anglophone de ce benchmark est disponible. Elle repose exactement sur la même architecture logique, les mêmes théorèmes et les mêmes identifiants de validation, mais les chaînes de caractères affichées dans les JSON générés sont traduites en anglais pour permettre l'évaluation de LLMs sur des prompts anglophones.

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