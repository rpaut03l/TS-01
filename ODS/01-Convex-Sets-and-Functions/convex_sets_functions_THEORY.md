# Convex Sets & Functions — Theory Guide
### ODS Topic 01 · Lectures 1–2 · Pr K Som

> **Navigation:** [← INDEX](./convex_sets_functions_INDEX.md) · [→ PRACTICE](./convex_sets_functions_PRACTICE.md) · [↑ Master Hub](../ODS_Master_INDEX.md)

---

## 1.1 Convex Sets — Definition

### Easy Story
Imagine you have a blob of Play-Doh on the table. Pick ANY two points inside the blob. Now draw a straight line between them. If that line stays COMPLETELY inside the blob — congratulations, your blob is a **convex set**!

If the line pokes outside (like a star shape or a crescent) — NOT convex!

### Formal Definition

> A set **C ⊆ Rⁿ** is **convex** if for all **x, y ∈ C** and **θ ∈ [0, 1]**:
> 
> **θx + (1 − θ)y ∈ C**

The point `θx + (1-θ)y` traces the line segment from y (at θ=0) to x (at θ=1).

### Visual Diagram

```
   CONVEX (rectangle)              NOT CONVEX (L-shape)

  +------------------+             +--------+
  |                  |             |        |
  |  x o----------o y |           |  x o   |
  |    (line stays   |             |     .  |
  |     INSIDE!)     |             +--+  .  |
  |                  |                |  .  |
  +------------------+                |  .  |   . = line between x and y
                                      | .   |       goes OUTSIDE the shape!
                                      |o y  |
                                      +-----+

  Any 2 points:                    Some 2 points:
  line INSIDE = CONVEX             line EXITS = NOT CONVEX
```

### Examples of Convex Sets

| Set | Convex? | Why |
|-----|---------|-----|
| A line segment | Yes | Line between any 2 points on a segment = still on the segment |
| A ball/circle (filled) | Yes | Straight line between interior points stays inside |
| The set {x : Ax ≤ b} (polyhedron) | Yes | Intersection of half-spaces |
| Star shape | No | Some connecting lines exit the shape |
| R^n (all of space) | Yes | Trivially — everything is inside |
| Empty set | Yes | Vacuously true (no points to check) |
| Hyperplane {x : aᵀx = b} | Yes | Any combo of points satisfying aᵀx=b also satisfies it |
| Half-space {x : aᵀx ≤ b} | Yes | Weighted average of points ≤ b is also ≤ b |

### Important Property: Intersection of Convex Sets is Convex

If C₁ and C₂ are convex, then C₁ ∩ C₂ is also convex. This extends to any (even infinite) number of convex sets.

> **Exam Hack:** Polyhedra {x : Ax ≤ b} are convex because they're intersections of half-spaces (each half-space is convex).

[Back to Top](#convex-sets--functions--theory-guide) · [Next: Convex Functions](#12-convex-functions--definition)

---

## 1.2 Convex Functions — Definition

### Baby Story
Think of a bowl. Put a marble on the rim — it rolls to the bottom. That bowl shape IS a convex function. Now think of a mountain peak (upside-down bowl) — that's CONCAVE. A wavy road with hills and valleys? Neither — that's non-convex.

**The "Chord Test":** Pick any two points on the curve. Draw a straight line (chord) between them. If the chord is ALWAYS above (or on) the curve → CONVEX!

### Formal Definition

> A function **f : Rⁿ → R** is **convex** if for all **x, y** and **θ ∈ [0, 1]**:
> 
> **f(θx + (1 − θ)y) ≤ θf(x) + (1 − θ)f(y)**

Left side = function value at the mixed point. Right side = mix of the function values. Convex means the function at the average is ≤ the average of the function.

### Visual Diagram

```
  f(x)
   │     Chord (straight line)
   │    ●───────────────────●  ← θf(x)+(1-θ)f(y) (ABOVE)
   │   / '-.           .-' /
   │  /     '-.     .-'   /
   │ /        '●.-'      /    ← f(θx+(1-θ)y) (BELOW chord)
   │/       (mixed)      /
   ●                    ●
   x                    y
   
   CONVEX: Curve is BELOW the chord
```

### Examples

| Function | Convex? | Reason |
|----------|---------|--------|
| f(x) = x² | Yes | Bowl shape, f''(x) = 2 > 0 |
| f(x) = ‖x‖₂ | Yes | Norm is convex |
| f(x) = eˣ | Yes | f''(x) = eˣ > 0 |
| f(x) = log(Σeˣⁱ) (log-sum-exp) | Yes | Famous convex function |
| f(x) = -x² | No (concave) | Upside-down bowl |
| f(x) = sin(x) | No | Wavy |
| f(x) = xᵀAx + bᵀx + c (A PSD) | Yes | Quadratic with PSD matrix |

### Indicator Function

For a set C ⊆ Rⁿ, the indicator function is:
```
I_C(x) = { 0    if x ∈ C
          { +∞   if x ∉ C
```
**Key result:** I_C is convex if and only if C is convex.

### Domain Matters!

f(x) = x³ is NOT convex on all of R, but IS convex on C = {x ≥ 0}.

f(x,y) = x² + y⁴ - y² is NOT convex on R², but IS convex on {y ≥ 2}.

> **Exam Hack:** Always check the domain! A function can be convex on a restricted domain even if not globally convex.

[Back to Top](#convex-sets--functions--theory-guide) · [Next: First-Order Characterization](#13-first-order-characterization)

---

## 1.3 First-Order Characterization

### Baby Story
Imagine standing on the convex bowl and laying a flat ruler tangent to the surface at your feet. For a convex function, the ruler (tangent plane) is ALWAYS below the actual surface. The bowl always curves UP from the tangent.

### Theorem (First-Order Condition)

> A differentiable function **f** is convex on convex set C if and only if:
> 
> **f(y) ≥ f(x) + ∇f(x)ᵀ(y − x)** for all x, y ∈ C

```
  f(y)
   │
   │         ● actual f(y)    ← always ABOVE tangent
   │        /
   │       /  curve
   │      /
   │     ● f(x)
   │    / tangent line: f(x) + ∇f(x)ᵀ(y-x)
   │   /
   │──/────────────────────
        x              y

  "Tangent line is a GLOBAL underestimator"
```

### Why This Matters

**Corollary 1: Local minimum = Global minimum!**
If ∇f(x*) = 0 for convex f, then for all y:
f(y) ≥ f(x*) + 0ᵀ(y - x*) = f(x*). So x* is GLOBAL minimum!

**Corollary 2: First-order conditions are SUFFICIENT for convex functions.**
Unlike general functions where ∇f = 0 could be a saddle, for convex f, ∇f(x*) = 0 guarantees global min.

### Proof Sketch (Necessity: convex → tangent below)

1. f is convex: f(y + t(x-y)) ≤ tf(x) + (1-t)f(y) for t ∈ [0,1]
2. Rearrange: [f(y + t(x-y)) - f(y)] / t ≤ f(x) - f(y)
3. Take limit t→0: ∇f(y)ᵀ(x-y) ≤ f(x) - f(y)
4. Rearrange: f(x) ≥ f(y) + ∇f(y)ᵀ(x-y) ✓

### Monotonicity of Gradient (Bonus)

f is convex on C ⟺ ⟨∇f(x) − ∇f(y), x − y⟩ ≥ 0 for all x, y ∈ C

> Think: the gradient "points more uphill" as you go further from the minimum. Gradients are "monotone" — they agree with the direction of change.

**Example:** f(x) = ‖x‖² = xᵀx, so ∇f(x) = 2x.
⟨2x − 2y, x − y⟩ = 2‖x − y‖² ≥ 0 ✓ → Convex!

[Back to Top](#convex-sets--functions--theory-guide) · [Next: Second-Order Characterization](#14-second-order-characterization)

---

## 1.4 Second-Order Characterization

### Baby Story
The first-order test asks: "Is the tangent always below?" The second-order test asks: "Does the bowl always curve UP?" If the bowl's curvature (Hessian) is non-negative everywhere, it's convex!

### Theorem (Second-Order Condition)

> If f is twice differentiable, then f is convex if and only if:
> 
> **∇²f(x) ≽ 0** (positive semidefinite) for all x

### What Does PSD Mean?

A symmetric matrix H is PSD (H ≽ 0) if:
- **Definition:** xᵀHx ≥ 0 for all x
- **Eigenvalue test:** All eigenvalues λᵢ ≥ 0
- **2×2 shortcut:** trace(H) ≥ 0 AND det(H) ≥ 0

If **all eigenvalues > 0** (strictly), then H is **Positive Definite (PD)** and f is **strictly convex**.

### Checking PSD — Decision Flowchart

```
  Is H symmetric?
     │
     ├─ No → NOT a valid Hessian (check your derivatives!)
     │
     └─ Yes → Compute eigenvalues
                │
                ├─ All λ > 0 → PD → STRICTLY convex
                │
                ├─ All λ ≥ 0 → PSD → Convex
                │
                ├─ Some λ > 0, some λ < 0 → INDEFINITE → Saddle point
                │
                └─ All λ < 0 → ND → Concave (strictly)
```

### Example: Quadratic Function

f(x) = (1/2)xᵀAx + bᵀx + c where A is symmetric.

- ∇f(x) = Ax + b
- ∇²f(x) = A

So f is convex ⟺ A is PSD. That's it!

### Example: f(x,y) = x² + xy + y²

∇f = [2x + y, x + 2y]ᵀ

∇²f = [2  1]
      [1  2]

Eigenvalues: det(H - λI) = (2-λ)² - 1 = 0 → λ = 1, 3. Both > 0 → PD → Strictly convex! ✓

### Example: Rosenbrock Function f(x,y) = 100(y - x²)² + (1-x)²

This is NOT convex globally (the Hessian is indefinite at many points). It's the classic "banana" function used to test optimizers.

[Back to Top](#convex-sets--functions--theory-guide) · [Next: Operations Preserving Convexity](#15-operations-preserving-convexity)

---

## 1.5 Operations Preserving Convexity

### Baby Story
If you have convex LEGO blocks, certain ways of combining them give you new convex blocks! Addition, scaling, and some compositions preserve convexity.

### Rules

| Operation | Rule | Example |
|-----------|------|---------|
| **Scaling** | f convex, α > 0 → αf convex | 3x² is convex |
| **Addition** | f₁, f₂ convex → f₁ + f₂ convex | x² + eˣ is convex |
| **Affine composition** | f convex → g(y) = f(Ay + b) convex | f(2x + 3) convex if f convex |
| **Pointwise maximum** | f₁, f₂ convex → max(f₁, f₂) convex | max(x, -x) = |x| is convex |
| **Composition (increasing)** | f convex, g increasing convex → g∘f convex | e^(x²) is convex |

> **Exam Hack:** To show a complex function is convex, break it into simple convex pieces and use these rules!

[Back to Top](#convex-sets--functions--theory-guide) · [Next: Strong Convexity](#16-strong-convexity)

---

## 1.6 Strong Convexity

### Baby Story
A regular convex function could be FLAT (like y = 0 — it's convex but boring). A STRONGLY convex function is like a DEEP bowl — it curves up with at least a minimum steepness µ. This guarantees a unique bottom and fast convergence!

### Definition

> f is **µ-strongly convex** (µ > 0) if:
> 
> **f(y) ≥ f(x) + ∇f(x)ᵀ(y − x) + (µ/2)‖y − x‖²**

Equivalently: f(x) - (µ/2)‖x‖² is convex, OR ∇²f(x) ≽ µI for all x.

### Why Strong Convexity Rocks

| Property | Convex | Strongly Convex (µ > 0) |
|----------|--------|------------------------|
| Local min = Global min? | Yes | Yes |
| Unique minimizer? | Not necessarily | **YES, always** |
| Convergence of GD | O(1/k) | **O((1-µ/L)ᵏ)** = FAST |
| Quadratic growth | Not guaranteed | f(x) - f(x*) ≥ (µ/2)‖x-x*‖² |

### Example

f(x) = (1/2)xᵀAx with eigenvalues λ₁ ≤ ... ≤ λₙ:
- L-smooth with L = λₙ (largest eigenvalue)
- µ-strongly convex with µ = λ₁ (smallest eigenvalue)
- Condition number κ = L/µ = λₙ/λ₁

```
  Small κ (well-conditioned):        Large κ (ill-conditioned):
  ┌─────────────────┐               ┌───────────────────────────┐
  │   ○  ○  ○       │               │         ○                 │
  │  ○  ◉  ○        │ ← circular   │    ○    ◉    ○            │ ← elongated
  │   ○  ○  ○       │   contours   │         ○                 │   ellipse
  └─────────────────┘               └───────────────────────────┘
    Easy to optimize!                 GD zigzags — SLOW!
```

[Back to Top](#convex-sets--functions--theory-guide) · [Next: Advanced Convex Sets](#17-advanced-convex-sets)

---

## 1.7 Advanced Convex Sets

### Convex Combinations and Convex Hull

**Convex combination** of x₁,...,xₖ: Σᵢλᵢxᵢ where λᵢ ≥ 0 and Σλᵢ = 1.

**Convex hull** conv(S) = set of all convex combinations from S.

**Carathéodory's theorem:** Any point in conv(S) ⊆ Rⁿ can be written as a convex combination of at most n+1 points from S.

### Extreme Points

A point x ∈ S is an **extreme point** if it CANNOT be written as x = θy + (1-θ)z for distinct y, z ∈ S and θ ∈ (0,1).

Think: corners of a polygon are extreme points!

**Krein-Milman Theorem:** A compact convex set equals the convex hull of its extreme points.

### Cones

A set C is a **cone** if x ∈ C → λx ∈ C for all λ > 0. It's a **convex cone** if also convex.

Examples: {x : Ax ≤ 0}, the Lorentz cone Lⁿ = {(x,t) : ‖x‖ ≤ t}.

### Separation Theorem

If S is closed convex and y ∉ S, there exists a hyperplane separating y from S:
⟨p, y⟩ > α and ⟨p, s⟩ ≤ α for all s ∈ S.

```
        p (normal)
        ↑
  S     │    ● y
  ○○○   │
  ○○○   │  ← separating hyperplane
  ○○○   │
        │
```

> This theorem is the mathematical foundation of SVMs! The hyperplane that separates classes with maximum margin.

---

## Applications in Data Science (from Lecture 2)

| Problem | Objective | Convex? |
|---------|-----------|---------|
| Least Squares | f(w) = ‖Xw - y‖² | Yes (quadratic, X^TX is PSD) |
| Logistic Regression | f(w) = Σ log(1 + e^{-yᵢwᵀxᵢ}) | Yes |
| SVM (Hinge loss) | f(w) = Σ max(0, 1 - yᵢwᵀxᵢ) | Yes |
| Neural Networks | General DNN loss | **NO** (non-convex!) |

---

> **Next:** [→ PRACTICE Problems](./convex_sets_functions_PRACTICE.md) · [→ Topic 02: Optimality Conditions](../02-Optimality-Conditions/optimality_conditions_INDEX.md)
>
> **Back:** [← INDEX](./convex_sets_functions_INDEX.md) · [↑ Master Hub](../ODS_Master_INDEX.md)

[Back to Top](#convex-sets--functions--theory-guide)
