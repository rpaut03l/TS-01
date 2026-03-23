# 📅 Greedy — Interview Scheduling (Activity Selection) — Crystal Clear Guide

> **One-Liner**: Pick the MAXIMUM number of non-overlapping activities by always choosing the one that finishes EARLIEST — leave the most room for future activities!

---

## 🧒 ELI5 — Explain Like I'm 5

**You have ONE TV and many shows to watch today!** 📺

Each show has a start time and end time. You can only watch ONE show at a time (no channel switching mid-show!).

```
Show A: 8:00 — 9:30     (1.5 hours)
Show B: 8:30 — 10:00    (1.5 hours)
Show C: 9:30 — 11:00    (1.5 hours)
Show D: 10:00 — 11:30   (1.5 hours)
Show E: 11:00 — 12:00   (1 hour)
```

**Question**: What's the MAXIMUM number of shows you can watch?

**The trick**: Always pick the show that **ENDS the soonest!**

Why? Because if a show ends early, you have MORE TIME LEFT for other shows!

```
1. Show A ends at 9:30 — that's the earliest ending. PICK IT! ✅
2. Next available show that starts at or after 9:30: Show C (starts 9:30). PICK IT! ✅
3. Next after 11:00: Show E (starts 11:00). PICK IT! ✅

Result: A, C, E = 3 shows! 🎉
```

What if we'd picked Show B first (ends at 10:00)?
```
B, then D (starts 10:00), then... nothing starts after 11:30.
Result: B, D = only 2 shows! 😢
```

**Picking the earliest-ending show first ALWAYS gives the best result!** This is the **greedy choice**.

---

## 📝 What Is a Greedy Algorithm?

A **greedy algorithm** makes the **locally best choice** at each step, hoping it leads to the **globally best solution**.

```
THE GREEDY RECIPE:
1. Define what "locally best" means (for us: "pick the earliest-finishing activity")
2. Make that choice
3. Eliminate all options that conflict with your choice
4. Repeat with the remaining options
5. NEVER go back and change a previous choice!
```

### When Does Greedy Work?

Greedy DOESN'T always work! It only works when you can PROVE two things:

1. **Greedy Choice Property**: Making the locally best choice always leads to a globally optimal solution.
2. **Optimal Substructure**: After making one choice, the remaining problem has the same structure.

For Activity Selection, BOTH properties hold (proven below!).

### When Does Greedy FAIL?

For problems like:
- **0/1 Knapsack**: Picking the best value/weight ratio item first doesn't always work.
- **Weighted Activity Selection**: If activities have different VALUES, just picking the earliest-ending one doesn't maximize total value — you need DP!

---

## 📋 The Activity Selection Problem — Formal

**Given**: n activities, each with start time s[i] and finish time f[i].
**Two activities are compatible** if they don't overlap: f[i] ≤ s[j] (one ends before the other starts).
**Goal**: Find the MAXIMUM-SIZE set of mutually compatible activities.

### Example Data

| Activity | Start | Finish |
|----------|-------|--------|
| a₁ | 1 | 4 |
| a₂ | 3 | 5 |
| a₃ | 0 | 6 |
| a₄ | 5 | 7 |
| a₅ | 3 | 9 |
| a₆ | 5 | 9 |
| a₇ | 6 | 10 |
| a₈ | 8 | 11 |
| a₉ | 8 | 12 |
| a₁₀ | 2 | 14 |
| a₁₁ | 12 | 16 |

---

## 📜 The Algorithm — Crystal Clear

```
GREEDY-ACTIVITY-SELECTOR(activities)
1   Sort activities by FINISH TIME (ascending)
2   Select the first activity (earliest finish)
3   last_finish = finish time of selected activity
4   for each remaining activity (in sorted order):
5       if this activity's start time ≥ last_finish:
6           Select this activity!
7           last_finish = this activity's finish time
8   return all selected activities
```

### In Plain English:

1. **Sort** all activities by when they END (earliest first).
2. **Pick** the first one (it ends earliest — leaves most room!).
3. **Skip** any activity that overlaps with the last one you picked.
4. **Pick** the next non-overlapping activity.
5. Repeat until you've considered all activities.

### Time Complexity

- Sorting: O(n log n)
- Scanning: O(n) (one pass through sorted activities)
- **Total: O(n log n)**

If activities are already sorted: just **O(n)**!

---

## 🎨 COMPLETE Visual Walkthrough

### Step 1: Sort by finish time

Activities already sorted by finish time:
```
a₁(1,4)  a₂(3,5)  a₃(0,6)  a₄(5,7)  a₅(3,9)  a₆(5,9)  a₇(6,10)  a₈(8,11)  a₉(8,12)  a₁₀(2,14)  a₁₁(12,16)
```

### Step 2: Greedy selection (step by step)

```
SELECT a₁(1,4). last_finish = 4.
  Timeline: [====]
            1   4

CHECK a₂(3,5): start=3 < last_finish=4? YES → OVERLAPS. SKIP! ❌
CHECK a₃(0,6): start=0 < 4? YES → OVERLAPS. SKIP! ❌
CHECK a₄(5,7): start=5 ≥ 4? YES → COMPATIBLE! SELECT! ✅ last_finish = 7.
  Timeline: [====]  [====]
            1   4  5    7

CHECK a₅(3,9): start=3 < 7? YES → SKIP! ❌
CHECK a₆(5,9): start=5 < 7? YES → SKIP! ❌
CHECK a₇(6,10): start=6 < 7? YES → SKIP! ❌
CHECK a₈(8,11): start=8 ≥ 7? YES → COMPATIBLE! SELECT! ✅ last_finish = 11.
  Timeline: [====]  [====]  [======]
            1   4  5    7  8     11

CHECK a₉(8,12): start=8 < 11? YES → SKIP! ❌
CHECK a₁₀(2,14): start=2 < 11? YES → SKIP! ❌
CHECK a₁₁(12,16): start=12 ≥ 11? YES → COMPATIBLE! SELECT! ✅ last_finish = 16.
  Timeline: [====]  [====]  [======]   [========]
            1   4  5    7  8     11  12       16

ALL ACTIVITIES CHECKED. DONE!
```

### Result: {a₁, a₄, a₈, a₁₁} = **4 activities** ✅

---

## ✅ Why This Works — Correctness Proof (Explained Simply)

### Greedy Choice Property

**Claim**: There EXISTS an optimal solution that includes the activity with the earliest finish time.

**Proof** (by exchange argument):

Let A* be ANY optimal solution (maximum number of activities).
Let a₁ be the activity with the earliest finish time overall.

**Case 1**: a₁ is already in A*. Done! ✅

**Case 2**: a₁ is NOT in A*. Let a_k be the activity in A* that finishes earliest.

Since a₁ has the earliest finish among ALL activities: f₁ ≤ f_k.

Now create A' = (A* minus a_k) plus a₁. Is A' still valid?
- a₁ finishes no later than a_k (f₁ ≤ f_k)
- So a₁ doesn't conflict with anything a_k was compatible with
- Therefore A' is a valid set of compatible activities
- |A'| = |A*| (same number of activities)
- So A' is ALSO optimal, and it includes a₁! ✅

**In plain English**: "If someone else's optimal solution doesn't include the earliest-ending activity, we can swap in the earliest-ending activity without breaking anything. So it's always safe to pick it!"

### Optimal Substructure

After picking a₁, the remaining problem is: find the max compatible activities from those that START at or after f₁. This is a SMALLER version of the SAME problem! Same structure, same greedy strategy works.

---

## ⚠️ Why Not Other Greedy Strategies?

| Strategy | Works? | Why Not? |
|----------|--------|----------|
| Earliest START time | ❌ | Activity (0, 100) starts first but blocks everything! |
| Shortest DURATION | ❌ | Short activity (4,6) can block both (1,5) and (5,9) |
| Fewest conflicts | ❌ | Complex counterexamples exist |
| **Earliest FINISH time** | ✅ | **Provably optimal** (proven above!) |

---

## ⚖️ Greedy vs DP for This Problem

| | Greedy | Dynamic Programming |
|-|--------|-------------------|
| **Time** | O(n log n) | O(n²) |
| **For unweighted?** | ✅ Perfect! | ✅ Works but overkill |
| **For WEIGHTED?** | ❌ FAILS! | ✅ Required! |

**Important**: If each activity has a WEIGHT (profit), and you want to maximize TOTAL WEIGHT (not count), greedy by earliest finish DOESN'T work! You need DP.

**Example where greedy fails for weighted version:**
```
Activity 1: (1, 4, profit=$1)
Activity 2: (3, 5, profit=$100)  ← huge profit!
Activity 3: (5, 7, profit=$1)

Greedy by finish: picks 1 and 3 → profit $2.
Optimal: pick just 2 → profit $100! Greedy missed it!
```

---

## 🐍 Python Implementation — Every Line Commented

```python
def activity_selection(activities):
    """
    Select the maximum number of non-overlapping activities.
    
    activities: list of (start, finish, name) tuples
    Returns: list of selected activities
    """
    # STEP 1: Sort by finish time (earliest finish first)
    sorted_acts = sorted(activities, key=lambda x: x[1])
    
    # STEP 2: Always pick the first (earliest-finishing)
    selected = [sorted_acts[0]]
    last_finish = sorted_acts[0][1]
    
    # STEP 3: Scan through remaining activities
    for i in range(1, len(sorted_acts)):
        start, finish, name = sorted_acts[i]
        
        # Is this activity compatible? (starts after last one finishes)
        if start >= last_finish:
            selected.append(sorted_acts[i])  # Pick it!
            last_finish = finish              # Update last finish time
    
    return selected


# ===== EXAMPLE =====
activities = [
    (1,4,"a1"), (3,5,"a2"), (0,6,"a3"), (5,7,"a4"),
    (3,9,"a5"), (5,9,"a6"), (6,10,"a7"), (8,11,"a8"),
    (8,12,"a9"), (2,14,"a10"), (12,16,"a11"),
]

result = activity_selection(activities)
print(f"Maximum activities: {len(result)}")
for s, f, name in result:
    print(f"  {name}: [{s}, {f})")

# Output:
# Maximum activities: 4
# a1: [1, 4)
# a4: [5, 7)
# a8: [8, 11)
# a11: [12, 16)

# Visualization
print("\nTimeline visualization:")
for s, f, name in result:
    spaces = " " * s
    bar = "█" * (f - s)
    print(f"  {name:4s} {spaces}{bar} [{s},{f})")
```

---

## 📝 Practice Questions with Detailed Solutions

### Q1: Activities: (1,3),(2,5),(4,7),(1,8),(5,9),(8,10). Find max set.

**Solution:**
```
Sort by finish: (1,3),(2,5),(4,7),(1,8),(5,9),(8,10)

Pick (1,3). last=3.
(2,5): 2 < 3 → SKIP (overlaps!)
(4,7): 4 ≥ 3 → PICK ✅. last=7.
(1,8): 1 < 7 → SKIP.
(5,9): 5 < 7 → SKIP.
(8,10): 8 ≥ 7 → PICK ✅. last=10.

Selected: {(1,3), (4,7), (8,10)} → 3 activities ✅
```

### Q2: Prove greedy is optimal for: (1,4),(3,5),(5,7).

**Solution:**
```
Greedy: pick (1,4), then (5,7). Size = 2.
All possible valid sets:
  {(1,4),(5,7)} → size 2 ✅
  {(3,5),(5,7)} → size 2 ✅ (start=5 ≥ finish=5, just barely compatible!)
  {(1,4)} → size 1
  {(3,5)} → size 1
  {(5,7)} → size 1
  {} → size 0

Maximum possible = 2. Greedy achieves 2. OPTIMAL! ✅
```

### Q3: Meeting rooms problem: (0,30),(5,10),(15,20). Min rooms needed?

**Solution:** This is a DIFFERENT problem (interval partitioning, not selection). Find the maximum number of overlapping activities at any point in time.

```
At time 5: (0,30) and (5,10) overlap → 2 meetings at once
At time 15: (0,30) and (15,20) overlap → 2 meetings at once
Max simultaneous = 2 → Minimum rooms = 2
```

### Q4: Does greedy maximize PROFIT for weighted activities?

**Solution:** NO! Example: (1,4,$1), (3,5,$100), (5,7,$1).
Greedy by finish: (1,4,$1) + (5,7,$1) = **$2**.
Optimal: just (3,5,$100) = **$100**!
Greedy fails because it doesn't consider the VALUE of each activity. Need DP for weighted version!

### Q5: What if we use `>` instead of `≥` for compatibility check?

**Solution:** With `start > last_finish`: activities that start EXACTLY when the last one finishes would be rejected. Example: (1,5) and (5,9). With ≥: compatible ✅ (finish 5, start 5). With >: NOT compatible ❌ (5 > 5 is false). Usually activities ending and starting at the same time ARE compatible, so **use ≥**.

### Q6: What if activities are already sorted by finish time?

**Solution:** Skip the sorting step! The scan is O(n). Total: **O(n)** — as fast as reading the input!

### Q7: Can Activity Selection be solved with DP?

**Solution:** Yes! Define dp[i] = max activities from {a₁..aᵢ}. For each aᵢ, either include it (find latest compatible, add 1) or exclude it (dp[i-1]). Time: O(n²) naive, O(n log n) with binary search. But greedy is simpler and just as fast at O(n log n)!

### Q8: 20 activities, greedy selects 5. Can ANY algorithm find 6?

**Solution:** **NO!** Greedy is provably optimal for unweighted activity selection. The greedy choice property and exchange argument guarantee that no solution with more activities exists. If greedy finds 5, the maximum is 5 — period!

### Q9: Interval coloring: (1,5),(2,6),(4,7),(6,8). Minimum colors?

**Solution:** Color so overlapping intervals get different colors = minimum colors needed = maximum overlap at any time.
```
At time 4: (1,5), (2,6), (4,7) all active → 3 overlapping
(6,8) doesn't overlap with (1,5), so max overlap is 3.
Minimum colors = 3 ✅
```

### Q10: Recursive version of activity selection?

**Solution:**
```python
def recursive_activity_sel(s, f, k, n):
    """Find first compatible activity after k, then recurse."""
    m = k + 1
    while m < n and s[m] < f[k]:   # Skip incompatible
        m += 1
    if m < n:
        return [(s[m], f[m])] + recursive_activity_sel(s, f, m, n)
    return []
```
Same result as iterative, but uses recursion. Base case: no more compatible activities left.

---

## 📋 Quick Revision Cheat Sheet

```
┌──────────────────────────────────────────────────────┐
│  GREEDY ACTIVITY SELECTION — EVERYTHING IN ONE BOX   │
├──────────────────────────────────────────────────────┤
│                                                      │
│  STRATEGY: Sort by FINISH time. Pick earliest finish.│
│  Skip overlapping. Repeat.                           │
│                                                      │
│  TIME: O(n log n) sorting + O(n) scan = O(n log n)   │
│                                                      │
│  WHY IT WORKS:                                       │
│  Greedy choice property (exchange argument proof)    │
│  + Optimal substructure (same problem after choosing)│
│                                                      │
│  REMEMBER:                                           │
│  ✅ Sort by FINISH time (NOT start time!)            │
│  ✅ Use ≥ for compatibility (start ≥ last_finish)    │
│  ❌ Does NOT work for weighted version (use DP!)     │
│  ❌ Don't sort by start time, duration, or conflicts │
│                                                      │
│  Greedy is PROVABLY OPTIMAL for this problem!        │
│                                                      │
└──────────────────────────────────────────────────────┘
```

## 📚 References
- CLRS Chapter 16 (Section 16.1: Activity Selection - https://walkccc.me/CLRS/Chap16/16.1/)
- [Lec's 18 — Pr V Raj S](CLRS - https://github.com/gzc/CLRS/blob/master/C16-Greedy-Algorithms/16.1.md)
