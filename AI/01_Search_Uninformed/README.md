# 🔍 Topic 01 — Uninformed Search Strategies (The Blind Explorers)

> **Difficulty**: 🟢 Easy → 🟡 Medium | **Syllabus Section**: Search | **Lectures**: Week 1-2
>
> **Slides**: RB-M & SD-M | **Quiz Relevance**: ⭐⭐⭐⭐⭐ (Quiz 1 — MOST IMPORTANT TOPIC)

---

## 🍼 The Big Story

### The Lost Teddy Bear Adventure 🧸

Imagine you're a little Kid in a **HUGE house** with 100 rooms. Your teddy bear is hiding in ONE of the rooms. You need to find it!

But here's the problem: **you're blindfolded!** 😱 You can't see anything. All you can do is:
1. Feel the room you're IN right now
2. Find the DOORS leading to other rooms
3. Walk through a door into the next room
4. Check: "Is my teddy here?"

That's EXACTLY what **uninformed search** is! The computer is "blindfolded" — it has NO idea where the goal is. It can only:
1. Know what state it's in NOW
2. See what actions (moves) it can take
3. Take an action and arrive at a new state
4. Check: "Am I at the goal?"

Now, even though you're blindfolded, you can be SMART about how you search:

- **Strategy 1 (BFS)**: Check ALL rooms on the ground floor first. Then ALL rooms on the first floor. Then ALL rooms on the second floor. You spread out EVENLY, level by level. Like ripples in a pond! 🌊
- **Strategy 2 (DFS)**: Pick ONE hallway and walk ALL the way to the end. Hit a dead end? Walk BACK and try the next hallway. You go DEEP before going WIDE. Like a mole digging tunnels! 🕳️
- **Strategy 3 (IDS)**: First, check rooms within 1 step. Then within 2 steps. Then 3. Then 4. Each time, you go a little deeper. Like dipping your toes in the pool, then ankles, then knees... 🏊
- **Strategy 4 (UCS)**: Always go to the room that's CHEAPEST to reach (maybe some hallways are short and some are long). You're trying to minimize the total walking distance. Like a smart delivery driver! 🚗

The word "uninformed" means **NO HINTS**. You don't have a map, you don't have a compass, you don't know which direction the teddy is. You just explore systematically and hope to find it!

---

## 📚 Table of Contents

1. [What is a Search Problem?](#1-what-is-a-search-problem)
2. [How Search Works: Trees, Nodes, and Frontiers](#2-how-search-works)
3. [Measuring Search Performance](#3-measuring-performance)
4. [BFS — The Ripple Explorer](#4-bfs)
5. [DFS — The Tunnel Digger](#5-dfs)
6. [Depth-Limited Search](#6-dls)
7. [Iterative Deepening Search — The Best of Both Worlds](#7-ids)
8. [Uniform Cost Search — The Cheapest Path Finder](#8-ucs)
9. [Bidirectional Search](#9-bidirectional)
10. [The Grand Comparison Table](#10-comparison)
11. [Worked Exam Problems](#11-worked-problems)
12. [Key Takeaways](#12-takeaways)
13. [Exam Tips](#13-exam-tips)

---

## 1. What is a Search Problem?

### The 6 Ingredients

Every search problem has exactly **6 components**:

**1. STATE SPACE** — All possible situations that exist

> 🍼 Think of a toy box where you can arrange 3 blocks (R, G, B) on 3 shelves. The state space is EVERY possible arrangement. Each arrangement is one "state."

| Problem | What is a "State"? | How many states? |
|---|---|---|
| Tic-Tac-Toe | Board configuration | ~5,478 |
| 8-Puzzle | Tile arrangement | 181,440 |
| Chess | All piece positions | ~10^47 |
| Romania Map | Current city | 20 |

### 🧮 How Did We Get These Numbers? (Step-by-Step Math)

This is important to understand because **knowing how to count states** tells you how BIG the search space is — and whether your algorithm can handle it!

---

#### 🔢 Romania Map → 20 states

**The simplest one.** The Romania map used in the AIMA textbook has exactly **20 cities**:

```
Arad, Bucharest, Craiova, Dobreta, Eforie, Fagaras, Giurgiu, Hirsova,
Iasi, Lugoj, Mehadia, Neamt, Oradea, Pitesti, Rimnicu Vilcea, Sibiu,
Timisoara, Urziceni, Vaslui, Zerind
```

A "state" = which city you are in right now. Since there are 20 cities, there are **20 possible states**. That's it — just count the cities!

> 🍼 **Easy Version**: You have 20 different rooms in a house. You can be in Room 1, or Room 2, or Room 3, ... or Room 20. So there are 20 possible "states" (places you could be). Simple counting!

---

#### 🔢 Tic-Tac-Toe → ~5,478 states

This one is trickier. Let's think about it step by step.

**What is a state?** A 3×3 grid where each cell is either: Empty, X, or O.

**Naive (wrong) upper bound:**
```
Each of the 9 cells can be: Empty, X, or O → 3 options per cell
Total combinations = 3 × 3 × 3 × 3 × 3 × 3 × 3 × 3 × 3 = 3^9 = 19,683
```

**But most of these are ILLEGAL!** Why?

Rule 1: X always goes first. So the number of X's must be equal to O's, or one more than O's.
```
Valid: XXO (2 X's, 1 O → X went first, then O, then X) ✅
Invalid: XOO (1 X, 2 O's → O went more times than X?!) ❌
```

Rule 2: The game STOPS when someone wins. So we can't have states where X has 3-in-a-row AND O also played after that.

Rule 3: We can't have BOTH X and O winning simultaneously.

**After removing all illegal states:**

```
Step 1: Start with 3^9 = 19,683 (all possible grid fillings)

Step 2: Remove states where O count > X count
        (X goes first, so #X ≥ #O always)

Step 3: Remove states where #X > #O + 1
        (X can have at most 1 more than O)

Step 4: Remove states where both X and O have 3-in-a-row
        (impossible — game stops when first player wins)

Step 5: Remove states where X has won but O played after
        (game should have stopped when X won)

After all these filters: approximately 5,478 valid states
```

**The exact number depends on whether you count "X wins" terminal states or not.** Different sources give slightly different numbers (5,478 is the commonly cited AIMA number for reachable states).

> 🍼 **Easy Version**: A tic-tac-toe board has 9 squares. Each can be empty, X, or O. That's 3×3×3×...×3 (nine times) = 19,683 possible boards. But MANY of those are impossible (like O going 5 times when X only went 3 times — that's cheating!). After throwing away the cheater-boards, we're left with about 5,478 real game positions.

---

#### 🔢 8-Puzzle → 181,440 states

**What is the 8-Puzzle?**

```
┌───┬───┬───┐
│ 1 │ 2 │ 3 │     This is the GOAL state.
├───┼───┼───┤     You start with tiles scrambled,
│ 4 │ 5 │ 6 │     and slide tiles into the blank
├───┼───┼───┤     space to reach this arrangement.
│ 7 │ 8 │   │ ← blank
└───┴───┴───┘
```

**What is a state?** An arrangement of 8 numbered tiles + 1 blank space on a 3×3 grid.

**Step-by-step calculation:**

```
We have 9 positions on the grid.
We have 9 items to place (tiles 1-8 plus the blank).

The blank can go in any of the 9 positions.
Then tile 1 can go in any of the 8 remaining positions.
Then tile 2 can go in any of the 7 remaining positions.
... and so on.

Total arrangements = 9! = 9 × 8 × 7 × 6 × 5 × 4 × 3 × 2 × 1 = 362,880
```

**But wait! Only HALF of these are reachable!**

There's a mathematical fact about sliding tile puzzles: the state space splits into exactly TWO groups of equal size. From any starting position, you can only reach states in the SAME group. The other half is forever unreachable (no matter how many moves you make!).

This is related to the **parity of permutations** (whether you need an even or odd number of swaps):

```
Total arrangements:    9! = 362,880
Reachable from any 
given start state:     9! / 2 = 362,880 / 2 = 181,440 ✅
```

> 🍼 **Easy Version**: Imagine you have 8 numbered tiles and 1 empty space on a small board. You can arrange them in 9! = 362,880 different ways (that's 9 × 8 × 7 × 6 × 5 × 4 × 3 × 2 × 1 — the math for "how many ways to arrange 9 things"). But here's a funny secret: half of those arrangements are IMPOSSIBLE to reach by sliding! It's like having a jigsaw puzzle where half the ways to put it together are magically forbidden. So we divide by 2: **362,880 ÷ 2 = 181,440**.

**Bonus — The 15-Puzzle (4×4 grid):**
```
16! / 2 = 20,922,789,888,000 / 2 = ~10.46 trillion states!
```
That's why the 15-puzzle is MUCH harder than the 8-puzzle!

---

#### 🔢 Chess → ~10^47 states

This is the most complex calculation and is actually an **estimate** (the exact number is unknown!).

**The Shannon Number (Upper Bound Estimate):**

Claude Shannon (father of information theory) estimated this in 1950:

```
Step 1: The board has 64 squares.

Step 2: Consider placing pieces on the board.
        White has: 1 King, 1 Queen, 2 Rooks, 2 Bishops, 2 Knights, 8 Pawns = 16 pieces
        Black has: same = 16 pieces
        Total: 32 pieces + 32 empty squares

Step 3: But pieces get captured during the game, so we could have 
        anywhere from 2 pieces (just the two kings) to 32 pieces.

Step 4: For each number of pieces, we need to count:
        - Which pieces are still alive?
        - Where is each piece placed?
        - Whose turn is it?
        - Can anyone castle? (king/rook haven't moved)
        - Is en passant available?

Step 5: The exact calculation is extremely complex because of:
        - Pawns can promote to any piece (so you could have 9 queens!)
        - Pawns can't be on rows 1 or 8 (they promote when they reach the end)
        - Bishops must be on opposite colors (one on light, one on dark squares)
        - The king can't be in check when it's not that player's turn
        - Many other chess-specific rules

Estimates range from 10^44 to 10^47 depending on which constraints 
you include. The commonly cited number is approximately 10^47.
```

**For context, how big is 10^47?**
```
Atoms in the observable universe:    ~10^80
Grains of sand on Earth:             ~10^19
Seconds since the Big Bang:          ~10^17
Chess positions:                     ~10^47  ← Bigger than grains of sand!
```

> 🍼 **Easy Version**: Chess has so many possible board positions that the number is BIGGER than the number of grains of sand on every beach on Earth — COMBINED! The exact number is around 10^47 (that's 1 followed by 47 zeros). Nobody has counted the exact number because it's just too huge. Smart math people ESTIMATED it.

---

### 📊 Summary Table (with the math!)

| Problem | State Description | Math | Result |
|---|---|---|---|
| **Romania Map** | Which city? | Count the cities | **20** |
| **Tic-Tac-Toe** | Board config | 3^9 minus illegal states | **~5,478** |
| **8-Puzzle** | Tile arrangement | 9! ÷ 2 (half unreachable) | **181,440** |
| **Chess** | Piece positions | Shannon's estimate | **~10^47** |

### 🔑 Why This Matters for Search

The state space size tells you WHETHER a brute-force search is even possible:

```
20 states (Romania)?        → BFS can solve in milliseconds ✅
5,478 states (Tic-Tac-Toe)? → BFS can solve in milliseconds ✅
181,440 states (8-Puzzle)?   → BFS can solve in seconds ✅
10^47 states (Chess)?        → BFS is IMPOSSIBLE! Need smarter methods ❌
                               (This is why chess engines use Minimax + Alpha-Beta!)
```

> 🍼 **The Lesson**: Before choosing a search algorithm, ALWAYS ask "how big is my state space?" If it's small → any algorithm works. If it's huge → you need informed search (A*), pruning (Alpha-Beta), or heuristics!

---

**2. INITIAL STATE** — Where you start

Example: In Romania map, we start in Arad.

**3. ACTIONS** — What you can do from any state

Example: From Arad, you can drive to Sibiu, Timisoara, or Zerind.

**Notation**: ACTIONS(s) returns all legal actions in state s.

**4. TRANSITION MODEL** — What happens when you act

**Notation**: RESULT(s, a) = s' → "Doing action a in state s takes you to state s'"

Example: RESULT(Arad, Drive-to-Sibiu) = Sibiu

**5. GOAL TEST** — Am I done?

Example: "Am I in Bucharest?" → Yes/No

**6. PATH COST** — How much does the journey cost?

Each action has a **step cost** c(s, a, s'). Total path cost = sum of all step costs.

Example: Arad→Sibiu costs 140 km, Sibiu→Fagaras costs 99 km. Total: 239 km.

### What is a Solution?

A **solution** = sequence of actions from initial state to a goal state.
An **optimal solution** = solution with the **lowest total path cost**.

---

## 2. How Search Works

### 2.1 The Search Tree

When we explore, we build a **tree** rooted at the initial state:

```
                         Arad (ROOT)
                       /        |          \
                  Sibiu     Timisoara     Zerind
                 /   |  \       |            |
          Fagaras  Oradea RV   Lugoj      Oradea
            |
        Bucharest (GOAL! 🎯)
```

**IMPORTANT**: The same state can appear MULTIPLE times in the tree (reached via different paths). Oradea appears twice above.

### 2.2 Node = State + Extra Info

A **node** in the search tree stores:

```
Node = {
    state:      "Sibiu"         ← Where am I?
    parent:     Node(Arad)      ← How did I get here?
    action:     "Drive Arad→Sibiu"  ← What did I do?
    path_cost:  140             ← Total cost from start
    depth:      1               ← Steps from root
}
```

### 2.3 The Frontier ("To-Do List")

The **frontier** = nodes discovered but NOT YET expanded.

Think of it as your **shopping list of rooms to visit**.

### 2.4 The Explored Set ("Already Visited")

Prevents revisiting states. Without it: A → B → A → B → ... forever! 😵

### 2.5 The General Algorithm

```
function GENERAL_SEARCH(problem, strategy):
    frontier = {initial_state}
    explored = {}
    
    while frontier NOT empty:
        node = REMOVE from frontier (HOW depends on strategy!)
        
        if GOAL(node): return path to node 🎯
        
        explored.add(node.state)
        
        for each child of node:
            if child NOT in explored and NOT in frontier:
                add child to frontier
    
    return FAILURE
```

**The ONLY difference between BFS, DFS, UCS is HOW they pick the next node from the frontier!**

| Strategy | Frontier = | Picks |
|---|---|---|
| BFS | Queue (FIFO) | Shallowest node |
| DFS | Stack (LIFO) | Deepest node |
| UCS | Priority Queue | Cheapest node |

---

## 3. Measuring Performance

| Criterion | Question | ELI5 |
|---|---|---|
| **Completeness** | Will it ALWAYS find a solution (if one exists)? | "Will I definitely find the teddy?" |
| **Optimality** | Does it find the BEST (cheapest) solution? | "Did I take the shortest path?" |
| **Time complexity** | How many nodes does it examine? | "How many rooms did I check?" |
| **Space complexity** | How many nodes does it store? | "How many sticky notes do I need?" |

**Key Variables:**
- **b** = branching factor (doors per room)
- **d** = depth of shallowest goal
- **m** = maximum tree depth
- **C\*** = optimal solution cost
- **ε** = minimum step cost

---

## 4. BFS — The Ripple Explorer 🌊

### How It Works

Uses a **Queue (FIFO)** — First In, First Out, like a line at a cafeteria.

> 🍼 **Easy Version**: Check ALL rooms 1 step away. Then ALL rooms 2 steps away. Then 3. Like ripples in a pond spreading outward.

### 🎪 What is a Queue? (The Ice Cream Shop Story)

This is the MOST IMPORTANT thing to understand about BFS. If you get this, you get BFS!

**Imagine an ice cream shop with ONE counter:**

```
🚪 ENTRANCE (back of line)              COUNTER (front of line) 🍦
                                         
People JOIN the line at the BACK →  →  →  People GET SERVED from the FRONT
```

**Rule 1**: New people ALWAYS join at the BACK of the line.
**Rule 2**: The shop ALWAYS serves the person at the FRONT.
**Rule 3**: The person who arrived FIRST gets served FIRST. (FAIR!)

This is called **FIFO = First In, First Out**.

**Let's watch it happen with names:**

```
Empty shop. Alice arrives:
  Line: [Alice]
         ↑ she's both first AND last

Bob arrives. He joins at the BACK:
  Line: [Alice, Bob]
         ↑front    ↑back

Charlie arrives. He joins at the BACK:
  Line: [Alice, Bob, Charlie]
         ↑front          ↑back

Now the shop SERVES the person at the FRONT → Alice gets ice cream! 🍦
She leaves the line:
  Line: [Bob, Charlie]
         ↑front  ↑back

Diana and Eve arrive (two new people join at the BACK):
  Line: [Bob, Charlie, Diana, Eve]
         ↑front               ↑back

Shop serves the FRONT → Bob gets ice cream! 🍦
  Line: [Charlie, Diana, Eve]
         ↑front          ↑back

Shop serves the FRONT → Charlie gets ice cream! 🍦
  Line: [Diana, Eve]
```

**See the pattern?** People are served in the EXACT ORDER they arrived:
Alice(1st) → Bob(2nd) → Charlie(3rd) → Diana(4th) → Eve(5th)

**Now replace "people" with "rooms to search" and "getting served" with "being explored"!**

### 🔄 How the Queue Makes BFS Work Level-by-Level

Here's the MAGIC. Watch what happens when we use a queue to explore a tree:

```
Our tree:
           Room 1 (START — you are here)
          /        \
      Room 2      Room 3          ← Level 1 (1 step away)
      /    \         \
  Room 4  Room 5   Room 6        ← Level 2 (2 steps away)
             |
          Room 7 (TEDDY! 🧸)     ← Level 3 (3 steps away)
```

**Step 0: You start in Room 1**
```
Queue: [Room1]
       "Rooms I need to check"
```

**Step 1: Check Room 1. Is teddy here? NO.**
"What rooms can I reach from Room 1? Room 2 and Room 3!"
Add them to the BACK of the queue:
```
Queue: [Room2, Room3]
        ↑front        ↑back

These are ALL the rooms that are 1 step away!
```

**Step 2: Check the FRONT of the queue → Room 2. Teddy here? NO.**
"What rooms can I reach from Room 2? Room 4 and Room 5!"
Add them to the BACK:
```
Queue: [Room3, Room4, Room5]
        ↑front              ↑back

Notice: Room3 (Level 1) is AHEAD of Room4 and Room5 (Level 2)!
The queue automatically keeps things in order! 🎉
```

**Step 3: Check FRONT → Room 3. Teddy here? NO.**
"From Room 3, I can reach Room 6."
Add to BACK:
```
Queue: [Room4, Room5, Room6]
        ↑front             ↑back

NOW look — the queue contains ONLY Level 2 rooms!
We finished ALL Level 1 rooms before starting Level 2!
That's the magic of the queue! ✨
```

**Step 4: Check FRONT → Room 4. Teddy here? NO.** Dead end (no new rooms).
```
Queue: [Room5, Room6]
```

**Step 5: Check FRONT → Room 5. Teddy here? NO.**
"From Room 5, I can reach Room 7."
Add to BACK:
```
Queue: [Room6, Room7]
```

**Step 6: Check FRONT → Room 6. Teddy here? NO.** Dead end.
```
Queue: [Room7]
```

**Step 7: Check FRONT → Room 7. TEDDY IS HERE! 🧸🎉**

**Path found by tracing back**: Room1 → Room2 → Room5 → Room7

### 🔑 WHY the Queue Creates Level-by-Level Exploration

```
Step 1-1: Start with level 0        Queue: [1]
Step 1-2: Process level 0           Queue: [2, 3]          ← All of level 1
Step 2-3: Process level 1           Queue: [4, 5, 6]       ← All of level 2
Step 4-6: Process level 2           Queue: [7]             ← All of level 3
Step 7:   Process level 3           Found it!
```

**The secret**: When we process a Level-1 node, its children (Level-2) go to the BACK of the queue. But ALL Level-1 nodes are AHEAD in the queue. So ALL of Level 1 gets processed before ANY of Level 2 starts! This happens automatically at every level!

> 🍼 **The SIMPLEST way to remember**: A Queue is FAIR — first come, first served. Rooms discovered EARLIER get checked FIRST. Since closer rooms are discovered before farther rooms, BFS checks close rooms before far rooms. That's it!

### The BFS Trace Table (Exam Format)

Same tree, now in the table format you'll see on exams:

```
           1
          / \
         2   3
        / \   \
       4   5   6
           |
           7 (GOAL 🎯)
```

| Step | Take from FRONT | Queue After (FRONT → BACK) | Already Visited | What Happened |
|---|---|---|---|---|
| 0 | — | `[1]` | `{}` | Start: put Room 1 in queue |
| 1 | **1** | `[2, 3]` | `{1}` | Room 1 not goal. Found doors to 2, 3. Added to back. |
| 2 | **2** | `[3, 4, 5]` | `{1,2}` | Room 2 not goal. Found doors to 4, 5. Added to back. |
| 3 | **3** | `[4, 5, 6]` | `{1,2,3}` | Room 3 not goal. Found door to 6. Added to back. |
| 4 | **4** | `[5, 6]` | `{1,2,3,4}` | Room 4 not goal. Dead end — no new doors. |
| 5 | **5** | `[6, 7]` | `{1,2,3,4,5}` | Room 5 not goal. Found door to 7. Added to back. |
| 6 | **6** | `[7]` | `{1,2,3,4,5,6}` | Room 6 not goal. Dead end. |
| 7 | **7** | `[]` | all | **FOUND THE TEDDY!** 🧸 Path: 1→2→5→7 |

**Check the expansion order: 1, 2, 3, 4, 5, 6, 7 — perfectly level by level!**
- Level 0: node 1
- Level 1: nodes 2, 3
- Level 2: nodes 4, 5, 6
- Level 3: node 7 ← goal found!

### Properties

| Property | Value | Why? |
|---|---|---|
| **Complete?** | ✅ YES (if b finite) | Systematically visits every depth |
| **Optimal?** | ✅ YES (if all costs = 1) | Shallowest goal = cheapest when costs uniform |
| **Time** | O(b^d) | Visits every node up to depth d |
| **Space** | **O(b^d) ← THE KILLER!** | Stores entire frontier (the bottom level) |

### The Memory Nightmare 😱

| Depth | Nodes (b=10) | Memory (1KB/node) | Time (10K nodes/sec) |
|---|---|---|---|
| 6 | ~10^6 | 1 GB | 2 min |
| 8 | ~10^8 | 103 GB | 3 hours |
| 10 | ~10^10 | **10 TB** | 13 days |
| 12 | ~10^12 | **1 PB** | 3.5 years |

**BFS needs 10 TERABYTES at depth 10!** That's why we need DFS and IDS.

---

## 5. DFS — The Tunnel Digger 🕳️

### How It Works

Uses a **Stack (LIFO)** — Last In, First Out, like a pile of plates.

> 🍼 **Easy Version**: Pick ONE tunnel, walk ALL the way to the dead end. Come back to the last fork, try the next tunnel. Go DEEP before going WIDE.

### 🍽️ What is a Stack? (The Plate Pile Story)

**Imagine a stack of plates at a buffet:**

```
You always put new plates ON TOP.
You always take plates FROM THE TOP.

        ┌─────┐
        │  C  │  ← plate C was added LAST
        ├─────┤
        │  B  │
        ├─────┤
        │  A  │  ← plate A was added FIRST
        └─────┘

Which plate do you grab? C! (the one on TOP — the LAST one added)
That's LIFO = Last In, First Out.
```

**This is the OPPOSITE of a queue!**

```
Queue (FIFO — like a line):  First person in line → first served
Stack (LIFO — like plates):  Last plate on pile  → first grabbed
```

### 🔄 How the Stack Makes DFS Go DEEP

```
Our tree:
           1
          / \
         2   3
        / \   \
       4   5   6
           |
           7 (GOAL 🎯)
```

**Step 0: Put Room 1 on the stack**
```
Stack: [1]      (top is on the left)
```

**Step 1: Take from TOP → Room 1. Teddy? NO.**
Found doors to Room 2 and Room 3. Put them ON TOP:
```
Stack: [2, 3]    ← Room 2 is on top (we'll check it NEXT)
        ↑top
```

**Step 2: Take from TOP → Room 2. Teddy? NO.**
Found doors to Room 4 and Room 5. Put ON TOP:
```
Stack: [4, 5, 3]    ← Room 4 is now on top!
        ↑top

Notice: Room 3 (from Level 1) got BURIED under Rooms 4 and 5 (Level 2)!
DFS will explore 4 and 5 BEFORE ever getting back to 3!
This is what makes DFS go DEEP!
```

**Step 3: Take from TOP → Room 4. Teddy? NO.** Dead end.
```
Stack: [5, 3]
        ↑top
```

**Step 4: Take from TOP → Room 5. Teddy? NO.**
Found door to Room 7. Put ON TOP:
```
Stack: [7, 3]
        ↑top
```

**Step 5: Take from TOP → Room 7. TEDDY! 🧸🎉**
Path: 1→2→5→7

**DFS explored: 1, 2, 4, 5, 7** — went DEEP (1→2→4) before going wide!
Room 3 and Room 6 were NEVER explored! 

### 🔑 Queue vs Stack — The Key Difference (Side by Side)

```
Same tree, two different behaviors:

           1
          / \
         2   3
        / \   \
       4   5   6

BFS (Queue — FIFO):              DFS (Stack — LIFO):
─────────────────────             ─────────────────────
Step 1: Process 1                 Step 1: Process 1
        Queue: [2, 3]                    Stack: [2, 3]

Step 2: Process 2 (FRONT)        Step 2: Process 2 (TOP)
        Queue: [3, 4, 5]                Stack: [4, 5, 3]
                ↑ 3 is NEXT!                    ↑ 4 is NEXT!
                (same level!)                   (deeper level!)

Step 3: Process 3 (FRONT)        Step 3: Process 4 (TOP)
        Queue: [4, 5, 6]                Stack: [5, 3]
        (still level 1!)                 (went even deeper!)

BFS order: 1, 2, 3, 4, 5, 6     DFS order: 1, 2, 4, 5, 7
(level by level)                  (deep into left branch first)
```

> 🍼 **The ONE thing to remember**:
> - **Queue** = new children go to the BACK (behind same-level siblings) → **level by level**
> - **Stack** = new children go to the TOP (in front of everything else) → **deep first**

### Full Trace

```
           1
          / \
         2   3
        / \   \
       4   5   6
           |
           7 (GOAL 🎯)
```

| Step | Pop | Stack After | Explored |
|---|---|---|---|
| 0 | — | `[1]` | `{}` |
| 1 | **1** | `[2, 3]` | `{1}` |
| 2 | **2** | `[4, 5, 3]` | `{1,2}` |
| 3 | **4** | `[5, 3]` | `{1,2,4}` |
| 4 | **5** | `[7, 3]` | `{1,2,4,5}` |
| 5 | **7** | `[3]` | `{1,2,4,5,7}` | **GOAL!** 🎯 |

**Expansion order: 1, 2, 4, 5, 7 — goes DEEP down the left branch first!**
Notice: nodes 3 and 6 were never even explored!

### DFS Can Fail!

```
A → B → C → D → E → ... (infinite chain!)
A → GOAL

DFS goes: A, B, C, D, E, F, ... forever down the infinite chain!
Never even TRIES the A→GOAL path! 😱
```

### Properties

| Property | Value | Why? |
|---|---|---|
| **Complete?** | ❌ NO | Can go infinitely deep down wrong path |
| **Optimal?** | ❌ NO | Might find deep goal when shallow one exists |
| **Time** | O(b^m) | m = max depth (could be >> d) |
| **Space** | **O(b·m) ← THE SUPERPOWER!** | Only stores current path + siblings |

**DFS's space = LINEAR!** For b=10, m=100: only ~1000 nodes in memory vs BFS's astronomical numbers!

---

## 6. Depth-Limited Search (DLS)

### The Idea

DFS with a **depth limit L**. Won't go deeper than L levels.

> 🍼 "You can explore at most L tunnels deep. If no treasure, come back!"

```
function DLS(problem, limit):
    return RECURSIVE_DLS(initial_node, problem, limit)

function RECURSIVE_DLS(node, problem, limit):
    if is_goal(node): return SUCCESS
    if limit == 0: return CUTOFF     ← Can't go deeper!
    
    cutoff_occurred = false
    for each child of node:
        result = RECURSIVE_DLS(child, problem, limit - 1)
        if result == CUTOFF: cutoff_occurred = true
        else if result ≠ FAILURE: return result
    
    return CUTOFF if cutoff_occurred else FAILURE
```

**Problem**: How to choose L? If L < d → miss the goal. If L >> d → waste time like DFS.

**Solution**: Try ALL limits! → IDS

---

## 7. Iterative Deepening Search (IDS) 🏆

### The BEST Default Strategy!

```
function IDS(problem):
    for limit = 0, 1, 2, 3, ...:
        result = DLS(problem, limit)
        if result ≠ CUTOFF: return result
```

> 🍼 "Teddy, are you 0 doors away?" No. "1 door?" No. "2 doors?" No. "3 doors?" YES! Found you!

### Detailed Trace

```
           A
          / \
         B   C
        / \
       D   E
           |
           G (GOAL at depth 3)
```

**Limit=0**: Check A only → Not goal → CUTOFF

**Limit=1**: Check A → expand → check B, C → Not goal → CUTOFF

**Limit=2**: Check A → B → D(leaf), E(limit reached!) → C(leaf) → CUTOFF

**Limit=3**: Check A → B → D(leaf) → E → **G → GOAL!** 🎯

### "Isn't re-expansion wasteful?"

**The stunning math** for b=10, d=5:

```
BFS total:       1 + 10 + 100 + 1000 + 10,000 + 100,000 = 111,111

IDS total:
  Limit 0:       1
  Limit 1:       1 + 10 = 11
  Limit 2:       1 + 10 + 100 = 111
  Limit 3:       1 + 10 + 100 + 1,000 = 1,111
  Limit 4:       1 + 10 + 100 + 1,000 + 10,000 = 11,111
  Limit 5:       1 + 10 + 100 + 1,000 + 10,000 + 100,000 = 111,111
  ────────────────────────────────────────────────────────────
  Grand total:   123,456
```

**IDS does only 11% more work than BFS!** The bottom level dominates — like a pyramid where the base is enormous and re-building the tiny top costs almost nothing.

### Properties (THE CHAMPION! 🏆)

| Property | Value | Combines best of... |
|---|---|---|
| **Complete?** | ✅ YES | ...BFS |
| **Optimal?** | ✅ YES (uniform costs) | ...BFS |
| **Time** | O(b^d) | ...BFS |
| **Space** | O(b·d) | ...DFS! |

> **IDS = BFS quality + DFS memory!** This is the GO-TO uninformed search when you don't know the solution depth.

---

## 8. Uniform Cost Search (UCS) 💰

### Why UCS?

BFS finds shallowest goal. But what if edges have DIFFERENT costs?

```
     1         100
A ────→ B ────→ GOAL     (cost = 101)
A ────→ GOAL              (cost = 50)
   50

BFS finds A→B→GOAL (2 steps) first! But A→GOAL (1 step, cost 50) is CHEAPER!
```

UCS always expands the node with the **lowest total path cost g(n)**.

### Data Structure: Priority Queue

Always dequeues the CHEAPEST element:
```
PQ: [(cost=2, Sibiu), (cost=5, Tim), (cost=7, Zerind)]
Dequeue → Sibiu (cheapest!)
```

### ⚠️ CRITICAL: Goal Test at EXPANSION, Not Generation!

```
     1         1
A ────→ B ────→ GOAL     (total: 2)
A ────→ GOAL              (total: 3)
   3

If goal-test at GENERATION:
  Expand A → generate B(1), GOAL(3) → "Found GOAL with cost 3!" WRONG!

If goal-test at EXPANSION:
  Expand A → frontier: [B(1), GOAL(3)]
  Expand B(1) → generate GOAL(2) → frontier: [GOAL(2), GOAL(3)]
  Expand GOAL(2) → "Found GOAL with cost 2!" CORRECT! ✅
```

### Full UCS Trace: Romania Map

**Goal**: Arad → Bucharest

| Step | Expand | g(n) | Frontier (sorted by cost) |
|---|---|---|---|
| 1 | Arad | 0 | Zerind(75), Timisoara(118), Sibiu(140) |
| 2 | Zerind | 75 | Timisoara(118), Sibiu(140), Oradea(146) |
| 3 | Timisoara | 118 | Sibiu(140), Oradea(146), Lugoj(229) |
| 4 | Sibiu | 140 | Oradea(146), RV(220), Lugoj(229), Fagaras(239) |
| 5 | Oradea | 146 | RV(220), Lugoj(229), Fagaras(239) |
| 6 | RV | 220 | Lugoj(229), Fagaras(239), Pitesti(317), Craiova(366) |
| 7 | Lugoj | 229 | Fagaras(239), Mehadia(299), Pitesti(317), Craiova(366) |
| 8 | Fagaras | 239 | Mehadia(299), Pitesti(317), Craiova(366), **Buch(450)** |
| 9 | Mehadia | 299 | Pitesti(317), Craiova(366), Dobreta(374), Buch(450) |
| 10 | Pitesti | 317 | Craiova(366), Dobreta(374), **Buch(418)**, Buch(450) |
| 11 | Craiova | 366 | Dobreta(374), **Buch(418)**, Buch(450) |
| 12 | Dobreta | 374 | **Buch(418)**, Buch(450) |
| 13 | **Bucharest** | **418** | **GOAL!** 🎯 |

**Path**: Arad→Sibiu→RV→Pitesti→Bucharest = **418 km** ✅

Bucharest was first generated at step 8 (cost 450 via Fagaras), but we DIDN'T stop! We found the cheaper path (418 via Pitesti) later.

### UCS Properties

| Property | Value |
|---|---|
| **Complete?** | ✅ YES (if step costs ≥ ε > 0) |
| **Optimal?** | ✅ **ALWAYS YES!** |
| **Time** | O(b^(1+⌊C*/ε⌋)) |
| **Space** | O(b^(1+⌊C*/ε⌋)) |

### BFS vs UCS

BFS is just UCS where all costs = 1. UCS is the general version!

---

## 9. Bidirectional Search 🤝

Search from BOTH start AND goal simultaneously. Meet in the middle!

> 🍼 You and your friend both search for each other in the maze. When your search areas overlap — found each other!

**Speed**: O(b^(d/2)) instead of O(b^d). For b=10, d=6: 2,000 nodes vs 1,000,000!

**Requirement**: Must be able to search BACKWARDS from the goal.

---

## 10. The Grand Comparison Table

| Strategy | Complete? | Optimal? | Time | Space | Data Structure |
|---|---|---|---|---|---|
| **BFS** | ✅ | ✅ (uniform) | O(b^d) | O(b^d) | Queue |
| **DFS** | ❌ | ❌ | O(b^m) | **O(bm)** | Stack |
| **DLS** | ❌ | ❌ | O(b^L) | O(bL) | Stack |
| **IDS** | ✅ | ✅ (uniform) | O(b^d) | **O(bd)** | Stack |
| **UCS** | ✅ | ✅ **always** | O(b^⌊C*/ε⌋) | O(b^⌊C*/ε⌋) | Priority Queue |

### Decision Guide

```
Uniform costs + unknown depth → IDS ★
Non-uniform costs            → UCS
Just need ANY solution       → DFS
Can search backwards         → Bidirectional
```

---

## 11. Worked Exam Problems

### Problem 1: BFS on a Graph

```
S ── A ── C ── G(GOAL)
|    |
B ── D
```

| Step | Dequeue | Queue | Explored |
|---|---|---|---|
| 1 | S | [A, B] | {S} |
| 2 | A | [B, C, D] | {S,A} |
| 3 | B | [C, D] | {S,A,B} |
| 4 | C | [D, G] | {S,A,B,C} |
| 5 | D | [G] | {S,A,B,C,D} |
| 6 | **G** | [] | **GOAL!** Path: S→A→C→G |

### Problem 2: UCS on Weighted Graph

```
     2       3
S ──── A ──── G     S-A: 2, A-G: 3
|                    S-B: 1, B-C: 1, C-D: 1, D-G: 1
|1    1     1
B ── C ── D ── G
```

| Step | Expand | g(n) | Frontier |
|---|---|---|---|
| 1 | S | 0 | B(1), A(2) |
| 2 | B | 1 | A(2), C(2) |
| 3 | A | 2 | C(2), G(5) |
| 4 | C | 2 | D(3), G(5) |
| 5 | D | 3 | **G(4)**, G(5) |
| 6 | **G** | **4** | **GOAL!** Path: S→B→C→D→G ✅ |

Not S→A→G (cost 5)! UCS found the cheaper path!

---

## 12. Key Takeaways

1. **BFS** = Queue → level by level → shallowest goal → but memory monster 🐉
2. **DFS** = Stack → deep first → saves memory → but can get lost forever 😵
3. **IDS** = DFS at increasing limits → **BFS quality + DFS memory = USE THIS!** 🏆
4. **UCS** = Priority Queue → cheapest path → **goal test at EXPANSION** → always optimal 💰
5. **IDS overhead is only ~11%** — practically free!
6. **BFS is UCS with all costs = 1**

---

## 13. Exam Tips

### Top Mistakes

❌ Using min() for BFS queue (BFS uses FIFO, not priority!)
❌ Saying DFS is complete (it's NOT in infinite spaces!)
❌ Testing UCS goal at generation (must be at EXPANSION!)
❌ Confusing depth d with max depth m
❌ Forgetting that IDS re-expands nodes (but it's efficient!)

### Memory Tricks

- **B**FS = **B**road = **Q**ueue (first come first served)
- **D**FS = **D**eep = **S**tack (last in first out)
- **U**CS = cheapest first = **P**riority **Q**ueue

---

## 📖 References

- AIMA — Chapter 3
- [MIT AI Lectures](https://www.youtube.com/playlist?list=PLUl4u3cNGP63gFHB6xb-kVBiQHYe_4hSi)
- [Stanford CS221](https://www.youtube.com/playlist?list=PLoROMvodv4rO1NB9TD4iUZ3qghGEGtqNX)

---

[⬅️ Back to Main](../README.md) | [Next: Informed Search (Greedy & A*) ➡️](../02_Search_Informed_Greedy_Astar/README.md)
