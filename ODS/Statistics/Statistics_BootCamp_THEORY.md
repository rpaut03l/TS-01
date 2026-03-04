# 📘 Statistics BootCamp — THEORY GUIDE

### 🎓 ODS | AI | All 20 Chapters + Q&A + AI/ML Uses + Diagrams
> **Navigation:** [<< INDEX](./Statistics_BootCamp_INDEX.md) | [>> Practice Guide](./Statistics_BootCamp_PRACTICE.md)
>
> Every concept explained from scratch. Nothing assumed. Pictures first, formulas second.

---

## 📚 Chapter Index

| Block | Chapters | Topics |
|-------|----------|--------|
| **FOUNDATIONS** | Ch 1-4 | What is statistics, sampling, descriptive stats, CLT |
| **ESTIMATION** | Ch 5-8 | Point estimation, bias/variance, MLE, confidence intervals |
| **TESTING** | Ch 9-14 | Hypothesis testing, Z/t/chi-sq tests, ANOVA |
| **MODELING** | Ch 15-20 | Regression, logistic, Bayesian, ML connections |

---

## BLOCK 1: FOUNDATIONS (Ch 1-4)

---

## Chapter 1 — What Is Statistics?

> [<< INDEX](./Statistics_BootCamp_INDEX.md) | [Chapter Index](#-chapter-index)

### The Big Picture

```
  PROBABILITY and STATISTICS are INVERSES of each other:

  PROBABILITY (forward):
    "I KNOW the coin is fair (p=0.5).
     What data should I expect?" --> predict outcomes

  STATISTICS (backward):
    "I SEE the data (72 heads in 100 flips).
     Is the coin fair?" --> infer the rules

  DIAGRAM:
  Probability:  Rules ---------> Data      (deduction)
  Statistics:   Data  ---------> Rules     (induction)

  PROBABILITY: "God's perspective" — you know the truth, predict observations
  STATISTICS:  "Human's perspective" — you see observations, guess the truth
```

### Why does an AI/ML engineer need statistics?

```
  Every ML pipeline IS statistics:
  1. COLLECT data (sampling)
  2. SUMMARIZE data (descriptive stats)
  3. FIT a model (estimation / MLE)
  4. EVALUATE the model (hypothesis testing, CI)
  5. PREDICT new outcomes (regression, classification)
  6. UPDATE beliefs (Bayesian inference)

  "Machine learning is statistics on steroids."
```

### Q&A

**Q: What's the difference between a parameter and a statistic?**
> Parameter = number describing the POPULATION (unknown, fixed). Example: true average height of ALL Indians.
> Statistic = number computed from a SAMPLE (known, varies). Example: average height of 100 surveyed people.
> Statistics ESTIMATES parameters. That's the whole game.

---

## Chapter 2 — Populations, Samples & Sampling

> [<< INDEX](./Statistics_BootCamp_INDEX.md) | [Practice P1](./Statistics_BootCamp_PRACTICE.md#-p1-descriptive-statistics) | [Chapter Index](#-chapter-index)

### Population vs Sample

```
  POPULATION = the ENTIRE group you care about
    - All M.Tech students at IIT Jodhpur
    - All images in ImageNet
    - All possible coin flips (infinite!)

  SAMPLE = a SUBSET you actually observe
    - 30 students you surveyed
    - 1000 images you labeled
    - 100 coin flips you did

  DIAGRAM:
  +--------------------------------------------------+
  | POPULATION (N = huge or infinite)                 |
  | Parameters: mu (mean), sigma (std dev), p (prop.) |
  | UNKNOWN! We want to learn these.                  |
  |                                                   |
  |    +------------------+                           |
  |    | SAMPLE (n = small)|                          |
  |    | Statistics: X_bar, |                         |
  |    | s, p-hat           |                         |
  |    | KNOWN! We compute  |                         |
  |    | these from data.   |                         |
  |    +------------------+                           |
  +--------------------------------------------------+
```

### Types of Sampling

```
  SIMPLE RANDOM SAMPLE (SRS): every subset of size n equally likely
    -> The gold standard. Like drawing names from a hat.

  STRATIFIED: divide population into groups, sample from each
    -> Ensures representation. Like sampling from each IIT department.

  SYSTEMATIC: every k-th item (e.g., every 10th person)

  CONVENIENCE: whatever is easy to get (BIASED! Avoid in research)

  IID ASSUMPTION: X1, X2, ..., Xn are
    Independent: one observation doesn't affect another
    Identically Distributed: all from the same population
    This is THE core assumption behind most of statistics!
```

---

## Chapter 3 — Descriptive Statistics

> [<< INDEX](./Statistics_BootCamp_INDEX.md) | [Practice P1](./Statistics_BootCamp_PRACTICE.md#-p1-descriptive-statistics) | [Chapter Index](#-chapter-index)

### Measures of Center

```
  MEAN: X_bar = (1/n) * sum(Xi)
    "Add up everything, divide by n"
    Sensitive to outliers. One billionaire skews the average.

  MEDIAN: middle value when sorted
    Robust to outliers. 50th percentile.

  MODE: most frequent value
    The only measure for categorical data (e.g., most popular color).

  DIAGRAM:
  Symmetric:          Right-skewed:
       *****               ***
      *******             *****
     *********           ******* *
  mean=median=mode     mode < median < mean
                       (mean pulled right by outliers)
```

### Measures of Spread

```
  VARIANCE: s^2 = (1/(n-1)) * sum((Xi - X_bar)^2)
    "Average squared distance from the mean"
    WHY n-1? Bessel's correction makes it UNBIASED.

  STD DEV: s = sqrt(s^2)     "Same units as data"

  RANGE: max - min            "Simplest but weakest"

  IQR: Q3 - Q1               "Middle 50% spread, robust to outliers"

  WHY n-1 (Bessel's Correction)?
    If you use the SAMPLE mean X_bar to compute deviations,
    you've already "used up" 1 piece of info (X_bar itself).
    Only n-1 deviations are FREE to vary (degrees of freedom).
    Dividing by n would UNDERESTIMATE the true variance.
```

---

## Chapter 4 — Sampling Distributions & CLT

> [<< INDEX](./Statistics_BootCamp_INDEX.md) | [Practice P2](./Statistics_BootCamp_PRACTICE.md#-p2-sampling-distribution--clt) | [Chapter Index](#-chapter-index)

### The Key Insight

```
  X_bar is ITSELF a random variable!
  If you took MANY samples of size n, each gives a different X_bar.
  The distribution of all possible X_bars = SAMPLING DISTRIBUTION.

  DIAGRAM: Take many samples from population
  Population (u=100, sigma=15)
    Sample 1 (n=30): X_bar = 98.3
    Sample 2 (n=30): X_bar = 102.1
    Sample 3 (n=30): X_bar = 99.7
    ...
    Sample 1000: X_bar = 100.5

  Plot all X_bars --> BELL CURVE centered at u=100!

  PROPERTIES:
    E[X_bar] = mu              (unbiased! centers on truth)
    Var(X_bar) = sigma^2 / n   (shrinks as n grows!)
    SE = sigma / sqrt(n)       (standard error)
```

### Central Limit Theorem (CLT) — THE Bridge

```
  THEOREM: For large n, X_bar is approximately Normal:

    X_bar ~ N(mu, sigma^2/n)

  REGARDLESS of the shape of the original population!

  DIAGRAM: How CLT transforms distributions
  Original population:     Sampling dist of X_bar (n=30):
  ▓ ▓     ▓ ▓                      *****
  ▓ ▓ ▓   ▓ ▓ ▓                  *********
  ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓              *************
  (any ugly shape!)           (beautiful bell curve!)

  WHY THIS MATTERS:
  CLT lets us use Normal-based formulas (Z-scores, CI, tests)
  even when the data itself isn't Normal!

  PRACTICAL RULE: n >= 30 is usually "large enough"
  (for heavily skewed data, may need n >= 50+)
```

---

## BLOCK 2: ESTIMATION (Ch 5-8)

---

## Chapter 5 — Point Estimation

> [<< INDEX](./Statistics_BootCamp_INDEX.md) | [Practice P3](./Statistics_BootCamp_PRACTICE.md#-p3-point-estimation--bias) | [Chapter Index](#-chapter-index)

### The Idea

```
  POINT ESTIMATE = single "best guess" for an unknown parameter

  Parameter (unknown)    Estimator (from sample)
  -----------------      ----------------------
  mu (population mean)   X_bar = sample mean
  sigma^2 (pop variance) s^2 = sample variance
  p (pop proportion)     p-hat = successes / n
  lambda (Poisson rate)  X_bar (also!)

  GOOD ESTIMATORS should be:
  1. UNBIASED: E[theta-hat] = theta (correct on average)
  2. CONSISTENT: theta-hat -> theta as n -> infinity
  3. EFFICIENT: smallest variance among all unbiased estimators
```

---

## Chapter 6 — Bias, Variance & MSE

> [<< INDEX](./Statistics_BootCamp_INDEX.md) | [Practice P3](./Statistics_BootCamp_PRACTICE.md#-p3-point-estimation--bias) | [Chapter Index](#-chapter-index)

### The Bias-Variance Tradeoff

```
  MSE(theta-hat) = Bias^2 + Variance

  Bias = E[theta-hat] - theta    "systematic error"
  Variance = Var(theta-hat)      "random scatter"

  DIAGRAM (dartboard analogy):
  Low Bias, Low Var:    Low Bias, High Var:
      +--+                  +--+
      |**|                  | *|  *
      |**|                  |* |    *
      +--+                  +--+  *
   (accurate & precise)   (accurate but scattered)

  High Bias, Low Var:   High Bias, High Var:
      +--+                  +--+
      |  |  **              |  |  *
      |  |  **              |  | *  *
      +--+                  +--+    *
   (wrong but consistent) (wrong & scattered)

  In ML this is FUNDAMENTAL:
    Simple model (few params) = high bias, low variance (underfitting)
    Complex model (many params) = low bias, high variance (overfitting)
    SWEET SPOT = minimum total error (MSE)
```

### Bessel's Correction Example

```
  WHY s^2 uses n-1:
    If s_biased^2 = (1/n) * sum((Xi-X_bar)^2)
    Then E[s_biased^2] = ((n-1)/n) * sigma^2 < sigma^2  (biased LOW!)

    Fix: s^2 = (1/(n-1)) * sum((Xi-X_bar)^2)
    Now E[s^2] = sigma^2  (unbiased!)

    The n-1 = DEGREES OF FREEDOM. We "used up" 1 df by estimating X_bar.
```

---

## Chapter 7 — Maximum Likelihood Estimation

> [<< INDEX](./Statistics_BootCamp_INDEX.md) | [Practice P4](./Statistics_BootCamp_PRACTICE.md#-p4-maximum-likelihood-estimation) | [Chapter Index](#-chapter-index)

### THE Most Important Estimation Method

```
  MLE = "Find the parameter value that makes the observed data MOST LIKELY"

  STEPS:
  1. Write down the LIKELIHOOD: L(theta) = product of f(xi|theta)
  2. Take the LOG: l(theta) = sum of ln(f(xi|theta))
  3. DIFFERENTIATE: dl/dtheta = 0
  4. SOLVE for theta-hat

  WHY take the log?
    Products become SUMS (much easier to differentiate!)
    ln(a*b*c) = ln(a) + ln(b) + ln(c)
    And the maximum of ln(L) is at the same theta as maximum of L.

  DIAGRAM:
  L(theta)
  0.02|            *
      |          *   *
      |        *       *
  0.01|      *           *
      |    *               *
      |  *                   *
  0.00+----+----+----+----+----
         2    3   3.5   4    5   theta
                   ^
              theta-hat (MLE) = the peak!
```

### MLE for Common Distributions

```
  Normal (unknown mu, known sigma):
    MLE of mu = X_bar (the sample mean!)

  Normal (unknown mu AND sigma):
    MLE of mu = X_bar
    MLE of sigma^2 = (1/n)*sum((Xi-X_bar)^2)  <- NOTE: 1/n, not 1/(n-1)!
    (MLE is BIASED for variance! But consistent.)

  Bernoulli (unknown p):
    MLE of p = p-hat = (number of successes) / n

  Poisson (unknown lambda):
    MLE of lambda = X_bar

  MLE is the FOUNDATION of training neural networks!
  "Minimize cross-entropy loss" = "Maximize likelihood"
```

---

## Chapter 8 — Confidence Intervals

> [<< INDEX](./Statistics_BootCamp_INDEX.md) | [Practice P5](./Statistics_BootCamp_PRACTICE.md#-p5-confidence-intervals) | [Chapter Index](#-chapter-index)

### From Point to Interval

```
  Point estimate: "mu is about 74.2"    (just one number)
  Confidence interval: "mu is in (71.8, 76.6) with 95% confidence"
    (a RANGE that probably contains the truth)

  FORMULA (sigma known):
    X_bar +/- z_(alpha/2) * sigma/sqrt(n)
    = X_bar +/- MARGIN OF ERROR

  FORMULA (sigma unknown, use t):
    X_bar +/- t_(alpha/2, n-1) * s/sqrt(n)

  DIAGRAM:
  |<---- 95% CI ---->|
  |                  |
  ----[---X_bar---]----
     Lower       Upper
     X_bar-ME   X_bar+ME
```

### What Does "95% Confidence" Actually Mean?

```
  NOT: "There's a 95% probability mu is in this interval"
  (mu is fixed! It's either in there or it's not.)

  CORRECT: "If we repeated this process many times,
  95% of the intervals we build would contain mu."

  DIAGRAM: 20 samples, each gives a CI
  CI  1: [----*----]       contains mu
  CI  2:   [----*----]     contains mu
  CI  3:          [----*----]     MISSES mu!
  CI  4:     [----*----]   contains mu
  ...
  CI 20: [----*----]       contains mu

  About 19 out of 20 (95%) capture the true mu.
  The interval is random, not mu!
```

### Common Critical Values

```
  Confidence Level   alpha   z_(alpha/2)
  ----------------   -----   -----------
  90%                0.10    1.645
  95%                0.05    1.96
  99%                0.01    2.576

  WIDER interval = MORE confident but LESS precise.
  NARROWER interval = LESS confident but MORE precise.
  More data (larger n) = narrower interval at SAME confidence!
```

---

## BLOCK 3: TESTING (Ch 9-14)

---

## Chapter 9 — Hypothesis Testing Framework

> [<< INDEX](./Statistics_BootCamp_INDEX.md) | [Practice P6](./Statistics_BootCamp_PRACTICE.md#-p6-z-test-for-a-mean) | [Chapter Index](#-chapter-index)

### The Logic of Hypothesis Testing

```
  1. State H0 (null = "nothing special") and H1 (alternative)
  2. Choose alpha (significance level, usually 0.05)
  3. Collect data, compute test statistic
  4. Find p-value = P(data this extreme or more | H0 true)
  5. If p-value < alpha: REJECT H0 (evidence against it!)
     If p-value >= alpha: FAIL TO REJECT H0 (not enough evidence)

  ANALOGY: Court trial
    H0 = "defendant is innocent" (default assumption)
    H1 = "defendant is guilty"
    Evidence = data
    "Reject H0" = "guilty verdict" (strong evidence)
    "Fail to reject" = "not guilty" (NOT the same as "innocent"!)

  DIAGRAM:
  H0 true (nothing happening)
  |                         |
  |    "Normal" data        | "Extreme" data
  |    (fail to reject)     | (reject H0!)
  |<--- 1-alpha = 95% ---->|<-- alpha = 5% -->|
  ════════════════════════════╗
                              ║ critical value
```

---

## Chapter 10 — Z-Test

> [<< INDEX](./Statistics_BootCamp_INDEX.md) | [Practice P6](./Statistics_BootCamp_PRACTICE.md#-p6-z-test-for-a-mean) | [Chapter Index](#-chapter-index)

```
  USE WHEN: testing a mean AND sigma is KNOWN

  Z = (X_bar - mu_0) / (sigma / sqrt(n))

  Under H0: Z ~ N(0,1)

  Two-tailed test (H1: mu != mu_0):
    Reject if |Z| > z_(alpha/2)

  One-tailed test (H1: mu > mu_0):
    Reject if Z > z_alpha

  DIAGRAM: Two-tailed at alpha=0.05
        reject        fail to reject       reject
  |<-- 2.5% -->|<------- 95% ------->|<-- 2.5% -->|
  ═════════════╬═══════════════════════╬═════════════
            -1.96                    +1.96
```

---

## Chapter 11 — T-Test

> [<< INDEX](./Statistics_BootCamp_INDEX.md) | [Practice P7](./Statistics_BootCamp_PRACTICE.md#-p7-t-test) | [Chapter Index](#-chapter-index)

```
  USE WHEN: testing a mean AND sigma is UNKNOWN (use s instead)

  T = (X_bar - mu_0) / (s / sqrt(n))     df = n - 1

  The t-distribution has HEAVIER TAILS than Normal.
  (More uncertainty because we estimated sigma.)

  As n -> infinity: t-distribution -> Normal

  DIAGRAM: t vs Normal
              Normal (Z)         t(df=5)
                *****             ****
              **     **         **    **
            **         **     **        **
          **             ** **            **
        **      Normal    ** t has fatter  **
      **     (thin tails)    tails (more    **
                              uncertainty)
```

---

## Chapter 12 — Type I & Type II Errors and Power

> [<< INDEX](./Statistics_BootCamp_INDEX.md) | [Practice P8](./Statistics_BootCamp_PRACTICE.md#-p8-type-i--type-ii-errors) | [Chapter Index](#-chapter-index)

```
  TRUTH TABLE:
                      H0 actually TRUE    H0 actually FALSE
  Reject H0           TYPE I ERROR         CORRECT!
  (say "guilty")      (false alarm)        (true positive)
                      P = alpha            P = 1 - beta = POWER

  Fail to reject H0   CORRECT!             TYPE II ERROR
  (say "not guilty")  (true negative)      (missed it!)
                      P = 1 - alpha        P = beta

  Type I  (alpha) = "crying wolf" = false positive = convicting innocent
  Type II (beta)  = "missing it"  = false negative = freeing guilty

  POWER = 1 - beta = P(correctly rejecting H0 when it's false)

  HOW TO INCREASE POWER:
    1. Increase n (more data!)
    2. Increase alpha (accept more false alarms)
    3. Larger true effect size
    4. Decrease sigma (less noise)
```

---

## Chapter 13 — Chi-Squared Tests

> [<< INDEX](./Statistics_BootCamp_INDEX.md) | [Practice P9](./Statistics_BootCamp_PRACTICE.md#-p9-chi-squared-goodness-of-fit) | [Chapter Index](#-chapter-index)

```
  FOR CATEGORICAL DATA (counts, not measurements)

  GOODNESS OF FIT: "Does data match an expected distribution?"
    chi^2 = sum of (Observed - Expected)^2 / Expected
    df = (number of categories) - 1

  INDEPENDENCE TEST: "Are two categorical variables related?"
    Expected = (row total * col total) / grand total
    chi^2 = sum of (O - E)^2 / E
    df = (rows - 1) * (cols - 1)

  If chi^2 is LARGE -> data doesn't fit expectations -> reject H0

  AI/ML: Chi-squared test for FEATURE SELECTION in categorical data.
  "Is this feature related to the target label?"
```

---

## Chapter 14 — ANOVA (F-Test)

> [<< INDEX](./Statistics_BootCamp_INDEX.md) | [Practice P10](./Statistics_BootCamp_PRACTICE.md#-p10-one-way-anova) | [Chapter Index](#-chapter-index)

```
  ANOVA = Analysis of Variance
  USE WHEN: comparing MEANS of 3 or more groups

  H0: mu_1 = mu_2 = ... = mu_k   (all group means equal)
  H1: at least one differs

  F = MSB / MSW = (between-group variance) / (within-group variance)

  MSB = SSB / (k-1)     SSB = sum of n_j * (X_bar_j - X_bar_overall)^2
  MSW = SSW / (N-k)     SSW = sum of sum of (Xij - X_bar_j)^2

  Large F -> groups are DIFFERENT -> reject H0

  DIAGRAM:
  Group A:  * * * *         mean_A
  Group B:    * * * *       mean_B  (close to A?)
  Group C:          * * * * mean_C  (far from A,B!)

  If between-group spread >> within-group spread -> F is large -> significant

  AI/ML: ANOVA is used in FEATURE IMPORTANCE.
  "Does this feature significantly affect the target?"
```

---

## BLOCK 4: MODELING (Ch 15-20)

---

## Chapter 15 — Simple Linear Regression

> [<< INDEX](./Statistics_BootCamp_INDEX.md) | [Practice P11](./Statistics_BootCamp_PRACTICE.md#-p11-simple-linear-regression) | [Chapter Index](#-chapter-index)

### The Model

```
  y = b0 + b1*x + error

  b1 (slope) = Sxy / Sxx
    Sxy = sum((xi - x_bar)(yi - y_bar))
    Sxx = sum((xi - x_bar)^2)

  b0 (intercept) = y_bar - b1 * x_bar

  DIAGRAM:
  y |          *  /
    |        *  /  *
    |      * /      residual = yi - y-hat
    |    * /    *   |
    |  */*        <-+
    | / *
    |/
    +------------------ x
    y-hat = b0 + b1*x  (the fitted line)

  The line minimizes SSE = sum((yi - y-hat_i)^2)
  This is called ORDINARY LEAST SQUARES (OLS).
```

### R-Squared

```
  SST = sum((yi - y_bar)^2)     total variability in y
  SSR = sum((y-hat_i - y_bar)^2)  variability explained by x
  SSE = sum((yi - y-hat_i)^2)     residual (unexplained)

  SST = SSR + SSE

  R^2 = SSR / SST = 1 - SSE/SST

  R^2 = 0: model explains NOTHING (flat line)
  R^2 = 1: model explains EVERYTHING (perfect fit)
  R^2 = 0.85: model explains 85% of the variability in y

  AI/ML: OLS regression IS the simplest form of supervised learning.
  "Minimize MSE" = "Maximize likelihood under Gaussian noise".
```

---

## Chapter 16 — Multiple Regression

> [<< INDEX](./Statistics_BootCamp_INDEX.md) | [Practice P12](./Statistics_BootCamp_PRACTICE.md#-p12-multiple-regression) | [Chapter Index](#-chapter-index)

```
  y = b0 + b1*x1 + b2*x2 + ... + bp*xp + error

  In MATRIX form:  y = X*beta + epsilon
    beta-hat = (X^T X)^(-1) X^T y   (normal equations)

  ADJUSTED R^2:
    R^2_adj = 1 - (1-R^2)*(n-1)/(n-p-1)
    Penalizes adding useless features. Use THIS for model comparison.

  AI/ML: This IS the foundation of:
    - Feature engineering (which x's to include?)
    - Ridge regression (add L2 penalty)
    - Lasso regression (add L1 penalty)
    - Neural network output layers (linear combination)
```

---

## Chapter 17 — Logistic Regression

> [<< INDEX](./Statistics_BootCamp_INDEX.md) | [Practice P13](./Statistics_BootCamp_PRACTICE.md#-p13-logistic-regression) | [Chapter Index](#-chapter-index)

```
  FOR BINARY classification (y = 0 or 1)

  P(y=1 | x) = 1 / (1 + e^(-(b0 + b1*x)))  = sigmoid(b0 + b1*x)

  SIGMOID FUNCTION:
  P(y=1)
  1.0 |                    ________
      |                 /
  0.5 |              /
      |           /
  0.0 |__________/
      +-------------------------------- b0 + b1*x
      Decision boundary at P = 0.5

  Trained by MAXIMIZING LIKELIHOOD (not OLS!)
  Loss = negative log-likelihood = CROSS-ENTROPY LOSS

  AI/ML: Logistic regression is the BUILDING BLOCK of neural nets.
  Each neuron with sigmoid activation IS a logistic regression!
```

---

## Chapter 18 — Bayesian Inference

> [<< INDEX](./Statistics_BootCamp_INDEX.md) | [Practice P14](./Statistics_BootCamp_PRACTICE.md#-p14-bayesian-inference) | [Chapter Index](#-chapter-index)

### The Bayesian Framework

```
  FREQUENTIST: theta is FIXED but unknown. Data is random.
  BAYESIAN:    theta is RANDOM. Has a probability distribution!

  BAYES' THEOREM FOR PARAMETERS:

  P(theta | data) = P(data | theta) * P(theta) / P(data)
  ^^posterior^^      ^^likelihood^^   ^^prior^^  ^^evidence^^

  Posterior is proportional to Likelihood * Prior

  DIAGRAM:
  Prior (before data):          Likelihood (data):       Posterior (after data):
       ****                          ***                      **
     **    **                      **   **                  **  **
   **        **           x       *       *        =      *      *
  **          **                **         **            **        *
  (what you believed)    (what data says)          (updated belief)
       wide/uncertain       peaked where          combines both!
                            data points to
```

### Conjugate Priors

```
  Some prior-likelihood pairs have CLEAN posteriors:

  Likelihood     Prior              Posterior
  ----------     -----              ---------
  Bernoulli      Beta(a,b)          Beta(a+successes, b+failures)
  Normal(mu,s)   Normal(m0,s0)      Normal(updated m, updated s)
  Poisson        Gamma(a,b)         Gamma(a+sum(xi), b+n)

  "Conjugate" = same family as prior. Makes math tractable!
```

---

## Chapter 19 — Bayesian vs Frequentist

> [<< INDEX](./Statistics_BootCamp_INDEX.md) | [Practice P15](./Statistics_BootCamp_PRACTICE.md#-p15-bayesian-vs-frequentist-comparison) | [Chapter Index](#-chapter-index)

```
  COMPARISON:

  Aspect          Frequentist              Bayesian
  ------          -----------              --------
  Parameter       Fixed (unknown number)   Random (has distribution)
  Probability     Long-run frequency       Degree of belief
  Prior info      Not used                 Encoded in prior
  Answer          CI, p-value              Posterior distribution
  "95% interval"  "95% of CIs contain mu"  "95% prob mu is here"
  Computation     Formulas / tables        Often needs MCMC
  Small data      Can struggle             Priors help stabilize
  Overfitting     Regularization           Prior = built-in regularization

  AI/ML CONNECTIONS:
    Frequentist: MLE, cross-validation, bootstrap
    Bayesian: MAP estimation, Bayesian neural nets, GP, uncertainty
    Ridge regression: Bayesian with Gaussian prior!
    Lasso regression: Bayesian with Laplace prior!
    Dropout in NNs: approximately Bayesian!
```

---

## Chapter 20 — Statistics in ML & AI

> [<< INDEX](./Statistics_BootCamp_INDEX.md) | [Chapter Index](#-chapter-index)

```
  EVERY ML concept maps to statistics:

  ML Concept              Statistical Foundation
  ----------              ----------------------
  Training                Maximum Likelihood Estimation
  Loss function           Negative log-likelihood
  Cross-entropy loss      MLE for classification
  MSE loss                MLE under Gaussian noise
  Regularization          Bayesian prior / penalized MLE
  Cross-validation        Estimating prediction error
  Bias-variance tradeoff  MSE = Bias^2 + Variance
  Batch normalization     Standardization (Z-scores)
  Dropout                 Approximate Bayesian inference
  Ensemble methods        Averaging reduces variance (CLT!)
  A/B testing             Hypothesis testing (two-sample t-test)
  Feature selection       ANOVA, chi-squared, correlation
  Confidence              Confidence intervals / credible intervals
  GPT uncertainty         Softmax probabilities (Bayesian interpretation)

  BOTTOM LINE:
  "You can't do ML without statistics. And you can't do statistics
   without probability. It's all one continuous chain."

  Probability --> Statistics --> Machine Learning --> AI
  (the math)     (the method)   (the automation)   (the application)
```

---

> [>> Practice Guide](./Statistics_BootCamp_PRACTICE.md) | [<< INDEX](./Statistics_BootCamp_INDEX.md)
>
> Created for: ODS | AI
