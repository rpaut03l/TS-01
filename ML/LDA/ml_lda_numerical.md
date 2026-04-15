# 🔢 ML LDA: NUMERICAL

### *Rules first → then solve. Every step shown.*

> **Nav:** [← INDEX](../ml_master_gap_index.md) | [📖 THEORY](ml_lda_theory.md) | 🔢 **NUMERICAL** | [💻 PRACTICE →](ml_lda_practice.md) | [📘 Detailed Guide](lda_guide_1.md)

---

## 📦 ALL FORMULAS

```
┌──────────────────────────────────────────────────────────────┐
│ CLASS MEAN:    μₖ = (1/nₖ) Σ xᵢ   (i in class k)              │
│ GLOBAL MEAN:   μ  = (1/n)  Σ xᵢ                              │
│                                                              │
│ WITHIN-CLASS SCATTER:                                        │
│   Sₖ = Σᵢ∈k (xᵢ − μₖ)(xᵢ − μₖ)ᵀ                               │
│   Sw = Σₖ Sₖ                                                  │
│                                                              │
│ BETWEEN-CLASS SCATTER:                                       │
│   Sb = Σₖ nₖ (μₖ − μ)(μₖ − μ)ᵀ                                 │
│                                                              │
│ FISHER CRITERION (2 class): J(w) = (wᵀ Sb w) / (wᵀ Sw w)     │
│ OPTIMAL DIRECTION:           w ∝ Sw⁻¹ (μ₂ − μ₁)              │
│                                                              │
│ MULTI-CLASS: eigenvectors of Sw⁻¹ Sb, top (C−1) of them      │
│                                                              │
│ LDA CLASSIF RULE (equal priors, shared Σ):                   │
│   δₖ(x) = xᵀΣ⁻¹μₖ − ½μₖᵀΣ⁻¹μₖ + log πₖ                         │
│   ŷ = argmax_k δₖ(x)                                         │
└──────────────────────────────────────────────────────────────┘
```

---

## P1: Two-class Fisher LDA — find w

```
CLASS 1:  X₁ = {(4,1), (2,4), (2,3), (3,6), (4,4)}
CLASS 2:  X₂ = {(9,10), (6,8), (9,5), (8,7), (10,8)}

STEP 1 — Class means
  μ₁ = (15/5, 18/5) = (3.0, 3.6)
  μ₂ = (42/5, 38/5) = (8.4, 7.6)

STEP 2 — Within-class scatter S₁
  Deviations from μ₁ for class 1:
    (4−3, 1−3.6)     = (+1.0, −2.6)
    (2−3, 4−3.6)     = (−1.0, +0.4)
    (2−3, 3−3.6)     = (−1.0, −0.6)
    (3−3, 6−3.6)     = ( 0.0, +2.4)
    (4−3, 4−3.6)     = (+1.0, +0.4)

  Σ (outer products):
    [ 1  −2.6 ]   [ 1  −0.4]   [ 1  +0.6]   [ 0    0 ]   [ 1  +0.4]
    [−2.6  6.76]  [−0.4 0.16]  [+0.6 0.36]  [ 0  5.76]   [+0.4 0.16]

  S₁ ≈ [  4.0    −2.0 ]
       [ −2.0    13.2 ]

STEP 3 — Within-class scatter S₂ (same recipe for class 2)
  Deviations from μ₂ = (8.4, 7.6):
    (9, 10) → (+0.6, +2.4)
    (6,  8) → (−2.4, +0.4)
    (9,  5) → (+0.6, −2.6)
    (8,  7) → (−0.4, −0.6)
    (10, 8) → (+1.6, +0.4)

  S₂ ≈ [  9.2    −0.4 ]
       [ −0.4    13.2 ]

STEP 4 — Sw
  Sw = S₁ + S₂ = [ 13.2  −2.4 ]
                 [ −2.4  26.4 ]

STEP 5 — w ∝ Sw⁻¹ (μ₂ − μ₁)
  μ₂ − μ₁ = (8.4 − 3.0, 7.6 − 3.6) = (5.4, 4.0)

  det(Sw) = 13.2·26.4 − (−2.4)(−2.4) = 348.48 − 5.76 = 342.72
  Sw⁻¹ = (1/342.72) · [  26.4   2.4 ]
                     [   2.4  13.2 ]

  w_unnorm = Sw⁻¹ · (5.4, 4.0)ᵀ
           = (1/342.72) · (26.4·5.4 + 2.4·4.0,
                           2.4·5.4 + 13.2·4.0)
           = (1/342.72) · (142.56 + 9.6,  12.96 + 52.8)
           = (1/342.72) · (152.16, 65.76)
           ≈ (0.4440, 0.1918)

  Normalize: ‖w‖ ≈ √(0.1972 + 0.0368) ≈ √0.2340 ≈ 0.4837
  ŵ ≈ (0.9179, 0.3966)

RESULT: the Fisher direction is ŵ ≈ (0.918, 0.397).
```

[↑ Back to Top](#-ml-lda-numerical)

---

## P2: Project points on w and check separation

```
Using ŵ ≈ (0.918, 0.397) from P1:

Class 1 projections (ŵᵀ x):
  (4, 1)  → 0.918·4 + 0.397·1 = 3.672 + 0.397 = 4.069
  (2, 4)  → 1.836 + 1.588     = 3.424
  (2, 3)  → 1.836 + 1.191     = 3.027
  (3, 6)  → 2.754 + 2.382     = 5.136
  (4, 4)  → 3.672 + 1.588     = 5.260
  mean ≈ 4.183

Class 2 projections:
  (9, 10) → 8.262 + 3.970 = 12.232
  (6,  8) → 5.508 + 3.176 =  8.684
  (9,  5) → 8.262 + 1.985 = 10.247
  (8,  7) → 7.344 + 2.779 = 10.123
  (10, 8) → 9.180 + 3.176 = 12.356
  mean ≈ 10.728

Separation (difference of class means on w):
  10.728 − 4.183 = 6.545

Within-class spread on w (std of projections):
  std(class 1) ≈ 0.99
  std(class 2) ≈ 1.45

Large difference in means vs small within-class spread ⟹ LDA works great here.
```

[↑ Back to Top](#-ml-lda-numerical)

---

## P3: LDA classifier decision rule (equal priors, shared Σ)

```
Assume shared covariance Σ (say identity for simplicity), two classes,
equal priors π₁ = π₂ = 0.5, μ₁ = (0,0), μ₂ = (4,0).

Discriminant:
  δₖ(x) = xᵀΣ⁻¹μₖ − ½μₖᵀΣ⁻¹μₖ + log πₖ

With Σ = I and equal priors:
  δ₁(x) = xᵀ·(0,0) − ½·0 = 0
  δ₂(x) = xᵀ·(4,0) − ½·(16)   = 4·x₁ − 8

Decision boundary: δ₁(x) = δ₂(x)
  0 = 4 x₁ − 8  ⟹  x₁ = 2

So the boundary is the vertical line x₁ = 2 — exactly the perpendicular
bisector of the segment between the two means (as expected for equal
priors + identity covariance).
```

[↑ Back to Top](#-ml-lda-numerical)

---

## P4: Why Sw can be singular (and how shrinkage fixes it)

```
Say d = 5 features, n = 4 samples total.
Each (xᵢ − μₖ) lives in R⁵.
Sw is a sum of rank-1 outer products: rank(Sw) ≤ min(d, n−C).

If n=4 and C=2, rank(Sw) ≤ 2 < 5 = d.
⟹ Sw is SINGULAR, cannot invert, LDA breaks.

SHRINKAGE:
  Sw' = (1−α)·Sw + α · (trace(Sw)/d) · I

  α = 0    → original Sw
  α = 1    → diagonal (= scalar identity scaled by avg variance)
  Automatic α (Ledoit-Wolf) estimates optimal shrinkage.

Now Sw' is always positive-definite and invertible, and LDA works
even when n < d.
```

[↑ Back to Top](#-ml-lda-numerical)

---

## P5: LDA dim reduction — max components = C − 1

```
Sb has rank ≤ C − 1 (there are C class means, only C−1 independent differences).
⟹ at most C−1 nonzero generalized eigenvalues.

IRIS: C = 3 classes ⟹ LDA can give at most 2 components.
MNIST: C = 10 ⟹ at most 9 components.

TAKEAWAY: PCA can give up to d dimensions; LDA is capped at C−1.
```

[↑ Back to Top](#-ml-lda-numerical)

---

## P6: Between-class scatter Sb — worked

```
Data from P1:
  n₁ = n₂ = 5, global mean μ = ( (15+42)/10, (18+38)/10 ) = (5.7, 5.6)

Sb = Σₖ nₖ (μₖ − μ)(μₖ − μ)ᵀ

  μ₁ − μ = (3.0 − 5.7, 3.6 − 5.6) = (−2.7, −2.0)
  μ₂ − μ = (8.4 − 5.7, 7.6 − 5.6) = (+2.7, +2.0)

  (μ₁ − μ)(μ₁ − μ)ᵀ = [  7.29   5.40 ]
                     [  5.40   4.00 ]
  (μ₂ − μ)(μ₂ − μ)ᵀ = same (since values are mirrored)

  Sb = 5·[ 7.29  5.40 ] + 5·[ 7.29  5.40 ]
       [ 5.40  4.00 ]      [ 5.40  4.00 ]
     = [ 72.90  54.00 ]
       [ 54.00  40.00 ]

Fisher ratio along direction w (rough check with ŵ from P1):
  wᵀSbw / wᵀSww   ≈ large  ⟹  w is a good Fisher direction ✓
```

[↑ Back to Top](#-ml-lda-numerical)

---

## P7: Classify a new point with two LDA means (1D projection)

```
From P2 we have class-mean projections on w:
  m₁' ≈ 4.18
  m₂' ≈ 10.73

Midpoint threshold (equal priors, equal within-class variance):
  t = (4.18 + 10.73) / 2 = 7.455

New point x* = (5, 5).
  projection: 0.918·5 + 0.397·5 = 4.59 + 1.985 = 6.575

  6.575 < 7.455  ⟹  class 1 ✓
```

[↑ Back to Top](#-ml-lda-numerical)

---

## P8: Effective degrees of freedom — LDA vs QDA

```
Dataset: d features, C classes, n samples.

LDA parameters:
  - C class means:     C · d
  - 1 shared cov:      d(d+1)/2
  - total:             C·d + d(d+1)/2

QDA parameters:
  - C class means:     C · d
  - C covariances:     C · d(d+1)/2
  - total:             C·d + C · d(d+1)/2

For d=10, C=3:
  LDA = 30 + 55 = 85
  QDA = 30 + 3·55 = 195

QDA has ~2.3× more parameters → needs more data to fit reliably.
Rule of thumb: prefer LDA when n/d is small; QDA when n/d is large.
```

[↑ Back to Top](#-ml-lda-numerical)

---

> **Next:** [📖 THEORY](ml_lda_theory.md) · [💻 PRACTICE](ml_lda_practice.md)
>
> *ML · LDA · github.com/rpaut03l/TS-01*
