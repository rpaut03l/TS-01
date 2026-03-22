# Optimality Conditions — Theory Guide
### ODS Topic 02 · Lecture 2

> **Nav:** [← INDEX](./optimality_conditions_INDEX.md) · [→ PRACTICE](./optimality_conditions_PRACTICE.md) · [↑ Hub](../ODS_Master_INDEX.md)

---

## 2.1 Fermat's Rule (1D)

### Easy Story
If you're walking along a path and you're at the LOWEST point, the ground must be flat (slope = 0). If the ground is sloping, you're NOT at the bottom yet!

### Theorem
> If f is differentiable at x* and x* is a local min or max → **f'(x*) = 0**

Points where f'(x*) = 0 are called **stationary points** or **critical points**.

**WARNING:** f'(x*) = 0 does NOT guarantee min! Could be max or inflection.
- f(x) = (x-1)²: f'(1) = 0 → LOCAL MIN ✓
- g(x) = -(x+1)²: g'(-1) = 0 → LOCAL MAX
- h(x) = x³: h'(0) = 0 → NEITHER (inflection point)

```
  MIN: ∪ shape        MAX: ∩ shape        INFLECTION: ~ shape
  f''(x*)>0           f''(x*)<0           f''(x*)=0
      ●                   ●                   ●
     / \                 / \                / \
    /   \              ●    ●              ●    ●
```

[Back to Top](#optimality-conditions--theory-guide)

---

## 2.2 Second-Order Sufficiency (1D)

At a critical point x* (where f'(x*) = 0):
- f''(x*) > 0 → **strict local minimum** (bowl curves up)
- f''(x*) < 0 → **strict local maximum** (bowl curves down)
- f''(x*) = 0 → **inconclusive** (need higher derivatives or Taylor)

**Why?** Taylor expansion: f(x) ≈ f(x*) + (1/2)f''(x*)(x - x*)²
If f''(x*) > 0, the quadratic term is positive → f(x) > f(x*) nearby → min!

[Back to Top](#optimality-conditions--theory-guide)

---

## 2.3 Multivariable Fermat's Rule

### Theorem
> If f: Rⁿ → R is differentiable at interior local min/max x* → **∇f(x*) = 0**

**Intuition:** Along ANY direction d, the 1D function φ(t) = f(x* + td) has a local extremum at t = 0. So φ'(0) = ∇f(x*)ᵀd = 0 for ALL d. This forces ∇f(x*) = 0.

### Example
f(x,y) = x² + xy + y²

∇f = [2x + y, x + 2y]ᵀ = 0 → x* = (0, 0)

```
  ∇f = 0 at (0,0)
  
  Contour plot:
     y
     │  ╱╲
     │ ╱  ╲  elliptical contours
     │╱  ◉ ╲ ← (0,0) is minimum
     │╲    ╱
     │ ╲  ╱
     └──────── x
```

[Back to Top](#optimality-conditions--theory-guide)

---

## 2.4 Second-Order Sufficiency (Multivariable)

Let x* be stationary (∇f(x*) = 0) and H = ∇²f(x*):

| Hessian H | Classification | Eigenvalue Pattern |
|-----------|---------------|-------------------|
| H ≻ 0 (PD) | **Strict local min** | All λᵢ > 0 |
| H ≺ 0 (ND) | **Strict local max** | All λᵢ < 0 |
| H indefinite | **Saddle point** | Some λᵢ > 0, some < 0 |
| H ≽ 0 (PSD) | Inconclusive | All λᵢ ≥ 0 (could be flat) |

### Worked Example (From Lecture 2)
f(x,y) = x² + xy + y²

H = [[2, 1], [1, 2]]. Eigenvalues: {1, 3} → all > 0 → PD → (0,0) is **strict local minimum** ✓

### Why Convexity Changes Everything

For **general** functions: ∇f = 0 is necessary but NOT sufficient. Need Hessian check.
For **convex** functions: ∇f = 0 IS sufficient for GLOBAL minimum! No Hessian needed.

```
  GENERAL f:                        CONVEX f:
  ∇f=0 could be:                   ∇f=0 means:
  - local min                       - GLOBAL min (guaranteed!)
  - local max                       
  - saddle point                    "Every valley bottom is THE
  - inflection                       deepest point"
```

---

## 2.5 Summary Decision Flowchart

```
  Given f(x), find and classify critical points:
  
  Step 1: Compute ∇f(x) and set = 0. Solve for x*.
           │
  Step 2: Compute H = ∇²f(x*) at each critical point.
           │
  Step 3:  ├─ Is f known to be convex?
           │   └─ YES → x* is GLOBAL MIN. Done!
           │
           └─ NO → Check eigenvalues of H:
                    ├─ All > 0 → Strict local min
                    ├─ All < 0 → Strict local max  
                    ├─ Mixed signs → Saddle point
                    └─ Some zero → Inconclusive (need more analysis)
```

---

> **Next:** [→ PRACTICE](./optimality_conditions_PRACTICE.md) · [→ Topic 03](../03-Least-Squares-Linear-Regression/least_squares_INDEX.md)
> **Back:** [← INDEX](./optimality_conditions_INDEX.md) · [↑ Hub](../ODS_Master_INDEX.md)

[Back to Top](#optimality-conditions--theory-guide)
