# 🔢 ML Foundations: NUMERICAL

### *Rules first → then solve. Every step shown.*

> **Nav:** [← INDEX](../ml_master_gap_index.md) | [📖 THEORY](ml_foundations_theory.md) | 🔢 **NUMERICAL** | [💻 PRACTICE →](ml_foundations_practice.md)

---

## 📦 ALL FORMULAS

```
┌─────────────────────────────────────────────────────────────┐
│ MIN-MAX:    x' = (x - x_min) / (x_max - x_min)              │
│ Z-SCORE:    x' = (x - μ) / σ                                │
│ ACCURACY:   (TP+TN) / (TP+TN+FP+FN)                         │
│ PRECISION:  TP / (TP+FP)                                    │
│ RECALL:     TP / (TP+FN)                                    │
│ F1:         2PR / (P+R)                                     │
│ VC SAMPLE:  n ≥ (VC/ε) × ln(1/δ)                            │
│ VC LINEAR:  VC-dim = d + 1 (d = input dimensions)           │
│ TOTAL ERR:  Bias² + Variance + σ²_noise                     │
│ R²:         1 - SS_res / SS_tot                             │
│ MSE:        (1/n) Σ(yᵢ - ŷᵢ)²                               │
│ CV SE:      σ_scores / √K                                   │
└─────────────────────────────────────────────────────────────┘
```

---

## P1: Min-Max + Z-Score Normalization

```
DATA: X = [10, 20, 30, 40, 50]

MIN-MAX (range [0,1]):
  x_min=10, x_max=50, range=40
  10 → (10-10)/40 = 0.000
  20 → (20-10)/40 = 0.250
  30 → (30-10)/40 = 0.500
  40 → (40-10)/40 = 0.750
  50 → (50-10)/40 = 1.000

Z-SCORE (mean=0, std=1):
  μ = (10+20+30+40+50)/5 = 30
  σ² = [(20²+10²+0+10²+20²)]/5 = [400+100+0+100+400]/5 = 200
  σ = √200 = 14.14
  10 → (10-30)/14.14 = -1.414
  20 → (20-30)/14.14 = -0.707
  30 → (30-30)/14.14 =  0.000
  40 → (40-30)/14.14 = +0.707
  50 → (50-30)/14.14 = +1.414
```

[↑ Back to Top](#-ml-foundations-numerical)

---

## P2: VC-Dimension & Sample Complexity

```
Q: Linear classifier in 10D. Need 5% error, 95% confidence. How many samples?

  VC(H) = d + 1 = 10 + 1 = 11
  ε = 0.05, δ = 0.05
  n ≥ (11/0.05) × ln(1/0.05)
    = 220 × ln(20)
    = 220 × 2.996
    = 659 samples (round up: ~660) ✅

Q: Can a line in 2D shatter 4 points?
  VC-dim of line = 2+1 = 3
  3 < 4 → NO, cannot shatter 4 points
  XOR arrangement of 4 points → no line separates all labellings ✅
```

[↑ Back to Top](#-ml-foundations-numerical)

---

## P3: Confusion Matrix Metrics

```
             Predicted
             Cancer  Healthy
  Actual  C  [ 85  |   15  ]   TP=85, FN=15
          H  [  5  |   95  ]   FP=5,  TN=95
  Total = 200

  Accuracy  = (85+95)/200 = 0.900
  Precision = 85/(85+5)   = 85/90  = 0.944
  Recall    = 85/(85+15)  = 85/100 = 0.850
  F1        = 2×(0.944×0.850)/(0.944+0.850)
            = 2×0.802/1.794 = 1.605/1.794 = 0.895

  Specificity = TN/(TN+FP) = 95/100 = 0.950
  FPR = FP/(FP+TN) = 5/100 = 0.050

  NOTE: High Recall is critical for cancer detection
  (missing a cancer patient is worse than false alarm)
```

[↑ Back to Top](#-ml-foundations-numerical)

---

## P4: K-Fold Cross-Validation

```
5-fold CV results: [0.91, 0.87, 0.93, 0.89, 0.90]

  Mean = (0.91+0.87+0.93+0.89+0.90)/5 = 4.50/5 = 0.900
  
  Deviations: [0.01, -0.03, 0.03, -0.01, 0.00]
  Squared:    [0.0001, 0.0009, 0.0009, 0.0001, 0.0000]
  σ² = 0.0020/5 = 0.0004
  σ = √0.0004 = 0.020
  
  SE = σ/√K = 0.020/√5 = 0.020/2.236 = 0.009
  
  Report: 0.900 ± 0.009 (mean ± SE) ✅
```

[↑ Back to Top](#-ml-foundations-numerical)

---

## P5: Bias-Variance Decomposition

```
True function: f(x) = x² at x=2 → f(2) = 4

5 models trained on different data give predictions at x=2:
  ŷ = [3.5, 4.2, 3.8, 4.5, 4.0]

  E[ŷ] = (3.5+4.2+3.8+4.5+4.0)/5 = 20.0/5 = 4.0

  Bias² = (E[ŷ] - f(x))² = (4.0 - 4.0)² = 0.000 ← unbiased!

  Variance = E[(ŷ - E[ŷ])²]
    = [(3.5-4)²+(4.2-4)²+(3.8-4)²+(4.5-4)²+(4.0-4)²]/5
    = [0.25+0.04+0.04+0.25+0.00]/5 = 0.58/5 = 0.116

  If noise σ² = 0.05:
    Total Error = 0.000 + 0.116 + 0.05 = 0.166

  DIAGNOSIS: Bias=0 but Variance=0.116 → HIGH VARIANCE → overfitting!
  FIX: Use bagging (Random Forest) or get more training data.
```

---

> **Nav:** [📖 THEORY](ml_foundations_theory.md) | 🔢 NUMERICAL | [💻 PRACTICE →](ml_foundations_practice.md)

[↑ Back to Top](#-ml-foundations-numerical)

*AI · ML · github.com/rpaut03l/TS-01*
