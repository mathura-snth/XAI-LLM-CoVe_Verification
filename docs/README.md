# XAI & LLM Verification : Fiabilité et Explicabilité de l'IA

Bienvenue dans l'espace de documentation. Vous y trouverez des fiches d'étude détaillées et structurées portant sur deux articles de recherche fondamentaux concernant les LLMs.

L'objectif de ces notes est de rendre accessibles des concepts techniques complexes autour de deux défis majeurs de l'IA : **empêcher une IA d'halluciner** et **rendre les décisions d'une "boîte noire" compréhensibles pour tous**.

---
## [Notes_CoVe.md](./Notes_CoVe.md) : Réduire les hallucinations par l'auto-vérification

Ce document analyse la méthode *Chain-of-Verification (CoVe)*, une approche qui permet aux modèles de langage d'évaluer la fiabilité de leurs propres réponses sans nécessiter de réentraînement coûteux.

Y sont abordés :
*   **Le Pipeline en 4 étapes :** Comment forcer un LLM à créer un brouillon, planifier des questions de vérification, y répondre isolément, puis générer un texte final expurgé de ses erreurs.
*   **Les mécanismes en action :** Un cas d'usage concret analysant l'évaluation du modèle sur le benchmark Wikidata (extraction et vérification de listes factuelles).

---

## [Notes_Democratizing_AI.md](./Notes_Democratizing_AI.md) : Rendre l'IA transparente et accessible

Ce document analyse un framework hybride innovant qui combine la rigueur mathématique des méthodes d'explicabilité classiques (XAI comme SHAP ou LIME) avec la fluidité linguistique des LLMs.

Y sont abordés :
*   **La traduction :** Comment le LLM agit comme un "médiateur" pour transformer des données brutes en explications personnalisées (profil expert, professionnel ou citoyen).
*   **Le danger de "l'illusion de fidélité" :** Comment repérer et filtrer les hallucinations logiques.
*   **L'Évaluation Duale :** Le fonctionnement du système de contrôle pour garantir un score de fiabilité réel.

---