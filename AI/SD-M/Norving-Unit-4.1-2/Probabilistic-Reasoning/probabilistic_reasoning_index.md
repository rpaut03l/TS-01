# 📋 Probabilistic Reasoning — Master INDEX
### Artificial Intelligence · AI
### (SDM) | Book: Norvig - Units 4.1 + 4.2

---

```
    ┌──────────────────────────────────────────────────────────────────┐
    │              HOW ALL FILES CONNECT                               │
    │                                                                  │
    │             ┌──────────────┐                                     │
    │             │  📋 INDEX    │  ← YOU ARE HERE                     │
    │             │  (This File) │                                     │
    │             └──────┬───────┘                                     │
    │                    │                                             │
    │           ┌────────┴────────┐                                    │
    │           ▼                 ▼                                    │
    │    ┌──────────────┐  ┌──────────────┐                            │
    │    │  📘 THEORY   │  │🔢 NUMERICALS │                            │
    │    │  Concepts +  │◄►│ Step-by-step │                            │
    │    │  Diagrams +  │  │  Solved +    │                            │
    │    │  Mnemonics   │  │  Practice    │                            │
    │    └──────┬───────┘  └──────┬───────┘                            │
    │           ▲                  ▲                                   │
    │           │   Cross-links    │                                   │
    │           └────────┬─────────┘                                   │
    │                    │                                             │
    │                    ▼  DEEP DIVE                                  │
    │    ┌─────────────────────────────────────────────┐               │
    │    │  🧠 BN INFERENCE (Separate Folder)          │               │
    │    │  AI/SD-M/Bayesian-Network-(BN)-Inference/   │               │
    │    │  ├── bn_inference_index.md                  │               │
    │    │  ├── bn_inference_theory.md                 │               │
    │    │  ├── bn_inference_numericals.md             │               │
    │    │  └── bn_inference_practice.md               │               │
    │    └─────────────────────────────────────────────┘               │
    │                                                                  │
    │    Sections 9-16 here LINK to BN Inference for deep coverage     │
    └──────────────────────────────────────────────────────────────────┘
```

---

## 🧠 THE GOLDEN RULE

```
╔══════════════════════════════════════════════════════════════════════╗
║   THE REAL WORLD IS MESSY. WE CAN'T KNOW EVERYTHING.                 ║
║   PROBABILITY = A NUMBER BETWEEN 0 AND 1 THAT SAYS                   ║
║   "HOW SURE AM I?" ABOUT SOMETHING.                                  ║
║                                                                      ║
║   Bayesian Network = A SMART SHORTCUT to avoid storing               ║
║   a GIANT table of every possible combination.                       ║
║                                                                      ║
║   Every formula here answers: "Given what I already know,            ║
║   how likely is THIS thing?"                                         ║
╚══════════════════════════════════════════════════════════════════════╝
```

---

## 📚 What's Covered (Source PDFs)

| PDF | Unit | What's Inside (In Simple Words) |
|-----|------|---------------|
| `AI-1_Quantifying_Uncertainty_4_1_SDM.pdf` | 4.1 | Why can't we be 100% sure?, How probability works, Bayes' rule (flipping questions around), Big tables of all possibilities, When things don't affect each other, Naive Bayes |
| `AI-1_Probabilistic_Reasoning_4_2_Partial_SDM.pdf` | 4.2 | Bayesian Networks (smart graphs that replace giant tables), Small tables called CPTs, Markov Blanket (a node's "protective bubble"), How to answer questions using BNs (Enumeration = try everything, Variable Elimination = be smart about it) |

---

## 🗺️ Complete Topic Map

```
UNIT 4: PROBABILISTIC REASONING
│
├── 4.1 QUANTIFYING UNCERTAINTY (= "How to put a number on doubt")
│   ├── 1. Why Uncertainty? (We're lazy, ignorant, or don't have all info)
│   ├── 2. Basic Probability
│   │   ├── Sample Space (Ω) = bag of ALL possible things that could happen
│   │   ├── Probability Model = give each thing a number (0 to 1)
│   │   ├── Random Variable = a question with many possible answers
│   │   ├── Prior = belief BEFORE seeing anything
│   │   │   Posterior = belief AFTER seeing evidence
│   │   └── Joint Distribution = big table of ALL combos
│   ├── 3. Probability Rules (your 3 power tools!)
│   │   ├── "Given": P(a|b) = P(a AND b) / P(b)
│   │   ├── "AND": P(a AND b) = P(a|b) × P(b)
│   │   ├── "OR": P(a OR b) = P(a) + P(b) - P(a AND b)
│   │   └── "NOT": P(not a) = 1 - P(a)
│   ├── 4. Bayes' Rule = FLIP the question around!
│   │   ├── P(cause|effect) = P(effect|cause) × P(cause) / P(effect)
│   │   └── Chain Rule = keep breaking AND into pieces
│   ├── 5. Getting Answers from the Big Table
│   │   ├── Marginalization = add up rows to get simpler answers
│   │   └── Conditioning = split the question into cases
│   ├── 6. Independence = "these two things don't affect each other"
│   ├── 7. Conditional Independence = "they don't affect each other IF I know this third thing"
│   └── 8. Naive Bayes = one cause → many independent effects
│
└── 4.2 PROBABILISTIC REASONING (= "Smart graphs instead of giant tables")
    ├── 1. Why BNs? (Giant table has 2^n rows... too many!)
    ├── 2. BN Syntax = Draw a picture: circles + arrows, no loops
    ├── 3. BN Semantics
    │   ├── CPTs = small tables at each node
    │   ├── Giant table needs O(2^n) rows, BN needs only O(n·2^m) — way less!
    │   └── Handy trick: P(NOT A|B) = 1 - P(A|B)
    ├── 4. Markov Blanket = a node's "bubble": Parents + Children + Kids' other parents
    ├── 5. Recreating the big table: multiply all CPTs together
    ├── 6. Answering Questions (Inference)
    │   ├── Query = what you're asking
    │   ├── Evidence = what you already know
    │   ├── Hidden = what you DON'T know (sum over these)
    │   ├── α trick = skip computing P(evidence), just normalize at the end!
    │   ├── Enumeration = try EVERY combo (correct but slow)
    │   └── Variable Elimination = be smart, reuse work (fast!)
    └── 7. Approximate Inference (just know the names for now)
        ├── Prior Sampling, Rejection Sampling
        ├── Likelihood Weighting
        └── Gibbs Sampling
```

---

## 🔗 Quick Jump Links

### 📘 THEORY File — [Open Theory Guide](./probabilistic_reasoning_theory.md)

| # | Topic (Simple Explanation) | Direct Link |
|---|-------|-------------|
| 1 | Why can't we be 100% sure about anything? | [Theory §1](./probabilistic_reasoning_theory.md#1-why-uncertainty--the-problem) |
| 2 | Sample space, events, random variables — the building blocks | [Theory §2](./probabilistic_reasoning_theory.md#2-basic-probability-terms) |
| 3 | The 3 power-tool rules (AND, OR, NOT, Given) | [Theory §3](./probabilistic_reasoning_theory.md#3-probability-axioms--rules) |
| 4 | Bayes' Rule — flip the question around! | [Theory §4](./probabilistic_reasoning_theory.md#4-bayes-rule) |
| 5 | How to get answers from one giant table | [Theory §5](./probabilistic_reasoning_theory.md#5-inference-using-full-joint-distribution) |
| 6 | Independence — "they don't affect each other" | [Theory §6](./probabilistic_reasoning_theory.md#6-independence) |
| 7 | Conditional Independence — "they don't affect each other IF I know Z" | [Theory §7](./probabilistic_reasoning_theory.md#7-conditional-independence) |
| 8 | Naive Bayes — one cause, many effects | [Theory §8](./probabilistic_reasoning_theory.md#8-naive-bayes-model) |
| 9 | Bayesian Networks — draw it as a picture! | [Theory §9](./probabilistic_reasoning_theory.md#9-bayesian-networks--syntax) |
| 10 | CPTs — the small tables at each node | [Theory §10](./probabilistic_reasoning_theory.md#10-bn-semantics--cpts) |
| 11 | Markov Blanket — a node's protective bubble | [Theory §11](./probabilistic_reasoning_theory.md#11-markov-blanket) |
| 12 | How to rebuild the big table from the small ones | [Theory §12](./probabilistic_reasoning_theory.md#12-obtaining-full-joint-from-bn) |
| 13 | Inference — what's the question, what do I know, what's hidden? | [Theory §13](./probabilistic_reasoning_theory.md#13-inference--formal-definition) |
| 14 | The α trick — skip hard work, just normalize! | [Theory §14](./probabilistic_reasoning_theory.md#14-normalization-constant-α) |
| 15 | Enumeration — try every combo (slow but correct) | [Theory §15](./probabilistic_reasoning_theory.md#15-exact-inference--enumeration) |
| 16 | Variable Elimination — reuse work, go fast! | [Theory §16](./probabilistic_reasoning_theory.md#16-exact-inference--variable-elimination) |
| 17 | Approximate methods — just know the names | [Theory §17](./probabilistic_reasoning_theory.md#17-approximate-inference-overview) |

### 🔢 NUMERICALS File — [Open Numericals Guide](./probabilistic_reasoning_numericals.md)

| # | Problem (What You'll Solve) | Direct Link |
|---|---------|-------------|
| 1 | Weather + Traffic: practice AND, OR, NOT, Given rules | [Num §1](./probabilistic_reasoning_numericals.md#problem-1-weather-traffic-axioms) |
| 2 | Toothache + Cavity: pull answers from a big table | [Num §2](./probabilistic_reasoning_numericals.md#problem-2-toothache-cavity-catch-joint-table) |
| 3 | Produce + Weather: use conditioning to find P(good produce) | [Num §3](./probabilistic_reasoning_numericals.md#problem-3-produce-weather-conditioning) |
| 4 | Burglary Alarm: build a Bayesian Network from scratch | [Num §4](./probabilistic_reasoning_numericals.md#problem-4-burglary-alarm-bn-construction) |
| 5 | What's the chance John calls? | [Num §5](./probabilistic_reasoning_numericals.md#problem-5-pjohncalls--true) |
| 6 | What's the chance Mary does NOT call? | [Num §6](./probabilistic_reasoning_numericals.md#problem-6-pmarycalls--false) |
| 7 | Calculate one specific row of the big table using BN | [Num §7](./probabilistic_reasoning_numericals.md#problem-7-joint-entry-pjma¬b¬e) |
| 8 | "Was there a burglary?" — solve by Enumeration (slow way) | [Num §8](./probabilistic_reasoning_numericals.md#problem-8-pburglary--jm--enumeration) |
| 9 | Same question — solve by Variable Elimination (fast way!) | [Num §9](./probabilistic_reasoning_numericals.md#problem-9-pb--jm--variable-elimination) |
| 10 | Homework: P(john calls AND earthquake) etc. | [Num §10](./probabilistic_reasoning_numericals.md#problem-10-homework-problems) |
| 11 | Cavity with OR evidence — uses the α normalization trick | [Num §11](./probabilistic_reasoning_numericals.md#problem-11-pcavity--toothache--catch) |

### 🧠 BN INFERENCE Deep Dive — [Open BN Inference Folder](../SD-M/Bayesian-Network-(BN)-Inference/bn_inference_index.md)

> **Want to go deeper on Bayesian Networks?** Sections 9–17 above are covered in much more detail in these dedicated guides — more theory, more solved problems, and practice problems you can try yourself!

| File | What's Inside (Simple) | Direct Link |
|------|--------------|-------------|
| 📋 BN Index | Starting point — links to everything BN-related | [bn_inference_index.md](../SD-M/Bayesian-Network-(BN)-Inference/bn_inference_index.md) |
| 📘 BN Theory | How to build BNs, read CPTs, do inference — explained in full detail | [bn_inference_theory.md](../SD-M/Bayesian-Network-(BN)-Inference/bn_inference_theory.md) |
| 🔢 BN Numericals | More solved problems with every step shown | [bn_inference_numericals.md](../SD-M/Bayesian-Network-(BN)-Inference/bn_inference_numericals.md) |
| 🏋️ BN Practice | Try these yourself! Problems with hints but no answers | [bn_inference_practice.md](../SD-M/Bayesian-Network-(BN)-Inference/bn_inference_practice.md) |

---

## 📝 Notation Dictionary (What Do All These Symbols Mean?)

```
SYMBOL          WHAT IT MEANS (in simple words)              EXAMPLE
──────────────────────────────────────────────────────────────────────
Ω               The bag of ALL possible things               {(1,1),(1,2),...,(6,6)}
ω               ONE specific thing from the bag              (3,4)
P(ω)            How likely is that one thing?                1/36
φ               A group of things you care about             "dice sum = 11"
P(a)            How likely is a? (before seeing anything)    P(cavity) = 0.2
P(a|b)          How likely is a, NOW THAT I KNOW b?          P(cavity|toothache)
P(a∧b)          How likely are BOTH a AND b together?        P(cavity AND toothache)
P(a∨b)          How likely is a OR b (or both)?              P(cavity OR toothache)
P(¬a)           How likely is NOT a?                         1 - P(a)
P(X)            All probabilities of X listed out            P(Weather) = <0.6,0.1,0.29,0.01>
Σ               Add up a bunch of things                     Σ P(ω) = 1
Π               Multiply a bunch of things together          Π P(Xi|parents)
α               The "normalize" trick number                 = 1/P(evidence)
⫫               "is independent of"                          a ⫫ b
X ⫫ Y | Z      "X and Y are independent IF I know Z"       Toothache ⫫ Catch | Cavity
DAG             A graph with arrows and NO loops             The BN picture
CPT             The small table at each node                 P(Alarm|Burglary,Earthquake)
parents(Xi)     The nodes that point INTO Xi                 parents(Alarm) = {Burglary, Earthquake}
f(X)            A "factor" = a vector of probabilities       f4(A) = <0.90, 0.05>
```

---

## ⚡ 60-Second Revision Card

```
┌──────────────────────────────────────────────────────────┐
│  WHY PROBABILITY?                                        │
│  Logic says YES/NO. Real world says MAYBE (0 to 1).      │
│  Three enemies: Laziness + Ignorance + Partial Info      │
│                                                          │
│  CORE RULES:                                             │
│  • P(a|b) = P(a∧b)/P(b)          ...definition           │
│  • P(a∧b) = P(a|b)·P(b)          ...product rule         │
│  • P(a∨b) = P(a)+P(b)-P(a∧b)    ...inclusion-exclusion   │
│  • P(¬a) = 1 - P(a)              ...complement           │
│  • Bayes: P(b|a) = P(a|b)P(b)/P(a)                       │
│                                                          │
│  INFERENCE TOOLS:                                        │
│  • Marginalization: P(X) = Σ_y P(X,y)                    │
│  • Conditioning: P(X) = Σ_y P(X|y)P(y)                   │
│                                                          │
│  BAYESIAN NETWORK:                                       │
│  • DAG where nodes=variables, arrows=cause→effect        │
│  • Each node has CPT: P(Xi|parents(Xi))                  │
│  • Joint = Π P(Xi|parents(Xi))                           │
│  • Way cheaper than full joint table!                    │
│  • Full Joint: O(2^n) vs BN CPTs: O(n·2^m)               │
│                                                          │
│  INFERENCE IN BN:                                        │
│  • P(X|e) = α · Σ_y P(X,e,y)                             │
│  • α = 1/P(e) = normalization constant                   │
│  • Enumeration: expand all combos (expensive)            │
│  • Variable Elimination: factor out, sum smartly (cheap) │
│                                                          │
│  MARKOV BLANKET of X:                                    │
│  = Parents + Children + Children's other Parents         │
│  Given MB, X is independent of ALL other nodes!          │
└──────────────────────────────────────────────────────────┘
```

---

## 🧩 Memory Tricks (Mnemonics)

| Say This | To Remember This |
|----------|----------------------|
| **LIP** = Laziness, Ignorance, Practical ignorance | Why logic fails: we're Lazy, Ignorant, or missing info |
| **PPC** = Product, Plus-minus, Complement | Your 3 power-tool rules: AND, OR, NOT |
| **BAIL** = Bayes = (A given B) × prior / evidence | How Bayes' formula is structured |
| **MC** = Marginalize, Condition | The 2 ways to get answers from a big table |
| **DAG-CPT** = Directed Acyclic Graph + Conditional Probability Tables | A Bayesian Network = picture + small tables |
| **PCK** = Parents, Children, Kids'-parents | What's in a Markov Blanket (the "bubble") |
| **NODE** = effects dowN, causes elevatEd | When writing the product, effects come first |
| **FAVE** = Factors, Assign, Variable-sum-out, Evaluate | Steps of Variable Elimination |

---

## 🏗️ The Burglary Network — Reference Diagram

```
              P(B)=0.001          P(E)=0.002
             ┌────────┐           ┌────────┐
             │Burglary│           │Earthqu.│
             └───┬────┘           └───┬────┘
                 │                    │
                 └────────┬───────────┘
                          ▼
                    ┌──────────┐
                    │  Alarm   │  P(A|B,E)
                    └────┬─────┘
                    ╱         ╲
                   ▼           ▼
            ┌──────────┐  ┌──────────┐
            │JohnCalls │  │MaryCalls │
            └──────────┘  └──────────┘
             P(J|A)        P(M|A)

   CPT Values:
   ┌────┬────┬───────┬────────┐
   │ B  │ E  │ P(a)  │ P(¬a)  │
   ├────┼────┼───────┼────────┤
   │ t  │ t  │ 0.95  │ 0.05   │
   │ t  │ f  │ 0.94  │ 0.06   │
   │ f  │ t  │ 0.29  │ 0.71   │
   │ f  │ f  │ 0.001 │ 0.999  │
   └────┴────┴───────┴────────┘

   P(j|a)=0.90  P(j|¬a)=0.05
   P(m|a)=0.70  P(m|¬a)=0.01
```

---

## 📂 GitHub Upload Path

```
TS-01/
└── AI/
    ├── Probabilistic-Reasoning/
    │   ├── probabilistic_reasoning_index.md        ← This file
    │   ├── probabilistic_reasoning_theory.md       ← Concepts + Diagrams
    │   └── probabilistic_reasoning_numericals.md   ← Solved Problems
    │
    └── SD-M/
        └── Bayesian-Network-(BN)-Inference/        ← DEEP DIVE (linked)
            ├── bn_inference_index.md
            ├── bn_inference_theory.md
            ├── bn_inference_numericals.md
            └── bn_inference_practice.md
```

---

## 🔗 Related Topics in Repository

| Topic | Path | Connection |
|-------|------|-----------|
| **🧠 BN Inference (Deep Dive)** | [`AI/SD-M/Bayesian-Network-(BN)-Inference/`](../SD-M/Bayesian-Network-(BN)-Inference/bn_inference_index.md) | **Extended coverage of §9-17: BN construction, inference algorithms, more solved problems & practice** |

---

> **Files:** [📘 THEORY](./probabilistic_reasoning_theory.md) | [🔢 NUMERICALS](./probabilistic_reasoning_numericals.md) | [🧠 BN Inference Deep Dive](../SD-M/Bayesian-Network-(BN)-Inference/bn_inference_index.md)
>
> **Source:** (SDM) Slides · AI 
>
> **Ref:** Russell & Norvig — AI: A Modern Approach (Chapter 12-14)

[🔝 Back to Top](#-probabilistic-reasoning--master-index)
