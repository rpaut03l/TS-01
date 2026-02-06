# AI SEARCH TECHNIQUES FLASHCARDS

## Card 1: Search in AI - Definition
**QUESTION SIDE**
What is Search in AI?

**ANSWER SIDE**
A computational method for encapsulating hypothetical reasoning about sequences of actions to achieve desired states from initial states, exploring state spaces systematically.

**Mnemonic: STAR**
- **S**tate space exploration
- **T**ransition via actions
- **A**chieve goal states
- **R**easoning method

**Category:** FUNDAMENTAL CONCEPTS
**Difficulty:** BASIC

---

## Card 2: State Space Components
**QUESTION SIDE**
What are the four essential components needed to formulate a search problem?

**ANSWER SIDE**
1. **STATE SPACE**: Computational representation of problem states
2. **ACTIONS**: Transitions between states
3. **INITIAL/START STATE and GOAL**: Starting point and desired condition
4. **HEURISTICS**: Factors to guide search

**Category:** PROBLEM FORMULATION
**Difficulty:** BASIC

---

## Card 3: Search Algorithm Inputs
**QUESTION SIDE**
What are the key inputs required for a search algorithm?

**ANSWER SIDE**
- **Initial state**: Specific starting world state
- **Successor function S(x)**: States reachable from x via single action
- **Goal test**: Function returning true if goal satisfied
- **Action cost function C(x,a,y)**: Cost of moving from x to y using action a

**Category:** ALGORITHM INPUTS
**Difficulty:** BASIC

---

## Card 4: Node Structure in Search
**QUESTION SIDE**
What are the four components of a search node?

**ANSWER SIDE**
- **n.STATE**: Corresponding state in state space
- **n.PARENT**: Node that generated this node
- **n.ACTION**: Action applied to parent
- **n.PATH-COST (g(n))**: Cost from initial state to node

**Category:** DATA STRUCTURES
**Difficulty:** BASIC

---

## Card 5: Critical Properties of Search
**QUESTION SIDE**
What are the four critical properties used to evaluate search algorithms?

**ANSWER SIDE**
1. **Completeness**: Will it always find a solution if one exists?
2. **Optimality**: Will it find the least cost solution?
3. **Time complexity**: How long to find a solution?
4. **Space complexity**: Maximum nodes stored in memory?

**Category:** ALGORITHM EVALUATION
**Difficulty:** BASIC

---

## Card 6: Breadth-First Search (BFS)
**QUESTION SIDE**
What is
∇(x^T x) = ?

**ANSWER SIDE**
∇(x^T x) = 2x

**Mnemonic: SDD**
*Self Dot Doubles*

**Why?**
x^T x = x₁² + x₂² + ... + xₙ²
d/dx₁ = 2x₁, d/dx₂ = 2x₂, ...
∴ ∇ = [2x₁, 2x₂, ..., 2xₙ]^T = 2x

**Use when:**
Finding ∇f when f(x) = ||x||²

⚠ **Don't forget the 2!**

**Category:** GRADIENT FORMULAS
**Difficulty:** BASIC

---

## Card 6: BFS Properties
**QUESTION SIDE**
What are the completeness, optimality, time and space complexity of Breadth-First Search?

**ANSWER SIDE**
- **Completeness**: Yes (finds solution if exists)
- **Optimality**: Finds shortest path, but NOT least cost if actions have varying costs
- **Time Complexity**: O(b^d)
- **Space Complexity**: O(b^d)

Where b = branching factor, d = depth of solution

**Category:** UNINFORMED SEARCH
**Difficulty:** INTERMEDIATE

---

## Card 7: Uniform-Cost Search (UCS)
**QUESTION SIDE**
How does Uniform-Cost Search differ from BFS?

**ANSWER SIDE**
UCS expands nodes in order of **increasing path cost g(n)** instead of depth.
- Frontier = priority queue ordered by lowest path cost
- Finds **optimal solution** when each transition has cost ≥ ε > 0
- Identical to BFS when all actions have same cost

**Category:** UNINFORMED SEARCH
**Difficulty:** INTERMEDIATE

---

## Card 8: UCS Optimality Proof
**QUESTION SIDE**
Why is Uniform-Cost Search optimal?

**ANSWER SIDE**
**Key Lemmas:**
1. If n₂ expanded after n₁, then c(n₁) ≤ c(n₂)
2. When n is expanded, all paths with cost < c(n) already expanded
3. First expansion of state S finds minimal cost path to S

Therefore: When goal path expanded, it must be optimal.

**Category:** UNINFORMED SEARCH
**Difficulty:** ADVANCED

---

## Card 9: Depth-First Search (DFS)
**QUESTION SIDE**
What are the key characteristics and issues of Depth-First Search?

**ANSWER SIDE**
**Characteristics:**
- Explores deepest node first (LIFO/Stack)
- Space: O(bm) where m = maximum depth
- Supports backtracking naturally

**Issues:**
- Not complete (infinite paths in tree-search)
- Not optimal
- Can get stuck in deep paths

**Category:** UNINFORMED SEARCH
**Difficulty:** INTERMEDIATE

---

## Card 10: Depth-Limited Search
**QUESTION SIDE**
What is Depth-Limited Search and why use it?

**ANSWER SIDE**
DFS with pre-specified depth limit D.
- Expands paths only to length D+1
- Handles infinite-path issue
- **Failure modes**: No solution exists OR no solution within depth D
- Useful in resource-constrained environments

**Tradeoff:** May miss solutions deeper than D

**Category:** UNINFORMED SEARCH
**Difficulty:** INTERMEDIATE

---

## Card 11: Iterative Deepening Search (IDS)
**QUESTION SIDE**
How does Iterative Deepening Search work?

**ANSWER SIDE**
Repeatedly applies depth-limited search with increasing depth limits (D = 0, 1, 2, ...).
- **Stop when**: Solution found OR depth-limited search examines all paths (no pruning)
- Combines BFS completeness with DFS space efficiency
- **Preferred** for large spaces with unknown solution depth

**Category:** UNINFORMED SEARCH
**Difficulty:** INTERMEDIATE

---

## Card 12: Heuristic Function Definition
**QUESTION SIDE**
What is a heuristic function h(n)?

**ANSWER SIDE**
h(n) = **Estimated cost** of cheapest path from state at node n to goal state

**Requirements:**
- Domain-specific
- Nonnegative
- h(n) = 0 for goal nodes

**Purpose:** Guide search toward promising nodes without exhaustive exploration

**Category:** INFORMED SEARCH
**Difficulty:** BASIC

---

## Card 13: Admissible Heuristic
**QUESTION SIDE**
What makes a heuristic "admissible"?

**ANSWER SIDE**
h(n) ≤ h*(n) for all n

Where h*(n) = actual cost of optimal path from n to goal

**Properties:**
- Never overestimates
- Optimistic
- Guarantees A* optimality
- h(goal) = 0

**Category:** HEURISTIC PROPERTIES
**Difficulty:** INTERMEDIATE

---

## Card 14: Consistent (Monotone) Heuristic
**QUESTION SIDE**
What is a consistent/monotone heuristic?

**ANSWER SIDE**
Satisfies **triangle inequality**:
h(n₁) ≤ C(n₁, a, n₂) + h(n₂)

For all nodes n₁, n₂ and actions a.

**Key point:** Consistency implies admissibility
**Ensures:** h values never decrease along paths (monotonic)

**Category:** HEURISTIC PROPERTIES
**Difficulty:** ADVANCED

---

## Card 15: Greedy Best-First Search
**QUESTION SIDE**
How does Greedy Best-First Search work and what are its limitations?

**ANSWER SIDE**
Expands node with **lowest h(n)** value (most promising).

**Limitations:**
- Not optimal (greedy → ignores path cost)
- Can be misled by heuristic
- May explore expensive paths that "look close" to goal

**Example:** May choose high-cost path that appears closer to goal

**Category:** INFORMED SEARCH
**Difficulty:** INTERMEDIATE

---

## Card 16: A* Search
**QUESTION SIDE**
What is the A* search evaluation function?

**ANSWER SIDE**
f(n) = g(n) + h(n)

Where:
- **g(n)**: Actual cost from start to n
- **h(n)**: Estimated cost from n to goal
- **f(n)**: Estimated total cost of cheapest solution through n

Always expands node with **lowest f-value**

**Category:** INFORMED SEARCH
**Difficulty:** BASIC

---

## Card 17: A* Optimality
**QUESTION SIDE**
Under what conditions is A* optimal?

**ANSWER SIDE**
A* is optimal when:
1. h(n) is **admissible** (h(n) ≤ h*(n))
2. All transition costs ≥ ε > 0

**Why:** A* explores paths in order of increasing f-cost, ensuring optimal path found before any higher-cost path.

**Category:** INFORMED SEARCH
**Difficulty:** ADVANCED

---

## Card 18: IDA* (Iterative Deepening A*)
**QUESTION SIDE**
How does IDA* differ from A*?

**ANSWER SIDE**
**Cutoff:** f-cost (g+h) instead of depth
- Each iteration: cutoff = smallest f-cost that exceeded previous cutoff
- **Advantage:** Addresses A* space issues (similar to IDS vs BFS)
- **Completeness/Optimality:** Same as A* with admissible h

**Category:** MEMORY-BOUNDED SEARCH
**Difficulty:** INTERMEDIATE

---

## Card 19: RBFS (Recursive Best-First Search)
**QUESTION SIDE**
What is the key mechanism of Recursive Best-First Search?

**ANSWER SIDE**
Stores only **f-limit** (best alternative path f-value) instead of open list.
- Dives deeper until current path exceeds f-limit
- **Backtracking:** Unwinds to stored alternative, updates f-limit
- **Space:** O(bd) vs O(b^d) for A*

**Tradeoff:** May re-expand nodes but saves memory

**Category:** MEMORY-BOUNDED SEARCH
**Difficulty:** ADVANCED

---

## Card 20: Local Search Philosophy
**QUESTION SIDE**
What is the basic philosophy of Local Search methods?

**ANSWER SIDE**
1. Generate initial guess (often random)
2. Assess quality via objective function
3. Move to neighbor states (local modifications)
4. Repeat until goal found or time limit

**Key difference:** No path saved, only current state
**Advantage:** Constant memory, handles huge/infinite spaces

**Category:** LOCAL SEARCH
**Difficulty:** BASIC

---

## Card 21: State-Space Landscape
**QUESTION SIDE**
What are the three main obstacles in hill climbing?

**ANSWER SIDE**
1. **Local maxima**: Peak higher than neighbors but not global maximum
2. **Ridges**: Sequence of local maxima, hard for greedy algorithms
3. **Plateaux**: Flat areas (flat local max OR shoulder)

All can trap greedy hill-climbing algorithms.

**Category:** LOCAL SEARCH
**Difficulty:** INTERMEDIATE

---

## Card 22: Hill Climbing Algorithm
**QUESTION SIDE**
Describe the Hill Climbing algorithm

**ANSWER SIDE**
```
current ← MAKE-NODE(INITIAL-STATE)
loop:
  neighbor ← highest-valued successor of current
  if neighbor.VALUE ≤ current.VALUE:
    return current.STATE
  current ← neighbor
```

**Greedy:** Always moves to best neighbor
**Issue:** Gets stuck at local optima

**Category:** LOCAL SEARCH
**Difficulty:** BASIC

---

## Card 23: Simulated Annealing
**QUESTION SIDE**
What is the key mechanism that allows Simulated Annealing to escape local optima?

**ANSWER SIDE**
Accepts worse solutions with probability:
**P = exp(-ΔE/T)**

Where:
- ΔE = next.VALUE - current.VALUE (negative for worse)
- T = temperature (decreases over time)

**High T:** Accept many worse moves (exploration)
**Low T:** Accept few worse moves (exploitation)

**Category:** LOCAL SEARCH
**Difficulty:** INTERMEDIATE

---

## Card 24: SA Cooling Schedules
**QUESTION SIDE**
Name three common cooling schedules for Simulated Annealing

**ANSWER SIDE**
1. **Geometric**: T_{k+1} = αT_k (0.8 ≤ α ≤ 1)
2. **Linear**: T_k = T_0 - kΔT
3. **Logarithmic**: T_k = C/ln(k+2)

**Tradeoff:** Slower cooling = better exploration but more computation

**Category:** LOCAL SEARCH
**Difficulty:** ADVANCED

---

## Card 25: Genetic Algorithm Components
**QUESTION SIDE**
What are the three main genetic operators in Genetic Algorithms?

**ANSWER SIDE**
1. **Selection**: Choose parents (roulette wheel, tournament)
2. **Crossover**: ABCD & MNOP → ABOP & CDMN
3. **Mutation**: ABCD → ABBC (flip/switch/scramble genes)

**Terminology:**
- Gene: Encoded variable value
- Chromosome: String of genes (solution)

**Category:** LOCAL SEARCH
**Difficulty:** INTERMEDIATE

---

## Card 26: GA Selection - Roulette Wheel
**QUESTION SIDE**
How does Roulette Wheel selection work in Genetic Algorithms?

**ANSWER SIDE**
Selection probability ∝ fitness:
**P(x) = F(x) / Σ F(x)**

**Expected Count** = P(x) × population size

Higher fitness → more likely selected → more offspring

**Alternative:** Tournament selection

**Category:** LOCAL SEARCH
**Difficulty:** INTERMEDIATE

---

## Card 27: AND-OR Search Trees
**QUESTION SIDE**
What is the difference between AND nodes and OR nodes in search trees?

**ANSWER SIDE**
**AND Nodes:** ALL children must be satisfied (conjunction)
- Represents states requiring multiple conditions

**OR Nodes:** AT LEAST ONE child must be satisfied (disjunction)
- Represents states with multiple solution paths
- Cost = minimum child cost

**Category:** NON-DETERMINISTIC SEARCH
**Difficulty:** INTERMEDIATE

---

## Card 28: AO* Algorithm
**QUESTION SIDE**
How does AO* evaluate nodes differently from A*?

**ANSWER SIDE**
For internal nodes, h' is:
- **AND node:** Sum of children's costs
- **OR node:** Minimum child cost

**Traverse:** Follow "current best path" (lowest cost)
**Propagate:** Update h' values backward to root after expansion

**Category:** NON-DETERMINISTIC SEARCH
**Difficulty:** ADVANCED

---

## Card 29: Minimax Algorithm
**QUESTION SIDE**
What is the Minimax principle in adversarial search?

**ANSWER SIDE**
Players alternate turns:
- **MAX player:** Chooses maximum value
- **MIN player:** Chooses minimum value

**Backpropagation:**
- MAX node value = max(children)
- MIN node value = min(children)

**Root value:** Best outcome MAX can guarantee against optimal opponent

**Category:** ADVERSARIAL SEARCH
**Difficulty:** INTERMEDIATE

---

## Card 30: Game Tree Components
**QUESTION SIDE**
What are the key components of a formal game definition?

**ANSWER SIDE**
- **S₀**: Initial state (game setup)
- **PLAYER(s)**: Whose move in state s
- **ACTIONS(s)**: Legal moves in s
- **RESULT(s,a)**: Transition model
- **TERMINAL-TEST(s)**: Is game over?
- **UTILITY(s,p)**: Payoff for player p in terminal state s

**Category:** ADVERSARIAL SEARCH
**Difficulty:** BASIC

---

## Card 31: Alpha-Beta Pruning Concept
**QUESTION SIDE**
What branches does Alpha-Beta pruning eliminate?

**ANSWER SIDE**
**Prunes branches** that cannot affect final minimax decision.

**Alpha (α):** Best MAX value found so far (lower bound for MAX)
**Beta (β):** Best MIN value found so far (upper bound for MIN)

**Prune when:** α ≥ β
(MAX already has better option OR MIN already has better option)

**Category:** ADVERSARIAL SEARCH
**Difficulty:** ADVANCED

---

## Card 32: Tree-Search vs Graph-Search
**QUESTION SIDE**
What is the key difference between Tree-Search and Graph-Search strategies?

**ANSWER SIDE**
**Tree-Search:**
- No explored set
- May revisit states (cycles possible)

**Graph-Search:**
- Maintains explored set
- Adds nodes to frontier only if not in explored/frontier
- Avoids cycles and redundant paths

**Category:** SEARCH STRATEGIES
**Difficulty:** BASIC

---

## Card 33: Complexity Notation
**QUESTION SIDE**
For search complexity, what do b, d, and m represent?

**ANSWER SIDE**
- **b**: Maximum branching factor (max successors of any node)
- **d**: Depth of shallowest solution
- **m**: Maximum depth of search tree

**Example Complexity:**
- BFS time: O(b^d)
- DFS space: O(bm)

**Category:** ALGORITHM ANALYSIS
**Difficulty:** BASIC

---

## Card 34: Frontier vs Explored Set
**QUESTION SIDE**
What is the role of OPEN (Frontier) and CLOSED (Explored) sets in search?

**ANSWER SIDE**
**OPEN (Frontier):**
- Nodes available for expansion
- Leaf nodes of current search tree

**CLOSED (Explored):**
- Nodes already expanded
- Prevents re-expansion in graph-search

**Category:** DATA STRUCTURES
**Difficulty:** BASIC

---

## Card 35: Optimal vs Complete
**QUESTION SIDE**
What is the difference between "optimal" and "complete" for search algorithms?

**ANSWER SIDE**
**Complete:** Guarantees finding *a* solution if one exists

**Optimal:** Guarantees finding the *best* (least cost/shortest) solution

**Example:** BFS is complete and finds shortest path, but not necessarily least cost if actions have different costs.

**Category:** ALGORITHM PROPERTIES
**Difficulty:** INTERMEDIATE

---

## Card 36: Euclidean Distance Heuristic
**QUESTION SIDE**
For the Romania travel problem, what heuristic is commonly used?

**ANSWER SIDE**
**Straight-line distance** to Bucharest (Euclidean distance)

**Properties:**
- Admissible (never overestimates actual road distance)
- Easy to compute from coordinates
- Domain-specific knowledge

**Example:** Arad to Bucharest = 366 km (straight-line)

**Category:** HEURISTIC DESIGN
**Difficulty:** BASIC

---

## Card 37: Water Jug Problem Formulation
**QUESTION SIDE**
How is the water jug problem formulated as a search problem?

**ANSWER SIDE**
**States:** (gal3, gal4) - gallons in each jug
**Actions:** Empty-3, Empty-4, Fill-3, Fill-4, Pour-3-into-4, Pour-4-into-3
**Initial:** (0,0)
**Goal:** e.g., (0,2) or (*,3)

**Note:** Only integer values reachable from integer start

**Category:** PROBLEM FORMULATION
**Difficulty:** INTERMEDIATE

---

## Card 38: Romania Travel Formulation
**QUESTION SIDE**
How is the Romania travel problem formulated?

**ANSWER SIDE**
**State Space:** Cities (Arad, Bucharest, Sibiu, ...)
**Actions:** Drive between neighboring cities
**Initial:** In Arad
**Goal:** In Bucharest
**Costs:** Road distances

**Abstraction:** Ignores low-level driving details

**Category:** PROBLEM FORMULATION
**Difficulty:** BASIC

---

## Card 39: BFS Data Structure
**QUESTION SIDE**
What data structure should be used to implement BFS?

**ANSWER SIDE**
**FIFO Queue** (First-In-First-Out)

- Add to end: New successors
- Remove from front: Node to expand

This ensures level-by-level exploration (breadth-first order).

**Category:** IMPLEMENTATION
**Difficulty:** BASIC

---

## Card 40: DFS Data Structure
**QUESTION SIDE**
What data structure should be used to implement DFS?

**ANSWER SIDE**
**LIFO Stack** (Last-In-First-Out) or recursion

- Push: New successors
- Pop: Node to expand

This ensures deepest-first exploration with natural backtracking.

**Category:** IMPLEMENTATION
**Difficulty:** BASIC

---

## Card 41: UCS Data Structure
**QUESTION SIDE**
What data structure should be used to implement Uniform-Cost Search?

**ANSWER SIDE**
**Priority Queue** ordered by path cost g(n)

- Always extract node with lowest g(n)
- May need to update priorities when better paths found

Ensures least-cost-first expansion.

**Category:** IMPLEMENTATION
**Difficulty:** INTERMEDIATE

---

## Card 42: A* Data Structure
**QUESTION SIDE**
What data structure should be used to implement A* Search?

**ANSWER SIDE**
**Priority Queue** ordered by f(n) = g(n) + h(n)

- Extract: Node with lowest f-value
- Update: When better path to existing node found

Combines actual cost with heuristic estimate.

**Category:** IMPLEMENTATION
**Difficulty:** INTERMEDIATE

---

## Card 43: Why Search is Important
**QUESTION SIDE**
What are three reasons why search is fundamental to AI?

**ANSWER SIDE**
1. **Successful:** Achieves super-human performance in many domains
2. **Practical:** Easiest way to solve problems without specific algorithms
3. **Critical:** Encodes intelligent behaviors like planning

**Heuristics** allow domain knowledge integration.

**Category:** MOTIVATION
**Difficulty:** BASIC

---

## Card 44: Search Limitations
**QUESTION SIDE**
What are the main limitations of search as an AI technique?

**ANSWER SIDE**
- Doesn't address **problem formulation** (how to cast as search)
- Assumes problem already correctly formulated
- Shows *how to solve* given formulation, not *what to solve*

**Still need:** Domain knowledge, abstraction, state space design

**Category:** LIMITATIONS
**Difficulty:** INTERMEDIATE

---

## Card 45: Heuristic Construction Methods
**QUESTION SIDE**
What are three approaches to constructing heuristics?

**ANSWER SIDE**
1. **Solving sub-problems** and aggregating costs (dynamic programming)
2. **Learning from experience** (reinforcement learning, semantic graphs)
3. **Multi-objective heuristic design** (combining multiple factors)

**Goal:** Domain-specific knowledge that guides search effectively

**Category:** HEURISTIC DESIGN
**Difficulty:** ADVANCED

---

## Card 46: Local Search vs Systematic Search
**QUESTION SIDE**
When should you use local search instead of systematic search?

**ANSWER SIDE**
**Use local search when:**
- State space is huge (> 10^100 states)
- Path doesn't matter, only final state
- Limited memory
- Continuous state spaces
- Approximation acceptable

**Examples:** Optimization, scheduling, design problems

**Category:** ALGORITHM SELECTION
**Difficulty:** INTERMEDIATE

---

## Card 47: Exploitation vs Exploration
**QUESTION SIDE**
What is the exploitation-exploration tradeoff in local search?

**ANSWER SIDE**
**Exploitation:** Focus on improving current best solution (hill climbing)
**Exploration:** Try new areas of search space (random moves)

**Balance needed:**
- Simulated Annealing: T controls tradeoff
- Genetic Algorithms: Mutation vs crossover
- Too much exploitation → local optima
- Too much exploration → inefficient

**Category:** LOCAL SEARCH
**Difficulty:** ADVANCED

---

## Card 48: Perfect Information Games
**QUESTION SIDE**
What characterizes a perfect information game?

**ANSWER SIDE**
All players have **complete knowledge** of:
- Current game state
- All possible actions
- Game rules and outcomes

**Examples:** Chess, Checkers, Tic-tac-toe
**Contrast:** Imperfect information (Poker - hidden cards)

**Enables:** Minimax algorithm

**Category:** ADVERSARIAL SEARCH
**Difficulty:** BASIC

---

## Card 49: Terminal Node Utility
**QUESTION SIDE**
In game trees, what is assigned to terminal nodes?

**ANSWER SIDE**
**Utility/Payoff values** representing outcome:
- +1 or +∞: Win for MAX
- -1 or -∞: Win for MIN (loss for MAX)
- 0: Draw

These values **backpropagate** up tree via minimax.

**Category:** ADVERSARIAL SEARCH
**Difficulty:** BASIC

---

## Card 50: Admissibility Example
**QUESTION SIDE**
Is straight-line distance admissible for road navigation? Why?

**ANSWER SIDE**
**Yes**, it's admissible because:
- Roads cannot be shorter than straight-line distance
- h(n) = straight-line ≤ h*(n) = actual shortest road
- Never overestimates

**Always:** Physical distance ≥ Euclidean distance

**Category:** HEURISTIC PROPERTIES
**Difficulty:** INTERMEDIATE

---

## Card 51: Multiple Heuristics
**QUESTION SIDE**
If you have multiple admissible heuristics h₁, h₂, ..., hₖ, how should you choose?

**ANSWER SIDE**
Use **h(n) = max(h₁(n), h₂(n), ..., hₖ(n))**

**Why:**
- Still admissible (if all hᵢ admissible)
- Closer to true cost h*
- Better informed search
- Fewer nodes expanded

**Category:** HEURISTIC DESIGN
**Difficulty:** ADVANCED

---

## Card 52: GA vs SA vs Hill Climbing
**QUESTION SIDE**
Compare Genetic Algorithms, Simulated Annealing, and Hill Climbing on search space breadth

**ANSWER SIDE**
**Hill Climbing:** Narrow (single neighbor)
**Simulated Annealing:** Medium (single neighbor, accepts worse)
**Genetic Algorithms:** Broad (population, explores multiple areas)

**Implication:** GA better for multimodal landscapes, SA for balance, HC for convex problems

**Category:** ALGORITHM COMPARISON
**Difficulty:** ADVANCED

---

## Card 53: Path Cost vs Heuristic Cost
**QUESTION SIDE**
What is the difference between g(n) and h(n) in A*?

**ANSWER SIDE**
**g(n):** Actual cost from start to n (known, exact, backward-looking)
**h(n):** Estimated cost from n to goal (approximate, forward-looking)

**Together:** f(n) = g(n) + h(n) estimates total solution cost through n

**Category:** INFORMED SEARCH
**Difficulty:** BASIC

---

## Card 54: When UCS = BFS
**QUESTION SIDE**
Under what condition are Uniform-Cost Search and Breadth-First Search identical?

**ANSWER SIDE**
When **all actions have equal cost**

Then:
- Path cost = depth
- Expanding least-cost = expanding shallowest
- Both explore in same order

**Category:** ALGORITHM RELATIONSHIPS
**Difficulty:** INTERMEDIATE

---

## Card 55: Cycle Detection Importance
**QUESTION SIDE**
Why is cycle detection critical in graph search?

**ANSWER SIDE**
Without it:
- May revisit states infinitely (non-termination)
- Exponential node redundancy
- Wasted computation

**Solution:** Graph-search with explored set
**Example:** Arad → Sibiu → Arad → Sibiu → ...

**Category:** SEARCH STRATEGIES
**Difficulty:** INTERMEDIATE

---

## Card 56: Branching Factor Impact
**QUESTION SIGN**
How does branching factor b affect search complexity?

**ANSWER SIDE**
**Exponential impact:**
- BFS: O(b^d) time and space
- Small increase in b → huge complexity increase
- Example: b=2 vs b=3 at d=10: 1024 vs 59,049 nodes

**Implication:** Reducing branching is critical for scaling

**Category:** ALGORITHM ANALYSIS
**Difficulty:** ADVANCED

---

## Card 57: Iterative Deepening Efficiency
**QUESTION SIDE**
Despite re-expanding nodes, why is Iterative Deepening efficient?

**ANSWER SIDE**
**Most nodes are at deepest level:**
- Re-expansion cost: O(b^d)
- Total cost still: O(b^d)
- Overhead: Only constant factor

**Example b=10, d=5:**
- Nodes at d=5: 100,000
- Re-expanded shallower: ~11,111
- Overhead: ~11%

**Category:** ALGORITHM ANALYSIS
**Difficulty:** ADVANCED

---

## Card 58: Objective Function Design
**QUESTION SIDE**
What makes a good objective function for local search?

**ANSWER SIDE**
1. **Continuous/smooth:** Avoids too many plateaux
2. **Informative:** Clear gradient toward optimum
3. **Computable:** Efficient evaluation
4. **Aligned:** Maximizing/minimizing it solves the problem

**Bad:** Step functions, many flat regions

**Category:** LOCAL SEARCH
**Difficulty:** ADVANCED

---

## Card 59: Minimax Decision
**QUESTION SIDE**
How does MAX player choose move at root of minimax tree?

**ANSWER SIDE**
1. Compute minimax values for all children
2. **Choose action** leading to child with **maximum value**

**Value at root** = best guaranteed outcome
**Move** = action achieving that outcome

**Category:** ADVERSARIAL SEARCH
**Difficulty:** BASIC

---

## Card 60: Depth Limit Selection
**QUESTION SIDE**
How do you choose depth limit D for Depth-Limited Search?

**ANSWER SIDE**
**Domain knowledge:**
- Expected solution depth
- Resource constraints (time/memory)

**Tradeoffs:**
- Too small: Miss solutions
- Too large: Inefficient

**Alternative:** Use IDS to avoid guessing

**Category:** SEARCH PARAMETERS
**Difficulty:** INTERMEDIATE

---

## Card 61: Greedy Best-First Example
**QUESTION SIDE**
Why might Greedy Best-First find suboptimal path (Arad → Bucharest)?

**ANSWER SIDE**
Chooses Fagaras (h=178) over Rimnicu Vilcea (h=193)
**Result:** Path cost 450
**Optimal:** Via Rimnicu Vilcea, cost 418

**Reason:** Ignores g(n), focuses only on h(n) (looking close ≠ getting there cheaply)

**Category:** INFORMED SEARCH EXAMPLE
**Difficulty:** INTERMEDIATE

---

## Card 62: A* Example
**QUESTION SIDE**
How does A* find optimal path (Arad → Bucharest) where Greedy fails?

**ANSWER SIDE**
Considers f(n) = g(n) + h(n):
- Fagaras: f = 239 + 178 = 417
- Rimnicu Vilcea: f = 220 + 193 = 413 ✓

Chooses Rimnicu Vilcea (lower f despite higher h)
**Result:** Finds optimal path cost 418

**Category:** INFORMED SEARCH EXAMPLE
**Difficulty:** INTERMEDIATE

---

## Card 63: SA Temperature Analogy
**QUESTION SIDE**
Why is Simulated Annealing named after metallurgy?

**ANSWER SIDE**
**Annealing process:**
1. Heat metal to high temperature (molecules move freely)
2. Gradually cool (molecules settle into low-energy configuration)

**Algorithm analogy:**
- High T: Accept bad moves (explore)
- Cool down: Restrict bad moves (converge)
- Result: Reach good (low-energy) solution

**Category:** LOCAL SEARCH
**Difficulty:** BASIC

---

## Card 64: Crossover vs Mutation
**QUESTION SIDE**
What is the difference in role between crossover and mutation in GAs?

**ANSWER SIDE**
**Crossover:**
- Combines good traits from parents
- Exploitation of known good solutions
- Main search operator

**Mutation:**
- Introduces random changes
- Exploration of new areas
- Maintains diversity

**Balance:** High crossover + low mutation rate typical

**Category:** LOCAL SEARCH
**Difficulty:** INTERMEDIATE

---

## Card 65: State Space Size
**QUESTION SIDE**
Why can search handle 10^100 states but local search needed for 10^30,000?

**ANSWER SIDE**
**Systematic search:**
- Stores O(b^d) nodes in memory
- 10^100 ≈ limit for breadth-first

**Local search:**
- Stores O(1) current state(s)
- Can handle arbitrarily large spaces
- Tradeoff: No optimality guarantee

**Category:** ALGORITHM SELECTION
**Difficulty:** ADVANCED

---

## Card 66: AND-OR vs Regular Search
**QUESTION SIDE**
When do you use AND-OR search trees instead of regular search?

**ANSWER SIDE**
**Use AND-OR when:**
- Non-deterministic actions (multiple outcomes)
- Partial observability
- Contingent planning (if-then-else plans)

**Regular search:** Deterministic, fully observable
**AND-OR:** Models uncertainty, branching on outcomes

**Category:** NON-DETERMINISTIC SEARCH
**Difficulty:** ADVANCED

---

## Card 67: Memory-Bounded Motivation
**QUESTION SIDE**
Why were IDA* and RBFS developed?

**ANSWER SIDE**
**Problem:** A* requires O(b^d) space
**Bottleneck:** Memory limits (storage nodes exponentially)

**Solutions:**
- IDA*: Iterative deepening with f-cost cutoff
- RBFS: Store only best alternative f-values

Both: O(bd) space with slight time overhead

**Category:** MEMORY-BOUNDED SEARCH
**Difficulty:** INTERMEDIATE

---

## Card 68: Utility Function in Games
**QUESTION SIDE**
What is the purpose of UTILITY(s, p) in game formulation?

**ANSWER SIDE**
Defines **payoff** for player p in terminal state s:
- Quantifies win/loss/draw
- Enables numeric comparison
- Drives minimax value backpropagation

**Example:** Chess utility: +1 (win), 0 (draw), -1 (loss)

**Category:** ADVERSARIAL SEARCH
**Difficulty:** BASIC

---

## Card 69: Graph-Search Optimality
**QUESTION SIDE**
Does graph-search (with explored set) always maintain optimality?

**ANSWER SIDE**
**Depends on strategy:**
- UCS: Yes (expands in cost order)
- A* with consistent h: Yes
- Greedy/DFS: No (may discard better paths)

**Key:** First expansion of state must be optimal path for optimality guarantee

**Category:** SEARCH PROPERTIES
**Difficulty:** ADVANCED

---

## Card 70: Romania Optimal Solution
**QUESTION SIDE**
What is the optimal path and cost from Arad to Bucharest?

**ANSWER SIDE**
**Path:** Arad → Sibiu → Rimnicu Vilcea → Pitesti → Bucharest
**Cost:** 140 + 80 + 97 + 101 = **418 km**

Found by: UCS, A* with admissible heuristic
Not found by: Greedy (gets 450), BFS (finds shortest, not cheapest)

**Category:** EXAMPLE PROBLEMS
**Difficulty:** BASIC

---

## Card 71: Heuristic Dominance
**QUESTION SIDE**
When does heuristic h₂ dominate h₁?

**ANSWER SIDE**
h₂(n) ≥ h₁(n) for all n

**Implication:**
- h₂ more informed
- A* with h₂ expands ≤ nodes than with h₁
- Both must be admissible for optimality

**Example:** Manhattan distance dominates misplaced tiles in 8-puzzle

**Category:** HEURISTIC PROPERTIES
**Difficulty:** ADVANCED

---

## Card 72: Fitness Function in GA
**QUESTION SIDE**
What role does the fitness function play in Genetic Algorithms?

**ANSWER SIDE**
**Measures quality** of each individual (solution):
- Guides selection (higher fitness → more offspring)
- Defines optimization objective
- Problem-specific

**Example:** For maximizing f(x)=x², fitness = x²

**Category:** LOCAL SEARCH
**Difficulty:** BASIC

---

## Card 73: Best-Case Local Search
**QUESTION SIDE**
When does simple hill climbing find the global optimum?

**ANSWER SIDE**
**Convex/unimodal** objective functions:
- Single global optimum
- No local maxima
- Monotonic gradient toward optimum

**Example:** Quadratic bowl f(x) = ||x||²

**Otherwise:** Needs SA, GA, or restarts

**Category:** LOCAL SEARCH
**Difficulty:** INTERMEDIATE

---

## Card 74: Search Problem Examples
**QUESTION SIDE**
Give three examples of real-world problems solved by search

**ANSWER SIDE**
1. **Route planning:** GPS navigation (A*)
2. **Game playing:** Chess engines (minimax with α-β)
3. **Scheduling:** Job shop scheduling (local search)

Also: Puzzle solving, robot motion planning, theorem proving

**Category:** APPLICATIONS
**Difficulty:** BASIC

---

## Card 75: Completeness Trade-offs
**QUESTION SIDE**
Which uninformed search methods are complete and why?

**ANSWER SIDE**
**Complete:**
- BFS (systematic, level by level)
- UCS (systematic, cost by cost)
- IDS (systematic, iteratively increasing depth)

**Incomplete:**
- DFS (may loop infinitely)

**Completeness requires:** Systematic exploration + avoidance of infinite paths

**Category:** ALGORITHM PROPERTIES
**Difficulty:** INTERMEDIATE

---

## Card 76: Optimality Trade-offs
**QUESTION SIDE**
Which search methods guarantee optimal solutions?

**ANSWER SIDE**
**Optimal:**
- UCS (least cost first)
- A* with admissible h (f-cost with h ≤ h*)

**Not optimal:**
- BFS (shortest path, not necessarily least cost)
- DFS (arbitrary path)
- Greedy (ignores path cost)
- Local search (approximate)

**Category:** ALGORITHM PROPERTIES
**Difficulty:** INTERMEDIATE

---

## Card 77: Path Reconstruction
**QUESTION SIDE**
How do you reconstruct the solution path after search?

**ANSWER SIDE**
Follow **parent pointers** from goal node back to start:
- Each node stores n.PARENT
- Trace: goal → parent → parent → ... → start
- Reverse for start-to-goal path

**Also track:** n.ACTION for action sequence

**Category:** IMPLEMENTATION
**Difficulty:** BASIC

---

## Card 78: Informed vs Uninformed
**QUESTION SIDE**
What distinguishes informed from uninformed search?

**ANSWER SIDE**
**Uninformed:** Uses only problem definition (states, actions, costs)
**Informed:** Uses domain-specific heuristic h(n) to estimate goal distance

**Uninformed:** BFS, DFS, UCS, IDS
**Informed:** Greedy, A*, IDA*

**Advantage:** Heuristics dramatically reduce search

**Category:** SEARCH CLASSIFICATION
**Difficulty:** BASIC

---

## Card 79: Successor Function
**QUESTION SIDE**
What does the successor function S(x) return?

**ANSWER SIDE**
**Set of states** reachable from x via single action

**With actions:** S(x) = {⟨state, action⟩ pairs}
**Example:** S(Arad) = {⟨Sibiu, drive⟩, ⟨Timisoara, drive⟩, ⟨Zerind, drive⟩}

**Used in:** Node expansion during search

**Category:** PROBLEM FORMULATION
**Difficulty:** BASIC

---

## Card 80: Explored Set Purpose
**QUESTION SIDE**
Why maintain an explored/closed set in graph search?

**ANSWER SIDE**
**Prevent:**
- Redundant expansion of same state
- Cycles (infinite loops)
- Wasted computation

**Cost:** Extra memory O(explored states)
**Benefit:** Correctness + efficiency in graphs with cycles

**Category:** DATA STRUCTURES
**Difficulty:** INTERMEDIATE

---

## Card 81: Node Expansion
**QUESTION SIDE**
What happens when a node n is "expanded" in search?

**ANSWER SIDE**
1. Remove n from frontier (OPEN)
2. Add n.STATE to explored (if graph-search)
3. Generate successors via S(n.STATE)
4. Add successor nodes to frontier (with parent pointers)

**Result:** Search tree grows

**Category:** SEARCH PROCESS
**Difficulty:** BASIC

---

## Card 82: Goal Test Timing
**QUESTION SIDE**
When should you apply the goal test: when generating nodes or when expanding?

**ANSWER SIDE**
**UCS, A*:** Test when **expanding** (popping from frontier)
- Ensures least-cost path found first
- Critical for optimality

**BFS:** Can test when generating (slight efficiency gain)

**Category:** IMPLEMENTATION
**Difficulty:** ADVANCED

---

## Card 83: Initial Temperature SA
**QUESTION SIDE**
How do you set the initial temperature T₀ in Simulated Annealing?

**ANSWER SIDE**
High enough to accept **most worse moves** initially:
- Estimate average ΔE (cost difference)
- Choose T₀ so exp(-ΔE/T₀) ≈ 0.8-0.9
- Rule of thumb: T₀ ≈ max(ΔE)

**Too low:** Acts like hill climbing
**Too high:** Random search

**Category:** ALGORITHM PARAMETERS
**Difficulty:** ADVANCED

---

## Card 84: Population Size GA
**QUESTION SIDE**
How does population size affect Genetic Algorithms?

**ANSWER SIDE**
**Small population:**
- Faster per generation
- Less diversity → premature convergence

**Large population:**
- More diverse exploration
- Slower per generation

**Typical:** 50-500, depends on problem complexity

**Category:** ALGORITHM PARAMETERS
**Difficulty:** INTERMEDIATE

---

## Card 85: Mutation Rate GA
**QUESTION SIDE**
What is a typical mutation rate in Genetic Algorithms and why?

**ANSWER SIDE**
**Typical:** 0.001 - 0.01 (0.1% - 1% per bit/gene)

**Reasoning:**
- Too high: Destroys good solutions (random search)
- Too low: Insufficient diversity
- Secondary to crossover

**Role:** Maintain diversity, escape local optima

**Category:** ALGORITHM PARAMETERS
**Difficulty:** INTERMEDIATE

---

## Card 86: Chess Complexity
**QUESTION SIDE**
Why is chess search challenging despite perfect information?

**ANSWER SIDE**
**Branching factor:** ~35 average
**Depth:** ~80 moves typical game
**State space:** ~10^47 positions

**Impossibly large:** Cannot search to end
**Solutions:** Depth-limited search + evaluation function + α-β pruning

**Category:** ADVERSARIAL SEARCH
**Difficulty:** ADVANCED

---

## Card 87: Evaluation Function
**QUESTION SIDE**
What is an evaluation function in game playing?

**ANSWER SIDE**
**Heuristic estimate** of position value for non-terminal states
- Replaces utility for depth-limited search
- Combines features (material, position, etc.)

**Example Chess:** Score = 9×queens + 5×rooks + 3×(bishops + knights) + 1×pawns

**Category:** ADVERSARIAL SEARCH
**Difficulty:** INTERMEDIATE

---

## Card 88: Depth-Limited Minimax
**QUESTION SIDE**
How does depth-limited minimax differ from full minimax?

**ANSWER SIDE**
**Stops at depth limit d** instead of terminal states:
- Applies evaluation function at cutoff depth
- Treats evaluated nodes as "pseudo-terminals"
- Trades optimality for tractability

**Horizon effect:** May miss important deeper moves

**Category:** ADVERSARIAL SEARCH
**Difficulty:** ADVANCED

---

## Card 89: Zero-Sum Games
**QUESTION SIDE**
What is a zero-sum game?

**ANSWER SIDE**
**One player's gain = other's loss:**
UTILITY(s, MAX) = -UTILITY(s, MIN)

**Examples:** Chess, Checkers, Tic-tac-toe
**Not zero-sum:** Poker (house takes cut), cooperative games

**Enables:** Single utility function in minimax

**Category:** GAME THEORY
**Difficulty:** BASIC

---

## Card 90: α-β Pruning Effectiveness
**QUESTION SIDE**
How much can α-β pruning reduce search?

**ANSWER SIDE**
**Best case:** O(b^(d/2)) vs O(b^d) for full minimax
- Doubles effective search depth!
- **Best move ordering:** Examine best moves first

**Worst case:** No pruning (bad move ordering)

**Typical:** 50-70% reduction

**Category:** ADVERSARIAL SEARCH
**Difficulty:** ADVANCED

---
