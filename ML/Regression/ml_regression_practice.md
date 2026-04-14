# 💻 ML Regression: PRACTICE

### *Code it, test it.*

> **Nav:** [📖 THEORY](ml_regression_theory.md) | [🔢 NUMERICAL](ml_regression_numerical.md) | 💻 **PRACTICE**

---

## Ex1: Simple Linear Regression — closed form from scratch

```python
import numpy as np

x = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([2, 4, 5, 4, 5], dtype=float)

x_bar, y_bar = x.mean(), y.mean()
beta1 = ((x - x_bar) * (y - y_bar)).sum() / ((x - x_bar) ** 2).sum()
beta0 = y_bar - beta1 * x_bar

print(f"β0 = {beta0:.3f},  β1 = {beta1:.3f}")   # 2.2, 0.6
print("ŷ =", beta0 + beta1 * x)
```

---

## Ex2: Multiple Linear Regression via the normal equation

```python
import numpy as np

X_raw = np.array([[1, 1],
                  [1, 2],
                  [2, 2],
                  [2, 3]], dtype=float)
y = np.array([6, 8, 11, 14], dtype=float)

X = np.hstack([np.ones((X_raw.shape[0], 1)), X_raw])   # add intercept column

beta = np.linalg.inv(X.T @ X) @ X.T @ y
print("β =", beta)                                     # [0.25, 3.0, 2.5]
print("ŷ =", X @ beta)
```

Compare to `sklearn`:

```python
from sklearn.linear_model import LinearRegression
lr = LinearRegression().fit(X_raw, y)
print(lr.intercept_, lr.coef_)      # 0.25, [3.0, 2.5]
```

---

## Ex3: Ridge & Lasso — and feature scaling

```python
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import cross_val_score

X, y = load_diabetes(return_X_y=True)

models = {
    "OLS  ": make_pipeline(StandardScaler(), LinearRegression()),
    "Ridge": make_pipeline(StandardScaler(), Ridge(alpha=1.0)),
    "Lasso": make_pipeline(StandardScaler(), Lasso(alpha=0.1)),
}
for name, m in models.items():
    r2 = cross_val_score(m, X, y, cv=5, scoring="r2").mean()
    print(f"{name}  CV R² = {r2:.4f}")
```

Notice: without `StandardScaler`, Ridge/Lasso penalize features inconsistently.

---

## Ex4: Lasso feature selection — which columns survived?

```python
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LassoCV
from sklearn.preprocessing import StandardScaler

X, y = load_diabetes(return_X_y=True)
Xs = StandardScaler().fit_transform(X)

lasso = LassoCV(cv=5, random_state=0).fit(Xs, y)
print(f"Best α:  {lasso.alpha_:.5f}")
for i, c in enumerate(lasso.coef_):
    mark = "⛔ZERO" if abs(c) < 1e-8 else f"{c:+.3f}"
    print(f"feature {i:2d}:  {mark}")
```

---

## Ex5: Logistic Regression — full pipeline with metrics

```python
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import (accuracy_score, precision_score, recall_score,
                              f1_score, roc_auc_score, confusion_matrix)

X, y = load_breast_cancer(return_X_y=True)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, stratify=y, random_state=0)

clf = make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000, C=1.0))
clf.fit(X_tr, y_tr)

proba = clf.predict_proba(X_te)[:, 1]
pred  = clf.predict(X_te)

print("Accuracy :", accuracy_score(y_te, pred).round(3))
print("Precision:", precision_score(y_te, pred).round(3))
print("Recall   :", recall_score(y_te, pred).round(3))
print("F1       :", f1_score(y_te, pred).round(3))
print("ROC-AUC  :", roc_auc_score(y_te, proba).round(3))
print("Confusion matrix:\n", confusion_matrix(y_te, pred))
```

`C` is the *inverse* of λ in sklearn — smaller C ⇒ more regularization.

---

## Ex6: Polynomial regression with regularization

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import Ridge
from sklearn.pipeline import make_pipeline

rng = np.random.default_rng(0)
X = np.sort(5 * rng.random(40)).reshape(-1, 1)
y = np.cos(X).ravel() + 0.2 * rng.standard_normal(40)

grid = np.linspace(0, 5, 300).reshape(-1, 1)

for deg, alpha in [(2, 0), (9, 0), (9, 1.0)]:
    model = make_pipeline(
        PolynomialFeatures(deg, include_bias=False),
        StandardScaler(),
        Ridge(alpha=alpha if alpha > 0 else 1e-12),
    ).fit(X, y)
    plt.plot(grid, model.predict(grid), label=f"deg={deg}, α={alpha}")
plt.scatter(X, y, c="k", s=15)
plt.legend(); plt.title("Polynomial fit: underfit vs overfit vs ridge"); plt.show()
```

High-degree unregularized ridge oscillates wildly; adding α tames it.

---

## Ex7: Diagnostics — residual plot & Q–Q plot

```python
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression

X, y = fetch_california_housing(return_X_y=True)
lr = LinearRegression().fit(X, y)
resid = y - lr.predict(X)

fig, ax = plt.subplots(1, 2, figsize=(10, 4))
ax[0].scatter(lr.predict(X), resid, s=3, alpha=0.3)
ax[0].axhline(0, color="r")
ax[0].set_xlabel("ŷ"); ax[0].set_ylabel("residuals")
ax[0].set_title("Residuals vs fitted (should look random)")

sm.qqplot(resid, line="45", ax=ax[1])
ax[1].set_title("Q–Q plot (points should hug the line)")
plt.tight_layout(); plt.show()
```

If the residual plot shows a funnel → heteroscedasticity. If Q–Q plot bends → errors aren't Gaussian → inference is off.

---

## Ex8: Quick hyperparameter search for Ridge / Lasso

```python
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.linear_model import RidgeCV, LassoCV, ElasticNetCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

X, y = load_diabetes(return_X_y=True)
Xs = StandardScaler().fit_transform(X)

alphas = np.logspace(-3, 2, 50)
print("Ridge  α =", RidgeCV(alphas=alphas, cv=5).fit(Xs, y).alpha_)
print("Lasso  α =", LassoCV(alphas=alphas, cv=5, random_state=0).fit(Xs, y).alpha_)
enet = ElasticNetCV(l1_ratio=[0.1, 0.5, 0.9], alphas=alphas, cv=5, random_state=0).fit(Xs, y)
print("ElasticNet (α, l1_ratio) =", enet.alpha_, enet.l1_ratio_)
```

---

> **See also:** [📖 THEORY](ml_regression_theory.md) · [🔢 NUMERICAL](ml_regression_numerical.md) · [Legacy: SLR Practice](simple_linear_regression_pe_practice.md)
>
> *ML · Regression · github.com/rpaut03l/TS-01*
