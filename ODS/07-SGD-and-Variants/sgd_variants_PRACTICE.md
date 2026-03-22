# SGD & Variants — Practice
### ODS Topic 07

> **Nav:** [← THEORY](./sgd_variants_THEORY.md) · [↑ Hub](../ODS_Master_INDEX.md)

---

## P1: SGD vs BGD (From Lecture 7)

**Q:** F(w) = (1/2)Σᵢ(aᵢw - bᵢ)² with n=3, a=[1,2,3], b=[2,4,6]. Compare BGD and SGD.

```
Full gradient: ∇F(w) = Σ aᵢ(aᵢw - bᵢ) = (1+4+9)w - (2+8+18) = 14w - 28
w* = 2.

Individual: ∇f₁(w) = 1(w-2), ∇f₂(w) = 2(2w-4) = 4w-8, ∇f₃(w) = 3(3w-6) = 9w-18

BGD at w=0: ∇F(0) = -28 → w₁ = 0 + η·28
SGD pick i=1: ∇f₁(0) = -2 → w₁ = 0 + η·2 (smaller but cheaper!)
SGD pick i=3: ∇f₃(0) = -18 → w₁ = 0 + η·18 (noisier but correct direction!)

All individual gradients point in same direction as full gradient ✓
```

---

> [← THEORY](./sgd_variants_THEORY.md) · [↑ Hub](../ODS_Master_INDEX.md)

[Back to Top](#sgd--variants--practice)
