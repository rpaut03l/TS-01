# 💻 SVM & Kernels: PRACTICE

> **Nav:** [📖 THEORY](ml_svm_kernels_theory.md) | [🔢 NUMERICAL](ml_svm_kernels_numerical.md) | 💻 **PRACTICE**

---

## Ex1: SVM with Different Kernels

```python
import numpy as np, matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.datasets import make_moons
from sklearn.model_selection import cross_val_score

X, y = make_moons(n_samples=300, noise=0.2, random_state=42)

for kernel in ['linear', 'poly', 'rbf']:
    svm = SVC(kernel=kernel, degree=3, gamma='scale', C=1.0)
    scores = cross_val_score(svm, X, y, cv=5)
    print(f"{kernel:8s} → {scores.mean():.3f} ± {scores.std():.3f}")
# RBF usually wins on non-linear data like moons!
```

## Ex2: C-γ Grid Search

```python
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.datasets import make_moons

X, y = make_moons(n_samples=300, noise=0.2, random_state=42)

param_grid = {'C': [0.1, 1, 10, 100], 'gamma': [0.01, 0.1, 1, 10]}
grid = GridSearchCV(SVC(kernel='rbf'), param_grid, cv=5, scoring='accuracy')
grid.fit(X, y)

print(f"Best params: {grid.best_params_}")
print(f"Best CV accuracy: {grid.best_score_:.3f}")
# Shows the C-γ tradeoff in action!
```

## Ex3: Support Vectors Visualization

```python
import numpy as np, matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.datasets import make_moons

X, y = make_moons(n_samples=100, noise=0.15, random_state=42)
svm = SVC(kernel='rbf', C=10, gamma=2).fit(X, y)

print(f"Total points: {len(X)}")
print(f"Support vectors: {len(svm.support_vectors_)} "
      f"({100*len(svm.support_vectors_)/len(X):.0f}%)")

# Plot decision boundary + support vectors
xx, yy = np.meshgrid(np.linspace(-2, 3, 200), np.linspace(-1.5, 2, 200))
Z = svm.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
plt.contourf(xx, yy, Z, alpha=0.3, cmap='RdYlBu')
plt.scatter(X[:,0], X[:,1], c=y, cmap='RdYlBu', edgecolors='k', s=30)
plt.scatter(svm.support_vectors_[:,0], svm.support_vectors_[:,1],
            s=100, facecolors='none', edgecolors='green', linewidths=2,
            label='Support Vectors')
plt.legend(); plt.title("SVM: Only support vectors define the boundary"); plt.show()
```

## Ex4: Kernel PCA

```python
from sklearn.decomposition import KernelPCA, PCA
from sklearn.datasets import make_circles
import matplotlib.pyplot as plt

X, y = make_circles(n_samples=200, factor=0.3, noise=0.1, random_state=42)

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
axes[0].scatter(X[:,0], X[:,1], c=y, cmap='RdYlBu', s=20)
axes[0].set_title("Original 2D (not linearly separable)")

pca = PCA(n_components=1).fit_transform(X)
axes[1].scatter(pca, np.zeros_like(pca), c=y, cmap='RdYlBu', s=20)
axes[1].set_title("Linear PCA → 1D (still mixed!)")

kpca = KernelPCA(n_components=1, kernel='rbf', gamma=5).fit_transform(X)
axes[2].scatter(kpca, np.zeros_like(kpca), c=y, cmap='RdYlBu', s=20)
axes[2].set_title("Kernel PCA → 1D (separated!)")
plt.tight_layout(); plt.show()
```

---

> **Nav:** [📖 THEORY](ml_svm_kernels_theory.md) | [🔢 NUMERICAL](ml_svm_kernels_numerical.md) | 💻 PRACTICE

[↑ Back to Top](#-svm--kernels-practice)

*AI · ML · github.com/rpaut03l/TS-01*
