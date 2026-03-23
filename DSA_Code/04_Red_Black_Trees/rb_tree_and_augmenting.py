# ╔══════════════════════════════════════════════════════════╗
# ║  🔴⚫ RED-BLACK TREE — Simplified Code (Colab Ready)    ║
# ╚══════════════════════════════════════════════════════════╝
# STORY: A BST that paints nodes red/black to stay balanced.
#        Insert as RED, fix violations with recolor + rotate.
# MNEMONIC: "Insert RED → Uncle RED? Recolor! Uncle BLACK? Rotate!"
# NOTE: RB-Trees are complex. Focus on understanding INSERT fixup cases.
#       The full delete code is in the README for reference.

class RBNode:
    def __init__(self, key, color='RED'):
        self.key = key
        self.color = color  # 'RED' or 'BLACK'
        self.left = self.right = self.parent = None
    def __repr__(self):
        c = 'R' if self.color == 'RED' else 'B'
        return f"{self.key}({c})"

class RedBlackTree:
    def __init__(self):
        self.NIL = RBNode(None, 'BLACK')
        self.root = self.NIL

    def left_rotate(self, x):
        y = x.right; x.right = y.left
        if y.left != self.NIL: y.left.parent = x
        y.parent = x.parent
        if x.parent == self.NIL: self.root = y
        elif x == x.parent.left: x.parent.left = y
        else: x.parent.right = y
        y.left = x; x.parent = y

    def right_rotate(self, y):
        x = y.left; y.left = x.right
        if x.right != self.NIL: x.right.parent = y
        x.parent = y.parent
        if y.parent == self.NIL: self.root = x
        elif y == y.parent.left: y.parent.left = x
        else: y.parent.right = x
        x.right = y; y.parent = x

    def insert(self, key):
        z = RBNode(key); z.left = z.right = self.NIL
        y = self.NIL; x = self.root
        while x != self.NIL:
            y = x
            x = x.left if z.key < x.key else x.right
        z.parent = y
        if y == self.NIL: self.root = z
        elif z.key < y.key: y.left = z
        else: y.right = z
        z.color = 'RED'
        self._fix_insert(z)
        print(f"  Inserted {key}. Inorder: ", end=""); self.inorder(); print()

    def _fix_insert(self, z):
        """
        FIX INSERT VIOLATIONS:
        While z's parent is RED (red-red violation):
          Look at z's UNCLE (parent's sibling)
          
          Case 1: Uncle RED    → Recolor parent+uncle BLACK, grandparent RED. Move up.
          Case 2: Uncle BLACK, z is inner child → Rotate to straighten → Case 3
          Case 3: Uncle BLACK, z is outer child → Rotate grandparent + recolor. DONE!
        
        MNEMONIC for cases:
          Uncle Red?  "Everyone swap shirts, check grandpa" (Case 1)
          Uncle Black, zig-zag? "Straighten the line" (Case 2 → 3)
          Uncle Black, straight? "Spin grandpa, swap shirts, done!" (Case 3)
        """
        while z.parent.color == 'RED':
            if z.parent == z.parent.parent.left:
                uncle = z.parent.parent.right
                if uncle.color == 'RED':             # CASE 1
                    z.parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    z = z.parent.parent
                else:
                    if z == z.parent.right:           # CASE 2
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = 'BLACK'          # CASE 3
                    z.parent.parent.color = 'RED'
                    self.right_rotate(z.parent.parent)
            else:  # Mirror
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
        self.root.color = 'BLACK'

    def inorder(self, x=None, first=True):
        if first: x = self.root
        if x != self.NIL:
            self.inorder(x.left, False)
            c = 'R' if x.color=='RED' else 'B'
            print(f"{x.key}({c})", end=' ')
            self.inorder(x.right, False)

print("="*50)
print("  RED-BLACK TREE — Insert Demo")
print("="*50)
rbt = RedBlackTree()
for k in [7, 3, 18, 10, 22, 8, 11, 26]:
    rbt.insert(k)


# ╔══════════════════════════════════════════════════════════╗
# ║  🔧 AUGMENTING TREES (Order-Statistic Tree)            ║
# ╚══════════════════════════════════════════════════════════╝
# STORY: Add a SIZE badge to each node. Now you can ask
#        "Who is the 5th smallest?" in O(log n)!
# MNEMONIC: "OS-SELECT: Compare i with left.size+1"

class OSNode:
    def __init__(self, key):
        self.key = key; self.size = 1
        self.left = self.right = self.parent = None

class OrderStatisticTree:
    def __init__(self):
        self.NIL = OSNode(None); self.NIL.size = 0
        self.root = self.NIL

    def insert(self, key):
        z = OSNode(key); z.left = z.right = self.NIL
        y = self.NIL; x = self.root
        while x != self.NIL:
            x.size += 1
            y = x
            x = x.left if z.key < x.key else x.right
        z.parent = y
        if y == self.NIL: self.root = z
        elif z.key < y.key: y.left = z
        else: y.right = z

    def select(self, x, i):
        """Find the i-th smallest element."""
        r = x.left.size + 1
        if i == r: return x
        elif i < r: return self.select(x.left, i)
        else: return self.select(x.right, i - r)

    def rank(self, x):
        """Find the rank of node x."""
        r = x.left.size + 1
        y = x
        while y != self.root:
            if y == y.parent.right:
                r += y.parent.left.size + 1
            y = y.parent
        return r

print("\n" + "="*50)
print("  ORDER-STATISTIC TREE — Select & Rank Demo")
print("="*50)
ost = OrderStatisticTree()
keys = [26, 17, 41, 14, 21, 47, 10]
for k in keys: ost.insert(k)
print(f"  Keys inserted: {keys}")
print(f"  Sorted: {sorted(keys)}")
for i in range(1, len(keys)+1):
    node = ost.select(ost.root, i)
    print(f"  {i}th smallest = {node.key} (rank = {ost.rank(node)})")

print("""
╔══════════════════════════════════════════════════╗
║  RB-TREE + AUGMENTING CHEAT SHEET                ║
╠══════════════════════════════════════════════════╣
║  RB-TREE: Insert RED, fix with Cases 1/2/3       ║
║    Case 1: Uncle RED → recolor, move up          ║
║    Case 2: Uncle BLACK, inner → rotate → Case 3  ║
║    Case 3: Uncle BLACK, outer → rotate → DONE    ║
║    Max 2 rotations per insert!                   ║
║                                                  ║
║  OS-TREE: x.size = left.size + right.size + 1    ║
║    SELECT(x,i): r=left.size+1                    ║
║      i==r→found, i<r→left, i>r→right with i-r    ║
║    RANK(x): walk up, add left.size+1 from right  ║
╚══════════════════════════════════════════════════╝
""")
