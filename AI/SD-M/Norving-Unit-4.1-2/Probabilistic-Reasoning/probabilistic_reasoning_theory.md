# 📘 Probabilistic Reasoning — THEORY Guide
### Artificial Intelligence 
### Units 4.1 (Quantifying Uncertainty) + 4.2 (Bayesian Networks)

---

> **Navigation:** [📋 INDEX](./probabilistic_reasoning_index.md) | [🔢 NUMERICALS](./probabilistic_reasoning_numericals.md)

---

## 📚 Section Index

| # | Section | Jump |
|---|---------|------|
| 1 | [Why Uncertainty?](#1-why-uncertainty--the-problem) | The Problem |
| 2 | [Basic Probability Terms](#2-basic-probability-terms) | Sample Space, Events, RVs |
| 3 | [Probability Axioms & Rules](#3-probability-axioms--rules) | Product, Inclusion-Exclusion |
| 4 | [Bayes' Rule](#4-bayes-rule) | The King Formula |
| 5 | [Inference from Joint Distribution](#5-inference-using-full-joint-distribution) | Marginalization, Conditioning |
| 6 | [Independence](#6-independence) | P(a,b) = P(a)P(b) |
| 7 | [Conditional Independence](#7-conditional-independence) | P(X,Y\|Z) = P(X\|Z)P(Y\|Z) |
| 8 | [Naive Bayes Model](#8-naive-bayes-model) | Cause → Effects |
| 9 | [Bayesian Networks — Syntax](#9-bayesian-networks--syntax) | DAG, Nodes, Arrows |
| 10 | [BN Semantics & CPTs](#10-bn-semantics--cpts) | Tables, Complexity |
| 11 | [Markov Blanket](#11-markov-blanket) | PCK rule |
| 12 | [Full Joint from BN](#12-obtaining-full-joint-from-bn) | The Product Formula |
| 13 | [Inference — Formal Definition](#13-inference--formal-definition) | X, E, Y variables |
| 14 | [Normalization Constant α](#14-normalization-constant-α) | The α trick |
| 15 | [Exact Inference — Enumeration](#15-exact-inference--enumeration) | Brute force |
| 16 | [Exact Inference — Variable Elimination](#16-exact-inference--variable-elimination) | Smart factoring |
| 17 | [Approximate Inference (Overview)](#17-approximate-inference-overview) | Sampling methods |

---

## 1. Why Uncertainty? — The Problem

> [📋 INDEX](./probabilistic_reasoning_index.md) | [Next →](#2-basic-probability-terms)

### Easy Story 🍼

Imagine you're a doctor. A patient walks in with a toothache. You think "cavity!" But wait — toothaches can also come from gum disease, an abscess, or just biting something hard. You can't be 100% sure. In logic, `Toothache ⇒ Cavity` would mean EVERY toothache = cavity. That's clearly wrong!

So instead of saying YES or NO, we say "there's an 80% chance it's a cavity." That's probability!

### Formal Explanation

Agents face uncertainty due to:

```
┌─────────────────────────────────────────────────────────────────┐
│  THREE ENEMIES OF CERTAINTY  (mnemonic: LIP)                    │
│                                                                 │
│  L = LAZINESS                                                   │
│      Too much work to list EVERY possible cause/effect.         │
│      "Toothache ⇒ Cavity ∨ GumDisease ∨ Abscess ∨ ..."          │
│      Nobody wants to write all that!                            │
│                                                                 │
│  I = (Theoretical) IGNORANCE                                    │
│      Science doesn't have complete theory for the domain.       │
│      We simply don't know all the rules.                        │
│                                                                 │
│  P = PRACTICAL (ignorance)                                      │
│      Even if we knew all rules, not all tests have been run.    │
│      Can't X-ray every patient before diagnosing.               │
└─────────────────────────────────────────────────────────────────┘
```

**Solution:** Use **PROBABILITY** — a number between 0 and 1 expressing our **degree of belief**.

**Key insight:** Probability is about YOUR KNOWLEDGE STATE, not about the real world. The patient either has a cavity or doesn't — the 0.8 reflects what WE know, not what IS.

> [🔢 Practice these concepts](./probabilistic_reasoning_numericals.md#problem-1-weather-traffic-axioms) | [🔝 Top](#-section-index) | [Next →](#2-basic-probability-terms)

---

## 2. Basic Probability Terms

> [← Prev](#1-why-uncertainty--the-problem) | [📋 INDEX](./probabilistic_reasoning_index.md) | [Next →](#3-probability-axioms--rules)

### Easy Story 🍼

Think of rolling two dice. Before you roll, there are 36 possible things that could happen: (1,1), (1,2), ... (6,6). That big bag of 36 possibilities? That's your **sample space**. Each one outcome like (3,4) is a single **possible world**. And when you ask "what's the chance the sum is 11?" you're asking about a smaller group (an **event**) inside that big bag.

### Sample Space (Ω)

The set of ALL possible worlds. They must be:

```
┌────────────────────────────────────────────────────────┐
│  MUTUALLY EXCLUSIVE: Only ONE world can be true        │
│  EXHAUSTIVE: ONE of them MUST be true                  │
│                                                        │
│  Two dice example:                                     │
│                                                        │
│  Ω = { (1,1), (1,2), (1,3), ... (6,6) }                │
│        ╰──────────── 36 outcomes ───────────╯          │
│                                                        │
│  Ω = big circle containing all possible worlds         │
│  ω = one specific world inside Ω                       │
└────────────────────────────────────────────────────────┘
```

### Probability Model

A rule that assigns a number P(ω) to each possible world:

```
  AXIOMS:
  ┌─────────────────────────────────────┐
  │  0 ≤ P(ω) ≤ 1    for every ω        │  ← each prob is 0 to 1
  │  Σ_{ω∈Ω} P(ω) = 1                   │  ← all probs add to 1
  └─────────────────────────────────────┘

  Fair dice: P(each outcome) = 1/36
  Check: 36 × (1/36) = 1 ✓
```

### Events and Propositions (φ)

An **event** = a SUBSET of Ω = a group of outcomes you care about.

```
  φ = "dice sum = 11" = { (5,6), (6,5) }

  P(φ) = Σ_{ω ∈ φ} P(ω)
       = P((5,6)) + P((6,5))
       = 1/36 + 1/36
       = 1/18 ≈ 0.056
```

### Random Variable and Domain

A **random variable** = a variable that can take different values.

```
  VARIABLE (Capital)     DOMAIN (set of values)
  ─────────────────────────────────────────────
  Total                  {2, 3, 4, ..., 12}
  Doubles                {(1,1), (2,2), ..., (6,6)}
  Die1                   {1, 2, 3, 4, 5, 6}
  Boo (Boolean)          {true, false}
  Weather                {sunny, rainy, cloudy, snowy}

  Convention:
  • Capital letter = variable name (Weather)
  • Lowercase = specific value (sunny)
```

### Prior vs Posterior Probability

```
┌──────────────────────┬──────────────────────────────────────┐
│  PRIOR (Unconditional)│  POSTERIOR (Conditional)            │
│  = before seeing      │  = after seeing evidence            │
│    any evidence       │                                     │
│                       │                                     │
│  P(doubles) = 6/36    │  P(doubles | Die1=5) = 1/6          │
│  P(cavity)  = 0.2     │  P(cavity | toothache) = 0.6        │
│                       │                                     │
│  "In general, how     │  "NOW that I KNOW this fact,        │
│   likely is X?"       │   how likely is X?"                 │
└──────────────────────┴──────────────────────────────────────┘

  Conditional Probability DEFINITION:
  ┌─────────────────────────────────────────┐
  │  P(a | b) = P(a ∧ b) / P(b)             │
  │                                         │
  │  Works when P(b) > 0                    │
  └─────────────────────────────────────────┘

  Think of it as: "Zoom into the world where b is true.
  Now, what fraction of that world also has a?"
```

### Probability Distribution P(X)

When we list probs for ALL values of a variable:

```
  P(Weather) = ⟨0.6, 0.1, 0.29, 0.01⟩   (in order: sunny, rainy, cloudy, snowy)

  ┌─────────┬───────┐
  │ Weather │ P(ω)  │
  ├─────────┼───────┤
  │ sunny   │ 0.6   │
  │ rainy   │ 0.1   │
  │ cloudy  │ 0.29  │
  │ snowy   │ 0.01  │
  └─────────┴───────┘
  Sum = 1.0 ✓
```

### Joint Probability Distribution P(X, Y)

Probs for ALL COMBINATIONS of two (or more) variables:

```
  P(Weather, Traffic):
  ┌─────────┬──────┬────────┐
  │ Weather │Traffic│ P(ω)  │
  ├─────────┼──────┼────────┤
  │ sunny   │ more │ 0.05   │
  │ sunny   │ less │ 0.55   │
  │ rainy   │ more │ 0.095  │
  │ rainy   │ less │ 0.005  │
  │ cloudy  │ more │ 0.145  │
  │ cloudy  │ less │ 0.145  │
  │ snowy   │ more │ 0.0099 │
  │ snowy   │ less │ 0.0001 │
  └─────────┴──────┴────────┘
  Sum = 1.0 ✓

  NOTE: P(X,Y) = P(Y,X)  (order doesn't matter for joint prob)
```

### Continuous Variables — PDF

For continuous random variables, we use a **probability density function** f(X).

```
  Example: Gaussian PDF
  f(X) = (1/σ√(2π)) · e^(-(x-μ)²/2σ²)

  Rules:
  • 0 ≤ f(x)
  • ∫_{x1}^{x2} f(x)dx = 1  (total area = 1)
  • P(x1 ≤ X ≤ x2) = area under curve between x1 and x2
```

> [🔢 Weather-Traffic Numericals](./probabilistic_reasoning_numericals.md#problem-1-weather-traffic-axioms) | [🔝 Top](#-section-index) | [Next →](#3-probability-axioms--rules)

---

## 3. Probability Axioms & Rules

> [← Prev](#2-basic-probability-terms) | [📋 INDEX](./probabilistic_reasoning_index.md) | [Next →](#4-bayes-rule)

### Easy Story 🍼

You have 3 power tools (mnemonic: **PPC**): **P**roduct rule to break ANDs apart, **P**lus-minus (inclusion-exclusion) for ORs, and **C**omplement to flip true/false. With just these 3, you can solve almost any probability question!

### The Rules (PPC)

```
┌──────────────────────────────────────────────────────────────────┐
│  RULE 1: CONDITIONAL PROBABILITY (definition)                    │
│                                                                  │
│  P(a | b) = P(a ∧ b) / P(b)       when P(b) > 0                  │
│                                                                  │
│  Read: "Prob of a GIVEN b = (prob of both) / (prob of b)"        │
├──────────────────────────────────────────────────────────────────┤
│  RULE 2: PRODUCT RULE (rearrange Rule 1)                         │
│                                                                  │
│  P(a ∧ b) = P(a | b) · P(b)                                      │
│                                                                  │
│  Read: "Prob of BOTH = (prob of a given b) × (prob of b)"        │
│                                                                  │
│  Also works as: P(a ∧ b) = P(b | a) · P(a)                       │
├──────────────────────────────────────────────────────────────────┤
│  RULE 3: INCLUSION-EXCLUSION (for OR)                            │
│                                                                  │
│  P(a ∨ b) = P(a) + P(b) - P(a ∧ b)                               │
│                                                                  │
│  Venn diagram:                                                   │
│  ┌───────────────────────────────┐                               │
│  │       ┌───┐   ┌───┐           │                               │
│  │       │ A │╲ ╱│ B │           │                               │
│  │       │   │ X │   │           │  We subtract A∧B              │
│  │       │   │╱ ╲│   │           │  because we counted           │
│  │       └───┘   └───┘           │  it twice!                    │
│  └───────────────────────────────┘                               │
├──────────────────────────────────────────────────────────────────┤
│  RULE 4: COMPLEMENT                                              │
│                                                                  │
│  P(¬a) = 1 - P(a)                                                │
│                                                                  │
│  Read: "Prob of NOT a = 1 minus prob of a"                       │
├──────────────────────────────────────────────────────────────────┤
│  BONUS: INTERSECTION WITH COMPLEMENT                             │
│                                                                  │
│  P(a ∧ ¬b) = P(a) - P(a ∧ b)                                     │
│                                                                  │
│  Venn diagram:                                                   │
│  ┌───────────────────────────────┐                               │
│  │  ████████┌───┐                │                               │
│  │  ██ A ███│ B │                │  Shaded area = A but not B    │
│  │  ██ only█│   │                │  = P(A) - P(A∩B)              │
│  │  ████████└───┘                │                               │
│  └───────────────────────────────┘                               │
└──────────────────────────────────────────────────────────────────┘
```

### Notation Quick Reference

```
  |   means "given"              P(a|b) = "prob of a given b"
  ∧   means "AND" (intersection) P(a∧b) = "prob of both a and b"
  ∨   means "OR" (union)         P(a∨b) = "prob of a or b or both"
  ¬   means "NOT"                P(¬a)  = "prob of not a"
```

> [🔢 Practice with Weather-Traffic](./probabilistic_reasoning_numericals.md#problem-1-weather-traffic-axioms) | [🔝 Top](#-section-index) | [Next →](#4-bayes-rule)

---

## 4. Bayes' Rule

> [← Prev](#3-probability-axioms--rules) | [📋 INDEX](./probabilistic_reasoning_index.md) | [Next →](#5-inference-using-full-joint-distribution)

### Easy Story 🍼

You know that 80% of people with cavities get toothaches. A patient has a toothache. But you want to know the REVERSE: what's the chance they have a cavity? Bayes' rule lets you flip the direction! If you know "prob of toothache given cavity," Bayes tells you "prob of cavity given toothache."

### The Formula (mnemonic: BAIL)

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│           P(b | a) = P(a | b) · P(b)                         │
│                      ─────────────────                       │
│                           P(a)                               │
│                                                              │
│  WHERE:                                                      │
│  P(b|a)  = POSTERIOR  = what we WANT                         │
│  P(a|b)  = LIKELIHOOD = how likely is evidence given b       │
│  P(b)    = PRIOR      = initial belief about b               │
│  P(a)    = EVIDENCE   = total probability of seeing a        │
│                                                              │
│  MNEMONIC: B.A.I.L.                                          │
│  Bayes = (A given B) × Initial / Likelihood-of-evidence      │
└──────────────────────────────────────────────────────────────┘
```

### How It's Derived

```
  From product rule, two forms:
  P(a ∧ b) = P(a | b) · P(b)     ... form 1
  P(a ∧ b) = P(b | a) · P(a)     ... form 2

  Both equal P(a∧b), so:
  P(b | a) · P(a) = P(a | b) · P(b)

  Divide both sides by P(a):
  P(b | a) = P(a | b) · P(b) / P(a)     ← BAYES' RULE! 🎉
```

### Chain Rule (Extension of Product Rule)

```
  2 variables: P(a ∧ b) = P(a|b) · P(b)

  3 variables: P(a ∧ b ∧ c) = P(a | b ∧ c) · P(b | c) · P(c)

  n variables: P(x1, x2, ..., xn)
             = P(x1 | x2,...,xn) · P(x2 | x3,...,xn) · ... · P(xn)

  This is just repeatedly applying product rule!
```

> [🔝 Top](#-section-index) | [Next →](#5-inference-using-full-joint-distribution)

---

## 5. Inference Using Full Joint Distribution

> [← Prev](#4-bayes-rule) | [📋 INDEX](./probabilistic_reasoning_index.md) | [Next →](#6-independence)

### Easy Story 🍼

Imagine you have a GIANT TABLE that lists the probability of every possible combination of Toothache, Cavity, and Catch. From this one table, you can answer ANY question — like "what's P(cavity)?" or "what's P(cavity|toothache)?" You just need two tricks: **marginalization** (adding up rows) and **conditioning** (dividing after adding).

### The Two Power Tools

```
┌──────────────────────────────────────────────────────────────────┐
│  TOOL 1: MARGINALIZATION (Summing Out)                           │
│  "To find P(X), sum over ALL values of the other variable Y"     │
│                                                                  │
│  P(X) = Σ_{y ∈ Y} P(X, y)                                        │
│                                                                  │
│  Example: P(sunny) = P(sunny,more) + P(sunny,less)               │
│                    = 0.05 + 0.55 = 0.6                           │
├──────────────────────────────────────────────────────────────────┤
│  TOOL 2: CONDITIONING                                            │
│  "To find P(X), split over all values of Y using conditional"    │
│                                                                  │
│  P(X) = Σ_{y ∈ Y} P(X | y) · P(y)                                │
│                                                                  │
│  This is marginalization + product rule combined!                │
└──────────────────────────────────────────────────────────────────┘

  Mnemonic: MC = Marginalize, Condition
```

### The Toothache-Cavity-Catch Joint Table

```
  ┌──────────┬───────────┬────────┬────────┐
  │          │           │ catch  │¬catch  │
  ├──────────┼───────────┼────────┼────────┤
  │ cavity   │ toothache │ 0.108  │ 0.012  │
  │ cavity   │¬toothache │ 0.072  │ 0.008  │
  │ ¬cavity  │ toothache │ 0.016  │ 0.064  │
  │ ¬cavity  │¬toothache │ 0.144  │ 0.576  │
  └──────────┴───────────┴────────┴────────┘
  Total = 1.0 ✓     (8 entries for 3 Boolean vars = 2³)

  From this table we can extract ANY probability:
  P(cavity) = 0.108 + 0.012 + 0.072 + 0.008 = 0.2
  P(toothache) = 0.108 + 0.012 + 0.016 + 0.064 = 0.2
  P(¬catch) = 0.012 + 0.008 + 0.064 + 0.576 = 0.66
```

> [🔢 Toothache-Cavity Practice](./probabilistic_reasoning_numericals.md#problem-2-toothache-cavity-catch-joint-table) | [🔝 Top](#-section-index) | [Next →](#6-independence)

---

## 6. Independence

> [← Prev](#5-inference-using-full-joint-distribution) | [📋 INDEX](./probabilistic_reasoning_index.md) | [Next →](#7-conditional-independence)

### Easy Story 🍼

Whether it rains today has NOTHING to do with whether you have a cavity. Knowing it's rainy doesn't change your belief about cavities at all. These two things are **independent** — they don't affect each other.

### Formal Definition

```
  Two events a, b are INDEPENDENT (a ⫫ b) if ANY of these hold:
  ┌──────────────────────────────────────────────────┐
  │  P(a | b) = P(a)         knowing b doesn't help  │
  │  P(b | a) = P(b)         knowing a doesn't help  │
  │  P(a ∧ b) = P(a) · P(b) joint = product          │
  └──────────────────────────────────────────────────┘
  ALL THREE ARE EQUIVALENT. Prove any one → others follow.

  For VARIABLES X, Y:
  X ⫫ Y  means  P(X, Y) = P(X) · P(Y)
```

### Why Independence is Powerful

```
  WITHOUT independence:
  P(Weather, Toothache, Catch, Cavity)
  = 4 × 2 × 2 × 2 = 32 entries needed!

  WITH independence (Weather ⫫ dental stuff):
  P(Weather, Toothache, Catch, Cavity)
  = P(Weather) · P(Toothache, Catch, Cavity)
  = 4 entries + 8 entries = 12 entries!   (saved 20 entries!)

  ┌─────────────────────────────────────────────┐
  │    Cavity                                   │
  │   Toothache  Catch     Weather              │
  │   ╰──── connected ─────╯  ╰── separate ──╯  │
  │                                             │
  │   decomposes into:                          │
  │                                             │
  │    Cavity                                   │
  │   Toothache  Catch    +    Weather          │
  │   (8 entries)              (4 entries)      │
  └─────────────────────────────────────────────┘
```

> [🔝 Top](#-section-index) | [Next →](#7-conditional-independence)

---

## 7. Conditional Independence

> [← Prev](#6-independence) | [📋 INDEX](./probabilistic_reasoning_index.md) | [Next →](#8-naive-bayes-model)

### Easy Story 🍼

Toothache and Catch (the dentist probe catching) are NOT completely independent — both are related to Cavity. BUT once you KNOW whether there's a cavity, they become independent! The toothache comes from nerves; the catch depends on dentist's skill. Cavity is the common cause linking them, and once you know the cause, the effects don't tell you about each other.

### Formal Definition

```
  X ⫫ Y | Z    means "X and Y are independent GIVEN Z"

  ┌──────────────────────────────────────────────────────────────┐
  │  EQUIVALENT FORMS (any one implies the others):              │
  │                                                              │
  │  P(X, Y | Z) = P(X | Z) · P(Y | Z)                           │
  │  P(X | Y, Z) = P(X | Z)      ← Y adds no info if Z known     │
  │  P(Y | X, Z) = P(Y | Z)      ← X adds no info if Z known     │
  └──────────────────────────────────────────────────────────────┘

  Dentistry Example:
  Toothache ⫫ Catch | Cavity

  P(Toothache | Catch, Cavity) = P(Toothache | Cavity)
  "If I already know whether there's a cavity,
   learning the probe caught doesn't change my
   belief about toothache."
```

### Power of Conditional Independence

```
  P(Toothache, Catch, Cavity)
  = P(Toothache | Catch, Cavity) · P(Catch, Cavity)    ...product rule
  = P(Toothache | Cavity) · P(Catch | Cavity) · P(Cavity)
    ╰──── cond.indep. ─────╯

  This decomposition = MUCH smaller tables!
```

### More Examples

```
  Traffic, Rain, Umbrella:
  T ⫫ U | R      "Given rain status, traffic doesn't affect umbrella use"
                  Rain → Traffic (rain causes traffic)
                  Rain → Umbrella (rain causes umbrella)
                  Traffic and Umbrella: no direct effect on each other!

  Fire, Smoke, Alarm:
  F ⫫ A | S      "Given smoke status, knowing fire doesn't change alarm belief"
                  Fire → Smoke → Alarm (chain)
                  Once you know about smoke, fire info is redundant for alarm
```

> [🔝 Top](#-section-index) | [Next →](#8-naive-bayes-model)

---

## 8. Naive Bayes Model

> [← Prev](#7-conditional-independence) | [📋 INDEX](./probabilistic_reasoning_index.md) | [Next →](#9-bayesian-networks--syntax)

### Easy Story 🍼

One CAUSE (like Cavity) creates many EFFECTS (Toothache, Catch, Bad-Breath, ...). All effects depend on the cause but not directly on each other. This "one cause, many independent effects" pattern is called **Naive Bayes** — "naive" because we ASSUME effects are independent given the cause (even if in reality they might not be perfectly independent).

### The Formula

```
  P(Cause, Effect₁, Effect₂, ..., Effectₙ)
  = P(Cause) × Π_i P(Effectᵢ | Cause)

  ┌──────────────────────────────────────────────────┐
  │         Cause                                    │
  │        ╱  |  ╲                                   │
  │       ▼   ▼   ▼                                  │
  │    Eff₁  Eff₂  Eff₃                             │
  │                                                  │
  │    All effects conditionally independent         │
  │    given the cause.                              │
  └──────────────────────────────────────────────────┘

  Also called: Bayesian classifier
  Used in: Spam detection, text classification, medical diagnosis
```

> [🔝 Top](#-section-index) | [Next →](#9-bayesian-networks--syntax)

---

## 9. Bayesian Networks — Syntax

> [← Prev](#8-naive-bayes-model) | [📋 INDEX](./probabilistic_reasoning_index.md) | [Next →](#10-bn-semantics--cpts)

### Easy Story 🍼

The full joint distribution table gets HUGE as you add variables. 5 Boolean variables = 2⁵ = 32 rows. 10 variables = 1024 rows! Bayesian Networks are a SMART SHORTCUT — instead of one giant table, you draw a picture (a graph) showing which variables CAUSE which, and store only small tables for each connection. Way less storage, same information!

### What IS a Bayesian Network?

Other names: belief network, probabilistic network, causal network, knowledge map.

### BN Syntax — 3 Rules

```
┌──────────────────────────────────────────────────────────────────┐
│  RULE 1: Each NODE = a random variable (discrete or continuous)  │
│                                                                  │
│  RULE 2: ARROWS (directed links) = cause → effect                │
│          • Arrow from Y to X means Y is a PARENT of X            │
│          • NO DIRECTED CYCLES (it's a DAG!)                      │
│          • "Cause precedes Effect"                               │
│                                                                  │
│  RULE 3: Each node Xᵢ has a CPT: P(Xᵢ | parents(Xᵢ))             │
│          This table says: "given my parents' states,             │
│          what's the prob of my different states?"                │
└──────────────────────────────────────────────────────────────────┘

  DAG = Directed Acyclic Graph
  Directed = arrows have direction (cause → effect)
  Acyclic = no loops (can't follow arrows and end up where you started)
```

### The Burglary Network — Step by Step Construction

```
  STORY: You have a burglar alarm at home. It detects burglaries
  but ALSO goes off for minor earthquakes. Two neighbors, John
  and Mary, promised to call you at work if they hear the alarm.

  STEP 1: Identify variables (nodes)
  → Burglary, Earthquake, Alarm, JohnCalls, MaryCalls

  STEP 2: Identify cause→effect relationships (arrows)
  → Burglary and Earthquake: NO parents (root causes)
  → Alarm: CAUSED BY Burglary and Earthquake
  → JohnCalls: CAUSED BY Alarm
  → MaryCalls: CAUSED BY Alarm

  STEP 3: Draw the DAG

              Burglary        Earthquake
                 ╲              ╱
                  ╲            ╱
                   ▼          ▼
                    Alarm
                   ╱     ╲
                  ╱       ╲
                 ▼         ▼
            JohnCalls    MaryCalls

  Causality flows TOP → DOWN

  STEP 4: Add CPTs (next section)
```

### Conditional Independencies in this BN

```
  JohnCalls ⫫ Burglary | Alarm
  JohnCalls ⫫ Earthquake | Alarm
  MaryCalls ⫫ Burglary | Alarm
  MaryCalls ⫫ Earthquake | Alarm
  JohnCalls ⫫ MaryCalls | Alarm

  In plain English:
  "Once you know whether the alarm rang,
   knowing about burglary/earthquake doesn't
   change your belief about John/Mary calling."
```

> [🔢 Build BN Practice](./probabilistic_reasoning_numericals.md#problem-4-burglary-alarm-bn-construction) | [🧠 BN Inference Deep Dive: Theory](https://github.com/rpaut03l/TS-01/blob/main/AI/SD-M/Bayesian-Network-(BN)-Inference/bn_inference_theory.md) | [🔝 Top](#-section-index) | [Next →](#10-bn-semantics--cpts)

---

## 10. BN Semantics & CPTs

> [← Prev](#9-bayesian-networks--syntax) | [📋 INDEX](./probabilistic_reasoning_index.md) | [Next →](#11-markov-blanket)

### Easy Story 🍼

Each node in the network has a little table (CPT) that says "IF my parents are in THIS state, THEN here's my probability." Root nodes (no parents) just have a simple probability. Nodes with one parent have a 2-row table. Nodes with two parents have a 4-row table. And so on.

### The Full CPTs for Burglary Network

```
  P(B):  Burglary (no parents — just a prior)
  ┌────────┬──────────┐
  │  P(b)  │  P(¬b)   │
  ├────────┼──────────┤
  │ 0.001  │  0.999   │
  └────────┴──────────┘

  P(E):  Earthquake (no parents — just a prior)
  ┌────────┬──────────┐
  │  P(e)  │  P(¬e)   │
  ├────────┼──────────┤
  │ 0.002  │  0.998   │
  └────────┴──────────┘

  P(A|B,E):  Alarm (2 parents → 4 rows)
  ┌─────┬─────┬────────┬─────────┐
  │  B  │  E  │  P(a)  │  P(¬a)  │
  ├─────┼─────┼────────┼─────────┤
  │  t  │  t  │  0.95  │  0.05   │
  │  t  │  f  │  0.94  │  0.06   │
  │  f  │  t  │  0.29  │  0.71   │
  │  f  │  f  │  0.001 │  0.999  │
  └─────┴─────┴────────┴─────────┘

  P(J|A):  JohnCalls (1 parent → 2 rows)
  ┌─────┬────────┬─────────┐
  │  A  │  P(j)  │  P(¬j)  │
  ├─────┼────────┼─────────┤
  │  t  │  0.90  │  0.10   │
  │  f  │  0.05  │  0.95   │
  └─────┴────────┴─────────┘

  P(M|A):  MaryCalls (1 parent → 2 rows)
  ┌─────┬────────┬─────────┐
  │  A  │  P(m)  │  P(¬m)  │
  ├─────┼────────┼─────────┤
  │  t  │  0.70  │  0.30   │
  │  f  │  0.01  │  0.99   │
  └─────┴────────┴─────────┘
```

### Complexity Comparison

```
  ┌──────────────────────────────────────────────────────────────┐
  │  FULL JOINT TABLE for n=5 Boolean variables:                 │
  │  O(2⁵) = 32 entries                                          │
  │                                                              │
  │  CPTs TOTAL for this BN:                                     │
  │  P(B): 1 + P(E): 1 + P(A|B,E): 4 + P(J|A): 2 + P(M|A): 2     │
  │  = 10 entries!   (saved 22 entries = 69% reduction!)         │
  │                                                              │
  │  GENERAL WORST-CASE:                                         │
  │  n Boolean vars, each with at most m parents:                │
  │  CPTs need O(n · 2^m) entries                                │
  │  vs Full Joint: O(2^n) entries                               │
  │                                                              │
  │  When m << n, BN is MASSIVELY more efficient!                │
  └──────────────────────────────────────────────────────────────┘
```

### Key Rule: Each CPT Row Sums to 1

```
  P(a|B,E) + P(¬a|B,E) = 1   for each (B,E) combination

  Example: P(a|b,e) + P(¬a|b,e) = 0.95 + 0.05 = 1 ✓

  WHY? Because given the parents' state, the node MUST be
  in one of its states. It's exhaustive!
```

### Proof: P(¬A|B) = 1 - P(A|B)

```
  P(¬A|B) = P(¬A ∧ B) / P(B)              ...definition
          = (P(B) - P(A ∧ B)) / P(B)       ...complement in B's world
          = 1 - P(A ∧ B)/P(B)
          = 1 - P(A|B)                      ...definition again

  Extendable:
  P(¬A | B, C) = 1 - P(A | B, C)
  P(¬A | B, C, ..., N) = 1 - P(A | B, C, ..., N)
```

> [🔝 Top](#-section-index) | [Next →](#11-markov-blanket)

---

## 11. Markov Blanket

> [← Prev](#10-bn-semantics--cpts) | [📋 INDEX](./probabilistic_reasoning_index.md) | [Next →](#12-obtaining-full-joint-from-bn)

### Easy Story 🍼

Imagine you're node X in the network. Your "Markov Blanket" is like a protective bubble around you. It includes your parents (who directly cause you), your children (who you directly cause), and your children's other parents (who team up with you to cause your children). Once you know the state of everyone in this bubble, you don't need to know ANYTHING about the rest of the network!

### Definition (mnemonic: PCK)

```
  MARKOV BLANKET of node X = { Parents, Children, Kids'-parents }

  ┌──────────────────────────────────────────────────┐
  │         U₁  ...  Uₘ    ← Parents of X            │
  │          ╲       ╱                               │
  │     Z₁ₖ  ╲     ╱  Zₙₖ ← Children's OTHER          │
  │       ╲    ╲   ╱    ╱     Parents (co-parents)   │
  │        ╲    ▼ ▼    ╱                             │
  │         ╲  [ X ]  ╱    ← THE NODE itself         │
  │          ╲╱     ╲╱                               │
  │          ╱╲     ╱╲                               │
  │         ▼         ▼                              │
  │        Y₁  ...  Yₙ    ← Children of X            │
  │                                                  │
  │  Gray area = Markov Blanket                      │
  │                                                  │
  │  KEY RULE:                                       │
  │  X ⫫ (ALL other nodes) | Markov Blanket(X)       │
  │                                                  │
  │  "Given its blanket, X is conditionally          │
  │   independent of EVERYTHING else!"               │
  └──────────────────────────────────────────────────┘
```

### Example: Burglary Network

```
  Markov Blanket of Alarm:
  • Parents: Burglary, Earthquake
  • Children: JohnCalls, MaryCalls
  • Children's other parents: none (J and M only have Alarm as parent)
  → MB(Alarm) = {Burglary, Earthquake, JohnCalls, MaryCalls}
  → That's ALL nodes! (because Alarm is central)

  Markov Blanket of JohnCalls:
  • Parents: Alarm
  • Children: none
  • Children's other parents: none
  → MB(JohnCalls) = {Alarm}
  → Given Alarm's state, John doesn't care about anything else!
```

> [🔝 Top](#-section-index) | [Next →](#12-obtaining-full-joint-from-bn)

---

## 12. Obtaining Full Joint from BN

> [← Prev](#11-markov-blanket) | [📋 INDEX](./probabilistic_reasoning_index.md) | [Next →](#13-inference--formal-definition)

### Easy Story 🍼

Even though we store only small CPTs, we CAN reconstruct the full joint table if needed. The trick: multiply together each node's CPT entry for the given assignment. It's like a recipe — each ingredient (CPT) contributes its piece, and the product is the full joint probability.

### The Master Formula

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  P(X₁, X₂, ..., Xₙ) = Π_{i=1}^{n} P(Xᵢ | parents(Xᵢ))        │
│                                                              │
│  "Joint prob of everything = product of each node's CPT      │
│   entry, using that node's parents as the condition."        │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

### How This Works (Derivation Sketch)

```
  Start with chain rule:
  P(X₁, X₂, ..., Xₙ) = P(X₁|X₂,...,Xₙ) · P(X₂|X₃,...,Xₙ) · ... · P(Xₙ)

  BN says: each Xᵢ is conditionally independent of non-parents given parents.
  So: P(Xᵢ | all predecessors) simplifies to P(Xᵢ | parents(Xᵢ))

  That's why the product works!
```

### Node Ordering Rule

```
  ┌──────────────────────────────────────────────────────────────┐
  │  IMPORTANT: When writing the product, list EFFECT nodes      │
  │  BEFORE their CAUSE nodes.                                   │
  │                                                              │
  │  For Burglary network:                                       │
  │  Order: JohnCalls, MaryCalls, Alarm, Burglary, Earthquake    │
  │  (effects first, causes last)                                │
  │                                                              │
  │  Mnemonic: NODE = effects down, causes elevated              │
  └──────────────────────────────────────────────────────────────┘
```

### Worked Example

```
  P(j, m, a, ¬b, ¬e) = ?

  Step 1: Identify each node's CPT entry:
  • P(j | a)    = 0.90   (JohnCalls=t given Alarm=t)
  • P(m | a)    = 0.70   (MaryCalls=t given Alarm=t)
  • P(a | ¬b,¬e)= 0.001  (Alarm=t given no burglary, no earthquake)
  • P(¬b)       = 0.999  (no burglary)
  • P(¬e)       = 0.998  (no earthquake)

  Step 2: Multiply:
  = 0.90 × 0.70 × 0.001 × 0.999 × 0.998
  = 0.000628
```

> [🔢 Joint Entry Practice](./probabilistic_reasoning_numericals.md#problem-7-joint-entry-pjma¬b¬e) | [🧠 BN Numericals: More Problems](https://github.com/rpaut03l/TS-01/blob/main/AI/SD-M/Bayesian-Network-(BN)-Inference/bn_inference_numericals.md) | [🔝 Top](#-section-index) | [Next →](#13-inference--formal-definition)

---

## 13. Inference — Formal Definition

> [← Prev](#12-obtaining-full-joint-from-bn) | [📋 INDEX](./probabilistic_reasoning_index.md) | [Next →](#14-normalization-constant-α)

### Easy Story 🍼

In any probability question, there are three types of players: the thing you're ASKING about (query), the things you already KNOW (evidence), and the things you DON'T know and need to sum over (hidden). Inference = finding the answer by combining these three.

### The Three Variable Types

```
  Example: P(Burglary | JohnCalls=t, MaryCalls=t)

  ┌─────────────────────────────────────────────────────┐
  │  X = Query Variables     = {Burglary}               │
  │      "What I'm asking about"                        │
  │                                                     │
  │  E = Evidence Variables  = {JohnCalls, MaryCalls}   │
  │      e = {j=t, m=t}  (specific observed values)     │
  │      "What I already know"                          │
  │                                                     │
  │  Y = Hidden Variables    = {Alarm, Earthquake}      │
  │      "What I don't know and need to sum over"       │
  └─────────────────────────────────────────────────────┘
```

### The Inference Formula

```
  ┌──────────────────────────────────────────────────────┐
  │                                                      │
  │  P(X | e) = α · P(X, e) = α · Σ_y P(X, e, y)         │
  │                                                      │
  │  WHERE:                                              │
  │  α = 1/P(e) = normalization constant                 │
  │  Σ_y = sum over ALL combinations of hidden vars      │
  │  P(X, e, y) = write as product of CPTs from BN       │
  │                                                      │
  └──────────────────────────────────────────────────────┘
```

> [🔝 Top](#-section-index) | [Next →](#14-normalization-constant-α)

---

## 14. Normalization Constant α

> [← Prev](#13-inference--formal-definition) | [📋 INDEX](./probabilistic_reasoning_index.md) | [Next →](#15-exact-inference--enumeration)

### Easy Story 🍼

Imagine you calculate P(cavity, toothache) = 0.192 and P(¬cavity, toothache) = 0.224. These don't add to 1 because they're joint probs, not conditional. But their RATIO is correct! So just scale them so they add to 1. That scaling factor is α. It saves you from computing P(evidence) separately!

### How α Works

```
  P(X | e) = [ P(x|e)  ]   = [ α × P(x,e)  ]
             [ P(¬x|e) ]     [ α × P(¬x,e) ]

  Since P(x|e) + P(¬x|e) = 1:
  α × P(x,e) + α × P(¬x,e) = 1
  α × (P(x,e) + P(¬x,e)) = 1
  α = 1 / (P(x,e) + P(¬x,e)) = 1/P(e)

  EXAMPLE:
  P(x,e) = 0.192    P(¬x,e) = 0.224
  α = 1/(0.192 + 0.224) = 1/0.416

  P(x|e)  = 0.192/0.416 = 0.4615
  P(¬x|e) = 0.224/0.416 = 0.5385
  Sum = 1.0 ✓

  ┌───────────────────────────────────────────────────┐
  │  TRICK: You don't need to compute P(e) directly!  │
  │  Just compute the unnormalized values, then       │
  │  divide each by their sum.                        │
  └───────────────────────────────────────────────────┘
```

> [🔢 Normalization Practice](./probabilistic_reasoning_numericals.md#problem-11-pcavity--toothache--catch) | [🔝 Top](#-section-index) | [Next →](#15-exact-inference--enumeration)

---

## 15. Exact Inference — Enumeration

> [← Prev](#14-normalization-constant-α) | [📋 INDEX](./probabilistic_reasoning_index.md) | [Next →](#16-exact-inference--variable-elimination)

### Easy Story 🍼

Enumeration means: "try every possible combination of hidden variables, compute each product, add them all up." It's like checking every single path through the network. Correct but slow — the number of combos explodes!

### How Enumeration Works

```
  GOAL: P(b | j, m) = α × Σ_{a,e} P(j|a) P(m|a) P(a|b,e) P(b) P(e)

  We enumerate ALL combos of (a, e):
  ┌──────┬──────┬────────────────────────────────────────────────────────┐
  │  a   │  e   │ P(j|a) × P(m|a) × P(a|b,e) × P(b) × P(e)               │
  ├──────┼──────┼────────────────────────────────────────────────────────┤
  │  t   │  t   │ 0.9 × 0.7 × 0.95 × 0.001 × 0.002 = 0.000001197         │
  │  t   │  f   │ 0.9 × 0.7 × 0.94 × 0.001 × 0.998 = 0.000591156         │
  │  f   │  t   │ 0.05× 0.01× 0.05 × 0.001 × 0.002 = 0.000000000050      │
  │  f   │  f   │ 0.05× 0.01× 0.06 × 0.001 × 0.998 = 0.000000029940      │
  └──────┴──────┴────────────────────────────────────────────────────────┘
  Sum ≈ 0.00059224

  COST: 16 multiplications + 3 additions (for ONE value of B)
  For BOTH b and ¬b: 32 multiplications + 6 additions
  Gets MUCH worse with more variables!
```

> [🔢 Full Enumeration Example](./probabilistic_reasoning_numericals.md#problem-8-pburglary--jm--enumeration) | [🧠 BN Inference: Extended Enumeration](https://github.com/rpaut03l/TS-01/blob/main/AI/SD-M/Bayesian-Network-(BN)-Inference/bn_inference_theory.md) | [🔝 Top](#-section-index) | [Next →](#16-exact-inference--variable-elimination)

---

## 16. Exact Inference — Variable Elimination

> [← Prev](#15-exact-inference--enumeration) | [📋 INDEX](./probabilistic_reasoning_index.md) | [Next →](#17-approximate-inference-overview)

### Easy Story 🍼

You need to calculate: 2 × 3 × 5 + 2 × 3 × 7 + 2 × 3 × 9

The DUMB way: do each multiplication from scratch (9 multiplications).

The SMART way: notice "2 × 3" repeats! Calculate 2 × 3 = 6 ONCE, then: 6×5 + 6×7 + 6×9 (only 4 multiplications). Same answer, less work!

**Variable Elimination does exactly this with probability terms.**

### The Key Idea

```
  We want: Σ_{a,e} P(j|a) × P(m|a) × P(a|b,e) × P(b) × P(e)

  DUMB WAY (Enumeration):
  Try all 4 combos of (a,e), multiply everything each time.
  → 16 multiplications, 3 additions

  SMART WAY (Variable Elimination):
  Notice P(b) appears in EVERY term. Don't multiply it 4 times!
  Pull it out and multiply ONCE at the end.

  Step 1: Handle the INNER part first (terms with 'a')
          Σ_a P(a|b,e) × P(j|a) × P(m|a) = some number f₆
          (only 2 values of a, so quick!)

  Step 2: Handle the MIDDLE part (terms with 'e')
          Σ_e P(e) × f₆ = some number f₇
          (only 2 values of e, so quick!)

  Step 3: Final answer
          P(b) × f₇ = done!

  → 7 multiplications, 2 additions (way less than 16+3!)

  RULE: If something doesn't change inside the sum,
        pull it OUTSIDE and multiply once at the end.
```

### Factor Notation

```
  Each probability term becomes a FACTOR (a vector/matrix of values):

  f₁(B) = P(B)         = [P(b), P(¬b)]     = [0.001, 0.999]
  f₂(E) = P(E)         = [P(e), P(¬e)]     = [0.002, 0.998]
  f₃(A,B,E) = P(A|B,E) = 4×2 matrix (A has 2 vals for each B,E combo)
  f₄(A) = P(j|A)       = [P(j|a), P(j|¬a)] = [0.90, 0.05]
  f₅(A) = P(m|A)       = [P(m|a), P(m|¬a)] = [0.70, 0.01]

  (J and M are fixed to true by the query, so f₄ and f₅ depend only on A)
```

### Point-wise Multiplication

```
  Multiplying two factors:  f₁(A,B) × f₂(B,C) = f₃(A,B,C)

  Example:
  ┌───┬───┬──────────┐   ┌───┬───┬──────────┐   ┌───┬───┬───┬────────────────┐
  │ A │ B │ f₁(A,B)  │   │ B │ C │ f₂(B,C)  │   │ A │ B │ C │ f₃(A,B,C)      │
  ├───┼───┼──────────┤   ├───┼───┼──────────┤   ├───┼───┼───┼────────────────┤
  │ T │ T │   .3     │   │ T │ T │   .2     │   │ T │ T │ T │ .3×.2 = .06    │
  │ T │ F │   .7     │   │ T │ F │   .8     │   │ T │ T │ F │ .3×.8 = .24    │
  │ F │ T │   .9     │   │ F │ T │   .6     │   │ T │ F │ T │ .7×.6 = .42    │
  │ F │ F │   .1     │   │ F │ F │   .4     │   │ T │ F │ F │ .7×.4 = .28    │
  └───┴───┴──────────┘   └───┴───┴──────────┘   │ F │ T │ T │ .9×.2 = .18    │
                                                  │ F │ T │ F │ .9×.8 = .72  │
  Match on SHARED variable (B),                   │ F │ F │ T │ .1×.6 = .06  │
  multiply the values.                            │ F │ F │ F │ .1×.4 = .04  │
  Counts as ONE multiplication operation!         └───┴───┴───┴──────────────┘
```

### The 3 Steps for P(B|j,m)

```
  P(B|j,m) = α · f₁(B) × Σ_e f₂(E) × Σ_a f₃(A,B,E) × f₄(A) × f₅(A)

  ┌──────────────────────────────────────────────────────────────────┐
  │  STEP 1: Sum out A (innermost sum)                               │
  │  f₆(B,E) = Σ_a f₃(A,B,E) × f₄(A) × f₅(A)                         │
  │                                                                  │
  │  = f₃(a,B,E)×f₄(a)×f₅(a) + f₃(¬a,B,E)×f₄(¬a)×f₅(¬a)              │
  │                                                                  │
  │  → Result: a 2×2 factor over (B,E)                               │
  │  COST: 4 multiplications + 1 addition                            │
  ├──────────────────────────────────────────────────────────────────┤
  │  STEP 2: Sum out E                                               │
  │  f₇(B) = Σ_e f₂(E) × f₆(B,E)                                     │
  │                                                                  │
  │  = f₂(e)×f₆(B,e) + f₂(¬e)×f₆(B,¬e)                               │
  │                                                                  │
  │  → Result: a 2-element factor over B                             │
  │  COST: 2 multiplications + 1 addition                            │
  ├──────────────────────────────────────────────────────────────────┤
  │  STEP 3: Final multiply                                          │
  │  P(B|j,m) = α · f₁(B) × f₇(B)                                    │
  │                                                                  │
  │  → Result: 2-element vector, normalize to get answer             │
  │  COST: 1 multiplication                                          │
  └──────────────────────────────────────────────────────────────────┘

  ┌──────────────────────────────────────────────┐
  │  TOTAL COST COMPARISON:                      │
  │                                              │
  │  Enumeration:           32 mul + 6 add       │
  │  Variable Elimination:   7 mul + 2 add       │
  │                                              │
  │  VE is 4-5× faster here, and the gap grows   │
  │  EXPONENTIALLY with more variables!          │
  └──────────────────────────────────────────────┘
```

### Mnemonic: FAVE

```
  F = Factors — identify all CPT factors
  A = Assign — assign observed variables their values
  V = Variable sum-out — sum out hidden vars one by one (innermost first)
  E = Evaluate — final pointwise multiply + normalize
```

> [🔢 VE Practice](./probabilistic_reasoning_numericals.md#problem-9-pb--jm--variable-elimination) | [🧠 BN Inference: Extended VE + Practice](https://github.com/rpaut03l/TS-01/blob/main/AI/SD-M/Bayesian-Network-(BN)-Inference/bn_inference_practice.md) | [🔝 Top](#-section-index) | [Next →](#17-approximate-inference-overview)

---

## 17. Approximate Inference (Overview)

> [← Prev](#16-exact-inference--variable-elimination) | [📋 INDEX](./probabilistic_reasoning_index.md)

### Easy Story 🍼

Even Variable Elimination can be slow for VERY large networks. Approximate methods say: "instead of computing exact numbers, let's SIMULATE the network many times and count how often things happen." Like flipping coins to estimate probabilities!

### Methods at a Glance

```
┌──────────────────────────────────────────────────────────────────┐
│  APPROXIMATE INFERENCE METHODS                                   │
│                                                                  │
│  A. DIRECT SAMPLING (generate samples from the network):         │
│                                                                  │
│     1. PRIOR SAMPLING                                            │
│        Sample all variables top-down using CPTs                  │
│        Count how often query matches                             │
│        Problem: might never generate the evidence!               │
│                                                                  │
│     2. REJECTION SAMPLING                                        │
│        Same as prior, but THROW AWAY samples that                │
│        don't match the evidence                                  │
│        Problem: throws away too many samples!                    │
│                                                                  │
│     3. LIKELIHOOD WEIGHTING                                      │
│        Fix evidence variables, sample rest normally              │
│        Weight each sample by evidence likelihood                 │
│        Better than rejection (no wasted samples)                 │
│                                                                  │
│  B. MARKOV CHAIN SAMPLING:                                       │
│                                                                  │
│     4. GIBBS SAMPLING                                            │
│        Start with random assignment                              │
│        Repeatedly resample ONE variable at a time                │
│        Using its Markov Blanket probabilities                    │
│        Eventually converges to correct distribution              │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

> **Note:** Detailed coverage of approximate methods is in the next unit AND in the dedicated BN Inference guides:
> [🧠 BN Inference Theory (Full Coverage)](../SD-M/Bayesian-Network-(BN)-Inference/bn_inference_theory.md) | [🏋️ BN Practice Problems](../SD-M/Bayesian-Network-(BN)-Inference/bn_inference_practice.md)

---

## 🧩 Complete Cheat Sheet

```
╔══════════════════════════════════════════════════════════════════╗
║  PROBABILISTIC REASONING — EXAM CHEAT SHEET                      ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  BASIC RULES:                                                    ║
║  P(a|b) = P(a∧b)/P(b)                 ...conditional def         ║
║  P(a∧b) = P(a|b)·P(b)                ...product rule             ║
║  P(a∨b) = P(a)+P(b)-P(a∧b)          ...inclusion-exclusion       ║
║  P(¬a) = 1-P(a)                       ...complement              ║
║  P(a∧¬b) = P(a)-P(a∧b)              ...set difference            ║
║                                                                  ║
║  BAYES:                                                          ║
║  P(b|a) = P(a|b)·P(b)/P(a)           ...flip the conditional     ║
║                                                                  ║
║  CHAIN: P(a,b,c) = P(a|b,c)·P(b|c)·P(c)                          ║
║                                                                  ║
║  INFERENCE TOOLS:                                                ║
║  Marginalization: P(X) = Σ_y P(X,y)                              ║
║  Conditioning:    P(X) = Σ_y P(X|y)·P(y)                         ║
║                                                                  ║
║  INDEPENDENCE:     P(a,b) = P(a)·P(b)                            ║
║  COND. INDEP.:    P(X,Y|Z) = P(X|Z)·P(Y|Z)                       ║
║                                                                  ║
║  BAYESIAN NETWORK:                                               ║
║  Joint = Π P(Xᵢ|parents(Xᵢ))                                     ║
║  CPT complexity: O(n·2^m) vs Joint: O(2^n)                       ║
║                                                                  ║
║  MARKOV BLANKET = Parents + Children + Children's Parents        ║
║  Given MB, node is independent of ALL others!                    ║
║                                                                  ║
║  INFERENCE:                                                      ║
║  P(X|e) = α·Σ_y P(X,e,y)    where α = 1/P(e)                     ║
║  Enumeration: expand all combos (O(2^n) work)                    ║
║  VarElim: factor + sum-out right-to-left (O(n·2^m) work)         ║
║                                                                  ║
║  α TRICK: compute unnormalized, then divide by sum               ║
║                                                                  ║
║  NEGATION UNDER CONDITIONING:                                    ║
║  P(¬A|B,...,N) = 1 - P(A|B,...,N)                                ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## 🎯 Exam Hacks

```
  1. ALWAYS draw the BN first — it makes everything clear
  2. For P(something), use CONDITIONING to break it down via parents
  3. If B and E are independent root nodes: P(b,e) = P(b)·P(e)
  4. Use α trick to avoid computing P(evidence) directly
  5. For VE: identify factors, work RIGHT-TO-LEFT, sum out innermost variable first
  6. CPT row always sums to 1: P(a|parents) + P(¬a|parents) = 1
  7. When asked "how many CPT entries": count rows × independent probs per row
  8. Markov Blanket question: PCK = Parents + Children + Kids'-parents
  9. For chain rule with n variables: you get n-1 conditional terms + 1 unconditional
  10. Check: does your answer make intuitive sense? (P(burglary|j,m) should be small!)
```

---

> **Navigation:** [📋 INDEX](./probabilistic_reasoning_index.md) | [🔢 NUMERICALS](./probabilistic_reasoning_numericals.md) | [🧠 BN Inference Deep Dive](https://github.com/rpaut03l/TS-01/blob/main/AI/SD-M/Bayesian-Network-(BN)-Inference/bn_inference_index.md)
>
> **Ref:** Russell & Norvig — AI: A Modern Approach (Ch. 13, 14)

[🔝 Back to Top](#-probabilistic-reasoning--theory-guide)
