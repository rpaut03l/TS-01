# 🔢 Essence of Calculus — PRACTICE PROBLEMS GUIDE
### 🎓 ODS | ML
> 🔗 **Navigation:** [← Back to INDEX](./Essence_of_Calculus_INDEX.md) | [← Theory Guide](./Essence_of_Calculus_THEORY.md)
>
> 🍎 **How to use this guide:** Every single step is explained as if you've NEVER seen it before. Nothing is assumed. Every rule is stated, every substitution shown, every simplification justified. Read top-to-bottom and you'll understand everything.

---

## 📚 Problem Index

| # | Problem | Concepts | Theory |
|---|---------|----------|--------|
| P1 | [Derivative from First Principles](#-p1-derivative-from-first-principles) | Definition of derivative | [📘 Ch2](./Essence_of_Calculus_THEORY.md#chapter-2--the-paradox-of-the-derivative) |
| P2 | [Power Rule Derivatives](#-p2-power-rule-derivatives) | Power rule | [📘 Ch3](./Essence_of_Calculus_THEORY.md#chapter-3--derivative-formulas-through-geometry) |
| P3 | [Trig Derivatives](#-p3-trig-derivatives) | sin, cos, tan | [📘 Ch3](./Essence_of_Calculus_THEORY.md#chapter-3--derivative-formulas-through-geometry) |
| P4 | [Product Rule](#-p4-product-rule) | Product rule | [📘 Ch4](./Essence_of_Calculus_THEORY.md#chapter-4--chain-rule--product-rule) |
| P5 | [Chain Rule](#-p5-chain-rule) | Chain rule | [📘 Ch4](./Essence_of_Calculus_THEORY.md#chapter-4--chain-rule--product-rule) |
| P6 | [Exponential Derivatives](#-p6-exponential-derivatives) | eˣ, aˣ | [📘 Ch5](./Essence_of_Calculus_THEORY.md#chapter-5--eulers-number-e) |
| P7 | [Implicit Differentiation](#-p7-implicit-differentiation) | Implicit diff | [📘 Ch6](./Essence_of_Calculus_THEORY.md#chapter-6--implicit-differentiation) |
| P8 | [Limits & L'Hôpital's Rule](#-p8-limits--lhôpitals-rule) | Limits | [📘 Ch7](./Essence_of_Calculus_THEORY.md#chapter-7--limits-and-lhôpitals-rule) |
| P9 | [Definite Integrals](#-p9-definite-integrals) | FTC, area | [📘 Ch8](./Essence_of_Calculus_THEORY.md#chapter-8--integration-and-the-fundamental-theorem) |
| P10 | [Antiderivatives](#-p10-antiderivatives--indefinite-integrals) | Indefinite integral | [📘 Ch8](./Essence_of_Calculus_THEORY.md#chapter-8--integration-and-the-fundamental-theorem) |
| P11 | [Higher Order Derivatives](#-p11-higher-order-derivatives) | f'', concavity | [📘 Ch10](./Essence_of_Calculus_THEORY.md#chapter-10--higher-order-derivatives) |
| P12 | [Taylor Series Expansion](#-p12-taylor-series-expansion) | Taylor/Maclaurin | [📘 Ch11](./Essence_of_Calculus_THEORY.md#chapter-11--taylor-series) |
| P13 | [Taylor Series Error Bound](#-p13-taylor-series-error-bound) | Convergence | [📘 Ch11](./Essence_of_Calculus_THEORY.md#chapter-11--taylor-series) |
| P14 | [Jacobian & Transformation View](#-p14-jacobian--transformation-view) | Jacobian | [📘 Ch12](./Essence_of_Calculus_THEORY.md#chapter-12--the-other-way-to-visualize-derivatives) |

---

## 📖 RULES & FORMULAS — Read This First!

> Every rule below is used in the problems. Come back here whenever you see a rule name.

### 🔹 What IS a Derivative?

```
  The DERIVATIVE of f(x) answers: "If I nudge x by a tiny amount,
  how much does f(x) change?"
  
  Written as: f'(x) or df/dx
  
  FORMAL DEFINITION:
  ┌──────────────────────────────────────────────────────────┐
  │                                                          │
  │           f(x + h) − f(x)                                │
  │  f'(x) = lim ─────────────                               │
  │           h→0       h                                    │
  │                                                          │
  │  In words: "take f at x+h, subtract f at x,              │
  │   divide by h, then shrink h toward zero"                │
  └──────────────────────────────────────────────────────────┘
  
  🍎 Kid version: How FAST is something changing RIGHT NOW?
```

### 🔹 Derivative Rules Cheat Sheet

```
  RULE NAME          │  FORMULA                          │  WHEN TO USE
  ───────────────────┼───────────────────────────────────┼──────────────────────
  Constant rule      │  d/dx(c) = 0                      │  c is any fixed number
  Power rule         │  d/dx(xⁿ) = n · xⁿ⁻¹              │  x raised to any power
  Constant multiple  │  d/dx(c·f) = c · f'(x)            │  number × function
  Sum rule           │  d/dx(f+g) = f' + g'              │  adding functions
  Product rule       │  d/dx(f·g) = f'·g + f·g'          │  multiplying functions
  Quotient rule      │  d/dx(f/g) = (f'g − fg')/g²       │  dividing functions
  Chain rule         │  d/dx[f(g(x))] = f'(g(x))·g'(x)   │  function INSIDE function
  ───────────────────┼───────────────────────────────────┼──────────────────────
  d/dx(sin x) = cos x         │  d/dx(eˣ) = eˣ
  d/dx(cos x) = −sin x        │  d/dx(aˣ) = aˣ · ln(a)
  d/dx(tan x) = sec²x         │  d/dx(ln x) = 1/x
```

### 🔹 Integration Rules Cheat Sheet

```
  Integration = REVERSE of differentiation (find the "original" function)
  
  ∫xⁿ dx = xⁿ⁺¹/(n+1) + C     (add 1 to power, divide by new power)
  ∫eˣ dx = eˣ + C               ∫(1/x) dx = ln|x| + C
  ∫cos x dx = sin x + C         ∫sin x dx = −cos x + C
  
  +C = "constant of integration" (any fixed number; disappears when differentiating)
  
  FTC (Fundamental Theorem):  ∫ₐᵇ f(x) dx = F(b) − F(a)
    where F is any antiderivative of f (meaning F' = f)
```

### 🔹 Key Notations

```
  f(x)    = a function: put x in, get a number out
  f'(x)   = first derivative of f  (also written df/dx)
  f''(x)  = second derivative       (also written d²f/dx²)
  h or dx = a tiny nudge (small number approaching 0)
  lim     = "the value approached as h gets closer and closer to 0"
  h→0
  ∫       = integral sign (means "add up all the thin slices")
  ∫ₐᵇ     = definite integral (add slices from x=a to x=b)
  n!      = n factorial = n × (n-1) × (n-2) × ... × 2 × 1
            Example: 4! = 4×3×2×1 = 24
```

---
---

## 🧮 P1: Derivative from First Principles

> 📘 Theory: [Ch 2 — Paradox of the Derivative](./Essence_of_Calculus_THEORY.md#chapter-2--the-paradox-of-the-derivative) | ⬆️ [Problem Index](#-problem-index)

### Problem (a): Find f'(x) from first principles for f(x) = x²

**What "from first principles" means:**
> We're NOT using any shortcut rules. We use the DEFINITION directly:
> f'(x) = lim[h→0] (f(x+h) − f(x)) / h

**Step 1 — Write down f(x):**
```
  f(x) = x²
  
  This means: whatever number you put in, you SQUARE it.
  Example: f(3) = 3² = 9,  f(5) = 5² = 25
```

**Step 2 — Compute f(x + h): Replace every "x" with "(x + h)":**
```
  f(x) = x²
  f(x + h) = (x + h)²
  
  Now EXPAND (x + h)² using the identity (a+b)² = a² + 2ab + b²:
    Here a = x and b = h, so:
    
    (x + h)² = x² + 2·x·h + h²
    
  ┌─────────────────────────────────────────────┐
  │  WHY does (x+h)² = x² + 2xh + h²?           │
  │                                             │
  │  (x+h)² = (x+h)(x+h)                        │
  │         = x·x + x·h + h·x + h·h             │
  │         = x² + xh + hx + h²                 │
  │         = x² + 2xh + h²                     │
  │                                             │
  │  (because xh + hx = 2xh)                    │
  └─────────────────────────────────────────────┘
  
  So: f(x + h) = x² + 2xh + h²
```

**Step 3 — Compute the DIFFERENCE f(x + h) − f(x):**
```
  f(x + h) − f(x) = (x² + 2xh + h²) − (x²)
  
  Now subtract term by term:
    x² − x² = 0          ← these CANCEL out! 
    + 2xh remains
    + h² remains
  
  Result: f(x + h) − f(x) = 2xh + h²
  
  🍎 What just happened? The x² terms disappeared! That's the key
     trick — most of the function cancels, leaving only the "change" part.
```

**Step 4 — DIVIDE by h:**
```
  f(x + h) − f(x)     2xh + h²
  ──────────────── = ───────────
         h                h
  
  Now divide EACH term in the numerator by h:
  
    2xh ÷ h = 2x       ← the h's cancel: (2x·h)/h = 2x
    h²  ÷ h = h        ← one h cancels: (h·h)/h = h
  
  Result: 2x + h
```

**Step 5 — Take the LIMIT as h → 0:**
```
  lim [2x + h]
  h→0
  
  "Let h get closer and closer to zero."
  
  When h = 0.1:   2x + 0.1    (close to 2x)
  When h = 0.001: 2x + 0.001  (very close to 2x)
  When h → 0:     2x + 0 = 2x (exactly!)
  
  ┌─────────────────────────────────────┐
  │  f'(x) = 2x  ✅                     │
  │                                     │
  │  Meaning: At any point x, the slope │
  │  of f(x)=x² is 2x.                  │
  │  At x=3: slope = 2(3) = 6           │
  │  At x=0: slope = 0 (flat!)          │
  └─────────────────────────────────────┘
```

**Step 6 — VERIFY using Power Rule shortcut:**
```
  Power Rule: d/dx(xⁿ) = n · xⁿ⁻¹
  
  For x²: n = 2
  d/dx(x²) = 2 · x²⁻¹ = 2 · x¹ = 2x  ✅  (matches!)
```

---

### Problem (b): Find f'(x) from first principles for f(x) = 3x² + 2x

**Step 1 — Write down f(x):**
```
  f(x) = 3x² + 2x
```

**Step 2 — Compute f(x + h): Replace every "x" with "(x + h)":**
```
  f(x + h) = 3(x + h)² + 2(x + h)
  
  Expand 3(x+h)²:
    First: (x+h)² = x² + 2xh + h²  (same as before)
    Then:  3 × (x² + 2xh + h²) = 3x² + 6xh + 3h²
    
  Expand 2(x+h):
    2 × x + 2 × h = 2x + 2h
  
  Combine everything:
    f(x + h) = 3x² + 6xh + 3h² + 2x + 2h
```

**Step 3 — Compute the DIFFERENCE:**
```
  f(x + h) − f(x) = (3x² + 6xh + 3h² + 2x + 2h) − (3x² + 2x)
  
  Subtract term by term:
    3x² − 3x² = 0      ← cancels!
    6xh remains
    3h² remains
    2x − 2x = 0         ← cancels!
    2h remains
  
  Result: 6xh + 3h² + 2h
```

**Step 4 — DIVIDE by h:**
```
  (6xh + 3h² + 2h) / h
  
  Divide each term by h:
    6xh ÷ h = 6x     (h cancels)
    3h² ÷ h = 3h      (one h cancels)
    2h  ÷ h = 2       (h cancels)
  
  Result: 6x + 3h + 2
```

**Step 5 — Take the LIMIT as h → 0:**
```
  lim [6x + 3h + 2] = 6x + 3(0) + 2 = 6x + 2
  h→0
  
  ┌────────────────────────┐
  │  f'(x) = 6x + 2  ✅    │
  └────────────────────────┘
```

**Step 6 — VERIFY using rules:**
```
  d/dx(3x²) = 3 · d/dx(x²) = 3 · 2x = 6x     (constant multiple + power rule)
  d/dx(2x)  = 2 · d/dx(x¹) = 2 · 1 = 2         (power rule: 1·x⁰ = 1)
  
  Sum rule: f'(x) = 6x + 2  ✅
```

---

## 🧮 P2: Power Rule Derivatives

> 📘 Theory: [Ch 3 — Derivative Formulas](./Essence_of_Calculus_THEORY.md#chapter-3--derivative-formulas-through-geometry) | ⬆️ [Problem Index](#-problem-index)

### The Power Rule — Explained Like You're 5:
```
  d/dx(xⁿ) = n · xⁿ⁻¹
  
  RECIPE:
  1. Take the POWER (the little number on top)
  2. BRING IT DOWN as a multiplier in front
  3. SUBTRACT 1 from the power
  
  Example: x⁷ → the power is 7
           Bring 7 down: 7 · x^(something)
           Subtract 1 from power: 7-1 = 6
           Answer: 7x⁶
```

### (a) d/dx(x⁷)
```
  The power is 7.
  Bring it down: 7 × x^(?)
  New power = 7 − 1 = 6
  
  Answer: 7x⁶  ✅
```

### (b) d/dx(4x³ − 2x² + 5x − 1)

> **Rule needed:** Differentiate each term SEPARATELY (sum rule), and constant multipliers stay.

```
  Term 1: d/dx(4x³)
    The 4 is a constant multiplier — it stays.
    d/dx(x³) = 3x² (power rule: bring 3 down, subtract 1)
    So: 4 × 3x² = 12x²
  
  Term 2: d/dx(−2x²)
    The −2 stays.
    d/dx(x²) = 2x
    So: −2 × 2x = −4x
  
  Term 3: d/dx(5x)
    5x = 5x¹ (x to the power 1)
    d/dx(x¹) = 1·x⁰ = 1  (because x⁰ = 1 for any x)
    So: 5 × 1 = 5
  
  Term 4: d/dx(−1)
    −1 is a CONSTANT (no x involved)
    The derivative of ANY constant = 0  (constants don't change!)
    So: 0
  
  PUT IT ALL TOGETHER:
  f'(x) = 12x² − 4x + 5 + 0 = 12x² − 4x + 5  ✅
```

### (c) d/dx(√x)

> **Key insight:** √x is the same as x^(1/2). The power rule works for fractions too!

```
  Step 1: Rewrite √x as a power of x.
    √x = x^(1/2)
    
    WHY? Because √x means "what number squared gives x?"
    And x^(1/2) × x^(1/2) = x^(1/2 + 1/2) = x¹ = x  ✅
  
  Step 2: Apply power rule with n = 1/2.
    d/dx(x^(1/2)) = (1/2) · x^(1/2 − 1)
    
    What is 1/2 − 1?
    1/2 − 1 = 1/2 − 2/2 = −1/2
    
    So: (1/2) · x^(−1/2)
  
  Step 3: Simplify x^(−1/2).
    x^(−1/2) means 1/x^(1/2) = 1/√x
    
    WHY? Negative exponent = "flip to denominator"
    x^(−n) = 1/xⁿ  (always!)
    
  FINAL ANSWER:
    d/dx(√x) = (1/2) · (1/√x) = 1/(2√x)  ✅
    
  CHECK with a number: At x=4, √4=2, derivative = 1/(2·2) = 0.25
  Meaning: when x=4, the √x curve has slope 0.25 (rising gently).
```

### (d) d/dx(1/x³)

> **Key insight:** 1/x³ = x^(−3). Negative exponents = power rule with negative n.

```
  Step 1: Rewrite 1/x³ as a power.
    1/x³ = x^(−3)
    
    WHY? 1/xⁿ = x^(−n)  (this is the definition of negative exponents)
  
  Step 2: Apply power rule with n = −3.
    d/dx(x^(−3)) = (−3) · x^(−3 − 1)
    
    What is −3 − 1? It's −4.
    
    So: −3 · x^(−4)
  
  Step 3: Rewrite in fraction form (optional, for clarity).
    −3 · x^(−4) = −3/x⁴
    
  FINAL ANSWER: −3/x⁴  ✅
```

---

## 🧮 P3: Trig Derivatives

> 📘 Theory: [Ch 3](./Essence_of_Calculus_THEORY.md#chapter-3--derivative-formulas-through-geometry) | ⬆️ [Problem Index](#-problem-index)

### Rules You Need (memorize these 2):
```
  d/dx(sin x) = cos x       "sine becomes cosine"
  d/dx(cos x) = −sin x      "cosine becomes NEGATIVE sine"
```

### (a) d/dx[3sin(x) + cos(x)]

```
  Step 1: Use SUM RULE — differentiate each piece separately.
  
  Piece 1: d/dx(3sin(x))
    The 3 is a constant multiplier — it stays.
    d/dx(sin x) = cos x   (trig rule)
    So: 3 · cos(x) = 3cos(x)
  
  Piece 2: d/dx(cos(x))
    d/dx(cos x) = −sin x   (trig rule — notice the MINUS!)
    So: −sin(x)
  
  Step 2: Combine.
    f'(x) = 3cos(x) + (−sin(x)) = 3cos(x) − sin(x)  ✅
```

### (b) d/dx(sin²(x))

> **Why is this harder?** sin²(x) means [sin(x)]². It's a COMPOSITION: the squaring function is WRAPPED AROUND the sin function. We need the **Chain Rule**.

```
  Step 1: Identify the OUTER and INNER functions.
    sin²(x) = [sin(x)]²
    
    OUTER function: (something)²    — "squaring"
    INNER function: sin(x)          — "the thing being squared"
    
    Think of it as: let u = sin(x), then f = u²
  
  Step 2: Apply Chain Rule.
    Chain Rule: d/dx[f(g(x))] = f'(g(x)) · g'(x)
    
    f'(outer) = derivative of u² = 2u = 2·sin(x)
    g'(inner) = derivative of sin(x) = cos(x)
    
    Multiply: 2·sin(x) · cos(x) = 2sin(x)cos(x)
  
  Step 3: Simplify (optional).
    There's a trig identity: 2sin(x)cos(x) = sin(2x)
    
    WHY? This is the "double angle formula" for sine.
    
  FINAL ANSWER: 2sin(x)cos(x) = sin(2x)  ✅
```

### (c) d/dx(tan(x))

> **Strategy:** Rewrite tan as sin/cos and use the **Quotient Rule**.

```
  Step 1: Rewrite tan(x).
    tan(x) = sin(x) / cos(x)
    
    (This is the DEFINITION of tangent)
  
  Step 2: Apply Quotient Rule.
    Quotient Rule: d/dx(f/g) = (f'·g − f·g') / g²
    
    Here: f = sin(x),  g = cos(x)
          f' = cos(x),  g' = −sin(x)
    
    Numerator = f'·g − f·g'
              = cos(x)·cos(x) − sin(x)·(−sin(x))
              = cos²(x) − (−sin²(x))
              = cos²(x) + sin²(x)
              
    ┌─────────────────────────────────────────────┐
    │  cos²(x) + sin²(x) = 1                      │
    │  (This is the PYTHAGOREAN IDENTITY —        │
    │   the most fundamental trig identity!)      │
    └─────────────────────────────────────────────┘
              
    Denominator = g² = [cos(x)]² = cos²(x)
    
  Step 3: Combine.
    d/dx(tan x) = 1 / cos²(x) = sec²(x)  ✅
    
    (Because sec(x) = 1/cos(x), so sec²(x) = 1/cos²(x))
```

---

## 🧮 P4: Product Rule

> 📘 Theory: [Ch 4](./Essence_of_Calculus_THEORY.md#chapter-4--chain-rule--product-rule) | ⬆️ [Problem Index](#-problem-index)

### The Product Rule — Explained Like You're 5:
```
  When you have TWO functions MULTIPLIED together:
  
  d/dx(f · g) = f' · g  +  f · g'
  
  In words:
  "Derivative of LEFT × RIGHT untouched"
    PLUS
  "LEFT untouched × Derivative of RIGHT"
  
  🍎 Kid version: If you have a rectangle with sides f and g,
  and both sides are changing, the total area change comes from
  the TOP strip (f changes, g stays) + RIGHT strip (g changes, f stays).
```

### (a) d/dx(x² · eˣ)

```
  Step 1: Identify f and g.
    f(x) = x²       g(x) = eˣ
  
  Step 2: Find f' and g' SEPARATELY.
    f'(x) = d/dx(x²) = 2x        (power rule: bring 2 down, subtract 1)
    g'(x) = d/dx(eˣ) = eˣ         (special rule: eˣ is its own derivative!)
  
  Step 3: Plug into the product rule formula.
    d/dx(f · g) = f' · g + f · g'
                = (2x)(eˣ) + (x²)(eˣ)
                = 2x·eˣ + x²·eˣ
  
  Step 4: Factor out common terms (optional simplification).
    Both terms have eˣ, so factor it out:
    = eˣ · (2x + x²)
    = eˣ · x · (2 + x)        (factor x from 2x+x²)
  
  FINAL: eˣ(x² + 2x)  or  x·eˣ(x + 2)  ✅
```

### (b) d/dx(x · sin(x) · cos(x))   — THREE functions multiplied!

> **Strategy:** Group two of them together, then apply product rule TWICE.

```
  Step 1: Group as (x · sin(x)) · cos(x).
    Let A(x) = x · sin(x)       (we'll need A' later)
    Let B(x) = cos(x)
    
    So our function = A · B
  
  Step 2: Find A'(x) using product rule on x · sin(x).
    f = x,     g = sin(x)
    f' = 1,    g' = cos(x)
    
    A'(x) = f'·g + f·g'
          = 1·sin(x) + x·cos(x)
          = sin(x) + x·cos(x)
  
  Step 3: Find B'(x).
    B'(x) = d/dx(cos(x)) = −sin(x)
  
  Step 4: Apply product rule to A · B.
    d/dx(A · B) = A' · B + A · B'
    
    = [sin(x) + x·cos(x)] · cos(x) + [x·sin(x)] · [−sin(x)]
    
  Step 5: EXPAND carefully.
    First part: [sin(x) + x·cos(x)] · cos(x)
      = sin(x)·cos(x) + x·cos(x)·cos(x)
      = sin(x)·cos(x) + x·cos²(x)
    
    Second part: x·sin(x)·(−sin(x))
      = −x·sin²(x)
    
  Step 6: Combine all terms.
    = sin(x)·cos(x) + x·cos²(x) − x·sin²(x)
    
  Step 7: Simplify (optional, using trig identities).
    cos²(x) − sin²(x) = cos(2x)    (double angle identity)
    
    = sin(x)cos(x) + x·[cos²(x) − sin²(x)]
    = sin(x)cos(x) + x·cos(2x)
    
    Also: sin(x)cos(x) = sin(2x)/2
    
  FINAL: sin(x)cos(x) + x·cos(2x)  ✅
```

---

## 🧮 P5: Chain Rule

> 📘 Theory: [Ch 4](./Essence_of_Calculus_THEORY.md#chapter-4--chain-rule--product-rule) | ⬆️ [Problem Index](#-problem-index)

### The Chain Rule — Explained Like You're 5:
```
  When one function is INSIDE another (like sin(x²) or e^(3x)):
  
  d/dx[f(g(x))] = f'(g(x)) · g'(x)
  
  RECIPE:
  1. OUTER function: Differentiate it, but leave the inside UNTOUCHED
  2. INNER function: Then multiply by the derivative of the inside
  
  🍎 Kid version: Like peeling an onion — start from the outside layer,
  peel it (differentiate), then peel the next layer, and MULTIPLY.
```

### (a) d/dx[sin(3x)]

```
  Step 1: Identify outer and inner.
    OUTER: sin(□)     — the sine function wrapping around something
    INNER: 3x         — the thing being wrapped (□ = 3x)
  
  Step 2: Differentiate the OUTER, keep inner untouched.
    d/d□(sin(□)) = cos(□)
    So: cos(3x)     ← we kept 3x inside, didn't touch it!
  
  Step 3: Multiply by derivative of INNER.
    d/dx(3x) = 3
  
  Step 4: Multiply outer' × inner'.
    = cos(3x) × 3 = 3cos(3x)  ✅
```

### (b) d/dx[e^(x²)]

```
  OUTER: e^(□)      INNER: x²
  
  Outer derivative: d/d□(e^□) = e^□ → e^(x²)  (eˣ is its own derivative!)
  Inner derivative: d/dx(x²) = 2x
  
  Multiply: e^(x²) × 2x = 2x · e^(x²)  ✅
```

### (c) d/dx[ln(x² + 1)]

```
  OUTER: ln(□)      INNER: x² + 1
  
  Outer derivative: d/d□(ln □) = 1/□ → 1/(x² + 1)
  Inner derivative: d/dx(x² + 1) = 2x + 0 = 2x
  
  Multiply: [1/(x²+1)] × 2x = 2x/(x² + 1)  ✅
```

### (d) d/dx[(2x + 1)⁵]

```
  OUTER: (□)⁵       INNER: 2x + 1
  
  Outer derivative: d/d□(□⁵) = 5□⁴ → 5(2x+1)⁴
  Inner derivative: d/dx(2x+1) = 2
  
  Multiply: 5(2x+1)⁴ × 2 = 10(2x+1)⁴  ✅
```

### BONUS: Triple-nested d/dx[sin(e^(3x))]

```
  Three layers!
  OUTERMOST: sin(□)    MIDDLE: e^(□)    INNERMOST: 3x
  
  Layer 1 (peel outer): d/d□(sin □) = cos □ → cos(e^(3x))
  Layer 2 (peel middle): d/d□(e^□) = e^□ → × e^(3x)
  Layer 3 (peel inner):  d/dx(3x) = 3 → × 3
  
  MULTIPLY ALL LAYERS:
  = cos(e^(3x)) × e^(3x) × 3 = 3 · e^(3x) · cos(e^(3x))  ✅
```

---

## 🧮 P6: Exponential Derivatives

> 📘 Theory: [Ch 5 — Euler's e](./Essence_of_Calculus_THEORY.md#chapter-5--eulers-number-e) | ⬆️ [Problem Index](#-problem-index)

### Rules You Need:
```
  d/dx(eˣ) = eˣ             ← eˣ is its own derivative! (the SPECIAL property of e)
  d/dx(aˣ) = aˣ · ln(a)     ← for any other base a, you get an extra ln(a) factor
  d/dx(c·f) = c · f'        ← constant multipliers pass through
```

### (a) d/dx(5eˣ)
```
  The 5 is a constant — it stays.
  d/dx(eˣ) = eˣ
  
  Answer: 5 · eˣ = 5eˣ  ✅
```

### (b) d/dx(2ˣ)
```
  This is aˣ where a = 2.
  d/dx(aˣ) = aˣ · ln(a)
  
  d/dx(2ˣ) = 2ˣ · ln(2)
  
  ln(2) ≈ 0.693 (a constant — the natural log of 2)
  
  Answer: 2ˣ · ln(2) ≈ 0.693 · 2ˣ  ✅
  
  Meaning: 2ˣ grows at about 69.3% of its current value per unit x.
```

### (c) d/dx[e^(−x²/2)]
```
  This needs the CHAIN RULE: eˣ is wrapped around −x²/2.
  
  OUTER: e^(□)          INNER: −x²/2
  
  Step 1: Outer derivative.
    d/d□(e^□) = e^□ → e^(−x²/2)
  
  Step 2: Inner derivative.
    d/dx(−x²/2) = −(1/2) · d/dx(x²) = −(1/2) · 2x = −x
    
    Detail: −x²/2 = (−1/2) · x²
    Constant −1/2 stays, d/dx(x²) = 2x
    So: (−1/2)(2x) = −x
  
  Step 3: Multiply.
    e^(−x²/2) × (−x) = −x · e^(−x²/2)  ✅
  
  🤖 AI/ML note: e^(−x²/2) is the Gaussian/Normal bell curve shape!
     Its derivative = −x · e^(−x²/2) tells us:
     - At x=0: derivative = 0 (peak of the bell, slope is flat)
     - At x>0: derivative < 0 (curve going downhill to the right)
     - At x<0: derivative > 0 (curve going uphill from the left)
```

### (d) d/dx(x · eˣ)
```
  Two functions MULTIPLIED → PRODUCT RULE!
  
  f = x,     g = eˣ
  f' = 1,    g' = eˣ
  
  d/dx(x·eˣ) = f'·g + f·g'
              = 1·eˣ + x·eˣ
              = eˣ + x·eˣ
              = eˣ(1 + x)  ✅  (factor out eˣ)
```

---

## 🧮 P7: Implicit Differentiation

> 📘 Theory: [Ch 6](./Essence_of_Calculus_THEORY.md#chapter-6--implicit-differentiation) | ⬆️ [Problem Index](#-problem-index)

### When Do You Use This?
```
  When x and y are MIXED together in an equation and you CAN'T
  easily solve for y. Example: x² + y² = 25 (circle).
  
  THE TRICK: Treat y as a function of x (even though you can't
  write it explicitly). Whenever you differentiate a y term,
  multiply by dy/dx (because of the chain rule!).
  
  WHY dy/dx? Because y depends on x:
    d/dx(y²) = 2y · (dy/dx)    ← chain rule! outer=², inner=y(x)
    d/dx(x²) = 2x              ← normal, no extra factor needed
```

### (a) Find dy/dx for x² + y² = 25

```
  Step 1: Differentiate BOTH SIDES with respect to x.
  
    LEFT SIDE: d/dx(x² + y²)
    
      d/dx(x²) = 2x                     ← straightforward power rule
      d/dx(y²) = 2y · (dy/dx)           ← CHAIN RULE! y is a function of x
        WHY? Think of it as d/dx([something]²) = 2·[something]·[something]'
        Here [something] = y, and [something]' = dy/dx
    
    RIGHT SIDE: d/dx(25)
      = 0                               ← derivative of a constant = 0
  
  Step 2: Write the equation.
    2x + 2y · (dy/dx) = 0
  
  Step 3: Solve for dy/dx.
    2y · (dy/dx) = −2x            ← subtract 2x from both sides
    dy/dx = −2x / (2y)            ← divide both sides by 2y
    dy/dx = −x/y                  ← simplify (the 2's cancel)
  
  ┌─────────────────────────────────────────────┐
  │  dy/dx = −x/y  ✅                           │
  │                                             │
  │  Check at (3,4) on the circle x²+y²=25:     │
  │  dy/dx = −3/4 = −0.75                       │
  │  The tangent line slopes downward-right ✅  │
  │                                             │
  │  Check at (0,5) — top of circle:            │
  │  dy/dx = −0/5 = 0                           │
  │  Tangent is HORIZONTAL at the top ✅        │
  └─────────────────────────────────────────────┘
```

### (b) Find dy/dx for x·y + y² = 3

```
  Step 1: Differentiate both sides w.r.t. x.
  
    d/dx(x·y): This is a PRODUCT of x and y, so use PRODUCT RULE!
      f = x,    g = y
      f' = 1,   g' = dy/dx
      d/dx(x·y) = 1·y + x·(dy/dx) = y + x·(dy/dx)
    
    d/dx(y²) = 2y · (dy/dx)       (chain rule, same as before)
    
    d/dx(3) = 0
  
  Step 2: Write the full equation.
    y + x·(dy/dx) + 2y·(dy/dx) = 0
  
  Step 3: Collect all (dy/dx) terms on one side.
    x·(dy/dx) + 2y·(dy/dx) = −y
    
    Factor out (dy/dx):
    (dy/dx) · (x + 2y) = −y
  
  Step 4: Solve.
    dy/dx = −y / (x + 2y)  ✅
```

---

## 🧮 P8: Limits & L'Hôpital's Rule

> 📘 Theory: [Ch 7](./Essence_of_Calculus_THEORY.md#chapter-7--limits-and-lhôpitals-rule) | ⬆️ [Problem Index](#-problem-index)

### L'Hôpital's Rule — When and How:
```
  WHEN: You try to evaluate a limit and get 0/0 or ∞/∞
  (These are called "indeterminate forms" — you can't tell the answer)
  
  HOW: Differentiate the TOP and BOTTOM SEPARATELY, then re-evaluate.
  
  lim f(x)/g(x) = lim f'(x)/g'(x)
  x→a             x→a
  
  ⚠️ This is NOT the quotient rule! You differentiate top and bottom
     INDEPENDENTLY, not as a fraction.
```

### (a) lim(x→0) sin(x)/x

```
  Step 1: Try direct substitution.
    sin(0)/0 = 0/0  ← INDETERMINATE! Can't determine the answer yet.
  
  Step 2: Apply L'Hôpital's Rule.
    Differentiate TOP: d/dx(sin x) = cos x
    Differentiate BOTTOM: d/dx(x) = 1
    
    New limit: lim(x→0) cos(x)/1
  
  Step 3: Evaluate the new limit.
    cos(0)/1 = 1/1 = 1
    
  ANSWER: 1  ✅
  
  🍎 This is one of the most famous limits in calculus!
     "sin(x)/x approaches 1 as x gets tiny"
```

### (b) lim(x→∞) x/eˣ

```
  Step 1: Try direct substitution.
    ∞/e^∞ = ∞/∞  ← INDETERMINATE!
  
  Step 2: Apply L'Hôpital's Rule.
    TOP: d/dx(x) = 1
    BOTTOM: d/dx(eˣ) = eˣ
    
    New limit: lim(x→∞) 1/eˣ
  
  Step 3: Evaluate.
    As x→∞, eˣ→∞, so 1/eˣ → 1/∞ = 0
    
  ANSWER: 0  ✅
  
  Meaning: eˣ grows SO much faster than x that the ratio goes to zero.
  Exponential ALWAYS beats polynomial growth!
```

### (c) lim(x→0) (eˣ − 1 − x)/x²

```
  Step 1: Try direct substitution.
    (e⁰ − 1 − 0)/0² = (1 − 1 − 0)/0 = 0/0  ← INDETERMINATE!
  
  Step 2: Apply L'Hôpital's FIRST time.
    TOP: d/dx(eˣ − 1 − x) = eˣ − 0 − 1 = eˣ − 1
    BOTTOM: d/dx(x²) = 2x
    
    New limit: lim(x→0) (eˣ − 1)/(2x)
  
  Step 3: Try substitution again.
    (e⁰ − 1)/(2·0) = (1−1)/0 = 0/0  ← STILL indeterminate!
  
  Step 4: Apply L'Hôpital's a SECOND time (this is allowed!).
    TOP: d/dx(eˣ − 1) = eˣ
    BOTTOM: d/dx(2x) = 2
    
    New limit: lim(x→0) eˣ/2
  
  Step 5: NOW substitute.
    e⁰/2 = 1/2
    
  ANSWER: 1/2  ✅
```

---

## 🧮 P9: Definite Integrals

> 📘 Theory: [Ch 8 — Integration & FTC](./Essence_of_Calculus_THEORY.md#chapter-8--integration-and-the-fundamental-theorem) | ⬆️ [Problem Index](#-problem-index)

### How Definite Integrals Work:
```
  ∫ₐᵇ f(x) dx = "area under f(x) from x=a to x=b"
  
  RECIPE (using Fundamental Theorem of Calculus):
  1. Find F(x) — the ANTIDERIVATIVE of f(x)
     (F is a function whose derivative = f)
  2. Compute F(b) − F(a)
     (evaluate at upper limit MINUS lower limit)
  
  That's it! The area = F(b) − F(a).
```

### (a) ∫₀³ x² dx

```
  Step 1: Find the antiderivative of x².
    We need F(x) such that F'(x) = x².
    
    Using the REVERSE power rule:
    ∫xⁿ dx = xⁿ⁺¹/(n+1)
    
    Here n=2, so: ∫x² dx = x²⁺¹/(2+1) = x³/3
    
    F(x) = x³/3
    
    VERIFY: d/dx(x³/3) = (1/3)·3x² = x²  ✅  (it IS the antiderivative)
  
  Step 2: Apply FTC: F(b) − F(a).
    Upper limit b = 3:  F(3) = 3³/3 = 27/3 = 9
    Lower limit a = 0:  F(0) = 0³/3 = 0/3 = 0
    
  Step 3: Subtract.
    ∫₀³ x² dx = F(3) − F(0) = 9 − 0 = 9  ✅
    
  Meaning: The area under the curve y=x² from x=0 to x=3 is exactly 9.
```

### (b) ∫₀^π sin(x) dx

```
  Step 1: Antiderivative of sin(x).
    ∫sin(x) dx = −cos(x)
    
    WHY negative? Because d/dx(−cos x) = −(−sin x) = sin x  ✅
  
  Step 2: Evaluate at limits.
    F(x) = −cos(x)
    
    F(π) = −cos(π)
    
    What is cos(π)? cos(180°) = −1
    So F(π) = −(−1) = 1
    
    F(0) = −cos(0) 
    
    What is cos(0)? cos(0°) = 1
    So F(0) = −(1) = −1
  
  Step 3: Subtract.
    ∫₀^π sin(x) dx = F(π) − F(0) = 1 − (−1) = 1 + 1 = 2  ✅
    
  Meaning: The area under one full arch of sin(x) = 2.
```

### (c) ∫₁ᵉ (1/x) dx

```
  Step 1: Antiderivative of 1/x.
    ∫(1/x) dx = ln|x|     (natural logarithm of |x|)
    
    ⚠️ You CANNOT use the power rule here!
    1/x = x⁻¹, and ∫x⁻¹ dx would give x⁰/0 = undefined!
    This is the ONE EXCEPTION: 1/x has the special antiderivative ln|x|.
    
    VERIFY: d/dx(ln x) = 1/x  ✅
  
  Step 2: Evaluate at limits.
    F(x) = ln|x|
    
    F(e) = ln(e) = 1      (because e¹ = e, so ln(e) = 1)
    F(1) = ln(1) = 0      (because e⁰ = 1, so ln(1) = 0)
  
  Step 3: Subtract.
    ∫₁ᵉ (1/x) dx = ln(e) − ln(1) = 1 − 0 = 1  ✅
```

---

## 🧮 P10: Antiderivatives & Indefinite Integrals

> 📘 Theory: [Ch 8](./Essence_of_Calculus_THEORY.md#chapter-8--integration-and-the-fundamental-theorem) | ⬆️ [Problem Index](#-problem-index)

### What's an Antiderivative?
```
  F(x) is the antiderivative of f(x) if F'(x) = f(x).
  
  It's the REVERSE of differentiation:
    If derivative of x³ is 3x², then antiderivative of 3x² is x³.
  
  +C: We always add "+C" because the derivative of any constant is 0.
  So x³, x³+5, x³−17 ALL have derivative 3x².
  The "+C" accounts for this unknown constant.
```

### (a) ∫6x² dx
```
  Reverse Power Rule: ∫xⁿ dx = xⁿ⁺¹/(n+1) + C
  
  Step 1: The 6 is a constant — it passes through the integral.
    = 6 · ∫x² dx
  
  Step 2: Apply reverse power rule with n=2.
    ∫x² dx = x²⁺¹/(2+1) = x³/3
  
  Step 3: Multiply by 6.
    = 6 · x³/3 = (6/3)·x³ = 2x³
  
  Step 4: Add +C.
    = 2x³ + C  ✅
  
  VERIFY: d/dx(2x³+C) = 2·3x² + 0 = 6x²  ✅
```

### (b) ∫(3cos x + eˣ) dx
```
  Step 1: Split into two separate integrals (sum rule).
    = ∫3cos x dx + ∫eˣ dx
  
  Step 2: First integral.
    ∫3cos x dx = 3 · ∫cos x dx = 3 · sin(x)
    (Because d/dx(sin x) = cos x, so antiderivative of cos x = sin x)
  
  Step 3: Second integral.
    ∫eˣ dx = eˣ
    (Because d/dx(eˣ) = eˣ, so eˣ is its own antiderivative too!)
  
  Step 4: Combine + add C.
    = 3sin(x) + eˣ + C  ✅
  
  VERIFY: d/dx(3sin x + eˣ + C) = 3cos x + eˣ + 0 = 3cos x + eˣ  ✅
```

### (c) ∫(1/x) dx
```
  ⚠️ SPECIAL CASE: Cannot use power rule (would give division by 0).
  
  ∫x⁻¹ dx ≠ x⁰/0  (UNDEFINED! Power rule breaks here!)
  
  Instead, use the special rule:
  ∫(1/x) dx = ln|x| + C
  
  The absolute value |x| handles negative x values.
  
  VERIFY: d/dx(ln|x| + C) = 1/x + 0 = 1/x  ✅
```

---

## 🧮 P11: Higher Order Derivatives

> 📘 Theory: [Ch 10](./Essence_of_Calculus_THEORY.md#chapter-10--higher-order-derivatives) | ⬆️ [Problem Index](#-problem-index)

### What Are Higher Derivatives?
```
  f'(x)  = first derivative  = SLOPE (how fast f changes)
  f''(x) = second derivative = how fast the SLOPE changes
           = ACCELERATION     = tells if curve bends UP or DOWN
  
  f'' > 0 → curve bends UPWARD   (concave up, like a bowl ∪)
  f'' < 0 → curve bends DOWNWARD (concave down, like a hill ∩)
  f'' = 0 → possible inflection point (curve changes direction of bending)
```

### Problem: f(x) = x⁴ − 6x² + 9. Find f', f'', and classify critical points.

```
  Step 1: First derivative f'(x).
    d/dx(x⁴) = 4x³                (power rule: n=4)
    d/dx(−6x²) = −6·2x = −12x    (constant × power rule)
    d/dx(9) = 0                    (constant)
    
    f'(x) = 4x³ − 12x
  
  Step 2: Critical points — set f'(x) = 0.
    4x³ − 12x = 0
    
    Factor out 4x:
    4x(x² − 3) = 0
    
    This equals zero when:
      4x = 0  →  x = 0
      OR  x² − 3 = 0  →  x² = 3  →  x = ±√3 ≈ ±1.732
    
    Critical points: x = −√3, 0, √3
  
  Step 3: Second derivative f''(x).
    f'(x) = 4x³ − 12x
    
    d/dx(4x³) = 4·3x² = 12x²
    d/dx(−12x) = −12
    
    f''(x) = 12x² − 12
  
  Step 4: Classify each critical point using f''.
  
    At x = 0:
      f''(0) = 12(0)² − 12 = 0 − 12 = −12
      f'' < 0 → concave DOWN → LOCAL MAXIMUM ✅
      f(0) = 0 − 0 + 9 = 9  (the max value is 9)
    
    At x = √3:
      f''(√3) = 12(√3)² − 12 = 12·3 − 12 = 36 − 12 = 24
      f'' > 0 → concave UP → LOCAL MINIMUM ✅
      f(√3) = (√3)⁴ − 6(√3)² + 9 = 9 − 18 + 9 = 0
    
    At x = −√3:
      f''(−√3) = 12(−√3)² − 12 = 12·3 − 12 = 24
      f'' > 0 → concave UP → LOCAL MINIMUM ✅
      f(−√3) = 0  (same as +√3 by symmetry)
  
  SUMMARY:
    (−√3, 0) = local minimum
    (0, 9) = local maximum
    (√3, 0) = local minimum
    
       f(x)
      9 │    ·──── local max
        │   ╱ ╲
        │  ╱   ╲
      0 ·╱─────╲·── local mins
       -√3   0   √3
```

---

## 🧮 P12: Taylor Series Expansion

> 📘 Theory: [Ch 11](./Essence_of_Calculus_THEORY.md#chapter-11--taylor-series) | ⬆️ [Problem Index](#-problem-index)

### What IS a Taylor Series?
```
  A way to write ANY function as an (infinite) polynomial!
  
  Formula (centered at a=0, called "Maclaurin series"):
  
  f(x) = f(0) + f'(0)·x + f''(0)·x²/2! + f'''(0)·x³/3! + ...
  
  RECIPE for each term:
    nth term = [nth derivative evaluated at 0] × xⁿ / n!
  
  n! means "n factorial":
    0! = 1,  1! = 1,  2! = 2,  3! = 6,  4! = 24,  5! = 120
```

### (a) Find 4th-degree Maclaurin polynomial for sin(x)

```
  We need: f(0), f'(0), f''(0), f'''(0), f⁴(0)
  
  Step 1: Compute successive derivatives of sin(x).
    f(x) = sin(x)       →  f(0) = sin(0) = 0
    f'(x) = cos(x)      →  f'(0) = cos(0) = 1
    f''(x) = −sin(x)    →  f''(0) = −sin(0) = 0
    f'''(x) = −cos(x)   →  f'''(0) = −cos(0) = −1
    f⁴(x) = sin(x)      →  f⁴(0) = sin(0) = 0
    
    Notice the PATTERN: 0, 1, 0, −1, 0, 1, 0, −1, ... (repeats!)
  
  Step 2: Build each term.
    Term 0: f(0)·x⁰/0!    = 0·1/1      = 0        (nothing)
    Term 1: f'(0)·x¹/1!   = 1·x/1      = x        ← FIRST term!
    Term 2: f''(0)·x²/2!  = 0·x²/2     = 0        (nothing)
    Term 3: f'''(0)·x³/3! = (−1)·x³/6  = −x³/6   ← SECOND term!
    Term 4: f⁴(0)·x⁴/4!  = 0·x⁴/24    = 0        (nothing)
  
  Step 3: Add them up.
    P₄(x) = 0 + x + 0 + (−x³/6) + 0 = x − x³/6
    
  FINAL: sin(x) ≈ x − x³/6  ✅  (for x near 0)
  
  Step 4: TEST — how good is this?
    sin(0.1) using our formula: 0.1 − (0.1)³/6 = 0.1 − 0.001/6
                                = 0.1 − 0.000167 = 0.099833
    
    Actual sin(0.1) = 0.099833...  ← AMAZINGLY close! 6 decimal places!
```

### (b) Maclaurin for 1/(1−x)

```
  f(x) = (1−x)⁻¹
  
  Step 1: Derivatives (using chain rule each time).
    f(x) = (1−x)⁻¹           → f(0) = 1
    f'(x) = (1−x)⁻²          → f'(0) = 1
    f''(x) = 2(1−x)⁻³        → f''(0) = 2
    f'''(x) = 6(1−x)⁻⁴       → f'''(0) = 6
    f⁴(x) = 24(1−x)⁻⁵        → f⁴(0) = 24
    
    Pattern: f⁽ⁿ⁾(0) = n!
  
  Step 2: Build terms.
    Term 0: 1·x⁰/0!  = 1/1  = 1
    Term 1: 1·x¹/1!  = x/1  = x
    Term 2: 2·x²/2!  = 2x²/2 = x²
    Term 3: 6·x³/3!  = 6x³/6 = x³
    Term 4: 24·x⁴/4! = 24x⁴/24 = x⁴
  
  FINAL: 1/(1−x) ≈ 1 + x + x² + x³ + x⁴  ✅
  
  This is the GEOMETRIC SERIES! Only works for |x| < 1.
```

---

## 🧮 P13: Taylor Series Error Bound

> 📘 Theory: [Ch 11](./Essence_of_Calculus_THEORY.md#chapter-11--taylor-series) | ⬆️ [Problem Index](#-problem-index)

### Problem: Estimate e^(0.1) using Taylor series. How close is it?

```
  The Taylor series for eˣ (centered at 0):
  eˣ = 1 + x + x²/2! + x³/3! + x⁴/4! + ...
  
  ┌────────────────────────────────────────────────────┐
  │  WHY does eˣ have such a simple series?            │
  │  Because ALL derivatives of eˣ are eˣ!             │
  │  And e⁰ = 1.                                       │
  │  So f⁽ⁿ⁾(0) = 1 for ALL n.                         │
  │  Each term = 1·xⁿ/n! = xⁿ/n!                       │
  └────────────────────────────────────────────────────┘
  
  Now plug in x = 0.1:
  
  1 term:  1                                    = 1.000000
  2 terms: 1 + 0.1                              = 1.100000
  3 terms: 1 + 0.1 + (0.1)²/2                  = 1 + 0.1 + 0.005  = 1.105000
  4 terms: 1 + 0.1 + 0.005 + (0.1)³/6          = 1.105 + 0.000167 = 1.105167
  5 terms: + (0.1)⁴/24                          = + 0.0000042      = 1.105171
  
  Actual: e^(0.1) = 1.105171...
  
  ERROR with 3 terms: |1.105000 − 1.105171| = 0.000171  (0.015% off)
  ERROR with 4 terms: |1.105167 − 1.105171| = 0.000004  (0.0004% off!)
  
  Just 4 terms give 5 decimal places of accuracy!
  
  🤖 AI/ML CONNECTION: Computers use Taylor-like approximations to compute
     exp(), sin(), cos(). When you call np.exp() in Python, truncated series
     + clever tricks are what run under the hood.
```

---

## 🧮 P14: Jacobian & Transformation View

> 📘 Theory: [Ch 12](./Essence_of_Calculus_THEORY.md#chapter-12--the-other-way-to-visualize-derivatives) | ⬆️ [Problem Index](#-problem-index)

### What IS a Jacobian?
```
  For a function f: ℝ² → ℝ² (takes 2 inputs, gives 2 outputs):
  
  f(x,y) = (f₁(x,y), f₂(x,y))
  
  The JACOBIAN is the matrix of ALL partial derivatives:
  
  J = [ ∂f₁/∂x    ∂f₁/∂y ]
      [ ∂f₂/∂x    ∂f₂/∂y ]
  
  ∂f₁/∂x = "how does f₁ change when x nudges?" (treat y as constant)
  ∂f₁/∂y = "how does f₁ change when y nudges?" (treat x as constant)
  
  |det(J)| = how much the transformation STRETCHES or SQUISHES area locally
```

### Problem: f(x,y) = (x² − y,  x + y²). Find J and det(J) at (1,1).

```
  Step 1: Identify f₁ and f₂.
    f₁(x,y) = x² − y       (first output)
    f₂(x,y) = x + y²       (second output)
  
  Step 2: Compute ALL FOUR partial derivatives.
  
    ∂f₁/∂x: differentiate x²−y with respect to x, treating y as constant.
      d/dx(x²) = 2x       (power rule on x)
      d/dx(−y) = 0          (y is treated as a constant!)
      ∂f₁/∂x = 2x
    
    ∂f₁/∂y: differentiate x²−y with respect to y, treating x as constant.
      d/dy(x²) = 0          (x² is a constant when we vary y!)
      d/dy(−y) = −1          (power rule: d/dy(y¹) = 1, with the minus)
      ∂f₁/∂y = −1
    
    ∂f₂/∂x: differentiate x+y² with respect to x.
      d/dx(x) = 1
      d/dx(y²) = 0          (y² is constant w.r.t. x)
      ∂f₂/∂x = 1
    
    ∂f₂/∂y: differentiate x+y² with respect to y.
      d/dy(x) = 0            (x is constant)
      d/dy(y²) = 2y          (power rule on y)
      ∂f₂/∂y = 2y
  
  Step 3: Write the Jacobian matrix (with variables).
    J = [ 2x    −1 ]
        [  1    2y ]
  
  Step 4: Evaluate at (x,y) = (1,1).
    J(1,1) = [ 2(1)    −1  ] = [ 2   −1 ]
             [  1     2(1) ]   [ 1    2 ]
  
  Step 5: Compute the determinant.
    det(J) = (2)(2) − (−1)(1)
           = 4 − (−1)
           = 4 + 1
           = 5
  
  ┌──────────────────────────────────────────────┐
  │  det(J) = 5  ✅                              │
  │                                              │
  │  |det(J)| = 5 → transformation STRETCHES     │
  │  areas by factor 5 near the point (1,1).     │
  │  det > 0 → orientation is PRESERVED.         │
  │                                              │
  │  🤖 AI/ML — Normalizing Flows:               │
  │  If old_density = 0.1 at a point,            │
  │  new_density = old_density / |det(J)|        │
  │             = 0.1 / 5 = 0.02                 │
  │  (Area stretched 5× → density shrinks 5×)    │
  └──────────────────────────────────────────────┘
```

---

> 🔗 **Theory explanations:** [← Theory Guide](./Essence_of_Calculus_THEORY.md)
>
> 🔗 **Master hub:** [← INDEX](./Essence_of_Calculus_INDEX.md)
>
> 🎓 **Created for:** ODS | ML
