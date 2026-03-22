# 📖 Ensemble Boosting & AdaBoost Deep-Dive: THEORY

### *ML Lecture (Pr. S. Bhagat) · Bagging vs Boosting · AdaBoost · Stumps · Model Selection · GMM Intro*

> **Nav:** [← INDEX](ml_ensemble_boosting_adaboost_index.md) | 📖 **THEORY** | [🔢 NUMERICAL →](ml_ensemble_boosting_adaboost_numerical.md) | [💻 PRACTICE →](ml_ensemble_boosting_adaboost_practice.md)
>
> 🔗 **Related:** [Ch7 THEORY (Géron)](https://github.com/rpaut03l/TS-01/blob/main/ML/Ch07_Ensemble_Learning/ml_ch7_theory.md)

---

## 🧠 MNEMONIC: **"BAD STEW MSG"**

> **B**agging · **A**daBoost · **D**ecision stumps · **S**ample weights · **T**otal error · **E**nsemble voting · **W**eight updates · **M**odel selection · **S**trong classifier · **G**MM intro

---

## 🗺️ Table of Contents

| # | Section | Jump |
|---|---------|------|
| 1 | Why Ensemble Learning? | [§1](#1%EF%B8%8F⃣-why-ensemble-learning) |
| 2 | Bagging vs Boosting | [§2](#2%EF%B8%8F⃣-bagging-vs-boosting) |
| 3 | AdaBoost — The Big Picture | [§3](#3%EF%B8%8F⃣-adaboost--the-big-picture) |
| 4 | Decision Stumps | [§4](#4%EF%B8%8F⃣-decision-stumps) |
| 5 | Amount of Say (α) | [§5](#5%EF%B8%8F⃣-amount-of-say-α) |
| 6 | Sample Weight Updates | [§6](#6%EF%B8%8F⃣-sample-weight-updates) |
| 7 | AdaBoost Full Walkthrough | [§7](#7%EF%B8%8F⃣-adaboost-full-walkthrough) |
| 8 | Model Selection | [§8](#8%EF%B8%8F⃣-model-selection--picking-the-right-tool) |
| 9 | GMM Introduction | [§9](#9%EF%B8%8F⃣-gaussian-mixture-models-gmm--introduction) |
| 10 | Cheat Sheet | [§10](#-cheat-sheet) |
| 11 | Exam Hacks | [§11](#-exam-hacks) |

---

## 1️⃣ WHY ENSEMBLE LEARNING?

### 👶 Easy Story

Imagine you're buying ice cream. You ask ONE friend → they might say "chocolate" (but they always say chocolate!). You ask TEN friends and go with the majority vote → much better chance of picking a flavour everyone loves!

**That's ensemble learning:** don't trust one model, combine MANY models!

### Formal Definition

Ensemble learning trains **multiple models** (called "base learners" or "weak learners") and **combines their predictions** to produce a final answer that is more accurate than any single model alone.

```
WHY IT WORKS — "Wisdom of Crowds"
─────────────────────────────────────────────────────
Single model accuracy:  51% (barely better than a coin flip)
10 models voting:       ~63%
100 models voting:      ~73%
1000 models voting:     ~75%+

CONDITION: models must make DIFFERENT mistakes (diversity!)
If all 1000 copy the same mistake → still wrong. Diversity is key.
```

```
ENSEMBLE LEARNING
   │
   ├─── BAGGING ──── parallel, different data
   │      └── Random Forest, Extra-Trees
   │
   ├─── BOOSTING ─── sequential, fix mistakes
   │      ├── AdaBoost      ← TODAY'S STAR
   │      ├── Gradient Boosting
   │      └── XGBoost, LightGBM, CatBoost
   │
   └─── STACKING ─── learn how to combine
```

[↑ Back to Top](#-ensemble-boosting--adaboost-deep-dive-theory)

---

## 2️⃣ BAGGING vs BOOSTING

### 👶 Easy Story

**Bagging** = You have 10 chefs. Each chef gets a DIFFERENT random basket of ingredients from the same pantry. They all cook separately (in parallel). You taste all 10 dishes and pick the average flavour → balanced and reliable!

**Boosting** = You have 10 chefs, but they cook ONE AFTER ANOTHER. Chef 1 cooks, you taste it. "Too salty!" Chef 2 gets that feedback and tries to fix it. "Now it's bland!" Chef 3 fixes THAT. Each chef only fixes what the previous one got wrong → the final dish is amazing!

### Side-by-Side Comparison

```
┌──────────────────┬────────────────────┬────────────────────┐
│   Feature        │   BAGGING          │   BOOSTING         │
├──────────────────┼────────────────────┼────────────────────┤
│ Training order   │ Parallel ✅        │ Sequential ⛓️     │
│ Data sampling    │ Bootstrap (random  │ Same data, but     │
│                  │  subsets w/ repl.) │   WEIGHTS change   │
│ Focus            │ Reduce VARIANCE    │ Reduce BIAS        │
│ Model diversity  │ Random data splits │ Focus on mistakes  │
│ Overfitting risk │ LOW                │ CAN overfit        │
│ Example          │ Random Forest      │ AdaBoost, GBM      │
│ Each model sees  │ ~63.2% of data     │ 100% (weighted)    │
│ Combination      │ Equal vote/average │ Weighted vote      │
│ Speed            │ Fast (parallel)    │ Slower (must wait) │
└──────────────────┴────────────────────┴────────────────────┘
```

### Text Diagram: How They Differ

```
BAGGING:                              BOOSTING:
────────                              ────────
Data ─┬─ Sample₁ → Model₁ ─┐        Data (w₁) → Model₁
      ├─ Sample₂ → Model₂ ─┤              │ (find mistakes)
      ├─ Sample₃ → Model₃ ─┼→ VOTE   Data (w₂) → Model₂
      └─ Sample₄ → Model₄ ─┘              │ (find mistakes)
                                      Data (w₃) → Model₃
   All run at the SAME TIME               │
   (parallel, independent)            → α₁·M₁ + α₂·M₂ + α₃·M₃
                                      (weighted combination)
                                      Each step DEPENDS on previous!
```

### When to Use What?

```
High VARIANCE (overfitting)?  → Use BAGGING (RF, Extra-Trees)
High BIAS (underfitting)?     → Use BOOSTING (AdaBoost, GBM)
Not sure?                     → Try both, compare with cross-val!
```

[↑ Back to Top](#-ensemble-boosting--adaboost-deep-dive-theory)

---

## 3️⃣ ADABOOST — The Big Picture

### 👶 Easy Story

Imagine a school test. After Test 1, the teacher looks at which questions students got WRONG. For Test 2, those hard questions are given DOUBLE marks — so students MUST pay extra attention to them. After Test 2, the teacher again increases marks for whatever is STILL wrong. After 10 tests, the teacher combines all tests, but gives MORE weight to the tests where the teacher was a good marker.

That's AdaBoost:
- Each "test" = a weak learner (decision stump)
- "Hard questions getting more marks" = increasing sample weights for misclassified points
- "Good marker gets more say" = higher α (amount of say) for accurate classifiers

### Formal Definition

**AdaBoost** (Adaptive Boosting) iteratively trains weak classifiers (typically decision stumps). After each round, it:
1. **Increases** the weight of misclassified examples
2. **Decreases** the weight of correctly classified examples
3. Assigns an **"amount of say"** (α) to each classifier based on its accuracy
4. The final prediction is a **weighted vote** of all classifiers

```
ADABOOST AT A GLANCE:
──────────────────────────────────────────────────
INPUT:   Training set {(x₁,y₁), ..., (xₙ,yₙ)}, T rounds
OUTPUT:  Strong classifier H(x) = sign(Σ αₜ·hₜ(x))

LOOP for t = 1, 2, ..., T:
   Step 1: Train weak learner hₜ using current weights
   Step 2: Compute total error rₜ = Σ wᵢ [hₜ(xᵢ) ≠ yᵢ] / Σ wᵢ
   Step 3: Compute amount of say αₜ = ½ · ln((1-rₜ)/rₜ)
   Step 4: Update weights:
           - Misclassified: wᵢ ← wᵢ × exp(+αₜ)
           - Correctly classified: wᵢ ← wᵢ × exp(-αₜ)
   Step 5: Normalize weights so they sum to 1

FINAL: H(x) = sign( α₁·h₁(x) + α₂·h₂(x) + ... + αT·hT(x) )
```

[↑ Back to Top](#-ensemble-boosting--adaboost-deep-dive-theory)

---

## 4️⃣ DECISION STUMPS

### 👶 Easy Story

A decision stump is the SIMPLEST possible tree — it asks exactly ONE question and makes a decision. Like asking "Is the patient's chest pain present? Yes → Heart disease. No → Healthy." That's it! One question, two answers. Super simple, super weak, but many together = super strong!

### Formal Definition

A **decision stump** is a decision tree with **depth = 1** (one split only). It picks the ONE best feature and the ONE best threshold to split the data.

```
DECISION STUMP:

       [Chest Pain?]          ← only 1 feature, 1 question
          /    \
        Yes     No
        /         \
  [Heart Disease]  [Healthy]   ← 2 leaves, that's it!

COMPARE TO FULL TREE:

       [Chest Pain?]
          /    \
        Yes     No
        /         \
  [Blood Pressure?]  [Age?]    ← deeper, more questions
      /   \          /   \
    High   Low    >60   ≤60
     ...   ...    ...   ...

Decision stump = ONE level = max_depth=1
It's a "weak learner" — barely better than random
But AdaBoost makes 100s of them → STRONG together!
```

### Why Stumps for AdaBoost?

```
REASON 1: Simple → low variance → won't overfit one tree
REASON 2: Fast → trains in O(n·d) per feature
REASON 3: Each stump captures ONE pattern
          100 stumps = 100 different patterns!
REASON 4: AdaBoost theory works best with weak learners
          (models slightly better than random guessing)
```

[↑ Back to Top](#-ensemble-boosting--adaboost-deep-dive-theory)

---

## 5️⃣ AMOUNT OF SAY (α)

### 👶 Easy Story

Imagine 5 friends giving you movie recommendations. Your friend who ALWAYS picks good movies gets a LOUD voice (high "say"). Your friend who picks 50-50 good/bad movies gets NO voice (zero "say"). Your friend who ALWAYS picks bad movies? You listen but do the OPPOSITE (negative "say")!

### Formal Definition

The **amount of say** (α) tells us how much to trust each weak learner in the final vote.

```
FORMULA:
─────────────────────────────────────────
   αₜ = ½ × ln( (1 - rₜ) / rₜ )

   where rₜ = weighted error rate (0 to 1)

   (some versions use η as learning rate: αₜ = η × ln((1-rₜ)/rₜ))
─────────────────────────────────────────

WHAT HAPPENS:

   Error rₜ    │  αₜ (amount of say)  │ Meaning
   ─────────────┼──────────────────────┼─────────────────────
   0.0 (perfect)│  +∞ (huge positive)  │ Trust completely!
   0.1 (great)  │  +1.10               │ Strong voice
   0.2 (good)   │  +0.69               │ Good voice
   0.3 (ok)     │  +0.42               │ Some voice
   0.4 (meh)    │  +0.20               │ Weak voice
   0.5 (random) │  0.00                │ Ignored! (coin flip)
   0.6 (bad)    │  -0.20               │ Flip predictions!
   0.8 (awful)  │  -0.69               │ Strong opposite!
   1.0 (always  │  -∞                  │ Always do opposite!
        wrong)  │                      │
```

### Text Diagram: α vs Error

```
   α (amount of say)
   │
   │  * (r=0.01, α=2.3)   ← perfect clf, huge say
   │
   │    * (r=0.1, α=1.1)  ← great clf
   │
   │       * (r=0.2)
   │
   │          * (r=0.3)
   │
 0 │─────────────* (r=0.5) ← random, IGNORED
   │            * (r=0.6)  ← worse than random, FLIP!
   │          * (r=0.7)
   │        * (r=0.8)
   │
   └──────────────────────→ Error rate (r)
   0                     1
```

[↑ Back to Top](#-ensemble-boosting--adaboost-deep-dive-theory)

---

## 6️⃣ SAMPLE WEIGHT UPDATES

### 👶 Easy Story

After a spelling test, the teacher says: "The words you got WRONG, I'm writing them 3 times bigger on the blackboard. The words you got RIGHT, I'm writing them tiny. Next test, you HAVE to focus on the big words!" That's exactly how AdaBoost updates weights!

### Formal Definition

After training each weak learner, AdaBoost adjusts the importance (weight) of each training example:

```
WEIGHT UPDATE RULES:
───────────────────────────────────────────────────────────
MISCLASSIFIED (got it wrong):
   new_wᵢ = old_wᵢ × exp(+αₜ)     ← INCREASE weight
   (exp(+α) > 1, so weight goes UP)

CORRECTLY CLASSIFIED (got it right):
   new_wᵢ = old_wᵢ × exp(-αₜ)     ← DECREASE weight
   (exp(-α) < 1, so weight goes DOWN)

NORMALIZE:
   wᵢ = wᵢ / (sum of all weights)  ← make them add up to 1
───────────────────────────────────────────────────────────

WHY?
- Wrong answers get heavier → next learner MUST focus on them
- Right answers get lighter → don't waste time on easy stuff
- This is what makes it "ADAPTIVE" → adapts to mistakes!
```

### Text Diagram: Weight Flow

```
Round 1: All weights equal
  w = [0.2, 0.2, 0.2, 0.2, 0.2]   (5 samples, equal)
       ✓    ✓    ✗    ✓    ✗       (✗ = wrong)

After update (say α=0.5):
  ✓ points: 0.2 × exp(-0.5) = 0.2 × 0.607 = 0.121
  ✗ points: 0.2 × exp(+0.5) = 0.2 × 1.649 = 0.330

Before normalize: [0.121, 0.121, 0.330, 0.121, 0.330]
Sum = 1.023
After normalize:  [0.118, 0.118, 0.323, 0.118, 0.323]
                                  ^^^^          ^^^^
                          Wrong points now have BIGGER weight!
                          Next learner MUST get these right!
```

[↑ Back to Top](#-ensemble-boosting--adaboost-deep-dive-theory)

---

## 7️⃣ ADABOOST FULL WALKTHROUGH

### The Complete Pipeline (All Steps Together)

```
ADABOOST PIPELINE — FROM START TO FINISH
═══════════════════════════════════════════════════════════

SETUP:
  n samples, each gets weight wᵢ = 1/n
  Choose T = number of rounds (e.g., 200)
  Choose base learner = Decision Stump (max_depth=1)

FOR EACH ROUND t = 1, 2, ..., T:
─────────────────────────────────────────────────────────
  STEP 1: FIND BEST STUMP
  ├── For each feature f:
  │     For each threshold θ:
  │       Compute weighted error = Σ wᵢ × [hₜ(xᵢ) ≠ yᵢ]
  │     Pick threshold with lowest weighted error
  │   Pick feature with lowest weighted error
  └── This gives us hₜ (the best stump for this round)

  STEP 2: COMPUTE ERROR
  ├── rₜ = (sum of weights of WRONG points) / (sum of ALL weights)
  ├── If rₜ = 0 → perfect! Stop early.
  └── If rₜ ≥ 0.5 → worse than random! Stop or restart.

  STEP 3: COMPUTE AMOUNT OF SAY
  └── αₜ = ½ × ln((1 - rₜ) / rₜ)

  STEP 4: UPDATE WEIGHTS
  ├── For each sample i:
  │     If WRONG:  wᵢ ← wᵢ × exp(+αₜ)
  │     If RIGHT:  wᵢ ← wᵢ × exp(-αₜ)
  └── Normalize: wᵢ ← wᵢ / Σwⱼ

FINAL CLASSIFIER:
─────────────────────────────────────────────────────────
  H(x) = sign( α₁·h₁(x) + α₂·h₂(x) + ... + αT·hT(x) )

  For classification:
    If weighted sum > 0 → Class +1
    If weighted sum < 0 → Class -1
═══════════════════════════════════════════════════════════
```

### Example: Chest Pain Classifier (from lecture)

```
FEATURE: Chest Pain (Yes/No)
LABELS:  Heart Disease (+1) or Healthy (-1)

DATA:
┌────────┬────────────┬─────────┬──────────────┐
│ Patient│ Chest Pain │  Label  │ Initial wᵢ   │
├────────┼────────────┼─────────┼──────────────┤
│   1    │    Yes     │   +1    │   1/8=0.125  │
│   2    │    Yes     │   +1    │   0.125      │
│   3    │    Yes     │   +1    │   0.125      │
│   4    │    No      │   -1    │   0.125      │
│   5    │    No      │   -1    │   0.125      │─────
│   6    │    Yes     │   -1    │   0.125  ← tricky! │
│   7    │    No      │   +1    │   0.125  ← tricky! │
│   8    │    No      │   -1    │   0.125      │─────
└────────┴────────────┴─────────┴──────────────┘

STUMP: "Chest Pain = Yes → +1, No → -1"
  Wrong on: Patient 6 (Yes but -1) and Patient 7 (No but +1)
  Error = (0.125 + 0.125) / 1.0 = 0.25

  α = ½ × ln((1-0.25)/0.25) = ½ × ln(3) = ½ × 1.099 = 0.549

  HIGH α → this stump has a STRONG say because error is low!
```

[↑ Back to Top](#-ensemble-boosting--adaboost-deep-dive-theory)

---

## 8️⃣ MODEL SELECTION — Picking the Right Tool

### 👶 Easy Story

You want to go from home to school. Should you walk, ride a bicycle, take a bus, or fly a helicopter? It depends on the DISTANCE, the ROAD, and the WEATHER! Similarly, picking a machine learning model depends on your DATA, your PROBLEM, and your GOALS.

### Formal Discussion (from lecture)

The lecture used a **traffic / shortest route** problem to illustrate model selection:

```
PROBLEM FORMULATION IS KEY:
═══════════════════════════════════════════════════════════
  Step 1: DEFINE the problem clearly
          "Find shortest route considering traffic"
          → Is this classification? Regression? Optimization?

  Step 2: UNDERSTAND the data
          → How many features? What type? Missing values?
          → How much data? (100 samples vs 1M samples)

  Step 3: CONSIDER the algorithm
          → Linear problem? → Linear Regression, SVM
          → Non-linear? → Decision Tree, RF, Neural Network
          → Clustering? → K-Means, GMM
          → Sequence? → RNN, LSTM

  Step 4: No Free Lunch Theorem!
          "No single algorithm works best for ALL problems."
          → Always try multiple models and compare!
═══════════════════════════════════════════════════════════
```

### Model Selection Cheat Sheet

```
PROBLEM TYPE → TRY THESE FIRST
────────────────────────────────────────────────────
Classification (few features):   Logistic Regression, SVM
Classification (many features):  Random Forest, XGBoost
Regression:                      Linear Reg, RF Regressor, GBM
Clustering:                      K-Means, GMM, DBSCAN
Anomaly Detection:               Isolation Forest, One-Class SVM
Sequence Data:                   LSTM, GRU, Transformer
Image Data:                      CNN
Text Data:                       BERT, Transformer

ALWAYS ASK:
  1. How much data do I have?
  2. Is it labeled? (supervised vs unsupervised)
  3. Do I need interpretability? (tree > neural net)
  4. What's my latency/speed requirement?
  5. Similarity function: Euclidean? Cosine? Domain-specific?
```

[↑ Back to Top](#-ensemble-boosting--adaboost-deep-dive-theory)

---

## 9️⃣ GAUSSIAN MIXTURE MODELS (GMM) — Introduction

### 👶 Easy Story

K-Means says: "Each point belongs to ONE cluster, period." GMM says: "Well, this point is 70% likely in Cluster A and 30% in Cluster B." GMM is the SOFT, GENTLE version of K-Means — it uses PROBABILITIES instead of hard assignments!

### Formal Introduction

**GMM** models data as a mixture of K Gaussian (bell-curve) distributions. Each data point has a **probability** of belonging to each cluster.

```
GMM MODEL:
───────────────────────────────────────────────────
  P(x) = Σ(k=1 to K) πₖ · N(x | μₖ, Σₖ)

  Where:
    K    = number of Gaussian components (clusters)
    πₖ   = mixing coefficient (weight of cluster k)
           Σ πₖ = 1, all πₖ > 0
    μₖ   = mean of cluster k (centre)
    Σₖ   = covariance matrix of cluster k (shape)
    N()  = Gaussian/Normal distribution

  TRAINED USING: EM (Expectation-Maximization) Algorithm
  → E-step: compute probability each point belongs to each cluster
  → M-step: update μₖ, Σₖ, πₖ using those probabilities
  → Repeat until convergence
───────────────────────────────────────────────────
```

### K-Means vs GMM

```
┌────────────────────┬────────────────────┬────────────────────┐
│ Feature            │ K-Means            │ GMM                │
├────────────────────┼────────────────────┼────────────────────┤
│ Assignment         │ Hard (0 or 1)      │ Soft (probability) │
│ Cluster shape      │ Spherical only     │ Any elliptical     │
│ Algorithm          │ Lloyd's iterations │ EM algorithm       │
│ Parameters         │ Just μₖ            │ μₖ, Σₖ, πₖ           │
│ Handles overlap?   │ Poorly             │ Well               │
│ Speed              │ Faster             │ Slower             │
│ Output             │ Cluster label      │ P(cluster|point)   │
└────────────────────┴────────────────────┴────────────────────┘

NOTE: Next lecture will cover EM algorithm steps, how to compute
the probabilities, and how to update the parameters in detail.
```

[↑ Back to Top](#-ensemble-boosting--adaboost-deep-dive-theory)

---

## 🃏 CHEAT SHEET

```
┌────────────────────────────────────────────────────────────────────┐
│                    ENSEMBLE BOOSTING CHEAT SHEET                   │
├──────────────────┬─────────────────────────────────────────────────┤
│ Bagging          │ Parallel, bootstrap samples, reduces VARIANCE   │
│ Boosting         │ Sequential, fixes mistakes, reduces BIAS        │
│ AdaBoost error   │ rₜ = Σw_wrong / Σw_all                           │
│ Amount of say    │ αₜ = ½ × ln((1-rₜ)/rₜ)                            │
│ Weight (wrong)   │ wᵢ × exp(+αₜ)  → gets BIGGER                     │
│ Weight (right)   │ wᵢ × exp(-αₜ)  → gets SMALLER                    │
│ Final prediction │ H(x) = sign(Σ αₜ·hₜ(x))                          │
│ Decision stump   │ max_depth=1, one split, one feature             │
│ OOB              │ ~36.8% unseen per bag → free validation         │
│ Random Forest    │ Bagging + random feature subset at each split   │
│ GMM              │ Soft clustering via Gaussian distributions      │
│ GMM formula      │ P(x) = Σ πₖ·N(x|μₖ,Σₖ)                           │
│ EM Algorithm     │ E-step (compute probs) + M-step (update params) │
│ No Free Lunch    │ No single best algorithm for all problems       │
└──────────────────┴─────────────────────────────────────────────────┘
```

---

## 🧪 EXAM HACKS

```
💡 "Bagging vs Boosting difference?" → Parallel vs Sequential,
    Variance vs Bias. That's the 2-sentence answer.
💡 AdaBoost uses DECISION STUMPS (depth=1) as weak learners.
💡 α = ½·ln((1-r)/r). If error=0.5 → α=0 → classifier IGNORED.
💡 If error > 0.5 → α is NEGATIVE → flip the predictions!
💡 Weight update: WRONG → multiply by exp(+α) → BIGGER.
    RIGHT → multiply by exp(-α) → SMALLER. Always normalize after.
💡 Final prediction = SIGN of weighted sum of all stumps.
💡 GMM = "soft K-Means" → gives PROBABILITIES, not hard labels.
💡 GMM uses EM algorithm. K-Means uses Lloyd's algorithm.
💡 GMM can model ELLIPTICAL clusters. K-Means only SPHERICAL.
💡 "Which model should I use?" → No Free Lunch! Try multiple, compare.
💡 Problem formulation > algorithm selection. Define problem FIRST.
💡 AdaBoost can overfit if T (rounds) is too large on noisy data.
💡 Learning rate (η) shrinks α → slower learning, often better.
💡 In exam: draw the stump, show error calc, show α calc, show
    weight update. These 4 steps = full marks for AdaBoost question.
```

---

## 🔗 Connection to Ch7 (Géron) Material

```
WHAT'S NEW vs WHAT WAS IN Ch7:
────────────────────────────────────────────────────────────
Ch7 (Géron):                   This Lecture (Pr S Bhagat):
────────────────────────────────────────────────────────────
Covered AdaBoost algorithm     Deep-dive into decision stumps
Covered formula for α          Chest pain example walkthrough
Covered GBM in detail          Model selection discussion
Covered Stacking               GMM introduction (new topic!)
sklearn code focus             More formula/theory focus
────────────────────────────────────────────────────────────
RECOMMENDATION: Read Ch7 theory first, then this lecture.
This lecture REINFORCES Ch7 and ADDS model selection + GMM.
```

---

> **Nav:** [← INDEX](ml_ensemble_boosting_adaboost_index.md) | 📖 THEORY | [🔢 NUMERICAL →](ml_ensemble_boosting_adaboost_numerical.md) | [💻 PRACTICE →](ml_ensemble_boosting_adaboost_practice.md)

[↑ Back to Top](#-ensemble-boosting--adaboost-deep-dive-theory)

---

*AI · ML · github.com/rpaut03l/TS-01-Pvt*
