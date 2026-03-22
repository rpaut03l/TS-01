# Optimization for Data Science (ODS) — Master Study Hub

### AI/ML · Pr. K Som
> **Goal:** Find the BEST answer (minimum/maximum) using math — the engine behind ALL of AI/ML!

---

## 60-Second Overview

```
Imagine you're LOST on a hilly landscape at night. You can only FEEL the slope under
your feet. Your goal: reach the LOWEST valley (minimum loss).

  That's optimization in a nutshell!

  - "Which way is downhill?" → Gradient (∇f)
  - "How fast should I walk?" → Step size (α)
  - "Am I at the bottom?"    → Optimality conditions (∇f = 0)
  - "Any fences I can't cross?" → Constraints (g(x) ≤ 0)

  This ENTIRE course teaches you the BEST ways to walk downhill!
```

---

## Course Structure Map

```
╔══════════════════════════════════════════════════════════════════════╗
║               OPTIMIZATION FOR DATA SCIENCE (MAL7070)                ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  PART 1: UNCONSTRAINED (14 Lectures)                                 ║
║  "No fences — walk freely to find the valley"                        ║
║  ┌─────────┐ ┌──────────┐ ┌──────────┐ ┌───────────┐                 ║
║  │ Convex  │→│Optimality│→│  Line    │→│ Gradient  │                 ║
║  │Sets/Func│ │Conditions│ │ Search   │ │ Descent   │                 ║
║  └─────────┘ └──────────┘ └──────────┘ └─────┬─────┘                 ║
║                                              │                       ║
║  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌────┴──────┐                ║
║  │Conjugate │←│Quasi-    │←│ Newton   │←│SGD/Adam/  │                ║
║  │ Gradient │ │Newton    │ │ Method   │ │Momentum   │                ║
║  └──────────┘ └──────────┘ └──────────┘ └───────────┘                ║
║                                                                      ║
║  PART 2: CONSTRAINED (14 Lectures)                                   ║
║  "Now there ARE fences — optimize inside boundaries"                 ║
║  ┌─────────┐ ┌──────────┐ ┌──────────┐ ┌───────────┐                 ║
║  │Constr.  │→│KKT &     │→│ Linear   │→│Penalty/   │                 ║
║  │Intro    │ │Lagrangian│ │ Prog/    │ │Barrier/   │                 ║
║  │FJ Cond. │ │Duality   │ │ Simplex  │ │Int. Point │                 ║
║  └─────────┘ └──────────┘ └──────────┘ └───────────┘                 ║
║                                                                      ║
║  PRE-REQUISITES (Already in repo)                                    ║
║  ┌─────────┐ ┌──────────┐ ┌──────────┐ ┌───────────┐                 ║
║  │Calculus │ │Linear    │ │Probability│ │Statistics │                ║
║  │BootCamp │ │Algebra   │ │ BootCamp │ │BootCamp  │                  ║
║  └─────────┘ └──────────┘ └──────────┘ └───────────┘                 ║
╚══════════════════════════════════════════════════════════════════════╝
```

---

## Master Table of Contents

### Part 1: Unconstrained Optimization

| # | Topic | Index | Theory | Practice | Lectures | AI/ML Use |
|---|-------|-------|--------|----------|----------|-----------|
| 01 | Convex Sets & Functions | [HUB](./01-Convex-Sets-and-Functions/convex_sets_functions_INDEX.md) | [THEORY](./01-Convex-Sets-and-Functions/convex_sets_functions_THEORY.md) | [PRACTICE](./01-Convex-Sets-and-Functions/convex_sets_functions_PRACTICE.md) | L1-L2 | Loss functions, SVM |
| 02 | Optimality Conditions | [HUB](./02-Optimality-Conditions/optimality_conditions_INDEX.md) | [THEORY](./02-Optimality-Conditions/optimality_conditions_THEORY.md) | [PRACTICE](./02-Optimality-Conditions/optimality_conditions_PRACTICE.md) | L2 | Training convergence |
| 03 | Least Squares / Linear Regression | [HUB](./03-Least-Squares-Linear-Regression/least_squares_INDEX.md) | [THEORY](./03-Least-Squares-Linear-Regression/least_squares_THEORY.md) | [PRACTICE](./03-Least-Squares-Linear-Regression/least_squares_PRACTICE.md) | L3 | Regression models |
| 04 | Line Search Methods | [HUB](./04-Line-Search-Methods/line_search_INDEX.md) | [THEORY](./04-Line-Search-Methods/line_search_THEORY.md) | [PRACTICE](./04-Line-Search-Methods/line_search_PRACTICE.md) | L3-L5 | Learning rate tuning |
| 05 | Gradient Descent (Steepest) | [HUB](./05-Gradient-Descent/gradient_descent_INDEX.md) | [THEORY](./05-Gradient-Descent/gradient_descent_THEORY.md) | [PRACTICE](./05-Gradient-Descent/gradient_descent_PRACTICE.md) | L3-L6 | Core of deep learning |
| 06 | Convergence Analysis | [HUB](./06-Convergence-Analysis/convergence_analysis_INDEX.md) | [THEORY](./06-Convergence-Analysis/convergence_analysis_THEORY.md) | [PRACTICE](./06-Convergence-Analysis/convergence_analysis_PRACTICE.md) | L6-L7 | When training stops |
| 07 | SGD, Momentum, Adam | [HUB](./07-SGD-and-Variants/sgd_variants_INDEX.md) | [THEORY](./07-SGD-and-Variants/sgd_variants_THEORY.md) | [PRACTICE](./07-SGD-and-Variants/sgd_variants_PRACTICE.md) | L6-L7 | PyTorch optimizers |
| 08 | Newton's Method | [HUB](./08-Newton-Method/newton_method_INDEX.md) | [THEORY](./08-Newton-Method/newton_method_THEORY.md) | [PRACTICE](./08-Newton-Method/newton_method_PRACTICE.md) | L8 | 2nd-order optimization |
| 09 | Quasi-Newton (DFP & BFGS) | [HUB](./09-Quasi-Newton-DFP-BFGS/quasi_newton_INDEX.md) | [THEORY](./09-Quasi-Newton-DFP-BFGS/quasi_newton_THEORY.md) | [PRACTICE](./09-Quasi-Newton-DFP-BFGS/quasi_newton_PRACTICE.md) | L8-L9 | L-BFGS in sklearn |
| 10 | Conjugate Gradient | [HUB](./10-Conjugate-Gradient/conjugate_gradient_INDEX.md) | [THEORY](./10-Conjugate-Gradient/conjugate_gradient_THEORY.md) | [PRACTICE](./10-Conjugate-Gradient/conjugate_gradient_PRACTICE.md) | L8-L9 | Large-scale solvers |

### Part 2: Constrained Optimization

| # | Topic | Index | Theory | Practice | Lectures | AI/ML Use |
|---|-------|-------|--------|----------|----------|-----------|
| 11 | Constrained Opt. Intro | [HUB](./11-Constrained-Optimization-Intro/constrained_intro_INDEX.md) | [THEORY](./11-Constrained-Optimization-Intro/constrained_intro_THEORY.md) | [PRACTICE](./11-Constrained-Optimization-Intro/constrained_intro_PRACTICE.md) | L9-L10 | Regularization |
| 12 | KKT & Lagrangian Duality | [HUB](./12-KKT-and-Lagrangian-Duality/kkt_lagrangian_INDEX.md) | [THEORY](./12-KKT-and-Lagrangian-Duality/kkt_lagrangian_THEORY.md) | [PRACTICE](./12-KKT-and-Lagrangian-Duality/kkt_lagrangian_PRACTICE.md) | L10-L11 | SVM dual, Regularization |
| 13 | Linear Programming & Simplex | [HUB](./13-Linear-Programming-Simplex/lp_simplex_INDEX.md) | [THEORY](./13-Linear-Programming-Simplex/lp_simplex_THEORY.md) | [PRACTICE](./13-Linear-Programming-Simplex/lp_simplex_PRACTICE.md) | L10+ | Resource allocation |
| 14 | Penalty, Barrier & Interior Point | [HUB](./14-Penalty-Barrier-Interior-Point/penalty_barrier_INDEX.md) | [THEORY](./14-Penalty-Barrier-Interior-Point/penalty_barrier_THEORY.md) | [PRACTICE](./14-Penalty-Barrier-Interior-Point/penalty_barrier_PRACTICE.md) | L10+ | Constrained DL |

### Pre-Requisite BootCamps (Already in Repo)

| Topic | Index | Theory | Practice |
|-------|-------|--------|----------|
| Calculus | [HUB](./Calculus/Essence_of_Calculus_INDEX.md) | [THEORY](./Calculus/Essence_of_Calculus_THEORY.md) | [PRACTICE](./Calculus/Essence_of_Calculus_PRACTICE.md) |
| Linear Algebra | [HUB](./Linear-Algebra/Essence_of_Linear_Algebra_INDEX.md) | [THEORY](./Linear-Algebra/Essence_of_Linear_Algebra_THEORY.md) | [PRACTICE](./Linear-Algebra/Essence_of_Linear_Algebra_PRACTICE.md) |
| Probability | [HUB](./Probability/Probability_BootCamp_INDEX.md) | [THEORY](./Probability/Probability_BootCamp_THEORY.md) | [PRACTICE](./Probability/Probability_BootCamp_PRACTICE.md) |
| Statistics | [HUB](./Statistics/Statistics_BootCamp_INDEX.md) | [THEORY](./Statistics/Statistics_BootCamp_THEORY.md) | [PRACTICE](./Statistics/Statistics_BootCamp_PRACTICE.md) |

---

## Notation Dictionary

| Symbol | Name | Meaning | Kid Analogy |
|--------|------|---------|-------------|
| `f(x)` | Objective function | The thing we minimize/maximize | "The score we want lowest" |
| `x*` | Optimal solution | The best answer | "The lowest point in the valley" |
| `∇f(x)` | Gradient | Vector of partial derivatives | "Arrow pointing uphill" |
| `∇²f(x)` or `H` | Hessian | Matrix of 2nd derivatives | "How curvy is the bowl?" |
| `α` or `η` | Step size / Learning rate | How far to walk each step | "Baby steps or giant leaps?" |
| `d` | Descent direction | Which way to walk | "Follow the slope downhill" |
| `S` or `C` | Constraint set | Allowed region | "The fence you can't cross" |
| `L` | Lipschitz constant | Max steepness of gradient | "Steepest hill slope" |
| `µ` | Strong convexity param | Min curvature of bowl | "How deep is the bowl?" |
| `κ = L/µ` | Condition number | Problem difficulty | "Narrow canyon = hard" |
| `λ` | Lagrange multiplier | Price of constraint | "Cost of the fence" |
| `g(x) ≤ 0` | Inequality constraint | Must-satisfy condition | "Rule you can't break" |
| `h(x) = 0` | Equality constraint | Exact condition | "Must land exactly here" |
| `PD / PSD` | Positive Definite / Semidefinite | Matrix property | "Bowl curves UP everywhere" |
| `∥x∥` | Norm | Length of a vector | "How far from zero?" |
| `⟨a,b⟩` | Inner product | Dot product of vectors | "How aligned are a and b?" |

---

## Master Mnemonic Table

| # | Mnemonic | What It Helps Remember | Topic |
|---|----------|----------------------|-------|
| 1 | **CLIFF** | **C**onvex = **L**ine between any 2 points stays **I**nside, **F**unction below line = convex **F**unction | [01](./01-Convex-Sets-and-Functions/convex_sets_functions_THEORY.md) |
| 2 | **FLAT-HILL** | **F**ermat's rule: at min/max, slope is **F**lat. **H**essian **I**ndicates **L**ocal shape, **L**ook at eigenvalues | [02](./02-Optimality-Conditions/optimality_conditions_THEORY.md) |
| 3 | **NORMAL** | **N**ormal equations: X^T X w = X^T y. **O**ptimal weight from **R**esidual **M**inimization via **AL**gebra | [03](./03-Least-Squares-Linear-Regression/least_squares_THEORY.md) |
| 4 | **ARROW-STEP** | Pick **A**rrow (direction), choose **S**tep (size), **T**ake the **E**xact or **P**artial step | [04](./04-Line-Search-Methods/line_search_THEORY.md) |
| 5 | **SLIDE** | **S**teepest descent = **L**earning rate × **I**nverse **D**irection of gradient = **E**asy but zigzags | [05](./05-Gradient-Descent/gradient_descent_THEORY.md) |
| 6 | **FAST-SLOW** | Strong convex = **F**ast (linear), Convex = **S**low (1/k), General = **S**lowest (1/√k) | [06](./06-Convergence-Analysis/convergence_analysis_THEORY.md) |
| 7 | **SAMBA** | **S**GD **A**dam **M**omentum **B**atch **A**dagrad — the optimizer dance party | [07](./07-SGD-and-Variants/sgd_variants_THEORY.md) |
| 8 | **QUADRATIC-KING** | Newton converges in 1 step for **Q**uadratics. **K**ing of speed but expensive (O(n³)) | [08](./08-Newton-Method/newton_method_THEORY.md) |
| 9 | **FAKE-HESSIAN** | DFP/BFGS = **F**ake hessian **A**pproximation via **K**eeping **E**ach step's gradient change | [09](./09-Quasi-Newton-DFP-BFGS/quasi_newton_THEORY.md) |
| 10 | **NO-ZIGZAG** | Conjugate directions = **N**o **O**verlap, each step fixes a new dimension permanently | [10](./10-Conjugate-Gradient/conjugate_gradient_THEORY.md) |
| 11 | **FENCE** | Feasible ∩ Descent = Empty at optimum. Can't go **F**orward AND stay inside the **F**ence | [11](./11-Constrained-Optimization-Intro/constrained_intro_THEORY.md) |
| 12 | **KKT-SLAP** | **S**tationarity, **L**agrange ≥0, **A**ctive complementarity, **P**rimal feasibility | [12](./12-KKT-and-Lagrangian-Duality/kkt_lagrangian_THEORY.md) |
| 13 | **CORNER** | LP solution lives at a **CORNER** (extreme point) of the feasible polytope | [13](./13-Linear-Programming-Simplex/lp_simplex_THEORY.md) |
| 14 | **WALL-LOG** | Barrier = invisible **LOG** wall near boundary. Penalty = **WALL** that hurts when crossed | [14](./14-Penalty-Barrier-Interior-Point/penalty_barrier_THEORY.md) |

---

## Algorithm Comparison Cheatsheet

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║  METHOD           │ DIRECTION d_k        │ COST/ITER │ CONVERGENCE │ MEMORY   ║
╠═══════════════════╪══════════════════════╪═══════════╪═════════════╪══════════╣
║  Gradient Descent │ -∇f(x_k)             │ O(n)      │ Linear*     │ O(n)     ║
║  Newton           │ -[∇²f]⁻¹ ∇f          │ O(n³)     │ Quadratic   │ O(n²)    ║
║  BFGS             │ -H_k ∇f(x_k)         │ O(n²)     │ Superlinear │ O(n²)    ║
║  L-BFGS           │ -H_k ∇f (implicit)   │ O(mn)     │ Superlinear │ O(mn)    ║
║  Conjugate Grad   │ -∇f + β_k p_{k-1}    │ O(n)      │ n steps*    │ O(n)     ║
║  SGD              │ -∇f_i(x_k)           │ O(n/batch)│ O(1/√T)     │ O(n)     ║
║  Adam             │ adaptive per-param   │ O(n)      │ Adaptive    │ O(n)     ║
╠═══════════════════╧══════════════════════╧═══════════╧═════════════╧══════════╣
║  * "Linear" = exponential decay of error for strongly convex functions        ║
║  * CG: exactly n steps for n-dimensional quadratic                            ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

---

## Exam Hacks

```
╔═══════════════════════════════════════════════════════════════════════════╗
║  EXAM HACK #1: "Is it convex?"                                            ║
║  → Check Hessian eigenvalues. ALL ≥ 0? → PSD → Convex!                    ║
║  → For 2×2: trace > 0 AND det > 0 → PD. trace ≥ 0 AND det ≥ 0 → PSD       ║
║                                                                           ║
║  EXAM HACK #2: "Find the minimizer"                                       ║
║  → Set ∇f = 0, solve. Check Hessian PD at that point.                     ║
║  → For least squares: w* = (X^T X)^{-1} X^T y (just memorize!)            ║
║                                                                           ║
║  EXAM HACK #3: "Gradient descent step"                                    ║
║  → x_{k+1} = x_k - α ∇f(x_k). Just plug in and compute.                   ║
║  → Safe α ≤ 1/L where L = largest eigenvalue of Hessian                   ║
║                                                                           ║
║  EXAM HACK #4: "KKT conditions"                                           ║
║  → Write: ∇f + Σ λ_i ∇g_i = 0, λ_i ≥ 0, λ_i g_i = 0, g_i ≤ 0              ║
║  → Complementary slackness: if g_i < 0, then λ_i = 0 (inactive)           ║
║                                                                           ║
║  EXAM HACK #5: "Condition number"                                         ║
║  → κ = λ_max / λ_min.  Small κ = easy. Large κ = slow convergence.        ║
║                                                                           ║
║  EXAM HACK #6: "Convergence rate question"                                ║
║  → General smooth: O(1/√k). Convex+smooth: O(1/k).                        ║
║  → Strongly convex+smooth: O((1-µ/L)^k) = LINEAR rate.                    ║
║  → Newton: QUADRATIC. BFGS: SUPERLINEAR. CG: n steps for quadratic.       ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

---

## AI/ML Connection Map

| ODS Concept | Where in AI/ML | Why It Matters |
|-------------|---------------|----------------|
| Gradient Descent | `optimizer.step()` in PyTorch | Trains every neural network |
| Convexity | Logistic Regression, SVM, Least Squares | Guarantees global optimum |
| Step size α | Learning rate in `Adam(lr=0.001)` | Too big = diverge, too small = slow |
| Newton/Hessian | 2nd-order methods (K-FAC) | Faster convergence in some settings |
| L-BFGS | `scipy.optimize.minimize(method='L-BFGS-B')` | Default optimizer in sklearn |
| SGD + Momentum | `torch.optim.SGD(momentum=0.9)` | Standard for training CNNs |
| Adam | `torch.optim.Adam()` | Default for transformers/LLMs |
| KKT conditions | SVM dual problem | Support vectors = active constraints |
| Ridge/Lasso | Constrained regression | Regularization = optimization constraint |
| Condition number | Batch normalization motivation | Reduces κ for faster training |

---

## Textbooks & References

| # | Book | Authors | Use |
|---|------|---------|-----|
| 1 | Introduction to Nonlinear Optimization | Amir Beck | Primary textbook |
| 2 | Nonlinear Programming: Theory and Algorithms | Bazaraa, Sherali, Shetty | Reference |
| 3 | Convex Optimization | Boyd & Vandenberghe | Classic reference |
| 4 | Linear and Nonlinear Programming | Luenberger & Ye | Operations Research angle |
| 5 | Algorithms for Optimization | Kochenderfer & Wheeler | MIT Press, code examples |

---

> **Start Learning:** Pick Topic 01 → [Convex Sets & Functions](./01-Convex-Sets-and-Functions/convex_sets_functions_INDEX.md)
>
> **Already know basics?** Jump to → [Gradient Descent](./05-Gradient-Descent/gradient_descent_INDEX.md) | [Newton](./08-Newton-Method/newton_method_INDEX.md) | [KKT](./12-KKT-and-Lagrangian-Duality/kkt_lagrangian_INDEX.md)
>
> **Pre-requisites:** [Calculus](./Calculus/Essence_of_Calculus_INDEX.md) | [Linear Algebra](./Linear-Algebra/Essence_of_Linear_Algebra_INDEX.md)

[Back to Top](#optimization-for-data-science-mal7070--master-study-hub)
