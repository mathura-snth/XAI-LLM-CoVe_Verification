# Expérimentations CRANE

Ce dossier regroupe les travaux et scripts d'expérimentation réalisés par Farah. Ces recherches portent sur la réduction des hallucinations des Modèles de Langage (LLMs) en utilisant des approches basées sur le décodage sous contrainte, notamment la méthode **CRANE** (*Reasoning with constrained LLM generation*).

## Objectif de cette section

Contrairement à l'approche qui explore la correction des hallucinations via **CoVe**, cette section explore une approche alternative et complémentaire. La méthode CRANE laisse le modèle raisonner librement (génération non contrainte) avant de forcer le formatage de sa réponse finale (génération contrainte) pour garantir sa validité syntaxique et sémantique.

## Contenu du dossier

### `first-contact.ipynb`
Il constitue l'exploration initiale et la mise en place des baselines. Il contient :
* **L'évaluation sur GSM8K** : Tests sur un dataset de problèmes mathématiques de niveau primaire, avec une baseline classique et une tentative d'extraction formelle de contraintes.
* **L'évaluation sur FOLIO** : Tests sur un dataset de déduction logique (First-Order Logic). 
* **Vérification multi-tours** : Implémentation d'un système de vérification en deux passages (le modèle génère une réponse, puis on lui demande de la revérifier), simulant une mécanique d'auto-correction.

*N.B. : Le mdèle utilisé est `Qwen/Qwen2.5-7B-Instruct`*
*N.B. : Utilisation de `bitsandbytes` pour la quantification en 4-bit (NF4) afin de faire tourner le modèle localement/sur GPU limité.*