import json
import random
from theoremes import THEOREMES
from generer_copie import generer_copie, TYPES_ERREURS

N = 100
SEED = 42
OUTPUT = "benchmark_data.json"

random.seed(SEED)

ids = list(THEOREMES.keys())
dataset = []

for _ in range(N):
    t_id = random.choice(ids)
    type_erreur = random.choice(TYPES_ERREURS)
    copie = generer_copie(t_id, type_erreur)
    dataset.append(copie)

with open(OUTPUT, "w", encoding="utf-8") as f:
    json.dump(dataset, f, ensure_ascii=False, indent=2)

print(f"{N} copies générées dans {OUTPUT}")

# affichage de 2 colonnes
print("\n" + "="*100)
print(f"{'COPIE':<70} | {'VERDICT':<30}")
print("="*100)

for item in dataset:
    copie = ", ".join(item["copie"])
    verdict = f"VRAI" if item["est_correcte"] else f"FAUX ({item['raison']})"
    print(f"{copie[:68]:<70} | {verdict:<30}")

print("="*100)
print(f"Total: {len(dataset)} | Copies correctes {sum(1 for d in dataset if d['est_correcte'])} | Copies incorrectes : {sum(1 for d in dataset if not d['est_correcte'])}")