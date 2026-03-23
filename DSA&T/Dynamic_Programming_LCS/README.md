# 🔗 Dynamic Programming — Longest Common Subsequence (LCS) — Crystal Clear Guide

> **One-Liner**: LCS finds the longest chain of characters that appears IN ORDER in BOTH strings — like finding the shared "DNA" between two sentences!

---

## 🧒 ELI5 — Explain Like I'm 5

**You and your friend each have a necklace of colored beads:**

```
YOURS:    🔴 🔵 🟢 🔵 🟡
FRIEND'S: 🔵 🟢 🔵 🔴 🟡
```

**Question**: What's the LONGEST chain of beads that appears in BOTH necklaces, **in the same order**? (You can skip beads, but you CAN'T rearrange them.)

Let's check: **🔵 🟢 🔵 🟡** appears in yours (skip the first 🔴) AND in friend's (skip the 🔴). That's length **4**!

Finding this longest shared chain is the **LCS problem!**

### Important: Subsequence ≠ Substring!

| Concept | Must be consecutive? | Example from "ABCDE" |
|---------|---------------------|---------------------|
| **Substring** | ✅ YES — no gaps! | "BCD" ✅, but "ACE" ❌ (has gaps) |
| **Subsequence** | ❌ NO — can skip! | "BCD" ✅ AND "ACE" ✅ (skip B and D) |

LCS looks for the longest common **SUBSEQUENCE** (with gaps allowed, but order preserved).

---

## 📐 How LCS Thinks — The Recurrence

Define **c[i][j]** = length of LCS of the first i characters of X and first j characters of Y.

### The Three Cases (at each cell in the table):

**Case 1: One string is empty** (i=0 or j=0)
→ LCS length = 0. (Nothing in common with an empty string!)

**Case 2: Last characters MATCH** (X[i] == Y[j])
→ This character MUST be part of the LCS! Count it (+1) and solve for the rest.
→ c[i][j] = c[i-1][j-1] + 1

**Case 3: Last characters DON'T match** (X[i] ≠ Y[j])
→ At least one of them can't be in the LCS. Try skipping each one and take the better result.
→ c[i][j] = max(c[i-1][j], c[i][j-1])

```
              ┌  0                            if i=0 or j=0 (empty string)
c[i][j] =    │  c[i-1][j-1] + 1              if X[i] = Y[j] (MATCH! +1)
              └  max(c[i-1][j], c[i][j-1])    if X[i] ≠ Y[j] (skip one)
```

**ELI5 for the three cases:**
1. "One string is empty → nothing in common → 0."
2. "Last letters are THE SAME → great, that's +1! Now check the rest (without those last letters)."
3. "Last letters are DIFFERENT → try removing the last letter from X, try removing from Y, keep whichever gives a longer LCS."

---

## 📜 The Algorithm

```
LCS-LENGTH(X, Y)
1   m = length of X
2   n = length of Y
3   Create table c[0..m][0..n]       // m+1 rows, n+1 columns
4   Fill first row and first column with 0's   // base cases
5   for i = 1 to m:
6       for j = 1 to n:
7           if X[i] == Y[j]:                   // Characters match!
8               c[i][j] = c[i-1][j-1] + 1     // Diagonal + 1
9           else if c[i-1][j] >= c[i][j-1]:    // Skip X's char
10              c[i][j] = c[i-1][j]            // Take value from above
11          else:                               // Skip Y's char
12              c[i][j] = c[i][j-1]            // Take value from left
13  return c[m][n]                              // Answer!
```

**To reconstruct the actual LCS**: trace back from c[m][n] to c[0][0]. At each cell:
- If the characters matched (diagonal) → include this character
- Otherwise → go up or left (whichever was larger)

---

## 🎨 COMPLETE Visual Walkthrough

### X = "ABCB", Y = "BDCAB"

**Step 1: Create the table**

```
         ""  B  D  C  A  B
    ""  [ 0  0  0  0  0  0 ]
     A  [ 0  _  _  _  _  _ ]
     B  [ 0  _  _  _  _  _ ]
     C  [ 0  _  _  _  _  _ ]
     B  [ 0  _  _  _  _  _ ]
```

First row and column are 0 (empty string has LCS 0 with anything).

**Step 2: Fill row by row**

**Row i=1 (A):**
```
c[1][1]: X[1]='A', Y[1]='B'. Match? NO. max(c[0][1], c[1][0]) = max(0,0) = 0
c[1][2]: X[1]='A', Y[2]='D'. Match? NO. max(c[0][2], c[1][1]) = max(0,0) = 0
c[1][3]: X[1]='A', Y[3]='C'. Match? NO. max(0,0) = 0
c[1][4]: X[1]='A', Y[4]='A'. MATCH! ✅ c[0][3] + 1 = 0 + 1 = 1
c[1][5]: X[1]='A', Y[5]='B'. NO match. max(c[0][5], c[1][4]) = max(0,1) = 1
```
```
         ""  B  D  C  A  B
    ""  [ 0  0  0  0  0  0 ]
     A  [ 0  0  0  0  1  1 ]     ← Row 1 filled
```

**Row i=2 (B):**
```
c[2][1]: 'B'='B'. MATCH! ✅ c[1][0]+1 = 0+1 = 1
c[2][2]: 'B'≠'D'. max(c[1][2], c[2][1]) = max(0,1) = 1
c[2][3]: 'B'≠'C'. max(c[1][3], c[2][2]) = max(0,1) = 1
c[2][4]: 'B'≠'A'. max(c[1][4], c[2][3]) = max(1,1) = 1
c[2][5]: 'B'='B'. MATCH! ✅ c[1][4]+1 = 1+1 = 2
```
```
         ""  B  D  C  A  B
     B  [ 0  1  1  1  1  2 ]     ← Row 2
```

**Row i=3 (C):**
```
c[3][1]: 'C'≠'B'. max(1,0) = 1
c[3][2]: 'C'≠'D'. max(1,1) = 1
c[3][3]: 'C'='C'. MATCH! ✅ c[2][2]+1 = 1+1 = 2
c[3][4]: 'C'≠'A'. max(c[2][4], c[3][3]) = max(1,2) = 2
c[3][5]: 'C'≠'B'. max(c[2][5], c[3][4]) = max(2,2) = 2
```
```
         ""  B  D  C  A  B
     C  [ 0  1  1  2  2  2 ]     ← Row 3
```

**Row i=4 (B):**
```
c[4][1]: 'B'='B'. MATCH! ✅ c[3][0]+1 = 0+1 = 1
c[4][2]: 'B'≠'D'. max(1,1) = 1
c[4][3]: 'B'≠'C'. max(c[3][3], c[4][2]) = max(2,1) = 2
c[4][4]: 'B'≠'A'. max(c[3][4], c[4][3]) = max(2,2) = 2
c[4][5]: 'B'='B'. MATCH! ✅ c[3][4]+1 = 2+1 = 3
```

**Complete table:**
```
         ""  B  D  C  A  B
    ""  [ 0  0  0  0  0  0 ]
     A  [ 0  0  0  0  1  1 ]
     B  [ 0  1  1  1  1  2 ]
     C  [ 0  1  1  2  2  2 ]
     B  [ 0  1  1  2  2  3 ]
```

**LCS length = c[4][5] = 3** ✅

**Step 3: Reconstruct the LCS (trace back from bottom-right):**
```
At c[4][5]=3: X[4]='B', Y[5]='B'. MATCH → include 'B'. Go to c[3][4].
At c[3][4]=2: X[3]='C', Y[4]='A'. NO match. c[2][4]=1, c[3][3]=2. Go LEFT to c[3][3].
At c[3][3]=2: X[3]='C', Y[3]='C'. MATCH → include 'C'. Go to c[2][2].
At c[2][2]=1: X[2]='B', Y[2]='D'. NO match. c[1][2]=0, c[2][1]=1. Go LEFT to c[2][1].
At c[2][1]=1: X[2]='B', Y[1]='B'. MATCH → include 'B'. Go to c[1][0].
At c[1][0]=0. DONE.

Reading matches in order: B, C, B → LCS = "BCB" (length 3) ✅
```

---

## ⏱️ Complexity

| | Value | Why |
|-|-------|-----|
| **Time** | O(m × n) | Two nested loops |
| **Space** | O(m × n) | The 2D table |
| **Reconstruction** | O(m + n) | Trace from corner to origin |

---

## 🐍 Python Implementation — Commented

```python
def lcs(X, Y):
    """Find Longest Common Subsequence using DP."""
    m, n = len(X), len(Y)
    
    # Create table (m+1 rows × n+1 columns), initialized to 0
    c = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i-1] == Y[j-1]:            # Characters match!
                c[i][j] = c[i-1][j-1] + 1   # Diagonal + 1
            else:                             # Don't match
                c[i][j] = max(c[i-1][j], c[i][j-1])  # Best of up/left
    
    # Reconstruct the LCS string
    lcs_chars = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:       # This character is in the LCS
            lcs_chars.append(X[i-1])
            i -= 1; j -= 1          # Go diagonal
        elif c[i-1][j] >= c[i][j-1]:
            i -= 1                   # Go up
        else:
            j -= 1                   # Go left
    
    lcs_chars.reverse()  # We built it backwards
    return c[m][n], ''.join(lcs_chars)

# Examples:
print(lcs("ABCBDAB", "BDCABA"))   # (4, 'BCBA')
print(lcs("ABCB", "BDCAB"))       # (3, 'BCB')
print(lcs("ABC", "DEF"))           # (0, '')  — nothing in common!
print(lcs("AAAA", "AAAA"))        # (4, 'AAAA') — identical!
```

---

## 📝 Practice Questions with Detailed Solutions

### Q1: Find LCS of "AGGTAB" and "GXTXAYB". Show full table.

**Solution:**
```
         ""  G  X  T  X  A  Y  B
    ""  [ 0  0  0  0  0  0  0  0]
     A  [ 0  0  0  0  0  1  1  1]
     G  [ 0  1  1  1  1  1  1  1]
     G  [ 0  1  1  1  1  1  1  1]
     T  [ 0  1  1  2  2  2  2  2]
     A  [ 0  1  1  2  2  3  3  3]
     B  [ 0  1  1  2  2  3  3  4]

LCS length = 4. Trace back: B(match), A(match), T(match), G(match).
LCS = "GTAB" ✅
```

### Q2: LCS of "ABC" and "ACB" — how many LCS exist?

**Solution:** LCS length = 2. Two possible LCS: "AB" and "AC". Both have length 2. Multiple LCS can exist — the algorithm finds one, but others may be valid.

### Q3: How to find longest common SUBSTRING (consecutive)?

**Solution:** Modify: when X[i] ≠ Y[j], set c[i][j] = **0** instead of max(above, left). Track the maximum value seen. The substring must be consecutive, so any mismatch resets the count.

### Q4: LCS of "ABCD" and "DCBA"?

**Solution:** LCS length = 1. Any single shared character works. The strings are reverses of each other, and the longest shared in-order chain is just 1 character.

### Q5: Edit distance from X to Y = m + n - 2×LCS(X,Y). Verify for "ABC" and "AEC".

**Solution:** LCS("ABC", "AEC") = "AC" (length 2). Edit distance = 3 + 3 - 2×2 = 2. Indeed: ABC → AEC requires replacing B with E = 1 operation... Hmm, actually Levenshtein allows insert/delete/replace. With only insert/delete: delete B, insert E = 2 operations ✅.

### Q6: Can we use O(n) space instead of O(mn)?

**Solution:** Yes! Keep only **2 rows** of the table (current and previous). Since c[i][j] depends only on c[i-1][j-1], c[i-1][j], and c[i][j-1], we only need the previous row. BUT: we lose the ability to reconstruct the actual LCS string (only get the length).

### Q7: What is LCS("", "anything")?

**Solution:** 0. Any string compared with an empty string has nothing in common.

### Q8: Application: how does `diff` (git diff) use LCS?

**Solution:** `diff` treats each LINE of a file as a "character." The LCS of two files' lines = the **unchanged lines**. Lines NOT in the LCS = additions (new file only) or deletions (old file only). The LCS is the "common backbone."

---

## 📋 Quick Revision Cheat Sheet

```
┌──────────────────────────────────────────────────────┐
│  LCS — EVERYTHING IN ONE BOX                         │
├──────────────────────────────────────────────────────┤
│                                                      │
│  SUBSEQUENCE ≠ SUBSTRING (can skip, maintain order)  │
│                                                      │
│  RECURRENCE:                                         │
│  Match → c[i][j] = c[i-1][j-1] + 1  (diagonal + 1)   │
│  No match → c[i][j] = max(above, left)               │
│  Base: c[0][j] = c[i][0] = 0                         │
│                                                      │
│  TIME: O(m × n)    SPACE: O(m × n)                   │
│                                                      │
│  RECONSTRUCT: trace from c[m][n] to c[0][0]          │
│  Match → include char, go diagonal                   │
│  No match → go up or left (whichever is larger)      │
│                                                      │
│  APPS: diff, DNA analysis, plagiarism, edit distance │
│                                                      │
└──────────────────────────────────────────────────────┘
```

## 📚 References
- [CLRS Chapter 15.4](https://walkccc.me/CLRS/Chap15/15.4/)
- Lec's 18 — Pr V Raj S
