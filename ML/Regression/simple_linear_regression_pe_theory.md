# 📘 Simple Linear Regression & Parameter Estimation — Complete Theory Guide

> **Subject:** Machine Learning | **Topics:** Parameter Estimation + Simple Linear Regression  

---

## 📑 Table of Contents

| # | Section | Jump To |
|---|---------|---------|
| **PART A — PARAMETER ESTIMATION** | | |
| A1 | [Parameters and Statistics](#a1--parameters-and-statistics) | |
| A2 | [Sampling Distribution](#a2--sampling-distribution) | |
| A3 | [Estimates vs Estimators](#a3--estimates-vs-estimators) | |
| A4 | [Quality of Estimators (Bias, Variance, MSE, Consistency, Efficiency)](#a4--quality-of-estimators) | |
| A5 | [Estimation Frameworks (LS, MoM, MLE)](#a5--estimation-frameworks) | |
| **PART B — SIMPLE LINEAR REGRESSION** | | |
| B1 | [The SLR Model & Error Component](#b1--the-slr-model--error-component) | |
| B2 | [Correlation Coefficient](#b2--correlation-coefficient) | |
| B3 | [Least Squares Estimation (OLS)](#b3--least-squares-estimation-ols) | |
| B4 | [Properties of OLS Estimators & Gauss-Markov](#b4--properties-of-ols-estimators--gauss-markov) | |
| B5 | [Residual Analysis](#b5--residual-analysis) | |
| B6 | [Centered Model & No-Intercept Model](#b6--centered-model--no-intercept-model) | |
| B7 | [Maximum Likelihood Estimation for Regression](#b7--maximum-likelihood-estimation-for-regression) | |
| B8 | [Hypothesis Testing (β₀, β₁, σ²)](#b8--hypothesis-testing-β₀-β₁-σ) | |
| B9 | [ANOVA & R² (Coefficient of Determination)](#b9--anova--r-coefficient-of-determination) | |
| B10 | [Prediction — Mean Response & New Observation](#b10--prediction--mean-response--new-observation) | |
| B11 | [Alternative Regression Methods](#b11--alternative-regression-methods) | |
| B12 | [Stochastic X](#b12--stochastic-x) | |
| **PART C — REFERENCE** | | |
| C1 | [Master Formula Sheet](#c1--master-formula-sheet) | |
| C2 | [Complete Notations Table](#c2--complete-notations-table) | |
| C3 | [Mnemonics & Memory Tricks](#c3--mnemonics--memory-tricks) | |

---

# PART A — PARAMETER ESTIMATION

---

## A1 | Parameters and Statistics

[⬆️ Back to Top](#-table-of-contents)

### What Is a Parameter? 🧒

Imagine a giant jar of 10,000 marbles — some red, some blue. The **true percentage** of red marbles is the **parameter**. You can't count all 10,000, so you grab a handful (sample) and estimate.

> **Parameter** = A number that describes the WHOLE population (usually unknown)  
> **Statistic** = A number calculated from a SAMPLE (what we actually compute)

### Formal Setup

A random variable **X** has a CDF: `F(x) = P(X ≤ x)`

F(·) has an associated:
- **PMF** (discrete): `f(x) = P(X = x)`
- **PDF** (continuous): `∫ₐᵇ f(x)dx = P(a < X < b)`

A **parameter** `θ = t(F)` is some function of the distribution F.

```
POPULATION (unknown)          SAMPLE (what we have)
┌─────────────────┐          ┌─────────────────┐
│  Parameter θ     │  ←───── │  Statistic T=s(x)│
│  (e.g., µ, σ²)  │ estimate │  (e.g., x̄, s²)  │
└─────────────────┘          └─────────────────┘
```

### Key Definitions

| Term | Symbol | Meaning | Example |
|------|--------|---------|---------|
| **Parameter** | θ | True population value | µ (population mean) |
| **Statistic** | T = s(x) | Function of sample data | x̄ (sample mean) |
| **Sample** | x₁, ..., xₙ | n observations from F | Test scores of 30 students |
| **iid** | xᵢ ~iid~ F | Independent & Identically Distributed | Each marble drawn randomly |

---

## A2 | Sampling Distribution

[⬆️ Back to Top](#-table-of-contents)

### What Is It? 🧒

If you repeated the experiment 1000 times (grabbing new handfuls of marbles each time), and computed x̄ each time, you'd get 1000 different x̄ values. The **distribution of these 1000 x̄ values** = the sampling distribution.

> **Sampling Distribution** = The probability distribution of a statistic T = s(x) over repeated samples.

### Key Properties

- Depends on the **distribution of data** — if data comes from F vs G, the sampling distribution changes
- Sometimes known as n → ∞ (Central Limit Theorem)
- CLT: `x̄ ~ N(µ, σ²/n)` approximately, for large n, regardless of F

```
Population F              Many Samples             Sampling Distribution
   ┌───┐                  ┌─ Sample 1 → T₁        ┌───────────┐
   │   │  ──── draw ────→ ├─ Sample 2 → T₂   ───→ │~N(µ, σ²/n)│
   │   │       many       ├─ Sample 3 → T₃        │ (by CLT)  │
   └───┘       times      ├─ ...                  └───────────┘
                          └─ Sample R → Tᵣ
```

---

## A3 | Estimates vs Estimators

[⬆️ Back to Top](#-table-of-contents)

### The Distinction 🧒

Think of it this way:
- **Estimator** = the **recipe** (the formula you use)
- **Estimate** = the **dish** (the actual number you get after plugging in data)

| Concept | Symbol | What It Is | Example |
|---------|--------|-----------|---------|
| **Estimator** | g(·) | The function/formula | "Take the average" |
| **Estimate** | θ̂ = g(x) | The computed value | x̄ = 72.5 |

### Hat Notation (θ̂)

A "hat" on a parameter means **estimate**:
- θ̂ = "theta hat" = an estimate of θ
- µ̂ = x̄ (estimate of population mean)
- σ̂² = s² (estimate of population variance)

### Common Examples

| Parameter | Estimator | Formula | Unbiased? |
|-----------|-----------|---------|-----------|
| µ = E(X) | x̄ = µ̂ | (1/n)Σxᵢ | ✅ Yes |
| σ² = E[(X−µ)²] | s² = σ̂² | 1/(n−1) Σ(xᵢ−x̄)² | ✅ Yes |
| σ² = E[(X−µ)²] | s̃² | 1/n Σ(xᵢ−x̄)² | ❌ No (biased low) |

> ⚠️ **Why n−1 not n?** Dividing by n gives a **downward bias** because E(s̃²) = (n−1)/n · σ². Dividing by n−1 corrects this → **Bessel's correction**.

---

## A4 | Quality of Estimators

[⬆️ Back to Top](#-table-of-contents)

### Overview: What Makes a "Good" Estimator?

Not all estimators are equal! We evaluate them on 4 criteria:

```
                    ┌─────────────┐
                    │ QUALITY OF  │
                    │ ESTIMATORS  │
                    └──────┬──────┘
           ┌───────────┬───┴───┬───────────┐
           ▼           ▼       ▼           ▼
       ┌──────┐   ┌────────┐ ┌─────┐  ┌───────────┐
       │ BIAS │   │VARIANCE│ │ MSE │  │CONSISTENCY│
       └──────┘   └────────┘ └─────┘  └───────────┘
       "Is it     "Is it     "Both    "Does more
       on target?" precise?" combined" data help?"
```

### 1. Bias — "Is It On Target?"

```
Bias(θ̂) = E(θ̂) − θ
```

| Bias(θ̂) | Meaning | Analogy |
|----------|---------|---------|
| = 0 | **Unbiased** — on average, hits the true value | Arrows centered on bullseye |
| > 0 | Overestimates on average | Arrows all above bullseye |
| < 0 | Underestimates on average | Arrows all below bullseye |

**Proof: x̄ is unbiased for µ:**
```
E(x̄) = E(1/n · Σxᵢ) = 1/n · Σ E(xᵢ) = 1/n · n·µ = µ  ✅
```

**Proof: s² is unbiased for σ² (sketch):**
```
Σ(xᵢ−x̄)² = Σxᵢ² − nx̄²

E(Σxᵢ²) = n(σ² + µ²)
E(nx̄²)  = n[σ²/n + µ²] = σ² + nµ²

E[Σ(xᵢ−x̄)²] = n(σ²+µ²) − (σ²+nµ²) = (n−1)σ²

∴ E(s²) = E[1/(n−1) · Σ(xᵢ−x̄)²] = σ²  ✅
```

**Why s̃² = (1/n)Σ(xᵢ−x̄)² is biased:**
```
E(s̃²) = (n−1)/n · σ²  →  Bias = −σ²/n  (downward bias)
```

> 💡 **Biased ≠ Bad!** Ridge, LASSO, Elastic Net deliberately add bias to reduce variance → better overall performance.

### 2. Variance — "Is It Precise?"

```
Var(θ̂) = E[(θ̂ − E(θ̂))²]

Standard Error: SE(θ̂) = √Var(θ̂)
```

**Variance of x̄:**
```
Var(x̄) = Var(1/n · Σxᵢ) = 1/n² · Σ Var(xᵢ) = 1/n² · nσ² = σ²/n
```

> 🧒 **Easy version:** As sample size n gets BIGGER, σ²/n gets SMALLER → more precise!

### 3. Mean Squared Error (MSE) — "The Full Picture"

```
┌─────────────────────────────────────────────────┐
│                                                 │
│   MSE(θ̂) = E[(θ̂ − θ)²]                          │
│                                                 │
│          = Bias(θ̂)² + Var(θ̂)                    │
│                                                 │
│   MSE = Bias² + Variance                        │
│                                                 │
└─────────────────────────────────────────────────┘
```

**Proof of MSE decomposition:**
```
E[(θ̂−θ)²] = E(θ̂²) − 2θ·E(θ̂) + θ²

Bias² = [E(θ̂)]² − 2θ·E(θ̂) + θ²
Var   = E(θ̂²) − [E(θ̂)]²

Bias² + Var = E(θ̂²) − 2θ·E(θ̂) + θ²  = MSE  ✅
```

```
  Bias-Variance Tradeoff:

  High Bias,         Balanced           Low Bias,
  Low Variance        (Sweet Spot)      High Variance

    ●●●                 ●                  ●
    ●●●              ● ⊕ ●                   ●
    ●●●                 ●               ●        ●
   (off-center       (near center,      (centered but
    but tight)        tight-ish)         spread out)
```

### 4. Consistency — "Does More Data Help?"

```
θ̂  →ᵖ  θ   as  n → ∞
```

> An estimator is **consistent** if it converges in probability to the true value as sample size increases. All reasonable estimators (x̄, s², s̃²) are consistent.

### 5. Efficiency — "Is It the Best?"

An estimator is **efficient** if it has the **smallest MSE** among all estimators of θ.

If comparing two **unbiased** estimators → the one with **smaller variance** is more efficient.

### Summary Table

| Property | Formula | Easy Version |
|----------|---------|-------------|
| **Unbiased** | E(θ̂) = θ | Aims at the right target on average |
| **Low Variance** | Var(θ̂) is small | Arrows are tightly clustered |
| **Low MSE** | Bias² + Var is small | Both accurate AND precise |
| **Consistent** | θ̂ →ᵖ θ as n→∞ | More data = better answer |
| **Efficient** | Smallest MSE among all estimators | The BEST possible estimator |

---

## A5 | Estimation Frameworks

[⬆️ Back to Top](#-table-of-contents)

Three major frameworks for finding estimators:

```
┌──────────────────────────────────────────────────┐
│           THREE ESTIMATION FRAMEWORKS            │
├──────────────┬──────────────┬────────────────────┤
│ Least Squares│ Method of    │ Maximum Likelihood │
│    (LS)      │ Moments (MoM)│    (MLE)           │
├──────────────┼──────────────┼────────────────────┤
│ Minimise     │ Match sample │ Maximise the       │
│ Σ(xᵢ−θ)²    │ moments to   │ likelihood of       │
│              │ population   │ observing the data │
│              │ moments      │                    │
├──────────────┼──────────────┼────────────────────┤
│ Works for    │ Works when   │ Works universally  │
│ means &      │ moments are  │ Needs distribution │
│ regression   │ known        │ assumption         │
└──────────────┴──────────────┴────────────────────┘
```

### Framework 1: Least Squares (LS)

**Goal:** Find θ̂ that minimises `Σ(h(xᵢ) − θ)²`

**Example — Estimating µ:**
```
LS(µ|x) = Σ(xᵢ − µ)² = Σxᵢ² − 2µΣxᵢ + nµ²

dLS/dµ = −2Σxᵢ + 2nµ = 0

∴ µ̂ = (1/n)Σxᵢ = x̄   ← Sample mean!
```

### Framework 2: Method of Moments (MoM)

**Idea:** Set sample moments = population moments, solve for parameters.

**j-th population moment:** `µⱼ = E(Xʲ)`  
**j-th sample moment:** `µ̂ⱼ = (1/n)Σxᵢʲ`

**Example — Normal N(µ, σ²):**
```
Population:  µ₁ = µ,           µ₂ = µ² + σ²
Sample:      µ̂₁ = x̄,           µ̂₂ = x̄² + s̃²

∴ µ̂ = x̄  and  σ̂² = s̃² = (1/n)Σ(xᵢ−x̄)²
```

**Example — Uniform U[a, b]:**
```
µ₁ = (a+b)/2,   µ₂ = (a² + ab + b²)/3

Solving: â = µ̂₁ − √3·√(µ̂₂ − µ̂₁²)
         b̂ = µ̂₁ + √3·√(µ̂₂ − µ̂₁²)
```

### Framework 3: Maximum Likelihood Estimation (MLE)

**Idea:** Find the parameter values that make the observed data MOST LIKELY.

**Likelihood function:**
```
L(θ|x) = ∏ᵢ₌₁ⁿ f(xᵢ|θ)
```

**Log-likelihood (easier to work with):**
```
ℓ(θ|x) = Σᵢ₌₁ⁿ log f(xᵢ|θ)
```

**MLE:** `θ̂_MLE = argmax ℓ(θ|x)`

> 🧒 **Easy version:** "Which θ makes it MOST PROBABLE that we'd see exactly this data?"

### MLE Properties (Why MLEs Are Awesome)

| Property | Meaning |
|----------|---------|
| **Consistent** | θ̂_MLE → θ as n → ∞ |
| **Asymptotically efficient** | Var(θ̂_MLE) ≤ Var(θ̂_any) for large n |
| **Functionally invariant** | If θ̂ is MLE of θ, then h(θ̂) is MLE of h(θ) |

### MLE Examples

**Normal N(µ, σ²):**
```
ℓ = −(1/2σ²)Σ(xᵢ−µ)² − (n/2)log(σ²) − c

∂ℓ/∂µ = 0  →  µ̂_MLE = x̄
∂ℓ/∂σ² = 0  →  σ̂²_MLE = s̃² = (1/n)Σ(xᵢ−x̄)²

Note: σ̂²_MLE = s̃² is BIASED (divides by n, not n−1)
      but it has LOWER VARIANCE than s²
```

**Binomial B[N, p]:**
```
ℓ = log(p)·Σxᵢ + log(1−p)·(nN − Σxᵢ) + c

dℓ/dp = 0  →  p̂_MLE = x̄/N
```

**Uniform U[a, b]:**
```
ℓ = −n·log(b−a)

Maximise by minimising (b−a) subject to a ≤ min(xᵢ), b ≥ max(xᵢ)

∴ â_MLE = x₍₁₎ = min(xᵢ),  b̂_MLE = x₍ₙ₎ = max(xᵢ)
```

---

# PART B — SIMPLE LINEAR REGRESSION

---

## B1 | The SLR Model & Error Component

[⬆️ Back to Top](#-table-of-contents)

### The Model

```
┌───────────────────────────────────────────────┐
│                                               │
│        yᵢ = β₀ + β₁xᵢ + εᵢ                    │
│                                               │
│   i = 1, 2, ..., n  (n data pairs)            │
└───────────────────────────────────────────────┘
```

| Symbol | Name | Role |
|--------|------|------|
| yᵢ | Dependent/study variable | What we predict |
| xᵢ | Independent/explanatory variable | What we use to predict |
| β₀ | Intercept | Y when X = 0 |
| β₁ | Slope | Change in Y per unit X |
| εᵢ | Error (unobservable) | Random noise |

### Why Do We Need ε? (What Causes Error?)

The error component accounts for:
1. **Data not falling on a perfect line** (real world is messy)
2. **Deleted/omitted variables** (things we didn't measure)
3. **Qualitative variables** we can't easily quantify
4. **Inherent randomness** in observations

### Key Assumptions on ε

```
┌──────────────────────────────────────┐
│  1.  E(ε) = 0      (zero mean)       │
│  2.  Var(ε) = σ²   (constant var.)   │
│  3.  εᵢ are iid    (independent)     │
└──────────────────────────────────────┘
```

### Model Properties (Derived from Assumptions)

| Property | When X is fixed | When X is random |
|----------|----------------|------------------|
| **Expected value** | E(y) = β₀ + β₁X | E(y\|x) = β₀ + β₁x |
| **Variance** | Var(y) = σ² | Var(y\|x) = σ² |

> 🧒 **Easy version:** The model says "Y is mostly β₀ + β₁X, plus some random wobble ε that averages out to zero."

### What Needs Estimation?

Three unknowns: **β₀**, **β₁**, and **σ²** — all estimated from data using Least Squares or MLE.

---

## B2 | Correlation Coefficient

[⬆️ Back to Top](#-table-of-contents)

Before building a model, check if X and Y are related:

```
         sxy              Σ(xᵢ − x̄)(yᵢ − ȳ)
r = ──────────── = ─────────────────────────────
    √(sxx · syy)   √[Σ(xᵢ−x̄)²] · √[Σ(yᵢ−ȳ)²]
```

| r value | Meaning |
|---------|---------|
| r = +1 | Perfect positive linear relationship |
| r = −1 | Perfect negative linear relationship |
| r = 0 | No linear relationship |

```
r ≈ +0.9           r ≈ 0              r ≈ −0.9
  Y|    * *          Y|  *   *   *       Y| *  *
   |   * *            | *  *    *         |   * *
   |  * *             |*  *  *            |     * *
   | * *              | *   *             |       * *
   |*                 |  *    *           |         *
   └────── X          └─────── X          └─────── X
```

**Key facts:**
- r is **dimensionless** (no units)
- r only measures **linear** relationships
- r(X,Y) = r(Y,X) (symmetric)
- **R² = r²** → proportion of variance explained
- **Correlation ≠ Causation!**

**Relationship with slope:** `b₁ = r · √(syy/sxx)`

---

## B3 | Least Squares Estimation (OLS)

[⬆️ Back to Top](#-table-of-contents)

### Four Types of Regression

| # | Method | What It Minimises | When to Use |
|---|--------|-------------------|-------------|
| 1 | **Direct (OLS)** | Vertical distances | Standard — Y has error |
| 2 | **Reverse** | Horizontal distances | X has error |
| 3 | **Orthogonal** | Perpendicular distances | Both have errors |
| 4 | **Reduced Major Axis** | Rectangle areas | Uncertainties in both |

### OLS — The Standard Approach

**Objective:** Minimise the Sum of Squared Errors

```
S(β₀, β₁) = Σᵢ₌₁ⁿ εᵢ² = Σᵢ₌₁ⁿ (yᵢ − β₀ − β₁xᵢ)²
```

### Derivation — Normal Equations

Take partial derivatives and set to zero:

```
∂S/∂β₀ = −2 Σ(yᵢ − β₀ − β₁xᵢ) = 0         ... (1)
∂S/∂β₁ = −2 Σ(yᵢ − β₀ − β₁xᵢ)·xᵢ = 0      ... (2)
```

### Solving → OLS Estimators

```
┌──────────────────────────────────────────┐
│                                          │
│         sxy     Σ(xᵢ−x̄)(yᵢ−ȳ)            │
│  b₁ = ───── = ─────────────────          │
│         sxx       Σ(xᵢ−x̄)²               │
│                                          │
│  b₀ = ȳ − b₁·x̄                           │
│                                          │
└──────────────────────────────────────────┘
```

### Global Minimum Proof (Hessian)

Second-order derivatives form the Hessian matrix:

```
∂²S/∂β₀² = 2n
∂²S/∂β₁² = 2Σxᵢ²
∂²S/∂β₀∂β₁ = 2nx̄

|H*| = 4n · Σ(xᵢ − x̄)² > 0  and  ∂²S/∂β₀² = 2n > 0

∴ (b₀, b₁) is a GLOBAL MINIMUM  ✅
```

### Fitted Values and Residuals

```
Fitted line:    ŷ = b₀ + b₁·x
Predicted:      ŷᵢ = b₀ + b₁·xᵢ
Residuals:      eᵢ = yᵢ − ŷᵢ = yᵢ − b₀ − b₁·xᵢ
```

---

## B4 | Properties of OLS Estimators & Gauss-Markov

[⬆️ Back to Top](#-table-of-contents)

### Unbiasedness Proofs

**b₁ is unbiased:**

b₁ can be written as a linear function of yᵢ: `b₁ = Σ kᵢyᵢ` where `kᵢ = (xᵢ − x̄)/sxx`

```
E(b₁) = Σ kᵢ · E(yᵢ) = Σ kᵢ(β₀ + β₁xᵢ)

Since Σkᵢ = 0 and Σkᵢxᵢ = 1:

E(b₁) = β₀·(0) + β₁·(1) = β₁  ✅
```

**b₀ is unbiased:**
```
E(b₀) = E(ȳ − b₁·x̄) = E(ȳ) − x̄·E(b₁) = (β₀+β₁x̄) − x̄·β₁ = β₀  ✅
```

### Variances of OLS Estimators

```
┌──────────────────────────────────────────────────┐
│                                                  │
│  Var(b₁) = σ²/sxx                                │
│                                                  │
│  Var(b₀) = σ²·(1/n + x̄²/sxx)                     │
│                                                  │
│  Cov(b₀, b₁) = −x̄·σ²/sxx                         │
│                                                  │
│  Cov(ȳ, b₁) = 0                                  │
│                                                  │
└──────────────────────────────────────────────────┘
```

### Gauss-Markov Theorem (BLUE)

```
┌──────────────────────────────────────────────────────┐
│  GAUSS-MARKOV THEOREM                                │
│                                                      │
│  Under assumptions E(ε)=0, Var(ε)=σ², εᵢ indep:      │
│                                                      │
│  OLS estimators b₀ and b₁ are BLUE:                  │
│    B — Best (minimum variance)                       │
│    L — Linear (in yᵢ)                                │
│    U — Unbiased (E(b)=β)                             │
│    E — Estimator                                     │
│                                                      │
│  Among ALL linear unbiased estimators, OLS has       │
│  the SMALLEST variance.                              │
└──────────────────────────────────────────────────────┘
```

---

## B5 | Residual Analysis

[⬆️ Back to Top](#-table-of-contents)

### Residual Sum of Squares

```
SSres = Σeᵢ² = Σ(yᵢ − ŷᵢ)²

Alternative forms:
  SSres = syy − b₁²·sxx = syy − sxy²/sxx = syy − b₁·sxy
```

### Properties of OLS Residuals

```
┌──────────────────────────────────────┐
│  1.  Σeᵢ = 0      (sum to zero)      │
│  2.  Σxᵢeᵢ = 0    (uncorrelated      │
│  3.  Σŷᵢeᵢ = 0     with X and ŷ)     │
│  4.  Σyᵢ = Σŷᵢ    (totals match)     │
│  5.  Line passes through (x̄, ȳ)      │
└──────────────────────────────────────┘
```

### Estimation of σ²

Under normality: `SSres/σ² ~ χ²(n−2)`

```
s² = SSres/(n−2) = MSE    ← Unbiased estimator of σ²

Degrees of freedom: n − 2 (lost 2 for estimating b₀ and b₁)
```

**Estimated variances of estimators:**
```
V̂ar(b₁) = s²/sxx
V̂ar(b₀) = s²·(1/n + x̄²/sxx)
```

---

## B6 | Centered Model & No-Intercept Model

[⬆️ Back to Top](#-table-of-contents)

### Centered Model

Replace xᵢ with (xᵢ − x̄):

```
yᵢ = β₀* + β₁(xᵢ − x̄) + εᵢ    where β₀* = β₀ + β₁x̄
```

**OLS estimates:**
```
b₀* = ȳ           (just the mean!)
b₁  = sxy/sxx     (same slope as before)
```

**Advantage:**
```
Cov(b₀*, b₁) = 0    ← Intercept and slope are UNCORRELATED!
Var(b₀*) = σ²/n     ← Simpler variance formula
```

### No-Intercept (Through Origin) Model

When theory says Y = 0 when X = 0:

```
yᵢ = β₁xᵢ + εᵢ    (no β₀)
```

**OLS estimator:**
```
b₁* = Σyᵢxᵢ / Σxᵢ²

E(b₁*) = β₁  (unbiased)
Var(b₁*) = σ² / Σxᵢ²
```

> Example: velocity = 0 when acceleration = 0

---

## B7 | Maximum Likelihood Estimation for Regression

[⬆️ Back to Top](#-table-of-contents)

**Assumption:** εᵢ ~iid~ N(0, σ²)

**Log-likelihood:**
```
ln L = −(n/2)ln(2π) − (n/2)ln(σ²) − (1/2σ²)·Σ(yᵢ − β₀ − β₁xᵢ)²
```

**MLE results:**

| Parameter | MLE | Same as OLS? |
|-----------|-----|-------------|
| β₁ | b̃₁ = sxy/sxx | ✅ Yes |
| β₀ | b̃₀ = ȳ − b̃₁x̄ | ✅ Yes |
| σ² | s̃² = SSres/n | ❌ No (biased!) |

**MLE vs OLS for σ²:**
```
s̃² = (n−2)/n · s²

s̃² is biased (divides by n) BUT has lower variance
s²  is unbiased (divides by n−2) BUT has higher variance
```

---

## B8 | Hypothesis Testing (β₀, β₁, σ²)

[⬆️ Back to Top](#-table-of-contents)

### Testing β₁ (Slope)

**H₀: β₁ = β₁₀  vs  H₁: β₁ ≠ β₁₀**

| σ² Known | σ² Unknown |
|----------|-----------|
| Z = (b₁−β₁₀)/√(σ²/sxx) | t = (b₁−β₁₀)/√(s²/sxx) |
| Z ~ N(0,1) under H₀ | t ~ t(n−2) under H₀ |
| Reject if \|Z\| > z_α/2 | Reject if \|t\| > t_(n−2,α/2) |

**CI for β₁ (σ² unknown):**
```
b₁ ± t_(n−2,α/2) · √(s²/sxx)
```

### Testing β₀ (Intercept)

**H₀: β₀ = β₀₀  vs  H₁: β₀ ≠ β₀₀**

```
t = (b₀ − β₀₀) / √[s²·(1/n + x̄²/sxx)]  ~  t(n−2)
```

**CI for β₀:**
```
b₀ ± t_(n−2,α/2) · √[s²·(1/n + x̄²/sxx)]
```

### Testing σ²

**H₀: σ² = σ₀²  vs  H₁: σ² ≠ σ₀²**

```
C₀ = SSres/σ₀²  ~  χ²(n−2)

Reject if C₀ < χ²_(n−2,α/2) or C₀ > χ²_(n−2,1−α/2)
```

**CI for σ²:**
```
[SSres/χ²_(n−2,1−α/2),  SSres/χ²_(n−2,α/2)]
```

### Joint Confidence Region for (β₀, β₁)

Using centered model:
```
[(n−2)/2] · Qf/SSres ≤ F_(2,n−2;1−α)
```

This defines an **ellipse** in (β₀, β₁) space.

---

## B9 | ANOVA & R² (Coefficient of Determination)

[⬆️ Back to Top](#-table-of-contents)

### ANOVA Decomposition

```
(yᵢ − ȳ) = (ŷᵢ − ȳ) + (yᵢ − ŷᵢ)
 Total      Explained   Unexplained

Σ(yᵢ−ȳ)² = Σ(ŷᵢ−ȳ)² + Σ(yᵢ−ŷᵢ)²
   syy    =   SSreg   +   SSres
```

### ANOVA Table

| Source | SS | df | MS | F |
|--------|----|----|----|----|
| **Regression** | SSreg = b₁·sxy | 1 | MSreg = SSreg/1 | F₀ = MSreg/MSE |
| **Residual** | SSres = syy − b₁·sxy | n−2 | MSE = SSres/(n−2) | |
| **Total** | syy | n−1 | | |

**F-test for H₀: β₁ = 0:**
```
F₀ = MSreg/MSE ~ F(1, n−2) under H₀
Reject H₀ if F₀ > F_(1,n−2;1−α)
```

### R² — Coefficient of Determination

```
┌───────────────────────────────────────────┐
│                                           │
│  R² = SSreg/syy = 1 − SSres/syy = r²xy    │
│                                           │
│  0 ≤ R² ≤ 1                               │
│                                           │
└───────────────────────────────────────────┘
```

> R² × 100% of the variation in Y is explained by X.

**Alternative expressions for SSreg:**
```
SSreg = b₁²·sxx = b₁·sxy = sxy²/sxx
```

---

## B10 | Prediction — Mean Response & New Observation

[⬆️ Back to Top](#-table-of-contents)

### Two Types of Prediction

| Predicting | Formula | Variance |
|-----------|---------|----------|
| **Mean response** E(y\|x₀) | µ̂ = b₀ + b₁x₀ | σ²·[1/n + (x₀−x̄)²/sxx] |
| **New observation** y₀ | ŷ₀ = b₀ + b₁x₀ | σ²·[**1** + 1/n + (x₀−x̄)²/sxx] |

> The new observation interval is **wider** because it includes the extra ε₀ variability.

### Confidence Interval for Mean Response

```
µ̂_(y|x₀) ± t_(n−2,α/2) · √[MSE · (1/n + (x₀−x̄)²/sxx)]
```

### Prediction Interval for New Observation

```
ŷ₀ ± t_(n−2,α/2) · √[MSE · (1 + 1/n + (x₀−x̄)²/sxx)]
```

### Key Insight: Width of Intervals

```
Narrow ◄────── x₀ = x̄ ──────► Wide

  Width is MINIMUM at x₀ = x̄ (centre of data)
  Width INCREASES as |x₀ − x̄| increases

  "The further you extrapolate, the less reliable!"
```

```
  Y|
   |  ╱‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾╲   ← Prediction band (new obs)
   | ╱  ╱‾‾‾‾‾‾‾‾‾‾‾╲    ╲  ← Confidence band (mean)
   |╱  ╱   ───────────  ╲  ╲ ← Fitted line
   |╲  ╲  ─────────── ╱  ╱
   | ╲  ╲_____________╱  ╱
   |  ╲_________________╱
   └────────────────────── X
             x̄
```

---

## B11 | Alternative Regression Methods

[⬆️ Back to Top](#-table-of-contents)

### 1. Reverse Regression (X on Y)

```
xᵢ = β₀* + β₁*·yᵢ + δᵢ

β̂_IR = sxy/syy
β̂_OR = x̄ − β̂_IR·ȳ

Relationship: β̂_IR · b₁ = r²xy
```

> Used in salary discrimination studies and calibration problems.

### 2. Orthogonal (Major Axis) Regression

Minimises perpendicular distances — used when **both X and Y have errors**.

```
β̂₁_OR = [(syy − sxx) + sign(sxy)·√((sxx−syy)² + 4sxy²)] / (2sxy)
β̂₀_OR = ȳ − β̂₁_OR·x̄
```

### 3. Reduced Major Axis Regression

Minimises rectangle areas:

```
β̂₁_RM = sign(sxy) · √(syy/sxx)
β̂₀_RM = ȳ − β̂₁_RM·x̄
```

### 4. Least Absolute Deviation (LAD) Regression

```
Minimise: Σ|yᵢ − β₀ − β₁xᵢ|
```

Properties: More **robust to outliers** than OLS, but no closed-form solution (needs algorithms).

---

## B12 | Stochastic X

[⬆️ Back to Top](#-table-of-contents)

When X is random (not fixed by experimenter), assume (X, Y) ~ Bivariate Normal:

```
N(µx, µy, σx², σy², ρ)
```

**Conditional distribution:**
```
E(y|X=x) = β₀ + β₁x    where β₁ = (σy/σx)·ρ,  β₀ = µy − µx·β₁
Var(y|X=x) = σy²(1 − ρ²)
```

**Sample correlation:**
```
ρ̂ = sxy/√(sxx·syy) = b₁·√(sxx/syy)

ρ̂² = R²
```

> **Key result:** OLS estimators remain valid even when X is random.

---

# PART C — REFERENCE

---

## C1 | Master Formula Sheet

[⬆️ Back to Top](#-table-of-contents)

```
╔═══════════════════════════════════════════════════════════════════╗
║            PARAMETER ESTIMATION FORMULAS                          ║
╠═══════════════════════════════════════════════════════════════════╣
║ Bias(θ̂) = E(θ̂) − θ                                                ║
║ Var(θ̂) = E[(θ̂ − E(θ̂))²]                                           ║
║ MSE(θ̂) = Bias² + Var = E[(θ̂ − θ)²]                                ║
║ SE(θ̂) = √Var(θ̂)                                                   ║
║                                                                   ║
║ Var(x̄) = σ²/n                                                     ║
║ E(s²) = σ²   (unbiased, divides by n−1)                           ║
║ E(s̃²) = (n−1)/n · σ²   (biased, divides by n)                     ║
║                                                                   ║
║ MLE: θ̂ = argmax Σ log f(xᵢ|θ)                                     ║
╠═══════════════════════════════════════════════════════════════════╣
║            SIMPLE LINEAR REGRESSION FORMULAS                      ║
╠═══════════════════════════════════════════════════════════════════╣
║ MODEL:   y = β₀ + β₁x + ε                                         ║
║ FITTED:  ŷ = b₀ + b₁x                                             ║
║                                                                   ║
║ SLOPE:   b₁ = sxy/sxx                                             ║
║ INTERCEPT: b₀ = ȳ − b₁x̄                                           ║
║                                                                   ║
║ sxx = Σ(xᵢ−x̄)² = Σxᵢ² − (Σxᵢ)²/n                                  ║
║ syy = Σ(yᵢ−ȳ)² = Σyᵢ² − (Σyᵢ)²/n                                  ║
║ sxy = Σ(xᵢ−x̄)(yᵢ−ȳ) = Σxᵢyᵢ − (Σxᵢ)(Σyᵢ)/n                        ║
║                                                                   ║
║ Var(b₁) = σ²/sxx                                                  ║
║ Var(b₀) = σ²(1/n + x̄²/sxx)                                        ║
║ Cov(b₀,b₁) = −x̄σ²/sxx                                             ║
║                                                                   ║
║ SSres = syy − b₁·sxy        s² = MSE = SSres/(n−2)                ║
║ SSreg = b₁·sxy              SSres/σ² ~ χ²(n−2)                    ║
║ syy = SSreg + SSres                                               ║
║                                                                   ║
║ R² = SSreg/syy = 1 − SSres/syy = r²                               ║
║ r = sxy/√(sxx·syy)                                                ║
║                                                                   ║
║ t-test β₁: t = (b₁−β₁₀)/√(s²/sxx) ~ t(n−2)                        ║
║ t-test β₀: t = (b₀−β₀₀)/√[s²(1/n+x̄²/sxx)] ~ t(n−2)                ║
║ χ²-test σ²: C = SSres/σ₀² ~ χ²(n−2)                               ║
║ F-test β₁=0: F = MSreg/MSE ~ F(1,n−2)                             ║
║                                                                   ║
║ CI mean:  µ̂±t·√[MSE(1/n+(x₀−x̄)²/sxx)]                             ║
║ PI new:   ŷ₀±t·√[MSE(1+1/n+(x₀−x̄)²/sxx)]                          ║
║                                                                   ║
║ MLE σ²: s̃² = SSres/n = (n−2)/n·s²  (biased)                       ║
╚═══════════════════════════════════════════════════════════════════╝
```

---

## C2 | Complete Notations Table

[⬆️ Back to Top](#-table-of-contents)

| Notation | Name | Meaning |
|----------|------|---------|
| θ | Parameter | Unknown population quantity |
| θ̂ | Estimate (theta-hat) | Sample-based approximation of θ |
| g(·) | Estimator | The function/rule applied to data |
| X | Random variable / Independent var | Input |
| Y, y | Dependent variable | Output |
| x̄, ȳ | Sample means | (1/n)Σxᵢ, (1/n)Σyᵢ |
| µ | Population mean | E(X) |
| σ² | Population variance | E[(X−µ)²] |
| s² | Sample variance (unbiased) | Σ(xᵢ−x̄)²/(n−1) |
| s̃² | Sample variance (MLE) | Σ(xᵢ−x̄)²/n |
| β₀, β₁ | Population regression coefficients | True intercept & slope |
| b₀, b₁ | OLS estimates | Calculated from data |
| b̃₀, b̃₁ | MLE of regression coefficients | Same as b₀, b₁ |
| εᵢ | True error | yᵢ − β₀ − β₁xᵢ (unobservable) |
| eᵢ | Residual | yᵢ − ŷᵢ (observable) |
| ŷᵢ | Fitted/predicted value | b₀ + b₁xᵢ |
| sxx | Sum of squares X | Σ(xᵢ−x̄)² |
| syy | Sum of squares Y | Σ(yᵢ−ȳ)² |
| sxy | Cross-product sum | Σ(xᵢ−x̄)(yᵢ−ȳ) |
| SSreg | Regression sum of squares | b₁·sxy |
| SSres | Residual sum of squares | syy − b₁·sxy |
| MSE | Mean squared error (residual) | SSres/(n−2) |
| R² | Coefficient of determination | SSreg/syy |
| r | Correlation coefficient | sxy/√(sxx·syy) |
| ρ | Population correlation | σxy/(σx·σy) |
| kᵢ | Weights for b₁ | (xᵢ−x̄)/sxx |
| L(θ\|x) | Likelihood function | ∏f(xᵢ\|θ) |
| ℓ(θ\|x) | Log-likelihood | Σlog f(xᵢ\|θ) |
| BLUE | Best Linear Unbiased Estimator | OLS by Gauss-Markov |
| iid | Independent & identically distributed | Standard assumption |
| CLT | Central Limit Theorem | x̄ → Normal for large n |

---

## C3 | Mnemonics & Memory Tricks

[⬆️ Back to Top](#-table-of-contents)

| # | Mnemonic | What It Helps Remember |
|---|----------|----------------------|
| 1 | **"BLUE"** | Best Linear Unbiased Estimator (Gauss-Markov) |
| 2 | **"MSE = B² + V"** | MSE = Bias² + Variance (the decomposition) |
| 3 | **"S before I"** | Calculate Slope (b₁) before Intercept (b₀) |
| 4 | **"Cross over Self"** | b₁ = sxy/sxx (cross-product / self-product) |
| 5 | **"L.I.N.E."** | Linearity, Independence, Normality, Equal variance |
| 6 | **"TRE" = Tree 🌳** | SST = SSR + SSE (Total = Regression + Error) |
| 7 | **"R² = Report Card"** | R² is your model's grade (0–100%) |
| 8 | **"n−1 for freedom, n−2 for regression"** | df for s² vs MSE |
| 9 | **"Hat = Estimate"** | θ̂ = estimate of θ, ŷ = predicted y |
| 10 | **"MLE loves n, OLS loves n−2"** | MLE divides by n (biased), OLS by n−2 (unbiased) |
| 11 | **"Further = Fatter"** | Prediction intervals widen as x₀ moves from x̄ |
| 12 | **"New obs = 1 extra"** | PI for new obs has extra "1+" inside the root |

---


**📝 See the companion file: [Practice Problems](./simple_linear_regression_pe_practice.md)**
