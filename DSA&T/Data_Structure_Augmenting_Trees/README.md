# 🔧 Augmenting Data Structures — Crystal Clear Complete Guide

> **One-Liner**: Augmenting means adding extra info to each node (like a "how many kids in my group?" badge) so you can answer NEW questions in O(log n)!

---

## 🧒 ELI5 — Explain Like I'm 5

Imagine 30 kids standing in a line sorted by height. The teacher asks: **"Who is the 5th shortest?"**

Without any help, you'd count from the shortest: 1... 2... 3... 4... 5! That works, but it's slow if there are 1000 kids.

**The clever trick**: What if every kid wore a BADGE that said: "There are X kids in my group (my section of the line)"?

Then you'd look at the first group leader: "You have 7 kids? OK, the 5th one is in YOUR group." Then look at their sub-leader: "You have 3 kids? The 5th is NOT here (5 > 3), so it must be in the other sub-group..." And so on!

**That badge is the "augmentation."** We add ONE extra piece of info to each node, and suddenly we can answer a completely new question in O(log n)!

---

## 📝 What Does "Augment" Mean?

**Augmenting** a data structure = adding **extra information** to each node so it can support **new operations** that the original structure couldn't do efficiently.

For trees, this means adding an extra **attribute** to each node. The most common augmentation:

```
Standard BST node:           Augmented node:
┌─────────────┐              ┌──────────────────┐
│  key        │              │  key             │
│ left, right │              │  left, right     │
│ parent      │              │  parent          │
└─────────────┘              │  size = 9  ← NEW │
                             └──────────────────┘
```

The `size` tells you: "How many nodes are in the subtree rooted at this node (including itself)?"

---

## 📋 The 4-Step Augmenting Recipe

```
Step 1: CHOOSE an underlying data structure.
        → We use a Red-Black Tree (guaranteed O(log n) height).

Step 2: DETERMINE what extra info to store.
        → We store the subtree SIZE at each node.

Step 3: VERIFY we can maintain this info during modifications.
        → During insert, delete, and rotations, can we update the size
          efficiently? YES — size depends only on children's sizes!

Step 4: DEVELOP new operations using the augmented info.
        → OS-SELECT (find i-th smallest) and OS-RANK (find position of element)
```

### The Augmenting Theorem (Why This Works)

> If the extra attribute at node x can be computed using ONLY information in x, x.left, and x.right (including THEIR extra attributes), then we can maintain it in O(log n) time during insert/delete without affecting performance.

**Why?** Because rotations only affect 2 nodes locally, and we can recompute the attribute for those 2 nodes in O(1). During insert/delete, we update the attribute along the path (O(log n) nodes).

---

## 🏆 Order-Statistic Trees — THE Main Example

An **Order-Statistic Tree** = Red-Black Tree + **size** attribute. It supports:

1. **OS-SELECT(x, i)**: Find the element with rank i (the i-th smallest)
2. **OS-RANK(T, x)**: Find the rank of element x (its position in sorted order)

### The Size Attribute

```
x.size = x.left.size + x.right.size + 1
```

- left.size = how many nodes in the left subtree
- right.size = how many nodes in the right subtree
- +1 = count this node itself

The NIL sentinel has size 0.

### Example Tree

```
            (26, size=7)
           /             \
      (17, size=4)    (41, size=2)
      /         \           \
  (14, size=2) (21, size=1) (47, size=1)
  /
(10, size=1)
```

**Let's verify node 17**: left is node 14 (size=2). Right is node 21 (size=1). 17.size = 2 + 1 + 1 = **4** ✅
**Verify node 26 (root)**: left is 17 (size=4). Right is 41 (size=2). 26.size = 4 + 2 + 1 = **7** ✅

---

## 🔍 OS-SELECT — "Find the i-th Smallest Element"

### The Idea (Very Simple!)

At any node x, we know how many nodes are in its left subtree: `x.left.size`. Call this `left_count`.

- The **rank** of x within its subtree = `left_count + 1` (all left nodes are smaller, plus x itself).

Now:
- If `i == rank`: x is the answer!
- If `i < rank`: the answer is in the LEFT subtree. Search for the i-th smallest there.
- If `i > rank`: the answer is in the RIGHT subtree. But we've already "used up" `rank` elements (everything in the left + x), so search for the **(i - rank)-th** smallest in the right subtree.

### Pseudocode

```
OS-SELECT(x, i)
1   r = x.left.size + 1     // rank of x in its subtree
2   if i == r
3       return x              // Found it!
4   else if i < r
5       return OS-SELECT(x.left, i)       // Go left (same i)
6   else
7       return OS-SELECT(x.right, i - r)  // Go right (adjusted i!)
```

### Walkthrough: Find the 3rd Smallest

Using the tree above. Sorted: [10, 14, 17, 21, 26, 41, 47]. The 3rd smallest = 17.

```
At root (26): r = left.size + 1 = 4 + 1 = 5.
  Is i=3 == 5? No.
  Is i=3 < 5? YES → go LEFT (stay with i=3)

At node (17): r = left.size + 1 = 2 + 1 = 3.
  Is i=3 == 3? YES! → Return node 17 ✅
```

Found in just 2 steps! ✅

### Walkthrough: Find the 6th Smallest

Sorted: [10, 14, 17, 21, 26, 41, 47]. The 6th = 41.

```
At root (26): r = 4 + 1 = 5.
  Is i=6 == 5? No.
  Is i=6 < 5? No.
  i=6 > 5 → go RIGHT with i = 6 - 5 = 1

At node (41): r = 0 + 1 = 1. (41 has no left child, so left.size = 0)
  Is i=1 == 1? YES! → Return node 41 ✅
```

---

## 📊 OS-RANK — "What Position Is This Element In?"

### The Idea

Start at node x. Count how many elements are SMALLER than x:
1. x.left.size elements are smaller (everything in left subtree)
2. Plus 1 for x itself
3. That gives x's rank WITHIN its subtree

But x might not be the root! So walk UP the tree. Every time you come from the RIGHT child of a parent, add the parent's left subtree + 1 (the parent itself) — because those are all smaller than x too.

### Pseudocode

```
OS-RANK(T, x)
1   r = x.left.size + 1       // rank within x's subtree
2   y = x
3   while y ≠ T.root
4       if y == y.parent.right // y came from the right
5           r = r + y.parent.left.size + 1  // add parent's left side + parent
6       y = y.parent
7   return r
```

### Walkthrough: Rank of Node 21

```
At node 21: r = 0 + 1 = 1 (no left child)

Walk up to parent 17: 21 is RIGHT child of 17.
  r = 1 + 17.left.size + 1 = 1 + 2 + 1 = 4

Walk up to parent 26: 17 is LEFT child of 26.
  (LEFT child → don't add anything)

Rank = 4 ✅
Verify: sorted = [10, 14, 17, 21, ...]. 21 is at position 4 ✅
```

---

## 🔄 Maintaining Size During Operations

### During INSERT
Walk down from root to find the insertion spot. At each node on the path, increment size by 1 (because one new node is being added to that subtree).

### During DELETE
After removing a node, walk up from the deletion point. Decrement size by 1 for every ancestor.

### During ROTATION
Only 2 nodes change position. Recompute their sizes:

```
After LEFT-ROTATE(x):  (y replaces x)
  y.size = x.size           // y takes x's old position
  x.size = x.left.size + x.right.size + 1  // recompute x
```

This is O(1) per rotation! ✅

---

## 🐍 Python Implementation

```python
class OSNode:
    def __init__(self, key):
        self.key = key
        self.size = 1  # Every node starts with size 1 (just itself)
        self.left = self.right = self.parent = None

class OrderStatisticTree:
    def __init__(self):
        self.NIL = OSNode(None)
        self.NIL.size = 0  # NIL has size 0
        self.root = self.NIL

    def insert(self, key):
        z = OSNode(key)
        z.left = z.right = self.NIL
        y = self.NIL; x = self.root
        while x != self.NIL:
            x.size += 1  # Each ancestor gets +1
            y = x
            x = x.left if z.key < x.key else x.right
        z.parent = y
        if y == self.NIL: self.root = z
        elif z.key < y.key: y.left = z
        else: y.right = z

    def os_select(self, x, i):
        """Find the i-th smallest element (1-indexed)."""
        r = x.left.size + 1  # rank of x in its subtree
        if i == r:
            return x
        elif i < r:
            return self.os_select(x.left, i)
        else:
            return self.os_select(x.right, i - r)

    def os_rank(self, x):
        """Find the rank (position in sorted order) of node x."""
        r = x.left.size + 1
        y = x
        while y != self.root:
            if y == y.parent.right:
                r += y.parent.left.size + 1
            y = y.parent
        return r

# Example:
ost = OrderStatisticTree()
for k in [26, 17, 41, 14, 21, 47, 10]:
    ost.insert(k)

print(f"3rd smallest: {ost.os_select(ost.root, 3).key}")  # 17
print(f"6th smallest: {ost.os_select(ost.root, 6).key}")  # 41
```

---

## 📝 Practice Questions with Detailed Solutions

### Q1: Build an OS-tree with [15, 10, 20, 8, 12, 18, 25]. Draw with sizes.

**Solution:**
```
        (15, s=7)
       /         \
  (10, s=3)   (20, s=3)
  /     \       /     \
(8,s=1)(12,s=1)(18,s=1)(25,s=1)
```

### Q2: OS-SELECT(root, 4) on the tree above.

**Solution:**
```
At 15: r = 3+1 = 4. i=4 == 4 → FOUND! Return 15.
Sorted: [8,10,12,15,18,20,25] → 4th = 15 ✅
```

### Q3: OS-SELECT(root, 6) on the same tree.

**Solution:**
```
At 15: r=4. i=6 > 4 → go RIGHT with i = 6-4 = 2.
At 20: r = 1+1 = 2. i=2 == 2 → FOUND! Return 20.
Sorted: 6th = 20 ✅
```

### Q4: OS-RANK(T, node 18).

**Solution:**
```
At 18: r = 0+1 = 1 (no left child)
Walk to 20: 18 is LEFT child → no addition.
Walk to 15: 20 is RIGHT child → r = 1 + 3 + 1 = 5
Rank = 5.
Sorted: [8,10,12,15,18,...] → 18 is 5th ✅
```

### Q5: How to count elements between keys a and b?

**Solution:** count = OS-RANK(node_b) - OS-RANK(node_a) + 1. Time: O(log n). Example: elements between 10 and 20 in our tree? RANK(10)=2, RANK(20)=6. Count = 6-2+1 = 5. Verify: {10,12,15,18,20} = 5 ✅

### Q6: OS-SELECT(root, 1) always returns what?

**Solution:** Always the **MINIMUM** element! Because we keep going left (i < r until r=1). Same as TREE-MINIMUM.

### Q7: OS-SELECT(root, root.size) always returns what?

**Solution:** Always the **MAXIMUM** element! Because i is always > r and we keep going right. Same as TREE-MAXIMUM.

### Q8: During left-rotation of x, which sizes change?

**Solution:** Only x and y (x's right child). y.size = x.size (takes x's position). x.size = x.left.size + x.right.size + 1 (recompute). Just 2 updates → O(1).

### Q9: Can you augment with "subtree sum" instead of "subtree size"?

**Solution:** Yes! Store x.sum = x.left.sum + x.right.sum + x.key. This satisfies the augmenting theorem (depends only on x and children). Now you can answer "what's the sum of all keys in a range?" in O(log n).

### Q10: What if we augment with "max key in subtree"?

**Solution:** x.max = max(x.key, x.left.max, x.right.max). Satisfies the theorem. Enables finding max in any subtree in O(1) and range-max queries in O(log n). This is the basis of **interval trees**!

---

## 📋 Quick Revision Cheat Sheet

```
┌───────────────────────────────────────────────────────┐
│  AUGMENTING TREES — EVERYTHING IN ONE BOX             │
├───────────────────────────────────────────────────────┤
│  Augmenting = add extra info to nodes                 │
│                                                       │
│  ORDER-STATISTIC TREE: size attribute                 │
│  x.size = x.left.size + x.right.size + 1              │
│                                                       │
│  OS-SELECT(x, i): find i-th smallest                  │
│    r = left.size + 1                                  │
│    i == r → found!                                    │
│    i < r → go left                                    │
│    i > r → go right with (i - r)                      │
│                                                       │
│  OS-RANK(x): find position of x                       │
│    Start with r = left.size + 1                       │
│    Walk up: add left.size+1 when coming from right    │
│                                                       │
│  BOTH: O(log n)                                       │
│                                                       │
│  Augmenting theorem: if f depends only on node +      │
│  children, it can be maintained in O(log n)           │
└───────────────────────────────────────────────────────┘
```

## 📚 References
- [CLRS Chapter 14](https://clrs.skanev.com)
- Lecture 10 — Pr V Raj S - DSA
