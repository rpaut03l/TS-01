# Least Squares & Linear Regression — Topic Hub
### ODS Topic 03 · Lecture 3 · Pr K Som

> **Easy Story:** You have scattered dots on a graph (like heights of kids vs age). You want to draw the BEST straight line through them — the one that's closest to ALL dots combined. "Closest" means the total squared distance from dots to line is as SMALL as possible. That's least squares!

---

## Study Materials

| # | Document | What's Inside | Link |
|---|----------|--------------|------|
| THEORY | Theory Guide | Matrix form, normal equations, gradient, Hessian, geometric view | [→ Theory](./least_squares_THEORY.md) |
| PRACTICE | Practice Problems | Normal equations numerical, gradient computation, condition number | [→ Practice](./least_squares_PRACTICE.md) |
| INDEX | This File | Hub, cheatsheet, mnemonics | You are here! |

```
     ┌──────────────┐
     │  INDEX (Hub) │  ← YOU ARE HERE
     └──────┬───────┘
    ┌───────┴───────┐
    ▼               ▼
 ┌────────────┐  ┌────────────┐
 │  THEORY    │◄►│  PRACTICE  │
 └────────────┘  └────────────┘
```

---

## Quick Cheatsheet

```
╔═════════════════════════════════════════════════════════════════════╗
║  DATA: {(xᵢ, yᵢ)} → X ∈ Rⁿˣᵈ (matrix), y ∈ Rⁿ (vector)              ║
║                                                                     ║
║  MODEL: ŷ = Xw  (linear prediction)                                 ║
║                                                                     ║
║  LOSS: f(w) = (1/2)‖Xw - y‖² = (1/2)(Xw-y)ᵀ(Xw-y)                   ║
║                                                                     ║
║  GRADIENT: ∇f(w) = Xᵀ(Xw - y)                                       ║
║                                                                     ║
║  HESSIAN: ∇²f(w) = XᵀX  (always PSD → convex!)                      ║
║                                                                     ║
║  ★ NORMAL EQUATION: w* = (XᵀX)⁻¹Xᵀy  ← MEMORIZE THIS! ★             ║
║                                                                     ║
║  GEOMETRIC VIEW: Xw* = projection of y onto column space of X       ║
║  Residual (y - Xw*) ⊥ column space → Xᵀ(y - Xw*) = 0                ║
╚═════════════════════════════════════════════════════════════════════╝
```

---

## Mnemonics

| # | Mnemonic | Meaning |
|---|----------|---------|
| 1 | **NORMAL** | **N**ormal equations: XᵀXw = Xᵀy. The residual is **N**ormal (perpendicular) to column space |
| 2 | **GRAM** | XᵀX is called the **Gram matrix** — it packs all dot-products of features |
| 3 | **PROJECTION** | w* = (XᵀX)⁻¹Xᵀy means Xw* is the **projection** of y onto Col(X) |

---

## AI/ML Connections

| Concept | Where in ML |
|---------|------------|
| Normal equation | `sklearn.linear_model.LinearRegression()` uses this (or SVD variant) |
| XᵀX invertibility | When n < d (more features than samples) → XᵀX singular → need regularization |
| Condition number of XᵀX | Determines how numerically stable the solution is |
| Adding λI to XᵀX | Ridge regression: (XᵀX + λI)⁻¹Xᵀy → improves conditioning |

---

> **Prev:** [← 02. Optimality Conditions](../02-Optimality-Conditions/optimality_conditions_INDEX.md) · **Next:** [→ 04. Line Search](../04-Line-Search-Methods/line_search_INDEX.md) · [↑ Master Hub](../ODS_Master_INDEX.md)

[Back to Top](#least-squares--linear-regression--topic-hub)
