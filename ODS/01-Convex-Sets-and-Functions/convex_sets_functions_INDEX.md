# Convex Sets & Functions — Topic Hub
### ODS Topic 01 · Lectures 1–2 · Pr K Som

> **Easy Story:** Imagine a rubber sheet stretched over a bowl. If you place a marble anywhere, it rolls to the bottom. That's a CONVEX function! And the bowl itself (the inside part) is a CONVEX SET — any two points inside, the straight line between them stays inside too!

---

## Study Materials

| # | Document | What's Inside | Link |
|---|----------|--------------|------|
| THEORY | Theory Guide | Definitions, proofs, properties, diagrams | [→ Theory](./convex_sets_functions_THEORY.md) |
| PRACTICE | Practice Problems | Solved numericals + exam-style questions | [→ Practice](./convex_sets_functions_PRACTICE.md) |
| INDEX | This File | Hub, cheatsheet, mnemonics | You are here! |

```
     ┌──────────────┐
     │  INDEX (Hub) │  ← YOU ARE HERE
     └──────┬───────┘
    ┌───────┴───────┐
    ▼               ▼
 ┌────────────┐  ┌────────────┐
 │  THEORY    │◄►│  PRACTICE  │
 │ Concepts + │  │ Problems + │
 │ Proofs     │  │Step-by-step│
 └────────────┘  └────────────┘
```

---

## Topics Covered

| # | Sub-topic | Theory | Practice |
|---|-----------|--------|----------|
| 1.1 | Convex Sets — Definition & Examples | [Theory](./convex_sets_functions_THEORY.md#11-convex-sets--definition) | [P1-P2](./convex_sets_functions_PRACTICE.md#p1-is-this-set-convex) |
| 1.2 | Convex Functions — Definition | [Theory](./convex_sets_functions_THEORY.md#12-convex-functions--definition) | [P3-P4](./convex_sets_functions_PRACTICE.md#p3-prove-convexity-of-a-function) |
| 1.3 | First-Order Characterization | [Theory](./convex_sets_functions_THEORY.md#13-first-order-characterization) | [P5](./convex_sets_functions_PRACTICE.md#p5-first-order-condition) |
| 1.4 | Second-Order Characterization | [Theory](./convex_sets_functions_THEORY.md#14-second-order-characterization) | [P6-P7](./convex_sets_functions_PRACTICE.md#p6-hessian-check-for-convexity) |
| 1.5 | Operations Preserving Convexity | [Theory](./convex_sets_functions_THEORY.md#15-operations-preserving-convexity) | [P8](./convex_sets_functions_PRACTICE.md#p8-composition-rules) |
| 1.6 | Strong Convexity | [Theory](./convex_sets_functions_THEORY.md#16-strong-convexity) | [P9](./convex_sets_functions_PRACTICE.md#p9-strong-convexity-parameter) |
| 1.7 | Convex Sets Advanced — Hull, Cones, Separation | [Theory](./convex_sets_functions_THEORY.md#17-advanced-convex-sets) | [P10](./convex_sets_functions_PRACTICE.md#p10-separation-theorem) |

---

## Quick Cheatsheet

```
╔════════════════════════════════════════════════════════════════╗
║  CONVEX SET: ∀ x,y ∈ C, θ ∈ [0,1]: θx + (1-θ)y ∈ C             ║
║  → "Line between any 2 points stays inside"                    ║
║                                                                ║
║  CONVEX FUNCTION: f(θx + (1-θ)y) ≤ θf(x) + (1-θ)f(y)           ║
║  → "Chord is always ABOVE the curve"                           ║
║                                                                ║
║  1st ORDER: f convex ⟺ f(y) ≥ f(x) + ∇f(x)ᵀ(y-x) ∀x,y         ║
║  → "Tangent line is always BELOW the curve"                    ║
║                                                                ║
║  2nd ORDER: f convex ⟺ ∇²f(x) ≽ 0 (PSD) ∀x                    ║
║  → "Hessian is Positive Semidefinite everywhere"               ║
║                                                                ║
║  STRONGLY CONVEX (µ>0):                                        ║
║  f(y) ≥ f(x) + ∇f(x)ᵀ(y-x) + (µ/2)‖y-x‖²                       ║
║  → "Bowl has minimum curvature µ"                              ║
║                                                                ║
║  KEY INSIGHT: Convex → every local min IS global min!          ║
╚════════════════════════════════════════════════════════════════╝
```

---

## Mnemonics

| # | Mnemonic | Meaning |
|---|----------|---------|
| 1 | **CLIFF** | **C**onvex set = **L**ine **I**nside **F**orever **F**or any two points |
| 2 | **CHORD-ABOVE** | Convex function: the chord (straight line) is always ABOVE the curve |
| 3 | **TANGENT-BELOW** | 1st order: tangent line always BELOW. Mirror of chord-above |
| 4 | **BOWL-UP** | 2nd order: Hessian PSD = bowl curves UP = convex |
| 5 | **LOCAL=GLOBAL** | In convex world, every local minimum IS the global minimum |

---

## AI/ML Connections

| Concept | AI/ML Application |
|---------|-------------------|
| Convex function | MSE loss, log-loss, hinge loss are all convex |
| Convex set | Feasible weight regions in regularized models |
| 1st order condition | Used to prove gradient descent finds global min for convex losses |
| Strong convexity | L2-regularization makes loss strongly convex → unique solution |
| PSD Hessian | Confirms your loss landscape has no saddle points |

---

> **Next Topic:** [→ 02. Optimality Conditions](../02-Optimality-Conditions/optimality_conditions_INDEX.md)
>
> **Back to Master Hub:** [→ ODS Master Index](../ODS_Master_INDEX.md)

[Back to Top](#convex-sets--functions--topic-hub)
