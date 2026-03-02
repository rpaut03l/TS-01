# 🔢 Essence of Calculus — PRACTICE PROBLEMS GUIDE
### 🎓 ODS | 14+ Fully Solved Problems — Steps Explained
> 🔗 **Navigation:** [← Back to INDEX](./Essence_of_Calculus_INDEX.md) | [← Theory Guide](./Essence_of_Calculus_THEORY.md)

---

## 📚 Problem Index

| # | Problem | Concepts | Theory |
|---|---------|----------|--------|
| P1 | [Derivative from First Principles](#-p1-derivative-from-first-principles) | Definition of derivative | [📘 Ch2](./Essence_of_Calculus_THEORY.md#chapter-2--the-paradox-of-the-derivative) |
| P2 | [Power Rule Derivatives](#-p2-power-rule-derivatives) | Power rule | [📘 Ch3](./Essence_of_Calculus_THEORY.md#chapter-3--derivative-formulas-through-geometry) |
| P3 | [Trig Derivatives](#-p3-trig-derivatives) | sin, cos derivatives | [📘 Ch3](./Essence_of_Calculus_THEORY.md#chapter-3--derivative-formulas-through-geometry) |
| P4 | [Product Rule](#-p4-product-rule) | Product rule | [📘 Ch4](./Essence_of_Calculus_THEORY.md#chapter-4--chain-rule--product-rule) |
| P5 | [Chain Rule](#-p5-chain-rule) | Chain rule | [📘 Ch4](./Essence_of_Calculus_THEORY.md#chapter-4--chain-rule--product-rule) |
| P6 | [Exponential Derivatives](#-p6-exponential-derivatives) | eˣ, aˣ | [📘 Ch5](./Essence_of_Calculus_THEORY.md#chapter-5--eulers-number-e) |
| P7 | [Implicit Differentiation](#-p7-implicit-differentiation) | Implicit diff | [📘 Ch6](./Essence_of_Calculus_THEORY.md#chapter-6--implicit-differentiation) |
| P8 | [Limits & L'Hôpital's Rule](#-p8-limits--lhôpitals-rule) | Limits, L'Hôpital | [📘 Ch7](./Essence_of_Calculus_THEORY.md#chapter-7--limits-and-lhôpitals-rule) |
| P9 | [Definite Integrals](#-p9-definite-integrals) | FTC, area | [📘 Ch8](./Essence_of_Calculus_THEORY.md#chapter-8--integration-and-the-fundamental-theorem) |
| P10 | [Antiderivatives](#-p10-antiderivatives--indefinite-integrals) | Indefinite integral | [📘 Ch8](./Essence_of_Calculus_THEORY.md#chapter-8--integration-and-the-fundamental-theorem) |
| P11 | [Higher Order Derivatives](#-p11-higher-order-derivatives) | f'', concavity | [📘 Ch10](./Essence_of_Calculus_THEORY.md#chapter-10--higher-order-derivatives) |
| P12 | [Taylor Series Expansion](#-p12-taylor-series-expansion) | Taylor/Maclaurin | [📘 Ch11](./Essence_of_Calculus_THEORY.md#chapter-11--taylor-series) |
| P13 | [Taylor Series Error Bound](#-p13-taylor-series-error-bound) | Convergence | [📘 Ch11](./Essence_of_Calculus_THEORY.md#chapter-11--taylor-series) |
| P14 | [Jacobian & Transformation View](#-p14-jacobian--transformation-view) | Jacobian | [📘 Ch12](./Essence_of_Calculus_THEORY.md#chapter-12--the-other-way-to-visualize-derivatives) |

---

## 📖 Rules & Formulas Quick Reference

```
 ┌───────────── DERIVATIVE RULES ─────────────────────────┐
 │  Power:     d/dx(xⁿ) = nxⁿ⁻¹                           │
 │  Product:   d/dx(fg) = f'g + fg'                       │
 │  Chain:     d/dx[f(g(x))] = f'(g(x))·g'(x)             │
 │  Trig:      (sin x)'=cos x   (cos x)'=−sin x           │
 │  Exp:       (eˣ)'=eˣ         (aˣ)'=aˣ·ln(a)            │
 │  Log:       (ln x)'=1/x                                │
 ├───────────── INTEGRATION RULES ────────────────────────┤
 │  Power:     ∫xⁿ dx = xⁿ⁺¹/(n+1)+C                      │
 │  Exp:       ∫eˣ dx = eˣ+C                              │
 │  Trig:      ∫cos dx = sin+C  ∫sin dx = −cos+C          │
 │  FTC:       ∫ₐᵇ f(x)dx = F(b)−F(a)                     │
 ├───────────── TAYLOR (at a=0) ──────────────────────────┤
 │  f(x) = f(0)+f'(0)x+f''(0)x²/2!+f'''(0)x³/3!+...       │
 ├───────────── L'HÔPITAL ────────────────────────────────┤
 │  If 0/0 or ∞/∞: lim f/g = lim f'/g'                    │
 └────────────────────────────────────────────────────────┘
```

---

## 🧮 P1: Derivative from First Principles

> 📘 [Theory Ch 2](./Essence_of_Calculus_THEORY.md#chapter-2--the-paradox-of-the-derivative) | ⬆️ [Index](#-problem-index)

**Problem:** Find f'(x) from first principles for (a) f(x)=x² (b) f(x)=3x²+2x

**Rule:** f'(x) = lim[h→0] (f(x+h)−f(x))/h

**(a) f(x) = x²:**
```
  Step 1: Compute f(x+h)
    f(x+h) = (x+h)² = x² + 2xh + h²
  
  Step 2: Compute f(x+h)−f(x)
    = x²+2xh+h² − x² = 2xh + h²
  
  Step 3: Divide by h
    (2xh + h²)/h = 2x + h
  
  Step 4: Take limit as h→0
    lim[h→0](2x + h) = 2x
  
  f'(x) = 2x  ✅
  
  Verify: Power rule gives d/dx(x²) = 2·x²⁻¹ = 2x  ✅
```

**(b) f(x) = 3x²+2x:**
```
  Step 1: f(x+h) = 3(x+h)²+2(x+h) = 3x²+6xh+3h²+2x+2h
  
  Step 2: f(x+h)−f(x) = 6xh+3h²+2h
  
  Step 3: Divide by h: 6x+3h+2
  
  Step 4: lim[h→0] = 6x+2
  
  f'(x) = 6x+2  ✅
  
  Verify: d/dx(3x²)+d/dx(2x) = 6x+2  ✅
```

---

## 🧮 P2: Power Rule Derivatives

> 📘 [Theory Ch 3](./Essence_of_Calculus_THEORY.md#chapter-3--derivative-formulas-through-geometry) | ⬆️ [Index](#-problem-index)

**Problem:** Differentiate: (a) x⁷ (b) 4x³−2x²+5x−1 (c) √x (d) 1/x³

**Rule:** d/dx(xⁿ) = nxⁿ⁻¹  (works for ALL real n, not just integers!)

```
  (a) d/dx(x⁷) = 7x⁶  ✅
      (Power 7 "comes down," exponent becomes 7−1=6)
  
  (b) d/dx(4x³−2x²+5x−1)
      = 4·3x² − 2·2x + 5·1 − 0
      = 12x² − 4x + 5  ✅
      (Differentiate term by term; constant disappears)
  
  (c) √x = x^(1/2)
      d/dx(x^(1/2)) = (1/2)·x^(1/2−1) = (1/2)·x^(−1/2) = 1/(2√x)  ✅
  
  (d) 1/x³ = x⁻³
      d/dx(x⁻³) = −3·x⁻⁴ = −3/x⁴  ✅
      (Power rule works with negative exponents too!)
```

---

## 🧮 P3: Trig Derivatives

> 📘 [Theory Ch 3](./Essence_of_Calculus_THEORY.md#chapter-3--derivative-formulas-through-geometry) | ⬆️ [Index](#-problem-index)

**Problem:** Differentiate: (a) 3sin(x)+cos(x) (b) sin²(x) (c) tan(x)

**Rules:** (sin x)'=cos x, (cos x)'=−sin x, chain rule for compositions.

```
  (a) d/dx[3sin(x)+cos(x)] = 3cos(x)+(−sin(x)) = 3cos(x)−sin(x)  ✅
  
  (b) sin²(x) = [sin(x)]²     ← needs CHAIN RULE!
      Outer: (·)²   Inner: sin(x)
      d/dx = 2·sin(x)·cos(x) = sin(2x)  ✅
      (Using double angle identity: 2sinxcosx = sin2x)
  
  (c) tan(x) = sin(x)/cos(x)   ← needs QUOTIENT RULE!
      d/dx = [cos(x)·cos(x)−sin(x)·(−sin(x))]/cos²(x)
           = [cos²(x)+sin²(x)]/cos²(x)
           = 1/cos²(x)
           = sec²(x)  ✅
```

---

## 🧮 P4: Product Rule

> 📘 [Theory Ch 4](./Essence_of_Calculus_THEORY.md#chapter-4--chain-rule--product-rule) | ⬆️ [Index](#-problem-index)

**Problem:** Differentiate: (a) x²·eˣ (b) x·sin(x)·cos(x)

**Rule:** (fg)' = f'g + fg'  — "Left'·Right + Left·Right'"

```
  (a) f=x², g=eˣ → f'=2x, g'=eˣ
      d/dx = 2x·eˣ + x²·eˣ = eˣ(2x+x²) = eˣ·x(2+x)  ✅
      
      Check logic:
        f'g = (deriv of left)×(right untouched) = 2x·eˣ
        fg' = (left untouched)×(deriv of right) = x²·eˣ
        Sum them!
  
  (b) Three functions! Use product rule twice:
      Let h = x·sin(x)·cos(x) = (x·sin(x))·cos(x)
      
      f=x·sin(x), g=cos(x)
      f'= 1·sin(x)+x·cos(x) = sin(x)+x·cos(x)   (product rule on f)
      g'= −sin(x)
      
      h' = f'·g + f·g'
         = [sin(x)+x·cos(x)]·cos(x) + x·sin(x)·(−sin(x))
         = sin(x)cos(x) + x·cos²(x) − x·sin²(x)
         = sin(x)cos(x) + x·cos(2x)  ✅
         (Using cos²x−sin²x = cos2x)
```

---

## 🧮 P5: Chain Rule

> 📘 [Theory Ch 4](./Essence_of_Calculus_THEORY.md#chapter-4--chain-rule--product-rule) | ⬆️ [Index](#-problem-index)

**Problem:** Differentiate: (a) sin(3x) (b) e^(x²) (c) ln(x²+1) (d) (2x+1)⁵

**Rule:** d/dx[f(g(x))] = f'(g(x))·g'(x) — "Outer derivative × Inner derivative"

```
  (a) Outer: sin(·)  Inner: 3x
      = cos(3x) · 3 = 3cos(3x)  ✅
  
  (b) Outer: e^(·)  Inner: x²
      = e^(x²) · 2x = 2x·e^(x²)  ✅
  
  (c) Outer: ln(·)  Inner: x²+1
      = 1/(x²+1) · 2x = 2x/(x²+1)  ✅
  
  (d) Outer: (·)⁵  Inner: 2x+1
      = 5(2x+1)⁴ · 2 = 10(2x+1)⁴  ✅
  
  NESTED example: d/dx[sin(e^(3x))]
      Outermost: sin(·)  → cos(e^(3x))
      Middle: e^(·)      → × e^(3x)
      Innermost: 3x      → × 3
      = 3·e^(3x)·cos(e^(3x))  ✅
      (Peel the ONION from outside in!)
```

---

## 🧮 P6: Exponential Derivatives

> 📘 [Theory Ch 5](./Essence_of_Calculus_THEORY.md#chapter-5--eulers-number-e) | ⬆️ [Index](#-problem-index)

**Problem:** Differentiate: (a) 5eˣ (b) 2ˣ (c) e^(−x²/2) (d) x·eˣ

**Rules:** (eˣ)'=eˣ, (aˣ)'=aˣ·ln(a). Chain rule for compositions.

```
  (a) d/dx(5eˣ) = 5eˣ  ✅   (constant factor stays)
  
  (b) d/dx(2ˣ) = 2ˣ·ln(2) ≈ 0.693·2ˣ  ✅
  
  (c) e^(−x²/2):  Outer=e^(·), Inner=−x²/2
      = e^(−x²/2) · d/dx(−x²/2)
      = e^(−x²/2) · (−x)
      = −x·e^(−x²/2)  ✅
      
      🤖 AI/ML note: This is the derivative of the Gaussian bell curve!
         p(x) ∝ e^(−x²/2) → p'(x) ∝ −x·e^(−x²/2)
  
  (d) x·eˣ: Product rule!
      = 1·eˣ + x·eˣ = eˣ(1+x)  ✅
```

---

## 🧮 P7: Implicit Differentiation

> 📘 [Theory Ch 6](./Essence_of_Calculus_THEORY.md#chapter-6--implicit-differentiation) | ⬆️ [Index](#-problem-index)

**Problem:** Find dy/dx for (a) x²+y²=25 (b) x·y+y²=3

**Rule:** Differentiate both sides w.r.t. x. Treat y as y(x). Use chain rule: d/dx(y²)=2y·(dy/dx).

```
  (a) x²+y²=25
      Diff both sides: 2x + 2y·(dy/dx) = 0
      Solve: dy/dx = −2x/(2y) = −x/y  ✅
      
      At (3,4): dy/dx = −3/4 (tangent slopes down-right)
      At (0,5): dy/dx = 0 (horizontal tangent at top of circle)
  
  (b) x·y+y²=3
      Use product rule on x·y: (1)·y + x·(dy/dx) + 2y·(dy/dx) = 0
      Collect: x·(dy/dx) + 2y·(dy/dx) = −y
      Factor: (x+2y)·(dy/dx) = −y
      Solve: dy/dx = −y/(x+2y)  ✅
```

---

## 🧮 P8: Limits & L'Hôpital's Rule

> 📘 [Theory Ch 7](./Essence_of_Calculus_THEORY.md#chapter-7--limits-and-lhôpitals-rule) | ⬆️ [Index](#-problem-index)

**Problem:** Evaluate: (a) lim(x→0) sin(x)/x (b) lim(x→∞) x/eˣ (c) lim(x→0)(eˣ−1−x)/x²

**Rule:** If 0/0 or ∞/∞ → differentiate top and bottom separately, re-evaluate.

```
  (a) lim(x→0) sin(x)/x = 0/0 → L'Hôpital:
      = lim(x→0) cos(x)/1 = cos(0)/1 = 1  ✅
  
  (b) lim(x→∞) x/eˣ = ∞/∞ → L'Hôpital:
      = lim(x→∞) 1/eˣ = 1/∞ = 0  ✅
      (Exponential beats polynomial → eˣ grows faster than x)
  
  (c) lim(x→0) (eˣ−1−x)/x² = (1−1−0)/0 = 0/0 → L'Hôpital:
      = lim(x→0) (eˣ−1)/(2x) = 0/0 → L'Hôpital AGAIN:
      = lim(x→0) eˣ/2 = 1/2  ✅
      (Applied L'Hôpital twice — legal since each step gave 0/0)
```

---

## 🧮 P9: Definite Integrals

> 📘 [Theory Ch 8](./Essence_of_Calculus_THEORY.md#chapter-8--integration-and-the-fundamental-theorem) | ⬆️ [Index](#-problem-index)

**Problem:** Compute: (a) ∫₀³ x² dx (b) ∫₀^π sin(x) dx (c) ∫₁ᵉ (1/x) dx

**Rule:** FTC Part 2: ∫ₐᵇ f(x)dx = F(b)−F(a), where F'(x)=f(x).

```
  (a) Antiderivative of x² is x³/3  (since d/dx(x³/3)=x²)
      ∫₀³ x² dx = [x³/3]₀³ = 3³/3 − 0³/3 = 27/3 = 9  ✅
  
  (b) Antiderivative of sin(x) is −cos(x)
      ∫₀^π sin(x) dx = [−cos(x)]₀^π = −cos(π)−(−cos(0))
                      = −(−1)−(−1) = 1+1 = 2  ✅
      
      Geometric check: area under one arch of sin = 2 ✅
  
  (c) Antiderivative of 1/x is ln|x|
      ∫₁ᵉ (1/x) dx = [ln|x|]₁ᵉ = ln(e)−ln(1) = 1−0 = 1  ✅
```

---

## 🧮 P10: Antiderivatives & Indefinite Integrals

> 📘 [Theory Ch 8](./Essence_of_Calculus_THEORY.md#chapter-8--integration-and-the-fundamental-theorem) | ⬆️ [Index](#-problem-index)

**Problem:** Find antiderivatives: (a) ∫6x² dx (b) ∫(3cos x+eˣ) dx (c) ∫x⁻¹ dx

**Rule:** Reverse the derivative rules! Add +C always.

```
  (a) ∫6x² dx = 6·x³/3 + C = 2x³ + C  ✅
      Verify: d/dx(2x³+C) = 6x²  ✅
  
  (b) ∫(3cos x+eˣ) dx = 3sin(x) + eˣ + C  ✅
      Verify: d/dx(3sin x + eˣ + C) = 3cos x + eˣ  ✅
  
  (c) ∫x⁻¹ dx = ∫(1/x) dx = ln|x| + C  ✅
      ⚠️ Cannot use power rule here! (n=−1 gives x⁰/0 = undefined)
      This is the ONE exception: 1/x integrates to ln|x|
```

---

## 🧮 P11: Higher Order Derivatives

> 📘 [Theory Ch 10](./Essence_of_Calculus_THEORY.md#chapter-10--higher-order-derivatives) | ⬆️ [Index](#-problem-index)

**Problem:** For f(x)=x⁴−6x²+9: find f', f'', classify critical points.

```
  Step 1: First derivative
    f'(x) = 4x³−12x
  
  Step 2: Critical points (f'=0)
    4x³−12x = 0 → 4x(x²−3) = 0 → x=0, x=±√3
  
  Step 3: Second derivative
    f''(x) = 12x²−12
  
  Step 4: Classify using f'':
    At x=0:   f''(0) = 0−12 = −12 < 0 → LOCAL MAXIMUM ✅
    At x=√3:  f''(√3) = 12·3−12 = 24 > 0 → LOCAL MINIMUM ✅
    At x=−√3: f''(−√3) = 12·3−12 = 24 > 0 → LOCAL MINIMUM ✅
  
  Step 5: Function values
    f(0) = 0−0+9 = 9 (local max)
    f(±√3) = 9−18+9 = 0 (local min)
  
       f(x)
      9 │    ·        local max at (0,9)
        │   ╱╲
        │  ╱  ╲       concave down (f''<0)
        │ ╱    ╲
      0 ·───────·──── local min at (±√3, 0)
       -√3      √3   concave up (f''>0) on sides
```

---

## 🧮 P12: Taylor Series Expansion

> 📘 [Theory Ch 11](./Essence_of_Calculus_THEORY.md#chapter-11--taylor-series) | ⬆️ [Index](#-problem-index)

**Problem:** Find 4th-degree Maclaurin polynomial for (a) sin(x) (b) 1/(1−x)

**Rule:** f(x) ≈ f(0)+f'(0)x+f''(0)x²/2!+f'''(0)x³/3!+f⁴(0)x⁴/4!

```
  (a) sin(x):
      f(0)=sin(0)=0       → term: 0
      f'(0)=cos(0)=1      → term: x
      f''(0)=−sin(0)=0    → term: 0
      f'''(0)=−cos(0)=−1  → term: −x³/3! = −x³/6
      f⁴(0)=sin(0)=0      → term: 0
      
      P₄(x) = x − x³/6  ✅
      
      Check: sin(0.1) ≈ 0.1 − 0.001/6 = 0.0998333...
      Actual: sin(0.1) = 0.0998334... → extremely close!
  
  (b) 1/(1−x):
      f(0)=1,  f'(x)=1/(1−x)² → f'(0)=1
      f''(x)=2/(1−x)³ → f''(0)=2 → term: 2x²/2!=x²
      f'''(0)=6 → term: 6x³/6=x³
      f⁴(0)=24 → term: 24x⁴/24=x⁴
      
      P₄(x) = 1+x+x²+x³+x⁴  ✅  (geometric series!)
      
      Converges only for |x|<1
```

---

## 🧮 P13: Taylor Series Error Bound

> 📘 [Theory Ch 11](./Essence_of_Calculus_THEORY.md#chapter-11--taylor-series) | ⬆️ [Index](#-problem-index)

**Problem:** Estimate e^(0.1) using 3-term Taylor series. How close to actual?

```
  eˣ = 1+x+x²/2+x³/6+...
  
  3 terms for x=0.1:
    e^(0.1) ≈ 1 + 0.1 + (0.1)²/2
            = 1 + 0.1 + 0.005
            = 1.105
  
  4 terms: + (0.1)³/6 = 0.000167 → 1.10517
  
  Actual: e^(0.1) = 1.10517...
  
  3-term error: |1.105 − 1.10517| = 0.00017 (0.015% error!)
  4-term error: |1.10517 − 1.10517| ≈ 0.000004
  
  Error bound: |Rₙ(x)| ≤ |x|ⁿ⁺¹/(n+1)!
  For n=2, x=0.1: (0.1)³/6 = 0.000167 ✅ matches actual error
  
  🤖 The fewer terms you use, the faster but less accurate.
     ML models face the SAME tradeoff (model complexity vs accuracy)!
```

---

## 🧮 P14: Jacobian & Transformation View

> 📘 [Theory Ch 12](./Essence_of_Calculus_THEORY.md#chapter-12--the-other-way-to-visualize-derivatives) | ⬆️ [Index](#-problem-index)

**Problem:** For f(x,y)=(x²−y, x+y²), find the Jacobian matrix and its determinant at (1,1).

**Rule:** Jacobian J = [[∂f₁/∂x, ∂f₁/∂y],[∂f₂/∂x, ∂f₂/∂y]]. |det(J)| = local area scaling.

```
  f₁(x,y) = x²−y     f₂(x,y) = x+y²
  
  Step 1: Partial derivatives
    ∂f₁/∂x = 2x    ∂f₁/∂y = −1
    ∂f₂/∂x = 1      ∂f₂/∂y = 2y
  
  Step 2: Jacobian matrix
    J = [ 2x   -1 ]
        [  1   2y ]
  
  Step 3: At (1,1):
    J = [ 2   -1 ]
        [ 1    2 ]
  
  Step 4: Determinant
    det(J) = 2·2−(−1)·1 = 4+1 = 5
  
  Interpretation:
    Near (1,1), the transformation STRETCHES areas by factor 5.
    det>0 → orientation preserved (no flipping).
    
    🤖 In normalizing flows: new_density = old_density / |det(J)|
       If a region stretches 5×, probability density shrinks to 1/5.
```

---

> 🔗 **Theory explanations:** [← Theory Guide](./Essence_of_Calculus_THEORY.md)
>
> 🔗 **Master hub:** [← INDEX](./Essence_of_Calculus_INDEX.md)
>
> 🎓 **Created for:** ODS
