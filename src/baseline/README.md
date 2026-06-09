# Code de référence : Pipeline XAI-LLM (Bounia & Ndour)

Ce dossier contient le code source original du projet de recherche **"Democratizing AI Explainability through a Hybrid XAI-LLM Framework"**. Il constitue la **baseline** sur laquelle s'appuie le stage.

---

## Vue d'ensemble du pipeline

Le pipeline transforme un arbre de décision entraîné en une explication en langage naturel, puis évalue mathématiquement si cette explication est fidèle au modèle.

```
Dataset CSV
    ↓
Arbre de décision (scikit-learn)
    ↓
Représentation CNF/DNF (my_tree.py, encodage_CNF.py)
    ↓
[Module 1] Génération de l'explication (LLM + prompt SHAP) → texte naturel
    ├── C'est ici qu'on injecte la méthode CoVe
    ↓
[Module 2] Parsing des règles (LLM + few-shot) → liste de règles logiques
    ↓
[Module 3] Évaluation duale
    ├── Non-formelle : un second LLM vérifie la cohérence → score %
    └── Formelle    : W_f(phi, règles, n) → score 1 − ε_h,x
```

---

## Description fichier par fichier

### `notebook_implementation.ipynb`

C'est le notebook principal. Il faut le lire et le faire tourner en premier.

**Ce qu'il fait :**

* **Chargement des packages** — importe scikit-learn, pysat, les modules maison, et le client LLM.
* **DatasetManager & Configuration** — lit `datasets_config.yaml` pour charger la "carte d'identité" du dataset ciblé (chemin CSV, colonne cible, etc.) en changeant juste son nom ("diabetes", "compas", etc.). Évite de réécrire le même code pour chaque dataset.
* **Chargement et Analyse Exploratoire des Données** — Lit le fichier CSV et effectue une vérification :
  * *Le Contrôle* : Affiche un aperçu des données (`df.head()`, les 5 premières lignes) pour vérifier le bon format.
  * *La Distribution* : Calcule et génère un graphique (`countplot`) de la répartition de la colonne cible (les classes).
  * *Classe minoritaire* : Cette étape est **importante** pour identifier un éventuel **déséquilibre** des données.
  >*N.B : Si une classe est trop minoritaire, l'arbre de décision risque de devenir "paresseux" (en prédisant toujours la classe majoritaire pour s'assurer un bon score mathématique).*
* **Entraînement de l'arbre, IA Prédictive** — DecisionTreeClassifier de scikit-learn + Grid Search pour optimiser les hyperparamètres. Ce bloc configure une machine qui va tester des dizaines d'arbres différents pour sortir le meilleur arbre possible qu'on va envoyer au Module 1 pour que le LLM l'explique.
  >*N.B. : DecisionTreeClassifier est une IA spécialisée et muette : elle sait faire qu'une seule chose (ex: détecter le diabète), et elle répond juste par "0" ou "1", contrairement au LLM qui est une IA générative (ex ChatGPT) qui sait parler de tout et s'exprime en langage naturel.*
* **Conversion de l'arbre en CNF/DNF** — appel à `my_tree.py` pour obtenir `dnf` (les chemins "classe 1") et `phi` (les chemins "classe 0"), nécessaires à l'évaluation formelle.
  * Le Traducteur (bina) : Crée un dictionnaire qui associe chaque règle de l'arbre (ex: 'immigration <= 0.5') à un numéro de variable logique (1, 2, 3...).
  * Binarisation : Convertit le profil du patient/votant évalué en format mathématique (ex: [1, -2, 3...] où positif = condition remplie, négatif = condition non remplie).
  * Matrices Logiques (dnf et phi) : L'arbre géant est transformé en listes de nombres (ex: [[4, 3, -2, 1], ...]). dnf représente tous les chemins menant à la classe 1, et phi ceux menant à la classe 0. C'est cette matrice qui sera évaluée par rapport aux règles du LLM pendant l'évaluation finale.
* **Calcul SHAP** — calcul des valeurs d'importance de chaque feature pour une instance donnée.
* **[Module 1] Génération de l'explication, IA Générative** — e pipeline transforme la décision mathématique en langage naturel via 5 étapes clés :
  * Extraction de l'instance : Sélection d'un profil (ligne du CSV) et récupération de la prédiction brute (ex: Classe 0) par l'IA prédictive.
  * System Prompt : Création d'un moule de prompt qui impose un rôle d'expert et réserve des espaces vides (entre accolades "{}") pour les données.
  * User Query (préparation de la requête) : Définition de la consigne explicite adressée au LLM.
  * Prompt Filling : Remplissage du moule avec les données réelles (instance, objectif, etc) via la fonction .format().
  * Appel LLM : Transmission du prompt complet aux serveurs distants (GPT-4/Claude) et réception du texte explicatif.
  >*N.B. : Les variables de remplacement (instance_dict, model_objectif) sont définies comme des espaces réservés ("vides") et automatiquement remplies par des données réelles lors du Prompt Filling grâce à .format().*

  >*N.B. : `local_interpretation = ""` crée un scénario de test à "basse fidélité" ; laisser ce champ vide permet d'observer les hallucinations du LLM lorsqu'il travaille sans aide (point de comparaison pour prouver l'efficacité de CoVe.)*

  >*N.B. : En les injectant SHAP, LIME et Anchors dans le champ local_interpretation, on donne au LLM les preuves pour éviter qu'il ne devine (et hallucine) les raisons de la décision du modèle.*
* **[Module 2] Extraction des règles** — un second prompt (few-shot) demande au LLM d'extraire de l'explication textuelle une liste Python de règles logiques du type `['glucose > 127.5', 'age <= 50']`.
* **[Module 3a] Évaluation non-formelle** — un troisième prompt donne au LLM la CNF du modèle et les règles extraites, et lui demande de vérifier leur cohérence. Retourne un score sur 100.
* **[Module 3b] Évaluation formelle** — `bina_term_transform` convertit les règles textuelles en représentation binaire, puis `W_f(phi, règles, n)` calcule l'erreur formelle. Le score final est `(1 - W_f) * 100`.

---

### `llm_calling.py` — Interface avec les LLMs

Contient la classe `LlmCalling` avec une méthode par LLM. Utilise les clés API stockées dans `.env` (fichier non versionné).

| Méthode | Modèle |
|---|---|
| `OpenAI_llm(prompt)` | GPT-4o |
| `claud_llm(prompt)` | Claude Sonnet 4 |
| `deepseek_llm(prompt)` | DeepSeek Chat |
| `gemini_llm(prompt)` | Gemini 1.5 Flash |
| `grok_llm(prompt)` | Grok-3 |
| `llama_llm(prompt)` | LLaMA 3.1 8B (via HuggingFace) |

Toutes les méthodes prennent un `prompt` (string) et retournent la réponse (string).

---

### `my_tree.py` — Représentation logique de l'arbre

C'est le fichier le plus complexe et le plus important pour la partie formelle.

**Ce qu'il fait :**
- Importe un `DecisionTreeClassifier` scikit-learn et le convertit en une structure interne (`decision_tree`).
- Calcule les **DNF orthogonales** : pour chaque classe cible, liste tous les chemins de l'arbre qui mènent à cette classe, sous forme de clauses logiques.
  - `dnf` = chemins menant à la classe 1 (prédiction positive)
  - `phi` = chemins menant à la classe 0 (négation, utile pour calculer l'erreur)
- `binarized_instance(instance)` : convertit une instance (valeurs réelles) en instance binaire selon les seuils de l'arbre.
- `find_direct_reason(instance)` : trouve l'explication minimale (raison directe) d'une prédiction — le sous-ensemble minimal de features qui suffit à expliquer la décision.
- `unbinarized_instance(reason)` : reconvertit une raison binaire en valeurs lisibles.
- `bina` : dictionnaire qui mappe chaque condition `(feature, seuil)` à un indice binaire — c'est ce référentiel qu'utilisent `bina_term_transform` et `W_f`.

---

### `encodage_CNF.py` — Encodage booléen de l'arbre

Transforme l'arbre de décision en formule CNF (Conjunctive Normal Form), une représentation logique utilisée par les solveurs SAT. Utilisé par `my_tree.py`.

**Pourquoi CNF ?** La CNF permet d'utiliser des solveurs SAT (comme Glucose4 via pysat) pour prouver formellement des propriétés sur le modèle — notamment vérifier si une règle est compatible ou non avec le comportement de l'arbre.

---

### `dtree.py` — Structure de données arbre (encodage Arenas 2022)

Définit les classes `DecisionTree` et `DTNode` pour représenter un arbre de décision comme structure récursive. Utilisé par `encoder.py` pour l'encodage SAT du papier Arenas et al. 2022 (approche différente de `my_tree.py`).

**Différence avec `my_tree.py`** : `dtree.py` travaille avec des arbres booléens purs (features binaires), tandis que `my_tree.py` gère les arbres à seuils réels (features continues comme `glucose > 127.5`).

---

### `encoder.py` — Encodage SAT (Arenas et al. 2022)

Génère les clauses CNF pour résoudre le problème : *"existe-t-il une explication de taille ≤ k avec une erreur ≤ δ ?"*. Utilise `dtree.py` et `utils.py`. Correspond à l'encodage du papier de référence de l'équipe du LIPN.

---

### `gen_dt.py` — Génération et sauvegarde d'arbres

Contient des utilitaires pour :
- `dt_to_file(dt, filename, ...)` : sauvegarder un arbre scikit-learn en fichier JSON (format utilisé par `dtree.py`).
- `generate_random_dt(...)` : générer des arbres aléatoires (utile pour les tests synthétiques).

---

### `utils.py` — Fonctions logiques bas niveau

Fonctions utilitaires pour la manipulation de formules SAT : addition binaire de variables booléennes, contraintes de cardinalité (`at_most_k`), export au format DIMACS. Utilisé uniquement par `encoder.py`.

---

### `datasets_config.yaml` — Configuration centralisée des datasets

Fichier clé pour comprendre comment le notebook charge les données automatiquement. Pour chaque dataset, il stocke :

- `chemin_csv` : chemin vers le fichier CSV
- `colonne_cible` : la colonne à prédire
- `objectif_classification` : description du problème (injectée dans les prompts LLM)
- `tests_result.exemple` : **un exemple manuel** d'explication textuelle + les règles logiques correspondantes → c'est l'exemple few-shot qui sert à guider le Module 2 (parsing)

---

### `datasets_description.yaml` — Métadonnées des datasets

Descriptions humaines des datasets (nombre de lignes, colonnes, classes). Utilisé pour la documentation, pas directement dans le code.

---

### `preprocessing_dataset.ipynb` — Prétraitement des données brutes

Notebook de nettoyage des datasets. Lit les fichiers bruts depuis `raw/`, les transforme (encodage des catégories, suppression de colonnes inutiles, renommage) et les sauvegarde dans `datasets/`. À exécuter une seule fois par dataset.

---

### `UAI_2023__example_to_use_the_code_.py` et `.html`

Exemple d'utilisation du pipeline formel (sans LLM) sur les datasets `tic-tac-toe` et `mnist49`. Montre comment utiliser `W_f`, `Approx_ascendant`, `Approx_descent` et `Dichotomie`. Bon point de départ pour comprendre la partie formelle isolément.

---

## Ordre de lecture recommandé

Pour comprendre le projet dans l'ordre logique :

1. `datasets_config.yaml` — comprendre la structure des données et les exemples few-shot
2. `UAI_2023__example_to_use_the_code_.html` — voir le pipeline formel seul (sans LLM), bien commenté
3. `notebook_implementation.ipynb` — lire le pipeline complet de bout en bout **sans l'exécuter** d'abord
4. `my_tree.py` — comprendre comment l'arbre est converti en DNF/phi
5. `llm_calling.py` — comprendre comment les LLMs sont appelés
6. Exécuter le notebook sur `vote_house_84` (le dataset le plus simple)

---

## Installation

```bash
# Dépendances principales
pip install scikit-learn pandas numpy shap matplotlib tqdm python-dotenv pyyaml openai anthropic google-generativeai

# PySAT (solveur SAT — indispensable pour my_tree.py et encoder.py)
pip install python-sat
```

> ⚠️ PySAT nécessite Python 3.7+ et pèse environ 50 Mo avec ses solveurs compilés (Glucose4, Minisat22). L'installation est simple via pip mais peut nécessiter un compilateur C sur certains systèmes.

---

## Fichier `.env` (non versionné)

Créer un fichier `.env` à la racine avec :

```
OPENAI_API_KEY=sk-...
CLAUD_API_KEY=sk-ant-...
DEEPSEEK_API_KEY=...
GEMINI_API_KEY=...
GROK_API_KEY=...
HUGGINGFACE_API_KEY=...
```