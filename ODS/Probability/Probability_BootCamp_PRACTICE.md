# 🔢 Probability BootCamp — PRACTICE PROBLEMS GUIDE

### 🎓 ODS | ML
> 🔗 **Navigation:** [← Back to INDEX](./Probability_BootCamp_INDEX.md) | [← Theory Guide](./Probability_BootCamp_THEORY.md)
>
> 🍎 Every step explained from scratch. Nothing assumed. Every diagram drawn out.

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
| P18 | [Variance & Standard Deviation](#-p18-variance--standard-deviation) | Var, sigma | [📘 Ch29](./Probability_BootCamp_THEORY.md#chapter-29--variance--standard-deviation) |
| P19 | [Inequalities, LLN & CLT](#-p19-inequalities--lln--clt) | Markov, Chebyshev, CLT | [📘 Ch30,33](./Probability_BootCamp_THEORY.md#chapter-30--markov--chebyshev-inequalities) |
| P20 | [Covariance & Correlation](#-p20-covariance--correlation) | Cov, rho | [📘 Ch32](./Probability_BootCamp_THEORY.md#chapter-32--covariance--correlation) |

---

## 📖 FORMULA CHEAT SHEET

```
 COUNTING                              PROBABILITY
 n! = n*(n-1)*...*1.  0!=1             P(A) = favorable / total
 P(n,r) = n!/(n-r)!   [order YES]     P(Ac) = 1 - P(A)
 C(n,k) = n!/[k!(n-k)!] [order NO]    P(AuB) = P(A)+P(B)-P(AnB)
                                       P(A|B) = P(AnB)/P(B)
 DISTRIBUTIONS                         Bayes: P(A|B)=P(B|A)P(A)/P(B)
 Binom: C(n,k) p^k (1-p)^(n-k)
 Poisson: e^(-L) L^k / k!             STATS
 Geom: (1-p)^(k-1) * p                E[X] = Sum x*P(x)
 Normal: Z = (X-u)/s                   Var = E[X^2] - (E[X])^2
 Expon: f(x) = L*e^(-Lx)              Cov = E[XY] - E[X]E[Y]
                                       rho = Cov / (sX * sY)
```

---
---

## 🧮 P1: Basic Counting & Coin Flips

> 📘 [Ch 2](./Probability_BootCamp_THEORY.md#chapter-2--counting-coin-flips--dice) | [Index](#-problem-index)

**Q: (a) Outcomes for 4 coin flips? (b) P(exactly 2H in 4 flips)? (c) P(sum>=10 with two dice)?**

### What does "counting outcomes" mean?

```
Before we can find ANY probability, we need to know:
  1. How many TOTAL outcomes are possible?  (the denominator)
  2. How many of those are FAVORABLE?       (the numerator)

Then: P(event) = favorable / total
```

### (a) Total outcomes for 4 coins

```
Each flip has 2 outcomes: H (Heads) or T (Tails).
The flips are INDEPENDENT (flip 1 doesn't affect flip 2).

MULTIPLICATION PRINCIPLE:
  If step 1 has "a" choices AND step 2 has "b" choices,
  then total = a * b choices.

  Flip 1: 2 choices
  Flip 2: 2 choices
  Flip 3: 2 choices
  Flip 4: 2 choices
  Total = 2 * 2 * 2 * 2 = 2^4 = 16
```

WHY multiply? Look at this TREE. Each level DOUBLES the branches:

```
                          START
                         /      \
                       H          T            <- Flip 1: 2 branches
                     /   \      /   \
                   H       T  H       T        <- Flip 2: 4 branches
                  /\      /\ /\      /\
                H   T   H  T H  T  H   T      <- Flip 3: 8 branches
               /\ /\   /\ /\ /\ /\ /\ /\
              H T H T H T H T H T H T H T H T <- Flip 4: 16 leaves!

   Reading each path top-to-bottom gives all 16 outcomes:
   HHHH HHHT HHTH HHTT HTHH HTHT HTTH HTTT
   THHH THHT THTH THTT TTHH TTHT TTTH TTTT

   Count them: 16 outcomes total!
   Each level DOUBLES: 1 -> 2 -> 4 -> 8 -> 16
```

### (b) P(exactly 2 Heads)

```
Step 1: WHICH 2 of the 4 flips are Heads? We need to CHOOSE 2 spots.
  This is a COMBINATION: C(4,2)

  C(4,2) = 4! / (2! * 2!)

  Let's compute step by step:
    4! = 4 * 3 * 2 * 1 = 24
    2! = 2 * 1 = 2
    C(4,2) = 24 / (2 * 2) = 24 / 4 = 6

  The 6 ways (mark which flips are H):
    Flips:  1234
    HHTT    HH-- (flips 1,2 are H)
    HTHT    H-H- (flips 1,3)
    HTTH    H--H (flips 1,4)
    THHT    -HH- (flips 2,3)
    THTH    -H-H (flips 2,4)
    TTHH    --HH (flips 3,4)
    Count: 6 ways. Matches C(4,2) = 6!

Step 2: Total outcomes = 16 (from part a)

Step 3: P(exactly 2H) = favorable / total = 6 / 16 = 3/8 = 0.375
```

VERIFY with BINOMIAL formula:

```
  X ~ Binomial(n=4, p=0.5)
  P(X=2) = C(4,2) * (0.5)^2 * (0.5)^2

  = 6 * 0.25 * 0.25
  = 6 * 0.0625
  = 0.375 = 3/8  MATCHES!
```

### (c) P(sum >= 10, two dice)

```
Two dice: each has 6 faces. Total = 6 * 6 = 36 outcomes.

GRID of all 36 sums (favorable ones marked with [brackets]):

        Die 2:  1    2    3    4    5    6
Die 1:
   1          | 2  | 3  | 4  | 5  | 6  | 7  |
   2          | 3  | 4  | 5  | 6  | 7  | 8  |
   3          | 4  | 5  | 6  | 7  | 8  | 9  |
   4          | 5  | 6  | 7  | 8  | 9  |[10]|
   5          | 6  | 7  | 8  | 9  |[10]|[11]|
   6          | 7  | 8  | 9  |[10]|[11]|[12]|

Count [bracketed] cells:
  Sum=10: (4,6), (5,5), (6,4)     -> 3 ways
  Sum=11: (5,6), (6,5)            -> 2 ways
  Sum=12: (6,6)                    -> 1 way
  Total favorable = 3 + 2 + 1 = 6

P(sum >= 10) = 6/36 = 1/6 = 0.167
```

```
🤖 AI/ML: Counting is the foundation of SAMPLING. Every Monte Carlo
   simulation counts favorable vs total outcomes.
```

---

## 🧮 P2: Permutations & Combinations

> 📘 [Ch 3](./Probability_BootCamp_THEORY.md#chapter-3--combinatorics--factorials) | [Index](#-problem-index)

**Q: (a) Arrange 5 books. (b) Choose 3 from 8. (c) P(flush in poker).**

### What is a factorial?

```
n! = n * (n-1) * (n-2) * ... * 2 * 1
"Multiply all whole numbers from n down to 1"

1! = 1        3! = 6        5! = 120
2! = 2        4! = 24       0! = 1 (by definition)
```

### (a) Arrange 5 books

```
ORDER MATTERS. Use ALL 5 books.

  Slot:    [ ? ][ ? ][ ? ][ ? ][ ? ]
  Choices:   5    4    3    2    1
  Total = 5 * 4 * 3 * 2 * 1 = 5! = 120 arrangements
```

### (b) Choose 3 from 8

```
ORDER DOESN'T MATTER ({A,B,C} = {C,B,A}).

  C(8,3) = 8! / (3! * 5!)
         = (8*7*6) / (3*2*1) = 336/6 = 56

  WHY divide by 3!?
  Permutations P(8,3) = 336 counts each GROUP in ALL orderings:
    {A,B,C} appears as: ABC ACB BAC BCA CAB CBA = 3! = 6 times
  Divide by 6 to remove duplicates: 336/6 = 56 unique teams.
```

### (c) P(flush in poker)

```
Step 1: Total 5-card hands = C(52,5) = 2,598,960
Step 2: Flushes = 4 suits * C(13,5) = 4 * 1287 = 5,148
Step 3: P = 5,148 / 2,598,960 = 0.00198 = 0.2%
```

---

## 🧮 P3: Set Theory & Sample Spaces

> 📘 [Ch 4](./Probability_BootCamp_THEORY.md#chapter-4--set-theory-sample-spaces--events) | [Index](#-problem-index)

**Q: Die roll. A={1,2,3}, B={3,4,5}. Find P(AuB), P(AnB), P(Ac).**

### VENN DIAGRAM

```
  +------------------------------------------+
  |           S = {1,2,3,4,5,6}              |
  |                                          |
  |    +----------+----------+               |
  |    |  A only  | OVERLAP  | B only        |
  |    |  {1, 2}  |   {3}   | {4, 5}        |
  |    +----------+----------+               |
  |                                          |
  |    Outside both: {6}                     |
  +------------------------------------------+
```

### Solutions

```
Each outcome: P = 1/6.  P(A) = 3/6.  P(B) = 3/6.

INTERSECTION: AnB = {3}         P(AnB) = 1/6

UNION: AuB = {1,2,3,4,5}
  P(AuB) = P(A) + P(B) - P(AnB)
         = 3/6 + 3/6 - 1/6 = 5/6

  WHY subtract P(AnB)?
  Adding P(A)+P(B) counts {3} TWICE. Subtract once to fix.

COMPLEMENT: Ac = {4,5,6}
  P(Ac) = 1 - P(A) = 1 - 3/6 = 3/6 = 1/2
```

---

## 🧮 P4: The Birthday Problem

> 📘 [Ch 5](./Probability_BootCamp_THEORY.md#chapter-5--the-birthday-problem) | [Index](#-problem-index)

**Q: P(at least 2 of 30 people share a birthday)?**

### The Complement Trick

```
HARD: count "at least one match"
EASY: count "NO matches at all"

  P(match) = 1 - P(NO matches)

  +-----------------------------+
  | ALL POSSIBILITIES = 100%    |
  |  +---------+  +-----------+ |
  |  |MATCHES  |  |NO MATCHES | |
  |  |(= WANT) |  |(= COMPUTE)| |
  |  +---------+  +-----------+ |
  +-----------------------------+
```

### Calculation

```
Person 1: 365/365 (any day)
Person 2: 364/365 (avoid 1 day)
Person 3: 363/365 (avoid 2 days)
...
Person 30: 336/365 (avoid 29 days)

P(no match) = 365*364*363*...*336 / 365^30 = 0.2937

P(at least one match) = 1 - 0.2937 = 0.7063 = 70.6%

  WHY so high? C(30,2) = 435 PAIRS to check!

  People:  10    23    30    50    70
  P(match): 12%  50.7% 70.6% 97%  99.9%
```

---

## 🧮 P5: Multinomial & Quality Control

> 📘 [Ch 6-7](./Probability_BootCamp_THEORY.md#chapter-7--the-binomial-distribution) | [Index](#-problem-index)

**Q: (a) 3% defect, test 20. P(>=1 defect)? (b) P(3H in 8 flips)?**

### (a) Quality Control

```
P(all 20 good) = 0.97^20 = 0.5438
P(>=1 defect) = 1 - 0.5438 = 0.4562 = 45.6%

  Of 1000 batches of 20:
  [544 all good] [456 have at least 1 defect!] <- nearly half!
```

### (b) Binomial: 3H in 8 flips

```
P(X=3) = C(8,3) * (0.5)^3 * (0.5)^5
       = 56 * 0.125 * 0.03125 = 0.21875 = 21.9%

  WHAT EACH PIECE MEANS:
  C(8,3) = 56   : 56 WAYS to pick which 3 flips are H
  (0.5)^3        : those 3 flips all land H
  (0.5)^5        : the other 5 flips all land T

  BINOMIAL SHAPE for n=8, p=0.5:
  P(k)
  0.27 |          **
  0.22 |       ***  ***
  0.16 |     **        **
  0.11 |   **            **
  0.05 | **                **
  0.00 +--+--+--+--+--+--+--+--+--
         0  1  2  3  4  5  6  7  8   k=Heads
                     ^
                  peak at np=4
```

---

## 🧮 P6: Conditional Probability

> 📘 [Ch 8](./Probability_BootCamp_THEORY.md#chapter-8--conditional-probability) | [Index](#-problem-index)

**Q: Bag: 5 red (3 big, 2 small), 5 blue (1 big, 4 small). Draw is BIG. P(red)?**

### Visual: The bag

```
  RED (5):                 BLUE (5):
  [Big][Big][Big][sm][sm]  [Big][sm][sm][sm][sm]
    3 big    2 small         1 big    4 small

  ALL BIG marbles (what we care about after seeing "BIG"):
  [R-Big][R-Big][R-Big][B-Big]   <- 4 total big marbles

  GIVEN it's big, universe SHRINKS to these 4.
  P(red | big) = 3 red-big / 4 total big = 3/4 = 75%
```

### Formal

```
P(red n big) = P(big|red)*P(red) = (3/5)(1/2) = 3/10
P(big) = P(big|red)*P(red) + P(big|blue)*P(blue)
       = 3/10 + 1/10 = 4/10
P(red|big) = (3/10)/(4/10) = 3/4 = 75%
```

---

## 🧮 P7: Law of Total Probability

> 📘 [Ch 9](./Probability_BootCamp_THEORY.md#chapter-9--the-law-of-total-probability) | [Index](#-problem-index)

**Q: M1=50%(2% defect), M2=30%(3%), M3=20%(5%). P(defective)?**

```
  1000 items flowing through factory:
  +----------+----------+----------+
  | M1: 500  | M2: 300  | M3: 200  |
  | 2% bad   | 3% bad   | 5% bad   |
  | =10 bad  | =9 bad   | =10 bad  |
  +----------+----------+----------+
  Total bad = 10 + 9 + 10 = 29 out of 1000

P(D) = (0.02)(0.50) + (0.03)(0.30) + (0.05)(0.20)
     = 0.010 + 0.009 + 0.010 = 0.029 = 2.9%
```

---

## 🧮 P8: Bayes' Theorem

> 📘 [Ch 10](./Probability_BootCamp_THEORY.md#chapter-10--bayes-theorem) | [Index](#-problem-index)

**Q: From P7 - item is defective. P(from M3)?**

```
  BAYES FLIPS THE DIRECTION:
  KNOW: Machine -> Defect?     (forward)
  WANT: Defect  -> Machine?    (backward = Bayes!)

P(M3|D) = P(D|M3)*P(M3) / P(D)
        = (0.05)(0.20) / 0.029
        = 0.010 / 0.029 = 0.345 = 34.5%

  CHECK: P(M1|D)=34.5%, P(M2|D)=31.0%, P(M3|D)=34.5%. Sum=100%

  PRIOR:     P(M3) = 20%         <- before seeing evidence
  POSTERIOR:  P(M3|D) = 34.5%    <- after seeing defect
  Bayes shifted blame TOWARD M3 (higher defect rate).
```

---

## 🧮 P9: Bayes Drug Testing & Medical Screening

> 📘 [Ch 11](./Probability_BootCamp_THEORY.md#chapter-11--bayes-example-drug-testing) | [Index](#-problem-index)

**Q: Disease 1%. Sensitivity=95%, Specificity=90%. Tests +. P(sick)?**

### The 10,000 people picture

```
  10,000 people
  +----------------------+-----------------------------------+
  | 100 SICK (1%)        | 9,900 HEALTHY (99%)               |
  |                      |                                   |
  | 95% test +           | 10% test + (false alarm!)         |
  | = 95 true positives  | = 990 FALSE positives             |
  +----------------------+-----------------------------------+

  Total positives: 95 + 990 = 1,085
  Actually sick among positives: 95 / 1085 = 8.8%

  A "95% accurate" test is WRONG 91% of the time on positives
  when the disease is rare (1%)!  This is the BASE RATE FALLACY.
```

### Formal

```
P(+) = (0.95)(0.01) + (0.10)(0.99) = 0.0095 + 0.0990 = 0.1085
P(D|+) = 0.0095 / 0.1085 = 0.0876 = 8.8%

🤖 AI/ML: This is why PRECISION matters! A 99% "accurate" fraud
   detector on 1% fraud data could just say "no fraud" always!
```

---

## 🧮 P10: Independence

> 📘 [Ch 12](./Probability_BootCamp_THEORY.md#chapter-12--independence-in-probability) | [Index](#-problem-index)

**Q: (a) P(HH)? (b) Red + face card independent? (c) Mutually exclusive = independent?**

### (a) Two coins

```
P(H1 n H2) = P(H1)*P(H2) = 0.5*0.5 = 0.25
(Can multiply because INDEPENDENT.)
```

### (b) Red and face card

```
P(red)=26/52=1/2. P(face)=12/52=3/13. P(red n face)=6/52=3/26.
Test: P(red)*P(face) = (1/2)(3/13) = 3/26 = P(red n face). YES independent!
```

### (c) Mutually exclusive vs independent

```
  Mutually Exclusive:        Independent:
  +------+  +------+        +------+---+---+
  |  A   |  |  B   |        |  A   |AnB|   |
  |      |  |      |        |      |   | B |
  +------+  +------+        +------+---+---+
  No overlap: P(AnB)=0       MUST overlap: P(AnB)=P(A)*P(B)>0

  They CANNOT be both (if P(A)>0 and P(B)>0)!
  Mutually exclusive means knowing A happened tells you B DIDN'T.
  That's the OPPOSITE of independence!
```

---

## 🧮 P11: Random Variables & PMF/PDF

> 📘 [Ch 13](./Probability_BootCamp_THEORY.md#chapter-13--random-variables--probability-distributions) | [Index](#-problem-index)

**Q: (a) X = sum of 2 dice. PMF, P(X=7). (b) f(x)=2x for 0<=x<=1. Valid PDF? P(X<=0.5)?**

### (a) Sum of 2 dice

```
  x  | ways | P(X=x) | bar chart
  ---+------+--------+-------------------
  2  |  1   | 1/36   | *
  3  |  2   | 2/36   | **
  4  |  3   | 3/36   | ***
  5  |  4   | 4/36   | ****
  6  |  5   | 5/36   | *****
  7  |  6   | 6/36   | ******       <- PEAK
  8  |  5   | 5/36   | *****
  9  |  4   | 4/36   | ****
  10 |  3   | 3/36   | ***
  11 |  2   | 2/36   | **
  12 |  1   | 1/36   | *

  Sum of ways: 1+2+3+4+5+6+5+4+3+2+1 = 36/36 = 1
  P(X=7) = 6/36 = 1/6 = 0.167 (most likely sum!)
```

### (b) Continuous PDF

```
  f(x) = 2x for 0<=x<=1.

  Valid? Area = integral 0 to 1 of 2x dx = [x^2] = 1-0 = 1. YES!

  P(X<=0.5) = integral 0 to 0.5 of 2x dx = [x^2] = 0.25

  f(x)
  2 |             /|
    |            / |
    |           /  |
  1 |          /   |
    |   AREA  /    |
    |  =0.25/     |
    |       /      |
  0 +------+------+
    0    0.5     1.0
```

---

## 🧮 P12: Bernoulli & Binomial

> 📘 [Ch 14](./Probability_BootCamp_THEORY.md#chapter-14--bernoulli--binomial-random-variables) | [Index](#-problem-index)

**Q: 80% free-throw, 10 shots. (a) P(X=7)? (b) P(X>=9)? (c) E[X], Var?**

### (a) P(X=7)

```
X ~ Binomial(n=10, p=0.8)
P(X=7) = C(10,7)*(0.8)^7*(0.2)^3 = 120*0.2097*0.008 = 0.2013 = 20.1%

  C(10,7)=120 : ways to pick which 7 shots go in
  (0.8)^7     : those 7 all succeed
  (0.2)^3     : the other 3 all miss
```

### (b) P(X>=9)

```
P(X=9) = 10*0.1342*0.2 = 0.2684
P(X=10) = 1*0.1074*1 = 0.1074
P(X>=9) = 0.2684 + 0.1074 = 0.3758 = 37.6%
```

### (c) E[X], Var(X)

```
E[X] = np = 10*0.8 = 8 makes on average
Var(X) = np(1-p) = 10*0.8*0.2 = 1.6
sigma = sqrt(1.6) = 1.265

"Expect ~8 makes, give or take ~1.3"
```

---

## 🧮 P13: Normal Distribution

> 📘 [Ch 15-16](./Probability_BootCamp_THEORY.md#chapter-15--the-normal-distribution) | [Index](#-problem-index)

**Q: Scores ~ N(u=75, s=10). (a) P(X>85)? (b) P(60<X<90)? (c) Top 5% cutoff?**

### The 68-95-99.7 Rule

```
           ....
         ..    ..
       ..  68%   ..
     ..  |<---->|  ..
   ..    | 95%  |    ..
  .   |<-------->|     .
  +---+---+---+---+---+---+
  45  55  65  75  85  95  105
         u-2s u-s  u  u+s u+2s
```

### (a) P(X > 85)

```
Z = (85-75)/10 = 1.0.  P(Z>1) = 1 - 0.8413 = 0.1587 = 15.9%
Quick check: 68% within 1s -> 32% outside -> 16% above. Matches!
```

### (b) P(60 < X < 90)

```
Z1=(60-75)/10=-1.5    Z2=(90-75)/10=1.5
P = P(Z<1.5) - P(Z<-1.5) = 0.9332 - 0.0668 = 0.8664 = 86.6%

           ....
         .. //// ..        shaded = 86.6%
       .. //////// ..
     .. //////////// ..
   .. //////////////// ..
  +---+---+---+---+---+---+
     55   60  75  90  95
          Z=-1.5  Z=+1.5
```

### (c) Top 5% cutoff

```
P(X<=c) = 0.95 -> Z=1.645
c = u + Z*s = 75 + 1.645*10 = 91.45
"Need ~91.5 to be in top 5%."
```

---

## 🧮 P14: Poisson Distribution

> 📘 [Ch 17](./Probability_BootCamp_THEORY.md#chapter-17--the-poisson-distribution) | [Index](#-problem-index)

**Q: L=4 calls/hr. (a) P(X=2)? (b) P(X=0)? (c) P(>=1 in 30min)?**

```
  P(X=k) = e^(-L) * L^k / k!    E[X] = Var(X) = L

  (a) P(X=2) = e^(-4)*16/2 = 0.01832*8 = 0.1465 = 14.7%
  (b) P(X=0) = e^(-4)*1/1 = 0.0183 = 1.8%
  (c) 30 min: L=2. P(>=1) = 1 - e^(-2) = 1-0.1353 = 86.5%

  POISSON SHAPE L=4:
  P(k)
  0.20 |     **
  0.15 |   **  **
  0.10 | **      **
  0.05 |*          ***
  0.00 +--+--+--+--+--+--+--+--+--
        0  1  2  3  4  5  6  7  8
                    ^
              peak near L=4
```

---

## 🧮 P15: Geometric & Exponential

> 📘 [Ch 18-19](./Probability_BootCamp_THEORY.md#chapter-18--the-geometric-distribution) | [Index](#-problem-index)

**Q: (a) Die until first 6. P(4th roll)? E? (b) Buses L=3/hr. P(wait>30min)?**

### (a) Geometric

```
X ~ Geometric(p=1/6).  P(X=k) = (1-p)^(k-1) * p

P(X=4) = (5/6)^3 * (1/6) = 125/1296 = 0.0965 = 9.6%

  TIMELINE:
  Roll:  1     2     3     4
         X     X     X     6!     "3 failures then success"
         5/6 * 5/6 * 5/6 * 1/6

E[X] = 1/p = 6 rolls on average
```

### (b) Exponential

```
T ~ Exponential(L=3).  P(T>t) = e^(-Lt).  E[T] = 1/L = 20 min.

P(T>0.5hr) = e^(-1.5) = 0.2231 = 22.3%

  f(t)
  3 |*
    | **
  2 |   **
    |     ***
  1 |        ****
    |            ********
  0 +------+------+------+------
    0    0.33   0.67    1.0   t(hr)
         E[T]
        =20min

  MEMORYLESS: Already waited 10 min? Expected additional wait
  is STILL 20 min. The exponential doesn't remember!
```

---

## 🧮 P16: Gamma & Chi-Squared

> 📘 [Ch 22,25](./Probability_BootCamp_THEORY.md#chapter-22--the-gamma-distribution) | [Index](#-problem-index)

**Q: (a) Buses L=3/hr, time until 5th bus? (b) X=Z1^2+Z2^2+Z3^2, E, Var?**

### (a) Gamma

```
T ~ Gamma(a=5, L=3).  "Wait for 5th event"

  Gamma = sum of a independent Exponentials:
  --bus1----bus2--bus3------bus4---bus5-->
  |<-Exp->|<--->|<-->|<------>|<-->|
  |<---------- Gamma(5,3) -------->|

E[T] = a/L = 5/3 hr = 1hr 40min
Var(T) = a/L^2 = 5/9 hr^2.   sigma = 45 min.
```

### (b) Chi-Squared

```
X = Z1^2+Z2^2+Z3^2 ~ Chi-sq(k=3) = Gamma(3/2, 1/2)

E[X] = k = 3      Var(X) = 2k = 6
```

---

## 🧮 P17: Joint Distributions & Expected Value

> 📘 [Ch 26-28](./Probability_BootCamp_THEORY.md#chapter-26--joint-probability-distributions) | [Index](#-problem-index)

**Q: Joint PMF table. Marginals, E[X], E[Y], E[X+Y].**

```
  JOINT TABLE:
            Y=0    Y=1    Y=2    | Row sum = P(X=x)
  X=0      0.10   0.15   0.05   |  0.30
  X=1      0.20   0.15   0.10   |  0.45
  X=2      0.05   0.10   0.10   |  0.25
  ---------+------+------+------+---------
  Col sum   0.35   0.40   0.25  |  1.00
  =P(Y=y)

E[X] = 0(0.30) + 1(0.45) + 2(0.25) = 0.95
E[Y] = 0(0.35) + 1(0.40) + 2(0.25) = 0.90
E[X+Y] = E[X] + E[Y] = 0.95 + 0.90 = 1.85

KEY: E[X+Y] = E[X]+E[Y] ALWAYS, even if dependent!
This is LINEARITY OF EXPECTATION.
```

---

## 🧮 P18: Variance & Standard Deviation

> 📘 [Ch 29](./Probability_BootCamp_THEORY.md#chapter-29--variance--standard-deviation) | [Index](#-problem-index)

**Q: P(X=1)=0.2, P(X=2)=0.5, P(X=3)=0.3. Find E[X], Var, sigma.**

```
  Small Var: values cluster tight    |    ****    |
  Large Var: values spread wide   *  |   *  *  * | *

Step 1: E[X] = 1(0.2) + 2(0.5) + 3(0.3)
             = 0.2 + 1.0 + 0.9 = 2.1

Step 2: E[X^2] = 1(0.2) + 4(0.5) + 9(0.3)
               = 0.2 + 2.0 + 2.7 = 4.9

Step 3: Var(X) = E[X^2] - (E[X])^2
               = 4.9 - (2.1)^2 = 4.9 - 4.41 = 0.49

Step 4: sigma = sqrt(0.49) = 0.7

MEANING: average=2.1, typical deviation=0.7
  Most values in [2.1-0.7, 2.1+0.7] = [1.4, 2.8]

BONUS: Var(3X+5) = 3^2 * Var(X) = 9*0.49 = 4.41
  (shifting +5 doesn't change spread, scaling *3 multiplies var by 9)
```

---

## 🧮 P19: Inequalities, LLN & CLT

> 📘 [Ch 30,33](./Probability_BootCamp_THEORY.md#chapter-30--markov--chebyshev-inequalities) | [Index](#-problem-index)

**Q: (a) E[X]=50, bound P(X>=200). (b) u=100,s=15, bound P(|X-100|>=45). (c) n=36,u=80,s=12, P(Xbar>84)?**

### (a) Markov

```
P(X>=a) <= E[X]/a.   P(X>=200) <= 50/200 = 25%.
"At most 25% chance. Loose but works for ANY X>=0."
```

### (b) Chebyshev

```
P(|X-u|>=ks) <= 1/k^2.  k = 45/15 = 3.
P(|X-100|>=45) <= 1/9 = 11.1%.
"Works for ANY distribution! (Normal actual: 0.3%)"
```

### (c) CLT

```
CLT: Xbar ~ N(u, s^2/n) = N(80, 144/36) = N(80, 4)
sigma_Xbar = 2.

Z = (84-80)/2 = 2.0
P(Xbar>84) = P(Z>2) = 1 - 0.9772 = 0.0228 = 2.3%

  WHY sqrt(n) MATTERS:
  Individual:       sigma = 12     (wide)
  Average of 36:    sigma = 12/6 = 2 (narrow!)

  More samples -> average gets MORE PRECISE.
  This is LLN + CLT working together!

🤖 AI/ML: Larger batch size = more stable gradient!
```

---

## 🧮 P20: Covariance & Correlation

> 📘 [Ch 32](./Probability_BootCamp_THEORY.md#chapter-32--covariance--correlation) | [Index](#-problem-index)

**Q: From P17's table, find Cov(X,Y), rho. Independent?**

### What do Cov and rho measure?

```
  rho=+1     rho=+0.5    rho=0      rho=-0.7
    /          .  .       . . .       .
   /          . .        .  .  .       . .
  /          . .  .     .  . .  .     .    .
             .  . .      . .  .      .      .
  perfect    moderate     no linear   strong neg
```

### Calculation

```
From P17: E[X]=0.95, E[Y]=0.90

E[XY] = 1*1*0.15 + 1*2*0.10 + 2*1*0.10 + 2*2*0.10
      = 0.15 + 0.20 + 0.20 + 0.40 = 0.95

Cov(X,Y) = E[XY] - E[X]*E[Y] = 0.95 - 0.855 = 0.095

Var(X) = 1.45 - 0.95^2 = 0.5475   sX = 0.7399
Var(Y) = 1.40 - 0.90^2 = 0.59     sY = 0.7681

rho = 0.095 / (0.7399*0.7681) = 0.095/0.5683 = 0.167

Independent? Check: P(X=0,Y=0)=0.10 vs P(X=0)*P(Y=0)=0.105
  0.10 != 0.105 -> NOT independent!

  SUMMARY:
  Cov = 0.095 > 0  :  weak positive
  rho = 0.167       :  weak positive linear correlation
  NOT independent    :  joint != product of marginals

  REMEMBER: Independent -> Cov=0. But Cov=0 does NOT mean independent!

🤖 AI/ML: Covariance matrix is the heart of PCA.
   Eigenvectors of Cov = principal components!
```

---

## 60-SECOND REVISION

```
COUNT:  P(n,r) for order, C(n,k) for no order
BASIC:  P(A)=fav/total  P(Ac)=1-P(A)  P(AuB)=P(A)+P(B)-P(AnB)
COND:   P(A|B)=P(AnB)/P(B)  "shrink universe to B"
BAYES:  P(A|B)=P(B|A)P(A)/P(B)  "flip cause and effect"
INDEP:  P(AnB)=P(A)P(B)  "knowing B doesn't help with A"
BINOM:  P(k)=C(n,k)p^k(1-p)^(n-k)   E=np  Var=np(1-p)
POISSON: P(k)=e^(-L)L^k/k!           E=Var=L
NORMAL:  Z=(X-u)/s  68-95-99.7 rule
EXPON:   P(T>t)=e^(-Lt)  memoryless  E=1/L
E[X]=Sum xP(x)  Var=E[X^2]-(E[X])^2  sigma=sqrt(Var)
CLT: averages -> Normal.  LLN: averages -> u.
Cov=E[XY]-E[X]E[Y]  rho=Cov/(sX*sY) in [-1,1]
```

---

> [<< Back to INDEX](./Probability_BootCamp_INDEX.md) | [<< Theory Guide](./Probability_BootCamp_THEORY.md)
>
> Created for: ODS | ML
