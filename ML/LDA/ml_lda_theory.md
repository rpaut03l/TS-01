# 📖 Linear Discriminant Analysis (LDA): THEORY + NUMERICAL + PRACTICE

### *Fisher's LDA · Projection · Multi-class · Dim Reduction*

> **Nav:** [← Foundations](../Foundations/ml_foundations_theory.md) | **LDA** | [Feature Selection →](../Feature-Selection-DimRed/ml_pca_ica_fs_theory.md)
>
> **Syllabus:** Fractal II — Discriminative Methods

---

## 🧠 MNEMONIC: **"FISH-SWIM"**

> **F**isher's criterion · **I**ncrease between-class · **S**catter matrices · **H**igh separation · **S**hrink within-class · **W**eight vector w · **I**nverse Sw · **M**ulti-class extension

---

## 📚 Table of Contents

| # | Topic | Jump |
|---|-------|------|
| 1 | What is LDA? | [§1](#1-what-is-lda) |
| 2 | Fisher's Criterion | [§2](#2-fishers-criterion) |
| 3 | Scatter Matrices | [§3](#3-scatter-matrices) |
| 4 | Optimal Projection | [§4](#4-optimal-projection) |
| 5 | Multi-class LDA | [§5](#5-multi-class-lda) |
| 6 | LDA vs PCA | [§6](#6-lda-vs-pca) |
| 7 | Numericals | [§7](#7-numericals) |
| 8 | Cheat Sheet & Exam Hacks | [§8](#8-cheat-sheet--exam-hacks) |

---

## 1. What is LDA?

### 👶 Easy Story
You have a pile of red and blue M&Ms on a table. You want to draw ONE line on the table and project (squish) all M&Ms onto that line. The BEST line is the one where red and blue groups are as FAR apart as possible, and each group is as TIGHT as possible. That's LDA: find the projection that maximizes class separation!

### Formal Definition
**LDA** finds a linear projection **w** that maximizes the ratio of between-class variance to within-class variance after projection.

```
GOAL: Project d-dimensional data onto 1D (or k-1 dimensions for k classes)
      such that classes are MAXIMALLY separated.

BEFORE LDA:                    AFTER LDA:
    ↑                              ↑
  • × • ×                       • • •
• × • × •    project onto w →   × × ×
  × • × •                       (well separated!)
    →                              →

KEY DIFFERENCE FROM PCA:
  PCA:  maximize TOTAL variance (ignores labels)
  LDA:  maximize BETWEEN-CLASS variance / WITHIN-CLASS variance (uses labels!)
```

[↑ Back to Top](#-linear-discriminant-analysis-lda-theory--numerical--practice)

---

## 2. Fisher's Criterion

```
FISHER'S LINEAR DISCRIMINANT:
──────────────────────────────
  Maximize: J(w) = (m₁ - m₂)² / (s₁² + s₂²)

  Where (after projection onto w):
    m₁ = wᵀμ₁     (projected mean of class 1)
    m₂ = wᵀμ₂     (projected mean of class 2)
    s₁² = Σ(wᵀxᵢ - m₁)² for xᵢ ∈ class 1  (projected scatter)
    s₂² = Σ(wᵀxᵢ - m₂)² for xᵢ ∈ class 2

  In matrix form:
    J(w) = wᵀ Sᵦ w / wᵀ Sᵥ w

    Sᵦ = between-class scatter matrix
    Sᵥ = within-class scatter matrix

  INTUITION:
    Numerator:   how FAR apart are the class means? (want BIG)
    Denominator: how SPREAD OUT is each class? (want SMALL)
    Maximize J = maximize separation / spread
```

[↑ Back to Top](#-linear-discriminant-analysis-lda-theory--numerical--practice)

---

## 3. Scatter Matrices

```
WITHIN-CLASS SCATTER (Sw):
──────────────────────────
  Sw = Σₖ Sₖ
  where Sₖ = Σ(xᵢ - μₖ)(xᵢ - μₖ)ᵀ  for xᵢ ∈ class k

  Measures: how spread out EACH class is internally
  Want this to be SMALL (tight clusters)

BETWEEN-CLASS SCATTER (Sb):
───────────────────────────
  Sb = Σₖ nₖ (μₖ - μ)(μₖ - μ)ᵀ
  where μ = overall mean, nₖ = size of class k

  Measures: how far apart the class MEANS are
  Want this to be BIG (well separated)

  For 2-class:  Sb = (μ₁ - μ₂)(μ₁ - μ₂)ᵀ

TOTAL SCATTER: St = Sw + Sb
```

[↑ Back to Top](#-linear-discriminant-analysis-lda-theory--numerical--practice)

---

## 4. Optimal Projection

```
SOLUTION:
──────────────────────────────
  w* = Sw⁻¹ (μ₁ - μ₂)       ← for 2-class case

  This is THE formula! Just compute:
  1. Mean of each class (μ₁, μ₂)
  2. Within-class scatter Sw
  3. Invert Sw
  4. Multiply by (μ₁ - μ₂)

  For MULTI-CLASS (K classes, d features):
    Solve generalized eigenvalue problem: Sb w = λ Sw w
    → Equivalently: Sw⁻¹ Sb w = λ w
    → Take top (K-1) eigenvectors (max K-1 useful dimensions)

CLASSIFICATION RULE (after projection):
  Project test point: y = wᵀ x
  Compare to threshold: t = wᵀ (μ₁ + μ₂) / 2
  If y > t → class 1, else → class 2
  (adjust if priors unequal: shift by log(P(ω₁)/P(ω₂)))
```

[↑ Back to Top](#-linear-discriminant-analysis-lda-theory--numerical--practice)

---

## 5. Multi-class LDA

```
K classes, d features:
  Sb: d × d matrix (between-class)
  Sw: d × d matrix (within-class)
  
  rank(Sb) ≤ K - 1 (at most K-1 useful directions)
  
  → LDA projects from d dimensions to at most K-1 dimensions
  → Solve Sw⁻¹ Sb w = λ w → take top K-1 eigenvectors
  
EXAMPLE: 3 classes in 10D → LDA gives at most 2 projection axes
```

[↑ Back to Top](#-linear-discriminant-analysis-lda-theory--numerical--practice)

---

## 6. LDA vs PCA

```
┌────────────────────┬────────────────────┬────────────────────┐
│ Feature            │ PCA                │ LDA                │
├────────────────────┼────────────────────┼────────────────────┤
│ Supervised?        │ No (unsupervised)  │ Yes (uses labels)  │
│ Objective          │ Max total variance │Max class separation│
│ Output dims        │ Up to d            │ At most K-1        │
│ Best for           │ Visualization      │ Classification     │
│ Scatter used       │ Total covariance   │ Sb / Sw ratio      │
│ Assumes            │ Nothing about y    │ Gaussian classes   │
│ Works when         │ No labels available│ Labels available   │
└────────────────────┴────────────────────┴────────────────────┘
```

[↑ Back to Top](#-linear-discriminant-analysis-lda-theory--numerical--practice)

---

## 7. Numericals

### N1: 2-Class LDA (2D → 1D)

```
Class 1: x₁=[4,2], x₂=[2,4], x₃=[2,3], x₄=[3,6], x₅=[4,4]
Class 2: x₆=[9,10], x₇=[6,8], x₈=[9,5], x₉=[8,7], x₁₀=[10,8]

STEP 1: Class means
  μ₁ = [15/5, 19/5] = [3.0, 3.8]
  μ₂ = [42/5, 38/5] = [8.4, 7.6]

STEP 2: Within-class scatter Sw = S₁ + S₂
  S₁ = Σ(xᵢ - μ₁)(xᵢ - μ₁)ᵀ for class 1
  (4-3)²=1, (2-3)²=1, (2-3)²=1, (3-3)²=0, (4-3)²=1 → Σ=4 (top-left)
  similarly compute all entries...
  
  S₁ = [4.0  0.0]    S₂ = [10.8  2.4]
       [0.0  8.8]         [2.4   13.2]
  
  Sw = S₁ + S₂ = [14.8  2.4]
                   [2.4  22.0]

STEP 3: Sw⁻¹
  det(Sw) = 14.8×22.0 - 2.4×2.4 = 325.6 - 5.76 = 319.84
  Sw⁻¹ = (1/319.84) × [22.0  -2.4] = [0.0688  -0.0075]
                        [-2.4  14.8]   [-0.0075  0.0463]

STEP 4: w* = Sw⁻¹ (μ₁ - μ₂)
  μ₁ - μ₂ = [-5.4, -3.8]
  w* = [0.0688  -0.0075] × [-5.4] = [0.0688×(-5.4) + (-0.0075)×(-3.8)]
       [-0.0075  0.0463]   [-3.8]   [(-0.0075)×(-5.4) + 0.0463×(-3.8)]
     = [-0.372 + 0.029] = [-0.343]
       [0.041 - 0.176]    [-0.135]

  w* = [-0.343, -0.135] (direction of max separation)
  normalize: ||w|| = √(0.343² + 0.135²) = 0.369
  w_unit = [-0.930, -0.366]

STEP 5: Classification threshold
  t = wᵀ(μ₁ + μ₂)/2 = [-0.930, -0.366]ᵀ × [5.7, 5.7]
    = -0.930×5.7 + (-0.366)×5.7 = -5.301 - 2.086 = -7.387

  New point x_new = [5, 5]:
  y = wᵀx_new = -0.930×5 + (-0.366)×5 = -6.480
  y = -6.480 > t = -7.387 → CLASS 1 ✅
```

### N2: Compute Fisher's J

```
Given projections: Class 1 projected: [2.1, 1.8, 2.3]  Class 2: [5.2, 4.8, 5.5]

  m₁ = (2.1+1.8+2.3)/3 = 2.067
  m₂ = (5.2+4.8+5.5)/3 = 5.167
  s₁² = (2.1-2.067)²+(1.8-2.067)²+(2.3-2.067)² = 0.001+0.071+0.054 = 0.127
  s₂² = (5.2-5.167)²+(4.8-5.167)²+(5.5-5.167)² = 0.001+0.135+0.111 = 0.247

  J = (m₁ - m₂)² / (s₁² + s₂²) = (2.067-5.167)² / (0.127+0.247)
    = (-3.1)² / 0.374 = 9.61 / 0.374 = 25.69

  HIGH J = good separation! ✅
```

[↑ Back to Top](#-linear-discriminant-analysis-lda-theory--numerical--practice)

---

## 8. Cheat Sheet & Exam Hacks

```
┌──────────────────────────────────────────────────────────────┐
│                    LDA CHEAT SHEET                           │
├──────────────────┬───────────────────────────────────────────┤
│ Goal             │ Max between-class / within-class variance │
│ Formula (2-class)│ w* = Sw⁻¹(μ₁ - μ₂)                        │
│ Fisher's J       │ J = (m₁-m₂)² / (s₁²+s₂²)                  │
│ Sw               │ Σₖ Σᵢ∈k (xᵢ-μₖ)(xᵢ-μₖ)ᵀ                    │
│ Sb               │ Σₖ nₖ(μₖ-μ)(μₖ-μ)ᵀ                          │
│ Multi-class dims │ At most K-1 (K=number of classes)         │
│ LDA vs PCA       │ LDA uses labels, PCA doesn't              │
│ Assumption       │ Classes are Gaussian with same covariance │
│ Classification   │ Project, compare to threshold t           │
│ Threshold        │ t = wᵀ(μ₁+μ₂)/2 (equal priors)            │
└──────────────────┴───────────────────────────────────────────┘

🧪 EXAM HACKS:
💡 w* = Sw⁻¹(μ₁ - μ₂) is THE most important formula
💡 Fisher's J = class separation / class spread (higher = better)
💡 LDA projects to K-1 dims max. 3 classes → 2D max.
💡 If Sw is singular (det=0), use pseudo-inverse or PCA first
💡 LDA assumes same covariance for both classes (QDA relaxes this)
💡 In exam: show Sw computation step by step, don't skip!
```

---

> **Nav:** [← Foundations](../Foundations/ml_foundations_theory.md) | **LDA** | [Feature Selection →](../Feature-Selection-DimRed/ml_pca_ica_fs_theory.md)

[↑ Back to Top](#-linear-discriminant-analysis-lda-theory--numerical--practice)

---

*AI · ML · github.com/rpaut03l/TS-01*
