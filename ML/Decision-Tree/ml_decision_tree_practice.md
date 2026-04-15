# 💻 ML Decision Tree: PRACTICE

### *Code it, test it.*

> **Nav:** [📘 Theory Guide](decision_tree_theory_slides_guide.md) | [📗 Guide w/ Math](decision_tree_guide_w_maths.md) | [🔢 NUMERICAL](ml_decision_tree_numerical.md) | 💻 **PRACTICE** | [← ML Master Index](../ml_master_gap_index.md)

---

## Ex1: Fit a tree — classification (Iris)

```python
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X, y = load_iris(return_X_y=True)
feat = load_iris().feature_names
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25,
                                          stratify=y, random_state=0)

tree = DecisionTreeClassifier(
    criterion="gini",   # or "entropy"
    max_depth=3,
    random_state=0,
).fit(X_tr, y_tr)

print("Test acc:", accuracy_score(y_te, tree.predict(X_te)).round(4))
print(export_text(tree, feature_names=feat))
```

`export_text` prints the entire tree in readable if/else form — excellent for debugging.

---

## Ex2: Visualise the tree

```python
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

X, y = load_iris(return_X_y=True)
tree = DecisionTreeClassifier(max_depth=3, random_state=0).fit(X, y)

fig, ax = plt.subplots(figsize=(12, 6))
plot_tree(tree, filled=True,
          feature_names=load_iris().feature_names,
          class_names=load_iris().target_names, ax=ax)
plt.tight_layout(); plt.show()
```

---

## Ex3: Regression tree on a smooth function (staircase effect)

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor

rng = np.random.default_rng(0)
X = np.sort(5 * rng.random((80, 1)), axis=0)
y = np.sin(X).ravel() + 0.15 * rng.standard_normal(80)

grid = np.linspace(0, 5, 500).reshape(-1, 1)
for depth in [2, 4, 8]:
    t = DecisionTreeRegressor(max_depth=depth).fit(X, y)
    plt.plot(grid, t.predict(grid), label=f"depth={depth}")
plt.scatter(X, y, c="k", s=8, alpha=0.5)
plt.legend(); plt.title("Regression tree — piecewise constant fit")
plt.show()
```

Regression trees output **piecewise-constant** functions — you'll see the staircase.

---

## Ex4: Gini vs Entropy — do they pick different trees?

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import cross_val_score

X, y = load_breast_cancer(return_X_y=True)

for crit in ("gini", "entropy"):
    clf = DecisionTreeClassifier(criterion=crit, random_state=0)
    acc = cross_val_score(clf, X, y, cv=5).mean()
    print(f"{crit:<8}  CV acc = {acc:.4f}")
```

On most datasets, Gini and Entropy give near-identical trees — Gini is just a touch faster.

---

## Ex5: Controlling overfitting — depth, min_samples_leaf, ccp_alpha

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X, y = load_breast_cancer(return_X_y=True)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, stratify=y, random_state=0)

for d in [None, 3, 5, 10]:
    t = DecisionTreeClassifier(max_depth=d, random_state=0).fit(X_tr, y_tr)
    print(f"max_depth={d!s:<5}  "
          f"train={accuracy_score(y_tr, t.predict(X_tr)):.3f}  "
          f"test={accuracy_score(y_te, t.predict(X_te)):.3f}  "
          f"leaves={t.get_n_leaves()}")
```

Watch the train/test gap shrink as depth decreases → classic overfit → regularize.

---

## Ex6: Cost-complexity pruning path

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X, y = load_breast_cancer(return_X_y=True)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, stratify=y, random_state=0)

path = DecisionTreeClassifier(random_state=0).cost_complexity_pruning_path(X_tr, y_tr)
alphas = path.ccp_alphas[:-1]   # drop the trivial one-leaf tree

train_acc, test_acc = [], []
for a in alphas:
    t = DecisionTreeClassifier(ccp_alpha=a, random_state=0).fit(X_tr, y_tr)
    train_acc.append(accuracy_score(y_tr, t.predict(X_tr)))
    test_acc.append(accuracy_score(y_te, t.predict(X_te)))

plt.plot(alphas, train_acc, label="train")
plt.plot(alphas, test_acc, label="test")
plt.xlabel("ccp_alpha"); plt.ylabel("accuracy"); plt.legend()
plt.title("Cost-complexity pruning path"); plt.show()
```

Pick the alpha with the best test accuracy — smaller tree, same or better generalization.

---

## Ex7: Feature importance (MDI / Gini)

```python
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)
names = load_breast_cancer().feature_names

tree = DecisionTreeClassifier(max_depth=5, random_state=0).fit(X, y)
imp = tree.feature_importances_

order = np.argsort(-imp)[:10]
for i in order:
    print(f"{names[i]:<30s} {imp[i]:.4f}")
```

Top features are those that caused the biggest impurity drops when used as splits.

---

## Ex8: Extract if/else rules from a fitted tree

```python
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
t = DecisionTreeClassifier(max_depth=3, random_state=0).fit(X, y)

rules = export_text(t, feature_names=load_iris().feature_names)
print(rules)
```

Copy this output, paste into a doc, and you have a human-readable classifier spec.

---

> **See also:** [📘 Theory Guide](decision_tree_theory_slides_guide.md) · [📗 Guide w/ Math](decision_tree_guide_w_maths.md) · [🔢 NUMERICAL](ml_decision_tree_numerical.md) · [Ch07 Ensemble](../Ch07_Ensemble_Learning/ml_ch7_theory.md) · [Random Forest](../Random-Forest/ml_random_forest_theory.md)
>
> *ML · Decision Tree · github.com/rpaut03l/TS-01*
