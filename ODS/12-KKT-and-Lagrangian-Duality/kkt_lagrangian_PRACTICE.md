# KKT & Lagrangian — Practice
### ODS Topic 12

> **Nav:** [← THEORY](./kkt_lagrangian_THEORY.md) · [↑ Hub](../ODS_Master_INDEX.md)

---

## P1: Fritz-John Point (From Lecture 10)

**Q:** min f(x₁,x₂) = x₁² + x₂² s.t. g(x) = 1 - x₁ ≤ 0.

```
Solution: x* = (1, 0) (closest point in {x₁ ≥ 1} to origin).

∇f(x*) = [2, 0], ∇g(x*) = [-1, 0], g(x*) = 0 (active).

FJ: λ₀[2,0] + λ₁[-1,0] = [0,0]
    → 2λ₀ - λ₁ = 0 → λ₁ = 2λ₀
    
Choose λ₀ = 1, λ₁ = 2 ≥ 0 ✓
Complementary slackness: λ₁g(x*) = 2·0 = 0 ✓
```

## P2: KKT for Ridge Regression (From Lecture 10)

**Q:** min ‖y - Xβ‖² s.t. ‖β‖² ≤ t. Write KKT conditions.

```
f(β) = ‖y - Xβ‖², g(β) = ‖β‖² - t ≤ 0

KKT:
1. ∇f + λ∇g = 0:  -2Xᵀ(y - Xβ*) + 2λβ* = 0
   → Xᵀ(Xβ* - y) + λβ* = 0
   → (XᵀX + λI)β* = Xᵀy
   → β* = (XᵀX + λI)⁻¹Xᵀy    ← Ridge regression solution!

2. g(β*) ≤ 0: ‖β*‖² ≤ t
3. λ ≥ 0
4. λ(‖β*‖² - t) = 0

If ‖β*‖² < t → λ = 0 → ordinary least squares
If ‖β*‖² = t → λ > 0 → regularization is ACTIVE
```

## P3: Farkas' Lemma Example (From Lecture 11)

**Q:** A = [[1,1],[-1,1]], c = [2,1]ᵀ. Which alternative holds?

```
Try system II: Aᵀy = c, y ≥ 0
  [1,-1][y₁]   [2]     y₁ - y₂ = 2
  [1, 1][y₂] = [1]  →  y₁ + y₂ = 1

  y₁ = 1.5, y₂ = -0.5 → y₂ < 0 → NOT feasible

So system I must hold. Take x = [1,-1]ᵀ:
  Ax = [[1,1],[-1,1]]·[1,-1] = [0,-2] ≤ 0 ✓
  cᵀx = [2,1]·[1,-1] = 1 > 0 ✓
```

---

> [← THEORY](./kkt_lagrangian_THEORY.md) · [↑ Hub](../ODS_Master_INDEX.md)

[Back to Top](#kkt--lagrangian--practice)
