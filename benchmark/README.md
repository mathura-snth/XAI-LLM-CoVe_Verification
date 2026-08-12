# Math LLM Verifier: From Formal Logic to Synthetic Evaluation

Welcome to the main repository of the **Mathematical Theorems Verification Benchmark** project.

This repository showcases the design and development of an evaluation tool (benchmark) intended for Large Language Models (LLMs). 
The core idea? To automatically and synthetically generate "student copies" applying mathematical theorems, in order to measure the AI's ability to detect precise logical errors (omissions, inventions, false implications) rather than performing simple text matching.

---

## Repository Navigation

This repository is split into two main sections corresponding to the project's evolution. **To run the tests or explore the final version, please navigate to `eng_ver/`. [INSÉRER LIEN VIDÉO ?]**

### 1. [eng_ver/](./eng_ver) : Active Version (Final Pipeline)
This is the culmination of the project. This directory contains the **final and polished version** of the benchmark. Here you will find:
* **The optimized generation scripts** (`run_benchmark.py`, `generate_copy.py`).
* **The formal logic engine** verifying mathematical implications (`implications.py`).
* **The data dictionaries** cataloging theorems and their hypotheses (`theorems.py`, `hypotheses.py`).
* **The final evaluation datasets** (`benchmark_data.json`, exported to CSV and Markdown).

**This is the version that MUST be used to run tests and evaluate your models.**

### 2. [archives/](./archives) : Foundations and History
This folder gathers all previous development iterations (initial scripts, drafts, early logic tree models). 
These files represent the algorithmic foundations that led to the final version present in `eng_ver`. They are preserved here for traceability, reference, and historical documentation purposes.

---

## The Core of the Project : The Formal Logic Engine

Unlike simple multiple-choice quizzes, this benchmark relies on a genuine mathematical implications engine. Each theorem is modeled with its **strict hypotheses (the ground truth)**. 

When the script generates a synthetic copy, it purposely modifies these hypotheses according to several categories, forcing the LLM to grasp the deep mathematical meaning:
- **`missing_hypothesis` / `multiple_missing`**: Omission of one or more necessary conditions.
- **`invented_hypothesis`**: Addition of an off-topic condition or substitution by an invalid one (e.g., replacing a closed interval with an open interval).
- **`valid_implication`** *(The standout feature of this benchmark)*: Replacement of a hypothesis by a *stronger* condition (e.g., stating "f is of class C¹" when the theorem only requires "f is continuous"). The system logically validates this replacement, forcing the LLM to prove it understands mathematics beyond mere pattern matching.
- **`correct` / `exact_match`**: The copy is perfectly valid, matching the ground truth expectations.

---

## Generation and Datasets

The scripts allow for on-the-fly generation of hundreds of test cases, each with a formally calculated and 100% guaranteed verdict (label). 

A typical extract of generated data:
```json
{
  "theorem_id": "T01",
  "name": "Rolle's Theorem",
  "copy": [
    "f is continuous on [a, b]",
    "f is differentiable on ]a, b["
  ],
  "expected": [
    "f is continuous on [a, b]",
    "f is differentiable on ]a, b[",
    "f(a) = f(b)"
  ],
  "is_correct": false,
  "reason": "missing: f(a) = f(b)",
  "validation_type": "missing_hypothesis"
}
```
---

## Quick Start (via `eng_ver/`)
Generate a test dataset (defaults to 100 random, reproducible iterations via seed):

```Bash
cd eng_ver
python3 run_benchmark.py
```

Export the results into analytical tables (CSV and Markdown):

```Bash
python3 exporter_tableau.py
```