# 💻 ML Parameter Estimation: PRACTICE

### *Code it, test it.*

> **Nav:** [📖 THEORY](ml_parameter_estimation_theory.md) | [🔢 NUMERICAL](ml_parameter_estimation_numerical.md) | 💻 **PRACTICE**

---

## Ex1: MLE of Bernoulli from raw flips

```python
import numpy as np

# Simulate a biased coin
rng = np.random.default_rng(42)
true_theta = 0.7
flips = rng.binomial(n=1, p=true_theta, size=100)   # 100 flips

# MLE = sample proportion
theta_mle = flips.mean()
print(f"True theta:  {true_theta}")
print(f"MLE theta:   {theta_mle:.3f}")      # ~0.7
print(f"k = {flips.sum()}, n = {len(flips)}")
```

---

## Ex2: MLE vs Unbiased Variance for Gaussian

```python
import numpy as np

rng = np.random.default_rng(0)
x = rng.normal(loc=5.0, scale=2.0, size=30)

mu_mle = x.mean()
var_mle      = ((x - mu_mle) ** 2).mean()       # ÷ n   — MLE (biased)
var_unbiased = ((x - mu_mle) ** 2).sum() / (len(x) - 1)  # ÷ (n−1)

print(f"μ̂        = {mu_mle:.3f}")
print(f"σ²_MLE    = {var_mle:.3f}   (÷ n)")
print(f"σ²_unbiased = {var_unbiased:.3f}   (÷ n−1)")
print(f"np.var default: {np.var(x):.3f}        (÷ n)")
print(f"np.var ddof=1:  {np.var(x, ddof=1):.3f}   (÷ n−1)")
```

---

## Ex3: MAP with Beta prior — pulling a noisy estimate toward prior

```python
def bernoulli_map(k, n, alpha, beta):
    """MAP = mode of Beta(alpha+k, beta+n−k)."""
    a_post, b_post = alpha + k, beta + n - k
    if a_post <= 1 or b_post <= 1:
        return float('nan')     # mode undefined
    return (a_post - 1) / (a_post + b_post - 2)

k, n = 7, 10
print("MLE       :", k / n)                         # 0.700
print("Uniform(1,1) MAP =", bernoulli_map(k, n, 1, 1))   # 0.700 ~ MLE
print("Beta(2,2)    MAP =", bernoulli_map(k, n, 2, 2))   # 0.667
print("Beta(10,10)  MAP =", bernoulli_map(k, n, 10, 10)) # ~0.571
```

---

## Ex4: Visualising a Beta posterior update sequentially

```python
import numpy as np
from scipy.stats import beta
import matplotlib.pyplot as plt

rng = np.random.default_rng(1)
flips = rng.binomial(1, 0.7, size=50)

alpha, beta_param = 2, 2       # prior
x = np.linspace(0, 1, 500)

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(x, beta.pdf(x, alpha, beta_param), label="Prior Beta(2,2)", lw=2)

for n_seen in [5, 20, 50]:
    k = flips[:n_seen].sum()
    a_post = alpha + k
    b_post = beta_param + n_seen - k
    ax.plot(x, beta.pdf(x, a_post, b_post),
            label=f"After n={n_seen} (k={k})")
ax.axvline(0.7, color='k', ls='--', alpha=0.4, label='true θ = 0.7')
ax.set_xlabel("θ"); ax.set_ylabel("density"); ax.legend()
plt.tight_layout(); plt.show()
```

Shows how the posterior sharpens around the true θ=0.7 as data grows.

---

## Ex5: Gaussian-Gaussian closed-form update

```python
def normal_update(mu0, var0, x, var_known):
    """σ² known, conjugate Normal prior on μ."""
    n = len(x)
    mu_post = (var_known * mu0 + var0 * x.sum()) / (var_known + n * var0)
    var_post = (var_known * var0) / (var_known + n * var0)
    return mu_post, var_post

import numpy as np
x = np.array([108, 112, 109, 111])          # 4 test scores
mu_post, var_post = normal_update(mu0=100, var0=25, x=x, var_known=16)
print(f"Posterior μ  ≈ {mu_post:.3f}")       # ≈ 108.62
print(f"Posterior σ² ≈ {var_post:.3f}")      # ≈ 3.45
print(f"Posterior σ  ≈ {var_post**0.5:.3f}") # ≈ 1.857
```

---

## Ex6: Ridge Regression as MAP (Gaussian prior on w)

```python
import numpy as np
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression, Ridge

X, y = make_regression(n_samples=30, n_features=50, noise=10, random_state=0)

# MLE = ordinary least squares → overfits with p > n after regularization grid
ols = LinearRegression().fit(X, y)
ridge = Ridge(alpha=1.0).fit(X, y)   # alpha = σ² / τ²

print("OLS   ||w||²:", (ols.coef_ ** 2).sum().round(2))
print("Ridge ||w||²:", (ridge.coef_ ** 2).sum().round(2))
print("Ridge pulls weights toward 0 → equivalent to a Gaussian MAP prior.")
```

---

## Ex7: MLE fitting with scipy.stats

```python
import numpy as np
from scipy import stats

rng = np.random.default_rng(7)
data = rng.normal(loc=10, scale=3, size=200)

# scipy's .fit() IS maximum-likelihood estimation
mu_hat, sigma_hat = stats.norm.fit(data)
print(f"MLE μ̂ = {mu_hat:.3f},  MLE σ̂ = {sigma_hat:.3f}")

# Exponential example
exp_data = rng.exponential(scale=1/0.5, size=200)   # true λ = 0.5 ⟹ mean = 2
loc, scale = stats.expon.fit(exp_data, floc=0)      # fix loc=0
print(f"MLE λ̂ = {1/scale:.3f}")                     # ≈ 0.5
```

---

## Ex8: "How much data do I need before prior washes out?"

```python
import numpy as np
from scipy.stats import beta

# Strong biased prior
a0, b0 = 50, 50            # centered at 0.5, effective sample size ≈ 100
true_theta = 0.8

for n in [10, 50, 100, 500, 2000]:
    rng = np.random.default_rng(n)
    flips = rng.binomial(1, true_theta, size=n)
    k = flips.sum()
    a_post, b_post = a0 + k, b0 + n - k
    mean_post = a_post / (a_post + b_post)
    print(f"n={n:>4}:  MLE={k/n:.3f},  posterior mean={mean_post:.3f}")
```

You'll see the posterior mean creep from ~0.5 toward 0.8 as n grows past the prior's effective sample size.

---

> **See also:** [📖 THEORY](ml_parameter_estimation_theory.md) · [🔢 NUMERICAL](ml_parameter_estimation_numerical.md)
>
> *ML · Parameter Estimation · github.com/rpaut03l/TS-01*
