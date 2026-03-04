# 📊 Statistics BootCamp — Master Study Hub

### 🎓 ODS | AI 
> **Source:** [Steve Brunton — Probability & Statistics BootCamp](https://www.youtube.com/playlist?list=PLMrJAkhIeNNR3sNYvfgiKgcStwuPSts9V) (Statistics portion) · University of Washington
> **Goal:** Understand every concept in ONE read — explained like you're seeing it for the first time!
> **Philosophy:** Think INTUITIVELY first, compute FORMALLY second

---

## 📂 Study Materials — Quick Navigation

| # | Document | What's Inside | Link |
|---|----------|---------------|------|
| 📘 | **Theory Guide** | All 20 chapters + Q&A + AI/ML uses + diagrams | **[Open Theory Guide](./Statistics_BootCamp_THEORY.md)** |
| 🔢 | **Practice Problems** | 15 fully solved problems — every step explained | **[Open Practice Guide](./Statistics_BootCamp_PRACTICE.md)** |
| 📋 | **This File (INDEX)** | Master hub, notation, formulas, concept map, mnemonics | **You are here!** |

```
    HOW THESE 3 FILES CONNECT

              +---------------+
              |  INDEX (this) |  <- START HERE
              |  formulas,    |
              |  notation,    |
              |  concept map  |
              +-------+-------+
                      |
             +--------+--------+
             v                 v
      +-----------+     +------------+
      |  THEORY   |<--->|  PRACTICE  |
      |  concepts |     |  solved    |
      |  diagrams |     |  problems  |
      |  Q&A      |     |  step by   |
      |  AI/ML    |     |  step      |
      +-----------+     +------------+
```

---

## 🔗 Prerequisite

These guides assume you've covered **Probability** first:
> [← Probability BootCamp INDEX](../Probability/Probability_BootCamp_INDEX.md)

**Probability** = "Given the RULES, what DATA do we expect?"
**Statistics** = "Given the DATA, what were the RULES?" (reverse!)

---

## 📖 Notation Dictionary

```
SYMBOL            MEANING                              EXAMPLE
------            -------                              -------
X1, X2, ..., Xn  random sample (n observations)        exam scores of 30 students
X_bar             sample mean = sum(Xi)/n               average exam score = 74.2
s^2               sample variance                       spread of scores
s                 sample std dev = sqrt(s^2)            typical deviation
mu (u)            population mean (UNKNOWN!)             true average of ALL students
sigma             population std dev (UNKNOWN!)          true spread
n                 sample size                           30 students
theta             generic unknown parameter             could be u, p, sigma, etc.
theta-hat         estimator of theta                    X_bar estimates u
SE                standard error = s/sqrt(n)            precision of X_bar
alpha             significance level                    0.05 = 5% false alarm rate
p-value           prob of data or more extreme if H0    0.03 means "unlikely under H0"
H0                null hypothesis                       "drug has no effect"
H1 (Ha)           alternative hypothesis                "drug works"
CI                confidence interval                   (72.3, 77.7) for u
df                degrees of freedom                    n-1 for t-test
t                 t-statistic / t-distribution          used when sigma unknown
z                 z-score (standard normal)             used when sigma known
chi^2             chi-squared statistic                 goodness-of-fit
F                 F-statistic                           comparing variances / ANOVA
b0, b1            regression coefficients               intercept, slope
r                 sample correlation                    strength of linear fit
R^2               coefficient of determination          % of variance explained
SSE, SSR, SST     sum of squares (error, reg, total)    regression decomposition
L(theta)          likelihood function                   product of f(xi|theta)
l(theta)          log-likelihood = ln(L)                sum of ln f(xi|theta)
MLE               maximum likelihood estimator          theta that maximizes L
Prior             belief BEFORE data                    P(theta)
Posterior         belief AFTER data                     P(theta|data)
```

---

## 📋 Formula Cheat Sheet

```
ESTIMATION
  X_bar = (1/n) * sum(Xi)                       sample mean
  s^2 = (1/(n-1)) * sum((Xi - X_bar)^2)         sample variance (Bessel)
  SE = s / sqrt(n)                               standard error
  Bias = E[theta-hat] - theta                    systematic error
  MSE = Bias^2 + Variance                        total error

CONFIDENCE INTERVALS
  Z-interval: X_bar +/- z_(a/2) * sigma/sqrt(n)      (sigma known)
  T-interval: X_bar +/- t_(a/2,n-1) * s/sqrt(n)      (sigma unknown)
  Proportion: p-hat +/- z_(a/2) * sqrt(p-hat*(1-p-hat)/n)
  Common z-values: 90%->1.645  95%->1.96  99%->2.576

HYPOTHESIS TESTING
  Z-test: Z = (X_bar - u0) / (sigma/sqrt(n))
  T-test: T = (X_bar - u0) / (s/sqrt(n)),  df = n-1
  p-value: P(|test stat| >= |observed| | H0 true)
  Reject H0 if p-value < alpha

MAXIMUM LIKELIHOOD (MLE)
  L(theta) = product of f(xi | theta)
  l(theta) = sum of ln(f(xi | theta))
  MLE: dl/dtheta = 0, solve for theta-hat

REGRESSION
  y-hat = b0 + b1*x
  b1 = Sxy / Sxx = sum((xi-x_bar)(yi-y_bar)) / sum((xi-x_bar)^2)
  b0 = y_bar - b1 * x_bar
  R^2 = 1 - SSE/SST = SSR/SST
  SST = SSR + SSE

BAYESIAN
  Posterior is proportional to Likelihood * Prior
  P(theta|data) = P(data|theta) * P(theta) / P(data)
```

---

## 🗺️ Concept Map

```
STATISTICS = "Reverse Probability"

Population (unknown u, sigma) --[sample]--> Data (X1,...,Xn)
Data --[compute]--> Statistics (X_bar, s)
Statistics --[inference]--> Conclusions (CI, test results, predictions)

                      STATISTICS
                          |
            +-------------+-------------+
            |             |             |
       ESTIMATION     TESTING       MODELING
            |             |             |
      +-----+-----+   +--+--+     +---+---+
      |     |     |   |     |     |       |
    Point Interval MLE H0/H1 p-val Linear  Bayesian
    Est.   (CI)       Z-test      Regression Inference
      |               t-test      Logistic
      v               chi-sq      Multiple
    X_bar             F/ANOVA
    s^2
    p-hat          +-------+
                   |       |
                Type I   Type II
                (false   (miss real
                alarm)    effect)
```

---

## 🌳 "Which Test Do I Use?" Decision Tree

```
START: What's your GOAL?
  |
  +-- Estimate a parameter? --> ESTIMATION
  |     +-- Point estimate --> X_bar, p-hat, MLE
  |     +-- Range estimate --> Confidence Interval
  |
  +-- Test a claim about a parameter? --> HYPOTHESIS TEST
  |     +-- About a MEAN?
  |     |     +-- sigma known --> Z-test
  |     |     +-- sigma unknown --> t-test (df=n-1)
  |     +-- About a PROPORTION? --> Z-test for proportions
  |     +-- Compare 2 means? --> Two-sample t-test
  |     +-- Compare 3+ means? --> ANOVA (F-test)
  |     +-- Categorical data fit? --> Chi-squared test
  |
  +-- Predict Y from X? --> REGRESSION
  |     +-- 1 predictor --> Simple Linear Regression
  |     +-- Multiple predictors --> Multiple Regression
  |     +-- Y is 0/1 --> Logistic Regression
  |
  +-- Update beliefs with new data? --> BAYESIAN INFERENCE
```

---

## 🧠 15 Mnemonics

| # | Mnemonic | Stands For | Concept |
|---|----------|-----------|---------|
| 1 | **SAMP** | Sample Approximates Mean of Population | Point estimation |
| 2 | **BESSEL** | Because Each Sample Systematically Estimates Less | Why divide by n-1 |
| 3 | **SEMN** | Standard Error = s/sqrt(n) | More data = more precision |
| 4 | **CLIP** | Confidence Level Interval for Parameter | CI definition |
| 5 | **NULL** | Nothing Unusual, Luck Likely | H0 = "nothing special" |
| 6 | **TRAP** | Type I = Reject (falsely), Alpha Prob | False positive |
| 7 | **MISS** | Missing It = Second-type Slip | Type II = false negative |
| 8 | **PVAL** | Probability Value Against Luck | p-value meaning |
| 9 | **LIKE** | Likelihood Is Key to Estimation | MLE principle |
| 10 | **SLOPE** | Sxy Laid Over Sxx Produces Estimate | b1 formula |
| 11 | **FIT** | Fraction of Information from Total | R^2 = SSR/SST |
| 12 | **RESID** | Residual = Estimated Subtracted from Identified Data | ei = yi - y-hat |
| 13 | **BAYES** | Belief After Yielding Evidence from Sample | Posterior update |
| 14 | **PRIOR** | Pre-data Information Reflecting Our Reasoning | Bayesian prior |
| 15 | **ANOVA** | Analyzing Numerous Observations' Variance Altogether | F-test for groups |

---

## 📚 Chapter-to-File Map

| Block | Ch | Topic | Theory | Practice |
|-------|-----|-------|--------|----------|
| **FOUNDATIONS** | 1 | What is Statistics? | [📘 Ch1](./Statistics_BootCamp_THEORY.md#chapter-1--what-is-statistics) | — |
| | 2 | Populations, Samples & Sampling | [📘 Ch2](./Statistics_BootCamp_THEORY.md#chapter-2--populations-samples--sampling) | [P1](./Statistics_BootCamp_PRACTICE.md#-p1-sampling--sample-statistics) |
| | 3 | Descriptive Statistics | [📘 Ch3](./Statistics_BootCamp_THEORY.md#chapter-3--descriptive-statistics) | [P1](./Statistics_BootCamp_PRACTICE.md#-p1-sampling--sample-statistics) |
| | 4 | Sampling Distributions & CLT | [📘 Ch4](./Statistics_BootCamp_THEORY.md#chapter-4--sampling-distributions--clt) | [P2](./Statistics_BootCamp_PRACTICE.md#-p2-point-estimation--unbiasedness) |
| **ESTIMATION** | 5 | Point Estimation | [📘 Ch5](./Statistics_BootCamp_THEORY.md#chapter-5--point-estimation) | [P2](./Statistics_BootCamp_PRACTICE.md#-p2-point-estimation--unbiasedness) |
| | 6 | Bias, Variance & MSE | [📘 Ch6](./Statistics_BootCamp_THEORY.md#chapter-6--bias-variance--mse) | [P4](./Statistics_BootCamp_PRACTICE.md#-p4-bias-variance-tradeoff) |
| | 7 | Maximum Likelihood (MLE) | [📘 Ch7](./Statistics_BootCamp_THEORY.md#chapter-7--maximum-likelihood-estimation) | [P3](./Statistics_BootCamp_PRACTICE.md#-p3-maximum-likelihood-estimation) |
| | 8 | Confidence Intervals | [📘 Ch8](./Statistics_BootCamp_THEORY.md#chapter-8--confidence-intervals) | [P5](./Statistics_BootCamp_PRACTICE.md#-p5-confidence-intervals) |
| **TESTING** | 9 | Hypothesis Testing Framework | [📘 Ch9](./Statistics_BootCamp_THEORY.md#chapter-9--hypothesis-testing-framework) | [P6](./Statistics_BootCamp_PRACTICE.md#-p6-hypothesis-testing-z-test) |
| | 10 | Z-Test | [📘 Ch10](./Statistics_BootCamp_THEORY.md#chapter-10--z-test) | [P6](./Statistics_BootCamp_PRACTICE.md#-p6-hypothesis-testing-z-test) |
| | 11 | T-Test | [📘 Ch11](./Statistics_BootCamp_THEORY.md#chapter-11--t-test) | [P7](./Statistics_BootCamp_PRACTICE.md#-p7-t-test) |
| | 12 | Type I & Type II Errors, Power | [📘 Ch12](./Statistics_BootCamp_THEORY.md#chapter-12--type-i--type-ii-errors-and-power) | [P8](./Statistics_BootCamp_PRACTICE.md#-p8-p-values--decision-making) |
| | 13 | Chi-Squared Tests | [📘 Ch13](./Statistics_BootCamp_THEORY.md#chapter-13--chi-squared-tests) | [P9](./Statistics_BootCamp_PRACTICE.md#-p9-chi-squared-test) |
| | 14 | ANOVA (F-Test) | [📘 Ch14](./Statistics_BootCamp_THEORY.md#chapter-14--anova-f-test) | [P10](./Statistics_BootCamp_PRACTICE.md#-p10-anova) |
| **MODELING** | 15 | Simple Linear Regression | [📘 Ch15](./Statistics_BootCamp_THEORY.md#chapter-15--simple-linear-regression) | [P11](./Statistics_BootCamp_PRACTICE.md#-p11-simple-linear-regression) |
| | 16 | Multiple Regression | [📘 Ch16](./Statistics_BootCamp_THEORY.md#chapter-16--multiple-regression) | [P12](./Statistics_BootCamp_PRACTICE.md#-p12-multiple-regression) |
| | 17 | Logistic Regression | [📘 Ch17](./Statistics_BootCamp_THEORY.md#chapter-17--logistic-regression) | [P13](./Statistics_BootCamp_PRACTICE.md#-p13-logistic-regression) |
| | 18 | Bayesian Inference | [📘 Ch18](./Statistics_BootCamp_THEORY.md#chapter-18--bayesian-inference) | [P14](./Statistics_BootCamp_PRACTICE.md#-p14-bayesian-inference) |
| | 19 | Bayesian vs Frequentist | [📘 Ch19](./Statistics_BootCamp_THEORY.md#chapter-19--bayesian-vs-frequentist) | [P15](./Statistics_BootCamp_PRACTICE.md#-p15-bayesian-vs-frequentist-comparison) |
| | 20 | Statistics in ML & AI | [📘 Ch20](./Statistics_BootCamp_THEORY.md#chapter-20--statistics-in-ml--ai) | — |

---

## 60-SECOND REVISION

```
STATISTICS = reverse of probability. Data -> inference about unknowns.
ESTIMATION: X_bar estimates u, s^2 estimates sigma^2, p-hat estimates p.
BESSEL: divide by n-1 (not n) for unbiased variance.
MLE: find theta that maximizes L(theta) = product of f(xi|theta).
CI: X_bar +/- (critical value) * SE.  95% CI uses z=1.96 or t-table.
HYPOTHESIS: H0="nothing special". Reject if p-value < alpha.
Z-TEST: sigma known. T-TEST: sigma unknown (use s, df=n-1).
TYPE I = false alarm (alpha). TYPE II = miss (beta). Power = 1-beta.
CHI-SQ: sum of (O-E)^2/E for categorical data.
ANOVA: compare 3+ group means, F = MSB/MSW.
REGRESSION: y-hat = b0 + b1*x.  b1 = Sxy/Sxx.  R^2 = SSR/SST.
BAYESIAN: Posterior proportional to Likelihood * Prior.
```

---

> [Open Theory Guide](./Statistics_BootCamp_THEORY.md) | [Open Practice Guide](./Statistics_BootCamp_PRACTICE.md)
>
> 🎓 Created for: ODS | AI
