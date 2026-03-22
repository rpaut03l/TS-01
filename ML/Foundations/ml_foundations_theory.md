# 📖 ML Foundations: THEORY + NUMERICAL + PRACTICE

### *Definitions · Paradigms · Normalization · Hypothesis Eval · VC-Dim · Bias-Variance*

> **Nav:** [← ML Master Index](../ml_master_gap_index.md) | **Foundations** | [LDA →](../LDA/ml_lda_theory.md)
>

---

## 🧠 MNEMONIC: **"DND-HVB"**

> **D**efinitions · **N**ormalization · **D**atasets · **H**ypothesis evaluation · **V**C-Dimensions · **B**ias-Variance

---

## 📚 Table of Contents

| # | Topic | Jump |
|---|-------|------|
| 1 | What is ML? | [§1](#1-what-is-machine-learning) |
| 2 | ML Paradigms | [§2](#2-ml-paradigms) |
| 3 | Datasets & Splits | [§3](#3-datasets--splits) |
| 4 | Data Normalization | [§4](#4-data-normalization) |
| 5 | Hypothesis Evaluation | [§5](#5-hypothesis-evaluation) |
| 6 | VC-Dimensions | [§6](#6-vc-dimensions) |
| 7 | Bias-Variance Tradeoff | [§7](#7-bias-variance-tradeoff) |
| 8 | Formulas & Numericals | [§8](#8-formulas--numericals) |
| 9 | Cheat Sheet & Exam Hacks | [§9](#9-cheat-sheet--exam-hacks) |

---

## 1. What is Machine Learning?

### 👶 Easy Story
You show a kid 100 pictures of cats and dogs. You never tell them the "rules" — no formula, no definition of whiskers. But after seeing enough, they LEARN to tell cats from dogs. That's ML: learning patterns from data without being explicitly programmed.

### Tom Mitchell's Definition
> A computer program **learns** from experience **E** with respect to task **T** and performance measure **P**, if its performance at T (measured by P) improves with E.

```
EXAMPLE — Email Spam Filter:
  T (Task):        Classify emails as spam / not-spam
  E (Experience):  Observing 10,000 labeled emails
  P (Performance): % of emails correctly classified

  MORE data (E) → BETTER accuracy (P) → LEARNING!
```

```
ML SYSTEM COMPONENTS:
┌─────────────────────────────────────────────────┐
│ 1. DATA   X = {x₁,...,xₙ}, Y = {y₁,...,yₙ}       │
│ 2. HYPOTHESIS CLASS  H (set of candidate fns)   │
│ 3. LEARNING ALGORITHM (finds best h ∈ H)        │
│ 4. LOSS FUNCTION  L(y, ŷ)  (measures error)     │
│ 5. OPTIMIZER  (gradient descent, closed-form)   │
└─────────────────────────────────────────────────┘
```

[↑ Back to Top](#-ml-foundations-theory--numerical--practice)

---

## 2. ML Paradigms

### 👶 Easy Story
- **Supervised**: Teacher shows you questions AND answers. You learn the pattern.
- **Unsupervised**: No teacher. You sort your toy box by colour yourself.
- **Reinforcement**: You play a game. Win = reward, Lose = penalty. You figure out strategy.

```
┌─────────────────────┬──────────────────────┬────────────────────┐
│ SUPERVISED          │ UNSUPERVISED         │ REINFORCEMENT      │
├─────────────────────┼──────────────────────┼────────────────────┤
│ Labels given ✅     │ No labels ❌         │ Rewards/penalties  │
│ Classification      │ Clustering           │ Policy learning    │
│ Regression          │ Dimensionality red.  │ Agent-environment  │
│ SVM, RF, LR, NN     │ K-Means, PCA, GMM    │ Q-learning, DQN    │
│ Predict y from x    │ Find structure in x  │ Maximize reward    │
└─────────────────────┴──────────────────────┴────────────────────┘

SEMI-SUPERVISED: Few labels + lots of unlabeled data
SELF-SUPERVISED: Create labels from the data itself (masked LM)
```

### Other Paradigms

```
BATCH vs ONLINE:
  Batch:  train on ALL data at once → update model
  Online: train one sample at a time → update model after each

INSTANCE-BASED vs MODEL-BASED:
  Instance-based: store all data, compare at test time (K-NN)
  Model-based:    learn parameters, discard data (Linear Reg)

GENERATIVE vs DISCRIMINATIVE:
  Generative:     models P(x|y) and P(y) → Bayes to get P(y|x)
                  (Naive Bayes, GMM, HMM)
  Discriminative: directly models P(y|x) or decision boundary
                  (Logistic Reg, SVM, NN)
```

[↑ Back to Top](#-ml-foundations-theory--numerical--practice)

---

## 3. Datasets & Splits

```
FULL DATASET
    │
    ├── TRAINING SET (60-80%)     → learn model parameters
    ├── VALIDATION SET (10-20%)   → tune hyperparameters
    └── TEST SET (10-20%)         → final unbiased evaluation

RULE: Test set = NEVER touched during training/tuning!

K-FOLD CROSS-VALIDATION:
  Split data into K folds (typically K=5 or 10)
  For each fold:
    Train on K-1 folds, validate on 1 fold
  Average all K scores → robust estimate

  ┌───┬───┬───┬───┬───┐
  │ 1 │ 2 │ 3 │ 4 │[5]│  ← Fold 5 = validation
  ├───┼───┼───┼───┼───┤
  │ 1 │ 2 │ 3 │[4]│ 5 │  ← Fold 4 = validation
  ├───┼───┼───┼───┼───┤
  │...│   │   │   │   │
  └───┴───┴───┴───┴───┘
  
  SE = σ / √K  (standard error of CV estimate)
```

[↑ Back to Top](#-ml-foundations-theory--numerical--practice)

---

## 4. Data Normalization

### 👶 Easy Story
Imagine comparing height (in cm, range 150-200) with salary (in rupees, range 20000-200000). The salary numbers are SO much bigger that they'll dominate. Normalization = putting everyone on the same scale so no feature bullies others!

```
METHOD 1: MIN-MAX SCALING (range [0,1])
───────────────────────────────────────
  x_norm = (x - x_min) / (x_max - x_min)
  
  Before: [150, 165, 180, 200]
  After:  [0.0, 0.3, 0.6, 1.0]

METHOD 2: Z-SCORE (STANDARDIZATION) (mean=0, std=1)
───────────────────────────────────────
  x_std = (x - μ) / σ
  
  Before: [150, 165, 180, 200]  (μ=173.75, σ=18.43)
  After:  [-1.29, -0.47, 0.34, 1.42]

METHOD 3: ROBUST SCALING (uses median & IQR, outlier-resistant)
───────────────────────────────────────
  x_robust = (x - median) / IQR
  IQR = Q3 - Q1

WHEN TO USE WHAT:
  Min-Max:  when you need bounded range (neural nets, images)
  Z-Score:  when features are Gaussian-ish (SVM, Logistic Reg)
  Robust:   when data has outliers
  NONE:     tree-based models (RF, DT) don't need normalization!
```

[↑ Back to Top](#-ml-foundations-theory--numerical--practice)

---

## 5. Hypothesis Evaluation

```
METRICS FOR CLASSIFICATION:
───────────────────────────
  Accuracy  = (TP + TN) / (TP + TN + FP + FN)
  Precision = TP / (TP + FP)    ← "of predicted +, how many correct?"
  Recall    = TP / (TP + FN)    ← "of actual +, how many found?"
  F1-Score  = 2 × (P × R) / (P + R)   ← harmonic mean

  CONFUSION MATRIX:
                 Predicted
                 +       -
  Actual  +  [ TP  |  FN ]
          -  [ FP  |  TN ]

  ROC CURVE: plot TPR vs FPR at different thresholds
  AUC: area under ROC (1.0 = perfect, 0.5 = random)

METRICS FOR REGRESSION:
───────────────────────
  MSE  = (1/n) Σ (yᵢ - ŷᵢ)²
  RMSE = √MSE
  MAE  = (1/n) Σ |yᵢ - ŷᵢ|
  R²   = 1 - (SS_res / SS_tot)    ← 1.0 = perfect, 0.0 = predicts mean

OVERFITTING DETECTION:
───────────────────────
  Train acc HIGH + Test acc LOW → gap = OVERFITTING
  Train acc LOW  + Test acc LOW → no gap = UNDERFITTING
  Train acc OK   + Test acc OK  → small gap = GOOD FIT
```

[↑ Back to Top](#-ml-foundations-theory--numerical--practice)

---

## 6. VC-Dimensions

### 👶 Easy Story
Imagine you have a ruler (linear classifier). You put 3 dots on paper and try every possible labelling (+++, ++-, +-+, etc.). If your ruler can always separate them correctly for ALL labellings, you can "shatter" 3 points. But with 4 dots in an XOR pattern, NO straight line works. So VC-dim of a line = 3.

### Formal Definition
**VC-Dimension** of hypothesis class H = largest number of points that H can **shatter** (perfectly classify under ALL possible labellings).

```
SHATTERING:
  n points → 2ⁿ possible labellings
  If H can correctly classify ALL 2ⁿ labellings → H shatters n points
  VC(H) = max n such that H can shatter n points

EXAMPLES:
  ┌──────────────────────────────┬────────────┐
  │ Hypothesis Class             │ VC-Dim     │
  ├──────────────────────────────┼────────────┤
  │ Linear clf in d-dimensions   │ d + 1      │
  │ Line in 2D                   │ 3          │
  │ Hyperplane in 3D             │ 4          │
  │ Axis-aligned rectangles 2D   │ 4          │
  │ Circles in 2D                │ 3          │
  │ k-NN (k=1)                   │ ∞          │
  │ Constant function            │ 0 or 1     │
  └──────────────────────────────┴────────────┘

WHY LINEAR IN 2D = VC-DIM 3:
  3 points: can shatter all 2³=8 labellings ✅
  4 points: XOR pattern → NO line can separate ✗

          •(+)     •(-)            •(+)     •(-)
                        → line OK       \     → line OK
          •(-)     •(+)            •(-)  \  •(+)
  
  But XOR:
          •(+)     •(-)
                        → NO line works! ✗
          •(-)     •(+)

SAMPLE COMPLEXITY (how much data you need):
  n ≥ (VC / ε) × ln(1/δ)
  where ε = desired error, δ = failure probability
  
  Example: Linear clf 2D (VC=3), want 1% error (ε=0.01), 95% conf (δ=0.05):
    n ≥ (3/0.01) × ln(20) = 300 × 3 = 900 samples
```

[↑ Back to Top](#-ml-foundations-theory--numerical--practice)

---

## 7. Bias-Variance Tradeoff

### 👶 Easy Story
You're throwing darts at a bullseye:
- **High bias, low variance**: Darts land in a tight cluster, but far from the bullseye (consistently wrong)
- **Low bias, high variance**: Darts are centered on bullseye but scattered everywhere (sometimes right, sometimes very wrong)
- **Sweet spot**: Tight cluster right on the bullseye!

```
TOTAL ERROR = Bias² + Variance + Irreducible Noise

  Bias²    = (E[ŷ] - f(x))²     ← systematic error from wrong assumptions
  Variance = E[(ŷ - E[ŷ])²]     ← how much ŷ changes with different data
  Noise    = σ²                   ← randomness in data, can't reduce

DIAGRAM:
  Error
    ↑
    │  ╲  Bias²                Total Error
    │   ╲    ╱─────────────── ╱
    │    ╲  ╱               ╱
    │     ╲╱  Variance    ╱
    │      ╱╲           ╱──── 
    │     ╱  ╲        ╱
    │    ╱    ╲──────╱
    │   ╱
    └──────────────────────→ Model Complexity
           ↑
       Sweet Spot
    (optimal complexity)

HIGH BIAS (underfitting):   simple model, high train+test error, small gap
HIGH VARIANCE (overfitting): complex model, low train, HIGH test error, BIG gap

FIX UNDERFITTING:  more features, more complex model, less regularization
FIX OVERFITTING:   more data, regularization (L1/L2), dropout, early stopping,
                   simpler model, ensemble (bagging)
```

[↑ Back to Top](#-ml-foundations-theory--numerical--practice)

---

## 8. Formulas & Numericals

### N1: Min-Max Normalization

```
DATA: X = [4, 8, 15, 16, 23, 42]
x_min = 4, x_max = 42, range = 38

  x_norm(4)  = (4 - 4)/38  = 0.000
  x_norm(8)  = (8 - 4)/38  = 0.105
  x_norm(15) = (15 - 4)/38 = 0.289
  x_norm(16) = (16 - 4)/38 = 0.316
  x_norm(23) = (23 - 4)/38 = 0.500
  x_norm(42) = (42 - 4)/38 = 1.000
```

### N2: Z-Score Normalization

```
DATA: X = [4, 8, 15, 16, 23, 42]
μ = (4+8+15+16+23+42)/6 = 108/6 = 18
σ² = [(4-18)²+(8-18)²+(15-18)²+(16-18)²+(23-18)²+(42-18)²]/6
   = [196+100+9+4+25+576]/6 = 910/6 = 151.67
σ = √151.67 = 12.32

  z(4)  = (4-18)/12.32  = -1.136
  z(8)  = (8-18)/12.32  = -0.812
  z(15) = (15-18)/12.32 = -0.244
  z(16) = (16-18)/12.32 = -0.162
  z(23) = (23-18)/12.32 = +0.406
  z(42) = (42-18)/12.32 = +1.948
```

### N3: VC-Dimension Sample Complexity

```
Q: A 5D linear classifier. How many samples for 2% error, 99% confidence?
  VC(H) = d + 1 = 5 + 1 = 6
  ε = 0.02,  δ = 0.01
  n ≥ (6/0.02) × ln(1/0.01) = 300 × 4.605 = 1382 samples
```

### N4: Confusion Matrix Metrics

```
            Predicted
            Spam  Not-Spam
Actual Spam [ 80  |  20  ]   TP=80, FN=20
  Not-Spam  [ 10  |  90  ]   FP=10, TN=90

  Accuracy  = (80+90)/200 = 0.850
  Precision = 80/(80+10)  = 0.889
  Recall    = 80/(80+20)  = 0.800
  F1        = 2×(0.889×0.800)/(0.889+0.800) = 0.842
```

### N5: K-Fold CV

```
Q: 5-fold CV gave accuracies: [0.88, 0.92, 0.86, 0.91, 0.93]
  Mean = (0.88+0.92+0.86+0.91+0.93)/5 = 0.900
  σ = √[Σ(xᵢ - 0.900)²/5] = √[(0.0004+0.0004+0.0016+0.0001+0.0009)/5]
    = √[0.0034/5] = √0.00068 = 0.026
  SE = σ/√K = 0.026/√5 = 0.012
  Report: 0.900 ± 0.012
```

[↑ Back to Top](#-ml-foundations-theory--numerical--practice)

---

## 9. Cheat Sheet & Exam Hacks

```
┌────────────────────────────────────────────────────────────────┐
│               ML FOUNDATIONS CHEAT SHEET                       │
├──────────────────┬─────────────────────────────────────────────┤
│ Mitchell def     │ T, E, P — task, experience, performance     │
│ Supervised       │ Labels given, predict y from x              │
│ Unsupervised     │ No labels, find structure/clusters          │
│ Min-Max          │ (x - min)/(max - min), range [0,1]          │
│ Z-Score          │ (x - μ)/σ, mean=0, std=1                    │
│ VC-dim (linear)  │ d + 1 in d dimensions                       │
│ Shattering       │ correctly classify ALL 2ⁿ labellings        │
│ Bias-Variance    │ Error = Bias² + Variance + Noise            │
│ Overfit fix      │ More data, regularize, simpler model        │
│ Underfit fix     │ More features, complex model, less reg      │
│ K-fold CV        │ Average over K train-test splits            │
│ Precision        │ TP/(TP+FP) — "of predicted +, how many +"   │
│ Recall           │ TP/(TP+FN) — "of actual +, how many found"  │
│ F1               │ 2PR/(P+R) — harmonic mean                   │
│ ROC-AUC          │ TPR vs FPR curve, AUC=1 perfect             │
└──────────────────┴─────────────────────────────────────────────┘

🧪 EXAM HACKS:
💡 "What is ML?" → Tom Mitchell definition + T, E, P example
💡 "Why normalize?" → different scales dominate distance metrics
💡 "VC-dim of line in 2D?" → 3 (can shatter 3, not 4 XOR)
💡 "Bias vs Variance" → draw the dart board analogy + error curve
💡 "Overfit vs Underfit" → check train-test gap
💡 Trees/RF don't need normalization (split-based, not distance-based)
💡 K-fold CV reduces variance of evaluation estimate
💡 Precision vs Recall: P = "when I say positive, am I right?"
   R = "did I find all positives?"
```

---

> **Nav:** [← ML Master Index](../ml_master_gap_index.md) | **Foundations** | [LDA →](../LDA/lda_guide_1.md)

[↑ Back to Top](#-ml-foundations-theory--numerical--practice)

---

*AI · ML · github.com/rpaut03l/TS-01*
