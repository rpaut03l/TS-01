# Constrained Optimization — Theory
### ODS Topic 11 · Lectures 9-10

> **Nav:** [← INDEX](./constrained_intro_INDEX.md) · [→ PRACTICE](./constrained_intro_PRACTICE.md) · [↑ Hub](../ODS_Master_INDEX.md)

---

## 11.1 Problem Setup

```
minimize f(x)
subject to x ∈ S = {x : gᵢ(x) ≤ 0, i=1,...,m}
```

Unlike unconstrained: ∇f(x*) = 0 is NOT necessary at constrained minimum!

## 11.2 Geometric Optimality Condition

**Descent direction:** F(x) = {d : f(x+αd) < f(x) for small α > 0}
**Feasible direction:** G(x) = {d : x+αd ∈ S for small α > 0}

> If x* is local min → **F(x*) ∩ G(x*) = ∅** (no direction is both improving AND feasible)

## 11.3 Characterizing F₀ and G₀

F₀(x) = {d : ∇f(x)ᵀd < 0} ⊆ F(x) (linearized descent)
G₀(x) = {d : ∇gᵢ(x)ᵀd < 0 for all i ∈ I(x)} ⊆ G(x) (linearized feasible)

Where I(x) = {i : gᵢ(x) = 0} is the **active set** (constraints that are tight).

Since F₀ ∩ G₀ = ∅ at optimum → leads to Fritz-John and KKT conditions.

## 11.4 Convex Sets (Advanced)

Convex hull, extreme points, Carathéodory, cones, separation theorem — see Theory section.

Key results:
- Polyhedral sets are convex (feasible regions of LP)
- Extreme points = vertices of polytope
- LP solutions exist at extreme points
- Separation theorem → foundation of SVMs and Farkas' Lemma

---

> [→ PRACTICE](./constrained_intro_PRACTICE.md) · [↑ Hub](../ODS_Master_INDEX.md)

[Back to Top](#constrained-optimization--theory)
