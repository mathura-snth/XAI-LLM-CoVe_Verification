# Étude de l'article : Democratizing AI Explainability through a Hybrid XAI-LLM Framework

> **Auteurs** : Louenas Bounia & Mor Ndour — LIPN, Université Sorbonne Paris Nord 
---

## L'article propose un framework hybride qui combine des méthodes XAI classiques (SHAP, LIME, Anchors) avec un LLM pour transformer des explications techniques en langage naturel accessible à tous, tout en vérifiant leur fiabilité.

---

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
Le LLM reçoit en entrée :
- L'architecture du modèle `h`
- Les sorties XAI (ex : valeurs SHAP)
- La prédiction `h(x)` pour l'instance `x`

Il génère une explication en langage naturel, par exemple :
> *"Le patient présente un risque de diabète principalement dû à un taux de glucose élevé, à l'âge et au poids. Son taux de cholestérol et son statut non-fumeur réduisent légèrement cette probabilité."*
