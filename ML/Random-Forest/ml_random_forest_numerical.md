# 🔢 ML Random Forest: NUMERICAL

### *Rules first → then solve. Every step shown.*

> **Nav:** [← INDEX](../ml_master_gap_index.md) | [📖 THEORY](ml_random_forest_theory.md) | 🔢 **NUMERICAL** | [💻 PRACTICE →](ml_random_forest_practice.md)

---

## 📦 ALL FORMULAS

```
┌──────────────────────────────────────────────────────────────┐
│ BOOTSTRAP UNIQUE:   1 − (1 − 1/n)^n  →  1 − 1/e ≈ 0.632      │
│ OOB FRACTION:       (1 − 1/n)^n  →  1/e ≈ 0.368              │
│                                                               │
│ FEATURES PER SPLIT: m = √p   (classification)                │
│                     m = p/3  (regression)                    │
│                                                               │
│ GINI:       1 − Σ pₖ²                                         │
│ ENTROPY:    − Σ pₖ log₂ pₖ                                    │
│ INFO GAIN:  H(parent) − Σ (|child|/|parent|) H(child)         │
│                                                               │
│ RF REGRESSION PRED:  ŷ = (1/B) Σ_b T_b(x)                    │
│ RF CLASSIF PRED:     ŷ = argmax_c Σ_b 1[T_b(x)=c]            │
│                                                               │
│ VARIANCE REDUCTION of avg of B correlated estimators:        │
│   Var = ρ σ²  +  (1−ρ)/B · σ²                                │
│   ρ = correlation between trees                              │
└──────────────────────────────────────────────────────────────┘
```

---

## P1: Bootstrap — how many unique samples?

```
n = 10 training points, draw a bootstrap sample of size 10 (with replacement).

PROB any one point is NOT picked in a single draw:  (1 − 1/10) = 0.9
PROB it is NOT picked in 10 draws:                   0.9^10 = 0.3487
PROB it IS picked at least once:                     1 − 0.3487 = 0.6513

EXPECTED unique points in bootstrap:                  10 · 0.6513 ≈ 6.5

LARGE n LIMIT:
  (1 − 1/n)^n  →  1/e  ≈ 0.3679   (not picked)
  unique       →  1 − 1/e  ≈ 0.632

CONSEQUENCE: ~63% unique → OOB set ≈ 37% of data.
```

[↑ Back to Top](#-ml-random-forest-numerical)

---

## P2: Gini impurity at a single split

```
NODE: 10 samples,  8 class A,  2 class B
GINI(parent) = 1 − (8/10)² − (2/10)² = 1 − 0.64 − 0.04 = 0.32

Candidate split on feature "age < 30":
  LEFT:   6 samples  →  5 A, 1 B     Gini_L = 1 − (5/6)² − (1/6)² = 1 − 0.694 − 0.028 = 0.278
  RIGHT:  4 samples  →  3 A, 1 B     Gini_R = 1 − (3/4)² − (1/4)² = 1 − 0.5625 − 0.0625 = 0.375

WEIGHTED GINI (children):
  (6/10)·0.278 + (4/10)·0.375
  = 0.167 + 0.150
  = 0.317

GINI GAIN = 0.320 − 0.317 = 0.003   ← tiny improvement

At each RF node, we do this for a RANDOM SUBSET of m features and pick
the best of those (not the global best).
```

[↑ Back to Top](#-ml-random-forest-numerical)

---

## P3: Feature subsampling — how many features per split?

```
p = 36 features.

CLASSIFICATION default:   m = √p = √36 = 6
REGRESSION default:       m = p/3 = 12

p = 100:
  CLASSIF m = 10
  REGRESS m ≈ 33

p = 1000:
  CLASSIF m ≈ 32
  REGRESS m ≈ 333

WHY? Smaller m → trees more de-correlated → lower ensemble variance
BUT each tree becomes weaker individually. There's a sweet spot.
```

[↑ Back to Top](#-ml-random-forest-numerical)

---

## P4: Majority vote with 5 trees — classification

```
Test point x.  5 trees predict:
  T₁: A
  T₂: B
  T₃: A
  T₄: A
  T₅: C

HARD VOTE (majority):
  Counts  A:3, B:1, C:1  →  ŷ = A  ✓

SOFT VOTE — suppose each tree also gives probabilities:
  T₁: P(A)=0.7, P(B)=0.2, P(C)=0.1
  T₂: P(A)=0.3, P(B)=0.5, P(C)=0.2
  T₃: P(A)=0.6, P(B)=0.3, P(C)=0.1
  T₄: P(A)=0.8, P(B)=0.1, P(C)=0.1
  T₅: P(A)=0.2, P(B)=0.2, P(C)=0.6

MEAN probabilities:
  P(A) = (0.7+0.3+0.6+0.8+0.2)/5 = 2.6/5 = 0.52
  P(B) = (0.2+0.5+0.3+0.1+0.2)/5 = 1.3/5 = 0.26
  P(C) = (0.1+0.2+0.1+0.1+0.6)/5 = 1.1/5 = 0.22

ŷ = argmax = A   (same choice; soft vote also gives calibrated probabilities)
```

[↑ Back to Top](#-ml-random-forest-numerical)

---

## P5: Regression averaging — 6 trees

```
x = test point.  6 trees predict:
  T₁: 12.0
  T₂: 13.5
  T₃: 11.8
  T₄: 14.2
  T₅: 12.9
  T₆: 13.1

ŷ = (12.0 + 13.5 + 11.8 + 14.2 + 12.9 + 13.1) / 6
  = 77.5 / 6
  = 12.92

UNCERTAINTY (std of predictions):
  σ ≈ √[ Σ(T_b − ŷ)² / 6 ] ≈ 0.82

TAKEAWAY: spread of trees gives a cheap uncertainty estimate.
```

[↑ Back to Top](#-ml-random-forest-numerical)

---

## P6: OOB error calculation by hand

```
TRAINING SET: 5 points x₁..x₅.  Build B = 4 trees.

BOOTSTRAP MEMBERSHIP (✓ = in bag, — = OOB):
         T₁   T₂   T₃   T₄
  x₁     ✓    ✓    —    ✓
  x₂     ✓    —    ✓    ✓
  x₃     —    ✓    ✓    —
  x₄     ✓    ✓    —    ✓
  x₅     —    —    ✓    ✓

FOR EACH xᵢ, PREDICT using only its OOB trees:
  x₁ → T₃ only
  x₂ → T₂ only
  x₃ → T₁, T₄
  x₄ → T₃ only
  x₅ → T₁, T₂

(Assume those predictions give binary outcomes; compare with yᵢ.)

If, say, x₁, x₃, x₅ predicted correctly and x₂, x₄ wrong:
  OOB error = 2 / 5 = 0.40

Note: x₅ had TWO OOB trees → averaged/voted; x₁, x₂, x₄ had only ONE.
```

[↑ Back to Top](#-ml-random-forest-numerical)

---

## P7: Variance of the averaged forest — correlation matters

```
RULE (Breiman): for B trees each with variance σ² and pairwise correlation ρ:

  Var[ensemble] = ρ σ²  +  (1 − ρ)/B · σ²

Case A — independent trees (ρ = 0):
  Var = 0 + σ²/B    → collapses to 0 as B → ∞    ✅ dream case

Case B — very correlated trees (ρ = 0.9):
  Var = 0.9 σ² + 0.1 σ²/B
  For B = 100:  Var ≈ 0.9 σ² + 0.001 σ² ≈ 0.901 σ²
  ⟹ barely better than a single tree ❌

LESSON: the whole point of feature subsampling is to DRIVE ρ DOWN.
        Lower ρ > more trees.
```

[↑ Back to Top](#-ml-random-forest-numerical)

---

## P8: Feature importance — permutation example

```
OOB baseline MSE (original data)   : e₀ = 5.20

Shuffle feature "income"          : e_income = 6.80
Shuffle feature "age"             : e_age    = 5.45
Shuffle feature "zip"             : e_zip    = 5.22

IMPORTANCE = e_shuffled − e₀
  income:  6.80 − 5.20 = 1.60   ← most important
  age:     5.45 − 5.20 = 0.25
  zip:     5.22 − 5.20 = 0.02   ← nearly irrelevant

Normalize by dividing by e₀ for a "% error increase":
  income: 30.8%,  age: 4.8%,  zip: 0.4%
```

[↑ Back to Top](#-ml-random-forest-numerical)

---

> **Next:** [📖 THEORY](ml_random_forest_theory.md) · [💻 PRACTICE](ml_random_forest_practice.md)
>
> *ML · Random Forest · github.com/rpaut03l/TS-01*
