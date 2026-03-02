# ∫ Essence of Calculus — Master Study Hub
### 🎓 ODS · Mathematics for AI/ML
> **Source:** [3Blue1Brown — Essence of Calculus](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr) by Grant Sanderson
> **Goal:** Feel like you could have INVENTED calculus yourself!
> **Philosophy:** Tiny nudges (dx) → big understanding 🧠

---

## 📂 Study Materials

| # | Document | What's Inside | Link |
|---|----------|--------------|------|
| 📘 | **Theory Guide** | All 12 chapters + 55 Q&A with full answers + AI/ML uses + diagrams | **[→ Theory Guide](./Essence_of_Calculus_THEORY.md)** |
| 🔢 | **Practice Problems** | 15+ solved problems — every step, rule, formula explained | **[→ Practice Guide](./Essence_of_Calculus_PRACTICE.md)** |
| 📋 | **This File (INDEX)** | Hub, notation, formula cheat sheet, concept map, mnemonics | **You are here!** |

```
     ┌──────────────┐
     │  📋 INDEX    │  ← YOU ARE HERE
     └──────┬───────┘
    ┌───────┴───────┐
    ▼               ▼
 ┌────────────┐  ┌────────────┐
 │ 📘 THEORY  │◄►│🔢 PRACTICE │
 │ Concepts + │  │ Problems + │
 │ Q&A + AI/ML│  │Step-by-step│
 └────────────┘  └────────────┘
```

---

## 🗺️ Master Table of Contents

| Ch# | Topic | Theory | Practice | AI/ML Use |
|-----|-------|--------|----------|-----------|
| 1 | Essence of Calculus (Overview) | [📘](./Essence_of_Calculus_THEORY.md#chapter-1--the-essence-of-calculus) | — | Foundation |
| 2 | The Paradox of the Derivative | [📘](./Essence_of_Calculus_THEORY.md#chapter-2--the-paradox-of-the-derivative) | [🔢 P1](./Essence_of_Calculus_PRACTICE.md#-p1-derivative-from-first-principles) | Gradient descent |
| 3 | Derivative Formulas (Geometry) | [📘](./Essence_of_Calculus_THEORY.md#chapter-3--derivative-formulas-through-geometry) | [🔢 P2-P3](./Essence_of_Calculus_PRACTICE.md#-p2-power-rule-derivatives) | Backprop |
| 4 | Chain Rule & Product Rule | [📘](./Essence_of_Calculus_THEORY.md#chapter-4--chain-rule--product-rule) | [🔢 P4-P5](./Essence_of_Calculus_PRACTICE.md#-p4-product-rule) | Backpropagation |
| 5 | Euler's Number e | [📘](./Essence_of_Calculus_THEORY.md#chapter-5--eulers-number-e) | [🔢 P6](./Essence_of_Calculus_PRACTICE.md#-p6-exponential-derivatives) | Softmax, decay |
| 6 | Implicit Differentiation | [📘](./Essence_of_Calculus_THEORY.md#chapter-6--implicit-differentiation) | [🔢 P7](./Essence_of_Calculus_PRACTICE.md#-p7-implicit-differentiation) | Constraints |
| 7 | Limits & L'Hôpital's Rule | [📘](./Essence_of_Calculus_THEORY.md#chapter-7--limits-and-lhôpitals-rule) | [🔢 P8](./Essence_of_Calculus_PRACTICE.md#-p8-limits--lhôpitals-rule) | Convergence |
| 8 | Integration & FTC | [📘](./Essence_of_Calculus_THEORY.md#chapter-8--integration-and-the-fundamental-theorem) | [🔢 P9-P10](./Essence_of_Calculus_PRACTICE.md#-p9-definite-integrals) | Expected value |
| 9 | Area vs Slope Connection | [📘](./Essence_of_Calculus_THEORY.md#chapter-9--what-does-area-have-to-do-with-slope) | — | Loss functions |
| 10 | Higher Order Derivatives | [📘](./Essence_of_Calculus_THEORY.md#chapter-10--higher-order-derivatives) | [🔢 P11](./Essence_of_Calculus_PRACTICE.md#-p11-higher-order-derivatives) | Hessian, Newton |
| 11 | Taylor Series | [📘](./Essence_of_Calculus_THEORY.md#chapter-11--taylor-series) | [🔢 P12-P13](./Essence_of_Calculus_PRACTICE.md#-p12-taylor-series-expansion) | Approximation |
| 12 | Derivatives as Transformations | [📘](./Essence_of_Calculus_THEORY.md#chapter-12--the-other-way-to-visualize-derivatives) | [🔢 P14](./Essence_of_Calculus_PRACTICE.md#-p14-jacobian--transformation-view) | Jacobian |

---

## 🔑 Notation Dictionary

| Symbol | Name | Meaning | Kid Analogy |
|--------|------|---------|-------------|
| `f(x)` | Function | Input→output machine | "Put x in, get y out" |
| `f'(x)` or `df/dx` | Derivative | Rate of change / slope | "How fast is it changing?" |
| `dx` | Tiny nudge | Infinitesimally small change in x | "A baby step in x" |
| `df` | Resulting nudge | Tiny change in f caused by dx | "How much did f wiggle?" |
| `∫ f(x)dx` | Integral | Accumulated area under curve | "Add up all the thin slices" |
| `∫ₐᵇ` | Definite integral | Area from x=a to x=b | "Area between two walls" |
| `F(x)` | Antiderivative | Function whose derivative = f(x) | "The undo of derivative" |
| `lim` | Limit | Value approached (never reached) | "Getting closer and closer" |
| `e ≈ 2.718` | Euler's number | Base where d/dx(eˣ)=eˣ | "The perfect growth rate" |
| `f''(x)` | 2nd derivative | Rate of change of the slope | "Is it speeding up or slowing?" |
| `Σ` | Summation | Add finitely many terms | "Big sigma = big addition" |
| `∞` | Infinity | Without bound | "Goes on forever" |

---

## 📋 FORMULA CHEAT SHEET

```
╔═══════════════════════════════════════════════════════════════════════╗
║  DERIVATIVE RULES                                                     ║
║  Power:      d/dx(xⁿ) = nxⁿ⁻¹                                         ║
║  Constant:   d/dx(c) = 0                                              ║
║  Sum:        d/dx(f+g) = f'+g'                                        ║
║  Product:    d/dx(fg) = f'g + fg'                                     ║
║  Quotient:   d/dx(f/g) = (f'g−fg')/g²                                 ║
║  Chain:      d/dx(f(g(x))) = f'(g(x))·g'(x)                           ║
║  Exponential: d/dx(eˣ) = eˣ    d/dx(aˣ) = aˣ·ln(a)                    ║
║  Trig:       d/dx(sin x) = cos x    d/dx(cos x) = −sin x              ║
║  Log:        d/dx(ln x) = 1/x                                         ║
║                                                                       ║
║  INTEGRATION (reverse of above)                                       ║
║  Power:      ∫xⁿ dx = xⁿ⁺¹/(n+1) + C     (n≠−1)                       ║
║  Exponential: ∫eˣ dx = eˣ + C                                         ║
║  Trig:       ∫cos x dx = sin x + C    ∫sin x dx = −cos x + C          ║
║  Log:        ∫(1/x) dx = ln|x| + C                                    ║
║                                                                       ║
║  FUNDAMENTAL THEOREM OF CALCULUS                                      ║
║  Part 1: d/dx[∫ₐˣ f(t)dt] = f(x)                                      ║
║  Part 2: ∫ₐᵇ f(x)dx = F(b)−F(a)  where F'=f                           ║
║                                                                       ║
║  TAYLOR SERIES (around a=0, "Maclaurin")                              ║
║  f(x) = f(0) + f'(0)x + f''(0)x²/2! + f'''(0)x³/3! + ...              ║
║  eˣ = 1 + x + x²/2! + x³/3! + ...                                     ║
║  sin x = x − x³/3! + x⁵/5! − ...                                      ║
║  cos x = 1 − x²/2! + x⁴/4! − ...                                      ║
║                                                                       ║
║  L'HÔPITAL'S RULE                                                     ║
║  If lim f/g = 0/0 or ∞/∞: lim f(x)/g(x) = lim f'(x)/g'(x)             ║
║                                                                       ║
║  KEY: Derivative=slope=rate  |  Integral=area=accumulation            ║
║       They are INVERSES of each other! (FTC)                          ║
╚═══════════════════════════════════════════════════════════════════════╝
```

---

## 🏆 CONCEPT MAP

```
                        ┌───────────────────────┐
                        │  CALCULUS = study of  │
                        │  CONTINUOUS CHANGE    │
                        └───────────┬───────────┘
                       ┌────────────┴────────────┐
                       ▼                         ▼
              ┌─────────────────┐      ┌─────────────────┐
              │  DERIVATIVES    │      │  INTEGRALS      │
              │  (Ch 2-7)       │◄────►│  (Ch 8-9)       │
              │  "Rate/Slope"   │ FTC  │  "Area/Accum."  │
              └────────┬────────┘      └────────┬────────┘
          ┌────────────┼──────────┐             │
          ▼            ▼          ▼             │
   ┌───────────┐ ┌──────────┐ ┌───────┐         │
   │Power Rule │ │Chain/Prod│ │Euler's│         │
   │Trig derivs│ │Rule(Ch4) │ │e(Ch5) │         │
   │(Ch 3)     │ └──────────┘ └───────┘         │
   └───────────┘                                │
                                                │
              ┌─────────────────────────────────┤
              ▼                                 ▼
       ┌───────────────┐              ┌─────────────────┐
       │ LIMITS (Ch 7) │              │ TAYLOR SERIES   │
       │ Foundation of │              │ (Ch 11)         │
       │ everything    │              │ "Polynomial     │
       └───────────────┘              │  approximation" │
                                      └─────────────────┘
```

---

## 🧩 MNEMONICS

| # | Mnemonic | Meaning | Link |
|---|----------|---------|------|
| 1 | **SNAIL** | Slope Nudge: A tiny Increase tells the Lean | [📘 Ch2](./Essence_of_Calculus_THEORY.md#chapter-2--the-paradox-of-the-derivative) |
| 2 | **POWER DOWN** | Power comes Down, exponent drops by 1 | [📘 Ch3](./Essence_of_Calculus_THEORY.md#chapter-3--derivative-formulas-through-geometry) |
| 3 | **LEFT-d-RIGHT** | Product rule: Left'·Right + Left·Right' | [📘 Ch4](./Essence_of_Calculus_THEORY.md#chapter-4--chain-rule--product-rule) |
| 4 | **ONION** | Chain rule: peel layers Outside·Inside' | [📘 Ch4](./Essence_of_Calculus_THEORY.md#chapter-4--chain-rule--product-rule) |
| 5 | **EULER TWIN** | eˣ is its own twin: derivative = itself | [📘 Ch5](./Essence_of_Calculus_THEORY.md#chapter-5--eulers-number-e) |
| 6 | **CLOSER** | Limit = value you get Closer to (never touch) | [📘 Ch7](./Essence_of_Calculus_THEORY.md#chapter-7--limits-and-lhôpitals-rule) |
| 7 | **UNDO** | Integration UNDOes differentiation (FTC!) | [📘 Ch8](./Essence_of_Calculus_THEORY.md#chapter-8--integration-and-the-fundamental-theorem) |
| 8 | **TAILOR** | Taylor series TAILORs a polynomial to fit any function | [📘 Ch11](./Essence_of_Calculus_THEORY.md#chapter-11--taylor-series) |

---

## 🤖 AI/ML Quick-Reference

| Concept | AI/ML Use | Simple Explanation |
|---------|----------|-------------------|
| Derivative | Gradient descent | "Which way is downhill?" for loss |
| Chain rule | Backpropagation | Compute gradients through layers |
| Product rule | Attention gradients | Derivatives of multiplied signals |
| e and exp | Softmax, sigmoid, log-loss | Probability functions built on eˣ |
| Integral | Expected value, probability | Area under PDF = probability |
| Taylor series | Function approximation | Approximate complex functions locally |
| Higher derivatives | Hessian matrix, Newton's method | 2nd-order optimization (curvature) |
| Limits | Convergence of training | "Does loss approach a minimum?" |
| Jacobian | Normalizing flows, transforms | How transforms stretch probability |

---

> 📘 **Start:** [→ Theory Guide](./Essence_of_Calculus_THEORY.md) | [→ Practice Guide](./Essence_of_Calculus_PRACTICE.md)
>
> 🔗 **Also see:** [Linear Algebra Guide](https://github.com/rpaut03l/TS-01/blob/ods-calc/ODS/Linear-Algebra/Essence_of_Linear_Algebra_INDEX.md)
>
> 🎓 **Created for:** ODS
