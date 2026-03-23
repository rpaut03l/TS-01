# 🤝 Disjoint-Set Union (Union-Find) — Crystal Clear Complete Guide

> **One-Liner**: DSU manages groups — "Are Alice and Bob in the same group?" and "Merge their groups" — both nearly instant!

---

## 🧒 ELI5 — Explain Like I'm 5

**Story time!** It's the first day of school. Every kid is alone — no friends yet.

Then things start happening:
- "Alice and Bob are now friends!" → They form a group. Alice is the group leader.
- "Charlie and Dana are friends!" → They form another group. Charlie is the leader.
- "Alice and Charlie are friends!" → Their groups MERGE into one big group.
- Someone asks: "Are Bob and Dana in the same friend group?" → YES! (Because Alice's group and Charlie's group merged.)

**That's Disjoint-Set Union!** You manage groups (sets) of things. You can:
1. **MAKE-SET**: Create a group for one person (everyone starts alone)
2. **FIND**: "Who is the leader of this person's group?" 
3. **UNION**: "Merge these two groups into one"

**But how to make it FAST?** Two magical tricks:

**Trick 1 — Union by Rank**: When merging two groups, the SMALLER group joins the BIGGER one. This keeps the "tree" (group structure) short and flat.

*ELI5*: "When two clubs merge, the bigger club's president stays president."

**Trick 2 — Path Compression**: When you ask "who's my leader?", you walk up to the leader. But along the way, you make EVERYONE you passed point DIRECTLY to the leader. Next time, it's instant!

*ELI5*: "When you visit the principal, everyone in line behind you also learns where the principal's office is. Next time → straight there!"

Together, these make every operation effectively **O(1)** (technically O(α(n)), where α grows so slowly it's ≤ 4 for any practical input).

---

## 📝 What Exactly Is a Disjoint-Set?

A **disjoint-set** data structure maintains a collection of **non-overlapping groups** (sets).

**"Non-overlapping"** means: every element belongs to EXACTLY one group. No element is in two groups at the same time.

Each group has a **representative** (leader) — one element that identifies the group. Two elements are in the same group if and only if they have the same representative.

---

## 📋 The Three Operations — Explained in Detail

### 1. MAKE-SET(x) — "x starts their own group"

Creates a new group containing only x. x is both the only member AND the leader.

```
MAKE-SET(x)
1   x.parent = x      // x points to itself (it's its own leader)
2   x.rank = 0        // rank starts at 0 (used for Union by Rank)
```

**After MAKE-SET for a, b, c, d:**
```
(a)  (b)  (c)  (d)    ← Four separate groups, each with 1 person
 ↑    ↑    ↑    ↑       (each points to itself)
```

### 2. FIND-SET(x) — "Who is x's group leader?"

Follow the chain of parent pointers from x up to the root (the node that points to itself). The root is the representative (leader).

**Without path compression:**
```
FIND-SET(x)
1   while x ≠ x.parent
2       x = x.parent
3   return x
```

**With path compression (THE GOOD VERSION):**
```
FIND-SET(x)
1   if x ≠ x.parent
2       x.parent = FIND-SET(x.parent)    // Recursively find root AND compress
3   return x.parent
```

What does path compression do? It makes EVERY node on the path point DIRECTLY to the root!

```
BEFORE FIND(d):           AFTER FIND(d):
    a (root)                  a (root)
    |                       / | \
    b                      b  c  d   ← everyone now points to a!
    |
    c
    |
    d
```

Next time anyone calls FIND(b), FIND(c), or FIND(d), it's ONE step instead of multiple!

### 3. UNION(x, y) — "Merge x's group and y's group"

First, find the leaders of both groups. If they're the same leader, they're already in the same group — done! If different, make one leader point to the other.

**With Union by Rank:**
```
UNION(x, y)
1   root_x = FIND-SET(x)
2   root_y = FIND-SET(y)
3   if root_x == root_y: return    // Already same group!
4   LINK(root_x, root_y)

LINK(x, y)    // x and y are both roots
1   if x.rank > y.rank
2       y.parent = x           // Smaller rank joins bigger rank
3   else if x.rank < y.rank
4       x.parent = y
5   else
6       x.parent = y           // Equal rank: pick one, increment
7       y.rank = y.rank + 1
```

**Why Union by Rank?** Without it, you might create a long chain:
```
BAD: a → b → c → d → e → f     ← FIND takes O(n)!
GOOD:      a                    ← FIND takes O(log n)
          / | \
         b  c  d
        / \
       e   f
```

Union by Rank prevents the chain from getting too long by always attaching the SHORTER tree under the TALLER one.

---

## 🌲 How the Tree Representation Works

Each group is a **rooted tree**:
- Each node points to its **parent**
- The **root** points to **itself** (that's how you know it's the root)
- The root = the representative (leader) of the group

```
Group {a, b, c, d}:          Group {e, f, g}:
       a (root, a.parent = a)      e (root, e.parent = e)
      / \                         / \
     b   c                       f   g
     |
     d
```

To check if d and g are in the same group:
- FIND(d): d → b → a (root). Leader = a.
- FIND(g): g → e (root). Leader = e.
- a ≠ e → **Different groups!**

To merge: UNION(d, g) → LINK(a, e) → one root points to the other.

---

## 🎨 Complete Visual Walkthrough

Let me trace a sequence of operations step by step.

### Setup: MAKE-SET for elements 1 through 8

```
(1) (2) (3) (4) (5) (6) (7) (8)     ← 8 separate groups
```

### UNION(1, 2): Merge groups of 1 and 2

```
FIND(1) = 1, FIND(2) = 2. Different roots.
Both rank 0 → equal: make 1.parent = 2 (or 2.parent = 1), increment rank.
Let's say 2.parent = 1, rank(1) = 1.

    1        (3) (4) (5) (6) (7) (8)
    |
    2
```

### UNION(3, 4): Merge groups of 3 and 4

```
    1        3        (5) (6) (7) (8)
    |        |
    2        4
```

### UNION(1, 3): Merge group {1,2} with group {3,4}

```
FIND(1) = 1 (rank=1), FIND(3) = 3 (rank=1). Equal ranks → 3.parent = 1, rank(1) = 2.

       1                (5) (6) (7) (8)
      / \
     2   3
         |
         4
```

### UNION(5, 6), UNION(7, 8), UNION(5, 7):

```
After UNION(5,6):    5       After UNION(7,8):    7
                     |                            |
                     6                            8

After UNION(5,7): equal rank → 5.parent = 7 (or vice versa)
Let's say: 
       7 (rank=2)
      / \
     5   8
     |
     6
```

### UNION(1, 5): Merge the two big groups

```
FIND(1) = 1 (rank=2), FIND(5): 5→7 (rank=2). Equal rank → 7.parent = 1, rank(1) = 3.

             1 (rank=3)
           / | \
          2  3  7
             |  / \
             4 5   8
               |
               6
```

### Now FIND(6) with PATH COMPRESSION:

```
Path: 6 → 5 → 7 → 1 (root!)

Path compression: make 6, 5, and 7 all point directly to 1.

BEFORE:                  AFTER:
       1                        1
     / | \                 / / | | \ \
    2  3  7               2 3 4 5 6 7 8
       |  / \
       4 5   8
         |
         6
```

Now ANY future FIND on 2, 3, 4, 5, 6, 7, or 8 takes just ONE step! 🚀

---

## ⏱️ Time Complexity — Why It's Practically O(1)

### Without Optimizations
FIND can take O(n) — following a long chain. m operations take O(mn). Terrible!

### With Union by Rank Only
FIND takes O(log n). Rank ensures tree height ≤ log n. m operations take O(m log n).

### With Path Compression Only
Amortized O(log n) per operation. Path compression gradually flattens the tree.

### With BOTH (This Is What We Use!)

**O(α(n)) per operation**, where α(n) is the **inverse Ackermann function**.

### What Is α(n)? Why Should I Care?

The Ackermann function grows INSANELY fast. Its inverse, α(n), grows INSANELY slowly:

| n | α(n) |
|---|------|
| 1 | 0 |
| 2 | 1 |
| 4 | 2 |
| 16 | 3 |
| 65,536 | 4 |
| 2^65,536 (a number with ~20,000 digits!) | 5 |

**α(n) ≤ 4 for any n that could possibly fit in any computer or even the observable universe.**

So O(α(n)) = O(4) = **effectively O(1)**!

### Summary Table

| Optimization | FIND Time | m Operations Total |
|-------------|----------|-------------------|
| None | O(n) | O(mn) |
| Union by Rank only | O(log n) | O(m log n) |
| Path Compression only | O(log n) amortized | O(m log n) |
| **BOTH** | **O(α(n)) ≈ O(1)** | **O(m · α(n)) ≈ O(m)** |

---

## 🌍 Where Is DSU Used?

| Application | How DSU Helps | Why DSU Is Perfect |
|------------|--------------|-------------------|
| **Kruskal's MST** | Check if edge creates cycle | FIND + UNION per edge = nearly O(1) |
| **Connected components** | Group connected vertices | Process edges, union connected pairs |
| **Network connectivity** | "Are computers A and B connected?" | FIND(A) == FIND(B)? |
| **Image segmentation** | Group similar adjacent pixels | Union neighboring similar pixels |
| **Percolation** | Does water flow from top to bottom? | Union connected cells |

---

## 🐍 Python Implementation — Every Line Commented

```python
class DisjointSetUnion:
    """
    Disjoint-Set Union (Union-Find) with:
    - Union by Rank (keeps trees short)
    - Path Compression (flattens trees during FIND)
    
    Together, these give O(α(n)) ≈ O(1) per operation!
    """
    
    def __init__(self, n):
        """
        Create n singleton sets (elements 0 through n-1).
        Each element starts as its own group, its own leader.
        """
        self.parent = list(range(n))    # parent[i] = i means "i is its own leader"
        self.rank = [0] * n             # All ranks start at 0
    
    def find(self, x):
        """
        Find the leader (root) of x's group.
        
        Uses PATH COMPRESSION: every node on the path from x to root
        gets rewired to point DIRECTLY to the root.
        
        This is the magic that makes future finds super fast!
        """
        if self.parent[x] != x:
            # x is NOT the root. Recursively find the root...
            self.parent[x] = self.find(self.parent[x])
            # ...and make x point directly to it! (Path compression)
        return self.parent[x]
    
    def union(self, x, y):
        """
        Merge the groups containing x and y.
        
        Uses UNION BY RANK: attach the shorter tree under the taller one.
        This keeps the tree height small (logarithmic without compression).
        
        Returns True if a merge happened, False if x and y were already
        in the same group.
        """
        root_x = self.find(x)    # Find leader of x's group
        root_y = self.find(y)    # Find leader of y's group
        
        if root_x == root_y:
            return False          # Already in the same group — nothing to do!
        
        # Union by Rank: smaller rank goes under bigger rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y      # x's tree goes under y's tree
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x      # y's tree goes under x's tree
        else:
            # Equal ranks: pick one (arbitrary), increment the other's rank
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        
        return True
    
    def connected(self, x, y):
        """Are x and y in the same group?"""
        return self.find(x) == self.find(y)


# ===== EXAMPLE =====
dsu = DisjointSetUnion(8)  # Elements 0, 1, 2, 3, 4, 5, 6, 7

# Build two groups: {0,1,2,3} and {4,5,6,7}
dsu.union(0, 1)
dsu.union(2, 3)
dsu.union(0, 2)     # Now {0,1,2,3} are in one group

dsu.union(4, 5)
dsu.union(6, 7)
dsu.union(4, 6)     # Now {4,5,6,7} are in one group

# Queries
print(f"0 and 3 in same group? {dsu.connected(0, 3)}")  # True
print(f"0 and 4 in same group? {dsu.connected(0, 4)}")  # False

# Merge the two big groups
dsu.union(0, 4)
print(f"1 and 7 in same group? {dsu.connected(1, 7)}")  # True — everyone is connected!
```

---

## 🧰 Problem-Solving Techniques

### Technique 1: Always Call FIND Before Comparing
Don't compare x.parent directly — it might not be the root! Always use FIND(x) to get the actual root.

### Technique 2: Cycle Detection in Graphs
For each edge (u, v): if FIND(u) == FIND(v) BEFORE union, adding this edge creates a cycle!

```python
def has_cycle(n, edges):
    dsu = DisjointSetUnion(n)
    for u, v in edges:
        if dsu.connected(u, v):
            return True  # u and v already connected → cycle!
        dsu.union(u, v)
    return False
```

### Technique 3: Counting Connected Components
Start with n components. Each successful UNION reduces the count by 1.

```python
components = n
for u, v in edges:
    if dsu.union(u, v):
        components -= 1
print(f"Connected components: {components}")
```

### Technique 4: Kruskal's MST Algorithm
Sort edges by weight. Process edges smallest first. For each edge, if it connects two DIFFERENT components (FIND gives different roots), add it to the MST and UNION.

---

## ⚠️ Common Mistakes

| Mistake | Why It's Wrong | Fix |
|---------|---------------|-----|
| Comparing x.parent instead of FIND(x) | Parent might not be the root | Always use FIND |
| Forgetting path compression | FIND stays O(log n) instead of ≈O(1) | Add `x.parent = FIND(x.parent)` |
| Incrementing rank on every union | Rank should only increase when equal | Only increment when both ranks are equal |
| Not checking if already same group | Wastes time | Check FIND(x) == FIND(y) first |

---

## 📝 Practice Questions with Detailed Solutions

### Q1: Perform UNION(a,b), UNION(c,d), UNION(e,f), UNION(a,c), UNION(a,e). Draw tree after each.

**Full Solution:**
```
Start: (a)(b)(c)(d)(e)(f)

UNION(a,b): equal rank → b.parent=a, rank(a)=1
    a
    |
    b

UNION(c,d): equal rank → d.parent=c, rank(c)=1
    c
    |
    d

UNION(e,f): equal rank → f.parent=e, rank(e)=1
    e
    |
    f

UNION(a,c): rank(a)=1, rank(c)=1, equal → c.parent=a, rank(a)=2
       a
      / \
     b   c
         |
         d

UNION(a,e): rank(a)=2 > rank(e)=1 → e.parent=a
          a
        / | \
       b  c  e
          |  |
          d  f
```

### Q2: After Q1, call FIND(d) with path compression. Show before and after.

**Full Solution:**
```
BEFORE:           AFTER:
     a                 a
   / | \         / | | \ \
  b  c  e       b  c  d  e  f
     |  |
     d  f

FIND(d): d → c → a (root!). Path compression: d.parent = a.
Now d points directly to a.
Also c already pointed to a, so no change for c.
```

### Q3: Use DSU to find connected components: edges (1,2),(3,4),(5,6),(1,5),(2,3).

**Full Solution:**
```
Start: 6 elements, 6 components.

UNION(1,2): merge. Components = 5. Groups: {1,2},{3},{4},{5},{6}
UNION(3,4): merge. Components = 4. Groups: {1,2},{3,4},{5},{6}
UNION(5,6): merge. Components = 3. Groups: {1,2},{3,4},{5,6}
UNION(1,5): FIND(1)≠FIND(5) → merge. Components = 2. Groups: {1,2,5,6},{3,4}
UNION(2,3): FIND(2)=root of {1,2,5,6}, FIND(3)=root of {3,4}. Different → merge.
            Components = 1. Groups: {1,2,3,4,5,6}

Final: 1 connected component.
```

### Q4: How to detect a cycle when adding edge (u,v)?

**Full Solution:**
```
Before adding edge (u,v):
  If FIND(u) == FIND(v) → they're ALREADY connected → adding this edge
  creates a CYCLE!

Example: edges processed so far: (1,2), (2,3)
  Now processing (1,3): FIND(1) = FIND(3) (both in same group)
  → CYCLE DETECTED! Triangle 1-2-3.
```

### Q5: Implement Kruskal's MST for edges: (A,B,1),(B,C,4),(A,C,3),(C,D,2),(B,D,5).

**Full Solution:**
```
Sort by weight: (A,B,1), (C,D,2), (A,C,3), (B,C,4), (B,D,5)

Process (A,B,1): FIND(A)≠FIND(B) → add to MST. UNION(A,B).
Process (C,D,2): FIND(C)≠FIND(D) → add to MST. UNION(C,D).
Process (A,C,3): FIND(A)≠FIND(C) → add to MST. UNION(A,C).
Process (B,C,4): FIND(B)==FIND(C) → SKIP (would create cycle!).
Process (B,D,5): FIND(B)==FIND(D) → SKIP (would create cycle!).

MST edges: {(A,B,1), (C,D,2), (A,C,3)}. Total weight = 6. ✅
```

### Q6: What is α(number of atoms in universe)?

**Solution:** The universe has ~10^80 atoms. α(10^80) = **4**. The inverse Ackermann function is mind-bogglingly slow-growing!

### Q7: Why use RANK instead of actual tree height?

**Solution:** Path compression changes the actual heights of subtrees, but we don't update rank when this happens. If we used actual height, we'd need to recompute it after every path compression — expensive! Rank is just an upper bound on height, and the analysis still works with this approximation. This keeps LINK at O(1).

### Q8: Starting from scratch with n=5, process: UNION(0,1), UNION(2,3), UNION(0,2), UNION(0,4). How many nodes does FIND(3) visit?

**Full Solution:**
```
After UNION(0,1): 1.parent=0, rank(0)=1
After UNION(2,3): 3.parent=2, rank(2)=1
After UNION(0,2): equal rank → 2.parent=0, rank(0)=2.
  Tree:    0
          /|\
         1 2
           |
           3
After UNION(0,4): rank(0)=2 > rank(4)=0 → 4.parent=0
  Tree:    0
         /||\
        1 2 4
          |
          3

FIND(3): 3→2→0 (root). Visits 3 nodes.
After path compression: 3.parent=0. Now FIND(3) would visit just 1 node!
```

### Q9: What happens if two elements are already in the same group and you call UNION?

**Solution:** FIND(x) and FIND(y) return the SAME root. The check `if root_x == root_y: return False` catches this and does nothing. No change to the tree. This is important — without this check, you'd create a loop!

### Q10: Can DSU determine the SIZE of each group?

**Solution:** Yes! Add a `size` array. Initialize `size[i] = 1`. During LINK, add the smaller group's size to the larger one's.

```python
def union(self, x, y):
    rx, ry = self.find(x), self.find(y)
    if rx == ry: return
    if self.rank[rx] < self.rank[ry]: rx, ry = ry, rx
    self.parent[ry] = rx
    self.size[rx] += self.size[ry]  # Track group size!
    if self.rank[rx] == self.rank[ry]: self.rank[rx] += 1
```

Now `self.size[FIND(x)]` gives the size of x's group in O(α(n)).

---

## 📋 Quick Revision Cheat Sheet

```
┌───────────────────────────────────────────────────────┐
│  DISJOINT-SET UNION — EVERYTHING IN ONE BOX           │
├───────────────────────────────────────────────────────┤
│                                                       │
│  THREE OPERATIONS:                                    │
│  MAKE-SET(x): x.parent = x, x.rank = 0                │
│  FIND(x): follow parents to root + path compression   │
│UNION(x,y): FIND both roots, LINK smaller under bigger │
│                                                       │
│  TWO OPTIMIZATIONS:                                   │
│  Union by Rank: shorter tree joins taller tree        │
│  Path Compression: everyone points directly to root   │
│                                                       │
│  TIME: O(α(n)) per operation ≈ O(1) in practice       │
│                                                       │
│  KEY APPLICATIONS:                                    │
│  ✅ Kruskal's MST                                     │
│  ✅ Cycle detection in undirected graphs              │
│  ✅ Connected components                              │
│  ✅ Network connectivity                              │
│                                                       │
└───────────────────────────────────────────────────────┘
```

## 📚 References
- CLRS Chapter 21 (Disjoint Sets)
- [Lectures 10, 11, 12 — Pr V Raj S](https://walkccc.me/CLRS/Chap21/21.1/)
