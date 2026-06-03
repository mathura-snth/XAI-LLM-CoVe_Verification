# Stage : Amélioration de la fidélité des explications XAI-LLM (CoVe)

Ce dépôt contient le code, la bibliographie et les expérimentations réalisés lors de mon stage au **LIPN (Laboratoire d'Informatique de l'Université Paris Nord)**.

## Objectif du projet
Améliorer la fidélité des explications générées par les modèles de langage (LLMs) dans un cadre d'explicabilité hybride (XAI-LLM), en réduisant les hallucinations via l'implémentation de la méthode **Chain-of-Verification (CoVe)**.

## La théorie
Envie de comprendre les concepts scientifiques qui sont à la base de ce projet ? J'ai rédigé des fiches de synthèse sur les deux articles à la base de cette recherche. Vous pouvez les consulter ici :

* **[Notes : Democratizing AI Explainability](./docs/Notes_Democratizing_AI.md)** — Comment traduire les mathématiques d'une "boîte noire" en explications accessibles à tous, et le danger de l'illusion de fidélité.
* **[Notes : Chain of Verification (CoVe)](./docs/Notes_CoVe.md)** — Comment forcer une intelligence artificielle à trouver, vérifier et corriger ses propres hallucinations avant de vous répondre.

## Architecture du dépôt
```text
XAI-LLM-Cove_Verification/
├── .gitignore
├── README.md                              <-- Présentation globale du projet
├── requirements.txt                       <-- (À venir) Liste des dépendances Python
│
├── data/                                  <-- (À venir) Échantillons de données pour les tests
│
├── docs/                                  <-- Bibliographie et fiches de lecture
│   ├── Chain of Verification.pdf
│   ├── Democratizing AI Explainability.pdf
│   ├── Notes_Democratizing_AI.md        <-- Étude du 1er article
│   └── Notes_CoVe.md                    <-- Étude du 2ème article
│
└── src/                                   <-- (À venir) Code source du projet
    ├── baseline/                          <-- Code initial de référence (MorNdour/explainable_ai)
    ├── cove_pipeline/                     <-- Implémentation de la chaîne de vérification (CoVe)
    └── evaluation/                        <-- Scripts de calcul des métriques et résultats
```