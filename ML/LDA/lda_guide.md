# 📊 Linear Discriminant Analysis (LDA) — Complete Study Guide
### Parts 1 & 2 Combined | LDA Details | Machine Learning (ML)..

> **"LDA is like PCA, but it has eyes — it can SEE the class labels!"**

---

## 📚 Table of Contents

| # | Section |
|---|---------|
| 1 | [The Real-World Problem LDA Solves](#1-the-real-world-problem-lda-solves) |
| 2 | [What is LDA?](#2-what-is-lda) |
| 3 | [LDA vs PCA — The Core Difference](#3-lda-vs-pca--the-core-difference) |
| 4 | [Visual Intuition — Step by Step](#4-visual-intuition--step-by-step) |
| 5 | [All Notations & Symbols Decoded](#5-all-notations--symbols-decoded) |
| 6 | [Part 1 — Fisher's LDA: The Math](#6-part-1--fishers-lda-the-math) |
| 7 | [Part 2 — The Full Algorithm (2 Classes)](#7-part-2--the-full-algorithm-2-classes) |
| 8 | [Full Worked Example (Flower Classification)](#8-full-worked-example-flower-classification) |
| 9 | [LDA for 3+ Categories](#9-lda-for-3-categories) |
| 10 | [LDA as a Classifier + Decision Rule](#10-lda-as-a-classifier--decision-rule) |
| 11 | [Connection to Other Classifiers](#11-connection-to-other-classifiers) |
| 12 | [ASCII Diagrams — Visual Reference](#12-ascii-diagrams--visual-reference) |
| 13 | [Cheatsheet](#13-cheatsheet) |
| 14 | [Mnemonics & Memory Tricks](#14-mnemonics--memory-tricks) |
| 15 | [Common Mistakes & Fixes](#15-common-mistakes--fixes) |
| 16 | [Quick Q&A for Exam](#16-quick-qa-for-exam) |

---

## 1. The Real-World Problem LDA Solves

### 🏥 Story: Cancer Drug Prediction (Part 2 — Slides 1–24)

A cancer drug:
- ✅ **Works** for some patients
- ❌ **Makes worse** other patients

**Goal:** Can we predict *who* should take it using gene expression data?

```
STEP 1 — One Gene (1D number line):

Fewer Transcripts ←————————————————————→ More Transcripts

🟢🟢🟢🟢  🔴  🟢  🔴🔴  🔴  🔴🔴

🟢 = Drug works  |  🔴 = Drug does NOT work

PROBLEM: There's an overlap zone — no clean cutoff!
```

```
STEP 2 — Two Genes (2D plot):

Gene Y ↑
       |  🟢         🔴  🔴🔴
       |     🟢         🔴
       |  🟢🟢     🔴      🔴
       └────────────────────────→ Gene X

With a DIAGONAL line we separate them much better! ✅
```

```
STEP 3 — Three Genes (3D space):

Need a PLANE instead of a line to separate groups.
4+ genes? Can't draw it — need math!

→ This is exactly where LDA steps in.
```

---

## 2. What is LDA?

**Linear Discriminant Analysis (LDA)** is a **supervised** dimensionality reduction and classification technique that:

1. Takes high-dimensional data (e.g. 10,000 genes per patient)
2. Finds new **axes** that **maximize separation** between known categories
3. **Projects** data onto those axes (reduces dimensions)
4. Allows **classification** in lower-dimensional space

### In one sentence:
> **LDA finds the direction(s) in feature space where known classes are most separated.**

---

## 3. LDA vs PCA — The Core Difference

```
PCA:  "Which direction has the most SPREAD/VARIANCE?"
LDA:  "Which direction best SEPARATES the classes?"

                     Unsupervised ←———→ Supervised
                     (no labels)        (uses labels)
                         ↑                   ↑
                        PCA                 LDA
```

| Feature | PCA | LDA |
|---|---|---|
| Full Name | Principal Component Analysis | Linear Discriminant Analysis |
| Type | Unsupervised | Supervised |
| Needs class labels? | ❌ No | ✅ Yes |
| Goal | Maximize **variance** | Maximize **class separation** |
| Axes named | PC1, PC2, … (by variance) | LD1, LD2, … (by separation) |
| Max axes | up to p (# features) | up to C−1 (# classes − 1) |

### Why PCA fails for classification:

```
PCA result on 3-class data:     LDA result on same data:
(PC1 vs PC2)                    (LD1 vs LD2)

🔵🔴🟢🔵🔴🟢 (mixed!)          🔵🔵🔵   🔴🔴🔴   🟢🟢🟢
                                  ↑ clean clusters! ✅

PCA picked directions of most   LDA picked directions that
overall variance — these may    actually pull classes apart.
have NOTHING to do with class
boundaries.
```

---

## 4. Visual Intuition — Step by Step

### 🎯 The Two Goals of LDA — "PULL APART, PACK TOGETHER"

```
GOAL 1 — PULL the class means APART (Big Gap)

     μ_green                       μ_red
        ↓                             ↓
   🟢🟢🟢🟢  ←——— d (big!) ———→  🔴🔴🔴🔴

   Maximize d² = (μ₁ − μ₂)²    ← WANT THIS LARGE ↑


GOAL 2 — PACK each class TOGETHER (Small Mess)

   BAD (large scatter = overlap):
   🟢   🟢   🟢   🔴   🟢   🔴   🔴
           ↑ spread out = they mix!

   GOOD (small scatter = clear gap):
   🟢🟢🟢🟢🟢           🔴🔴🔴🔴🔴
       ↑ tight             ↑ tight

   Minimize s² (scatter) within each class   ← WANT THIS SMALL ↓
```

### 🏆 The LDA Objective Formula (2 Classes)

```
         (μ₁ − μ₂)²            Big Gap
ratio = ──────────────  =  ─────────────────
         s₁² + s₂²           Small Mess

MAXIMIZE this ratio → best separating axis found!
```

### "The Shadow Play" Analogy

```
Imagine shining a flashlight at green and red balls on a table.

LDA asks: "At what angle should I shine the flashlight so the
SHADOWS of the two groups are FAR APART and each group's
shadows are TIGHTLY CLUSTERED?"

        Flashlight (angle = w*)
             ↓
Table:     🟢🟢🟢   🔴🔴🔴

Wall:   🟢🟢🟢━━━━━━━━🔴🔴🔴
                 ↑ Big gap!
```

---

## 5. All Notations & Symbols Decoded

| Symbol | Name | Meaning | Memory Trick |
|---|---|---|---|
| **μₖ** (mu) | Class mean vector | Average position of class k | "Mu = Middle of class" |
| **m̃ₖ** | Projected class mean | Mean after projection onto w | Tilde = "transformed" |
| **s²** | Scatter | Within-class spread/variance | "s = Spread Squared" |
| **N₁, N₂** | Class sizes | # samples in each class | "N = Number" |
| **Sᵂ** | Within-class scatter matrix | Total spread inside all classes | **W** = **W**ithin |
| **Sʙ** | Between-class scatter matrix | Spread between class means | **B** = **B**etween |
| **w** | Direction vector | The LDA projection axis | "w = Where to project" |
| **w*** | Optimal w | The best LDA direction (solution) | "*" = optimal |
| **d** | Distance | Difference between class means | d = distance |
| **J(w)** | Fisher criterion | The ratio we maximize | "J = Judge how good" |
| **LD1, LD2** | Linear Discriminants | New axes created by LDA | LD = Linear Discriminant |
| **Σ** (capital) | Covariance matrix | Spread in all directions | "Sigma = Spread matrix" |
| **xₙ** | Data point n | One observation/sample | n = nth sample |
| **ᵀ** | Transpose | Flip rows ↔ columns | "T = Turn around" |
| **⁻¹** | Matrix inverse | Undoes a matrix (like ÷) | "-1 = reverse" |
| **C** | # Classes | Number of categories | C = Categories |
| **p** | # Features | Number of dimensions/genes | p = properties |
| **λ** (lambda) | Eigenvalue | How good an LDA axis is | "λ = Level of goodness" |

---

## 6. Part 1 — Fisher's LDA: The Math

### 6.1 The Projection Concept

```
Each data point x gets PROJECTED onto direction w:

   Projected value y = wᵀx  (w-transpose times x)

What this means:
   w = a direction arrow in p-dimensional space
   wᵀx = dot product = how far x lies along w
   y = a single number (the 1D coordinate)

Example (2D data):
   w = [0.8, 0.6]    ← LDA direction
   x = [5.0, 3.0]    ← one data point

   y = wᵀx = (0.8 × 5.0) + (0.6 × 3.0)
           = 4.0 + 1.8
           = 5.8       ← this point's projected value
```

### 6.2 Class Means

```
Compute the average of each class:

   μₖ = (1/Nₖ) × Σ xₙ   for all n in class k
                n∈Cₖ

Example:
   Class 1 data: x₁=[5.1, 3.5], x₂=[4.9, 3.0]
   μ₁ = ([5.1,3.5] + [4.9,3.0]) / 2 = [5.0, 3.25]

After projection onto w:
   m̃₁ = wᵀμ₁    (projected mean of class 1)
   m̃₂ = wᵀμ₂    (projected mean of class 2)

   We want |m̃₂ − m̃₁| to be LARGE
```

### 6.3 Within-Class Scatter Matrices

```
For class k, the scatter matrix captures internal spread:

   Sₖ = Σ (xₙ − μₖ)(xₙ − μₖ)ᵀ
       n∈Cₖ

Reading step by step:
   For every point xₙ in class k:
     1. Subtract class mean:  diff = xₙ − μₖ
     2. Outer product:        diff × diffᵀ  →  gives a p×p matrix
     3. Add all these matrices together

Example (1 point contribution):
   xₙ = [5.1, 3.5],  μₖ = [5.0, 3.25]
   diff = [0.1, 0.25]

   diff × diffᵀ = [0.1 ] × [0.1, 0.25] = [0.01   0.025 ]
                  [0.25]                  [0.025  0.0625]

Total within-class scatter (both classes combined):
   Sᵂ = S₁ + S₂
```

### 6.4 Between-Class Scatter Matrix

```
Captures how far APART the two class means are:

   Sʙ = (μ₂ − μ₁)(μ₂ − μ₁)ᵀ

Example:
   μ₁ = [5.0, 3.25],  μ₂ = [6.7, 3.2]
   diff = [1.7, −0.05]

   Sʙ = [1.7  ] × [1.7, −0.05] = [2.89    −0.085]
        [−0.05]                   [−0.085  0.0025]
```

### 6.5 Fisher's Criterion — The Formula

```
         wᵀSʙw
J(w) = ─────────
         wᵀSᵂw

Numerator   wᵀSʙw = projected between-class spread  → WANT BIG  ↑
Denominator wᵀSᵂw = projected within-class spread   → WANT SMALL ↓

Maximize J(w) to find the best w!
```

### 6.6 The Closed-Form Solution

```
LDA has a beautiful closed-form answer — no training loop needed!

   w* = Sᵂ⁻¹ (μ₂ − μ₁)

Reading it:
   Sᵂ⁻¹          = inverse of within-class scatter matrix
   (μ₂ − μ₁)     = vector pointing from class 1 to class 2
   Multiply them  = optimal projection direction

Memory: "Inverse Within, times Mean Difference"
         Sᵂ⁻¹   ×   (μ₂ − μ₁)
```

---

## 7. Part 2 — The Full Algorithm (2 Classes)

```
INPUT:   Training data with class labels
OUTPUT:  LDA direction w*, projected data

┌──────────────────────────────────────────────────────────┐
│  STEP 1 ── Compute class means                          │
│                                                          │
│  μ₁ = (1/N₁) Σ xₙ   for all n in class 1               │
│  μ₂ = (1/N₂) Σ xₙ   for all n in class 2               │
└──────────────────────────────────────────────────────────┘
                           ↓
┌──────────────────────────────────────────────────────────┐
│  STEP 2 ── Compute within-class scatter matrices        │
│                                                          │
│  S₁ = Σ (xₙ−μ₁)(xₙ−μ₁)ᵀ    for n in class 1           │
│  S₂ = Σ (xₙ−μ₂)(xₙ−μ₂)ᵀ    for n in class 2           │
│  Sᵂ = S₁ + S₂                                           │
└──────────────────────────────────────────────────────────┘
                           ↓
┌──────────────────────────────────────────────────────────┐
│  STEP 3 ── Compute between-class scatter matrix         │
│                                                          │
│  Sʙ = (μ₂ − μ₁)(μ₂ − μ₁)ᵀ                             │
└──────────────────────────────────────────────────────────┘
                           ↓
┌──────────────────────────────────────────────────────────┐
│  STEP 4 ── Find optimal direction w*                    │
│                                                          │
│  w* = Sᵂ⁻¹ (μ₂ − μ₁)                                   │
└──────────────────────────────────────────────────────────┘
                           ↓
┌──────────────────────────────────────────────────────────┐
│  STEP 5 ── Project all data                             │
│                                                          │
│  yₙ = (w*)ᵀ xₙ   for every training point xₙ           │
│                                                          │
│  Also project class means:                              │
│  m̃₁ = (w*)ᵀ μ₁                                         │
│  m̃₂ = (w*)ᵀ μ₂                                         │
└──────────────────────────────────────────────────────────┘
                           ↓
┌──────────────────────────────────────────────────────────┐
│  STEP 6 ── Classify new point x_new                     │
│                                                          │
│  y_new = (w*)ᵀ x_new                                    │
│  threshold t = (m̃₁ + m̃₂) / 2                           │
│                                                          │
│  If y_new ≥ t  →  class 2                               │
│  If y_new < t  →  class 1                               │
└──────────────────────────────────────────────────────────┘
```

### The FISH Mnemonic — Algorithm Steps
```
F ── Find class means       (Step 1: μ₁, μ₂)
I ── Internal scatter       (Step 2: Sᵂ = S₁ + S₂)
S ── Separation scatter     (Step 3: Sʙ = (μ₂−μ₁)(μ₂−μ₁)ᵀ)
H ── Hit best direction     (Step 4: w* = Sᵂ⁻¹(μ₂−μ₁))
```

---

## 8. Full Worked Example (Flower Classification)

### Problem Setup

```
Task: Classify a flower as Setosa or Versicolor

Training Data:
Class         Sepal Length    Sepal Width
──────────────────────────────────────────
Setosa         5.1             3.5
Setosa         4.9             3.0
Versicolor     7.0             3.2
Versicolor     6.4             3.2

Test point:  x_new = [5.9, 3.0]
```

---

### STEP 1 — Compute Class Means

```
Setosa (Class 1):
   μ₁ = ([5.1, 3.5] + [4.9, 3.0]) / 2
      = [10.0, 6.5] / 2
      = [5.0, 3.25]   ← Setosa center ✓

Versicolor (Class 2):
   μ₂ = ([7.0, 3.2] + [6.4, 3.2]) / 2
      = [13.4, 6.4] / 2
      = [6.7, 3.2]    ← Versicolor center ✓
```

---

### STEP 2 — Compute Within-Class Scatter Sᵂ

```
For Setosa:
  x₁ = [5.1, 3.5],  diff₁ = x₁ − μ₁ = [0.1, 0.25]
  x₂ = [4.9, 3.0],  diff₂ = x₂ − μ₁ = [−0.1, −0.25]

  diff₁ × diff₁ᵀ = [0.01   0.025 ]     diff₂ × diff₂ᵀ = [0.01   0.025 ]
                   [0.025  0.0625]                        [0.025  0.0625]

  S₁ = [0.02   0.05  ]
       [0.05   0.125 ]

For Versicolor:
  x₃ = [7.0, 3.2],  diff₃ = [0.3, 0]
  x₄ = [6.4, 3.2],  diff₄ = [−0.3, 0]

  S₂ = [0.18  0]
       [0     0]

Total within-class scatter:
  Sᵂ = S₁ + S₂ = [0.02+0.18   0.05+0] = [0.20   0.05 ]
                  [0.05+0      0.125 ]   [0.05   0.125]
```

---

### STEP 3 — Compute Between-Class Scatter Sʙ

```
Mean difference:
  μ₂ − μ₁ = [6.7−5.0, 3.2−3.25] = [1.7, −0.05]

  Sʙ = [1.7  ] × [1.7, −0.05] = [2.89    −0.085]
       [−0.05]                   [−0.085  0.0025]
```

---

### STEP 4 — Find w* = Sᵂ⁻¹ (μ₂ − μ₁)

```
Sᵂ = [0.20   0.05 ]
     [0.05   0.125]

Formula for 2×2 inverse:
  For matrix [a b], inverse = 1/(ad−bc) × [ d  −b]
             [c d]                         [−c   a]

  det(Sᵂ) = (0.20 × 0.125) − (0.05 × 0.05)
           = 0.025 − 0.0025 = 0.0225

  Sᵂ⁻¹ = (1/0.0225) × [ 0.125  −0.05]
                        [−0.05    0.20]

       = [ 5.556  −2.222]
         [−2.222   8.889]

Now compute w* = Sᵂ⁻¹ × (μ₂ − μ₁):
  
  w*[1] = (5.556 × 1.7) + (−2.222 × −0.05) = 9.445 + 0.111 = 9.556
  w*[2] = (−2.222 × 1.7) + (8.889 × −0.05) = −3.777 − 0.444 = −4.221

  w* = [9.556, −4.221]   ← This is the best LDA direction ✓
```

---

### STEP 5 — Project Means and Test Point

```
Project class means:
  m̃₁ = (w*)ᵀ μ₁ = (9.556 × 5.0) + (−4.221 × 3.25) = 47.78 − 13.72 = 34.06
  m̃₂ = (w*)ᵀ μ₂ = (9.556 × 6.7) + (−4.221 × 3.2)  = 64.03 − 13.51 = 50.52

Decision threshold:
  t = (m̃₁ + m̃₂) / 2 = (34.06 + 50.52) / 2 = 42.29

Project test point x_new = [5.9, 3.0]:
  y_new = (9.556 × 5.9) + (−4.221 × 3.0)
        = 56.38 − 12.66
        = 43.72
```

---

### STEP 6 — Classify

```
Projected 1D number line:

  34.06        42.29        43.72   50.52
    |            |            |       |
    ↓            ↓            ↓       ↓
   m̃₁         threshold    y_new    m̃₂
 (Setosa)                (test pt) (Versicolor)

  y_new (43.72) > threshold (42.29)

  → Classified as VERSICOLOR (Class 2) ✅
```

### Memory Technique — "MSPC"
```
M ── Means         (compute μ₁, μ₂)
S ── Scatter       (compute Sᵂ)
P ── Project       (find w*, compute y)
C ── Classify      (compare to threshold)
```

---

## 9. LDA for 3+ Categories

### How Many LDA Axes?

```
Rule:  # LDA axes = min(C−1,  p)
                        ↑      ↑
                     # classes  # features

Examples:
  2 classes,  1000 genes  →  1 LDA axis  (LD1 only)
  3 classes,  1000 genes  →  2 LDA axes  (LD1, LD2)
  5 classes,  1000 genes  →  4 LDA axes  (LD1 ... LD4)
 10 classes,  1000 genes  →  9 LDA axes

Memory: "One Less Than the Team Count"
```

### Why? — Geometric Reasoning

```
2 class means  →  1 line separates them  →  need 1 axis
3 class means  →  1 plane separates them →  need 2 axes
4 class means  →  3D space needed        →  need 3 axes

   2 points define a line      →  1 axis (LD1)
   3 points define a plane     →  2 axes (LD1, LD2)
   N points define (N−1)D space → N−1 axes
```

### Modified Between-Class Scatter for 3+ Classes

```
Step 1: Find OVERALL mean μ̄ (mean of ALL data, all classes):
  μ̄ = (1/N) Σₖ Nₖ μₖ

Step 2: Between-class scatter becomes:
  Sʙ = Σₖ Nₖ (μₖ − μ̄)(μₖ − μ̄)ᵀ

  where: k  = class index
         Nₖ = # points in class k
         μₖ = mean of class k
         μ̄  = overall mean

Step 3: Within-class scatter stays the same:
  Sᵂ = Σₖ Σ(n∈Cₖ) (xₙ − μₖ)(xₙ − μₖ)ᵀ

Step 4: Solve the GENERALIZED EIGENVALUE PROBLEM:
  Sʙ w = λ Sᵂ w

  → Eigenvectors w  = LDA axes (LD1, LD2, ...)
  → Eigenvalues  λ  = how good each axis is at separating
  → Sort by λ: largest λ → LD1 (best axis)
```

### The Extended Formula (3 Classes)

```
            d₁² + d₂² + d₃²
  J    =  ─────────────────────
            s₁² + s₂² + s₃²

  where dₖ = distance of class k mean from OVERALL mean μ̄
        sₖ² = within-class scatter of class k

  Same idea: Big numerator (far means), small denominator (tight clusters)
```

### Visual for 3 Classes

```
Gene Y ↑
       │  🔵🔵🔵
       │   🔵🔵      🔴🔴🔴
       │                🔴🔴
       │  🟢🟢
       │   🟢🟢
       └─────────────────────→ Gene X

                 ↓  LDA projects to 2D (LD1 vs LD2)

LD2 ↑
    │      🔵🔵🔵
    │       🔵🔵
    │
    │  🟢🟢         🔴🔴🔴
    │   🟢🟢          🔴🔴
    └────────────────────────→ LD1

Three clean clusters! 10,000 genes → 2 axes ✅
```

---

## 10. LDA as a Classifier + Decision Rule

### Decision Rule (2 Classes)

```
Given new point x:

   1. Compute:    y = wᵀx               (project onto LDA axis)
   2. Compute:    t = (m̃₁ + m̃₂) / 2    (midpoint threshold)
   3. Decide:
       y ≥ t  →  class 2
       y < t  →  class 1
```

### LDA Assumptions

```
For LDA to work best:
  1. Classes follow Normal (Gaussian) distributions
  2. All classes share the SAME covariance matrix (Σ₁ = Σ₂ = ... = Σ)

If assumption 2 is violated:
  → Use Quadratic Discriminant Analysis (QDA)
  → Each class gets its OWN covariance matrix
  → Decision boundary becomes CURVED (quadratic) instead of a straight line
```

---

## 11. Connection to Other Classifiers

```
Distance-from-Means Classifier
│
│  When Σ = I (identity matrix, spherical data):
│  LDA reduces to → classify to nearest class centroid
│
│  f(x) = ‖μ₋ − x‖² − ‖μ₊ − x‖²
│  If f(x) > 0  → class +1
│  If f(x) < 0  → class −1
│
│  All produce same form:  f(x) = wᵀx + b
│                                  ↑
│                      Linear boundary (hyperplane)
│
├─ Distance from Means:  w = μ₊ − μ₋         (closed-form)
├─ Perceptron:           w updated iteratively (any separator)
├─ SVM:                  w = maximum margin   (best separator)
└─ LDA:                  w = Sᵂ⁻¹(μ₂−μ₁)    (best separation ratio)
```

---

## 12. ASCII Diagrams — Visual Reference

### Diagram A — BAD vs GOOD Projection

```
ORIGINAL 2D DATA:
Gene Y ↑
     5 │  🟢              🔴  🔴
     4 │     🟢         🔴
     3 │  🟢  🟢     🔴      🔴
       └──────────────────────────→ Gene X
            1   2   3   4   5   6

BAD: Drop Gene Y, project onto Gene X only:
  🟢🟢🟢 🔴 🟢 🔴🔴 🔴  ← MIXED, useless!

LDA: Project onto diagonal w* axis:
  🟢🟢🟢🟢🟢   🔴🔴🔴🔴🔴
  ←class 1→   ←class 2→   ← PERFECT! ✅
```

---

### Diagram B — Scatter Matrices Visualized

```
WITHIN-CLASS SCATTER Sᵂ (want SMALL):

  Class 1 (tight = good ✓)      Class 2 (tight = good ✓)
       🟢🟢                            🔴🔴
        🟢🟢                             🔴🔴
        ←s²→                            ←s²→
       small!                           small!


BETWEEN-CLASS SCATTER Sʙ (want LARGE):

  μ₁ ●                                    ● μ₂
       ←──────────────── d ────────────────→
                      LARGE gap! ✓

FISHER'S RATIO = Sʙ / Sᵂ = BIG / small = MAXIMIZE ✅
```

---

### Diagram C — LDA Full Pipeline

```
10,000-GENE DATA (patients)
         │
         ▼
 ┌───────────────────┐
 │  Compute μ₁, μ₂  │  ← Step 1: Class means
 └───────────────────┘
         │
         ▼
 ┌───────────────────┐
 │  Compute Sᵂ, Sʙ  │  ← Step 2 & 3: Scatter matrices
 └───────────────────┘
         │
         ▼
 ┌───────────────────┐
 │  w* = Sᵂ⁻¹(Δμ)   │  ← Step 4: Best direction
 └───────────────────┘
         │
         ▼
 ┌───────────────────┐
 │  y = wᵀx         │  ← Step 5: Project all data
 └───────────────────┘
         │
         ▼
 1D (or 2D) PLOT — Easy to classify! ✅
```

---

### Diagram D — Why BOTH Criteria Matter

```
Case 1: Big d, but BIG scatter → FAIL ❌

  🟢   🟢  🟢 🔴🔴 🟢 🔴  🔴   🔴
       ↑ high scatter = overlap despite large mean distance


Case 2: Small scatter, but SMALL d → FAIL ❌

  🟢🟢🟢🟢🔴🔴🔴🔴
          ↑ too close together


Case 3: Large d AND small scatter → PERFECT ✅

  🟢🟢🟢🟢🟢     ←gap→     🔴🔴🔴🔴🔴
  Small scatter ✓         Large gap ✓
```

---

## 13. Cheatsheet

```
╔══════════════════════════════════════════════════════════════════╗
║                     LDA COMPLETE CHEATSHEET                     ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  WHAT:  Supervised dimensionality reduction + classification     ║
║  WHY:   Maximize class separation (not just variance like PCA)   ║
║                                                                  ║
╠══════════════════════════════════════════════════════════════════╣
║  CORE FORMULA — Fisher's Criterion:                             ║
║                                                                  ║
║          wᵀ Sʙ w         Between-class scatter                  ║
║  J(w) = ──────────  =  ──────────────────────                   ║
║          wᵀ Sᵂ w         Within-class scatter                   ║
║                                                                  ║
║  MAXIMIZE J(w) → find the best projection direction w*          ║
║                                                                  ║
╠══════════════════════════════════════════════════════════════════╣
║  CLOSED-FORM SOLUTION:                                          ║
║                                                                  ║
║  w* = Sᵂ⁻¹ (μ₂ − μ₁)          [2-class case]                   ║
║                                                                  ║
║  General: solve  Sʙ w = λ Sᵂ w  [eigenvalue problem]            ║
║                                                                  ║
╠══════════════════════════════════════════════════════════════════╣
║  SCATTER MATRICES:                                              ║
║                                                                  ║
║  Within:   Sᵂ = S₁ + S₂                                        ║
║            Sₖ = Σ(xₙ−μₖ)(xₙ−μₖ)ᵀ                              ║
║                                                                  ║
║  Between:  Sʙ = (μ₂−μ₁)(μ₂−μ₁)ᵀ              [2-class]        ║
║            Sʙ = Σₖ Nₖ(μₖ−μ̄)(μₖ−μ̄)ᵀ           [multi-class]  ║
║                                                                  ║
╠══════════════════════════════════════════════════════════════════╣
║  NUMBER OF LDA AXES:                                            ║
║                                                                  ║
║  # axes = min(C−1,  p)                                          ║
║  C = # classes       p = # features                             ║
║                                                                  ║
║  2 classes → 1 axis   │  3 classes → 2 axes                     ║
║  5 classes → 4 axes   │  N classes → N−1 axes                   ║
║                                                                  ║
╠══════════════════════════════════════════════════════════════════╣
║  CLASSIFICATION RULE:                                           ║
║                                                                  ║
║  y = wᵀ x_new                                                   ║
║  t = (m̃₁ + m̃₂) / 2      ← midpoint threshold                  ║
║  y ≥ t  →  class 2                                              ║
║  y < t  →  class 1                                              ║
║                                                                  ║
╠══════════════════════════════════════════════════════════════════╣
║  2×2 MATRIX INVERSE (exam helper):                              ║
║                                                                  ║
║  A = [a b]     A⁻¹ = ──1──  × [ d  −b]                         ║
║      [c d]           ad−bc     [−c   a]                         ║
║                                                                  ║
║  det(A) = ad − bc                                               ║
║                                                                  ║
╠══════════════════════════════════════════════════════════════════╣
║  LDA vs PCA:                                                    ║
║                                                                  ║
║  PCA:  Unsupervised │ max variance  │ no labels   │ any # axes  ║
║  LDA:  Supervised   │ max separation│ needs labels│ C−1 axes    ║
║                                                                  ║
╠══════════════════════════════════════════════════════════════════╣
║  ASSUMPTIONS:                                                   ║
║  1. Classes are Gaussian (normally distributed)                 ║
║  2. Equal covariance across classes (Σ₁ = Σ₂)                  ║
║     [If violated → use QDA instead]                             ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## 14. Mnemonics & Memory Tricks

### 🧠 The Big 7 Mnemonics

---

#### 1. "PULL APART, PACK TOGETHER" — LDA's Two Goals
```
PULL the class means APART  →  maximize Sʙ (between-class scatter)
PACK each class TOGETHER    →  minimize Sᵂ (within-class scatter)

Ratio = PULL APART / PACK TOGETHER = Sʙ / Sᵂ
```

---

#### 2. "PCA is BLIND, LDA can SEE" — The Key Difference
```
PCA is BLIND → doesn't see class labels  → unsupervised
LDA can SEE  → uses class labels          → supervised

"Blind PCA wanders; Seeing LDA separates."
```

---

#### 3. "BIG GAP, SMALL MESS" — The Ideal LDA Outcome
```
BIG GAP  =  large distance between class means  →  numerator big
SMALL MESS = small scatter within each class     →  denominator small

BIG GAP / SMALL MESS  →  best J(w) value!
```

---

#### 4. "ONE LESS AXIS" — Number of LDA Axes
```
C classes → C−1 LDA axes

2 classes  →  1 axis (LD1)
3 classes  →  2 axes (LD1, LD2)
10 classes →  9 axes

"Count the classes, subtract one — that's your axes done!"
```

---

#### 5. "FISH" — The LDA Algorithm
```
F ── Find class means       μ₁, μ₂
I ── Internal scatter       Sᵂ = S₁ + S₂
S ── Separation scatter     Sʙ = (μ₂−μ₁)(μ₂−μ₁)ᵀ
H ── Hit best direction     w* = Sᵂ⁻¹(μ₂−μ₁)
```

---

#### 6. "MSPC" — Classification Steps
```
M ── Means          compute μ₁, μ₂
S ── Scatter        compute Sᵂ, w*
P ── Project        y = wᵀx
C ── Classify       compare y to threshold t
```

---

#### 7. "Sᵂ for Within, Sʙ for Between" — Scatter Matrix Names
```
Sᵂ → W = Within  → measures spread INSIDE each class
Sʙ → B = Between → measures gap BETWEEN different classes
```

---

#### 8. Closet Analogy — The Big Picture
```
LDA is like organizing a closet:

BEFORE:                   AFTER (LDA):
T-shirts, dresses,       [TTT]  gap  [DDD]
dresses, T-shirts   →    All       All
mixed together!          T-shirts  Dresses

1. Maximize space BETWEEN shirt types  → maximize Sʙ
2. Minimize space WITHIN each type     → minimize Sᵂ
3. Result: Easy to find what you need! → easy to classify!
```

---

## 15. Common Mistakes & Fixes

| Mistake | What Goes Wrong | The Fix |
|---|---|---|
| Only maximizing d without controlling s² | Means are far but groups overlap due to high scatter | Always optimize the RATIO d²/(s₁²+s₂²) |
| Confusing Sᵂ and Sʙ | Wrong matrices → wrong direction | W = Within (same class); B = Between (different classes) |
| Forgetting to invert Sᵂ | Wrong formula | w* = **Sᵂ⁻¹** (μ₂−μ₁), NOT Sᵂ × (μ₂−μ₁) |
| Expecting C axes for C classes | Over-counting output dimensions | LDA gives **C−1** axes, not C |
| Using LDA when class covariances differ a lot | Poor performance | Switch to **QDA** |
| Assuming LDA and PCA give same result | Using wrong tool | PCA = max variance; LDA = max separation; different axes! |
| Not normalizing w before comparing | Scale-dependent results | Normalize: ŵ = w/‖w‖ |

---

## 16. Quick Q&A for Exam

**Q: Is LDA supervised or unsupervised?**
> **Supervised** — it requires class labels during training.

**Q: Can LDA be used for visualization only (not classification)?**
> Yes! LDA can reduce 10,000 dimensions to 2D (LD1 vs LD2) just to visualize cluster structure.

**Q: What is the relationship between Distance-from-Means and LDA?**
> Distance-from-Means is a **special case** of LDA. When all classes have equal spherical covariance (Σ = I), LDA reduces to classifying by the nearest class centroid.

**Q: What if Sᵂ is not invertible?**
> Happens when features > samples, or features are linearly dependent. Solutions: regularize by adding λI to Sᵂ (Ridge-style), use pseudo-inverse, or reduce dimensions with PCA first.

**Q: What does eigenvalue λ tell us in Sʙw = λSᵂw?**
> λ measures how good that axis is for separation. Higher λ = better separation. Sort eigenvectors by their λ to get LD1 (best), LD2 (second best), etc.

**Q: What is QDA?**
> Quadratic Discriminant Analysis. Like LDA but each class gets its own covariance matrix Σₖ. The decision boundary becomes a curved (quadratic) surface instead of a straight hyperplane.

**Q: How does LDA compare to Logistic Regression?**
> Both are linear classifiers. LDA assumes Gaussian data + equal covariance → works better with small data if assumptions hold. Logistic Regression makes no distribution assumption → works better with large data or non-Gaussian data.

**Q: Why does PCA sometimes fail where LDA succeeds?**
> PCA finds the directions of maximum **variance**. But the most variable direction may be completely uncorrelated with class labels. LDA directly optimizes for **class separability**, guaranteeing the found axes are useful for classification.

---

## 🏁 Summary in 5 Lines

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. PROBLEM:   High-D data, classify into known groups
2. IDEA:      Find axis that SEPARATES classes best
3. MATH:      Maximize J(w) = Sʙ/Sᵂ  → w* = Sᵂ⁻¹(μ₂−μ₁)
4. OUTPUT:    C−1 new axes (LD1, LD2…) for C classes
5. CLASSIFY:  Project new point, compare to midpoint threshold
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Key difference from PCA:
  PCA = BLIND (no labels) → max variance
  LDA = HAS EYES (uses labels) → max separation
```

---

*Covers: LDA Part-1 (Fisher's LDA + Math) & Part-2 (Gene Expression + 3-Class LDA)*
