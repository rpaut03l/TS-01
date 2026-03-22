# 💻 Clustering: PRACTICE

> **Nav:** [📖 THEORY](ml_kmeans_gmm_em_theory.md) | [🔢 NUMERICAL](ml_kmeans_gmm_em_numerical.md) | 💻 **PRACTICE**

---

## Ex1: K-Means + Elbow Method

```python
import numpy as np, matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

X, _ = make_blobs(n_samples=300, centers=3, cluster_std=1.0, random_state=42)

# Elbow method
inertias = []
for k in range(1, 8):
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X)
    inertias.append(km.inertia_)

plt.figure(figsize=(8,4))
plt.plot(range(1,8), inertias, 'bo-', linewidth=2)
plt.xlabel("K"); plt.ylabel("Inertia (J)")
plt.title("Elbow Method → pick K where curve bends")
plt.grid(True, alpha=0.3); plt.show()
# Elbow at K=3 ✅
```

## Ex2: GMM vs K-Means

```python
from sklearn.mixture import GaussianMixture
from sklearn.cluster import KMeans

X, _ = make_blobs(n_samples=300, centers=[[0,0],[4,4],[8,0]],
                   cluster_std=[1.2, 1.5, 0.8], random_state=42)

km = KMeans(n_clusters=3, random_state=42, n_init=10).fit(X)
gmm = GaussianMixture(n_components=3, random_state=42).fit(X)
probs = gmm.predict_proba(X)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))
axes[0].scatter(X[:,0], X[:,1], c=km.labels_, cmap='viridis', s=20, alpha=0.7)
axes[0].set_title("K-Means (hard)")
axes[1].scatter(X[:,0], X[:,1], c=gmm.predict(X), cmap='viridis',
                s=20, alpha=probs.max(axis=1))
axes[1].set_title("GMM (soft — faded = uncertain)")
plt.show()

# Show soft probabilities
print("First 5 points — GMM probabilities:")
for i in range(5):
    p = probs[i]
    print(f"  x[{i}]: C0={p[0]:.3f} C1={p[1]:.3f} C2={p[2]:.3f}")
```

## Ex3: EM Convergence — Log-Likelihood

```python
from sklearn.mixture import GaussianMixture
import numpy as np, matplotlib.pyplot as plt

X, _ = make_blobs(n_samples=200, centers=3, random_state=42)

lls = []
for n_iter in range(1, 30):
    gmm = GaussianMixture(n_components=3, max_iter=n_iter, random_state=42)
    gmm.fit(X)
    lls.append(gmm.score(X) * len(X))  # total log-likelihood

plt.plot(range(1,30), lls, 'g.-', linewidth=2)
plt.xlabel("EM Iterations"); plt.ylabel("Log-Likelihood")
plt.title("EM: Log-Likelihood ALWAYS increases (never decreases)")
plt.grid(True, alpha=0.3); plt.show()
```

---

> **Nav:** [📖 THEORY](ml_kmeans_gmm_em_theory.md) | [🔢 NUMERICAL](ml_kmeans_gmm_em_numerical.md) | 💻 PRACTICE

[↑ Back to Top](#-clustering-practice)

*AI · ML · github.com/rpaut03l/TS-01*
