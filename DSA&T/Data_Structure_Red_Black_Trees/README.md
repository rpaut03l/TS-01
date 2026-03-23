# 🔴⚫ Red-Black Trees — Crystal Clear Complete Guide

> **One-Liner**: A Red-Black Tree is a BST that paints nodes red or black and follows 5 simple rules to GUARANTEE it stays balanced — so everything is always O(log n)!

---

## 🧒 ELI5 — Explain Like I'm 5

Remember how BSTs can become a long stick if you add sorted numbers? That's like a seesaw where all kids sit on ONE side — it tips over!

A Red-Black Tree is a **SMART tree** that REFUSES to become lopsided.

**Here's how it works:**

Every kid (node) wears either a **RED shirt** 🔴 or a **BLACK shirt** ⚫.

There are 5 rules:
1. Every kid wears red OR black (no other colors!)
2. The **principal** (root) ALWAYS wears black
3. The **invisible walls** (NIL leaves at the bottom) are black
4. A kid in red **can't have a parent also in red** (no two reds in a row!)
5. If you walk from ANY kid down to the ground, you always pass the **same number of black shirts** on every path

**Why do these rules matter?**

Rules 4 and 5 together FORCE the tree to be balanced! Think about it:
- Rule 4 says you can't have too many reds in a row (limits "thin" paths)
- Rule 5 says all paths have the same number of blacks (limits "one side being much longer")

Together, these guarantee the tree is never taller than **2 × log(n)** — so all operations stay fast!

**When you add a new kid (insert), you:**
1. Give them a RED shirt (why red? explained below!)
2. Check: "Did this break any rules?"
3. If YES → repaint some shirts and/or spin branches until fixed

The "spinning" is called **rotation** — it rearranges a few nodes to rebalance the tree, and it takes just O(1) time!

---

## 📝 Why Do We Need Red-Black Trees?

| Problem with Plain BSTs | How RB-Trees Fix It |
|------------------------|---------------------|
| Sorted input → tree becomes a stick → O(n) height | Height is ALWAYS ≤ 2·log(n+1) |
| No self-balancing | Auto-rebalances after every insert/delete |
| Worst case O(n) per operation | Worst case **O(log n)** per operation — guaranteed! |

### Where Are They Used in Real Life?

| Product | What Uses RB-Trees |
|---------|-------------------|
| **Java** | TreeMap, TreeSet |
| **C++ STL** | std::map, std::set, std::multimap |
| **Linux Kernel** | Process scheduling (Completely Fair Scheduler) |
| **Databases** | Internal indexing |

---

## 🎯 The 5 Red-Black Properties — Explained Very Carefully

```
Property 1: Every node is either RED or BLACK.
Property 2: The ROOT is BLACK.
Property 3: Every LEAF (NIL sentinel) is BLACK.
Property 4: If a node is RED, then BOTH its children are BLACK.
            (In other words: no parent-child pair can both be red!)
Property 5: For each node, ALL simple paths from that node to
            descendant leaves contain the SAME number of BLACK nodes.
```

### Let me explain each one:

**Property 1** is trivial — each node has a color attribute, either RED or BLACK. Nothing fancy.

**Property 2**: The root is always black. Think of the root as the "principal" of the school — they always wear the standard black uniform.

**Property 3**: This is about the NIL sentinel. Instead of using actual NULL pointers, we use a special "nil" node that's always BLACK. This simplifies the code — you never have to check for NULL.

**Property 4 (THE IMPORTANT ONE)**: No two adjacent reds! If a node is red, its parent must be black, and its children must be black. This prevents long chains of red nodes.

*Why this matters*: If you could have many reds in a row, a path could be very long (all reds) without adding to the black-height. Rule 4 prevents this.

**Property 5 (THE OTHER IMPORTANT ONE)**: Every path from any node down to a leaf passes through the SAME number of black nodes. This number is called the **black-height**.

*Why this matters*: This ensures no path is "much longer" than another. Combined with rule 4 (reds can't be consecutive), this bounds the tree height.

### What Is Black-Height?

The **black-height** bh(x) of a node x = number of black nodes on any path from x DOWN to a leaf (NOT counting x itself).

```
Example:
          (7:B)  bh=2
         /     \
      (3:R)    (18:R)  bh=2
      /   \    /    \
   (1:B) (5:B)(10:B)(22:B)  bh=1
   / \   / \   / \    / \
  NIL NIL ...  (all NIL are BLACK, bh=0)

Path from root to any NIL: always 2 black nodes (excluding root).
bh(root) = 2 ✅
```

---

## 📏 Height Bound: h ≤ 2·log₂(n+1) — Why the Tree Can't Get Too Tall

### The Theorem (in plain English)

> A Red-Black Tree with n internal nodes has height **at most 2·log₂(n+1)**.

For n = 1,000,000: h ≤ 2 × 20 = 40 levels maximum. That's incredibly shallow!

### Why Is This True? (Proof Sketch)

**Fact 1**: A subtree rooted at node x contains at least **2^bh(x) - 1** internal nodes.

*Why?* Because each path has bh(x) black nodes, and each black node must exist. The minimum tree is when every non-leaf has exactly 2 children (binary tree), giving 2^bh(x) - 1 nodes.

**Fact 2**: bh(root) ≥ h/2.

*Why?* Because of Property 4 (no two consecutive reds), at least HALF the nodes on any root-to-leaf path must be black.

**Putting it together**:
```
n ≥ 2^bh(root) - 1 ≥ 2^(h/2) - 1
n + 1 ≥ 2^(h/2)
log₂(n+1) ≥ h/2
h ≤ 2·log₂(n+1)  ✅
```

---

## 🔄 Rotations — The Rebalancing Tool (Simple!)

A **rotation** is a local rearrangement of 2-3 nodes that changes the tree's shape WITHOUT breaking the BST property. It takes **O(1)** time — just changing a few pointers.

### LEFT-ROTATE

```
BEFORE:              AFTER:
    x                   y
   / \                 / \
  a    y      →       x    c
      / \            / \
     b    c         a    b
```

**What happened?**
- y (x's right child) becomes the new parent
- x becomes y's left child
- b (y's old left child) becomes x's new right child

**Why does BST property still hold?**
- a < x < b < y < c — this ordering is the same before and after! ✅

### RIGHT-ROTATE (Mirror of left-rotate)

```
BEFORE:              AFTER:
      y                 x
     / \               / \
    x    c    →       a    y
   / \                    / \
  a    b                 b    c
```

### Pseudocode for LEFT-ROTATE

```
LEFT-ROTATE(T, x)
1   y = x.right                    // y is x's right child
2   x.right = y.left               // b becomes x's right child
3   if y.left ≠ T.nil
4       y.left.parent = x          // update b's parent
5   y.parent = x.parent            // y takes x's place
6   if x.parent == T.nil           
7       T.root = y                 // x was root, now y is
8   else if x == x.parent.left
9       x.parent.left = y          // x was a left child
10  else
11      x.parent.right = y         // x was a right child
12  y.left = x                     // x becomes y's left child
13  x.parent = y                   // update x's parent
```

**Key point**: Rotation is O(1) — just changing ~5 pointers. It's VERY cheap!

---

## ➕ Insertion — Step by Step

### Big Picture

1. **Insert like a normal BST** (find the right spot, attach the node)
2. **Color the new node RED** (why? explained below!)
3. **Fix any rule violations** using recoloring and rotations

### Why Insert as RED?

If we insert as BLACK, we IMMEDIATELY violate Property 5 (one path has an extra black node — messing up the equal-black-height property). This is hard to fix!

If we insert as RED, we MIGHT violate Property 4 (if the parent is also red — a red-red violation). But this is EASY to fix with recoloring and at most 2 rotations!

### Full Insert Pseudocode

```
RB-INSERT(T, z)
1   // Standard BST insert
2   y = T.nil; x = T.root
3   while x ≠ T.nil
4       y = x
5       if z.key < x.key then x = x.left
6       else x = x.right
7   z.parent = y
8   if y == T.nil then T.root = z
9   else if z.key < y.key then y.left = z
10  else y.right = z
11  z.left = T.nil; z.right = T.nil
12  z.color = RED          // ← NEW node is always RED
13  RB-INSERT-FIXUP(T, z)  // Fix any violations
```

---

## 🔧 Insert Fixup — The 3 Cases Explained VERY Clearly

After inserting z (RED), there might be a RED-RED violation (z and its parent both RED). To fix it, we look at z's **uncle** (the sibling of z's parent).

### The Players

```
g = z's grandparent (must be BLACK, because z's parent is RED
    and if grandparent were RED, there was already a violation before our insert)
p = z's parent (RED — that's the problem!)
u = z's uncle (p's sibling)
z = the node we just inserted (RED)
```

---

### CASE 1: Uncle is RED 🔴

**This is the easiest case!**

```
BEFORE:                    AFTER:
      g(B)                    g(R) ← might cause new violation above!
     / \                     / \
   p(R)  u(R)     →      p(B)  u(B)
   /                      /
 z(R)                   z(R)

WHAT WE DO:
1. Recolor p to BLACK
2. Recolor u to BLACK  
3. Recolor g to RED
4. Move z up to g (check for violations at grandparent now)
```

**Why does this work?**

- Making p and u BLACK fixes the red-red violation between z and p.
- Making g RED keeps the black-height the same on all paths through g (we removed one black from each side by changing p and u, but added one black to the children, so the net effect on any path is... wait, let me think more carefully).
- Actually: before, paths through p had g(B)→p(R)→... and paths through u had g(B)→u(R)→...  
  After: paths through p have g(R)→p(B)→... and paths through u have g(R)→u(B)→...  
  The number of black nodes on each path stays the same! ✅
- But now g is RED, and if g's parent is also RED, we have a NEW violation! So we move z up to g and check again.

**ELI5**: "If uncle is red, everyone swaps shirts! Then check grandpa for problems."

**Important**: This case might repeat all the way up the tree (O(log n) times), but each repetition is O(1) work.

---

### CASE 2: Uncle is BLACK ⚫ and z is an INNER child (zig-zag shape)

**What does "inner child" mean?**

If p is a LEFT child of g, and z is a RIGHT child of p → z is the "inner" child (they make a zig-zag shape: left-then-right).

```
BEFORE:                 AFTER (→ becomes Case 3):
      g(B)                   g(B)
     / \                    / \
   p(R)  u(B)            z(R)  u(B)
     \                   /
     z(R)              p(R)

WHAT WE DO:
1. Set z = p (move z up to parent)
2. LEFT-ROTATE on z (the old p)
→ Now we have a straight-line shape (Case 3!)
```

**ELI5**: "z is on the wrong side — it makes a zig-zag. Rotate to straighten it into a line, then handle it as Case 3."

---

### CASE 3: Uncle is BLACK ⚫ and z is an OUTER child (straight line)

**What does "outer child" mean?**

If p is a LEFT child of g, and z is a LEFT child of p → z is the "outer" child (they make a straight line: left-left).

```
BEFORE:                 AFTER:
      g(B)                  p(B) ← new root of subtree, colored BLACK
     / \                   / \
   p(R)  u(B)    →     z(R)  g(R) ← g becomes RED
   /                            \
 z(R)                           u(B)

WHAT WE DO:
1. Recolor p to BLACK
2. Recolor g to RED
3. RIGHT-ROTATE on g
→ DONE! No more violations! ✅
```

**Why does this work?**
- p is now the root of the subtree, colored BLACK — no red-red above or below.
- g is now p's right child, colored RED — but its children (u and former p.right) are BLACK, so no violation.
- Black-heights are preserved because we moved one BLACK (g→p) and one RED (p→g).

**ELI5**: "z and parent make a straight line. Spin grandpa down, swap shirts between parent and grandpa. All fixed!"

---

### Mirror Cases

Everything above assumes p is a LEFT child of g. If p is a RIGHT child, swap all "left" and "right" in the descriptions and rotations. The logic is identical, just mirrored.

### Summary of All Cases

| Case | Uncle Color | z Position | Action | Done? |
|------|------------|-----------|--------|-------|
| 1 | RED | Either | Recolor p,u,g. Move z to g. | Maybe — check again |
| 2 | BLACK | Inner (zig-zag) | Rotate p to straighten → Case 3 | → Case 3 |
| 3 | BLACK | Outer (straight) | Rotate g, recolor p,g | YES ✅ |

**At most 2 rotations** for any insert! (Case 2 does 1 rotation, Case 3 does 1 rotation, and after Case 3 we're done.)

**At most O(log n) recolorings** (Case 1 can repeat up the tree).

---

## 🎨 Complete Visual Walkthrough: Insert 7, 3, 18, 10, 22, 8, 11, 26

Let me trace every insert carefully.

### Insert 7: First node → root → color BLACK
```
  (7:B)
```
Properties: ✅ all good.

### Insert 3: 3 < 7 → left child. Color RED. Parent 7 is BLACK → no violation.
```
  (7:B)
  /
(3:R)
```
Properties: ✅ (rule 4: 3 is red, its parent 7 is black — fine!)

### Insert 18: 18 > 7 → right child. Color RED. Parent 7 is BLACK → no violation.
```
    (7:B)
   /    \
(3:R)  (18:R)
```
Properties: ✅

### Insert 10: 10 > 7 → right, 10 < 18 → left of 18. Color RED.
```
    (7:B)
   /    \
(3:R)  (18:R)
       /
     (10:R)    ← RED-RED VIOLATION! (10 and 18 both red)
```

**Fix**: z=10, p=18(R), g=7(B), uncle=3(R). **Uncle is RED → Case 1!**
- Recolor: 18→B, 3→B, 7→R. Then root must be BLACK: 7→B.

```
    (7:B)
   /    \
(3:B)  (18:B)
       /
     (10:R)
```
Properties: ✅ All good now!

### Insert 22: 22 > 7 → right, 22 > 18 → right of 18. Color RED. Parent 18 is BLACK → fine.
```
    (7:B)
   /    \
(3:B)  (18:B)
       /    \
     (10:R) (22:R)
```
Properties: ✅

### Insert 8: 8 > 7 → right, 8 < 18 → left, 8 < 10 → left of 10. Color RED.
```
    (7:B)
   /    \
(3:B)  (18:B)
       /    \
     (10:R) (22:R)
     /
   (8:R)     ← RED-RED! (8 and 10 both red)
```

**Fix**: z=8, p=10(R), g=18(B), uncle=22(R). **Uncle is RED → Case 1!**
- Recolor: 10→B, 22→B, 18→R.
- Check: 18(R) parent is 7(B) → no new violation.

```
    (7:B)
   /    \
(3:B)  (18:R)
       /    \
     (10:B) (22:B)
     /
   (8:R)
```
Properties: ✅

### Insert 11: 11 > 7 → right, 11 < 18 → left, 11 > 10 → right of 10. Color RED. Parent 10 is BLACK → fine.
```
    (7:B)
   /    \
(3:B)  (18:R)
       /    \
     (10:B) (22:B)
     /   \
   (8:R) (11:R)
```
Properties: ✅

### Insert 26: 26 > 7 → right, 26 > 18 → right, 26 > 22 → right of 22. Color RED. Parent 22 is BLACK → fine.
```
      (7:B)
     /    \
  (3:B)  (18:R)
         /    \
      (10:B) (22:B)
      /   \      \
   (8:R)(11:R) (26:R)
```
Properties: ✅ **FINAL TREE!**

**Height = 3** for 8 nodes. log₂(8) = 3. Maximum allowed = 2×log₂(9) ≈ 6.3. We're well under the limit! ✅

---

## ⏱️ Time Complexity

| Operation | Time | Rotations |
|-----------|------|-----------|
| Search | O(log n) | 0 |
| Insert | O(log n) | ≤ 2 |
| Delete | O(log n) | ≤ 3 |
| Insert fixup | O(log n) recolorings + ≤ 2 rotations |
| Delete fixup | O(log n) recolorings + ≤ 3 rotations |

---

## 🐍 Python Implementation

```python
class RBNode:
    def __init__(self, key, color='RED'):
        self.key = key
        self.color = color
        self.left = self.right = self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NIL = RBNode(None, 'BLACK')  # Sentinel
        self.root = self.NIL

    def left_rotate(self, x):
        """Rotate x's right child up."""
        y = x.right
        x.right = y.left
        if y.left != self.NIL: y.left.parent = x
        y.parent = x.parent
        if x.parent == self.NIL: self.root = y
        elif x == x.parent.left: x.parent.left = y
        else: x.parent.right = y
        y.left = x; x.parent = y

    def right_rotate(self, y):
        """Rotate y's left child up."""
        x = y.left
        y.left = x.right
        if x.right != self.NIL: x.right.parent = y
        x.parent = y.parent
        if y.parent == self.NIL: self.root = x
        elif y == y.parent.left: y.parent.left = x
        else: y.parent.right = x
        x.right = y; y.parent = x

    def insert(self, key):
        """Insert key and fix any violations."""
        z = RBNode(key)
        z.left = z.right = self.NIL
        
        # Standard BST insert
        y = self.NIL; x = self.root
        while x != self.NIL:
            y = x
            x = x.left if z.key < x.key else x.right
        z.parent = y
        if y == self.NIL: self.root = z
        elif z.key < y.key: y.left = z
        else: y.right = z
        
        z.color = 'RED'  # New node is RED
        self._fix_insert(z)

    def _fix_insert(self, z):
        """Fix red-red violations after insert."""
        while z.parent.color == 'RED':  # While there's a red-red violation
            if z.parent == z.parent.parent.left:  # Parent is LEFT child
                uncle = z.parent.parent.right
                if uncle.color == 'RED':          # CASE 1: uncle is red
                    z.parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    z = z.parent.parent           # Move up
                else:
                    if z == z.parent.right:        # CASE 2: z is inner child
                        z = z.parent
                        self.left_rotate(z)        # Straighten → Case 3
                    z.parent.color = 'BLACK'       # CASE 3: z is outer child
                    z.parent.parent.color = 'RED'
                    self.right_rotate(z.parent.parent)
            else:  # Parent is RIGHT child (mirror of above)
                uncle = z.parent.parent.left
                if uncle.color == 'RED':
                    z.parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    self.left_rotate(z.parent.parent)
        
        self.root.color = 'BLACK'  # Root is ALWAYS black

    def inorder(self, x=None, first=True):
        if first: x = self.root
        if x != self.NIL:
            self.inorder(x.left, False)
            print(f"{x.key}({x.color[0]})", end=' ')
            self.inorder(x.right, False)

# Example:
rbt = RedBlackTree()
for k in [7, 3, 18, 10, 22, 8, 11, 26]:
    rbt.insert(k)
rbt.inorder()
# Output: 3(B) 7(B) 8(R) 10(B) 11(R) 18(R) 22(B) 26(R)
```

---

## ❌ RB-DELETE — The Complete Deletion Algorithm (Crystal Clear)

Deletion in Red-Black Trees is the HARDEST operation. But don't panic — I'll break it into tiny pieces.

### Why Is Deletion Hard?

When we delete a node from a BST, we might remove a BLACK node. If we remove a BLACK node, one path now has FEWER black nodes than others → **Property 5 is violated!** (All paths must have the same number of black nodes.)

This creates what's called a **"double black"** situation — the node that replaces the deleted one "owes" an extra black to its path. We need to redistribute this extra blackness through rotations and recoloring.

### The Big Picture of RB-DELETE

```
STEP 1: Do a normal BST delete (with TRANSPLANT helper)
STEP 2: Track which node might cause a violation
STEP 3: If a BLACK node was removed → call RB-DELETE-FIXUP to restore properties
```

### When Do We Need Fixup?

- If the **deleted node** (or the node that was actually removed) was **RED** → No problem! Removing a red node doesn't change any black-heights. No fixup needed!
- If the **deleted node** was **BLACK** → Houston, we have a problem! One path lost a black node. We MUST fix this.

---

### Helper: TRANSPLANT — Replace One Subtree with Another

This is the same as in regular BST deletion, adapted for RB-trees:

```
RB-TRANSPLANT(T, u, v)
1   if u.parent == T.nil
2       T.root = v                    // u was root → v becomes root
3   else if u == u.parent.left
4       u.parent.left = v             // u was a left child → v takes its place
5   else
6       u.parent.right = v            // u was a right child
7   v.parent = u.parent               // update v's parent pointer
```

**Note**: Unlike regular BST transplant, we DON'T check if v is NIL before setting v.parent. In RB-trees, T.nil is a real node, so this always works.

---

### The Full RB-DELETE Algorithm

```
RB-DELETE(T, z)
────────────────────────────────────────────────────────
1   y = z                              // y = node that will be physically removed
2   y_original_color = y.color         // Remember y's original color
3   
4   if z.left == T.nil                 // CASE A: z has no left child
5       x = z.right                    // x = the child that replaces z
6       RB-TRANSPLANT(T, z, z.right)
7   
8   else if z.right == T.nil           // CASE B: z has no right child
9       x = z.left
10      RB-TRANSPLANT(T, z, z.left)
11  
12  else                                // CASE C: z has TWO children
13      y = TREE-MINIMUM(z.right)      // y = z's successor (min of right subtree)
14      y_original_color = y.color     // Remember SUCCESSOR's color (not z's!)
15      x = y.right                    // x = y's only possible child
16      
17      if y.parent == z               // Successor is z's immediate right child
18          x.parent = y               // (handles case where x is T.nil)
19      else
20          RB-TRANSPLANT(T, y, y.right)   // Detach successor
21          y.right = z.right              // Give successor z's right subtree
22          y.right.parent = y
23      
24      RB-TRANSPLANT(T, z, y)         // Replace z with successor
25      y.left = z.left                // Give successor z's left subtree
26      y.left.parent = y
27      y.color = z.color              // Successor takes z's color
28  
29  if y_original_color == BLACK       // Did we remove a BLACK node?
30      RB-DELETE-FIXUP(T, x)          // YES → must fix!
```

### Let Me Explain the Three Cases of RB-DELETE:

**Case A (lines 4-6): Node z has NO LEFT child**

z might have a right child or no children at all. Either way, replace z with z.right (which might be T.nil).

```
BEFORE:         AFTER:
    z               x (z.right)
     \              
      x (might be NIL)
```

**Case B (lines 8-10): Node z has NO RIGHT child**

Replace z with z.left.

```
BEFORE:         AFTER:
    z               x (z.left)
   /
  x
```

**Case C (lines 12-27): Node z has TWO children — the tricky one!**

1. Find z's **successor** y (the minimum of z's right subtree).
2. y replaces z in the tree.
3. y takes z's COLOR (so properties 4 and 5 are preserved from z's perspective).
4. The node that's ACTUALLY REMOVED from its position is y (the successor).
5. x is y's right child (y can't have a left child because y is a minimum).

```
BEFORE:                     AFTER:
      z(B)                      y(B) ← takes z's color
     / \                       / \
    A   ...                   A   ...
        /                         /
       y(?)                     (y's old position is gone)
        \                       
         x(?)  ← this might need fixing
```

### The Critical Decision (line 29):

- If `y_original_color` was **RED** → removing a red node doesn't affect black-heights → **no fixup needed!** ✅
- If `y_original_color` was **BLACK** → removing a black node means one path lost a black node → **MUST call RB-DELETE-FIXUP!** ⚠️

---

## 🔧 RB-DELETE-FIXUP — The 4 Cases Explained VERY Clearly

### What's the Problem We're Fixing?

After deleting a BLACK node, the node x (which took the deleted node's place) is on a path that has **one fewer black node** than it should. We say x has an "extra black" that needs to be pushed somewhere.

The goal: redistribute blackness so all paths have equal black-height again.

### The Setup

```
x = the node that replaced the deleted node (might be T.nil!)
w = x's SIBLING (the other child of x's parent)
```

We keep fixing while:
- x is not the root, AND
- x is BLACK (if x were RED, we'd just color it BLACK and be done!)

### Overview of the 4 Cases

Assume x is the LEFT child of its parent (if it's the right child, everything is mirrored).

```
RB-DELETE-FIXUP(T, x)
────────────────────────────────────────────────────────
1   while x ≠ T.root and x.color == BLACK
2       if x == x.parent.left                // x is left child
3           w = x.parent.right               // w = x's sibling
4           
5           if w.color == RED                 // ══ CASE 1 ══
6               ... (see below)
7           
8           if w.left.color == BLACK and w.right.color == BLACK  // ══ CASE 2 ══
9               ... (see below)
10          else
11              if w.right.color == BLACK     // ══ CASE 3 ══
12                  ... (see below)
13              // ══ CASE 4 ══
14              ... (see below)
15      else
16          ... (mirror of above — x is right child)
17  
18  x.color = BLACK                          // Final: make x black
```

---

### CASE 1: Sibling w is RED 🔴

```
BEFORE:                         AFTER:
       p(B)                          w(B)    ← new parent (was sibling)
      / \                           / \
    x(B) w(R)              →     p(R)  D
   "owes" / \                   / \
     extra C   D              x(B)  C
     black               "still owes"
                          extra black
```

**What we do:**
```
w.color = BLACK               // Sibling becomes black
x.parent.color = RED          // Parent becomes red
LEFT-ROTATE(T, x.parent)      // Rotate parent
w = x.parent.right            // New sibling (was w's left child)
→ Now fall through to Case 2, 3, or 4 with the NEW sibling
```

**ELI5**: "The sibling is red, which is hard to deal with. Let's rotate to make it black, giving us a black sibling. Now we can handle it with Cases 2/3/4."

**Why it helps**: After this transformation, x has a BLACK sibling. Cases 2, 3, 4 all require a black sibling. So Case 1 is a "conversion step."

**Important**: Case 1 does NOT fix the problem directly — it just converts to a situation where Cases 2/3/4 can fix it!

---

### CASE 2: Sibling w is BLACK, and BOTH of w's children are BLACK

```
BEFORE:                         AFTER:
       p(?)                          p(?)    ← p absorbs extra black
      / \                           / \        (if p was red → done!)
    x(B) w(B)              →     x(B) w(R)   (if p was black → p has
   "owes" / \                         / \      the extra black now →
    extra A(B) B(B)                  A(B) B(B)  repeat from p)
    black
```

**What we do:**
```
w.color = RED                  // Take black away from sibling
x = x.parent                  // Move the "extra black" problem UP to parent
→ If parent was RED, the while loop ends (parent becomes BLACK on line 18)
→ If parent was BLACK, repeat the loop with parent as the new x
```

**ELI5**: "Both sibling's kids are black, so I can't steal from them. Instead, I'll make the sibling red (taking away one black from sibling's paths) and push the problem UP to the parent. If the parent was red, we just color it black and we're done!"

**Key insight**: This is the ONLY case that might repeat multiple times (moving up the tree). But it moves up at most O(log n) times — one level per iteration.

---

### CASE 3: Sibling w is BLACK, w's LEFT child is RED, w's RIGHT child is BLACK

```
BEFORE:                         AFTER (→ becomes Case 4):
       p(?)                          p(?)
      / \                           / \
    x(B) w(B)              →     x(B) w'(B)  ← was w's left child
   "owes" / \                         \
    extra C(R) D(B)                    w(R)   ← old sibling is now red
    black                               \
                                        D(B)
```

**What we do:**
```
w.left.color = BLACK           // w's left child becomes black
w.color = RED                  // w becomes red
RIGHT-ROTATE(T, w)             // Rotate w
w = x.parent.right             // New sibling
→ Now this is CASE 4! (sibling is black, sibling's RIGHT child is red)
```

**ELI5**: "The sibling's red child is on the wrong side (left instead of right). Rotate to move it to the right side, then handle it as Case 4."

**Important**: Case 3 does NOT fix the problem — it converts to Case 4, which DOES fix it!

---

### CASE 4: Sibling w is BLACK, w's RIGHT child is RED ← THE FIXER!

This is the case that ACTUALLY resolves the "extra black" problem!

```
BEFORE:                         AFTER:
       p(?)                          w(p's old color)
      / \                           / \
    x(B) w(B)              →     p(B)   D(B)
   "owes" / \                    / \
    extra C(?) D(R)            x(B) C(?)
    black
```

**What we do:**
```
w.color = x.parent.color       // w takes parent's color
x.parent.color = BLACK         // parent becomes black (compensates for x's extra)
w.right.color = BLACK          // w's right child becomes black
LEFT-ROTATE(T, x.parent)       // Rotate parent
x = T.root                     // WE'RE DONE! Set x to root to exit loop
```

**ELI5**: "The sibling's right child is red — perfect! Rotate the parent down, make it black (fixing x's path), and color the sibling's red child black (keeping sibling's paths balanced). Everything is balanced now!"

**Why this works**:
- x's path gains one black (parent, which is now black) → **extra black absorbed!** ✅
- w takes parent's old color → the subtree root's color doesn't change from outside view ✅  
- D becomes black → w's right path doesn't lose a black ✅
- All paths through this subtree now have the correct number of blacks ✅

**This is the TERMINAL case** — after Case 4, we set x = root and exit the loop. No more iterations needed!

---

### Summary: How the 4 Cases Relate to Each Other

```
START: x has "extra black"
  │
  ├─ Sibling RED?
  │   └─ YES → CASE 1: Rotate to get black sibling → go to Case 2/3/4
  │   └─ NO (sibling is BLACK) → check sibling's children:
  │       │
  │       ├─ Both children BLACK?
  │       │   └─ YES → CASE 2: Push extra black UP. Repeat or done.
  │       │   └─ NO → at least one child is RED:
  │       │       │
  │       │       ├─ Right child BLACK (left is RED)?
  │       │       │   └─ CASE 3: Rotate to move red to right → CASE 4
  │       │       │
  │       │       └─ Right child RED?
  │       │           └─ CASE 4: Rotate + recolor → DONE! ✅
```

### Case Flow Diagram:

```
Case 1 → Case 2, 3, or 4
Case 2 → might repeat (move up), or done if parent was red
Case 3 → Case 4
Case 4 → DONE! ✅
```

**Maximum work**: At most 3 rotations total (1 from Case 1, 1 from Case 3, 1 from Case 4) + O(log n) recolorings from Case 2 repeating up the tree.

---

### Complete DELETE-FIXUP Pseudocode

```
RB-DELETE-FIXUP(T, x)
────────────────────────────────────────────────────────
1   while x ≠ T.root and x.color == BLACK
2       if x == x.parent.left              // x is LEFT child
3           w = x.parent.right             // w = sibling
4           
5           // ══ CASE 1: Sibling is RED ══
6           if w.color == RED
7               w.color = BLACK
8               x.parent.color = RED
9               LEFT-ROTATE(T, x.parent)
10              w = x.parent.right         // New sibling
11          
12          // ══ CASE 2: Both of sibling's children are BLACK ══
13          if w.left.color == BLACK and w.right.color == BLACK
14              w.color = RED
15              x = x.parent               // Move problem up
16          else
17              // ══ CASE 3: Sibling's right child is BLACK ══
18              if w.right.color == BLACK
19                  w.left.color = BLACK
20                  w.color = RED
21                  RIGHT-ROTATE(T, w)
22                  w = x.parent.right     // New sibling
23              
24              // ══ CASE 4: Sibling's right child is RED ══
25              w.color = x.parent.color
26              x.parent.color = BLACK
27              w.right.color = BLACK
28              LEFT-ROTATE(T, x.parent)
29              x = T.root                 // DONE!
30      
31      else    // MIRROR: x is RIGHT child (swap left↔right in all above)
32          ... (symmetric code)
33  
34  x.color = BLACK                        // Final cleanup
```

---

## 🎨 RB-DELETE Walkthrough — Deleting a Node Step by Step

### Example Tree:

```
          (13:B)
         /      \
      (8:R)     (17:R)
      /   \      /   \
   (1:B) (11:B)(15:B)(25:B)
      \    /          /
    (6:R)(9:R)     (22:R)
```

### Delete node 13 (the root — has two children!)

**Step 1**: Find successor of 13 = minimum of right subtree = **15**.

**Step 2**: y = 15 (the node that will be physically removed from its position). y_original_color = BLACK.

**Step 3**: x = y.right = T.nil (15 has no right child). 

**Step 4**: Since y (15) is not z's immediate right child:
- TRANSPLANT(T, y, y.right): remove 15 from its position, replace with T.nil
- y.right = z.right (17 subtree)
- TRANSPLANT(T, z, y): replace 13 with 15
- y.left = z.left (8 subtree)
- y.color = z.color = BLACK (15 takes 13's color)

```
AFTER BST DELETE + COLOR COPY:
          (15:B)          ← 15 takes 13's position and color
         /      \
      (8:R)     (17:R)
      /   \         \
   (1:B) (11:B)   (25:B)
      \    /        /
    (6:R)(9:R)   (22:R)
    
    x = T.nil (was 15's right child, now in 15's old position)
    x is under 17, on the left: (17:R).left = T.nil = x
```

**Step 5**: y_original_color was BLACK → **MUST call RB-DELETE-FIXUP(T, x)**!

x = T.nil (BLACK), x.parent = 17.

**FIXUP**: x is left child of 17. Sibling w = 25(B).

Check w's children: w.left = 22(R), w.right = T.nil(B).

w.right is BLACK → **Case 3!** (sibling's right child is black, left is red)
- w.left(22).color = BLACK
- w(25).color = RED
- RIGHT-ROTATE(T, w=25)

```
After Case 3:
          (15:B)
         /      \
      (8:R)     (17:R)
      /   \      /   \
   (1:B) (11:B) x(nil) (22:B)  ← new sibling
      \    /                \
    (6:R)(9:R)             (25:R)
```

Now new sibling w = 22(B), w.right = 25(R) → **Case 4!**
- w(22).color = x.parent(17).color = RED
- x.parent(17).color = BLACK
- w.right(25).color = BLACK
- LEFT-ROTATE(T, x.parent=17)

```
After Case 4:
          (15:B)
         /      \
      (8:R)     (22:R)      ← was sibling, takes parent's color
      /   \     /    \
   (1:B)(11:B)(17:B)(25:B)  ← 17 becomes black, 25 becomes black
      \    /
    (6:R)(9:R)
```

x = T.root → **DONE!** ✅

Verify Property 5 (sample paths):
- 15→8→1→6→nil: blacks = 15(B), 1(B) = 2 ✅
- 15→22→17→nil: blacks = 15(B), 17(B) = 2 ✅
- 15→22→25→nil: blacks = 15(B), 25(B) = 2 ✅

All paths have black-height 2 from root. **All 5 properties restored!** ✅

---

## 🐍 RB-DELETE Python Implementation

```python
def rb_delete(self, z):
    """Delete node z from the Red-Black Tree."""
    y = z
    y_original_color = y.color
    
    if z.left == self.NIL:                    # Case A: no left child
        x = z.right
        self._transplant(z, z.right)
    elif z.right == self.NIL:                 # Case B: no right child
        x = z.left
        self._transplant(z, z.left)
    else:                                      # Case C: two children
        y = self._minimum(z.right)            # Find successor
        y_original_color = y.color
        x = y.right
        
        if y.parent == z:
            x.parent = y                      # Handle x = NIL case
        else:
            self._transplant(y, y.right)
            y.right = z.right
            y.right.parent = y
        
        self._transplant(z, y)
        y.left = z.left
        y.left.parent = y
        y.color = z.color                     # Successor takes z's color
    
    if y_original_color == 'BLACK':           # Removed a BLACK node?
        self._delete_fixup(x)                 # Fix violations!

def _delete_fixup(self, x):
    """Fix RB properties after deleting a BLACK node."""
    while x != self.root and x.color == 'BLACK':
        if x == x.parent.left:               # x is LEFT child
            w = x.parent.right               # w = sibling
            
            # CASE 1: sibling is RED
            if w.color == 'RED':
                w.color = 'BLACK'
                x.parent.color = 'RED'
                self.left_rotate(x.parent)
                w = x.parent.right
            
            # CASE 2: both of sibling's children are BLACK
            if w.left.color == 'BLACK' and w.right.color == 'BLACK':
                w.color = 'RED'
                x = x.parent                 # Move up
            else:
                # CASE 3: sibling's right child is BLACK
                if w.right.color == 'BLACK':
                    w.left.color = 'BLACK'
                    w.color = 'RED'
                    self.right_rotate(w)
                    w = x.parent.right
                
                # CASE 4: sibling's right child is RED
                w.color = x.parent.color
                x.parent.color = 'BLACK'
                w.right.color = 'BLACK'
                self.left_rotate(x.parent)
                x = self.root                # DONE!
        
        else:                                # x is RIGHT child (mirror)
            w = x.parent.left
            
            if w.color == 'RED':
                w.color = 'BLACK'
                x.parent.color = 'RED'
                self.right_rotate(x.parent)
                w = x.parent.left
            
            if w.right.color == 'BLACK' and w.left.color == 'BLACK':
                w.color = 'RED'
                x = x.parent
            else:
                if w.left.color == 'BLACK':
                    w.right.color = 'BLACK'
                    w.color = 'RED'
                    self.left_rotate(w)
                    w = x.parent.left
                
                w.color = x.parent.color
                x.parent.color = 'BLACK'
                w.left.color = 'BLACK'
                self.right_rotate(x.parent)
                x = self.root
    
    x.color = 'BLACK'                        # Final cleanup

def _transplant(self, u, v):
    """Replace subtree rooted at u with subtree rooted at v."""
    if u.parent == self.NIL:
        self.root = v
    elif u == u.parent.left:
        u.parent.left = v
    else:
        u.parent.right = v
    v.parent = u.parent

def _minimum(self, x):
    """Find minimum in subtree rooted at x."""
    while x.left != self.NIL:
        x = x.left
    return x
```

---

## 📝 RB-DELETE Practice Questions with Detailed Solutions

### Q-D1: From the tree below, delete the RED node 8. Does fixup trigger?

```
      (10:B)
     /      \
   (5:B)   (15:B)
   / \
 (3:R)(8:R)
```

**Solution:**

Node 8 is a RED leaf (no children). Delete it directly: set 5.right = T.nil.

y_original_color = RED → **NO fixup needed!** ✅

Removing a red leaf never violates any property — black-heights are unchanged!

```
Result:
      (10:B)
     /      \
   (5:B)   (15:B)
   /
 (3:R)
```

---

### Q-D2: From the tree below, delete the BLACK leaf node 1.

```
      (5:B)
     /     \
   (2:R)   (8:R)
   / \     / \
 (1:B)(3:B)(7:B)(9:B)
```

**Solution:**

Node 1 is a BLACK leaf. Delete it: TRANSPLANT(T, 1, T.nil).

y_original_color = BLACK → **MUST call fixup!**

x = T.nil, x.parent = 2. x is LEFT child of 2.
Sibling w = 3(B).

w.left = T.nil(B), w.right = T.nil(B) → both children BLACK → **Case 2!**
- w(3).color = RED
- x = x.parent = 2

Now x = 2(R). x.color is RED → **while loop exits!**
Line 18: x.color = BLACK → 2 becomes BLACK.

```
Result:
      (5:B)
     /     \
   (2:B)   (8:R)    ← 2 was RED, now BLACK (absorbed extra black)
      \    / \
    (3:R)(7:B)(9:B)  ← 3 was BLACK, now RED
```

Verify: Path 5→2→nil: 2 black nodes (5,2). Path 5→2→3→nil: 2 black nodes (5,2). Path 5→8→7→nil: 2 (5,7). All equal! ✅

---

### Q-D3: Delete the root node 7 from this tree:

```
      (7:B)
     /     \
   (3:R)   (18:R)
   / \     / \
 (1:B)(5:B)(10:B)(22:B)
```

**Solution:**

Node 7 has two children → find successor = minimum of right subtree = **10**.

y = 10, y_original_color = **BLACK**, x = T.nil (10 has no children).

Steps:
1. TRANSPLANT(T, 10, T.nil) — remove 10 from its position
2. y.right = 7.right (18 subtree)
3. TRANSPLANT(T, 7, 10) — replace root 7 with 10
4. y.left = 7.left (3 subtree)
5. y.color = 7.color = BLACK

```
After BST delete:
      (10:B)           ← 10 replaces 7, takes BLACK color
     /      \
   (3:R)   (18:R)
   / \        \
 (1:B)(5:B) (22:B)
 
 x = T.nil at 18.left (where 10 used to be)
```

y_original_color = BLACK → **FIXUP!**

x = T.nil, x.parent = 18. x is LEFT child.
Sibling w = 22(B).
w.left = T.nil(B), w.right = T.nil(B) → **Case 2!**
- w(22).color = RED
- x = x.parent = 18(R)

x = 18, x.color = RED → **loop exits!**
18.color = BLACK.

```
Final result:
      (10:B)
     /      \
   (3:R)   (18:B)    ← was RED, now BLACK
   / \        \
 (1:B)(5:B) (22:R)   ← was BLACK, now RED
```

Verify all paths have 2 blacks from root. ✅

---

### Q-D4: When deleting a node with two children, why do we track y_original_color of the SUCCESSOR, not the deleted node?

**Solution:**

The deleted node z's position in the tree is taken by the successor y, and y gets z's color. So z's position "looks the same" from the outside — no property violation there.

The ACTUAL structural change happens at **y's original position** — that's where a node was physically removed. If y was BLACK, y's original position loses a black node on its path. So we need to fix at y's old position, and we need to know y's ORIGINAL color (before it was changed to z's color) to decide if fixup is needed.

**ELI5**: "z gets replaced by a clone. The real question is: what happened at the spot where we kidnapped the clone from? If the clone was wearing a black shirt, that spot is now missing a black shirt!"

---

### Q-D5: What is the maximum number of rotations RB-DELETE-FIXUP can perform?

**Solution:**

- **Case 1**: 1 rotation (LEFT-ROTATE on parent) → then falls to Case 2, 3, or 4
- **Case 2**: 0 rotations (just recoloring) → but may repeat up the tree
- **Case 3**: 1 rotation (RIGHT-ROTATE on sibling) → falls to Case 4
- **Case 4**: 1 rotation (LEFT-ROTATE on parent) → DONE

Maximum path through cases: Case 1 → Case 3 → Case 4 = **3 rotations total**.

Case 2 can repeat O(log n) times (moving up the tree), but each repetition is just recoloring (O(1) work, 0 rotations).

**Total: at most 3 rotations + O(log n) recolorings = O(log n) time.**

---

### Q-D6: If the deleted node was RED and was a leaf, what happens?

**Solution:**

**Nothing!** y_original_color = RED, so line 29 (`if y_original_color == BLACK`) is FALSE. No fixup is called. The tree is already valid because:
- Removing a red leaf doesn't change any path's black-height (Property 5 safe)
- No red-red violations are created (Property 4 safe)
- Root is still the same color (Property 2 safe)

**This is the easiest case!**

---

## 📋 Updated Quick Revision — Now Including Deletion

```
┌───────────────────────────────────────────────────────────────┐
│  RED-BLACK TREES — COMPLETE CHEAT SHEET                       │
├───────────────────────────────────────────────────────────────┤
│                                                               │
│  5 RULES: node color, root BLACK, NIL BLACK, no red-red,      │
│           equal black-height on all paths                     │
│                                                               │
│  INSERT:                                                      │
│  Color RED → fix with recolor + ≤ 2 rotations                 │
│  Case 1: Uncle RED → recolor, move up                         │
│  Case 2: Uncle BLACK, inner → rotate parent → Case 3          │
│  Case 3: Uncle BLACK, outer → rotate grandparent → DONE ✅    │
│                                                               │
│  DELETE:                                                      │
│  BST delete → if removed BLACK node → fixup                   │
│  Case 1: Sibling RED → rotate to get BLACK sibling → 2/3/4    │
│  Case 2: Sibling BLACK, both kids BLACK → recolor, move up    │
│  Case 3: Sibling BLACK, far kid BLACK → rotate → Case 4       │
│  Case 4: Sibling BLACK, far kid RED → rotate + recolor → ✅   │
│                                                               │
│  MAX ROTATIONS: Insert ≤ 2, Delete ≤ 3                        │
│  TIME: All operations O(log n) guaranteed!                    │
│                                                               │
└───────────────────────────────────────────────────────────────┘
```

---

## 📝 Practice Questions with Detailed Solutions

### Q1: Insert [41, 38, 31, 12, 19, 8] into an empty RB-tree. Show tree after each insert.

**Full Solution:**

```
Insert 41: root → (41:B)

Insert 38: 38<41 → left. RED. Parent is BLACK → OK.
  (41:B)
  /
(38:R)

Insert 31: 31<41 → left, 31<38 → left of 38. RED.
Parent 38 is RED → VIOLATION! Uncle = NIL(B) → Case 3 (outer child, left-left)
  Right-rotate 41, recolor 38→B, 41→R:
    (38:B)
    / \
  (31:R)(41:R)

Insert 12: 12<38 → left, 12<31 → left of 31. RED.
Parent 31 is RED. Uncle = 41(R) → Case 1!
  Recolor: 31→B, 41→B, 38→R. Root must be BLACK → 38→B.
    (38:B)
    / \
  (31:B)(41:B)
  /
(12:R)

Insert 19: 19<38 → left, 19<31? No, 19>12? Yes → right of 12. Actually:
  19<38 → left. At 31: 19<31 → left. At 12: 19>12 → right of 12. RED.
  Parent=12(R). Uncle=NIL(B). z=19 is RIGHT child of 12, which is LEFT child of 31.
  → Case 2 (inner child)! Left-rotate 12, then Case 3:
  
  After left-rotate 12:
    (38:B)
    / \
  (31:B)(41:B)
  /
(19:R)
/
(12:R)

  Now Case 3: Right-rotate 31, recolor 19→B, 31→R:
    (38:B)
    / \
  (19:B)(41:B)
  / \
(12:R)(31:R)

Insert 8: 8<38 → left, 8<19 → left, 8<12 → left of 12. RED.
Parent=12(R). Uncle=31(R) → Case 1!
  Recolor: 12→B, 31→B, 19→R.
  Check: 19(R), parent=38(B) → no new violation.

Final tree:
      (38:B)
      / \
   (19:R)(41:B)
   / \
(12:B)(31:B)
/
(8:R)

✅ All 5 properties hold!
```

### Q2: What is the maximum height of an RB-tree with 15 nodes?

**Solution:** h ≤ 2·log₂(15+1) = 2·4 = **8**. In practice, it's usually around 4-5.

### Q3: Is this a valid RB-tree? Check all 5 properties.
```
    (10:B)
   / \
 (5:R)(20:B)
 /
(3:B)
```

**Solution:**
1. Every node is R or B ✅
2. Root (10) is BLACK ✅
3. NIL leaves are BLACK ✅
4. Red node (5) — children are 3(B) and NIL(B). No red-red ✅
5. Black-height check from root:
   - Path 10→5→3→NIL: black nodes (not counting root) = 3(B). bh = 1.
   - Path 10→5→NIL(right of 5): blacks below root = none (5 is red, NIL is leaf). bh = 0.
   
   **BH MISMATCH! Path through 3 has bh=1, path through 5's right NIL has bh=0.**
   **INVALID!** ❌

### Q4: After left-rotating node x, what changes? What stays the same?

**Solution:**
- **Changes**: x moves down, x.right (y) moves up. The subtree structure changes.
- **Stays the same**: The BST property (inorder traversal is identical before and after).
- **Time**: O(1) — just pointer changes.

### Q5: Why do we use a sentinel (T.nil) instead of regular NULL?

**Solution:** The sentinel simplifies the code. Instead of checking "if x.parent is not NULL" everywhere, we can always access x.parent.color, x.parent.left, etc., because the sentinel is a real node (with color BLACK). This avoids special-case handling and makes the fixup code cleaner.

### Q6: Insert 5 into this tree. What happens?
```
    (10:B)
   / \
 (3:B)(15:B)
```

**Solution:** 5 > 3 → right of 3. Color RED. Parent 3 is BLACK → NO VIOLATION! Done.
```
    (10:B)
   / \
 (3:B)(15:B)
    \
    (5:R)
```
No fixup needed! ✅

### Q7: Now insert 2 into the tree from Q6.

**Solution:** 2 < 3 → left of 3. Color RED. Parent 3 is BLACK → NO VIOLATION!
```
    (10:B)
   / \
 (3:B)(15:B)
 / \
(2:R)(5:R)
```
Still fine! ✅

### Q8: Now insert 1. What cases trigger?

**Solution:** 1 < 3 → left, 1 < 2 → left of 2. RED.
Parent=2(R)! Uncle=5(R)! → **Case 1**: recolor 2→B, 5→B, 3→R.
Check: 3(R), parent=10(B) → OK.
```
    (10:B)
   / \
 (3:R)(15:B)
 / \
(2:B)(5:B)
/
(1:R)
```
✅ All properties hold!

### Q9: Why can't we just use AVL trees instead?

**Solution:** AVL trees are MORE strictly balanced (height ratio ≤ 1 between left and right subtrees), so searches are slightly faster. BUT AVL trees may need up to O(log n) rotations during insert/delete. RB-trees need at most 2 rotations for insert and 3 for delete. For applications with many writes (inserts/deletes), RB-trees have lower overhead. That's why production systems prefer them.

### Q10: How many nodes can an RB-tree have with black-height 3?

**Solution:**
- **Minimum**: All black path, minimum branching. Minimum = 2^3 - 1 = **7 nodes** (a perfect binary tree of height 3 with all blacks: root(B), 2 children(B), 4 grandchildren(B)).

Actually, minimum nodes for bh=3 means the tree could have just the blacks without any reds. A complete binary tree of 3 levels of blacks = 2^3 - 1 = 7 nodes. The actual height is 3.

- **Maximum**: Alternate red and black on every path to maximize reds. Maximum height = 2×3 = 6. Maximum nodes = 2^6 - 1 = **63 nodes**.

---

## 📋 Quick Revision Cheat Sheet

```
┌───────────────────────────────────────────────────────────────┐
│  RED-BLACK TREES — EVERYTHING IN ONE BOX                      │
├───────────────────────────────────────────────────────────────┤
│                                                               │
│  5 RULES:                                                     │
│  1. Every node = RED or BLACK                                 │
│  2. Root = BLACK                                              │
│  3. NIL leaves = BLACK                                        │
│  4. RED node → children must be BLACK (no red-red!)           │
│  5. All paths from node to leaves: same # of BLACKs           │
│                                                               │
│  HEIGHT: ≤ 2·log₂(n+1)                                        │
│                                                               │
│  INSERT: Color RED → fix with recolor + ≤ 2 rotations         │
│  Fixup: Uncle RED → Case 1 (recolor, move up)                 │
│         Uncle BLACK, inner → Case 2 (rotate → Case 3)         │
│         Uncle BLACK, outer → Case 3 (rotate + recolor = done) │
│                                                               │
│  ALL OPERATIONS: O(log n) guaranteed!                         │
│                                                               │
│  USED IN: Java TreeMap, C++ std::map, Linux kernel            │
│                                                               │
└───────────────────────────────────────────────────────────────┘
```

---

## 📚 References

- CLRS — Introduction to Algorithms, Chapter 13
- [Lectures 6, 7 — Pr V Raj S, DSA](https://clrs.skanev.com)
- [Red-Black Tree Visualizer](https://www.cs.usfca.edu/~galles/visualization/RedBlack.html)
