# 📖 ML Random Forest: THEORY

### *Bagging · Feature Subsampling · OOB · Feature Importance*

> **Nav:** [← ML Master Index](../ml_master_gap_index.md) | **Random Forest** | [🔢 NUMERICAL](ml_random_forest_numerical.md) | [💻 PRACTICE](ml_random_forest_practice.md) | [Related: Ch07 Ensemble →](../Ch07_Ensemble_Learning/ml_ch7_theory.md)
>

---

## 🧠 MNEMONIC: **"B-FROB"**

> **B**ootstrap · **F**eature random subset · **R**eplicate trees · **O**OB error · **B**allot (majority vote)

---

## 📚 Table of Contents

| # | Topic | Jump |
|---|-------|------|
| 1 | Why Random Forest? | [§1](#1-why-random-forest) |
| 2 | Bagging Recap | [§2](#2-bagging-recap) |
| 3 | Two Sources of Randomness | [§3](#3-two-sources-of-randomness) |
| 4 | Random Forest Algorithm | [§4](#4-random-forest-algorithm) |
| 5 | Prediction — Classification & Regression | [§5](#5-prediction) |
| 6 | Out-of-Bag (OOB) Estimate | [§6](#6-out-of-bag-oob-estimate) |
| 7 | Feature Importance | [§7](#7-feature-importance) |
| 8 | Hyperparameters & Tuning | [§8](#8-hyperparameters--tuning) |
| 9 | RF vs Single Tree vs Boosting | [§9](#9-rf-vs-single-tree-vs-boosting) |
| 10 | Strengths · Weaknesses · When to Use | [§10](#10-strengths--weaknesses) |
| 11 | Cheat Sheet & Exam Hacks | [§11](#11-cheat-sheet--exam-hacks) |

---

## 1. Why Random Forest?

### 👶 Easy Story
One doctor can be wrong. Ask **500 doctors** — each with slightly different training — and take the **majority diagnosis**. You'll almost always do better than any single doctor. That's a Random Forest: **many decision trees, each trained differently, vote together**.

### The Problem with Single Trees
- **Low bias** — can fit any pattern.
- **High variance** — tiny change in training data ⇒ totally different tree.
- **Unstable** ⇒ they overfit.

### The Random Forest Fix
> **Grow many de-correlated trees → average them → variance collapses, bias stays.**

```
┌───────────────────────────────────────────────┐
│ RANDOM FOREST = BAGGING + FEATURE RANDOMNESS  │
│                                                │
│     high-variance tree                         │
│          +                                     │
│     many independent copies                    │
│     ────────────────────                       │
│     low-variance ensemble                      │
└───────────────────────────────────────────────┘
```

[↑ Back to Top](#-ml-random-forest-theory)

---

## 2. Bagging Recap

**Bagging** = **B**ootstrap **Agg**regat**ing**, invented by Breiman (1996).

```
ALGORITHM — BAGGING
─────────────────────────────────────────────────────
 For b = 1 to B:
   1. Sample n points from training set WITH replacement
      → bootstrap sample D_b   (≈ 63.2% of unique points)
   2. Train base learner h_b on D_b
 Final prediction:
   Classification:  majority vote of h_1,...,h_B
   Regression:      average of h_1,...,h_B
```

> 🔑 Bagging reduces **variance** without increasing bias — IF the base learners are roughly independent.

### Why "63.2%"?
Probability a particular point is **not** picked in n draws with replacement:
```
(1 - 1/n)^n  →  1/e ≈ 0.368   as n → ∞
⟹ fraction picked at least once ≈ 0.632
```

The ~36.8% NOT picked form the **out-of-bag (OOB) set** for tree b.

[↑ Back to Top](#-ml-random-forest-theory)

---

## 3. Two Sources of Randomness

Random Forest adds a **second** randomness on top of bagging:

| Randomness | What is randomized | Purpose |
|---|---|---|
| **1. Bootstrap** | The **rows** (samples) | Creates variety between trees |
| **2. Feature subsampling** | The **columns** (features) at each split | **De-correlates** trees |

Without feature subsampling, every tree would greedily pick the same top feature at the root ⟹ trees would be too similar ⟹ averaging wouldn't help.

```
AT EACH SPLIT:
  Standard tree:  consider ALL p features → greedy best
  Random Forest:  consider m ≪ p features (random subset) → best within m
```

### Typical `m` (aka `max_features`)
- **Classification:** m = √p
- **Regression:** m = p/3

[↑ Back to Top](#-ml-random-forest-theory)

---

## 4. Random Forest Algorithm

```
ALGORITHM — RANDOM FOREST (Breiman 2001)
──────────────────────────────────────────────────────────────
 INPUT: data D (n samples, p features), B trees, m features/split
 FOR  b = 1 to B:
   1. Draw bootstrap sample D_b of size n
   2. Grow unpruned decision tree T_b on D_b:
      At each node:
        a. Randomly select m features from p
        b. Choose best split among those m (Gini / entropy / MSE)
        c. Split node
      Continue until node size ≤ min_samples_leaf
 OUTPUT: forest {T_1, ..., T_B}

 PREDICT(x):
   Classification: argmax_c Σ 1[T_b(x) = c]   (majority vote)
   Regression:     (1/B) Σ T_b(x)             (average)
```

[↑ Back to Top](#-ml-random-forest-theory)

---

## 5. Prediction

### Classification — Majority Vote
```
Trees predict: [A, B, A, A, B, A, C, A, A, B]
Counts:         A:6, B:3, C:1
Prediction:     A                           ← majority
```

### Classification — Soft Vote (probability averaging)
Better than hard vote: average the class probabilities across trees:
```
p̂(c | x) = (1/B) Σ p̂_b(c | x)
ŷ = argmax_c p̂(c | x)
```
Most libraries (sklearn `predict_proba`) use soft voting.

### Regression — Average
```
ŷ(x) = (1/B) Σ_b T_b(x)
```

[↑ Back to Top](#-ml-random-forest-theory)

---

## 6. Out-of-Bag (OOB) Estimate

Each tree sees ~63.2% of the data ⇒ the remaining ~36.8% is a **free validation set** for that tree — **no need for separate CV**.

```
ALGORITHM — OOB ERROR
──────────────────────────────────────────────
 For each training point xᵢ:
   1. Find all trees T_b where xᵢ was NOT in D_b   (OOB trees)
   2. Predict ŷᵢ by averaging those trees only
 OOB error = (1/n) Σ L(yᵢ, ŷᵢ)
```

> ✅ OOB error is a **nearly unbiased estimate of generalization error** — free cross-validation!

### Practical use
- Skip separate CV to save time.
- Use OOB error to pick `n_estimators` — stop when OOB error plateaus.
- Doesn't replace a true held-out test set, but very close.

[↑ Back to Top](#-ml-random-forest-theory)

---

## 7. Feature Importance

### Method 1 — Mean Decrease in Impurity (MDI, "Gini importance")
```
For each feature j:
  importance(j) = Σ_trees Σ_nodes-using-j  (impurity reduction) × (weighted node size)
```
- **Cheap** (computed during training).
- **Biased** toward features with many unique values (cardinality bias).
- Default in sklearn `.feature_importances_`.

### Method 2 — Permutation Importance
```
1. Compute OOB error e₀
2. For each feature j:
     a. Shuffle feature j's values in OOB set
     b. Recompute error e_j
     c. importance(j) = e_j − e₀
```
- **Unbiased** by cardinality.
- More expensive (one pass per feature).
- Use `sklearn.inspection.permutation_importance`.

### Method 3 — SHAP
Model-agnostic, game-theoretic, slowest but gives per-sample attributions. Not RF-specific.

[↑ Back to Top](#-ml-random-forest-theory)

---

## 8. Hyperparameters & Tuning

| Hyperparameter | What it does | Typical range | Effect |
|---|---|---|---|
| `n_estimators` (B) | Number of trees | 100 – 2000 | ↑ = better & slower (diminishing returns) |
| `max_features` (m) | Features per split | √p (clf), p/3 (reg) | ↓ = more randomness, more trees needed |
| `max_depth` | Max tree depth | None (unlimited) | Shallow → more bias, less overfit |
| `min_samples_split` | Min to split a node | 2 – 10 | ↑ = stronger regularization |
| `min_samples_leaf` | Min per leaf | 1 – 5 | ↑ = smoother |
| `bootstrap` | Use bagging? | True | False = "Extra Trees" |
| `max_samples` | Bootstrap size | n | Smaller → faster, more variance |

### Tuning order of priority
1. **`n_estimators`** — more is always better (up to compute budget). Use OOB to find the knee.
2. **`max_features`** — biggest lever on accuracy after `n_estimators`.
3. **`max_depth` / `min_samples_leaf`** — only if overfitting on small data.
4. Everything else — usually defaults.

[↑ Back to Top](#-ml-random-forest-theory)

---

## 9. RF vs Single Tree vs Boosting

```
┌─────────────┬────────────────┬───────────────┬─────────────────┐
│ ASPECT      │ DECISION TREE  │ RANDOM FOREST │ BOOSTING        │
├─────────────┼────────────────┼───────────────┼─────────────────┤
│ Bias        │ Low            │ Low           │ Progressive ↓    │
│ Variance    │ Very high      │ Low           │ Medium          │
│ Train order │ —              │ Parallel ✅   │ Sequential ❌    │
│ Overfit risk│ High           │ Very low      │ Medium (tune)   │
│ Speed       │ Fast           │ Parallel fast │ Slow            │
│ Interpretable│ ✅ Yes          │ Partial       │ Partial         │
│ Noisy labels│ Bad            │ Robust        │ Hurt by outliers│
│ Hyperparams │ Few            │ Few           │ Many (sensitive)│
└─────────────┴────────────────┴───────────────┴─────────────────┘
```

> **Rule of thumb:** default to RF for tabular data. Switch to gradient boosting (XGBoost / LightGBM / CatBoost) only when you need the last 1–2% and can afford tuning.

[↑ Back to Top](#-ml-random-forest-theory)

---

## 10. Strengths & Weaknesses

### ✅ Strengths
- Works out of the box — minimal tuning.
- Handles mixed data types, missing values (with surrogate splits).
- No scaling needed.
- Built-in OOB validation.
- Feature importance out of the box.
- Parallelizable (trees are independent).
- Robust to outliers and noise.

### ❌ Weaknesses
- Worse than boosting on very clean tabular problems with enough tuning.
- Large memory footprint (thousands of trees).
- Slower prediction than a single tree.
- Not good for very sparse / very high-dimensional data (SVM / linear may win).
- Less interpretable than one tree.
- Biased toward categorical features with many levels (use target encoding or permutation importance).

### When to Use
| Situation | Use RF? |
|---|---|
| Tabular data, mixed types | ✅ First choice |
| < 10k samples | ✅ Yes |
| Image / audio / text | ❌ Use CNN / RNN / transformer |
| Extreme low-latency inference | ❌ Single tree or linear |
| Want uncertainty estimates | ✅ Tree disagreement gives it for free |

[↑ Back to Top](#-ml-random-forest-theory)

---

## 11. Cheat Sheet & Exam Hacks

```
╔══════════════════════════════════════════════════════════════╗
║  RANDOM FOREST ONE-LINERS                                    ║
╠══════════════════════════════════════════════════════════════╣
║  RF = Bagging + random feature subset at every split        ║
║  Bootstrap: sample n WITH replacement → ~63.2% unique       ║
║  OOB: ~36.8% left out → built-in validation                 ║
║  m = √p (classification),  m = p/3 (regression)             ║
║  Classification predict: majority (or soft) vote            ║
║  Regression predict: average                                ║
║  Variance reduction requires de-correlated trees            ║
║  Trees are grown fully (unpruned) — variance handled        ║
║       by averaging, not by depth limits.                    ║
╚══════════════════════════════════════════════════════════════╝
```

### ⚡ Exam Red Flags
1. **"Why does RF reduce variance but not bias?"** — averaging independent estimators shrinks variance by a factor of 1/B (if fully independent) while leaving the expectation unchanged.
2. **"Why random feature subset?"** — to **de-correlate** the trees. Bagging alone isn't enough because the top feature dominates.
3. **"Why are individual trees unpruned?"** — so each is **low-bias** (high-variance). The ensemble averaging handles the variance.
4. **"What is OOB error?"** — error on points **not in each tree's bootstrap sample**. ~1/e of points. Free CV.
5. **"Why is default importance biased?"** — Gini importance favours features with more unique values (more splits possible). Use permutation importance instead.
6. **"RF vs Boosting?"** — RF = parallel, variance-reducer, robust. Boosting = sequential, bias-reducer, usually more accurate when tuned.

[↑ Back to Top](#-ml-random-forest-theory)

---

> **Next:** [🔢 NUMERICAL](ml_random_forest_numerical.md) · [💻 PRACTICE](ml_random_forest_practice.md)
>
> *ML · Random Forest · github.com/rpaut03l/TS-01*
