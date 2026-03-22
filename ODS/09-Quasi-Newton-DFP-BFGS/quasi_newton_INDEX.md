# Quasi-Newton Methods (DFP & BFGS) — Topic Hub
### ODS Topic 09 · Lectures 8–9 · Pr K Som

> **Easy Story:** Newton needs the FULL Hessian (n×n matrix) — expensive! Quasi-Newton says: I'll BUILD a FAKE Hessian by remembering what the gradients did at each step. Each update is cheap (rank-2 correction), and over time the fake Hessian becomes a good approximation!

---

## Study Materials

| Doc | Link |
|-----|------|
| THEORY | [→ Theory](./quasi_newton_THEORY.md) |
| PRACTICE | [→ Practice](./quasi_newton_PRACTICE.md) |

---

## Quick Cheatsheet

```
╔══════════════════════════════════════════════════════════════════════╗
║  KEY VARIABLES:                                                      ║
║    sₖ = x_{k+1} - xₖ          (step taken)                            ║
║    yₖ = ∇f(x_{k+1}) - ∇f(xₖ)  (gradient change)                       ║
║                                                                      ║
║  SECANT EQUATION: B_{k+1}sₖ = yₖ  (or H_{k+1}yₖ = sₖ)                  ║
║  CURVATURE CONDITION: sₖᵀyₖ > 0  (ensures PD update)                  ║
║                                                                      ║
║  DFP UPDATE (on H = B⁻¹):                                            ║
║  Hₖ₊₁ = Hₖ - (HₖyₖyₖᵀHₖ)/(yₖᵀHₖyₖ) + (sₖsₖᵀ)/(yₖᵀsₖ)                      ║
║                                                                      ║
║  BFGS UPDATE (on H):                                                 ║
║  Hₖ₊₁ = (I - ρsₖyₖᵀ)Hₖ(I - ρyₖsₖᵀ) + ρsₖsₖᵀ                             ║
║  where ρ = 1/(yₖᵀsₖ)                                                  ║
║                                                                      ║
║  L-BFGS: Store only last m pairs (sᵢ,yᵢ). Memory: O(mn) not O(n²)    ║
║                                                                      ║
║  CONVERGENCE: Superlinear (between linear & quadratic)               ║
║  For quadratics: converges in ≤ n steps (like CG!)                   ║
╚══════════════════════════════════════════════════════════════════════╝
```

## Mnemonic: FAKE-HESSIAN
- **F**ake hessian **A**pproximation via
- **K**eeping **E**ach step's (sₖ, yₖ) pair
- DFP = "**D**avidon **F**letcher **P**owell" (1959, first quasi-Newton)
- BFGS = "**B**royden **F**letcher **G**oldfarb **S**hanno" (most popular)

---

> **Prev:** [← 08. Newton](../08-Newton-Method/newton_method_INDEX.md) · **Next:** [→ 10. Conjugate Gradient](../10-Conjugate-Gradient/conjugate_gradient_INDEX.md) · [↑ Master Hub](../ODS_Master_INDEX.md)

[Back to Top](#quasi-newton-methods-dfp--bfgs--topic-hub)
