# Constrained Optimization — Topic Hub
### ODS Topic 11 · Lectures 9–10 · Pr K Som

> **Easy Story:** Until now we could walk ANYWHERE on the mountain to find the valley. Now there are FENCES (constraints). You must find the lowest point INSIDE the fenced area. At the optimum, you can't improve because every direction that goes downhill leads OUTSIDE the fence! F(x*) ∩ G(x*) = ∅.

---

## Study Materials

| Doc | Link |
|-----|------|
| THEORY | [→ Theory](./constrained_intro_THEORY.md) |
| PRACTICE | [→ Practice](./constrained_intro_PRACTICE.md) |

---

## Quick Cheatsheet

```
╔══════════════════════════════════════════════════════════════════════╗
║  PROBLEM: min f(x) subject to gᵢ(x) ≤ 0                              ║
║                                                                      ║
║  KEY DIFFERENCE FROM UNCONSTRAINED:                                  ║
║  ∇f(x*) = 0 is NOT necessary! (min could be on boundary)             ║
║                                                                      ║
║  GEOMETRIC OPTIMALITY:                                               ║
║  F(x*) ∩ G(x*) = ∅                                                   ║
║  (No direction is BOTH descent AND feasible at optimum)              ║
║                                                                      ║
║  WHERE:                                                              ║
║  F(x) = descent directions = {d : ∇f(x)ᵀd < 0}                       ║
║  G(x) = feasible directions = {d : ∇gᵢ(x)ᵀd < 0, i ∈ I(x)}           ║
║  I(x) = active set = {i : gᵢ(x) = 0}                                 ║
║                                                                      ║
║  CONVEX SETS ADVANCED: convex hull, extreme points, cones,           ║
║  Carathéodory, Krein-Milman, Separation Theorem, Farkas' Lemma       ║
╚══════════════════════════════════════════════════════════════════════╝
```

## Mnemonic: FENCE
- **F**easible ∩ **E**mpty descent at optimum
- At the **FENCE**, gradient points outside — you're stuck (optimally!)

---

> **Prev:** [← 10. Conjugate Gradient](../10-Conjugate-Gradient/conjugate_gradient_INDEX.md) · **Next:** [→ 12. KKT](../12-KKT-and-Lagrangian-Duality/kkt_lagrangian_INDEX.md) · [↑ Master Hub](../ODS_Master_INDEX.md)

[Back to Top](#constrained-optimization--topic-hub)
