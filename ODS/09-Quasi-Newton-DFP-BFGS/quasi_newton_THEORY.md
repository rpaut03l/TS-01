# Quasi-Newton Methods (DFP & BFGS) — Theory
### ODS Topic 09 · Lectures 8-9

> **Nav:** [← INDEX](./quasi_newton_INDEX.md) · [→ PRACTICE](./quasi_newton_PRACTICE.md) · [↑ Hub](../ODS_Master_INDEX.md)

---

## 9.1 Core Idea

Replace true Hessian ∇²f with approximation Bₖ (or inverse approximation Hₖ ≈ [∇²f]⁻¹).
Update Bₖ/Hₖ using only GRADIENT information from each step.

## 9.2 The Secant Equation

```
sₖ = x_{k+1} - xₖ          (step taken)
yₖ = ∇f(x_{k+1}) - ∇f(xₖ)  (gradient change)

Secant equation: B_{k+1} sₖ = yₖ
Or equivalently: H_{k+1} yₖ = sₖ

Curvature condition: sₖᵀyₖ > 0 (ensures PD solution exists)
```

## 9.3 DFP (Davidon-Fletcher-Powell)

Approximate Bₖ, update via secant equation on B:
```
Hₖ₊₁ = Hₖ - (Hₖyₖyₖᵀhₖ)/(yₖᵀHₖyₖ) + (sₖsₖᵀ)/(yₖᵀsₖ)
```
(Rank-2 correction to inverse Hessian approximation)

## 9.4 BFGS (Broyden-Fletcher-Goldfarb-Shanno)

Directly approximate H (inverse), secant on H:
```
Hₖ₊₁ = (I - sₖyₖᵀ/(yₖᵀsₖ)) Hₖ (I - yₖsₖᵀ/(yₖᵀsₖ)) + sₖsₖᵀ/(yₖᵀsₖ)
```

**BFGS is the MOST popular quasi-Newton method.**

## 9.5 Comparison

| Feature | DFP | BFGS |
|---------|-----|------|
| Secant eq. on | B (then invert) | H (inverse directly) |
| Self-correcting? | Less | **More robust** |
| Convergence | Superlinear | Superlinear |
| For quadratics | n steps | n steps |
| Practical choice | Rarely used | **Standard choice** |

## 9.6 L-BFGS (Limited Memory)

Store only last m pairs (sᵢ, yᵢ). Compute H∇f implicitly via two-loop recursion.
Memory: O(mn) instead of O(n²). The default in scipy.optimize!

## 9.7 Broyden Family

B_{k+1} = φ B_{k+1}^DFP + (1-φ) B_{k+1}^BFGS, φ ∈ (0,1).

For quadratics with exact line search: ALL members converge in ≤ n steps!

---

> [→ PRACTICE](./quasi_newton_PRACTICE.md) · [↑ Hub](../ODS_Master_INDEX.md)

[Back to Top](#quasi-newton-methods-dfp--bfgs--theory)
