# 💑 Bipartite Maximum Matching — Crystal Clear Complete Guide

> **One-Liner**: Pair students with projects so the MAXIMUM number of pairs are formed — solved by turning it into a water-pipe (max-flow) problem!

---

## 🧒 ELI5 — Explain Like I'm 5

**It's project day at school!** 4 students need to pick projects. Each student has preferences:

```
Alice likes:   Project 1 and Project 3
Bob likes:     Project 2
Charlie likes: Project 1 and Project 2
Dana likes:    Project 3 and Project 4
```

**Rules**: Each student gets EXACTLY one project. Each project is assigned to AT MOST one student.

**Question**: What's the MAXIMUM number of students we can assign?

The clever trick: **Build a water-pipe network!** Add a "super tap" (source) connected to all students, and a "super drain" (sink) connected to all projects. Each pipe has capacity 1. The maximum water flow = maximum number of matched pairs!

**Result**: Alice→P3, Bob→P2, Charlie→P1, Dana→P4. **All 4 matched!** 🎉

---

## 📝 What Is a Bipartite Graph?

A **bipartite graph** splits its vertices into TWO groups (L and R). Every edge connects a vertex in L to a vertex in R. **No edges within the same group.**

```
LEFT (students)     RIGHT (projects)
   Alice ─────────── P1
   Alice ─────────── P3
   Bob ───────────── P2
   Charlie ────────── P1
   Charlie ────────── P2
   Dana ──────────── P3
   Dana ──────────── P4
```

**How to check if a graph is bipartite?** BFS 2-coloring: try to color vertices with 2 colors so no adjacent vertices share a color. If possible → bipartite. If impossible → NOT bipartite (must have an odd cycle).

---

## 🤝 What Is a Matching?

A **matching** = a set of edges where **no vertex appears more than once**. Every vertex is in at most ONE pair.

- **Maximum matching**: The matching with the MOST edges possible.
- **Perfect matching**: EVERY vertex is matched (only possible if |L| = |R| and graph allows it).

---

## 🔄 The Reduction: Matching → Max Flow

This is the BRILLIANT insight! We transform the matching problem into a max-flow problem:

```
CONSTRUCTION:
1. Create a super-source s
2. Add edge s → every LEFT vertex (capacity 1)
3. Direct all original edges: LEFT → RIGHT (capacity 1)
4. Add edge every RIGHT vertex → super-sink t (capacity 1)
5. Run Ford-Fulkerson / Edmonds-Karp
6. Max flow = max matching size!
7. Edges from L to R with flow = 1 are the matched pairs!
```

### Why Capacity 1?

- s→student has cap 1 → each student gets at most ONE project
- project→t has cap 1 → each project gets at most ONE student
- student→project has cap 1 → each pair is either matched (1) or not (0)

---

## 🎨 Complete Walkthrough

```
Students: Alice→{P1,P3}, Bob→{P2}, Charlie→{P1,P2}, Dana→{P3,P4}

Flow network:
s →(1)→ Alice →(1)→ P1 →(1)→ t
s →(1)→ Alice →(1)→ P3 →(1)→ t
s →(1)→ Bob   →(1)→ P2 →(1)→ t
s →(1)→ Charlie→(1)→ P1 →(1)→ t
s →(1)→ Charlie→(1)→ P2 →(1)→ t
s →(1)→ Dana  →(1)→ P3 →(1)→ t
s →(1)→ Dana  →(1)→ P4 →(1)→ t

RUNNING FORD-FULKERSON:

Path 1: s → Alice → P1 → t. Push 1. Match: Alice↔P1. Total flow = 1.
Path 2: s → Bob → P2 → t. Push 1. Match: Bob↔P2. Total flow = 2.
Path 3: s → Charlie → P1 → t? P1→t is FULL (already 1)!
         s → Charlie → P2 → t? P2→t is FULL!
         
         USE RESIDUAL NETWORK:
         s → Charlie → P1 → (BACKWARD to Alice) → Alice → P3 → t
         
         This means: "Unmatch Alice from P1. Match Charlie to P1 instead.
                       Give Alice her second choice P3."
         
         Push 1. Total flow = 3.
         New matches: Charlie↔P1, Alice↔P3, Bob↔P2.

Path 4: s → Dana → P4 → t. Push 1. Match: Dana↔P4. Total flow = 4.

No more paths! MAXIMUM MATCHING = 4 (perfect matching!)

Final matches:
  Alice   → Project 3
  Bob     → Project 2
  Charlie → Project 1
  Dana    → Project 4
```

**See how the backward edge helped?** Alice was initially matched to P1, but Charlie needed P1 more (no alternatives). The backward edge let the algorithm "reassign" Alice to P3, freeing P1 for Charlie. Everyone wins!

---

## 📜 Alternative: Direct Augmenting Path Method

Instead of building a full flow network, you can directly find **augmenting paths** in the matching:

```python
def max_bipartite_matching(left, right, edges):
    """Find maximum matching using augmenting paths."""
    adj = {u: [] for u in left}
    for u, v in edges:
        adj[u].append(v)
    
    match_r = {v: None for v in right}  # Which left vertex is matched to each right vertex?
    
    def try_match(u, visited):
        """Try to find an augmenting path from unmatched left vertex u."""
        for v in adj[u]:
            if v not in visited:
                visited.add(v)
                # If v is free OR we can find an alternative for v's current match
                if match_r[v] is None or try_match(match_r[v], visited):
                    match_r[v] = u  # Match u ↔ v
                    return True
        return False
    
    count = 0
    for u in left:
        if try_match(u, set()):
            count += 1
    
    return count, {v: u for v, u in match_r.items() if u is not None}

# Example:
left = ['Alice', 'Bob', 'Charlie', 'Dana']
right = ['P1', 'P2', 'P3', 'P4']
edges = [('Alice','P1'),('Alice','P3'),('Bob','P2'),
         ('Charlie','P1'),('Charlie','P2'),('Dana','P3'),('Dana','P4')]

count, matching = max_bipartite_matching(left, right, edges)
print(f"Max matching: {count}")
for project, student in matching.items():
    print(f"  {student} → {project}")
```

---

## 📝 Practice Questions with Detailed Solutions

### Q1: L={A,B,C}, R={1,2,3}. Edges: A-1, A-2, B-2, B-3, C-1. Find max matching.

**Solution:**
```
Try A: match A↔1. ✅
Try B: match B↔2. ✅
Try C: C wants 1, but 1 is taken by A!
  Can A switch? A also likes 2, but 2 is taken by B!
  Can B switch? B also likes 3, which is free! Match B↔3.
  Now A can take 2! Match A↔2.
  Now C can take 1! Match C↔1.
Max matching = 3 (perfect!): A↔2, B↔3, C↔1 ✅
```

### Q2: L={A,B}, R={1,2}. Edges: A-1, B-1 only. Max matching?

**Solution:** Both A and B can ONLY connect to 1. But 1 can only be matched to ONE of them. Max matching = **1**. Not a perfect matching.

### Q3: Is triangle (1-2-3) bipartite?

**Solution:** Try 2-coloring. Color 1=RED, 2=BLUE (edge 1-2 ✅), 3=RED (edge 2-3 ✅). But edge 3-1 connects RED-RED → **NOT bipartite!** Odd cycles are never bipartite.

### Q4: Hall's theorem: when does perfect matching exist?

**Solution:** **Hall's Marriage Theorem**: A bipartite graph has a matching that covers ALL of L if and only if for EVERY subset S ⊆ L, the neighborhood N(S) satisfies |N(S)| ≥ |S|. In words: every group of students must collectively like at least as many projects as there are students in the group.

### Q5: Maximum matching vs maximal matching?

**Solution:** **Maximal** = you can't add any more edges without breaking the rule (greedy stops). **Maximum** = the absolute largest possible. Maximum ≥ maximal, but maximal can be smaller! Example: greedy might match A↔1, leaving B and C unable to match. But optimal is B↔1, C↔2 (size 2 > 1).

### Q6: Time complexity of bipartite matching?

**Solution:** Using augmenting paths: O(V × E). For each of V left vertices, we do a DFS of O(E) to find an augmenting path. Hopcroft-Karp improves this to O(E√V).

### Q7: König's theorem — what does it say?

**Solution:** In a bipartite graph, **minimum vertex cover** = **maximum matching**. A vertex cover is a set of vertices that "touches" every edge. The smallest such set has the same size as the largest matching!

### Q8: Can a matching have more edges than min(|L|, |R|)?

**Solution:** NO! Each edge in the matching uses one L vertex and one R vertex. Since no vertex can appear twice, the matching size ≤ min(|L|, |R|). If matching size = min(|L|, |R|), it saturates the smaller side.

---

## 📋 Quick Revision Cheat Sheet

```
┌──────────────────────────────────────────────────────┐
│  BIPARTITE MATCHING — EVERYTHING IN ONE BOX          │
├──────────────────────────────────────────────────────┤
│                                                      │
│  Bipartite: 2 groups, edges only BETWEEN groups      │
│  Matching: set of edges, no vertex repeated          │
│                                                      │
│  REDUCTION TO MAX FLOW:                              │
│  Add s→L (cap 1), R→t (cap 1), L→R (cap 1)           │
│  Max flow = max matching                             │
│                                                      │
│  AUGMENTING PATHS:                                   │
│  For each unmatched L: DFS to find augmenting path   │
│  Flip matched/unmatched edges on path → +1 matching  │
│                                                      │
│  Time: O(VE)                                         │
│  Hall's theorem: |N(S)| ≥ |S| for all S ⊆ L          │
│  König: min vertex cover = max matching              │
│                                                      │
└──────────────────────────────────────────────────────┘
```

## 📚 References
- [CLRS Chapter 26.3](https://walkccc.me/CLRS/Chap26/26.3/)
- Lec's 16 — Pr V Raj S
