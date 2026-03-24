# 🧠 Topic 03 — Memory-Bounded Heuristic Search (IDA*, RBFS, SMA*)

> **Difficulty**: 🔴 Hard | **Syllabus Section**: Search
>
> **Slides**: RB-M | **Quiz Relevance**: ⭐⭐⭐

---

## 🍼 The Big Story (ELI5)

### The Notebook Problem 📓

Remember A*? It's brilliant — always finds the best path! But it has a HUGE problem: it writes down EVERY room it discovers on sticky notes. For big mazes, you'd need MILLIONS of sticky notes. Your notebook runs out of pages!

So smart scientists invented ways to be ALMOST as smart as A* but use WAY fewer sticky notes:

> 🍼 **The Three Solutions — Kid Stories:**
>
> **IDA* (The Budget Explorer)**: "I'll only explore paths costing up to $5. Found nothing? Okay, now up to $7. Still nothing? Up to $10." Each round, you increase your budget. You only need to remember the path you're currently walking — no sticky notes for other paths!
>
> **RBFS (The Breadcrumb Explorer)**: "I'll walk down one path, but I'll leave a breadcrumb at each fork saying 'the OTHER path costs at least $X.' If my current path gets too expensive, I go back to the cheapest breadcrumb."
>
> **SMA* (The Fixed Notebook)**: "I have exactly 100 sticky notes. When I run out, I erase the WORST one and reuse it for a new room."

---

## 📚 Table of Contents

1. [Why A* Runs Out of Memory](#1-the-memory-problem)
2. [IDA* — Iterative Deepening A*](#2-ida-star)
3. [RBFS — Recursive Best-First Search](#3-rbfs)
4. [SMA* — Simplified Memory-Bounded A*](#4-sma-star)
5. [Comparison](#5-comparison)
6. [Key Takeaways](#6-key-takeaways)
7. [Exam Tips](#7-exam-tips)

---

## 1. The Memory Problem

### Why A* Runs Out of Memory

A* stores ALL generated nodes in memory. For big problems this explodes:

```
Problem        Branching(b)  Depth(d)   Nodes     Memory Needed
───────────────────────────────────────────────────────────────
8-Puzzle       ~3            ~25        3^25      ~800 billion nodes!
15-Puzzle      ~3            ~50        3^50      More than atoms in you!
Robot path     ~8            ~100       8^100     Universe isn't big enough!
```

**A*'s space = O(b^d) = EXPONENTIAL → 💀 for big problems**

### What We Want

Keep A*'s optimality (always finds the best path) but use memory that grows **linearly** O(bd) instead of exponentially O(b^d).

---

## 2. IDA* — Iterative Deepening A*

### The Core Idea

Remember how IDS (Topic 01) did DFS with increasing depth limits?

**IDA* does the same thing, but instead of a DEPTH limit, it uses an f-cost limit!**

```
IDS:   "Don't go deeper than L levels"
IDA*:  "Don't explore paths with f(n) = g(n)+h(n) > limit"
```

### The Algorithm

```
function IDA_STAR(problem):
    limit = h(start)           ← Initial limit = heuristic of start
    
    loop:
        result, new_limit = DFS_WITH_LIMIT(start, 0, limit)
        if result == FOUND: return solution
        if new_limit == ∞: return FAILURE   ← No solution exists
        limit = new_limit      ← Increase limit to the smallest f that exceeded it

function DFS_WITH_LIMIT(node, g, limit):
    f = g + h(node)
    if f > limit: return CUTOFF, f          ← Too expensive! Report my f-value
    if node is goal: return FOUND, 0
    
    next_limit = ∞             ← Track smallest f that exceeded limit
    for each child of node:
        result, child_f = DFS_WITH_LIMIT(child, g + cost, limit)
        if result == FOUND: return FOUND, 0
        next_limit = min(next_limit, child_f)
    
    return CUTOFF, next_limit
```

### 🧮 IDA* Complete Trace (Step by Step!)

**Problem**: Find cheapest path from A to G

```
Graph:
        A ──(3)──> B ──(4)──> G
        |                      ↑
       (1)                    (2)
        ↓                      |
        C ──(5)──> D ──(2)──> G

Heuristic h (straight-line estimates to G):
  A: h=6,  B: h=4,  C: h=7,  D: h=2,  G: h=0
```

**Iteration 1: limit = h(A) = 6**

```
Explore A:  f(A) = g(0) + h(6) = 6.  6 ≤ 6? YES, continue.
  ├── Explore B: f(B) = g(3) + h(4) = 7.  7 ≤ 6? NO! ✂️ CUTOFF. Record 7.
  └── Explore C: f(C) = g(1) + h(7) = 8.  8 ≤ 6? NO! ✂️ CUTOFF. Record 8.

Result: NOT FOUND. Next limit = min(7, 8) = 7
```

> 🍼 "I checked with a budget of $6. Path through B costs at least $7, path through C costs at least $8. Both too expensive! Let me raise my budget to $7."

**Iteration 2: limit = 7**

```
Explore A:  f(A) = 0+6 = 6 ≤ 7? YES ✓
  ├── Explore B: f(B) = 3+4 = 7 ≤ 7? YES ✓
  │     └── Explore G via B: f(G) = 3+4+0 = 7 ≤ 7? YES ✓
  │         g(G) = 3+4 = 7. IS IT THE GOAL? YES! 🎯
  │         But wait — is this the best? (Yes, because f = 7 = limit)
  │
  └── (C would cost 8 > 7, so it's still cut off)

FOUND! Path: A→B→G, cost = 3+4 = 7
```

> 🍼 "With budget $7, the path through B fits! A→B costs $3, B→G costs $4, total $7. Found it!"

**But is there a cheaper path through C→D→G?**
```
A→C→D→G = 1+5+2 = 8 (more expensive than 7!)
```
So IDA* found the OPTIMAL path! ✅

### Why IDA* Uses Almost No Memory

```
At any moment, IDA* only stores:
  - The current path from root to the node being explored
  - That's it! No frontier, no explored set!

Memory = O(b × d) = LINEAR (same as DFS!)

Compare with A*: O(b^d) = EXPONENTIAL
```

### When IDA* Struggles

**Problem**: If f-values are real numbers (like 3.14159), almost every node has a UNIQUE f-value. Each iteration only adds ONE node → thousands of iterations needed!

```
Iteration 1: limit = 5.000 → explores 1 node past limit
Iteration 2: limit = 5.001 → explores 1 more node
Iteration 3: limit = 5.003 → explores 1 more node
... (thousands of iterations!)
```

**Solution**: Use RBFS or SMA* for real-valued costs.

### IDA* Properties

| Property | Value |
|---|---|
| **Complete?** | ✅ Yes |
| **Optimal?** | ✅ Yes (with admissible h) |
| **Time** | O(b^d) — same as A* |
| **Space** | **O(b × d) — LINEAR!** The whole point! |
| **Best for** | Integer/discrete costs (few unique f-values) |

---

## 3. RBFS — Recursive Best-First Search

### The Idea

RBFS explores depth-first like IDA*, but it **remembers the f-value of the best alternative** at each level. When the current path becomes too expensive (exceeds the best alternative), it **backtracks** and updates the parent's f-value to remember how good this subtree was.

> 🍼 **Kid Version**: You're exploring a cave. At every fork, your friend stands there and writes on the wall: "The other tunnel costs at least $15." If your tunnel costs more than $15, you come back and try the other one. When you leave a tunnel, you update the wall sign with the actual cost you found.

### How the "Backed-Up" f-value Works

```
At node B, we explored its subtree and found the best path costs f=12.
We backtrack from B. But we UPDATE B's f-value to 12.
Now if we ever reconsider B, we know it costs at least 12 — no need to re-explore!
```

This is the key trick: **when backtracking, store the best f-value found so you don't forget!**

### RBFS Properties

| Property | Value |
|---|---|
| **Complete?** | ✅ Yes |
| **Optimal?** | ✅ Yes (with admissible h) |
| **Space** | O(b × d) — LINEAR! |
| **Time** | Can be worse than A* (re-expands forgotten nodes) |
| **Best for** | Real-valued costs, when IDA* has too many iterations |

---

## 4. SMA* — Simplified Memory-Bounded A*

### The Idea

Run A* normally until memory is FULL. Then, to make room for a new node, **drop the WORST node** (highest f-value on the frontier) and reuse that memory slot.

> 🍼 **Kid Version**: You have a backpack that holds exactly 10 sticky notes. When it's full and you find a new room:
> 1. Find the WORST sticky note in your backpack (highest cost room)
> 2. Write that room's cost on its PARENT's note (so the parent remembers)
> 3. Throw away the worst note
> 4. Write the new room on the freed-up note

### The Memory-Time Trade-off

```
More memory → fewer forgotten nodes → faster (closer to A*)
Less memory → more forgotten/regenerated nodes → slower (closer to IDA*)
Unlimited memory → SMA* = A* exactly!
```

### SMA* Properties

| Property | Value |
|---|---|
| **Complete?** | ✅ Yes (if solution fits in memory) |
| **Optimal?** | ✅ Yes (if optimal solution fits in memory) |
| **Space** | Whatever you set! (configurable) |
| **Best for** | When you know exactly how much memory you can afford |

---

## 5. Comparison

| Feature | A* | IDA* | RBFS | SMA* |
|---|---|---|---|---|
| **Space** | O(b^d) 💀 | O(bd) ✅ | O(bd) ✅ | You choose! |
| **Optimal?** | ✅ | ✅ | ✅ | ✅ (if fits) |
| **Re-expands?** | Never | Between iterations | Often | Sometimes |
| **Best for** | Small problems | Integer costs | General use | Fixed memory |

### Decision Flowchart

```
Can A* fit in memory?
├── YES → Use A* (fastest!)
└── NO → Are costs integers?
         ├── YES → Use IDA* (simple and effective)
         └── NO → Want fixed memory budget?
                  ├── YES → Use SMA*
                  └── NO → Use RBFS
```

---

## 6. Key Takeaways

1. **A*'s memory = exponential** → can't solve big problems
2. **IDA*** = A* + iterative deepening → linear memory, optimal, great for integer costs
3. **RBFS** = remembers best alternative cost → linear memory, handles real costs
4. **SMA*** = A* with a memory budget → drops worst nodes when full
5. **All three are optimal** with admissible heuristics — the trade-off is memory vs time
6. **The backed-up f-value trick** is key: when forgetting a subtree, store its best cost at the parent

---

## 7. Exam Tips

### Must-Know

1. **Trace IDA*** showing iterations with different limits and which nodes get pruned
2. **Explain why the limit increases** to the minimum pruned f-value (not limit+1!)
3. **Compare space: A* = O(b^d) vs IDA*/RBFS = O(bd)**

### Common Mistakes

❌ Thinking IDA* limit increases by 1 each time (it increases to the SMALLEST f that was pruned!)
❌ Forgetting that RBFS can re-expand the SAME nodes many times
❌ Assuming SMA* always finds optimal (only if the solution PATH fits in memory)

---

## 📖 References

- [AIMA — Chapter 3.5.3-3.5.5](Russell & Norvig - https://aima.cs.berkeley.edu/contents.html)

---

[⬅️ Prev: Informed Search](../02_Search_Informed_Greedy_Astar/README.md) | [Back to Main](../README.md) | [Next: Local & Evolutionary Search ➡️](../04_Search_Local_and_Evolutionary/README.md)
