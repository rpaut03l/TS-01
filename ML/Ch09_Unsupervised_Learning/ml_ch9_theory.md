# 📖 Ch9 — Unsupervised Learning: THEORY
### *Hands-On ML Ch9 · K-Means · DBSCAN · GMM · Anomaly Detection*

> **Nav:** [← INDEX](./ml_ch9_index.md) | 📖 **THEORY** | [🔢 NUMERICAL →](./ml_ch9_numerical.md) | [💻 PRACTICE →](./ml_ch9_practice.md)

---

## 🧠 MNEMONIC: **"GLAD CAD"**
> **G**aussian Mixture · **L**abel Propagation · **A**nomaly · **D**ensity (DBSCAN) · **C**lustering · **A**lgorithm Select · **D**im Reduction

---

## 🗺️ Big Picture

```
UNSUPERVISED LEARNING  (no labels!)
      │
      ├─ CLUSTERING ──────────────────────────────────────────
      │       ├─ K-Means          spherical, fast, large data
      │       ├─ DBSCAN           any shape, handles outliers
      │       ├─ Agglomerative    hierarchy, small data
      │       └─ Label Propagation  semi-supervised trick
      │
      └─ DENSITY ESTIMATION ──────────────────────────────────
              └─ GMM (Gaussian Mixture Model)
                      ├─ Soft clustering
                      ├─ Anomaly detection
                      └─ Data generation 🎲
```

---

## 1️⃣ CLUSTERING — What & Why

👶 You have a bag of mixed Lego bricks. No labels. You group them by colour yourself. That's clustering — finding groups WITHOUT being told what groups exist.

```
MAIN USES:
  Customer segmentation   → group buyers by habits
  Image segmentation      → group pixels of same colour
  Anomaly detection       → lone points far from all groups
  Semi-supervised         → label few → propagate to cluster
  Dim reduction           → replace features with cluster distances
```

---

## 2️⃣ K-MEANS

👶 Put K magnets on the floor. Every brick jumps to its nearest magnet. Each magnet moves to the centre of its pile. Repeat until magnets stop moving!

```
ALGORITHM:
  1. Pick K random centroids μ₁...μₖ
  2. Assign each xᵢ → nearest centroid (min squared distance)
  3. Update each μₖ = mean of its assigned points
  4. Repeat 2-3 until centroids don't move

INERTIA = Σ d²(xᵢ, its centroid) — lower is better but always drops with K↑

SELECTING K:
  Elbow:      plot inertia vs K → find the "bend"  (fast, visual)
  Silhouette: plot score vs K → pick highest        (reliable, use this!)
```

```python
km = KMeans(n_clusters=5, n_init=10, random_state=42)
km.fit(X)
km.labels_           # cluster of each point
km.cluster_centers_  # centroid coordinates
km.inertia_          # J value
km.transform(X)      # distances to each centroid ← dim reduction!
```

```
PROS ✅  Fast, scales to millions, easy to understand
CONS ❌  Must pick K, fails on non-spherical, sensitive to outliers
```

---

## 3️⃣ LABEL PROPAGATION (Semi-Supervised)

👶 1000 students, you can only label 10. Cluster all 1000 first. Give a label to the one student closest to each cluster centre. Everyone in that cluster gets the same label!

```
STEPS:
  1. Cluster ALL data (labelled + unlabelled) with K-Means
  2. Find point closest to each centroid → "representative"
  3. Manually label each representative (only K labels needed!)
  4. Propagate: all points in cluster k → get k's label
  5. Train any classifier on propagated labels
```

```python
distances = km.transform(X_train)           # shape: (n, K)
repr_idx  = np.argmin(distances, axis=0)    # one per cluster
y_repr    = y_train[repr_idx]               # their labels

y_propagated = np.empty(len(X_train), dtype=int)
for i in range(k):
    y_propagated[km.labels_ == i] = y_repr[i]
```

---

## 4️⃣ DBSCAN

👶 You're at a party. You belong to a group if you can reach others through a chain of nearby people (no large gaps). Lone people in a corner = outliers!

```
KEY PARAMS:
  ε (eps)       = max distance to count as "neighbour"
  min_samples   = min neighbours to be a "core point"

POINT TYPES:
  CORE POINT   → has ≥ min_samples neighbours within ε
  BORDER POINT → is a neighbour of core, but not core itself
  OUTLIER      → neither → labelled −1 by sklearn ⚠️

PROS ✅  No need to pick K, any shape, outliers = −1
CONS ❌  Struggles with varying density, ε is sensitive
```

```python
from sklearn.cluster import DBSCAN
db = DBSCAN(eps=0.5, min_samples=5)
db.fit_predict(X)   # −1 = outlier
```

---

## 5️⃣ GAUSSIAN MIXTURE MODEL (GMM)

👶 3 people baked cookies — each with a different average size and spread. All cookies mixed in a jar. GMM figures out: "this cookie (8.5cm) is probably from Person 1 (avg=9cm)." Soft assignment — could be 80% Person1, 20% Person2.

```
MATH:
  p(x) = Σₖ φₖ · N(x | μₖ, Σₖ)
  
  φₖ  = mixing weight (how common is cluster k)
  μₖ  = centre of Gaussian k
  Σₖ  = shape/spread of Gaussian k
  N() = normal (bell curve) distribution

SOFT vs HARD:
  K-Means: "you're IN cluster 3" (hard)
  GMM:     "70% cluster 3, 30% cluster 1" (soft)

EM ALGORITHM trains GMM:
  E-step: compute r(i,k) = P(cluster=k | point i) for each point
  M-step: update φ, μ, Σ using weighted averages
  Repeat until log-likelihood converges
```

```python
from sklearn.mixture import GaussianMixture
gm = GaussianMixture(n_components=3, covariance_type='full')
gm.fit(X)
gm.predict(X)            # hard labels
gm.predict_proba(X)      # soft: (n, K) probabilities
gm.score_samples(X)      # log probability per point
gm.sample(100)           # generate 100 NEW synthetic points 🎲
gm.bic(X), gm.aic(X)    # model selection (lower = better)
```

---

## 6️⃣ ANOMALY vs NOVELTY DETECTION

```
ANOMALY DETECTION:
  Training data has outliers in it.
  Detect weird points IN the training set.
  Ex: find the black burnt cookie in the batch you just baked.
  → IsolationForest, LocalOutlierFactor, GMM

NOVELTY DETECTION:
  Training data is CLEAN (all normal).
  Detect weird NEW points at test time.
  Ex: trained on round cookies, now given a star-shaped one.
  → OneClassSVM, GMM with threshold

GMM anomaly detection:
  low score_samples(x) = low probability = unusual = anomaly
  threshold = np.percentile(train_scores, 4)  ← bottom 4% flagged
```

---

## 7️⃣ MODEL SELECTION: BIC & AIC

```
PROBLEM: How many Gaussians (K) for GMM? More K always fits better — but overfits!
SOLUTION: BIC/AIC penalise model complexity.

BIC = −2·ℓ + k·ln(n)    (use for large n, penalises more)
AIC = −2·ℓ + 2k          (use for small n)

ℓ = log-likelihood (higher=better fit)
k = number of free parameters
n = number of data points

LOWER BIC/AIC = better model. Pick K that minimises it.
```

```python
bics = [GaussianMixture(n_components=k).fit(X).bic(X) for k in range(1,11)]
best_k = np.argmin(bics) + 1
```

---

## 8️⃣ DIM REDUCTION VIA CLUSTERING

```
Instead of raw features → transform to cluster distances:
  X_reduced = km.transform(X)   # shape: (n_samples, K)
  Each column = distance to one centroid

This gives K new features capturing non-linear structure.
Then train a classifier on X_reduced — often better!
Speed up SVM/NNs on high-dimensional data this way.
```

---

## 🃏 CHEAT SHEET

```
┌──────────────┬──────────┬────────────┬──────┬──────────────────┐
│ Algorithm    │ Pick K?  │ Shape      │ Soft?│ Anomaly?         │
├──────────────┼──────────┼────────────┼──────┼──────────────────┤
│ K-Means      │ ✅ Yes   │ Spherical  │ ❌   │ Partial (inertia)│
│ DBSCAN       │ ❌ Auto  │ Any        │ ❌   │ ✅ (label=−1)    │
│ Agglomerative│ ✅ Yes   │ Any        │ ❌   │ ❌               │
│ GMM          │ ✅ Yes   │ Ellipse    │ ✅   │ ✅ (score_samples│
└──────────────┴──────────┴────────────┴──────┴──────────────────┘

KEY SKLEARN CALLS:
  km.transform(X)          → distances (dim reduction)
  gm.score_samples(X)      → log-prob (anomaly detection)
  gm.sample(n)             → generate synthetic data
  silhouette_score(X, labels) → clustering quality metric
```

---

## 🧪 EXAM HACKS

```
💡 "How to choose K?" → Elbow (inertia plot) + Silhouette score
💡 "GMM vs K-Means?" → GMM = soft + oval; K-Means = hard + spherical
💡 "Anomaly with GMM?" → score_samples() — low score = anomaly
💡 "Label propagation steps?" → Cluster → rep → label → propagate
💡 "DBSCAN outlier label?" → −1
💡 "GMM can generate data?" → YES: gm.sample(n)
💡 "E-step output?" → responsibilities r(i,k) (soft probabilities)
💡 "M-step output?" → updated μ, Σ, φ
💡 "BIC vs AIC?" → BIC penalises more for large n → use BIC in practice
💡 "Inertia always decreases with K?" → YES (not a good metric alone!)
```

---

> **Nav:** [← INDEX](./ml_ch9_index.md) | 📖 THEORY | [🔢 NUMERICAL →](./ml_ch9_numerical.md) | [💻 PRACTICE →](./ml_ch9_practice.md)

* AI · ML · github.com/rpaut03l/TS-01*
