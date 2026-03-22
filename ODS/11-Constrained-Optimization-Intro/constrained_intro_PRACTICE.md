# Constrained Optimization — Practice
### ODS Topic 11

> **Nav:** [← THEORY](./constrained_intro_THEORY.md) · [↑ Hub](../ODS_Master_INDEX.md)

---

## P1: Constrained Min (From Lecture 10)

**Q:** min f(x,y) = x² + y² subject to x + y ≥ 2.

```
Rewrite constraint: g(x,y) = 2 - x - y ≤ 0 (or g = -(x+y-2) ≤ 0)

Unconstrained min is (0,0) but g(0,0) = 2 > 0 → NOT feasible!

By symmetry (since f is symmetric in x,y), solution is on constraint boundary:
x + y = 2, with x = y → x = y = 1.

f(1,1) = 2. ∇f(1,1) = [2, 2] ≠ 0 (gradient is NOT zero at constrained min!)

This is the key difference from unconstrained optimization.
```

---

## P2: Active Set Identification

**Q:** min f(x,y) = (x-1)² + y² subject to x ≥ 0, y ≥ 0, x+y ≤ 2.

```
Constraints: g₁ = -x ≤ 0, g₂ = -y ≤ 0, g₃ = x+y-2 ≤ 0

Unconstrained min: x*=1, y*=0. Check feasibility:
  g₁(1,0) = -1 ≤ 0 ✓, g₂(1,0) = 0 ≤ 0 ✓, g₃(1,0) = -1 ≤ 0 ✓

(1,0) IS feasible AND ∇f(1,0) = [0, 0]. So it's optimal!
Active set: I = {2} (g₂ = 0 is active/tight)
```

---

> [← THEORY](./constrained_intro_THEORY.md) · [↑ Hub](../ODS_Master_INDEX.md)

[Back to Top](#constrained-optimization--practice)
