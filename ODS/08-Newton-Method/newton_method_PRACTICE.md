# Newton's Method — Practice
### ODS Topic 08

> **Nav:** [← THEORY](./newton_method_THEORY.md) · [↑ Hub](../ODS_Master_INDEX.md)

---

## P1: Newton for Quadratic

**Q:** f(x) = (1/2)xᵀ[[4,2],[2,2]]x + [-8,-4]ᵀx. Find x* in one Newton step from x₀=(0,0).

```
A = [[4,2],[2,2]], b = [-8,-4]ᵀ
∇f(x₀) = Ax₀ + b = [-8,-4]
A⁻¹ = (1/4)[[2,-2],[-2,4]] = [[0.5,-0.5],[-0.5,1]]

p₀ = -A⁻¹·[-8,-4] = -[[0.5,-0.5],[-0.5,1]]·[-8,-4]
   = -[(-4+2),( 4-4)] = -[-2, 0] = [2, 0]

x₁ = x₀ + p₀ = (0,0) + (2,0) = (2, 0)

Verify: ∇f(2,0) = [[4,2],[2,2]]·[2,0] + [-8,-4] = [8,-4]+[-8,-4]? 
Wait: [8,4]+[-8,-4] = [0,0] ✓  (stationary in 1 step!)
```

## P2: Newton-Raphson for Root Finding

**Q:** Find root of g(x) = xeˣ - 1 near x₀ = 0.5.

```
x_{n+1} = xₙ - g(xₙ)/g'(xₙ)
g'(x) = eˣ + xeˣ = eˣ(1+x)

x₀ = 0.5: g(0.5) = 0.5e⁰·⁵ - 1 ≈ 0.824 - 1 = -0.176
           g'(0.5) = e⁰·⁵(1.5) ≈ 2.473
x₁ = 0.5 - (-0.176)/2.473 ≈ 0.5 + 0.071 = 0.571

x₁ = 0.571: g(0.571) ≈ 0.571·1.770 - 1 ≈ 0.011
             g'(0.571) ≈ 1.770·1.571 ≈ 2.780
x₂ = 0.571 - 0.011/2.780 ≈ 0.567

True answer: x ≈ 0.5671 (Lambert W function). Converged in ~2 steps!
```

---

> [← THEORY](./newton_method_THEORY.md) · [↑ Hub](../ODS_Master_INDEX.md)

[Back to Top](#newtons-method--practice)
