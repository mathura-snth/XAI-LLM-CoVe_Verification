# Benchmark Synthétique

Les théorèmes mathématiques ont des hypothèses **formelles et vérifiables** — comme les règles d'un arbre de décision.

On génère synthétiquement des réponses d'étudiants appliquant un théorème (correctement ou non), et on mesure si le LLM détecte les hypothèses manquantes, mal citées, ou inventées.

---

## Structure d'une entrée du benchmark

Pour chaque cas, on a toujours trois éléments :
- L'**énoncé** (ce qu'on donne à l'IA)
- La **vérité terrain** (les hypothèses obligatoires)
- Le **type d'erreur** qu'on veut tester

---

## Exemple 1 : Théorème de Rolle

**Vérité terrain — 3 hypothèses obligatoires :**
```
H1 : f continue sur [a, b]
H2 : f dérivable sur ]a, b[
H3 : f(a) = f(b)
```

| Copie synthétique | Ce que l'IA doit détecter |
|---|---|
| "f est dérivable sur ]a,b[ et f(a)=f(b), donc ∃c..." | **FAUX** : H1 manquante |
| "f est continue et dérivable sur [a,b], f(a)=f(b)..." | **FAUX** :  H2 mal citée (dérivable sur fermé ≠ ouvert) |
| "f est continue sur [a,b], dérivable sur ]a,b[, f(a)=f(b)..." | **VRAI** : Tout correct |
| "f est continue, dérivable, et atteint ses bornes..." | **FAUX** :  H3 manquante + hypothèse inventée |

---

## Exemple 2 : Théorème des Valeurs Intermédiaires

**Vérité terrain — 2 hypothèses obligatoires :**
```
H1 : f continue sur [a, b]
H2 : f(a) et f(b) de signes opposés (ou valeur y comprise entre f(a) et f(b))
```

| Copie synthétique | Ce que l'IA doit détecter |
|---|---|
| "f est continue et f(a) < 0 < f(b), donc..." | **VRAI** : Correct |
| "f est dérivable et change de signe, donc..." | **VRAI** : ATTENTION même si dérivable ≠ continue, puisque dérivable implique continue, H1 est vérifiée implicitement |
| "f est continue sur ]a,b[ et change de signe..." | **FAUX** : H1 sur mauvais intervalle (ouvert au lieu de fermé) |

---

## Mesure concrète

```
Score de fidélité = hypothèses correctement identifiées / hypothèses totales requises
```

**Trois types d'erreurs mesurables :**

- **Oubli** — une hypothèse requise n'est pas détectée par le LLM
- **Invention** — le LLM signale une hypothèse fausse comme manquante
- **Confusion** — le LLM confond deux théorèmes proches (ex: Rolle vs Lagrange)

---

## Lien avec CoVe

Après la correction initiale (brouillon), le LLM génère des questions de vérification :

```
"Est ce que j'ai bien vérifié que f est continue sur un intervalle FERMÉ ?"
"Est ce que j'ai distingué l'intervalle de continuité [a,b] de celui de continuité sur ]a,b[ ?"
"La condition f(a)=f(b) est-elle bien citée ?"
```

Ces questions courtes et isolées (variante Factored de CoVe) permettent de corriger les oublis et confusions du brouillon initial.

---

## Dynamisme du benchmark

Le benchmark s'étend à tout nouveau théorème sans changer sa structure :

| Théorème | Nouvelles hypothèses testées |
|---|---|
| Rolle | Continuité, dérivabilité, égalité aux bornes |
| Lagrange | Continuité, dérivabilité (cas général) |
| TVI | Continuité, signe aux bornes |
| Weierstrass | Continuité, compacité |
| Convergence dominée | Convergence p.p., domination intégrable |
| *etc* | ... |

Chaque nouveau théorème enrichit la base de connaissances sans modifier le pipeline d'évaluation.