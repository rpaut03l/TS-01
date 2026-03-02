# 🔢 Essence of Linear Algebra — PRACTICE PROBLEMS GUIDE
### 🎓ODS | 18+ Fully Solved Problems — Every Step Explained
> 🔗 **Navigation:** [← Back to INDEX](./Essence_of_Linear_Algebra_INDEX.md) | [← Theory Guide](./Essence_of_Linear_Algebra_THEORY.md)

---

## 📚 Problem Index

| # | Problem | Concepts Tested | Theory Link |
|---|---------|----------------|-------------|
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

## 📖 Rules & Formulas Reference Sheet

> Use this section as a QUICK LOOKUP while solving problems below. For full explanations see [Theory Guide](./Essence_of_Linear_Algebra_THEORY.md).

```
 ┌──────────────────────── KEY FORMULAS ────────────────────────┐
 │                                                              │
 │  VECTOR OPS                                                  │
 │  v⃗+w⃗ = [v₁+w₁, v₂+w₂]   c·v⃗ = [cv₁, cv₂]                     │
 │  |v⃗| = √(v₁²+v₂²+...)                                        │
 │                                                              │
 │  DOT PRODUCT                                                 │
 │  v⃗·w⃗ = v₁w₁+v₂w₂        = |v⃗||w⃗|cos(θ)                       │
 │  proj_v(w⃗) = (v⃗·w⃗ / v⃗·v⃗) · v⃗                                 │
 │                                                              │
 │  CROSS PRODUCT (3D)                                          │
 │  v⃗×w⃗ = [v₂w₃−v₃w₂, v₃w₁−v₁w₃, v₁w₂−v₂w₁]                     │
 │                                                              │
 │  DETERMINANT                                                 │
 │  2×2: det([a,b;c,d]) = ad−bc                                 │
 │  3×3: a(ei−fh) − b(di−fg) + c(dh−eg)                         │
 │                                                              │
 │  INVERSE (2×2)                                               │
 │  A⁻¹ = (1/(ad−bc)) · [d,−b; −c,a]                            │
 │                                                              │
 │  EIGENVALUES                                                 │
 │  det(A−λI) = 0                                               │
 │  Quick 2×2: λ = m±√(m²−p),  m=(a+d)/2,  p=ad−bc              │
 │                                                              │
 │  DIAGONALIZATION:  Aⁿ = P·Dⁿ·P⁻¹                             │
 │  CRAMER:  xⱼ = det(Aⱼ)/det(A)                                │
 │  RANK-NULLITY:  rank + nullity = #columns                    │
 └──────────────────────────────────────────────────────────────┘
```

---

## 🧮 P1: Vector Addition & Scalar Multiplication

> 📘 Theory: [Ch 1 — Vectors](./Essence_of_Linear_Algebra_THEORY.md#chapter-1--vectors-what-even-are-they) | ⬆️ [Problem Index](#-problem-index)

**Problem:** Given v⃗ = [3, -1] and w⃗ = [-2, 4]:
(a) Compute v⃗ + w⃗    (b) Compute 3v⃗ − 2w⃗    (c) Is [7, -6] a linear combination of v⃗ and w⃗?

**Rules Used:**
- **Addition:** [a,b]+[c,d] = [a+c, b+d] (add each component)
- **Scalar mult:** k·[a,b] = [ka, kb] (multiply each component by k)
- **Linear combo:** a·v⃗+b·w⃗=[x,y] → solve for a,b

**Solution:**

**(a) v⃗ + w⃗:**
```
  Rule: [v₁+w₁, v₂+w₂]
  = [3+(-2), (-1)+4]
  = [1, 3]  ✅
```

**(b) 3v⃗ − 2w⃗:**
```
  Step 1: Scale each vector
    3·v⃗ = 3·[3,-1] = [3×3, 3×(-1)] = [9, -3]
    2·w⃗ = 2·[-2,4] = [2×(-2), 2×4]  = [-4, 8]
  
  Step 2: Subtract (3v⃗ minus 2w⃗)
    [9,-3] − [-4,8] = [9-(-4), -3-8] = [13, -11]  ✅
```

**(c) Is [7,-6] = a·v⃗ + b·w⃗?**
```
  Need: a·[3,-1] + b·[-2,4] = [7,-6]
  
  This gives two equations (one per component):
    3a − 2b = 7    ... (i)   ← x-components
    −a + 4b = −6   ... (ii)  ← y-components
  
  From (ii): a = 4b + 6
  Substitute into (i): 3(4b+6) − 2b = 7
                        12b + 18 − 2b = 7
                        10b = −11
                        b = −1.1
                        a = 4(−1.1)+6 = 1.6
  
  Verify: 1.6·[3,-1]+(-1.1)·[-2,4] = [4.8,-1.6]+[2.2,-4.4] = [7,-6] ✅
  
  YES! [7,-6] = 1.6·v⃗ + (−1.1)·w⃗
```

---

## 🧮 P2: Linear Independence Test

> 📘 Theory: [Ch 2 — Span & Basis](./Essence_of_Linear_Algebra_THEORY.md#chapter-2--linear-combinations-span--basis-vectors) | ⬆️ [Problem Index](#-problem-index)

**Problem:** Are these sets linearly independent?
(a) {[1,2], [3,6]}   (b) {[1,0,0], [0,1,0], [0,0,1]}   (c) {[1,2], [3,4]}

**Rule:** Vectors are independent if NONE can be written as a combo of others. Quick test for 2 vectors: check if one is a scalar multiple. For n vectors in n-D: compute determinant — if det≠0 → independent.

**(a) {[1,2], [3,6]}:**
```
  Check: is [3,6] = k·[1,2]?
  3/1 = 3, 6/2 = 3.  Same ratio! So [3,6] = 3·[1,2]
  LINEARLY DEPENDENT ❌  (same direction, redundant)
```

**(b) {[1,0,0], [0,1,0], [0,0,1]}:**
```
  These are î, ĵ, k̂ — the standard basis.
  det = |1 0 0; 0 1 0; 0 0 1| = 1·(1·1−0·0)−0+0 = 1 ≠ 0
  LINEARLY INDEPENDENT ✅
```

**(c) {[1,2], [3,4]}:**
```
  Check scalar multiple: 3/1=3, 4/2=2. Ratios differ! Not parallel.
  Alternatively: det([1,3; 2,4]) = 1·4−3·2 = 4−6 = −2 ≠ 0
  LINEARLY INDEPENDENT ✅
```

---

## 🧮 P3: Span Geometric Description

> 📘 Theory: [Ch 2](./Essence_of_Linear_Algebra_THEORY.md#chapter-2--linear-combinations-span--basis-vectors) | ⬆️ [Problem Index](#-problem-index)

**Problem:** What is the span of {[1,2], [2,4]}?

```
  [2,4] = 2·[1,2] → PARALLEL (dependent)
  
  Any combo: a·[1,2]+b·[2,4] = a·[1,2]+2b·[1,2] = (a+2b)·[1,2]
  
  This is always a multiple of [1,2] → a LINE through origin!
  
  Span = the line y = 2x
  
       ▲ y
       │  ╱ [1,2]
       │ ╱
  ─────┼╱──────► x    span = this line only
       │╱              can't reach [1,0] or [0,1]!
```

---

## 🧮 P4: Matrix as Transformation

> 📘 Theory: [Ch 3 — Transforms](./Essence_of_Linear_Algebra_THEORY.md#chapter-3--linear-transformations--matrices) | ⬆️ [Problem Index](#-problem-index)

**Problem:** A = [[2,1],[0,3]]. (a) Where does î land? (b) ĵ? (c) Where does [4,-1] go? (d) Unit square?

**Rule:** Column 1 = where î lands, Column 2 = where ĵ lands. For any v⃗=[x,y]: result = x·col1 + y·col2.

**(a)** î lands at **Col 1 = [2, 0]** (stretched right, stays on x-axis)
**(b)** ĵ lands at **Col 2 = [1, 3]** (moved right and stretched up)

**(c) A·[4,-1]:**
```
  Rule: result = x·col1 + y·col2
  = 4·[2,0] + (-1)·[1,3]
  = [8,0] + [-1,-3]
  = [7, -3]  ✅
  
  Alternatively (row method):
  Row 1: 2·4+1·(-1) = 8-1 = 7
  Row 2: 0·4+3·(-1) = 0-3 = -3
  Result: [7, -3]  ✅
```

**(d) Unit square corners:**
```
  (0,0) → (0,0)    origin stays
  (1,0) → (2,0)    î lands
  (0,1) → (1,3)    ĵ lands
  (1,1) → (2+1, 0+3) = (3,3)  î+ĵ lands
  
  Area = det(A) = 2·3−1·0 = 6  (area scales 6×)
```

---

## 🧮 P5: Matrix Multiplication (Composition)

> 📘 Theory: [Ch 4](./Essence_of_Linear_Algebra_THEORY.md#chapter-4--matrix-multiplication-as-composition) | ⬆️ [Problem Index](#-problem-index)

**Problem:** Compute M₂·M₁ where M₁=[[1,-1],[1,1]], M₂=[[0,1],[1,0]].

**Rule:** Column j of product = M₂ applied to Column j of M₁. Or: element (i,j) = dot product of row i of M₂ with column j of M₁.

```
  Geometric method — track basis vectors:
  
  î → M₁ sends to col1 of M₁ = [1,1]
     → M₂ sends [1,1] to 1·[0,1]+1·[1,0] = [1,1]    ← Product col 1
  
  ĵ → M₁ sends to col2 of M₁ = [-1,1]
     → M₂ sends [-1,1] to (-1)·[0,1]+1·[1,0] = [1,-1] ← Product col 2
  
  M₂·M₁ = [ 1   1 ]
           [ 1  -1 ]
  
  Verify (formula method):
  (1,1): 0·1+1·1 = 1 ✅    (1,2): 0·(-1)+1·1 = 1 ✅
  (2,1): 1·1+0·1 = 1 ✅    (2,2): 1·(-1)+0·1 = -1 ✅
```

---

## 🧮 P6: Rotation Matrix Composition

> 📘 Theory: [Ch 4](./Essence_of_Linear_Algebra_THEORY.md#chapter-4--matrix-multiplication-as-composition) | ⬆️ [Problem Index](#-problem-index)

**Problem:** R(θ)=[[cosθ,-sinθ],[sinθ,cosθ]]. (a) Compute R(90°). (b) Verify R(90°)²=R(180°). (c) What is R(θ)⁻¹?

```
  (a) R(90°) = [cos90°,-sin90°; sin90°,cos90°] = [0,-1; 1,0]
  
  (b) R(90°)² = [0,-1; 1,0]·[0,-1; 1,0]
     = [0·0+(-1)·1,  0·(-1)+(-1)·0] = [-1, 0]
       [1·0+0·1,     1·(-1)+0·0   ]   [0, -1]
     
     R(180°) = [cos180°,-sin180°; sin180°,cos180°] = [-1,0; 0,-1]
     
     R(90°)² = R(180°) ✅  (rotating 90° twice = rotating 180°)
  
  (c) R(θ)⁻¹ = R(−θ) = [cosθ, sinθ; -sinθ, cosθ]
     "Rotating back by θ undoes the rotation"
     Check: det(R(θ)) = cos²θ+sin²θ = 1 ≠ 0, so inverse exists ✅
```

---

## 🧮 P7: Determinant Computation & Geometric Meaning

> 📘 Theory: [Ch 6 — Determinant](./Essence_of_Linear_Algebra_THEORY.md#chapter-6--the-determinant) | ⬆️ [Problem Index](#-problem-index)

**Problem:** Compute det and state geometric meaning:
(a) [[3,0],[0,2]]   (b) [[1,2],[3,6]]   (c) [[-1,0],[0,-1]]

**Rule:** det([a,b;c,d]) = ad−bc. |det|=area scale, sign=orientation.

```
  (a) det = 3·2−0·0 = 6
      → Areas scale 6×, orientation preserved (positive) ✅
  
  (b) det = 1·6−2·3 = 6−6 = 0
      → Space SQUISHED to a line! No inverse! ❌
      (Columns [1,3] and [2,6] are parallel: [2,6]=2·[1,3])
  
  (c) det = (-1)(-1)−0·0 = 1
      → Areas unchanged, orientation preserved
      This is 180° rotation: [x,y]→[-x,-y]
```

---

## 🧮 P8: Finding the Inverse Matrix

> 📘 Theory: [Ch 7 — Inverse](./Essence_of_Linear_Algebra_THEORY.md#chapter-7--inverse-matrices-column-space--null-space) | ⬆️ [Problem Index](#-problem-index)

**Problem:** Find A⁻¹ for A=[[4,7],[2,6]] and verify.

**Rule:** A⁻¹ = (1/det)·[d,-b;-c,a]. Steps: (1) compute det, (2) swap a↔d, (3) negate b,c, (4) divide by det.

```
  Step 1: det(A) = 4·6−7·2 = 24−14 = 10
  
  Step 2-4: A⁻¹ = (1/10)·[6,-7; -2,4] = [0.6,-0.7; -0.2,0.4]
  
  Verify A·A⁻¹ = I:
    Row1: [4·0.6+7·(-0.2), 4·(-0.7)+7·0.4] = [2.4-1.4, -2.8+2.8] = [1,0] ✅
    Row2: [2·0.6+6·(-0.2), 2·(-0.7)+6·0.4] = [1.2-1.2, -1.4+2.4] = [0,1] ✅
```

---

## 🧮 P9: Column Space, Null Space & Rank

> 📘 Theory: [Ch 7](./Essence_of_Linear_Algebra_THEORY.md#chapter-7--inverse-matrices-column-space--null-space) | ⬆️ [Problem Index](#-problem-index)

**Problem:** A=[[1,2,1],[2,4,2],[3,6,3]]. Find (a) det, (b) rank, (c) column space, (d) null space.

**Rules:** Rank-Nullity: rank+nullity=#columns. Column space=span of independent columns.

```
  (a) Row2=2·Row1, Row3=3·Row1 → det=0 (rows dependent)
  
  (b) All columns are multiples of [1,2,3]:
      Col2=2·Col1, Col3=1·Col1 → rank=1
  
  (c) Col space = span{[1,2,3]} = a LINE in direction [1,2,3]
  
  (d) Null space: solve Ax⃗=0⃗
      Only independent equation: x+2y+z=0
      Free vars: y,z (since rank=1, nullity=3-1=2)
      y=1,z=0 → x=-2 → [-2,1,0]
      y=0,z=1 → x=-1 → [-1,0,1]
      
      Null space = span{[-2,1,0], [-1,0,1]} = a 2D PLANE
      
      Check: rank(1)+nullity(2)=3=#columns ✅
```

---

## 🧮 P10: Dot Product & Projection

> 📘 Theory: [Ch 9 — Dot Products](./Essence_of_Linear_Algebra_THEORY.md#chapter-9--dot-products--duality) | ⬆️ [Problem Index](#-problem-index)

**Problem:** v⃗=[1,2,3], w⃗=[4,-5,6]. (a) v⃗·w⃗, (b) perpendicular?, (c) projection of w⃗ onto v⃗.

**Rules:** v⃗·w⃗=Σvᵢwᵢ. If 0→perpendicular. proj=(v⃗·w⃗/v⃗·v⃗)·v⃗.

```
  (a) v⃗·w⃗ = 1·4+2·(-5)+3·6 = 4-10+18 = 12
  
  (b) 12≠0 → NOT perpendicular
  
  (c) v⃗·v⃗ = 1+4+9 = 14
      proj = (12/14)·[1,2,3] = (6/7)·[1,2,3] = [6/7, 12/7, 18/7]
      ≈ [0.857, 1.714, 2.571]
```

---

## 🧮 P11: Cross Product

> 📘 Theory: [Ch 10 — Cross Products](./Essence_of_Linear_Algebra_THEORY.md#chapter-10--cross-products) | ⬆️ [Problem Index](#-problem-index)

**Problem:** v⃗=[2,3,4], w⃗=[5,6,7]. (a) v⃗×w⃗, (b) verify perpendicular, (c) parallelogram area.

**Rule:** v⃗×w⃗ = [v₂w₃−v₃w₂, v₃w₁−v₁w₃, v₁w₂−v₂w₁]
```
  Component 1: "2nd×3rd minus 3rd×2nd" → indices (2,3)
  Component 2: "3rd×1st minus 1st×3rd" → indices (3,1)
  Component 3: "1st×2nd minus 2nd×1st" → indices (1,2)
```

```
  (a) v⃗×w⃗ = [3·7−4·6, 4·5−2·7, 2·6−3·5]
           = [21-24, 20-14, 12-15]
           = [-3, 6, -3]
  
  (b) Check: [-3,6,-3]·[2,3,4] = -6+18-12 = 0 ✅ perpendicular to v⃗
      Check: [-3,6,-3]·[5,6,7] = -15+36-21 = 0 ✅ perpendicular to w⃗
  
  (c) Area = |v⃗×w⃗| = √(9+36+9) = √54 = 3√6 ≈ 7.35
```

---

## 🧮 P12: Cramer's Rule

> 📘 Theory: [Ch 12 — Cramer's Rule](./Essence_of_Linear_Algebra_THEORY.md#chapter-12--cramers-rule-explained-geometrically) | ⬆️ [Problem Index](#-problem-index)

**Problem:** Solve 3x+2y=5, x−y=1 using Cramer's Rule.

**Rule:** x=det(Aₓ)/det(A), y=det(Aᵧ)/det(A). Replace the column for each variable with b⃗.

```
  A = [3,2; 1,-1]    b⃗ = [5,1]
  
  Step 1: det(A) = 3·(-1)−2·1 = -3-2 = -5     (≠0, unique solution exists!)
  
  Step 2: x — replace COLUMN 1 with b⃗:
    Aₓ = [5,2; 1,-1]
    det(Aₓ) = 5·(-1)−2·1 = -5-2 = -7
    x = -7/-5 = 7/5 = 1.4
  
  Step 3: y — replace COLUMN 2 with b⃗:
    Aᵧ = [3,5; 1,1]
    det(Aᵧ) = 3·1−5·1 = 3-5 = -2
    y = -2/-5 = 2/5 = 0.4
  
  Verify: 3(7/5)+2(2/5) = 21/5+4/5 = 25/5 = 5 ✅
          (7/5)−(2/5) = 5/5 = 1 ✅
```

---

## 🧮 P13: Change of Basis

> 📘 Theory: [Ch 13 — Change of Basis](./Essence_of_Linear_Algebra_THEORY.md#chapter-13--change-of-basis) | ⬆️ [Problem Index](#-problem-index)

**Problem:** New basis b⃗₁=[2,1], b⃗₂=[1,3]. (a) Change-of-basis matrix P. (b) Convert [7,8] to new basis. (c) If [3,1] in new basis, what in standard?

**Rule:** P=[basis vectors as columns]. P·[new]==[old]. P⁻¹·[old]=[new].

```
  (a) P = [2,1; 1,3]   (new basis vectors as columns)
  
  (b) Need P⁻¹·[7,8]:
      det(P) = 2·3−1·1 = 5
      P⁻¹ = (1/5)·[3,-1; -1,2] = [0.6,-0.2; -0.2,0.4]
      
      P⁻¹·[7,8] = [0.6·7+(-0.2)·8, (-0.2)·7+0.4·8]
                 = [4.2-1.6, -1.4+3.2] = [2.6, 1.8]
      
      Verify: 2.6·[2,1]+1.8·[1,3] = [5.2,2.6]+[1.8,5.4] = [7,8] ✅
  
  (c) P·[3,1] = [2·3+1·1, 1·3+3·1] = [7, 6]
      In standard coords: [7, 6]
```

---

## 🧮 P14: Eigenvalues & Eigenvectors (Full Computation)

> 📘 Theory: [Ch 14 — Eigenvectors](./Essence_of_Linear_Algebra_THEORY.md#chapter-14--eigenvectors--eigenvalues) | ⬆️ [Problem Index](#-problem-index)

**Problem:** Find eigenvalues and eigenvectors of A=[[4,2],[1,3]].

**Rules:** det(A−λI)=0 for eigenvalues. Then solve (A−λI)v⃗=0⃗ for eigenvectors.

```
  Step 1: Characteristic equation
    A−λI = [4-λ, 2; 1, 3-λ]
    det = (4-λ)(3-λ)−2·1 = 12-7λ+λ²-2 = λ²-7λ+10 = 0
    Factor: (λ-5)(λ-2)=0
    λ₁=5, λ₂=2
  
  Step 2: Eigenvectors for λ₁=5
    (A-5I)v⃗=0 → [-1,2; 1,-2]·[x,y]=[0,0]
    Row 1: -x+2y=0 → x=2y
    Choose y=1: eigenvector v₁=[2,1]
    Verify: A·[2,1]=[4·2+2·1, 1·2+3·1]=[10,5]=5·[2,1] ✅
  
  Step 3: Eigenvectors for λ₂=2
    (A-2I)v⃗=0 → [2,2; 1,1]·[x,y]=[0,0]
    Row 1: 2x+2y=0 → x=-y
    Choose y=1: eigenvector v₂=[-1,1]
    Verify: A·[-1,1]=[4·(-1)+2·1, 1·(-1)+3·1]=[-2,2]=2·[-1,1] ✅
```

---

## 🧮 P15: Diagonalization & Matrix Power

> 📘 Theory: [Ch 14](./Essence_of_Linear_Algebra_THEORY.md#chapter-14--eigenvectors--eigenvalues) | ⬆️ [Problem Index](#-problem-index)

**Problem:** Using P14 results, diagonalize A and compute A³.

**Rule:** A=PDP⁻¹ → Aⁿ=PDⁿP⁻¹. P=[eigenvectors], D=diag(eigenvalues).

```
  P = [2,-1; 1,1]    D = [5,0; 0,2]
  
  det(P)=2·1-(-1)·1=3    P⁻¹=(1/3)·[1,1; -1,2]
  
  D³ = [125,0; 0,8]    (just cube each diagonal entry!)
  
  P·D³ = [2,-1; 1,1]·[125,0; 0,8] = [250,-8; 125,8]
  
  A³ = (P·D³)·P⁻¹ = [250,-8; 125,8]·(1/3)·[1,1; -1,2]
     = (1/3)·[250+8, 250-16; 125-8, 125+16]
     = (1/3)·[258, 234; 117, 141]
     = [86, 78; 39, 47]
  
  Quick verify: A²=A·A=[18,14;7,11], A³=A²·A=[86,78;39,47] ✅
```

---

## 🧮 P16: Mean-Product Eigenvalue Trick

> 📘 Theory: [Ch 15 — Quick Trick](./Essence_of_Linear_Algebra_THEORY.md#chapter-15--a-quick-trick-for-computing-eigenvalues) | ⬆️ [Problem Index](#-problem-index)

**Problem:** Find eigenvalues using the trick for: (a) [[7,2],[0,3]]  (b) [[2,1],[1,2]]  (c) [[0,-1],[1,0]]

**Rule:** m=(a+d)/2, p=ad−bc, λ=m±√(m²−p)

```
  (a) m=(7+3)/2=5,  p=7·3-2·0=21
      λ=5±√(25-21)=5±2   →  λ₁=7, λ₂=3
  
  (b) m=(2+2)/2=2,  p=2·2-1·1=3
      λ=2±√(4-3)=2±1     →  λ₁=3, λ₂=1
  
  (c) m=(0+0)/2=0,  p=0·0-(-1)·1=1
      λ=0±√(0-1)=±√(-1)  →  λ=±i  (COMPLEX!)
      This is a 90° rotation — no vector stays on its line!
```

---

## 🧮 P17: Vector Space Verification

> 📘 Theory: [Ch 16 — Abstract Spaces](./Essence_of_Linear_Algebra_THEORY.md#chapter-16--abstract-vector-spaces) | ⬆️ [Problem Index](#-problem-index)

**Problem:** Which are vector spaces? (a) All 2×2 matrices (b) Polynomials degree≤3 (c) Polynomials degree exactly 2 (d) Functions f where f(0)=0

**Rule:** Check closure under addition and scaling. All 8 axioms must hold.

```
  (a) All 2×2 matrices → YES ✅
      Sum of two 2×2 = 2×2. Scalar times 2×2 = 2×2. Zero matrix exists.
  
  (b) Polynomials degree ≤ 3 → YES ✅
      Sum of degree≤3 has degree≤3. Scalar doesn't change degree. Zero poly ∈ set.
  
  (c) Polynomials degree EXACTLY 2 → NO ❌
      (x²+1)+(-x²+2)=3 — degree 0, NOT 2! Closure under addition FAILS.
      Also zero polynomial has degree undefined, not 2.
  
  (d) Functions where f(0)=0 → YES ✅
      If f(0)=0 and g(0)=0: (f+g)(0)=0+0=0 ✅
      (cf)(0)=c·0=0 ✅. Zero function: 0(0)=0 ✅
```

---

## 🧮 P18: Derivative as Linear Transformation

> 📘 Theory: [Ch 16](./Essence_of_Linear_Algebra_THEORY.md#chapter-16--abstract-vector-spaces) | ⬆️ [Problem Index](#-problem-index)

**Problem:** Derivative D maps polynomials degree≤2. Basis={1,x,x²}. (a) Matrix of D. (b) Null space. (c) Rank.

**Rule:** Apply D to each basis element. Express result in same basis → columns of matrix.

```
  (a) D(1)=0   = 0·(1)+0·(x)+0·(x²)  → col [0,0,0]
      D(x)=1   = 1·(1)+0·(x)+0·(x²)  → col [1,0,0]
      D(x²)=2x = 0·(1)+2·(x)+0·(x²)  → col [0,2,0]
      
      Matrix = [ 0  1  0 ]
               [ 0  0  2 ]
               [ 0  0  0 ]
  
  (b) Null space: polynomials p where p'=0 → CONSTANTS
      Null space = span{1} → in coords: span{[1,0,0]}
      Verify: D·[1,0,0]=[0,0,0] ✅
  
  (c) Rank = 2 (columns [1,0,0] and [0,2,0] are independent)
      Check: rank(2)+nullity(1)=3=dimension of domain ✅
```

---

> 🔗 **Theory explanations:** [← Theory Guide](./Essence_of_Linear_Algebra_THEORY.md)
>
> 🔗 **Master hub:** [← INDEX](./Essence_of_Linear_Algebra_INDEX.md)
>
> 🎓 **Created for:** ODS
