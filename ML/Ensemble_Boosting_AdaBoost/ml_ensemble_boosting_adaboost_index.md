# 📑 Ensemble Boosting & AdaBoost Deep-Dive: INDEX

### *ML Lecture Notes (Pr. S Bhagat) · 22 March 2026*

> 🔗 **Part of:** [github.com/rpaut03l/TS-01-Pvt](https://github.com/rpaut03l/TS-01-Pvt) · ML Track
>
> 🔗 **Related Ch7 (Géron):** [Ch07_Ensemble_Learning](https://github.com/rpaut03l/TS-01/tree/main/ML/Ch07_Ensemble_Learning) · [Ch7 INDEX](https://github.com/rpaut03l/TS-01/blob/main/ML/Ch07_Ensemble_Learning/ml_ch7_index.md)

---

## 🗺️ File Map

```
ML/Ensemble_Boosting_AdaBoost/
  ├── INDEX.md          ← YOU ARE HERE
  ├── THEORY.md         ← concepts, diagrams, cheat sheet, exam hacks
  ├── NUMERICAL.md      ← formulas first, then step-by-step solved problems
  ├── PRACTICE.md       ← coded examples + Colab-ready exercises
  └── ensemble_boosting_adaboost_lab.ipynb  ← Jupyter notebook (kid-friendly)
```

---

## ⚡ Quick Links

| File | What's inside | Time |
|------|---------------|------|
| [📖 THEORY](ml_ensemble_boosting_adaboost_theory.md) | Bagging vs Boosting / AdaBoost / Decision Stumps / Model Selection / GMM Intro | 25 min |
| [🔢 NUMERICAL](ml_ensemble_boosting_adaboost_numerical.md) | All formulas upfront + 6 worked problems (weights, alpha, stumps) | 20 min |
| [💻 PRACTICE](ml_ensemble_boosting_adaboost_practice.md) | Coded walkthroughs + exercises + Colab snippets | 1-2 hrs |

---

## 🧠 Topic → File Mapping

```
Topic                          Theory    Numerical   Practice
──────────────────────────────────────────────────────────────
Ensemble Learning (Why?)       §1        —           Ex1
Bagging vs Boosting            §2        P1          Ex2
AdaBoost Algorithm             §3        P2,P3,P4    Ex3,Ex4
Decision Stumps                §4        P3          Ex4
Amount of Say (α)              §5        P2,P4       Ex3
Sample Weight Updates          §6        P4,P5       Ex5
Model Selection (Traffic eg)   §7        —           Ex6
GMM Introduction               §8        P6          Ex7
```

---

## 🃏 60-Second Recap

```
WHAT WE COVERED TODAY:
─────────────────────────────────────────────────────────────
1. Ensemble = combine many weak models → one strong model
2. Bagging  = train SAME algo on DIFFERENT data (parallel)
3. Boosting = train SAME algo on SAME data but FIX mistakes (sequential)
4. AdaBoost = the KING of boosting:
   - Uses decision stumps (1-level trees)
   - Wrong answers get MORE weight next round
   - Each stump gets an "amount of say" (α)
   - Final answer = weighted vote of all stumps
5. Model selection = match problem → algorithm (no free lunch!)
6. GMM = soft clustering using probability distributions (next lecture)
─────────────────────────────────────────────────────────────
```

---

## 🔗 Cross-References

| This Lecture Links To | Where |
|---|---|
| Bagging / Random Forest / GBM (Géron Ch7) | [Ch7 THEORY §3-§7](https://github.com/rpaut03l/TS-01/blob/main/ML/Ch07_Ensemble_Learning/ml_ch7_theory.md) |
| AdaBoost formulas (Géron Ch7) | [Ch7 NUMERICAL P2-P3](https://github.com/rpaut03l/TS-01/blob/main/ML/Ch07_Ensemble_Learning/ml_ch7_numerical.md) |
| AdaBoost code (Géron Ch7) | [Ch7 PRACTICE Q6](https://github.com/rpaut03l/TS-01/blob/main/ML/Ch07_Ensemble_Learning/ml_ch7_practice.md) |
| Decision Trees (basics) | [ML Decision Trees](https://github.com/rpaut03l/TS-01/tree/main/ML/) |
| K-Means / Clustering | [ML Clustering](https://github.com/rpaut03l/TS-01/tree/main/ML/) |

---

> **Nav:** 📑 INDEX | [📖 THEORY →](ml_ensemble_boosting_adaboost_theory.md) | [🔢 NUMERICAL →](ml_ensemble_boosting_adaboost_numerical.md) | [💻 PRACTICE →](ml_ensemble_boosting_adaboost_practice.md)

[↑ Back to Top](#-ensemble-boosting--adaboost-deep-dive-index)

---

*AI · ML · github.com/rpaut03l/TS-01-Pvt*
