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

seen_errors = set()

max_attempts = N * 30
attempts = 0

while len(dataset) < N and attempts < max_attempts:
    attempts += 1
    t_id = random.choice(ids)
    error_type = random.choice(ERROR_TYPES)
    la_copy = generate_copy(t_id, error_type)

    key = (la_copy["theorem_id"], tuple(sorted(la_copy["copy"])), la_copy["error_type"])
    if key in seen_errors:
        continue
    seen_errors.add(key)

    dataset.append(la_copy)

if attempts >= max_attempts:
    print(f"Warning: stopped after {attempts} attempts with only {len(dataset)}/{N} copies "
          f"(not enough remaining unique (theorem, error_type) pairs).")

with open(OUTPUT, "w", encoding="utf-8") as f:
    json.dump(dataset, f, ensure_ascii=False, indent=2)

print(f"{len(dataset)} copies generated in {OUTPUT} ({attempts} attempts)")

# Display in 2 columns
print("\n" + "="*100)
print(f"{'COPY':<70} | {'VERDICT':<30}")
print("="*100)

for item in dataset:
    la_copytext = ", ".join(item["copy"])
    verdict = f"TRUE" if item["is_correct"] else f"FALSE ({item['reason']})"
    print(f"{la_copytext[:68]:<70} | {verdict:<30}")

print("="*100)
print(f"Total: {len(dataset)} | Correct copies: {sum(1 for d in dataset if d['is_correct'])} | Incorrect copies: {sum(1 for d in dataset if not d['is_correct'])}")