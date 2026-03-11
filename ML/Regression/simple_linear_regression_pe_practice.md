# 📝 Practice Problems — Simple Linear Regression (SLR) & Parameter Estimation (PE)

> **Companion to:** [Theory Guide](./simple_linear_regression_pe_theory.md)  
> **Subject:** Machine Learning | AI

---

## 📑 Problem Index

| # | Topic | Difficulty | Jump To |
|---|-------|-----------|---------|
| **PART A — PARAMETER ESTIMATION** | | | |
| P1 | [Bias & Unbiasedness](#p1--bias--unbiasedness) | ⭐ Easy | |
| P2 | [MSE Decomposition](#p2--mse-decomposition) | ⭐⭐ Medium | |
| P3 | [Method of Moments](#p3--method-of-moments) | ⭐⭐ Medium | |
| P4 | [MLE — Normal Distribution](#p4--mle--normal-distribution) | ⭐⭐ Medium | |
| P5 | [MLE — Binomial & Uniform](#p5--mle--binomial--uniform) | ⭐⭐⭐ Hard | |
| **PART B — SIMPLE LINEAR REGRESSION** | | | |
| P6 | [Basic OLS Computation](#p6--basic-ols-computation) | ⭐ Easy | |
| P7 | [Correlation & R²](#p7--correlation--r) | ⭐ Easy | |
| P8 | [Residual Properties](#p8--residual-properties) | ⭐⭐ Medium | |
| P9 | [Hypothesis Testing (t-test, F-test)](#p9--hypothesis-testing) | ⭐⭐⭐ Hard | |
| P10 | [Prediction Intervals](#p10--prediction-intervals) | ⭐⭐⭐ Hard | |
| P11 | [Centered & No-Intercept Models](#p11--centered--no-intercept-models) | ⭐⭐ Medium | |
| P12 | [MLE vs OLS Comparison](#p12--mle-vs-ols-comparison) | ⭐⭐ Medium | |
| P13 | [Conceptual True/False](#p13--conceptual-truefalse) | ⭐ Exam Prep | |
| P14 | [ANOVA Table Construction](#p14--anova-table-construction) | ⭐⭐⭐ Hard | |

---

# PART A — PARAMETER ESTIMATION PROBLEMS

---

## P1 | Bias & Unbiasedness
⭐ Easy

[⬆️ Back to Index](#-problem-index)

### Problem

Given: X₁, X₂, ..., Xₙ ~iid~ F with E(Xᵢ) = µ and Var(Xᵢ) = σ²

Consider three estimators of µ:

- **T₁** = X₁ (just the first observation)
- **T₂** = (1/n)ΣXᵢ = X̄ (sample mean)
- **T₃** = (X₁ + Xₙ)/2 (average of first and last)

**(a)** Show that all three are unbiased for µ  
**(b)** Find Var(T₁), Var(T₂), Var(T₃)  
**(c)** Which is the most efficient? Why?

---

### Solution

**(a) Unbiasedness:**

```
E(T₁) = E(X₁) = µ  ✅

E(T₂) = E(1/n · ΣXᵢ) = 1/n · nµ = µ  ✅

E(T₃) = E[(X₁+Xₙ)/2] = (µ+µ)/2 = µ  ✅
```

All three are unbiased.

**(b) Variances:**

```
Var(T₁) = Var(X₁) = σ²

Var(T₂) = Var(X̄) = σ²/n

Var(T₃) = Var[(X₁+Xₙ)/2] = (1/4)[Var(X₁) + Var(Xₙ)]
         = (1/4)(σ² + σ²) = σ²/2
```

**(c) Efficiency comparison:**

```
Var(T₁) = σ²          ← Worst (uses only 1 observation!)
Var(T₃) = σ²/2        ← Better (uses 2 observations)
Var(T₂) = σ²/n        ← BEST (uses ALL n observations)
```

> T₂ = X̄ is the most efficient. For n > 2, it has the smallest variance. This aligns with Gauss-Markov: the sample mean is BLUE for estimating µ.

---

## P2 | MSE Decomposition
⭐⭐ Medium

[⬆️ Back to Index](#-problem-index)

### Problem

Let X₁, ..., Xₙ ~iid~ N(µ, σ²).

Consider two estimators of σ²:
- s² = Σ(Xᵢ − X̄)²/(n−1) (unbiased)
- s̃² = Σ(Xᵢ − X̄)²/n (MLE)

**(a)** Find Bias(s²) and Bias(s̃²)  
**(b)** Which has lower MSE for small n? (Hint: use MSE = Bias² + Var)

---

### Solution

**(a) Bias:**

```
E(s²) = σ²  →  Bias(s²) = 0  (unbiased)

E(s̃²) = (n−1)/n · σ²  →  Bias(s̃²) = (n−1)/n · σ² − σ² = −σ²/n
```

**(b) MSE comparison:**

For normal distribution, Var(s²) = 2σ⁴/(n−1):

```
MSE(s²) = 0² + 2σ⁴/(n−1) = 2σ⁴/(n−1)

For s̃²:
Var(s̃²) = ((n−1)/n)² · 2σ⁴/(n−1) = 2(n−1)σ⁴/n²

MSE(s̃²) = (σ²/n)² + 2(n−1)σ⁴/n²
         = σ⁴/n² + 2(n−1)σ⁴/n²
         = (2n−1)σ⁴/n²
```

**Comparison:**
```
MSE(s²) = 2σ⁴/(n−1)      MSE(s̃²) = (2n−1)σ⁴/n²

For n=5:
MSE(s²) = 2σ⁴/4 = 0.500σ⁴
MSE(s̃²) = 9σ⁴/25 = 0.360σ⁴  ← LOWER!
```

> s̃² (the biased MLE) has **lower MSE** than s² for all finite n. This demonstrates the bias-variance tradeoff: a little bias can reduce overall error.

---

## P3 | Method of Moments
⭐⭐ Medium

[⬆️ Back to Index](#-problem-index)

### Problem

Data: X₁ = 3, X₂ = 7, X₃ = 5, X₄ = 9, X₅ = 6

**(a)** Find MoM estimates of µ and σ² assuming X ~ N(µ, σ²)  
**(b)** Find MoM estimates of a and b assuming X ~ Uniform[a, b]

---

### Solution

**Compute sample moments:**
```
µ̂₁ = x̄ = (3+7+5+9+6)/5 = 30/5 = 6

µ̂₂ = (1/n)Σxᵢ² = (9+49+25+81+36)/5 = 200/5 = 40
```

**(a) Normal MoM:**
```
µ̂ = µ̂₁ = 6

σ̂² = µ̂₂ − µ̂₁² = 40 − 36 = 4
```

**(b) Uniform MoM:**
```
â = µ̂₁ − √3·√(µ̂₂ − µ̂₁²) = 6 − √3·√4 = 6 − 2√3 ≈ 2.536

b̂ = µ̂₁ + √3·√(µ̂₂ − µ̂₁²) = 6 + √3·√4 = 6 + 2√3 ≈ 9.464
```

> Check: (â+b̂)/2 = 6 = x̄ ✅

---

## P4 | MLE — Normal Distribution
⭐⭐ Medium

[⬆️ Back to Index](#-problem-index)

### Problem

Given data: 12, 15, 18, 14, 16 from a Normal distribution.

**(a)** Derive the MLE for µ (show steps from log-likelihood)  
**(b)** Compute µ̂_MLE and σ̂²_MLE  
**(c)** Compare σ̂²_MLE with s² (unbiased estimator)

---

### Solution

**(a) Derivation:**
```
Log-likelihood:
ℓ = −(1/2σ²)Σ(xᵢ−µ)² − (n/2)log(σ²) − (n/2)log(2π)

∂ℓ/∂µ = (1/σ²)Σ(xᵢ−µ) = 0
       → Σxᵢ − nµ = 0
       → µ̂ = (1/n)Σxᵢ = x̄
```

**(b) Computation:**
```
x̄ = (12+15+18+14+16)/5 = 75/5 = 15

σ̂²_MLE = (1/n)Σ(xᵢ−x̄)²
        = (1/5)[(12−15)²+(15−15)²+(18−15)²+(14−15)²+(16−15)²]
        = (1/5)[9+0+9+1+1]
        = 20/5 = 4
```

**(c) Comparison:**
```
s² = (1/(n−1))Σ(xᵢ−x̄)² = 20/4 = 5

σ̂²_MLE = 4     (biased, divides by n=5)
s²      = 5     (unbiased, divides by n−1=4)

Relationship: σ̂²_MLE = (n−2)/n · s²? NO!
Correct:      σ̂²_MLE = (n−1)/n · s² = (4/5)·5 = 4  ✅
```

---

## P5 | MLE — Binomial & Uniform
⭐⭐⭐ Hard

[⬆️ Back to Index](#-problem-index)

### Problem A (Binomial)

In 4 independent experiments with N = 10 trials each, the number of successes are: X₁=3, X₂=5, X₃=4, X₄=6. Find the MLE of p.

### Problem B (Uniform)

Data: 2.1, 4.7, 1.3, 5.8, 3.2 from U[a,b]. Find MLEs of a and b.

---

### Solution A

```
x̄ = (3+5+4+6)/4 = 18/4 = 4.5

p̂_MLE = x̄/N = 4.5/10 = 0.45
```

### Solution B

```
â_MLE = min(xᵢ) = x₍₁₎ = 1.3
b̂_MLE = max(xᵢ) = x₍ₙ₎ = 5.8
```

> For Uniform, MLE simply uses the smallest and largest observations.

---

# PART B — SIMPLE LINEAR REGRESSION PROBLEMS

---

## P6 | Basic OLS Computation
⭐ Easy

[⬆️ Back to Index](#-problem-index)

### Problem

| X | 2 | 4 | 6 | 8 | 10 |
|---|---|---|---|---|---|
| Y | 5 | 9 | 13 | 18 | 22 |

**(a)** Compute b₁, b₀, and the regression equation  
**(b)** Predict Y when X = 12  
**(c)** Compute R²  
**(d)** Compute SSres and estimate σ² (MSE)

---

### Solution

**Step 1: Means**
```
n = 5,  x̄ = 30/5 = 6,  ȳ = 67/5 = 13.4
```

**Step 2: Calculation table**

| xᵢ | yᵢ | xᵢ−x̄ | yᵢ−ȳ | (xᵢ−x̄)(yᵢ−ȳ) | (xᵢ−x̄)² | (yᵢ−ȳ)² |
|----|-----|-------|-------|----------------|----------|----------|
| 2 | 5 | −4 | −8.4 | 33.6 | 16 | 70.56 |
| 4 | 9 | −2 | −4.4 | 8.8 | 4 | 19.36 |
| 6 | 13 | 0 | −0.4 | 0 | 0 | 0.16 |
| 8 | 18 | 2 | 4.6 | 9.2 | 4 | 21.16 |
| 10 | 22 | 4 | 8.6 | 34.4 | 16 | 73.96 |
| **Σ** | | **0** | **0** | **sxy=86** | **sxx=40** | **syy=185.2** |

**(a) Regression:**
```
b₁ = sxy/sxx = 86/40 = 2.15
b₀ = ȳ − b₁x̄ = 13.4 − 2.15×6 = 13.4 − 12.9 = 0.5

ŷ = 0.5 + 2.15x
```

**(b) Prediction:**
```
ŷ(12) = 0.5 + 2.15×12 = 0.5 + 25.8 = 26.3
```

**(c) R²:**
```
SSreg = b₁·sxy = 2.15 × 86 = 184.9
R² = SSreg/syy = 184.9/185.2 = 0.9984 (99.84%)
```

**(d) σ² estimation:**
```
SSres = syy − SSreg = 185.2 − 184.9 = 0.3
s² = MSE = SSres/(n−2) = 0.3/3 = 0.1
```

---

## P7 | Correlation & R²
⭐ Easy

[⬆️ Back to Index](#-problem-index)

### Problem

| X | 1 | 3 | 5 | 7 | 9 |
|---|---|---|---|---|---|
| Y | 8 | 6 | 5 | 3 | 1 |

**(a)** Compute r  
**(b)** What does it tell you?  
**(c)** Compute R² and interpret  

---

### Solution

```
x̄ = 5,  ȳ = 23/5 = 4.6

sxy = (1−5)(8−4.6)+(3−5)(6−4.6)+(5−5)(5−4.6)+(7−5)(3−4.6)+(9−5)(1−4.6)
    = (−4)(3.4)+(−2)(1.4)+(0)(0.4)+(2)(−1.6)+(4)(−3.6)
    = −13.6 − 2.8 + 0 − 3.2 − 14.4 = −34

sxx = 16 + 4 + 0 + 4 + 16 = 40
syy = 11.56 + 1.96 + 0.16 + 2.56 + 12.96 = 29.2
```

**(a):**
```
r = sxy/√(sxx·syy) = −34/√(40×29.2) = −34/√1168 = −34/34.176 ≈ −0.995
```

**(b):** Very strong negative linear relationship. As X↑, Y↓ almost perfectly.

**(c):**
```
R² = r² = (−0.995)² ≈ 0.990 (99.0%)

99% of Y's variation is explained by X.
```

---

## P8 | Residual Properties
⭐⭐ Medium

[⬆️ Back to Index](#-problem-index)

### Problem

Using the regression from P6 (ŷ = 0.5 + 2.15x):

**(a)** Compute all residuals eᵢ  
**(b)** Verify that Σeᵢ = 0  
**(c)** Verify that Σxᵢeᵢ = 0  
**(d)** Verify that Σyᵢ = Σŷᵢ  

---

### Solution

| xᵢ | yᵢ | ŷᵢ = 0.5+2.15xᵢ | eᵢ = yᵢ−ŷᵢ |
|----|-----|------------------|-------------|
| 2 | 5 | 4.80 | 0.20 |
| 4 | 9 | 9.10 | −0.10 |
| 6 | 13 | 13.40 | −0.40 |
| 8 | 18 | 17.70 | 0.30 |
| 10 | 22 | 22.00 | 0.00 |

**(b)** Σeᵢ = 0.20 − 0.10 − 0.40 + 0.30 + 0.00 = **0** ✅

**(c)** Σxᵢeᵢ = 2(0.20) + 4(−0.10) + 6(−0.40) + 8(0.30) + 10(0)
= 0.40 − 0.40 − 2.40 + 2.40 + 0 = **0** ✅

**(d)** Σyᵢ = 67, Σŷᵢ = 4.80+9.10+13.40+17.70+22.00 = **67.00** ✅

---

## P9 | Hypothesis Testing
⭐⭐⭐ Hard

[⬆️ Back to Index](#-problem-index)

### Problem

Using results from P6: b₁ = 2.15, b₀ = 0.5, s² = 0.1, sxx = 40, n = 5

**(a)** Test H₀: β₁ = 0 vs H₁: β₁ ≠ 0 at α = 0.05 using t-test  
**(b)** Construct a 95% CI for β₁  
**(c)** Perform the F-test for overall significance  
**(d)** Test H₀: β₀ = 0 at α = 0.05  

---

### Solution

**(a) t-test for β₁:**
```
SE(b₁) = √(s²/sxx) = √(0.1/40) = √0.0025 = 0.05

t₀ = (b₁ − 0)/SE(b₁) = 2.15/0.05 = 43.0

df = n−2 = 3,  t_(3, 0.025) ≈ 3.182

|t₀| = 43.0 >> 3.182  →  REJECT H₀ ✅

β₁ is highly significant — X strongly predicts Y.
```

**(b) 95% CI for β₁:**
```
b₁ ± t_(3,0.025) · SE(b₁) = 2.15 ± 3.182 × 0.05
                            = 2.15 ± 0.159
                            = [1.991, 2.309]
```

**(c) F-test:**
```
SSreg = 184.9,  MSreg = 184.9/1 = 184.9
SSres = 0.3,    MSE = 0.3/3 = 0.1

F₀ = MSreg/MSE = 184.9/0.1 = 1849.0

F_(1,3;0.95) ≈ 10.13

F₀ = 1849 >> 10.13  →  REJECT H₀ ✅

Note: F₀ = t₀² = 43² = 1849 ✅ (relationship between t and F tests)
```

**(d) t-test for β₀:**
```
SE(b₀) = √[s²(1/n + x̄²/sxx)] = √[0.1(1/5 + 36/40)]
       = √[0.1(0.2 + 0.9)] = √[0.1 × 1.1] = √0.11 ≈ 0.3317

t₀ = (0.5 − 0)/0.3317 = 1.507

|t₀| = 1.507 < 3.182 = t_(3,0.025)  →  FAIL TO REJECT H₀

β₀ is NOT significantly different from 0 at α = 0.05.
```

---

## P10 | Prediction Intervals
⭐⭐⭐ Hard

[⬆️ Back to Index](#-problem-index)

### Problem

Using P6 results. For x₀ = 7:

**(a)** Find the predicted value  
**(b)** Construct 95% CI for the **mean response** E(y|x₀=7)  
**(c)** Construct 95% PI for a **new observation** at x₀=7  
**(d)** Why is (c) wider than (b)?

---

### Solution

**(a):**
```
ŷ₀ = 0.5 + 2.15(7) = 0.5 + 15.05 = 15.55
```

**(b) CI for mean response:**
```
SE_mean = √[MSE(1/n + (x₀−x̄)²/sxx)]
        = √[0.1(1/5 + (7−6)²/40)]
        = √[0.1(0.2 + 0.025)]
        = √[0.1 × 0.225] = √0.0225 = 0.15

CI: 15.55 ± 3.182 × 0.15 = 15.55 ± 0.477
    = [15.073, 16.027]
```

**(c) PI for new observation:**
```
SE_new = √[MSE(1 + 1/n + (x₀−x̄)²/sxx)]
       = √[0.1(1 + 0.2 + 0.025)]
       = √[0.1 × 1.225] = √0.1225 = 0.35

PI: 15.55 ± 3.182 × 0.35 = 15.55 ± 1.114
    = [14.436, 16.664]
```

**(d):** The PI for a new observation is wider because it includes the extra variability (σ²) from the new error term ε₀. The mean response CI only captures uncertainty in the estimated line, while the new observation PI also captures the random scatter around that line.

---

## P11 | Centered & No-Intercept Models
⭐⭐ Medium

[⬆️ Back to Index](#-problem-index)

### Problem

Using the P6 data (x̄ = 6, ȳ = 13.4):

**(a)** Write the centered model and find its estimates  
**(b)** Verify Cov(b₀*, b₁) = 0 conceptually  
**(c)** If theory says Y = 0 when X = 0, find the no-intercept estimate b₁*

---

### Solution

**(a) Centered model:**
```
yᵢ = β₀* + β₁(xᵢ − 6) + εᵢ

b₀* = ȳ = 13.4
b₁ = sxy/sxx = 86/40 = 2.15  (same slope!)

Fitted: ŷ = 13.4 + 2.15(x − 6)
```

**(b):** In the centered model, the intercept estimate is simply ȳ (a constant from data), independent of the slope calculation. Since centering removes the correlation between x̄ and the deviation terms, Cov(b₀*, b₁) = 0.

**(c) No-intercept model:**
```
b₁* = Σyᵢxᵢ / Σxᵢ²

Σyᵢxᵢ = 2(5)+4(9)+6(13)+8(18)+10(22) = 10+36+78+144+220 = 488
Σxᵢ² = 4+16+36+64+100 = 220

b₁* = 488/220 = 2.218

Fitted: ŷ = 2.218x  (line through origin)
```

---

## P12 | MLE vs OLS Comparison
⭐⭐ Medium

[⬆️ Back to Index](#-problem-index)

### Problem

Using P6 data where SSres = 0.3, n = 5:

**(a)** Compute the OLS estimate of σ² (s²)  
**(b)** Compute the MLE of σ² (s̃²)  
**(c)** Verify the relationship s̃² = (n−2)/n · s²  
**(d)** Which is unbiased? Which has lower variance?

---

### Solution

**(a):**
```
s² = SSres/(n−2) = 0.3/3 = 0.1
```

**(b):**
```
s̃² = SSres/n = 0.3/5 = 0.06
```

**(c):**
```
(n−2)/n · s² = (3/5) × 0.1 = 0.06 = s̃²  ✅
```

**(d):**
```
s² = 0.1   → Unbiased (E(s²) = σ²)  ✅
s̃² = 0.06  → Biased (E(s̃²) = (n−2)/n · σ²)

But Var(s̃²) < Var(s²) — MLE has lower variance despite being biased.
```

---

## P13 | Conceptual True/False
⭐ Exam Prep

[⬆️ Back to Index](#-problem-index)

| # | Statement | T/F | Explanation |
|---|-----------|-----|-------------|
| 1 | The MLE of µ for Normal data is the sample mean | **T** | ∂ℓ/∂µ = 0 gives µ̂ = x̄ |
| 2 | MLE is always unbiased | **F** | σ̂²_MLE is biased (divides by n) |
| 3 | MSE = Bias² + Variance | **T** | Fundamental decomposition |
| 4 | A consistent estimator must be unbiased | **F** | s̃² is biased but consistent |
| 5 | OLS regression line passes through (x̄, ȳ) | **T** | ȳ = b₀ + b₁x̄ by construction |
| 6 | Σeᵢ = 0 always holds in OLS with intercept | **T** | First normal equation implies this |
| 7 | r = 0.5 means R² = 0.5 | **F** | R² = 0.25 |
| 8 | F-test and t-test for β₁ give same conclusion in SLR | **T** | F = t² in simple regression |
| 9 | PI for new observation is always wider than CI for mean | **T** | Extra "1+" in variance formula |
| 10 | MLE for σ² in regression divides by n, not n−2 | **T** | MLE uses n; OLS uses n−2 |
| 11 | Gauss-Markov says OLS is the best among ALL estimators | **F** | Best among LINEAR UNBIASED only |
| 12 | SSreg + SSres = syy (total corrected SS) | **T** | ANOVA decomposition |
| 13 | If β₁ = 0, then R² = 0 | **T** | No relationship → no explanation |
| 14 | Higher R² always means better model | **F** | Can be overfitting; add any variable increases R² |
| 15 | In centered model, Cov(b₀*, b₁) = 0 | **T** | Major advantage of centering |
| 16 | Prediction is best at x₀ = x̄ | **T** | Minimum width of prediction band |
| 17 | Correlation implies causation | **F** | Classic fallacy |
| 18 | MLE has functional invariance | **T** | h(θ̂_MLE) = MLE of h(θ) |
| 19 | In no-intercept model, Σeᵢ = 0 necessarily | **F** | Only true when intercept is present |
| 20 | s̃² has lower MSE than s² despite being biased | **T** | Bias-variance tradeoff in action |

---

## P14 | ANOVA Table Construction
⭐⭐⭐ Hard

[⬆️ Back to Index](#-problem-index)

### Problem

Given: n = 20, Σxᵢ = 100, Σyᵢ = 200, Σxᵢ² = 600, Σyᵢ² = 2400, Σxᵢyᵢ = 1200

**(a)** Find b₁, b₀  
**(b)** Construct the complete ANOVA table  
**(c)** Test H₀: β₁ = 0 at α = 0.05  
**(d)** Compute R² and interpret  
**(e)** Find 95% CI for β₁ (use t_(18,0.025) ≈ 2.101)

---

### Solution

**Preliminaries:**
```
x̄ = 100/20 = 5,   ȳ = 200/20 = 10

sxx = Σxᵢ² − (Σxᵢ)²/n = 600 − 10000/20 = 600 − 500 = 100
syy = Σyᵢ² − (Σyᵢ)²/n = 2400 − 40000/20 = 2400 − 2000 = 400
sxy = Σxᵢyᵢ − (Σxᵢ)(Σyᵢ)/n = 1200 − 20000/20 = 1200 − 1000 = 200
```

**(a) Regression coefficients:**
```
b₁ = sxy/sxx = 200/100 = 2.0
b₀ = ȳ − b₁x̄ = 10 − 2(5) = 0

ŷ = 0 + 2x = 2x
```

**(b) ANOVA Table:**
```
SSreg = b₁·sxy = 2 × 200 = 400
SSres = syy − SSreg = 400 − 400 = 0   ← Perfect fit!

Wait — let's double-check: SSres = syy − sxy²/sxx = 400 − 40000/100 = 400 − 400 = 0
```

Hmm, SSres = 0 means perfect linear relationship. Let's proceed:

| Source | SS | df | MS | F |
|--------|----|----|----|----|
| Regression | 400 | 1 | 400 | ∞ |
| Residual | 0 | 18 | 0 | |
| Total | 400 | 19 | | |

**(c):** F₀ = ∞ >> any critical value → **Reject H₀**. β₁ is significant (perfect fit!).

**(d):**
```
R² = SSreg/syy = 400/400 = 1.00  (100%)
r = sxy/√(sxx·syy) = 200/√(100×400) = 200/200 = 1.0
```

All variation in Y is explained by X. Perfect positive linear relationship.

**(e):** Since s² = MSE = 0, the confidence interval degenerates to exactly [2, 2]. In practice, this means every data point falls exactly on the line ŷ = 2x.

> This is a **special case** — in exams, SSres is usually > 0. This example illustrates what happens with a perfect fit.

---


**📘 See the companion file: [Theory Guide](./simple_linear_regression_pe_theory.md)**
