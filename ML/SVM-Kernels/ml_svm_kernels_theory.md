# 📖 SVM & Kernel Methods: THEORY + NUMERICAL + PRACTICE

### *Kernel Trick · SVM Primal/Dual · K-SVR · K-PCA*

> **Nav:** [← Clustering](../Clustering/ml_kmeans_gmm_em_theory.md) | **SVM & Kernels** | [Neural Networks →](../Neural-Networks/ml_nn_mlp_bp_theory.md)

---

## 🧠 MNEMONIC: **"SLIM-KPDR"**

> **S**upport vectors · **L**agrangian · **I**nner product · **M**argin · **K**ernel trick · **P**rimal-dual · **D**ecision boundary · **R**BF

---

## 📚 Table of Contents

| # | Topic | Jump |
|---|-------|------|
| 1 | SVM Intuition | [§1](#1-svm-intuition) |
| 2 | Hard-Margin SVM (Primal) | [§2](#2-hard-margin-svm-primal) |
| 3 | Soft-Margin SVM | [§3](#3-soft-margin-svm) |
| 4 | Dual Form | [§4](#4-dual-form) |
| 5 | Kernel Trick | [§5](#5-kernel-trick) |
| 6 | Common Kernels | [§6](#6-common-kernels) |
| 7 | K-SVR & K-PCA | [§7](#7-kernel-svr--kernel-pca) |
| 8 | Numericals | [§8](#8-numericals) |
| 9 | Cheat Sheet | [§9](#9-cheat-sheet--exam-hacks) |

---

## 1. SVM Intuition

### 👶 Easy Story
Imagine separating red and blue marbles on a table with a ruler. Many lines can separate them, but SVM finds the line with the FATTEST gap (margin) between the two groups. The marbles closest to the line are called "support vectors" — they're the only ones that matter!

```
         +          SMALL MARGIN:         MAXIMUM MARGIN (SVM):
      +     +         +  |  -               +    |    -
   +    +   +    +   +  |  - -           +   + ===|=== -  -
      + +  +     +   + | - -               +  +  |   - -
         +            | -  -                     |    -

                      ^thin gap           ^FAT gap = SVM's goal!
                                          |<-margin->|

SUPPORT VECTORS: the points ON the margin boundary
  → Only these determine the decision boundary
  → Remove any non-support-vector → boundary doesn't change!
```

[↑ Back to Top](#-svm--kernel-methods-theory--numerical--practice)

---

## 2. Hard-Margin SVM (Primal)

```
PRIMAL FORMULATION:
━━━━━━━━━━━━━━━━━━
  minimize:   ½||w||²            ← minimize inverse of margin
  subject to: yᵢ(wᵀxᵢ + b) ≥ 1  ← all points correctly classified
                                    with margin ≥ 1

  MARGIN = 2/||w||  (distance between the two margin boundaries)
  → Minimize ||w|| = Maximize margin

  Decision boundary: wᵀx + b = 0
  Margin boundaries: wᵀx + b = +1 (positive class side)
                     wᵀx + b = -1 (negative class side)

  ONLY WORKS when data is LINEARLY SEPARABLE!
```

[↑ Back to Top](#-svm--kernel-methods-theory--numerical--practice)

---

## 3. Soft-Margin SVM

```
WHEN DATA IS NOT PERFECTLY SEPARABLE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Allow some points to violate margin using SLACK VARIABLES ξᵢ

  minimize:   ½||w||² + C Σᵢ ξᵢ      ← balance margin vs violations
  subject to: yᵢ(wᵀxᵢ + b) ≥ 1 - ξᵢ  ← allow slack
              ξᵢ ≥ 0                    ← slack is non-negative

  C = regularization parameter:
    C → ∞:  no violations allowed (hard margin)
    C → 0:  ignore violations, maximize margin (very soft)
    
  ξᵢ = 0:   point is on correct side of margin
  0 < ξᵢ < 1: point is in margin but correctly classified
  ξᵢ > 1:   point is MISCLASSIFIED

CHOOSING C:
  Large C → narrow margin, few violations → can overfit
  Small C → wide margin, more violations → can underfit
  → Use cross-validation to find best C
```

[↑ Back to Top](#-svm--kernel-methods-theory--numerical--practice)

---

## 4. Dual Form

```
WHY DUAL? → Allows us to use the KERNEL TRICK!

DUAL FORMULATION:
━━━━━━━━━━━━━━━━━
  maximize:   Σᵢ αᵢ − ½ ΣᵢΣⱼ αᵢαⱼyᵢyⱼ(xᵢᵀxⱼ)
  subject to: Σᵢ αᵢyᵢ = 0
              0 ≤ αᵢ ≤ C    (soft margin; for hard margin: αᵢ ≥ 0)

  DECISION FUNCTION:
    f(x) = sign( Σᵢ αᵢyᵢ(xᵢᵀx) + b )

  KEY INSIGHT: data appears ONLY as dot products xᵢᵀxⱼ
    → Replace xᵢᵀxⱼ with K(xᵢ,xⱼ) = kernel trick!

  SUPPORT VECTORS: points where αᵢ > 0
    Most αᵢ = 0 → sparse solution → fast prediction!

  KKT CONDITIONS:
    αᵢ = 0     → point outside margin (doesn't matter)
    0 < αᵢ < C → point ON margin boundary (support vector)
    αᵢ = C     → point violating margin (in margin or misclassified)
```

[↑ Back to Top](#-svm--kernel-methods-theory--numerical--practice)

---

## 5. Kernel Trick

### 👶 Easy Story
A circle of red points surrounded by blue points — no line can separate them in 2D. But if you ADD a 3rd dimension (z = x²+y²), the red points go up and blue stay low. Now a FLAT plane separates them! The kernel trick does this IMPLICITLY without actually computing the higher-dimensional coordinates.

```
THE TRICK:
━━━━━━━━━━
  Instead of:  φ(xᵢ)ᵀφ(xⱼ)     ← map to high-D, then dot product (EXPENSIVE)
  Compute:     K(xᵢ, xⱼ)        ← same result, never compute φ! (CHEAP)

  EXAMPLE (polynomial, degree 2):
    x = [x₁, x₂]
    φ(x) = [x₁², √2·x₁x₂, x₂²]  ← 2D → 3D
    
    φ(x)ᵀφ(z) = x₁²z₁² + 2x₁x₂z₁z₂ + x₂²z₂² = (xᵀz)²
    
    K(x,z) = (xᵀz)²  ← just compute this! No need for φ!

  2D (not separable):          3D after kernel (separable!):
       - - -                        - - -
     - + + + -                    ╱─────────╲
     - + + + -                   │  + + +    │ ← hyperplane
     - + + + -                    ╲─────────╱    separates!
       - - -                        - - -
```

[↑ Back to Top](#-svm--kernel-methods-theory--numerical--practice)

---

## 6. Common Kernels

```
┌──────────────┬────────────────────────┬──────────────────────────┐
│ Kernel       │ Formula                │ When to Use              │
├──────────────┼────────────────────────┼──────────────────────────┤
│ Linear       │ K(x,z) = xᵀz           │ Already linearly sep.    │
│ Polynomial   │ K(x,z) = (xᵀz + c)ᵈ    │ Polynomial relationships │
│ RBF/Gaussian │K(x,z) = exp(-γ||x-z||²)│ Most common default      │
│ Sigmoid      │ K(x,z) = tanh(κxᵀz+c)  │ Neural-net-like          │
└──────────────┴────────────────────────┴──────────────────────────┘

RBF KERNEL (most popular):
  γ small → wide Gaussian → smooth boundary → may underfit
  γ large → narrow Gaussian → complex boundary → may overfit
  
  RULE: γ = 1/(2σ²) where σ = bandwidth

MERCER'S CONDITION:
  A valid kernel must produce a positive semi-definite Gram matrix:
  K_matrix[i,j] = K(xᵢ,xⱼ)  must have all eigenvalues ≥ 0
```

[↑ Back to Top](#-svm--kernel-methods-theory--numerical--practice)

---

## 7. Kernel SVR & Kernel PCA

```
KERNEL SVR (Support Vector Regression):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Goal: fit a tube (ε-tube) around data in kernel space
  
  minimize: ½||w||² + C Σᵢ (ξᵢ + ξᵢ*)
  subject to: yᵢ - (wᵀφ(xᵢ)+b) ≤ ε + ξᵢ
              (wᵀφ(xᵢ)+b) - yᵢ ≤ ε + ξᵢ*
              ξᵢ, ξᵢ* ≥ 0
  
  ε = tube width (errors within ε are ignored)
  Points OUTSIDE tube → support vectors
  
  Prediction: f(x) = Σᵢ (αᵢ - αᵢ*) K(xᵢ, x) + b

KERNEL PCA:
━━━━━━━━━━━
  Regular PCA: linear, finds straight directions of max variance
  Kernel PCA: maps to high-D via kernel, then does PCA there
  → Captures non-linear structure!
  
  Steps:
  1. Compute K matrix: Kᵢⱼ = K(xᵢ, xⱼ)
  2. Center K: K̃ = K - 1ₙK - K1ₙ + 1ₙK1ₙ  (where 1ₙ = (1/n)11ᵀ)
  3. Eigendecompose K̃: K̃α = λα
  4. Project: PCₖ(x) = Σᵢ αᵢₖ K(xᵢ, x)
```

[↑ Back to Top](#-svm--kernel-methods-theory--numerical--practice)

---

## 8. Numericals

### N1: Compute Margin

```
Given w = [3, 4], b = -1. Find margin.
  ||w|| = √(9+16) = √25 = 5
  Margin = 2/||w|| = 2/5 = 0.4

  Decision boundary: 3x₁ + 4x₂ - 1 = 0
  Positive margin: 3x₁ + 4x₂ - 1 = +1
  Negative margin: 3x₁ + 4x₂ - 1 = -1
```

### N2: Kernel Computation

```
x = [1, 2], z = [3, 1]

Linear:      K = xᵀz = 1×3 + 2×1 = 5
Poly (d=2):  K = (xᵀz + 1)² = (5+1)² = 36
RBF (γ=0.5): K = exp(-0.5×||x-z||²) = exp(-0.5×((1-3)²+(2-1)²))
             = exp(-0.5×5) = exp(-2.5) = 0.082
```

### N3: SVM Classification

```
Support vectors: sv₁=[2,3] y₁=+1 α₁=0.5, sv₂=[4,1] y₂=-1 α₂=0.5
Kernel: linear, b = -0.5

Classify x_new = [3, 2]:
  f(x) = α₁y₁K(sv₁,x) + α₂y₂K(sv₂,x) + b
       = 0.5×(+1)×(2×3+3×2) + 0.5×(-1)×(4×3+1×2) + (-0.5)
       = 0.5×12 + 0.5×(-14) + (-0.5)
       = 6 - 7 - 0.5 = -1.5
  sign(-1.5) = -1 → CLASS -1 ✅
```

[↑ Back to Top](#-svm--kernel-methods-theory--numerical--practice)

---

## 9. Cheat Sheet & Exam Hacks

```
┌─────────────────────────────────────────────────────────────┐
│              SVM & KERNELS CHEAT SHEET                      │
├──────────────────┬──────────────────────────────────────────┤
│ Margin           │ 2/||w||                                  │
│ Primal           │ min ½||w||² + CΣξᵢ s.t. yᵢ(wᵀx+b)≥1-ξᵢ   │
│ Dual             │ max Σαᵢ - ½ΣΣαᵢαⱼyᵢyⱼK(xᵢ,xⱼ)            │
│ Decision fn      │ f(x) = sign(ΣαᵢyᵢK(xᵢ,x) + b)            │
│ Support vectors  │ Points with αᵢ > 0 (on/inside margin)    │
│ Kernel trick     │ Replace xᵢᵀxⱼ with K(xᵢ,xⱼ)              │
│ RBF kernel       │ exp(-γ||x-z||²), most popular default    │
│ Large C          │ Narrow margin, fewer violations (overfit)│
│ Small C          │ Wide margin, more violations (underfit)  │
│ Large γ          │ Complex boundary (overfit)               │
│ Small γ          │ Smooth boundary (underfit)               │
│ SVR ε-tube       │ Errors within ε are free                 │
│ Kernel PCA       │ Non-linear PCA via kernel matrix         │
│ Mercer condition  │ Kernel matrix must be PSD               │
└──────────────────┴──────────────────────────────────────────┘

🧪 EXAM HACKS:
💡 Margin = 2/||w||. This is THE formula for margin.
💡 Dual form: data only in dot products → kernel trick possible
💡 Support vectors: ONLY points that determine the boundary
💡 RBF with large γ → memorize data → overfit (like small K in K-NN)
💡 C-γ tradeoff: use grid search + CV to tune both
💡 Kernel PCA: compute K matrix → eigendecompose → project
💡 In exam: show dual formulation, then plug in kernel
```

---

> **Nav:** [← Clustering](../Clustering/ml_kmeans_gmm_em_theory.md) | **SVM & Kernels** | [Neural Networks →](../Neural-Networks/ml_nn_mlp_bp_theory.md)

[↑ Back to Top](#-svm--kernel-methods-theory--numerical--practice)

---

*AI · ML · github.com/rpaut03l/TS-01*
