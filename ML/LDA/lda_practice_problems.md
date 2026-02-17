# 📝 LDA Practice Problems with Detailed Solutions

> **10 Carefully Crafted Problems** covering all aspects of Linear Discriminant Analysis
> 
> Solutions are hidden in collapsible sections — try solving first!

---

## 📋 Table of Contents

| # | Problem | Difficulty | Topics Covered |
|---|---------|------------|----------------|
| 1 | [Basic 2D LDA Projection](#problem-1-basic-2d-lda-projection) | ⭐ Easy | Class means, projection, classification |
| 2 | [Within-Class Scatter Matrix](#problem-2-within-class-scatter-matrix) | ⭐⭐ Medium | Scatter matrix computation, matrix operations |
| 3 | [Complete LDA from Scratch](#problem-3-complete-lda-from-scratch) | ⭐⭐⭐ Hard | All 6 steps, matrix inverse, classification |
| 4 | [LDA vs PCA Conceptual](#problem-4-lda-vs-pca-conceptual) | ⭐ Easy | Understanding differences, when to use which |
| 5 | [3-Class LDA Axes](#problem-5-3-class-lda-axes) | ⭐⭐ Medium | Number of axes, eigenvalues, multi-class |
| 6 | [Fisher's Criterion Calculation](#problem-6-fishers-criterion-calculation) | ⭐⭐ Medium | Ratio computation, interpretation |
| 7 | [2×2 Matrix Inverse](#problem-7-2x2-matrix-inverse-shortcut) | ⭐ Easy | Matrix algebra, determinant |
| 8 | [Between-Class Scatter](#problem-8-between-class-scatter-matrix) | ⭐⭐ Medium | Sʙ computation, outer product |
| 9 | [Projection and Classification](#problem-9-projection-and-classification) | ⭐⭐⭐ Hard | Complete workflow, decision boundary |
| 10 | [Assumption Violation](#problem-10-assumption-violation-qda) | ⭐⭐ Medium | When LDA fails, QDA alternative |

---

## Problem 1: Basic 2D LDA Projection

### Question

You have already computed the optimal LDA direction vector:

```
w* = [0.6, 0.8]
```

And the projected class means are:
```
m̃₁ = 2.0   (Class 1)
m̃₂ = 8.0   (Class 2)
```

**Tasks:**
1. Project the test point `x = [3, 4]` onto the LDA axis
2. Compute the decision threshold
3. Classify the test point

<details>
<summary><b>👉 Click to reveal solution</b></summary>

---

### Solution

#### **Step 1: Project the test point**

**Formula Used:**
```
y = wᵀ x    (dot product / projection formula)
```

**Calculation:**
```
x = [3, 4]
w* = [0.6, 0.8]

y = wᵀ x
  = (0.6 × 3) + (0.8 × 4)
  = 1.8 + 3.2
  = 5.0
```

**Result:** The projected value of the test point is **y = 5.0**

---

#### **Step 2: Compute decision threshold**

**Formula Used:**
```
threshold t = (m̃₁ + m̃₂) / 2
```

**Why this formula?**
> The decision boundary is placed at the midpoint between the two projected class means.

**Calculation:**
```
m̃₁ = 2.0
m̃₂ = 8.0

t = (2.0 + 8.0) / 2
  = 10.0 / 2
  = 5.0
```

**Result:** Threshold **t = 5.0**

---

#### **Step 3: Classify the test point**

**Decision Rule:**
```
If y ≥ t  →  Class 2
If y < t  →  Class 1
```

**Comparison:**
```
y = 5.0
t = 5.0

y ≥ t  →  5.0 ≥ 5.0  ✓ TRUE
```

**Result:** Classified as **Class 2**

---

**Visual Representation:**
```
1D Projected Line:

  2.0         5.0         5.0         8.0
   |           |           |           |
   ↓           ↓           ↓           ↓
  m̃₁      threshold    test pt       m̃₂
(Class 1)     (t)         (y)      (Class 2)

Since y is at the threshold (boundary case), 
and our rule uses ≥, it goes to Class 2.
```

---

**Key Concepts:**
- **Projection:** Reducing multi-dimensional point to 1D value
- **Dot Product:** wᵀx = w₁x₁ + w₂x₂
- **Threshold:** Midpoint decision boundary
- **Classification:** Compare projected value to threshold

---

</details>

---

## Problem 2: Within-Class Scatter Matrix

### Question

Given the following data:

**Class 1 (Green):**
```
x₁ = [2, 1]
x₂ = [3, 2]
```

**Class mean already computed:**
```
μ₁ = [2.5, 1.5]
```

**Task:** Compute the within-class scatter matrix S₁ for Class 1.

<details>
<summary><b>👉 Click to reveal solution</b></summary>

---

### Solution

#### **Formula Used:**
```
Sₖ = Σ (xₙ − μₖ)(xₙ − μₖ)ᵀ
    n∈Cₖ

For each point in class k:
  1. Compute deviation: xₙ − μₖ
  2. Compute outer product: (xₙ − μₖ)(xₙ − μₖ)ᵀ
  3. Sum all outer products
```

---

#### **Step 1: Compute deviations**

**For point x₁:**
```
x₁ = [2, 1]
μ₁ = [2.5, 1.5]

diff₁ = x₁ − μ₁
      = [2 − 2.5, 1 − 1.5]
      = [−0.5, −0.5]
```

**For point x₂:**
```
x₂ = [3, 2]
μ₁ = [2.5, 1.5]

diff₂ = x₂ − μ₁
      = [3 − 2.5, 2 − 1.5]
      = [0.5, 0.5]
```

---

#### **Step 2: Compute outer products**

**What is an outer product?**
> For a column vector v, the outer product v × vᵀ produces a matrix.
> 
> Example: [a] × [a, b] = [a×a  a×b]
>          [b]             [b×a  b×b]

**For diff₁:**
```
diff₁ = [−0.5, −0.5]

As column vector: [−0.5]
                  [−0.5]

diff₁ × diff₁ᵀ = [−0.5] × [−0.5, −0.5]
                  [−0.5]

                = [−0.5×(−0.5)   −0.5×(−0.5)]
                  [−0.5×(−0.5)   −0.5×(−0.5)]

                = [0.25  0.25]
                  [0.25  0.25]
```

**For diff₂:**
```
diff₂ = [0.5, 0.5]

diff₂ × diff₂ᵀ = [0.5] × [0.5, 0.5]
                  [0.5]

                = [0.5×0.5   0.5×0.5]
                  [0.5×0.5   0.5×0.5]

                = [0.25  0.25]
                  [0.25  0.25]
```

---

#### **Step 3: Sum the outer products**

```
S₁ = diff₁×diff₁ᵀ + diff₂×diff₂ᵀ

   = [0.25  0.25] + [0.25  0.25]
     [0.25  0.25]   [0.25  0.25]

   = [0.25+0.25    0.25+0.25]
     [0.25+0.25    0.25+0.25]

   = [0.5  0.5]
     [0.5  0.5]
```

---

#### **Final Answer:**
```
S₁ = [0.5  0.5]
     [0.5  0.5]
```

---

**Interpretation:**
- **Diagonal elements (0.5, 0.5):** Variance in each dimension
- **Off-diagonal elements (0.5):** Covariance between dimensions
- **Symmetry:** Scatter matrices are always symmetric (Sᵀ = S)

---

**Key Formulas Recap:**
1. **Deviation:** diff = xₙ − μₖ
2. **Outer product:** diff × diffᵀ (column × row = matrix)
3. **Scatter matrix:** Sum of all outer products
4. **Properties:** Always square, always symmetric

---

</details>

---

## Problem 3: Complete LDA from Scratch

### Question

**Training Data:**

Class 1 (Setosa):
```
x₁ = [1, 2]
x₂ = [2, 3]
```

Class 2 (Versicolor):
```
x₃ = [6, 5]
x₄ = [7, 6]
```

**Test point:**
```
x_test = [4, 3]
```

**Tasks:**
1. Compute class means μ₁ and μ₂
2. Compute within-class scatter matrix Sᵂ
3. Compute between-class scatter matrix Sʙ
4. Find optimal direction w* = Sᵂ⁻¹(μ₂ − μ₁)
5. Project test point and classify it

<details>
<summary><b>👉 Click to reveal solution</b></summary>

---

### Solution

---

#### **STEP 1: Compute Class Means**

**Formula:**
```
μₖ = (1/Nₖ) Σ xₙ
```

**For Class 1 (Setosa):**
```
x₁ = [1, 2]
x₂ = [2, 3]
N₁ = 2

μ₁ = (x₁ + x₂) / 2
   = ([1,2] + [2,3]) / 2
   = [3, 5] / 2
   = [1.5, 2.5]
```

**For Class 2 (Versicolor):**
```
x₃ = [6, 5]
x₄ = [7, 6]
N₂ = 2

μ₂ = (x₃ + x₄) / 2
   = ([6,5] + [7,6]) / 2
   = [13, 11] / 2
   = [6.5, 5.5]
```

**Result:** 
```
μ₁ = [1.5, 2.5]   ← Setosa center
μ₂ = [6.5, 5.5]   ← Versicolor center
```

---

#### **STEP 2: Compute Within-Class Scatter Sᵂ**

**Formula:**
```
Sᵂ = S₁ + S₂
Sₖ = Σ (xₙ − μₖ)(xₙ − μₖ)ᵀ
```

**For Class 1:**

Point x₁:
```
diff₁ = x₁ − μ₁ = [1,2] − [1.5,2.5] = [−0.5, −0.5]

diff₁ × diff₁ᵀ = [−0.5] × [−0.5, −0.5]
                  [−0.5]

                = [0.25  0.25]
                  [0.25  0.25]
```

Point x₂:
```
diff₂ = x₂ − μ₁ = [2,3] − [1.5,2.5] = [0.5, 0.5]

diff₂ × diff₂ᵀ = [0.5] × [0.5, 0.5]
                  [0.5]

                = [0.25  0.25]
                  [0.25  0.25]
```

Sum for S₁:
```
S₁ = [0.25  0.25] + [0.25  0.25]
     [0.25  0.25]   [0.25  0.25]

   = [0.5  0.5]
     [0.5  0.5]
```

**For Class 2:**

Point x₃:
```
diff₃ = x₃ − μ₂ = [6,5] − [6.5,5.5] = [−0.5, −0.5]

diff₃ × diff₃ᵀ = [0.25  0.25]
                  [0.25  0.25]
```

Point x₄:
```
diff₄ = x₄ − μ₂ = [7,6] − [6.5,5.5] = [0.5, 0.5]

diff₄ × diff₄ᵀ = [0.25  0.25]
                  [0.25  0.25]
```

Sum for S₂:
```
S₂ = [0.25  0.25] + [0.25  0.25]
     [0.25  0.25]   [0.25  0.25]

   = [0.5  0.5]
     [0.5  0.5]
```

**Total Within-Class Scatter:**
```
Sᵂ = S₁ + S₂

   = [0.5  0.5] + [0.5  0.5]
     [0.5  0.5]   [0.5  0.5]

   = [1.0  1.0]
     [1.0  1.0]
```

---

#### **STEP 3: Compute Between-Class Scatter Sʙ**

**Formula:**
```
Sʙ = (μ₂ − μ₁)(μ₂ − μ₁)ᵀ
```

**Calculate mean difference:**
```
μ₂ − μ₁ = [6.5, 5.5] − [1.5, 2.5]
        = [5.0, 3.0]
```

**Compute outer product:**
```
Sʙ = [5.0] × [5.0, 3.0]
     [3.0]

   = [5.0×5.0   5.0×3.0]
     [3.0×5.0   3.0×3.0]

   = [25.0  15.0]
     [15.0   9.0]
```

---

#### **STEP 4: Find Optimal Direction w***

**Formula:**
```
w* = Sᵂ⁻¹ (μ₂ − μ₁)
```

**Need to compute Sᵂ⁻¹:**

For 2×2 matrix:
```
A = [a  b]     A⁻¹ = ───1───  × [ d  −b]
    [c  d]           ad − bc     [−c   a]
```

Given:
```
Sᵂ = [1.0  1.0]
     [1.0  1.0]

a = 1.0,  b = 1.0,  c = 1.0,  d = 1.0

det(Sᵂ) = ad − bc
        = (1.0 × 1.0) − (1.0 × 1.0)
        = 1.0 − 1.0
        = 0
```

**⚠️ PROBLEM:** Determinant is 0! Matrix is **singular** (non-invertible).

**Why?**
> The scatter matrix has rank 1 (both rows are identical).
> This happens when data points lie on a line.

**Solution approach:**
> In practice, we'd add regularization: Sᵂ + λI where λ is small (e.g., 0.01)

**Let's add regularization:**
```
λ = 0.01

Sᵂ_reg = [1.0  1.0] + [0.01  0   ]
         [1.0  1.0]   [0     0.01]

       = [1.01  1.00]
         [1.00  1.01]

det(Sᵂ_reg) = (1.01 × 1.01) − (1.00 × 1.00)
             = 1.0201 − 1.0000
             = 0.0201

Sᵂ_reg⁻¹ = ──1──── × [ 1.01  −1.00]
            0.0201    [−1.00   1.01]

         = 49.75 × [ 1.01  −1.00]
                    [−1.00   1.01]

         = [ 50.25  −49.75]
           [−49.75   50.25]
```

**Now compute w*:**
```
μ₂ − μ₁ = [5.0, 3.0]

w* = Sᵂ_reg⁻¹ × (μ₂ − μ₁)

   = [ 50.25  −49.75] × [5.0]
     [−49.75   50.25]   [3.0]

w*[1] = (50.25 × 5.0) + (−49.75 × 3.0)
      = 251.25 − 149.25
      = 102.0

w*[2] = (−49.75 × 5.0) + (50.25 × 3.0)
      = −248.75 + 150.75
      = −98.0

w* = [102.0, −98.0]
```

**Normalize (optional, for cleaner numbers):**
```
‖w*‖ = √(102² + 98²) = √(10404 + 9604) = √20008 ≈ 141.45

ŵ = w* / ‖w*‖ = [102/141.45, −98/141.45]
              ≈ [0.72, −0.69]
```

For this problem, we'll use **w* = [102.0, −98.0]** (unnormalized).

---

#### **STEP 5: Project and Classify Test Point**

**Project class means:**
```
m̃₁ = (w*)ᵀ μ₁
    = (102.0 × 1.5) + (−98.0 × 2.5)
    = 153.0 − 245.0
    = −92.0

m̃₂ = (w*)ᵀ μ₂
    = (102.0 × 6.5) + (−98.0 × 5.5)
    = 663.0 − 539.0
    = 124.0
```

**Project test point:**
```
x_test = [4, 3]

y_test = (w*)ᵀ x_test
       = (102.0 × 4) + (−98.0 × 3)
       = 408.0 − 294.0
       = 114.0
```

**Compute threshold:**
```
t = (m̃₁ + m̃₂) / 2
  = (−92.0 + 124.0) / 2
  = 32.0 / 2
  = 16.0
```

**Classify:**
```
y_test = 114.0
t = 16.0

y_test > t  →  114.0 > 16.0  ✓

→ Classified as CLASS 2 (Versicolor)
```

---

**Visual on 1D line:**
```
  −92.0        16.0       114.0      124.0
    |            |           |          |
    ↓            ↓           ↓          ↓
   m̃₁       threshold    y_test       m̃₂
(Setosa)        (t)      (TEST)   (Versicolor)

Test point is much closer to Versicolor! ✓
```

---

**Key Takeaways:**
1. **Singular matrices** require regularization in practice
2. **All 6 steps** executed: means → scatter → direction → project → classify
3. **Matrix inverse** for 2×2 case uses the shortcut formula
4. **Outer products** build scatter matrices
5. **Threshold** is midpoint of projected means

---

</details>

---

## Problem 4: LDA vs PCA Conceptual

### Question

**Scenario:** You have a dataset of patient health records with 50 features (blood pressure, cholesterol, age, etc.) and 3 disease categories (Healthy, Type-A, Type-B). You want to visualize the data in 2D.

**Tasks:**
1. Should you use PCA or LDA? Why?
2. What if the categories were unknown (unsupervised clustering task)?
3. If you use LDA, how many axes will you get? Why?
4. Give one advantage of PCA over LDA in this scenario.

<details>
<summary><b>👉 Click to reveal solution</b></summary>

---

### Solution

---

#### **Question 1: Should you use PCA or LDA?**

**Answer: Use LDA**

**Reasoning:**

```
Goal: Visualize 3 disease categories separately

✓ LDA is the right choice because:
  1. You HAVE class labels (Healthy, Type-A, Type-B)
  2. You want to SEE separation between disease types
  3. LDA maximizes between-class separation
  4. Resulting plot will show distinct clusters

✗ PCA would be WRONG because:
  1. PCA doesn't use labels → ignores disease categories
  2. PCA finds directions of VARIANCE, not SEPARATION
  3. High-variance features (e.g., age range) might dominate
  4. Categories might overlap in PCA plot even if separable
```

**Visualization comparison:**
```
PCA Result (PC1 vs PC2):        LDA Result (LD1 vs LD2):
   Healthy patients               Healthy cluster
   Type-A patients                  ●●●●●
   Type-B patients                ●●●●●●●

PC2 ↑                           LD2 ↑
    │ ●■▲●■▲                        │     ●●●●
    │ ▲●■▲●■                        │     ●●●●●
    │ ■●▲■●▲                        │  ■■■■     ▲▲▲▲
    │ ●■▲●■▲                        │  ■■■■     ▲▲▲▲
    └───────→ PC1                   └──────────────→ LD1

  Mixed! Can't tell               Clear clusters! ✓
  categories apart
```

---

#### **Question 2: What if categories were unknown?**

**Answer: Use PCA**

**Reasoning:**

```
If NO labels available (unsupervised):

✓ PCA is the right choice:
  1. Works without labels
  2. Reduces dimensions to visualize structure
  3. Can be followed by clustering (K-means, etc.)

✗ LDA CANNOT be used:
  1. LDA is SUPERVISED → requires labels
  2. No way to compute class means without labels
  3. Cannot compute between-class scatter
```

**Workflow for unknown categories:**
```
1. Apply PCA (unsupervised dimensionality reduction)
2. Visualize in 2D (PC1 vs PC2)
3. Apply K-means or DBSCAN clustering
4. Discover natural groupings
```

---

#### **Question 3: How many LDA axes? Why?**

**Answer: 2 axes (LD1 and LD2)**

**Formula:**
```
# LDA axes = min(C − 1,  p)
                 ↑       ↑
              classes  features

C = 3 categories (Healthy, Type-A, Type-B)
p = 50 features

# axes = min(3 − 1, 50)
      = min(2, 50)
      = 2
```

**Geometric explanation:**
```
2 points → define 1 line   → 1 axis needed
3 points → define 1 plane  → 2 axes needed
4 points → define 3D space → 3 axes needed

3 class centroids lie in a 2D plane → need 2 axes to span it
```

**Result:**
```
LDA reduces 50D → 2D
  Feature 1:  LD1 (best separating axis)
  Feature 2:  LD2 (second-best separating axis)

Perfect for visualization! ✓
```

---

#### **Question 4: One advantage of PCA over LDA?**

**Answer: PCA can use more dimensions for better representation**

**Explanation:**

```
PCA:  Can use up to p axes (all 50 in this case)
      PC1, PC2, ..., PC50

      You can capture 95% of variance with maybe PC1-PC10

LDA:  Limited to C−1 = 2 axes only
      LD1, LD2 (that's it!)

      Might lose important variance not related to class separation
```

**Example scenario where PCA wins:**

```
Suppose within each disease category, there are important
sub-patterns (e.g., age groups, genetic variants).

PCA can capture these sub-patterns using PC3, PC4, PC5...

LDA is STUCK with 2 axes → can only show class separation,
loses all within-class structure.
```

**Other PCA advantages:**
- Works with ANY number of samples (LDA needs enough for stable covariance)
- No assumption of equal covariance across classes
- Can detect outliers in unsupervised manner
- Useful for data compression (not just visualization)

---

**Summary Table:**

| Aspect | PCA | LDA |
|--------|-----|-----|
| **For this scenario** | ❌ No (we have labels!) | ✅ Yes (use labels!) |
| **If no labels** | ✅ Yes | ❌ No (impossible) |
| **# axes possible** | Up to 50 | Only 2 (C−1) |
| **Best for** | Variance preservation | Class separation |
| **Advantage** | More flexibility | Better classification |

---

</details>

---

## Problem 5: 3-Class LDA Axes

### Question

You are working with gene expression data:
- **Features:** 10,000 genes per patient
- **Classes:** 3 cancer subtypes (A, B, C)
- **Samples:** 100 patients total

**Tasks:**
1. How many LDA axes will be created? Show the formula.
2. What are these axes called?
3. Which axis is most important and why?
4. If you had 2 classes instead, how many axes?
5. If you had 100 classes, how many axes?

<details>
<summary><b>👉 Click to reveal solution</b></summary>

---

### Solution

---

#### **Question 1: How many LDA axes?**

**Formula:**
```
# LDA axes = min(C − 1,  p)
```

**Where:**
- **C** = number of classes
- **p** = number of features

**Given:**
- C = 3 (cancer subtypes A, B, C)
- p = 10,000 (genes)

**Calculation:**
```
# axes = min(3 − 1, 10,000)
      = min(2, 10,000)
      = 2
```

**Answer: 2 LDA axes** (LD1 and LD2)

---

#### **Why this formula?**

**Geometric reasoning:**
```
3 class means (μ_A, μ_B, μ_C) in 10,000D space

These 3 points define a PLANE in high-dimensional space.

To span a plane, you need 2 axes.

General rule:
  N points define an (N−1)-dimensional space
  → need N−1 axes to represent it
```

**Visual analogy (in 3D):**
```
Imagine 3 dots in a 3D room:

        ● μ_C
       /│\
      / │ \
     /  │  \
    ●───┼───● 
   μ_A  │  μ_B
        │
    (They define a flat plane)

To describe positions ON this plane,
you only need 2 coordinates (x, y on the plane),
NOT all 3 dimensions of the room.

Same idea: 3 classes → 2 LDA axes
```

---

#### **Question 2: What are these axes called?**

**Answer:**
```
LD1 and LD2

LD = Linear Discriminant

Full names:
  LD1 = First Linear Discriminant (best separating axis)
  LD2 = Second Linear Discriminant (second-best axis)
```

**Alternative names you might see:**
- Discriminant Function 1 and 2
- Canonical Variables 1 and 2
- LDA Component 1 and 2

---

#### **Question 3: Which axis is most important?**

**Answer: LD1 is most important**

**Reasoning:**

```
LDA axes are ranked by their EIGENVALUES (λ)

When solving:  Sʙ w = λ Sᵂ w

We get multiple eigenvectors (w₁, w₂) with eigenvalues (λ₁, λ₂)

λ₁ > λ₂  →  LD1 separates classes better than LD2
```

**What the eigenvalue means:**
```
         wᵀ Sʙ w         Between-class variance along w
J(w) = ─────────── = ───────────────────────────────────
         wᵀ Sᵂ w         Within-class variance along w

λ = this ratio for the axis w

Higher λ → better separation!

Typical values:
  λ₁ = 15.3  ← LD1 (best!)
  λ₂ = 4.2   ← LD2 (good, but not as good as LD1)
```

**Practical implication:**
```
For visualization:
  - LD1 vs LD2 plot: Best 2D view
  - LD1 alone: Often sufficient for classification
  - LD2 alone: Less useful than LD1

For classification:
  - Can use LD1 only for simpler model
  - Use both LD1 + LD2 for better accuracy
```

---

#### **Question 4: If 2 classes, how many axes?**

**Answer: 1 axis**

**Calculation:**
```
C = 2
p = 10,000

# axes = min(C − 1, p)
      = min(2 − 1, 10,000)
      = min(1, 10,000)
      = 1
```

**Intuition:**
```
2 class means define a LINE (not a plane)

   μ_A ●──────────● μ_B

A line is 1-dimensional → need only 1 axis (LD1)

This is the standard binary LDA case!
```

---

#### **Question 5: If 100 classes, how many axes?**

**Answer: 99 axes**

**Calculation:**
```
C = 100
p = 10,000

# axes = min(C − 1, p)
      = min(100 − 1, 10,000)
      = min(99, 10,000)
      = 99
```

**BUT there's a practical limit:**

```
⚠️ Even though mathematically we get 99 axes,
   we can only compute them if we have ENOUGH samples!

Rule of thumb:
  Need at least C samples (ideally much more)
  to reliably estimate C class means and covariances

With only 100 patients total:
  100 samples / 100 classes = 1 sample per class!
  → Not enough to compute reliable statistics
  → LDA would fail

Better approach with 100 classes:
  1. Use hierarchical classification
  2. Group similar classes
  3. Use deep learning instead
```

---

**Summary Table:**

| Classes (C) | Features (p) | LDA Axes | Limiting Factor |
|-------------|--------------|----------|-----------------|
| 2 | 10,000 | 1 | C−1 = 1 |
| 3 | 10,000 | 2 | C−1 = 2 |
| 10 | 10,000 | 9 | C−1 = 9 |
| 100 | 10,000 | 99 | C−1 = 99 |
| 3 | 2 | 2 | p = 2 (both limit equally) |
| 10 | 5 | 5 | **p = 5** (features limit!) |

---

**Key Formula to Remember:**
```
# LDA axes = min(C − 1, p)
            ↑        ↑
        class limit  feature limit

Whichever is SMALLER is the bottleneck!
```

---

</details>

---

## Problem 6: Fisher's Criterion Calculation

### Question

Given the following 1D projected data:

**Class 1 (after projection onto w):**
```
Projected points: y₁ = 2, y₂ = 3, y₃ = 4
```

**Class 2 (after projection onto w):**
```
Projected points: y₄ = 8, y₅ = 9, y₆ = 10
```

**Tasks:**
1. Compute projected class means m̃₁ and m̃₂
2. Compute within-class scatter s₁² and s₂²
3. Compute Fisher's criterion J
4. Interpret: Is this a good separation?

<details>
<summary><b>👉 Click to reveal solution</b></summary>

---

### Solution

---

#### **STEP 1: Compute Projected Class Means**

**Formula:**
```
m̃ₖ = (1/Nₖ) Σ yₙ
```

**For Class 1:**
```
y₁ = 2,  y₂ = 3,  y₃ = 4
N₁ = 3

m̃₁ = (y₁ + y₂ + y₃) / 3
   = (2 + 3 + 4) / 3
   = 9 / 3
   = 3.0
```

**For Class 2:**
```
y₄ = 8,  y₅ = 9,  y₆ = 10
N₂ = 3

m̃₂ = (y₄ + y₅ + y₆) / 3
   = (8 + 9 + 10) / 3
   = 27 / 3
   = 9.0
```

**Result:**
```
m̃₁ = 3.0   (Class 1 center on projected axis)
m̃₂ = 9.0   (Class 2 center on projected axis)
```

---

#### **STEP 2: Compute Within-Class Scatter**

**Formula:**
```
sₖ² = Σ (yₙ − m̃ₖ)²
     n∈Cₖ

This is the variance of projected points around their class mean.
```

**For Class 1:**
```
m̃₁ = 3.0

Point y₁ = 2:   (y₁ − m̃₁)² = (2 − 3.0)² = (−1.0)² = 1.0
Point y₂ = 3:   (y₂ − m̃₁)² = (3 − 3.0)² = (0.0)²  = 0.0
Point y₃ = 4:   (y₃ − m̃₁)² = (4 − 3.0)² = (1.0)²  = 1.0

s₁² = 1.0 + 0.0 + 1.0 = 2.0
```

**For Class 2:**
```
m̃₂ = 9.0

Point y₄ = 8:   (y₄ − m̃₂)² = (8 − 9.0)²  = (−1.0)² = 1.0
Point y₅ = 9:   (y₅ − m̃₂)² = (9 − 9.0)²  = (0.0)²  = 0.0
Point y₆ = 10:  (y₆ − m̃₂)² = (10 − 9.0)² = (1.0)²  = 1.0

s₂² = 1.0 + 0.0 + 1.0 = 2.0
```

**Result:**
```
s₁² = 2.0   (Class 1 spread)
s₂² = 2.0   (Class 2 spread)
```

---

#### **STEP 3: Compute Fisher's Criterion**

**Formula:**
```
         (m̃₁ − m̃₂)²
J(w) = ──────────────
         s₁² + s₂²
```

**Numerator (between-class separation):**
```
(m̃₁ − m̃₂)² = (3.0 − 9.0)²
            = (−6.0)²
            = 36.0
```

**Denominator (within-class scatter):**
```
s₁² + s₂² = 2.0 + 2.0
          = 4.0
```

**Fisher's Criterion:**
```
J = 36.0 / 4.0
  = 9.0
```

**Result: J = 9.0**

---

#### **STEP 4: Interpretation**

**Is this a good separation?**

**Answer: YES, excellent separation! ✓**

**Reasoning:**

```
J = 9.0

What does this mean?

J = (between-class distance)² / (within-class scatter)
  = 36.0 / 4.0
  = 9.0

The between-class distance is 9× larger than within-class spread!
```

**Visual representation:**
```
1D Number Line:

  2  3  4        8  9  10
  ●  ●  ●        ●  ●  ●
  Class 1        Class 2
  ↑              ↑
  m̃₁=3          m̃₂=9

Gap = |9 − 3| = 6 units
Spread (σ) ≈ √2 ≈ 1.4 units per class

Gap / Spread ≈ 6 / 1.4 ≈ 4.3

The gap is 4.3× larger than the typical spread → CLEAN SEPARATION ✓
```

**Guidelines for interpreting J:**

| J Value | Quality | Interpretation |
|---------|---------|----------------|
| J < 1 | Poor | Classes overlap heavily |
| 1 ≤ J < 3 | Moderate | Some overlap, classification challenging |
| 3 ≤ J < 10 | Good | Clear separation, good for classification |
| J ≥ 10 | Excellent | Very clean separation |

**In this case:** J = 9.0 → **Good to Excellent** range

---

**Alternative metric — Separation Ratio:**

```
How many "scatter widths" fit in the gap?

Scatter width ≈ √(s₁² + s₂²) = √4 = 2.0
Gap = |m̃₂ − m̃₁| = 6.0

Ratio = 6.0 / 2.0 = 3.0

The gap is 3 scatter-widths wide → very clean!
```

---

**What if J was different?**

**Example 1: Poor separation (J = 0.5)**
```
Suppose m̃₁ = 3.0, m̃₂ = 5.0, s₁² = s₂² = 4.0

J = (3.0 − 5.0)² / (4.0 + 4.0)
  = 4.0 / 8.0
  = 0.5

Visual:
  1  2  3  4  5  6  7  8
  ●  ●  ●  ●  ●  ●  ●  ●
     Class 1  |  Class 2
     (spread)    (spread)

Heavily overlapping! Classification would be poor.
```

**Example 2: Excellent separation (J = 25)**
```
Suppose m̃₁ = 0.0, m̃₂ = 10.0, s₁² = s₂² = 1.0

J = (0.0 − 10.0)² / (1.0 + 1.0)
  = 100.0 / 2.0
  = 50.0

Visual:
  -1  0  1         8  9  10  11
   ●  ●  ●         ●  ●  ●
   Class 1         Class 2

Perfectly separated! Near-perfect classification.
```

---

**Key Formulas Recap:**

1. **Projected mean:** m̃ₖ = (1/Nₖ) Σ yₙ
2. **Scatter:** sₖ² = Σ (yₙ − m̃ₖ)²
3. **Fisher's criterion:** J = (m̃₁ − m̃₂)² / (s₁² + s₂²)
4. **Interpretation:** Higher J = better separation

---

</details>

---

## Problem 7: 2×2 Matrix Inverse Shortcut

### Question

**Given the within-class scatter matrix:**
```
Sᵂ = [3.0  1.0]
     [1.0  2.0]
```

**Tasks:**
1. Compute the determinant
2. Find the inverse Sᵂ⁻¹ using the 2×2 shortcut formula
3. Verify your answer by checking Sᵂ × Sᵂ⁻¹ = I

<details>
<summary><b>👉 Click to reveal solution</b></summary>

---

### Solution

---

#### **STEP 1: Compute the Determinant**

**Formula for 2×2 determinant:**
```
For matrix A = [a  b]
               [c  d]

det(A) = ad − bc
```

**Given:**
```
Sᵂ = [3.0  1.0]    →  a = 3.0,  b = 1.0
     [1.0  2.0]        c = 1.0,  d = 2.0
```

**Calculation:**
```
det(Sᵂ) = ad − bc
        = (3.0 × 2.0) − (1.0 × 1.0)
        = 6.0 − 1.0
        = 5.0
```

**Result: det(Sᵂ) = 5.0**

**✓ Matrix is invertible** (det ≠ 0)

---

#### **STEP 2: Compute the Inverse**

**Formula for 2×2 inverse:**
```
For matrix A = [a  b]
               [c  d]

         1
A⁻¹ = ────── × [ d  −b]
      ad−bc    [−c   a]

Memory trick: "Swap a and d, negate b and c, divide by det"
```

**Apply to Sᵂ:**
```
Sᵂ = [3.0  1.0]
     [1.0  2.0]

det(Sᵂ) = 5.0

Step 1: Swap diagonal elements (a ↔ d)
        [ d  ?] = [2.0  ?]
        [ ?  a]   [?   3.0]

Step 2: Negate off-diagonal elements (−b, −c)
        [2.0  −1.0]
        [−1.0  3.0]

Step 3: Divide by determinant
        1
Sᵂ⁻¹ = ─── × [2.0  −1.0]
        5.0    [−1.0  3.0]
```

**Final computation:**
```
Sᵂ⁻¹ = [2.0/5.0   −1.0/5.0]
       [−1.0/5.0   3.0/5.0]

     = [0.4   −0.2]
       [−0.2   0.6]
```

**Result:**
```
Sᵂ⁻¹ = [0.4   −0.2]
       [−0.2   0.6]
```

---

#### **STEP 3: Verify the Inverse**

**Property to check:**
```
A × A⁻¹ = I   (Identity matrix)

I = [1  0]
    [0  1]
```

**Compute Sᵂ × Sᵂ⁻¹:**
```
Sᵂ × Sᵂ⁻¹ = [3.0  1.0] × [0.4   −0.2]
            [1.0  2.0]   [−0.2   0.6]
```

**Matrix multiplication (row × column):**

**Element [1,1]:**
```
Row 1 × Column 1
= (3.0 × 0.4) + (1.0 × −0.2)
= 1.2 + (−0.2)
= 1.0 ✓
```

**Element [1,2]:**
```
Row 1 × Column 2
= (3.0 × −0.2) + (1.0 × 0.6)
= −0.6 + 0.6
= 0.0 ✓
```

**Element [2,1]:**
```
Row 2 × Column 1
= (1.0 × 0.4) + (2.0 × −0.2)
= 0.4 + (−0.4)
= 0.0 ✓
```

**Element [2,2]:**
```
Row 2 × Column 2
= (1.0 × −0.2) + (2.0 × 0.6)
= −0.2 + 1.2
= 1.0 ✓
```

**Result:**
```
Sᵂ × Sᵂ⁻¹ = [1.0  0.0] = I ✓✓✓
            [0.0  1.0]

VERIFIED! The inverse is correct.
```

---

**Summary of 2×2 Inverse Steps:**

```
Given: A = [a  b]
           [c  d]

Step 1: Compute det(A) = ad − bc

Step 2: If det ≠ 0, compute:

         1      [ d  −b]
A⁻¹ = ────── × [      ]
      ad−bc    [−c   a]

Step 3: Verify: A × A⁻¹ = I

Shortcut memory:
"Flip main diagonal, flip signs of anti-diagonal, divide by det"
```

---

**Common mistakes to avoid:**

❌ **Mistake 1:** Forgetting to negate off-diagonal
```
WRONG: A⁻¹ = (1/det) × [d  b]   ← b should be −b
                        [c  a]   ← c should be −c
```

❌ **Mistake 2:** Not dividing by determinant
```
WRONG: A⁻¹ = [d  −b]   ← Missing the 1/det factor!
             [−c  a]
```

❌ **Mistake 3:** Swapping wrong elements
```
WRONG: A⁻¹ = (1/det) × [a  −b]   ← a,d should swap!
                        [−c  d]
```

✓ **Correct:**
```
A⁻¹ = (1/det) × [ d  −b]   ← d in top-left
                [−c   a]   ← a in bottom-right
```

---

</details>

---

## Problem 8: Between-Class Scatter Matrix

### Question

**Given class means:**
```
μ₁ = [2, 1]   (Class 1 center)
μ₂ = [5, 4]   (Class 2 center)
```

**Tasks:**
1. Compute the mean difference vector
2. Compute the between-class scatter matrix Sʙ
3. Interpret the result: What do the matrix elements represent?

<details>
<summary><b>👉 Click to reveal solution</b></summary>

---

### Solution

---

#### **STEP 1: Compute Mean Difference Vector**

**Formula:**
```
Δμ = μ₂ − μ₁
```

**Calculation:**
```
μ₁ = [2, 1]
μ₂ = [5, 4]

Δμ = μ₂ − μ₁
   = [5, 4] − [2, 1]
   = [5−2, 4−1]
   = [3, 3]
```

**Result: Δμ = [3, 3]**

**Interpretation:**
> This vector points FROM Class 1 center TO Class 2 center.
> It shows the direction and magnitude of class separation.

---

#### **STEP 2: Compute Between-Class Scatter Sʙ**

**Formula:**
```
Sʙ = (μ₂ − μ₁)(μ₂ − μ₁)ᵀ
   = Δμ × (Δμ)ᵀ
   = (column vector) × (row vector)
   = outer product
```

**Setup:**
```
Δμ as column vector:  [3]
                      [3]

Δμ as row vector:  [3, 3]
```

**Outer product computation:**
```
Sʙ = [3] × [3, 3]
     [3]

   = [3×3  3×3]
     [3×3  3×3]

   = [9  9]
     [9  9]
```

**Result:**
```
Sʙ = [9  9]
     [9  9]
```

---

#### **STEP 3: Interpretation**

**What do these matrix elements mean?**

```
Sʙ = [Sʙ₁₁  Sʙ₁₂]
     [Sʙ₂₁  Sʙ₂₂]

Sʙ₁₁ = 9   →  Variance of class separation in dimension 1
Sʙ₂₂ = 9   →  Variance of class separation in dimension 2
Sʙ₁₂ = 9   →  Covariance between dimensions
Sʙ₂₁ = 9   →  Same as Sʙ₁₂ (matrix is symmetric)
```

**Breaking it down:**

**Diagonal elements (Sʙ₁₁, Sʙ₂₂):**
```
Sʙ₁₁ = (μ₂[1] − μ₁[1])²
     = (5 − 2)²
     = 3²
     = 9

"How far apart are the class means in dimension 1?"
→ 3 units apart → 9 when squared

Sʙ₂₂ = (μ₂[2] − μ₁[2])²
     = (4 − 1)²
     = 3²
     = 9

"How far apart are the class means in dimension 2?"
→ 3 units apart → 9 when squared
```

**Off-diagonal elements (Sʙ₁₂, Sʙ₂₁):**
```
Sʙ₁₂ = (μ₂[1] − μ₁[1]) × (μ₂[2] − μ₁[2])
     = (5 − 2) × (4 − 1)
     = 3 × 3
     = 9

"How correlated is the separation across dimensions?"
→ Perfect correlation (both dimensions separate equally)
```

---

**Geometric interpretation:**

```
2D plot:

     Dim 2 ↑
         4 │           ● μ₂ [5,4]
         3 │          /
         2 │         /  ← Δμ = [3,3]
         1 │        /     separation vector
           │● μ₁ [2,1]
           └─────────────→ Dim 1
             1  2  3  4  5

The classes are separated:
  - 3 units in dimension 1
  - 3 units in dimension 2
  - Diagonal direction (45° angle)
```

**Why is Sʙ singular (rank 1)?**
```
det(Sʙ) = (9 × 9) − (9 × 9) = 81 − 81 = 0

Reason: All columns/rows are multiples of each other
        Row 2 = 1 × Row 1

This is ALWAYS true for 2-class LDA:
  Sʙ has rank 1 (only 1 direction of separation)
```

---

**Properties of Between-Class Scatter:**

1. **Always symmetric:** Sʙ = Sʙᵀ
2. **Always positive semi-definite:** xᵀSʙx ≥ 0 for all x
3. **Rank = min(C−1, p):** For 2 classes, rank = 1
4. **Larger values = better separation**

---

**Compare to Within-Class Scatter:**

```
Within-class (Sᵂ):                Between-class (Sʙ):
- Measures spread INSIDE classes  - Measures gap BETWEEN classes
- Want SMALL (tight clusters)     - Want LARGE (far apart means)
- Sum over all points             - Based only on means
- Full rank (usually)             - Rank ≤ C−1
```

---

**Using Sʙ in LDA:**

```
The LDA solution is:

w* = Sᵂ⁻¹ × (μ₂ − μ₁)

This can also be written as:

w* = Sᵂ⁻¹ × Sʙ   (when Sʙ is treated as outer product)

The direction w* balances:
  - Maximizing Sʙ (push classes apart)
  - Minimizing Sᵂ (keep classes tight)
```

---

**Calculation shortcut:**

For 2-class LDA, you don't actually need to form Sʙ as a matrix!

```
Direct formula:
w* = Sᵂ⁻¹ (μ₂ − μ₁)

This is simpler than:
1. Computing Sʙ
2. Solving eigenvalue problem
3. Finding eigenvectors

The 2-class case has a closed form! ✓
```

---

</details>

---

## Problem 9: Projection and Classification

### Question

**Setup:**
You have computed the optimal LDA direction:
```
w* = [4, −3]
```

**Training data projections (already computed):**
```
Class 1 projected values: [1.0, 1.5, 2.0, 2.5, 3.0]
Class 2 projected values: [7.0, 7.5, 8.0, 8.5, 9.0]
```

**Tasks:**
1. Compute the threshold for classification
2. A new patient has features x_new = [2.0, 1.5]. Project and classify.
3. Another patient has x_new = [1.5, 3.0]. Project and classify.
4. What is the decision boundary equation in the original 2D space?

<details>
<summary><b>👉 Click to reveal solution</b></summary>

---

### Solution

---

#### **STEP 1: Compute Classification Threshold**

**Method: Use projected class means**

**Class 1 projected mean:**
```
Projected values: [1.0, 1.5, 2.0, 2.5, 3.0]
N₁ = 5

m̃₁ = (1.0 + 1.5 + 2.0 + 2.5 + 3.0) / 5
   = 10.0 / 5
   = 2.0
```

**Class 2 projected mean:**
```
Projected values: [7.0, 7.5, 8.0, 8.5, 9.0]
N₂ = 5

m̃₂ = (7.0 + 7.5 + 8.0 + 8.5 + 9.0) / 5
   = 40.0 / 5
   = 8.0
```

**Threshold (midpoint):**
```
t = (m̃₁ + m̃₂) / 2
  = (2.0 + 8.0) / 2
  = 10.0 / 2
  = 5.0
```

**Result: Threshold t = 5.0**

**Decision rule:**
```
If y < 5.0  →  Class 1
If y ≥ 5.0  →  Class 2
```

---

#### **STEP 2: Patient 1 — x_new = [2.0, 1.5]**

**Project onto w*:**
```
w* = [4, −3]
x_new = [2.0, 1.5]

y = wᵀ x
  = (4 × 2.0) + (−3 × 1.5)
  = 8.0 + (−4.5)
  = 3.5
```

**Compare to threshold:**
```
y = 3.5
t = 5.0

y < t  →  3.5 < 5.0  ✓

→ Classified as CLASS 1
```

**Visual:**
```
1D Line:

  1.0      2.0      3.5      5.0      7.0      8.0      9.0
   |        |        |        |        |        |        |
   ↓        ↓        ↓        ↓        ↓        ↓        ↓
  C1      m̃₁    Patient1  threshold  C2      m̃₂      C2
points                (t)          points

Patient 1 falls in the Class 1 region ✓
```

---

#### **STEP 3: Patient 2 — x_new = [1.5, 3.0]**

**Project onto w*:**
```
w* = [4, −3]
x_new = [1.5, 3.0]

y = wᵀ x
  = (4 × 1.5) + (−3 × 3.0)
  = 6.0 + (−9.0)
  = −3.0
```

**Compare to threshold:**
```
y = −3.0
t = 5.0

y < t  →  −3.0 < 5.0  ✓

→ Classified as CLASS 1
```

**Note the negative projection:**
```
A negative y value means the point projects to the
"left" side of the origin on the LDA axis.

Since −3.0 < 5.0, it's still Class 1 (which makes sense,
as Class 1 has lower projected values).
```

**Visual:**
```
1D Line:

  −3.0     1.0      2.0      5.0      7.0      8.0
    |       |        |        |        |        |
    ↓       ↓        ↓        ↓        ↓        ↓
 Patient2   C1      m̃₁    threshold  C2      m̃₂
                                    points

Patient 2 is even further into Class 1 region ✓
```

---

#### **STEP 4: Decision Boundary in Original 2D Space**

**The LDA decision boundary is a hyperplane (in 2D, a line):**

**General form:**
```
wᵀx = constant

For classification, the boundary is where:
wᵀx = threshold

Expanded:
w₁x₁ + w₂x₂ = t
```

**Substitute values:**
```
w* = [4, −3]
t = 5.0

4x₁ + (−3)x₂ = 5.0

Simplified:
4x₁ − 3x₂ = 5
```

**This is the decision boundary equation! ✓**

---

**Express as y = mx + b (standard line form):**

```
4x₁ − 3x₂ = 5

Solve for x₂:
−3x₂ = 5 − 4x₁
x₂ = (4x₁ − 5) / 3
x₂ = (4/3)x₁ − 5/3

Slope m = 4/3
Intercept b = −5/3
```

---

**Visualize in 2D:**

```
Feature x₂ ↑
           │
         3 │          ● Patient 2 [1.5, 3.0]
           │         /
         2 │        /  Decision boundary:
           │       /   4x₁ − 3x₂ = 5
         1 │● Patient 1 [2.0, 1.5]
           │     /
           │    /
         0 │───/───────────────────→ Feature x₁
           0   1   2   3   4   5

Points BELOW line → Class 1
Points ABOVE line → Class 2

(Both patients are below the line → Class 1 ✓)
```

---

**Classification regions:**

```
REGION 1 (Class 1):
  4x₁ − 3x₂ < 5
  All points below/left of the line

REGION 2 (Class 2):
  4x₁ − 3x₂ ≥ 5
  All points above/right of the line
```

---

**Alternative formulation:**

The decision boundary can also be written as:
```
f(x) = wᵀx − t = 0

f(x) = 4x₁ − 3x₂ − 5 = 0

Decision rule:
  f(x) < 0  →  Class 1
  f(x) ≥ 0  →  Class 2
```

**Verify patients:**
```
Patient 1: f([2.0, 1.5])
         = 4(2.0) − 3(1.5) − 5
         = 8.0 − 4.5 − 5
         = −1.5 < 0  →  Class 1 ✓

Patient 2: f([1.5, 3.0])
         = 4(1.5) − 3(3.0) − 5
         = 6.0 − 9.0 − 5
         = −8.0 < 0  →  Class 1 ✓
```

---

**Key Concepts:**

1. **Projection:** wᵀx reduces 2D point to 1D value
2. **Threshold:** Midpoint between projected class means
3. **Decision boundary:** Hyperplane perpendicular to w*
4. **Equation:** wᵀx = t separates the space
5. **Classification:** Based on which side of hyperplane

---

</details>

---

## Problem 10: Assumption Violation (QDA)

### Question

You are trying to use LDA on a dataset with 2 classes, but the scatter plots show:

**Class 1 (circles):**
- Very tight cluster
- Small variance in all directions
- Covariance matrix: Σ₁ = [[1, 0], [0, 1]]

**Class 2 (squares):**
- Very spread out cluster
- Large variance in all directions
- Covariance matrix: Σ₂ = [[100, 0], [0, 100]]

**Tasks:**
1. Which LDA assumption is violated here?
2. Will LDA perform well? Why or why not?
3. What alternative should you use instead?
4. Draw a sketch showing why LDA's linear boundary might fail.

<details>
<summary><b>👉 Click to reveal solution</b></summary>

---

### Solution

---

#### **Question 1: Which LDA Assumption is Violated?**

**Answer: The equal covariance assumption**

**LDA's Key Assumptions:**
```
1. Classes are normally distributed (Gaussian) ✓ (might be OK)
2. Classes have EQUAL covariance matrices ✗ (VIOLATED!)
   Σ₁ = Σ₂ = Σ

In this problem:
Σ₁ = [[1, 0], [0, 1]]       ← Small, tight
Σ₂ = [[100, 0], [0, 100]]   ← Large, spread out

Σ₁ ≠ Σ₂  →  ASSUMPTION VIOLATED ✗
```

**What does equal covariance mean?**
```
Equal covariance = same shape and orientation of clusters

✓ Same shape:    ●●●   ■■■    (both circular)
                  ●●●   ■■■

✗ Different:     ●●●   ■■■■■■  (different sizes)
                  ●●●   ■■■■■■
                        ■■■■■■

Our problem is the second case!
```

---

#### **Question 2: Will LDA Perform Well?**

**Answer: NO, LDA will perform poorly ✗**

**Reasoning:**

```
LDA assumes:  Sᵂ = S₁ + S₂ ≈ Σ₁ = Σ₂

Reality:      S₁ is tiny, S₂ is huge
              S₁ + S₂ ≈ S₂  (dominated by Class 2!)

Problem: LDA will create a decision boundary that:
  - Is too influenced by Class 2's large spread
  - Doesn't adapt to Class 1's tight cluster
  - May misclassify Class 1 points that are actually close
    to their own mean but far from Class 2
```

---

**Numerical example:**

Suppose:
```
Class 1: μ₁ = [0, 0],  tight cluster (σ = 1)
Class 2: μ₂ = [10, 0], spread out (σ = 10)
```

**What LDA does:**
```
Sᵂ = S₁ + S₂ ≈ [[1,0],[0,1]] + [[100,0],[0,100]]
              ≈ [[101,0],[0,101]]

LDA assumes BOTH classes have this large spread!

Decision boundary is placed at:
  x₁ = 5  (midpoint between 0 and 10)

But Class 1 is tightly at 0 → boundary should be closer!
```

**Misclassification scenario:**
```
Point at x = [2, 0]:

Truth: Very close to Class 1 (within 2σ), far from Class 2
LDA says: "It's past x₁ = 5? No. It's Class 1." ← Correct by luck

Point at x = [8, 0]:

Truth: Far from Class 1, but within Class 2's large spread
      → Should be Class 2
LDA says: "It's past x₁ = 5? Yes. It's Class 2." ← Correct

Point at x = [3, 6]:

Truth: Far from Class 1's tight cluster (distance = √45 ≈ 6.7)
      Way too far! Should be Class 2.
LDA boundary: Linear, may misclassify based on x₁ position only
```

The linear boundary doesn't capture the different cluster shapes!

---

#### **Question 3: What Alternative to Use?**

**Answer: Use Quadratic Discriminant Analysis (QDA)**

**QDA relaxes the equal covariance assumption:**

```
LDA:  Σ₁ = Σ₂ = Σ  (forced to be equal)
QDA:  Σ₁ ≠ Σ₂     (each class gets its own)

QDA allows:
  - Class 1 to have small Σ₁
  - Class 2 to have large Σ₂
  - Curved (quadratic) decision boundary
```

---

**LDA vs QDA Comparison:**

| Feature | LDA | QDA |
|---------|-----|-----|
| **Assumption** | Equal Σ | Different Σ allowed |
| **Boundary** | Linear (hyperplane) | Curved (quadratic) |
| **Parameters** | Fewer (p² + p) | More (C × p² + p) |
| **Works best when** | Equal covariances | Unequal covariances |
| **Sample size needed** | Smaller OK | Needs more samples |

Where:
- p = # features
- C = # classes

---

**QDA decision boundary:**

```
Instead of:  wᵀx + b = 0  (linear)

QDA uses:    xᵀAx + bᵀx + c = 0  (quadratic)

A depends on Σ₁ and Σ₂ (different for each class)
```

---

**When to use each:**

```
Use LDA when:
  ✓ Classes have similar spread
  ✓ Small dataset (need parameter efficiency)
  ✓ Want interpretable linear boundary

Use QDA when:
  ✓ Classes have different shapes/sizes ← OUR CASE
  ✓ Enough data for more parameters
  ✓ Higher accuracy > interpretability
```

---

#### **Question 4: Sketch Why LDA Fails**

**Visual explanation:**

```
ORIGINAL 2D DATA:

  x₂ ↑
     │
   8 │               ■
     │          ■         ■
   6 │     ■                  ■
     │          ■         ■
   4 │     ■         ■
     │          ■
   2 │  ●●●
     │  ●●●        Class 2: spread out ■■■
   0 │  ●●●        (large Σ₂)
     │
  -2 │  Class 1: tight ●●●
     │  (small Σ₁)
     └───────────────────────────────→ x₁
        -2  0  2  4  6  8  10  12

LDA Decision Boundary (linear):
     │
     │        /
     │       /  ← Straight line
     │      /     Doesn't wrap around
     │     /      Class 1
     │    /
     │   /
     │  /
     │ /
     │/
```

**The problem:**
```
LDA's linear boundary:
  - Splits space with a straight line
  - Cannot create a "bubble" around Class 1
  - Misclassifies Class 2 points that are near but
    not inside Class 1's tight cluster

Better boundary (QDA):
  - Circular/elliptical around Class 1
  - Adapts to Class 1's small spread
  - Adapts to Class 2's large spread
```

---

**QDA Decision Boundary (curved):**

```
  x₂ ↑
     │
   8 │               ■
     │          ■         ■
   6 │     ■        ╱─╲       ■
     │          ■  │ ●●●│ ■
   4 │     ■       │●●●│
     │          ■  │ ●●●│
   2 │             ╲─╱
     │
   0 │        Circular boundary
     │        around Class 1 ← QDA creates this!
  -2 │
     └───────────────────────────────→ x₁

Now Class 1 is properly enclosed! ✓
Everything outside the circle → Class 2
```

---

**Mathematical intuition:**

```
LDA uses pooled covariance:
  Sᵂ = S₁ + S₂

When S₂ >> S₁:
  Sᵂ ≈ S₂  (dominated by larger class)

LDA treats BOTH classes as if they have spread ≈ S₂
→ Ignores Class 1's tightness
→ Poor boundary

QDA uses separate covariances:
  Class 1 uses Σ₁
  Class 2 uses Σ₂

Each class is modeled with its true shape ✓
→ Better boundary
```

---

**Real-world analogy:**

```
Imagine classifying:
  Class 1: Basketballs (all same size, tight cluster)
  Class 2: Beach balls (varying sizes, spread out)

LDA assumes:
  "All balls have the same size distribution"
  → Wrong! Misses that basketballs are uniform.

QDA recognizes:
  "Basketballs: tight size range"
  "Beach balls: wide size range"
  → Correct! Adapts to each class.
```

---

**Conclusion:**

When covariances differ significantly:
  1. LDA assumption is violated
  2. Linear boundary performs poorly
  3. Switch to QDA for curved boundary
  4. Accept increased model complexity for better accuracy

---

</details>

---

## 🎯 Summary & Tips

### How to Approach These Problems:

1. **Read carefully** — Note what's given vs what needs to be computed
2. **Write formulas first** — Before calculating, write down the relevant formula
3. **Show all steps** — Don't skip intermediate calculations
4. **Check units** — Make sure dimensions match (2×2 matrices, etc.)
5. **Verify answers** — Use properties like Sᵂ × Sᵂ⁻¹ = I to check

### Common Formula Patterns:

```
Means:           μₖ = (1/Nₖ) Σ xₙ
Projection:      y = wᵀ x
Scatter:         Sₖ = Σ (xₙ−μₖ)(xₙ−μₖ)ᵀ
Between:         Sʙ = (μ₂−μ₁)(μ₂−μ₁)ᵀ
LDA solution:    w* = Sᵂ⁻¹(μ₂−μ₁)
Fisher's J:      J = (m̃₂−m̃₁)² / (s₁²+s₂²)
Threshold:       t = (m̃₁ + m̃₂) / 2
2×2 inverse:     A⁻¹ = (1/det) × [d −b; −c a]
```

### Exam Strategy:

- ✅ **Memorize the 2×2 inverse formula** — Saves huge time
- ✅ **Practice outer products** — Key to scatter matrices
- ✅ **Know when LDA fails** — Equal covariance assumption
- ✅ **Understand QDA alternative** — Curved boundaries
- ✅ **Draw diagrams** — Visual understanding prevents mistakes

---

*Practice these problems multiple times until the steps become automatic!*
