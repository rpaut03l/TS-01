# AI QUIZ MASTER CHEAT SHEET
**Slides 1-86 Complete Reference | Dr: RB-M**

---

## 📑 Table of Contents
1. [Search Problem Formulation (Slides 1-10)](#section-1-search-problem-formulation)
2. [Uninformed Search - BFS & DFS (Slides 11-25)](#section-2-uninformed-search---bfs--dfs)
3. [Uninformed Search - UCS, DLS, IDS (Slides 26-35)](#section-3-uninformed-search---ucs-dls-ids)
4. [Complexity Comparison (Slides 36-40)](#section-4-complexity-comparison-table)
5. [Heuristic Functions (Slides 41-50)](#section-5-heuristic-functions)
6. [A* Algorithm & Admissibility (Slides 51-60)](#section-6-a-algorithm--admissibility)
7. [Consistency & Dominance (Slides 51-60 continued)](#section-7-consistency--dominance)
8. [Memory-Bounded Heuristics (Slides 61-65)](#section-8-memory-bounded-heuristics)
9. [Local Search - Hill Climbing (Slides 66-75)](#section-9-local-search---hill-climbing)
10. [Simulated Annealing (Slides 66-75 continued)](#section-10-simulated-annealing)
11. [Genetic Algorithms (Slides 76-82)](#section-11-genetic-algorithms)
12. [Local Search Comparison (Slides 83-86)](#section-12-local-search-comparison)
13. [AND-OR Search Trees (Slides 83-86)](#section-13-and-or-search-trees)

---

## SECTION 1: SEARCH PROBLEM FORMULATION
**Coverage: Slides 1-10**

### 🎯 MNEMONIC: "SAGI-H"

- **S** - State Space (all possible configurations)
- **A** - Actions/Operators (moves between states)
- **G** - Goal Test (condition to check success)
- **I** - Initial State (starting point)
- **H** - Heuristic (optional - for informed search)

### 📌 Example 1: Romania Travel Problem

- **State:** Current city name
- **Actions:** Drive(city1, city2)
- **Goal:** InCity(Bucharest)
- **Initial:** InCity(Arad)
- **Heuristic:** StraightLineDistance(current, Bucharest)

### 📌 Example 2: Water Jug Problem

- **State:** (x, y) where x=gal in 3-jug, y=gal in 4-jug
- **Actions:** Fill(jug), Empty(jug), Pour(jug1, jug2)
- **Goal:** (x, 2) - get exactly 2 gallons in 4-gallon jug
- **Initial:** (0, 0) - both empty

### 🔑 Key Concepts

- **Solution:** Sequence of actions from Initial to Goal
- **Path Cost:** g(n) = sum of action costs
- **State Space Graph:** Nodes=states, Edges=actions

---

## SECTION 2: UNINFORMED SEARCH - BFS & DFS
**Coverage: Slides 11-25**

### 🎯 MNEMONIC: "BUD-DI Searches Blindly"

- **B** - Breadth-First Search
- **U** - Uniform-Cost Search
- **D** - Depth-First Search
- **D** - Depth-Limited Search
- **I** - Iterative-Deepening Search

---

### 🍔 BREADTH-FIRST SEARCH (BFS)

**Visual:** Burger Line (Queue - FIFO)  
**Mnemonic:** "Big Fat Storage Queen"

#### Data Structure: QUEUE (First In First Out)

```
┌───┬───┬───┬───┐
│ A │ B │ C │🍔│ → Remove from front
└───┴───┴───┴───┘
  ↑ Add to back
```

#### Algorithm:
1. OPEN = [start]
2. Remove FIRST from OPEN (FIFO)
3. If GOAL → return path
4. Add children to END of OPEN
5. Repeat from step 2

#### Properties: "COTS"
- ✅ **Complete:** YES (finds solution if exists)
- ✅ **Optimal:** YES* (only for uniform cost!)
- ⏱️ **Time:** O(b^d) - exponential
- 💾 **Space:** O(b^d) - HUGE! 💥

**Where:** b = branching factor, d = depth of goal

#### ⚠️ QUIZ TRAP
**Q:** "Is BFS always optimal?"  
**A:** NO! Only for UNIFORM cost. Use UCS for varying costs.

---

### 📚 DEPTH-FIRST SEARCH (DFS)

**Visual:** Book Stack (Stack - LIFO)  
**Mnemonic:** "Deep Diver, Small Bag"

#### Data Structure: STACK (Last In First Out)

```
  ║ C ║ ← Remove from top
  ║ B ║
  ║ A ║
  ╚═══╝
    ↑ Add to top
```

#### Algorithm:
1. OPEN = [start]
2. Remove LAST from OPEN (LIFO)
3. If GOAL → return path
4. Add children to FRONT of OPEN
5. Repeat from step 2

#### Properties: "COTS"
- ❌ **Complete:** NO (can loop infinitely)
- ❌ **Optimal:** NO
- ⏱️ **Time:** O(b^m) - exponential in max depth
- 💾 **Space:** O(bm) - LINEAR! ⭐ BEST SPACE

**Where:** m = maximum depth of tree

#### ⚠️ QUIZ TRAP
**Q:** "DFS saves space, so use it always?"  
**A:** NO! Not complete - might never find solution.

---

### 💡 MEMORY TRICK: "Q-S" (Queue-Stack)
- BFS = **Q** for Queue
- DFS = **S** for Stack

---

## SECTION 3: UNINFORMED SEARCH - UCS, DLS, IDS
**Coverage: Slides 26-35**

---

### 🏆 UNIFORM-COST SEARCH (UCS)

**Visual:** VIP Priority Line  
**Mnemonic:** "Use Cost to Sort"

#### Data Structure: PRIORITY QUEUE (by path cost g(n))

```
[3:A] [5:B] [8:C] → Always remove lowest cost
  ↑ lowest
```

#### Algorithm:
1. OPEN = [(start, cost=0)]
2. Remove LOWEST COST from OPEN
3. If GOAL → return path
4. For each child:
   - g(child) = g(parent) + edge_cost
   - Add (child, g(child)) to OPEN
5. Repeat from step 2

#### 🔑 KEY FORMULA:

```
┌──────────────────────────────────┐
│ g(child) = g(parent) + cost(edge)│
└──────────────────────────────────┘
```

#### Properties:
- ✅ **Complete:** YES (if step cost > ε > 0)
- ✅ **Optimal:** ALWAYS ✓ (no conditions!)
- ⏱️ **Time:** O(b^d)
- 💾 **Space:** O(b^d)

#### Difference from BFS:
- **BFS** → expands by DEPTH
- **UCS** → expands by COST (cheapest first)

#### ⚠️ QUIZ TRAP
**Q:** "When to use UCS vs BFS?"  
**A:** Varying edge costs → UCS. Uniform costs → BFS/IDS.

---

### 📏 DEPTH-LIMITED SEARCH (DLS)

**Concept:** DFS with maximum depth limit L

#### Algorithm:
DFS but stop at depth L

#### Properties:
- ❌ **Complete:** NO (only if solution at depth ≤ L)
- ❌ **Optimal:** NO
- ⏱️ **Time:** O(b^L)
- 💾 **Space:** O(bL)

**Use Case:** When you know maximum depth

---

### 🪜 ITERATIVE DEEPENING SEARCH (IDS) ⭐⭐ MOST IMPORTANT!

**Visual:** Climb Ladder (one step at a time)  
**Mnemonic:** "Increment Depth Slowly"

#### Algorithm:

```python
for depth_limit = 0, 1, 2, 3, ... ∞:
    result = DLS(depth_limit)
    if result found:
        return result
```

#### Visual Process:
- **Depth 0:** Check root only
- **Depth 1:** Check root + children
- **Depth 2:** Check root + children + grandchildren
- ...until goal found

#### Properties: "COTS"
- ✅ **Complete:** YES
- ✅ **Optimal:** YES* (for uniform cost)
- ⏱️ **Time:** O(b^d)
- 💾 **Space:** O(bd) ← AMAZING! ⭐⭐

#### WHY IDS IS THE BEST:
✓ BFS optimality (finds shallowest)  
✓ DFS space efficiency (linear memory)  
✓ Best of both worlds!

#### ⚠️ QUIZ TRAP
**Q:** "IDS wastes time repeating?"  
**A:** Only ~11% overhead! Saves EXPONENTIAL space.

**Example:** For b=10, d=5:
- BFS: 100,000 nodes in memory
- IDS: 50 nodes in memory (2000x better!)

---

## SECTION 4: COMPLEXITY COMPARISON TABLE
**Coverage: Slides 36-40** ⭐ MEMORIZE!

| Algo | Data Structure | Complete | Optimal | Time    | Space   | Best For      |
|------|---------------|----------|---------|---------|---------|---------------|
| BFS  | Queue         | ✓        | ✓*      | O(b^d)  | O(b^d)💥 | Shallowest    |
| UCS  | Priority      | ✓        | ✓       | O(b^d)  | O(b^d)💥 | Varying cost  |
| DFS  | Stack         | ✗        | ✗       | O(b^m)  | O(bm)⭐  | Memory limit  |
| DLS  | Stack         | ✗        | ✗       | O(b^L)  | O(bL)    | Known depth   |
| IDS  | Stack         | ✓        | ✓*      | O(b^d)  | O(bd)⭐⭐ | Unknown depth |

**\*Optimal for uniform cost only**

### 📝 Notation:
- **b** = branching factor (avg children per node)
- **d** = depth of shallowest goal
- **m** = maximum depth of tree
- **L** = depth limit

### 💡 MEMORY TRICK: "Q-S-P-S-S"
BFS=Queue, DFS=Stack, UCS=Priority, DLS=Stack, IDS=Stack

### 🔑 KEY INSIGHT:

**Exponential O(b^d) vs Linear O(bd) is MASSIVE!**

**Example:** b=10, d=12
- **BFS:** 10^12 = 1 TRILLION nodes 💀
- **IDS:** 120 nodes ✓ (8 billion times better!)

---

## SECTION 5: HEURISTIC FUNCTIONS
**Coverage: Slides 41-50**

### 📖 Definition:

```
┌──────────────────────────────────────────────┐
│ h(n) = Estimated cost from node n to goal   │
│                                              │
│ Visual: 🧭 Compass pointing to treasure      │
└──────────────────────────────────────────────┘
```

### ✅ Requirements:
1. **h(goal) = 0** ← ALWAYS! (at goal, no cost remaining)
2. **h(n) ≥ 0** ← Non-negative for all nodes
3. **Domain-specific** (depends on problem)

---

### 📌 Common Heuristics

#### 1️⃣ ROMANIA PROBLEM: Straight-Line Distance

**h(n) = Euclidean distance from current city to Bucharest**

```
City A 📍━━━━━━━━━━🏁 Bucharest
         ↑ straight line
```

**Why admissible?** Roads ≥ straight line (can't go through buildings)

---

#### 2️⃣ 8-PUZZLE: Two Common Heuristics

##### h₁ = Number of Misplaced Tiles

```
Current:  [1 2 3]    Goal: [1 2 3]
          [4 _ 6]          [4 5 6]
          [7 5 8]          [7 8 _]

Misplaced: 5, 6, 8 → h₁ = 3 tiles wrong
```

##### h₂ = Manhattan Distance (Sum of distances)

**For each tile:** |x_current - x_goal| + |y_current - y_goal|

**Example for tile 5:**
- Current position: (2, 1)
- Goal position: (1, 1)
- Distance = |2-1| + |1-1| = 1

Sum for all tiles → h₂

**KEY FACT:** h₂ dominates h₁ (h₂ ≥ h₁ for all states, so h₂ is more informed)

---

### 📐 MANHATTAN DISTANCE FORMULA ⭐ MEMORIZE!

```
┌────────────────────────────────────┐
│ h = |x₁ - x₂| + |y₁ - y₂|        │
└────────────────────────────────────┘
```

**Visual:** Taxi-cab distance 🚕

```
    (x₁,y₁)
       ┌─────┐
       │  →  │ horizontal: |x₁-x₂|
       └──┐  │
          ↓  │ vertical: |y₁-y₂|
          └──┘
        (x₂,y₂)
```

**Example:** (1,2) to (4,6)
= |1-4| + |2-6| = 3 + 4 = **7**

---

### 🎯 MNEMONIC: "ACORN" for Heuristic Properties

- **A** - Admissible (h ≤ h*)
- **C** - COnsistent (triangle inequality)
- **O** - Optimistic (never overestimate)
- **R** - Remain non-negative
- **N** - Null at goal (h(goal) = 0)

---

## SECTION 6: A* ALGORITHM & ADMISSIBILITY
**Coverage: Slides 51-60** ⭐⭐⭐

### 🌟 A* SEARCH - THE BEST INFORMED ALGORITHM

#### EVALUATION FUNCTION ⭐ MOST IMPORTANT FORMULA!

```
┌─────────────────────────────────┐
│                                 │
│      f(n) = g(n) + h(n)        │
│             ↑       ↑           │
│           past   future         │
│           cost   estimate       │
│                                 │
└─────────────────────────────────┘
```

**Where:**
- **g(n)** = actual cost from start to node n
- **h(n)** = estimated cost from n to goal
- **f(n)** = estimated total cost through n

#### Visual Analogy: GPS Navigation 🧭

```
START ━━━━━━━ YOU ━━━━━━━ GOAL
       g(n)          h(n)
    (distance      (distance
     traveled)     remaining)
```

---

### 🔄 Algorithm:

1. OPEN = [(start, g=0, h=h(start), f=h(start))]
2. Remove node with LOWEST f(n) from OPEN
3. If node is GOAL → return path
4. For each child of node:
   - g(child) = g(node) + cost(node → child)
   - h(child) = heuristic(child)
   - f(child) = g(child) + h(child)
   - Add to OPEN (or update if better path found)
5. Repeat from step 2

---

### 📊 Properties:

- ✅ **Complete:** YES
- ✅ **Optimal:** YES (if h is admissible)
- ⏱️ **Time:** O(b^d)
- 💾 **Space:** O(b^d) ← Main drawback

---

### 🎯 ADMISSIBLE HEURISTIC ⭐ CRUCIAL CONCEPT

**Definition:** "Never Overpromise" 🤥❌

```
┌──────────────────────────────────┐
│  h(n) ≤ h*(n)  for ALL nodes n  │
└──────────────────────────────────┘
```

**Where:** h*(n) = true optimal cost from n to goal

**Meaning:** Heuristic NEVER OVERESTIMATES actual cost

#### Visual: Speed Limit Analogy

```
┌───────────────────────────┐
│  [55 mph] ← Your estimate │
│     ≤                      │
│  [60 mph] ← Actual limit  │
│                            │
│  55 ≤ 60 ✓ Admissible!    │
└───────────────────────────┘
```

#### WHY IT MATTERS:
**If h is admissible → A* finds OPTIMAL solution**

#### ⚠️ QUIZ TRAP
**Q:** "Can A* with inadmissible h find optimal?"  
**A:** YES, by luck! But NOT GUARANTEED. Admissibility GUARANTEES optimality.

---

### 🏃💨 GREEDY BEST-FIRST SEARCH (for comparison)

**Evaluation:** f(n) = h(n) ONLY (ignores g!)

**Visual:** "Sprint to goal blindly"

#### Properties:
- ❌ **Complete:** NO (can loop)
- ❌ **Optimal:** NO (ignores path cost)
- ⚡ **Fast but risky**

#### Difference from A*:
- **Greedy** = h only → Can be misled
- **A*** = g + h → Balanced, optimal

---

## SECTION 7: CONSISTENCY & DOMINANCE
**Coverage: Slides 51-60 continued**

### 📐 CONSISTENT (MONOTONIC) HEURISTIC ⭐ STRONGER PROPERTY

**Definition:** "Triangle Inequality"

```
┌──────────────────────────────────────────┐
│  h(n) ≤ c(n, a, n') + h(n')             │
│  for all n, a, n'                        │
└──────────────────────────────────────────┘
```

**Where:** c(n, a, n') = cost of action a from n to n'

#### Visual Triangle:

```
      n
     /|\
  h / | \ c(n,a,n')
   /  |  \
  /   |   \
 G    |    n'
      | h(n')
```

**Meaning:** Estimated cost from n cannot be more than (actual step cost + estimate from next node)

---

### 🔗 RELATIONSHIP WITH ADMISSIBILITY:

```
┌──────────────────────────────────────┐
│  Consistent → Admissible (ALWAYS) ✓ │
│  Admissible ↛ Consistent (NOT) ✗    │
└──────────────────────────────────────┘
```

**Mnemonic:** "C before A in alphabet" (Consistent is stronger, implies Admissible)

---

### 🎯 KEY CONSEQUENCE:

If h is consistent:
- f-values are NON-DECREASING along any path
- A* never re-expands nodes (with graph search)
- First path to goal is optimal

---

### 📈 DOMINANCE

**Definition:** h₂ dominates h₁ if:

```
┌────────────────────────────────┐
│  h₂(n) ≥ h₁(n) for ALL n      │
│  AND both are admissible       │
└────────────────────────────────┘
```

**Consequence:**
- h₂ is MORE INFORMED
- A* with h₂ expands FEWER nodes

**Example (8-Puzzle):**
- h₁ = Misplaced tiles
- h₂ = Manhattan distance

For any state: h₂(n) ≥ h₁(n)  
Therefore: h₂ dominates h₁  
**Result:** Use h₂ for better performance!

---

## SECTION 8: MEMORY-BOUNDED HEURISTICS
**Coverage: Slides 61-65**

**Problem:** A* uses O(b^d) space - too much for large problems!  
**Solution:** Memory-bounded variants

---

### 🔄 ITERATIVE DEEPENING A* (IDA*)

**Concept:** IDS + A* = IDA*

#### Algorithm:

```python
threshold = h(start)
while True:
    result = DFS with f-cost limit = threshold
    if result is goal:
        return result
    if result is ∞:
        return failure
    threshold = minimum f-cost that exceeded limit
```

#### Difference from IDS:
- **IDS:** Cutoff by DEPTH
- **IDA*:** Cutoff by F-COST

#### Properties:
- ✅ **Complete:** YES
- ✅ **Optimal:** YES (if h admissible)
- ⏱️ **Time:** Similar to A*
- 💾 **Space:** O(bd) ⭐ BEST!

**Use when:** Large search space, limited memory

---

### 🔁 RECURSIVE BEST-FIRST SEARCH (RBFS)

**Key Idea:** Remember f-value of best alternative path

#### Properties:
- ✅ **Complete:** YES
- ✅ **Optimal:** YES (if h admissible)
- 💾 **Space:** O(bd) ⭐
- ⚠️ May re-expand nodes (unlike A*)

#### Comparison:
- **IDA*** = Simpler, easier to understand
- **RBFS** = More sophisticated, less re-expansion

---

## SECTION 9: LOCAL SEARCH - HILL CLIMBING
**Coverage: Slides 66-75**

**Philosophy:** Don't care about PATH, only SOLUTION  
**Applications:** Optimization in HUGE spaces (>10^30,000 states)

### 🎯 MNEMONIC: "HiSaGa - High School Saga"

- **Hi** - Hill Climbing
- **Sa** - Simulated Annealing
- **Ga** - Genetic Algorithm

---

### 🧗 HILL CLIMBING

**Visual:** Climb nearest peak  
**Mnemonic:** "Greedy Local Search"

#### State-Space Landscape:

```
     ⛰️ Local Max              🏔️ Global Max
     /\    (STUCK!)             /\
    /  \                       /  \
   /    \________             /    \
  /              \___________/      \
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ↑ Start here
```

#### Algorithm:

```python
current = initial_state
loop:
    neighbor = highest_valued_neighbor(current)
    if neighbor.value ≤ current.value:
        return current  # Local maximum reached
    current = neighbor
```

---

### ⚠️ PROBLEMS: "LRP" ⭐ MEMORIZE!

#### L - Local Maxima
Gets stuck on small peaks, can't see higher ones

#### R - Ridges
Long, flat slopes that are difficult to navigate

#### P - Plateaus (two types)
- **Shoulders:** Flat regions with upward exit
- **Flat maxima:** Flat regions at peak

---

### 📊 Properties:

- ❌ **Complete:** NO (gets stuck)
- ❌ **Optimal:** NO (local maximum ≠ global)
- 💾 **Memory:** O(1) - single state ⭐
- ⚡ **Speed:** FAST

---

### 🔀 Variants:

#### 1. Stochastic Hill Climbing
- Pick random uphill move
- Less optimal but faster

#### 2. First-Choice Hill Climbing
- Generate neighbors randomly
- Accept first improvement
- Good for large branching factor

#### 3. Random-Restart Hill Climbing
- Try multiple random starts
- Pick best result
- Increases chance of finding global max

---

## SECTION 10: SIMULATED ANNEALING
**Coverage: Slides 66-75 continued**

### 🔥❄️ SIMULATED ANNEALING (SA)

**Visual:** Temperature Chef  
**Mnemonic:** "Sometimes Accept Worse"

**Key Idea:** Accept worse moves with probability to escape local max

---

### ⭐ ACCEPTANCE FORMULA - MOST IMPORTANT!

```
┌────────────────────────────────┐
│  P(accept worse) = e^(ΔE/T)   │
└────────────────────────────────┘
```

**Where:**
- **ΔE** = new_value - current_value (negative if worse)
- **T** = temperature (decreases over time)

**Mnemonic:** "e to the Delta E over T"

---

### 🔄 Algorithm:

```python
current = initial_state
for t = 1 to ∞:
    T = schedule(t)  # Temperature decreases
    if T = 0:
        return current
    next = random_successor(current)
    ΔE = next.value - current.value
    
    if ΔE > 0:  # Better move
        current = next
    else:  # Worse move
        with probability e^(ΔE/T):
            current = next  # Accept anyway!
```

---

### 🌡️ TEMPERATURE CONTROL:

#### High T (early): 🔥
- High probability of accepting worse moves
- EXPLORATION phase
- Jumps around search space

#### Low T (late): ❄️
- Low probability of accepting worse moves
- EXPLOITATION phase
- Converges to solution

---

### 📉 COOLING SCHEDULES ⭐ MEMORIZE AT LEAST ONE!

#### 1. Geometric (Most Common)

```
┌────────────────────────────┐
│ T(k+1) = α × T(k)         │
│ where α ∈ [0.8, 0.99]     │
│ Typical: α = 0.95         │
└────────────────────────────┘
```

#### 2. Linear
T(k) = T₀ - k·ΔT

#### 3. Logarithmic
T(k) = C / ln(k+2)

#### 4. Exponential
T(k) = T₀ × α^k

---

### 🧮 EXAMPLE CALCULATION:

**Given:**
- Current solution value = 100
- New solution value = 90 (worse!)
- Temperature T = 50

**Calculate:**
- ΔE = 90 - 100 = -10
- P = e^(-10/50) = e^(-0.2) ≈ **0.82**

**Interpretation:** 82% chance to accept this worse move!

---

### 📊 Properties:

- ✅ **Complete:** YES (with proper schedule)
- ✅ **Optimal:** Probabilistically YES (given infinite time)
- 💾 **Memory:** O(1) ⭐
- ✅ **Escapes local maxima:** YES

**Use for:** TSP, scheduling, VLSI layout, continuous optimization

---

## SECTION 11: GENETIC ALGORITHMS
**Coverage: Slides 76-82**

### 🧬 GENETIC ALGORITHMS (GA)

**Visual:** Evolution Search  
**Mnemonic:** "GERMS" ⭐ MOST IMPORTANT!

```
┌──────────────────────────────────┐
│ G - Generate initial population  │
│ E - Evaluate fitness             │
│ R - Reproduce (crossover parents)│
│ M - Mutate (random changes)      │
│ S - Select survivors             │
└──────────────────────────────────┘
```

---

### 🔑 KEY CONCEPTS:

#### Individual/Chromosome
Encoded solution  
**Example:** [1,0,1,1,0,1,0,0] (binary string)

#### Gene
Single element of chromosome  
**Example:** Each bit is a gene

#### Population
Set of N individuals  
**Example:** 100 different binary strings

#### Fitness
Quality measure (how good the solution is)  
**Example:** fitness([1,0,1,1,0,1,0,0]) = 8.5

---

### 🔄 Algorithm:

```
1. Generate initial population randomly

2. Repeat until termination:

   a) Evaluate fitness of each individual

   b) Select parents (based on fitness)
      - Roulette wheel, tournament, rank, etc.

   c) Reproduce (crossover)
      - Combine parent chromosomes → children

   d) Mutate offspring (with small probability)
      - Randomly change genes

   e) Form new population from offspring

3. Return best individual found
```

---

### 🎰 SELECTION METHODS:

#### 1. ROULETTE WHEEL SELECTION ⭐

```
┌──────────────────────────────────────┐
│ P(select i) = fitness(i) / Σ(fitness)│
└──────────────────────────────────────┘
```

**Example:**
- Individual A: fitness = 10 → P = 10/25 = **40%**
- Individual B: fitness = 8  → P = 8/25  = **32%**
- Individual C: fitness = 5  → P = 5/25  = **20%**
- Individual D: fitness = 2  → P = 2/25  = **8%**

#### 2. TOURNAMENT SELECTION
- Pick k random individuals
- Select best among them
- Repeat for desired number

---

### 🧬 CROSSOVER (REPRODUCTION):

#### 1. SINGLE-POINT CROSSOVER ⭐

```
┌────────────────────────────┐
│ Parent 1: A B C | D E F    │
│ Parent 2: a b c | d e f    │
│            ↑ cut point     │
│ Child 1:  A B C | d e f    │
│ Child 2:  a b c | D E F    │
└────────────────────────────┘
```

#### 2. TWO-POINT CROSSOVER

```
Parent 1: A B | C D E | F
Parent 2: a b | c d e | f
Child 1:  A B | c d e | F
Child 2:  a b | C D E | f
```

#### 3. UNIFORM CROSSOVER
Randomly pick each gene from either parent

---

### 🧬 MUTATION:

**Probability:** Typically 0.01 to 0.1 (1-10%)

**Binary strings:** Flip bit

```
Before: 1 0 1 1 0 1 0 0
After:  1 0 1 0 0 1 0 0  (4th bit flipped)
             ↑
```

**Purpose:**
- Maintain diversity in population
- Prevent premature convergence
- Escape local optima

---

### 📊 Properties:

- 💾 **Memory:** O(N) where N = population size
- ✅✅ **Escapes local optima:** BEST
- 📈 **Diversity:** HIGH (population-based)
- 🐌 **Speed:** SLOW (many fitness evaluations)
- ⚡ **Parallelizable:** YES

**Use for:** Multi-objective optimization, complex landscapes, feature selection, neural architecture search

---

## SECTION 12: LOCAL SEARCH COMPARISON
**Coverage: Slides 83-86**

| Criterion     | Hill       | SA         | GA         | Key Difference    |
|---------------|------------|------------|------------|-------------------|
| Search Width  | Narrow     | Medium     | Broad      | GA explores most  |
| Accept worse? | NO         | Prob.e^ΔE/T| YES        | HC never does     |
| Escape local? | STUCK      | Escapes    | Avoids     | HC worst          |
| Memory        | O(1)       | O(1)       | O(N)       | GA needs pop      |
| Speed/iter    | Fast⚡     | Medium🚶   | Slow🐌     | HC fastest        |
| Parameters    | Few        | Medium     | Many       | GA most complex   |
| Diversity     | None       | Low        | High       | Population wins   |
| Best for      | Convex     | TSP        | Multi-obj  | Match to problem  |

---

### 📋 DECISION GUIDE:

#### Use HILL CLIMBING when:
✓ Smooth, convex landscape  
✓ Quick prototyping needed  
✓ Local optimum acceptable  
✓ Memory extremely limited

#### Use SIMULATED ANNEALING when:
✓ TSP, scheduling problems  
✓ Single objective  
✓ Rugged landscape with local optima  
✓ Memory limited (can't use GA)

#### Use GENETIC ALGORITHM when:
✓ Multi-objective optimization  
✓ Very complex search space  
✓ Building-block structure exists  
✓ Parallel processing available  
✓ Memory not a constraint

---

## SECTION 13: AND-OR SEARCH TREES
**Coverage: Slides 83-86**

**Context:** Non-deterministic environments (outcomes uncertain)

---

### 🔀 NODE TYPES:

#### OR NODE (○): Pick ANY child to succeed

```
┌──────────────────────────────┐
│ Cost = MIN(children costs)   │
└──────────────────────────────┘
```

**Visual:** 🍕 Pizza toppings  
"Pick Pepperoni OR Mushroom OR Veggie"  
Cost = min($8, $7, $9) = **$7** (choose cheapest)

---

#### AND NODE (⌒): ALL children must succeed

```
┌──────────────────────────────┐
│ Cost = SUM(children costs)   │
└──────────────────────────────┘
```

**Visual:** 🍕🥤🍰 Complete meal  
"Need Pizza AND Drink AND Dessert"  
Cost = $8 + $2 + $3 = **$13** (add all costs)

---

### 🌳 EXAMPLE TREE:

```
          OR (root)
         /  \
       AND   OR
       /\     |
      3  4    5

Solution:
AND node: 3 + 4 = 7
OR nodes: min(7, 5) = 5
Root cost: 5
```

---

### 💡 MEMORY TRICKS:

- **OR** = "Options" → Choose best → **MIN**
- **AND** = "All" → Need everything → **SUM**

---

### ⚠️ QUIZ TRAP
**Q:** "Do AND nodes take minimum?"  
**A:** NO! AND = SUM (need all), OR = MIN (pick best)

---

## 🎯 EMERGENCY QUICK REFERENCE

### Top 25 Must-Know Facts

1. BFS→Queue, DFS→Stack, UCS→Priority, IDS→Stack
2. f(n) = g(n) + h(n) [A* formula]
3. Admissible: h(n) ≤ h*(n)
4. Consistent: h(n) ≤ c(n,a,n') + h(n')
5. Consistent → Admissible (ALWAYS)
6. IDS space: O(bd) ⭐ BEST
7. UCS ALWAYS optimal (no conditions)
8. BFS optimal ONLY for uniform cost
9. DFS NOT complete (infinite loops)
10. Manhattan = |x₁-x₂| + |y₁-y₂|
11. h(goal) = 0 ALWAYS
12. Greedy = h(n) only (NOT optimal)
13. SA formula: P = e^(ΔE/T)
14. Alpha-Beta: prune when α ≥ β
15. AND = SUM, OR = MIN
16. Hill climbing: stuck at local maxima (LRP)
17. GA: GERMS (Generate, Evaluate, Reproduce, Mutate, Select)
18. Roulette wheel: P(i) = fitness(i)/Σfitness
19. IDA*: IDS with f-cost cutoff
20. h₂ dominates h₁ if h₂ ≥ h₁ for all n
21. β-cutoff at MIN, α-cutoff at MAX
22. Search problem: SAGI-H
23. Uninformed: BUD-DI
24. Local search: HiSaGa
25. Heuristics: ACORN

---

### ⚠️ Common Traps

- ❌ "BFS always optimal" → NO (uniform cost only)
- ❌ "Admissible → Consistent" → NO (other way!)
- ❌ "DFS best space so use it" → NO (not complete!)
- ❌ "Higher h is better" → NO (must be ≤ h*)
- ❌ "IDS wastes time" → NO (11% overhead, saves exponential space)
- ❌ "AND nodes take MIN" → NO (AND=SUM, OR=MIN)

---
