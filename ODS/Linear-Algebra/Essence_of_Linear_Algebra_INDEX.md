# 📐 Essence of Linear Algebra — Master Study Hub
### 🎓 ODS · Mathematics for AI/ML
> **Source:** [3Blue1Brown — Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) by Grant Sanderson
> **Goal:** Understand every concept in ONE read — explained like you're seeing it for the first time!
> **Philosophy:** Think GEOMETRICALLY first, compute NUMERICALLY second 🧠

---

## 📂 Study Materials — Quick Navigation

| # | Document | What's Inside | Link |
|---|----------|--------------|------|
| 📘 | **Theory Guide** | All 16 chapters + 70 Q&A with FULL answers + AI/ML real-world uses + diagrams | **[→ Open Theory Guide](./Essence_of_Linear_Algebra_THEORY.md)** |
| 🔢 | **Practice Problems** | 18+ solved problems — every step, rule, formula, notation explained from scratch | **[→ Open Practice Guide](./Essence_of_Linear_Algebra_PRACTICE.md)** |
| 📋 | **This File (INDEX)** | Master hub, notation dictionary, formula cheat sheet, concept map, mnemonics | **You are here!** |

```
    ┌─────────────────────────────────────────────────────────┐
    │              HOW THESE 3 FILES CONNECT                  │
    │                                                         │
    │            ┌──────────────┐                             │
    │            │  📋 INDEX     │  ← YOU ARE HERE            │
    │            │  (This File)  │                            │
    │            └──────┬───────┘                             │
    │                   │                                     │
    │          ┌────────┴────────┐                            │
    │          ▼                 ▼                            │
    │   ┌──────────────┐  ┌──────────────┐                    │
    │   │  📘 THEORY    │  │  🔢 PRACTICE  │                  │
    │   │  Concepts +   │◄►│  Problems +   │                  │
    │   │  Q&A + AI/ML  │  │  Step-by-step │                  │
    │   └──────────────┘  └──────────────┘                    │
    │         ▲                    ▲                          │
    │         │    Cross-links     │                          │
    │         └────────────────────┘                          │
    │   Every chapter in THEORY links to its PRACTICE         │
    │   Every problem in PRACTICE links back to THEORY        │
    └─────────────────────────────────────────────────────────┘
```

---

## 🧠 THE GOLDEN RULE

```
╔══════════════════════════════════════════════════════════════════╗
║   MATRICES ARE NOT JUST GRIDS OF NUMBERS.                        ║
║   MATRICES ARE TRANSFORMATIONS OF SPACE.                         ║
║   Every time you see a matrix, VISUALIZE what it does to space!  ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## 🗺️ Master Table of Contents (Cross-Linked)

| Ch# | Topic | Theory | Practice | AI/ML Use |
|-----|-------|--------|----------|-----------|
| 0 | Preview — Why Linear Algebra? | [📘](./Essence_of_Linear_Algebra_THEORY.md#chapter-0--preview--why-linear-algebra) | — | Foundation |
| 1 | Vectors | [📘](./Essence_of_Linear_Algebra_THEORY.md#chapter-1--vectors-what-even-are-they) | [🔢 P1-P3](./Essence_of_Linear_Algebra_PRACTICE.md#-p1-vector-addition--scalar-multiplication) | Feature vectors |
| 2 | Span & Basis | [📘](./Essence_of_Linear_Algebra_THEORY.md#chapter-2--linear-combinations-span--basis-vectors) | [🔢 P2-P3](./Essence_of_Linear_Algebra_PRACTICE.md#-p2-linear-independence-test) | Feature selection |
| 3 | Linear Transformations | [📘](./Essence_of_Linear_Algebra_THEORY.md#chapter-3--linear-transformations--matrices) | [🔢 P4](./Essence_of_Linear_Algebra_PRACTICE.md#-p4-matrix-as-transformation) | Neural net layers |
| 4 | Matrix Multiplication | [📘](./Essence_of_Linear_Algebra_THEORY.md#chapter-4--matrix-multiplication-as-composition) | [🔢 P5-P6](./Essence_of_Linear_Algebra_PRACTICE.md#-p5-matrix-multiplication-composition) | Deep networks |
| 5 | 3D Transformations | [📘](./Essence_of_Linear_Algebra_THEORY.md#chapter-5--three-dimensional-linear-transformations) | — | 3D vision |
| 6 | The Determinant | [📘](./Essence_of_Linear_Algebra_THEORY.md#chapter-6--the-determinant) | [🔢 P7](./Essence_of_Linear_Algebra_PRACTICE.md#-p7-determinant-computation--geometric-meaning) | Covariance |
| 7 | Inverse, Column & Null Space | [📘](./Essence_of_Linear_Algebra_THEORY.md#chapter-7--inverse-matrices-column-space--null-space) | [🔢 P8-P9](./Essence_of_Linear_Algebra_PRACTICE.md#-p8-finding-the-inverse-matrix) | Regression |
| 8 | Nonsquare Matrices | [📘](./Essence_of_Linear_Algebra_THEORY.md#chapter-8--nonsquare-matrices-as-transformations-between-dimensions) | — | Embeddings |
| 9 | Dot Products & Duality | [📘](./Essence_of_Linear_Algebra_THEORY.md#chapter-9--dot-products--duality) | [🔢 P10](./Essence_of_Linear_Algebra_PRACTICE.md#-p10-dot-product--projection) | Cosine similarity |
| 10 | Cross Products | [📘](./Essence_of_Linear_Algebra_THEORY.md#chapter-10--cross-products) | [🔢 P11](./Essence_of_Linear_Algebra_PRACTICE.md#-p11-cross-product) | 3D graphics |
| 11 | Cross Products & Transforms | [📘](./Essence_of_Linear_Algebra_THEORY.md#chapter-11--cross-products-in-the-light-of-linear-transformations) | — | Robotics |
| 12 | Cramer's Rule | [📘](./Essence_of_Linear_Algebra_THEORY.md#chapter-12--cramers-rule-explained-geometrically) | [🔢 P12](./Essence_of_Linear_Algebra_PRACTICE.md#-p12-cramers-rule) | System solving |
| 13 | Change of Basis | [📘](./Essence_of_Linear_Algebra_THEORY.md#chapter-13--change-of-basis) | [🔢 P13](./Essence_of_Linear_Algebra_PRACTICE.md#-p13-change-of-basis) | PCA |
| 14 | Eigenvectors & Eigenvalues | [📘](./Essence_of_Linear_Algebra_THEORY.md#chapter-14--eigenvectors--eigenvalues) | [🔢 P14-P15](./Essence_of_Linear_Algebra_PRACTICE.md#-p14-eigenvalues--eigenvectors-full-computation) | PCA, PageRank |
| 15 | Quick Eigenvalue Trick | [📘](./Essence_of_Linear_Algebra_THEORY.md#chapter-15--a-quick-trick-for-computing-eigenvalues) | [🔢 P16](./Essence_of_Linear_Algebra_PRACTICE.md#-p16-mean-product-eigenvalue-trick) | Quick checks |
| 16 | Abstract Vector Spaces | [📘](./Essence_of_Linear_Algebra_THEORY.md#chapter-16--abstract-vector-spaces) | [🔢 P17-P18](./Essence_of_Linear_Algebra_PRACTICE.md#-p17-vector-space-verification) | Kernel methods |

---

## 🔑 Notation Dictionary

| Symbol | Meaning | Kid Analogy | Theory | Practice |
|--------|---------|-------------|--------|----------|
| `v⃗` | Vector | Arrow from origin | [📘 Ch1](./Essence_of_Linear_Algebra_THEORY.md#chapter-1--vectors-what-even-are-they) | [🔢 P1](./Essence_of_Linear_Algebra_PRACTICE.md#-p1-vector-addition--scalar-multiplication) |
| `î, ĵ, k̂` | Basis vectors | "1 step Right/Up/Out" | [📘 Ch2](./Essence_of_Linear_Algebra_THEORY.md#chapter-2--linear-combinations-span--basis-vectors) | [🔢 P4](./Essence_of_Linear_Algebra_PRACTICE.md#-p4-matrix-as-transformation) |
| `A` | Matrix | "Space machine" | [📘 Ch3](./Essence_of_Linear_Algebra_THEORY.md#chapter-3--linear-transformations--matrices) | [🔢 P4](./Essence_of_Linear_Algebra_PRACTICE.md#-p4-matrix-as-transformation) |
| `det(A)` | Determinant | "Rubber sheet stretch" | [📘 Ch6](./Essence_of_Linear_Algebra_THEORY.md#chapter-6--the-determinant) | [🔢 P7](./Essence_of_Linear_Algebra_PRACTICE.md#-p7-determinant-computation--geometric-meaning) |
| `A⁻¹` | Inverse | "Undo button" | [📘 Ch7](./Essence_of_Linear_Algebra_THEORY.md#chapter-7--inverse-matrices-column-space--null-space) | [🔢 P8](./Essence_of_Linear_Algebra_PRACTICE.md#-p8-finding-the-inverse-matrix) |
| `λ` | Eigenvalue | "Stretch factor" | [📘 Ch14](./Essence_of_Linear_Algebra_THEORY.md#chapter-14--eigenvectors--eigenvalues) | [🔢 P14](./Essence_of_Linear_Algebra_PRACTICE.md#-p14-eigenvalues--eigenvectors-full-computation) |
| `v⃗ · w⃗` | Dot product | "How much they agree" | [📘 Ch9](./Essence_of_Linear_Algebra_THEORY.md#chapter-9--dot-products--duality) | [🔢 P10](./Essence_of_Linear_Algebra_PRACTICE.md#-p10-dot-product--projection) |
| `v⃗ × w⃗` | Cross product | "Perpendicular arrow" | [📘 Ch10](./Essence_of_Linear_Algebra_THEORY.md#chapter-10--cross-products) | [🔢 P11](./Essence_of_Linear_Algebra_PRACTICE.md#-p11-cross-product) |

---

## 📋 FORMULA CHEAT SHEET

> 🔗 See derivations → [Theory Guide](./Essence_of_Linear_Algebra_THEORY.md) | See worked examples → [Practice Guide](./Essence_of_Linear_Algebra_PRACTICE.md)

```
╔════════════════════════════════════════════════════════════════════════════╗
║  VECTOR OPS:  v⃗+w⃗ = [v₁+w₁, v₂+w₂]   c·v⃗ = [cv₁, cv₂]                      ║
║  DOT:         v⃗·w⃗ = v₁w₁+v₂w₂ = |v⃗||w⃗|cos(θ)                               ║
║  CROSS:       v⃗×w⃗ = [v₂w₃-v₃w₂, v₃w₁-v₁w₃, v₁w₂-v₂w₁]                      ║
║  DET 2×2:     det([a,b;c,d]) = ad−bc                                       ║
║  DET 3×3:     a(ei−fh) − b(di−fg) + c(dh−eg)                               ║
║  INV 2×2:     A⁻¹ = (1/(ad−bc))·[d,−b;−c,a]                                ║
║  EIGEN:       det(A−λI)=0  |  Quick: λ = m ± √(m²−p)                       ║
║  DIAG:        Aⁿ = P·Dⁿ·P⁻¹                                                ║
║  CRAMER:      x = det(Aₓ)/det(A)                                           ║
║  BASIS:       A_new = P⁻¹·A·P                                              ║
║  RANK-NULL:   rank + nullity = #columns                                    ║
╚════════════════════════════════════════════════════════════════════════════╝
```

---

## 🏆 CONCEPT MAP

```
                                ┌──────────────────┐
                                │   VECTORS (Ch 1)  │
                                └────────┬─────────┘
                        ┌────────────────┼────────────────┐
                        ▼                ▼                ▼
                ┌──────────────┐ ┌─────────────┐  ┌───────────────┐
                │ SPAN/BASIS   │ │ DOT PRODUCT │  │ CROSS PRODUCT │
                │ (Ch 2)       │ │ (Ch 9)      │  │ (Ch 10-11)    │
                └──────┬───────┘ └──────┬──────┘  └───────┬───────┘
                       ▼                │                  │
            ┌──────────────────┐        │                  │
            │ TRANSFORMATIONS  │◄───────┴──────────────────┘
            │ = MATRICES (Ch3) │
            └────┬────┬────────┘
        ┌────────┘    └──────────┐
        ▼                        ▼
 ┌──────────────┐        ┌──────────────┐
 │ COMPOSITION  │        │ DETERMINANT  │
 │ (Ch 4-5)     │        │ (Ch 6)       │
 └──────────────┘        └──────┬───────┘
                  ┌─────────────┼─────────────┐
                  ▼             ▼             ▼
          ┌──────────────┐ ┌────────────┐ ┌──────────────┐
          │ INVERSE/COL/ │ │ CRAMER'S   │ │ EIGEN        │
          │ NULL (Ch 7-8)│ │ (Ch 12)    │ │ (Ch 14-15)   │
          └──────────────┘ └────────────┘ └──────┬───────┘
                              ┌───────────────────┼───────────┐
                              ▼                   ▼           ▼
                      ┌──────────────┐   ┌────────────┐ ┌────────────┐
                      │ CHANGE BASIS │   │ DIAGONAL   │ │ ABSTRACT   │
                      │ (Ch 13)      │   │ A=PDP⁻¹    │ │ SPACES(16) │
                      └──────────────┘   └────────────┘ └────────────┘
```

---

## 🧩 MNEMONICS

| # | Mnemonic | Meaning | Link |
|---|----------|---------|------|
| 1 | **VALS** | Vectors Are Lists with Scaling | [📘](./Essence_of_Linear_Algebra_THEORY.md#chapter-1--vectors-what-even-are-they) |
| 2 | **SLIM** | Span=Linear combos, Independence=Max reach | [📘](./Essence_of_Linear_Algebra_THEORY.md#chapter-2--linear-combinations-span--basis-vectors) |
| 3 | **COLS** | Columns show Output Landing Spots | [📘](./Essence_of_Linear_Algebra_THEORY.md#chapter-3--linear-transformations--matrices) |
| 4 | **READ RIGHT** | Read matrix products Right-to-Left | [📘](./Essence_of_Linear_Algebra_THEORY.md#chapter-4--matrix-multiplication-as-composition) |
| 5 | **DOSE** | Determinant=Output Scaling of Everything | [📘](./Essence_of_Linear_Algebra_THEORY.md#chapter-6--the-determinant) |
| 6 | **COIN** | Col=Outputs, Inverse if Not-squished, Null=dies | [📘](./Essence_of_Linear_Algebra_THEORY.md#chapter-7--inverse-matrices-column-space--null-space) |
| 7 | **DOPPLE** | Dot=Overlap Projection Produces Linear Expression | [📘](./Essence_of_Linear_Algebra_THEORY.md#chapter-9--dot-products--duality) |
| 8 | **CARD** | Cramer's=Area Ratios via Determinants | [📘](./Essence_of_Linear_Algebra_THEORY.md#chapter-12--cramers-rule-explained-geometrically) |
| 9 | **BABEL** | Basis As Bridge: Express in another Language | [📘](./Essence_of_Linear_Algebra_THEORY.md#chapter-13--change-of-basis) |
| 10 | **ELSE** | Eigenvalues: Lambda Scales Eigenvectors | [📘](./Essence_of_Linear_Algebra_THEORY.md#chapter-14--eigenvectors--eigenvalues) |
| 11 | **MPED** | Mean ± √(Mean²−Product) | [📘](./Essence_of_Linear_Algebra_THEORY.md#chapter-15--a-quick-trick-for-computing-eigenvalues) |
| 12 | **FAST** | Functions Are Scaled Things | [📘](./Essence_of_Linear_Algebra_THEORY.md#chapter-16--abstract-vector-spaces) |

---

> 📘 **Start studying:** **[→ Theory Guide](./Essence_of_Linear_Algebra_THEORY.md)** | **[→ Practice Guide](./Essence_of_Linear_Algebra_PRACTICE.md)**
>
> 🎓 **Created for:** ODS
