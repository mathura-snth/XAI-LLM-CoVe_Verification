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
* **Chargement et Analyse Exploratoire des Données (EDA)** — Lit le fichier CSV et effectue une vérification :
  * *Le Contrôle* : Affiche un aperçu des données (`df.head()`, les 5 premières lignes) pour vérifier le bon format.
  * *La Distribution* : Calcule et génère un graphique (`countplot`) de la répartition de la colonne cible (les classes).
  * *Classe minoritaire* : Cette étape est **importante** pour identifier un éventuel **déséquilibre** des données.
  >*N.B : Si une classe est trop minoritaire, l'arbre de décision risque de devenir "paresseux" (en prédisant toujours la classe majoritaire pour s'assurer un bon score mathématique).*
* **Entraînement de l'arbre** — DecisionTreeClassifier de scikit-learn + Grid Search pour optimiser les hyperparamètres. Ce bloc configure une machine qui va tester des dizaines d'arbres différents pour sortir le meilleur arbre possible qu'on va envoyer au Module 1 pour que le LLM l'explique.
* **Conversion de l'arbre en CNF/DNF** — appel à `my_tree.py` pour obtenir `dnf` (les chemins "classe 1") et `phi` (les chemins "classe 0"), nécessaires à l'évaluation formelle.
  * Le Traducteur (bina) : Crée un dictionnaire qui associe chaque règle de l'arbre (ex: 'immigration <= 0.5') à un numéro de variable logique (1, 2, 3...).
  * Binarisation : Convertit le profil du patient/votant évalué en format mathématique (ex: [1, -2, 3...] où positif = condition remplie, négatif = condition non remplie).
  * Matrices Logiques (dnf et phi) : L'arbre géant est transformé en listes de nombres (ex: [[4, 3, -2, 1], ...]). dnf représente tous les chemins menant à la classe 1, et phi ceux menant à la classe 0. C'est cette matrice qui sera évaluée par rapport aux règles du LLM pendant l'évaluation finale.
* **Calcul SHAP** — calcul des valeurs d'importance de chaque feature pour une instance donnée.