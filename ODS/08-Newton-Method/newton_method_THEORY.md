# Newton's Method — Theory
### ODS Topic 08 · Lecture 8

> **Nav:** [← INDEX](./newton_method_INDEX.md) · [→ PRACTICE](./newton_method_PRACTICE.md) · [↑ Hub](../ODS_Master_INDEX.md)

---

## 8.1 The Idea

Approximate f by a QUADRATIC model at xₖ:
```
mₖ(p) = f(xₖ) + ∇f(xₖ)ᵀp + (1/2)pᵀ∇²f(xₖ)p
```

Minimize this model → Newton direction:
```
pₖᴺ = -[∇²f(xₖ)]⁻¹ ∇f(xₖ)
```

## 8.2 Pure Newton Algorithm

```
while ‖∇f(xₖ)‖ > tol:
    pₖ = -(∇²f(xₖ))⁻¹ ∇f(xₖ)    # Newton direction
    x_{k+1} = xₖ + pₖ              # full step (α=1)
```

## 8.3 Why It's Amazing

**For quadratics:** Converges in EXACTLY 1 step from ANY starting point!
```
f(x) = (1/2)xᵀAx + bᵀx + c, A PD
∇f = Ax + b, ∇²f = A
p₀ = -A⁻¹(Ax₀ + b) = -(x₀ + A⁻¹b)
x₁ = x₀ + p₀ = x₀ - x₀ - A⁻¹b = -A⁻¹b = x* ✓
```

**General case:** Quadratic convergence: ‖x_{k+1} - x*‖ ≤ C‖xₖ - x*‖²

## 8.4 GD as Regularized Linear Model

GD direction comes from minimizing: f(xₖ) + ∇f(xₖ)ᵀp + (1/2η)‖p‖²
This is a LINEAR model + quadratic penalty. Result: p* = -η∇f(xₖ).

Newton uses the ACTUAL curvature (Hessian) instead of the identity penalty.

## 8.5 Damped Newton

Add line search: x_{k+1} = xₖ + αₖ pₖ. Safer than pure Newton.

## 8.6 Problems with Newton

- **Cost:** O(n³) per iteration (Hessian inverse)
- **Non-convex:** If Hessian not PD, direction may not be descent!
- **Memory:** Store n×n matrix

→ This motivates Quasi-Newton methods!

---

> [→ PRACTICE](./newton_method_PRACTICE.md) · [↑ Hub](../ODS_Master_INDEX.md)

[Back to Top](#newtons-method--theory)
