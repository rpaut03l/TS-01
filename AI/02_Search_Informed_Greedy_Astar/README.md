# 🧭 Topic 02 — Informed Search: Greedy Best-First & A* Search

> **Difficulty**: 🟡 Medium | **Syllabus Section**: Search 
>
> **Slides**: RB-M & SD-M | **Quiz Relevance**: ⭐⭐⭐⭐⭐ (Quiz 1)

---

## 🍼 Explain Like I'm 5 (ELI5)

Remember how uninformed search was like finding your mom in a mall with your eyes CLOSED? Well, **informed search** is like having your eyes OPEN — plus someone gave you a **hint**: "Your mom is somewhere near the food court!"

Now you don't wander randomly. You use this hint (called a **heuristic**) to walk TOWARD the food court. Much smarter!

- **Greedy Search** = "I'll always walk toward wherever SEEMS closest to the food court" (but might take a wrong shortcut!)
- **A* Search** = "I'll balance the distance I've ALREADY walked with how far I THINK I still need to go" (finds the BEST path!)

---

## 📚 Table of Contents

1. [What is a Heuristic?](#1-what-is-a-heuristic)
2. [Greedy Best-First Search](#2-greedy-best-first-search)
3. [A* Search](#3-a-search)
4. [Heuristic Properties (Admissibility & Consistency)](#4-heuristic-properties)
5. [Designing Good Heuristics](#5-designing-good-heuristics)
6. [Comparison: UCS vs Greedy vs A*](#6-comparison)
7. [Key Takeaways](#7-key-takeaways)
8. [Exam Tips](#8-exam-tips)

---

## 1. What is a Heuristic?

### Definition

A **heuristic function h(n)** is an **estimate** of the cost from node `n` to the nearest goal.

> 🍼 **ELI5**: A heuristic is your **gut feeling** about how far away the goal is. It's not exact — it's a guess. But a GOOD guess helps you find the goal much faster!

### Examples of Heuristics

| Problem | Heuristic h(n) | Why It Works |
|---|---|---|
| **Romania Map** | Straight-line distance to Bucharest | Straight line is always ≤ actual road distance |
| **8-Puzzle** | Number of misplaced tiles | Each misplaced tile needs at least 1 move |
| **8-Puzzle** | Manhattan distance (sum of distances of each tile from its goal) | Each tile needs at least that many moves |
| **Pac-Man** | Maze distance to nearest food dot | Can't eat food without reaching it |

### 🧮 How Heuristic Numbers Are Calculated (Step by Step!)

#### Example 1: Romania Map — Straight-Line Distance (SLD)

The heuristic for the Romania problem is the **straight-line distance** (as the crow flies) from each city to Bucharest. These are measured from actual coordinates on a map — not the road distance!

```
Think of it like this: You're standing in Arad. You take out a ruler and 
measure the STRAIGHT LINE from Arad to Bucharest on a paper map. That's 366 km.
The actual ROAD distance is longer (because roads curve, go through mountains, etc.)
but the straight line is your "optimistic guess."

City              Straight-Line to Bucharest (h)    Actual Road Distance
─────────────────────────────────────────────────────────────────────
Arad              366 km                             418 km (via best route)
Sibiu             253 km                             route varies
Fagaras           176 km                             211 km (direct road)
Pitesti           100 km                             101 km (direct road)
Bucharest         0 km                               0 km (you're already there!)
```

> 🍼 **Kid Version**: Imagine you're on a football field. The GOAL is at the other end. You can MEASURE the straight-line distance to the goal with a tape measure (that's h(n)). But you can't walk in a straight line — you have to follow the path around obstacles. The tape-measure distance is always SHORTER than the actual walk!

**Why is SLD a good heuristic?** Because a straight line is ALWAYS shorter than or equal to ANY path that follows roads. So h(n) ≤ actual cost — this means it NEVER overestimates. This property is called **admissibility** (more on this below).

#### Example 2: 8-Puzzle — Two Different Heuristics

Given this 8-puzzle state:

```
Current State:        Goal State:
┌───┬───┬───┐         ┌───┬───┬───┐
│ 7 │ 2 │ 4 │         │ 1 │ 2 │ 3 │
├───┼───┼───┤         ├───┼───┼───┤
│ 5 │   │ 6 │         │ 4 │ 5 │ 6 │
├───┼───┼───┤         ├───┼───┼───┤
│ 8 │ 3 │ 1 │         │ 7 │ 8 │   │
└───┴───┴───┘         └───┴───┴───┘
```

**Heuristic 1: Misplaced Tiles (h₁)**

Count how many tiles are NOT in their goal position:

```
Tile 7: Currently at (0,0), Goal at (2,0) → MISPLACED ❌
Tile 2: Currently at (0,1), Goal at (0,1) → CORRECT ✅
Tile 4: Currently at (0,2), Goal at (1,0) → MISPLACED ❌
Tile 5: Currently at (1,0), Goal at (1,1) → MISPLACED ❌
Blank:  (don't count the blank)
Tile 6: Currently at (1,2), Goal at (1,2) → CORRECT ✅
Tile 8: Currently at (2,0), Goal at (2,1) → MISPLACED ❌
Tile 3: Currently at (2,1), Goal at (0,2) → MISPLACED ❌
Tile 1: Currently at (2,2), Goal at (0,0) → MISPLACED ❌

h₁ = number of misplaced tiles = 6
```

**Heuristic 2: Manhattan Distance (h₂)**

For each tile, count how many squares it needs to move (horizontally + vertically) to reach its goal. Sum all of these up:

```
Tile 1: at (2,2), goal (0,0) → |2-0| + |2-0| = 2 + 2 = 4 moves
Tile 2: at (0,1), goal (0,1) → |0-0| + |1-1| = 0 + 0 = 0 moves ✅
Tile 3: at (2,1), goal (0,2) → |2-0| + |1-2| = 2 + 1 = 3 moves
Tile 4: at (0,2), goal (1,0) → |0-1| + |2-0| = 1 + 2 = 3 moves
Tile 5: at (1,0), goal (1,1) → |1-1| + |0-1| = 0 + 1 = 1 move
Tile 6: at (1,2), goal (1,2) → |1-1| + |2-2| = 0 + 0 = 0 moves ✅
Tile 7: at (0,0), goal (2,0) → |0-2| + |0-0| = 2 + 0 = 2 moves
Tile 8: at (2,0), goal (2,1) → |2-2| + |0-1| = 0 + 1 = 1 move

h₂ = 4 + 0 + 3 + 3 + 1 + 0 + 2 + 1 = 14
```

**Comparison:**

```
h₁ (misplaced tiles) = 6    ← Less informed (just counts "wrong" tiles)
h₂ (Manhattan distance) = 14 ← More informed (measures HOW FAR each tile is wrong)

h₂ ≥ h₁ ALWAYS! → h₂ is BETTER (A* with h₂ expands fewer nodes!)
```

> 🍼 **Kid Version for Manhattan Distance**: Imagine each tile is a kid in a classroom. Each kid needs to walk to their assigned seat. They can only walk along the aisles (up/down or left/right, NOT diagonally). Manhattan distance = total steps ALL kids need to take to reach their seats. It's called "Manhattan" because in Manhattan (New York City), the streets are in a GRID and you walk in straight lines along blocks!

### The Key Notation

| Symbol | Meaning | ELI5 |
|---|---|---|
| **g(n)** | Actual cost from START to node n | "How far have I walked already?" |
| **h(n)** | Estimated cost from n to GOAL | "How far do I THINK I still need to walk?" |
| **f(n)** | g(n) + h(n) = Total estimated cost | "How much will this whole trip cost?" |

```
START ───── g(n) ─────> n ───── h(n) ─────> GOAL
<────────────── f(n) = g(n) + h(n) ──────────────>
```

---

## 2. Greedy Best-First Search

### The Idea

Always expand the node that **appears to be closest to the goal** — the one with the smallest h(n).

> 🍼 **ELI5**: Imagine you're walking to a candy store. At every intersection, you look at which road SEEMS to point most directly toward the store. You always take that road. Quick? Usually! Best path? Not always — you might walk into a dead end or take a detour!

### How It Works

- Uses a **Priority Queue** ordered by **h(n)** (heuristic value only)
- Always expands the node with the LOWEST h(n)
- Ignores how far you've already traveled (g(n))

### Example: Romania Map

**Goal**: Get from Arad to Bucharest
**Heuristic**: Straight-line distance to Bucharest

```
City            h(n) = Straight-line to Bucharest
─────────────────────────────────────────
Arad            366
Sibiu           253
Fagaras         176
Bucharest       0     ← GOAL!
Timisoara       329
Zerind          374
Oradea          380
Rimnicu Vilcea  193
Pitesti         100
```

**Greedy trace — showing FULL frontier at each step:**

| Step | Expand | h(n) | Frontier (sorted by h) | Why this node? |
|---|---|---|---|---|
| 1 | Arad | h=366 | — | Start node |
| 2 | Sibiu | h=253 | ~~Sibiu(253)~~, Timisoara(329), Zerind(374) | 253 < 329 < 374 → Sibiu closest to goal |
| 3 | Fagaras | h=176 | ~~Fagaras(176)~~, RV(193), Timisoara(329), Zerind(374), Oradea(380) | 176 is smallest h |
| 4 | **Bucharest** | h=0 | ~~Bucharest(0)~~, RV(193), ... | 0 = GOAL! 🎯 |

**How Greedy picked each step (think like a 5-year-old):**

```
Step 1: "I'm in Arad. Where should I go?"
        Look at all neighbors and their h(n):
          Sibiu:     h = 253 km straight-line to Bucharest
          Timisoara: h = 329 km straight-line to Bucharest
          Zerind:    h = 374 km straight-line to Bucharest
        "Sibiu SEEMS closest! Go there!" → Pick Sibiu

Step 2: "I'm in Sibiu. Where should I go?"
        Neighbors (not yet visited):
          Fagaras: h = 176  ← Wow, this seems really close!
          RV:      h = 193
          Oradea:  h = 380
        "Fagaras SEEMS closest! Go there!" → Pick Fagaras

Step 3: "I'm in Fagaras. Where should I go?"
        Neighbors:
          Bucharest: h = 0  ← ZERO! That's the goal!
        "Go to Bucharest!" → DONE! 🎯
```

**Path found**: Arad → Sibiu → Fagaras → Bucharest
**Cost**: 140 + 99 + 211 = **450 km**

**But wait!** The OPTIMAL path is:
Arad → Sibiu → Rimnicu Vilcea → Pitesti → Bucharest
**Cost**: 140 + 80 + 97 + 101 = **418 km** (32 km shorter!)

**Why did Greedy get it wrong?** Because at Sibiu, Greedy chose Fagaras (h=176) over RV (h=193) purely because Fagaras SEEMED closer. But the actual road from Fagaras to Bucharest is 211 km, while going through RV+Pitesti is only 80+97+101=278 km from Sibiu. **Greedy was fooled by the straight-line shortcut!**

> 🍼 **Kid Version**: Imagine you're walking to school. There are two paths from the park: Path A LOOKS like it goes straight toward school (short straight line), but it goes through a muddy swamp that's slow. Path B goes a bit sideways first (longer straight line), but it's on a smooth road that's actually faster. Greedy picks Path A because it LOOKS more direct. But Path B was actually quicker!

### Properties of Greedy Best-First Search

| Property | Value | Explanation |
|---|---|---|
| **Complete?** | ❌ No (can loop in graph without explored set) | Might keep bouncing between states |
| **Optimal?** | ❌ No | Ignores path cost, can miss better routes |
| **Time** | O(b^m) worst case | Can explore everything if heuristic is bad |
| **Space** | O(b^m) | Stores all generated nodes |

### The Fatal Flaw

Greedy search is **myopic** (short-sighted) — it only looks at h(n) and ignores g(n). It's like a person who always walks toward the destination "as the crow flies" but ignores that they might be walking through mountains!

---

## 3. A* Search

### The Idea — The Star of AI Search! ⭐

**A* combines the best of both worlds:**
- **g(n)** = actual cost so far (what UCS uses)
- **h(n)** = estimated cost to goal (what Greedy uses)
- **f(n) = g(n) + h(n)** = total estimated cost of the path through n

> 🍼 **ELI5**: Imagine you're at a candy store deciding which route to take. Route A is "I've walked 2 blocks and I THINK there are 5 more blocks to go" (total guess: 7). Route B is "I've walked 4 blocks and I THINK there are 2 more" (total guess: 6). A* picks Route B because the TOTAL estimated journey is shorter!

### How It Works

1. Use a **Priority Queue** ordered by **f(n) = g(n) + h(n)**
2. Always expand the node with the LOWEST f(n)
3. When you expand the goal, you've found the OPTIMAL path!

### Step-by-Step Example: Romania Map (FULL ARITHMETIC)

**Goal**: Arad → Bucharest

**Reference — Road distances (g costs) and Straight-line distances (h values):**
```
Road distances:                    Straight-line to Bucharest (h):
Arad → Sibiu:       140 km        Arad:      366
Arad → Timisoara:   118 km        Sibiu:     253
Arad → Zerind:      75 km         Fagaras:   176
Sibiu → Fagaras:    99 km         RV:        193
Sibiu → RV:         80 km         Pitesti:   100
Sibiu → Oradea:     151 km        Timisoara: 329
RV → Pitesti:       97 km         Zerind:    374
Fagaras → Bucharest: 211 km       Oradea:    380
Pitesti → Bucharest: 101 km       Bucharest: 0
```

**The trace — showing EVERY calculation of f(n) = g(n) + h(n):**

**Step 1: Expand Arad** (f = 0 + 366 = 366)
```
Arad's neighbors:
  Sibiu:     g = 0 + 140 = 140,  h = 253,  f = 140 + 253 = 393
  Timisoara: g = 0 + 118 = 118,  h = 329,  f = 118 + 329 = 447
  Zerind:    g = 0 + 75  = 75,   h = 374,  f = 75  + 374 = 449

Frontier: [Sibiu(393), Timisoara(447), Zerind(449)]
Pick lowest f → Sibiu (393)
```

**Step 2: Expand Sibiu** (f = 393)
```
Sibiu's neighbors (not explored):
  Fagaras: g = 140 + 99  = 239,  h = 176,  f = 239 + 176 = 415
  RV:      g = 140 + 80  = 220,  h = 193,  f = 220 + 193 = 413
  Oradea:  g = 140 + 151 = 291,  h = 380,  f = 291 + 380 = 671

Frontier: [RV(413), Fagaras(415), Timisoara(447), Zerind(449), Oradea(671)]
                ↑ Lowest!
Pick lowest f → RV (413)
```

**Step 3: Expand Rimnicu Vilcea** (f = 413)
```
RV's neighbors:
  Pitesti: g = 220 + 97  = 317,  h = 100,  f = 317 + 100 = 417
  Craiova: g = 220 + 146 = 366,  h = 160,  f = 366 + 160 = 526

Frontier: [Fagaras(415), Pitesti(417), Timisoara(447), Zerind(449), Craiova(526), Oradea(671)]
Pick lowest f → Fagaras (415)
```

**Step 4: Expand Fagaras** (f = 415)
```
Fagaras's neighbors:
  Bucharest: g = 239 + 211 = 450,  h = 0,  f = 450 + 0 = 450

Frontier: [Pitesti(417), Timisoara(447), Zerind(449), Bucharest-via-Fag(450), Craiova(526), Oradea(671)]
                ↑ Pitesti(417) < Bucharest(450)! Don't stop yet!
Pick lowest f → Pitesti (417)
```

**⚠️ KEY MOMENT**: Bucharest is in the frontier with f=450, but Pitesti has f=417 which is LOWER! A* does NOT stop when it first GENERATES the goal. It continues expanding cheaper nodes because they might lead to a BETTER path to the goal!

**Step 5: Expand Pitesti** (f = 417)
```
Pitesti's neighbors:
  Bucharest: g = 317 + 101 = 418,  h = 0,  f = 418 + 0 = 418

Frontier: [Bucharest-via-Pit(418), Timisoara(447), Zerind(449), Bucharest-via-Fag(450), ...]
               ↑ This is CHEAPER than the Bucharest we found before (450)!
Pick lowest f → Bucharest (418)
```

**Step 6: Expand Bucharest** (f = 418) → **GOAL! 🎯**

```
A* tests for goal when EXPANDING (like UCS), so NOW it reports success!
```

**Optimal Path**: Arad → Sibiu → RV → Pitesti → Bucharest = **418 km** ✅

### 🔍 Why A* Got It Right and Greedy Got It Wrong

```
Greedy's path:  Arad →(140)→ Sibiu →(99)→ Fagaras →(211)→ Bucharest = 450 km
                Greedy chose Fagaras(h=176) over RV(h=193) because 176 < 193

A*'s path:      Arad →(140)→ Sibiu →(80)→ RV →(97)→ Pitesti →(101)→ Bucharest = 418 km
                A* chose RV(f=413) over Fagaras(f=415) because 413 < 415
                Even though RV looks farther from Bucharest, the road to RV is shorter!
```

> 🍼 **Kid Version**: Greedy is like a kid who always runs STRAIGHT toward the ice cream truck, even through mud puddles. A* is like a smart kid who thinks "The sidewalk goes around the mud — it LOOKS longer, but I'll actually get there FASTER because I won't get stuck in mud!"

### Pseudocode

```
function A_STAR(problem, heuristic):
    node = Node(problem.initial_state, g=0, h=heuristic(initial))
    frontier = PriorityQueue(ordered by f = g + h)
    frontier.add(node)
    explored = empty set
    
    while frontier is not empty:
        node = frontier.pop()          ← Node with lowest f(n)
        
        if node is goal: return node   ← Optimal solution!
        explored.add(node.state)
        
        for each action in problem.actions(node.state):
            child = problem.result(node, action)
            child.g = node.g + step_cost(node, action, child)
            child.h = heuristic(child)
            child.f = child.g + child.h
            
            if child.state not in explored:
                if child not in frontier:
                    frontier.add(child)
                else if child.g < existing.g:
                    replace existing with child  ← Found cheaper path
    
    return FAILURE
```

### Why A* is Optimal — The Proof Intuition

Suppose A* is about to expand the goal with cost f(G) = g(G) + 0 = g(G).

Could there be a BETTER path we haven't found yet? Let's say there's an unexpanded node `n` on that better path.

- Since `n` is on the frontier: f(n) ≥ f(G) (because A* expands lowest f first)
- If h is **admissible**: f(n) = g(n) + h(n) ≤ g(n) + actual cost to goal = true cost of path through n
- So true cost through n ≥ f(n) ≥ f(G) = g(G)

This means the path through n is **at least as expensive** as the path A* found! So A*'s path IS optimal! ✅

---

## 4. Heuristic Properties

### 4.1 Admissibility (The "Optimistic" Rule)

A heuristic is **admissible** if it **NEVER overestimates** the true cost to the goal.

```
h(n) ≤ h*(n)    for all n

where h*(n) = true cheapest cost from n to goal
```

> 🍼 **ELI5**: An admissible heuristic is like a friend who always says "Oh, the store is MAYBE 2 blocks away" when it's actually 5 blocks. They always UNDERESTIMATE. They never say "10 blocks" if it's really 5. They're always optimistic!

**Why it matters**: A* with an admissible heuristic is **guaranteed to find the optimal solution** in tree search.

#### 🧮 Proving Admissibility — Concrete Example

**Is straight-line distance (SLD) admissible for Romania?**

We need to check: h(n) ≤ actual shortest road distance, for EVERY city.

```
City          h(n) = SLD    Actual shortest road to Bucharest    h ≤ actual?
──────────────────────────────────────────────────────────────────────────
Arad          366            418 (Arad→Sibiu→RV→Pit→Buch)       366 ≤ 418 ✅
Sibiu         253            278 (Sibiu→RV→Pit→Buch)             253 ≤ 278 ✅
Fagaras       176            211 (Fagaras→Buch direct)           176 ≤ 211 ✅
Pitesti       100            101 (Pitesti→Buch direct)           100 ≤ 101 ✅
Timisoara     329            536 (Tim→Arad→Sibiu→RV→Pit→Buch)   329 ≤ 536 ✅
```

Every h(n) ≤ actual cost → **SLD is admissible!** ✅

**Why is SLD ALWAYS admissible?** Because a straight line is the SHORTEST possible distance between two points. Any road, path, or route must be at least as long as the straight line. This is literally geometry! 📐

#### 🧮 Example of a NON-admissible heuristic

```
Suppose h(Pitesti) = 200    but actual cost Pitesti→Bucharest = 101
200 > 101 → OVERESTIMATE! → NOT admissible ❌

If A* uses this heuristic, it might skip the Pitesti→Bucharest path
because f = g + 200 looks expensive, and choose a worse path instead!
```

### 4.2 Consistency (The "Triangle Inequality" Rule)

A heuristic is **consistent** (or **monotone**) if for every node n and every successor n':

```
h(n) ≤ cost(n, n') + h(n')
```

> 🍼 **ELI5**: It's the triangle rule! Going directly from A to C should never seem "longer" than going A→B→C according to the heuristic. Like, if you estimate it's 10 blocks to school, and you walk 3 blocks to a park, your estimate from the park should be at most 7 blocks (10 - 3).

#### 🧮 Checking Consistency — Concrete Example

**Check: Is SLD consistent for the edge Arad → Sibiu?**

```
h(Arad) ≤ cost(Arad, Sibiu) + h(Sibiu)
  366   ≤      140           +   253
  366   ≤      393     ✅ YES!
```

**Check: Edge Sibiu → Fagaras?**

```
h(Sibiu) ≤ cost(Sibiu, Fagaras) + h(Fagaras)
  253    ≤        99             +   176
  253    ≤       275     ✅ YES!
```

**Check: Edge Sibiu → RV?**

```
h(Sibiu) ≤ cost(Sibiu, RV) + h(RV)
  253    ≤      80          +  193
  253    ≤     273     ✅ YES!
```

You need to check this for EVERY edge in the graph. If it holds for all edges → consistent!

#### 🧮 Example of a NON-consistent heuristic

```
Suppose: h(A) = 10, h(B) = 3, cost(A,B) = 2

Check: h(A) ≤ cost(A,B) + h(B)
       10   ≤    2       +   3
       10   ≤    5     ❌ FAILS!

This means: the heuristic says A is 10 away from the goal,
but after taking one step (cost 2) to B, it says B is only 3 away.
That's a DROP of 7 in just 2 cost units — too fast! Something's wrong.
```

#### The Relationship: Consistency → Admissibility

```
Consistent ──implies──→ Admissible     (always true!)
Admissible ──does NOT imply──→ Consistent (sometimes fails!)
```

> 🍼 **Kid Version**: All consistent heuristics are also admissible (like how all squares are also rectangles). But not all admissible heuristics are consistent (like how not all rectangles are squares).

```
         h(n)
    n ─────────────────> Goal
    |                    ↗
cost(n,n')         h(n')
    |            ↗
    n' ──────────

Rule: h(n) ≤ cost(n, n') + h(n')
```

**Important**: Consistency implies admissibility (but not vice versa)!

**Why it matters**: A* with a consistent heuristic is optimal in **graph search** (with explored set) too.

### 4.3 Dominance

If h₂(n) ≥ h₁(n) for all n, and both are admissible, then h₂ **dominates** h₁.

A dominant heuristic is ALWAYS better — it's more informed and will expand fewer nodes!

**Example for 8-Puzzle:**
- h₁ = Number of misplaced tiles = 6
- h₂ = Manhattan distance = 2+3+0+1+2+1+3+1 = 13

h₂ ≥ h₁ always, so h₂ dominates h₁ → A* with Manhattan distance expands fewer nodes!

---

## 5. Designing Good Heuristics

### Method 1: Relaxed Problems

Remove some constraints from the original problem → the cost of solving the easier problem is a heuristic!

**8-Puzzle Example:**
- **Original**: A tile can move from A to B if A is adjacent to B AND B is blank
- **Relaxation 1**: A tile can move from A to B if A is adjacent to B → **Manhattan distance**
- **Relaxation 2**: A tile can move from A to B → **Misplaced tiles count**

### Method 2: Pattern Databases

Pre-compute exact costs for solving PART of the problem and store them in a lookup table.

### Method 3: Max of Multiple Heuristics

If h₁ and h₂ are both admissible:

```
h(n) = max(h₁(n), h₂(n))
```

This is also admissible and DOMINATES both h₁ and h₂! Free improvement!

---

## 6. Comparison

| Feature | UCS | Greedy Best-First | A* |
|---|---|---|---|
| **Evaluates by** | g(n) | h(n) | g(n) + h(n) |
| **What it "cares" about** | Past cost only | Future estimate only | Past + Future |
| **Complete?** | ✅ Yes | ❌ No | ✅ Yes |
| **Optimal?** | ✅ Yes | ❌ No | ✅ Yes (with admissible h) |
| **Speed** | Slow (no guidance) | Fast but unreliable | Fast AND reliable |
| **Like a person who...** | Only counts steps taken | Only looks at how far the destination seems | Balances both wisely |

### Visual Intuition

```
UCS expands like this:            Greedy expands like this:       A* expands like this:
(uniform circles)                 (toward goal, messy)            (oval toward goal)

    ● ● ● ●                             ●                          ● ● ●
  ● ● ● ● ● ●                         ● ●                        ● ● ● ● ●
● ● ● S ● ● ● ●                    ● ● ● G                    ● ● S ● ● ● G
  ● ● ● ● ● ●                       ● ●                          ● ● ● ●
    ● ● ● ●                          ●                              ● ●

(S = Start, G = Goal)
```

---

## 7. Key Takeaways

1. **Heuristics make search SMART** — they guide us toward the goal instead of blindly exploring
2. **Greedy** is fast but unreliable — it can be fooled by bad estimates
3. **A* = UCS + Greedy** — it gets the optimality of UCS and the speed of Greedy
4. **Admissible heuristic** = never overestimates → guarantees A* finds optimal in tree search
5. **Consistent heuristic** = triangle inequality → guarantees A* finds optimal in graph search
6. **Better heuristics = fewer nodes expanded** — always try to make h(n) as large as possible (while staying admissible)
7. **A* is optimally efficient** — no other optimal algorithm expands fewer nodes (given the same heuristic)

### The Mental Model

Think of it like hiking with a map:
- **UCS** = You have NO map, you just measure distance walked
- **Greedy** = You have a map showing straight-line distances to destination, you ONLY look at that
- **A*** = You have BOTH a pedometer (distance walked) AND the map (distance estimate) — you use BOTH to make the best decision

---

## 8. Exam Tips

### Must-Know for Quizzes

1. **Trace A* step by step** on a graph → show f(n)=g(n)+h(n) at each step
2. **Prove a heuristic is admissible** → show h(n) ≤ true cost for all n
3. **Check consistency** → verify h(n) ≤ c(n,n') + h(n') for all edges
4. **Compare heuristics** → which dominates? which makes A* faster?
5. **When does A* fail to be optimal?** → when h is NOT admissible!

### Common Exam Traps

❌ Confusing g(n) and h(n) → g = past (actual), h = future (estimate)
❌ Saying A* always expands fewer nodes than UCS → only true with a good heuristic
❌ Using h(n) in UCS (UCS uses ONLY g(n)!)
❌ Thinking Greedy is optimal because it's fast
❌ Forgetting that consistency ⟹ admissibility (but NOT the reverse)

### Quick Formulas

```
f(n) = g(n) + h(n)          ← A* evaluation function
h(n) = 0 for all n          ← Makes A* behave exactly like UCS
g(n) = 0 for all n          ← Makes A* behave exactly like Greedy (conceptually)
```

---

## 📖 References

- AIMA — Chapter 3.5-3.6 (Informed Search)
- [Stanford CS221 — Heuristic Search](https://www.youtube.com/playlist?list=PLoROMvodv4rO1NB9TD4iUZ3qghGEGtqNX)

---

[⬅️ Prev: Uninformed Search](../01_Search_Uninformed/README.md) | [Back to Main](../README.md) | [Next: Memory-Bounded Heuristic Search ➡️](../03_Search_Memory_Bounded_Heuristic/README.md)
