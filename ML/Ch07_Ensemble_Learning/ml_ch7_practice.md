# 💻 Ch7 — Ensemble Learning: PRACTICE
### *All book exercises solved. Mind-friendly steps. Full Colab code.*

> **Nav:** [← INDEX](./ml_ch7_index.md) | [📖 THEORY](./ml_ch7_theory.md) | [🔢 NUMERICAL](./ml_ch7_practice.md) | 💻 **PRACTICE**

---

## 📋 Exercise Map

| # | Question | Topic | Level |
|---|----------|-------|-------|
| Q1 | 5 models at 95% — can combine? | Voting math | 🟢 |
| Q2 | Hard vs Soft voting | Voting | 🟢 |
| Q3 | Speed up bagging across servers | Bagging | 🟡 |
| Q4 | OOB benefit | OOB | 🟡 |
| Q5 | Extra-Trees: more random, slower/faster? | Extra-Trees | 🟡 |
| Q6 | AdaBoost overfits → what to tweak? | AdaBoost | 🟡 |
| Q7 | GBM underfits → what to tweak? | GBM | 🟡 |
| Q8 | MNIST: voting ensemble (code) | Coding | 🔴 |
| Q9 | MNIST: stacking blender (code) | Coding | 🔴 |

---

## 🟢 Q1 — Five 95%-accurate models. Can combining help?

```
👶 5 friends each score 95% on a test. If they work together, even better?
   YES — IF they make different mistakes (independent errors).

MATH: Each clf error = 0.05. 5 classifiers majority vote.
  Wrong only if 3+ of 5 wrong:
  P(3 wrong) = C(5,3)×0.05³×0.95² = 10×0.000125×0.9025 = 0.00113
  P(4 wrong) = 5×0.05⁴×0.95¹                            = 0.000030
  P(5 wrong) = 1×0.05⁵                                  = 0.0000003

  Ensemble error = 0.00113+0.000030+0.0000003 ≈ 0.00116 = 0.116%

  Individual: 5% error → Ensemble: 0.116% (43× better!) ✅

CAVEAT: Works only if errors are INDEPENDENT.
  Same model type + same data → correlated errors → no benefit.
  Need DIVERSE classifiers (different algorithms/feature subsets).
```

---

## 🟢 Q2 — Hard vs Soft Voting

```
HARD:  each clf predicts a label → majority wins
       Works with any clf. Ignores confidence.

SOFT:  each clf gives probabilities → average → pick highest
       Needs predict_proba(). Uses confidence. USUALLY BETTER.

Where soft beats hard:
  Clf A: P(class1)=0.51  → hard vote: class1 (barely!)
  Clf B: P(class1)=0.51  → hard vote: class1 (barely!)
  Clf C: P(class1)=0.02  → hard vote: class0 (very confident!)

  Hard vote: class1 wins 2-1  ← WRONG, A&B barely care
  Soft vote: avg=(0.51+0.51+0.02)/3=0.347 → class0  ✅

ENABLE SOFT IN SKLEARN:
  VotingClassifier(voting='soft')
  NOTE: SVC needs SVC(probability=True)
```

---

## 🟡 Q3 — Speed Up Bagging Across Servers

```
YES — Bagging is embarrassingly parallel!

Each tree needs only its own bootstrap sample → completely independent.
→ Train 100 trees on 100 machines simultaneously
→ Combine at the end (just collect all trees)

LOCAL (multi-core):   BaggingClassifier(n_jobs=-1)
DISTRIBUTED (manual): train on each server, then combine:
    all_trees = server1.estimators_ + server2.estimators_ + ...

SPEEDUP is linear in number of machines ✅
```

---

## 🟡 Q4 — OOB Evaluation Benefit

```
WITHOUT OOB: You split data → 80% train, 20% val. Less training data.

WITH OOB:
  Bootstrap sample: ~63.2% unique points per tree
  ~36.8% never seen = OOB instances = FREE validation for that tree!

  Each point gets predicted by ~36.8% of trees (those that never saw it)
  Average those → OOB score ≈ leave-one-out cross-val accuracy

  BaggingClassifier(oob_score=True)
  model.oob_score_  ← prints accuracy for FREE, no val split needed ✅

USE WHEN: limited data, or quick quality estimate without CV.
```

---

## 🟡 Q5 — Extra-Trees More Random. Slower or Faster?

```
RANDOM FOREST at each node:
  → try √n features, find BEST threshold for each  ← sorting needed O(n log n)

EXTRA-TREES at each node:
  → try √n features, pick RANDOM threshold for each ← no sorting O(n)

RESULT: Extra-Trees is FASTER ✅
  More bias (random thresholds not optimal)
  Less variance (more diverse trees)

WHEN EXTRA-TREES WINS:
  High-noise data (extra randomness helps)
  Speed is important

HOW TO CHOOSE: cross-validate both, pick the better one.
```

---

## 🟡 Q6 — AdaBoost Overfits. What to Tweak?

```
👶 Student memorising last year's questions → fails new ones.
   Fix: study less intensely, or fewer rounds.

OVERFITTING SIGNALS: high train accuracy, low val accuracy

FIXES:
  1. ↓ learning_rate (η)     → each tree has less influence
     (compensate with ↑ n_estimators)
  2. ↓ n_estimators           → fewer boosting rounds
  3. Keep base learner shallow (max_depth=1 is already minimal)
  4. More training data

TYPICAL GOOD VALUES: learning_rate=0.1, n_estimators=200

  AdaBoostClassifier(learning_rate=0.1, n_estimators=200)
```

---

## 🟡 Q7 — GBM Underfits. What to Tweak?

```
👶 Student learning too slowly, gave up too early.
   Fix: bigger steps, or more practice rounds.

UNDERFITTING SIGNALS: low train AND val accuracy (high bias)

FIXES:
  1. ↑ learning_rate           → bigger correction steps
  2. ↑ n_estimators            → more boosting rounds
  3. ↑ max_depth (e.g. 3→5)   → more expressive trees
  4. ↓ min_samples_leaf        → allow finer splits
```

```python
# ── Early stopping to find optimal n_estimators ──────────────────
# staged_predict() yields predictions after each tree is added

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score
import numpy as np

# Tiny demo with make_classification (no MNIST needed)
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X_d, y_d = make_classification(n_samples=2000, n_features=20, random_state=42)
X_dt, X_dv, y_dt, y_dv = train_test_split(X_d, y_d, random_state=42)

gbm = GradientBoostingClassifier(n_estimators=300, learning_rate=0.1,
                                  max_depth=3, random_state=42)
gbm.fit(X_dt, y_dt)

# staged_predict → accuracy after each of the 300 trees
val_errors = [1 - accuracy_score(y_dv, y_pred)
              for y_pred in gbm.staged_predict(X_dv)]

best_n = int(np.argmin(val_errors)) + 1   # +1 because index is 0-based
print(f"Optimal n_estimators = {best_n}")
print(f"Best val error        = {val_errors[best_n-1]:.4f}")

# Refit with optimal n_estimators
gbm_best = GradientBoostingClassifier(n_estimators=best_n, learning_rate=0.1,
                                       max_depth=3, random_state=42)
gbm_best.fit(X_dt, y_dt)
print(f"Final val acc = {gbm_best.score(X_dv, y_dv):.4f}")
```

---

## 🔴 Q8 — MNIST Voting Ensemble (Full Code)

> ⚠️ **Self-contained cell. SVM on 50k samples takes ~10-15 min in Colab. Use the faster version below if you're in a hurry.**

```python
# ── CELL Q8: fully self-contained — paste & run directly ─────────
import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, VotingClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# ── 1. Load MNIST ────────────────────────────────────────────────
print("Loading MNIST (this may take ~30s)...")
mnist = fetch_openml('mnist_784', version=1, as_frame=False, parser='auto')
X, y  = mnist.data, mnist.target.astype(int)
print(f"Loaded: X={X.shape}, y={y.shape}")

# ── 2. Split: 10k train / 5k val / 5k test  (fast version)
#    Change train_size=50000 for full experiment (slow SVM!)
X_tr, X_tmp, y_tr, y_tmp = train_test_split(
    X, y, train_size=10000, random_state=42, stratify=y)
X_val, X_test, y_val, y_test = train_test_split(
    X_tmp, y_tmp, test_size=0.5, random_state=42, stratify=y_tmp)

print(f"Train: {X_tr.shape}  Val: {X_val.shape}  Test: {X_test.shape}")

# ── 3. Scale ─────────────────────────────────────────────────────
scaler   = StandardScaler()
X_tr_s   = scaler.fit_transform(X_tr)   # fit on train only!
X_val_s  = scaler.transform(X_val)
X_test_s = scaler.transform(X_test)

# ── 4. Train each classifier individually ────────────────────────
rf  = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
et  = ExtraTreesClassifier(n_estimators=100, random_state=42, n_jobs=-1)
svm = SVC(probability=True, random_state=42)   # probability=True needed for soft voting!

for name, clf in [("Random Forest", rf), ("Extra Trees", et), ("SVM", svm)]:
    print(f"Training {name}...")
    clf.fit(X_tr_s, y_tr)
    print(f"  val acc: {clf.score(X_val_s, y_val):.4f}")

# ── 5. Soft Voting Ensemble ──────────────────────────────────────
# VotingClassifier with pre-fitted estimators: set voting='soft'
# NOTE: When estimators are already fitted, VotingClassifier re-fits them
#       internally. To avoid that, use set_params to pass fitted ones
#       OR just use predict_proba manually (Method B below).

# Method A: Let VotingClassifier re-fit (straightforward)
voting_clf = VotingClassifier(
    estimators=[('rf', RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)),
                ('et', ExtraTreesClassifier(n_estimators=100, random_state=42, n_jobs=-1)),
                ('svm', SVC(probability=True, random_state=42))],
    voting='soft'
)
voting_clf.fit(X_tr_s, y_tr)
print(f"\nVoting (soft) val acc: {voting_clf.score(X_val_s, y_val):.4f}")

# Method B: Manual soft vote using already-trained clfs (faster, no re-fit)
proba_val = np.mean([
    rf.predict_proba(X_val_s),
    et.predict_proba(X_val_s),
    svm.predict_proba(X_val_s)
], axis=0)
manual_preds = np.argmax(proba_val, axis=1)
print(f"Manual soft vote val acc: {accuracy_score(y_val, manual_preds):.4f}")

# ── 6. Compare: drop one clf at a time ───────────────────────────
print("\n── Drop-one analysis (manual soft vote) ──")
all_clfs = [("rf", rf), ("et", et), ("svm", svm)]
for drop_name, _ in all_clfs:
    keep = [(n, c) for n, c in all_clfs if n != drop_name]
    p = np.mean([c.predict_proba(X_val_s) for _, c in keep], axis=0)
    acc = accuracy_score(y_val, np.argmax(p, axis=1))
    print(f"  Without {drop_name:3s}: val acc = {acc:.4f}")

# ── 7. Final test score (run ONCE) ──────────────────────────────
proba_test = np.mean([
    rf.predict_proba(X_test_s),
    et.predict_proba(X_test_s),
    svm.predict_proba(X_test_s)
], axis=0)
test_acc = accuracy_score(y_test, np.argmax(proba_test, axis=1))
print(f"\nFinal TEST acc (soft vote): {test_acc:.4f}")
```

---

## 🔴 Q9 — MNIST Stacking Blender (Full Code)

> ⚠️ **Self-contained cell — includes all data loading. No dependency on Q8.**

```python
# ── CELL Q9: fully self-contained — paste & run directly ─────────
import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split, cross_val_predict
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import (RandomForestClassifier, ExtraTreesClassifier,
                               StackingClassifier, GradientBoostingClassifier)
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# ── 1. Load & split MNIST ────────────────────────────────────────
print("Loading MNIST...")
mnist = fetch_openml('mnist_784', version=1, as_frame=False, parser='auto')
X, y  = mnist.data, mnist.target.astype(int)

# 3-way split: train / val (blender training) / test
X_tr, X_tmp, y_tr, y_tmp = train_test_split(
    X, y, train_size=10000, random_state=42, stratify=y)
X_val, X_test, y_val, y_test = train_test_split(
    X_tmp, y_tmp, test_size=0.5, random_state=42, stratify=y_tmp)

print(f"Train: {X_tr.shape}  Val: {X_val.shape}  Test: {X_test.shape}")

# ── 2. Scale ─────────────────────────────────────────────────────
scaler   = StandardScaler()
X_tr_s   = scaler.fit_transform(X_tr)
X_val_s  = scaler.transform(X_val)
X_test_s = scaler.transform(X_test)

# ── 3. Train base classifiers ────────────────────────────────────
rf  = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
et  = ExtraTreesClassifier(n_estimators=100, random_state=42, n_jobs=-1)
svm = SVC(probability=True, random_state=42)

print("Training base classifiers...")
for name, clf in [("RF", rf), ("ET", et), ("SVM", svm)]:
    clf.fit(X_tr_s, y_tr)
    print(f"  {name} val acc: {clf.score(X_val_s, y_val):.4f}")

# ── 4. METHOD A: sklearn StackingClassifier ──────────────────────
# cv=5 internally generates out-of-fold predictions for meta-learner
print("\nTraining sklearn StackingClassifier (cv=5, may take a few mins)...")
stack = StackingClassifier(
    estimators=[
        ('rf',  RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)),
        ('et',  ExtraTreesClassifier(n_estimators=100, random_state=42, n_jobs=-1)),
        ('svm', SVC(probability=True, random_state=42))
    ],
    final_estimator=LogisticRegression(max_iter=1000, random_state=42),
    cv=3,         # use 3 for speed, 5 for better results
    n_jobs=-1
)
stack.fit(X_tr_s, y_tr)
print(f"Stacking val acc:  {stack.score(X_val_s, y_val):.4f}")
print(f"Stacking test acc: {stack.score(X_test_s, y_test):.4f}")

# ── 5. METHOD B: Manual stacking (understand the internals) ──────
# Key insight: base clfs predict on VAL SET → becomes blender's train data
# Val set was NEVER seen by base clfs during their training → no leakage!

val_meta = np.column_stack([
    rf.predict_proba(X_val_s),    # shape (n_val, 10) — 10 digit classes
    et.predict_proba(X_val_s),    # shape (n_val, 10)
    svm.predict_proba(X_val_s)    # shape (n_val, 10)
])   # final shape: (n_val, 30)
print(f"\nMeta-features shape: {val_meta.shape}")

blender = LogisticRegression(max_iter=1000, random_state=42)
blender.fit(val_meta, y_val)

# Blender predicts on TEST SET using base clf predictions
test_meta = np.column_stack([
    rf.predict_proba(X_test_s),
    et.predict_proba(X_test_s),
    svm.predict_proba(X_test_s)
])
print(f"Manual blender test acc: {blender.score(test_meta, y_test):.4f}")

# ── 6. Final leaderboard ─────────────────────────────────────────
print("\n=== LEADERBOARD (test set) ===")

# Manual soft vote (for comparison)
proba_test = np.mean([rf.predict_proba(X_test_s),
                      et.predict_proba(X_test_s),
                      svm.predict_proba(X_test_s)], axis=0)
vote_acc = accuracy_score(y_test, np.argmax(proba_test, axis=1))

results = {
    "Random Forest":     rf.score(X_test_s, y_test),
    "Extra Trees":       et.score(X_test_s, y_test),
    "SVM":               svm.score(X_test_s, y_test),
    "Soft Voting":       vote_acc,
    "Stacking (sklearn)": stack.score(X_test_s, y_test),
    "Manual Blender":    blender.score(test_meta, y_test),
}
for name, acc in sorted(results.items(), key=lambda x: -x[1]):
    bar = "█" * int(acc * 40)
    print(f"  {name:22s}: {acc:.4f}  {bar}")
```

---

## ⚡ One-Liners (copy-paste snippets)

```python
# Voting (soft) — always set probability=True for SVC
VotingClassifier([('rf', RandomForestClassifier()), ('svm', SVC(probability=True))],
                 voting='soft').fit(X_train, y_train)

# Bagging with free OOB validation
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
bg = BaggingClassifier(DecisionTreeClassifier(), n_estimators=500,
                        oob_score=True, n_jobs=-1).fit(X_train, y_train)
print(bg.oob_score_)

# Random Forest feature importance
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators=100).fit(X_train, y_train)
print(rf.feature_importances_)   # array of length n_features, sums to 1

# AdaBoost with decision stump
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
AdaBoostClassifier(DecisionTreeClassifier(max_depth=1),
                   n_estimators=200, learning_rate=0.1).fit(X_train, y_train)

# GBM early stopping
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score
import numpy as np
gbm = GradientBoostingClassifier(n_estimators=300).fit(X_train, y_train)
errs = [1 - accuracy_score(y_val, p) for p in gbm.staged_predict(X_val)]
best_n = np.argmin(errs) + 1

# Stacking
from sklearn.ensemble import StackingClassifier
from sklearn.linear_model import LogisticRegression
StackingClassifier(estimators=[('rf', rf), ('et', et)],
                   final_estimator=LogisticRegression(), cv=5).fit(X_train, y_train)

# Manual soft vote (no re-fitting)
proba = np.mean([clf.predict_proba(X_test) for clf in [rf, et, svm]], axis=0)
preds = np.argmax(proba, axis=1)
```

---

## 🧪 EXAM HACKS

```
💡 Stacking blender trained on VAL predictions (never on training preds)
💡 OOB ≈ 36.8% of data per tree → use oob_score=True for free val
💡 Soft voting: SVC needs probability=True
💡 AdaBoost overfit → ↓ learning_rate. GBM underfit → ↑ max_depth
💡 staged_predict() → find optimal n_estimators with early stopping
💡 Combining diverse classifiers → errors cancel → better ensemble
```

---

> **Nav:** [← INDEX](./ml_ch7_index.md) | [📖 THEORY](./ml_ch7_theory.md) | [🔢 NUMERICAL](./ml_ch7_practice.md) | 💻 **PRACTICE**

* AI · ML · github.com/rpaut03l/TS-01*
