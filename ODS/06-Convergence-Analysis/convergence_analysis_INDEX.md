# Convergence Analysis — Topic Hub
### ODS Topic 06 · Lectures 6–7 · Pr K Som

> **Easy Story:** How do you know your optimizer is actually getting CLOSER to the answer? And how FAST? Some algorithms are like express trains (quadratic convergence), some like regular trains (linear), and some like walking (sublinear). This topic measures the speed!

---

## Study Materials

| Doc | Link |
|-----|------|
| THEORY | [→ Theory](./convergence_analysis_THEORY.md) |
| PRACTICE | [→ Practice](./convergence_analysis_PRACTICE.md) |

---

## Quick Cheatsheet

```
╔══════════════════════════════════════════════════════════════════════╗
║  CONVERGENCE RATES:                                                  ║
║                                                                      ║
║  Sublinear: error ~ 1/kᵖ          (polynomial decay, SLOW)           ║
║  Linear:    error ~ βᵏ, β<1       (geometric decay, GOOD)            ║
║  Superlinear: ratio → 0            (better than linear)              ║
║  Quadratic: error ~ C·(prev error)² (doubles correct digits!)        ║
║                                                                      ║
║  GD RATES SUMMARY:                                                   ║
║  ┌──────────────────────┬─────────────────┬───────────────────┐      ║
║  │ Assumption           │ Rate            │ To get ε error    │      ║
║  ├──────────────────────┼─────────────────┼───────────────────┤      ║
║  │ L-smooth             │ O(1/√k)         │ O(1/ε²) iters     │      ║
║  │ L-smooth + convex    │ O(1/k)          │ O(1/ε) iters      │      ║
║  │ L-smooth + µ-SC      │ O((1-µ/L)ᵏ)     │ O(κ log(1/ε))     │      ║
║  │ Newton               │ Quadratic       │ O(log log(1/ε))   │      ║
║  │ BFGS                 │ Superlinear     │Between GD & Newton│      ║
║  └──────────────────────┴─────────────────┴───────────────────┘      ║
║                                                                      ║
║  CONDITION NUMBER: κ = L/µ = λ_max/λ_min                             ║
║    κ ≈ 1 → circular contours → fast                                  ║
║    κ >> 1 → elongated ellipse → slow zigzag                          ║
╚══════════════════════════════════════════════════════════════════════╝
```

## Mnemonic: FAST-SLOW
- **F**ast = strongly convex (linear rate, like an express train)
- **S**low = just convex (1/k, like a local train)
- **S**lowest = non-convex (1/√k, like walking)

---

> **Prev:** [← 05. Gradient Descent](../05-Gradient-Descent/gradient_descent_INDEX.md) · **Next:** [→ 07. SGD & Variants](../07-SGD-and-Variants/sgd_variants_INDEX.md) · [↑ Master Hub](../ODS_Master_INDEX.md)

[Back to Top](#convergence-analysis--topic-hub)
