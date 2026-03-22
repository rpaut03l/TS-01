# Penalty, Barrier & Interior Point — Topic Hub
### ODS Topic 14 · Pr K Som

> **Easy Story:** Instead of dealing with fences directly, TRICK the algorithm: Penalty method adds a "fine" for going past the fence — bigger fine → stays inside better. Barrier method puts an invisible LOG wall near the fence — the closer you get, the harder it pushes back. Interior point starts INSIDE and carefully approaches the boundary along the "central path."

---

## Study Materials

| Doc | Link |
|-----|------|
| THEORY | [→ Theory](./penalty_barrier_THEORY.md) |
| PRACTICE | [→ Practice](./penalty_barrier_PRACTICE.md) |

---

## Quick Cheatsheet

```
╔══════════════════════════════════════════════════════════════════════╗
║  PENALTY: min f(x) + (ρ/2)Σ max(0, gᵢ(x))²                           ║
║    → ρ → ∞: forces feasibility. Solve sequence of unconstrained.     ║
║                                                                      ║
║  LOG BARRIER: min f(x) - (1/t)Σ log(-gᵢ(x))                          ║
║    → t → ∞: barrier shrinks. Start inside, approach boundary.        ║
║    → log(-gᵢ) → -∞ as gᵢ → 0⁻ (invisible wall!)                      ║
║                                                                      ║
║  INTERIOR POINT: Follow central path as t increases.                 ║
║    → Use Newton at each t value (few iterations per t).              ║
║    → Polynomial worst-case complexity (unlike simplex!)              ║
║                                                                      ║
║  FRANK-WOLFE (Conditional Gradient): Mentioned in syllabus.          ║
║    → Linearize f, minimize linear approx over feasible set.          ║
║    → Good for structured constraint sets (simplex, nuclear norm).    ║
╚══════════════════════════════════════════════════════════════════════╝
```

## Mnemonic: WALL-LOG
- **BARRIER** = invisible **LOG** wall near boundary
- **PENALTY** = a **WALL** of fines that hurts when crossed
- Interior Point = walk INSIDE, gradually approach the edge

---

> **Prev:** [← 13. LP & Simplex](../13-Linear-Programming-Simplex/lp_simplex_INDEX.md) · [↑ Master Hub](../ODS_Master_INDEX.md)

[Back to Top](#penalty-barrier--interior-point--topic-hub)
