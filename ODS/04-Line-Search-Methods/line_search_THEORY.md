# Line Search Methods — Theory
### ODS Topic 04 · Lectures 3-5

> **Nav:** [← INDEX](./line_search_INDEX.md) · [→ PRACTICE](./line_search_PRACTICE.md) · [↑ Hub](../ODS_Master_INDEX.md)

---

## 4.1 The Big Picture

Every iterative optimizer does: **x_{k+1} = x_k + α_k d_k**

Where:
- d_k = descent direction (WHERE to go)
- α_k = step size (HOW FAR to go)

This section is about choosing α_k!

## 4.2 Descent Direction

> d is a descent direction at x if ⟨∇f(x), d⟩ < 0

Most common choices:
- **Steepest descent:** d = -∇f(x) (always descent if ∇f ≠ 0)
- **Newton:** d = -[∇²f(x)]⁻¹∇f(x)
- **General:** d = -B∇f(x) for any PD matrix B

```
  ∇f(x) points UPHILL    d = -∇f(x) points DOWNHILL
  
       ↗ ∇f(x)           d ↙
      /                     \
     / ∇f·d < 0              \
    ●─────────────────────────●
    x_k                     x_{k+1} = x_k + αd
```

## 4.3 Step Size Choices

### A) Constant Step Size
α_k = α (fixed). Simple but risky:
- Too big → diverge (overshoot)
- Too small → very slow
- Safe range: α ∈ (0, 2/L) where L = Lipschitz constant of gradient

### B) Exact Line Search
α_k = argmin_{α>0} f(x_k + αd_k)

Solve a 1D optimization sub-problem each step.

**For quadratic** f(x) = (1/2)xᵀHx + bᵀx + c:
```
α_k = -(gₖ)ᵀdₖ / (dₖᵀHdₖ)

where gₖ = ∇f(xₖ) = Hxₖ + b
```

### C) Inexact Line Search (Armijo + Wolfe)

**Armijo condition (sufficient decrease):**
```
f(x_k + α d_k) ≤ f(x_k) + c₁ α ⟨∇f(x_k), d_k⟩    (c₁ ∈ (0,1))
```
"The function actually decreases by at least a fraction c₁ of what the linear model predicts."

**Curvature condition (Wolfe):**
```
⟨∇f(x_k + α d_k), d_k⟩ ≥ c₂ ⟨∇f(x_k), d_k⟩    (c₂ ∈ (c₁, 1))
```
"Don't stop too early — the gradient at the new point shouldn't be too steep."

### D) Backtracking Line Search

```
Algorithm:
  Initialize: α > 0, ρ ∈ (0,1), c₁ ∈ (0,1)
  While f(x + αd) > f(x) + c₁ α ∇f(x)ᵀd:
      α = ρα        ← shrink step by factor ρ
  Return α
```

Simple, practical, widely used! Just keep halving α until Armijo is satisfied.

## 4.4 Lipschitz Gradient (L-Smoothness)

> f has **L-Lipschitz gradient** if: ‖∇f(x) - ∇f(y)‖ ≤ L‖x - y‖ for all x, y

### Descent Lemma
If f has L-Lipschitz gradient:
```
f(y) ≤ f(x) + ∇f(x)ᵀ(y-x) + (L/2)‖y-x‖²
```
"The function stays below a quadratic upper bound."

### Why It Matters
With step α = 1/L: guaranteed decrease at each step!
```
f(x_{k+1}) ≤ f(x_k) - (1/2L)‖∇f(x_k)‖²
```

## 4.5 Zigzagging Problem

For exact line search on quadratics, consecutive directions are ORTHOGONAL:
⟨x_{k+2} - x_{k+1}, x_{k+1} - x_k⟩ = 0

This causes zigzag paths, especially when condition number is large!

```
  Well-conditioned (κ≈1):    Ill-conditioned (κ>>1):
  
  x₀ → x₁ → x₂ → x*        x₀
                                ↓↗↓↗↓↗
                                   ↓↗↓↗
                                     x* (many zigzags!)
```

---

> [→ PRACTICE](./line_search_PRACTICE.md) · [↑ Hub](../ODS_Master_INDEX.md)

[Back to Top](#line-search-methods--theory)
