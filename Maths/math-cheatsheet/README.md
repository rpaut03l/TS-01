# 📐 Data Science Mathematics — Master Cheatsheet

> **Covers:** Linear Algebra, Calculus, Optimization, Probability & Statistics  
> **Purpose:** Quick-reference for all rules, formulas, and notations used across ODS coursework  
> **Level:** Written for absolute beginners — every symbol explained

---

## 📑 Table of Contents

1. [Notation Guide — What Every Symbol Means](#1-notation-guide--what-every-symbol-means)
   - [Sets & Spaces](#sets--spaces)
   - [Vectors & Matrices](#vectors--matrices)
   - [Functions & Calculus](#functions--calculus)
   - [Optimization-Specific](#optimization-specific)
   - [Probability & Statistics](#probability--statistics)
2. [Linear Algebra Rules & Formulas](#2-linear-algebra-rules--formulas)
   - [Vector Operations](#vector-operations)
   - [Matrix Operations](#matrix-operations)
   - [Special Matrices](#special-matrices)
   - [Eigenvalues & Eigenvectors](#eigenvalues--eigenvectors)
   - [Norms](#norms)
   - [Matrix Decompositions](#matrix-decompositions)
3. [Calculus Rules & Formulas](#3-calculus-rules--formulas)
   - [Single Variable Derivatives](#single-variable-derivatives)
   - [Common Derivatives Table](#common-derivatives-table)
   - [Matrix Calculus (Gradients & Hessians)](#matrix-calculus-gradients--hessians)
   - [Key Matrix Calculus Identities](#key-matrix-calculus-identities)
   - [Integration Essentials](#integration-essentials)
   - [Taylor Expansion](#taylor-expansion)
4. [Optimization Formulas](#4-optimization-formulas)
   - [Convexity Conditions](#convexity-conditions)
   - [Gradient Descent Family](#gradient-descent-family)
   - [Line Search Methods](#line-search-methods)
   - [Newton & Quasi-Newton](#newton--quasi-newton)
   - [Conjugate Gradient](#conjugate-gradient)
   - [Convergence Rates](#convergence-rates)
5. [Probability & Statistics Formulas](#5-probability--statistics-formulas)
   - [Basic Probability](#basic-probability)
   - [Distributions](#distributions)
   - [Expectation & Variance](#expectation--variance)
   - [Maximum Likelihood Estimation](#maximum-likelihood-estimation)
6. [Linear Regression Formulas](#6-linear-regression-formulas)
7. [Inequalities & Bounds](#7-inequalities--bounds)
8. [Greek Letters Quick Reference](#8-greek-letters-quick-reference)
9. [Common Pitfalls & Gotchas](#9-common-pitfalls--gotchas)

---

## 1. Notation Guide — What Every Symbol Means

[⬆️ Back to Top](#-table-of-contents)

### Sets & Spaces

| Symbol | Name | Meaning | Example |
|--------|------|---------|---------|
| ℝ | Real numbers | All real numbers (the number line) | 3.14, −7, √2 ∈ ℝ |
| ℝⁿ | n-dimensional real space | Vectors with n real entries | ℝ³ = 3D space |
| ℝᵐˣⁿ | Matrix space | m × n matrices with real entries | A ∈ ℝ³ˣ⁴ = 3 rows, 4 columns |
| ∈ | "belongs to" / "is in" | Element membership | x ∈ ℝⁿ means x is an n-dim vector |
| ∅ or {} | Empty set | Set with nothing in it | Null(A) ∩ Null(B) = {0} |
| ⊂ | Subset | One set is inside another | Strongly convex ⊂ Convex |
| ∀ | "for all" | Universal quantifier | ∀x ∈ ℝⁿ means "for every x" |
| ∃ | "there exists" | Existence quantifier | ∃L > 0 such that ... |
| ⟺ | "if and only if" | Two-way implication | A ⟺ B means A implies B AND B implies A |
| ⟹ | "implies" | One-way implication | A ⟹ B means "if A then B" |
| {0} | Zero set | Set containing only the zero vector | Null(A) = {0} means only 0 maps to 0 |

### Vectors & Matrices

| Symbol | Name | Meaning |
|--------|------|---------|
| **x**, x | Vector | A column of numbers (bold or lowercase) |
| x_i | i-th component | Single entry of vector x |
| A, B, Q | Matrix | Uppercase letters = matrices |
| Aᵀ | Transpose | Flip rows ↔ columns: (Aᵀ)ᵢⱼ = Aⱼᵢ |
| A⁻¹ | Inverse | Matrix such that A⁻¹A = I |
| I | Identity matrix | Diagonal of 1s; Ix = x for all x |
| 0 | Zero vector/matrix | All entries are zero |
| diag(λ₁,...,λₙ) | Diagonal matrix | Only diagonal entries are nonzero |
| xᵀy or x·y | Dot product | Σᵢ xᵢyᵢ = scalar |
| xyᵀ | Outer product | n×n matrix: (xyᵀ)ᵢⱼ = xᵢyⱼ |
| ‖x‖ or ‖x‖₂ | Euclidean norm | √(Σ xᵢ²) = "length" of vector |
| ‖A‖ | Spectral norm | Largest singular value of A |
| Null(A) | Null space | {x : Ax = 0} — vectors A "kills" |
| rank(A) | Rank | Number of linearly independent rows/columns |
| det(A) | Determinant | Scalar measuring "volume scaling" of A |
| tr(A) | Trace | Sum of diagonal entries: Σ Aᵢᵢ |

### Functions & Calculus

| Symbol | Name | Meaning |
|--------|------|---------|
| f : ℝⁿ → ℝ | Function signature | f takes n-dim vector, returns scalar |
| f(x) | Function value | Output of f at point x |
| ∇f(x) | Gradient | Vector of partial derivatives [∂f/∂x₁, ..., ∂f/∂xₙ]ᵀ |
| ∇²f(x) | Hessian | n×n matrix of second derivatives |
| ∂f/∂xᵢ | Partial derivative | Derivative w.r.t. xᵢ holding others fixed |
| f'(x) | Derivative (1D) | Rate of change of f |
| f''(x) | Second derivative (1D) | Rate of change of the rate of change |
| ∫ₐᵇ f(x)dx | Definite integral | Area under curve from a to b |
| O(·) | Big-O notation | Upper bound on growth rate |
| o(·) | Little-o notation | Grows strictly slower |
| ≈ | Approximately | Nearly equal |
| lim | Limit | Value approached as variable tends to something |

### Optimization-Specific

| Symbol | Name | Meaning |
|--------|------|---------|
| x* | Optimal point | The minimizer: f(x*) ≤ f(x) for all x |
| f* | Optimal value | f* = f(x*) = minimum function value |
| x_k | k-th iterate | Current point at iteration k |
| p_k | Search direction | Direction to move from x_k |
| α_k | Step size / learning rate | How far to move along p_k |
| g_k | Gradient shorthand | g_k = ∇f(x_k) |
| H_k | Hessian (or approx) | ∇²f(x_k) or its approximation |
| B_k | Hessian approximation | Quasi-Newton Hessian estimate |
| s_k | Step vector | s_k = x_{k+1} − x_k |
| y_k | Gradient change | y_k = ∇f(x_{k+1}) − ∇f(x_k) |
| L | Lipschitz constant | Bounds how fast gradient changes |
| μ | Strong convexity parameter | Minimum curvature |
| κ | Condition number | κ = L/μ = ratio of max to min curvature |
| c₁ | Armijo constant | Sufficient decrease parameter (≈ 10⁻⁴) |
| ρ | Contraction factor | Backtracking shrink rate (≈ 0.5) |
| ε | Tolerance | Convergence threshold |

### Probability & Statistics

| Symbol | Name | Meaning |
|--------|------|---------|
| P(A) | Probability | Likelihood of event A |
| E[X] | Expectation | Average/mean value of random variable X |
| Var(X) | Variance | E[(X − E[X])²] = spread around mean |
| σ² | Variance (common notation) | Same as Var(X) |
| σ | Standard deviation | √Var(X) |
| 𝒩(μ, σ²) | Normal distribution | Bell curve with mean μ, variance σ² |
| Σ | Summation | Σᵢ₌₁ⁿ xᵢ = x₁ + x₂ + ... + xₙ |
| ∏ | Product | ∏ᵢ₌₁ⁿ xᵢ = x₁ × x₂ × ... × xₙ |
| argmin | Argument of minimum | Value of x that minimizes f(x) |
| sup / inf | Supremum / Infimum | Least upper bound / Greatest lower bound |

---

## 2. Linear Algebra Rules & Formulas

[⬆️ Back to Top](#-table-of-contents)

### Vector Operations

**Dot Product (Inner Product):**
```
xᵀy = Σᵢ xᵢyᵢ = ‖x‖ · ‖y‖ · cos(θ)

where θ is the angle between x and y
```

| Property | Formula |
|----------|---------|
| Commutative | xᵀy = yᵀx |
| Distributive | xᵀ(y + z) = xᵀy + xᵀz |
| Scalar factor | (cx)ᵀy = c(xᵀy) |
| Self-dot | xᵀx = ‖x‖² ≥ 0 |
| Orthogonality | x ⊥ y ⟺ xᵀy = 0 |

**Outer Product:**
```
xyᵀ = n×n matrix where (xyᵀ)ᵢⱼ = xᵢyⱼ

Rank of xyᵀ = 1 (always!)
```

### Matrix Operations

**Matrix Multiplication (A ∈ ℝᵐˣⁿ, B ∈ ℝⁿˣᵖ):**
```
(AB)ᵢⱼ = Σₖ Aᵢₖ Bₖⱼ      Result: ℝᵐˣᵖ
```

| Rule | Formula | Kid-Friendly |
|------|---------|-------------|
| NOT commutative | AB ≠ BA in general | Order matters! |
| Associative | (AB)C = A(BC) | Grouping doesn't matter |
| Distributive | A(B + C) = AB + AC | Works like regular numbers |
| Transpose of product | (AB)ᵀ = BᵀAᵀ | **Reverses order!** |
| Inverse of product | (AB)⁻¹ = B⁻¹A⁻¹ | **Reverses order!** |
| Transpose of transpose | (Aᵀ)ᵀ = A | Double flip = original |
| Inverse of transpose | (Aᵀ)⁻¹ = (A⁻¹)ᵀ | Can do either first |

**Trace Properties:**
```
tr(A) = Σᵢ Aᵢᵢ (sum of diagonal)

tr(AB) = tr(BA)                   ← cyclic property
tr(A + B) = tr(A) + tr(B)
tr(cA) = c · tr(A)
tr(xᵀAx) = xᵀAx                 ← scalar = its own trace
```

### Special Matrices

| Type | Definition | Properties | Example |
|------|-----------|------------|---------|
| **Symmetric** | A = Aᵀ | Real eigenvalues; orthogonal eigenvectors | Hessian ∇²f |
| **Positive Definite (PD)** | xᵀAx > 0 ∀x ≠ 0 | All eigenvalues > 0; invertible | Q in quadratic form |
| **Positive Semi-Definite (PSD)** | xᵀAx ≥ 0 ∀x | All eigenvalues ≥ 0 | AᵀA (always PSD) |
| **Orthogonal** | AᵀA = AAᵀ = I | A⁻¹ = Aᵀ; preserves lengths | Rotation matrices |
| **Diagonal** | Aᵢⱼ = 0 for i≠j | Easy to invert: (D⁻¹)ᵢᵢ = 1/Dᵢᵢ | diag(λ₁,...,λₙ) |
| **Identity** | Iᵢⱼ = δᵢⱼ | Ax = x; AI = IA = A | n×n identity I |

**How to check Positive Definiteness:**
```
A is PD ⟺ all eigenvalues > 0
       ⟺ all leading minors > 0 (Sylvester's criterion)
       ⟺ xᵀAx > 0 for all x ≠ 0
       ⟺ A = LLᵀ (Cholesky factorization exists)
```

**Key Identity — AᵀA is always PSD:**
```
xᵀ(AᵀA)x = (Ax)ᵀ(Ax) = ‖Ax‖² ≥ 0   ✅
```

### Eigenvalues & Eigenvectors

**Definition:**
```
Av = λv    where v ≠ 0

v = eigenvector (direction that A just "stretches")
λ = eigenvalue (the stretching factor)
```

**Key Properties:**

| Property | Formula |
|----------|---------|
| Characteristic equation | det(A − λI) = 0 |
| Sum of eigenvalues | Σ λᵢ = tr(A) |
| Product of eigenvalues | ∏ λᵢ = det(A) |
| Eigenvalues of A⁻¹ | 1/λᵢ |
| Eigenvalues of A² | λᵢ² |
| Eigenvalues of A + cI | λᵢ + c |
| Eigenvalues of cA | cλᵢ |

**For Symmetric Matrices (most important in optimization):**
- All eigenvalues are **real**
- Eigenvectors are **orthogonal**
- A = QΛQᵀ where Q is orthogonal, Λ = diag(λ₁,...,λₙ)
- Spectral norm: ‖A‖ = max|λᵢ|

### Norms

**Vector Norms:**

| Norm | Formula | Geometric Meaning |
|------|---------|-------------------|
| ‖x‖₁ (L1) | Σ \|xᵢ\| | Manhattan distance |
| ‖x‖₂ (L2) | √(Σ xᵢ²) | Euclidean distance (default) |
| ‖x‖∞ (L∞) | max \|xᵢ\| | Largest component |
| ‖x‖ₚ (Lp) | (Σ \|xᵢ\|ᵖ)^(1/p) | Generalized |

**Matrix Norms:**

| Norm | Formula | Usage |
|------|---------|-------|
| Spectral norm ‖A‖₂ | max singular value = max\|λᵢ\| (for symmetric A) | Lipschitz constants |
| Frobenius norm ‖A‖_F | √(Σᵢⱼ Aᵢⱼ²) = √(tr(AᵀA)) | General purpose |

**Cauchy-Schwarz Inequality (THE most important inequality):**
```
|xᵀy| ≤ ‖x‖ · ‖y‖

Equality holds when x = cy (parallel vectors)
```

### Matrix Decompositions

| Decomposition | Formula | When Used |
|---------------|---------|-----------|
| **Eigendecomposition** | A = QΛQᵀ (symmetric) | Understanding matrix behavior |
| **Cholesky** | A = LLᵀ (PD matrices) | Efficient solving of Ax = b |
| **SVD** | A = UΣVᵀ | Any matrix; dimensionality reduction |
| **LU** | A = LU | General linear system solving |
| **QR** | A = QR | Least squares, orthogonalization |

---

## 3. Calculus Rules & Formulas

[⬆️ Back to Top](#-table-of-contents)

### Single Variable Derivatives

**Basic Rules:**

| Rule | Formula | Example |
|------|---------|---------|
| Constant | d/dx(c) = 0 | d/dx(5) = 0 |
| Power | d/dx(xⁿ) = nxⁿ⁻¹ | d/dx(x⁴) = 4x³ |
| Sum | d/dx(f + g) = f' + g' | d/dx(x² + x) = 2x + 1 |
| Product | d/dx(fg) = f'g + fg' | d/dx(x·eˣ) = eˣ + xeˣ |
| Quotient | d/dx(f/g) = (f'g − fg')/g² | d/dx(sin x/x) = ... |
| Chain | d/dx f(g(x)) = f'(g(x))·g'(x) | d/dx(e^(x²)) = 2x·e^(x²) |
| Scalar mult | d/dx(cf) = c·f' | d/dx(3x²) = 6x |

### Common Derivatives Table

| Function f(x) | Derivative f'(x) | Used In |
|---------------|-------------------|---------|
| xⁿ | nxⁿ⁻¹ | Polynomial objectives |
| eˣ | eˣ | Logistic loss, softmax |
| ln(x) | 1/x | Log-likelihood, entropy |
| log(1 + eˣ) | eˣ/(1+eˣ) = σ(x) | **Logistic loss** (Q8) |
| σ(x) = 1/(1+e⁻ˣ) | σ(x)(1−σ(x)) | Sigmoid derivative |
| sin(x) | cos(x) | Signal processing |
| cos(x) | −sin(x) | Signal processing |
| \|x\| | sign(x) | L1 regularization (subgradient) |
| x² | 2x | Quadratic objectives |
| √x | 1/(2√x) | Norm computations |

**Chain Rule Expanded (for optimization):**
```
If h(x) = f(g(x)):

h'(x) = f'(g(x)) · g'(x)

Example: f(x) = (x − 2)²
  Let g(x) = x − 2, f(u) = u²
  f'(x) = 2(x − 2) · 1 = 2(x − 2)
```

### Matrix Calculus (Gradients & Hessians)

**Gradient (∇f) — Vector of All Partial Derivatives:**
```
For f : ℝⁿ → ℝ:

         ⎡ ∂f/∂x₁ ⎤
∇f(x) = ⎢ ∂f/∂x₂ ⎥    ← column vector (n × 1)
         ⎢   ⋮    ⎥
         ⎣ ∂f/∂xₙ ⎦
```

**Hessian (∇²f) — Matrix of All Second Partial Derivatives:**
```
For f : ℝⁿ → ℝ:

              ⎡ ∂²f/∂x₁²     ∂²f/∂x₁∂x₂  ⋯  ∂²f/∂x₁∂xₙ ⎤
∇²f(x) = H = ⎢ ∂²f/∂x₂∂x₁   ∂²f/∂x₂²    ⋯  ∂²f/∂x₂∂xₙ ⎥
              ⎢      ⋮              ⋮        ⋱       ⋮       ⎥
              ⎣ ∂²f/∂xₙ∂x₁   ∂²f/∂xₙ∂x₂  ⋯  ∂²f/∂xₙ²   ⎦

Always symmetric (if f is C²): ∂²f/∂xᵢ∂xⱼ = ∂²f/∂xⱼ∂xᵢ
```

### Key Matrix Calculus Identities

**These are the formulas you'll use MOST in optimization:**

| Expression f(x) | Gradient ∇f(x) | Hessian ∇²f(x) |
|-----------------|-----------------|-----------------|
| aᵀx | a | 0 |
| xᵀx = ‖x‖² | 2x | 2I |
| xᵀAx | (A + Aᵀ)x = 2Ax (if A symmetric) | A + Aᵀ = 2A (if symmetric) |
| ½xᵀQx | Qx (if Q symmetric) | Q |
| ½xᵀQx − bᵀx | Qx − b | Q |
| ‖Ax − b‖² | 2Aᵀ(Ax − b) | 2AᵀA |
| ½‖Ax − b‖² | Aᵀ(Ax − b) | AᵀA |

**Memorization Trick:**
- Linear in x → gradient is the coefficient → Hessian is 0
- Quadratic in x → gradient is linear in x → Hessian is constant
- Cubic in x → gradient is quadratic → Hessian is linear (not constant)

### Integration Essentials

| Integral | Result | Usage |
|----------|--------|-------|
| ∫ xⁿ dx | xⁿ⁺¹/(n+1) + C | Fundamental theorem proofs |
| ∫₀¹ t dt | 1/2 | Descent lemma derivation (Q4) |
| ∫₀¹ t² dt | 1/3 | Higher-order bounds |
| ∫ eˣ dx | eˣ + C | Probability distributions |
| ∫ 1/x dx | ln\|x\| + C | Log-likelihood |

### Taylor Expansion

**Single Variable:**
```
f(x + h) = f(x) + f'(x)·h + ½f''(x)·h² + O(h³)
```

**Multivariate (THE key formula for optimization):**
```
First-order:   f(x + p) ≈ f(x) + ∇f(x)ᵀp

Second-order:  f(x + p) ≈ f(x) + ∇f(x)ᵀp + ½pᵀ∇²f(x)p
```

**Why It Matters:**
- First-order → gives us **gradient descent** direction
- Second-order → gives us **Newton's** direction (Q22)
- The approximation quality depends on how "smooth" f is (Lipschitz constant L)

---

## 4. Optimization Formulas

[⬆️ Back to Top](#-table-of-contents)

### Convexity Conditions

| Type | Definition | Hessian Condition |
|------|-----------|-------------------|
| **Convex** | f(λx+(1−λ)y) ≤ λf(x)+(1−λ)f(y) | ∇²f(x) ⪰ 0 (PSD) |
| **Strictly Convex** | f(λx+(1−λ)y) < λf(x)+(1−λ)f(y) for x≠y | ∇²f(x) ≻ 0 at most points |
| **μ-Strongly Convex** | f(y) ≥ f(x) + ∇fᵀ(y−x) + (μ/2)‖y−x‖² | ∇²f(x) ⪰ μI |
| **L-Smooth** | ‖∇f(x) − ∇f(y)‖ ≤ L‖x−y‖ | ∇²f(x) ⪯ LI |
| **L-Smooth + μ-Strong** | Both conditions hold | μI ⪯ ∇²f(x) ⪯ LI |

**Descent Lemma (L-smooth f):**
```
f(y) ≤ f(x) + ∇f(x)ᵀ(y − x) + (L/2)‖y − x‖²
```

**Strong Convexity Lower Bound (μ-strongly convex f):**
```
f(y) ≥ f(x) + ∇f(x)ᵀ(y − x) + (μ/2)‖y − x‖²
```

### Gradient Descent Family

| Method | Update Rule | Step Size |
|--------|-------------|-----------|
| **Fixed Step GD** | x_{k+1} = x_k − α∇f(x_k) | α = 1/L (safe) |
| **Exact Line Search** | x_{k+1} = x_k − α_k∇f(x_k) | α_k = ‖g_k‖²/(g_kᵀQg_k) for quadratic |
| **Backtracking GD** | x_{k+1} = x_k − α_k∇f(x_k) | α_k from Armijo backtracking |
| **SGD** | x_{k+1} = x_k − α_k∇f_{iₖ}(x_k) | α_k = O(1/k), Robbins-Monro |
| **Mini-Batch SGD** | x_{k+1} = x_k − α_k(1/b)Σ_{i∈B}∇fᵢ(x_k) | Same as SGD |

### Line Search Methods

**Armijo Condition (Sufficient Decrease):**
```
f(x_k + αp_k) ≤ f(x_k) + c₁ · α · ∇f(x_k)ᵀp_k

c₁ ∈ (0, 1), typically c₁ = 10⁻⁴
```

**Wolfe Conditions (Armijo + Curvature):**
```
Armijo:    f(x_k + αp_k) ≤ f(x_k) + c₁α∇f_kᵀp_k
Curvature: ∇f(x_k + αp_k)ᵀp_k ≥ c₂∇f_kᵀp_k

0 < c₁ < c₂ < 1, typically c₁ = 10⁻⁴, c₂ = 0.9
```

**Backtracking Algorithm:**
```
α ← 1;  while Armijo violated:  α ← ρ·α
```

**Robbins-Monro (SGD step sizes):**
```
Σ α_k = ∞    AND    Σ α_k² < ∞

Classic choice: α_k = c/k
```

### Newton & Quasi-Newton

| Method | Direction p_k | Cost per Step | Convergence |
|--------|--------------|---------------|-------------|
| **Newton** | −[∇²f(x_k)]⁻¹∇f(x_k) | O(n³) | Quadratic (local) |
| **Modified Newton** | −[∇²f(x_k) + λI]⁻¹∇f(x_k) | O(n³) | Quadratic (global) |
| **BFGS** | −H_k∇f(x_k) | O(n²) | Superlinear |
| **DFP** | −H_k∇f(x_k) | O(n²) | Superlinear |
| **L-BFGS** | −H_k∇f(x_k) (implicit) | O(mn) | Superlinear |

**Secant Equation:** B_{k+1}s_k = y_k

**BFGS Inverse Hessian Update:**
```
H_{k+1} = (I − ρ_k s_k y_kᵀ) H_k (I − ρ_k y_k s_kᵀ) + ρ_k s_k s_kᵀ

where ρ_k = 1/(y_kᵀs_k), s_k = x_{k+1}−x_k, y_k = g_{k+1}−g_k
```

### Conjugate Gradient

**Q-Conjugacy:** pᵢᵀQpⱼ = 0 for i ≠ j

**CG Step Size:** α_k = r_kᵀr_k / (p_kᵀQp_k)

**CG Beta:** β_{k+1} = r_{k+1}ᵀr_{k+1} / (r_kᵀr_k)

**Fletcher-Reeves:** β^FR = ‖g_{k+1}‖² / ‖g_k‖²

**Polak-Ribière:** β^PR = g_{k+1}ᵀ(g_{k+1} − g_k) / ‖g_k‖²

### Convergence Rates

| Rate Name | Math Meaning | Typical Method |
|-----------|-------------|----------------|
| **Sublinear O(1/k)** | Error ≤ C/k | GD on convex functions |
| **Linear O(rᵏ)** | Error ≤ C·rᵏ, r < 1 | GD on strongly convex |
| **Superlinear** | ‖e_{k+1}‖/‖e_k‖ → 0 | BFGS |
| **Quadratic** | ‖e_{k+1}‖ ≤ C·‖e_k‖² | Newton's method |

**Concrete Bounds:**

```
Convex + L-smooth:
    f(x_k) − f* ≤ L‖x₀ − x*‖² / (2k)

μ-Strongly Convex + L-smooth:
    f(x_k) − f* ≤ (1 − μ/L)ᵏ · (f(x₀) − f*)

Condition Number: κ = L/μ
    Iterations for ε-accuracy: O(κ · log(1/ε))    [GD]
                                O(√κ · log(1/ε))    [CG/Accelerated GD]
```

---

## 5. Probability & Statistics Formulas

[⬆️ Back to Top](#-table-of-contents)

### Basic Probability

| Rule | Formula |
|------|---------|
| Complement | P(Aᶜ) = 1 − P(A) |
| Union | P(A ∪ B) = P(A) + P(B) − P(A ∩ B) |
| Conditional | P(A\|B) = P(A ∩ B) / P(B) |
| Bayes' Theorem | P(A\|B) = P(B\|A)·P(A) / P(B) |
| Independence | P(A ∩ B) = P(A)·P(B) |
| Total Probability | P(A) = Σ P(A\|Bᵢ)P(Bᵢ) |

### Distributions

| Distribution | PDF/PMF | Mean | Variance |
|-------------|---------|------|----------|
| Bernoulli(p) | P(X=1)=p, P(X=0)=1−p | p | p(1−p) |
| Binomial(n,p) | C(n,k)pᵏ(1−p)ⁿ⁻ᵏ | np | np(1−p) |
| Uniform(a,b) | 1/(b−a) | (a+b)/2 | (b−a)²/12 |
| Normal(μ,σ²) | (1/√(2πσ²))exp(−(x−μ)²/(2σ²)) | μ | σ² |
| Exponential(λ) | λe^(−λx) | 1/λ | 1/λ² |

### Expectation & Variance

| Property | Formula |
|----------|---------|
| Linearity of E | E[aX + bY] = aE[X] + bE[Y] |
| Variance definition | Var(X) = E[X²] − (E[X])² |
| Variance of sum (independent) | Var(X + Y) = Var(X) + Var(Y) |
| Variance of scaled | Var(aX) = a²Var(X) |
| Covariance | Cov(X,Y) = E[XY] − E[X]E[Y] |

**Unbiased Estimator (from Q20):**
```
An estimator θ̂ is unbiased if E[θ̂] = θ (true parameter)

SGD: E[∇f_{iₖ}(x)] = ∇f(x)  ← unbiased!
```

### Maximum Likelihood Estimation

```
Given data {x₁,...,xₙ} from distribution p(x|θ):

Likelihood:     L(θ) = ∏ᵢ p(xᵢ|θ)
Log-likelihood: ℓ(θ) = Σᵢ log p(xᵢ|θ)
MLE:            θ* = argmax_θ ℓ(θ)
```

---

## 6. Linear Regression Formulas

[⬆️ Back to Top](#-table-of-contents)

**Model:** y = Xβ + ε

**Loss (MSE):** f(β) = (1/2n)‖Xβ − y‖²

**Gradient:** ∇f(β) = (1/n)Xᵀ(Xβ − y)

**Hessian:** ∇²f(β) = (1/n)XᵀX

**Normal Equations:** (XᵀX)β = Xᵀy

**Closed-form Solution:** β* = (XᵀX)⁻¹Xᵀy

**With Regularization (Ridge):**
```
β* = (XᵀX + λI)⁻¹Xᵀy

λ > 0 ensures invertibility and prevents overfitting
```

**Metrics:**
```
MSE = (1/n) Σ (yᵢ − ŷᵢ)²
R² = 1 − Σ(yᵢ − ŷᵢ)² / Σ(yᵢ − ȳ)²
```

---

## 7. Inequalities & Bounds

[⬆️ Back to Top](#-table-of-contents)

| Inequality | Statement | Usage |
|-----------|-----------|-------|
| **Cauchy-Schwarz** | \|xᵀy\| ≤ ‖x‖·‖y‖ | Bounding dot products |
| **Triangle** | ‖x + y‖ ≤ ‖x‖ + ‖y‖ | Norm bounds |
| **AM-GM** | (a+b)/2 ≥ √(ab) for a,b ≥ 0 | Bounding products |
| **Jensen's** | f(E[X]) ≤ E[f(X)] for convex f | Convexity proofs |
| **Young's** | ab ≤ a²/2 + b²/2 | Splitting products |
| **Spectral** | ‖Ax‖ ≤ ‖A‖·‖x‖ | Matrix-vector bounds |
| **Rayleigh Quotient** | λ_min ≤ xᵀAx/xᵀx ≤ λ_max | Eigenvalue bounds |

**Most Used in ODS (memorize these!):**

```
1. Cauchy-Schwarz:  |∇f(x)ᵀp| ≤ ‖∇f(x)‖ · ‖p‖

2. Descent Lemma:   f(y) ≤ f(x) + ∇fᵀ(y−x) + (L/2)‖y−x‖²

3. Strong Convexity: f(y) ≥ f(x) + ∇fᵀ(y−x) + (μ/2)‖y−x‖²

4. Rayleigh Bound:  λ_min‖x‖² ≤ xᵀQx ≤ λ_max‖x‖²
```

---

## 8. Greek Letters Quick Reference

[⬆️ Back to Top](#-table-of-contents)

| Letter | Name | Common Usage in DS/Optimization |
|--------|------|------|
| α (alpha) | Alpha | Step size / learning rate |
| β (beta) | Beta | CG coefficient; regression coefficients |
| γ (gamma) | Gamma | Discount factor; kernel parameter |
| δ (delta) | Delta | Small change; Kronecker delta |
| ε (epsilon) | Epsilon | Tolerance; small positive number |
| η (eta) | Eta | Learning rate (alternative to α) |
| θ (theta) | Theta | Parameters (ML models); angle |
| κ (kappa) | Kappa | Condition number κ = L/μ |
| λ (lambda) | Lambda | Eigenvalue; regularization parameter |
| μ (mu) | Mu | Strong convexity parameter; mean |
| ρ (rho) | Rho | Backtracking shrink factor; correlation |
| σ (sigma) | Sigma | Singular value; standard deviation |
| Σ (Sigma) | Capital Sigma | Summation; covariance matrix |
| τ (tau) | Tau | Threshold; time constant |
| φ (phi) | Phi | Line search function φ(α) = f(x+αp) |
| ∇ (nabla) | Nabla/Del | Gradient operator |

---

## 9. Common Pitfalls & Gotchas

[⬆️ Back to Top](#-table-of-contents)

### Notation Traps

| Pitfall | Clarification |
|---------|---------------|
| ‖x‖² vs ‖x²‖ | ‖x‖² = (Σxᵢ²) is norm-squared. ‖x²‖ = √(Σxᵢ⁴) is norm of squared vector. **Very different!** |
| xᵀy vs xyᵀ | xᵀy = scalar (dot product). xyᵀ = n×n matrix (outer product). |
| ∇f vs ∇²f | ∇f is a vector (n×1). ∇²f is a matrix (n×n). |
| (AB)ᵀ vs AᵀBᵀ | (AB)ᵀ = **Bᵀ Aᵀ** (reversed!). AᵀBᵀ = (BA)ᵀ. |
| PD vs PSD | PD: xᵀAx > 0 (strict). PSD: xᵀAx ≥ 0 (allows zero). PD ⟹ invertible. PSD ⟹ might not be. |
| f convex vs f' increasing | Same thing! f''(x) ≥ 0 ⟺ f'(x) is non-decreasing ⟺ f is convex. |

### Optimization Traps

| Pitfall | Clarification |
|---------|---------------|
| "Gradient points downhill" | **NO!** ∇f points **UPHILL** (steepest increase). −∇f points downhill. |
| "Small step = convergence" | **NO!** You need **sufficient decrease** (Armijo), not just any decrease. |
| "Newton always converges" | **NO!** Only locally near x* with PD Hessian. Can diverge if started far away. |
| "SGD converges to minimum" | Only with decaying step sizes (Robbins-Monro). Fixed α → oscillates around minimum. |
| "More iterations = better" | Not for SGD! After a point, noise dominates. Use early stopping or decay α. |
| "CG = n iterations always" | In exact arithmetic, yes. With floating point, may need more or less. |

---

[⬆️ Back to Top](#-table-of-contents)

> 💡 **Pro Tip for Exams:** When stuck on a proof, start by writing the DEFINITION of the concept. Most proofs follow directly from definitions + one key inequality.

---

[⬆️ Back to Top](#-table-of-contents)
