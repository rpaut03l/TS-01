# Least Squares & Linear Regression — Theory
### ODS Topic 03 · Lecture 3

> **Nav:** [← INDEX](./least_squares_INDEX.md) · [→ PRACTICE](./least_squares_PRACTICE.md) · [↑ Hub](../ODS_Master_INDEX.md)

---

## 3.1 The Setup

Given data {(xᵢ, yᵢ)}ⁿᵢ₌₁ where xᵢ ∈ Rᵈ, yᵢ ∈ R. Assume linear model: ŷᵢ = xᵢᵀw.

**Goal:** Choose w that minimizes prediction error.

**Residual:** rᵢ(w) = yᵢ - xᵢᵀw (how far off each prediction is)

**Loss (Empirical Risk):**
```
f(w) = (1/2) Σᵢ rᵢ(w)² = (1/2) Σᵢ (yᵢ - xᵢᵀw)²
```

## 3.2 Matrix Formulation

```
X = [x₁ᵀ; x₂ᵀ; ...; xₙᵀ] ∈ Rⁿˣᵈ    (data matrix, each ROW = one sample)
y = [y₁; y₂; ...; yₙ] ∈ Rⁿ            (target vector)

f(w) = (1/2) ‖Xw - y‖² = (1/2)(Xw - y)ᵀ(Xw - y)
```

This is a QUADRATIC function in w → guaranteed CONVEX!

## 3.3 Solving: Normal Equations

```
∇f(w) = Xᵀ(Xw - y) = 0

→ XᵀXw = Xᵀy

→ w* = (XᵀX)⁻¹Xᵀy    ← THE NORMAL EQUATION (memorize this!)
```

**Hessian:** ∇²f(w) = XᵀX (PSD) → f is convex → w* is global minimum.

If X has full column rank (rank d) → XᵀX is PD → unique solution.

```
  DIAGRAM: Normal Equations Pipeline
  
  Data (X, y) → Compute XᵀX and Xᵀy → Solve XᵀXw = Xᵀy → w*
                    ↑                        ↑
                 O(nd²) cost            O(d³) to invert
```

## 3.4 Geometric Interpretation

The prediction ŷ = Xw lives in the column space of X. The residual (y - Xw*) is PERPENDICULAR to this column space. That's why Xᵀ(y - Xw*) = 0 — the residual is orthogonal to all columns of X!

```
       y ●
        /|
       / |  residual (y - Xw*)
      /  |  ← perpendicular!
     /   |
    /    ● Xw* (projection of y onto column space of X)
   /────────────────
   Column space of X
```

## 3.5 Connection to Optimization

Linear regression IS an unconstrained convex optimization problem:
```
min_{w ∈ Rᵈ} f(w) = (1/2)‖Xw - y‖²
```

Properties:
- f is convex (Hessian XᵀX is PSD)
- If X full rank → f is strongly convex with µ = λ_min(XᵀX)
- Lipschitz constant L = λ_max(XᵀX) (= largest eigenvalue)
- Condition number κ = λ_max/λ_min

---

> **Next:** [→ PRACTICE](./least_squares_PRACTICE.md) · [→ Topic 04: Line Search](../04-Line-Search-Methods/line_search_INDEX.md)
> **Back:** [← INDEX](./least_squares_INDEX.md) · [↑ Hub](../ODS_Master_INDEX.md)

[Back to Top](#least-squares--linear-regression--theory)
