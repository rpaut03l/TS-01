# ╔══════════════════════════════════════════════════════════════════╗
# ║  🤝 DISJOINT-SET UNION (Union-Find) — Colab Ready                ║
# ╚══════════════════════════════════════════════════════════════════╝
#
# 🧒 THE STORY:
# First day of school. Everyone is alone. Then friendships form:
# "Alice and Bob are friends!" → Merge their groups.
# "Are Charlie and Dana in the same group?" → Check leaders.
#
# TWO MAGIC TRICKS:
# 1. Union by Rank: smaller group joins bigger (keeps tree short)
# 2. Path Compression: everyone shortcuts to leader (next time = instant!)
#
# 🧠 MNEMONIC: "Find your leader, Unite your teams"

class DSU:
    """
    Disjoint-Set Union with Union by Rank + Path Compression.
    
    WHAT THE VARIABLES MEAN:
    - parent[i] = who is i's boss? (if parent[i] == i, then i IS the boss)
    - rank[i]   = how tall is i's tree? (used to keep things balanced)
    """
    
    def __init__(self, n):
        # Everyone starts as their own boss
        # parent = [0, 1, 2, 3, 4] means: 0's boss is 0, 1's boss is 1, etc.
        self.parent = list(range(n))
        
        # Everyone starts with rank 0 (just one person = shortest tree)
        self.rank = [0] * n
        
        print(f"Created {n} groups: each person is their own boss")
        print(f"  parent = {self.parent}")
    
    def find(self, x):
        """
        WHO IS x's BOSS? Follow the chain of parents to the TOP.
        
        TRICK: Path Compression — while walking up, make everyone
        point DIRECTLY to the boss. Next time = 1 step!
        
        HOW TO READ THIS CODE:
        
        if self.parent[x] != x:
            → "Is x its own boss? No? Then keep looking..."
            
        self.parent[x] = self.find(self.parent[x])
            → "Ask x's parent who the REAL boss is" (recursion!)
            → "Then make x point directly to that boss" (compression!)
            
        return self.parent[x]
            → "Return the boss"
        """
        if self.parent[x] != x:    # x is NOT the boss
            self.parent[x] = self.find(self.parent[x])  # Find boss + compress!
        return self.parent[x]
    
    def union(self, x, y):
        """
        MERGE the groups of x and y.
        
        TRICK: Union by Rank — shorter tree goes UNDER taller tree.
        This keeps the overall tree short!
        
        HOW TO READ THIS CODE:
        
        rx, ry = self.find(x), self.find(y)
            → "Find x's boss and y's boss"
            
        if rx == ry: return False
            → "Same boss? Already in the same group! Nothing to do."
            
        if self.rank[rx] < self.rank[ry]: rx, ry = ry, rx
            → "Make sure rx is the BIGGER boss (swap if needed)"
            
        self.parent[ry] = rx
            → "Smaller boss (ry) now reports to bigger boss (rx)"
            
        if self.rank[rx] == self.rank[ry]: self.rank[rx] += 1
            → "If they were equal height, the new tree is 1 taller"
        """
        rx = self.find(x)    # Find x's boss
        ry = self.find(y)    # Find y's boss
        
        if rx == ry:
            print(f"  UNION({x},{y}): already same group (boss={rx})")
            return False
        
        # Union by rank: smaller under bigger
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx   # Swap so rx is always the bigger one
        
        self.parent[ry] = rx  # ry's group now joins rx's group
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        
        print(f"  UNION({x},{y}): merged! boss of {ry}→{rx}. parent={self.parent}")
        return True
    
    def connected(self, x, y):
        """Are x and y in the same group?"""
        result = self.find(x) == self.find(y)
        print(f"  CONNECTED({x},{y})? → {result}")
        return result


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# LET'S TEST IT!
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
print("=" * 60)
print("  DSU — Step by Step Demo")
print("=" * 60)

dsu = DSU(8)  # 8 people: 0,1,2,3,4,5,6,7

print("\n--- Making friendships ---")
dsu.union(0, 1)   # 0 and 1 are friends
dsu.union(2, 3)   # 2 and 3 are friends
dsu.union(0, 2)   # Now {0,1} and {2,3} merge → {0,1,2,3}

dsu.union(4, 5)   # 4 and 5 are friends
dsu.union(6, 7)   # 6 and 7 are friends
dsu.union(4, 6)   # {4,5} and {6,7} merge → {4,5,6,7}

print("\n--- Checking connections ---")
dsu.connected(0, 3)   # True (both in group {0,1,2,3})
dsu.connected(0, 4)   # False (different groups!)

print("\n--- Merging the two big groups ---")
dsu.union(0, 4)        # Now EVERYONE is in one group!

print("\n--- Check again ---")
dsu.connected(1, 7)    # True! Everyone connected now!


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# APPLICATION: Cycle Detection in Graphs
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def has_cycle(n, edges):
    """Check if adding edges creates a cycle."""
    dsu = DSU(n)
    for u, v in edges:
        if dsu.connected(u, v):
            print(f"  ⚠️ CYCLE: edge ({u},{v}) — they're already connected!")
            return True
        dsu.union(u, v)
    print("  ✅ No cycle found")
    return False

print("\n" + "=" * 60)
print("  CYCLE DETECTION")
print("=" * 60)
has_cycle(4, [(0,1), (1,2), (2,3), (3,0)])  # Has cycle: 0-1-2-3-0


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# APPLICATION: Kruskal's MST
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def kruskal_mst(n, edges):
    """Find Minimum Spanning Tree using DSU."""
    edges.sort(key=lambda e: e[2])   # Sort by weight
    dsu = DSU(n)
    mst = []
    total_weight = 0
    
    for u, v, w in edges:
        if not dsu.connected(u, v):  # Different groups?
            dsu.union(u, v)           # Merge!
            mst.append((u, v, w))
            total_weight += w
    
    print(f"\n  MST edges: {mst}")
    print(f"  Total weight: {total_weight}")
    return mst

print("\n" + "=" * 60)
print("  KRUSKAL'S MST")
print("=" * 60)
kruskal_mst(4, [(0,1,1), (1,2,4), (0,2,3), (2,3,2), (1,3,5)])


print("""
╔══════════════════════════════════════════════════════╗
║  DSU CHEAT SHEET                                     ║
╠══════════════════════════════════════════════════════╣
║  parent[i] = i's boss. rank[i] = tree height bound.  ║
║                                                      ║
║  FIND: follow parents to root + compress path        ║
║  UNION: find both roots, smaller under bigger        ║
║  TIME: O(α(n)) ≈ O(1) per operation!                 ║
║                                                      ║
║  USES: Cycle detection, Kruskal's MST,               ║
║        Connected components, Network connectivity    ║
╚══════════════════════════════════════════════════════╝
""")
