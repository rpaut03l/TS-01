# Newton's Method — Topic Hub
### ODS Topic 08 · Lecture 8 · Pr K Som
> **Easy Story:** Gradient descent only knows the SLOPE (first derivative). Newton's method also knows the CURVATURE (second derivative / Hessian). It builds a perfect quadratic model at each step and jumps directly to that model's minimum. For quadratics, it reaches the EXACT answer in just ONE step!

---

## Study Materials

| Doc | Link |
|-----|------|
| THEORY | [→ Theory](./newton_method_THEORY.md) |
| PRACTICE | [→ Practice](./newton_method_PRACTICE.md) |

---

## Quick Cheatsheet

```
╔══════════════════════════════════════════════════════════════════════╗
║  NEWTON DIRECTION: pₖ = -[∇²f(xₖ)]⁻¹ ∇f(xₖ)                           ║
║  UPDATE: x_{k+1} = xₖ + pₖ   (pure Newton, step = 1)                  ║
║  DAMPED: x_{k+1} = xₖ + αₖpₖ (add line search for safety)             ║
║                                                                      ║
║  FOR QUADRATICS: f = ½xᵀAx + bᵀx + c                                 ║
║    → Converges in EXACTLY 1 step! (x₁ = -A⁻¹b = x*)                  ║
║                                                                      ║
║  GENERAL: Quadratic convergence near x*                              ║
║    ‖x_{k+1} - x*‖ ≤ C‖xₖ - x*‖²  (doubles correct digits!)           ║
║                                                                      ║
║  COST: O(n³) per step (Hessian inversion)                            ║
║  MEMORY: O(n²) (store full Hessian)                                  ║
║                                                                      ║
║  PROBLEMS: Non-PD Hessian → not descent! O(n³) too expensive!        ║
║  → This motivates Quasi-Newton methods                               ║
╚══════════════════════════════════════════════════════════════════════╝
```

## Mnemonic: QUADRATIC-KING
- Newton is **KING** of convergence speed (quadratic rate)
- But the **crown is heavy** (O(n³) cost, O(n²) memory)
- Solves **QUAD**ratics in 1 step

---

> **Prev:** [← 07. SGD](../07-SGD-and-Variants/sgd_variants_INDEX.md) · **Next:** [→ 09. Quasi-Newton](../09-Quasi-Newton-DFP-BFGS/quasi_newton_INDEX.md) · [↑ Master Hub](../ODS_Master_INDEX.md)

[Back to Top](#newtons-method--topic-hub)
