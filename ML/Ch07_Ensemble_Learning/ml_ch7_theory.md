# 📖 Ch7 — Ensemble Learning: THEORY
### *Hands-On ML Ch7 · Voting · Bagging · RF · AdaBoost · GBM · Stacking*

> **Nav:** [← INDEX](./ml_ch7_index.md) | 📖 **THEORY** | [🔢 NUMERICAL →](./ml_ch7_numerical.md) | [💻 PRACTICE →](./ml_ch7_practice.md)

---

## 🧠 MNEMONIC: **"BRAVE BOSS"**
> **B**agging · **R**andom Forest · **A**daBoost · **V**oting · **E**xtra-Trees · **B**oosting · **O**OB · **S**tacking · **S**oft-Hard

---

## 🗺️ Big Picture

```
ENSEMBLE LEARNING
   │
   ├─ VOTING ──────── ask many, combine answers
   │
   ├─ BAGGING ─────── same algorithm, different data samples
   │     └─ Random Forest ← Extra-Trees
   │
   ├─ BOOSTING ────── each model fixes previous one's mistakes
   │     ├─ AdaBoost
   │     └─ Gradient Boosting
   │
   └─ STACKING ────── train a model to combine other models

     Bagging/RF = parallel ✅    Boosting = sequential ⛓️
     Bagging reduces VARIANCE    Boosting reduces BIAS
```

---

## 1️⃣ WHY ENSEMBLES WORK

👶 Would you trust 1 doctor's opinion or 1000 doctors voting? 1000 — because their mistakes cancel out!

```
Each clf: 51% accurate (barely better than flipping a coin)
1000 together voting → ~75% accurate!

WHY: If errors are INDEPENDENT, wrong votes cancel each other.
     Diverse classifiers → more independent errors → better ensemble
```

---

## 2️⃣ VOTING

```
HARD VOTING:   each clf predicts a label → majority wins
SOFT VOTING:   each clf gives probabilities → average → pick highest
               BETTER — uses confidence, not just label

Example (soft):
  Clf A: P(cat)=0.9   Clf B: P(cat)=0.8   Clf C: P(cat)=0.35
  avg P(cat) = (0.9+0.8+0.35)/3 = 0.683 → cat ✅
```

```python
VotingClassifier(estimators=[('lr',lr),('svm',svm)], voting='soft')
# SVC needs SVC(probability=True) for soft voting
```

---

## 3️⃣ BAGGING

👶 Run 500 polls on random subsets of voters → average results. Less noisy than one big poll!

```
Bootstrap: sample n points WITH replacement (~63.2% unique per sample)
           Each tree sees different data → diverse → averages out errors

OOB: ~36.8% points never seen by each tree → free validation set!
     oob_score=True → no need for separate val set ✅
```

```python
BaggingClassifier(DecisionTreeClassifier(), n_estimators=500,
                  bootstrap=True, oob_score=True, n_jobs=-1)
# .oob_score_ = free validation accuracy
```

---

## 4️⃣ RANDOM FOREST

👶 Bagging of trees + extra trick: each split only sees a RANDOM SUBSET of features. Makes trees even more different from each other!

```
At each split:
  Bagging:       tries ALL features, picks best split
  Random Forest: tries only √(n_features) random features → picks best of those

More diversity → lower variance → better generalisation
BONUS: feature_importances_ for FREE 🎁
```

```python
RandomForestClassifier(n_estimators=500, max_features='sqrt',
                       oob_score=True, n_jobs=-1)
# .feature_importances_ = which features matter most
```

---

## 5️⃣ EXTRA-TREES

```
One more step of randomness vs Random Forest:
  RF:          try √n features, find OPTIMAL threshold for each
  Extra-Trees: try √n features, use RANDOM threshold → pick best of those

Result: FASTER (no sorting/optimisation) + more random
Trade-off: slightly more bias, less variance

When to prefer:  noisy data, or when speed matters
```

```python
ExtraTreesClassifier(n_estimators=500, n_jobs=-1)
```

---

## 6️⃣ ADABOOST

👶 After each quiz, students who got wrong answers get MORE weight in the next quiz. Each new teacher focuses on the hard cases!

```
ALGORITHM (5 steps):
  1. Start: all sample weights wᵢ = 1/n (equal)
  2. Train weak clf hₜ
  3. Compute error:  r = Σwᵢ[wrong] / Σwᵢ
  4. Compute α:      α = η·ln((1−r)/r)
  5. Update weights: wrong → ×exp(+α), correct → ×exp(−α), normalize
  Repeat T times
  Final: ŷ = sign(Σ αₜ·hₜ(x))

r < 0.5 → α > 0 (useful clf)
r = 0.5 → α = 0 (ignored, random)
r > 0.5 → α < 0 (flip its predictions!)
```

```python
AdaBoostClassifier(DecisionTreeClassifier(max_depth=1),  # stump
                   n_estimators=200, learning_rate=0.5)
```

---

## 7️⃣ GRADIENT BOOSTING

👶 You're predicting exam scores. First guess: average=60. Residual: who's above/below 60? Train tree 2 to fix those gaps. Residual again. Fix again. Each tree ONLY works on the leftover errors!

```
ALGORITHM:
  ŷ₀ = mean(y)
  for m = 1, 2, ..., M:
    rₘ = y − ŷ_current           ← residuals
    fit hₘ₊₁ on (X, rₘ)          ← new tree fits residuals
    ŷ_new = ŷ_old + η·hₘ₊₁(x)   ← small step toward truth

η (learning rate): small η → more trees needed, usually better
subsample < 1: use random subset of data per tree → Stochastic GBM

EARLY STOPPING: use staged_predict() to find best n_estimators
```

```python
GradientBoostingClassifier(n_estimators=200, learning_rate=0.1,
                            max_depth=3, subsample=0.8)
```

---

## 8️⃣ OOB EVALUATION

```
Bootstrap sample: ~63.2% of data → each tree never sees ~36.8%
Those ~36.8% = Out-Of-Bag (OOB) instances for that tree

OOB prediction for point i = average of all trees that never saw i
OOB score ≈ leave-one-out cross-validation accuracy

BENEFIT: Free validation! No held-out set needed.
USE WHEN: Limited data, want fast model quality estimate.
```

---

## 9️⃣ STACKING

👶 5 friends predict tomorrow's weather. Instead of equal vote, you train a 6th friend who has watched all 5 friends for a year and knows WHEN to trust each one. That's the blender/meta-learner!

```
LAYER 1 (Base learners):
  Train rf, svm, lr on training data (using cross-val)
  → predict on hold-out data → get [p_rf, p_svm, p_lr] per point

LAYER 2 (Blender/Meta-learner):
  Train on [p_rf, p_svm, p_lr] → y
  → Learns smart combination

KEY: Base learners never see the blender's training data → no leakage
```

```python
StackingClassifier(
    estimators=[('rf',rf),('svm',svm),('lr',lr)],
    final_estimator=LogisticRegression(),
    cv=5
)
```

---

## 🃏 CHEAT SHEET

```
┌──────────────┬──────────────────┬───────────────┬────────────────┐
│ Method       │ Parallel?        │ Reduces       │ Key param      │
├──────────────┼──────────────────┼───────────────┼────────────────┤
│ Hard Voting  │ ✅               │ Both          │ voting='hard'  │
│ Soft Voting  │ ✅               │ Both          │ voting='soft'  │
│ Bagging      │ ✅               │ Variance      │ oob_score=True │
│ Random Forest│ ✅               │ Variance      │ max_features   │
│ Extra-Trees  │ ✅ (faster RF)   │ Variance      │ n_estimators   │
│ AdaBoost     │ ❌ (sequential)  │ Bias          │ learning_rate  │
│ Grad Boost   │ ❌ (sequential)  │ Bias          │ max_depth=3    │
│ Stacking     │ Partial ✅       │ Both          │ final_estimator│
└──────────────┴──────────────────┴───────────────┴────────────────┘
```

---

## 🧪 EXAM HACKS

```
💡 Bagging reduces VARIANCE. Boosting reduces BIAS.
💡 OOB ~36.8% → free validation, no held-out set needed
💡 RF: max_features='sqrt' at each split (not whole feature set!)
💡 Extra-Trees: random threshold → faster, more diverse
💡 AdaBoost: wrong samples → weight UP (×exp(+α))
💡 GBM: each tree fits RESIDUALS (y − current prediction)
💡 Soft voting > hard voting when classifiers output probabilities
💡 Stacking > Voting: stacking LEARNS the combination weights
💡 Feature importance: only RF/ET give it for free
💡 AdaBoost underfit? → decrease learning_rate OR increase n_estimators
💡 GBM underfit? → increase max_depth OR increase n_estimators
```

---

> **Nav:** [← INDEX](./ml_ch7_index.md) | 📖 THEORY | [🔢 NUMERICAL →](./ml_ch7_numerical.md) | [💻 PRACTICE →](./ml_ch7_practice.md)

*AI · ML · github.com/rpaut03l/TS-01*
