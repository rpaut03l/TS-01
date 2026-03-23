# 🪵 Dynamic Programming — Rod Cutting — Crystal Clear Complete Guide

> **One-Liner**: Cut a rod into pieces to make the MOST money — Dynamic Programming remembers solutions to smaller problems so it never solves the same thing twice!

---

## 🧒 ELI5 — Explain Like I'm 5

**Imagine you have a chocolate bar that's 4 squares long.** 🍫

The candy shop will buy pieces at different prices:
```
1 square  = $1
2 squares = $5
3 squares = $8
4 squares = $9
```

**How should you break it to get the MOST money?**

Let's try ALL options:
- Sell whole (4): **$9**
- Cut 1+3: $1 + $8 = **$9**
- Cut 2+2: $5 + $5 = **$10** ← BEST!
- Cut 1+1+2: $1 + $1 + $5 = **$7**
- Cut 1+1+1+1: $1×4 = **$4**

**Answer: $10** (cut into two pieces of size 2).

But what if the bar is 100 squares long with 100 different prices? You can't try ALL combinations by hand — there are 2^99 of them! That's more than the number of atoms in the universe!

**Dynamic Programming** solves this by being SMART: Instead of trying every combination, it builds up from small problems:
- First figure out the best way to cut a bar of length 1 (trivial!)
- Then length 2 (try: sell as 2, or two 1's)
- Then length 3 (use your answers for 1 and 2 to help!)
- ...keep going until you reach length 100.

Each step only takes a moment because you REUSE previous answers!

---

## 📝 What Is Dynamic Programming? (The Concept)

**Dynamic Programming (DP)** is a technique for solving problems by:
1. Breaking them into **smaller overlapping subproblems**
2. Solving each subproblem **ONCE** and **storing the result**
3. Using stored results to build solutions to **bigger problems**

### Two Key Properties That Tell You "Use DP!"

| Property | What It Means | ELI5 |
|----------|--------------|------|
| **Optimal Substructure** | The best solution contains best solutions to sub-problems | "The best way to cut a 10-bar uses the best ways to cut smaller bars" |
| **Overlapping Subproblems** | The same sub-problems appear again and again | "When computing r[5], I need r[3]. When computing r[6], I also need r[3]. Don't solve r[3] twice!" |

### Two Approaches to DP

| Approach | How It Works | Direction | Analogy |
|----------|-------------|-----------|---------|
| **Top-Down (Memoization)** | Start with big problem, recursively solve smaller ones, CACHE results | Big → Small | "Ask the question, if I've answered it before → use cached answer" |
| **Bottom-Up (Tabulation)** | Start with smallest problems, build table of solutions up to the big one | Small → Big | "Fill in a table row by row, from easy to hard" |

---

## 📐 The Rod Cutting Problem — Formal Statement

**Given:**
- A rod of length **n** (integer)
- A price table **p[1..n]** where p[i] = price for a piece of length i

**Find:** The maximum total revenue **r[n]** from cutting the rod into pieces and selling them. (You can also choose NOT to cut at all — selling the whole rod for p[n].)

### Example Price Table

| Length i | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---------|---|---|---|---|---|---|---|---|---|---|
| Price p[i] | 1 | 5 | 8 | 9 | 10 | 17 | 17 | 20 | 24 | 30 |

---

## 📐 The Recurrence — How to Think About It

The KEY insight: to find the best cut for a rod of length n, **try every possible FIRST cut** and pick the best.

If you make the first cut at position i (taking a piece of length i), you get:
- p[i] dollars for that piece
- PLUS the best revenue for the REMAINING rod of length (n - i)

Since we don't know which first cut is best, we TRY ALL of them:

```
r[n] = max over all i from 1 to n of { p[i] + r[n - i] }

Base case: r[0] = 0  (a rod of length 0 earns nothing)
```

**In plain English**: "Try cutting a piece of length 1 (earn p[1] + best for remaining n-1), or length 2 (earn p[2] + best for remaining n-2), ... or length n (earn p[n], nothing remaining). Take whichever gives the most money."

---

## 🐌 Naive Recursion — Why It's TERRIBLE

```
CUT-ROD(p, n)
1   if n == 0: return 0
2   q = -∞
3   for i = 1 to n:
4       q = max(q, p[i] + CUT-ROD(p, n - i))
5   return q
```

**Time: O(2ⁿ)** — EXPONENTIAL! Why?

Because the same subproblems are solved over and over:

```
CUT-ROD(4) calls CUT-ROD(3), CUT-ROD(2), CUT-ROD(1), CUT-ROD(0)
CUT-ROD(3) calls CUT-ROD(2), CUT-ROD(1), CUT-ROD(0)
CUT-ROD(2) calls CUT-ROD(1), CUT-ROD(0)

CUT-ROD(0) is called 8 times!
CUT-ROD(1) is called 4 times!
```

Total calls = 2ⁿ. For n=30, that's over 1 BILLION calls. Way too slow!

---

## 💾 DP Solution — Bottom-Up (THE Way to Do It)

Instead of recomputing, **store every answer in a table** and look it up when needed:

```
BOTTOM-UP-CUT-ROD(p, n)
1   let r[0..n] be a new array          // Our answer table
2   r[0] = 0                            // Base case: empty rod = $0
3   for j = 1 to n:                     // Solve for length 1, then 2, ... then n
4       q = -∞
5       for i = 1 to j:                 // Try all possible first cuts
6           q = max(q, p[i] + r[j - i]) // Use STORED answer for remaining part!
7       r[j] = q                        // Store the answer for length j
8   return r[n]                          // Answer for the full rod
```

**Time: O(n²)**. **Space: O(n)**. MASSIVELY better than O(2ⁿ)!

### Why O(n²)?

Two nested loops: outer loop runs n times, inner loop runs up to j times (averaging n/2). Total = n × n/2 = n²/2 = O(n²).

---

## ✂️ Extended Version — Track WHERE to Cut

```
EXTENDED-BOTTOM-UP-CUT-ROD(p, n)
1   r[0] = 0
2   for j = 1 to n:
3       q = -∞
4       for i = 1 to j:
5           if q < p[i] + r[j - i]:
6               q = p[i] + r[j - i]
7               s[j] = i                  // Record: "for length j, best first cut = i"
8       r[j] = q
9   return r, s

To print the actual cuts:
  while n > 0:
      print "Cut a piece of length", s[n]
      n = n - s[n]
```

---

## 🎨 COMPLETE Visual Walkthrough

### Price: p = [0, 1, 5, 8, 9] (p[0] unused)

```
═══ Computing r[0] ═══
r[0] = 0  (base case)

═══ Computing r[1] ═══
  Try i=1: p[1] + r[1-1] = 1 + r[0] = 1 + 0 = 1
  r[1] = 1. s[1] = 1. (Best: sell as one piece of length 1)

═══ Computing r[2] ═══
  Try i=1: p[1] + r[2-1] = 1 + r[1] = 1 + 1 = 2  ← cut into 1+1
  Try i=2: p[2] + r[2-2] = 5 + r[0] = 5 + 0 = 5  ← sell as one piece of 2
  r[2] = 5. s[2] = 2. (Best: sell as one piece of length 2 for $5)

═══ Computing r[3] ═══
  Try i=1: p[1] + r[2] = 1 + 5 = 6    ← cut 1 + (best for 2) = 1 + 5
  Try i=2: p[2] + r[1] = 5 + 1 = 6    ← cut 2 + (best for 1) = 5 + 1
  Try i=3: p[3] + r[0] = 8 + 0 = 8    ← sell as one piece of 3
  r[3] = 8. s[3] = 3. (Best: sell whole as length 3 for $8)

═══ Computing r[4] ═══
  Try i=1: p[1] + r[3] = 1 + 8 = 9    ← cut 1 + (best for 3) = 1 + 8
  Try i=2: p[2] + r[2] = 5 + 5 = 10   ← cut 2 + (best for 2) = 5 + 5  ✅ BEST!
  Try i=3: p[3] + r[1] = 8 + 1 = 9    ← cut 3 + (best for 1) = 8 + 1
  Try i=4: p[4] + r[0] = 9 + 0 = 9    ← sell whole for $9
  r[4] = 10. s[4] = 2. (Best: cut into 2+2 for $5+$5=$10)

═══ RECONSTRUCTING THE CUTS ═══
n=4: s[4]=2 → cut a piece of length 2. Remaining: 4-2 = 2.
n=2: s[2]=2 → cut a piece of length 2. Remaining: 2-2 = 0.
n=0: done!

Cuts: [2, 2]. Revenue: $5 + $5 = $10 ✅
```

---

## 🐍 Python Implementation — Every Line Commented

```python
def cut_rod(prices, n):
    """
    Find max revenue from cutting a rod of length n.
    
    prices: list where prices[i] = price for piece of length i (prices[0] unused)
    n: length of rod
    
    Returns: (max_revenue, list_of_cuts)
    """
    # r[j] = max revenue for rod of length j
    r = [0] * (n + 1)
    # s[j] = optimal first cut for rod of length j
    s = [0] * (n + 1)
    
    # Build table from small to large
    for j in range(1, n + 1):
        best = float('-inf')
        for i in range(1, j + 1):
            # Try first cut of length i
            revenue = prices[i] + r[j - i]
            if revenue > best:
                best = revenue
                s[j] = i  # Remember best first cut
        r[j] = best
    
    # Reconstruct the actual cuts
    cuts = []
    remaining = n
    while remaining > 0:
        cuts.append(s[remaining])
        remaining -= s[remaining]
    
    return r[n], cuts

# Example:
prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

for n in range(1, 11):
    revenue, cuts = cut_rod(prices, n)
    print(f"Rod length {n:2d}: max revenue = ${revenue:3d}, cuts = {cuts}")

# Output:
# Rod length  1: max revenue = $  1, cuts = [1]
# Rod length  2: max revenue = $  5, cuts = [2]
# Rod length  3: max revenue = $  8, cuts = [3]
# Rod length  4: max revenue = $ 10, cuts = [2, 2]
# Rod length  5: max revenue = $ 13, cuts = [2, 3]
# Rod length  6: max revenue = $ 17, cuts = [6]
# Rod length  7: max revenue = $ 18, cuts = [1, 6]
# Rod length  8: max revenue = $ 22, cuts = [2, 6]
# Rod length  9: max revenue = $ 25, cuts = [3, 6]
# Rod length 10: max revenue = $ 30, cuts = [10]
```

---

## 📝 Practice Questions with Detailed Solutions

### Q1: Compute r[1] through r[5] for p = [0, 2, 5, 7, 8, 10].

**Solution:**
```
r[0] = 0
r[1]: i=1: 2+0=2.  r[1]=2, s[1]=1
r[2]: i=1: 2+2=4. i=2: 5+0=5.  r[2]=5, s[2]=2
r[3]: i=1: 2+5=7. i=2: 5+2=7. i=3: 7+0=7.  r[3]=7 (all tie at 7!)
r[4]: i=1: 2+7=9. i=2: 5+5=10. i=3: 7+2=9. i=4: 8+0=8.  r[4]=10, s[4]=2
r[5]: i=1: 2+10=12. i=2: 5+7=12. i=3: 7+5=12. i=4: 8+2=10. i=5: 10+0=10.
      r[5]=12 (three-way tie!)
```

### Q2: Reconstruct cuts for n=5 from Q1.

**Solution:** s[5]=1 (or 2 or 3 — any tie-breaker). Say s[5]=1: cut 1, remaining=4. s[4]=2: cut 2, remaining=2. s[2]=2: cut 2, remaining=0. **Cuts: [1,2,2]. Revenue: 2+5+5=12** ✅

### Q3: Can greedy (best price-per-length) solve rod cutting?

**Solution:** **NO!** Example: p=[0,1,5,8,9]. Price/length ratios: 1/1=1, 5/2=2.5, 8/3=2.67, 9/4=2.25. Greedy picks length 3 first (ratio 2.67): 8 + r[1] = 8+1=9. But optimal is 5+5=10 (two pieces of 2). **Greedy fails!** Must use DP.

### Q4: What's the time complexity of naive recursion for n=20?

**Solution:** O(2^n) = 2^20 = **1,048,576 calls**. DP: n²/2 = 200 operations. DP is **~5000× faster!**

### Q5: If p[i] = i for all i, what's the optimal strategy?

**Solution:** If the price is exactly the length, then every way of cutting gives the same revenue (pieces always sum to n). r[n] = n. No incentive to cut!

### Q6: Rod of length 6, p=[0,1,5,8,9,10,17]. Max revenue?

**Solution:**
```
r[6]: i=1:1+13=14, i=2:5+10=15, i=3:8+8=16, i=4:9+5=14, i=5:10+1=11, i=6:17+0=17
r[6] = 17 (don't cut at all!) ✅
```

### Q7: How many ways to cut a rod of length 4?

**Solution:** Each of the 3 internal positions (between squares) can be cut or not: 2³ = **8 ways**. They are: 4, 3+1, 1+3, 2+2, 2+1+1, 1+2+1, 1+1+2, 1+1+1+1.

### Q8: Top-down (memoization) vs bottom-up — which is better?

**Solution:** Both are O(n²). Bottom-up has no recursion overhead (no function call stack), so it's slightly faster in practice. Top-down only solves subproblems actually needed (which is ALL of them for rod cutting, so no advantage here). **Bottom-up is preferred for rod cutting.**

---

## 📋 Quick Revision Cheat Sheet

```
┌──────────────────────────────────────────────────────┐
│  ROD CUTTING — EVERYTHING IN ONE BOX                 │
├──────────────────────────────────────────────────────┤
│                                                      │
│  RECURRENCE:                                         │
│  r[n] = max(p[i] + r[n-i]) for i = 1 to n            │
│  r[0] = 0                                            │
│                                                      │
│  NAIVE: O(2^n) — TOO SLOW!                           │
│  DP: O(n²) — FAST!                                   │
│                                                      │
│  BOTTOM-UP: fill table r[0], r[1], ..., r[n]         │
│  Track s[j] for reconstruction                       │
│                                                      │
│  TWO DP PROPERTIES:                                  │
│  1. Optimal substructure ✅                          │
│  2. Overlapping subproblems ✅                       │
│                                                      │
│  Greedy does NOT work here!                          │
│                                                      │
└──────────────────────────────────────────────────────┘
```

## 📚 References
- [CLRS Chapter 15.1](https://walkccc.me/CLRS/Chap15/15.1/)
- Lec's 18 — Pr V Raj S
