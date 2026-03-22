# Least Squares — Practice Problems
### ODS Topic 03

> **Nav:** [← THEORY](./least_squares_THEORY.md) · [↑ Hub](../ODS_Master_INDEX.md)

---

## P1: Normal Equations (From Lecture 3)

**Q:** X = {-1, 0, 1, 4}, y = {2, 5, 8, 17}. True: y = 3x + 5. Find w by normal equations.

```
Design matrix (with bias): X = [[-1,1],[0,1],[1,1],[4,1]]
y = [2, 5, 8, 17]ᵀ

XᵀX = [[1+0+1+16, -1+0+1+4], [-1+0+1+4, 1+1+1+1]]
     = [[18, 4], [4, 4]]

Xᵀy = [-2+0+8+68, 2+5+8+17] = [74, 32]

Solve [[18,4],[4,4]] w = [74, 32]:
  From row 2: 4w₁ + 4w₂ = 32 → w₁ + w₂ = 8
  From row 1: 18w₁ + 4w₂ = 74
  Substitute: 18w₁ + 4(8-w₁) = 74 → 14w₁ = 42 → w₁ = 3
  w₂ = 8 - 3 = 5

w* = [3, 5]ᵀ → ŷ = 3x + 5 ✓ (matches true relationship!)
```

---

## P2: Gradient Computation

**Q:** For f(w) = (1/2)‖Xw - y‖², compute ∇f at w = [0, 0]ᵀ.

```
∇f(w) = Xᵀ(Xw - y) = Xᵀ(0 - y) = -Xᵀy = -[74, 32]ᵀ = [-74, -32]ᵀ

This means: at w=0, the steepest descent direction points toward [74, 32].
```

---

## P3: Hessian and Condition Number

**Q:** For the above problem, find the Hessian and condition number.

```
H = XᵀX = [[18, 4], [4, 4]]

Eigenvalues: det(H - λI) = (18-λ)(4-λ) - 16 = λ² - 22λ + 56 = 0
  λ = (22 ± √(484-224))/2 = (22 ± √260)/2 ≈ (22 ± 16.12)/2
  λ₁ ≈ 2.94, λ₂ ≈ 19.06

Condition number κ = 19.06/2.94 ≈ 6.48
→ Moderately conditioned (not too bad)
```

---

> [← THEORY](./least_squares_THEORY.md) · [↑ Hub](../ODS_Master_INDEX.md)

[Back to Top](#least-squares--practice-problems)
