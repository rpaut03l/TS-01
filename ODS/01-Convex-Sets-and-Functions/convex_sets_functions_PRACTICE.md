# Convex Sets & Functions — Practice Problems
### ODS Topic 01 · Solved Numericals

> **Navigation:** [← INDEX](./convex_sets_functions_INDEX.md) · [← THEORY](./convex_sets_functions_THEORY.md) · [↑ Master Hub](../ODS_Master_INDEX.md)

---

## P1: Is This Set Convex?

**Q:** Determine if S = {(x,y) : x² + y² ≤ 1} is convex.

**Approach:** Take any two points in S, show their convex combination is also in S.

**Solution:**
```
Let a, b ∈ S, so ‖a‖² ≤ 1 and ‖b‖² ≤ 1.
For θ ∈ [0,1], consider c = θa + (1-θ)b.

‖c‖ = ‖θa + (1-θ)b‖
     ≤ θ‖a‖ + (1-θ)‖b‖     (triangle inequality)
     ≤ θ·1 + (1-θ)·1        (since ‖a‖ ≤ 1, ‖b‖ ≤ 1)
     = 1

So c ∈ S. ✓ The unit ball IS convex.
```

> **Exam Hack:** Any norm ball {x : ‖x‖ ≤ r} is convex. Just cite triangle inequality!

[Back to Top](#convex-sets--functions--practice-problems)

---

## P2: Intersection of Convex Sets

**Q:** S₁ = {x : x₁ + x₂ ≤ 5} and S₂ = {x : x₁ ≥ 0, x₂ ≥ 0}. Is S₁ ∩ S₂ convex?

**Solution:**
```
S₁ is a half-space → convex.
S₂ = {x₁ ≥ 0} ∩ {x₂ ≥ 0} = intersection of two half-spaces → convex.
S₁ ∩ S₂ = intersection of convex sets → CONVEX. ✓
```

[Back to Top](#convex-sets--functions--practice-problems)

---

## P3: Prove Convexity of a Function

**Q:** Show f(x) = x² is convex on R.

**Method 1 (Definition):**
```
Need: f(θa + (1-θ)b) ≤ θf(a) + (1-θ)f(b)

LHS = (θa + (1-θ)b)² = θ²a² + 2θ(1-θ)ab + (1-θ)²b²

RHS = θa² + (1-θ)b²

RHS - LHS = θa² + (1-θ)b² - θ²a² - 2θ(1-θ)ab - (1-θ)²b²
           = θ(1-θ)a² - 2θ(1-θ)ab + θ(1-θ)b²
           = θ(1-θ)(a-b)² ≥ 0  ✓
```

**Method 2 (Second derivative):**
```
f''(x) = 2 > 0 for all x → f is strictly convex. ✓
```

> **Exam Hack:** Second derivative test is MUCH faster than definition for 1D functions!

[Back to Top](#convex-sets--functions--practice-problems)

---

## P4: Is eˣ Convex?

**Q:** Prove f(x) = eˣ is convex.

**Solution:**
```
f'(x) = eˣ
f''(x) = eˣ > 0 for all x ∈ R

Since f''(x) > 0 everywhere → f is strictly convex. ✓
```

[Back to Top](#convex-sets--functions--practice-problems)

---

## P5: First-Order Condition

**Q:** Using the first-order characterization, verify f(x) = ‖x‖² is convex.

**Solution:**
```
∇f(x) = 2x

First-order condition: f(y) ≥ f(x) + ∇f(x)ᵀ(y - x)

LHS = ‖y‖² = yᵀy
RHS = xᵀx + 2xᵀ(y - x) = xᵀx + 2xᵀy - 2xᵀx = 2xᵀy - xᵀx

LHS - RHS = yᵀy - 2xᵀy + xᵀx = (y - x)ᵀ(y - x) = ‖y - x‖² ≥ 0 ✓
```

**Alternative (Monotonicity):**
```
⟨∇f(x) - ∇f(y), x - y⟩ = ⟨2x - 2y, x - y⟩ = 2‖x - y‖² ≥ 0 ✓
```

[Back to Top](#convex-sets--functions--practice-problems)

---

## P6: Hessian Check for Convexity

**Q:** Is f(x,y) = x² + xy + y² convex? (From Lecture 2)

**Solution:**
```
Step 1: Compute gradient
  ∇f = [2x + y, x + 2y]ᵀ

Step 2: Compute Hessian
  H = [2  1]
      [1  2]

Step 3: Check PSD (eigenvalue method)
  det(H - λI) = (2-λ)² - 1 = 0
  λ² - 4λ + 3 = 0
  λ = 1, 3

  Both eigenvalues > 0 → H is PD → f is STRICTLY convex ✓

Step 3 (alt): 2×2 shortcut
  trace(H) = 4 > 0 ✓
  det(H) = 4 - 1 = 3 > 0 ✓
  → PD → Strictly convex ✓
```

> **Exam Hack:** For 2×2, trace > 0 AND det > 0 ⟹ PD. Much faster than eigenvalues!

[Back to Top](#convex-sets--functions--practice-problems)

---

## P7: Non-Convex Function Check

**Q:** Is f(x,y) = 8x + 12y + x² - 2y² convex? (From Lecture 2)

**Solution:**
```
∇f = [8 + 2x, 12 - 4y]ᵀ

H = [2   0]
    [0  -4]

Eigenvalues: 2 and -4.

One positive, one negative → H is INDEFINITE → f is NOT convex.
The function has a saddle point structure.
```

[Back to Top](#convex-sets--functions--practice-problems)

---

## P8: Composition Rules

**Q:** Show that f(x) = log(Σᵢ eˣⁱ) (log-sum-exp) is convex.

**Solution (using preservation rules):**
```
Step 1: Each eˣⁱ is convex (exponential of linear function)
Step 2: Σᵢ eˣⁱ is convex (sum of convex functions)
Step 3: log is CONCAVE (not convex!) — so we can't directly compose.

Need to verify via Hessian instead. The Hessian of log-sum-exp is:
  H = diag(p) - ppᵀ where pᵢ = eˣⁱ / Σⱼ eˣʲ

For any vector v:
  vᵀHv = Σᵢ pᵢvᵢ² - (Σᵢ pᵢvᵢ)² ≥ 0  (by Cauchy-Schwarz / Jensen)

So H ≽ 0 → convex ✓
```

> **Exam Hack:** Log-sum-exp is the standard "convex and you should know it" function. Just state it's convex and cite the Hessian is PSD.

[Back to Top](#convex-sets--functions--practice-problems)

---

## P9: Strong Convexity Parameter

**Q:** Find the strong convexity parameter µ for f(x) = (1/2)xᵀAx where A = [[4, 0], [0, 2]].

**Solution:**
```
∇²f(x) = A = [[4, 0], [0, 2]]

Eigenvalues: λ₁ = 2, λ₂ = 4.

Strong convexity parameter µ = λ_min = 2
Smoothness parameter L = λ_max = 4
Condition number κ = L/µ = 4/2 = 2

This is well-conditioned (κ close to 1 is best).
```

[Back to Top](#convex-sets--functions--practice-problems)

---

## P10: Separation Theorem

**Q:** Let S = {(x,y) : x² + y² ≤ 1} and point p = (2, 0) ∉ S. Find a separating hyperplane.

**Solution:**
```
Step 1: Project p onto S.
  Closest point in S to (2,0) is (1,0) (unit circle boundary toward p).

Step 2: Normal direction = p - projection = (2,0) - (1,0) = (1,0).

Step 3: Separating hyperplane: x = 1.
  - For all (x,y) ∈ S: x ≤ 1 ✓
  - For p = (2,0): x = 2 > 1 ✓

The hyperplane {(x,y) : x = 1} separates p from S.
```

```
      S (unit disk)       separating line: x = 1
         ┌───┐              │
        /  ○  \             │    ● p = (2,0)
       │  ○○○  │            │
        \  ○  /             │
         └───┘              │
              ↑
         closest point (1,0)
```

[Back to Top](#convex-sets--functions--practice-problems)

---

## Exam-Style Quick Questions

| # | Question | Quick Answer |
|---|----------|-------------|
| 1 | Is {x : ‖x‖₁ ≤ 5} convex? | Yes (norm ball) |
| 2 | Is f(x) = max(x₁, x₂) convex? | Yes (pointwise max of linear functions) |
| 3 | If H has eigenvalues {0, 3, 5}, is f convex? | Yes (PSD, all ≥ 0) |
| 4 | If H has eigenvalues {-1, 3, 5}, is f convex? | No (indefinite) |
| 5 | Is f(x) = ‖Ax - b‖² convex? | Yes (AᵀA is PSD) |
| 6 | Does convex function always have a minimum? | No (f(x)=eˣ is convex, no finite min) |
| 7 | Strong convexity implies unique min? | Yes, always |

---

> **Next:** [→ Topic 02: Optimality Conditions](../02-Optimality-Conditions/optimality_conditions_INDEX.md)
>
> **Back:** [← THEORY](./convex_sets_functions_THEORY.md) · [← INDEX](./convex_sets_functions_INDEX.md) · [↑ Master Hub](../ODS_Master_INDEX.md)

[Back to Top](#convex-sets--functions--practice-problems)
