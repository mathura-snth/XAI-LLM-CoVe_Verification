# Étude de l'article : Chain of Verification reduces Hallucination in LLM

> **Auteurs** : Shehzaad Dhuliawala, Mojtaba Komeili, Jing Xu, Roberta Raileanu, Xian Li, Asli Celikyilmaz, Jason Weston.

## Le concept central : Chain-of-Verification (CoVe)
L'article propose la méthode "Chain-of-Verification" (CoVe), une technique qui permet à un grand modèle de langage (LLM) de réfléchir sur ses propres réponses, de s'auto-évaluer via des questions de vérification et de corriger ses erreurs pour réduire les hallucinations.

## Contexte : Les 3 grandes approches pour réduire les hallucinations

1. La correction à l'entraînement (Training-time correction)
   > Principe : améliorer la génération brute (de gauche à droite) en ajustant ou en réentraînant les poids mathématiques du modèle pour qu'il génère moins d'hallucinations de base.
   
   Les techniques utilisées : l'apprentissage par renforcement (Reinforcement Learning) ou l'apprentissage contrastif (Contrastive Learning).
   
   La limite : C'est très coûteux en temps et en puissance de calcul, et il faut avoir accès à l'architecture interne du modèle (ce qui est impossible avec des API fermées comme GPT-4).

2. La correction à la génération (Generation-time correction)
   *C'est dans cette catégorie que se trouve la méthode Chain-of-Verification (CoVe).*

   > Principe : On ne touche pas aux poids du modèle. On prend le LLM tel qu'il est, et on ajoute une couche de prise de décision ou de raisonnement par-dessus au moment où il génère son texte pour le rendre plus fiable.
   
   Les techniques utilisées : analyser la probabilité (la confiance) des tokens générés par le modèle, ou tirer plusieurs échantillons de réponses pour détecter des incohérences, ou soit utiliser le modèle pour s'auto-évaluer soit utiliser un autre LLM comme examinateur (concept de cross-examination "LM vs LM").
   
   L'approche de CoVe est dans cette logique d'auto-cohérence (self-consistency), en forçant le modèle à planifier et exécuter des vérifications sur ses propres réponses avant de donner son résultat final.

3. L'augmentation par outils externes (Augmentation / Tool-use)
   ***N.B : lien vers projet perso***
   
   > Principe : Plutôt que de se contenter des connaissances internes (et faillibles) apprises par le modèle de langage, on lui donne accès à des outils externes pour réduire les hallucinations.
   
   Les techniques utilisées : les outils de fact-checking automatisés, ou l'ajout de citations vers des documents externes, ou la Génération Augmentée par la Recherche (RAG), qui utilise des documents factuels pour ancrer (grounding) la réponse du modèle dans la réalité.


