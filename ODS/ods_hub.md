# 📊 ODS — Optimization for Data Science · Master Hub
> **Course:** ODS · Optimization for Data Science · AI
> **Repo:** [rpaut03l/TS-01](https://github.com/rpaut03l/TS-01) → `ODS/`

---

## 📚 Table of Contents
1. [Directory Structure](#1-directory-structure)
2. [Full Topic Map](#2-full-topic-map)
3. [60-Second Course Recap](#3-60-second-course-recap)
4. [Navigation Table](#4-navigation-table)

---

## 1. Directory Structure

```
ODS/
├── ods_hub.md                          ← YOU ARE HERE
├── Foundations/
│   ├── foundations_hub.md
│   ├── foundations_theory.md
│   ├── foundations_numericals.md
│   └── foundations_practice.md
├── LineSearch/
│   ├── line_search_hub.md
│   ├── line_search_theory.md
│   ├── line_search_numericals.md
│   └── line_search_practice.md
├── GradientDescent/
│   ├── gradient_descent_hub.md
│   ├── gradient_descent_theory.md
│   ├── gradient_descent_numericals.md
│   └── gradient_descent_practice.md
├── NewtonMethods/
│   ├── newton_hub.md
│   ├── newton_theory.md
│   ├── newton_numericals.md
│   └── newton_practice.md
├── QuasiNewton/
│   ├── quasi_newton_hub.md
│   ├── quasi_newton_theory.md
│   ├── quasi_newton_numericals.md
│   └── quasi_newton_practice.md
├── ConjugateGradient/
│   ├── cg_hub.md
│   ├── cg_theory.md
│   ├── cg_numericals.md
│   └── cg_practice.md
└── LinearRegression/
    ├── lr_ods_hub.md
    ├── lr_ods_theory.md
    ├── lr_ods_numericals.md
    └── lr_ods_practice.md
```

---

## 2. Full Topic Map

```
MAL7070 — Optimization for Data Science
│
├── T1 Foundations
│   ├── Fermat's Rule: f'(x*)=0  (necessary at extremum)
│   ├── Convex Sets & Functions (3 equivalent definitions)
│   ├── First-Order Condition:  ∇f(x*)=0
│   ├── Second-Order Condition: ∇²f(x*)≻0
│   ├── Lipschitz Gradient (L): ‖∇f(x)-∇f(y)‖ ≤ L‖x-y‖
│   └── Strong Convexity (μ):   f(y)≥f(x)+∇fᵀ(y-x)+(μ/2)‖y-x‖²
│
├── T2 Line Search
│   ├── Descent Directions: ∇f(x)ᵀp < 0
│   ├── Armijo Condition (sufficient decrease)
│   ├── Wolfe Conditions (Armijo + curvature)
│   └── Backtracking Algorithm
│
├── T3 Gradient Descent
│   ├── Steepest Descent: xₖ₊₁ = xₖ - αₖ∇f(xₖ)
│   ├── Exact Step for Quadratics: αₖ = ‖g‖²/(gᵀQg)
│   ├── Convergence O(1/k) — convex
│   ├── Linear Convergence — strongly convex, rate (1-1/κ)ᵏ
│   ├── Condition Number κ = L/μ
│   ├── SGD: one random sample per step
│   └── Robbins-Monro: Σα=∞, Σα²<∞
│
├── T4 Newton Methods
│   ├── Newton Direction: pₖ = -Hₖ⁻¹gₖ
│   ├── Quadratic Convergence: ‖eₖ₊₁‖ ≤ C‖eₖ‖²
│   ├── Trust Region (ρₖ ratio, expand/shrink Δ)
│   └── Damped Newton (Newton dir + backtracking α)
│
├── T5 Quasi-Newton
│   ├── Secant Equation: Bₖ₊₁sₖ = yₖ
│   ├── DFP Update Formula
│   └── BFGS Update Formula (more robust)
│
├── T6 Conjugate Gradient
│   ├── Q-Conjugate: pᵢᵀQpⱼ=0 (i≠j)
│   ├── Linear CG (solves Qx=b in exactly n steps)
│   ├── Fletcher-Reeves (FR): β=‖g_{k+1}‖²/‖gₖ‖²
│   └── Polak-Ribiere (PR): β=g_{k+1}ᵀ(g_{k+1}-gₖ)/‖gₖ‖²
│
└── T7 Linear Regression (Optimization View)
    ├── Model: ŷ=Xβ, Loss: f(β)=(1/2n)‖Xβ-y‖²
    ├── ∇f(β) = (1/n)Xᵀ(Xβ-y),  ∇²f(β) = (1/n)XᵀX
    ├── Normal Equations: XᵀXβ = Xᵀy
    └── Ridge: β*=(XᵀX+λI)⁻¹Xᵀy
```

---

## 3. 60-Second Course Recap

```
FOUNDATIONS → when is x* a minimum? (Fermat + convexity + Lipschitz)
LINE SEARCH  → pick step size α so we go downhill (Armijo, Wolfe)
GRAD DESC    → subtract gradient, converge O(1/k) or linearly
NEWTON       → use Hessian → quadratic convergence (super fast near x*)
QUASI-NEWTON → fake the Hessian from gradient history → superlinear
CONJ GRAD    → n special perpendicular directions → exact in n steps
LINEAR REG   → apply optimization to fit Xβ=y via normal equations
```

---

## 4. Navigation Table

| # | Topic | Hub | Theory | Numericals | Practice |
|---|-------|-----|--------|------------|---------|
| 1 | Foundations | [Hub](./Foundations/foundations_hub.md) | [Theory](./Foundations/foundations_theory.md) | [Nums](./Foundations/foundations_numericals.md) | [Practice](./Foundations/foundations_practice.md) |
| 2 | Line Search | [Hub](./LineSearch/line_search_hub.md) | [Theory](./LineSearch/line_search_theory.md) | [Nums](./LineSearch/line_search_numericals.md) | [Practice](./LineSearch/line_search_practice.md) |
| 3 | Gradient Descent | [Hub](./GradientDescent/gradient_descent_hub.md) | [Theory](./GradientDescent/gradient_descent_theory.md) | [Nums](./GradientDescent/gradient_descent_numericals.md) | [Practice](./GradientDescent/gradient_descent_practice.md) |
| 4 | Newton Methods | [Hub](./NewtonMethods/newton_hub.md) | [Theory](./NewtonMethods/newton_theory.md) | [Nums](./NewtonMethods/newton_numericals.md) | [Practice](./NewtonMethods/newton_practice.md) |
| 5 | Quasi-Newton | [Hub](./QuasiNewton/quasi_newton_hub.md) | [Theory](./QuasiNewton/quasi_newton_theory.md) | [Nums](./QuasiNewton/quasi_newton_numericals.md) | [Practice](./QuasiNewton/quasi_newton_practice.md) |
| 6 | Conjugate Gradient | [Hub](./ConjugateGradient/cg_hub.md) | [Theory](./ConjugateGradient/cg_theory.md) | [Nums](./ConjugateGradient/cg_numericals.md) | [Practice](./ConjugateGradient/cg_practice.md) |
| 7 | Linear Regression (ODS) | [Hub](./LinearRegression/lr_ods_hub.md) | [Theory](./LinearRegression/lr_ods_theory.md) | [Nums](./LinearRegression/lr_ods_numericals.md) | [Practice](./LinearRegression/lr_ods_practice.md) |

---

## 🔗 Navigation
[🔝 Top](#-ods--optimization-for-data-science--master-hub) · [T1 Foundations →](./Foundations/foundations_hub.md)

> **Other subjects:** [ML →](../ML/) · [AI →](../AI/) · [DSA →](../DSA/)
