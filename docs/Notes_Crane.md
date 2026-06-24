# Étude de l'article : Crane

> **Auteurs** : Debangshu Banerjee, Tarun Suresh, Shubham Ugare, Sasa Misailovic, Gagandeep Singh
---

## Le problème central

Les LLMs doivent parfois produire des sorties à la fois **syntaxiquement** et **sémantiquement correctes**.

Une solution naturelle est le **décodage contraint** : on impose une grammaire formelle G à la sortie du LLM pour garantir la syntaxe. Mais les travaux précédents ont observé que cette contrainte **dégrade les capacités de raisonnement** du modèle.

**CRANE** apporte une explication théorique à ce phénomène et propose une solution pratique.

---

### Proposition 3.1

Forcer le LLM à produire directement la réponse finale sans étapes intermédiaires lui retire la capacité de raisonner.

### Proposition 3.3 (solution)

On augmente la grammaire G avec des règles supplémentaires qui autorisent des étapes de raisonnement intermédiaires, tout en garantissant que la réponse finale reste dans G. La grammaire augmentée Ga suit la structure :

```
Ga → R · G
```

où R capture les étapes de raisonnement libres, et G contraint uniquement la réponse finale. Avec Ga, le LLM retrouve son expressivité.

---

## L'algorithme CRANE

CRANE traduit cette idée théorique en algorithme pratique. Le principe est simple : **alterner entre génération libre (pour raisonner) et génération contrainte (pour la réponse finale)**.

### Mécanisme des délimiteurs

CRANE utilise deux symboles spéciaux S₁ et S₂ qui marquent le début et la fin de la zone contrainte :

```
[raisonnement libre...] S₁ [réponse contrainte] S₂ [raisonnement libre...]
```

En pratique, CRANE utilise `<<` et `>>` pour les expressions mathématiques, ou des backticks pour le code — des délimiteurs que les LLMs connaissent déjà naturellement.

### Fonctionnement pas à pas

```
1. Le LLM génère librement (raisonnement)
2. Dès que S₁ apparaît → passage en mode contraint
3. Le décodeur contraint CSD filtre les tokens invalides
4. Dès que S₂ apparaît → retour en génération libre
5. On répète jusqu'à la fin de la génération
```

### Exemple concret (GSM-Symbolic)

| Méthode | Sortie | Résultat |
|---|---|---|
| **Non contraint + CoT** | `<<first_hour_cost + (int((end_hour - start_hour).total_seconds() / 3600) - free_hours - 1) * ...>>` | ❌ Erreur de syntaxe |
| **Contraint seul** | `<<(int(end_hour - start_hour) - free_hours) * first_hour_cost + ...>>` | ❌ Syntaxe correcte mais réponse fausse |
| **CRANE** | `Let's think step by step... The final answer is <<first_hour_cost + (int(end_hour - start_hour) - free_hours - 1) * multiplier * first_hour_cost>>` | ✅ Syntaxe et sémantique correctes |

---

## Benchmarks utilisés

### GSM-Symbolic (raisonnement mathématique)
Problèmes mathématiques de niveau primaire avec des **variables symboliques** à la place des nombres. Le LLM doit produire une expression symbolique correcte.

- **Vérification** : le solveur Z3 vérifie l'équivalence fonctionnelle entre la réponse du LLM et la réponse gold.
- **Métrique principale** : Accuracy (% de réponses fonctionnellement correctes)
- **Métrique secondaire** : Parse (% de réponses syntaxiquement valides)

### FOLIO (raisonnement logique)
203 problèmes de raisonnement en langage naturel avec leurs annotations en **logique du premier ordre (FOL)**. Le LLM doit traduire le problème en formules FOL que Prover9 (solveur logique) peut vérifier.

- **Vérification** : Prover9 vérifie la correction des formules FOL générées.
- **Métrique principale** : Accuracy (% de traductions fonctionnellement correctes)
- **Métrique secondaire** : Compiles (% de formules syntaxiquement valides)

---

## Résultats clés

### Sur GSM-Symbolic

| Modèle | Non contraint CoT | Contraint | CRANE |
|---|---|---|---|
| Qwen2.5-1.5B | 26% | 22% | **31%** |
| Qwen2.5-Math-7B | 29% | 29% | **38%** |
| Llama-3.1-8B | 30% | 26% | **33%** |

### Sur FOLIO

| Modèle | Non contraint CoT | Contraint | CRANE |
|---|---|---|---|
| Qwen2.5-7B | 36.95% | 37.44% | **42.36%** |
| Llama-3.1-8B | 32.02% | 39.41% | **46.31%** |

**CRANE améliore systématiquement les deux métriques** — raisonnement correct ET syntaxe valide — là où les autres méthodes font un compromis entre les deux.

---

## Lien avec notre projet

| CRANE | Notre benchmark |
|---|---|
| Grammaire G = expressions mathématiques valides | Grammaire G = liste d'hypothèses bien formées |
| Raisonnement libre avant `<<` | Raisonnement du LLM avant de citer les hypothèses |
| Vérification par Z3 / Prover9 | Vérification par table d'implications + PySAT |
| Benchmark GSM-Symbolic / FOLIO | Benchmark théorèmes mathématiques (Rolle, Lagrange...) |

CRANE et CoVe attaquent le même problème par deux angles différents : CoVe corrige les hallucinations **après** génération (auto-vérification), CRANE les prévient **pendant** la génération (contraintes grammaticales). Notre benchmark peut servir à évaluer les deux approches sur le même jeu de données.

---

## Limites de CRANE

- Proposition 3.1 ne couvre que les grammaires G dont le langage L(G) est **fini** — la généralisation à des grammaires infinies reste ouverte.
- CRANE nécessite un accès aux **logits** du modèle pour le décodage contraint — inapplicable aux modèles API qui ne les exposent pas (GPT-4o, Claude via API publique...).