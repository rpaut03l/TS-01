# Linear Programming & Simplex — Topic Hub
### ODS Topic 13 · Lecture 10+ · Pr K Som

> **Easy Story:** Everything is straight lines — the score you're optimizing AND the fences (constraints). The allowed region is a POLYGON (polytope). Amazing mathematical fact: the BEST answer is ALWAYS at a CORNER (vertex)! The simplex algorithm walks along corners, checking each neighbor, until it finds the best one.

---

## Study Materials

| Doc | Link |
|-----|------|
| THEORY | [→ Theory](./lp_simplex_THEORY.md) |
| PRACTICE | [→ Practice](./lp_simplex_PRACTICE.md) |

---

## Quick Cheatsheet

```
╔══════════════════════════════════════════════════════════════════════╗
║  STANDARD FORM: min cᵀx  s.t. Ax = b, x ≥ 0                          ║
║                                                                      ║
║  FEASIBLE SET = polyhedron (always convex!)                          ║
║                                                                      ║
║  KEY THEOREM: If LP has optimal solution → exists at extreme point   ║
║                                                                      ║
║  SIMPLEX: Start at vertex → move to better neighbor → repeat         ║
║                                                                      ║
║  ML CONNECTIONS:                                                     ║
║  • Lasso = LP reformulation with auxiliary variables                 ║
║  • Ridge = QCQP (quadratic constraint, quadratic objective)          ║
║  • Transportation = classic LP application                           ║
╚══════════════════════════════════════════════════════════════════════╝
```

## Mnemonic: CORNER
- LP solution lives at a **CORNER** (extreme point) of the polytope!

---

> **Prev:** [← 12. KKT](../12-KKT-and-Lagrangian-Duality/kkt_lagrangian_INDEX.md) · **Next:** [→ 14. Penalty/Barrier](../14-Penalty-Barrier-Interior-Point/penalty_barrier_INDEX.md) · [↑ Master Hub](../ODS_Master_INDEX.md)

[Back to Top](#linear-programming--simplex--topic-hub)
