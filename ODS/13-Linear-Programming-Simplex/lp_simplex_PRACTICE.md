# LP & Simplex — Practice
### ODS Topic 13

> **Nav:** [← THEORY](./lp_simplex_THEORY.md) · [↑ Hub](../ODS_Master_INDEX.md)

---

## P1: Identify Extreme Points

**Q:** S = {(x,y) : x ≥ 0, y ≥ 0, x + y ≤ 3}. Find extreme points.

```
Extreme points = intersections of constraint boundaries:
  x=0, y=0 → (0, 0)
  x=0, x+y=3 → (0, 3)
  y=0, x+y=3 → (3, 0)

Three extreme points: (0,0), (0,3), (3,0).
```

## P2: LP at Corners

**Q:** max 2x + 3y over S from P1.

```
Evaluate at extreme points:
  f(0,0) = 0
  f(0,3) = 9  ← MAXIMUM
  f(3,0) = 6

Optimal: (0, 3) with value 9.
```

---

> [← THEORY](./lp_simplex_THEORY.md) · [↑ Hub](../ODS_Master_INDEX.md)

[Back to Top](#lp--simplex--practice)
