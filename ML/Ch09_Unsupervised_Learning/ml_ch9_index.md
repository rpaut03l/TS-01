# 📑 Ch9 — Unsupervised Learning: INDEX
### *Hands-On ML (Aurélien Géron, 3rd Ed.) · Chapter 9*

> 🔗 **Part of:** [github.com/rpaut03l/TS-01](https://github.com/rpaut03l/TS-01) · ML Track

---

## 🗺️ File Map

```
ML/Ch09_Unsupervised_Learning/
  ├── INDEX.md      ← START HERE
  ├── THEORY.md     ← concepts, diagrams, cheat sheet, exam hacks
  ├── NUMERICAL.md  ← formulas first, then 7 solved problems
  └── PRACTICE.md   ← all 13 book exercises + full Colab code
```

---

## ⚡ Quick Links

| File | What's inside | Time |
|------|--------------|------|
| [📖 THEORY](./ml_ch9_theory.md) | K-Means/DBSCAN/GMM/Anomaly/BIC | 20 min |
| [🔢 NUMERICAL](./ml_ch9_numerical.md) | All formulas upfront + 7 worked problems | 25 min |
| [💻 PRACTICE](./ml_ch9_practice.md) | Q1-Q13 + full Olivetti faces lab code | 2-3 hrs |

---

## 🧠 Topic → File Mapping

```
Topic                  Theory   Numerical  Practice
─────────────────────────────────────────────────────
Clustering definition  §1       —          Q1, Q2
K-Means algorithm      §2       P1         Q3, Q10
Selecting K            §2       P5         Q3
Label propagation      §3       —          Q4, Q11
DBSCAN                 §4       —          Q5
GMM                    §5       P3, P4     Q8, Q9, Q12
Anomaly vs Novelty     §6       P7         Q7, Q13
BIC/AIC                §7       P6         Q12
```

---

## 🃏 One-Page Summary

```
Algorithm     Pick K?  Shape      Soft?  Anomaly?     sklearn
──────────────────────────────────────────────────────────────
K-Means       ✅ Yes   Spherical  ❌     Partial      KMeans
DBSCAN        ❌ Auto  Any        ❌     ✅ (label=-1) DBSCAN
Agglomerative ✅ Yes   Any        ❌     ❌           AgglomerativeClustering
GMM           ✅ Yes   Ellipse    ✅     ✅ score_samp GaussianMixture
```

---
* AI · ML · github.com/rpaut03l/TS-01*
