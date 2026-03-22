# Optimality Conditions — Topic Hub
### ODS Topic 02 · Lecture 2 · Pr K Som

> **Easy Story:** You're blindfolded on a hill. How do you know you're at the bottom? First check: is the ground FLAT under your feet? (gradient = 0). Second check: does it curve UP in every direction? (Hessian PD). If both — congrats, you found a minimum!

---

## Study Materials

| Doc | Link |
|-----|------|
| THEORY | [→ Theory](./optimality_conditions_THEORY.md) |
| PRACTICE | [→ Practice](./optimality_conditions_PRACTICE.md) |

## Quick Cheatsheet

```
╔══════════════════════════════════════════════════════════════════╗
║  FERMAT'S RULE (Necessary, 1st order):                           ║
║  If x* is local min of differentiable f → ∇f(x*) = 0             ║
║  (Flat ground = necessary for being at bottom)                   ║
║                                                                  ║
║  2nd ORDER SUFFICIENT:                                           ║
║  If ∇f(x*) = 0 AND ∇²f(x*) ≻ 0 (PD) → x* is strict local min     ║
║                                                                  ║
║  1D VERSION:                                                     ║
║  f'(x*) = 0 and f''(x*) > 0 → local min                          ║
║  f'(x*) = 0 and f''(x*) < 0 → local max                          ║
║  f'(x*) = 0 and f''(x*) = 0 → inconclusive!                      ║
║                                                                  ║
║  CONVEX BONUS: ∇f(x*) = 0 → x* is GLOBAL min (no 2nd check!)     ║
╚══════════════════════════════════════════════════════════════════╝
```

## Mnemonic: FLAT-HILL
- **F**ermat says: **F**lat gradient is necessary
- **H**essian PD = curves up like a **H**ill (inverted) = minimum
- **I**ndefinite Hessian = saddle (ride a horse)
- **L**ook at eigenvalues to decide!

---

> **Prev:** [← 01. Convex Sets](../01-Convex-Sets-and-Functions/convex_sets_functions_INDEX.md) · **Next:** [→ 03. Least Squares](../03-Least-Squares-Linear-Regression/least_squares_INDEX.md) · [↑ Master Hub](../ODS_Master_INDEX.md)

[Back to Top](#optimality-conditions--topic-hub)
