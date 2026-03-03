# 🔢 Essence of Linear Algebra — PRACTICE PROBLEMS GUIDE
### 🎓 ODS | ML
> 🔗 **Navigation:** [← Back to INDEX](./Essence_of_Linear_Algebra_INDEX.md) | [← Theory Guide](./Essence_of_Linear_Algebra_THEORY.md)
>
> 🍎 **How to use this guide:** Every single step is explained as if you've NEVER seen it before. Nothing is assumed. Every rule is stated, every substitution shown, every simplification justified. Read top-to-bottom and you'll understand everything.

---

## 📚 Problem Index

| # | Problem | Concepts Tested | Theory Link |
|---|---------|-----------------|-------------|
| P1 | [Vector Addition & Scalar Multiplication](#-p1-vector-addition--scalar-multiplication) | Vector ops | [📘 Ch 1](./Essence_of_Linear_Algebra_THEORY.md#chapter-1--vectors-what-even-are-they) |
| P2 | [Linear Independence Test](#-p2-linear-independence-test) | Independence, det | [📘 Ch 2](./Essence_of_Linear_Algebra_THEORY.md#chapter-2--linear-combinations-span--basis-vectors) |
| P3 | [Span Geometric Description](#-p3-span-geometric-description) | Span, dependence | [📘 Ch 2](./Essence_of_Linear_Algebra_THEORY.md#chapter-2--linear-combinations-span--basis-vectors) |
| P4 | [Matrix as Transformation](#-p4-matrix-as-transformation) | Matrix-vector product | [📘 Ch 3](./Essence_of_Linear_Algebra_THEORY.md#chapter-3--linear-transformations--matrices) |
| P5 | [Matrix Multiplication (Composition)](#-p5-matrix-multiplication-composition) | Composition | [📘 Ch 4](./Essence_of_Linear_Algebra_THEORY.md#chapter-4--matrix-multiplication-as-composition) |
| P6 | [Rotation Matrix Composition](#-p6-rotation-matrix-composition) | Rotation, verify | [📘 Ch 4](./Essence_of_Linear_Algebra_THEORY.md#chapter-4--matrix-multiplication-as-composition) |
| P7 | [Determinant Computation](#-p7-determinant-computation--geometric-meaning) | 2×2, 3×3 det | [📘 Ch 6](./Essence_of_Linear_Algebra_THEORY.md#chapter-6--the-determinant) |
| P8 | [Finding the Inverse](#-p8-finding-the-inverse-matrix) | Inverse formula | [📘 Ch 7](./Essence_of_Linear_Algebra_THEORY.md#chapter-7--inverse-matrices-column-space--null-space) |
| P9 | [Column Space, Null Space, Rank](#-p9-column-space-null-space--rank) | Rank-Nullity | [📘 Ch 7](./Essence_of_Linear_Algebra_THEORY.md#chapter-7--inverse-matrices-column-space--null-space) |
| P10 | [Dot Product & Projection](#-p10-dot-product--projection) | Dot, angle, proj | [📘 Ch 9](./Essence_of_Linear_Algebra_THEORY.md#chapter-9--dot-products--duality) |
| P11 | [Cross Product](#-p11-cross-product) | Cross, perpendicular | [📘 Ch 10](./Essence_of_Linear_Algebra_THEORY.md#chapter-10--cross-products) |
| P12 | [Cramer's Rule](#-p12-cramers-rule) | Solve Ax=b | [📘 Ch 12](./Essence_of_Linear_Algebra_THEORY.md#chapter-12--cramers-rule-explained-geometrically) |
| P13 | [Change of Basis](#-p13-change-of-basis) | Basis conversion | [📘 Ch 13](./Essence_of_Linear_Algebra_THEORY.md#chapter-13--change-of-basis) |
| P14 | [Eigenvalues & Eigenvectors](#-p14-eigenvalues--eigenvectors-full-computation) | Full eigen | [📘 Ch 14](./Essence_of_Linear_Algebra_THEORY.md#chapter-14--eigenvectors--eigenvalues) |
| P15 | [Diagonalization & Matrix Power](#-p15-diagonalization--matrix-power) | A=PDP⁻¹, Aⁿ | [📘 Ch 14](./Essence_of_Linear_Algebra_THEORY.md#chapter-14--eigenvectors--eigenvalues) |
| P16 | [Mean-Product Eigenvalue Trick](#-p16-mean-product-eigenvalue-trick) | Quick eigen | [📘 Ch 15](./Essence_of_Linear_Algebra_THEORY.md#chapter-15--a-quick-trick-for-computing-eigenvalues) |
| P17 | [Vector Space Verification](#-p17-vector-space-verification) | Axioms | [📘 Ch 16](./Essence_of_Linear_Algebra_THEORY.md#chapter-16--abstract-vector-spaces) |
| P18 | [Derivative as Linear Transformation](#-p18-derivative-as-linear-transformation) | Function spaces | [📘 Ch 16](./Essence_of_Linear_Algebra_THEORY.md#chapter-16--abstract-vector-spaces) |

---

## 📖 RULES & FORMULAS — Read This First!

> Every rule below is used in the problems. Come back here whenever you see a rule name.

### 🔹 What IS a Vector?

```
  A VECTOR is just a list of numbers (an arrow from the origin).
  
  In 2D: v⃗ = [3, -1]  means "go 3 right, 1 down"
  In 3D: v⃗ = [1, 2, 5] means "go 1 right, 2 up, 5 forward"
  
  🍎 Kid version: A vector is like DIRECTIONS on a treasure map.
     [3, -1] means "walk 3 steps East, then 1 step South."
     
  The NUMBER of entries = the DIMENSION.
  [3, -1] lives in 2D.   [1, 2, 5] lives in 3D.
```

### 🔹 Vector Operations Cheat Sheet

```
  OPERATION            │  FORMULA                          │  WHEN TO USE
  ─────────────────────┼───────────────────────────────────┼──────────────────────
  Addition             │  [a,b]+[c,d] = [a+c, b+d]         │  combining two vectors
  Scalar multiplication│  k·[a,b] = [ka, kb]               │  stretching/shrinking
  Magnitude (length)   │  |v⃗| = √(v₁²+v₂²+...)             │  "how long is the arrow?"
  Linear combination   │  a·v⃗ + b·w⃗                        │  mixing vectors together
```

### 🔹 Matrix Operations Cheat Sheet

```
  A MATRIX is a grid of numbers. A 2×2 matrix has 2 rows, 2 columns.
  
  Matrix × Vector:  A·v⃗ = v₁·(column 1) + v₂·(column 2)
    OR: each entry = dot product of that ROW with the vector
  
  Matrix × Matrix (composition):
    Column j of (AB) = A applied to Column j of B
    OR: entry (i,j) = dot product of row i of A with column j of B
  
  ┌────────────────────── 2×2 FORMULAS ──────────────────────────┐
  │  Matrix:  A = [a  b]                                         │
  │               [c  d]                                         │
  │                                                              │
  │  Determinant:  det(A) = ad − bc                              │
  │  Inverse:      A⁻¹ = (1/(ad−bc)) · [d  −b]                   │
  │                                     [−c   a]                 │
  │  (Swap a↔d, negate b and c, divide everything by determinant)│
  └──────────────────────────────────────────────────────────────┘
```

### 🔹 Dot Product & Cross Product

```
  DOT PRODUCT (works in any dimension):
    v⃗·w⃗ = v₁w₁ + v₂w₂ + v₃w₃ + ...
    = |v⃗| · |w⃗| · cos(θ)     (where θ = angle between them)
    
    If v⃗·w⃗ = 0 → the vectors are PERPENDICULAR (90° angle)
  
  PROJECTION of w⃗ onto v⃗:
    proj_v(w⃗) = (v⃗·w⃗ / v⃗·v⃗) · v⃗
    
    🍎 "How much of w⃗ points in the v⃗ direction?"
  
  CROSS PRODUCT (3D only):
    v⃗ × w⃗ = [v₂w₃−v₃w₂,  v₃w₁−v₁w₃,  v₁w₂−v₂w₁]
    Result is a vector PERPENDICULAR to both v⃗ and w⃗.
    |v⃗ × w⃗| = area of parallelogram formed by v⃗ and w⃗.
```

### 🔹 Eigenvalues & Eigenvectors

```
  EIGENVALUE λ and EIGENVECTOR v⃗ satisfy:  A·v⃗ = λ·v⃗
  
  "The matrix just STRETCHES v⃗ by factor λ, doesn't change direction!"
  
  To FIND eigenvalues:  det(A − λI) = 0   (characteristic equation)
  To FIND eigenvectors: Solve (A − λI)·v⃗ = 0⃗  for each λ
  
  Quick 2×2 trick:
    m = (a+d)/2              (mean of diagonal = average eigenvalue)
    p = ad − bc              (product of eigenvalues = determinant)
    λ = m ± √(m² − p)
    
  DIAGONALIZATION: A = P·D·P⁻¹  →  Aⁿ = P·Dⁿ·P⁻¹
    P = matrix of eigenvectors as columns
    D = diagonal matrix of eigenvalues
```

### 🔹 Key Notations

```
  v⃗        = a vector (arrow with direction and length)
  î, ĵ, k̂  = standard basis vectors: [1,0,0], [0,1,0], [0,0,1]
  A⁻¹      = inverse of matrix A (the "undo" transformation)
  det(A)   = determinant (area/volume scaling factor)
  |v⃗|      = magnitude/length of vector v⃗
  λ        = eigenvalue (Greek letter "lambda")
  I        = identity matrix: [1,0; 0,1] (does nothing)
  span{...}= all possible linear combinations of the given vectors
  rank     = number of independent columns = dimension of column space
  nullity  = dimension of null space = number of "free" variables
  rank + nullity = number of columns (Rank-Nullity Theorem)
```

---
---

## 🧮 P1: Vector Addition & Scalar Multiplication

> 📘 Theory: [Ch 1 — Vectors](./Essence_of_Linear_Algebra_THEORY.md#chapter-1--vectors-what-even-are-they) | ⬆️ [Problem Index](#-problem-index)

### Problem: Given v⃗ = [3, -1] and w⃗ = [-2, 4]:
**(a)** Compute v⃗ + w⃗
**(b)** Compute 3v⃗ − 2w⃗
**(c)** Is [7, -6] a linear combination of v⃗ and w⃗?

---

### (a) v⃗ + w⃗

**What does vector addition mean?**
> You have TWO arrows. To ADD them, you add each matching component (each "slot") separately. First slot + first slot, second slot + second slot.

```
  v⃗ = [3, -1]     w⃗ = [-2, 4]
  
  Rule: [v₁ + w₁,  v₂ + w₂]
  
  First component:   3 + (-2) = 3 - 2 = 1
  Second component: -1 + 4    = 3
  
  ┌───────────────────────────┐
  │  v⃗ + w⃗ = [1, 3]  ✅       │
  └───────────────────────────┘
  
  🍎 Kid version: You're walking.
     v⃗ says "go 3 right, 1 down."
     w⃗ says "go 2 left, 4 up."
     Total trip: 1 right, 3 up → [1, 3]
```

---

### (b) 3v⃗ − 2w⃗

**What does scalar multiplication mean?**
> A "scalar" is just a single number (like 3 or -2). When you MULTIPLY a vector by a scalar, you multiply EVERY component by that number. It stretches (or shrinks/flips) the arrow.

**Step 1 — Compute 3v⃗ (scale v⃗ by 3):**
```
  3 · v⃗ = 3 · [3, -1]
  
  Multiply each component by 3:
    3 × 3 = 9        ← first component
    3 × (-1) = -3    ← second component
  
  3v⃗ = [9, -3]
  
  🍎 This means: take the arrow [3,-1] and make it 3× LONGER.
     It points the same direction, just stretched.
```

**Step 2 — Compute 2w⃗ (scale w⃗ by 2):**
```
  2 · w⃗ = 2 · [-2, 4]
  
  Multiply each component by 2:
    2 × (-2) = -4    ← first component
    2 × 4 = 8        ← second component
  
  2w⃗ = [-4, 8]
```

**Step 3 — Subtract: 3v⃗ − 2w⃗:**
```
  [9, -3] − [-4, 8]
  
  Subtraction = add each component with a sign flip:
    9 − (-4) = 9 + 4 = 13    ← first component
    -3 − 8 = -11               ← second component
    
  ┌─────────────────────────────────┐
  │  3v⃗ − 2w⃗ = [13, -11]  ✅        │
  └─────────────────────────────────┘
```

---

### (c) Is [7, -6] a linear combination of v⃗ and w⃗?

**What does "linear combination" mean?**
> Can we find numbers a and b such that a·v⃗ + b·w⃗ = [7, -6]?
> In other words: can we MIX v⃗ and w⃗ (stretch/flip/add them) to reach [7, -6]?

**Step 1 — Set up the equation:**
```
  a · [3, -1] + b · [-2, 4] = [7, -6]
  
  Left side: [3a, -a] + [-2b, 4b] = [3a - 2b,  -a + 4b]
  
  This must equal [7, -6], so we match EACH component:
  
    Component 1:  3a − 2b = 7     ... equation (i)
    Component 2:  −a + 4b = −6    ... equation (ii)
```

**Step 2 — Solve the system of equations:**
```
  From equation (ii), isolate a:
    −a + 4b = −6
    −a = −6 − 4b          (subtract 4b from both sides)
    a = 6 + 4b             (multiply both sides by −1)
    
  ┌───────────────────────────────────────────────┐
  │  WHY multiply by −1?                          │
  │  −a = −6 − 4b                                 │
  │  (−1)(−a) = (−1)(−6 − 4b)                     │
  │  a = 6 + 4b                                   │
  │ (Negatives cancel on left; distribute on right)│
  └───────────────────────────────────────────────┘
```

**Step 3 — Substitute a = 6 + 4b into equation (i):**
```
  3(6 + 4b) − 2b = 7
  
  Expand 3(6+4b):
    3×6 + 3×4b = 18 + 12b
  
  So: 18 + 12b − 2b = 7
      18 + 10b = 7        (combine 12b − 2b = 10b)
      10b = 7 − 18        (subtract 18 from both sides)
      10b = −11
      b = −11/10 = −1.1
```

**Step 4 — Find a:**
```
  a = 6 + 4b = 6 + 4(−1.1) = 6 + (−4.4) = 6 − 4.4 = 1.6
```

**Step 5 — VERIFY (always verify!):**
```
  1.6 · [3, -1] + (-1.1) · [-2, 4]
  = [1.6×3, 1.6×(-1)] + [(-1.1)×(-2), (-1.1)×4]
  = [4.8, -1.6] + [2.2, -4.4]
  = [4.8 + 2.2,  -1.6 + (-4.4)]
  = [7.0, -6.0]  ✅  (matches!)
  
  ┌──────────────────────────────────────────────────┐
  │  YES! [7, -6] = 1.6·v⃗ + (−1.1)·w⃗                 │
  │  It IS a linear combination of v⃗ and w⃗.          │
  └──────────────────────────────────────────────────┘
```

---

## 🧮 P2: Linear Independence Test

> 📘 Theory: [Ch 2 — Span & Basis](./Essence_of_Linear_Algebra_THEORY.md#chapter-2--linear-combinations-span--basis-vectors) | ⬆️ [Problem Index](#-problem-index)

### What IS Linear Independence?

```
  Vectors are LINEARLY INDEPENDENT if NO vector in the set
  can be made by mixing the others together.
  
  If you CAN write one as a combo of the rest → DEPENDENT (redundant)
  
  🍎 Kid version: Independent vectors point in "genuinely different" 
     directions. Dependent = one is just a stretched/flipped copy 
     of another (or a mix of others). It adds NO new direction.
  
  QUICK TESTS:
  ● For 2 vectors: check if one = k × (the other).
    If ratio of components is the SAME → dependent.
  ● For n vectors in n dimensions: compute the determinant.
    det ≠ 0 → INDEPENDENT.  det = 0 → DEPENDENT.
```

### (a) Are {[1, 2], [3, 6]} independent?

```
  Step 1: Check if [3, 6] is a scalar multiple of [1, 2].
  
    Is [3, 6] = k · [1, 2]  for some number k?
    
    Look at first components:  3/1 = 3    → k would be 3
    Look at second components: 6/2 = 3    → k would be 3
    
    The ratios are THE SAME! So: [3, 6] = 3 · [1, 2]
    
  ┌──────────────────────────────────────────────────────┐
  │  LINEARLY DEPENDENT ❌                               │
  │                                                      │
  │  [3, 6] is just [1, 2] stretched 3× longer.          │
  │  Both point in the SAME direction.                   │
  │  The second vector adds no new information.          │
  │                                                      │
  │      ▲ y                                             │
  │    6 │      · [3,6]                                  │
  │    4 │    ╱                                          │
  │    2 │  · [1,2]     same line!                       │
  │      │╱                                              │
  │  ────┼──────► x                                      │
  └──────────────────────────────────────────────────────┘
```

### (b) Are {[1,0,0], [0,1,0], [0,0,1]} independent?

```
  These are the STANDARD BASIS vectors î, ĵ, k̂ in 3D.
  
  Method: Compute the 3×3 determinant.
  
  Put them as columns of a matrix:
    A = [ 1  0  0 ]
        [ 0  1  0 ]
        [ 0  0  1 ]
    
    This is the IDENTITY matrix I.
  
  det(I):
    Using the 3×3 determinant formula:
    det = a(ei − fh) − b(di − fg) + c(dh − eg)
    
    Here: a=1,b=0,c=0,d=0,e=1,f=0,g=0,h=0,i=1
    
    = 1·(1·1 − 0·0) − 0·(anything) + 0·(anything)
    = 1·(1 − 0) − 0 + 0
    = 1·1 = 1
    
    det = 1 ≠ 0
  
  ┌──────────────────────────────────────────────────────┐
  │  LINEARLY INDEPENDENT ✅                             │
  │                                                      │
  │  î points purely right, ĵ purely up, k̂ purely forward│
  │  No one is a mix of the others!                      │
  │  They span ALL of 3D space.                          │
  └──────────────────────────────────────────────────────┘
```

### (c) Are {[1, 2], [3, 4]} independent?

```
  Step 1: Check scalar multiple.
    Is [3, 4] = k · [1, 2]?
    
    First components:  3/1 = 3
    Second components: 4/2 = 2
    
    3 ≠ 2 → ratios are DIFFERENT → NOT a scalar multiple!
    
  Step 2: Confirm with determinant.
    A = [1  3]
        [2  4]
    
    det(A) = 1·4 − 3·2 = 4 − 6 = −2
    
    −2 ≠ 0
    
  ┌──────────────────────────────────────────────────────┐
  │  LINEARLY INDEPENDENT ✅                             │
  │                                                      │
  │  These two vectors point in genuinely different      │
  │  directions. Together they can reach ANY point       │
  │  in 2D space (they span all of ℝ²).                  │
  └──────────────────────────────────────────────────────┘
```

---

## 🧮 P3: Span Geometric Description

> 📘 Theory: [Ch 2](./Essence_of_Linear_Algebra_THEORY.md#chapter-2--linear-combinations-span--basis-vectors) | ⬆️ [Problem Index](#-problem-index)

### What IS Span?

```
  span{v⃗₁, v⃗₂, ...} = the set of ALL vectors you can make
  by mixing v⃗₁, v⃗₂, ... with any combination of stretches and adds.
  
  🍎 Kid version: If you can only walk in the directions v⃗₁ and v⃗₂
     (forward, backward, any amount), what places can you reach?
     THAT set of places = the span.
```

### Problem: What is the span of {[1, 2], [2, 4]}?

**Step 1 — Check if vectors are dependent:**
```
  Is [2, 4] = k · [1, 2]?
  
  2/1 = 2,  4/2 = 2.  Same ratio!
  
  [2, 4] = 2 · [1, 2]   →  DEPENDENT! They point the SAME direction.
```

**Step 2 — Any linear combination simplifies:**
```
  a · [1, 2] + b · [2, 4]
  = a · [1, 2] + b · 2 · [1, 2]     ← because [2,4] = 2·[1,2]
  = a · [1, 2] + 2b · [1, 2]
  = (a + 2b) · [1, 2]
  
  No matter WHAT a and b you pick, you always get
  "some number" × [1, 2].
  
  This means the result is ALWAYS a multiple of [1, 2]!
```

**Step 3 — Geometric description:**
```
  Multiples of [1, 2] form a LINE through the origin.
  
  What line? The direction [1, 2] means: for every 1 step in x,
  go 2 steps in y. That's the line y = 2x.
  
  ┌──────────────────────────────────────────────────┐
  │  Span = the LINE y = 2x                          │
  │                                                  │
  │       ▲ y                                        │
  │       │  ╱ all multiples of [1,2]                │
  │       │ ╱                                        │
  │  ─────┼╱──────► x                                │
  │       │╱                                         │
  │                                                  │
  │  You CAN'T reach [1, 0] or [0, 1] or [3, 5]!     │
  │  Only points on this one line.                   │
  │                                                  │
  │  🍎 Two dependent vectors give the same span     │
  │     as ONE vector — just a line, not a plane.    │
  └──────────────────────────────────────────────────┘
```

---

## 🧮 P4: Matrix as Transformation

> 📘 Theory: [Ch 3 — Transforms](./Essence_of_Linear_Algebra_THEORY.md#chapter-3--linear-transformations--matrices) | ⬆️ [Problem Index](#-problem-index)

### What IS a Matrix Transformation?

```
  A matrix is a MACHINE that moves/stretches/rotates space.
  
  A 2×2 matrix A = [a  b]  tells you:
                    [c  d]
  
  Column 1 = [a, c] = where the vector î = [1, 0] LANDS after transformation
  Column 2 = [b, d] = where the vector ĵ = [0, 1] LANDS after transformation
  
  To transform ANY vector [x, y]:
    Result = x · (column 1) + y · (column 2)
    
  🍎 Kid version: The matrix tells you "î goes HERE, ĵ goes HERE."
     Every other vector is built from î and ĵ, so it follows along!
```

### Problem: A = [[2, 1], [0, 3]].
**(a)** Where does î land? **(b)** Where does ĵ land? **(c)** Where does [4, -1] go? **(d)** What happens to the unit square?

### (a) Where does î land?

```
  î = [1, 0] = the arrow pointing 1 unit to the right.
  
  After transformation: î lands at COLUMN 1 of A.
  
  Column 1 = [2, 0]
  
  ┌────────────────────────────────────────────┐
  │  î lands at [2, 0]  ✅                     │
  │                                            │
  │  Meaning: the right-pointing arrow         │
  │  gets STRETCHED to be 2× longer,           │
  │  but stays on the x-axis.                  │
  └────────────────────────────────────────────┘
```

### (b) Where does ĵ land?

```
  ĵ = [0, 1] = the arrow pointing 1 unit upward.
  
  After transformation: ĵ lands at COLUMN 2 of A.
  
  Column 2 = [1, 3]
  
  ┌────────────────────────────────────────────┐
  │  ĵ lands at [1, 3]  ✅                     │
  │                                            │
  │  Meaning: the upward arrow gets TILTED     │
  │  to the right by 1 AND stretched upward    │
  │  to height 3.                              │
  └────────────────────────────────────────────┘
```

### (c) Where does [4, -1] go?

**Method: Column Combination (the "geometric" way)**

```
  Rule: result = x · (column 1) + y · (column 2)
  
  Here x = 4, y = -1:
  
  Step 1: Scale column 1 by x = 4.
    4 · [2, 0] = [4×2, 4×0] = [8, 0]
  
  Step 2: Scale column 2 by y = -1.
    (-1) · [1, 3] = [(-1)×1, (-1)×3] = [-1, -3]
  
  Step 3: ADD the two results.
    [8, 0] + [-1, -3] = [8 + (-1),  0 + (-3)] = [7, -3]
    
  ┌────────────────────────┐
  │  A · [4, -1] = [7, -3] │
  └────────────────────────┘
```

**Verify with Row-Dot-Product method:**

```
  This is the "standard" matrix multiplication you may know:
  
  Row 1 of A = [2, 1].  Dot with [4, -1]:
    2×4 + 1×(-1) = 8 + (-1) = 7     ← first component of result ✅
    
  Row 2 of A = [0, 3].  Dot with [4, -1]:
    0×4 + 3×(-1) = 0 + (-3) = -3    ← second component of result ✅
    
  Result: [7, -3]  ✅  (both methods agree!)
  
  ┌───────────────────────────────────────────────────────┐
  │  WHY two methods?                                     │
  │                                                       │
  │  Column method: "4 copies of where-î-lands PLUS       │
  │                  -1 copies of where-ĵ-lands"          │
  │  Row method:    "dot each row with the input vector"  │
  │                                                       │
  │  They ALWAYS give the same answer.                    │
  │  Column method = geometric intuition.                 │
  │  Row method = faster for computation.                 │
  └───────────────────────────────────────────────────────┘
```

### (d) What happens to the unit square?

```
  The unit square has corners at (0,0), (1,0), (0,1), (1,1).
  Transform each corner:
  
  (0,0): A·[0,0] = 0·[2,0] + 0·[1,3] = [0, 0]
         Origin ALWAYS stays at origin for linear transforms.
  
  (1,0): This is î → lands at [2, 0]  (column 1)
  
  (0,1): This is ĵ → lands at [1, 3]  (column 2)
  
  (1,1): This is î + ĵ → [2,0] + [1,3] = [3, 3]
  
  Original square         →    Transformed parallelogram
    (0,1)──(1,1)                 (1,3)───(3,3)
      │      │                  ╱       ╱
      │      │         →      ╱       ╱
    (0,0)──(1,0)           (0,0)───(2,0)
  
  AREA of new shape:
    Area = |det(A)| = |2×3 − 1×0| = |6 − 0| = 6
    
    Original unit square had area 1.
    New parallelogram has area 6.
    The transformation STRETCHED areas by factor 6!
```

---

## 🧮 P5: Matrix Multiplication (Composition)

> 📘 Theory: [Ch 4](./Essence_of_Linear_Algebra_THEORY.md#chapter-4--matrix-multiplication-as-composition) | ⬆️ [Problem Index](#-problem-index)

### What IS Matrix Multiplication?

```
  Multiplying matrices M₂ · M₁ means:
  "FIRST apply transformation M₁, THEN apply M₂."
  
  It's like a two-step machine:
    Input → [M₁ transforms it] → [M₂ transforms THAT result] → Output
  
  The product M₂·M₁ is a SINGLE matrix that does BOTH steps at once!
  
  🍎 Kid version: First rotate, then stretch.
     Matrix multiplication finds the ONE matrix that does both.
     
  ⚠️ ORDER MATTERS! M₂·M₁ ≠ M₁·M₂ (usually)
     "Rotate then stretch" ≠ "Stretch then rotate"
```

### Problem: Compute M₂·M₁ where M₁ = [[1,-1],[1,1]], M₂ = [[0,1],[1,0]]

**Method 1: Track Basis Vectors (Geometric Way)**

```
  We need to track where î and ĵ end up after BOTH transformations.
  
  ── Step 1: Where does î go? ──
  
    M₁ sends î to column 1 of M₁ = [1, 1]
    (First transformation: î moves to [1,1])
    
    Now M₂ sends [1, 1] to:
      1 · (col1 of M₂) + 1 · (col2 of M₂)
      = 1 · [0, 1] + 1 · [1, 0]
      = [0, 1] + [1, 0]
      = [1, 1]
    
    î ends up at [1, 1] → this is COLUMN 1 of the product.
  
  ── Step 2: Where does ĵ go? ──
  
    M₁ sends ĵ to column 2 of M₁ = [-1, 1]
    
    Now M₂ sends [-1, 1] to:
      (-1) · [0, 1] + 1 · [1, 0]
      = [0, -1] + [1, 0]
      = [1, -1]
    
    ĵ ends up at [1, -1] → this is COLUMN 2 of the product.
  
  ┌──────────────────────────────────┐
  │  M₂ · M₁ = [ 1    1 ]            │
  │             [ 1   -1 ]  ✅       │
  └──────────────────────────────────┘
```

**Method 2: Row-Column Formula (Verify)**

```
  Entry (i,j) = dot product of row i of M₂ with column j of M₁.
  
  M₂ = [0  1]    M₁ = [ 1  -1]
       [1  0]         [ 1   1]
  
  Entry (1,1): Row 1 of M₂ · Col 1 of M₁
    = [0,1] · [1,1] = 0×1 + 1×1 = 0 + 1 = 1  ✅
    
  Entry (1,2): Row 1 of M₂ · Col 2 of M₁
    = [0,1] · [-1,1] = 0×(-1) + 1×1 = 0 + 1 = 1  ✅
    
  Entry (2,1): Row 2 of M₂ · Col 1 of M₁
    = [1,0] · [1,1] = 1×1 + 0×1 = 1 + 0 = 1  ✅
    
  Entry (2,2): Row 2 of M₂ · Col 2 of M₁
    = [1,0] · [-1,1] = 1×(-1) + 0×1 = -1 + 0 = -1  ✅
  
  Result: [1, 1; 1, -1]  ✅  (matches!)
```

---

## 🧮 P6: Rotation Matrix Composition

> 📘 Theory: [Ch 4](./Essence_of_Linear_Algebra_THEORY.md#chapter-4--matrix-multiplication-as-composition) | ⬆️ [Problem Index](#-problem-index)

### What IS the Rotation Matrix?

```
  R(θ) rotates every vector by angle θ counterclockwise.
  
  R(θ) = [ cos θ    -sin θ ]
         [ sin θ     cos θ ]
  
  WHY? After rotation by θ:
    î = [1,0] lands at [cos θ, sin θ]     → Column 1
    ĵ = [0,1] lands at [-sin θ, cos θ]    → Column 2
```

### (a) Compute R(90°)

```
  We need cos(90°) and sin(90°).
  
  cos(90°) = 0       (on the unit circle, 90° is at the top: x=0)
  sin(90°) = 1       (on the unit circle, 90° is at the top: y=1)
  
  R(90°) = [ cos 90°    -sin 90° ] = [ 0    -1 ]
           [ sin 90°     cos 90° ]   [ 1     0 ]
  
  ┌────────────────────────────────────────────────┐
  │  R(90°) = [ 0   -1 ]  ✅                       │
  │           [ 1    0 ]                           │
  │                                                │
  │  Check: î=[1,0] → [0·1+(-1)·0, 1·1+0·0]=[0,1]  │
  │  That's ĵ! So î rotated 90° counterclockwise   │
  │  indeed lands pointing straight up. ✅         │
  └────────────────────────────────────────────────┘
```

### (b) Verify R(90°)² = R(180°)

**Step 1: Compute R(90°)²  = R(90°) · R(90°):**
```
  R(90°) = [0, -1; 1, 0]
  
  [0  -1] · [0  -1]
  [1   0]   [1   0]
  
  Entry (1,1): [0,-1]·[0,1] = 0×0 + (-1)×1 = -1
  Entry (1,2): [0,-1]·[-1,0] = 0×(-1) + (-1)×0 = 0
  Entry (2,1): [1,0]·[0,1] = 1×0 + 0×1 = 0
  Entry (2,2): [1,0]·[-1,0] = 1×(-1) + 0×0 = -1
  
  R(90°)² = [-1   0]
            [ 0  -1]
```

**Step 2: Compute R(180°) directly:**
```
  cos(180°) = -1      sin(180°) = 0
  
  R(180°) = [-1    0]
            [ 0   -1]
```

**Step 3: Compare:**
```
  R(90°)² = [-1, 0; 0, -1]
  R(180°)  = [-1, 0; 0, -1]
  
  THEY'RE IDENTICAL!  ✅
  
  🍎 Makes perfect sense: rotating 90° TWICE = rotating 180° once!
     Just like turning left at a street corner twice means you turned around.
```

### (c) What is R(θ)⁻¹?

```
  R(θ)⁻¹ = R(−θ)     "Rotating BACKWARD by θ undoes the rotation"
  
  R(−θ) = [ cos(−θ)    -sin(−θ) ]
          [ sin(−θ)     cos(−θ)  ]
  
  Using trig identities:
    cos(−θ) = cos(θ)      (cosine is EVEN: symmetric)
    sin(−θ) = −sin(θ)     (sine is ODD: flips sign)
  
  R(−θ) = [ cos θ     sin θ ]
          [ -sin θ    cos θ ]
  
  ┌──────────────────────────────────────────────────┐
  │  R(θ)⁻¹ = R(−θ) = [ cos θ    sin θ  ]  ✅        │
  │                     [-sin θ    cos θ  ]          │
  │                                                  │
  │  Notice: this is the TRANSPOSE of R(θ)!          │
  │  For rotation matrices: R⁻¹ = Rᵀ (always!)       │
  │                                                  │
  │  det(R(θ)) = cos²θ + sin²θ = 1 ≠ 0               │
  │  So the inverse always exists. ✅                │
  └──────────────────────────────────────────────────┘
```

---

## 🧮 P7: Determinant Computation & Geometric Meaning

> 📘 Theory: [Ch 6 — Determinant](./Essence_of_Linear_Algebra_THEORY.md#chapter-6--the-determinant) | ⬆️ [Problem Index](#-problem-index)

### What IS the Determinant?

```
  The determinant tells you HOW MUCH a matrix transformation
  STRETCHES or SQUISHES area (in 2D) or volume (in 3D).
  
  For A = [a  b], det(A) = a·d − b·c
          [c  d]
  
  ● |det| > 1  → areas get BIGGER (stretching)
  ● |det| = 1  → areas stay the SAME (rotation, reflection)
  ● |det| < 1  → areas get SMALLER (squishing)
  ● det = 0    → space gets CRUSHED to a lower dimension (flat!)
  ● det < 0    → orientation FLIPS (like looking in a mirror)
  
  🍎 Kid version: Determinant = "area multiplier."
     If det=6, a 1cm² square becomes 6cm² after transformation.
     If det=0, everything gets squashed flat (no area at all!).
```

### (a) det([[3, 0], [0, 2]])

```
  A = [3  0]
      [0  2]
      
  det(A) = a·d − b·c = 3·2 − 0·0 = 6 − 0 = 6
  
  ┌────────────────────────────────────────────────────┐
  │  det = 6  ✅                                       │
  │                                                    │
  │  What this matrix DOES:                            │
  │    î=[1,0] → [3,0]  (stretches x by 3)             │
  │    ĵ=[0,1] → [0,2]  (stretches y by 2)             │
  │                                                    │
  │  A 1×1 square becomes a 3×2 rectangle = area 6     │
  │  det > 0 → orientation preserved (no flipping)     │
  └────────────────────────────────────────────────────┘
```

### (b) det([[1, 2], [3, 6]])

```
  A = [1  2]
      [3  6]
      
  det(A) = 1·6 − 2·3 = 6 − 6 = 0
  
  ┌────────────────────────────────────────────────────┐
  │  det = 0  ✅                                       │
  │                                                    │
  │  ZERO determinant! This is special!                │
  │                                                    │
  │  WHY? Check the columns:                           │
  │    Col 1 = [1, 3]    Col 2 = [2, 6]                │
  │    [2, 6] = 2 · [1, 3]   → PARALLEL!               │
  │                                                    │
  │  Both columns point the same direction.            │
  │  The entire 2D plane gets SQUISHED onto a line.    │
  │  No area survives → det = 0.                       │
  │                                                    │
  │  ⚠️ det = 0 means:                                 │
  │    • Matrix has NO inverse                         │
  │    • Ax = b may have NO solution or infinite many  │
  │    • Information is lost (can't undo the squish)   │
  └────────────────────────────────────────────────────┘
```

### (c) det([[-1, 0], [0, -1]])

```
  A = [-1   0]
      [ 0  -1]
      
  det(A) = (-1)·(-1) − 0·0 = 1 − 0 = 1
  
  ┌────────────────────────────────────────────────────┐
  │  det = 1  ✅                                       │
  │                                                    │
  │  What this matrix does:                            │
  │    î=[1,0] → [-1,0]  (flipped left)                │
  │    ĵ=[0,1] → [0,-1]  (flipped down)               │
  │    [x,y] → [-x,-y]   (everything through origin!) │
  │                                                    │
  │  This is a 180° ROTATION.                          │
  │  Areas unchanged (|det|=1), orientation preserved. │
  │  (Two flips = no net flip → det positive)          │
  └────────────────────────────────────────────────────┘
```

---

## 🧮 P8: Finding the Inverse Matrix

> 📘 Theory: [Ch 7 — Inverse](./Essence_of_Linear_Algebra_THEORY.md#chapter-7--inverse-matrices-column-space--null-space) | ⬆️ [Problem Index](#-problem-index)

### What IS an Inverse Matrix?

```
  A⁻¹ is the transformation that UNDOES what A did.
  
  If A rotates clockwise 30°, then A⁻¹ rotates counterclockwise 30°.
  If A stretches by 2, then A⁻¹ shrinks by 1/2.
  
  A · A⁻¹ = I = A⁻¹ · A    (doing A then A⁻¹ = doing nothing = identity)
  
  A⁻¹ exists ONLY when det(A) ≠ 0.
  If det = 0, information was destroyed — you can't undo it!
  
  🍎 Kid version: A⁻¹ is the "undo button" for the transformation A.
  
  FORMULA for 2×2:
    A = [a  b]  →  A⁻¹ = (1/det) · [ d  -b]
        [c  d]                      [-c   a]
    
    RECIPE:
    1. Compute det = ad − bc
    2. SWAP a and d (diagonal elements switch places)
    3. NEGATE b and c (off-diagonal get minus signs)
    4. DIVIDE everything by det
```

### Problem: Find A⁻¹ for A = [[4, 7], [2, 6]] and verify.

**Step 1 — Compute the determinant:**
```
  A = [4  7]
      [2  6]
  
  det(A) = a·d − b·c = 4·6 − 7·2 = 24 − 14 = 10
  
  det = 10 ≠ 0  → Inverse EXISTS! (we can proceed)
```

**Step 2 — Apply the formula:**
```
  A⁻¹ = (1/det) · [ d   -b ]
                   [-c    a ]
  
  Swap a↔d:   a=4, d=6  →  swap to get 6 and 4
  Negate b,c: b=7→-7,  c=2→-2
  
  A⁻¹ = (1/10) · [ 6   -7 ]
                  [-2    4 ]
  
  Divide each entry by 10:
  
  A⁻¹ = [ 6/10    -7/10 ] = [ 0.6   -0.7 ]
        [-2/10     4/10 ]   [-0.2    0.4 ]
```

**Step 3 — VERIFY: A · A⁻¹ should = Identity:**
```
  A · A⁻¹ = [4, 7] · [ 0.6  -0.7]
            [2, 6]   [-0.2   0.4]
  
  Entry (1,1): Row 1 of A · Col 1 of A⁻¹
    = 4×0.6 + 7×(-0.2)
    = 2.4 + (-1.4)
    = 2.4 − 1.4 = 1.0  ✅
    
  Entry (1,2): Row 1 of A · Col 2 of A⁻¹
    = 4×(-0.7) + 7×0.4
    = -2.8 + 2.8
    = 0  ✅
    
  Entry (2,1): Row 2 of A · Col 1 of A⁻¹
    = 2×0.6 + 6×(-0.2)
    = 1.2 + (-1.2)
    = 0  ✅
    
  Entry (2,2): Row 2 of A · Col 2 of A⁻¹
    = 2×(-0.7) + 6×0.4
    = -1.4 + 2.4
    = 1.0  ✅
  
  A · A⁻¹ = [1  0] = I  ✅  (It's the identity! Inverse confirmed.)
            [0  1]
```

---

## 🧮 P9: Column Space, Null Space & Rank

> 📘 Theory: [Ch 7](./Essence_of_Linear_Algebra_THEORY.md#chapter-7--inverse-matrices-column-space--null-space) | ⬆️ [Problem Index](#-problem-index)

### Key Concepts Explained:

```
  COLUMN SPACE: All possible outputs of the matrix A.
    "What vectors can A·x⃗ produce?"
    = span of the columns of A.
  
  NULL SPACE: All inputs that A sends to the zero vector.
    "Which vectors x⃗ satisfy A·x⃗ = 0⃗?"
    These vectors "die" (get crushed to nothing).
  
  RANK: The number of truly independent columns.
    = dimension of the column space.
  
  NULLITY: Dimension of the null space.
  
  RANK-NULLITY THEOREM: rank + nullity = number of columns
    🍎 "independent directions used" + "directions crushed" = total directions
```

### Problem: A = [[1,2,1], [2,4,2], [3,6,3]]. Find (a) det, (b) rank, (c) column space, (d) null space.

### (a) Determinant

```
  First, NOTICE something:
    Row 2 = [2, 4, 2] = 2 × [1, 2, 1] = 2 × Row 1
    Row 3 = [3, 6, 3] = 3 × [1, 2, 1] = 3 × Row 1
    
  ALL rows are multiples of Row 1!
  
  When rows are dependent → det = 0.
  
  ┌───────────────────────────────────────────────────┐
  │  det(A) = 0  ✅                                   │
  │                                                   │
  │  WHY intuitively? If all rows are multiples of    │
  │  one row, the matrix squishes 3D space down to    │
  │  something smaller. Volume = 0 → det = 0.         │
  └───────────────────────────────────────────────────┘
```

### (b) Rank

```
  Look at the columns:
    Col 1 = [1, 2, 3]
    Col 2 = [2, 4, 6] = 2 × [1, 2, 3] = 2 × Col 1
    Col 3 = [1, 2, 3] = 1 × Col 1
    
  ALL three columns are multiples of [1, 2, 3]!
  Only ONE independent column.
  
  ┌────────────────────────┐
  │  rank = 1  ✅          │
  └────────────────────────┘
```

### (c) Column Space

```
  Column space = span of all columns = span{[1,2,3], [2,4,6], [1,2,3]}
  
  But since Col 2 and Col 3 are just multiples of Col 1:
  
  Column space = span{[1, 2, 3]}
  
  This is a LINE through the origin in the direction [1, 2, 3].
  
  ┌─────────────────────────────────────────────────────┐
  │  Column space = the line through origin in          │
  │  direction [1, 2, 3]                                │
  │                                                     │
  │  Meaning: No matter WHAT vector x⃗ you input,        │
  │  A·x⃗ will ALWAYS be some multiple of [1, 2, 3].     │
  │  The output is forever stuck on this one line!      │
  └─────────────────────────────────────────────────────┘
```

### (d) Null Space

```
  We need all x⃗ = [x, y, z] such that A·x⃗ = [0, 0, 0].
  
  A·x⃗ = [1·x + 2·y + 1·z]   [0]
         [2·x + 4·y + 2·z] = [0]
         [3·x + 6·y + 3·z]   [0]
  
  Look: Row 2 = 2×Row 1, Row 3 = 3×Row 1.
  So ALL three equations say the SAME thing:
  
    x + 2y + z = 0     ← only ONE independent equation!
  
  We have 3 unknowns but only 1 equation.
  That means 2 variables are FREE (we can pick them freely).
  
  Let's pick y and z as free variables:
  
  ── Choice 1: y = 1, z = 0 ──
    x + 2(1) + 0 = 0  →  x = -2
    Solution: [-2, 1, 0]
    
  ── Choice 2: y = 0, z = 1 ──
    x + 2(0) + 1 = 0  →  x = -1
    Solution: [-1, 0, 1]
  
  Null space = span{[-2, 1, 0], [-1, 0, 1]}
  
  This is a 2D PLANE through the origin in 3D space!
  
  ── Verify both vectors: ──
    A·[-2,1,0] = [1(-2)+2(1)+1(0), 2(-2)+4(1)+2(0), 3(-2)+6(1)+3(0)]
               = [-2+2+0, -4+4+0, -6+6+0] = [0, 0, 0]  ✅
    
    A·[-1,0,1] = [1(-1)+2(0)+1(1), 2(-1)+4(0)+2(1), 3(-1)+6(0)+3(1)]
               = [-1+0+1, -2+0+2, -3+0+3] = [0, 0, 0]  ✅
  
  ── Rank-Nullity check: ──
    rank + nullity = number of columns
    1 + 2 = 3  ✅
```

---

## 🧮 P10: Dot Product & Projection

> 📘 Theory: [Ch 9 — Dot Products](./Essence_of_Linear_Algebra_THEORY.md#chapter-9--dot-products--duality) | ⬆️ [Problem Index](#-problem-index)

### What IS the Dot Product?

```
  The dot product takes two vectors and returns a single NUMBER.
  
  v⃗ · w⃗ = v₁w₁ + v₂w₂ + v₃w₃     (multiply matching slots, add up)
  
  What does this number MEAN?
    v⃗ · w⃗ = |v⃗| · |w⃗| · cos(θ)
    
    • If positive → vectors point roughly the SAME direction (θ < 90°)
    • If zero     → vectors are PERPENDICULAR (θ = 90°)
    • If negative → vectors point roughly OPPOSITE (θ > 90°)
  
  🍎 Kid version: "How much do these two arrows agree in direction?"
     If they point the same way → big positive number.
     If they're at right angles → zero.
     If they oppose each other → negative.
```

### Problem: v⃗ = [1, 2, 3], w⃗ = [4, -5, 6].
**(a)** v⃗ · w⃗ **(b)** perpendicular? **(c)** projection of w⃗ onto v⃗

### (a) Compute v⃗ · w⃗

```
  v⃗ · w⃗ = v₁w₁ + v₂w₂ + v₃w₃
  
  = 1×4 + 2×(-5) + 3×6
  
  Compute each term:
    1 × 4 = 4
    2 × (-5) = -10
    3 × 6 = 18
    
  Add them up: 4 + (-10) + 18 = 4 - 10 + 18 = 12
  
  ┌──────────────────────┐
  │  v⃗ · w⃗ = 12  ✅      │
  └──────────────────────┘
```

### (b) Are they perpendicular?

```
  Vectors are perpendicular ⟺ their dot product = 0.
  
  v⃗ · w⃗ = 12 ≠ 0
  
  ┌──────────────────────────────────────────┐
  │  NOT perpendicular ❌                    │
  │                                          │
  │  Since 12 > 0, they point somewhat in    │
  │  the same general direction.             │
  └──────────────────────────────────────────┘
```

### (c) Projection of w⃗ onto v⃗

**What IS a projection?**
```
  The projection answers: "If I shine a light straight down onto 
  the line of v⃗, where does w⃗'s shadow land?"
  
  It's the COMPONENT of w⃗ that lies in the v⃗ direction.
  
  Formula: proj_v(w⃗) = (v⃗ · w⃗) / (v⃗ · v⃗)  ×  v⃗
  
  The (v⃗·w⃗)/(v⃗·v⃗) part gives us a NUMBER (how much to scale v⃗).
  Then we multiply v⃗ by that number.
```

**Step 1 — Compute v⃗ · v⃗:**
```
  v⃗ · v⃗ = 1×1 + 2×2 + 3×3 = 1 + 4 + 9 = 14
  
  (This is also |v⃗|² — the squared length of v⃗)
```

**Step 2 — Compute the scalar coefficient:**
```
  v⃗ · w⃗ / v⃗ · v⃗ = 12 / 14 = 6/7 ≈ 0.857
```

**Step 3 — Scale v⃗ by this coefficient:**
```
  proj = (6/7) · [1, 2, 3]
       = [6/7, 12/7, 18/7]
       ≈ [0.857, 1.714, 2.571]
  
  ┌────────────────────────────────────────────────────┐
  │  proj_v(w⃗) = [6/7, 12/7, 18/7]  ✅                 │
  │                                                    │
  │  This vector lies exactly along the v⃗ direction.   │
  │  It's the "shadow" of w⃗ cast onto the v⃗ line.      │
  │                                                    │
  │  🤖 AI/ML: Projections are the heart of PCA!       │
  │  "Project high-dimensional data onto the           │
  │   direction of maximum variance."                  │
  └────────────────────────────────────────────────────┘
```

---

## 🧮 P11: Cross Product

> 📘 Theory: [Ch 10 — Cross Products](./Essence_of_Linear_Algebra_THEORY.md#chapter-10--cross-products) | ⬆️ [Problem Index](#-problem-index)

### What IS the Cross Product?

```
  The cross product takes two 3D vectors and returns a NEW VECTOR
  that is PERPENDICULAR to BOTH of them.
  
  v⃗ × w⃗ = a vector ⊥ to v⃗ AND ⊥ to w⃗
  
  Its MAGNITUDE = area of the parallelogram formed by v⃗ and w⃗.
  
  Formula (MEMORIZE the pattern):
    v⃗ × w⃗ = [ v₂w₃ − v₃w₂ ]     ← "2,3 minus 3,2"
             [ v₃w₁ − v₁w₃ ]     ← "3,1 minus 1,3"
             [ v₁w₂ − v₂w₁ ]     ← "1,2 minus 2,1"
  
  🍎 Memory trick: go in CYCLIC order (1→2→3→1→2→3...)
     Component 1 uses indices 2,3
     Component 2 uses indices 3,1
     Component 3 uses indices 1,2
     Each time: "first pair minus swapped pair"
```

### Problem: v⃗ = [2, 3, 4], w⃗ = [5, 6, 7].
**(a)** v⃗ × w⃗ **(b)** verify perpendicular **(c)** parallelogram area

### (a) Compute v⃗ × w⃗

```
  v⃗ = [2, 3, 4]    (v₁=2, v₂=3, v₃=4)
  w⃗ = [5, 6, 7]    (w₁=5, w₂=6, w₃=7)
  
  Component 1 (use indices 2,3):
    v₂×w₃ − v₃×w₂ = 3×7 − 4×6 = 21 − 24 = -3
    
  Component 2 (use indices 3,1):
    v₃×w₁ − v₁×w₃ = 4×5 − 2×7 = 20 − 14 = 6
    
  Component 3 (use indices 1,2):
    v₁×w₂ − v₂×w₁ = 2×6 − 3×5 = 12 − 15 = -3
  
  ┌──────────────────────────────────┐
  │  v⃗ × w⃗ = [-3, 6, -3]  ✅         │
  └──────────────────────────────────┘
```

### (b) Verify it's perpendicular to both

```
  A vector is perpendicular to another ⟺ their dot product = 0.
  
  Check: [-3, 6, -3] · v⃗ = [-3, 6, -3] · [2, 3, 4]
    = (-3)×2 + 6×3 + (-3)×4
    = -6 + 18 + (-12)
    = -6 + 18 - 12 = 0  ✅  Perpendicular to v⃗!
  
  Check: [-3, 6, -3] · w⃗ = [-3, 6, -3] · [5, 6, 7]
    = (-3)×5 + 6×6 + (-3)×7
    = -15 + 36 + (-21)
    = -15 + 36 - 21 = 0  ✅  Perpendicular to w⃗!
  
  Both dot products are zero → cross product is perpendicular to BOTH! ✅
```

### (c) Parallelogram area

```
  Area = |v⃗ × w⃗| = magnitude of [-3, 6, -3]
  
  |[-3, 6, -3]| = √((-3)² + 6² + (-3)²)
                = √(9 + 36 + 9)
                = √54
  
  Simplify √54:
    54 = 9 × 6
    √54 = √9 × √6 = 3√6 ≈ 3 × 2.449 ≈ 7.35
  
  ┌────────────────────────────────────────────────┐
  │  Area = 3√6 ≈ 7.35 square units  ✅            │
  │                                                │
  │  This is the area of the parallelogram whose   │
  │  sides are v⃗ and w⃗.                            │
  └────────────────────────────────────────────────┘
```

---

## 🧮 P12: Cramer's Rule

> 📘 Theory: [Ch 12 — Cramer's Rule](./Essence_of_Linear_Algebra_THEORY.md#chapter-12--cramers-rule-explained-geometrically) | ⬆️ [Problem Index](#-problem-index)

### What IS Cramer's Rule?

```
  A method to solve systems of linear equations using DETERMINANTS.
  
  System: Ax⃗ = b⃗     (A is the coefficient matrix, b⃗ is the right side)
  
  To find variable xⱼ:
    1. Take matrix A
    2. REPLACE column j with the vector b⃗
    3. Call this new matrix Aⱼ
    4. xⱼ = det(Aⱼ) / det(A)
  
  ⚠️ Only works when det(A) ≠ 0 (unique solution exists).
  
  🍎 Kid version: To find x, swap in b⃗ for x's column, take determinant, divide.
                  To find y, swap in b⃗ for y's column, take determinant, divide.
```

### Problem: Solve 3x + 2y = 5,  x − y = 1

**Step 1 — Write in matrix form:**
```
  A = [3   2]    x⃗ = [x]    b⃗ = [5]
      [1  -1]        [y]        [1]
  
  The system is:  [3   2] · [x] = [5]
                  [1  -1]   [y]   [1]
```

**Step 2 — Compute det(A):**
```
  det(A) = 3×(-1) − 2×1 = -3 − 2 = -5
  
  det ≠ 0  →  unique solution exists! We can proceed.
```

**Step 3 — Find x (replace COLUMN 1 with b⃗):**
```
  Aₓ = [5   2]     ← column 1 replaced with b⃗ = [5, 1]
       [1  -1]        column 2 stays the same
  
  det(Aₓ) = 5×(-1) − 2×1 = -5 − 2 = -7
  
  x = det(Aₓ) / det(A) = -7 / -5 = 7/5 = 1.4
```

**Step 4 — Find y (replace COLUMN 2 with b⃗):**
```
  Aᵧ = [3  5]     ← column 1 stays
       [1  1]        column 2 replaced with b⃗ = [5, 1]
  
  det(Aᵧ) = 3×1 − 5×1 = 3 − 5 = -2
  
  y = det(Aᵧ) / det(A) = -2 / -5 = 2/5 = 0.4
```

**Step 5 — VERIFY:**
```
  Equation 1: 3x + 2y = 3(7/5) + 2(2/5) = 21/5 + 4/5 = 25/5 = 5  ✅
  Equation 2: x − y   = 7/5 − 2/5        = 5/5         = 1      ✅
  
  ┌───────────────────────────────┐
  │  x = 7/5 = 1.4                │
  │  y = 2/5 = 0.4  ✅            │
  └───────────────────────────────┘
```

---

## 🧮 P13: Change of Basis

> 📘 Theory: [Ch 13 — Change of Basis](./Essence_of_Linear_Algebra_THEORY.md#chapter-13--change-of-basis) | ⬆️ [Problem Index](#-problem-index)

### What IS Change of Basis?

```
  A "basis" is a set of vectors you use as your COORDINATE SYSTEM.
  
  Standard basis: î=[1,0] and ĵ=[0,1]
  
  But you could use ANY two independent vectors as your basis!
  Different basis = different "rulers" to measure positions.
  
  The SAME point in space has DIFFERENT coordinates in different bases.
  
  🍎 Kid version: In English, "the big red house" uses English words.
     In French, it's "la grande maison rouge."
     SAME house, different description. Change of basis = translation!
  
  P = [b⃗₁ | b⃗₂]  (new basis vectors as columns)
  P · [coords in new basis] = [coords in standard basis]
  P⁻¹ · [coords in standard basis] = [coords in new basis]
```

### Problem: New basis b⃗₁ = [2, 1], b⃗₂ = [1, 3].
**(a)** Change-of-basis matrix P
**(b)** Convert [7, 8] (standard) to new basis
**(c)** If [3, 1] in new basis, what in standard?

### (a) The matrix P

```
  P is formed by placing the new basis vectors as COLUMNS:
  
  P = [b⃗₁ | b⃗₂] = [2  1]
                    [1  3]
  
  ┌────────────────────────────────┐
  │  P = [2  1]  ✅                │
  │      [1  3]                    │
  └────────────────────────────────┘
```

### (b) Convert [7, 8] from standard to new basis

**We need P⁻¹ · [7, 8].**

**Step 1 — Find P⁻¹:**
```
  det(P) = 2×3 − 1×1 = 6 − 1 = 5
  
  P⁻¹ = (1/5) · [ 3  -1] = [ 3/5   -1/5] = [0.6   -0.2]
                 [-1   2]   [-1/5    2/5]   [-0.2    0.4]
```

**Step 2 — Multiply P⁻¹ · [7, 8]:**
```
  Row 1: 0.6×7 + (-0.2)×8 = 4.2 + (-1.6) = 4.2 - 1.6 = 2.6
  Row 2: (-0.2)×7 + 0.4×8 = -1.4 + 3.2 = 1.8
  
  In new basis coordinates: [2.6, 1.8]
```

**Step 3 — VERIFY: does 2.6·b⃗₁ + 1.8·b⃗₂ = [7, 8]?**
```
  2.6 · [2, 1] = [5.2, 2.6]
  1.8 · [1, 3] = [1.8, 5.4]
  
  Sum: [5.2 + 1.8, 2.6 + 5.4] = [7.0, 8.0]  ✅
  
  ┌────────────────────────────────────────────────────────────┐
  │  [7, 8] in standard basis = [2.6, 1.8] in new basis ✅     │
  │                                                            │
  │  Meaning: to reach [7, 8], walk 2.6 steps along b⃗₁=[2,1]   │
  │  and 1.8 steps along b⃗₂=[1,3].                             │
  └────────────────────────────────────────────────────────────┘
```

### (c) [3, 1] in new basis → what in standard?

**Multiply P · [3, 1]:**
```
  P · [3, 1] means: 3 copies of b⃗₁ + 1 copy of b⃗₂
  
  = 3 · [2, 1] + 1 · [1, 3]
  = [6, 3] + [1, 3]
  = [7, 6]
  
  ┌────────────────────────────────────────────────────────┐
  │  [3, 1] in new basis = [7, 6] in standard basis  ✅    │
  └────────────────────────────────────────────────────────┘
```

---

## 🧮 P14: Eigenvalues & Eigenvectors (Full Computation)

> 📘 Theory: [Ch 14 — Eigenvectors](./Essence_of_Linear_Algebra_THEORY.md#chapter-14--eigenvectors--eigenvalues) | ⬆️ [Problem Index](#-problem-index)

### What ARE Eigenvalues & Eigenvectors?

```
  Most vectors CHANGE DIRECTION when multiplied by a matrix.
  But some special vectors only get STRETCHED (or flipped),
  staying on the SAME LINE. These are EIGENVECTORS.
  
  A · v⃗ = λ · v⃗
  
  v⃗ = eigenvector (the special direction that doesn't rotate)
  λ = eigenvalue  (the stretching factor)
  
  🍎 Kid version: Imagine pushing a door. Most arrows on the door 
     move in complicated ways. But the arrow along the HINGE stays 
     pointing the same direction — it just might stretch or flip. 
     That arrow is an eigenvector!
  
  To FIND them:
    Step 1: Solve det(A − λI) = 0 for λ  (eigenvalues)
    Step 2: For each λ, solve (A − λI)·v⃗ = 0⃗ for v⃗ (eigenvectors)
```

### Problem: Find eigenvalues and eigenvectors of A = [[4, 2], [1, 3]]

### Step 1 — Characteristic Equation (find λ):

```
  A − λI = [4  2] − λ·[1  0] = [4-λ    2  ]
           [1  3]     [0  1]   [  1   3-λ  ]
  
  Set det(A − λI) = 0:
  
    det = (4-λ)(3-λ) − 2·1
    
    Expand (4-λ)(3-λ):
      = 4·3 + 4·(-λ) + (-λ)·3 + (-λ)·(-λ)
      = 12 - 4λ - 3λ + λ²
      = λ² - 7λ + 12
    
    Subtract 2·1 = 2:
      λ² - 7λ + 12 - 2 = 0
      λ² - 7λ + 10 = 0
  
  Factor the quadratic:
    We need two numbers that MULTIPLY to 10 and ADD to -7.
    -5 × -2 = 10  ✅    -5 + (-2) = -7  ✅
    
    (λ - 5)(λ - 2) = 0
    
  ┌───────────────────────────────────┐
  │  λ₁ = 5   and   λ₂ = 2  ✅        │
  └───────────────────────────────────┘
```

### Step 2 — Eigenvector for λ₁ = 5:

```
  Solve (A - 5I)·v⃗ = 0⃗
  
  A - 5I = [4-5    2 ] = [-1   2]
           [  1   3-5]   [ 1  -2]
  
  System of equations:
    Row 1: -1·x + 2·y = 0  →  -x + 2y = 0  →  x = 2y
    Row 2:  1·x + (-2)·y = 0  →  x - 2y = 0  →  x = 2y
    
    (Both rows give the SAME equation! That's expected — 
     the matrix is rank-deficient by design when we use an eigenvalue.)
  
  Pick y = 1 (any nonzero choice works):
    x = 2(1) = 2
    
  Eigenvector: v⃗₁ = [2, 1]
  
  VERIFY: A · [2, 1] should equal 5 · [2, 1] = [10, 5]
    A · [2, 1] = [4×2 + 2×1,  1×2 + 3×1] = [8+2, 2+3] = [10, 5]
    5 · [2, 1] = [10, 5]
    [10, 5] = [10, 5]  ✅
```

### Step 3 — Eigenvector for λ₂ = 2:

```
  Solve (A - 2I)·v⃗ = 0⃗
  
  A - 2I = [4-2   2 ] = [2   2]
           [  1  3-2]   [1   1]
  
  Row 1: 2x + 2y = 0  →  x + y = 0  →  x = -y
  Row 2:  x + y = 0  →  same thing!
  
  Pick y = 1:  x = -1
    
  Eigenvector: v⃗₂ = [-1, 1]
  
  VERIFY: A · [-1, 1] should equal 2 · [-1, 1] = [-2, 2]
    A · [-1, 1] = [4×(-1) + 2×1,  1×(-1) + 3×1] = [-4+2, -1+3] = [-2, 2]
    2 · [-1, 1] = [-2, 2]
    [-2, 2] = [-2, 2]  ✅
  
  ┌──────────────────────────────────────────────────────┐
  │  SUMMARY:                                            │
  │    λ₁ = 5,  v⃗₁ = [2, 1]   (stretched 5× along this   │
  │                              direction)              │
  │    λ₂ = 2,  v⃗₂ = [-1, 1]  (stretched 2× along this   │
  │                              direction)              │
  │                                                      │
  │  🤖 AI/ML: Eigenvalues power PCA, Google PageRank,   │
  │  stability analysis, and spectral clustering!        │
  └──────────────────────────────────────────────────────┘
```

---

## 🧮 P15: Diagonalization & Matrix Power

> 📘 Theory: [Ch 14](./Essence_of_Linear_Algebra_THEORY.md#chapter-14--eigenvectors--eigenvalues) | ⬆️ [Problem Index](#-problem-index)

### What IS Diagonalization?

```
  Diagonalization rewrites a matrix as: A = P · D · P⁻¹
  
  P = matrix with eigenvectors as columns
  D = diagonal matrix with eigenvalues on the diagonal
  
  WHY bother? Because POWERS become trivially easy!
  
  A² = (P·D·P⁻¹)(P·D·P⁻¹) = P·D·(P⁻¹·P)·D·P⁻¹ = P·D²·P⁻¹
  Aⁿ = P · Dⁿ · P⁻¹
  
  And Dⁿ is easy: just raise each diagonal entry to the nth power!
  
  🍎 Kid version: Diagonalization finds the "natural axes" of the matrix
     where it just stretches. Computing Aⁿ = stretch each axis n times.
```

### Problem: Using P14 results, diagonalize A = [[4,2],[1,3]] and compute A³.

**Step 1 — Build P and D:**
```
  From P14: λ₁=5, v⃗₁=[2,1]   λ₂=2, v⃗₂=[-1,1]
  
  P = [v⃗₁ | v⃗₂] = [ 2  -1]     ← eigenvectors as columns
                    [ 1   1]
  
  D = [λ₁   0 ] = [5  0]     ← eigenvalues on diagonal
      [ 0  λ₂]    [0  2]
```

**Step 2 — Find P⁻¹:**
```
  det(P) = 2×1 − (-1)×1 = 2 − (-1) = 2 + 1 = 3
  
  P⁻¹ = (1/3) · [1   1] = [1/3   1/3]
                 [-1  2]   [-1/3  2/3]
```

**Step 3 — Compute D³:**
```
  D³ = [5³   0 ] = [125   0]
       [ 0  2³]    [  0   8]
  
  (Just cube each diagonal entry! That's the beauty of diagonal matrices.)
```

**Step 4 — Compute A³ = P · D³ · P⁻¹:**
```
  First: P · D³
  
  P · D³ = [ 2  -1] · [125  0]
           [ 1   1]   [  0  8]
  
  Entry (1,1): 2×125 + (-1)×0 = 250
  Entry (1,2): 2×0 + (-1)×8 = -8
  Entry (2,1): 1×125 + 1×0 = 125
  Entry (2,2): 1×0 + 1×8 = 8
  
  P · D³ = [250  -8]
           [125   8]
  
  Next: (P · D³) · P⁻¹
  
  [250  -8] · (1/3) · [ 1   1]
  [125   8]            [-1   2]
  
  = (1/3) · [250×1 + (-8)×(-1),    250×1 + (-8)×2   ]
            [125×1 + 8×(-1),        125×1 + 8×2      ]
  
  = (1/3) · [250 + 8,    250 - 16]
            [125 - 8,    125 + 16]
  
  = (1/3) · [258,  234]
            [117,  141]
  
  = [258/3,  234/3] = [86,  78]
    [117/3,  141/3]   [39,  47]
  
  ┌────────────────────────────┐
  │  A³ = [86   78]  ✅        │
  │       [39   47]            │
  └────────────────────────────┘
```

**Step 5 — VERIFY by direct multiplication:**
```
  A² = A · A = [4,2]·[4,2] = [4×4+2×1, 4×2+2×3] = [18, 14]
               [1,3] [1,3]   [1×4+3×1, 1×2+3×3]   [ 7, 11]
  
  A³ = A² · A = [18,14]·[4,2] = [18×4+14×1, 18×2+14×3] = [86, 78]
                [ 7,11] [1,3]   [ 7×4+11×1,  7×2+11×3]   [39, 47]
  
  A³ = [86, 78; 39, 47]  ✅  (matches diagonalization method!)
```

---

## 🧮 P16: Mean-Product Eigenvalue Trick

> 📘 Theory: [Ch 15 — Quick Trick](./Essence_of_Linear_Algebra_THEORY.md#chapter-15--a-quick-trick-for-computing-eigenvalues) | ⬆️ [Problem Index](#-problem-index)

### The Trick Explained:

```
  For a 2×2 matrix A = [a  b]:
                        [c  d]
  
  m = (a + d) / 2    ← MEAN of the diagonal entries
  p = ad − bc         ← PRODUCT of eigenvalues = determinant
  
  λ = m ± √(m² − p)
  
  WHY does this work?
  For 2×2: the eigenvalues λ₁ and λ₂ satisfy:
    λ₁ + λ₂ = a + d = trace    (sum of diagonal)
    λ₁ × λ₂ = ad − bc = det    (determinant)
    
  Mean of eigenvalues = (λ₁+λ₂)/2 = m
  So λ₁ = m + something, λ₂ = m − something
  That "something" = √(m² − p)
  
  🍎 Kid version: The two eigenvalues are like two numbers that are
     EQUALLY SPACED from their average m. The spread = √(m²−p).
```

### (a) A = [[7, 2], [0, 3]]

```
  m = (7 + 3) / 2 = 10/2 = 5
  p = 7×3 − 2×0 = 21 − 0 = 21
  
  λ = 5 ± √(5² − 21) = 5 ± √(25 − 21) = 5 ± √4 = 5 ± 2
  
  λ₁ = 5 + 2 = 7
  λ₂ = 5 − 2 = 3
  
  ┌─────────────────────────────────────────┐
  │  λ₁ = 7,  λ₂ = 3  ✅                    │
  │                                         │
  │  Notice: for a triangular matrix        │
  │ (zeros below diagonal), the eigenvalues │
  │  ARE the diagonal entries! (7 and 3)    │
  └─────────────────────────────────────────┘
```

### (b) A = [[2, 1], [1, 2]]

```
  m = (2 + 2) / 2 = 4/2 = 2
  p = 2×2 − 1×1 = 4 − 1 = 3
  
  λ = 2 ± √(2² − 3) = 2 ± √(4 − 3) = 2 ± √1 = 2 ± 1
  
  λ₁ = 2 + 1 = 3
  λ₂ = 2 − 1 = 1
  
  ┌──────────────────────────────────────────────┐
  │  λ₁ = 3,  λ₂ = 1  ✅                         │
  │                                              │
  │  This is a SYMMETRIC matrix (a=d, b=c).      │
  │  Symmetric matrices always have REAL         │
  │  eigenvalues. Important for PCA in ML!       │
  └──────────────────────────────────────────────┘
```

### (c) A = [[0, -1], [1, 0]]

```
  m = (0 + 0) / 2 = 0
  p = 0×0 − (-1)×1 = 0 − (-1) = 0 + 1 = 1
  
  λ = 0 ± √(0² − 1) = 0 ± √(-1) = ±i
  
  ┌──────────────────────────────────────────────────────────┐
  │  λ₁ = +i,  λ₂ = -i  ✅  (COMPLEX eigenvalues!)           │
  │                                                          │
  │  √(-1) = i (the "imaginary unit")                        │
  │                                                          │
  │  This matrix is R(90°) — a 90° rotation!                 │
  │  No real vector stays on its line after a 90° rotation.  │
  │  That's WHY the eigenvalues are complex.                 │
  │                                                          │
  │  🍎 RULE: If m² < p → eigenvalues are complex            │
  │     This happens for rotation-like matrices.             │
  │     Here: 0 < 1, so complex eigenvalues.                 │
  └──────────────────────────────────────────────────────────┘
```

---

## 🧮 P17: Vector Space Verification

> 📘 Theory: [Ch 16 — Abstract Spaces](./Essence_of_Linear_Algebra_THEORY.md#chapter-16--abstract-vector-spaces) | ⬆️ [Problem Index](#-problem-index)

### What IS a Vector Space?

```
  A vector space is any set of "things" where you can:
    1. ADD two things and get another thing in the set
    2. SCALE a thing by a number and get another thing in the set
    3. There's a ZERO element (adding it changes nothing)
  
  These two rules are called CLOSURE:
    • Closure under addition:  if u⃗ and v⃗ are in the set, u⃗+v⃗ is too
    • Closure under scaling:   if v⃗ is in the set, c·v⃗ is too (for any c)
  
  🍎 Kid version: A vector space is like a "club" with two rules:
     Rule 1: If two members are added together, the result is also a member.
     Rule 2: If you stretch any member by any amount, the result is a member.
     Rule 3: There must be a "do-nothing" member (zero).
     If ANY rule fails for even ONE example → NOT a vector space.
```

### (a) All 2×2 matrices — vector space?

```
  Addition: If M₁ and M₂ are 2×2 matrices, is M₁ + M₂ a 2×2 matrix?
    YES — adding two 2×2 grids gives a 2×2 grid.  ✅
  
  Scaling: If M is a 2×2 matrix and c is a number, is c·M a 2×2 matrix?
    YES — multiplying every entry by c keeps it 2×2.  ✅
  
  Zero: The zero matrix [0,0; 0,0] is a 2×2 matrix.  ✅
  
  ┌────────────────────────────────┐
  │  YES — this is a vector space! │
  │  Dimension = 4 (need 4         │
  │  numbers to specify a 2×2)     │
  └────────────────────────────────┘
```

### (b) Polynomials of degree ≤ 3 — vector space?

```
  These are polynomials like: 5x³ + 2x² − x + 7,  or  x + 1,  or  4
  
  Addition: (x³ + 1) + (2x² + x) = x³ + 2x² + x + 1
    Degree = 3  ≤ 3  ✅  (still in the set)
  
  Scaling: 5 · (x³ + 1) = 5x³ + 5
    Degree = 3  ≤ 3  ✅
  
  Zero: The zero polynomial (all coefficients = 0) has degree ≤ 3.  ✅
  
  ┌───────────────────────────────┐
  │  YES — vector space!  ✅      │
  │  Dimension = 4                │
  │  Basis: {1, x, x², x³}        │
  └───────────────────────────────┘
```

### (c) Polynomials of degree EXACTLY 2 — vector space?

```
  These are polynomials like: 3x² + x − 1,  or  x²,  or  −5x² + 2x
  (Must have x² term with nonzero coefficient)
  
  Test addition:
    Take p₁(x) = x² + 1     (degree exactly 2  ✅)
    Take p₂(x) = −x² + 2    (degree exactly 2  ✅)
    
    p₁ + p₂ = (x² + 1) + (−x² + 2)
             = x² − x² + 1 + 2
             = 0 + 3
             = 3
    
    The result is just the number 3 — degree 0!
    That's NOT degree exactly 2.
    
  ⚠️ Closure under addition FAILS!
  
  Also: the zero polynomial has degree undefined (not 2), so it's
  not in the set either. No zero element!
  
  ┌───────────────────────────────────────────────────────┐
  │  NO — NOT a vector space! ❌                          │
  │                                                       │
  │  The x² terms can cancel when adding, giving a        │
  │  polynomial of lower degree that's outside the set.   │
  └───────────────────────────────────────────────────────┘
```

### (d) Functions f where f(0) = 0 — vector space?

```
  These are all functions that PASS THROUGH THE ORIGIN.
  Examples: f(x) = x,  f(x) = sin(x),  f(x) = x³ − 2x
  All have f(0) = 0.
  
  Test addition:
    If f(0) = 0 and g(0) = 0, is (f+g)(0) = 0?
    (f+g)(0) = f(0) + g(0) = 0 + 0 = 0  ✅
  
  Test scaling:
    If f(0) = 0, is (c·f)(0) = 0?
    (c·f)(0) = c · f(0) = c · 0 = 0  ✅
  
  Zero element:
    The zero function z(x) = 0 for all x. z(0) = 0  ✅
  
  ┌───────────────────────────────┐
  │  YES — vector space!  ✅      │
  │                               │
  │  This is infinite-dimensional │
  │  (infinitely many independent │
  │   functions pass through 0!)  │
  └───────────────────────────────┘
```

---

## 🧮 P18: Derivative as Linear Transformation

> 📘 Theory: [Ch 16](./Essence_of_Linear_Algebra_THEORY.md#chapter-16--abstract-vector-spaces) | ⬆️ [Problem Index](#-problem-index)

### What Does This Problem Mean?

```
  The derivative operator D maps polynomials to polynomials:
    D(a + bx + cx²) = b + 2cx
  
  It's LINEAR because:
    D(f + g) = D(f) + D(g)     ✅  (derivative of sum = sum of derivatives)
    D(c·f)   = c · D(f)        ✅  (constant pulls out)
  
  Since it's a linear transformation, we can represent it as a MATRIX!
  
  We just need to choose a BASIS (coordinate system for polynomials):
    Basis = {1, x, x²}   (all polynomials of degree ≤ 2)
  
  Then a polynomial like 3 + 5x − 2x² becomes the vector [3, 5, -2].
  
  🍎 Kid version: Polynomials are like vectors, just with different
     "components": the constant part, the x part, the x² part.
     Derivative is a machine that takes polynomials and outputs 
     polynomials — just like a matrix takes vectors and outputs vectors!
```

### Problem: Basis = {1, x, x²}. Find (a) matrix of D, (b) null space, (c) rank.

### (a) Matrix of D

**Strategy: Apply D to each basis element, express result in same basis.**

```
  ── D(1) = ? ──
    The derivative of the constant 1 is 0.
    D(1) = 0
    
    Express 0 in basis {1, x, x²}:
    0 = 0·(1) + 0·(x) + 0·(x²)
    
    Coordinate vector: [0, 0, 0]  → this becomes COLUMN 1 of the matrix
  
  ── D(x) = ? ──
    The derivative of x is 1.
    D(x) = 1
    
    Express 1 in basis:
    1 = 1·(1) + 0·(x) + 0·(x²)
    
    Coordinate vector: [1, 0, 0]  → COLUMN 2
  
  ── D(x²) = ? ──
    The derivative of x² is 2x.
    D(x²) = 2x
    
    Express 2x in basis:
    2x = 0·(1) + 2·(x) + 0·(x²)
    
    Coordinate vector: [0, 2, 0]  → COLUMN 3
  
  PUT THE COLUMNS TOGETHER:
  
  ┌─────────────────────────────────────────────┐
  │  Matrix of D = [ 0   1   0 ]  ✅            │
  │                [ 0   0   2 ]                │
  │                [ 0   0   0 ]                │
  │                                             │
  │  Column 1 = D(1)  = [0,0,0]                 │
  │  Column 2 = D(x)  = [1,0,0]                 │
  │  Column 3 = D(x²) = [0,2,0]                 │
  └─────────────────────────────────────────────┘
```

### (b) Null Space

```
  The null space = all polynomials p where D(p) = 0.
  
  Which polynomials have derivative zero? CONSTANTS!
  
  Any constant c → D(c) = 0.
  
  In coordinate form: the constant c is represented as [c, 0, 0].
  
  Verify with the matrix: 
    D · [c, 0, 0] = [0×c + 1×0 + 0×0,  0×c + 0×0 + 2×0,  0×c + 0×0 + 0×0]
                   = [0, 0, 0]  ✅  (yep, goes to zero)
  
  ┌───────────────────────────────────────────────────┐
  │  Null space = span{[1, 0, 0]} = constants  ✅     │
  │                                                   │
  │  Nullity = 1 (one-dimensional)                    │
  │                                                   │
  │  Meaning: only constants have zero derivative.    │
  │  All non-constant polynomials have nonzero        │
  │  derivatives (they CHANGE when you move).         │
  └───────────────────────────────────────────────────┘
```

### (c) Rank

```
  Look at the columns of the matrix:
    Col 1 = [0, 0, 0]  — the zero vector (never independent)
    Col 2 = [1, 0, 0]  — independent!
    Col 3 = [0, 2, 0]  — independent! (not a multiple of Col 2)
  
  Number of independent columns = 2
  
  ┌────────────────────────────┐
  │  Rank = 2  ✅              │
  └────────────────────────────┘
  
  Rank-Nullity check:
    rank + nullity = number of columns
    2 + 1 = 3  ✅
    
  The domain (degree ≤ 2 polynomials) is 3-dimensional.
  D "uses up" 2 dimensions (maps to degree ≤ 1 polynomials)
  and "crushes" 1 dimension (the constants) to zero.
  
  🤖 AI/ML: This idea of representing operators as matrices is 
  how we do things like understand gradient operators, Hessians,
  and Jacobians — all crucial in optimization!
```

---

> 🔗 **Theory explanations:** [← Theory Guide](./Essence_of_Linear_Algebra_THEORY.md)
>
> 🔗 **Master hub:** [← INDEX](./Essence_of_Linear_Algebra_INDEX.md)
>
> 🎓 **Created for:** ODS | ML
