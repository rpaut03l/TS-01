# 🔢 Statistics BootCamp — PRACTICE PROBLEMS GUIDE

### 🎓 ODS | AI 
> **Navigation:** [<< INDEX](./Statistics_BootCamp_INDEX.md) | [<< Theory Guide](./Statistics_BootCamp_THEORY.md)
>
> Every step explained from scratch. Nothing assumed. Every diagram drawn out.

---

## 📚 Problem Index

| # | Problem | Concepts | Theory |
|---|---------|----------|--------|
| P1 | [Sampling & Sample Statistics](#-p1-sampling--sample-statistics) | X_bar, s^2, SE | [Ch2-3](./Statistics_BootCamp_THEORY.md#chapter-2--populations-samples--sampling) |
| P2 | [Point Estimation & Unbiasedness](#-p2-point-estimation--unbiasedness) | Bias, Bessel's correction | [Ch5](./Statistics_BootCamp_THEORY.md#chapter-5--point-estimation) |
| P3 | [Maximum Likelihood Estimation](#-p3-maximum-likelihood-estimation) | MLE for Normal, Bernoulli | [Ch7](./Statistics_BootCamp_THEORY.md#chapter-7--maximum-likelihood-estimation) |
| P4 | [Bias-Variance Tradeoff](#-p4-bias-variance-tradeoff) | MSE decomposition | [Ch6](./Statistics_BootCamp_THEORY.md#chapter-6--bias-variance--mse) |
| P5 | [Confidence Intervals](#-p5-confidence-intervals) | Z-interval, t-interval | [Ch8](./Statistics_BootCamp_THEORY.md#chapter-8--confidence-intervals) |
| P6 | [Hypothesis Testing: Z-Test](#-p6-hypothesis-testing-z-test) | Z-test, p-value, decision | [Ch9-10](./Statistics_BootCamp_THEORY.md#chapter-9--hypothesis-testing-framework) |
| P7 | [T-Test](#-p7-t-test) | One-sample, two-sample | [Ch11](./Statistics_BootCamp_THEORY.md#chapter-11--t-test) |
| P8 | [P-Values & Decision Making](#-p8-p-values--decision-making) | Interpretation, errors | [Ch12](./Statistics_BootCamp_THEORY.md#chapter-12--type-i--type-ii-errors-and-power) |
| P9 | [Chi-Squared Test](#-p9-chi-squared-test) | Goodness-of-fit, independence | [Ch13](./Statistics_BootCamp_THEORY.md#chapter-13--chi-squared-tests) |
| P10 | [ANOVA](#-p10-anova) | F-test, comparing groups | [Ch14](./Statistics_BootCamp_THEORY.md#chapter-14--anova-f-test) |
| P11 | [Simple Linear Regression](#-p11-simple-linear-regression) | b0, b1, R^2, residuals | [Ch15](./Statistics_BootCamp_THEORY.md#chapter-15--simple-linear-regression) |
| P12 | [Multiple Regression](#-p12-multiple-regression) | Matrix form, Adjusted R^2 | [Ch16](./Statistics_BootCamp_THEORY.md#chapter-16--multiple-regression) |
| P13 | [Logistic Regression](#-p13-logistic-regression) | Sigmoid, log-odds, MLE | [Ch17](./Statistics_BootCamp_THEORY.md#chapter-17--logistic-regression) |
| P14 | [Bayesian Inference](#-p14-bayesian-inference) | Prior, posterior, conjugate | [Ch18](./Statistics_BootCamp_THEORY.md#chapter-18--bayesian-inference) |
| P15 | [Bayesian vs Frequentist Comparison](#-p15-bayesian-vs-frequentist-comparison) | CI vs credible interval | [Ch19](./Statistics_BootCamp_THEORY.md#chapter-19--bayesian-vs-frequentist) |

---

## FORMULA CHEAT SHEET

```
ESTIMATION                              TESTING
X_bar = sum(Xi)/n                       Z = (X_bar - u0)/(sigma/sqrt(n))
s^2 = sum(Xi-X_bar)^2 / (n-1)          T = (X_bar - u0)/(s/sqrt(n))
SE = s / sqrt(n)                        chi^2 = sum (O-E)^2 / E
MSE = Bias^2 + Variance                 F = MSB / MSW

CONFIDENCE INTERVALS                    REGRESSION
Z-CI: X_bar +/- z*sigma/sqrt(n)        b1 = Sxy/Sxx   b0 = y_bar - b1*x_bar
T-CI: X_bar +/- t*s/sqrt(n)            R^2 = 1 - SSE/SST
Proportion: p-hat +/- z*sqrt(p(1-p)/n) SST = SSR + SSE

MLE                                     BAYESIAN
L(theta) = product f(xi|theta)          Posterior = Likelihood * Prior / Evidence
Set d/dtheta[ln L] = 0                  Beta(a,b) + Binomial -> Beta(a+x, b+n-x)
```

---
---

## 🧮 P1: Sampling & Sample Statistics

> [Ch 2-3](./Statistics_BootCamp_THEORY.md#chapter-2--populations-samples--sampling) | [Problem Index](#-problem-index)

**Q: A sample of n=8 student exam scores: {65, 72, 68, 80, 75, 70, 78, 72}. Find: (a) sample mean, (b) sample variance and std dev, (c) standard error of the mean.**

### What's happening here?

```
We have 8 numbers from a LARGER population (all students).
We want to summarize these 8 numbers with statistics.

POPULATION (all students, unknown u and sigma)
+------------------------------------------+
| . . . . . . . . . . . . . . . . . . . . |
| . . . . . . . . . . . . . . . . . . . . |
+------------------------------------------+
        |
        v  (we pulled out 8)
SAMPLE: {65, 72, 68, 80, 75, 70, 78, 72}
```

### (a) Sample Mean X_bar

```
X_bar = sum of all values / n

Step 1: Add them up.
  65 + 72 + 68 + 80 + 75 + 70 + 78 + 72 = 580

Step 2: Divide by n=8.
  X_bar = 580 / 8 = 72.5

ANSWER: X_bar = 72.5

DIAGRAM: Where does 72.5 sit?
  65  68  70  72  72  75  78  80
  |---|---|---|-*-|---|---|---|
              72.5 (the balance point)
```

### (b) Sample Variance s^2 and Std Dev s

```
s^2 = sum of (Xi - X_bar)^2 / (n - 1)

WHY (n-1)? Bessel's correction. Using X_bar instead of the TRUE
mean u "uses up" one degree of freedom. Dividing by (n-1) makes
s^2 an UNBIASED estimator of sigma^2.

Step 1: Compute each deviation (Xi - X_bar):
  65 - 72.5 = -7.5
  72 - 72.5 = -0.5
  68 - 72.5 = -4.5
  80 - 72.5 = +7.5
  75 - 72.5 = +2.5
  70 - 72.5 = -2.5
  78 - 72.5 = +5.5
  72 - 72.5 = -0.5

  CHECK: sum of deviations = (-7.5)+(-0.5)+(-4.5)+(7.5)+(2.5)+(-2.5)+(5.5)+(-0.5)
       = 0.0  (ALWAYS sums to zero — that's why we lose 1 degree of freedom!)

Step 2: Square each deviation:
  (-7.5)^2 = 56.25
  (-0.5)^2 =  0.25
  (-4.5)^2 = 20.25
  ( 7.5)^2 = 56.25
  ( 2.5)^2 =  6.25
  (-2.5)^2 =  6.25
  ( 5.5)^2 = 30.25
  (-0.5)^2 =  0.25

Step 3: Sum them.
  56.25 + 0.25 + 20.25 + 56.25 + 6.25 + 6.25 + 30.25 + 0.25 = 176.00

Step 4: Divide by (n-1) = 7.
  s^2 = 176.00 / 7 = 25.14 (rounded)

Step 5: Standard deviation.
  s = sqrt(25.14) = 5.01

ANSWER: s^2 = 25.14, s = 5.01
```

### (c) Standard Error

```
SE = s / sqrt(n) = 5.01 / sqrt(8) = 5.01 / 2.828 = 1.77

WHAT SE MEANS: If we took MANY samples of n=8 and computed
X_bar each time, those X_bars would have a standard deviation
of about 1.77. It measures HOW PRECISE our X_bar is.

ANSWER: SE = 1.77
```

---

## 🧮 P2: Point Estimation & Unbiasedness

> [Ch 5](./Statistics_BootCamp_THEORY.md#chapter-5--point-estimation) | [Problem Index](#-problem-index)

**Q: (a) Show that X_bar is unbiased for u. (b) Show dividing by n (not n-1) gives biased variance. (c) If X_bar = 50 and s = 12 with n=36, what's the estimated SE?**

### (a) X_bar is unbiased

```
UNBIASED means: E[estimator] = true parameter.

E[X_bar] = E[(X1 + X2 + ... + Xn) / n]
         = (1/n) * (E[X1] + E[X2] + ... + E[Xn])    (linearity of E)
         = (1/n) * (u + u + ... + u)                  (each Xi has mean u)
         = (1/n) * n*u
         = u

UNBIASED CHECK:
  E[X_bar] = u  =  true parameter?  YES!

DIAGRAM:
  Many samples, each gives an X_bar:
  X_bar values: 49, 52, 48, 51, 50, 53, 47, 50, 51, 49, ...
  Average of these X_bars -> u (exactly)
  "X_bar might miss in any ONE sample, but ON AVERAGE it hits u."
```

### (b) Biased variance (dividing by n)

```
Let sigma_n^2 = (1/n) * sum(Xi - X_bar)^2     (dividing by n, not n-1)

It can be shown:
  E[sigma_n^2] = sigma^2 * (n-1)/n

For n=8:  E[sigma_n^2] = sigma^2 * 7/8 = 0.875 * sigma^2
  -> UNDERESTIMATES sigma^2 by 12.5%!

For n=100: E[sigma_n^2] = sigma^2 * 99/100 = 0.99 * sigma^2
  -> Only 1% bias. For large n, barely matters.

That's why we use s^2 = sum(Xi-X_bar)^2 / (n-1). It corrects the bias:
  E[s^2] = sigma^2  (unbiased)
```

### (c) Estimated SE

```
SE = s / sqrt(n) = 12 / sqrt(36) = 12 / 6 = 2.0

ANSWER: SE = 2.0

This means: X_bar = 50 with "plus or minus about 2" precision.
```

---

## 🧮 P3: Maximum Likelihood Estimation

> [Ch 7](./Statistics_BootCamp_THEORY.md#chapter-7--maximum-likelihood-estimation) | [Problem Index](#-problem-index)

**Q: (a) Derive MLE for Bernoulli parameter p given data {1,0,1,1,0,1,0,1,1,1}. (b) Derive MLE for Normal mean u (sigma^2 known).**

### What is MLE?

```
MLE = "What parameter value makes my observed data MOST LIKELY?"

  Think of it as trying on different parameter values like trying
  on shoes — which one FITS the data best?

  FLOW:
  Data: {x1, x2, ..., xn}
     |
     v
  L(theta) = P(seeing this data | theta)  <-- likelihood function
     |
     v
  Find theta-hat that MAXIMIZES L(theta)
     |
     v
  theta-hat = MLE!
```

### (a) MLE for Bernoulli p

```
Data: {1, 0, 1, 1, 0, 1, 0, 1, 1, 1}
n = 10, number of 1s = x = 7

Each Xi ~ Bernoulli(p): P(Xi=1) = p, P(Xi=0) = 1-p

Step 1: Write the likelihood.
  L(p) = product of P(Xi = xi)
       = p^7 * (1-p)^3

  DIAGRAM:
  L(p)
    |           *
    |         *   *
    |       *       *
    |     *           *
    |   *               *
    | *                   *
    +--+--+--+--+--+--+--+-- p
    0    0.3  0.5  0.7  1.0
                   ^
               peak = MLE

Step 2: Take log-likelihood.
  l(p) = ln(L(p)) = 7*ln(p) + 3*ln(1-p)

Step 3: Differentiate and set to 0.
  dl/dp = 7/p - 3/(1-p) = 0
  7/p = 3/(1-p)
  7*(1-p) = 3*p
  7 - 7p = 3p
  7 = 10p
  p-hat = 7/10 = 0.7

Step 4: Verify it's a maximum (second derivative negative).
  d^2l/dp^2 = -7/p^2 - 3/(1-p)^2 < 0  (always negative)

ANSWER: p-hat = 0.7 = (number of successes) / n

MLE for Bernoulli is just the SAMPLE PROPORTION.
```

### (b) MLE for Normal mean

```
Data: X1,...,Xn ~ N(u, sigma^2), sigma^2 known. Find MLE for u.

Step 1: Likelihood.
  L(u) = product of (1/(sigma*sqrt(2*pi))) * exp(-(Xi-u)^2/(2*sigma^2))

Step 2: Log-likelihood.
  l(u) = -(n/2)*ln(2*pi*sigma^2) - (1/(2*sigma^2)) * sum(Xi - u)^2

  The first term is a CONSTANT (doesn't depend on u). Focus on second term.
  Maximizing l(u) = minimizing sum(Xi - u)^2.

Step 3: Differentiate.
  dl/du = (1/sigma^2) * sum(Xi - u) = 0
  sum(Xi) - n*u = 0
  u-hat = sum(Xi)/n = X_bar

ANSWER: u-hat = X_bar (the sample mean!)

AI/ML CONNECTION: Training a neural net with MSE loss on Gaussian data
is EXACTLY finding the MLE. Minimizing MSE = maximizing Normal likelihood.
```

---

## 🧮 P4: Bias-Variance Tradeoff

> [Ch 6](./Statistics_BootCamp_THEORY.md#chapter-6--bias-variance--mse) | [Problem Index](#-problem-index)

**Q: An estimator theta-hat has E[theta-hat] = theta + 2 and Var(theta-hat) = 9. (a) What's the bias? (b) What's the MSE? (c) Another estimator has E[theta-hat2] = theta (unbiased) but Var = 20. Which is better by MSE?**

### (a) Bias

```
Bias = E[theta-hat] - theta = (theta + 2) - theta = 2

MEANING: This estimator CONSISTENTLY overshoots by 2 units.

  DIAGRAM:
  True theta     theta-hat values
      |              . .
      |             . . .
      * -------->  . * . .     <- centered at theta+2, not theta
      |              . .
```

### (b) MSE of first estimator

```
MSE = Bias^2 + Variance = 2^2 + 9 = 4 + 9 = 13

ANSWER: MSE = 13
```

### (c) Compare

```
Estimator 1 (biased):   MSE = 4 + 9 = 13
Estimator 2 (unbiased): MSE = 0 + 20 = 20

Estimator 1 has LOWER MSE despite being biased!

  LESSON: Unbiased is NOT always better.
  A little bias with much less variance can give LOWER total error.

  This is WHY regularization works in ML:
  - Ridge/Lasso ADD BIAS to reduce variance.
  - Total error (MSE) goes DOWN even though bias goes UP.

  DIAGRAM:
  Error
    |  \           /
    |   \  13    /        <- Estimator 1 (biased but tight)
    |    *-----*           vs
    |         20           <- Estimator 2 (unbiased but scattered)
```

---

## 🧮 P5: Confidence Intervals

> [Ch 8](./Statistics_BootCamp_THEORY.md#chapter-8--confidence-intervals) | [Problem Index](#-problem-index)

**Q: (a) X_bar=175cm, sigma=8cm, n=64. Build 95% Z-interval. (b) X_bar=42, s=6, n=16. Build 95% t-interval. (c) In a survey, 120 out of 400 said "yes". Build 95% CI for proportion.**

### (a) Z-interval (sigma known)

```
FORMULA: X_bar +/- z_(alpha/2) * sigma/sqrt(n)

Given: X_bar=175, sigma=8, n=64, confidence=95% -> z=1.96

SE = sigma/sqrt(n) = 8/sqrt(64) = 8/8 = 1.0

CI = 175 +/- 1.96 * 1.0 = 175 +/- 1.96

CI = (173.04, 176.96)

DIAGRAM:
  |------|=========*=========|------|
       173.04     175      176.96
       lower               upper
  "We're 95% confident the true mean height is between 173.04 and 176.96 cm."
```

### (b) T-interval (sigma unknown)

```
FORMULA: X_bar +/- t_(alpha/2, df) * s/sqrt(n)

Given: X_bar=42, s=6, n=16. df = n-1 = 15. 95% -> t_(0.025, 15) = 2.131

SE = s/sqrt(n) = 6/sqrt(16) = 6/4 = 1.5

CI = 42 +/- 2.131 * 1.5 = 42 +/- 3.197

CI = (38.80, 45.20)

WHY t instead of z?
  sigma is UNKNOWN, so we used s instead. This adds EXTRA uncertainty.
  t-distribution has heavier tails -> wider interval -> accounts for that.

  If we'd (wrongly) used z=1.96: CI = 42 +/- 2.94 = (39.06, 44.94)
  t-interval is WIDER (38.80, 45.20) because we're LESS certain.
```

### (c) Proportion CI

```
FORMULA: p-hat +/- z_(alpha/2) * sqrt(p-hat*(1-p-hat)/n)

p-hat = 120/400 = 0.30

SE = sqrt(0.30 * 0.70 / 400) = sqrt(0.21 / 400) = sqrt(0.000525) = 0.0229

CI = 0.30 +/- 1.96 * 0.0229 = 0.30 +/- 0.0449

CI = (0.255, 0.345)  or  (25.5%, 34.5%)

ANSWER: We're 95% confident the true proportion is between 25.5% and 34.5%.
```

---

## 🧮 P6: Hypothesis Testing: Z-Test

> [Ch 9-10](./Statistics_BootCamp_THEORY.md#chapter-9--hypothesis-testing-framework) | [Problem Index](#-problem-index)

**Q: A machine fills bottles with u=500ml (claimed). You sample n=49 bottles: X_bar=498ml. Population sigma=7ml. At alpha=0.05, is the machine underfilling? (Test H0: u=500 vs H1: u<500)**

### Step-by-step solution

```
THE COURT TRIAL ANALOGY:
  H0: "Machine is innocent" (u = 500, working correctly)
  H1: "Machine is guilty"  (u < 500, underfilling)
  Evidence: X_bar = 498 (seems low, but is it LOW ENOUGH?)
  Threshold: alpha = 0.05 (5% false alarm rate)
```

### Step 1: State hypotheses

```
H0: u = 500 (null: nothing wrong)
H1: u < 500 (alternative: underfilling — LEFT-tailed test)
```

### Step 2: Compute test statistic

```
Z = (X_bar - u0) / (sigma/sqrt(n))
  = (498 - 500) / (7/sqrt(49))
  = (-2) / (7/7)
  = -2 / 1
  = -2.0

DIAGRAM: Where does Z=-2.0 sit on the standard normal?
     Rejection
     region
      |   |
      v   v
   ▓▓▓▓|                  |
  -----+--+----*----+--+------
  -3  -2 -1.645  0    1    2
       ^    ^
    Z=-2.0  critical value
  Z=-2.0 falls IN the rejection region!
```

### Step 3: Find p-value

```
p-value = P(Z < -2.0) = 0.0228

MEANING: If the machine were TRULY filling at 500ml, there's only
a 2.28% chance of seeing a sample mean as low as 498ml.
```

### Step 4: Decision

```
p-value = 0.0228 < alpha = 0.05

REJECT H0.

CONCLUSION: At the 5% significance level, there is sufficient evidence
that the machine is underfilling (mean < 500ml).

ALTERNATIVELY using critical value:
  Left-tailed at alpha=0.05: z_critical = -1.645
  Z = -2.0 < -1.645 -> falls in rejection region -> REJECT H0.
```

---

## 🧮 P7: T-Test

> [Ch 11](./Statistics_BootCamp_THEORY.md#chapter-11--t-test) | [Problem Index](#-problem-index)

**Q: (a) One-sample: A diet claims avg weight loss is 5kg. Sample of n=12 people: X_bar=4.2kg, s=1.8kg. Test at alpha=0.05. (b) Two-sample: Group A (n1=10, X_bar1=78, s1=8), Group B (n2=12, X_bar2=72, s2=7). Is A significantly better?**

### (a) One-sample t-test

```
H0: u = 5     (diet works as claimed)
H1: u < 5     (diet is LESS effective than claimed — left-tailed)

T = (X_bar - u0) / (s/sqrt(n))
  = (4.2 - 5) / (1.8/sqrt(12))
  = (-0.8) / (1.8/3.464)
  = -0.8 / 0.5196
  = -1.54

df = n-1 = 11.
Critical value: t_(0.05, 11) = -1.796 (left-tailed)

DECISION: T = -1.54 > -1.796 (does NOT fall in rejection region)

FAIL TO REJECT H0.
Not enough evidence to say the diet is less effective than claimed.

  DIAGRAM:
  Rejection
     |   |
     v   v
   ▓▓▓▓|                    |
  -----+----+------*--+--+------
  -3  -1.796  T=-1.54  0    2
              ^
         NOT in rejection region
```

### (b) Two-sample t-test

```
H0: u1 = u2     (groups are equal)
H1: u1 > u2     (A is better — right-tailed)

T = (X_bar1 - X_bar2) / sqrt(s1^2/n1 + s2^2/n2)
  = (78 - 72) / sqrt(64/10 + 49/12)
  = 6 / sqrt(6.4 + 4.083)
  = 6 / sqrt(10.483)
  = 6 / 3.238
  = 1.853

Approximate df (Welch's): use smaller of (n1-1, n2-1) = min(9, 11) = 9
  (conservative approach; Welch-Satterthwaite gives ~18.7)

Critical value: t_(0.05, 9) = 1.833 (right-tailed)

T = 1.853 > 1.833 -> BARELY in the rejection region.

REJECT H0 (barely). Group A is significantly better than Group B
at alpha=0.05.

AI/ML: This is how you'd compare two model accuracies!
"Is Model A's 78% accuracy significantly better than Model B's 72%?"
```

---

## 🧮 P8: P-Values & Decision Making

> [Ch 12](./Statistics_BootCamp_THEORY.md#chapter-12--type-i--type-ii-errors-and-power) | [Problem Index](#-problem-index)

**Q: (a) Z-test gives Z=1.87, two-tailed. Find p-value and decide at alpha=0.05. (b) Identify Type I and Type II errors for "new drug is effective" test. (c) If power=0.80, what's beta?**

### (a) P-value for two-tailed test

```
Two-tailed means H1: u != u0 (could be higher OR lower).

p-value = 2 * P(Z > |1.87|) = 2 * P(Z > 1.87)

From Z-table: P(Z > 1.87) = 1 - 0.9693 = 0.0307

p-value = 2 * 0.0307 = 0.0614

DECISION: p-value = 0.0614 > alpha = 0.05

FAIL TO REJECT H0.

  DIAGRAM (two-tailed):
   Reject    |              |    Reject
   ▓▓▓▓▓▓|  |              |  |▓▓▓▓▓▓
  --------+--+------*-------+--+--------
       -1.96      0       1.87 1.96
                           ^
                    Z=1.87 is INSIDE acceptance region
                    (between -1.96 and +1.96)

NOTE: If this were one-tailed (H1: u > u0),
p-value = 0.0307 < 0.05 -> REJECT.
The choice of one-tailed vs two-tailed MATTERS!
```

### (b) Type I and Type II errors

```
Context: Testing if new drug is effective.
  H0: Drug has NO effect.
  H1: Drug IS effective.

                      REALITY
                  Drug useless    Drug works
  DECISION  +--------------+--------------+
  "Drug     | TYPE I ERROR | CORRECT      |
   works"   | (false alarm)| (true pos)   |
  (reject   | Approve a    | Approve a    |
   H0)      | useless drug!| good drug    |
  ----------+--------------+--------------+
  "Drug     | CORRECT      | TYPE II ERROR|
   useless" | (true neg)   | (missed it!) |
  (fail to  | Correctly    | Reject a good|
   reject)  | reject it    | drug!        |
            +--------------+--------------+

  Type I  (alpha): Approving a drug that doesn't work -> DANGEROUS
  Type II (beta):  Rejecting a drug that DOES work -> WASTEFUL
```

### (c) Power

```
Power = 1 - beta

If power = 0.80: beta = 1 - 0.80 = 0.20

MEANING: 20% chance of missing a real effect.
         80% chance of detecting it if it exists.

RULE OF THUMB: Power >= 0.80 is the standard minimum in research.
```

---

## 🧮 P9: Chi-Squared Test

> [Ch 13](./Statistics_BootCamp_THEORY.md#chapter-13--chi-squared-tests) | [Problem Index](#-problem-index)

**Q: (a) Goodness-of-fit: A bag claims equal mix of 4 colors. You draw 200: Red=60, Blue=45, Green=55, Yellow=40. Fair? (b) Independence: Contingency table for gender vs preference. Test at alpha=0.05.**

### (a) Goodness-of-fit

```
H0: All 4 colors are equally likely (p = 1/4 each).
H1: At least one color has a different probability.

Expected count per color = 200 * (1/4) = 50

chi^2 = sum of (O - E)^2 / E

  Color   | Observed | Expected | (O-E)^2/E
  --------+----------+----------+-----------
  Red     |    60    |    50    | (10)^2/50 = 2.00
  Blue    |    45    |    50    | (-5)^2/50 = 0.50
  Green   |    55    |    50    | (5)^2/50  = 0.50
  Yellow  |    40    |    50    | (-10)^2/50= 2.00
  --------+----------+----------+-----------
  TOTAL   |   200    |   200    | chi^2 = 5.00

df = (number of categories) - 1 = 4 - 1 = 3

Critical value: chi^2_(0.05, 3) = 7.815

DECISION: 5.00 < 7.815 -> FAIL TO REJECT H0.

No significant evidence that the bag is unfair.

DIAGRAM:
  chi^2 distribution (df=3):
        *
       * *
      *   *
     *     * * *
    *           * * *
  --+---+---+---+---+---+---
    0   3   5   7.815  12
            ^       ^
         chi^2=5  critical
         (NOT in rejection region)
```

### (b) Test of Independence

```
Contingency table (Gender vs Pizza preference):

              Cheese  Pepperoni  Veggie  | Row Total
  Male          30       45       25    |   100
  Female        40       30       30    |   100
  ---------+--------+---------+--------+----------
  Col Total     70       75       55    |   200

H0: Gender and preference are INDEPENDENT.
H1: They are NOT independent.

Expected = (row total * col total) / grand total

  E(Male,Cheese)    = 100*70/200  = 35
  E(Male,Pepperoni) = 100*75/200  = 37.5
  E(Male,Veggie)    = 100*55/200  = 27.5
  E(Female,Cheese)    = 100*70/200  = 35
  E(Female,Pepperoni) = 100*75/200  = 37.5
  E(Female,Veggie)    = 100*55/200  = 27.5

chi^2 = (30-35)^2/35 + (45-37.5)^2/37.5 + (25-27.5)^2/27.5
      + (40-35)^2/35 + (30-37.5)^2/37.5 + (30-27.5)^2/27.5

      = 25/35 + 56.25/37.5 + 6.25/27.5
      + 25/35 + 56.25/37.5 + 6.25/27.5

      = 0.714 + 1.500 + 0.227 + 0.714 + 1.500 + 0.227

      = 4.882

df = (rows-1)(cols-1) = (2-1)(3-1) = 2

Critical value: chi^2_(0.05, 2) = 5.991

DECISION: 4.882 < 5.991 -> FAIL TO REJECT H0.

No significant evidence that gender and pizza preference are related.

AI/ML: Chi-squared independence test is used for FEATURE SELECTION
with categorical features. "Is this feature related to the target?"
```

---

## 🧮 P10: ANOVA

> [Ch 14](./Statistics_BootCamp_THEORY.md#chapter-14--anova-f-test) | [Problem Index](#-problem-index)

**Q: Three teaching methods. Scores: Method A={85,90,78,92}, Method B={70,75,72,68}, Method C={80,82,79,85}. Test if means differ at alpha=0.05.**

### Setup

```
WHY NOT just do 3 separate t-tests (A vs B, A vs C, B vs C)?
  Each test has alpha=0.05 false alarm rate.
  3 tests -> overall false alarm rate is about 1-(0.95)^3 = 14.3%!
  ANOVA does it in ONE test with correct alpha.

  H0: uA = uB = uC    (all methods are equal)
  H1: at least one differs
```

### Step 1: Compute group means and grand mean

```
X_bar_A = (85+90+78+92)/4 = 345/4 = 86.25
X_bar_B = (70+75+72+68)/4 = 285/4 = 71.25
X_bar_C = (80+82+79+85)/4 = 326/4 = 81.50

Grand mean X_bar = (345+285+326)/12 = 956/12 = 79.67

  DIAGRAM:
  A: ----[-----*-----]----        86.25
  B: --[---*---]--                71.25
  C: -------[----*----]---        81.50
       |    |    |    |    |
       65   70   75   80   90
  Are these differences real, or just random noise?
```

### Step 2: Compute SSB (between groups)

```
SSB = sum of nj * (X_bar_j - X_bar)^2

  = 4*(86.25-79.67)^2 + 4*(71.25-79.67)^2 + 4*(81.50-79.67)^2
  = 4*(6.58)^2 + 4*(-8.42)^2 + 4*(1.83)^2
  = 4*43.30 + 4*70.90 + 4*3.35
  = 173.20 + 283.60 + 13.40
  = 470.20
```

### Step 3: Compute SSW (within groups)

```
SSW = sum of all (Xij - X_bar_j)^2

Group A: (85-86.25)^2+(90-86.25)^2+(78-86.25)^2+(92-86.25)^2
       = 1.5625 + 14.0625 + 68.0625 + 33.0625 = 116.75

Group B: (70-71.25)^2+(75-71.25)^2+(72-71.25)^2+(68-71.25)^2
       = 1.5625 + 14.0625 + 0.5625 + 10.5625 = 26.75

Group C: (80-81.50)^2+(82-81.50)^2+(79-81.50)^2+(85-81.50)^2
       = 2.25 + 0.25 + 6.25 + 12.25 = 21.00

SSW = 116.75 + 26.75 + 21.00 = 164.50
```

### Step 4: Compute F-statistic

```
k = 3 groups, N = 12 total observations.

MSB = SSB / (k-1) = 470.20 / 2 = 235.10
MSW = SSW / (N-k) = 164.50 / 9 = 18.28

F = MSB / MSW = 235.10 / 18.28 = 12.86

df1 = k-1 = 2,  df2 = N-k = 9
Critical value: F_(0.05, 2, 9) = 4.26

DECISION: F = 12.86 > 4.26 -> REJECT H0.

At least one teaching method produces significantly different scores.
(Post-hoc tests like Tukey HSD would tell you WHICH pairs differ.)
```

---

## 🧮 P11: Simple Linear Regression

> [Ch 15](./Statistics_BootCamp_THEORY.md#chapter-15--simple-linear-regression) | [Problem Index](#-problem-index)

**Q: Study hours (x) vs exam score (y). Data: x={2,3,5,7,8}, y={55,62,70,80,85}. (a) Find b1, b0. (b) Predict score for x=6. (c) Compute R^2.**

### Setup

```
  y (score)
  85|                    *
  80|                *
  70|          *
  62|      *
  55|  *
    +--+--+--+--+--+--+--+-- x (hours)
       2  3  4  5  6  7  8
  "Looks like a strong positive linear relationship!"
```

### (a) Find slope b1 and intercept b0

```
n = 5

Step 1: Compute means.
  x_bar = (2+3+5+7+8)/5 = 25/5 = 5.0
  y_bar = (55+62+70+80+85)/5 = 352/5 = 70.4

Step 2: Compute Sxy and Sxx.
  xi | yi | xi-x_bar | yi-y_bar | (xi-x_bar)(yi-y_bar) | (xi-x_bar)^2
  ---+----+----------+----------+----------------------+-------------
   2 | 55 |   -3.0   |  -15.4   |       46.2           |     9.0
   3 | 62 |   -2.0   |   -8.4   |       16.8           |     4.0
   5 | 70 |    0.0   |   -0.4   |        0.0           |     0.0
   7 | 80 |   +2.0   |   +9.6   |       19.2           |     4.0
   8 | 85 |   +3.0   |  +14.6   |       43.8           |     9.0
  ---+----+----------+----------+----------------------+-------------
                          SUMS:  Sxy = 126.0         Sxx = 26.0

Step 3: Slope.
  b1 = Sxy / Sxx = 126.0 / 26.0 = 4.846

Step 4: Intercept.
  b0 = y_bar - b1 * x_bar = 70.4 - 4.846*5.0 = 70.4 - 24.23 = 46.17

REGRESSION EQUATION: y-hat = 46.17 + 4.846*x

MEANING: Each extra hour of study -> +4.85 points on the exam.
```

### (b) Prediction for x=6

```
y-hat = 46.17 + 4.846*6 = 46.17 + 29.08 = 75.25

ANSWER: Predicted score for 6 hours of study = 75.25

DIAGRAM:
  y (score)
  85|                    *
  80|                *
  75|            o          <- predicted (6, 75.25)
  70|          *  /
  62|      *  /
  55|  *  /
    +--/--+--+--+--+--+--+-- x (hours)
       2  3  4  5  6  7  8
       (line: y = 46.17 + 4.85x)
```

### (c) R-squared

```
Step 1: Compute SST (total variability in y).
  SST = sum(yi - y_bar)^2
      = (-15.4)^2 + (-8.4)^2 + (-0.4)^2 + (9.6)^2 + (14.6)^2
      = 237.16 + 70.56 + 0.16 + 92.16 + 213.16
      = 613.20

Step 2: Compute predicted values and SSE.
  x=2: y-hat = 46.17 + 4.846*2 = 55.86.  Residual = 55-55.86 = -0.86
  x=3: y-hat = 46.17 + 4.846*3 = 60.71.  Residual = 62-60.71 = +1.29
  x=5: y-hat = 46.17 + 4.846*5 = 70.40.  Residual = 70-70.40 = -0.40
  x=7: y-hat = 46.17 + 4.846*7 = 80.09.  Residual = 80-80.09 = -0.09
  x=8: y-hat = 46.17 + 4.846*8 = 84.94.  Residual = 85-84.94 = +0.06

  SSE = (-0.86)^2 + (1.29)^2 + (-0.40)^2 + (-0.09)^2 + (0.06)^2
      = 0.74 + 1.66 + 0.16 + 0.008 + 0.004
      = 2.57

Step 3: R^2.
  R^2 = 1 - SSE/SST = 1 - 2.57/613.20 = 1 - 0.0042 = 0.996

ANSWER: R^2 = 0.996

MEANING: 99.6% of the variation in exam scores is explained by
study hours. Extremely strong linear relationship!
```

---

## 🧮 P12: Multiple Regression

> [Ch 16](./Statistics_BootCamp_THEORY.md#chapter-16--multiple-regression) | [Problem Index](#-problem-index)

**Q: A model predicts house price (y, in $1000s) using x1=sqft and x2=bedrooms. Given: b0=50, b1=0.1, b2=15. (a) Predict price for 2000sqft, 3 bedrooms. (b) Interpret coefficients. (c) R^2=0.85, n=50, p=2. Find Adjusted R^2.**

### (a) Prediction

```
y-hat = b0 + b1*x1 + b2*x2
      = 50 + 0.1*(2000) + 15*(3)
      = 50 + 200 + 45
      = 295

ANSWER: Predicted price = $295,000
```

### (b) Interpretation

```
b0 = 50:   A house with 0 sqft and 0 bedrooms would cost $50K.
           (meaningless in reality — just the intercept)

b1 = 0.1:  Holding bedrooms CONSTANT, each additional sqft
           increases price by $100. (0.1 * $1000 = $100)

b2 = 15:   Holding sqft CONSTANT, each additional bedroom
           increases price by $15,000.

KEY PHRASE: "Holding other variables constant" = CONTROLLING for them.
This is how regression separates individual effects.
```

### (c) Adjusted R^2

```
Adjusted R^2 = 1 - (1-R^2)*(n-1)/(n-p-1)

  = 1 - (1-0.85)*(50-1)/(50-2-1)
  = 1 - (0.15)*(49)/(47)
  = 1 - 0.15*1.0426
  = 1 - 0.1564
  = 0.8436

ANSWER: Adjusted R^2 = 0.844

WHY ADJUSTED?
  Regular R^2 ALWAYS increases when you add more predictors,
  even useless ones. Adjusted R^2 PENALIZES adding useless variables.
  If Adjusted R^2 drops when you add a variable -> that variable is useless.

  AI/ML: Adjusted R^2 is like AIC/BIC — model selection tools
  that balance fit vs complexity. Same spirit as regularization.
```

---

## 🧮 P13: Logistic Regression

> [Ch 17](./Statistics_BootCamp_THEORY.md#chapter-17--logistic-regression) | [Problem Index](#-problem-index)

**Q: A logistic model: ln(p/(1-p)) = -3 + 0.5*x, where x = study hours, p = P(pass). (a) Find P(pass) for x=8 hours. (b) At what x is P(pass) = 0.5? (c) Interpret the coefficient 0.5.**

### What's happening?

```
Linear regression predicts continuous y. But "pass/fail" is BINARY (0 or 1).
Logistic regression predicts the PROBABILITY of success.

  The SIGMOID (logistic) function:
  P(Y=1)
  1.0 |                --------
      |             /
  0.5 |          /           <- decision boundary
      |       /
  0.0 |------
      +--+--+--+--+--+--+-- x
         2  4  6  8  10
```

### (a) P(pass) for x=8

```
ln(p/(1-p)) = -3 + 0.5*8 = -3 + 4 = 1

Now solve for p:
  p/(1-p) = e^1 = 2.718
  p = 2.718 * (1-p)
  p = 2.718 - 2.718*p
  p + 2.718*p = 2.718
  3.718*p = 2.718
  p = 2.718/3.718 = 0.731

OR use the sigmoid formula directly:
  p = 1 / (1 + e^(-1)) = 1 / (1 + 0.368) = 1/1.368 = 0.731

ANSWER: P(pass | 8 hours of study) = 73.1%
```

### (b) Decision boundary (P = 0.5)

```
When P = 0.5:  ln(0.5/0.5) = ln(1) = 0

So: -3 + 0.5*x = 0
    0.5*x = 3
    x = 6

ANSWER: At x=6 hours, the probability of passing is exactly 50%.
Students studying more than 6 hours are predicted to PASS.
Students studying less than 6 hours are predicted to FAIL.
```

### (c) Interpretation of coefficient

```
b1 = 0.5 means:

  Each additional hour of study increases the LOG-ODDS of passing by 0.5.

  In terms of ODDS RATIO: e^0.5 = 1.649
  "Each extra hour MULTIPLIES the odds of passing by 1.649"
  "The odds of passing increase by 64.9% per additional hour."

  NOTE: It does NOT mean P increases by 0.5! The effect on P depends
  on where you are on the sigmoid curve. Near the middle (P=0.5),
  the effect is large. Near the extremes (P near 0 or 1), it's small.

  AI/ML: Every neuron in a neural net with sigmoid activation
  is doing logistic regression! The weights are the b coefficients.
```

---

## 🧮 P14: Bayesian Inference

> [Ch 18](./Statistics_BootCamp_THEORY.md#chapter-18--bayesian-inference) | [Problem Index](#-problem-index)

**Q: A coin may be fair or biased. Prior: P(fair)=0.6, P(biased with p=0.8)=0.4. You flip it 5 times and get 4 heads. (a) Find posterior P(fair|data). (b) Now use conjugate prior: p ~ Beta(2,2). Observe 7 heads in 10 flips. Find posterior.**

### (a) Discrete Bayesian Update

```
PRIOR:
  P(fair)   = 0.6    (fair means p=0.5)
  P(biased) = 0.4    (biased means p=0.8)

DATA: 4 heads in 5 flips.

LIKELIHOOD (using Binomial):
  P(4H in 5 | fair):   C(5,4) * 0.5^4 * 0.5^1 = 5 * 0.03125 = 0.15625
  P(4H in 5 | biased): C(5,4) * 0.8^4 * 0.2^1 = 5 * 0.08192 = 0.4096

BAYES' THEOREM:
  P(fair|data) = P(data|fair)*P(fair) / P(data)

  P(data) = P(data|fair)*P(fair) + P(data|biased)*P(biased)
           = 0.15625*0.6 + 0.4096*0.4
           = 0.09375 + 0.16384
           = 0.25759

  P(fair|data)   = 0.09375 / 0.25759 = 0.364
  P(biased|data) = 0.16384 / 0.25759 = 0.636

DIAGRAM:
  PRIOR:     fair=0.60 ████████████  biased=0.40 ████████
  POSTERIOR: fair=0.36 ███████       biased=0.64 ████████████

  Seeing 4/5 heads SHIFTED our belief toward biased.
  Prior: 60% fair.  Posterior: 36% fair.  Data updated our belief!

ANSWER: P(fair | 4 heads in 5 flips) = 0.364
```

### (b) Conjugate Prior: Beta-Binomial

```
PRIOR: p ~ Beta(a=2, b=2)  (symmetric, mildly favors p=0.5)

  Beta(2,2) looks like:
  f(p)
    |    *****
    |  **     **
    | *         *
    |*           *
    +--+--+--+--+-- p
    0  0.25 0.5 0.75  1

DATA: x=7 heads in n=10 flips.

CONJUGATE UPDATE RULE:
  Prior:     Beta(a, b)
  Data:      x successes in n trials
  Posterior: Beta(a + x, b + n - x)

  Posterior: Beta(2+7, 2+10-7) = Beta(9, 5)

POSTERIOR MEAN:
  E[p|data] = a'/(a'+b') = 9/(9+5) = 9/14 = 0.643

COMPARE:
  Prior mean:    a/(a+b)     = 2/4 = 0.500
  MLE:           x/n         = 7/10 = 0.700
  Posterior mean: (a+x)/(a+b+n) = 9/14 = 0.643  (between prior and MLE!)

DIAGRAM:
  f(p)
    |           *           <- Posterior Beta(9,5)
    |          * *             peaks near 0.64
    |    ..   *   *
    |   .  . *     *        <- Prior Beta(2,2)
    |  .    *       *          centered at 0.5
    | .   *          *
    +--+--+--+--+--+--+-- p
    0    0.25  0.5  0.7  1
                    ^
               Posterior pulled toward data

  With MORE data, the posterior concentrates tighter around MLE.
  The prior matters LESS as you get more data.
```

---

## 🧮 P15: Bayesian vs Frequentist Comparison

> [Ch 19](./Statistics_BootCamp_THEORY.md#chapter-19--bayesian-vs-frequentist) | [Problem Index](#-problem-index)

**Q: Sample: n=25, X_bar=100, s=15. (a) Frequentist 95% CI. (b) Bayesian 95% credible interval with flat prior. (c) Bayesian with informative prior N(90, 10^2). (d) Compare and interpret.**

### (a) Frequentist 95% CI

```
sigma unknown, use t-interval.
df = n-1 = 24.  t_(0.025, 24) = 2.064.

SE = s/sqrt(n) = 15/sqrt(25) = 15/5 = 3.0

CI = X_bar +/- t * SE = 100 +/- 2.064*3.0 = 100 +/- 6.19

95% CI = (93.81, 106.19)

INTERPRETATION: "If we repeated this experiment many times,
95% of such intervals would contain the true mean."
It does NOT mean "95% probability u is in this interval."
```

### (b) Bayesian with flat (uninformative) prior

```
Flat prior: P(u) = constant for all u. (No prior information.)

With flat prior, the Bayesian posterior = N(X_bar, SE^2) = N(100, 9).

95% CREDIBLE INTERVAL:
  100 +/- 1.96*3.0 = (94.12, 105.88)

  (Nearly identical to frequentist CI with flat prior!)

INTERPRETATION: "There is a 95% probability that u lies in (94.12, 105.88)."
This IS a direct probability statement about u! (Unlike frequentist CI.)
```

### (c) Bayesian with informative prior N(90, 100)

```
Prior:      u ~ N(u0=90, tau^2=100)  -> prior SD = 10
Likelihood: X_bar | u ~ N(u, sigma^2/n) -> N(u, 9)  (SE^2=9)

POSTERIOR (Normal-Normal conjugate):
  Posterior precision = 1/tau^2 + n/sigma^2 = 1/100 + 1/9 = 0.01 + 0.111 = 0.121
  Posterior variance  = 1/0.121 = 8.26
  Posterior SD        = sqrt(8.26) = 2.87

  Posterior mean = (u0/tau^2 + X_bar*n/sigma^2) / (1/tau^2 + n/sigma^2)
                 = (90/100 + 100/9) / (0.01 + 0.111)
                 = (0.9 + 11.11) / 0.121
                 = 12.01 / 0.121
                 = 99.26

Posterior: u | data ~ N(99.26, 8.26)

95% CREDIBLE INTERVAL:
  99.26 +/- 1.96*2.87 = 99.26 +/- 5.63 = (93.63, 104.89)

POSTERIOR MEAN = 99.26  (pulled toward prior of 90 from data of 100)
```

### (d) Comparison

```
  Method          | Interval         | Center | Width | Interpretation
  ----------------+------------------+--------+-------+-----------------
  Frequentist CI  | (93.81, 106.19)  | 100.00 | 12.38 | Repeated sampling
  Bayesian (flat) | (94.12, 105.88)  | 100.00 | 11.76 | P(u in interval)=95%
  Bayesian (info) | (93.63, 104.89)  |  99.26 | 11.26 | P(u in interval)=95%

  DIAGRAM:
  Frequentist:  |-------[=======*=======]-------|
  Bayes (flat): |--------[======*======]--------|
  Bayes (info): |-------[=====*======]----------|
                90     94   97  100  103  106  110
                 ^                ^
            prior mean=90    data X_bar=100

  KEY INSIGHTS:
  1. With FLAT prior, Bayesian ~ Frequentist (nearly identical).
  2. With INFORMATIVE prior, Bayesian is pulled toward prior -> narrower CI.
  3. Bayesian interpretation is MORE INTUITIVE ("95% chance u is here").
  4. With MORE data, prior matters less -> all methods converge.

  AI/ML:
  - Regularization (L2/Ridge) = Bayesian with Gaussian prior on weights.
  - More regularization = stronger prior = more shrinkage toward 0.
  - Bayesian neural nets give UNCERTAINTY estimates on predictions.
  - Frequentist methods dominate when you have lots of data and no prior.
```

---
---

## 60-SECOND REVISION BOX

```
+------------------------------------------------------------------+
| STATISTICS IN 60 SECONDS                                          |
|                                                                  |
| Data -> Inference (reverse of probability).                      |
| X_bar estimates u. s^2 estimates sigma^2 (use n-1!).             |
| MLE: maximize L(theta) = product of f(xi|theta).                |
| MSE = Bias^2 + Variance (tradeoff!).                            |
| CI: X_bar +/- (z or t) * SE.  95% uses z=1.96 or t-table.      |
| Hypothesis: H0=nothing special. Reject if p-value < alpha.      |
| Z-test: sigma known. T-test: sigma unknown (df=n-1).            |
| Type I=false alarm. Type II=miss. Power=1-beta.                 |
| Chi^2: sum (O-E)^2/E for categorical data.                      |
| ANOVA: F=MSB/MSW for comparing 3+ group means.                  |
| Regression: y-hat=b0+b1*x. b1=Sxy/Sxx. R^2=1-SSE/SST.         |
| Logistic: P=sigmoid(b0+b1*x). Uses MLE, not least squares.     |
| Bayesian: Posterior = Likelihood * Prior / Evidence.             |
| Bayesian with flat prior ~ Frequentist CI.                      |
| More data -> prior matters less -> all methods agree.           |
+------------------------------------------------------------------+
```

---

> [<< INDEX](./Statistics_BootCamp_INDEX.md) | [<< Theory Guide](./Statistics_BootCamp_THEORY.md)
>
> Created for: ODS | AI
