# Gradient Descent — Theory
### ODS Topic 05 · Lectures 3-6

> **Nav:** [← INDEX](./gradient_descent_INDEX.md) · [→ PRACTICE](./gradient_descent_PRACTICE.md) · [↑ Hub](../ODS_Master_INDEX.md)

---

## 5.1 The Algorithm

```
GRADIENT DESCENT (Pseudocode):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Input: f, x₀, tol, step_size_method
k = 0
while ‖∇f(xₖ)‖ > tol:
    dₖ = -∇f(xₖ)                    # direction: negative gradient
    αₖ = choose_step(...)            # constant / exact / backtracking
    x_{k+1} = xₖ + αₖ dₖ           # update
    k = k + 1
return xₖ
```

## 5.2 Why Negative Gradient?

> **Theorem:** Among ALL unit vectors d (‖d‖=1), the direction d = -∇f(x)/‖∇f(x)‖ has the SMALLEST directional derivative ∇f(x)ᵀd.

Translation: the negative gradient is the direction of STEEPEST DESCENT.

## 5.3 Worked Example (From Lecture 3)

f(x₁, x₂) = x₁ - x₂ + 2x₁x₂ + 2x₁² + x₂²

```
∇f = [1 + 2x₂ + 4x₁, -1 + 2x₁ + 2x₂]ᵀ
H = [[4, 2], [2, 2]]
x* = [-1, 1.5]ᵀ

Starting at x₀ = [0, 0]ᵀ with α = 1:
  d₀ = -∇f(0,0) = -[1, -1] = [-1, 1]
  x₁ = [0,0] + 1·[-1,1] = [-1, 1]
  
  d₁ = -∇f(-1,1) = -[-1, -1] = [1, 1]
  x₂ = [-1,1] + 1·[1,1] = [0, 2]
  
  Continue iterating...
```

## 5.4 Convergence Summary

| Setting | Step Size | Rate | Meaning |
|---------|-----------|------|---------|
| L-smooth | α ∈ (0, 2/L) | O(1/√k) gradient norm | Slow; finds approx stationary point |
| L-smooth + convex | α = 1/L | O(1/k) function gap | Sublinear |
| L-smooth + µ-strongly convex | α = 1/L or 2/(µ+L) | O((1-µ/L)ᵏ) | LINEAR (exponential decay!) |

```
  Error
  │████
  │██   
  │█    ← Strongly convex: error drops EXPONENTIALLY
  │█
  │▪
  │▪▪▪▪▪▪▪▪▪▪  ← Convex: error drops as 1/k (slow tail)
  │
  └───────────────── Iterations k
```

## 5.5 The Sufficient Decrease Lemma

For f with L-Lipschitz gradient, step size α = 1/L:
```
f(xₖ) - f(x_{k+1}) ≥ (1/2L) ‖∇f(xₖ)‖²
```
Each iteration GUARANTEES decrease proportional to squared gradient norm!

---

> [→ PRACTICE](./gradient_descent_PRACTICE.md) · [↑ Hub](../ODS_Master_INDEX.md)

[Back to Top](#gradient-descent--theory)
