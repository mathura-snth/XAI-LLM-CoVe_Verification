# Étude de l'article : Democratizing AI Explainability through a Hybrid XAI-LLM Framework

> **Auteurs** : Louenas Bounia & Mor Ndour — LIPN, Université Sorbonne Paris Nord 
---

## L'article propose un framework hybride qui combine des méthodes XAI classiques (SHAP, LIME, Anchors) avec un LLM pour transformer des explications techniques en langage naturel accessible à tous, tout en vérifiant leur fiabilité.

## Notions clés abordées

### XAI — Explainable Artificial Intelligence
L'**explicabilité de l'IA** regroupe les méthodes qui cherchent à rendre compréhensibles les décisions d'un modèle d'IA pour que les humains puissent comprendre pourquoi un modèle a pris une décision plutôt qu'une autre.

---

### Les méthodes XAI classiques

| Méthode | Description | Limite |
|---|---|---|
| **SHAP** | Mesure l'importance de chaque variable dans une prédiction (ex : glucose → +0,34 au risque de diabète) | Précis mais problème : incompréhensible sans expertise |
| **LIME** | Crée un modèle simple autour d'une prédiction locale pour expliquer le comportement à cet endroit précis | Problème : peu généralisable |
| **Anchors** | Génère des règles du type "SI glucose > 140 ET âge > 50 → diabète" | Problème : difficile d'accès pour les non-experts |

> **Problème commun** : malgré leurs différences, toutes ces méthodes produisent des sorties trop techniques pour un utilisateur non-expert.

---

### LLM — Large Language Model
Un **grand modèle de langage** (comme GPT-4o, Claude ou encore Gemini) est capable de générer du texte naturel. Ici, il joue le rôle de **médiateur intelligent** en traduisant les sorties techniques de SHAP/LIME en explications conversationnelles compréhensibles par tous.

---

### Le Framework Hybride XAI-LLM
Il combine :

- Les méthodes XAI → **précision technique**
- Les LLMs → **accessibilité linguistique**

pour produire des explications **personnalisées selon le profil** de l'utilisateur :

| Profil utilisateur | Type d'explication générée |
|---|---|
| Expert | Détails techniques avec contexte |
| Professionnel | Explications actionnables métier-spécifiques |
| Citoyen | Langage simple et clair |

---

## Les 3 modules du pipeline

```
[Instance + Prédiction + Sorties XAI]
              ↓
        1. Module Génératif     ← LLM génère une explication en langage naturel

              ↓
        2. Module Parsing       ← Extrait des règles logiques via few-shot learning
                                + filtre les règles hors-domaine (anti-hallucinations)
              ↓
        3. Système d'Eval.      ← Évaluation DUALE : formelle + qualitative
              ↓
        [Score de fiabilité]
```

### Module 1 — Système Génératif
>But : Prendre les résultats mathématiques des méthodes d'explicabilité classiques, et les traduire en un texte naturel, fluide et parfaitement adapté à la personne (non-experte) qui le lit.

#### Étape 1 : Réception des données

| Ce que le LLM reçoit | Interprétation |
|---|---|
| La prédiction $h(x)$ pour l'instance $x$ |  La donnée dont il est question et la décision finale |
| L'architecture du modèle $h$ | Les règles internes globales du modèle de Machine Learning |
| Les sorties XAI (ex : valeurs SHAP) | Les calculs mathématiques bruts qui expliquent le poids de chaque variable |

N.B : $h$ est le modèle prédictif boîte noire. C'est l'algorithme qui a analysé les données et pris une décision. Ici, pour tester la framework, on choisit d'utiliser un **Arbre de Décision** comme modèle cible. Donc ici, $h$ = un arbre de décision entraîné sur un jeu de données.

#### Étape 2 : Cadrage du LLM

Les données reçues à l'Étape 1 sont envoyées à un LLM (comme GPT-4 ou Claude). Le système lui envoie un prompt bien structuré, défini par plusieurs paramètres :
- le rôle : on lui donne une entité précise
- le contexte : toutes les données des sorties XAI
- le profil utilisateur (user query)

#### Étape 3 : Création de l'Explication en langage naturel
Le LLM génère une explication en langage naturel, par exemple :
Au lieu d'afficher un graphique avec la valeur Glucose +0.34, il va générer :

"Le patient présente un risque de diabète principalement dû à un taux de glucose élevé, à l'âge et au poids. Son taux de cholestérol normal réduit légèrement cette probabilité."

Ce module accomplit avec succès l'objectif d'accessibilité. Mais comme le LLM a formulé cette phrase librement, il y a un risque qu'il ait ajouté une hallucination logique pour que la phrase sonne mieux.

### Module 2 — Module de Parsing
>But : transformer le texte naturel en règles logiques vérifiables, tout en réduisant les hallucinations.

#### Étape 1 : L'Extraction des Règles (via prompt)

Ce module utilse le LLM  comme un parseur pour **extraire des règles logiques** (ex : Si A et B alors C) à partir de l'explication générée, le système utilise la méthode du Few-Shot Learning (apprentissage à l'aide de quelques exemples).

Chaque modèle est entraîné sur des variables précises avec des plages de valeurs définies. Le **domaine théorique** du modèle, c'est en fait l'espace valide. Exemple pour le dataset Diabetes :

| Variable | Plage valide |
|---|---|
| Glucose | 0 – 200 mg/dL |
| Âge | 18 – 90 ans |
| Poids | 40 – 150 kg |

Problème : le LLM peut inventer des règles qui ne correspondent à aucune variable ou valeur présente dans les données d'entraînement, par exemple :

"Si le patient a les yeux bleus → risque élevé" : variable inexistante
"Si glucose = 450 mg/dL → risque élevé" : valeur impossible dans le dataset

#### Hallucination
C'est ce qu'on appelle une hallucination : le LLM produit une information fausse mais formulée avec confiance et apparente cohérence. Le danger est que ces règles erronées semblent plausibles à l'utilisateur non-expert, créant une illusion de fidélité. Il fait alors confiance à une explication qui ne reflète pas ce que le modèle a réellement calculé. C'est pour contrer ce risque que le module de parsing fait un **filtrage** des règles hors-domaine.

#### Étape 2 : Processus de filtrage
```
1 - Vérification de l'existence : La variable citée par le LLM existe-t-elle dans les données d'entraînement ?

NON → Règle REJETÉE.

OUI → On passe à l'étape 2.

2 - Vérification de la validité : La valeur associée à cette variable est-t-elle comprise dans la plage du domaine théorique ?

NON → Règle REJETÉE.

OUI → Règle CONSERVÉE.
```

Sans ce filtrage, une explication peut sembler cohérente à l'utilisateur tout en étant techniquement fausse — c'est ce que l'article appelle les **l'illusion de fidélité**. Autrement dit, l'hallucination est la cause, l'illusion de fidélité est la conséquence côté utilisateur.

#### Étape 3 : Conversion Binaire
Pour que les règles finalement conservées puissent être évaluées mathématiquement, le module les convertit dans sous Forme Normale Conjonctive (CNF) par exemple (Si A et B Alors C) devient (NON A ou NON B ou C), une pure équation de booléens qu'on envoie au module 3.

### Module 3 - Évaluation Duale
>But : Ce module s'assure que les règles logiques extraites à l'étape précédente reflètent fidèlement ce qui s'est réellement passé dans la boîte noire du modèle d'Intelligence Artificielle.

#### Étape 1 : Préparation
Dans le Module 2 : Ce sont uniquement les petites règles logiques (extraites de la phrase de l'IA) qui sont converties en CNF (ex: NON A OU NON B OU C).

Ici, c'est l'architecture interne complète de l'arbre de décision qui est transformée en un grand circuit booléen (CNF). Résultat : Le modèle n'est plus une boîte noire, c'est une équation logique.

#### Étape 2 : L'Évaluation Non-Formelle
Le système fait appel à un second LLM indépendant qui va jouer le rôle d'inspecteur en lisant les règles extraites au Module 2 et en vérifiant leur cohérence sémantique par rapport à la structure du modèle.

Les résultats typiques sont souvent **excellents**, l'explication a l'air parfaite.

#### Étape 3 : L'Évaluation Formelle
La règle extraite (au format binaire FNC du Module 2) est branchée directement dans le circuit booléen du modèle géant (créé à l'Étape 1).

$\epsilon_{h,x}$ est une fonction d'erreur d'explication qui mesure la proportion de cas où les règles extraites par le LLM contredisent le comportement réel du modèle h sur l'instance x. Donc $1-\epsilon_{h,x}$, c'est l'inverse (proportion de cas où il y a cohérence).

*N.B : Plus* $1-\epsilon_{h,x}$ *est proche de 1 (100%), plus l'explication est fidèle au modèle réel.*

Les résultats typiques sont **beaucoup plus bas**.

Résumé :
| | Évaluation Non-Formelle (Qualitative) | Évaluation Formelle (Mathématique) |
|---|---|---|
| **Comment** | Un deuxième LLM juge la cohérence logique des règles | Calcul de la métrique $1-\epsilon_{h,x}$ |
| **Ce que ça mesure** | Cohérence perçue | Réelle fidélité au modèle interne |
| **Scores observés** | 83 – 100% | 52 – 84% |

*N.B : L'objectif de CoVe est justement d'augmenter ce score.*


> **Résultat** : l'écart constant entre les deux évaluations prouve qu'une explication peut *sembler* cohérente sans être *vraiment* fidèle au modèle. Donc en imposant cette double évaluation, le framework protège l'utilisateur en lui donnant un score de fiabilité réel, empêchant ainsi une confiance aveugle envers l'IA.