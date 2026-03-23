# ╔══════════════════════════════════════════════════════════════════╗
# ║  🌲 BINARY SEARCH TREE — Complete Code Tutorial (Colab Ready)    ║
# ╚══════════════════════════════════════════════════════════════════╝
#
# 🧒 THE STORY:
# Think of the "higher or lower" guessing game!
# Someone thinks of a number. You guess. They say "higher!" or "lower!"
# A BST works the same way: left = smaller, right = bigger.
#
# 🧠 MNEMONIC: "Left Less, Right moRe"

# ━━━ BUILDING BLOCK: What is a Node? ━━━
# A node is like a BOX with three compartments:
#   [left pointer | KEY (the number) | right pointer]
# left points to a smaller node, right to a bigger one.

class Node:
    def __init__(self, key):
        self.key = key          # The number stored here
        self.left = None        # Pointer to left child (smaller)
        self.right = None       # Pointer to right child (bigger)
        self.parent = None      # Pointer to parent (above)
    
    def __repr__(self):
        return f"Node({self.key})"


class BST:
    def __init__(self):
        self.root = None        # Empty tree = no root

    # ━━━ INSERT: Add a new number to the tree ━━━
    # ELI5: Walk down the tree asking "left or right?" until you
    #       fall off the bottom. THAT'S where the new node goes.
    def insert(self, key):
        new_node = Node(key)
        
        # If tree is empty, new node becomes the root
        if self.root is None:
            self.root = new_node
            print(f"  Inserted {key} as ROOT")
            return
        
        # Walk down to find the right spot
        current = self.root     # Start at the top
        parent = None           # Track the parent
        
        while current is not None:
            parent = current    # Remember parent before going down
            if key < current.key:
                print(f"  {key} < {current.key} → go LEFT")
                current = current.left
            else:
                print(f"  {key} ≥ {current.key} → go RIGHT")
                current = current.right
        
        # Attach the new node to its parent
        new_node.parent = parent
        if key < parent.key:
            parent.left = new_node
            print(f"  ✅ Inserted {key} as LEFT child of {parent.key}")
        else:
            parent.right = new_node
            print(f"  ✅ Inserted {key} as RIGHT child of {parent.key}")

    # ━━━ SEARCH: Find a number in the tree ━━━
    # ELI5: Start at root. "Is this it? No? Is my target smaller or bigger?"
    #       Go left if smaller, right if bigger. Repeat.
    def search(self, key):
        current = self.root
        steps = 0
        while current is not None and current.key != key:
            steps += 1
            if key < current.key:
                current = current.left      # Target is smaller → go left
            else:
                current = current.right     # Target is bigger → go right
        
        if current:
            print(f"  🔍 Found {key} in {steps + 1} steps!")
        else:
            print(f"  ❌ {key} NOT found after {steps} steps")
        return current

    # ━━━ MINIMUM: Smallest number = go all the way LEFT ━━━
    def minimum(self, node=None):
        if node is None: node = self.root
        while node.left is not None:
            node = node.left
        return node

    # ━━━ MAXIMUM: Biggest number = go all the way RIGHT ━━━
    def maximum(self, node=None):
        if node is None: node = self.root
        while node.right is not None:
            node = node.right
        return node

    # ━━━ SUCCESSOR: Next bigger number ━━━
    # ELI5: Two cases:
    #   Case 1: Has right child? → Minimum of right subtree
    #   Case 2: No right child? → Walk up until you "turn left"
    def successor(self, node):
        if node.right:
            return self.minimum(node.right)
        parent = node.parent
        while parent and node == parent.right:
            node = parent
            parent = parent.parent
        return parent

    # ━━━ INORDER: Print everything in sorted order ━━━
    # ELI5: Visit left subtree → print me → visit right subtree
    # This ALWAYS gives sorted output because left < root < right!
    def inorder(self, node=None, first=True):
        if first: node = self.root
        if node:
            self.inorder(node.left, False)    # Left first (smaller)
            print(node.key, end=' ')           # Then me
            self.inorder(node.right, False)   # Then right (bigger)

    # ━━━ VISUAL PRINT: See the tree structure ━━━
    def print_tree(self, node=None, prefix="", is_left=True, first=True):
        if first: node = self.root
        if node:
            self.print_tree(node.right, prefix + ("│   " if is_left else "    "), False, False)
            print(prefix + ("└── " if is_left else "┌── ") + str(node.key))
            self.print_tree(node.left, prefix + ("    " if is_left else "│   "), True, False)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# LET'S BUILD A TREE AND TEST EVERYTHING!
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
print("=" * 60)
print("  BUILDING A BST")
print("=" * 60)
tree = BST()
for key in [15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9]:
    tree.insert(key)
    print()

print("\n📊 Tree structure:")
tree.print_tree()

print("\n📋 Inorder traversal (should be SORTED!):")
tree.inorder()
print()

print(f"\n🔽 Minimum: {tree.minimum().key}")
print(f"🔼 Maximum: {tree.maximum().key}")

print(f"\n🔍 Searching for 13:")
tree.search(13)

print(f"\n🔍 Searching for 99:")
tree.search(99)

node7 = tree.search(7)
succ = tree.successor(node7)
print(f"\n➡️  Successor of 7: {succ.key if succ else 'None'}")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CHEAT SHEET
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
print("""
╔══════════════════════════════════════════════════════╗
║  BST CHEAT SHEET                                     ║
╠══════════════════════════════════════════════════════╣
║  PROPERTY: left < node ≤ right (for EVERY node)      ║
║                                                      ║
║  SEARCH:    go left if smaller, right if bigger      ║
║  MIN:       go all the way LEFT                      ║
║  MAX:       go all the way RIGHT                     ║
║  SUCCESSOR: min of right subtree, OR walk up         ║
║  INSERT:    search for spot → attach at NIL          ║
║  INORDER:   left → root → right = SORTED!            ║
║                                                      ║
║  TIME: O(h)  Balanced h=O(log n), Worst h=O(n)       ║
║  MNEMONIC: "Left Less, Right moRe"                   ║
║                                                      ║
║  WORST CASE: inserting sorted data → becomes stick!  ║
║  FIX: Use Red-Black Trees (auto-balance)             ║
╚══════════════════════════════════════════════════════╝
""")
