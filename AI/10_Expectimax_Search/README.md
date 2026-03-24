# 🎲 Topic 10 — Expectimax Search

> **Difficulty**: 🟡 Medium | **Syllabus Section**: Adversarial Search
>
> **Slides**: SD-M | **Quiz Relevance**: ⭐⭐⭐⭐

---

## 🍼 The Big Story (ELI5)

### Minimax vs Expectimax — Two Board Games

**Game 1 (Chess — use Minimax)**: You play against your GENIUS big sister. She ALWAYS picks the move that hurts you the most. You need to plan for the WORST case.

**Game 2 (Backgammon — use Expectimax)**: You roll DICE before each move. The dice don't HATE you — they're random! Sometimes you roll a 6 (great!), sometimes a 1 (bad). You should plan for the AVERAGE case.

> 🍼 **The Simplest Explanation**:
> - **Minimax**: "My opponent is a GENIUS who always picks the WORST move for me" → plan for the worst
> - **Expectimax**: "My opponent is a RANDOM monkey throwing darts" → plan for the average

---

## 📚 Table of Contents

1. [When Is Minimax Wrong?](#1-when-minimax-wrong)
2. [The Three Node Types](#2-three-nodes)
3. [How CHANCE Nodes Work (The Key Math!)](#3-chance-nodes)
4. [🧮 Complete Example 1: Coin Flip Game](#4-example-1)
5. [🧮 Complete Example 2: Loaded Dice Game](#5-example-2)
6. [🧮 Complete Example 3: Three Outcomes](#6-example-3)
7. [Minimax vs Expectimax Side by Side](#7-comparison)
8. [Why Alpha-Beta Pruning Doesn't Work Here](#8-no-pruning)
9. [Key Takeaways](#9-key-takeaways)
10. [Exam Tips](#10-exam-tips)

---

## 1. When Is Minimax Wrong?

Minimax assumes your opponent is PERFECT. But what if the opponent is:

```
Scenario                    Minimax thinks           Reality              Use what?
─────────────────────────────────────────────────────────────────────────────────
Chess grandmaster           "They'll destroy me"     They WILL destroy you   Minimax ✅
Random 3-year-old player    "They'll destroy me"     They make random moves  Expectimax ✅
Dice roll                   "Dice hate me"           Dice are random!        Expectimax ✅
Pac-Man random ghosts       "Ghosts are hunting me"  Ghosts move randomly    Expectimax ✅
```

**The problem with Minimax for random opponents:**

```
        YOU (MAX)
       /         \
  Move A         Move B
  (MIN)          (MIN)
  /    \         /    \
 2    100       3      4

Minimax says:
  A: MIN picks min(2, 100) = 2
  B: MIN picks min(3, 4) = 3
  MAX picks max(2, 3) = 3 → Choose B!

But if opponent is RANDOM (50/50):
  A: Average = (2 + 100) / 2 = 51   ← MUCH better!
  B: Average = (3 + 4) / 2 = 3.5

Expectimax picks A (expected value 51 >> 3.5)!

Minimax was too PESSIMISTIC — it avoided Move A because of the 
worst case (2), but the AVERAGE case (51) is amazing!
```

---

## 2. The Three Node Types

### In Minimax: MAX and MIN

```
MAX node: YOU pick the BIGGEST child       (your turn)
MIN node: OPPONENT picks the SMALLEST child (opponent's turn)
```

### In Expectimax: MAX and CHANCE

```
MAX node: YOU pick the BIGGEST child           (your turn — same!)
CHANCE node: NOBODY picks — compute the AVERAGE (random event)
```

**CHANCE replaces MIN.** Instead of an evil opponent picking the worst, random chance gives you an AVERAGE.

```
MINIMAX tree:                    EXPECTIMAX tree:
     MAX                              MAX
    / \                               / \
  MIN   MIN                       CHANCE  CHANCE
  / \   / \                        / \      / \
 3   7 5   1                   (0.5)(0.5)(0.5)(0.5)
                                 3   7    5   1

MIN picks: min(3,7)=3, min(5,1)=1    CHANCE computes: avg(3,7)=5, avg(5,1)=3
MAX picks: max(3,1)=3                 MAX picks: max(5,3)=5

Minimax: best guaranteed = 3          Expectimax: best expected = 5
```

---

## 3. How CHANCE Nodes Work (The Key Math!)

### What Does a CHANCE Node Compute?

A CHANCE node computes the **weighted average** (expected value) of its children:

```
CHANCE value = P(outcome₁) × Value(outcome₁) 
             + P(outcome₂) × Value(outcome₂) 
             + P(outcome₃) × Value(outcome₃) + ...
```

### 🧮 What Is a "Weighted Average"? (From Zero!)

**Regular average** (when all outcomes are equally likely):
```
You flip a coin and get either 10 or 4. Each has 50% chance.

Average = (10 + 4) / 2 = 14 / 2 = 7

Or equivalently: 0.5 × 10 + 0.5 × 4 = 5 + 2 = 7
```

**Weighted average** (when outcomes have DIFFERENT probabilities):
```
You roll a loaded die:
  70% chance of getting 10
  30% chance of getting 4

Weighted average = 0.70 × 10 + 0.30 × 4 = 7.0 + 1.2 = 8.2

NOT just (10 + 4) / 2 = 7! The 10 is MORE likely so the average is HIGHER!
```

> 🍼 **Kid Version**: Imagine a bag with 7 red balls (worth $10 each) and 3 blue balls (worth $4 each). If you grab a random ball, what's the EXPECTED value? You're MORE likely to grab red ($10) than blue ($4), so the expected value is closer to $10 than to $4. Exactly: 0.7 × 10 + 0.3 × 4 = 8.2.

### ⚠️ CRITICAL: Probabilities Must Add to 1!

```
P(outcome₁) + P(outcome₂) + ... = 1.0   ← ALWAYS check this!

Example: P(Heads) = 0.5, P(Tails) = 0.5 → 0.5 + 0.5 = 1.0 ✅
Example: P(Win) = 0.7, P(Lose) = 0.3    → 0.7 + 0.3 = 1.0 ✅
Example: P(A) = 0.5, P(B) = 0.6         → 0.5 + 0.6 = 1.1 ❌ WRONG!
```

---

## 4. 🧮 Complete Example 1: Fair Coin Flip Game

```
                    YOU (MAX)
                   /         \
          Action A            Action B
          (CHANCE)            (CHANCE)
         /        \          /        \
      Heads     Tails     Heads     Tails
      p=0.5     p=0.5     p=0.5     p=0.5
       |          |          |         |
      10          4          7         8
```

### Step 1: Compute CHANCE node A

```
Value(A) = P(Heads) × V(Heads) + P(Tails) × V(Tails)

Plugging in:
         = 0.5 × 10 + 0.5 × 4

Computing step by step:
         = 5.0 + 2.0
         = 7.0

Check probabilities: 0.5 + 0.5 = 1.0 ✅
```

### Step 2: Compute CHANCE node B

```
Value(B) = 0.5 × 7 + 0.5 × 8
         = 3.5 + 4.0
         = 7.5

Check probabilities: 0.5 + 0.5 = 1.0 ✅
```

### Step 3: MAX picks the best

```
MAX = max(7.0, 7.5) = 7.5 → Choose Action B! ✅
```

> 🍼 **Kid Version**: "Action A is like flipping a coin where Heads gives $10 and Tails gives $4. On average I get $7. Action B gives Heads=$7 or Tails=$8, averaging $7.50. I pick B because $7.50 > $7!"

---

## 5. 🧮 Complete Example 2: Loaded Dice Game

Now with UNEQUAL probabilities:

```
                    YOU (MAX)
                   /         \
             A (CHANCE)    B (CHANCE)
            / | \           / | \
         p:0.1 0.3 0.6   p:0.5 0.3 0.2
          |    |    |       |    |    |
         100   50   0      60   60   60
```

### CHANCE node A:

```
Value(A) = P₁ × V₁ + P₂ × V₂ + P₃ × V₃
         = 0.1 × 100 + 0.3 × 50 + 0.6 × 0

Step by step:
  0.1 × 100 = 10.0
  0.3 × 50  = 15.0
  0.6 × 0   = 0.0
  
  Total = 10.0 + 15.0 + 0.0 = 25.0

Check probabilities: 0.1 + 0.3 + 0.6 = 1.0 ✅
```

### CHANCE node B:

```
Value(B) = 0.5 × 60 + 0.3 × 60 + 0.2 × 60

Step by step:
  0.5 × 60 = 30.0
  0.3 × 60 = 18.0
  0.2 × 60 = 12.0
  
  Total = 30.0 + 18.0 + 12.0 = 60.0

Check: 0.5 + 0.3 + 0.2 = 1.0 ✅
```

### MAX picks:

```
MAX = max(25.0, 60.0) = 60.0 → Choose B!
```

**Even though A has a CHANCE of getting 100 (the highest!), it usually gets 0! B always gets 60 — much more reliable.**

> 🍼 **Kid Version**: "Would you rather: (A) have a 10% chance of getting $100 but 60% chance of getting nothing, or (B) always get $60? Smart choice is B! Getting $60 for sure beats MAYBE getting $100."

---

## 6. 🧮 Complete Example 3: Three-Level Tree with MAX + CHANCE

```
                         MAX (you)
                      /            \
              CHANCE (dice)     CHANCE (dice)
             /       \          /       \
          p=0.6    p=0.4     p=0.5    p=0.5
            |        |         |        |
          MAX      MAX       MAX      MAX
          / \      / \       / \      / \
         8   3    2   7     5   6    4   9
```

### Step 1: Solve the bottom MAX nodes first

```
MAX₁ = max(8, 3) = 8     "I pick 8 over 3"
MAX₂ = max(2, 7) = 7     "I pick 7 over 2"
MAX₃ = max(5, 6) = 6     "I pick 6 over 5"
MAX₄ = max(4, 9) = 9     "I pick 9 over 4"
```

### Step 2: Solve CHANCE nodes

```
CHANCE_left  = 0.6 × MAX₁ + 0.4 × MAX₂
             = 0.6 × 8 + 0.4 × 7
             = 4.8 + 2.8
             = 7.6

CHANCE_right = 0.5 × MAX₃ + 0.5 × MAX₄
             = 0.5 × 6 + 0.5 × 9
             = 3.0 + 4.5
             = 7.5
```

### Step 3: Root MAX picks

```
MAX = max(7.6, 7.5) = 7.6 → Choose LEFT!
```

**Final tree:**
```
                      MAX = 7.6 → Left!
                     /            \
            CHANCE = 7.6      CHANCE = 7.5
            /       \          /       \
          (0.6)   (0.4)     (0.5)   (0.5)
         MAX=8   MAX=7     MAX=6   MAX=9
         / \      / \       / \      / \
        8   3    2   7     5   6    4   9
```

---

## 7. Minimax vs Expectimax Side by Side

| Feature | Minimax | Expectimax |
|---|---|---|
| **Opponent** | PERFECT (worst case) | RANDOM (average case) |
| **MIN nodes?** | ✅ Yes (opponent picks worst) | ❌ No (replaced by CHANCE) |
| **CHANCE nodes?** | ❌ No | ✅ Yes (computes average) |
| **α-β pruning?** | ✅ Yes! | ❌ NO! |
| **Against random opponent** | Too pessimistic | Just right! ✅ |
| **Against perfect opponent** | Just right! ✅ | Too optimistic |

### When to Use What

```
Opponent is a genius (chess)?        → Minimax (assume worst)
Opponent is random (Pac-Man ghosts)? → Expectimax (assume average)
Game has dice/cards (backgammon)?    → Expectimax (random outcomes)
Mix of skill + luck (poker)?         → Expectiminimax (MAX + MIN + CHANCE!)
```

---

## 8. Why Alpha-Beta Pruning Doesn't Work Here

In minimax, α-β pruning works because:
```
MIN always picks the SMALLEST → if we find something ≤ α, the rest can't help → skip!
```

In expectimax, CHANCE computes an AVERAGE:
```
CHANCE = 0.5 × 3 + 0.5 × ???
We NEED to know ??? to compute the average! Can't skip!
Every single child changes the average.
```

> 🍼 **Kid Version**: "In minimax, the mean opponent only keeps bad gifts — so if the first gift is already terrible, the rest don't matter. But in expectimax, EVERY gift matters because they ALL contribute to the average. You can't skip any!"

---

## 9. Key Takeaways

1. **Expectimax** = for random/chance events (not adversarial opponents)
2. **CHANCE node** = weighted average: Σ P(outcome) × Value(outcome)
3. **Probabilities must sum to 1** — always verify!
4. **MAX nodes** still pick the biggest (same as minimax)
5. **Cannot use α-β pruning** (every child affects the average)
6. **Minimax is pessimistic**, **Expectimax is realistic** for random opponents

---

## 10. Exam Tips

### Must-Know

1. **Compute CHANCE node values**: multiply each outcome by probability, then SUM
2. **Work BOTTOM-UP**: first leaves → then CHANCE/MAX → then root
3. **Check probabilities sum to 1**

### Common Mistakes

❌ Using min() for chance nodes → use WEIGHTED AVERAGE!
❌ Forgetting to MULTIPLY by probability: it's `p × v`, not just `v`
❌ Probabilities not summing to 1 → your answer will be wrong
❌ Trying α-β pruning with chance nodes → doesn't work!

### Quick Formula Card

```
Equal probability (fair coin/die):     V = (v₁ + v₂ + ... + vₙ) / n
Unequal probability (loaded die):      V = p₁v₁ + p₂v₂ + ... + pₙvₙ
Always check:                          p₁ + p₂ + ... + pₙ = 1
```

---

## 📖 References

- AIMA — Chapter 5.5

---

[⬅️ Prev: Alpha-Beta](../09_Alpha_Beta_Pruning/README.md) | [Back to Main](../README.md) | [Next: Propositional Logic ➡️](../11_Propositional_Logic/README.md)
