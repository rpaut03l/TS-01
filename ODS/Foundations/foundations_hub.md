# 🏗️ Foundations — Hub
> **Course:** ODS · AI

| File | Contents |
|------|----------|
| **foundations_hub.md** | You are here — overview & quick recap |
| [foundations_theory.md](./foundations_theory.md) | Fermat's Rule, Convexity, Lipschitz Gradient, Strong Convexity, Optimality Conditions |
| [foundations_numericals.md](./foundations_numericals.md) | Convexity checks, critical point classification, PD/PSD tests, solved problems |
| [foundations_practice.md](./foundations_practice.md) | MCQs, fill-blanks, unsolved problems, answers, checklist |

## ⚡ 60-Second Recap
```
FERMAT'S RULE:    f'(x*)=0  at local extremum (necessary, NOT sufficient)
1ST ORDER COND:   ∇f(x*)=0
2ND ORDER COND:   ∇f(x*)=0 AND ∇²f(x*)≻0  →  strict local minimum
CONVEXITY (def):  f(θx+(1-θ)y) ≤ θf(x)+(1-θ)f(y)   θ∈[0,1]
CONVEXITY (1st):  f(y) ≥ f(x) + ∇f(x)ᵀ(y-x)
CONVEXITY (2nd):  ∇²f(x) ⪰ 0  for all x
STRONG CONV:      f(y) ≥ f(x) + ∇f(x)ᵀ(y-x) + (μ/2)‖y-x‖²  (μ>0)
LIPSCHITZ GRAD:   ‖∇f(x)-∇f(y)‖ ≤ L‖x-y‖
```

## 🔗 Navigation
[← ODS Hub](../ods_hub.md) · [🔝 Top](#️-foundations--hub) · [Theory →](./foundations_theory.md)
