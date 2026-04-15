# 💻 ML Random Forest: PRACTICE

### *Code it, test it.*

> **Nav:** [📖 THEORY](ml_random_forest_theory.md) | [🔢 NUMERICAL](ml_random_forest_numerical.md) | 💻 **PRACTICE**

---

## Ex1: RF Classification — the minimal baseline

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

X, y = load_breast_cancer(return_X_y=True)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=0, stratify=y)

rf = RandomForestClassifier(
    n_estimators=300,
    max_features='sqrt',   # √p  → classification default
    oob_score=True,        # free validation
    random_state=0,
    n_jobs=-1,
)
rf.fit(X_tr, y_tr)

print(f"OOB score:   {rf.oob_score_:.3f}")
print(f"Test acc:    {accuracy_score(y_te, rf.predict(X_te)):.3f}")
print(classification_report(y_te, rf.predict(X_te)))
```

OOB score should be very close to the held-out test accuracy — the built-in validation works.

---

## Ex2: RF Regression — California housing

```python
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

X, y = fetch_california_housing(return_X_y=True)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=0)

rf = RandomForestRegressor(
    n_estimators=500,
    max_features=1/3,      # p/3  → regression default
    oob_score=True,
    random_state=0,
    n_jobs=-1,
)
rf.fit(X_tr, y_tr)
pred = rf.predict(X_te)

print(f"OOB R²:       {rf.oob_score_:.3f}")
print(f"Test MSE:     {mean_squared_error(y_te, pred):.3f}")
print(f"Test R²:      {r2_score(y_te, pred):.3f}")
```

---

## Ex3: Scan `n_estimators` using OOB error (no CV needed)

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)

oob_errors = []
ns = [10, 25, 50, 100, 200, 400, 800]
for n in ns:
    rf = RandomForestClassifier(
        n_estimators=n, oob_score=True, warm_start=False,
        random_state=0, n_jobs=-1,
    )
    rf.fit(X, y)
    oob_errors.append(1 - rf.oob_score_)
    print(f"n={n:>4}  OOB error = {1 - rf.oob_score_:.4f}")

plt.plot(ns, oob_errors, marker='o')
plt.xlabel("n_estimators"); plt.ylabel("OOB error")
plt.title("OOB error vs number of trees")
plt.grid(alpha=0.3); plt.show()
```

---

## Ex4: Default importance vs permutation importance

```python
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.inspection import permutation_importance
from sklearn.model_selection import train_test_split

X, y = load_breast_cancer(return_X_y=True)
feat_names = load_breast_cancer().feature_names
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, random_state=0)

rf = RandomForestClassifier(n_estimators=400, random_state=0, n_jobs=-1).fit(X_tr, y_tr)

# Method 1 — Gini / MDI (default, biased)
gini_imp = rf.feature_importances_
# Method 2 — Permutation (unbiased, slower)
perm = permutation_importance(rf, X_te, y_te, n_repeats=10, random_state=0, n_jobs=-1)
perm_imp = perm.importances_mean

for i in np.argsort(-perm_imp)[:10]:
    print(f"{feat_names[i]:<30s}  gini={gini_imp[i]:.4f}  perm={perm_imp[i]:.4f}")
```

Note how the ordering can differ — permutation is what you should trust for model explanation.

---

## Ex5: Grid search the important knobs

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)

grid = {
    "n_estimators":      [200, 500],
    "max_features":      ["sqrt", "log2", 0.3],
    "max_depth":         [None, 10, 20],
    "min_samples_leaf":  [1, 3, 5],
}

gs = GridSearchCV(
    RandomForestClassifier(random_state=0, n_jobs=-1),
    grid, cv=5, scoring="f1", n_jobs=-1, verbose=1,
)
gs.fit(X, y)
print("best params:", gs.best_params_)
print("best CV f1 :", gs.best_score_)
```

Priority of the knobs: `n_estimators` → `max_features` → `max_depth/min_samples_leaf`.

---

## Ex6: Checking OOB ≈ CV on the same problem

```python
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import cross_val_score

X, y = load_breast_cancer(return_X_y=True)

rf = RandomForestClassifier(
    n_estimators=400, oob_score=True, random_state=0, n_jobs=-1
).fit(X, y)

cv_acc = cross_val_score(
    RandomForestClassifier(n_estimators=400, random_state=0, n_jobs=-1),
    X, y, cv=5, scoring="accuracy",
)
print(f"OOB   acc:  {rf.oob_score_:.4f}")
print(f"5-CV  acc:  {cv_acc.mean():.4f} ± {cv_acc.std():.4f}")
```

On a moderate dataset, OOB and 5-fold CV usually agree within the noise — OOB is "free".

---

## Ex7: Extra Trees (no bootstrap, fully random splits)

```python
from sklearn.ensemble import ExtraTreesClassifier, RandomForestClassifier
from sklearn.datasets import load_wine
from sklearn.model_selection import cross_val_score

X, y = load_wine(return_X_y=True)
rf = RandomForestClassifier(n_estimators=300, random_state=0, n_jobs=-1)
et = ExtraTreesClassifier(n_estimators=300, random_state=0, n_jobs=-1)

print("RF :", cross_val_score(rf, X, y, cv=5).mean().round(4))
print("ET :", cross_val_score(et, X, y, cv=5).mean().round(4))
```

Extra Trees = even more randomness → faster, sometimes slightly better on noisy data.

---

## Ex8: Visualising tree disagreement as uncertainty (regression)

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

rng = np.random.default_rng(0)
X = np.linspace(0, 10, 200).reshape(-1, 1)
y = np.sin(X.ravel()) + 0.3*rng.standard_normal(200)

rf = RandomForestRegressor(n_estimators=200, random_state=0, n_jobs=-1).fit(X, y)

# Per-tree predictions → mean and std across trees
per_tree = np.stack([t.predict(X) for t in rf.estimators_])
mean_pred = per_tree.mean(axis=0)
std_pred  = per_tree.std(axis=0)

plt.scatter(X, y, s=8, alpha=0.4, label="data")
plt.plot(X, mean_pred, label="RF mean")
plt.fill_between(X.ravel(), mean_pred - std_pred, mean_pred + std_pred,
                 alpha=0.2, label="±1σ across trees")
plt.legend(); plt.title("RF regression with tree-disagreement uncertainty")
plt.show()
```

The spread of per-tree predictions gives a free, cheap uncertainty band.

---

> **See also:** [📖 THEORY](ml_random_forest_theory.md) · [🔢 NUMERICAL](ml_random_forest_numerical.md) · [Ch07 Ensemble](../Ch07_Ensemble_Learning/ml_ch7_theory.md)
>
> *ML · Random Forest · github.com/rpaut03l/TS-01*
