# Étude de l'article : Chain of Verification reduces Hallucination in LLM

> **Auteurs** : Shehzaad Dhuliawala, Mojtaba Komeili, Jing Xu, Roberta Raileanu, Xian Li, Asli Celikyilmaz, Jason Weston.

## Le concept central : Chain-of-Verification (CoVe)
L'article propose la méthode "Chain-of-Verification" (CoVe), une technique qui permet à un grand modèle de langage (LLM) de réfléchir sur ses propres réponses, de s'auto-évaluer via des questions de vérification et de corriger ses erreurs pour réduire les hallucinations.

## Contexte : Les 3 grandes approches pour réduire les hallucinations

### 1. La correction à l'entraînement (Training-time correction)
   > Principe : améliorer la génération brute (de gauche à droite) en ajustant ou en réentraînant les poids mathématiques du modèle pour qu'il génère moins d'hallucinations de base.
   
   Techniques utilisées : l'apprentissage par renforcement (Reinforcement Learning) ou l'apprentissage contrastif (Contrastive Learning).
   
   Limite : C'est très coûteux en temps et en puissance de calcul, et il faut avoir accès à l'architecture interne du modèle (ce qui est impossible avec des API fermées comme GPT-4).

### 2. La correction à la génération (Generation-time correction)
   
   *C'est dans cette catégorie que se trouve la méthode Chain-of-Verification (CoVe).*

   > Principe : On ne touche pas aux poids du modèle. On prend le LLM tel qu'il est, et on ajoute une couche de prise de décision ou de raisonnement par-dessus au moment où il génère son texte pour le rendre plus fiable.
   
   Techniques utilisées : analyser la probabilité (la confiance) des tokens générés par le modèle, ou tirer plusieurs échantillons de réponses pour détecter des incohérences, ou soit utiliser le modèle pour s'auto-évaluer soit utiliser un autre LLM comme examinateur (concept de cross-examination "LM vs LM").
   
   L'approche de CoVe est dans cette logique d'auto-cohérence (self-consistency), en forçant le modèle à planifier et exécuter des vérifications sur ses propres réponses avant de donner son résultat final.

### 3. L'augmentation par outils externes (Augmentation / Tool-use)
   
   ***N.B : lien vers projet perso***
   
   > Principe : Plutôt que de se contenter des connaissances internes (et faillibles) apprises par le modèle de langage, on lui donne accès à des outils externes pour réduire les hallucinations.
   
   Techniques utilisées : les outils de fact-checking automatisés, ou l'ajout de citations vers des documents externes, ou la Génération Augmentée par la Recherche (RAG), qui utilise des documents factuels pour ancrer (grounding) la réponse du modèle dans la réalité.

## Le Fonctionnement de CoVe : Pipeline en 4 étapes
La méthode CoVe repose sur l'idée qu'un modèle de langage peut vérifier son propre travail s'il est guidé étape par étape.

#### Étape 1 : Génération de la réponse initiale (Baseline Response)
Le modèle génère une réponse standard (de gauche à droite) à la requête de l'utilisateur. Cette réponse sert de brouillon de base qui est susceptible de contenir des hallucinations qu'il va falloir trouver.

#### Étape 2 : Planification des vérifications (Plan Verifications)
En prenant en compte à la fois la requête initiale et son propre brouillon, le modèle génère une série de questions de vérification qui ciblent les affirmations factuelles du texte initial pour les tester.

#### Étape 3 : Exécution des vérifications (Execute Verifications)
Le modèle doit répondre aux questions qu'il vient de créer afin d'évaluer si les faits avancés initialement sont justes ou non. C'est l'étape la plus **critique**, car le modèle risque d'être biaisé par son brouillon et de répéter la même hallucination.

Pour contrer cela, on teste différentes variantes d'exécution :
- Joint : la planification et l'exécution se font dans un seul prompt, mais problème : le modèle lit sa propre erreur et a tendance à la répéter.
- 2-Step : la planification et l'exécution sont séparées en deux requêtes distinctes. Dans la seconde étape, le contexte fourni au LLM ne contient plus le brouillon initial, on évite ainsi le mimétisme.
- Factored : chaque question de vérification est posée de manière totalement indépendante dans des prompts séparés, ce qui supprime toute interférence possible entre le brouillon et les différentes questions.
- Factor + Revise : après la réponse aux questions, le système ajoute un prompt supplémentaire dédié au "cross-checking". Le modèle compare le fait initial avec la réponse vérifiée et doit explicitement dire s'il y a une incohérence.

