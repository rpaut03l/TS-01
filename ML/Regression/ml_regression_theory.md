# 📖 ML Regression: THEORY

### *Simple Linear · Multiple Linear · Logistic · Ridge · Lasso*

> **Nav:** [← ML Master Index](../ml_master_gap_index.md) | **Regression** | [🔢 NUMERICAL](ml_regression_numerical.md) | [💻 PRACTICE](ml_regression_practice.md) | [Legacy: SLR Theory](simple_linear_regression_pe_theory.md)
>

---

## 🧠 MNEMONIC: **"SMLRL"**

> **S**imple linear · **M**ultiple linear · **L**ogistic · **R**idge (L2) · **L**asso (L1)

---

## 📚 Table of Contents

| # | Topic | Jump |
|---|-------|------|
| 1 | What is Regression? | [§1](#1-what-is-regression) |
| 2 | Simple Linear Regression | [§2](#2-simple-linear-regression) |
| 3 | Multiple Linear Regression | [§3](#3-multiple-linear-regression) |
| 4 | Assumptions of Linear Regression | [§4](#4-assumptions-of-linear-regression) |
| 5 | Evaluation Metrics | [§5](#5-evaluation-metrics) |
| 6 | Logistic Regression | [§6](#6-logistic-regression) |
| 7 | Regularization — Ridge & Lasso | [§7](#7-regularization--ridge--lasso) |
| 8 | Polynomial & Basis-Expansion Regression | [§8](#8-polynomial-regression) |
| 9 | Pitfalls: Overfitting · Multicollinearity · Outliers | [§9](#9-pitfalls) |
| 10 | Side-by-Side Summary | [§10](#10-side-by-side-summary) |
| 11 | Cheat Sheet & Exam Hacks | [§11](#11-cheat-sheet--exam-hacks) |

---

## 1. What is Regression?

### 👶 Easy Story
You want to predict a **number** (not a category).
- How much will this house sell for? → regression.
- Is this email spam? → **classification**, but logistic regression is how we bolt a classifier onto the regression framework.

Regression = **fit a function f(x) ≈ y** where y is continuous (or we pretend it is).

```
┌────────────────────────────────────────────────┐
│ Given: (x₁,y₁),...,(xₙ,yₙ)                      │
│ Find:  f ∈ H such that Σ L(yᵢ, f(xᵢ)) is small │
│ For linear regression: f(x) = wᵀx + b          │
│ Loss:  (yᵢ − f(xᵢ))²  (squared error)          │
└────────────────────────────────────────────────┘
```

[↑ Back to Top](#-ml-regression-theory)

---

## 2. Simple Linear Regression

### Model
> **y = β₀ + β₁ x + ε**,   ε ~ N(0, σ²)

- β₀ = intercept (where the line hits the y-axis)
- β₁ = slope (change in y per unit change in x)

### Ordinary Least Squares (OLS) — closed form
Minimize **SSE = Σ (yᵢ − β₀ − β₁ xᵢ)²** → take derivatives, set to 0:

```
β̂₁ = Σ (xᵢ − x̄)(yᵢ − ȳ)  /  Σ (xᵢ − x̄)²
    = Cov(x, y) / Var(x)
β̂₀ = ȳ − β̂₁ x̄
```

Both formulas come from setting ∂SSE/∂β₀ = 0 and ∂SSE/∂β₁ = 0 — a 2×2 linear system.

### Why squared error?
- Closed-form solution exists.
- Corresponds to **MLE under Gaussian noise** (see [Parameter Estimation](../Parameter-Estimations-Guide/ml_parameter_estimation_theory.md)).
- Differentiable, convex → unique minimum.
- Penalizes large errors quadratically ⇒ sensitive to outliers (a weakness, not a strength).

[↑ Back to Top](#-ml-regression-theory)

---

## 3. Multiple Linear Regression

### Model
> **y = β₀ + β₁ x₁ + β₂ x₂ + ⋯ + β_p x_p + ε**

Matrix form:

> **y = X β + ε**,   X is n×(p+1) design matrix (first column all 1s)

### Normal Equation (closed form)
```
SSE = (y − Xβ)ᵀ (y − Xβ)
∂SSE/∂β = −2 Xᵀ(y − Xβ) = 0
⟹ β̂ = (Xᵀ X)⁻¹ Xᵀ y       ← NORMAL EQUATION
```

### Cost & Numerical Notes
- Computing (XᵀX)⁻¹ is O(p³). Fine for p ≤ 10k. Use QR/SVD in practice.
- Fails when **XᵀX is singular** (perfect multicollinearity, p > n) — use Ridge or pseudo-inverse.

### Gradient Descent Alternative
For large n or p:
```
β ← β − η · (2/n) Xᵀ (Xβ − y)
```
Scales linearly. Must tune learning rate η. Converges for η small enough because OLS is convex.

[↑ Back to Top](#-ml-regression-theory)

---

## 4. Assumptions of Linear Regression

| # | Assumption | What breaks if violated |
|---|---|---|
| 1 | **Linearity** — E[y\|x] is linear in β | Biased predictions; transform x or use polynomial |
| 2 | **Independence** of errors | Underestimated standard errors (use time-series / mixed models) |
| 3 | **Homoscedasticity** — constant variance of ε | SE's wrong; weighted LS fixes it |
| 4 | **Normality of errors** (for inference) | Predictions still OK, but t-tests / p-values invalid |
| 5 | **No perfect multicollinearity** | XᵀX not invertible; coefficients explode |

> 📊 **Residual plot is the #1 diagnostic** — if residuals have a pattern, one of the above is violated.

[↑ Back to Top](#-ml-regression-theory)

---

## 5. Evaluation Metrics

```
┌──────────────────────────────────────────────────────────────┐
│ MSE   =  (1/n) Σ (yᵢ − ŷᵢ)²                                  │
│ RMSE  =  √MSE                (same units as y)               │
│ MAE   =  (1/n) Σ |yᵢ − ŷᵢ|    (robust to outliers)           │
│ R²    =  1 − SS_res / SS_tot                                 │
│           SS_res = Σ (yᵢ − ŷᵢ)²                              │
│           SS_tot = Σ (yᵢ − ȳ)²                               │
│ ADJUSTED R² = 1 − (1−R²)(n−1)/(n−p−1)                        │
└──────────────────────────────────────────────────────────────┘
```

- **R² ∈ (−∞, 1]**. R² = 1 perfect, R² = 0 no better than mean, R² < 0 worse than mean.
- **Adjusted R²** penalizes adding useless features — prefer for model comparison.
- **MAE vs MSE:** MSE is differentiable and penalizes outliers harder; MAE is robust.

[↑ Back to Top](#-ml-regression-theory)

---

## 6. Logistic Regression

### Model
Despite the name, **it's classification**. We model the probability of class 1:

```
p(y=1 | x) = σ(wᵀ x + b),   σ(z) = 1 / (1 + e^(−z))
```

The sigmoid squashes (−∞, ∞) → (0, 1), so the linear predictor becomes a probability.

### Log-Odds (the "linear" part)
> **logit(p) = log( p / (1−p) ) = wᵀx + b**

One-unit change in xⱼ multiplies the odds by **e^(wⱼ)**.

### Loss: Binary Cross-Entropy (aka Log Loss)
```
L(w, b) = − (1/n) Σ [ yᵢ log p̂ᵢ + (1−yᵢ) log(1−p̂ᵢ) ]
```

This is **MLE** under a Bernoulli model — you choose w, b to maximize the likelihood of the observed labels.

### No closed form — why?
σ is nonlinear ⇒ setting ∂L/∂w = 0 gives a non-linear system. Solve with:
- **Gradient descent / Newton-Raphson / IRLS** (iteratively reweighted least squares).
- Convex ⇒ any minimum is global.

### Multi-class: Softmax
```
p(y = k | x) = exp(wₖᵀx) / Σⱼ exp(wⱼᵀx)
```
Same idea with K weight vectors; loss is categorical cross-entropy.

[↑ Back to Top](#-ml-regression-theory)

---

## 7. Regularization — Ridge & Lasso

Vanilla OLS / logistic can overfit when p is large or features are correlated. **Add a penalty** on w:

```
Loss_total = Loss_data + λ · Penalty(w)
```

### Ridge (L2)
```
min  Σ (yᵢ − xᵢᵀw)² + λ ‖w‖²²
```
- **Closed form:**  **ŵ = (XᵀX + λI)⁻¹ Xᵀ y**
- **Shrinks** weights toward 0 **smoothly**; never exactly 0.
- Helps with **multicollinearity** (adds λ to eigenvalues of XᵀX → always invertible).
- Corresponds to **Gaussian prior** on w (MAP view).

### Lasso (L1)
```
min  Σ (yᵢ − xᵢᵀw)² + λ ‖w‖₁
```
- **No closed form** (L1 is non-differentiable at 0). Solve via **coordinate descent**.
- **Produces sparsity**: pushes weights exactly to 0 ⇒ automatic feature selection.
- Corresponds to **Laplace prior** on w.

### Elastic Net
> Loss + λ₁ ‖w‖₁ + λ₂ ‖w‖²₂

Best of both: Lasso sparsity + Ridge stability when features correlate.

### Choosing λ
- **Cross-validation** on a grid. `sklearn` has `RidgeCV`, `LassoCV`, `ElasticNetCV`.
- Too small ⇒ no regularization (overfit). Too large ⇒ underfit (all weights → 0).

### Must scale features first!
L1/L2 penalties are **not scale-invariant**. Always `StandardScaler` before ridge/lasso.

[↑ Back to Top](#-ml-regression-theory)

---

## 8. Polynomial Regression

Not a new model — a linear regression on **transformed features**:

```
x  →  [x, x², x³, ..., xᵈ]
```

Still linear in the parameters, so the normal equation still works. Degree **d** is a hyperparameter:
- Small d ⇒ underfit.
- Large d ⇒ wild oscillations, overfit (Runge phenomenon).
- Combine with ridge regularization to tame high-degree polynomials.

More generally, **basis expansions** (splines, RBF features, Fourier) give nonlinear regression without leaving the linear-model framework.

[↑ Back to Top](#-ml-regression-theory)

---

## 9. Pitfalls

### Overfitting
- Caused by too many features, too-flexible models, too little data.
- Diagnose: **train error ≪ test error**.
- Fix: regularization, more data, feature selection, simpler model.

### Multicollinearity
- Two predictors nearly linearly related.
- Effect: XᵀX near-singular ⇒ huge / unstable weights, tiny change in data flips signs.
- Detect: **Variance Inflation Factor (VIF)**. VIF > 5 is suspicious, > 10 is bad.
- Fix: drop one of the collinear features, or use Ridge.

### Outliers
- Squared loss penalizes them quadratically ⇒ a single outlier can pivot the fit line dramatically.
- Fix: Huber loss, RANSAC, or explicit outlier removal.

### Heteroscedasticity
- Residuals have varying variance (e.g., funnel shape in residual plot).
- Fix: transform y (log, √), use weighted least squares, or robust standard errors.

[↑ Back to Top](#-ml-regression-theory)

---

## 10. Side-by-Side Summary

```
┌──────────────┬──────────────┬───────────────┬─────────────┬─────────────┐
│              │ SIMPLE LR    │ MULTIPLE LR   │ LOGISTIC    │ RIDGE/LASSO │
├──────────────┼──────────────┼───────────────┼─────────────┼─────────────┤
│ Output       │ continuous   │ continuous    │ probability │ continuous  │
│ # features   │ 1            │ p             │ p           │ p           │
│ Closed form  │ ✅ Yes       │ ✅ (XᵀX)⁻¹    │ ❌         │ Ridge ✅    │
│ Loss         │ MSE          │ MSE           │ log-loss    │ MSE + reg   │
│ Optimizer    │ formula      │ formula / GD  │ GD / Newton │ formula/CD  │
│ Hyperparams  │ none         │ none          │ none        │ λ           │
│ MLE under    │ Gaussian ε   │ Gaussian ε    │ Bernoulli   │ Gauss+prior │
│ Interpret    │ easy         │ easy          │ odds ratio  │ shrunk      │
└──────────────┴──────────────┴───────────────┴─────────────┴─────────────┘
```

[↑ Back to Top](#-ml-regression-theory)

---

## 11. Cheat Sheet & Exam Hacks

```
╔══════════════════════════════════════════════════════════════╗
║  KEY EQUATIONS                                               ║
╠══════════════════════════════════════════════════════════════╣
║  SLR slope:     β̂₁ = Σ(x−x̄)(y−ȳ) / Σ(x−x̄)²                   ║
║  SLR intercept: β̂₀ = ȳ − β̂₁ x̄                                ║
║  MLR normal eq: β̂  = (XᵀX)⁻¹ Xᵀ y                            ║
║  Ridge:         β̂  = (XᵀX + λI)⁻¹ Xᵀ y                       ║
║  Logistic:      p = σ(wᵀx + b),  σ(z) = 1/(1+e⁻ᶻ)            ║
║  R²:            1 − SS_res / SS_tot                          ║
║  Adj R²:        1 − (1−R²)(n−1)/(n−p−1)                      ║
║  Log loss:      −(1/n) Σ [y log p̂ + (1−y) log(1−p̂)]          ║
╚══════════════════════════════════════════════════════════════╝
```

### ⚡ Exam Red Flags
1. **"Derive OLS from MLE"** → assume ε ~ N(0, σ²), write the Gaussian likelihood, take log, drop constants ⇒ minimize Σ(y − Xβ)² ⇒ MLE = OLS.
2. **"Why squared error?"** → Gaussian noise MLE + differentiable + convex + closed-form.
3. **"When does OLS fail?"** → XᵀX singular (multicollinearity or p ≥ n). Fix with Ridge or pseudo-inverse.
4. **"L1 vs L2?"** → L1 = sparsity (feature selection), L2 = shrinkage only (stability). L1 non-smooth ⇒ no closed form.
5. **"R² = 1 − SS_res / SS_tot"** — memorize which is which. SS_res uses model predictions, SS_tot uses mean.
6. **"Interpret logistic coefficient wⱼ"** → a one-unit change in xⱼ multiplies the **odds** (not the probability) by e^(wⱼ).
7. **"Why scale features before Ridge?"** → because the L2 penalty is not scale-invariant; unscaled features get arbitrary regularization.
8. **"MAP of OLS with Gaussian prior = Ridge"** → see [parameter estimation P7](../Parameter-Estimations-Guide/ml_parameter_estimation_numerical.md).

[↑ Back to Top](#-ml-regression-theory)

---

> **Next:** [🔢 NUMERICAL](ml_regression_numerical.md) · [💻 PRACTICE](ml_regression_practice.md)
>
> *ML · Regression · github.com/rpaut03l/TS-01*
