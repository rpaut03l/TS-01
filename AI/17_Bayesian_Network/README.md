# 🕸️ Topic 17 — Bayesian Networks

> **Difficulty**: 🔴 Hard | **Syllabus Section**: Bayesian Networks & Uncertain Reasoning | Directed/Undirected Models, Inference
>
> **Slides**: RB-M & SD-M | **Quiz Relevance**: ⭐⭐⭐⭐⭐

---

## 🍼 Explain Like I'm 5 (ELI5)

In the real world, we're NEVER 100% sure about anything. "Will it rain?" "Is my friend sick?" "Will the car start?" Everything is UNCERTAIN!

**Bayesian Networks** (BNs) are like a MAP of how things are connected by cause and effect, with NUMBERS showing how likely each connection is.

> 🍼 **ELI5**: Imagine a chain of dominoes:
> - Rain → Wet Grass → Muddy Shoes
> - If it rained, there's an 80% chance the grass is wet
> - If grass is wet, there's a 90% chance your shoes get muddy
> - A Bayesian Network draws these connections with the probabilities!
>
> Now, if you see muddy shoes, you can work BACKWARDS: "Hmm, probably the grass was wet, and probably it rained!" That's inference!

---

## 📚 Table of Contents

1. [Probability Basics Review](#1-probability-basics)
2. [What is a Bayesian Network?](#2-what-is-a-bayesian-network)
3. [Building a Bayesian Network](#3-building-a-bn)
4. [The Classic Example: Alarm Network](#4-alarm-network)
5. [Inference in Bayesian Networks](#5-inference)
6. [Directed vs Undirected Models](#6-directed-vs-undirected)
7. [Key Takeaways](#7-key-takeaways)
8. [Exam Tips](#8-exam-tips)

---

## 1. Probability Basics Review

### Key Formulas

| Formula | Name | Meaning |
|---|---|---|
| P(A) | Prior | Probability of A before any evidence |
| P(A\|B) | Conditional | Probability of A given B is true |
| P(A,B) | Joint | Probability of both A and B |
| P(A,B) = P(A\|B) × P(B) | Product Rule | Joint = conditional × marginal |
| P(A) = Σ_B P(A,B) | Marginalization | Sum over all values of B |
| P(A\|B) = P(B\|A)P(A)/P(B) | **Bayes' Rule** | Flip the conditional! |

### Bayes' Rule — The Star Formula!

```
                P(evidence | cause) × P(cause)
P(cause | evidence) = ────────────────────────────────
                            P(evidence)

              P(B|A) × P(A)
P(A|B) = ─────────────────────
                P(B)
```

> 🍼 **ELI5**: You see wet grass (evidence). What's the chance it rained (cause)?
> Bayes says: Take "how often rain causes wet grass" × "how often it rains" ÷ "how often grass is wet for any reason"

### Independence

**A and B are independent if**: P(A,B) = P(A) × P(B) or equivalently P(A|B) = P(A)

**Conditional independence**: A and B are independent GIVEN C:
P(A,B|C) = P(A|C) × P(B|C)

---

## 2. What is a Bayesian Network?

### Definition

A Bayesian Network is a **directed acyclic graph (DAG)** where:
- Each **node** represents a random variable
- Each **edge** represents a direct probabilistic dependency (parent → child)
- Each node has a **Conditional Probability Table (CPT)** showing P(node | parents)

### What It Encodes

The BN represents the **full joint probability distribution** compactly:

```
P(X₁, X₂, ..., Xₙ) = ∏ᵢ P(Xᵢ | Parents(Xᵢ))
```

> 🍼 **ELI5**: Instead of writing a HUGE table of every possible combination (2ⁿ rows for n binary variables), we just store small tables at each node. The structure of the graph tells us which variables directly affect which!

### Compact Representation

**Full joint for n binary variables**: 2ⁿ - 1 numbers needed
**Bayesian Network**: If each node has at most k parents: n × 2ᵏ numbers needed

For n=20, k=3:
- Full joint: 2²⁰ = 1,048,576 numbers
- BN: 20 × 2³ = 160 numbers → **6,500x more compact!**

---

## 3. Building a Bayesian Network

### The Process

1. **Identify variables**: What are the relevant random variables?
2. **Order them**: Choose a causal ordering (causes before effects)
3. **For each variable**: Decide which earlier variables are its DIRECT parents
4. **Fill in CPTs**: Assign conditional probabilities P(Xᵢ | Parents(Xᵢ))

### Conditional Probability Tables (CPTs)

**Root node** (no parents): Just a prior probability
```
P(Burglary = T) = 0.001
P(Burglary = F) = 0.999
```

**Node with parents**: A table with one row per combination of parent values
```
P(Alarm | Burglary, Earthquake):

| Burglary | Earthquake | P(Alarm=T) | P(Alarm=F) |
|----------|------------|------------|------------|
| T        | T          | 0.95       | 0.05       |
| T        | F          | 0.94       | 0.06       |
| F        | T          | 0.29       | 0.71       |
| F        | F          | 0.001      | 0.999      |
```

---

## 4. The Classic Example: Alarm Network

### The Story

You have a burglar alarm at home. It can be triggered by a burglary OR an earthquake. If the alarm goes off, your neighbors John and Mary might call you.

### The Network

```
    Burglary          Earthquake
    (0.001)            (0.002)
       \                 /
        \               /
         ↓             ↓
           Alarm
          /     \
         /       \
        ↓         ↓
   JohnCalls    MaryCalls
```

### The CPTs

**P(Burglary)** = 0.001
**P(Earthquake)** = 0.002

**P(Alarm | Burglary, Earthquake)**:
| B | E | P(A=T) |
|---|---|---|
| T | T | 0.95 |
| T | F | 0.94 |
| F | T | 0.29 |
| F | F | 0.001 |

**P(JohnCalls | Alarm)**:
| A | P(J=T) |
|---|---|
| T | 0.90 |
| F | 0.05 |

**P(MaryCalls | Alarm)**:
| A | P(M=T) |
|---|---|
| T | 0.70 |
| F | 0.01 |

### Computing a Joint Probability

P(B=T, E=F, A=T, J=T, M=T) = ?

Using the chain rule for BNs:

**The chain rule says**: P(X₁, X₂, ..., Xₙ) = ∏ P(Xᵢ | Parents(Xᵢ))

**So we just look up each variable's CPT given its parents:**

```
P(B=T, E=F, A=T, J=T, M=T)

= P(B=T)           ← Burglary has no parents, look up prior
  × P(E=F)         ← Earthquake has no parents, look up prior
  × P(A=T|B=T,E=F) ← Alarm's parents are B and E, look up CPT row
  × P(J=T|A=T)     ← John's parent is Alarm, look up CPT row
  × P(M=T|A=T)     ← Mary's parent is Alarm, look up CPT row

Now plug in the numbers from the CPTs above:

= 0.001            ← P(B=T) from Burglary prior
  × 0.998          ← P(E=F) = 1 - P(E=T) = 1 - 0.002
  × 0.94           ← P(A=T|B=T,E=F) from Alarm CPT row
  × 0.90           ← P(J=T|A=T) from John CPT
  × 0.70           ← P(M=T|A=T) from Mary CPT

= 0.001 × 0.998 × 0.94 × 0.90 × 0.70

Let's compute step by step:
  0.001 × 0.998 = 0.000998
  0.000998 × 0.94 = 0.000938
  0.000938 × 0.90 = 0.000844
  0.000844 × 0.70 = 0.000591

= 0.000591 (approximately)
```

> 🍼 **Kid Version**: We're asking "What's the chance that ALL of these happen at once: burglary=yes, earthquake=no, alarm=yes, john calls=yes, mary calls=yes?" We just MULTIPLY the probability of each thing, given what caused it. Like: chance of burglary × chance of no earthquake × chance alarm rings (given burglary and no earthquake) × chance John calls (given alarm) × chance Mary calls (given alarm).

### 🧮 Full Worked Example: Computing P(Burglary | JohnCalls, MaryCalls)

This is the CLASSIC exam question. Let's compute it with every single arithmetic step.

**Question**: Both John and Mary called. What's the probability of a burglary?

**What we need**: P(B=T | J=T, M=T)

**Using Bayes' Rule**:
```
P(B=T | J=T, M=T) = P(B=T, J=T, M=T) / P(J=T, M=T)
```

Since we need to sum over hidden variables (E and A), let's compute:

```
P(B=T, J=T, M=T) = Σ_e Σ_a P(B=T) × P(e) × P(a|B=T,e) × P(J=T|a) × P(M=T|a)
```

**We need to compute 4 terms (E ∈ {T,F} and A ∈ {T,F}):**

```
Term 1: E=T, A=T
  = P(B=T) × P(E=T) × P(A=T|B=T,E=T) × P(J=T|A=T) × P(M=T|A=T)
  = 0.001  × 0.002  × 0.95            × 0.90        × 0.70
  = 0.001 × 0.002 × 0.95 × 0.90 × 0.70
  = 0.001 × 0.002 = 0.000002
  × 0.95 = 0.0000019
  × 0.90 = 0.00000171
  × 0.70 = 0.000001197

Term 2: E=T, A=F
  = 0.001 × 0.002 × 0.05 × 0.05 × 0.01
  = 0.001 × 0.002 = 0.000002
  × 0.05 = 0.0000001
  × 0.05 = 0.000000005
  × 0.01 = 0.00000000005  (tiny!)

Term 3: E=F, A=T
  = 0.001 × 0.998 × 0.94 × 0.90 × 0.70
  = 0.001 × 0.998 = 0.000998
  × 0.94 = 0.000938
  × 0.90 = 0.000844
  × 0.70 = 0.000591  ← This is the BIGGEST term!

Term 4: E=F, A=F
  = 0.001 × 0.998 × 0.06 × 0.05 × 0.01
  = 0.001 × 0.998 = 0.000998
  × 0.06 = 0.0000599
  × 0.05 = 0.000003
  × 0.01 = 0.00000003

P(B=T, J=T, M=T) = 0.000001197 + 0.00000000005 + 0.000591 + 0.00000003
                  ≈ 0.000592
```

**Similarly compute P(B=F, J=T, M=T)** (same but with B=False):

```
Term 1: E=T, A=T: 0.999 × 0.002 × 0.29 × 0.90 × 0.70 = 0.000365
Term 2: E=T, A=F: 0.999 × 0.002 × 0.71 × 0.05 × 0.01 = 0.0000007
Term 3: E=F, A=T: 0.999 × 0.998 × 0.001 × 0.90 × 0.70 = 0.000628
Term 4: E=F, A=F: 0.999 × 0.998 × 0.999 × 0.05 × 0.01 = 0.000499

P(B=F, J=T, M=T) ≈ 0.000365 + 0.0000007 + 0.000628 + 0.000499 ≈ 0.001493
```

**Now normalize:**

```
P(B=T | J=T, M=T) = 0.000592 / (0.000592 + 0.001493)
                   = 0.000592 / 0.002085
                   ≈ 0.284

P(B=F | J=T, M=T) ≈ 0.716
```

**Answer**: P(Burglary | both John and Mary called) ≈ **0.284 (28.4%)**

> 🍼 **What does this mean?** Burglary is normally super rare (0.1%). But when BOTH neighbors call, the probability jumps to 28.4%! That's a 284× increase! The evidence (two calls) dramatically changed our belief.

---

## 5. Inference in Bayesian Networks

### Types of Inference

| Type | Direction | Example |
|---|---|---|
| **Causal** (predictive) | Parent → Child | "Given burglary, what's P(John calls)?" |
| **Evidential** (diagnostic) | Child → Parent | "John called. What's P(burglary)?" |
| **Intercausal** | Between causes | "John called. No earthquake. What's P(burglary)?" |

### Inference by Enumeration

To compute P(X | e) where e is evidence:

```
P(X | e) = α × Σ_hidden P(X, e, hidden)
           where α = 1/P(e) is the normalization constant
```

### Example: P(Burglary | JohnCalls=T, MaryCalls=T)

```
P(B | j, m) = α × P(B) × Σ_e P(e) × Σ_a P(a|B,e) × P(j|a) × P(m|a)
```

This requires summing over all hidden variables (E and A).

**Computing P(B=T | j=T, m=T)**:
```
= α × 0.001 × [Σ_e Σ_a P(e) × P(a|B=T,e) × P(j=T|a) × P(m=T|a)]

Expanding... (lots of arithmetic)

Result: P(B=T | j=T, m=T) ≈ 0.284
```

So even though burglary is rare (0.1%), if BOTH neighbors call, there's a 28.4% chance of burglary!

### Conditional Independence in BNs

BNs encode conditional independence through the graph structure:

**A node is conditionally independent of ALL non-descendants given its parents.**

This is the **Markov Property** and it's what makes BN inference tractable!

### d-Separation

Two variables X and Y are conditionally independent given evidence Z if every path between X and Y is "blocked" by Z.

A path is blocked if it contains:
1. **Chain**: A → B → C where B is observed (in Z)
2. **Fork**: A ← B → C where B is observed (in Z)
3. **Collider**: A → B ← C where B is NOT observed (and no descendant of B is observed)

> 🍼 **ELI5**: 
> - **Chain** (A→B→C): If you know B, then A doesn't tell you anything new about C. Like: Rain→Wet→Muddy. If you KNOW the grass is wet, knowing whether it rained doesn't change your prediction about muddy shoes.
> - **Fork** (A←B→C): If you know B, then A and C become independent. Like: Flu→Fever and Flu→Headache. If you KNOW someone has the flu, their fever and headache are independent symptoms.
> - **Collider** (A→B←C): If you DON'T know B, A and C are independent. But if you DO know B, they become DEPENDENT! Like: Burglary→Alarm←Earthquake. If the alarm goes off and there's no earthquake, it's probably a burglary (explaining away).

---

## 6. Directed vs Undirected Models

### Directed Models (Bayesian Networks)

- Edges have **directions** (arrows)
- Represent **causal relationships**
- CPTs define P(child | parents)
- Good for modeling cause → effect

### Undirected Models (Markov Random Fields)

- Edges have **no direction**
- Represent **correlations/affinities**
- Use **potential functions** (not conditional probabilities)
- Good for modeling symmetric relationships (pixels in an image)

```
Directed (BN):         Undirected (MRF):
  A → B → C            A ── B ── C
  ↓                     |         |
  D                     D ────────+
```

### Key Difference

| Feature | Directed (BN) | Undirected (MRF) |
|---|---|---|
| **Edges** | Arrows (parent→child) | Lines (no direction) |
| **Parameters** | Conditional probabilities P(X\|Parents) | Potential functions φ(clique) |
| **Normalization** | Automatic (probabilities sum to 1) | Requires computing partition function Z |
| **Causality** | Natural causal interpretation | No causal direction |
| **Independence** | d-separation | Graph separation |

---

## 7. Key Takeaways

1. **Bayesian Networks** = DAG + CPTs = compact representation of joint probability
2. **Joint probability**: P(X₁,...,Xₙ) = ∏ P(Xᵢ | Parents(Xᵢ))
3. **CPTs** specify P(node | parent values) for each node
4. **Inference** = computing P(query | evidence) by marginalizing over hidden variables
5. **Conditional independence** is encoded by the graph structure (d-separation)
6. **Explaining away**: Observing a common effect makes its causes dependent!
7. **Directed (BN)** vs **Undirected (MRF)**: directions vs no directions, conditional probs vs potentials
8. BNs are MUCH more compact than full joint probability tables

---

## 8. Exam Tips

### Must-Know

1. **Draw a BN** from a problem description
2. **Write CPTs** for each node
3. **Compute joint probabilities** using the chain rule
4. **Compute conditional probabilities** using inference by enumeration
5. **Identify conditional independencies** using d-separation
6. **Explain the explaining away phenomenon**

### Common Mistakes

❌ Drawing cycles in a BN (it must be a DAG — no cycles!)
❌ Forgetting to normalize when computing conditional probabilities
❌ Getting d-separation wrong — especially the collider case (observing a collider CREATES dependency!)
❌ Confusing prior P(A) with conditional P(A|B)
❌ Wrong CPT size: a node with k binary parents has 2ᵏ rows

---

## 📖 References

- AIMA — Chapter 13-14 (Probabilistic Reasoning, Bayesian Networks)

---

[⬅️ Prev: Partial Order Planning](../16_Planning_Partial_Order/README.md) | [Back to Main](../README.md) | [Next: Causality & Probabilistic Reasoning ➡️](../18_Causality_Probabilistic_Reasoning/README.md)
