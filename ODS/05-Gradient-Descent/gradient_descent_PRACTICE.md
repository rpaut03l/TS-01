# Gradient Descent — Practice
### ODS Topic 05

> **Nav:** [← THEORY](./gradient_descent_THEORY.md) · [↑ Hub](../ODS_Master_INDEX.md)

---

## P1: GD Steps (From Lecture 3)

**Q:** f(x₁,x₂) = x₁ - x₂ + 2x₁x₂ + 2x₁² + x₂². Do 2 GD steps from x₀=(0,0), α=1.

```
∇f = [1 + 2x₂ + 4x₁, -1 + 2x₁ + 2x₂]

Step 0: ∇f(0,0) = [1, -1], d₀ = [-1, 1]
  x₁ = (0,0) + 1·(-1,1) = (-1, 1)
  f(x₁) = -1 - 1 + 2(-1)(1) + 2(1) + 1 = -1

Step 1: ∇f(-1,1) = [1+2-4, -1-2+2] = [-1, -1], d₁ = [1, 1]
  x₂ = (-1,1) + 1·(1,1) = (0, 2)
  f(x₂) = 0 - 2 + 0 + 0 + 4 = 2 ← INCREASED! α=1 too large!
```

> **Lesson:** Constant α=1 can cause DIVERGENCE. Need smaller α or line search!

---

## P2: Safe Step Size

**Q:** For f(x) = (1/2)xᵀAx, A = [[4,2],[2,2]], what is the safe constant step size?

```
L = λ_max(A). Eigenvalues: det(A-λI) = (4-λ)(2-λ) - 4 = λ² - 6λ + 4 = 0
λ = (6 ± √20)/2 = 3 ± √5 ≈ 0.76, 5.24

L = 5.24, so safe α < 2/L ≈ 0.38.
Optimal: α = 2/(µ+L) = 2/(0.76+5.24) = 2/6 = 1/3.
```

---

> [← THEORY](./gradient_descent_THEORY.md) · [↑ Hub](../ODS_Master_INDEX.md)

[Back to Top](#gradient-descent--practice)
