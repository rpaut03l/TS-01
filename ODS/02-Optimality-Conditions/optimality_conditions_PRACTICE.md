# Optimality Conditions — Practice Problems
### ODS Topic 02

> **Nav:** [← INDEX](./optimality_conditions_INDEX.md) · [← THEORY](./optimality_conditions_THEORY.md) · [↑ Hub](../ODS_Master_INDEX.md)

---

## P1: Classify Critical Points (1D)

**Q:** Find and classify critical points of f(x) = x³ - 3x.

```
f'(x) = 3x² - 3 = 0 → x² = 1 → x = ±1

f''(x) = 6x
  At x = 1:  f''(1) = 6 > 0 → LOCAL MIN, f(1) = -2
  At x = -1: f''(-1) = -6 < 0 → LOCAL MAX, f(-1) = 2
```

---

## P2: Multivariable Stationary Point (From Lecture 2)

**Q:** Find and classify stationary points of f(x,y) = x² + xy + y².

```
∇f = [2x + y, x + 2y]ᵀ = [0, 0]ᵀ

Solve: 2x + y = 0 and x + 2y = 0
       → x = 0, y = 0. Critical point: (0, 0).

H = [[2, 1], [1, 2]]
Eigenvalues: λ = 1, 3 (both > 0) → PD → (0,0) is STRICT LOCAL MIN ✓

Since f is convex (H PD everywhere), it's also GLOBAL MIN.
f(0,0) = 0.
```

---

## P3: Saddle Point Detection

**Q:** f(x,y) = x² - y². Find and classify critical points.

```
∇f = [2x, -2y]ᵀ = 0 → (0,0)

H = [[2, 0], [0, -2]]
Eigenvalues: 2 and -2 → INDEFINITE → SADDLE POINT at (0,0)

This is the classic "horse saddle" — goes UP in x, DOWN in y.
```

---

## P4: When Convexity Helps

**Q:** f(w) = ‖Xw - y‖². Show the minimizer and verify.

```
∇f(w) = 2Xᵀ(Xw - y) = 0
→ XᵀXw = Xᵀy
→ w* = (XᵀX)⁻¹Xᵀy  (if XᵀX invertible)

∇²f(w) = 2XᵀX which is PSD.
→ f is convex, so w* is GLOBAL minimum. No further checks needed!
```

---

## Quick Exam Answers

| Q | A |
|---|---|
| f'(x*)=0 guarantees min? | NO — only necessary, not sufficient |
| f convex + ∇f=0 guarantees min? | YES — global min |
| H indefinite at critical point means? | Saddle point |
| How to check PD for 2×2? | trace > 0 AND det > 0 |

---

> **Next:** [→ Topic 03: Least Squares](../03-Least-Squares-Linear-Regression/least_squares_INDEX.md)
> **Back:** [← THEORY](./optimality_conditions_THEORY.md) · [↑ Hub](../ODS_Master_INDEX.md)

[Back to Top](#optimality-conditions--practice-problems)
