# 📋 Bayesian Network Inference — Master INDEX
### Artificial Intelligence · AI
### Book: Norvig | Unit: Probabilistic Reasoning — Part 2

---

```
┌──────────────────────────────────────────────────────────────────┐
│                  HOW THESE 3 FILES CONNECT                       │
│                                                                  │
│   BN_Inference_INDEX.md  ←── YOU ARE HERE                        │
│         │                                                        │
│         ├──→  BN_Inference_THEORY.md                             │
│         │          All concepts, rules, formulas,                │
│         │          text diagrams, mnemonics, cheatsheet          │
│         │                                                        │
│         ├──→  BN_Inference_NUMERICALS.md                         │
│         │          Every problem fully solved,                   │
│         │          step-by-step with tables                      │
│         │                                                        │
│         └──→  BN_Inference_PRACTICE.md                           │
│                    Python code, exam hacks,                      │
│                    graded problems, self-test Q&A                │
└──────────────────────────────────────────────────────────────────┘
```

---

## 📂 File Navigation

| File | Lines | What's Inside |
|------|-------|--------------|
| 📋 **INDEX** *(you are here)* | — | Topic map, notation dict, 60-sec revision card, quick links |
| 📘 [THEORY](./bn_inference_theory.md) | ~750 | All concepts kid-style, formulas, diagrams, mnemonics, cheatsheet |
| 🔢 [NUMERICALS](./bn_inference_numericals.md) | ~600 | 8 fully solved problems with all working shown |
| 💻 [PRACTICE](./bn_inference_practice.md) | ~500 | Python code, graded problems, exam hacks, self-test |

---

## 🗺️ Topic Map — Everything in This Module

```
BAYESIAN NETWORK INFERENCE
│
├── 1. THREE VARIABLE TYPES
│       ├── X  = Query variable     (what you WANT)
│       ├── e  = Evidence           (what you KNOW)
│       └── Y  = Hidden variables   (SUM over all values!)
│
├── 2. MASTER INFERENCE FORMULA
│       └── P(X|e) = α × Σ P(X,e,y)
│                          y
│
├── 3. ALPHA α — NORMALIZATION CONSTANT
│       ├── What it is: α = 1/P(e) = 1/(sum of unnorm values)
│       ├── Why it exists: avoids computing P(e) separately
│       ├── How to use: compute P(X=T,e) and P(X=F,e), divide by total
│       └── Slide example: 0.192 and 0.224 → 0.4615 and 0.5385
│
├── 4. FULL POSTERIOR INFERENCE — ENUMERATION
│       ├── P(B|j,m) — complete 8-world calculation
│       ├── CPT lookup for every world
│       ├── Marginalize over Alarm + Earthquake
│       └── Final: P(B=T|j,m) = 0.284 (jumped 284× from prior!)
│
├── 5. VARIABLE ELIMINATION — EXACT INFERENCE
│       ├── Core idea: compute once, save as factor, reuse
│       ├── Two Golden Rules: pull out constants from sums
│       ├── Factor f(b,e): inner a-sum computed ONCE for all 4 combos
│       ├── Outer e-sum: uses saved factors
│       └── Savings: 32 ops → 14 ops = 56% fewer (grows to ~100% for n=30!)
│
└── 6. ALGORITHM COMPARISON
        ├── Exact: Enumeration vs Variable Elimination
        └── Approximate: Prior Sampling, Rejection, LW, Gibbs
```

---

## 📖 Notation Dictionary — Every Symbol Used

```
Symbol     Name                        Meaning
─────────────────────────────────────────────────────────────────────
P(X)       Marginal Probability        How likely is X alone?
P(X, Y)    Joint Probability           Both X AND Y happen together
P(X | Y)   Conditional Probability     X given Y has happened
Σ          Sigma (Sum)                 Add up all listed values
∏          Pi (Product)                Multiply all listed values
α          Alpha                       Normalisation constant = 1/P(e)
⊥⊥         Independence                No direct connection in the graph
¬          NOT / Negation              The complement / opposite
∧          AND                         Both true
∨          OR                          At least one true
∈          Belongs to                  Is one of these options
X          Query variable              What you're computing P(?) for
e          Evidence (observed)         Known/fixed observed values
Y / y      Hidden variable             Unknown — sum over ALL values!
f(b,e)     Factor                      Pre-computed, saved inner sum (VE)
n          Node count                  Total number of BN variables
parents    Parent set                  Direct cause-nodes of a variable
posterior  Updated belief              P(X|e) — after seeing evidence
prior      Initial belief              P(X) — before seeing evidence
```

---

## 🔑 60-Second Revision Card

```
╔══════════════════════════════════════════════════════════════════╗
║               INFERENCE ESSENTIALS                               ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  IDENTIFY FIRST:  X (want) · e (know) · Y (sum over)             ║
║                                                                  ║
║  FORMULA:  P(X|e) = α × Σ P(X, e, y)                             ║
║                           y                                      ║
║                                                                  ║
║  EXPAND:   P(j,m,a,b,e) = P(j|a)·P(m|a)·P(a|b,e)·P(b)·P(e)       ║
║                                                                  ║
║  ALPHA:    α = 1/(P(X=T,e) + P(X=F,e))   ← sum = 1/α!            ║
║                                                                  ║
║  VE TRICK: P(b)×Σe P(e)×[Σa P(a|b,e)·P(j|a)·P(m|a)]              ║
║            P(b) = constant → pull out first                      ║
║            f(b,e) = inner a-sum → compute ONCE per (b,e) pair    ║
║                                                                  ║
║  KEY RESULT:                                                     ║
║  P(B=T | John=T, Mary=T) = 0.284  ← jumped 284× from 0.001!      ║
║  But still only 28.4% — rare events stay rare!                   ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## 🧠 Master Mnemonic Collection

```
"XEY"  — Variable types in inference
  X = what you want (query)
  E = what you know (evidence)
  Y = hidden — sum over everY value!

"ALPHA" — What α does
  A = Always same for all X values (compute once!)
  L = 1 / (sum of aLL unnorm values)
  P = Probabilities must sum to 1 — α ensures this
  H = Hides P(e) computation (no extra work!)
  A = Apply by multiplying each unnorm value × α

"SAVE" — Variable Elimination steps
  S = Spot what depends on what
  A = Arrange nested sums (inner → outer)
  V = pull out constants and Variables that don't belong
  E = Evaluate inner sum → save as factor, rEuse!

"REEF" — When to pull constants outside sums
  R = Read each term carefully
  E = Every term that lacks the current sum variable
  E = Exits (gets pulled outside)
  F = Factor it out front!

"PEAL" — Parts of the inference formula
  P = P(X,e,y) is the joint
  E = Evidence e is fixed throughout
  A = Alpha normalises at the end
  L = Likelihood from each CPT row
```

---

## 🕸️ The Bruno Network — Quick Reference

```
┌──────────────────────────────────────────────────────────────┐
│                  BURGLAR-ALARM NETWORK                       │
│                                                              │
│   🦹 Burglary (B)         🌍 Earthquake (E)                 │
│   P(B=T) = 0.001          P(E=T) = 0.002                     │
│          \                      /                            │
│           ↓                    ↓                             │
│                🚨 Alarm (A)                                  │
│               /           \                                  │
│              ↓              ↓                                │
│       📞 John (J)     📞 Mary (M)                           │
│                                                              │
│   ALARM CPT:         JOHN CPT:    MARY CPT:                  │
│   B  E  P(A)  P(¬A)  A  P(J)     A  P(M)                     │
│   T  T  0.950 0.050  T  0.90     T  0.70                     │
│   T  F  0.940 0.060  F  0.05     F  0.01                     │
│   F  T  0.290 0.710                                          │
│   F  F  0.001 0.999                                          │
│                                                              │
│   CAUSALITY FLOW →  B,E → A → J,M                            │
│   INFERENCE  FLOW ← J,M → A → B,E  (detective direction!)    │
└──────────────────────────────────────────────────────────────┘
```

---

## ⚡ Quick Navigation by Goal

```
"I need to understand α from scratch"
  → THEORY.md  §3 — Normalization Constant α

"I need P(B|j,m) solved step by step"
  → NUMERICALS.md  Problem 2 — Full Enumeration

"I need Variable Elimination worked example"
  → NUMERICALS.md  Problem 3 — VE with factor table

"Exam in 1 hour — give me essentials"
  → PRACTICE.md  §1 Cheatsheet + §2 Exam Hacks

"I want to run the code"
  → PRACTICE.md  §5, §6, §7 — Python scripts
```


---

## 🗓️ Suggested Study Order

```
First time reading:
  INDEX (this file) → THEORY → NUMERICALS → PRACTICE

Solving an exam problem:
  NUMERICALS checklist → verify with THEORY formulas

Quick revision day-before:
  INDEX 60-sec card → PRACTICE cheatsheet → NUMERICALS answers table
```

---

**📂 GitHub Path:** `TS-01/AI/SD-M/Bayesian-Network-(BN)-Inference`

> **Navigation:** 📋 **INDEX** *(you are here)* | [📘 THEORY →](./bn_inference_theory.md) | [🔢 NUMERICALS →](./bn_inference_numericals.md) | [💻 PRACTICE →](./bn_inference_practice.md)
>
> **Course:** AI 

[🔝 Back to Top](#-bayesian-network-inference--master-index)
