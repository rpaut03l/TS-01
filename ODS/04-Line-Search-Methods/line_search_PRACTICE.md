# Line Search — Practice Problems
### ODS Topic 04

> **Nav:** [← THEORY](./line_search_THEORY.md) · [↑ Hub](../ODS_Master_INDEX.md)

---

## P1: Exact Line Search (From Lecture 3)

**Q:** f(x₁,x₂) = x₁² + x₂². x = (5,4), d = (-1,1). Find optimal α.

```
h(α) = f(x + αd) = (5-α)² + (4+α)²
     = 25 - 10α + α² + 16 + 8α + α²
     = 41 - 2α + 2α²

h'(α) = -2 + 4α = 0 → α = 0.5

x_new = (5,4) + 0.5(-1,1) = (4.5, 4.5)
f_new = 4.5² + 4.5² = 40.5 < 41 = f_old ✓
```

---

## P2: Exact Line Search for Quadratic

**Q:** f(x) = (1/2)xᵀHx + bᵀx, H = [[4,0],[0,2]], b = [-4,-2]ᵀ. Start at x₀ = [0,0]. Use gradient descent with exact line search.

```
g₀ = Hx₀ + b = [0,0] + [-4,-2] = [-4,-2]
d₀ = -g₀ = [4, 2]

α₀ = -(g₀ᵀd₀)/(d₀ᵀHd₀)
   = -([−4,−2]·[4,2]) / ([4,2]·[[4,0],[0,2]]·[4,2])
   = -(−16−4) / ([4,2]·[16,4])
   = 20 / (64+8) = 20/72 = 5/18

x₁ = x₀ + α₀d₀ = [0,0] + (5/18)[4,2] = [20/18, 10/18] = [10/9, 5/9]
```

---

## P3: Backtracking

**Q:** f(x) = x⁴. At x=2, d=-1. Use backtracking with α₀=1, ρ=0.5, c₁=0.1.

```
f(2) = 16, ∇f(2) = 4(8) = 32, ∇f(2)·d = -32

Check α=1: f(2-1) = f(1) = 1. Need: 1 ≤ 16 + 0.1(1)(-32) = 16-3.2 = 12.8? YES ✓
So α=1 is accepted on first try!

x_new = 2 - 1 = 1, f = 1 (huge improvement from 16!)
```

---

> [← THEORY](./line_search_THEORY.md) · [↑ Hub](../ODS_Master_INDEX.md)

[Back to Top](#line-search--practice-problems)
