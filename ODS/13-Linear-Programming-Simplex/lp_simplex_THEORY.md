# Linear Programming & Simplex — Theory
### ODS Topic 13 · Lecture 10+

> **Nav:** [← INDEX](./lp_simplex_INDEX.md) · [→ PRACTICE](./lp_simplex_PRACTICE.md) · [↑ Hub](../ODS_Master_INDEX.md)

---

## 13.1 LP Standard Form

```
minimize cᵀx
subject to Ax = b, x ≥ 0
```

Feasible set = polyhedron = {x : Ax = b, x ≥ 0} → always CONVEX.

## 13.2 Key Theorem: Solutions at Extreme Points

> If an LP has an optimal solution, it has one at an **extreme point** (vertex/corner) of the feasible polytope.

This is the foundation of the simplex algorithm!

## 13.3 Simplex Algorithm (Idea)

1. Start at a vertex (extreme point)
2. Move to an adjacent vertex that improves objective
3. Repeat until no improving neighbor exists → OPTIMAL!

## 13.4 Applications in ML

- Lasso reformulation (with auxiliary variables → LP constraints)
- Transportation problems
- Resource allocation

---

> [→ PRACTICE](./lp_simplex_PRACTICE.md) · [↑ Hub](../ODS_Master_INDEX.md)

[Back to Top](#linear-programming--simplex--theory)
