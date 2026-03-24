# 🔄 Topic 07 — CSP: Local Search (Min-Conflicts)

> **Difficulty**: 🟢 Easy | **Syllabus Section**: CSP, Min-Conflicts, CSP as Optimization
>
> **Slides**: SD-M | **Quiz Relevance**: ⭐⭐⭐

---

## 🍼 The Big Story (ELI5)

### The Seating Chart Trick 🪑

Remember backtracking? You carefully place ONE student at a time, checking rules after each. Slow and careful.

**Min-Conflicts says**: "Forget being careful! Just sit EVERYONE down randomly — even if some people are next to someone they hate! Then, one at a time, move the most unhappy person to a seat where they have the FEWEST complaints."

> 🍼 **Kid Version**: Imagine arranging 8 toy soldiers on a chess board. Just plop them all down randomly! Now look — some soldiers are "attacking" each other. Pick one that's in trouble and move it to the safest spot in its column. Keep doing this until nobody is attacking anyone. Done!

---

## 📚 Table of Contents

1. [The Idea: Start Complete, Then Fix](#1-the-idea)
2. [Min-Conflicts Algorithm](#2-algorithm)
3. [🧮 Complete 4-Queens Trace](#3-trace)
4. [Why It Works Amazingly Well](#4-why-it-works)
5. [Limitations](#5-limitations)
6. [Key Takeaways](#6-key-takeaways)
7. [Exam Tips](#7-exam-tips)

---

## 1. The Idea: Start Complete, Then Fix

### Backtracking vs Local Search for CSPs

```
BACKTRACKING:                      MIN-CONFLICTS:
Start with empty board             Start with FULL board (random!)
Place queen 1 → check              Count conflicts
Place queen 2 → check              Pick a conflicted queen
Place queen 3 → conflict!          Move her to least-conflict spot
  → Undo queen 3, try again        Repeat until 0 conflicts
  → Undo queen 2, try again
... (can take FOREVER)             ... (usually VERY fast!)
```

### When to Use Each

| Method | Best When | Weakness |
|---|---|---|
| **Backtracking** | Need to find ALL solutions or prove none exist | Can be very slow |
| **Min-Conflicts** | Just need ANY solution, problem has many solutions | Can't prove "no solution exists" |

---

## 2. Min-Conflicts Algorithm

```
function MIN_CONFLICTS(csp, max_steps):
    current = assign every variable a RANDOM value
    
    for step = 1 to max_steps:
        if current has 0 conflicts: return current  🎯
        
        var = pick a random CONFLICTED variable
        value = the value for var that causes FEWEST conflicts
        current[var] = value
    
    return FAILURE  (couldn't solve in max_steps tries)
```

> 🍼 **Kid Version**:
> 1. Put all toys down randomly on the board
> 2. Is anyone fighting? No? You're done! 🎉
> 3. Yes? Pick someone who IS fighting
> 4. Move them to the spot where they fight with the FEWEST others
> 5. Go back to step 2

---

## 3. 🧮 Complete 4-Queens Trace (Every Step!)

**Problem**: Place 4 queens on a 4×4 board so no two queens attack each other (no same row, column, or diagonal).

**Convention**: One queen per column. Queen in column i has a row value Q[i].

### Step 0: Random Initial Placement

Let's say we randomly place: Q = [2, 4, 1, 3] (Queen 1 in row 2, Queen 2 in row 4, etc.)

```
Column:  1   2   3   4
       ┌───┬───┬───┬───┐
Row 1: │   │   │ Q │   │  Q3
       ├───┼───┼───┼───┤
Row 2: │ Q │   │   │   │  Q1
       ├───┼───┼───┼───┤
Row 3: │   │   │   │ Q │  Q4
       ├───┼───┼───┼───┤
Row 4: │   │ Q │   │   │  Q2
       └───┴───┴───┴───┘
```

### Count ALL Conflicts

Two queens conflict if: same row, same column, OR same diagonal.
(Same column is impossible since we have one queen per column.)

**Check each pair:**
```
Q1(col1,row2) vs Q2(col2,row4): 
  Same row? 2≠4 NO
  Same diagonal? |1-2|=1, |2-4|=2, 1≠2 NO
  → No conflict ✅

Q1(col1,row2) vs Q3(col3,row1):
  Same row? 2≠1 NO  
  Same diagonal? |1-3|=2, |2-1|=1, 2≠1 NO
  → No conflict ✅

Q1(col1,row2) vs Q4(col4,row3):
  Same row? 2≠3 NO
  Same diagonal? |1-4|=3, |2-3|=1, 3≠1 NO
  → No conflict ✅

Q2(col2,row4) vs Q3(col3,row1):
  Same row? 4≠1 NO
  Same diagonal? |2-3|=1, |4-1|=3, 1≠3 NO
  → No conflict ✅

Q2(col2,row4) vs Q4(col4,row3):
  Same row? 4≠3 NO
  Same diagonal? |2-4|=2, |4-3|=1, 2≠1 NO
  → No conflict ✅

Q3(col3,row1) vs Q4(col4,row3):
  Same row? 1≠3 NO
  Same diagonal? |3-4|=1, |1-3|=2, 1≠2 NO
  → No conflict ✅
```

**Total conflicts = 0!** 🎉 We got LUCKY — the random placement is already a solution!

---

### Let's Try Again With a BAD Random Start

**Q = [1, 3, 1, 3]**: Queens in rows 1, 3, 1, 3

```
       ┌───┬───┬───┬───┐
Row 1: │ Q │   │ Q │   │  Q1 and Q3 — SAME ROW! ❌
       ├───┼───┼───┼───┤
Row 2: │   │   │   │   │
       ├───┼───┼───┼───┤
Row 3: │   │ Q │   │ Q │  Q2 and Q4 — SAME ROW! ❌
       ├───┼───┼───┼───┤
Row 4: │   │   │   │   │
       └───┴───┴───┴───┘
```

**Count conflicts:**
```
Q1(c1,r1) vs Q2(c2,r3): row 1≠3, diag |1-2|=1,|1-3|=2 → NO conflict
Q1(c1,r1) vs Q3(c3,r1): row 1=1 → CONFLICT! ❌ (same row!)
Q1(c1,r1) vs Q4(c4,r3): row 1≠3, diag |1-4|=3,|1-3|=2 → NO conflict
Q2(c2,r3) vs Q3(c3,r1): row 3≠1, diag |2-3|=1,|3-1|=2 → NO conflict
Q2(c2,r3) vs Q4(c4,r3): row 3=3 → CONFLICT! ❌ (same row!)
Q3(c3,r1) vs Q4(c4,r3): row 1≠3, diag |3-4|=1,|1-3|=2 → NO conflict

Conflicts per queen:
  Q1: 1 conflict (with Q3)
  Q2: 1 conflict (with Q4)  
  Q3: 1 conflict (with Q1)
  Q4: 1 conflict (with Q2)
Total: 2 conflicting pairs
```

### Min-Conflicts Step 1

**Pick a conflicted variable randomly**: Say we pick Q3 (in column 3, currently row 1)

**Try each row for Q3 and count conflicts:**

```
Q3 in row 1 (current): conflicts with Q1(same row!) = 1 conflict
Q3 in row 2: check vs Q1(c1,r1): diag |3-1|=2,|2-1|=1 NO. vs Q2(c2,r3): diag |3-2|=1,|2-3|=1 YES! ❌
             vs Q4(c4,r3): row 2≠3, diag |3-4|=1,|2-3|=1 YES! ❌ → 2 conflicts
Q3 in row 3: check vs Q2(c2,r3): same row! ❌. vs Q4(c4,r3): same row! ❌ → 2 conflicts  
Q3 in row 4: check vs Q1: diag |3-1|=2,|4-1|=3 NO. vs Q2: diag |3-2|=1,|4-3|=1 YES! ❌
             vs Q4: row 4≠3, diag |3-4|=1,|4-3|=1 YES! ❌ → 2 conflicts

Summary:
  Row 1: 1 conflict (current)
  Row 2: 2 conflicts
  Row 3: 2 conflicts
  Row 4: 2 conflicts

MINIMUM = Row 1 (1 conflict). That's the current position! No improvement possible for Q3.
```

Hmm, Q3 can't improve. Let's pick another: **Q1 (column 1, currently row 1)**

```
Q1 in row 1 (current): conflicts with Q3(c3,r1) same row → 1 conflict
Q1 in row 2: vs Q2(c2,r3): diag |1-2|=1,|2-3|=1 YES ❌ → 1 conflict
Q1 in row 3: vs Q2(c2,r3): same row! ❌. vs Q4(c4,r3): same row! ❌ → 2 conflicts
Q1 in row 4: vs Q2(c2,r3): diag |1-2|=1,|4-3|=1 YES ❌ → 1 conflict

Summary:
  Row 1: 1 conflict (current)
  Row 2: 1 conflict (tie!)
  Row 3: 2 conflicts
  Row 4: 1 conflict (tie!)

Minimum = 1 (rows 1, 2, or 4). Pick randomly from non-current ties → Row 2
```

**Move Q1 to row 2**: Q = [2, 3, 1, 3]

```
       ┌───┬───┬───┬───┐
Row 1: │   │   │ Q │   │
       ├───┼───┼───┼───┤
Row 2: │ Q │   │   │   │
       ├───┼───┼───┼───┤
Row 3: │   │ Q │   │ Q │  ← Still same row conflict!
       ├───┼───┼───┼───┤
Row 4: │   │   │   │   │
       └───┴───┴───┴───┘

Remaining conflicts: Q2 vs Q4 (both row 3) = 1 pair
```

### Min-Conflicts Step 2

Pick Q4 (conflicted). Try each row:

```
Q4 in row 1: vs Q3(c3,r1) same row ❌ → 1 conflict
Q4 in row 2: vs Q1(c1,r2) diag |4-1|=3,|2-2|=0 NO → 0 conflicts! ✅
Q4 in row 3: vs Q2(c2,r3) same row ❌ → 1 conflict (current)
Q4 in row 4: vs Q2(c2,r3) diag |4-2|=2,|4-3|=1 NO → 0 conflicts! ✅

Minimum = 0! Pick row 2 or row 4. Say row 4.
```

**Move Q4 to row 4**: Q = [2, 3, 1, 4]

```
       ┌───┬───┬───┬───┐
Row 1: │   │   │ Q │   │
       ├───┼───┼───┼───┤
Row 2: │ Q │   │   │   │
       ├───┼───┼───┼───┤
Row 3: │   │ Q │   │   │
       ├───┼───┼───┼───┤
Row 4: │   │   │   │ Q │
       └───┴───┴───┴───┘

Check ALL pairs: No conflicts! SOLVED! 🎯
```

**Solution found in just 2 steps!**

---

## 4. Why It Works Amazingly Well

### The Stunning N-Queens Result

| N (board size) | Avg steps to solve |
|---|---|
| 100 | ~40 |
| 1,000 | ~50 |
| **1,000,000** | **~50** |

**It barely gets harder as the problem gets BIGGER!** This is because most random placements are CLOSE to a solution (few conflicts), and min-conflicts quickly fixes them.

> 🍼 **Kid Version**: Imagine a million toy soldiers on a giant board. You plop them all down randomly. Turns out, almost all of them are already in good spots! Only a few dozen need to be moved. So you fix those ~50 soldiers and you're done — whether the board has 100 or 1 million soldiers!

---

## 5. Limitations

| Problem | Why | Solution |
|---|---|---|
| **Plateaus** | No single move reduces conflicts | Allow sideways moves (same # conflicts) |
| **Local minima** | Stuck but not solved | Random restarts |
| **Can't prove unsolvability** | Will loop forever if no solution | Set max_steps limit |

---

## 6. Key Takeaways

1. **Min-Conflicts** = start with random complete assignment → fix conflicts one at a time
2. **Pick a conflicted variable, move it to the value with FEWEST conflicts**
3. **Astonishingly fast** for N-Queens — O(n) steps regardless of N!
4. **Cannot prove** no solution exists — just times out
5. **Best for large CSPs** with many solutions (scheduling, N-Queens)

---

## 7. Exam Tips

### Must-Know

1. **Trace min-conflicts** for 2-3 steps on 4-Queens (as shown above!)
2. **Count conflicts** for each possible value of a variable
3. **Explain why it's fast** for N-Queens

### Common Mistakes

❌ Starting with an EMPTY board (min-conflicts starts FULL!)
❌ Forgetting to check DIAGONAL conflicts (not just row/column)
❌ Not handling ties (when multiple values have same min conflicts, pick randomly)

---

## 📖 References

- AIMA — Chapter 6.4

---

[⬅️ Prev: CSP Backtracking](../06_CSP_Backtracking/README.md) | [Back to Main](../README.md) | [Next: Minimax ➡️](../08_Adversarial_Search_Minimax/README.md)
