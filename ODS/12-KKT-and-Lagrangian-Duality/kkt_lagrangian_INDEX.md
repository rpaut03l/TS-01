# KKT Conditions & Lagrangian Duality — Topic Hub
### ODS Topic 12 · Lectures 10–11 · Pr K Som

> **Easy Story:** KKT conditions are the RULES for finding the best spot inside a fenced area. Each fence has a "price" called λ (Lagrange multiplier). If you're NOT touching a fence, its price is 0 (why pay for a fence you're not at?). If you ARE touching it, λ tells you how much better you COULD do if the fence moved!

---

## Study Materials

| Doc | Link |
|-----|------|
| THEORY | [→ Theory](./kkt_lagrangian_THEORY.md) |
| PRACTICE | [→ Practice](./kkt_lagrangian_PRACTICE.md) |

---

## Quick Cheatsheet

```
╔══════════════════════════════════════════════════════════════════════╗
║  KKT CONDITIONS (min f s.t. gᵢ≤0, hⱼ=0):                             ║
║                                                                      ║
║  ★ S: Stationarity                                                   ║
║      ∇f(x*) + Σ λᵢ∇gᵢ(x*) + Σ µⱼ∇hⱼ(x*) = 0                          ║
║                                                                      ║
║  ★ L: Lagrange multipliers ≥ 0                                       ║
║      λᵢ ≥ 0 for all i                                                ║
║                                                                      ║
║  ★ A: Active complementarity (slackness)                             ║
║      λᵢ gᵢ(x*) = 0 for all i                                         ║
║      (if gᵢ < 0 inactive → λᵢ = 0)                                   ║
║      (if λᵢ > 0 → gᵢ = 0 active/tight)                               ║
║                                                                      ║
║  ★ P: Primal feasibility                                             ║
║      gᵢ(x*) ≤ 0, hⱼ(x*) = 0                                          ║
║                                                                      ║
║  FRITZ-JOHN: Same but with extra λ₀ ≥ 0 in front of ∇f.              ║
║    Problem: λ₀ could be 0 → uninformative.                           ║
║    Fix: LICQ (active gradients linearly independent) → λ₀ = 1 = KKT  ║
║                                                                      ║
║  FOR CONVEX PROBLEMS: KKT = necessary AND sufficient!                ║
║                                                                      ║
║  FARKAS' LEMMA: Exactly one holds:                                   ║
║    (I)  Ax ≤ 0 and cᵀx > 0     OR                                    ║
║    (II) Aᵀy = c, y ≥ 0                                               ║
╚══════════════════════════════════════════════════════════════════════╝
```

## Mnemonic: KKT-SLAP
- **S**tationarity (gradient balance)
- **L**agrange ≥ 0 (dual feasibility)
- **A**ctive complementarity (λᵢgᵢ = 0)
- **P**rimal feasibility (constraints satisfied)

---

> **Prev:** [← 11. Constrained Intro](../11-Constrained-Optimization-Intro/constrained_intro_INDEX.md) · **Next:** [→ 13. LP & Simplex](../13-Linear-Programming-Simplex/lp_simplex_INDEX.md) · [↑ Master Hub](../ODS_Master_INDEX.md)

[Back to Top](#kkt-conditions--lagrangian-duality--topic-hub)
