# Gradient Descent (Steepest Descent) — Topic Hub
### ODS Topic 05 · Lectures 3–6 · Pr K Som

> **Easy Story:** Imagine skiing down a mountain in fog. At each moment, you feel the slope under your skis and go in the STEEPEST downhill direction. That's gradient descent — always follow -∇f! Simple, reliable, the workhorse of ALL machine learning.

---

## Study Materials

| Doc | Link |
|-----|------|
| THEORY | [→ Theory](./gradient_descent_THEORY.md) |
| PRACTICE | [→ Practice](./gradient_descent_PRACTICE.md) |

---

## Quick Cheatsheet

```
╔══════════════════════════════════════════════════════════════════════╗
║  ALGORITHM:                                                          ║
║    x_{k+1} = xₖ - α ∇f(xₖ)                                            ║
║                                                                      ║
║  WHY -∇f? It's the direction of STEEPEST DESCENT among all           ║
║  unit vectors: minimizes ∇f(x)ᵀd subject to ‖d‖=1                    ║
║                                                                      ║
║  STEP SIZE RULES:                                                    ║
║    • Constant: α ∈ (0, 2/L)  → always safe                           ║
║    • Optimal constant: α = 2/(µ+L) for strongly convex               ║
║    • 1/L: simplest safe choice for L-smooth functions                ║
║                                                                      ║
║  CONVERGENCE:                                                        ║
║    • General smooth:         O(1/√k) for ‖∇f‖                        ║
║    • Convex + smooth:        O(1/k) for f(xₖ)-f*                     ║
║    • Strongly convex+smooth: O((1-µ/L)ᵏ) LINEAR RATE!                ║
║                                                                      ║
║  ZIGZAG PROBLEM: GD with exact line search → orthogonal steps!       ║
║    High κ = L/µ → narrow valley → extreme zigzagging                 ║
╚══════════════════════════════════════════════════════════════════════╝
```

## Mnemonics

| # | Mnemonic | Meaning |
|---|----------|---------|
| 1 | **SLIDE** | **S**teepest descent = **L**earning rate × **I**nverse **D**irection of gradient, **E**asy but zigzags |
| 2 | **2/L** | "**Too** over **L**arge" — step must be less than 2/L or you diverge |
| 3 | **κ = pain** | Condition number κ = L/µ. High κ = painful convergence |

---

> **Prev:** [← 04. Line Search](../04-Line-Search-Methods/line_search_INDEX.md) · **Next:** [→ 06. Convergence](../06-Convergence-Analysis/convergence_analysis_INDEX.md) · [↑ Master Hub](../ODS_Master_INDEX.md)

[Back to Top](#gradient-descent-steepest-descent--topic-hub)
