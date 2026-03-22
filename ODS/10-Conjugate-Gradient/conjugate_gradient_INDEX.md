# Conjugate Gradient Method — Topic Hub
### ODS Topic 10 · Lectures 8–9 · Pr K Som

> **Easy Story:** GD zigzags because each step partially undoes the previous one. CG is SMARTER: each direction is INDEPENDENT (Q-conjugate) of all previous ones. Think of it like solving a Rubik's cube — each move fixes a new face WITHOUT messing up the ones you already solved! For n variables, CG finds the EXACT answer in exactly n steps.

---

## Study Materials

| Doc | Link |
|-----|------|
| THEORY | [→ Theory](./conjugate_gradient_THEORY.md) |
| PRACTICE | [→ Practice](./conjugate_gradient_PRACTICE.md) |

---

## Quick Cheatsheet

```
╔══════════════════════════════════════════════════════════════════════╗
║  Q-CONJUGATE: pᵢᵀQpⱼ = 0 for i≠j (orthogonal in Q-stretched space)   ║
║                                                                      ║
║  CG ALGORITHM (for f = ½xᵀQx - bᵀx):                                 ║
║    g₀ = Qx₀ - b, p₀ = -g₀                                            ║
║    Loop:                                                             ║
║      αₖ = -(gₖᵀpₖ)/(pₖᵀQpₖ)        ← exact line search                 ║
║      x_{k+1} = xₖ + αₖpₖ                                              ║
║      g_{k+1} = Qx_{k+1} - b                                          ║
║      βₖ₊₁ = (gₖ₊₁ᵀgₖ₊₁)/(gₖᵀgₖ)  ← Fletcher-Reeves                     ║
║      pₖ₊₁ = -gₖ₊₁ + βₖ₊₁pₖ         ← new conjugate direction           ║
║                                                                      ║
║  KEY FACT: Solves n-dimensional quadratic in AT MOST n steps!        ║
║  MEMORY: O(n) only — no matrices stored!                             ║
║                                                                      ║
║  NON-LINEAR CG: Replace g with ∇f, use line search for α             ║
║    FR: β = ‖∇f_{k+1}‖²/‖∇f_k‖²                                       ║
║    PR: β = ∇f_{k+1}ᵀ(∇f_{k+1}-∇f_k)/‖∇f_k‖²                          ║
╚══════════════════════════════════════════════════════════════════════╝
```

## Mnemonic: NO-ZIGZAG
- Each direction is **independent** of previous ones (conjugate)
- **N**o **O**verlap: never undo previous progress
- n dimensions → exactly n steps (for quadratics)

---

> **Prev:** [← 09. Quasi-Newton](../09-Quasi-Newton-DFP-BFGS/quasi_newton_INDEX.md) · **Next:** [→ 11. Constrained Intro](../11-Constrained-Optimization-Intro/constrained_intro_INDEX.md) · [↑ Master Hub](../ODS_Master_INDEX.md)

[Back to Top](#conjugate-gradient-method--topic-hub)
