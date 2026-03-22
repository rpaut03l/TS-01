# Conjugate Gradient — Theory
### ODS Topic 10 · Lectures 8-9

> **Nav:** [← INDEX](./conjugate_gradient_INDEX.md) · [→ PRACTICE](./conjugate_gradient_PRACTICE.md) · [↑ Hub](../ODS_Master_INDEX.md)

---

## 10.1 Q-Conjugacy

Vectors {p₀, p₁, ..., pₙ₋₁} are Q-conjugate if: pᵢᵀQpⱼ = 0 for i ≠ j.

Like orthogonality, but in the "Q-stretched" space.

## 10.2 Conjugate Direction Method (for quadratics)

f(x) = (1/2)xᵀQx - bᵀx (Q PD). Equivalent to solving Qx = b.

```
Algorithm:
  g₀ = Qx₀ + b (gradient at x₀, note: ∇f = Qx - b so g₀ = Qx₀ - b... 
                  careful: if f = ½xᵀQx - bᵀx then ∇f = Qx - b)
  For k = 0, 1, ..., n-1:
    αₖ = -(gₖᵀpₖ)/(pₖᵀQpₖ)      # exact line search
    x_{k+1} = xₖ + αₖpₖ
    g_{k+1} = Qx_{k+1} - b

Finds exact solution in AT MOST n steps!
```

## 10.3 CG Algorithm (Generating Conjugate Directions from Gradients)

```
g₀ = Qx₀ - b, p₀ = -g₀
For k = 0, 1, ...:
    αₖ = -(gₖᵀpₖ)/(pₖᵀQpₖ)
    x_{k+1} = xₖ + αₖpₖ
    g_{k+1} = Qx_{k+1} - b
    βₖ₊₁ = (gₖ₊₁ᵀgₖ₊₁)/(gₖᵀgₖ)          # Fletcher-Reeves
    pₖ₊₁ = -gₖ₊₁ + βₖ₊₁pₖ               # new conjugate direction
```

The magic: βₖ₊₁ is chosen so that pₖ₊₁ is automatically Q-conjugate to all previous directions!

## 10.4 Non-Linear CG

For general f (not quadratic):
- Replace g with ∇f, use line search for α
- Fletcher-Reeves: βₖ₊₁ = ‖∇f(xₖ₊₁)‖²/‖∇f(xₖ)‖²
- Polak-Ribière: βₖ₊₁ = ∇f(xₖ₊₁)ᵀ(∇f(xₖ₊₁)-∇f(xₖ))/‖∇f(xₖ)‖²

Needs Strong Wolfe conditions on line search for convergence!

---

> [→ PRACTICE](./conjugate_gradient_PRACTICE.md) · [↑ Hub](../ODS_Master_INDEX.md)

[Back to Top](#conjugate-gradient--theory)
