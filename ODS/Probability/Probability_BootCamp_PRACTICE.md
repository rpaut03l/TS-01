# 🔢 Probability BootCamp — PRACTICE PROBLEMS GUIDE

### 🎓 ODS | ML
> 🔗 **Navigation:** [← Back to INDEX](./Probability_BootCamp_INDEX.md) | [← Theory Guide](./Probability_BootCamp_THEORY.md)
>
> 🍎 Every step explained from scratch. Nothing assumed.

---

## 📚 Problem Index

| # | Problem | Concepts | Theory |
|---|---------|----------|--------|
| P1 | [Basic Counting & Coin Flips](#-p1-basic-counting--coin-flips) | Counting, multiplication | [📘 Ch2](./Probability_BootCamp_THEORY.md#chapter-2--counting-coin-flips--dice) |
| P2 | [Permutations & Combinations](#-p2-permutations--combinations) | P(n,r), C(n,k) | [📘 Ch3](./Probability_BootCamp_THEORY.md#chapter-3--combinatorics--factorials) |
| P3 | [Set Theory & Sample Spaces](#-p3-set-theory--sample-spaces) | Union, intersection | [📘 Ch4](./Probability_BootCamp_THEORY.md#chapter-4--set-theory-sample-spaces--events) |
| P4 | [The Birthday Problem](#-p4-the-birthday-problem) | Complement trick | [📘 Ch5](./Probability_BootCamp_THEORY.md#chapter-5--the-birthday-problem) |
| P5 | [Multinomial & Quality Control](#-p5-multinomial--quality-control) | Binomial, multinomial | [📘 Ch6-7](./Probability_BootCamp_THEORY.md#chapter-7--the-binomial-distribution) |
| P6 | [Conditional Probability](#-p6-conditional-probability) | P(A\|B) | [📘 Ch8](./Probability_BootCamp_THEORY.md#chapter-8--conditional-probability) |
| P7 | [Law of Total Probability](#-p7-law-of-total-probability) | Partition, total prob | [📘 Ch9](./Probability_BootCamp_THEORY.md#chapter-9--the-law-of-total-probability) |
| P8 | [Bayes' Theorem](#-p8-bayes-theorem) | Prior, posterior | [📘 Ch10](./Probability_BootCamp_THEORY.md#chapter-10--bayes-theorem) |
| P9 | [Bayes Drug Testing & Medical](#-p9-bayes-drug-testing--medical-screening) | Base rate fallacy | [📘 Ch11](./Probability_BootCamp_THEORY.md#chapter-11--bayes-example-drug-testing) |
| P10 | [Independence](#-p10-independence) | Independent events | [📘 Ch12](./Probability_BootCamp_THEORY.md#chapter-12--independence-in-probability) |
| P11 | [Random Variables & PMF/PDF](#-p11-random-variables--pmfpdf) | Discrete, continuous | [📘 Ch13](./Probability_BootCamp_THEORY.md#chapter-13--random-variables--probability-distributions) |
| P12 | [Bernoulli & Binomial](#-p12-bernoulli--binomial) | Binomial formula | [📘 Ch14](./Probability_BootCamp_THEORY.md#chapter-14--bernoulli--binomial-random-variables) |
| P13 | [Normal Distribution](#-p13-normal-distribution) | Z-scores, 68-95-99.7 | [📘 Ch15-16](./Probability_BootCamp_THEORY.md#chapter-15--the-normal-distribution) |
| P14 | [Poisson Distribution](#-p14-poisson-distribution) | Rare events | [📘 Ch17](./Probability_BootCamp_THEORY.md#chapter-17--the-poisson-distribution) |
| P15 | [Geometric & Exponential](#-p15-geometric--exponential) | Waiting times | [📘 Ch18-19](./Probability_BootCamp_THEORY.md#chapter-18--the-geometric-distribution) |
| P16 | [Gamma & Chi-Squared](#-p16-gamma--chi-squared) | Advanced distributions | [📘 Ch22,25](./Probability_BootCamp_THEORY.md#chapter-22--the-gamma-distribution) |
| P17 | [Joint Distributions & E[X]](#-p17-joint-distributions--expected-value) | Joint, marginal, E[X] | [📘 Ch26-28](./Probability_BootCamp_THEORY.md#chapter-26--joint-probability-distributions) |
| P18 | [Variance & Standard Deviation](#-p18-variance--standard-deviation) | Var, σ | [📘 Ch29](./Probability_BootCamp_THEORY.md#chapter-29--variance--standard-deviation) |
| P19 | [Inequalities, LLN & CLT](#-p19-inequalities--lln--clt) | Markov, Chebyshev, CLT | [📘 Ch30,33](./Probability_BootCamp_THEORY.md#chapter-30--markov--chebyshev-inequalities) |
| P20 | [Covariance & Correlation](#-p20-covariance--correlation) | Cov, ρ | [📘 Ch32](./Probability_BootCamp_THEORY.md#chapter-32--covariance--correlation) |

---

## 📖 FORMULA CHEAT SHEET

```
┌──────────── COUNTING ────────────┐  ┌──────────── PROBABILITY ─────────┐
│ n! = n×(n-1)×...×1.  0!=1        │  │ P(A) = favorable/total           │
│ P(n,r) = n!/(n-r)!               │  │ P(Aᶜ) = 1 − P(A)                 │
│ C(n,k) = n!/[k!(n-k)!]           │  │ P(A∪B) = P(A)+P(B)−P(A∩B)        │
└──────────────────────────────────┘  │ P(A|B) = P(A∩B)/P(B)             │
┌──────────── DISTRIBUTIONS ───────┐  │ Bayes: P(A|B)=P(B|A)P(A)/P(B)    │
│ Binom: C(n,k)pᵏ(1-p)ⁿ⁻ᵏ          │  └──────────────────────────────────┘
│ Poisson: e⁻λ·λᵏ/k!               │  ┌──────────── STATS ───────────────┐
│ Geom: (1-p)ᵏ⁻¹·p                 │  │ E[X]=Σx·P(x)                     │
│ Normal: Z=(X-μ)/σ                │  │ Var=E[X²]−(E[X])²                │
│ Expon: f(x)=λe⁻λˣ                │  │ Cov=E[XY]−E[X]E[Y]               │
└──────────────────────────────────┘  │ ρ=Cov/(σₓσᵧ)                     │
                                      └──────────────────────────────────┘
```

---
---

## 🧮 P1: Basic Counting & Coin Flips

> 📘 [Ch 2](./Probability_BootCamp_THEORY.md#chapter-2--counting-coin-flips--dice) | ⬆️ [Index](#-problem-index)

**Q: (a) Outcomes for 4 coin flips? (b) P(exactly 2H in 4 flips)? (c) P(sum≥10 with two dice)?**

### (a) Total outcomes for 4 coins

```
Each flip: 2 outcomes (H or T). Flips are independent.
Multiplication principle: 2 × 2 × 2 × 2 = 2⁴ = 16

🍎 WHY multiply? Think of a TREE:
   Flip 1 branches into 2 → each branches into 2 → ... → 16 leaves total.
```

### (b) P(exactly 2 Heads)

```
Step 1: "Which 2 of the 4 flips are Heads?" → C(4,2)
  C(4,2) = 4!/(2!·2!) = (4×3)/(2×1) = 6

  The 6 ways: HHTT, HTHT, HTTH, THHT, THTH, TTHH

Step 2: Total = 16.    P = 6/16 = 3/8 = 0.375 ✅

┌─── WHY? ────────────────────────────────────────────────┐
│ This is the BINOMIAL formula with n=4, k=2, p=0.5:      │
│ P(X=2) = C(4,2)·(0.5)²·(0.5)² = 6·0.25·0.25 = 3/8  ✅   │
└─────────────────────────────────────────────────────────┘
```

### (c) P(sum ≥ 10, two dice)

```
Total: 6×6 = 36.
Sum=10: (4,6)(5,5)(6,4) → 3 ways
Sum=11: (5,6)(6,5)       → 2 ways
Sum=12: (6,6)             → 1 way
Favorable = 6.    P = 6/36 = 1/6 ≈ 0.167 ✅

🤖 AI/ML: Counting is the foundation of SAMPLING — every Monte Carlo
   simulation counts favorable vs total outcomes.
```

---

## 🧮 P2: Permutations & Combinations

> 📘 [Ch 3](./Probability_BootCamp_THEORY.md#chapter-3--combinatorics--factorials) | ⬆️ [Index](#-problem-index)

**Q: (a) Arrange 5 books on a shelf. (b) Choose 3 from 8 for a team. (c) P(flush in 5-card poker).**

### (a) Arrange 5 books

```
Order matters (leftmost ≠ rightmost). All 5 books used.
5! = 5×4×3×2×1 = 120 arrangements ✅

🍎 Slot 1: 5 choices → Slot 2: 4 left → 3 → 2 → 1
```

### (b) Choose 3 from 8

```
Order doesn't matter ({A,B,C} = {C,B,A}).
C(8,3) = 8!/(3!·5!) = (8×7×6)/(3×2×1) = 336/6 = 56 ✅

┌─── WHY divide by 3!? ────────────────────────────────────┐
│ P(8,3) = 8×7×6 = 336 counts each GROUP 3! = 6 times      │
│ (ABC, ACB, BAC, BCA, CAB, CBA = 6 orderings of same 3)   │
│ Remove duplicates: 336/6 = 56                            │
└──────────────────────────────────────────────────────────┘
```

### (c) P(flush)

```
Step 1: Total 5-card hands = C(52,5) = 2,598,960
Step 2: Flush = all same suit.
  Pick suit: 4 ways.  Pick 5 from 13: C(13,5) = 1,287
  Total flushes = 4 × 1,287 = 5,148
Step 3: P = 5,148/2,598,960 ≈ 0.00198 ≈ 0.2% ✅
```

---

## 🧮 P3: Set Theory & Sample Spaces

> 📘 [Ch 4](./Probability_BootCamp_THEORY.md#chapter-4--set-theory-sample-spaces--events) | ⬆️ [Index](#-problem-index)

**Q: Die roll. A={1,2,3}, B={3,4,5}. Find P(A∪B), P(A∩B), P(Aᶜ).**

```
S = {1,2,3,4,5,6}     Each outcome: P = 1/6

A = {1,2,3}     P(A) = 3/6 = 1/2
B = {3,4,5}     P(B) = 3/6 = 1/2

INTERSECTION: A ∩ B = {3}  (the ONLY element in BOTH)
  P(A∩B) = 1/6

UNION: A ∪ B = {1,2,3,4,5}  (everything in A OR B)
  Method 1 (counting): 5 elements → P = 5/6
  Method 2 (formula):
    P(A∪B) = P(A) + P(B) − P(A∩B)
           = 1/2 + 1/2 − 1/6 = 3/6 + 3/6 − 1/6 = 5/6 ✅

COMPLEMENT: Aᶜ = {4,5,6}
  P(Aᶜ) = 1 − P(A) = 1 − 1/2 = 1/2 ✅

┌─── 🍎 WHY subtract P(A∩B) in the union formula? ─────────┐
│ When you add P(A)+P(B), you COUNT the overlap TWICE.     │
│ Subtract it once to fix the double-counting.             │
│ Like counting students in "Math OR Science club" —       │
│ students in BOTH clubs get counted twice if you just add.│
└──────────────────────────────────────────────────────────┘
```

---

## 🧮 P4: The Birthday Problem

> 📘 [Ch 5](./Probability_BootCamp_THEORY.md#chapter-5--the-birthday-problem) | ⬆️ [Index](#-problem-index)

**Q: What's P(at least 2 people share a birthday) in a room of 30?**

```
THE COMPLEMENT TRICK:
  P(match) = 1 − P(NO matches)

Step 1: P(all 30 have different birthdays)
  Person 1: 365/365 = 1           (any day)
  Person 2: 364/365               (avoid person 1's day)
  Person 3: 363/365               (avoid 2 days)
  ...
  Person 30: 336/365              (avoid 29 days)

  P(no match) = 365/365 × 364/365 × 363/365 × ... × 336/365
              = (365 × 364 × 363 × ... × 336) / 365³⁰

Step 2: Calculate (use calculator or approximate):
  P(no match) ≈ 0.2937

Step 3: P(at least one match) = 1 − 0.2937 = 0.7063 ≈ 70.6% ✅

┌─── 🍎 WHY is this so high? ──────────────────────────────┐
│ With 30 people, there are C(30,2) = 435 PAIRS to check!  │
│ Each pair has a 1/365 chance of matching.                │
│ 435 chances add up fast (not exactly, but intuitively).  │
│ For 23 people: 50.7%.  For 50 people: 97%!               │
└──────────────────────────────────────────────────────────┘

🤖 AI/ML: Same math explains hash collisions in data structures
   and why random feature generation can have unexpected overlaps.
```

---

## 🧮 P5: Multinomial & Quality Control

> 📘 [Ch 6-7](./Probability_BootCamp_THEORY.md#chapter-7--the-binomial-distribution) | ⬆️ [Index](#-problem-index)

**Q: (a) Defect rate 3%, test 20 items. P(at least 1 defect)? (b) P(exactly 3 Heads in 8 fair coin flips)?**

### (a) Quality control — complement trick

```
P(item good) = 0.97.   P(all 20 good) = 0.97²⁰

  0.97²⁰ ≈ 0.5438

P(at least 1 defect) = 1 − 0.5438 = 0.4562 ≈ 45.6% ✅

🍎 Even with only 3% defect rate, testing 20 gives you
   nearly a coin-flip chance of catching a defect!
```

### (b) Binomial: exactly 3H in 8 flips

```
X ~ Binomial(n=8, p=0.5)
P(X=3) = C(8,3) · (0.5)³ · (0.5)⁵

Step 1: C(8,3) = 8!/(3!·5!) = (8×7×6)/(3×2×1) = 336/6 = 56
Step 2: (0.5)³ = 0.125
Step 3: (0.5)⁵ = 0.03125
Step 4: P = 56 × 0.125 × 0.03125 = 56 × 0.00390625 = 0.21875 ✅

Verify: E[X] = np = 8×0.5 = 4  (so 3 is close to average — makes sense P is high)
```

---

## 🧮 P6: Conditional Probability

> 📘 [Ch 8](./Probability_BootCamp_THEORY.md#chapter-8--conditional-probability) | ⬆️ [Index](#-problem-index)

**Q: A bag has 5 red (3 big, 2 small) and 5 blue (1 big, 4 small). You draw one and it's BIG. P(red)?**

```
  WHAT WE KNOW:
    P(red) = 5/10 = 1/2       P(blue) = 5/10 = 1/2
    P(big | red) = 3/5         P(big | blue) = 1/5

  WHAT WE WANT: P(red | big)

  FORMULA: P(red | big) = P(red ∩ big) / P(big)

  Step 1: P(red ∩ big) = P(big|red) · P(red) = (3/5)(1/2) = 3/10

  Step 2: P(big) = P(big|red)·P(red) + P(big|blue)·P(blue)
                  = (3/5)(1/2) + (1/5)(1/2)
                  = 3/10 + 1/10 = 4/10 = 2/5

  Step 3: P(red | big) = (3/10)/(4/10) = 3/4 = 75% ✅

┌─── 🍎 Kid version ──────────────────────────────────────┐
│ Out of 10 marbles, 4 are big: 3 red-big + 1 blue-big.    │
│ GIVEN it's big, we only look at these 4.                 │
│ 3 out of 4 bigs are red → 75%.                           │
│ Conditioning SHRINKS the universe from 10 to 4!          │
└──────────────────────────────────────────────────────────┘
```

---

## 🧮 P7: Law of Total Probability

> 📘 [Ch 9](./Probability_BootCamp_THEORY.md#chapter-9--the-law-of-total-probability) | ⬆️ [Index](#-problem-index)

**Q: Factory has 3 machines. M1 makes 50% of items (2% defect), M2 makes 30% (3% defect), M3 makes 20% (5% defect). P(random item is defective)?**

```
  P(D) = P(D|M1)·P(M1) + P(D|M2)·P(M2) + P(D|M3)·P(M3)

  = (0.02)(0.50) + (0.03)(0.30) + (0.05)(0.20)
  = 0.010 + 0.009 + 0.010
  = 0.029 = 2.9% ✅

┌─── 🍎 Kid version ──────────────────────────────────────┐
│ Imagine 1000 items:                                      │
│   M1 makes 500 → 10 defective                            │
│   M2 makes 300 → 9 defective                             │
│   M3 makes 200 → 10 defective                            │
│   Total defective = 29 out of 1000 = 2.9%                │
│                                                          │
│ "Split into CASES, solve each, add up!" (mnemonic SPLIT) │
└──────────────────────────────────────────────────────────┘

🤖 AI/ML: Marginalization in Bayesian networks uses this exact formula.
   P(output) = sum over all hidden states of P(output|state)·P(state).
```

---

## 🧮 P8: Bayes' Theorem

> 📘 [Ch 10](./Probability_BootCamp_THEORY.md#chapter-10--bayes-theorem) | ⬆️ [Index](#-problem-index)

**Q: From P7's factory — if an item IS defective, P(it came from M3)?**

```
  WANT: P(M3 | D)    "Given defective, what's the chance it's from M3?"

  BAYES: P(M3|D) = P(D|M3)·P(M3) / P(D)

  We already know from P7: P(D) = 0.029

  P(M3|D) = (0.05)(0.20) / 0.029
           = 0.010 / 0.029
           = 0.3448 ≈ 34.5% ✅

  CHECK all three:
    P(M1|D) = (0.02)(0.50)/0.029 = 0.010/0.029 = 34.5%
    P(M2|D) = (0.03)(0.30)/0.029 = 0.009/0.029 = 31.0%
    P(M3|D) = 34.5%
    Sum = 34.5 + 31.0 + 34.5 = 100% ✅ (they must sum to 1)

┌─── 🍎 Insight ───────────────────────────────────────────┐
│ M3 makes only 20% of items but is responsible for 34.5%  │
│ of defects! Bayes UPDATES the blame based on evidence.   │
│ PRIOR: P(M3) = 20%.  POSTERIOR: P(M3|defect) = 34.5%.    │
│ Evidence (defect) shifted our belief toward M3.          │
└──────────────────────────────────────────────────────────┘
```

---

## 🧮 P9: Bayes Drug Testing & Medical Screening

> 📘 [Ch 11](./Probability_BootCamp_THEORY.md#chapter-11--bayes-example-drug-testing) | ⬆️ [Index](#-problem-index)

**Q: Disease prevalence=1%. Test sensitivity=95%, specificity=90%. Person tests positive. P(actually sick)?**

```
  GIVEN:
    P(D) = 0.01       P(Dᶜ) = 0.99
    P(+|D) = 0.95     (sensitivity: catches 95% of sick people)
    P(−|Dᶜ) = 0.90    → P(+|Dᶜ) = 0.10 (10% false positive rate)

  WANT: P(D | +)

  Step 1: P(+) via total probability
    = P(+|D)·P(D) + P(+|Dᶜ)·P(Dᶜ)
    = (0.95)(0.01) + (0.10)(0.99)
    = 0.0095 + 0.0990 = 0.1085

  Step 2: Bayes
    P(D|+) = P(+|D)·P(D) / P(+)
           = 0.0095 / 0.1085
           = 0.0876 ≈ 8.8% ✅

┌─── 🍎 THE BASE RATE FALLACY ────────────────────────────┐
│ A "95% accurate" test gives only 8.8% chance of disease  │
│ when the disease is rare (1%)!                           │
│                                                          │
│ Think of 10,000 people:                                  │
│   100 sick → 95 test positive (true pos)                 │
│   9900 healthy → 990 test positive (FALSE pos!)          │
│   Total positives: 95 + 990 = 1,085                      │
│   Actually sick: 95/1085 ≈ 8.8%                          │
│                                                          │
│ The FALSE POSITIVES overwhelm the true ones because      │
│ healthy people vastly outnumber sick ones.               │
└──────────────────────────────────────────────────────────┘

🤖 AI/ML: This is why PRECISION matters in rare-event classification!
   A model that's "99% accurate" for fraud detection (1% fraud rate)
   could just predict "no fraud" every time and be 99% right!
```

---

## 🧮 P10: Independence

> 📘 [Ch 12](./Probability_BootCamp_THEORY.md#chapter-12--independence-in-probability) | ⬆️ [Index](#-problem-index)

**Q: (a) P(HH) for 2 independent fair coins? (b) Card drawn: A="red", B="face card". Independent? (c) Are mutually exclusive events independent?**

### (a) Two independent coins

```
P(H₁ ∩ H₂) = P(H₁) · P(H₂) = 0.5 × 0.5 = 0.25 ✅
(Can multiply because flips are INDEPENDENT.)
```

### (b) Red and face card — independent?

```
P(red) = 26/52 = 1/2.    P(face) = 12/52 = 3/13
P(red ∩ face) = 6/52 = 3/26  (6 red face cards: J♥Q♥K♥J♦Q♦K♦)

Test: P(red)·P(face) = (1/2)(3/13) = 3/26 ✅
      P(red ∩ face)  = 3/26 ✅

EQUAL! So red and face card ARE independent.
🍎 Knowing a card is red doesn't change the chance it's a face card.
```

### (c) Mutually exclusive = independent?

```
NO! They're almost OPPOSITES.

Mutually exclusive: P(A∩B) = 0
Independent: P(A∩B) = P(A)·P(B)

If P(A)>0 and P(B)>0, then P(A)·P(B) > 0 ≠ 0.
So they CANNOT be both mutually exclusive AND independent!

🍎 If events CAN'T happen together (mutually exclusive),
   then knowing one happened tells you the other DIDN'T.
   That's the OPPOSITE of independence!
```

---

## 🧮 P11: Random Variables & PMF/PDF

> 📘 [Ch 13](./Probability_BootCamp_THEORY.md#chapter-13--random-variables--probability-distributions) | ⬆️ [Index](#-problem-index)

**Q: (a) X = sum of 2 dice. Write the PMF. Find P(X=7). (b) f(x)=2x for 0≤x≤1. Verify it's a valid PDF. Find P(X≤0.5).**

### (a) Discrete: Sum of 2 dice

```
X can be: 2,3,4,...,12.  Total outcomes = 36.

  x  | ways | P(X=x)
  ---+------+--------
  2  |  1   | 1/36
  3  |  2   | 2/36
  4  |  3   | 3/36
  5  |  4   | 4/36
  6  |  5   | 5/36
  7  |  6   | 6/36  ← MOST LIKELY
  8  |  5   | 5/36
  9  |  4   | 4/36
  10 |  3   | 3/36
  11 |  2   | 2/36
  12 |  1   | 1/36

Verify: 1+2+3+4+5+6+5+4+3+2+1 = 36.  36/36 = 1 ✅
P(X=7) = 6/36 = 1/6 ≈ 0.167 ✅
```

### (b) Continuous: f(x) = 2x

```
Step 1: Valid PDF? Need ∫₀¹ 2x dx = 1
  ∫₀¹ 2x dx = [x²]₀¹ = 1² − 0² = 1 ✅
  Also f(x) = 2x ≥ 0 for 0≤x≤1 ✅

Step 2: P(X ≤ 0.5) = ∫₀^0.5 2x dx = [x²]₀^0.5 = 0.25 ✅

🍎 For continuous RVs, probability = AREA under the curve.
   P(X = exact value) = 0 always! Only ranges have nonzero probability.
```

---

## 🧮 P12: Bernoulli & Binomial

> 📘 [Ch 14](./Probability_BootCamp_THEORY.md#chapter-14--bernoulli--binomial-random-variables) | ⬆️ [Index](#-problem-index)

**Q: Free-throw shooter makes 80% of shots. Takes 10 shots. (a) P(exactly 7 makes)? (b) P(at least 9)? (c) E[X] and Var(X)?**

### (a) P(X = 7)

```
X ~ Binomial(n=10, p=0.8)
P(X=7) = C(10,7) · (0.8)⁷ · (0.2)³

Step 1: C(10,7) = C(10,3) = 120   (symmetry: C(n,k) = C(n,n-k))
Step 2: (0.8)⁷ = 0.2097
Step 3: (0.2)³ = 0.008
Step 4: P = 120 × 0.2097 × 0.008 = 120 × 0.001678 = 0.2013 ≈ 20.1% ✅
```

### (b) P(X ≥ 9) = P(X=9) + P(X=10)

```
P(X=9) = C(10,9)·(0.8)⁹·(0.2)¹ = 10 × 0.1342 × 0.2 = 0.2684
P(X=10)= C(10,10)·(0.8)¹⁰·(0.2)⁰ = 1 × 0.1074 × 1 = 0.1074

P(X≥9) = 0.2684 + 0.1074 = 0.3758 ≈ 37.6% ✅
```

### (c) E[X] and Var(X)

```
E[X] = np = 10 × 0.8 = 8 makes on average ✅
Var(X) = np(1-p) = 10 × 0.8 × 0.2 = 1.6 ✅
σ = √1.6 ≈ 1.265

🍎 On average 8 makes, typically varying by about 1.3 either way.
```

---

## 🧮 P13: Normal Distribution

> 📘 [Ch 15-16](./Probability_BootCamp_THEORY.md#chapter-15--the-normal-distribution) | ⬆️ [Index](#-problem-index)

**Q: Test scores ~ N(μ=75, σ=10). (a) P(score > 85)? (b) P(60 < X < 90)? (c) What score is top 5%?**

### (a) P(X > 85)

```
Step 1: Standardize → Z = (X−μ)/σ = (85−75)/10 = 1.0
Step 2: P(X>85) = P(Z>1) = 1 − P(Z≤1) = 1 − 0.8413 = 0.1587 ≈ 15.9% ✅

🍎 85 is exactly 1σ above the mean.
   By the 68-95-99.7 rule: 68% within 1σ → 32% outside → 16% above. ✅
```

### (b) P(60 < X < 90)

```
Z₁ = (60−75)/10 = −1.5      Z₂ = (90−75)/10 = 1.5
P(−1.5 < Z < 1.5) = P(Z<1.5) − P(Z<−1.5)
                   = 0.9332 − 0.0668 = 0.8664 ≈ 86.6% ✅

🍎 About 87% of students score between 60 and 90.
```

### (c) Top 5% cutoff

```
"Top 5%" means P(X > c) = 0.05, so P(X ≤ c) = 0.95.
From Z-table: Z = 1.645 for 95th percentile.
c = μ + Z·σ = 75 + 1.645×10 = 75 + 16.45 = 91.45 ✅

🍎 You need about 91.5 to be in the top 5%.
```

---

## 🧮 P14: Poisson Distribution

> 📘 [Ch 17](./Probability_BootCamp_THEORY.md#chapter-17--the-poisson-distribution) | ⬆️ [Index](#-problem-index)

**Q: A call center gets λ=4 calls/hour. (a) P(exactly 2 calls in an hour)? (b) P(0 calls)? (c) P(≥1 call in 30 min)?**

### (a) P(X = 2)

```
X ~ Poisson(λ=4)
P(X=k) = e⁻λ · λᵏ / k!

P(X=2) = e⁻⁴ · 4² / 2!
       = 0.01832 × 16 / 2
       = 0.01832 × 8
       = 0.1465 ≈ 14.7% ✅
```

### (b) P(X = 0)

```
P(X=0) = e⁻⁴ · 4⁰ / 0! = e⁻⁴ · 1 / 1 = e⁻⁴ ≈ 0.0183 ≈ 1.8% ✅

🍎 Only about 2% chance of a silent hour — makes sense if you
   normally get 4 calls!
```

### (c) P(≥1 call in 30 min)

```
In 30 min = 0.5 hours, rate = 4 × 0.5 = 2 calls.
So Y ~ Poisson(λ=2) for this interval.

P(Y≥1) = 1 − P(Y=0) = 1 − e⁻² = 1 − 0.1353 = 0.8647 ≈ 86.5% ✅

🤖 AI/ML: Poisson models count data — website clicks, error rates,
   anomaly detection (if count >> λ, something unusual is happening!).
```

---

## 🧮 P15: Geometric & Exponential

> 📘 [Ch 18-19](./Probability_BootCamp_THEORY.md#chapter-18--the-geometric-distribution) | ⬆️ [Index](#-problem-index)

**Q: (a) Roll die until first 6. P(first 6 on 4th roll)? E[rolls]? (b) Buses arrive at rate λ=3/hour. P(wait > 30 min)?**

### (a) Geometric

```
X ~ Geometric(p = 1/6)
P(X=k) = (1−p)ᵏ⁻¹ · p

P(X=4) = (5/6)³ · (1/6) = (125/216) · (1/6) = 125/1296 ≈ 0.0965 ≈ 9.6% ✅

E[X] = 1/p = 1/(1/6) = 6 rolls on average ✅

🍎 3 failures (not-6) then 1 success (6): (5/6)(5/6)(5/6)(1/6)
```

### (b) Exponential waiting time

```
T ~ Exponential(λ=3)    (3 buses per hour)
P(T > t) = e⁻λᵗ

P(T > 0.5 hours) = e⁻³ˣ⁰·⁵ = e⁻¹·⁵ ≈ 0.2231 ≈ 22.3% ✅

E[T] = 1/λ = 1/3 hour = 20 minutes

MEMORYLESS CHECK: If you've waited 10 min already,
  P(wait 20 more min | already waited 10 min) = P(wait 20 min from scratch)
  The exponential doesn't "remember" how long you've waited!
```

---

## 🧮 P16: Gamma & Chi-Squared

> 📘 [Ch 22,25](./Probability_BootCamp_THEORY.md#chapter-22--the-gamma-distribution) | ⬆️ [Index](#-problem-index)

**Q: (a) Buses at rate λ=3/hr. Time until 5th bus: E and Var? (b) Z₁,Z₂,Z₃ ~ N(0,1) independent. X=Z₁²+Z₂²+Z₃². E[X]? Var(X)?**

### (a) Gamma — wait for 5th bus

```
T ~ Gamma(α=5, λ=3)

E[T] = α/λ = 5/3 hours ≈ 1 hour 40 min ✅
Var(T) = α/λ² = 5/9 ≈ 0.556 hours² ✅
σ = √(5/9) ≈ 0.745 hours ≈ 45 min

🍎 Gamma(5,3) = sum of 5 independent Exponential(3) waiting times.
   Each bus takes avg 20 min → 5 buses take avg 100 min.
```

### (b) Chi-Squared

```
X = Z₁² + Z₂² + Z₃² ~ χ²(k=3)

E[X] = k = 3 ✅
Var(X) = 2k = 6 ✅

┌─── 🍎 Connection ────────────────────────────────────────┐
│ χ²(3) = Gamma(3/2, 1/2)                                  │
│ E = (3/2)/(1/2) = 3 ✅   Var = (3/2)/(1/2)² = 6 ✅      │
│ Chi-squared IS a Gamma distribution with special params! │
└──────────────────────────────────────────────────────────┘
```

---

## 🧮 P17: Joint Distributions & Expected Value

> 📘 [Ch 26-28](./Probability_BootCamp_THEORY.md#chapter-26--joint-probability-distributions) | ⬆️ [Index](#-problem-index)

**Q: Joint PMF table. Find marginals, E[X], E[Y], and E[X+Y].**

```
       Y=0    Y=1    Y=2
X=0   0.10   0.15   0.05  │ 0.30
X=1   0.20   0.15   0.10  │ 0.45
X=2   0.05   0.10   0.10  │ 0.25
      ─────  ─────  ─────
      0.35   0.40   0.25  │ 1.00 ✅
```

### Marginals (sum across rows / columns)

```
P(X=0) = 0.10+0.15+0.05 = 0.30
P(X=1) = 0.20+0.15+0.10 = 0.45
P(X=2) = 0.05+0.10+0.10 = 0.25    Sum = 1.00 ✅

P(Y=0) = 0.10+0.20+0.05 = 0.35
P(Y=1) = 0.15+0.15+0.10 = 0.40
P(Y=2) = 0.05+0.10+0.10 = 0.25    Sum = 1.00 ✅
```

### E[X] and E[Y]

```
E[X] = 0·(0.30) + 1·(0.45) + 2·(0.25) = 0 + 0.45 + 0.50 = 0.95 ✅
E[Y] = 0·(0.35) + 1·(0.40) + 2·(0.25) = 0 + 0.40 + 0.50 = 0.90 ✅
```

### E[X+Y]

```
E[X+Y] = E[X] + E[Y] = 0.95 + 0.90 = 1.85 ✅

┌─── 🍎 KEY PROPERTY ─────────────────────────────────────┐
│ E[X+Y] = E[X] + E[Y] ALWAYS — even if X,Y dependent!     │
│ This is LINEARITY of expectation, the most useful        │
│ property in all of probability.                          │
└──────────────────────────────────────────────────────────┘
```

---

## 🧮 P18: Variance & Standard Deviation

> 📘 [Ch 29](./Probability_BootCamp_THEORY.md#chapter-29--variance--standard-deviation) | ⬆️ [Index](#-problem-index)

**Q: X has PMF: P(X=1)=0.2, P(X=2)=0.5, P(X=3)=0.3. Find E[X], E[X²], Var(X), σ.**

```
Step 1: E[X] = Σ x·P(x)
  = 1(0.2) + 2(0.5) + 3(0.3)
  = 0.2 + 1.0 + 0.9 = 2.1 ✅

Step 2: E[X²] = Σ x²·P(x)
  = 1²(0.2) + 2²(0.5) + 3²(0.3)
  = 1(0.2) + 4(0.5) + 9(0.3)
  = 0.2 + 2.0 + 2.7 = 4.9 ✅

Step 3: Var(X) = E[X²] − (E[X])²
  = 4.9 − (2.1)²
  = 4.9 − 4.41 = 0.49 ✅

Step 4: σ = √0.49 = 0.7 ✅

┌─── 🍎 What does this MEAN? ─────────────────────────────┐
│ Average value = 2.1                                     │
│ Typical deviation from average = 0.7                    │
│ So most values fall in [2.1−0.7, 2.1+0.7] = [1.4, 2.8]  │
│ Indeed: X=2 (prob 50%) is right in this range!          │
└──────────────────────────────────────────────────────────┘
```

**Bonus: Var(3X + 5)?**

```
Var(aX + b) = a² · Var(X)     (shifting by b doesn't change spread!)
Var(3X + 5) = 9 × 0.49 = 4.41 ✅

🤖 AI/ML: Feature scaling. If you multiply feature by 3, variance 
   scales by 9. This is why standardization (subtract mean, divide by σ)
   is crucial before training — it equalizes feature variances.
```

---

## 🧮 P19: Inequalities, LLN & CLT

> 📘 [Ch 30,33](./Probability_BootCamp_THEORY.md#chapter-30--markov--chebyshev-inequalities) | ⬆️ [Index](#-problem-index)

**Q: (a) E[X]=50, X≥0. Bound P(X≥200). (b) μ=100, σ=15. Bound P(|X−100|≥45). (c) 36 samples from pop with μ=80, σ=12. P(X̄ > 84)?**

### (a) Markov's Inequality

```
P(X ≥ a) ≤ E[X]/a

P(X ≥ 200) ≤ 50/200 = 0.25 ✅

🍎 "At most 25% chance X exceeds 200."
   Markov only needs E[X] and X≥0. Very loose but always works!
```

### (b) Chebyshev's Inequality

```
P(|X−μ| ≥ kσ) ≤ 1/k²

Here: |X−100| ≥ 45 → kσ = 45 → k = 45/15 = 3
P(|X−100| ≥ 45) ≤ 1/3² = 1/9 ≈ 0.111 ✅

🍎 "At most 11.1% chance of being 3σ from the mean."
   For Normal: actual = 0.3%. Chebyshev is conservative but universal!
```

### (c) CLT Application

```
n = 36, μ = 80, σ = 12
By CLT: X̄ ≈ N(μ, σ²/n) = N(80, 144/36) = N(80, 4)
So σ_X̄ = √4 = 2

Z = (X̄ − μ)/(σ/√n) = (84 − 80)/2 = 2.0

P(X̄ > 84) = P(Z > 2) = 1 − 0.9772 = 0.0228 ≈ 2.3% ✅

┌─── 🍎 Why √n matters ───────────────────────────────────┐
│ Individual σ = 12 (wide).                               │
│ Average of 36: σ_X̄ = 12/√36 = 12/6 = 2 (narrow!).       │
│ More samples → average gets MORE PRECISE.               │
│ This is the Law of Large Numbers in action.             │
│                                                         │
│ 🤖 In ML: larger batch size → more stable gradient!     │
└──────────────────────────────────────────────────────────┘
```

---

## 🧮 P20: Covariance & Correlation

> 📘 [Ch 32](./Probability_BootCamp_THEORY.md#chapter-32--covariance--correlation) | ⬆️ [Index](#-problem-index)

**Q: Using the joint PMF from P17, find Cov(X,Y) and ρ(X,Y). Are X,Y independent?**

```
From P17: E[X] = 0.95, E[Y] = 0.90

Step 1: Find E[XY] = ΣΣ xy · P(x,y)
  Only nonzero when BOTH x≠0 AND y≠0:
  
  x=0: all terms = 0 (since x=0)
  x=1, y=0: 1·0·0.20 = 0
  x=1, y=1: 1·1·0.15 = 0.15
  x=1, y=2: 1·2·0.10 = 0.20
  x=2, y=0: 2·0·0.05 = 0
  x=2, y=1: 2·1·0.10 = 0.20
  x=2, y=2: 2·2·0.10 = 0.40
  
  E[XY] = 0 + 0 + 0.15 + 0.20 + 0 + 0.20 + 0.40 = 0.95

Step 2: Cov(X,Y) = E[XY] − E[X]·E[Y]
  = 0.95 − (0.95)(0.90) = 0.95 − 0.855 = 0.095 ✅

Step 3: Need Var(X) and Var(Y)
  E[X²] = 0²(0.30) + 1²(0.45) + 2²(0.25) = 0 + 0.45 + 1.00 = 1.45
  Var(X) = 1.45 − 0.95² = 1.45 − 0.9025 = 0.5475
  σ_X = √0.5475 ≈ 0.7399

  E[Y²] = 0²(0.35) + 1²(0.40) + 2²(0.25) = 0 + 0.40 + 1.00 = 1.40
  Var(Y) = 1.40 − 0.90² = 1.40 − 0.81 = 0.59
  σ_Y = √0.59 ≈ 0.7681

Step 4: ρ = Cov(X,Y)/(σ_X · σ_Y)
  = 0.095 / (0.7399 × 0.7681)
  = 0.095 / 0.5683
  = 0.1672 ≈ 0.167 ✅

Step 5: Independent?
  If independent: P(X=x,Y=y) = P(X=x)·P(Y=y) for ALL x,y.
  Check: P(X=0,Y=0) = 0.10
         P(X=0)·P(Y=0) = 0.30 × 0.35 = 0.105 ≠ 0.10
  NOT independent! ✅

┌─── 🍎 Summary ───────────────────────────────────────────┐
│ Cov = 0.095 > 0: X and Y tend to increase together       │
│ ρ = 0.167: WEAK positive linear relationship             │
│ NOT independent (joint ≠ product of marginals)           │
│                                                          │
│ REMEMBER: Cov=0 does NOT mean independent!               │
│ But independent DOES mean Cov=0.                         │
│                                                          │
│ 🤖 In PCA: the covariance matrix of features tells you   │
│    which features move together → find principal axes.   │
└──────────────────────────────────────────────────────────┘
```

---

## ⏱️ 60-SECOND REVISION

```
┌──────────────────────────────────────────────────────────────────────┐
│  COUNT: P(n,r)=n!/(n-r)! [order] C(n,k)=n!/k!(n-k)! [no order]       │
│  BASIC: P(A)=fav/total  P(Aᶜ)=1-P(A)  P(A∪B)=P(A)+P(B)-P(A∩B)        │
│  CONDITIONAL: P(A|B)=P(A∩B)/P(B)  → "shrink the universe to B"       │
│  BAYES: P(A|B)=P(B|A)P(A)/P(B) → "flip cause and effect"             │
│  INDEPENDENT: P(A∩B)=P(A)P(B) → "knowing B doesn't help with A"      │
│  BINOMIAL: n trials, P(k successes)=C(n,k)pᵏ(1-p)ⁿ⁻ᵏ                 │
│  POISSON: rare events, P(X=k)=e⁻λλᵏ/k!   mean=var=λ                  │
│  NORMAL: bell curve, Z=(X-μ)/σ, 68-95-99.7 rule                      │
│  EXPONENTIAL: waiting time, P(T>t)=e⁻λᵗ, memoryless                  │
│  E[X]=ΣxP(x)  Var=E[X²]-(E[X])²  σ=√Var                              │
│  CLT: averages → Normal.  LLN: averages → μ.                         │
│  Cov=E[XY]-E[X]E[Y]  ρ=Cov/(σₓσᵧ) ∈ [-1,1]                           │
└──────────────────────────────────────────────────────────────────────┘
```

---

> 🔗 [← Back to INDEX](./Probability_BootCamp_INDEX.md) | [← Theory Guide](./Probability_BootCamp_THEORY.md)
>
> 🎓 **Created for:** ODS | ML
