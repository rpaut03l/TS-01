# Convergence Analysis — Practice
### ODS Topic 06

> **Nav:** [← THEORY](./convergence_analysis_THEORY.md) · [↑ Hub](../ODS_Master_INDEX.md)

---

## P1: Iterations to Accuracy

**Q:** f is L-smooth, µ-strongly convex with L=10, µ=1. How many GD iterations for f(xₖ)-f* ≤ 0.001(f(x₀)-f*)?

```
Rate: (1 - µ/L)ᵏ ≤ 0.001
(1 - 1/10)ᵏ = (0.9)ᵏ ≤ 0.001

k ≥ log(0.001)/log(0.9) = -3/log₁₀(0.9) ≈ -3/(-0.046) ≈ 65.5

Need about 66 iterations. (κ=10, moderate difficulty)
```

## P2: Condition Number Impact

**Q:** Same as P1 but now L=1000, µ=1 (κ=1000). How many iterations?

```
(1 - 1/1000)ᵏ ≤ 0.001
(0.999)ᵏ ≤ 0.001
k ≥ log(0.001)/log(0.999) ≈ 6907 iterations!

Compare: κ=10 → 66 iterations, κ=1000 → 6907 iterations.
This is why condition number matters so much!
```

---

> [← THEORY](./convergence_analysis_THEORY.md) · [↑ Hub](../ODS_Master_INDEX.md)

[Back to Top](#convergence-analysis--practice)
