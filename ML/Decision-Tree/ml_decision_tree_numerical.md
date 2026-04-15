# 🔢 ML Decision Tree: NUMERICAL

### *Rules first → then solve. Every step shown.*

> **Nav:** [← INDEX](../ml_master_gap_index.md) | [📘 Theory Guide](decision_tree_theory_slides_guide.md) | [📗 Guide w/ Math](decision_tree_guide_w_maths.md) | 🔢 **NUMERICAL** | [💻 PRACTICE →](ml_decision_tree_practice.md)

---

## 📦 ALL FORMULAS

```
┌──────────────────────────────────────────────────────────────┐
│ ENTROPY:      H(S) = − Σ pₖ log₂ pₖ                          │
│ GINI:         G(S) = 1 − Σ pₖ²                               │
│ MISCLASS:     E(S) = 1 − max pₖ                              │
│                                                               │
│ INFO GAIN:    IG(S, f) = H(S) − Σ (|Sᵥ|/|S|) · H(Sᵥ)          │
│ GAIN RATIO:   GR = IG / SplitInfo                             │
│    SplitInfo = − Σ (|Sᵥ|/|S|) log₂(|Sᵥ|/|S|)                  │
│                                                               │
│ GINI GAIN:    ΔG = G(S) − Σ (|Sᵥ|/|S|) · G(Sᵥ)                │
│                                                               │
│ REGRESSION SPLIT CRITERION (variance reduction):             │
│   Var(S) = (1/|S|) Σ (yᵢ − ȳ_S)²                              │
│   ΔVar = Var(parent) − Σ (|Sᵥ|/|S|) · Var(Sᵥ)                │
│                                                               │
│ BASE-2 LOG cheat:                                            │
│   log₂(2) = 1, log₂(3) ≈ 1.585, log₂(4) = 2, log₂(5) ≈ 2.322 │
└──────────────────────────────────────────────────────────────┘
```

---

## P1: Compute Entropy and Gini for a node

```
NODE: 10 samples, 6 class A, 4 class B.
  p(A) = 0.6, p(B) = 0.4

ENTROPY:
  H = −(0.6 log₂ 0.6 + 0.4 log₂ 0.4)
    = −(0.6 · (−0.737) + 0.4 · (−1.322))
    = −(−0.442 − 0.529)
    = 0.971 bits

GINI:
  G = 1 − 0.6² − 0.4² = 1 − 0.36 − 0.16 = 0.48

MISCLASS:
  E = 1 − max(0.6, 0.4) = 0.4
```

[↑ Back to Top](#-ml-decision-tree-numerical)

---

## P2: Information Gain on a binary split

```
NODE S (from P1): 10 samples, 6A 4B,  H(S) = 0.971

Split on feature "age < 30":
  LEFT  (age<30)  : 5 samples → 4A, 1B    p = (0.8, 0.2)
  RIGHT (age≥30)  : 5 samples → 2A, 3B    p = (0.4, 0.6)

H(LEFT)  = −(0.8·log₂0.8 + 0.2·log₂0.2)
         = −(0.8·(−0.322) + 0.2·(−2.322))
         = −(−0.258 − 0.464)
         = 0.722
H(RIGHT) = −(0.4·log₂0.4 + 0.6·log₂0.6)
         = −(0.4·(−1.322) + 0.6·(−0.737))
         = −(−0.529 − 0.442)
         = 0.971

WEIGHTED CHILDREN ENTROPY:
  (5/10)·0.722 + (5/10)·0.971 = 0.361 + 0.486 = 0.847

INFO GAIN = H(S) − 0.847 = 0.971 − 0.847 = 0.124 bits
```

[↑ Back to Top](#-ml-decision-tree-numerical)

---

## P3: Gini Gain for the same split

```
G(S) = 1 − 0.6² − 0.4² = 0.48

G(LEFT)  = 1 − 0.8² − 0.2² = 1 − 0.64 − 0.04 = 0.32
G(RIGHT) = 1 − 0.4² − 0.6² = 1 − 0.16 − 0.36 = 0.48

WEIGHTED CHILDREN GINI = (5/10)·0.32 + (5/10)·0.48 = 0.16 + 0.24 = 0.40

ΔG = 0.48 − 0.40 = 0.08

INTERPRETATION: the split lowers Gini by 0.08 → valid improvement.
Gini and Entropy usually agree; Gini is slightly faster (no log).
```

[↑ Back to Top](#-ml-decision-tree-numerical)

---

## P4: Gain Ratio — correcting for many-branch bias

```
Problem with raw Info Gain: splits with MANY categories look great
(because they create tiny, near-pure children). Gain Ratio normalises
by the split's own entropy.

Suppose feature "zip" splits S into 5 equal children:
  SplitInfo = −5 · (1/5) log₂(1/5) = log₂(5) ≈ 2.322
  If IG = 0.9, GR = 0.9 / 2.322 ≈ 0.388

Suppose feature "age<30" splits S into 2 equal children (P2):
  SplitInfo = −2·(1/2)·log₂(1/2) = 1
  IG = 0.124, GR = 0.124 / 1 = 0.124

Even though raw IG of zip (0.9) >> age (0.124), GAIN RATIO fixes that
only if the split-info penalty is big enough. C4.5 uses Gain Ratio.
```

[↑ Back to Top](#-ml-decision-tree-numerical)

---

## P5: Continuous feature — candidate thresholds

```
DATA (feature x, label y):
  (1.0, A), (1.5, A), (2.2, A), (2.9, B), (3.1, B), (4.0, B), (4.5, A)

STEP 1 — Sort by x (already sorted).
STEP 2 — Candidate thresholds are midpoints between CONSECUTIVE
         points with DIFFERENT labels:
  between (2.2,A) and (2.9,B)  →  t = 2.55
  between (4.0,B) and (4.5,A)  →  t = 4.25

STEP 3 — Evaluate each threshold:
  t = 2.55:
    LEFT  {(1.0,A),(1.5,A),(2.2,A)}    = 3A, 0B  pure → G=0, H=0
    RIGHT {(2.9,B),(3.1,B),(4.0,B),(4.5,A)} = 3B, 1A
    G(R) = 1 − (1/4)² − (3/4)² = 1 − 0.0625 − 0.5625 = 0.375
    Weighted G = (3/7)·0 + (4/7)·0.375 ≈ 0.214

  t = 4.25:
    LEFT  {...six points} = 3A, 3B   G = 1 − 0.25 − 0.25 = 0.50
    RIGHT {(4.5,A)}         pure → G=0
    Weighted G = (6/7)·0.50 + (1/7)·0 ≈ 0.429

PICK t = 2.55 (lowest weighted Gini).
```

[↑ Back to Top](#-ml-decision-tree-numerical)

---

## P6: Regression split — variance reduction

```
DATA (x, y):
  (1, 2), (2, 3), (3, 5), (4, 8), (5, 9), (6, 10)

PARENT:
  ȳ = (2+3+5+8+9+10) / 6 = 37/6 ≈ 6.167
  Var = (1/6)·[(2−6.167)² + (3−6.167)² + (5−6.167)² +
               (8−6.167)² + (9−6.167)² + (10−6.167)²]
      = (1/6)·[17.36 + 10.03 + 1.36 + 3.36 + 8.03 + 14.69]
      = 54.83 / 6 ≈ 9.139

SPLIT at x < 4:
  LEFT  {(1,2),(2,3),(3,5)}  ȳ_L = 10/3 ≈ 3.333
    Var_L = (1/3)·[(2−3.33)² + (3−3.33)² + (5−3.33)²]
          = (1/3)·[1.78 + 0.11 + 2.78]
          = 4.67 / 3 ≈ 1.556
  RIGHT {(4,8),(5,9),(6,10)} ȳ_R = 27/3 = 9
    Var_R = (1/3)·[(8−9)² + (9−9)² + (10−9)²] = 2/3 ≈ 0.667

WEIGHTED CHILD VARIANCE:
  (3/6)·1.556 + (3/6)·0.667 = 0.778 + 0.333 = 1.111

VARIANCE REDUCTION:
  ΔVar = 9.139 − 1.111 = 8.028   ← big → good split
```

[↑ Back to Top](#-ml-decision-tree-numerical)

---

## P7: Cost-complexity (weakest-link) pruning — walk-through

```
COST-COMPLEXITY:  Cα(T) = R(T) + α · |leaves(T)|
  R(T)   = training error (sum of impurities weighted by node size)
  α      = complexity parameter

AS α ↑:
  α = 0:     biggest (unpruned) tree is best.
  α ↑:       collapse the subtree whose removal INCREASES R(T)
             least per leaf removed (the "weakest link").
  α large:   only the root remains.

ALGORITHM:
  1. Fit the full tree T₀.
  2. Compute, for each internal node t:
       g(t) = (R(t) − R(T_t)) / (|leaves(T_t)| − 1)
     = cost of pruning this subtree per leaf removed.
  3. The subtree with smallest g(t) is the weakest link — prune it.
  4. Record (α_k = g(t), T_k) and repeat until only root remains.
  5. Pick the tree with best CV error.

sklearn returns (ccp_alphas, impurities) via `.cost_complexity_pruning_path`.
```

[↑ Back to Top](#-ml-decision-tree-numerical)

---

## P8: Gini / Entropy / Misclassification — compare at the same node

```
NODE: (p, 1−p) for various p of class A
  Gini        = 2p(1−p)
  Entropy     = −p log₂ p − (1−p) log₂(1−p)
  Misclass    = 1 − max(p, 1−p)

  p          Gini   Entropy   Misclass
  ─────────  ─────  ────────  ────────
  0.00       0.00    0.000    0.00
  0.10       0.18    0.469    0.10
  0.30       0.42    0.881    0.30
  0.50       0.50    1.000    0.50       ← all max at p=0.5
  0.70       0.42    0.881    0.30
  0.90       0.18    0.469    0.10
  1.00       0.00    0.000    0.00

OBSERVATIONS:
- All three peak at p = 0.5 (maximum uncertainty).
- Gini and Entropy are smooth → differentiable splits → used for training.
- Misclassification is piecewise-linear → not smooth → used only for
  pruning ("validation" time), not for choosing splits.
```

[↑ Back to Top](#-ml-decision-tree-numerical)

---

> **Next:** [📘 Theory Guide](decision_tree_theory_slides_guide.md) · [💻 PRACTICE](ml_decision_tree_practice.md)
>
> *ML · Decision Tree · github.com/rpaut03l/TS-01*
