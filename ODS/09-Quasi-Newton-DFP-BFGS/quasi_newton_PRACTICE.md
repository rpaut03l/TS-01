# Quasi-Newton — Practice
### ODS Topic 09

> **Nav:** [← THEORY](./quasi_newton_THEORY.md) · [↑ Hub](../ODS_Master_INDEX.md)

---

## P1: BFGS Update Step

**Q:** H₀ = I, s₀ = [1, 0]ᵀ, y₀ = [2, 1]ᵀ. Compute H₁ using BFGS.

```
ρ = 1/(y₀ᵀs₀) = 1/([2,1]·[1,0]) = 1/2

V = I - ρ s₀y₀ᵀ = I - (1/2)[1,0][2,1]ᵀ = I - (1/2)[[2,1],[0,0]]
  = [[1,0],[0,1]] - [[1,0.5],[0,0]] = [[0, -0.5],[0, 1]]

H₁ = VᵀH₀V + ρ s₀s₀ᵀ
   = Vᵀ·I·V + (1/2)[[1,0],[0,0]]
   = VᵀV + [[0.5,0],[0,0]]

VᵀV = [[0,0],[-0.5,1]]·[[0,-0.5],[0,1]] = [[0,0],[0,1.25]]

H₁ = [[0,0],[0,1.25]] + [[0.5,0],[0,0]] = [[0.5, 0],[0, 1.25]]
```

---

> [← THEORY](./quasi_newton_THEORY.md) · [↑ Hub](../ODS_Master_INDEX.md)

[Back to Top](#quasi-newton--practice)
