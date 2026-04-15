# 💻 ML LDA: PRACTICE

### *Code it, test it.*

> **Nav:** [📖 THEORY](ml_lda_theory.md) | [🔢 NUMERICAL](ml_lda_numerical.md) | 💻 **PRACTICE** | [📘 Detailed Guide](lda_guide_1.md)

---

## Ex1: Two-class Fisher LDA from scratch (NumPy)

```python
import numpy as np

# Class 1 and class 2, 2D points
X1 = np.array([[4, 1], [2, 4], [2, 3], [3, 6], [4, 4]])
X2 = np.array([[9, 10], [6, 8], [9, 5], [8, 7], [10, 8]])

m1 = X1.mean(axis=0)
m2 = X2.mean(axis=0)

# Within-class scatter
S1 = (X1 - m1).T @ (X1 - m1)
S2 = (X2 - m2).T @ (X2 - m2)
Sw = S1 + S2

# Fisher direction
w = np.linalg.inv(Sw) @ (m2 - m1)
w = w / np.linalg.norm(w)

# Project
p1 = X1 @ w
p2 = X2 @ w
print("w =", w.round(4))
print("class 1 projections:", p1.round(3))
print("class 2 projections:", p2.round(3))
print("class 1 mean:", p1.mean().round(3))
print("class 2 mean:", p2.mean().round(3))
```

This is Fisher LDA — pick the direction that maximises between-class spread / within-class spread.

---

## Ex2: sklearn LDA — classifier and dim-reducer

```python
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X, y = load_iris(return_X_y=True)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, stratify=y, random_state=0)

# As a classifier
lda = LinearDiscriminantAnalysis().fit(X_tr, y_tr)
print("Test accuracy:", accuracy_score(y_te, lda.predict(X_te)).round(4))

# As a dimensionality reducer (max K-1 = 2 dims for 3 classes)
X_tr_2d = lda.transform(X_tr)
print("Projected shape:", X_tr_2d.shape)
print("Explained variance ratio:", lda.explained_variance_ratio_.round(4))
```

LDA can reduce to at most **C − 1** dimensions where C = number of classes.

---

## Ex3: LDA vs PCA on Iris — visualisation

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

X, y = load_iris(return_X_y=True)
names = load_iris().target_names

X_pca = PCA(n_components=2).fit_transform(X)
X_lda = LinearDiscriminantAnalysis(n_components=2).fit_transform(X, y)

fig, ax = plt.subplots(1, 2, figsize=(10, 4))
for c, label in enumerate(names):
    ax[0].scatter(X_pca[y == c, 0], X_pca[y == c, 1], label=label, s=15)
    ax[1].scatter(X_lda[y == c, 0], X_lda[y == c, 1], label=label, s=15)
ax[0].set_title("PCA — unsupervised")
ax[1].set_title("LDA — supervised")
ax[0].legend(); ax[1].legend()
plt.tight_layout(); plt.show()
```

LDA typically gives **better class separation** than PCA because it uses labels.

---

## Ex4: Compare LDA, QDA, Logistic

```python
from sklearn.datasets import make_classification
from sklearn.discriminant_analysis import (
    LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis
)
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

X, y = make_classification(
    n_samples=500, n_features=20, n_informative=8,
    n_redundant=4, random_state=0,
)

models = {
    "LDA":      LinearDiscriminantAnalysis(),
    "QDA":      QuadraticDiscriminantAnalysis(),
    "Logistic": LogisticRegression(max_iter=2000),
}
for name, m in models.items():
    acc = cross_val_score(m, X, y, cv=5).mean()
    print(f"{name:<9}  CV acc = {acc:.4f}")
```

- **LDA** assumes shared covariance per class → fewer params, linear boundary.
- **QDA** relaxes that → quadratic boundary, more params.
- **Logistic** makes no Gaussian assumption at all.

---

## Ex5: Shrinkage — regularising LDA on small data

```python
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.datasets import make_classification
from sklearn.model_selection import cross_val_score

X, y = make_classification(n_samples=60, n_features=50, n_informative=10,
                           n_redundant=5, random_state=0)

for shrink in [None, 'auto', 0.1, 0.5, 0.9]:
    lda = LinearDiscriminantAnalysis(solver='lsqr', shrinkage=shrink)
    acc = cross_val_score(lda, X, y, cv=5).mean()
    print(f"shrinkage={shrink!s:<6} CV acc = {acc:.4f}")
```

When n < p (more features than samples), Sw is singular — shrinkage toward the identity fixes it.

---

## Ex6: Manual decision boundary in 2D

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.datasets import make_classification

X, y = make_classification(n_samples=300, n_features=2, n_informative=2,
                           n_redundant=0, n_clusters_per_class=1, random_state=1)

lda = LinearDiscriminantAnalysis().fit(X, y)

xx, yy = np.meshgrid(np.linspace(X[:,0].min()-1, X[:,0].max()+1, 300),
                     np.linspace(X[:,1].min()-1, X[:,1].max()+1, 300))
Z = lda.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

plt.contourf(xx, yy, Z, alpha=0.25)
plt.scatter(X[:,0], X[:,1], c=y, s=15, edgecolor='k')
plt.title("LDA decision boundary (linear)")
plt.show()
```

---

## Ex7: Pipeline with scaling + LDA dimensionality reduction

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_wine
from sklearn.model_selection import cross_val_score

X, y = load_wine(return_X_y=True)

pipe = Pipeline([
    ("scale", StandardScaler()),
    ("lda",   LinearDiscriminantAnalysis(n_components=2)),
    ("clf",   LogisticRegression(max_iter=2000)),
])

acc = cross_val_score(pipe, X, y, cv=5).mean()
print(f"StdScaler → LDA(2d) → Logistic  CV acc = {acc:.4f}")
```

Use LDA as a supervised dim-reducer in front of any classifier.

---

> **See also:** [📖 THEORY](ml_lda_theory.md) · [🔢 NUMERICAL](ml_lda_numerical.md) · [Feature Selection & DimRed](../Feature-Selection-DimRed/ml_pca_ica_fs_theory.md)
>
> *ML · LDA · github.com/rpaut03l/TS-01*
