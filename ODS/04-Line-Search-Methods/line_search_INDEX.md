# Line Search Methods — Topic Hub
### ODS Topic 04 · Lectures 3–5 · Pr K Som

> **Easy Story:** You know which direction is downhill (gradient). But HOW FAR should you walk? Take baby/easy steps (too slow) or giant leaps (might overshoot and end up higher!). Line search = finding the PERFECT step size each time!

---

## Study Materials

| Doc | Link |
|-----|------|
| THEORY | [→ Theory](./line_search_THEORY.md) |
| PRACTICE | [→ Practice](./line_search_PRACTICE.md) |

---

## Quick Cheatsheet

```
╔══════════════════════════════════════════════════════════════════════╗
║  UPDATE RULE: x_{k+1} = xₖ + αₖ dₖ                                    ║
║                                                                      ║
║  DESCENT DIRECTION: ⟨∇f(xₖ), dₖ⟩ < 0                                  ║
║    • Steepest: dₖ = -∇f(xₖ)                                           ║
║    • Newton:   dₖ = -H⁻¹∇f(xₖ)                                        ║
║                                                                      ║
║  STEP SIZE CHOICES:                                                  ║
║  ┌──────────────┬────────────────────────────────────────────┐       ║
║  │ Constant     │ α fixed. Safe: α ∈ (0, 2/L)                │       ║
║  │ Exact        │ α = argmin f(x+αd). For quad: α=-gᵀd/dᵀHd  │       ║
║  │ Backtracking │ Start big, shrink by ρ until Armijo holds  │       ║
║  └──────────────┴────────────────────────────────────────────┘       ║
║                                                                      ║
║  ARMIJO: f(x+αd) ≤ f(x) + c₁α∇fᵀd        (sufficient decrease)       ║
║  WOLFE:  ∇f(x+αd)ᵀd ≥ c₂∇f(x)ᵀd          (curvature condition)       ║
║                                                                      ║
║  L-SMOOTHNESS: ‖∇f(x)-∇f(y)‖ ≤ L‖x-y‖                                ║
║  DESCENT LEMMA: f(y) ≤ f(x) + ∇fᵀ(y-x) + (L/2)‖y-x‖²                 ║
╚══════════════════════════════════════════════════════════════════════╝
```

## Mnemonics

| # | Mnemonic | Meaning |
|---|----------|---------|
| 1 | **ARROW-STEP** | Pick **A**rrow (direction d), choose **S**tep (α), **T**ake a walk, **E**valuate, re**P**eat |
| 2 | **ARMIJO = ARM** | **A**ctual decrease ≥ c₁ × **R**equired **M**inimum (fraction of linear model) |
| 3 | **BACKTRACK** | Start with big α → keep multiplying by ρ < 1 (shrink) until Armijo says OK |

---

> **Prev:** [← 03. Least Squares](../03-Least-Squares-Linear-Regression/least_squares_INDEX.md) · **Next:** [→ 05. Gradient Descent](../05-Gradient-Descent/gradient_descent_INDEX.md) · [↑ Master Hub](../ODS_Master_INDEX.md)

[Back to Top](#line-search-methods--topic-hub)
