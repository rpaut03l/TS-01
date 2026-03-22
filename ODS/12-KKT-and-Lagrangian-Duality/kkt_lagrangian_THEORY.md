# KKT Conditions & Lagrangian Duality — Theory
### ODS Topic 12 · Lectures 10-11

> **Nav:** [← INDEX](./kkt_lagrangian_INDEX.md) · [→ PRACTICE](./kkt_lagrangian_PRACTICE.md) · [↑ Hub](../ODS_Master_INDEX.md)

---

## 12.1 Fritz-John Conditions

For min f(x) s.t. gᵢ(x) ≤ 0:

If x* is local min → ∃ λ₀, λ₁,...,λₘ ≥ 0 (not all zero) such that:
```
1. λ₀∇f(x*) + Σ λᵢ∇gᵢ(x*) = 0         (stationarity with λ₀)
2. λᵢgᵢ(x*) = 0  for all i            (complementary slackness)
3. λᵢ ≥ 0 for all i = 0,1,...,m       (non-negativity)
```

**Problem:** λ₀ might be 0, making the condition uninformative!

## 12.2 KKT Conditions (The Key Theorem)

Add **LICQ** (Linear Independence Constraint Qualification): gradients of active constraints are linearly independent at x*.

Then λ₀ = 1 (can be normalized), giving:

```
╔══════════════════════════════════════════════════════════════╗
║  KKT CONDITIONS (for min f s.t. gᵢ ≤ 0, hⱼ = 0):             ║
║                                                              ║
║  1. STATIONARITY:                                            ║
║     ∇f(x*) + Σᵢ λᵢ∇gᵢ(x*) + Σⱼ µⱼ∇hⱼ(x*) = 0                 ║
║                                                              ║
║  2. PRIMAL FEASIBILITY:                                      ║
║     gᵢ(x*) ≤ 0, hⱼ(x*) = 0                                   ║
║                                                              ║
║  3. DUAL FEASIBILITY:                                        ║
║     λᵢ ≥ 0                                                   ║
║                                                              ║
║  4. COMPLEMENTARY SLACKNESS:                                 ║
║     λᵢ gᵢ(x*) = 0  for all i                                 ║
║     (If gᵢ < 0 → λᵢ = 0: inactive constraint has zero        ║
║      multiplier. If λᵢ > 0 → gᵢ = 0: positive multiplier     ║
║      only for active/tight constraints.)                     ║
╚══════════════════════════════════════════════════════════════╝
```

## Mnemonic: KKT-SLAP
- **S**tationarity: gradient balance
- **L**agrange ≥ 0: dual feasibility
- **A**ctive complementarity: λᵢgᵢ = 0
- **P**rimal feasibility: constraints satisfied

## 12.3 Farkas' Lemma

> Exactly one of these has a solution:
> (I) Ax ≤ 0 and cᵀx > 0
> (II) Aᵀy = c, y ≥ 0

Foundation for proving Fritz-John/KKT conditions.

## 12.4 Constraint Qualifications

| CQ Name | Condition |
|---------|-----------|
| LICQ | Active constraint gradients linearly independent |
| MFCQ | Weaker than LICQ, allows some linear dependence |
| Slater | ∃ strictly feasible point (for convex problems) |

## 12.5 For Convex Problems

If f and gᵢ are convex, hⱼ are affine:
- KKT is **necessary AND sufficient** for global optimality!
- Under Slater's condition, KKT point = global solution

---

> [→ PRACTICE](./kkt_lagrangian_PRACTICE.md) · [↑ Hub](../ODS_Master_INDEX.md)

[Back to Top](#kkt-conditions--lagrangian-duality--theory)
