# 💻 Ch9 — Unsupervised Learning: PRACTICE
### *All book exercises solved. Mind-friendly steps. Colab code.*

> **Nav:** [← INDEX](./ml_ch9_index.md) | [📖 THEORY](./ml_ch9_theory.md) | [🔢 NUMERICAL](./ml_ch9_numerical.md) | 💻 **PRACTICE**

---

## 📋 Exercise Map

| # | Question | Topic | Level |
|---|----------|-------|-------|
| Q1 | Define clustering + name algorithms | Concept | 🟢 |
| Q2 | Main applications | Concept | 🟢 |
| Q3 | Two techniques to select K | K-Means | 🟡 |
| Q4 | Label propagation — what & how | Semi-supervised | 🟡 |
| Q5 | Algorithms that scale to large data | Scalability | 🟡 |
| Q6 | Active learning use case | Active Learning | 🟡 |
| Q7 | Anomaly vs Novelty detection | GMM | 🟡 |
| Q8 | GMM — what it is, what tasks | GMM | 🟡 |
| Q9 | Two GMM anomaly techniques | GMM | 🟡 |
| Q10 | Olivetti: K-Means + dim reduction | Coding | 🔴 |
| Q11 | Olivetti: semi-supervised learning | Coding | 🔴 |
| Q12 | Olivetti: GMM + anomaly detection | Coding | 🔴 |
| Q13 | Olivetti: PCA + reconstruction error | Coding | 🔴 |

---

## 🟢 Q1 — What is Clustering? Name Algorithms.

```
DEFINITION: Group similar data points WITHOUT labels.
            Algorithm finds structure on its own.

ALGORITHMS:
  K-Means        → spherical clusters, fast, large data
  DBSCAN         → any shape, handles outliers (label=−1)
  Agglomerative  → hierarchical tree, good for small data
  GMM            → soft (probabilistic) assignment, oval clusters
  Mean Shift     → no K needed, finds dense regions
```

---

## 🟢 Q2 — Main Applications

```
Customer segmentation  → personalise marketing
Data analysis          → explore before modelling
Dim reduction          → km.transform(X) = distances to centroids
Anomaly detection      → lonely points = suspicious
Semi-supervised        → label few → propagate to cluster
Image segmentation     → group same-colour pixels
Recommendation         → "users like you also liked..."
```

---

## 🟡 Q3 — Two Techniques to Select K

👶 Too many cuts → tiny slices. Too few → giant slices. Elbow says when cutting more doesn't help. Silhouette says if each slice has the right people!

```python
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

# TECHNIQUE 1: Elbow (inertia)
inertias = []
for k in range(1, 11):
    km = KMeans(n_clusters=k, n_init=10, random_state=42).fit(X)
    inertias.append(km.inertia_)
plt.plot(range(1,11), inertias, 'bo-')
plt.xlabel('K'); plt.ylabel('Inertia'); plt.title('Elbow Method')
# Look for the bend/elbow in the curve

# TECHNIQUE 2: Silhouette score (better!)
sil_scores = []
for k in range(2, 11):  # needs k>=2
    labels = KMeans(n_clusters=k, n_init=10, random_state=42).fit_predict(X)
    sil_scores.append(silhouette_score(X, labels))
best_k = range(2,11)[sil_scores.index(max(sil_scores))]
print(f"Best K = {best_k}")  # highest silhouette = best K
```

```
ELBOW:      fast, visual, subjective
SILHOUETTE: reliable, mathematical, use this!
Best practice: use BOTH and check they agree ✅
```

---

## 🟡 Q4 — Label Propagation

👶 1000 students, only label 10 (one per class). Cluster all 1000. Give a cluster representative its label. Everyone in that cluster gets the same label. Done!

> ⚠️ **Run this full cell in Colab — it is self-contained. Don't skip any line.**

```python
# ── CELL: fully self-contained, paste & run directly in Colab ────

import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

# ── 1. Load data ──────────────────────────────────────────────────
X, y = load_digits(return_X_y=True)          # 1797 images, 64 features each
                                              # 10 classes (digits 0-9)

# ── 2. Split into train / val ────────────────────────────────────
X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
# X_train: (1437, 64)    X_val: (360, 64)

# ── 3. Scale features ────────────────────────────────────────────
scaler  = StandardScaler()
X_train = scaler.fit_transform(X_train)      # fit on train only!
X_val   = scaler.transform(X_val)

print(f"Train: {X_train.shape}   Val: {X_val.shape}")

# ── 4. K-Means clustering ────────────────────────────────────────
k  = 50
km = KMeans(n_clusters=k, n_init=10, random_state=42)
km.fit(X_train)

# ── 5. Find one representative per cluster ────────────────────────
# distances shape → (n_train, k) — distance from each point to each centroid
distances = km.transform(X_train)
repr_idx  = np.argmin(distances, axis=0)     # one closest index per cluster
y_repr    = y_train[repr_idx]                # true label of each representative

print(f"Labelled only {k} points (one per cluster) out of {len(X_train)}")

# ── 6. Propagate labels to all cluster members ───────────────────
y_prop = np.empty(len(X_train), dtype=int)
for i in range(k):
    y_prop[km.labels_ == i] = y_repr[i]     # all in cluster i get rep's label

# ── 7. Train classifier on propagated labels ──────────────────────
clf = LogisticRegression(max_iter=1000, random_state=42)
clf.fit(X_train, y_prop)

# ── 8. Evaluate ───────────────────────────────────────────────────
semi_acc  = clf.score(X_val, y_val)
print(f"Semi-supervised accuracy: {semi_acc:.4f}")

# Compare: fully supervised (uses ALL true labels)
clf_full = LogisticRegression(max_iter=1000, random_state=42)
clf_full.fit(X_train, y_train)
full_acc = clf_full.score(X_val, y_val)
print(f"Fully supervised accuracy: {full_acc:.4f}")
print(f"Gap: {full_acc - semi_acc:.4f}  (we labelled only {k}/{len(X_train)} points!)")
```


---

## 🟡 Q5 — Algorithms that Scale to Large Datasets?

```
SCALES WELL:
  ✅ K-Means (MiniBatchKMeans for huge data)
  ✅ DBSCAN (with spatial index, O(n log n))
  ✅ BIRCH  (O(n), designed for huge datasets)

DOES NOT SCALE:
  ❌ Agglomerative (O(n² log n) memory)
  ❌ Spectral (O(n³) eigendecomposition)

Two algorithms that scale AND handle density regions:
  → K-Means:  spherical high-density regions
  → DBSCAN:   arbitrary-shape high-density regions ✅
```

---

## 🟡 Q6 — Active Learning Use Case

👶 You can label only 100 of 10,000 images. Instead of random 100, cluster into 100 groups and pick one representative from each. You cover all types with minimum effort!

```python
km = KMeans(n_clusters=100).fit(X)
repr_idx = np.argmin(km.transform(X), axis=0)   # 100 representatives
# → Ask human to label only X[repr_idx] (100 images)
# → Propagate labels to full clusters
# → Train on propagated labels

BENEFIT: Labels spread across full data distribution.
         No wasted effort labelling 100 similar images.
```

---

## 🟡 Q7 — Anomaly vs Novelty Detection

```
ANOMALY DETECTION:
  Training data CONTAINS outliers.
  Detect weird points even in training.
  Ex: credit card fraud (some fraud in training data)
  → IsolationForest, LocalOutlierFactor, GMM

NOVELTY DETECTION:
  Training data is CLEAN.
  Model learns "what normal looks like."
  Detect NEW unusual test points.
  Ex: machine trained on normal vibrations → detect fault in production
  → OneClassSVM, GMM with threshold

KEY DIFFERENCE: Anomaly = outliers IN training. Novelty = normal training, weird test.
```

---

## 🟡 Q8 — What is a Gaussian Mixture? What Tasks?

```
👶 3 people each bake cookies with different sizes.
   GMM figures out which baker probably made each cookie.
   Gives probabilities: "70% Baker1, 30% Baker2."

GAUSSIAN MIXTURE MODEL:
  Data comes from K overlapping Gaussians.
  Learns: μₖ (centre), Σₖ (shape), φₖ (how common each is).
  Gives SOFT assignments (probabilities not hard labels).

TASKS:
  1. Clustering     → predict(X) or predict_proba(X)
  2. Density        → score_samples(X) → log probability
  3. Anomaly        → low score = unusual
  4. Generation     → gm.sample(100) → synthetic data 🎲
```

---

## 🟡 Q9 — Two GMM Anomaly Detection Techniques

```
TECHNIQUE 1: LOG-PROBABILITY THRESHOLD
  scores = gm.score_samples(X_train)         # log-prob per point
  threshold = np.percentile(scores, 4)        # bottom 4% = anomalies
  anomalies = X[scores < threshold]

TECHNIQUE 2: RECONSTRUCTION ERROR (with PCA)
  pca = PCA(n_components=0.99).fit(X_train)
  X_compressed  = pca.transform(X)
  X_reconstructed = pca.inverse_transform(X_compressed)
  error = np.mean((X - X_reconstructed)**2, axis=1)  # per point
  threshold = np.percentile(error, 96)   # top 4% errors = anomalies
  anomalies = X[error > threshold]

WHEN TO USE:
  Score threshold → fast, works with GMM directly
  Reconstruction error → useful for images/high-dim data
```

---

## 🔴 Q10 — Olivetti Faces: K-Means + Dim Reduction

```python
import numpy as np
from sklearn.datasets import fetch_olivetti_faces
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.metrics import silhouette_score

# ── 1. Load ──────────────────────────────────────────────────────
faces = fetch_olivetti_faces(random_state=42)
X, y  = faces.data, faces.target   # (400, 4096), 40 people × 10 photos

# ── 2. Stratified split (keep all 40 people in each set) ─────────
sss = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
train_idx, test_idx = next(sss.split(X, y))
X_tr, X_test = X[train_idx], X[test_idx]
y_tr, y_test = y[train_idx], y[test_idx]

sss2 = StratifiedShuffleSplit(n_splits=1, test_size=0.1, random_state=42)
tr_idx, val_idx = next(sss2.split(X_tr, y_tr))
X_train, X_val = X_tr[tr_idx], X_tr[val_idx]
y_train, y_val = y_tr[tr_idx], y_tr[val_idx]

# ── 3. Baseline (raw 4096 features) ─────────────────────────────
clf_base = RandomForestClassifier(n_estimators=150, random_state=42)
clf_base.fit(X_train, y_train)
print("Baseline val acc:", clf_base.score(X_val, y_val))

# ── 4. Find best K via silhouette ────────────────────────────────
best_k, best_sil = 40, -1
for k in [40, 80, 120, 160]:
    labels = KMeans(n_clusters=k, n_init=5, random_state=42).fit_predict(X_train)
    s = silhouette_score(X_train, labels, sample_size=300, random_state=42)
    print(f"K={k}: silhouette={s:.3f}")
    if s > best_sil: best_k, best_sil = k, s
print(f"Best K = {best_k}")

# ── 5. Dim reduction: 4096 → K distances ────────────────────────
km = KMeans(n_clusters=best_k, n_init=10, random_state=42).fit(X_train)
X_train_r = km.transform(X_train)   # (n, K)
X_val_r   = km.transform(X_val)
X_test_r  = km.transform(X_test)

# ── 6. Classifier on reduced features ───────────────────────────
clf_r = RandomForestClassifier(n_estimators=150, random_state=42)
clf_r.fit(X_train_r, y_train)
print("Reduced val acc:", clf_r.score(X_val_r, y_val))
```

---

## 🔴 Q11 — Olivetti: Semi-Supervised Label Propagation

> ⚠️ **Self-contained cell — run Q10 first OR paste the setup block below before this.**

```python
# ── SETUP (paste this if running Q11 standalone) ─────────────────
import numpy as np
from sklearn.datasets import fetch_olivetti_faces
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier

faces = fetch_olivetti_faces(random_state=42)
X, y  = faces.data, faces.target

sss = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
train_idx, test_idx = next(sss.split(X, y))
X_tr, X_test = X[train_idx], X[test_idx]
y_tr, y_test = y[train_idx], y[test_idx]

sss2 = StratifiedShuffleSplit(n_splits=1, test_size=0.1, random_state=42)
tr_idx, val_idx = next(sss2.split(X_tr, y_tr))
X_train, X_val = X_tr[tr_idx], X_tr[val_idx]
y_train, y_val = y_tr[tr_idx], y_tr[val_idx]

best_k = 40   # use 40 (one per person) if not running K search from Q10
km = KMeans(n_clusters=best_k, n_init=10, random_state=42).fit(X_train)
# ─────────────────────────────────────────────────────────────────

# ── Find one representative per cluster ──────────────────────────
distances = km.transform(X_train)              # (n_train, best_k)
repr_idx  = np.argmin(distances, axis=0)       # best_k representatives
y_repr    = y_train[repr_idx]                  # their true labels

print(f"Labelled only {best_k} images out of {len(X_train)}")

# ── Propagate labels to all cluster members ───────────────────────
y_prop = np.empty(len(X_train), dtype=int)
for i in range(best_k):
    y_prop[km.labels_ == i] = y_repr[i]

# ── Train on propagated labels ────────────────────────────────────
clf_semi = RandomForestClassifier(n_estimators=150, random_state=42)
clf_semi.fit(X_train, y_prop)
print(f"Semi-supervised val acc:  {clf_semi.score(X_val, y_val):.4f}")

# Compare with fully supervised
clf_full = RandomForestClassifier(n_estimators=150, random_state=42)
clf_full.fit(X_train, y_train)
print(f"Fully supervised val acc: {clf_full.score(X_val, y_val):.4f}")

# ── BONUS: High-confidence only (nearest to centroid) ────────────
confident_mask = np.zeros(len(X_train), dtype=bool)
for i in range(best_k):
    mask = km.labels_ == i
    thr  = np.percentile(distances[mask, i], 20)   # closest 20%
    confident_mask |= (mask & (distances[:, i] <= thr))

clf_conf = RandomForestClassifier(n_estimators=150, random_state=42)
clf_conf.fit(X_train[confident_mask], y_prop[confident_mask])
print(f"High-confidence semi-sup: {clf_conf.score(X_val, y_val):.4f}")
```

---

## 🔴 Q12 — Olivetti: GMM + Anomaly Detection

> ⚠️ **Self-contained cell — includes setup. Paste and run directly.**

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_olivetti_faces
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.mixture import GaussianMixture

# ── Setup ─────────────────────────────────────────────────────────
faces = fetch_olivetti_faces(random_state=42)
X, y  = faces.data, faces.target

sss = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
train_idx, test_idx = next(sss.split(X, y))
X_tr, X_test = X[train_idx], X[test_idx]
y_tr, y_test = y[train_idx], y[test_idx]

sss2 = StratifiedShuffleSplit(n_splits=1, test_size=0.1, random_state=42)
tr_idx, val_idx = next(sss2.split(X_tr, y_tr))
X_train, X_val = X_tr[tr_idx], X_tr[val_idx]
y_train, y_val = y_tr[tr_idx], y_tr[val_idx]

# ── 1. Find best K using BIC ─────────────────────────────────────
# NOTE: GMM on 4096 features is very slow!
# Use PCA to compress first (good practice anyway)
from sklearn.decomposition import PCA
pca = PCA(n_components=0.99, random_state=42)
X_train_pca = pca.fit_transform(X_train)
print(f"PCA: 4096 → {X_train_pca.shape[1]} components")

bics = []
for k in range(1, 16):
    gm = GaussianMixture(n_components=k, covariance_type='full',
                         n_init=3, random_state=42).fit(X_train_pca)
    bics.append(gm.bic(X_train_pca))
    print(f"  K={k:2d}: BIC={bics[-1]:.1f}")

best_k_gm = np.argmin(bics) + 1
print(f"\nBest K for GMM = {best_k_gm}")

# ── 2. Fit best GMM ──────────────────────────────────────────────
gm_best = GaussianMixture(n_components=best_k_gm, covariance_type='full',
                           n_init=10, random_state=42).fit(X_train_pca)

# ── 3. Anomaly detection ─────────────────────────────────────────
train_scores = gm_best.score_samples(X_train_pca)
threshold    = np.percentile(train_scores, 4)     # bottom 4% = anomalies
anomaly_mask = train_scores < threshold
print(f"Anomalies in training set: {anomaly_mask.sum()} points")

# ── 4. Generate synthetic faces 🎲 ───────────────────────────────
X_syn_pca, _ = gm_best.sample(10)                # sample in PCA space
X_synthetic   = pca.inverse_transform(X_syn_pca) # back to pixel space

fig, axes = plt.subplots(2, 5, figsize=(10, 4))
for i, ax in enumerate(axes.flat):
    ax.imshow(X_synthetic[i].reshape(64, 64), cmap='gray')
    ax.axis('off')
plt.suptitle("GMM-Generated Synthetic Faces")
plt.tight_layout()
plt.savefig("gmm_faces.png", dpi=100)
plt.show()
print("Saved gmm_faces.png")
```

---

## 🔴 Q13 — Olivetti: PCA + Reconstruction Error Anomaly

> ⚠️ **Self-contained cell. Paste and run directly in Colab.**

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_olivetti_faces
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.decomposition import PCA
from scipy.ndimage import rotate

# ── Setup ─────────────────────────────────────────────────────────
faces = fetch_olivetti_faces(random_state=42)
X, y  = faces.data, faces.target

sss = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
train_idx, test_idx = next(sss.split(X, y))
X_tr, X_test = X[train_idx], X[test_idx]
y_tr, y_test = y[train_idx], y[test_idx]

sss2 = StratifiedShuffleSplit(n_splits=1, test_size=0.1, random_state=42)
tr_idx, val_idx = next(sss2.split(X_tr, y_tr))
X_train, X_val = X_tr[tr_idx], X_tr[val_idx]
y_train, y_val = y_tr[tr_idx], y_tr[val_idx]

# ── 1. PCA keeping 99% variance ──────────────────────────────────
pca = PCA(n_components=0.99, random_state=42)
X_train_pca = pca.fit_transform(X_train)
print(f"PCA: 4096 → {X_train_pca.shape[1]} components (99% variance kept)")

# ── 2. Reconstruction error on training set ──────────────────────
X_train_rec  = pca.inverse_transform(X_train_pca)
train_errors = np.mean((X_train - X_train_rec)**2, axis=1)
threshold    = np.percentile(train_errors, 96)    # top 4% errors = anomalies
print(f"Reconstruction error threshold (96th pct): {threshold:.6f}")

# ── 3. Test: normal face vs rotated (anomalous) face ────────────
def recon_error(x):
    """Reconstruction error for a single sample."""
    compressed    = pca.transform(x.reshape(1, -1))
    reconstructed = pca.inverse_transform(compressed)
    return np.mean((x - reconstructed) ** 2)

normal_face    = X_test[0]
rotated_face   = rotate(normal_face.reshape(64, 64), angle=90).flatten()
darkened_face  = np.clip(normal_face - 0.5, 0, 1)   # extra test

err_normal  = recon_error(normal_face)
err_rotated = recon_error(rotated_face)
err_dark    = recon_error(darkened_face)

print(f"\nNormal face error:   {err_normal:.6f}  → anomaly: {err_normal > threshold}")
print(f"Rotated face error:  {err_rotated:.6f}  → anomaly: {err_rotated > threshold}")
print(f"Darkened face error: {err_dark:.6f}  → anomaly: {err_dark > threshold}")

# ── 4. Visualise ─────────────────────────────────────────────────
fig, axes = plt.subplots(1, 3, figsize=(9, 3))
for ax, img, title, err in zip(
    axes,
    [normal_face, rotated_face, darkened_face],
    ["Normal", "Rotated 90°", "Darkened"],
    [err_normal, err_rotated, err_dark]
):
    ax.imshow(img.reshape(64, 64), cmap='gray')
    flag = "⚠️ ANOMALY" if err > threshold else "✅ Normal"
    ax.set_title(f"{title}\nerr={err:.4f}\n{flag}", fontsize=9)
    ax.axis('off')

plt.suptitle("Reconstruction Error Anomaly Detection", fontsize=11)
plt.tight_layout()
plt.savefig("anomaly_recon.png", dpi=100)
plt.show()
print("Saved anomaly_recon.png")
```

---

## ⚡ One-Liners

```python
KMeans(n_clusters=K, n_init=10).fit_predict(X)                  # cluster labels
km.transform(X)                                                   # dim reduction
silhouette_score(X, labels)                                       # clustering quality
gm.score_samples(X)                                               # log-prob (anomaly)
gm.sample(100)                                                    # generate data
np.percentile(scores, 4)                                          # anomaly threshold
PCA(n_components=0.99).fit_transform(X)                          # compress 99% var
np.argmin(km.transform(X), axis=0)                               # cluster reps
```

---

## 🧪 EXAM HACKS

```
💡 StratifiedShuffleSplit for Olivetti → ensures all 40 people in each split
💡 km.transform(X) → distances → dim reduction + label propagation
💡 gm.score_samples → low = anomaly. Use percentile(scores, 4) as threshold.
💡 gm.sample(n) → GMM is generative — can create synthetic data!
💡 BIC: pick K where BIC is MINIMUM (lower = better model)
💡 PCA reconstruction error: big error = image is weird = anomaly
💡 covariance_type='full' → most flexible, most params (use for Olivetti)
```

---

> **Nav:** [← INDEX](./ml_ch9_index.md) | [📖 THEORY](./ml_ch9_theory.md) | [🔢 NUMERICAL](./ml_ch9_numerical.md) | 💻 **PRACTICE**

* AI · ML · github.com/rpaut03l/TS-01*
