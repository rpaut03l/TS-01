# 📖 ML K-Nearest Neighbors (K-NN): THEORY

### *Lazy learning · Distance metrics · Choosing k · Curse of dimensionality*

> **Nav:** [← ML Master Index](../ml_master_gap_index.md) | **K-NN** | [🔢 NUMERICAL](ml_knn_numerical.md) | [💻 PRACTICE Guide](k-nn_algorithm_practice_guide_with_code.md) | [📘 Detailed Guide](k-nn_classification_algorithm_guide.md)
>

---

## 🧠 MNEMONIC: **"LAZY-DK"**

> **L**azy learner · **A**ll training stored · **Z**ero training cost · **Y**ields by vote · **D**istance-based · **K** neighbors

---

## 📚 Table of Contents

| # | Topic | Jump |
|---|-------|------|
| 1 | What is K-NN? | [§1](#1-what-is-k-nn) |
| 2 | The Algorithm | [§2](#2-the-algorithm) |
| 3 | Distance Metrics | [§3](#3-distance-metrics) |
| 4 | Choosing k | [§4](#4-choosing-k) |
| 5 | Weighted Voting | [§5](#5-weighted-voting) |
| 6 | K-NN Regression | [§6](#6-k-nn-regression) |
| 7 | Feature Scaling — NON-NEGOTIABLE | [§7](#7-feature-scaling--non-negotiable) |
| 8 | Curse of Dimensionality | [§8](#8-curse-of-dimensionality) |
| 9 | Complexity & Speed-ups (KD-Tree, Ball Tree) | [§9](#9-complexity--speed-ups) |
| 10 | Strengths · Weaknesses · When to Use | [§10](#10-strengths--weaknesses) |
| 11 | Cheat Sheet & Exam Hacks | [§11](#11-cheat-sheet--exam-hacks) |

---

## 1. What is K-NN?

### 👶 Easy Story
You move to a new city. To guess if a restaurant is good, you find the **5 most similar restaurants you already know** and check how many of them you liked. If 4 out of 5 were good, this one probably is too. That's K-NN: **classify by looking at the k closest training points**.

### Key Idea
> **K-NN is a LAZY learner** — it doesn't build a model during training. All the "work" happens at prediction time.

```
┌───────────────────────────────────────────────┐
│ TRAINING:   store all (xᵢ, yᵢ)   → O(1)        │
│ PREDICT:    compute distance to each xᵢ        │
│             pick k smallest → majority vote    │
│             → O(n · d) per query               │
└───────────────────────────────────────────────┘
```

- **Non-parametric** — no fixed model form, can fit arbitrary decision boundaries.
- **Instance-based** — the training data IS the model.
- **Works for** classification **and** regression.

[↑ Back to Top](#-ml-k-nearest-neighbors-k-nn-theory)

---

## 2. The Algorithm

```
ALGORITHM — K-NN CLASSIFICATION
────────────────────────────────────────────
 INPUT: training set {(xᵢ, yᵢ)}ᵢ₌₁ⁿ, query x, k
 1. For each i in 1..n:
       compute  d(x, xᵢ)
 2. Pick the k indices with smallest d
 3. Collect their labels y_(1), ..., y_(k)
 4. Return  argmax_c  Σ 1[y_(j) = c]   (majority vote)
```

### Decision Boundary
As k → 1, the boundary is **jagged** (every point claims a Voronoi cell). As k → n, it flattens to the **global majority class**. Choosing k is a bias-variance knob:

```
 k small  →  LOW bias,  HIGH variance  (overfit)
 k large  →  HIGH bias, LOW  variance  (underfit)
```

[↑ Back to Top](#-ml-k-nearest-neighbors-k-nn-theory)

---

## 3. Distance Metrics

| Metric | Formula | Use when |
|---|---|---|
| **Euclidean** (L2) | √Σ(xᵢ − yᵢ)² | Continuous features, scaled |
| **Manhattan** (L1) | Σ\|xᵢ − yᵢ\| | Grid-like / robust to outliers |
| **Minkowski** (Lp) | (Σ\|xᵢ − yᵢ\|ᵖ)^(1/p) | Generalization of L1/L2 |
| **Chebyshev** (L∞) | max\|xᵢ − yᵢ\| | Worst-coordinate distance |
| **Cosine** | 1 − (x·y)/(‖x‖‖y‖) | Text, sparse vectors, direction > magnitude |
| **Hamming** | Σ 1[xᵢ ≠ yᵢ] | Binary / categorical |
| **Mahalanobis** | √((x−y)ᵀ Σ⁻¹ (x−y)) | Accounts for feature correlation |

### Minkowski is the boss
```
Lp(x, y) = (Σ |xᵢ − yᵢ|ᵖ)^(1/p)
  p = 1   → Manhattan
  p = 2   → Euclidean
  p → ∞   → Chebyshev
```

sklearn's `KNeighborsClassifier(metric='minkowski', p=2)` default ⇒ Euclidean.

[↑ Back to Top](#-ml-k-nearest-neighbors-k-nn-theory)

---

## 4. Choosing k

### Rules of thumb
- **k = √n** is a decent starting point.
- Prefer **odd k** for binary classification (avoid ties).
- Tune with **cross-validation** — pick the k with the lowest CV error.

### Bias–Variance View
```
              ┌───────────┐
              │ TOTAL ERR │
              └─────┬─────┘
    ┌───────────────┼───────────────┐
    ▼               ▼               ▼
  BIAS²         VARIANCE          NOISE
  ↑ with k      ↓ with k         constant
```

- **k = 1**: memorizes training data → train error 0, test error high (overfit).
- **k = n**: predicts global majority → train = test error (severe underfit).

[↑ Back to Top](#-ml-k-nearest-neighbors-k-nn-theory)

---

## 5. Weighted Voting

Not all neighbors are equally close. Give closer ones more say:

```
weight_i = 1 / d(x, xᵢ)ᵖ        (inverse distance)

Prediction = argmax_c  Σᵢ∈Nₖ  weight_i · 1[yᵢ = c]
```

**Pros:** smoother decision boundary, less sensitive to k, reduces ties.
**Cons:** a point at distance 0 causes a divide-by-zero (use `d + ε` or `weights='distance'` in sklearn).

[↑ Back to Top](#-ml-k-nearest-neighbors-k-nn-theory)

---

## 6. K-NN Regression

Same idea, different aggregation:
```
ŷ(x) = (1/k) Σᵢ∈Nₖ  yᵢ              (unweighted mean)
ŷ(x) = Σᵢ wᵢ yᵢ / Σᵢ wᵢ              (distance-weighted mean)
```
The prediction is the **average** (or weighted average) of the neighbors' target values.

[↑ Back to Top](#-ml-k-nearest-neighbors-k-nn-theory)

---

## 7. Feature Scaling — NON-NEGOTIABLE

K-NN uses distance ⇒ any feature on a larger scale dominates the sum.

```
EXAMPLE — house data
  age:    1–100
  price:  100,000 – 10,000,000

Euclidean distance is dominated by price.
Age contributes essentially nothing.
```

**Fix:** StandardScaler (mean 0, std 1) or MinMaxScaler ([0, 1]) BEFORE K-NN. Always.

> ⚠️ If you take nothing else from this note, take this: **scale your features before K-NN**.

[↑ Back to Top](#-ml-k-nearest-neighbors-k-nn-theory)

---

## 8. Curse of Dimensionality

In high dimensions, **all points become roughly equidistant** — the concept of "nearest neighbor" breaks down.

### Intuition
- In 1D, a unit interval holds points densely.
- In 10D, to cover the same *fraction* of the volume you need 1.2¹⁰ ≈ 6.2× the side length.
- By d = 100, the nearest neighbor is barely closer than the farthest.

```
┌────────────────────────────────────────────┐
│ d = 2   →  nearest vs farthest ratio ≈ 2  │
│ d = 10  →  ratio ≈ 1.2                     │
│ d = 100 →  ratio ≈ 1.02   ← meaningless!   │
└────────────────────────────────────────────┘
```

### Mitigations
- **Dimensionality reduction** — PCA, LDA (see [Feature Selection](../Feature-Selection-DimRed/ml_pca_ica_fs_theory.md))
- **Feature selection** — keep only informative features
- **Metric learning** — learn a Mahalanobis matrix that emphasizes useful directions
- **Fewer, smarter features** > many raw features

[↑ Back to Top](#-ml-k-nearest-neighbors-k-nn-theory)

---

## 9. Complexity & Speed-ups

```
NAIVE:
  Train  : O(1)       — just store
  Predict: O(n · d)   per query — compute all distances

FOR n LARGE:
  - KD-Tree     (sklearn default if d < 20) → O(log n) avg
  - Ball Tree   for metric spaces            → O(log n) avg
  - Approx NN   HNSW, FAISS, Annoy           → sub-linear
  - LSH         locality-sensitive hashing
```

KD-Trees collapse back to O(n) in very high dimensions (curse of dimensionality, again).

[↑ Back to Top](#-ml-k-nearest-neighbors-k-nn-theory)

---

## 10. Strengths & Weaknesses

### ✅ Strengths
- **Zero training cost** — no model fitting.
- **Non-parametric** — can approximate any boundary.
- **Works for classification AND regression.**
- **Naturally handles multi-class.**
- Easy to explain: "this point is like these 5 neighbors."

### ❌ Weaknesses
- **Slow inference** — O(n·d) per query (unless indexed).
- **Memory-hungry** — stores all training data.
- **Sensitive to scale, irrelevant features, curse of dimensionality.**
- **No model to inspect** — interpretability is only via neighbors.
- **Imbalanced classes** skew majority votes.

### When to Use
| Situation | Use K-NN? |
|---|---|
| Small dataset (< 10k samples) | ✅ Great baseline |
| Low dimensional, scaled features | ✅ |
| Recommender systems ("users like you…") | ✅ |
| High-dimensional text / vision | ❌ Use linear / NN / tree models |
| Low-latency inference needed | ❌ |
| Streaming data | ❌ (memory grows) |

[↑ Back to Top](#-ml-k-nearest-neighbors-k-nn-theory)

---

## 11. Cheat Sheet & Exam Hacks

```
╔══════════════════════════════════════════════════════════════╗
║  K-NN ONE-LINERS                                             ║
╠══════════════════════════════════════════════════════════════╣
║  Lazy learner: store training data, compute at query time   ║
║  Predict: majority vote (classification), mean (regression) ║
║  Default k rule-of-thumb:  k ≈ √n,  odd for binary          ║
║  Small k → overfit ; Large k → underfit                     ║
║  Always SCALE features before K-NN                          ║
║  Euclidean = L2, Manhattan = L1, Cosine for text            ║
║  O(nd) prediction; KD-Tree helps if d small                 ║
║  Curse of dimensionality hurts in high d                    ║
╚══════════════════════════════════════════════════════════════╝
```

### ⚡ Exam Red Flags
1. **"Why must we scale features?"** — distance metric is dominated by the largest-scale feature otherwise.
2. **"What happens as k → 1 and k → n?"** — k=1 overfits (memorization), k=n predicts the global majority.
3. **"Why is K-NN 'lazy'?"** — training just stores data; all computation is deferred to query time.
4. **"What is the curse of dimensionality in K-NN?"** — in high d, all pairwise distances concentrate near the same value, so "nearest" stops being informative.
5. **"Difference: K-NN regression vs classification?"** — regression averages (or weighted-averages) the k neighbors' y values; classification takes the majority vote.
6. **"When does weighted voting help?"** — when there's a clear difference in distance between neighbors and you want closer ones to dominate; also reduces ties.

[↑ Back to Top](#-ml-k-nearest-neighbors-k-nn-theory)

---

> **Next:** [🔢 NUMERICAL](ml_knn_numerical.md) · [💻 PRACTICE GUIDE](k-nn_algorithm_practice_guide_with_code.md)
>
> *ML · K-NN · github.com/rpaut03l/TS-01*
