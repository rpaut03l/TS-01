# ╔══════════════════════════════════════════════════════════════════════╗
# ║  🧠 DSA MNEMONICS, LEARNING TECHNIQUES & STUDY GUIDE                 ║
# ║  How to REMEMBER every algorithm — tricks, stories, and patterns     ║
# ╚══════════════════════════════════════════════════════════════════════╝
#
# This file is NOT code — it's a STUDY GUIDE. Read it like a textbook.
# Print it out, stick it on your wall, read it before exams!
#
# ══════════════════════════════════════════════════════════════════════


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# PART 1: THE MASTER SONG — Remember ALL algorithms in 30 seconds
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"""
🎵 THE DSA SONG (sing to any tune you like!) 🎵

    "I Must Remember BSTs, Red-Black, Augmented, Disjoint —
     Graphs Bring Dijkstra, Networks Flow, Matching Points —
     Dynamic Programs Cut Rods, LCS is Long,
     Greedy Picks the Earliest — and now you know this song!"

First letter of each main word:
I-M-R-B-R-A-D-G-B-D-N-F-M-D-P-C-R-L-G-P-E

Or group by category:
    SORTING:     Insertion (cards), Merge (split & merge)
    RECURRENCE:  Tree method (draw the tree, sum levels)
    DATA STRUCT: BST → Red-Black → Augmenting → DSU
    GRAPHS:      Intro(BFS/DFS) → Dijkstra → Flow → Matching
    DP:          Rod Cutting → LCS
    GREEDY:      Activity Selection
"""


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# PART 2: ONE MNEMONIC PER ALGORITHM — Quick recall cards
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"""
╔═══════════════════════════════════════════════════════════════════╗
║  ALGORITHM             MNEMONIC                    WHAT IT MEANS  ║
╠═══════════════════════════════════════════════════════════════════╣
║                                                                   ║
║  Insertion Sort        "Pick→Scan→Shift→Drop"      Pick card,     ║
║                                                     scan left,    ║
║                                                     shift big,    ║
║                                                     drop in gap   ║
║                                                                   ║
║  Merge Sort            "Split→Sort→Merge"           Split in      ║
║                        "Smaller top card wins"       half, sort   ║
║                                                     each, merge   ║
║                                                                   ║
║  BST                   "Left Less, Right moRe"      Smaller=left  ║
║                                                     Bigger=right  ║
║                                                                   ║
║  Red-Black Insert      "Uncle Red? Swap shirts!"    Case 1: re-   ║
║                        "Uncle Black? Spin!"          color.       ║
║                                                     Cases 2,3:    ║
║                                                     rotate        ║
║                                                                   ║
║  RB Delete Fixup       "Sibling Red? Convert!"      Case 1→2/3/4  ║
║                        "Both kids Black? Push up!"   Case 2: up   ║
║                        "Far kid Black? Straighten!"  Case 3→4     ║
║                        "Far kid Red? Fix it!"        Case 4: done ║
║                                                                   ║
║  Augmenting Trees      "left.size+right.size+1"     Size formula  ║
║                        "Compare i with left+1"       OS-SELECT    ║
║                                                                   ║
║  DSU                   "Find leader, Unite teams"   Path compress ║
║                                                     + union rank  ║
║                                                                   ║
║  BFS                   "Brothers first, Sons later" Level-by-     ║
║                        Uses: QUEUE (FIFO)            level with   ║
║                                                     queue         ║
║                                                                   ║
║  DFS                   "Dive First, Surface later"  Go deep with  ║
║                        Uses: STACK/RECURSION         recursion    ║
║                        "Gray neighbor = CYCLE!"                   ║
║                                                                   ║
║  Dijkstra              "Pick the Daintiest Distance" Always pick  ║
║                        "Can I get there cheaper      cheapest.    ║
║                         through you?" (relax)        Relax edges. ║
║                                                                   ║
║  Ford-Fulkerson        "Find→Push→Update→Repeat"   BFS for path,  ║
║                        "Backward = undo button"      push flow    ║
║                                                                   ║
║  Bipartite Matching    "Try match. Stuck? Ask        Augmenting   ║
║                         matched to switch!"          paths        ║
║                                                                   ║
║  Rod Cutting (DP)      "DP = Don't recompute,       Try all cuts, ║
║                         just look it uP!"            store answers║
║                                                                   ║
║  LCS (DP)              "Match→Diagonal+1"           Same char=+1  ║
║                        "Miss→Max(Up, Left)"          Diff=best of ║
║                                                     skip either   ║
║                                                                   ║
║  Greedy Activity       "Grab what Goes away first"  Sort by finish║
║                        "Earliest finish = most room" pick earliest║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
"""


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# PART 3: PATTERN RECOGNITION — "Which algorithm do I use?"
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"""
WHEN YOU SEE THIS...              USE THIS ALGORITHM:
─────────────────────────────────────────────────────────────
"Sort this data"                → Merge Sort (large) or Insertion Sort (small/nearly sorted)
"Find shortest path"            → BFS (unweighted) or Dijkstra (weighted, no negatives)
"Is there a cycle?"             → DFS (check for back edges)
"Order tasks by dependencies"   → DFS topological sort
"Group items / connected?"      → DSU (Union-Find) or BFS/DFS
"Maximum flow through network"  → Ford-Fulkerson / Edmonds-Karp
"Match pairs optimally"         → Bipartite Matching (reduce to max flow)
"Maximize value with choices"   → Dynamic Programming (Rod Cutting, LCS)
"Pick most without overlap"     → Greedy Activity Selection
"Find i-th smallest element"    → Augmenting Trees (OS-SELECT)
"Keep things balanced"          → Red-Black Trees


THE TWO BIG QUESTIONS TO ASK:
1. "Does it have overlapping subproblems?"  → YES = DP
2. "Does the greedy choice always work?"    → YES = Greedy, NO = DP
"""


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# PART 4: LEARNING TECHNIQUES — How to actually LEARN this stuff
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"""
╔══════════════════════════════════════════════════════════════════╗
║  🎯 THE 5-STEP METHOD TO LEARN ANY ALGORITHM                     ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  STEP 1: UNDERSTAND THE STORY (2 min)                            ║
║  ─────────────────────────────────────                           ║
║  Read the ELI5 explanation. Understand WHAT the algorithm does   ║
║  and WHY it works, using the real-world analogy.                 ║
║  Don't look at code yet!                                         ║
║                                                                  ║
║  STEP 2: TRACE BY HAND (10 min)                                  ║
║  ────────────────────────────────                                ║
║  Take a small example (5-6 elements). Draw it on paper.          ║
║  Walk through the algorithm step by step. Write every state.     ║
║  This is THE most important step. If you can trace it,           ║
║  you understand it.                                              ║
║                                                                  ║
║  STEP 3: MEMORIZE THE MNEMONIC (1 min)                           ║
║  ──────────────────────────────────────                          ║
║  Learn the mnemonic phrase. Say it out loud 3 times.             ║
║  Example: "Pick → Scan → Shift → Drop" for Insertion Sort.       ║
║  The mnemonic maps directly to the code structure!               ║
║                                                                  ║
║  STEP 4: WRITE THE CODE FROM MEMORY (10 min)                     ║
║  ──────────────────────────────────────────                      ║
║  Close the reference. Open a blank file. Write the algorithm     ║
║  from scratch. Use the mnemonic as your guide.                   ║
║  Stuck? Look at ONE line, close reference, continue.             ║
║  Repeat until you can write it without looking.                  ║
║                                                                  ║
║  STEP 5: EXPLAIN IT TO SOMEONE (5 min)                           ║
║  ─────────────────────────────────────                           ║
║  The Feynman Technique: explain the algorithm to a friend,       ║
║  a rubber duck, or an imaginary 5-year-old. If you can't         ║
║  explain it simply, you don't understand it yet.                 ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝


╔══════════════════════════════════════════════════════════════════╗
║  📅 STUDY SCHEDULE — 2-Week Plan Before Exam                     ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  WEEK 1 (Learn):                                                 ║
║  Day 1: Insertion Sort + Merge Sort                              ║
║  Day 2: Recursion Tree Method                                    ║
║  Day 3: BST (all operations)                                     ║
║  Day 4: Red-Black Trees (insert + 3 cases)                       ║
║  Day 5: RB-Delete (4 cases) + Augmenting Trees                   ║
║  Day 6: DSU + Graph basics (BFS, DFS)                            ║
║  Day 7: Dijkstra + Network Flow + Bipartite Matching             ║
║                                                                  ║
║  WEEK 2 (Practice):                                              ║
║  Day 8: Rod Cutting + LCS + Greedy                               ║
║  Day 9: Practice problems — Sorting + Recurrences                ║
║  Day 10: Practice — BST + RB-Trees + Augmenting                  ║
║  Day 11: Practice — DSU + Graphs + Dijkstra                      ║
║  Day 12: Practice — Flow + DP + Greedy                           ║
║  Day 13: Write ALL algorithms from memory (timed!)               ║
║  Day 14: Review mistakes, re-read mnemonics, relax!              ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝


╔══════════════════════════════════════════════════════════════════╗
║  🔥 EXAM DAY QUICK-RECALL CHECKLIST                              ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  Before entering the exam, say these out loud:                   ║
║                                                                  ║
║  □ "Pick Scan Shift Drop" (Insertion Sort)                       ║
║  □ "Split Sort Merge" (Merge Sort)                               ║
║  □ "T(n)=2T(n/2)+n → n per level × log n levels" (Recurrence)    ║
║  □ "Left Less Right moRe" (BST)                                  ║
║  □ "Uncle Red=recolor, Uncle Black=rotate" (RB Insert)           ║
║  □ "Sibling cases: Red→convert, BothBlack→up, FarRed→fix" (RB)   ║
║  □ "left.size+right.size+1" (Augmenting)                         ║
║  □ "Find leader Unite teams" (DSU)                               ║
║  □ "Brothers first" (BFS) "Dive first" (DFS)                     ║
║  □ "Pick Daintiest Distance, Relax" (Dijkstra)                   ║
║  □ "Find Push Update Repeat" (Ford-Fulkerson)                    ║
║  □ "Don't recompute, look it uP" (DP)                            ║
║  □ "Match=Diagonal+1, Miss=Max(Up,Left)" (LCS)                   ║
║  □ "Grab what Goes first" (Greedy)                               ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
"""


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# PART 5: COMPLEXITY QUICK-REFERENCE (for exam problems)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"""
GROWTH RATES (slowest to fastest — memorize this order!):

    O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2ⁿ) < O(n!)
    
    ← FAST                                                    SLOW →

COMMON VALUES:
    n = 10:     log n ≈ 3,   n log n ≈ 33,    n² = 100
    n = 100:    log n ≈ 7,   n log n ≈ 664,   n² = 10,000
    n = 1000:   log n ≈ 10,  n log n ≈ 9,966, n² = 1,000,000
    n = 1M:     log n ≈ 20,  n log n ≈ 20M,   n² = 1 TRILLION!

MNEMONIC for growth order:
    "One Log Nice Nice-Log Nasty Naughty Nuclear Nightmare"
     O(1) O(logn) O(n) O(nlogn) O(n²) O(n³) O(2ⁿ) O(n!)

RECURRENCE SHORTCUTS:
    T(n) = T(n/2) + O(1)      → O(log n)      [Binary Search]
    T(n) = 2T(n/2) + O(n)     → O(n log n)     [Merge Sort]
    T(n) = 2T(n/2) + O(1)     → O(n)           [Tree traversal]
    T(n) = T(n-1) + O(n)      → O(n²)          [Insertion Sort worst]
    T(n) = T(n-1) + O(1)      → O(n)           [Linear scan]
    T(n) = 2T(n-1) + O(1)     → O(2ⁿ)          [Naive Fibonacci]
"""


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# PART 6: PYTHON CODE PATTERNS — The building blocks of DSA code
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"""
PATTERN 1: "Find the best" (used in DP, Dijkstra)
    best = float('-inf')  # or float('inf') for minimum
    for option in options:
        if option > best:
            best = option

PATTERN 2: "Two pointers merge" (used in Merge Sort)
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]: pick A[i]; i += 1
        else: pick B[j]; j += 1

PATTERN 3: "BFS template" (used in BFS, Dijkstra, Edmonds-Karp)
    queue = deque([start])
    visited = {start}
    while queue:
        u = queue.popleft()
        for v in neighbors(u):
            if v not in visited:
                visited.add(v)
                queue.append(v)

PATTERN 4: "DFS template" (used in DFS, tree traversals)
    def visit(u):
        mark u as visited
        for v in neighbors(u):
            if v not visited:
                visit(v)  # recurse!

PATTERN 5: "DP table fill" (used in Rod Cutting, LCS)
    dp = [0] * (n+1)  # or 2D: [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        dp[i] = best of (dp[smaller] + something)

PATTERN 6: "Greedy scan" (used in Activity Selection)
    sort by some key
    pick first
    for each remaining:
        if compatible with last picked:
            pick it

PATTERN 7: "Union-Find" (used in DSU, Kruskal)
    find(x): follow parent to root + compress
    union(x,y): find both roots, attach smaller under bigger
"""


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# PART 7: COMMON EXAM QUESTION TYPES & How to Solve Them
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"""
QUESTION TYPE                          HOW TO APPROACH
─────────────────────────────────────────────────────────────────
"Trace the algorithm on this input"  → Write each step. Show array/tree state.
"How many comparisons/shifts?"       → Count during trace. Use formulas.
"What is the time complexity?"       → Count loops. Nested = multiply.
"Solve this recurrence"              → Draw recursion tree. Sum levels.
"Is this a valid RB-tree?"           → Check all 5 properties.
"Insert X into RB-tree"              → BST insert + color RED + fixup cases.
"Delete X from BST/RB-tree"          → Find successor for 2-child case.
"Run BFS/DFS from vertex X"          → Draw graph. Process with queue/stack.
"Find shortest path"                 → BFS (unweighted) or Dijkstra (weighted).
"Find max flow"                      → Edmonds-Karp: BFS for paths.
"Fill DP table for Rod Cutting"      → Row by row, try all first cuts.
"Fill DP table for LCS"              → Match=diagonal+1, miss=max(up,left).
"Select max activities"              → Sort by finish, pick greedily.
"Prove greedy is optimal"            → Exchange argument.
"Prove algorithm correct"            → Loop invariant (init, maintain, terminate).
"""


print("""
╔══════════════════════════════════════════════════════════════════╗
║  📖 HOW TO USE THIS STUDY GUIDE                                  ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  1. READ Part 1 — Learn the Master Song                          ║
║  2. PRINT Part 2 — Stick mnemonic cards on your wall             ║
║  3. PRACTICE Part 3 — Pattern recognition for exam questions     ║
║  4. FOLLOW Part 4 — 5-step method for each algorithm             ║
║  5. MEMORIZE Part 5 — Complexity table and growth order          ║
║  6. INTERNALIZE Part 6 — Code patterns appear EVERYWHERE         ║
║  7. DRILL Part 7 — Practice each exam question type              ║
║                                                                  ║
║  🎯 GOLDEN RULE:                                                 ║
║  If you can TRACE it by hand and EXPLAIN it to a 5-year-old,     ║
║  you KNOW it. If you can't, go back to the README.               ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
""")
