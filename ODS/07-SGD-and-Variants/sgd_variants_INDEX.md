# SGD, Momentum, Adam & Variants — Topic Hub
### ODS Topic 07 · Lectures 6–7 · Pr K Som

> **Easy Story:** Computing gradients on ALL your data is like reading EVERY book in the library before deciding what to study next. SGD says: just pick ONE random book! It's noisier but SO much faster. Add momentum (remember past directions), and you get Adam — the most popular optimizer in deep learning!

---

## Study Materials

| Doc | Link |
|-----|------|
| THEORY | [→ Theory](./sgd_variants_THEORY.md) |
| PRACTICE | [→ Practice](./sgd_variants_PRACTICE.md) |

---

## Quick Cheatsheet

```
╔══════════════════════════════════════════════════════════════════════╗
║  BATCH GD:    w ← w - (η/n) Σᵢ ∇fᵢ(w)     (uses ALL n samples)       ║
║  SGD:         w ← w - η ∇f_iₜ(w)            (uses 1 random sample)    ║
║  MINI-BATCH:  w ← w - (η/b) Σ_{i∈B} ∇fᵢ(w) (uses batch of b)         ║
║                                                                      ║
║  MOMENTUM:    v ← βv + ∇F(w);  w ← w - ηv   (β≈0.9)                  ║
║  NAG:         v ← βv + η∇F(w-βv); w ← w - v  ("look-ahead")          ║
║                                                                      ║
║  SGD CONVERGENCE: O(1/√T)  (slower per-iter than GD's O(1/T))        ║
║  BUT: each iter costs O(1) vs O(n) → SGD wins for large n!           ║
║                                                                      ║
║  ROBBINS-MONRO: Σηₜ = ∞ and Σηₜ² < ∞  (e.g., ηₜ = 1/t)                 ║
║  VARIANCE: Var(mini-batch gradient) = σ²/b                           ║
╚══════════════════════════════════════════════════════════════════════╝
```

## Mnemonic: SAMBA
- **S**GD: one sample at a time
- **A**dam: adaptive + momentum combined
- **M**omentum: remember past velocity
- **B**atch: use all data (expensive)
- **A**daGrad: adapt LR per parameter

---

> **Prev:** [← 06. Convergence](../06-Convergence-Analysis/convergence_analysis_INDEX.md) · **Next:** [→ 08. Newton](../08-Newton-Method/newton_method_INDEX.md) · [↑ Master Hub](../ODS_Master_INDEX.md)

[Back to Top](#sgd-momentum-adam--variants--topic-hub)
