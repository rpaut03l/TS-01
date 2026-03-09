# 💻 Ch7 — Ensemble Learning: PRACTICE
### *All book exercises solved. Mind-friendly steps. Colab code.*

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

EARLY STOPPING to find optimal n_estimators:
  for y_pred in gbm.staged_predict(X_val):
      val_errors.append(1 - accuracy_score(y_val, y_pred))
  best_n = np.argmin(val_errors) + 1
```

---

## 🔴 Q8 — MNIST Voting Ensemble (Full Code)

```python
import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, VotingClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# ── 1. Load MNIST ────────────────────────────────────────────────
mnist = fetch_openml('mnist_784', version=1, as_frame=False)
X, y  = mnist.data, mnist.target.astype(int)

# Use 50k train / 10k val / 10k test
X_tr, X_tmp, y_tr, y_tmp = train_test_split(X, y, train_size=50000, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_tmp, y_tmp, test_size=0.5, random_state=42)

# ── 2. Scale ─────────────────────────────────────────────────────
scaler = StandardScaler()
X_tr_s   = scaler.fit_transform(X_tr)
X_val_s  = scaler.transform(X_val)
X_test_s = scaler.transform(X_test)

# ── 3. Train base classifiers ────────────────────────────────────
rf  = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
et  = ExtraTreesClassifier(n_estimators=100, random_state=42, n_jobs=-1)
svm = SVC(probability=True, random_state=42)

for name, clf in [("RF", rf), ("ET", et), ("SVM", svm)]:
    clf.fit(X_tr_s, y_tr)
    print(f"{name} val acc: {clf.score(X_val_s, y_val):.4f}")

# ── 4. Soft Voting Ensemble ──────────────────────────────────────
voting = VotingClassifier(
    estimators=[('rf',rf),('et',et),('svm',svm)],
    voting='soft'
)
voting.fit(X_tr_s, y_tr)
print(f"Voting val acc: {voting.score(X_val_s, y_val):.4f}")

# ── 5. Test set (run ONCE at the end) ───────────────────────────
print(f"\nFinal TEST acc: {voting.score(X_test_s, y_test):.4f}")

# ── 6. Remove weakest member and retest ─────────────────────────
# Try removing the worst individual classifier
for drop in ['rf','et','svm']:
    remaining = [(n,c) for n,c in [('rf',rf),('et',et),('svm',svm)] if n != drop]
    v2 = VotingClassifier(estimators=remaining, voting='soft')
    v2.fit(X_tr_s, y_tr)
    print(f"Without {drop}: val acc = {v2.score(X_val_s, y_val):.4f}")
```

---

## 🔴 Q9 — MNIST Stacking Blender (Full Code)

```python
# Continuing from Q8 (base classifiers already trained)
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import StackingClassifier

# ── METHOD 1: sklearn StackingClassifier ────────────────────────
stack = StackingClassifier(
    estimators=[('rf',rf),('et',et),('svm',svm)],
    final_estimator=LogisticRegression(max_iter=1000),
    cv=5,
    n_jobs=-1
)
stack.fit(X_tr_s, y_tr)
print(f"Stacking val acc: {stack.score(X_val_s, y_val):.4f}")

# ── METHOD 2: Manual Stacking (understand the internals) ─────────
# Base models predict on VAL SET → becomes blender's training data
val_meta = np.column_stack([
    rf.predict_proba(X_val_s),     # (10000, 10)
    et.predict_proba(X_val_s),
    svm.predict_proba(X_val_s)
])  # shape: (10000, 30)

blender = LogisticRegression(max_iter=1000, random_state=42)
blender.fit(val_meta, y_val)

# Blender predicts on TEST SET
test_meta = np.column_stack([
    rf.predict_proba(X_test_s),
    et.predict_proba(X_test_s),
    svm.predict_proba(X_test_s)
])
print(f"Manual stacking test acc: {blender.score(test_meta, y_test):.4f}")

# ── Final comparison ─────────────────────────────────────────────
print("\n=== LEADERBOARD ===")
results = {
    "Random Forest":  rf.score(X_test_s, y_test),
    "Extra Trees":    et.score(X_test_s, y_test),
    "SVM":            svm.score(X_test_s, y_test),
    "Soft Voting":    voting.score(X_test_s, y_test),
    "Stacking":       stack.score(X_test_s, y_test),
}
for name, acc in sorted(results.items(), key=lambda x: -x[1]):
    print(f"  {name:20s}: {acc:.4f}  {'█'*int(acc*40)}")
```

---

## ⚡ One-Liners

```python
VotingClassifier([('rf',rf),('svm',svm)], voting='soft').fit(X,y)
BaggingClassifier(n_estimators=500, oob_score=True).fit(X,y).oob_score_
rf.feature_importances_
AdaBoostClassifier(DecisionTreeClassifier(max_depth=1), n_estimators=200)
np.argmin([e for e in gbm.staged_predict(X_val)]) + 1  # best n_estimators
StackingClassifier([...], final_estimator=LogisticRegression())
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

> **Nav:** [← INDEX](./ml_ch7_index.md) | [📖 THEORY](./ml_ch7_theory.md) | [🔢 NUMERICAL](./ml_ch7_numerical.md) | 💻 PRACTICE

*AI · ML · github.com/rpaut03l/TS-01*
