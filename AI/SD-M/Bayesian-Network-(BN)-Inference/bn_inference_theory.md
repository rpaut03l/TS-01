# 📘 Bayesian Network Inference — THEORY
### Artificial Intelligence 
### Book: Norvig | Unit: Probabilistic Reasoning

> **Navigation:** [📋 INDEX](./bn_inference_index.md) | 📘 **THEORY** *(you are here)* | [🔢 NUMERICALS →](./bn_inference_numericals.md) | [💻 PRACTICE →](./bn_inference_practice.md)

---

## 📚 Table of Contents

| # | Section | What's In It |
|---|---------|-------------|
| 1 | [The Bruno Network — Full Setup](#1-the-bruno-network--full-setup) | Network, all CPT tables, chain rule |
| 2 | [Three Variable Types](#2-three-variable-types) | Query X, Evidence e, Hidden Y — identify first! |
| 3 | [Three Tools of Inference](#3-three-tools-of-inference) | Marginalization, Conditioning, Independence |
| 4 | [Master Inference Formula](#4-master-inference-formula) | P(X\|e) = α Σ P(X,e,y) — the one formula |
| 5 | [Alpha α — Normalization Constant](#5-alpha---normalization-constant) | Easy story, derivation, visual, why it's clever |
| 6 | [Full Posterior Inference — Enumeration](#6-full-posterior-inference--enumeration) | Recipe, expansion, detective direction |
| 7 | [Variable Elimination Algorithm](#7-variable-elimination-algorithm) | Core idea, two rules, transformation, factors |
| 8 | [VE vs Enumeration — Savings](#8-ve-vs-enumeration--savings) | Operations count, savings table, key insight |
| 9 | [All Inference Algorithms — Comparison](#9-all-inference-algorithms--comparison) | Exact vs Approximate, when to use each |
| 10 | [Cheatsheet — One Page Summary](#10-cheatsheet--one-page-summary) | Everything on one screen |
| 11 | [Mnemonics](#11-mnemonics) | ALPHA · SAVE · XEY · REEF · PEAL |
| 12 | [Symbol Reference Table](#12-symbol-reference-table) | Every symbol defined |

---

## 1. The Bruno Network — Full Setup

> [🔝 Top](#-table-of-contents) · [Next §2 →](#2-three-variable-types)

### Easy Story 🧒
> You live alone. One day you get TWO phone calls — John AND Mary.
> Both say they heard your alarm going off.
> You're far away. You ask yourself:
> "Was there a BURGLAR? Was there an EARTHQUAKE?"
> You can't check directly. You have to REASON BACKWARDS from the calls.
> That's INFERENCE in a Bayesian Network!

### The Network Structure

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│   🦹 Burglary (B)           🌍 Earthquake (E)               │
│   ┌─────────────┐           ┌─────────────┐                  │
│   │ P(B)=0.001  │           │ P(E)=0.002  │                  │
│   └──────┬──────┘           └──────┬──────┘                  │
│          │                         │                         │
│          └────────────┬────────────┘                         │
│                       ↓                                      │
│               ┌──────────────┐                               │
│               │  🚨 Alarm (A) │                              │
│               │  P(A|B,E) CPT│                               │
│               └──────┬───────┘                               │
│                      │                                       │
│            ┌─────────┴─────────┐                             │
│            ↓                   ↓                             │
│    ┌─────────────┐    ┌─────────────┐                        │
│    │ 📞 John (J) │    │ 📞 Mary (M) │                       │
│    │  P(J|A) CPT │    │  P(M|A) CPT │                        │
│    └─────────────┘    └─────────────┘                        │
│                                                              │
│    ←─── Causality flows DOWNWARD ──────────────→             │
└──────────────────────────────────────────────────────────────┘
```

### All CPT Tables

```
BURGLARY (0 parents):          EARTHQUAKE (0 parents):
┌───────┬───────┐              ┌───────┬───────┐
│ P(B)  │ P(¬B) │              │ P(E)  │ P(¬E) │
├───────┼───────┤              ├───────┼───────┤
│ 0.001 │ 0.999 │              │ 0.002 │ 0.998 │
└───────┴───────┘              └───────┴───────┘

ALARM (2 parents — B and E → 4 rows):
┌─────┬─────┬───────┬───────┐
│  B  │  E  │ P(A)  │ P(¬A) │
├─────┼─────┼───────┼───────┤
│  T  │  T  │ 0.950 │ 0.050 │  ← Burglar + Quake → alarm almost certain
│  T  │  F  │ 0.940 │ 0.060 │  ← Burglar only → alarm very likely
│  F  │  T  │ 0.290 │ 0.710 │  ← Quake only → alarm sometimes
│  F  │  F  │ 0.001 │ 0.999 │  ← Nothing → alarm almost never (false alarm)
└─────┴─────┴───────┴───────┘

JOHN (1 parent — A → 2 rows):    MARY (1 parent — A → 2 rows):
┌─────┬──────┬───────┐            ┌─────┬──────┬───────┐
│  A  │ P(J) │ P(¬J) │            │  A  │ P(M) │ P(¬M) │
├─────┼──────┼───────┤            ├─────┼──────┼───────┤
│  T  │ 0.90 │ 0.10  │            │  T  │ 0.70 │ 0.30  │
│  F  │ 0.05 │ 0.95  │            │  F  │ 0.01 │ 0.99  │
└─────┴──────┴───────┘            └─────┴──────┴───────┘
```

### The BN Chain Rule — How Joint is Computed

```
P(B, E, A, J, M) = P(B) × P(E) × P(A|B,E) × P(J|A) × P(M|A)
                    ↑      ↑       ↑            ↑         ↑
                  B CPT  E CPT  Alarm CPT    John CPT  Mary CPT

Each node only needs its DIRECT PARENTS!
B and E are independent (no arrow between them) → P(B,E) = P(B)×P(E) ✅
```

---

## 2. Three Variable Types

> [← §1](#1-the-bruno-network--full-setup) · [🔝 Top](#-table-of-contents) · [Next §3 →](#3-three-tools-of-inference)

### Easy Story 🧒
> You're Sherlock Holmes. A client comes in.
> She TELLS you what she saw (evidence).
> You want to know WHO did it (query).
> There are suspects you haven't ruled out yet (hidden).
>
> You can't ignore hidden suspects — you must consider every one
> and weigh how likely each is.

### The Three Types

```
╔═══════════════╦════════════╦══════════════════════════════════════╗
║ TYPE          ║ SYMBOL     ║ MEANING                              ║
╠═══════════════╬════════════╬══════════════════════════════════════╣
║ Query         ║ X          ║ What you WANT to find                ║
║               ║            ║ → compute P(X|e)                     ║
╠═══════════════╬════════════╬══════════════════════════════════════╣
║ Evidence      ║ e          ║ What you KNOW / OBSERVED             ║
║               ║            ║ → fixed, don't sum over              ║
╠═══════════════╬════════════╬══════════════════════════════════════╣
║ Hidden        ║ Y / y      ║ Unknown — MUST sum over ALL values   ║
║               ║            ║ → marginalize: Σ P(..., y, ...)      ║
╚═══════════════╩════════════╩══════════════════════════════════════╝
```

### Example Classification

```
Query: P(Burglary | JohnCalls=T, MaryCalls=T)

X = Burglary                  ← query — what we WANT
e = {John=T, Mary=T}          ← evidence — what we KNOW
Y = {Alarm, Earthquake}       ← hidden — SUM OVER THESE!

Alarm:      2 values (T,F)
Earthquake: 2 values (T,F)
→ 2 × 2 = 4 hidden worlds to enumerate
```

### The Mnemonic: XEY

```
X = what you want
E = what you know
Y = sum over everY hidden value!
```

---

## 3. Three Tools of Inference

> [← §2](#2-three-variable-types) · [🔝 Top](#-table-of-contents) · [Next §4 →](#4-master-inference-formula)

### TOOL 1 — Marginalization

```
Formula:  P(X) = Σ P(X, y)
                  y

Easy story:
You want P(Win at carnival) but there are two games.
P(Win) = P(Win, RingToss) + P(Win, DuckPond)
You summed OUT the game variable → it disappeared!

When to use: Remove a hidden variable by adding up all its worlds.
```

### TOOL 2 — Conditioning

```
Formula:  P(X) = Σ P(X | y) × P(y)
                  y

Easy story:
P(Get wet today) depends on weather:
= P(Wet | Rain) × P(Rain) + P(Wet | Sun) × P(Sun)
= 0.90 × 0.30  + 0.10 × 0.70
= 0.34

When to use: You have CPT tables P(X|y) — weigh each world by P(y).
```

### TOOL 3 — Independence

```
Formula:  If a ⊥⊥ b  →  P(a,b) = P(a) × P(b)

Easy story:
Coin in London, coin in Tokyo.
No arrow between them in the BN.
P(both heads) = 0.5 × 0.5 = 0.25

When to use: No ARROW between two nodes → just multiply.
In Bruno network: B ⊥⊥ E → P(B,E) = P(B) × P(E) ✅
```

### Summary Table

```
┌──────────────────┬─────────────────────────┬──────────────────────┐
│ TOOL             │ FORMULA                 │ USE WHEN             │
├──────────────────┼─────────────────────────┼──────────────────────┤
│ Marginalization  │ Σ P(X,y)                │ Remove hidden var    │
├──────────────────┼─────────────────────────┼──────────────────────┤
│ Conditioning     │ Σ P(X|y)·P(y)           │ Have CPT table       │
├──────────────────┼─────────────────────────┼──────────────────────┤
│ Independence     │ P(a,b) = P(a)·P(b)      │ No arrow between     │
└──────────────────┴─────────────────────────┴──────────────────────┘
```

---

## 4. Master Inference Formula

> [← §3](#3-three-tools-of-inference) · [🔝 Top](#-table-of-contents) · [Next §5 →](#5-alpha---normalization-constant)

### The One Formula That Does Everything

$$P(X \mid \mathbf{e}) = \alpha \, P(X, \mathbf{e}) = \alpha \sum_{y} P(X, \mathbf{e}, y)$$

### In Plain English

```
To find P(Query | Evidence):

Step 1: Fix the evidence (lock in what you KNOW)
Step 2: Fix the query variable value (T or F)
Step 3: Sum over ALL combinations of hidden variables
Step 4: Repeat for the OTHER query value
Step 5: Normalise with α so everything sums to 1.0
```

### As a Vector (both values at once)

```
P(X | e) = α × ┌ P(X=T, e) ┐
               └ P(X=F, e) ┘

Compute both, then divide by their total → you're done!
```

### What α Means Here

```
α = 1 / [P(X=T, e) + P(X=F, e)]

= 1 / (sum of both unnormalised values)

α is a SINGLE number that scales both values to sum to 1.
Same α for BOTH values of X!
```

---

## 5. Alpha α — Normalization Constant

> [← §4](#4-master-inference-formula) · [🔝 Top](#-table-of-contents) · [Next §6 →](#6-full-posterior-inference--enumeration)

### Easy Story 🧒
> Baking contest. You bake two batches:
> - Chocolate cookies: total weight = 192g
> - Vanilla cookies:   total weight = 224g
>
> Someone asks: "What FRACTION of your output is chocolate?"
> You can't say "192" — that's not a fraction!
> Fractions must be between 0 and 1, and must ADD UP to 1.
>
> So you divide by the TOTAL (192 + 224 = 416):
>   Chocolate fraction = 192/416 = 0.4615
>   Vanilla fraction   = 224/416 = 0.5385
>   Sum                =           1.0000 ✅
>
> α = 1/416 = the "divide by total" step.
> That's ALL it is in Bayesian Networks!

### The Problem α Solves

```
Exact formula: P(x|e) = P(x,e) / P(e)

PROBLEM:
Computing P(e) requires a SEPARATE big sum:
  P(e) = Σ P(x,e)  ← extra work!
          x

SOLUTION (using α):
Don't compute P(e) separately.
Just compute P(X=T, e) and P(X=F, e).
Add them up → total = 1/α automatically!
α finds ITSELF from numbers already computed! 🎉
```

### Full Derivation from the Slide

```
GIVEN:  P(x=T, e) = 0.192
        P(x=F, e) = 0.224

STEP 1: Write as unnormalised vector
        P(X|e) = α × [0.192]
                      [0.224]

STEP 2: Apply must-sum-to-1 rule
        α × 0.192 + α × 0.224 = 1
        α × (0.192 + 0.224) = 1
        α × 0.416 = 1
        α = 1/0.416 = 2.4038

STEP 3: Compute final probabilities
        P(x=T|e) = 0.192/0.416 = 0.4615
        P(x=F|e) = 0.224/0.416 = 0.5385
        CHECK:     0.4615 + 0.5385 = 1.0000 ✅
```

### Visual — Before and After α

```
Before α (unnormalised):        After ÷ by 0.416 (normalised):
┌─────────┐                     ┌──────────┐
│  0.192  │  ─────────────────→ │  0.4615  │  46.15%
├─────────┤                     ├──────────┤
│  0.224  │                     │  0.5385  │  53.85%
└─────────┘                     └──────────┘
Total = 0.416                    Total = 1.000 ✅
```

### Key Properties of α

```
• α = 1/P(e)  — always
• SAME α for ALL values of X — compute ONCE, apply to ALL
• Evidence e can be a LONG LIST — α still works the same way!
• P(¬x|e) = 1 - P(x|e)  — complement rule still holds after normalising
• α "reduces computations" — slide title — because no separate P(e) needed
```

---

## 6. Full Posterior Inference — Enumeration

> [← §5](#5-alpha---normalization-constant) · [🔝 Top](#-table-of-contents) · [Next §7 →](#7-variable-elimination-algorithm)

### Easy Story 🧒
> John called. Mary called. Were there burglars?
>
> You imagine EVERY possible world:
>   World 1: Alarm rang + Earthquake happened
>   World 2: Alarm rang + No earthquake
>   World 3: Alarm silent + Earthquake happened
>   World 4: Alarm silent + No earthquake
>
> For EACH world: how likely would John AND Mary call?
> Add up all four answers → that's your unnormalised value!
> Do this for BOTH burglar=T and burglar=F.
> Then normalise with α.

### The Recipe — 6 Steps

```
Step 1: Identify X, e, Y
        X = Burglary, e = {j=T, m=T}, Y = {A, E}

Step 2: Write marginalisation formula
        P(B, j, m) = Σ    P(j|a)·P(m|a)·P(a|b,e)·P(b)·P(e)
                     a,e

Step 3: Pull P(b) out — it's constant to both a and e
        = P(b) × Σ    P(j|a)·P(m|a)·P(a|b,e)·P(e)
                  a,e

Step 4: Compute all 4 worlds for each B value
        (Sum over a ∈ {T,F} and e ∈ {T,F})

Step 5: Multiply inner sum × P(b)
        → gives unnormalised P(B=T,j,m) and P(B=F,j,m)

Step 6: Normalise: divide each by their total → final P(B|j,m)
```

### Two Directions in BN — Why This is Hard

```
CAUSAL DIRECTION  →  (easy: read CPT directly)
  Burglar ──→ Alarm ──→ John calls
  P(John | Alarm) = read from CPT table

INFERENCE DIRECTION  ←  (hard: need full inference)
  John calls ──→ Alarm ──→ Burglar?
  P(Burglar | John called) = requires entire computation above

The BN was built FORWARD (causes to effects).
We want BACKWARD (effects to causes).
Marginalization + α allows us to go backwards! 🔄
```

---

## 7. Variable Elimination Algorithm

> [← §6](#6-full-posterior-inference--enumeration) · [🔝 Top](#-table-of-contents) · [Next §8 →](#8-ve-vs-enumeration--savings)

### Easy Story 🧒
> Imagine you have 10 maths worksheets.
> Each needs sub-step 1 → sub-step 2 → sub-step 3.
>
> SLOW WAY (Enumeration):
> Do sub-step 1 fresh for EVERY worksheet.
> If sub-step 1 answer is the same in worksheets 1,2,3,4,5 → you redid it 5 times!
>
> SMART WAY (Variable Elimination):
> Do sub-step 1 ONCE.
> Write answer on a sticky note. 📝
> For worksheets 2,3,4,5 → just READ THE STICKY NOTE!
>
> Variable Elimination = doing each sub-calculation once, saving it,
> and reusing it everywhere it appears!

### Core Idea

```
╔══════════════════════════════════════════════════════════════╗
║  Compute each sub-sum ONCE                                   ║
║  SAVE the result as a "factor"                               ║
║  REUSE it wherever it's needed                               ║
║  Never recompute the same thing twice!                       ║
╚══════════════════════════════════════════════════════════════╝
```

### Two Golden Rules

```
RULE 1 — Summing over variable 'a'?
  Pull out ALL terms that do NOT contain 'a'!
  They are constants to this sum.

  Example:
    Σ [P(j|a) × P(b)]
     a
  = P(b) × Σ P(j|a)     ← P(b) pulled out! No 'b' in the a-sum!
             a

RULE 2 — Summing over variable 'e'?
  Pull out ALL terms that do NOT contain 'e'!

  Example:
    Σ [P(a|b,e) × P(b)]
     e
  = P(b) × Σ P(a|b,e)   ← P(b) pulled out!
             e
```

### Dependency Table — What Contains What?

```
For the expression: P(j|a)·P(m|a)·P(a|b,e)·P(b)·P(e)

Term           contains 'a'?    contains 'e'?
──────────────────────────────────────────────
P(j|a)             YES               NO
P(m|a)             YES               NO
P(a|b,e)           YES               YES
P(b)               NO                NO    ← exits BOTH sums!
P(e)               NO                YES

→ P(b) has no a, no e → pulled all the way out FIRST
→ P(e) has no a       → pulled out of the inner a-sum
```

### The Full Transformation

```
BEFORE (Enumeration — double sum, messy):
────────────────────────────────────────────────────────
Σ    P(j|a)·P(m|a)·P(a|b,e)·P(b)·P(e)
a,e

STEP 1 — P(b) contains neither a nor e → pull ALL THE WAY OUT:
────────────────────────────────────────────────────────
P(b) × Σ    P(j|a)·P(m|a)·P(a|b,e)·P(e)
             a,e

STEP 2 — Separate into nested sums; P(e) has no 'a' → pull out of inner:
────────────────────────────────────────────────────────
P(b) × Σ  P(e) × Σ  P(a|b,e)·P(j|a)·P(m|a)
          e          a
                     └──────────────────────┘
                             = f(b,e)  📝 FACTOR!

FINAL FORM:
────────────────────────────────────────────────────────
P(b) × Σ  P(e) × f(b,e)
          e
```

### What is a Factor?

```
f(b,e) = Σ  P(a|b,e) × P(j|a) × P(m|a)
          a

= A pre-computed, saved intermediate result

For a=T:  contribution = P(A=T|b,e) × P(j|T) × P(m|T)
                       = P(A=T|b,e) × 0.90   × 0.70
                       = P(A=T|b,e) × 0.63

For a=F:  contribution = P(A=F|b,e) × P(j|F) × P(m|F)
                       = P(A=F|b,e) × 0.05   × 0.01
                       = P(A=F|b,e) × 0.0005

f(b,e) = P(A=T|b,e)×0.63 + P(A=F|b,e)×0.0005

Compute once for each of 4 (b,e) combos → store in table!
```

### Factor Table (all 4 values)

```
┌───────┬───────┬──────────────────────────────────────────────┬───────────┐
│  b    │  e    │  Calculation                                  │  f(b,e)   │
├───────┼───────┼──────────────────────────────────────────────┼───────────┤
│  T    │  T    │  0.950×0.63 + 0.050×0.0005 = 0.5985+0.000025 │ 0.598525  │
│  T    │  F    │  0.940×0.63 + 0.060×0.0005 = 0.5922+0.000030 │ 0.592230  │
│  F    │  T    │  0.290×0.63 + 0.710×0.0005 = 0.1827+0.000355 │ 0.183055  │
│  F    │  F    │  0.001×0.63 + 0.999×0.0005 = 0.000630+0.0005 │ 0.001130  │
└───────┴───────┴──────────────────────────────────────────────┴───────────┘
📝 Computed ONCE — reused for both B=T step and B=F step below!
```

### Diagram — What Gets Pulled Where

```
         ┌──────────────────────────────────────────────┐
         │  Σ P(j|a)·P(m|a)·P(a|b,e)·P(b)·P(e)          │
         │   a,e                                        │
         └───────────────────┬──────────────────────────┘
                             │
                  P(b) contains no a, no e
                             │ pull out!
                             ↓
         ┌──────────────────────────────────────────────┐
         │  P(b) × Σ P(j|a)·P(m|a)·P(a|b,e)·P(e)        │
         │          a,e                                 │
         └───────────────────┬──────────────────────────┘
                             │
                  Separate: P(e) has no 'a'
                             │ nest the sums!
                             ↓
         ┌──────────────────────────────────────────────┐
         │  P(b) × Σ P(e) × [Σ P(a|b,e)·P(j|a)·P(m|a)]  │
         │          e          a                        │
         │                     └───────────────────────┘│
         │                          = f(b,e) 📝 SAVED!  │
         └──────────────────────────────────────────────┘
```

---

## 8. VE vs Enumeration — Savings

> [← §7](#7-variable-elimination-algorithm) · [🔝 Top](#-table-of-contents) · [Next §9 →](#9-all-inference-algorithms--comparison)

### Operation Count for P(B|j,m)

```
ENUMERATION:
  4 (a,e) worlds × 4 multiplications each = 16 ops for B=T
  4 (a,e) worlds × 4 multiplications each = 16 ops for B=F
  Total: 32 multiplications 😩

VARIABLE ELIMINATION:
  Factor f(b,e): 4 combos × 2 multiplications = 8 ops
  Outer e-sum:   2 b-values × 2 e-values = 4 ops
  P(b) multiply: 2 ops
  Total: 14 multiplications ✅

Saved: 32 - 14 = 18 ops = 56% fewer!
```

### Savings Grow Dramatically with Network Size

```
Nodes   Enumeration       VE (approx)    Savings
─────────────────────────────────────────────────
5       32                14             56%
10      1,024             40             96%
20      1,048,576         80             99.99%
30      1,073,741,824     120            ~100%
```

### Why the Savings Grow

```
Enumeration: every combination → exponential explosion 2ⁿ
VE:          smart reuse → roughly linear in n

KEY INSIGHT:
Enumeration recomputes the SAME inner sums
over and over for different outer variable values.

VE computes each inner sum ONCE, saves it,
and reuses → eliminates ALL redundant computation!
```

---

## 9. All Inference Algorithms — Comparison

> [← §8](#8-ve-vs-enumeration--savings) · [🔝 Top](#-table-of-contents) · [Next §10 →](#10-cheatsheet--one-page-summary)

```
╔══════════════════════════════════════════════════════════════════╗
║                  INFERENCE ALGORITHMS MAP                        ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  📐 EXACT INFERENCE (perfect answer)                             ║
║     ├── Enumeration:       list all worlds, compute all          ║
║     │                      O(2ⁿ) — exact but slow                ║
║     └── Variable Elim:     compute factors once, reuse           ║
║                            same answer, much fewer steps         ║
║                                                                  ║
║  🎲 APPROXIMATE INFERENCE (good enough, much faster)             ║
║     ├── Prior Sampling:    roll dice per CPT, follow network     ║
║     │                      fast but rare evidence wastes runs    ║
║     ├── Rejection Sampling: keep only evidence-matching samples  ║
║     │                      still wastes samples for rare e       ║
║     ├── Likelihood Weighting: fix evidence, weight each sample   ║
║     │                      NO wasted samples — better!           ║
║     └── Gibbs Sampling:    flip one variable at a time           ║
║                            converges to true distribution        ║
╚══════════════════════════════════════════════════════════════════╝
```

```
WHEN TO USE WHICH:
< 20 nodes  →  Exact (Variable Elimination)
≥ 20 nodes  →  Approximate (Likelihood Weighting or Gibbs)
```

---

## 10. Cheatsheet — One Page Summary

> [← §9](#9-all-inference-algorithms--comparison) · [🔝 Top](#-table-of-contents) · [Next §11 →](#11-mnemonics)

```
╔══════════════════════════════════════════════════════════════════╗
║         BAYESIAN NETWORK INFERENCE — MASTER CHEATSHEET           ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  VARIABLES                                                       ║
║  X = query (want)  ·  e = evidence (know)  ·  Y = hidden (Σ)     ║
║                                                                  ║
║  MASTER FORMULA                                                  ║
║  P(X|e) = α × Σ P(X,e,y)     α = 1/(P(X=T,e)+P(X=F,e))           ║
║                y                                                 ║
║                                                                  ║
║  JOINT EXPANSION                                                 ║
║  P(j,m,a,b,e) = P(j|a)·P(m|a)·P(a|b,e)·P(b)·P(e)                 ║
║                                                                  ║
║  THREE TOOLS                                                     ║
║  Marginalise:   P(X)=Σ P(X,y)        sum out hidden              ║
║  Condition:     P(X)=Σ P(X|y)P(y)    use CPT weights             ║
║  Independence:  P(a,b)=P(a)P(b)      no arrow = multiply         ║
║                                                                  ║
║  VARIABLE ELIMINATION FINAL FORM                                 ║
║  P(b)×Σ P(e)×[Σ P(a|b,e)·P(j|a)·P(m|a)]                          ║
║        e       a                                                 ║
║               └─────────────────────────┘                        ║
║                    f(b,e) — computed ONCE, saved! 📝             ║
║                                                                  ║
║  KEY CPT SHORTCUTS                                               ║
║  P(j|A=T)×P(m|A=T) = 0.90×0.70 = 0.63    ← memorise!             ║
║  P(j|A=F)×P(m|A=F) = 0.05×0.01 = 0.0005  ← memorise!             ║
║                                                                  ║
║  KEY RESULTS                                                     ║
║  P(B=T|j,m) = 0.284   P(B=F|j,m) = 0.716  (sum=1 ✅)             ║
║  α (slide)  = 1/0.416 = 2.4038                                   ║
║  Prior P(B) = 0.001 → posterior 0.284 = 284× jump!               ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## 11. Mnemonics

> [← §10](#10-cheatsheet--one-page-summary) · [🔝 Top](#-table-of-contents) · [Next §12 →](#12-symbol-reference-table)

### "ALPHA" — What α Does
```
A = Always the same for all X values
L = 1 / (sum of aLL unnorm values)
P = Probabilities must sum to 1
H = Hides P(e) computation inside itself
A = Apply by multiplying each unnorm value × α
```

### "SAVE" — Variable Elimination Steps
```
S = Spot what depends on what (draw the dependency table)
A = Arrange nested sums (inner eliminates first)
V = pull out constants and Variables that don't belong
E = Evaluate inner sum → save as factor, rEuse!
```

### "XEY" — Variable Types
```
X = what you want (query)
E = what you know (evidence)
Y = sum over everY value of hidden!
```

### "REEF" — When to Pull Constants Out
```
R = Read every term carefully
E = Every term that lacks current sum variable
E = Exits the sum (gets pulled outside)
F = Factor it out front — reduces inner work!
```

### "PEAL" — Parts of Inference Formula
```
P = P(X,e,y) is the joint — expand it
E = Evidence e is fixed throughout — don't sum over it
A = Alpha normalises at the end — compute once
L = Likelihood from each CPT row feeds the product
```

---

## 12. Symbol Reference Table

> [← §11](#11-mnemonics) · [🔝 Top](#-table-of-contents)

```
Symbol    Name                  Meaning
────────────────────────────────────────────────────────────────
α         Alpha                 Normalisation constant = 1/P(e)
P(X|e)    Posterior             Updated belief after evidence
P(X)      Prior / Marginal      Belief before any evidence
P(X,e)    Joint                 Both X and e are true together
P(X|Y)    Conditional           X given Y has happened
Σ         Sigma                 Sum over all listed values
∏         Pi                    Product (multiply) over all values
⊥⊥        Independence          No direct connection in BN graph
¬         NOT                   Complement / negation
f(b,e)    Factor                Pre-computed saved inner sum (VE)
X         Query variable        What you are computing P(?) for
e         Evidence              Observed / known fixed values
Y / y     Hidden variable       Unknown — must sum over all values
n         Node count            Total number of variables in BN
parents   Parent set            Direct cause-nodes of a variable
posterior Updated belief        P(X|e) — after seeing evidence
prior     Initial belief        P(X) — before seeing evidence
CPT       Cond. Prob. Table     Lookup table for each BN node
```

---

> **Navigation:** [📋 INDEX](./bn_inference_index.md) | 📘 **THEORY** *(you are here)* | [🔢 NUMERICALS →](./bn_inference_numericals.md) | [💻 PRACTICE →](./bn_inference_practice.md)
>
> **Course:** AI

[🔝 Back to Top](#-bayesian-network-inference--theory)
