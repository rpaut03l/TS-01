# 🌲 Binary Search Trees (BST) — Crystal Clear Complete Guide

> **One-Liner**: A BST is a tree where left = smaller, right = bigger — finding anything is like playing the "higher or lower" guessing game!

---

## 🧒 ELI5 — Explain Like I'm 5

**Let's play a game!**

I'm thinking of a number between 1 and 100.

You guess: **"50?"**
I say: **"Go HIGHER!"** — Now you know the answer is between 51-100. You just eliminated HALF the possibilities!

You guess: **"75?"**
I say: **"Go LOWER!"** — Now it's between 51-74. Half again!

You guess: **"62?"**
I say: **"YES!"** — Found it in just 3 guesses instead of up to 100!

**A BST works the same way!** At each node, you ask: "Is my target smaller or bigger?" and go left or right. You eliminate half the remaining possibilities each time!

Now imagine a TREE (upside down, root at top):
```
        50
       /  \
     25    75
    / \    / \
  10  30  60  90
```

To find 60: 60 > 50 → go right. 60 < 75 → go left. Found 60! **Just 3 steps!**

---

## 📝 What Exactly Is a BST?

A **Binary Search Tree** is a tree where:
- Each node stores a **key** (a number or value)
- Each node has at most **two children** (left and right)
- The tree obeys the **BST Property**

### The BST Property — The ONE Rule That Makes Everything Work

> **For EVERY node x in the tree:**
> - Everything in x's **LEFT subtree** has keys **≤ x.key**
> - Everything in x's **RIGHT subtree** has keys **≥ x.key**

**IMPORTANT**: This rule applies to the ENTIRE subtree, not just the immediate children!

```
        15          ← root
       /  \
      6    18       ← 6 < 15 ✅, 18 > 15 ✅
     / \   / \
    3   7 17  20    ← ALL of these are < 15 (left side) or > 15 (right side) ✅
   / \   \
  2   4   13        ← 13 is in the LEFT subtree of 15, and indeed 13 < 15 ✅
```

### Why Is This Useful?

Because of this property, SEARCHING is super fast! At each node, you can eliminate an entire subtree:
- If target < node → the target CAN'T be in the right subtree → go left
- If target > node → the target CAN'T be in the left subtree → go right

---

## 📚 Terminology — Let's Make Sure We Speak the Same Language

| Term | What It Means | Picture |
|------|--------------|---------|
| **Node** | A "box" that stores a key and points to children | Each circle in the tree |
| **Root** | The topmost node (the "boss") | The one at the very top |
| **Leaf** | A node with NO children (the "end of the line") | Nodes at the very bottom |
| **Parent** | The node directly above | Your mom/dad in a family tree |
| **Child** | The node directly below | Your kids in a family tree |
| **Height** | Longest path from root to any leaf | "How tall is this tree?" |
| **Depth** | Distance from root to a specific node | "How far down is this node?" |
| **Subtree** | A node and ALL its descendants | A "mini tree" inside the big tree |
| **Left subtree** | Everything to the left of a node | All nodes with smaller keys |
| **Right subtree** | Everything to the right | All nodes with bigger keys |

---

## 📋 All BST Operations — Explained Simply

Here's everything a BST can do:

| Operation | What It Does | How Fast? | ELI5 |
|-----------|-------------|-----------|------|
| **SEARCH** | Find a node with a specific key | O(h) | "Where is number 13?" |
| **MINIMUM** | Find the smallest key | O(h) | "What's the smallest number?" |
| **MAXIMUM** | Find the largest key | O(h) | "What's the biggest number?" |
| **SUCCESSOR** | Find the next-larger key | O(h) | "What comes right after 13?" |
| **PREDECESSOR** | Find the next-smaller key | O(h) | "What comes right before 13?" |
| **INSERT** | Add a new key | O(h) | "Add number 5 to the tree" |
| **DELETE** | Remove a key | O(h) | "Remove number 13 from the tree" |
| **INORDER WALK** | Print all keys in sorted order | O(n) | "List everything from smallest to biggest" |

Where **h = height of the tree**. If balanced, h = O(log n). If skewed, h = O(n).

---

## 🔍 SEARCH — Finding a Key

### The Idea (Super Simple!)

Start at the root. At each node, ask: "Is this what I'm looking for?"
- **YES** → Found it! Return this node.
- **NO, target is SMALLER** → Go LEFT (smaller things are on the left).
- **NO, target is BIGGER** → Go RIGHT (bigger things are on the right).
- **Hit NIL (dead end)** → The key doesn't exist in the tree.

### Pseudocode

```
TREE-SEARCH(x, k)
1   if x == NIL or k == x.key     // Found it, or dead end
2       return x
3   if k < x.key                   // Target is smaller
4       return TREE-SEARCH(x.left, k)    // Go LEFT
5   else                            // Target is bigger
6       return TREE-SEARCH(x.right, k)   // Go RIGHT
```

### Iterative Version (No Recursion — More Efficient in Practice)

```
ITERATIVE-TREE-SEARCH(x, k)
1   while x ≠ NIL and k ≠ x.key
2       if k < x.key
3           x = x.left      // Go left
4       else
5           x = x.right     // Go right
6   return x                 // Either found it or x is NIL
```

### Walkthrough: Search for 13 in this tree

```
        15
       /  \
      6    18
     / \   / \
    3   7 17  20
   / \   \
  2   4   13
         /
        9
```

```
Step 1: Start at root (15). Is 13 == 15? No. Is 13 < 15? YES → go LEFT.
Step 2: At node 6. Is 13 == 6? No. Is 13 < 6? No, 13 > 6 → go RIGHT.
Step 3: At node 7. Is 13 == 7? No. Is 13 < 7? No, 13 > 7 → go RIGHT.
Step 4: At node 13. Is 13 == 13? YES! → FOUND! Return this node.

Total: 4 comparisons (4 nodes visited).
```

### Walkthrough: Search for 10 (NOT in the tree)

```
Step 1: At 15. 10 < 15 → go LEFT.
Step 2: At 6. 10 > 6 → go RIGHT.
Step 3: At 7. 10 > 7 → go RIGHT.
Step 4: At 13. 10 < 13 → go LEFT.
Step 5: At 9. 10 > 9 → go RIGHT.
Step 6: Right child of 9 is NIL → NOT FOUND. Return NIL.
```

---

## ⬇️ MINIMUM and MAXIMUM

### MINIMUM: Go ALL the way LEFT

The smallest key in a BST is always at the leftmost node. Why? Because every left child is smaller than its parent. So the leftmost node has no one smaller — it's the minimum!

```
TREE-MINIMUM(x)
1   while x.left ≠ NIL
2       x = x.left          // Keep going left!
3   return x
```

**In the tree above**: 15 → 6 → 3 → 2 → (2.left is NIL) → **Minimum = 2** ✅

### MAXIMUM: Go ALL the way RIGHT

Same idea, but go right instead.

```
TREE-MAXIMUM(x)
1   while x.right ≠ NIL
2       x = x.right         // Keep going right!
3   return x
```

**In the tree above**: 15 → 18 → 20 → (20.right is NIL) → **Maximum = 20** ✅

---

## ➡️ SUCCESSOR — "What Comes Next?"

The **successor** of node x is the node with the **smallest key that's bigger than x.key**. In other words, if you listed all keys in sorted order, the successor is the one RIGHT AFTER x.

### There Are Two Cases

**Case 1: x HAS a right subtree.**
Then the successor is the MINIMUM of x's right subtree. (Go right once, then all the way left.)

Why? The right subtree contains everything bigger than x. The minimum of that subtree is the SMALLEST of the bigger things — that's the successor!

**Case 2: x has NO right subtree.**
Then the successor is the LOWEST ANCESTOR of x whose LEFT child is also an ancestor of x. (Walk up until you "turn left.")

Why? If there's nothing bigger below x, the next bigger thing must be somewhere above. You walk up until you find an ancestor that you're in the LEFT subtree of — that ancestor is bigger than x and is the successor.

### Pseudocode

```
TREE-SUCCESSOR(x)
1   if x.right ≠ NIL
2       return TREE-MINIMUM(x.right)    // Case 1
3   y = x.parent
4   while y ≠ NIL and x == y.right     // Walk up while we're a right child
5       x = y
6       y = y.parent
7   return y                             // Case 2
```

### Example: Successor of 7

```
        15
       /  \
      6    18
     / \   / \
    3   7 17  20
       \
        13
       /
      9
```

Node 7 HAS a right child (13). So:
Successor = MINIMUM(right subtree of 7) = MINIMUM(subtree rooted at 13) = **9** ✅

Verification: Sorted order is [2, 3, 4, 6, 7, **9**, 13, 15, 17, 18, 20]. After 7 comes 9. ✅

### Example: Successor of 4

Node 4 has NO right child. Walk up:
- 4 is the RIGHT child of 3 → keep going up
- 3 is the LEFT child of 6 → STOP! **Successor = 6** ✅

Sorted: [2, 3, 4, **6**, 7, ...]. After 4 comes 6. ✅

---

## ➕ INSERT — Adding a New Key

### The Idea

Walk down the tree like you're SEARCHING for the key. When you fall off the bottom (reach NIL), THAT'S where the new node goes!

### Pseudocode

```
TREE-INSERT(T, z)
1   x = T.root          // Start at the root
2   y = NIL             // y trails one step behind x (will be z's parent)
3   while x ≠ NIL       // Walk down the tree
4       y = x
5       if z.key < x.key
6           x = x.left
7       else
8           x = x.right
9   z.parent = y         // Link z to its parent
10  if y == NIL
11      T.root = z       // Tree was empty — z becomes root
12  else if z.key < y.key
13      y.left = z       // z goes on the left
14  else
15      y.right = z      // z goes on the right
```

### Walkthrough: Insert 5

```
Before:                After:
    15                    15
   /  \                  /  \
  6    18               6    18
 / \                   / \
3   7                 3   7
 \                     \
  4                     4
                         \
                          5  ← NEW!
```

Path: 15 → 6 (5<15, go left) → 3 (5>6? No, 5<6, go left? No, 5>3, go right) → Wait, let me redo:
- At 15: 5 < 15 → go left
- At 6: 5 < 6 → go left
- At 3: 5 > 3 → go right
- At 4: 5 > 4 → go right
- Right of 4 is NIL → **INSERT 5 as right child of 4** ✅

---

## ❌ DELETE — The Trickiest Operation

Deleting a node is the hardest BST operation because we have to handle THREE different cases. Let me explain each one very carefully.

### Case 1: Node Has NO Children (It's a Leaf)

This is the easiest. Just remove it! Set the parent's pointer to NIL.

```
Delete 2:
Before:      After:
    5            5
   / \          / \
  3   7        3   7
 /
2  ← delete
```

Just snip it off. Nobody depends on it.

### Case 2: Node Has ONE Child

Replace the node with its one child. The child takes the node's place.

```
Delete 3 (which has only left child 2):
Before:      After:
    5            5
   / \          / \
  3   7        2   7
 /
2
```

Node 3 is removed, and its child (2) takes its place.

### Case 3: Node Has TWO Children — The Hard One!

You can't just remove a node with two children without breaking the tree. Instead:

1. Find the node's **successor** (the smallest node in its right subtree).
2. **Replace** the node's key with the successor's key.
3. **Delete** the successor (which has at most ONE child — its right child).

Why the successor? Because the successor is the NEXT key in sorted order. Putting it where the deleted node was preserves the BST property!

```
Delete 15 (which has children 6 and 18):

Step 1: Successor of 15 = MINIMUM(right subtree) = 17

Step 2: Replace 15's key with 17

Step 3: Delete original node 17 (which has no children — easy!)

Before:           After:
    15                17
   /  \              /  \
  6    18           6    18
      / \                  \
     17  20               20
```

### Helper Function: TRANSPLANT

This helper replaces one subtree with another:

```
TRANSPLANT(T, u, v)    // Replace subtree u with subtree v
1   if u.parent == NIL
2       T.root = v              // u was the root
3   else if u == u.parent.left
4       u.parent.left = v       // u was a left child
5   else
6       u.parent.right = v      // u was a right child
7   if v ≠ NIL
8       v.parent = u.parent     // Update v's parent pointer
```

### Complete DELETE Pseudocode

```
TREE-DELETE(T, z)
1   if z.left == NIL                    // Case 1 or 2: no left child
2       TRANSPLANT(T, z, z.right)
3   else if z.right == NIL              // Case 2: no right child
4       TRANSPLANT(T, z, z.left)
5   else                                 // Case 3: two children
6       y = TREE-MINIMUM(z.right)       // Find successor
7       if y ≠ z.right                  // Successor isn't immediate right child
8           TRANSPLANT(T, y, y.right)   // Detach successor
9           y.right = z.right           // Give successor z's right subtree
10          y.right.parent = y
11      TRANSPLANT(T, z, y)             // Replace z with successor
12      y.left = z.left                 // Give successor z's left subtree
13      y.left.parent = y
```

---

## 📋 INORDER TRAVERSAL — Print Everything Sorted

**Inorder** = visit LEFT subtree, then ROOT, then RIGHT subtree.

```
INORDER-TREE-WALK(x)
1   if x ≠ NIL
2       INORDER-TREE-WALK(x.left)      // Visit left subtree
3       print x.key                      // Print this node
4       INORDER-TREE-WALK(x.right)     // Visit right subtree
```

**Why does this give sorted output?** Because:
- Left subtree has all smaller keys → printed first (in order)
- Then this node → printed in the middle
- Right subtree has all bigger keys → printed last (in order)

```
        15
       /  \
      6    18
     / \   / \
    3   7 17  20

Inorder: 3, 6, 7, 15, 17, 18, 20  ← SORTED! ✅
```

---

## ⏱️ Time Complexity — It All Depends on Height!

EVERY BST operation takes **O(h)** time where h = height of the tree.

### The Big Question: What Is h?

| Tree Shape | Height h | When It Happens |
|-----------|----------|----------------|
| **Balanced** | O(log n) | Random insertion order |
| **Perfectly balanced** | ⌊log₂ n⌋ | Best possible |
| **Skewed (stick)** | n - 1 | Sorted insertion order |

### The Balanced Case (Best) — h = O(log n)

If the tree looks like a nice triangle (roughly balanced), you eliminate about half the nodes at each level. So finding anything takes about log₂(n) steps.

For n = 1,000,000 nodes → h ≈ 20 steps. That's FAST!

### The Skewed Case (Worst) — h = O(n)

If you insert elements in sorted order (1, 2, 3, 4, 5...), the tree becomes a straight line (linked list):

```
1
 \
  2
   \
    3
     \
      4
       \
        5
```

Now h = n - 1 = 4, and searching takes O(n) = O(5) steps. That's no better than a list!

**THIS IS THE PROBLEM THAT RED-BLACK TREES SOLVE** — they keep the tree balanced automatically!

---

## 🐍 Python Implementation — Every Line Commented

```python
class Node:
    """A single node in the BST."""
    def __init__(self, key):
        self.key = key          # The value stored
        self.left = None        # Left child (smaller keys)
        self.right = None       # Right child (bigger keys)
        self.parent = None      # Parent node


class BST:
    """Binary Search Tree with all standard operations."""

    def __init__(self):
        self.root = None        # Empty tree has no root

    # ===== SEARCH =====
    def search(self, key):
        """Find a node by key. Returns the node or None."""
        x = self.root
        while x is not None and key != x.key:
            if key < x.key:
                x = x.left     # Target is smaller → go left
            else:
                x = x.right    # Target is bigger → go right
        return x                # Either found it, or None (not found)

    # ===== MINIMUM =====
    def minimum(self, x=None):
        """Find the node with the smallest key."""
        if x is None:
            x = self.root
        while x.left is not None:
            x = x.left         # Keep going left!
        return x

    # ===== MAXIMUM =====
    def maximum(self, x=None):
        """Find the node with the largest key."""
        if x is None:
            x = self.root
        while x.right is not None:
            x = x.right        # Keep going right!
        return x

    # ===== SUCCESSOR =====
    def successor(self, x):
        """Find the next-larger node after x."""
        if x.right is not None:
            return self.minimum(x.right)   # Case 1: min of right subtree
        # Case 2: walk up until we turn left
        y = x.parent
        while y is not None and x == y.right:
            x = y
            y = y.parent
        return y

    # ===== INSERT =====
    def insert(self, key):
        """Insert a new key into the BST."""
        z = Node(key)
        y = None               # Will be z's parent
        x = self.root          # Start at root

        # Walk down to find where z belongs
        while x is not None:
            y = x              # Remember the parent
            if z.key < x.key:
                x = x.left
            else:
                x = x.right

        # Attach z to its parent
        z.parent = y
        if y is None:
            self.root = z      # Tree was empty
        elif z.key < y.key:
            y.left = z         # z is a left child
        else:
            y.right = z        # z is a right child

    # ===== TRANSPLANT (helper for delete) =====
    def _transplant(self, u, v):
        """Replace subtree rooted at u with subtree rooted at v."""
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

    # ===== DELETE =====
    def delete(self, z):
        """Delete node z from the BST."""
        if z.left is None:              # Case 1/2: no left child
            self._transplant(z, z.right)
        elif z.right is None:           # Case 2: no right child
            self._transplant(z, z.left)
        else:                            # Case 3: two children
            y = self.minimum(z.right)   # Find successor
            if y != z.right:            # Successor isn't immediate right child
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self._transplant(z, y)      # Replace z with successor
            y.left = z.left
            y.left.parent = y

    # ===== INORDER TRAVERSAL =====
    def inorder(self, x=None, first_call=True):
        """Print all keys in sorted order."""
        if first_call:
            x = self.root
        if x is not None:
            self.inorder(x.left, False)
            print(x.key, end=' ')
            self.inorder(x.right, False)


# ===== EXAMPLE =====
tree = BST()
for key in [15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9]:
    tree.insert(key)

print("Inorder traversal (should be sorted):")
tree.inorder()
# Output: 2 3 4 6 7 9 13 15 17 18 20

print(f"\nSearch for 13: {tree.search(13).key}")     # 13
print(f"Search for 99: {tree.search(99)}")           # None
print(f"Minimum: {tree.minimum().key}")               # 2
print(f"Maximum: {tree.maximum().key}")               # 20

node7 = tree.search(7)
print(f"Successor of 7: {tree.successor(node7).key}")  # 9

# Delete node 6 (has two children: 3 and 7)
node6 = tree.search(6)
tree.delete(node6)
print("After deleting 6:")
tree.inorder()
# Output: 2 3 4 7 9 13 15 17 18 20
```

---

## 🧰 Problem-Solving Techniques

### Technique 1: Always Draw the Tree
When solving BST problems, DRAW the tree on paper first. Insert elements one by one following the BST property.

### Technique 2: Inorder = Sorted
After building or modifying a BST, verify your work by doing an inorder traversal. If the output is sorted, your tree is correct.

### Technique 3: Deletion with Two Children
Remember the recipe: find SUCCESSOR (min of right subtree), copy its key over, delete the successor. The successor always has at most ONE child (its right child), making the final deletion easy.

### Technique 4: Height Determines Everything
For n nodes: best height = ⌊log₂ n⌋ (perfectly balanced), worst height = n-1 (stick). All operations are O(h).

---

## 📝 Practice Questions with Detailed Solutions

### Q1: Insert [10, 5, 15, 3, 7, 12, 18] into an empty BST. Draw the tree.

**Full Solution:**
```
Insert 10: root.       10

Insert 5: 5<10 → left.
         10
        /
       5

Insert 15: 15>10 → right.
         10
        /  \
       5    15

Insert 3: 3<10→left, 3<5→left.
         10
        /  \
       5    15
      /
     3

Insert 7: 7<10→left, 7>5→right.
         10
        /  \
       5    15
      / \
     3   7

Insert 12: 12>10→right, 12<15→left.
         10
        /  \
       5    15
      / \   /
     3   7 12

Insert 18: 18>10→right, 18>15→right.
         10
        /  \
       5    15
      / \   / \
     3   7 12  18

Final tree! ✅
```

### Q2: Find minimum, maximum, successor of 7, predecessor of 15 in the tree above.

**Full Solution:**
```
Minimum: go all the way left from root. 10→5→3→(nil). Min = 3 ✅
Maximum: go all the way right from root. 10→15→18→(nil). Max = 18 ✅

Successor of 7: 
  7 has no right child. Walk up: 7 is right child of 5. Keep going.
  5 is left child of 10. STOP. Successor = 10 ✅
  Verify sorted: [3, 5, 7, 10, 12, 15, 18]. After 7 comes 10 ✅

Predecessor of 15:
  15 has a left child (12). Max of left subtree = 12.
  Predecessor = 12 ✅
  Verify: [3, 5, 7, 10, 12, 15, 18]. Before 15 comes 12 ✅
```

### Q3: Delete node 5 from the tree above (it has TWO children: 3 and 7).

**Full Solution:**
```
Step 1: Find successor of 5. Min of right subtree of 5 = min of subtree rooted at 7 = 7.
Step 2: Replace 5's key with 7.
Step 3: Delete original node 7 (it's a leaf — easy! just remove it).

Before:          After:
    10               10
   /  \             /  \
  5    15          7    15
 / \   / \        /    / \
3   7 12  18     3    12  18

Verify inorder: 3, 7, 10, 12, 15, 18. Was: 3, 5, 7, 10, 12, 15, 18 minus 5. ✅
```

### Q4: What insertion order produces the TALLEST BST for keys {1,2,3,4,5,6,7}?

**Full Solution:**
Insert in sorted order: 1, 2, 3, 4, 5, 6, 7.
```
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
           \
            7

Height = 6 (worst possible for 7 nodes).
```
This creates a "right-leaning stick" — basically a linked list!

### Q5: What insertion order produces the SHORTEST BST for {1,2,3,4,5,6,7}?

**Full Solution:**
Insert the median first, then medians of halves: 4, 2, 6, 1, 3, 5, 7.
```
        4
       / \
      2   6
     / \ / \
    1  3 5  7

Height = 2 = ⌊log₂(7)⌋ (best possible for 7 nodes!)
```
This creates a perfectly balanced tree.

### Q6: How many different BSTs can store keys {1, 2, 3}?

**Full Solution:**
The number of structurally different BSTs with n keys = nth Catalan number = C₃ = 5.

```
 1           1         2         3       3
  \           \       / \       /       /
   2           3     1   3     1       2
    \         /                 \      /
     3       2                   2    1
```

These are all 5 valid BSTs.

### Q7: Prove inorder traversal of BST gives sorted output.

**Full Solution:**
By strong induction on tree size n.

Base case (n=0): Empty tree → empty output → sorted trivially ✅

Inductive step: Assume true for all trees with < n nodes.
For a BST with n nodes rooted at x:
- Inorder first visits the LEFT subtree. By induction, this outputs left subtree keys in sorted order. All these keys ≤ x.key (BST property).
- Then prints x.key.
- Then visits the RIGHT subtree. By induction, this outputs right subtree keys in sorted order. All these keys ≥ x.key.
- Since left keys ≤ x.key ≤ right keys, and each group is sorted, the ENTIRE output is sorted. ✅

### Q8: What is the time complexity of building a BST by inserting n elements?

**Full Solution:**
```
Best case (balanced): O(log 1 + log 2 + ... + log n) = O(n log n)
Worst case (sorted input): O(1 + 2 + ... + (n-1)) = O(n²/2) = O(n²)
Average case (random): O(n log n) (proven in CLRS using expected height of random BST)
```

### Q9: Search for 13 in the tree from Q1. How many nodes visited?

**Full Solution:**
```
At 10: 13 > 10 → go right. (1)
At 15: 13 < 15 → go left.  (2)
At 12: 13 > 12 → go right. (3)
12's right child is NIL → NOT FOUND. (3 nodes visited + 1 NIL check)
```
Wait — 13 was NOT in our tree from Q1! The keys were [10, 5, 15, 3, 7, 12, 18]. No 13.

So: 3 comparisons, result = NOT FOUND. ✅

### Q10: Can BSTs have duplicate keys? How do you handle them?

**Full Solution:**
Yes! You need a convention:
- **Option A**: Duplicates go to the RIGHT subtree (most common)
- **Option B**: Duplicates go to the LEFT subtree
- **Option C**: Each node stores a count of duplicates

With option A, inserting [5, 3, 5, 7, 5]:
```
    5
   / \
  3   5
       \
        7
       /
      5
```
Inorder: 3, 5, 5, 5, 7 ✅

The key is to be CONSISTENT — pick one convention and stick with it!

---

## 📋 Quick Revision Cheat Sheet

```
┌──────────────────────────────────────────────────────────────┐
│  BST — EVERYTHING IN ONE BOX                                 │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  THE ONE RULE:                                               │
│  Left subtree ≤ Node ≤ Right subtree (for EVERY node)        │
│                                                              │
│  ALL OPERATIONS: O(h) where h = tree height                  │
│  Balanced: h = O(log n)  |  Skewed: h = O(n)                 │
│                                                              │
│  SEARCH: go left if smaller, right if bigger                 │
│  MIN: go all the way left                                    │
│  MAX: go all the way right                                   │
│  SUCCESSOR: min of right subtree, OR walk up and turn left   │
│  INSERT: search for spot, attach at NIL                      │
│  DELETE: 0 kids = remove, 1 kid = replace, 2 kids = swap     │
│          with successor then delete successor                │
│  INORDER: left → root → right = SORTED output                │
│                                                              │
│  THE PROBLEM: sorted input → stick → O(n) per operation!     │
│  THE SOLUTION: Red-Black Trees (next topic!)                 │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

---

## 📚 References

- CLRS — Introduction to Algorithms, Chapter 12 (Binary Search Trees)
- Lectures 4, 5, 6 — Pr V Raj S, DSA
- [CLRS Solutions](https://walkccc.me/CLRS/Chap12/12.1/)
- [Visualgo BST](https://visualgo.net/en/bst)
