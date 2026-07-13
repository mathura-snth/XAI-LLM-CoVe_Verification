import json
import random
from theorems import THEOREMS
from copy import generate_copy, ERROR_TYPES

N = 100
SEED = 42
OUTPUT = "benchmark_data.json"

random.seed(SEED)

ids = list(THEOREMS.keys())
dataset = []

for _ in range(N):
    t_id = random.choice(ids)
    error_type = random.choice(ERROR_TYPES)
    copy = generate_copy(t_id, error_type)
    dataset.append(copy)

with open(OUTPUT, "w", encoding="utf-8") as f:
    json.dump(dataset, f, ensure_ascii=False, indent=2)

print(f"{N} copies generated in {OUTPUT}")

# Display in 2 columns
print("\n" + "="*100)
print(f"{'COPY':<70} | {'VERDICT':<30}")
print("="*100)

for item in dataset:
    copy_text = ", ".join(item["copy"])
    verdict = f"TRUE" if item["is_correct"] else f"FALSE ({item['reason']})"
    print(f"{copy_text[:68]:<70} | {verdict:<30}")

print("="*100)
print(f"Total: {len(dataset)} | Correct copies: {sum(1 for d in dataset if d['is_correct'])} | Incorrect copies: {sum(1 for d in dataset if not d['is_correct'])}")