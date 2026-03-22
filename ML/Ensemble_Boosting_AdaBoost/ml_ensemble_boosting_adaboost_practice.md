# 💻 Ensemble Boosting & AdaBoost Deep-Dive: PRACTICE

### *Code it, test it, break it, fix it. Every line explained like you're 5.*

> **Nav:** [← INDEX](ml_ensemble_boosting_adaboost_index.md) | [📖 THEORY](ml_ensemble_boosting_adaboost_theory.md) | [🔢 NUMERICAL](ml_ensemble_boosting_adaboost_numerical.md) | 💻 **PRACTICE**
>
> 🔗 **Related:** [Ch7 PRACTICE (Géron)](https://github.com/rpaut03l/TS-01/blob/main/ML/Ch07_Ensemble_Learning/ml_ch7_practice.md)
>
> 📓 **Jupyter Notebook:** [ensemble_boosting_adaboost_lab.ipynb](ensemble_boosting_adaboost_lab.ipynb) ← run this in Colab!

---

## 🗺️ Exercise Map

| # | Exercise | What You'll Learn | Colab Cell |
|---|----------|-------------------|------------|
| Ex1 | Bagging vs Single Tree | Why ensembles beat single models | Cell 1-3 |
| Ex2 | Bagging vs Boosting side-by-side | Visual comparison on same data | Cell 4-6 |
| Ex3 | AdaBoost from scratch (manual) | Full algorithm, step by step | Cell 7-10 |
| Ex4 | Decision Stump builder | Build a stump, compute error + α | Cell 11-13 |
| Ex5 | Weight update visualizer | Watch weights change each round | Cell 14-16 |
| Ex6 | Model selection experiment | Compare 5 models on traffic-like data | Cell 17-19 |
| Ex7 | GMM basics | Soft clustering vs K-Means | Cell 20-22 |

---

## Ex1: Bagging vs Single Tree

### What This Shows

A single decision tree overfits. Bagging 100 trees and averaging → smooth, stable predictions.

```python
# ============================================================
# Ex1: WHY BAGGING WORKS — Single Tree vs Bagging
# ============================================================
# Think of it like this:
# One student takes one exam → might get lucky or unlucky
# 100 students take the exam → average score is more reliable!

import numpy as np                    # math library
import matplotlib.pyplot as plt       # for drawing graphs
from sklearn.tree import DecisionTreeClassifier    # one tree
from sklearn.ensemble import BaggingClassifier     # many trees
from sklearn.datasets import make_moons            # toy dataset
from sklearn.model_selection import train_test_split

# --- STEP 1: Make some fake data (two half-moon shapes) ---
# n_samples=300: we want 300 data points
# noise=0.3: add some randomness so it's not perfect
# random_state=42: so you get the exact same data every time
X, y = make_moons(n_samples=300, noise=0.3, random_state=42)

# --- STEP 2: Split into training (80%) and test (20%) ---
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# --- STEP 3: Train a SINGLE deep tree (will overfit!) ---
single_tree = DecisionTreeClassifier(random_state=42)  # no depth limit!
single_tree.fit(X_train, y_train)
print(f"Single Tree - Train acc: {single_tree.score(X_train, y_train):.3f}")
print(f"Single Tree - Test  acc: {single_tree.score(X_test, y_test):.3f}")
# You'll see: train acc ~1.000, test acc ~0.85-0.90 → OVERFITTING!

# --- STEP 4: Train BAGGING (100 trees, each on bootstrap sample) ---
bag_clf = BaggingClassifier(
    estimator=DecisionTreeClassifier(),  # base learner = tree
    n_estimators=100,     # 100 trees in the bag
    bootstrap=True,       # sample WITH replacement
    oob_score=True,       # use out-of-bag for free validation
    random_state=42,
    n_jobs=-1             # use all CPU cores (parallel!)
)
bag_clf.fit(X_train, y_train)
print(f"\nBagging    - Train acc: {bag_clf.score(X_train, y_train):.3f}")
print(f"Bagging    - Test  acc: {bag_clf.score(X_test, y_test):.3f}")
print(f"Bagging    - OOB  acc: {bag_clf.oob_score_:.3f}")
# You'll see: test acc ~0.90-0.95 → BETTER and more STABLE!

# --- STEP 5: Visualize the decision boundaries ---
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

for ax, clf, title in zip(
    axes,
    [single_tree, bag_clf],
    ["Single Tree (overfits!)", "Bagging 100 Trees (smooth!)"]
):
    # Create a mesh grid to plot decision regions
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    xx, yy = np.meshgrid(
        np.linspace(x_min, x_max, 200),
        np.linspace(y_min, y_max, 200)
    )
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
    ax.contourf(xx, yy, Z, alpha=0.3, cmap='RdYlBu')
    ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap='RdYlBu',
               edgecolors='black', s=50)
    ax.set_title(title, fontsize=14)

plt.tight_layout()
plt.savefig("ex1_bagging_vs_single_tree.png", dpi=100)
plt.show()
print("DONE! Notice how the single tree has jagged boundaries (overfit)")
print("while bagging has smooth boundaries (generalizes better).")
```

[↑ Back to Top](#-ensemble-boosting--adaboost-deep-dive-practice)

---

## Ex2: Bagging vs Boosting Side-by-Side

```python
# ============================================================
# Ex2: BAGGING vs BOOSTING — Same Data, Different Strategy
# ============================================================
# Bagging: 100 trees trained in PARALLEL on different data subsets
# Boosting (AdaBoost): trees trained ONE AFTER ANOTHER, each
#                      focusing on what the previous one got WRONG

from sklearn.ensemble import (
    BaggingClassifier,
    AdaBoostClassifier,
    GradientBoostingClassifier
)
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_moons
from sklearn.model_selection import cross_val_score
import numpy as np

# --- STEP 1: Create data ---
X, y = make_moons(n_samples=500, noise=0.3, random_state=42)

# --- STEP 2: Define all 3 models ---
models = {
    "Bagging (100 trees)": BaggingClassifier(
        estimator=DecisionTreeClassifier(max_depth=5),
        n_estimators=100, random_state=42, n_jobs=-1
    ),
    "AdaBoost (100 stumps)": AdaBoostClassifier(
        estimator=DecisionTreeClassifier(max_depth=1),  # stump!
        n_estimators=100, learning_rate=0.5, random_state=42,
        algorithm='SAMME'
    ),
    "GradientBoosting (100 trees)": GradientBoostingClassifier(
        n_estimators=100, max_depth=3, learning_rate=0.1,
        random_state=42
    ),
}

# --- STEP 3: Compare using 5-fold cross-validation ---
print("MODEL COMPARISON (5-fold CV):")
print("=" * 50)
for name, model in models.items():
    # cross_val_score: train on 4 folds, test on 1 fold, rotate 5 times
    scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
    print(f"{name:35s} → {scores.mean():.3f} ± {scores.std():.3f}")

# EXPECTED OUTPUT (approx):
# Bagging (100 trees)                 → 0.940 ± 0.015
# AdaBoost (100 stumps)               → 0.920 ± 0.020
# GradientBoosting (100 trees)        → 0.950 ± 0.012
#
# KEY INSIGHT: All better than a single tree (~0.88)!
# GBM often wins because it combines boosting + deeper trees.
```

[↑ Back to Top](#-ensemble-boosting--adaboost-deep-dive-practice)

---

## Ex3: AdaBoost From Scratch (Manual)

```python
# ============================================================
# Ex3: ADABOOST FROM SCRATCH — Every Single Step Visible
# ============================================================
# We'll implement AdaBoost manually on a tiny dataset
# so you can see EXACTLY what happens at each round.

import numpy as np

# --- STEP 1: Tiny dataset (same as NUMERICAL P4) ---
X = np.array([[1,2], [2,1], [3,3], [4,2], [5,4]])
y = np.array([+1, +1, -1, -1, -1])
n = len(y)  # 5 samples

print("=" * 60)
print("ADABOOST FROM SCRATCH — MANUAL IMPLEMENTATION")
print("=" * 60)

# --- STEP 2: Initialize weights (all equal) ---
w = np.ones(n) / n  # [0.2, 0.2, 0.2, 0.2, 0.2]
print(f"\nInitial weights: {w}")

# --- STEP 3: Define a simple stump (we'll hardcode for clarity) ---
# Stump: "x₂ <= 2.5 → +1, else → -1"
def stump_1(X_input):
    """First stump: split on feature x₂ at threshold 2.5"""
    predictions = np.where(X_input[:, 1] <= 2.5, +1, -1)
    return predictions

# --- STEP 4: Train Round 1 ---
print("\n--- ROUND 1 ---")

# 4a: Get predictions
preds = stump_1(X)
print(f"Predictions: {preds}")
print(f"Actual:      {y}")

# 4b: Find which are wrong
wrong = (preds != y)                    # boolean array
print(f"Wrong?:      {wrong}")          # [F, F, F, T, F] → P4 is wrong

# 4c: Compute weighted error
r = np.sum(w[wrong]) / np.sum(w)       # sum of wrong weights / total
print(f"Weighted error r = {r:.3f}")    # 0.200

# 4d: Compute amount of say (alpha)
alpha = 0.5 * np.log((1 - r) / r)
print(f"Alpha (amount of say) = {alpha:.3f}")  # 0.693

# 4e: Update weights
#   Wrong points: multiply by exp(+alpha)
#   Right points: multiply by exp(-alpha)
for i in range(n):
    if wrong[i]:
        w[i] = w[i] * np.exp(+alpha)   # increase!
        print(f"  P{i+1}: WRONG → w = {w[i]:.4f} (increased)")
    else:
        w[i] = w[i] * np.exp(-alpha)   # decrease!

# 4f: Normalize weights (make them sum to 1)
w = w / np.sum(w)
print(f"\nNormalized weights after Round 1: {np.round(w, 3)}")
# Expected: [0.125, 0.125, 0.125, 0.500, 0.125]
# P4 now has weight 0.500 = half the total!

print(f"\nRound 1 complete!")
print(f"  Stump: x₂ <= 2.5 → +1")
print(f"  Alpha: {alpha:.3f}")
print(f"  Next round will FOCUS on P4 (weight = {w[3]:.3f})")
print(f"  because it was misclassified and now has highest weight!")

# --- STEP 5: Show how final prediction works ---
print("\n--- FINAL PREDICTION (after 1 round) ---")
test_point = np.array([[3, 1]])  # new point
h1_pred = stump_1(test_point)[0]
H_score = alpha * h1_pred
H_pred = np.sign(H_score)
print(f"Test point: x = {test_point[0]}")
print(f"  Stump 1 says: {h1_pred:+d}")
print(f"  Weighted: {alpha:.3f} × {h1_pred:+d} = {H_score:+.3f}")
print(f"  Final: sign({H_score:+.3f}) = {int(H_pred):+d}")
```

[↑ Back to Top](#-ensemble-boosting--adaboost-deep-dive-practice)

---

## Ex4: Decision Stump Builder

```python
# ============================================================
# Ex4: BUILD A DECISION STUMP — Find Best Feature + Threshold
# ============================================================
# A decision stump = simplest tree = 1 split = 1 question

import numpy as np

def find_best_stump(X, y, weights):
    """
    Find the best decision stump for weighted data.
    
    Think of it like trying EVERY possible question:
    "Is feature 0 <= 1.5?" "Is feature 0 <= 2.5?" etc.
    and picking the one that gets the LEAST wrong answers
    (weighted by importance of each sample).
    
    Returns: best_feature, best_threshold, best_error, predictions
    """
    n_samples, n_features = X.shape
    best_error = float('inf')  # start with worst possible
    best_feature = None
    best_threshold = None
    best_preds = None
    
    # Try each feature (column)
    for feature_idx in range(n_features):
        # Get all unique values of this feature
        values = np.sort(np.unique(X[:, feature_idx]))
        
        # Try each midpoint as a threshold
        for i in range(len(values) - 1):
            threshold = (values[i] + values[i + 1]) / 2
            
            # Try both directions: <= threshold → +1 or -1
            for direction in [+1, -1]:
                # Make predictions
                preds = np.where(
                    X[:, feature_idx] <= threshold,
                    direction,      # left side
                    -direction      # right side
                )
                
                # Compute WEIGHTED error
                wrong = (preds != y)
                weighted_error = np.sum(weights[wrong])
                
                # Is this the best stump so far?
                if weighted_error < best_error:
                    best_error = weighted_error
                    best_feature = feature_idx
                    best_threshold = threshold
                    best_preds = preds.copy()
    
    return best_feature, best_threshold, best_error, best_preds

# --- TEST IT on our data ---
X = np.array([[1,2], [2,1], [3,3], [4,2], [5,4]])
y = np.array([+1, +1, -1, -1, -1])
w = np.ones(len(y)) / len(y)

feat, thresh, err, preds = find_best_stump(X, y, w)
alpha = 0.5 * np.log((1 - err) / err) if err > 0 else float('inf')

print(f"Best stump: feature x{feat+1} <= {thresh}")
print(f"Weighted error: {err:.3f}")
print(f"Amount of say (alpha): {alpha:.3f}")
print(f"Predictions: {preds}")
print(f"Actual:      {y}")
print(f"Correct:     {np.sum(preds == y)}/{len(y)}")
```

[↑ Back to Top](#-ensemble-boosting--adaboost-deep-dive-practice)

---

## Ex5: Weight Update Visualizer

```python
# ============================================================
# Ex5: WATCH WEIGHTS CHANGE — AdaBoost Weight Animation
# ============================================================
# See how misclassified points get HEAVIER each round

import numpy as np
import matplotlib.pyplot as plt

# Data
X = np.array([[1,2], [2,1], [3,3], [4,2], [5,4]])
y = np.array([+1, +1, -1, -1, -1])
n = len(y)

# AdaBoost for 3 rounds (using sklearn-style stumps)
from sklearn.tree import DecisionTreeClassifier

weights_history = []
alpha_history = []
w = np.ones(n) / n
weights_history.append(w.copy())

for t in range(3):
    # Train a weighted stump
    stump = DecisionTreeClassifier(max_depth=1)
    stump.fit(X, y, sample_weight=w)
    preds = stump.predict(X)
    
    # Compute error
    wrong = (preds != y)
    r = np.sum(w[wrong]) / np.sum(w)
    r = np.clip(r, 1e-10, 1 - 1e-10)  # avoid log(0)
    
    # Alpha
    alpha = 0.5 * np.log((1 - r) / r)
    alpha_history.append(alpha)
    
    # Update weights
    w = w * np.exp(alpha * np.where(wrong, +1, -1))
    w = w / np.sum(w)  # normalize
    weights_history.append(w.copy())
    
    print(f"Round {t+1}: error={r:.3f}, alpha={alpha:.3f}")
    print(f"  Weights: {np.round(w, 3)}")
    print(f"  Wrong:   {np.where(wrong)[0] + 1}")

# --- Plot weight evolution ---
fig, ax = plt.subplots(figsize=(10, 5))
weight_matrix = np.array(weights_history)
for i in range(n):
    label = f"P{i+1} (y={y[i]:+d})"
    ax.plot(range(len(weights_history)), weight_matrix[:, i],
            'o-', linewidth=2, markersize=8, label=label)

ax.set_xlabel("Round", fontsize=12)
ax.set_ylabel("Weight", fontsize=12)
ax.set_title("AdaBoost: Sample Weights Over Rounds", fontsize=14)
ax.set_xticks(range(len(weights_history)))
ax.set_xticklabels(["Init"] + [f"Round {t+1}" for t in range(3)])
ax.legend(loc='upper left')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("ex5_weight_evolution.png", dpi=100)
plt.show()
print("\nNOTICE: Misclassified points get HEAVIER (go UP) each round!")
print("Correctly classified points get LIGHTER (go DOWN).")
```

[↑ Back to Top](#-ensemble-boosting--adaboost-deep-dive-practice)

---

## Ex6: Model Selection Experiment

```python
# ============================================================
# Ex6: MODEL SELECTION — Which Algorithm Fits Your Problem?
# ============================================================
# The lecture discussed choosing the right model.
# Let's actually TRY 5 models on the same data and compare!

import numpy as np
from sklearn.datasets import make_moons
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import (
    RandomForestClassifier,
    AdaBoostClassifier,
    GradientBoostingClassifier
)
from sklearn.svm import SVC

# --- STEP 1: Create data (non-linear, like real-world) ---
X, y = make_moons(n_samples=500, noise=0.25, random_state=42)

# --- STEP 2: Define 5 different algorithms ---
models = {
    "Logistic Regression": LogisticRegression(),
    "Decision Tree (depth=5)": DecisionTreeClassifier(max_depth=5, random_state=42),
    "Random Forest (100)": RandomForestClassifier(n_estimators=100, random_state=42),
    "AdaBoost (100 stumps)": AdaBoostClassifier(
        estimator=DecisionTreeClassifier(max_depth=1),
        n_estimators=100, random_state=42, algorithm='SAMME'
    ),
    "SVM (RBF kernel)": SVC(kernel='rbf', gamma='scale'),
}

# --- STEP 3: 5-fold cross-validation for each ---
print("MODEL SELECTION EXPERIMENT")
print("=" * 55)
print(f"{'Model':<30} {'Mean Acc':>10} {'Std':>8}")
print("-" * 55)

results = {}
for name, model in models.items():
    scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
    results[name] = scores
    print(f"{name:<30} {scores.mean():>10.3f} {scores.std():>8.3f}")

# --- STEP 4: Find the winner ---
best_model = max(results, key=lambda k: results[k].mean())
print(f"\nBEST MODEL: {best_model}")
print(f"\nNO FREE LUNCH: This is the best for THIS data.")
print(f"For different data, a different model might win!")
print(f"ALWAYS try multiple models and compare with cross-validation.")
```

[↑ Back to Top](#-ensemble-boosting--adaboost-deep-dive-practice)

---

## Ex7: GMM Basics — Soft Clustering

```python
# ============================================================
# Ex7: GMM vs K-MEANS — Hard vs Soft Clustering
# ============================================================
# K-Means: "You belong to Cluster A. Period."
# GMM:     "You're 70% Cluster A, 30% Cluster B."

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture

# --- STEP 1: Create overlapping blob data ---
# 3 clusters that partially overlap (GMM should handle better)
X, y_true = make_blobs(
    n_samples=300,
    centers=[[0, 0], [3, 3], [6, 0]],  # 3 cluster centers
    cluster_std=[1.2, 1.5, 1.0],        # different spreads!
    random_state=42
)

# --- STEP 2: K-Means (hard assignment) ---
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans_labels = kmeans.fit_predict(X)

# --- STEP 3: GMM (soft assignment) ---
gmm = GaussianMixture(n_components=3, random_state=42)
gmm.fit(X)
gmm_labels = gmm.predict(X)           # hard labels (for plotting)
gmm_probs = gmm.predict_proba(X)      # SOFT probabilities!

# --- STEP 4: Show the difference ---
print("GMM SOFT PROBABILITIES (first 5 points):")
print("=" * 55)
print(f"{'Point':<8} {'P(C1)':>8} {'P(C2)':>8} {'P(C3)':>8} {'Assign':>8}")
print("-" * 55)
for i in range(5):
    probs = gmm_probs[i]
    assigned = np.argmax(probs)
    print(f"  x[{i}]  {probs[0]:>8.3f} {probs[1]:>8.3f} {probs[2]:>8.3f}    C{assigned}")

# --- STEP 5: Plot side by side ---
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].scatter(X[:, 0], X[:, 1], c=kmeans_labels, cmap='viridis',
                s=30, alpha=0.7)
axes[0].scatter(kmeans.cluster_centers_[:, 0],
                kmeans.cluster_centers_[:, 1],
                c='red', marker='X', s=200, edgecolors='black')
axes[0].set_title("K-Means (Hard Clustering)", fontsize=14)

# For GMM, color by max probability (opacity = confidence)
axes[1].scatter(X[:, 0], X[:, 1], c=gmm_labels, cmap='viridis',
                s=30, alpha=gmm_probs.max(axis=1))  # opacity = confidence!
axes[1].scatter(gmm.means_[:, 0], gmm.means_[:, 1],
                c='red', marker='X', s=200, edgecolors='black')
axes[1].set_title("GMM (Soft Clustering — faded = uncertain)", fontsize=14)

plt.tight_layout()
plt.savefig("ex7_gmm_vs_kmeans.png", dpi=100)
plt.show()

print("\nKEY INSIGHT:")
print("  Faded points in GMM plot = the model is UNCERTAIN about them.")
print("  K-Means can't express uncertainty — it's always 100% confident.")
print("  GMM gives probabilities, which is more honest and useful!")

# --- STEP 6: GMM parameters ---
print("\nGMM LEARNED PARAMETERS:")
for k in range(3):
    print(f"\n  Component {k}:")
    print(f"    Mean (center): {gmm.means_[k].round(2)}")
    print(f"    Covariance:\n{np.round(gmm.covariances_[k], 2)}")
    print(f"    Weight (pi):   {gmm.weights_[k]:.3f}")
```

[↑ Back to Top](#-ensemble-boosting--adaboost-deep-dive-practice)

---

## 🎯 Self-Test: Can You Do These Without Looking?

```
□ 1. Given error r=0.2, compute alpha from memory
     (Answer: α = ½ × ln(4) = ½ × 1.386 = 0.693)

□ 2. Given 5 equal-weight samples, one misclassified with α=0.693,
     write the updated weights before and after normalization

□ 3. Write 3 lines of sklearn code to train AdaBoost with 200 stumps

□ 4. Explain in one sentence: why does AdaBoost use stumps not deep trees?

□ 5. Compute GMM responsibility for a point equidistant from 2 means
     (Answer: γ₁ = γ₂ = 0.5, since distances are equal and same σ, π)
```

---

## 🔗 What's Next?

```
AFTER THIS LECTURE:
  → GMM deep-dive (EM algorithm in detail) — NEXT LECTURE
  → SVM and kernel methods — UPCOMING
  → Practice: Try AdaBoost on your own dataset in Colab!

REVISION PATH:
  1. Re-read THEORY (20 min)
  2. Redo NUMERICAL P4 and P5 by hand (15 min)
  3. Run all Colab exercises (1 hr)
  4. Do the self-test above without peeking
```

---

> **Nav:** [← INDEX](ml_ensemble_boosting_adaboost_index.md) | [📖 THEORY](ml_ensemble_boosting_adaboost_theory.md) | [🔢 NUMERICAL](ml_ensemble_boosting_adaboost_numerical.md) | 💻 PRACTICE

[↑ Back to Top](#-ensemble-boosting--adaboost-deep-dive-practice)

---

*AI · ML · github.com/rpaut03l/TS-01-Pvt*
