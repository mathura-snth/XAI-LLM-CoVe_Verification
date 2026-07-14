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

erreurs_vues = set()

max_tentatives = N * 30 # d'après claude pour éviter boucle infinie
tentatives = 0

while len(dataset) < N and tentatives < max_tentatives:
    tentatives += 1
    t_id = random.choice(ids)
    type_erreur = random.choice(TYPES_ERREURS)
    copie = generer_copie(t_id, type_erreur)

    if copie["type_erreur"] != "correcte":
        cle = (copie["theoreme_id"], copie["type_erreur"])
        if cle in erreurs_vues:
            continue  # cette paire (théorème, type_erreur) existe déjà, on l'ignore
        erreurs_vues.add(cle)

    dataset.append(copie)

if tentatives >= max_tentatives:
    print(f"Attention, arrêt après {tentatives} tentatives avec seulement {len(dataset)}/{N} copies")

with open(OUTPUT, "w", encoding="utf-8") as f:
    json.dump(dataset, f, ensure_ascii=False, indent=2)

print(f"{len(dataset)} copies générées dans {OUTPUT} ({tentatives} tentatives)")

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