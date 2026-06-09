# Expérimentations CRANE

Ce dossier documente l'implémentation et la fiabilisation du framework expérimental basé sur la méthode CRANE (Reasoning with constrained LLM generation). Ces travaux visent à évaluer la réduction des hallucinations dans les LLMs par le biais de méthodes de décodage sous contrainte.

## Objectif de cette section

Contrairement à l'approche qui explore la correction des hallucinations via **CoVe**, cette section explore une approche alternative et complémentaire. La méthode CRANE laisse le modèle raisonner librement (génération non contrainte) avant de forcer le formatage de sa réponse finale (génération contrainte) pour garantir sa validité syntaxique et sémantique.

## Contributions

Le pipeline initial a été restructuré pour garantir une reproductibilité scientifique rigoureuse :

- Remplacement des dépendances privées par un pipeline de téléchargement dynamique via l'API Hugging Face.
- Gestion de chemins (local vs cloud) permettant l'exécution du notebook sans modification manuelle du code.
- Développement d'un moteur d'extraction de réponses basé sur des expressions régulières (Regex) pour pallier les variations de formatage du modèle.

## Contenu du dossier

### `crane_baselines.ipynb`, notebook principal
Il contient :
- **Baseline GSM8K** : Évaluation sur problèmes arithmétiques avec analyse des échecs.
- **Baseline FOLIO** : Évaluation sur logique du premier ordre.

*N.B. : Le mdèle utilisé est `Qwen/Qwen2.5-7B-Instruct`*
*N.B. : Utilisation de `bitsandbytes` pour la quantification en 4-bit (NF4) afin de faire tourner le modèle localement/sur GPU limité.*