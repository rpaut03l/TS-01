# Penalty, Barrier & Interior Point — Theory
### ODS Topic 14 · Lecture 10+

> **Nav:** [← INDEX](./penalty_barrier_INDEX.md) · [→ PRACTICE](./penalty_barrier_PRACTICE.md) · [↑ Hub](../ODS_Master_INDEX.md)

---

## 14.1 Penalty Method

Convert constrained → unconstrained by adding penalty:
```
minimize f(x) + (ρ/2) Σ max(0, gᵢ(x))²

ρ → ∞: penalty increases, solution approaches feasible region
```

## 14.2 Barrier Method (Log Barrier)

For inequality constraints gᵢ(x) ≤ 0, add barrier:
```
minimize f(x) - (1/t) Σ log(-gᵢ(x))

t → ∞: barrier shrinks, solution approaches boundary
```

The log term → -∞ as gᵢ → 0⁻, creating an invisible wall!

## 14.3 Interior Point Methods

Start inside feasible region, follow the **central path** as t increases:
```
For increasing t values:
  Solve: minimize f(x) - (1/t) Σ log(-gᵢ(x))
  Use Newton's method (one or few steps per t)
```

Key: Interior point methods have **polynomial** worst-case complexity, unlike simplex.

## 14.4 Applications

- SVM training (quadratic objective + linear constraints)
- Large-scale LP/QCQP in ML
- Modern solvers (MOSEK, Gurobi) use interior point methods

---

> [→ PRACTICE](./penalty_barrier_PRACTICE.md) · [↑ Hub](../ODS_Master_INDEX.md)

[Back to Top](#penalty-barrier--interior-point--theory)
