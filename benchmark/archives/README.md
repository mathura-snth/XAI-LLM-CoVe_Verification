# Archives : Fondements du Benchmark Mathématique

Ce dossier `archives/` constitue la mémoire du projet **Math LLM Verifier**. 

Il regroupe les toutes premières versions des scripts et les itérations algorithmiques initiales en français, avant leur traduction, optimisation et refactorisation dans le dossier principal [eng_ver/](../eng_ver).

**Attention :** Le code présent ici n'est plus maintenu et ne doit pas être utilisé comme tests finaux. Pour générer un benchmark ou évaluer un modèle, veuillez utiliser exclusivement le dossier [eng_ver/](../eng_ver).

---

## Contenu de l'archive

Vous y trouverez les versions "brouillons" qui ont permis de forger la logique formelle du projet :

* **`theoremes.py` & `hypotheses.py`** : Les dictionnaires de théorèmes et de leurs hypothèses associées, avec leurs identifiants initiaux.
* **`implications.py` & `implications.md`** : L'ébauche du moteur de logique formelle, définissant les implications mathématiques valides et invalides.
* **`generer_copie.py`** : Le prototype du script chargé de dégrader la vérité terrain pour créer des copies d'étudiants synthétiques avec différentes catégories d'erreurs.
* **`run_benchmark.py`** : Le premier script orchestrant la génération des données.
* **`exporter_tableau.py`** : Les premiers essais de formatage des résultats.
* **Fichiers de données** (`benchmark_data.json`, `benchmark_data_tab.csv`, `benchmark_data_tab.md`) : Des extraits d'anciennes générations conservés à titre d'exemple historique.

---

Ce dossier est conservé à des fins de :
1. **Traçabilité** : Permettre de comprendre l'évolution de l'algorithme, notamment le passage d'une vérification textuelle simple à un moteur d'implications formelles.
2. **Référence** : Garder une trace des premiers choix d'architecture et des noms de variables originaux en français (ex: `F_CONTINUE_FERME`).
3. **Documentation** : Illustrer le processus itératif propre au développement d'un outil d'évaluation IA robuste.

**Retourner à la racine du projet pour accéder à la version active (`eng_ver/`).**