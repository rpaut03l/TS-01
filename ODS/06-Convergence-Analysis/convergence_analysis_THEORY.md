# Convergence Analysis — Theory
### ODS Topic 06 · Lectures 6-7

> **Nav:** [← INDEX](./convergence_analysis_INDEX.md) · [→ PRACTICE](./convergence_analysis_PRACTICE.md) · [↑ Hub](../ODS_Master_INDEX.md)

---

## 6.1 Orders of Convergence

| Name | Definition | Speed |
|------|-----------|-------|
| **Sublinear** | \|rₖ - r*\| = O(1/k^p) | Slow |
| **Linear** | \|r_{k+1} - r*\|/\|rₖ - r*\| → β < 1 | Like geometric series |
| **Superlinear** | \|r_{k+1} - r*\|/\|rₖ - r*\| → 0 | Faster than linear |
| **Quadratic** | \|r_{k+1} - r*\|/\|rₖ - r*\|² → C | Doubles correct digits each step |

## 6.2 GD Convergence Rates (The Big Table)

```
╔══════════════════════╦══════════╦════════════════════════════════╗
║ Assumptions          ║ Step α   ║ Rate                           ║
╠══════════════════════╬══════════╬════════════════════════════════╣
║ L-smooth only        ║ (0,2/L)  ║ min‖∇f(xₖ)‖ ≤ O(1/√k)          ║
║ L-smooth + convex    ║ 1/L      ║ f(xₖ)-f* ≤ L‖x₀-x*‖²/(2k)      ║
║ L-smooth + µ-SC      ║ 1/L      ║ f(xₖ)-f* ≤ (1-µ/L)ᵏ(f₀-f*)     ║
║ L-smooth + µ-SC      ║ 2/(µ+L)  ║ ‖xₖ-x*‖ ≤ ((L-µ)/(L+µ))ᵏ       ║
╚══════════════════════╩══════════╩════════════════════════════════╝
```

## 6.3 Condition Number κ = L/µ

- Small κ → easy problem, fast convergence
- Large κ → ill-conditioned, slow zigzagging
- For quadratic f = (1/2)xᵀAx: κ = λ_max/λ_min

## 6.4 Zoutendijk's Theorem

Under Wolfe conditions: Σₖ cos²θₖ ‖∇f(xₖ)‖² < ∞

This guarantees ∇f(xₖ) → 0 (gradient vanishes) for any descent method with Wolfe line search.

---

> [→ PRACTICE](./convergence_analysis_PRACTICE.md) · [↑ Hub](../ODS_Master_INDEX.md)

[Back to Top](#convergence-analysis--theory)
