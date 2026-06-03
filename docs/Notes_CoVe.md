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
En prenant en compte à la fois la requête initiale et son propre brouillon, le modèle génère une série de questions de vérification qui ciblent les affirmations factuelles du texte initial pour les tester. Pour formuler les questions de vérification on utilise la méthode du Few-Shot Prompting (avant de donner la tâche réelle à l'IA, on intègre dans le texte du prompt quelques exemples de de ce que l'on attend d'elle).

#### Étape 3 : Exécution des vérifications (Execute Verifications)
Le modèle doit répondre aux questions qu'il vient de créer afin d'évaluer si les faits avancés initialement sont justes ou non. C'est l'étape la plus **critique**, car le modèle risque d'être biaisé par son brouillon et de répéter la même hallucination.

Pour contrer cela, on teste différentes variantes d'exécution :
- Joint : les étapes 2 et 3 se font dans un seul prompt, mais le problème est que le modèle lit sa propre erreur et a tendance à la répéter.
- 2-Step : les étapes 2 et 3 sont séparées en deux requêtes distinctes, cette fois, à l'étape 3, le contexte fourni au LLM ne contient plus le brouillon initia mais seulement les questions, on évite ainsi le mimétisme.
- Factored : chaque question de vérification est posée de manière totalement indépendante dans des prompts séparés. Cela supprime non seulement l'influence du brouillon, mais empêche surtout toute interférence possible entre les différentes questions (la réponse à la question A ne peut pas biaiser la réponse à la question B).
- Factor + Revise : après la réponse aux questions, le système ajoute un prompt supplémentaire dédié au "cross-checking". Le modèle compare le fait initial avec la réponse vérifiée et doit explicitement dire s'il y a une incohérence.

#### Étape 4 : Génération de la réponse vérifiée finale (Final Verified Response)
Le modèle génère sa réponse définitive et améliorée. Pour cela, le système fournit au modèle un contexte final regroupant le brouillon de départ et toutes les questions/réponses de vérification (et les détections d'incohérences si la méthode Factor+Revise a été utilisée). Ainsi le modèle corrige les hallucinations identifiées à l'étape 3 et renvoie un texte beaucoup plus rigoureux.

## Benchmarks

Un benchmark est un standard d'évaluation composé de questions et de réponses de référence (gold answers) tirées d'une source de vérité fiable. On pose les mêmes questions à tous les modèles, on compare leurs réponses au gold, et on obtient un score comparable.

| Benchmark | Ce que l'IA doit faire | Exemple | Métrique |
|---|---|---|---|
| Wikidata | Générer une liste simple, le test interroge l'IA sur des relations basiques extraites de la base de données Wikidata |"Quels sont les politiciens nés à Boston ?"|Précision, nb d'entités positives/négatives|
| Wiki-Category List | Générer une liste experte, l'IA doit énumérer des éléments appartenant à des catégories Wikipédia très spécifiques (rares) |"Citez des films d'horreur animés mexicains."|Précision, nb d'entités positives/négatives|
| MultiSpanQA | Répondre à des questions à tiroirs. L'IA est testée sans recherche externe autorisée sur des questions exigeant plusieurs petits éléments de réponse précis. |"Qui a inventé la première presse à imprimer et en quelle année ?"|Score F1 (Précision et Rappel)|
| Longform Generation (Biographies) | Rédaction d'un texte long (plusieurs phrases/paragraphes) sur une entité spécifique |"Donne-moi la biographie de Victor Hugo."|FACTSCORE (vérification des faits par une IA externe)|

#### Exemple concret, benchmark Wikidata
1. Dans le dataset Wikidata, il n'y a pas de texte, mais des liens mathématiques (les triplets) mis à jour. Par exemple :

```text
[Donald Trump] -> [Profession : Politicien] -> [Lieu de naissance : Queens, New York]

[Alexandria Ocasio-Cortez] -> [Profession : Politicien] -> [Lieu de naissance : Bronx, New York]

[Hillary Clinton] -> [Profession : Politicien] -> [Lieu de naissance : Chicago, Illinois]

[Michael Bloomberg] -> [Profession : Politicien] -> [Lieu de naissance : Boston, Massachusetts]
```
2. On transforme notre filtre de base de données en une question en langage naturel pour tester le modèle de langage (LLM).
```text
Question du benchmark : "Citez des politiciens qui sont nés à NY, New York."
```

3. Le LM classque génère sa liste de gauche à droite, avec des hallucinations car il associe logiquement certains politiciens à New York (parce qu'ils y ont travaillé), même s'ils n'y sont pas nés.  

```text
Réponse du LLM :

Hillary Clinton - ancienne sénatrice de l'État de New York.

Donald Trump - ancien président des États-Unis.

Michael Bloomberg - ancien maire de New York.
```
Métrique de Précision : Mauvaise car sur 3 réponses, 2 sont des hallucinations (Clinton et Bloomberg).

4. On corrige pviaar CoVe qui force le modèle à vérifier sa propre copie en créant des questions courtes pour chaque élément de la liste :  

```text
Question générée : "Où est née Hillary Clinton ?"

Réponse vérifiée : Chicago, Illinois. (-> l'IA repère l'incohérence)


Question générée : "Où est né Donald Trump ?"

Réponse vérifiée : Queens, New York. (-> correct)


Question générée : "Où est né Michael Bloomberg ?"

Réponse vérifiée : Boston, Massachusetts. (-> l'IA repère l'incohérence)
```
5. Grâce à ces vérifications isolées, le modèle supprime ses erreurs et génère une nouvelle réponse propre.  

```text
Réponse Finale :

Donald Trump - ancien président des États-Unis.  

Alexandria Ocasio-Cortez - membre de la Chambre des représentants.  
```

La note finale : **Excellente**, le nombre de réponses négatives (les hallucinations) chute, ce qui fait monter le score de précision du modèle sur ce benchmark.  


*N.B : La vraie différence avec un benchmark en Recherche d'Information est ce qu'on **évalue** :*
- ***IR** : le système cherche dans un **index externe**, la réponse est une **liste de documents classés** et la source de vérité sert à **définir quels docs sont pertinents**. On utilise pour ça les métriques : **nDCG, MAP, Recall@k**.*
- ***Benchmark LLM (CoVe)** : le système puise dans sa **mémoire interne**, la réponse est du **texte généré**, la source de vérité sert à **vérifier si les faits générés sont corrects**. On utilise pour ça les métriques : **Précision, F1, FACTSCORE**.*