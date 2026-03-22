# Penalty, Barrier & Interior Point — Practice
### ODS Topic 14

> **Nav:** [← THEORY](./penalty_barrier_THEORY.md) · [↑ Hub](../ODS_Master_INDEX.md)

---

## P1: Penalty Method

**Q:** min x² s.t. x ≥ 1. Solve using penalty method with ρ = 10.

```
Penalized: minimize x² + (10/2) max(0, 1-x)²

For x ≥ 1: just x² → min at x = 1.
For x < 1: x² + 5(1-x)² = x² + 5 - 10x + 5x² = 6x² - 10x + 5
  Derivative: 12x - 10 = 0 → x = 5/6 < 1

Check: f(5/6) = 25/36 + 5(1/6)² = 25/36 + 5/36 = 30/36 ≈ 0.833
       f(1) = 1

Penalty solution: x = 5/6 (slightly infeasible). As ρ → ∞, x → 1.
```

## P2: Barrier Method

**Q:** min x² s.t. x ≥ 1, using log barrier with t = 10.

```
Barrier: minimize x² - (1/10) log(x - 1)    (for x > 1)

Derivative: 2x - 1/(10(x-1)) = 0
  20x(x-1) = 1
  20x² - 20x - 1 = 0
  x = (20 ± √(400+80))/40 = (20 ± √480)/40 ≈ (20 + 21.9)/40 ≈ 1.048

As t → ∞, x → 1 (the true constrained solution).
```

---

> [← THEORY](./penalty_barrier_THEORY.md) · [↑ Hub](../ODS_Master_INDEX.md)

[Back to Top](#penalty-barrier--interior-point--practice)
