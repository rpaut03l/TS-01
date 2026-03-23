# ╔══════════════════════════════════════════════════════════════════╗
# ║  🔧 AUGMENTING TREES — Order-Statistic Tree (Colab Ready)        ║
# ╚══════════════════════════════════════════════════════════════════╝
#
# 🧒 THE STORY:
# 30 kids in line sorted by height. Teacher asks "Who is 5th shortest?"
# WITHOUT badge: count 1..2..3..4..5 — slow!
# WITH SIZE BADGE: jump directly to answer — fast!
#
# SIZE badge: "How many kids in my group (subtree), including me?"
# This gives OS-SELECT (find i-th smallest) and OS-RANK (find position).
#
# 🧠 MNEMONICS:
#   SIZE:   "left.size + right.size + 1 = my.size"
#   SELECT: "Compare i with left+1. Match? Left? Right-minus?"
#   RANK:   "Start left+1. Walk up. From right? Add left+1"

class OSNode:
    def __init__(self, key):
        self.key = key
        self.size = 1
        self.left = self.right = self.parent = None
    def __repr__(self):
        return f"({self.key}, s={self.size})"

class OrderStatisticTree:
    def __init__(self):
        self.NIL = OSNode(None); self.NIL.size = 0
        self.root = self.NIL

    def insert(self, key):
        z = OSNode(key); z.left = z.right = self.NIL
        y = self.NIL; x = self.root
        while x != self.NIL:
            x.size += 1           # Every ancestor gets +1
            y = x
            x = x.left if z.key < x.key else x.right
        z.parent = y
        if y == self.NIL: self.root = z
        elif z.key < y.key: y.left = z
        else: y.right = z

    def os_select(self, x, i):
        """Find i-th smallest. r=left.size+1. Match? Left? Right with i-r?"""
        r = x.left.size + 1
        if i == r: return x
        elif i < r: return self.os_select(x.left, i)
        else: return self.os_select(x.right, i - r)

    def os_rank(self, x):
        """Find rank of node x. Walk up, add left.size+1 when coming from right."""
        r = x.left.size + 1
        y = x
        while y != self.root:
            if y == y.parent.right:
                r += y.parent.left.size + 1
            y = y.parent
        return r

    def search(self, key):
        x = self.root
        while x != self.NIL and x.key != key:
            x = x.left if key < x.key else x.right
        return x if x != self.NIL else None

    def inorder(self, node=None, first=True):
        if first: node = self.root
        result = []
        if node != self.NIL:
            result.extend(self.inorder(node.left, False))
            result.append(node.key)
            result.extend(self.inorder(node.right, False))
        return result

    def print_tree(self, node=None, prefix="", is_left=True, first=True):
        if first: node = self.root
        if node != self.NIL:
            self.print_tree(node.right, prefix + ("│   " if is_left else "    "), False, False)
            print(prefix + ("└── " if is_left else "┌── ") + f"{node.key}(s={node.size})")
            self.print_tree(node.left, prefix + ("    " if is_left else "│   "), True, False)


# ━━━ DEMO ━━━
print("=" * 60)
print("  ORDER-STATISTIC TREE — Complete Demo")
print("=" * 60)

ost = OrderStatisticTree()
keys = [26, 17, 41, 14, 21, 47, 10]
for k in keys: ost.insert(k)
sorted_keys = ost.inorder()

print(f"\n  Keys: {keys}")
print(f"  Sorted: {sorted_keys}")
print(f"\n  Tree:")
ost.print_tree()

print(f"\n  OS-SELECT tests:")
for i in range(1, len(keys)+1):
    node = ost.os_select(ost.root, i)
    print(f"    {i}th smallest = {node.key}")

print(f"\n  OS-RANK tests:")
for key in sorted_keys:
    node = ost.search(key)
    print(f"    RANK({key}) = {ost.os_rank(node)}")

print("""
╔════════════════════════════════════════════════════╗
║  AUGMENTING TREES CHEAT SHEET                      ║
╠════════════════════════════════════════════════════╣
║  x.size = left.size + right.size + 1               ║
║  SELECT: r=left.size+1. i==r? i<r→left. i>r→right  ║
║  RANK: r=left.size+1. Walk up. Right? Add left+1   ║
║  TIME: O(log n) for both. Rotation update: O(1)    ║
╚════════════════════════════════════════════════════╝
""")
