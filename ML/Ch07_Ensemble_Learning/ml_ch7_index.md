# 📑 Ch7 — Ensemble Learning: INDEX
### *Hands-On ML (Aurélien Géron, 3rd Ed.) · Chapter 7*

> 🔗 **Part of:** [github.com/rpaut03l/TS-01](https://github.com/rpaut03l/TS-01) · ML Track

---

## 🗺️ File Map

```
ML/Ch07_Ensemble_Learning/
  ├── INDEX.md      ← START HERE
  ├── THEORY.md     ← concepts, diagrams, cheat sheet, exam hacks
  ├── NUMERICAL.md  ← formulas first, then 7 solved problems
  └── PRACTICE.md   ← all 9 book exercises + full Colab code
```

---

## ⚡ Quick Links

| File | What's inside | Time |
|------|--------------|------|
| [📖 THEORY](./ML_Ch7_THEORY.md) | Voting/Bagging/RF/AdaBoost/GBM/Stacking | 20 min |
| [🔢 NUMERICAL](./ML_Ch7_NUMERICAL.md) | All formulas upfront + 7 worked problems | 20 min |
| [💻 PRACTICE](./ML_Ch7_PRACTICE.md) | Q1-Q9 answered + MNIST voting+stacking code | 1-2 hrs |

---

## 🧠 Topic → File Mapping

```
Topic                  Theory   Numerical  Practice
─────────────────────────────────────────────────────
Voting (hard/soft)     §2       P6         Q1, Q2
Bagging + OOB          §3       P5         Q3, Q4
Random Forest          §4       P7         Q8
Extra-Trees            §5       —          Q5
AdaBoost               §6       P2, P3     Q6
Gradient Boosting      §7       P4         Q7
Stacking               §9       —          Q9
```

---

## 🃏 One-Page Summary

```
Method         Parallel?  Reduces    sklearn class
──────────────────────────────────────────────────
Voting         ✅         Both       VotingClassifier
Bagging        ✅         Variance   BaggingClassifier
Random Forest  ✅         Variance   RandomForestClassifier
Extra-Trees    ✅ faster  Variance   ExtraTreesClassifier
AdaBoost       ❌ seq     Bias       AdaBoostClassifier
Gradient Boost ❌ seq     Bias       GradientBoostingClassifier
Stacking       ✅ partial Both       StackingClassifier
```

---

## 🔗 Links in TS-01

- [→ Ch9 Unsupervised Learning](./ML_Ch9_INDEX.md)
- [→ Ch3 Classification](../Ch03/INDEX.md)
- [→ DSA Trees](../../DSA/Trees/INDEX.md)

---
* AI · ML · github.com/rpaut03l/TS-01*
