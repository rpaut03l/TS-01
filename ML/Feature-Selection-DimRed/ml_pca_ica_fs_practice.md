# 💻 Feature Selection & Dim Reduction: PRACTICE

> **Nav:** [📖 THEORY](ml_pca_ica_fs_theory.md) | [🔢 NUMERICAL](ml_pca_ica_fs_numerical.md) | 💻 **PRACTICE**

---

## Ex1: PCA on Iris (4D → 2D)

```python
import numpy as np, matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

iris = load_iris()
X = StandardScaler().fit_transform(iris.data)  # ALWAYS standardize first!

pca = PCA(n_components=4)  # fit all 4 to see variance explained
X_pca = pca.fit_transform(X)

print("Eigenvalues (variance per PC):", pca.explained_variance_.round(3))
print("Variance % per PC:", (pca.explained_variance_ratio_ * 100).round(1))
print("Cumulative %:", np.cumsum(pca.explained_variance_ratio_ * 100).round(1))
# PC1+PC2 ≈ 95% → 2 PCs is enough!

plt.figure(figsize=(8,5))
for i, name in enumerate(iris.target_names):
    mask = iris.target == i
    plt.scatter(X_pca[mask,0], X_pca[mask,1], label=name, alpha=0.7)
plt.xlabel(f"PC1 ({pca.explained_variance_ratio_[0]*100:.1f}%)")
plt.ylabel(f"PC2 ({pca.explained_variance_ratio_[1]*100:.1f}%)")
plt.title("PCA: Iris 4D → 2D"); plt.legend(); plt.grid(True, alpha=0.3); plt.show()
```

## Ex2: ICA (Blind Source Separation)

```python
import numpy as np, matplotlib.pyplot as plt
from sklearn.decomposition import FastICA

np.random.seed(42)
t = np.linspace(0, 1, 500)
s1 = np.sin(2*np.pi*5*t)          # sine wave
s2 = np.sign(np.sin(2*np.pi*3*t)) # square wave
S = np.c_[s1, s2]                  # 2 sources

A = np.array([[1, 0.5], [0.5, 1]])  # mixing matrix
X = S @ A.T                          # mixed signals

ica = FastICA(n_components=2, random_state=42)
S_recovered = ica.fit_transform(X)

fig, axes = plt.subplots(3, 1, figsize=(10, 6))
axes[0].plot(S); axes[0].set_title("Original Sources")
axes[1].plot(X); axes[1].set_title("Mixed Signals (observed)")
axes[2].plot(S_recovered); axes[2].set_title("ICA Recovered Sources")
plt.tight_layout(); plt.show()
# Recovered signals match originals (possibly flipped/scaled)!
```

## Ex3: Sequential Feature Selection (SFFS)

```python
from sklearn.feature_selection import SequentialFeatureSelector
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris

iris = load_iris()
knn = KNeighborsClassifier(n_neighbors=3)

# SFFS (forward with floating = not in sklearn, but forward is available)
sfs = SequentialFeatureSelector(knn, n_features_to_select=2, direction='forward', cv=5)
sfs.fit(iris.data, iris.target)
print(f"Selected features: {sfs.get_support()}")
print(f"Feature indices: {list(np.where(sfs.get_support())[0])}")
print(f"Feature names: {[iris.feature_names[i] for i in np.where(sfs.get_support())[0]]}")

# Backward
sbs = SequentialFeatureSelector(knn, n_features_to_select=2, direction='backward', cv=5)
sbs.fit(iris.data, iris.target)
print(f"\nBackward selected: {[iris.feature_names[i] for i in np.where(sbs.get_support())[0]]}")
```

---

> **Nav:** [📖 THEORY](ml_pca_ica_fs_theory.md) | [🔢 NUMERICAL](ml_pca_ica_fs_numerical.md) | 💻 PRACTICE

[↑ Back to Top](#-feature-selection--dim-reduction-practice)

*AI · ML · github.com/rpaut03l/TS-01*
