# ♟️ Topic 08 — Adversarial Search: Minimax Algorithm

> **Difficulty**: 🟡 Medium | **Syllabus Section**: Adversarial Search
>
> **Slides**: RB-M & SD-M | **Quiz Relevance**: ⭐⭐⭐⭐⭐

---

## 🍼 The Big Story (ELI5)

### The Cookie Game 🍪

Imagine you and your sister are playing a game. There are cookies on a table, and you take turns:
- **Your turn**: You want to get the MOST cookies possible → **MAXIMIZE**
- **Sister's turn**: She wants to give you the FEWEST cookies possible → **MINIMIZE**

You're trying to **MAX**imize. She's trying to **MIN**imize. That's **MINIMAX**!

> 🍼 **Kid Version**: You and your opponent take turns. You ALWAYS pick the move that's BEST for you. Your opponent ALWAYS picks the move that's WORST for you. Minimax figures out: "If BOTH of us play perfectly, what's the best I can guarantee?"

Think of it like this:
- When it's YOUR turn → pick the **BIGGEST** number (MAX)
- When it's OPPONENT's turn → they pick the **SMALLEST** number (MIN)
- Work from the BOTTOM of the tree UP to figure out what happens

---

## 📚 Table of Contents

1. [Games as Search Problems](#1-games)
2. [The Game Tree](#2-game-tree)
3. [Minimax Algorithm](#3-minimax)
4. [🧮 Complete Worked Example](#4-worked-example)
5. [Depth-Limited Minimax + Evaluation Functions](#5-eval-functions)
6. [Key Takeaways](#6-key-takeaways)
7. [Exam Tips](#7-exam-tips)

---

## 1. Games as Search Problems

### What Defines a Game?

| Component | Meaning | Tic-Tac-Toe Example |
|---|---|---|
| **Initial State** | Starting position | Empty 3×3 board |
| **Players** | Who moves? | X (MAX) and O (MIN) |
| **Actions** | Legal moves | Place X or O in empty cell |
| **Result** | New state after move | Board with new mark |
| **Terminal Test** | Is the game over? | 3-in-a-row, or board full |
| **Utility** | Score at game end | +1 (X wins), 0 (draw), -1 (O wins) |

### Zero-Sum Games

**What YOU gain, your opponent LOSES.** Your +1 is their -1. Total = 0.

Examples: Chess, Tic-Tac-Toe, Go, Checkers.

---

## 2. The Game Tree

A game tree shows ALL possible moves for ALL players:

```
MAX's turn:            A                    ← MAX picks HIGHEST
                      / \
MIN's turn:          B   C                  ← MIN picks LOWEST
                    / \   / \
Terminal:          3   5 2   9              ← Known scores
```

**How to read it**: The bottom numbers are the game scores (for MAX). We work BOTTOM-UP:
- MIN at B: picks min(3, 5) = **3** (gives MAX the worst option)
- MIN at C: picks min(2, 9) = **2**
- MAX at A: picks max(3, 2) = **3** (chooses the better option)

MAX's best move = go to B (guaranteed score of 3).

---

## 3. Minimax Algorithm

### The Formula

```
MINIMAX(state) = 
  UTILITY(state)                          if terminal state
  MAX over children's MINIMAX values      if it's MAX's turn
  MIN over children's MINIMAX values      if it's MIN's turn
```

### Pseudocode

```
function MINIMAX_DECISION(state):
    best_action = the action a that gives max MIN_VALUE(Result(state, a))
    return best_action

function MAX_VALUE(state):
    if terminal(state): return utility(state)
    v = -∞                              ← Start with worst possible
    for each action a:
        v = max(v, MIN_VALUE(Result(state, a)))
    return v

function MIN_VALUE(state):
    if terminal(state): return utility(state)
    v = +∞                              ← Start with best possible (for MAX)
    for each action a:
        v = min(v, MAX_VALUE(Result(state, a)))
    return v
```

---

## 4. 🧮 Complete Worked Example (Exam-Style!)

### The Tree

```
                           A (MAX)
                        /    |    \
                B (MIN)   C (MIN)   D (MIN)
               / \        / \        / \
              E    F     G    H     I    J
              3    12    8    2     4    6
```

### Step-by-Step Solution (Bottom Up)

**Step 1: Leaf values are given (these are game outcomes)**
```
E = 3,  F = 12,  G = 8,  H = 2,  I = 4,  J = 6
```

**Step 2: Calculate MIN nodes (MIN picks the SMALLEST child)**

```
Node B (MIN): children are E=3 and F=12
  B = min(3, 12) = 3
  
  🍼 Why? B is MIN's turn. MIN wants MAX to get as FEW points as possible.
  Between 3 and 12, MIN picks 3 (worse for MAX).
  It's like your opponent saying "I'll make sure you only get 3, not 12!"
```

```
Node C (MIN): children are G=8 and H=2
  C = min(8, 2) = 2
  
  🍼 MIN picks 2 instead of 8. "You're only getting 2 points, not 8!"
```

```
Node D (MIN): children are I=4 and J=6
  D = min(4, 6) = 4
  
  🍼 MIN picks 4 instead of 6.
```

**Step 3: Calculate MAX node (MAX picks the LARGEST child)**

```
Node A (MAX): children are B=3, C=2, D=4
  A = max(3, 2, 4) = 4
  
  🍼 It's MAX's turn! MAX looks at the three options:
  "If I go to B, I'll get 3 (because MIN will give me 3 there)"
  "If I go to C, I'll get 2 (because MIN will give me 2 there)"
  "If I go to D, I'll get 4 (because MIN will give me 4 there)"
  "4 is the best! I choose D!"
```

**Final tree with all values filled in:**

```
                        A = 4 (MAX) ← MAX chooses D!
                       /    |    \
              B = 3      C = 2     D = 4 ★ (best for MAX)
              / \        / \        / \
             3   12     8   2      4   6
```

**Answer**: MAX's optimal move is D, guaranteeing a score of 4.

### 🧮 Another Example (3 levels deep)

```
                         A (MAX)
                       /         \
               B (MIN)           C (MIN)
              /    \            /    \
         D (MAX)  E (MAX)  F (MAX)  G (MAX)
         / \      / \      / \      / \
        3   17   2   12   15   2   5   2
```

**Step 1**: Leaf values: 3, 17, 2, 12, 15, 2, 5, 2

**Step 2**: MAX nodes (pick biggest):
```
D = max(3, 17)  = 17    "I want 17, not 3!"
E = max(2, 12)  = 12    "I want 12, not 2!"
F = max(15, 2)  = 15    "I want 15, not 2!"
G = max(5, 2)   = 5     "I want 5, not 2!"
```

**Step 3**: MIN nodes (pick smallest):
```
B = min(17, 12) = 12    "I'll only let you have 12, not 17!"
C = min(15, 5)  = 5     "I'll only let you have 5, not 15!"
```

**Step 4**: MAX at root:
```
A = max(12, 5) = 12     "12 is better than 5. I choose B!"
```

```
                      A = 12 (MAX) → Choose B!
                     /              \
              B = 12 ★              C = 5
             /    \                /    \
         D = 17  E = 12       F = 15  G = 5
         / \      / \          / \      / \
        3   17   2   12      15   2    5   2
```

### Properties

| Property | Value | Why |
|---|---|---|
| **Complete?** | ✅ Yes (finite trees) | Explores entire tree |
| **Optimal?** | ✅ Yes (against optimal opponent) | Assumes perfect play |
| **Time** | O(b^m) | Must explore full tree |
| **Space** | O(b × m) | DFS exploration |

---

## 5. Depth-Limited Minimax + Evaluation Functions

### The Problem

Chess has b≈35, m≈100 → 35^100 nodes. **Impossible to search the whole tree!**

### The Solution

1. **Stop searching at depth d** (not the bottom of the tree)
2. At depth d, use an **evaluation function EVAL(s)** to ESTIMATE the score

```
H_MINIMAX(state, depth):
    if TERMINAL(state): return UTILITY(state)
    if depth == 0: return EVAL(state)     ← Use estimate!
    if MAX's turn: return max of children's H_MINIMAX(child, depth-1)
    if MIN's turn: return min of children's H_MINIMAX(child, depth-1)
```

### What is an Evaluation Function?

An EVAL(s) gives a **score** that estimates how good the position is for MAX.

**Chess example:**
```
EVAL(s) = w₁ × (material) + w₂ × (mobility) + w₃ × (king safety) + ...

Material score:
  Queen  = 9 points
  Rook   = 5 points
  Bishop = 3 points  
  Knight = 3 points
  Pawn   = 1 point

EVAL = (your material - opponent's material) + other factors

Example: You have 1 Queen + 2 Rooks + 1 Bishop vs opponent's 1 Rook + 3 Pawns
  Your material:  9 + 5 + 5 + 3 = 22
  Their material: 5 + 1 + 1 + 1 = 8
  Material advantage: 22 - 8 = +14 → You're winning!
```

> 🍼 **Kid Version**: Since you can't play the WHOLE game in your head, you play 5 moves ahead and then say "Hmm, I have more toys than my opponent, so I'm probably winning." The evaluation function is your "gut feeling" about who's winning.

---

## 6. Key Takeaways

1. **Games are adversarial** — opponent tries to MINIMIZE your score
2. **MAX nodes** pick the LARGEST child; **MIN nodes** pick the SMALLEST
3. **Work BOTTOM-UP**: start from leaf values, propagate up through MAX/MIN
4. **Minimax is optimal** against a perfect opponent
5. **Time = O(b^m)** — exponential! → need Alpha-Beta pruning (next topic!)
6. **Depth limit + evaluation function** for real games (can't search to the bottom)

---

## 7. Exam Tips

### Must-Know

1. **Fill in minimax values** bottom-up on a given tree (MOST COMMON EXAM QUESTION!)
2. **Identify MAX's best move** from the root
3. **Know the simple rule**: MAX=biggest, MIN=smallest
4. **Explain evaluation functions** for a given game

### The #1 Exam Trick 🪤

**DON'T mix up MAX and MIN!** At MAX nodes pick max(), at MIN nodes pick min().

Draw MAX with △ (triangle up = going up = maximum) and MIN with ▽ (triangle down = going down = minimum).

### Step-by-Step Method for Exams

1. Write the leaf (terminal) values
2. At each MIN node: write min(children)
3. At each MAX node: write max(children)
4. At the root: the value = game value, the child that gave it = best move

---

## 📖 References

- AIMA — Chapter 5.1-5.2

---

[⬅️ Prev: CSP Local Search](../07_CSP_Local_Search/README.md) | [Back to Main](../README.md) | [Next: Alpha-Beta Pruning ➡️](../09_Alpha_Beta_Pruning/README.md)
