# 🔢 Logical Agents — Numerical & Problem-Solving Guide
### AI Unit III: Knowledge, Reasoning, and Planning
#### Step-by-Step Solved Problems with Detailed Explanations

---

## 📚 Table of Contents

| # | Problem Type | Jump Link |
|---|---|---|
| 1 | [Truth Table Construction](#problem-1-truth-table-construction) | Build complete truth tables |
| 2 | [Evaluating Sentences in a Model](#problem-2-evaluating-sentences-in-a-model) | Compute truth values |
| 3 | [Checking Entailment via Model Checking](#problem-3-checking-entailment-via-model-checking) | KB ⊨ α? |
| 4 | [Wumpus World — Pit Detection](#problem-4-wumpus-world--pit-detection) | Agent reasoning |
| 5 | [Wumpus World — Wumpus Location](#problem-5-wumpus-world--wumpus-location) | Elimination reasoning |
| 6 | [Forward Chaining Step-by-Step](#problem-6-forward-chaining-step-by-step) | Data-driven inference |
| 7 | [Backward Chaining Step-by-Step](#problem-7-backward-chaining-step-by-step) | Goal-driven inference |
| 8 | [Building a KB from Scratch](#problem-8-building-a-kb-from-scratch) | Writing formal sentences |
| 9 | [Soundness & Completeness Analysis](#problem-9-soundness--completeness-analysis) | Identifying errors |
| 10 | [Operator Precedence & Parsing](#problem-10-operator-precedence--parsing) | Correct interpretation |
| 11 | [Counting Models](#problem-11-counting-models) | How many possible worlds? |
| 12 | [Implication & Biconditional Practice](#problem-12-implication--biconditional-practice) | Tricky truth values |
| 13 | [Full Wumpus Walkthrough with Score](#problem-13-full-wumpus-walkthrough-with-score) | Complete game |
| 14 | [TT-ENTAILS Pseudocode Tracing](#problem-14-tt-entails-pseudocode-tracing) | Algorithm trace |

---

> 🔗 **Theory Guide:** [Logical Agents Theory Guide](./logical_agents_theory_guide.md) | 🎯 **Exam Prep:** [Minor Exam Guide](./logical_agents_exam_guide.md) | 🗺️ **Mind Map:** [Visual Mind Map](./logical_agents_mindmap.png)

---

## 🟢 Before You Start — How to Use This Guide

### Who is this for?
If you've **never solved a logic problem** before, you're in the right place! Every problem starts from absolute zero.

### How Each Problem is Structured
```
📝 Problem     → What we're asked to solve
🤔 Why Care?   → Why this type of problem matters (NEW!)  
🧒 Mind-Friendly → The problem explained using everyday language
🔧 Tools Needed → Which formulas/rules you'll use (NEW!)
📐 Step-by-Step → Detailed solution (nothing skipped!)
✅ Answer       → The final result
💡 Key Takeaway → The one thing to remember (NEW!)
```

### Essential Formulas You'll Need (Cheat Sheet)
```
╔═══════════════════════════════════════════════════════╗
║  FORMULA CHEAT SHEET — Keep This Open!                ║
╠═══════════════════════════════════════════════════════╣
║                                                       ║
║  CONNECTIVES (how to combine facts):                  ║
║    ¬P        = NOT P (flip true↔false)               ║
║    P ∧ Q     = P AND Q (both must be true)           ║
║    P ∨ Q     = P OR Q (at least one true)            ║
║    P ⇒ Q     = IF P THEN Q                          ║
║                 FALSE only when P=T, Q=F ⬅ MEMORIZE! ║
║    P ⇔ Q     = P and Q always match                  ║
║                                                       ║
║  ENTAILMENT:                                          ║
║    KB ⊨ α    = α is true in EVERY model where KB     ║
║                is true (KB guarantees α)              ║
║                                                       ║
║  MODELS:                                              ║
║    n symbols → 2ⁿ possible models (rows in table)    ║
║    Example: 3 symbols → 2³ = 8 rows                  ║
║                                                       ║
║  PRECEDENCE (which to compute first):                 ║
║    ¬ > ∧ > ∨ > ⇒ > ⇔                               ║
║    "Naughty Ants Often Irritate Insects"              ║
╚═══════════════════════════════════════════════════════╝
```

### Difficulty Ratings
```
⭐          = Warm-up (start here!)
⭐⭐        = Standard exam question  
⭐⭐⭐      = Challenging (combines multiple concepts)
```

---

## Problem 1: Truth Table Construction ⭐

### 🤔 Why This Matters
Truth tables are the **#1 most fundamental skill** in logic. Every exam will have at least one truth table question. Master this, and everything else becomes easier!

### 📝 Problem
**Build the complete truth table for: (P ⇒ Q) ∧ (Q ⇒ R)**

### 🧒 Mind-Friendly Setup
Imagine two promises your mom makes:
- **Promise 1:** "If it rains (P), I'll give you an umbrella (Q)"
- **Promise 2:** "If you have an umbrella (Q), you'll stay dry (R)"

We want to check: when are BOTH promises true at the same time?

### 🔧 Tools You Need
```
1. Know how many rows: 2ⁿ where n = number of symbols
2. P⇒Q rule: FALSE only when P=True, Q=False
3. P∧Q rule: TRUE only when BOTH P and Q are true
```

### 📐 Step-by-Step Solution

**Step 1:** Count symbols and rows.
- Symbols = P, Q, R (that's 3 symbols)
- Rows = 2³ = 8 (we need 8 rows in our table)
- **Tip:** Write all combinations: start with all F, and count up like binary: FFF, FFT, FTF, FTT, TFF, TFT, TTF, TTT

**Step 2:** Compute each intermediate column:

```
 P  | Q  | R  | P⇒Q | Q⇒R | (P⇒Q) ∧ (Q⇒R)
────┼────┼────┼─────┼─────┼────────────────
 F  | F  | F  |  T  |  T  |      T
 F  | F  | T  |  T  |  T  |      T
 F  | T  | F  |  T  |  F  |      F
 F  | T  | T  |  T  |  T  |      T
 T  | F  | F  |  F  |  T  |      F
 T  | F  | T  |  F  |  T  |      F
 T  | T  | F  |  T  |  F  |      F
 T  | T  | T  |  T  |  T  |      T
```

**How to compute P⇒Q:** FALSE only when P=T, Q=F (row 5,6). All others = TRUE.

**How to compute final AND:** TRUE only when BOTH columns are TRUE.

### ✅ Answer
TRUE in 4 models (rows 1, 2, 4, 8). Observation: when P=T and sentence is true (row 8 only), R must be T — this proves transitivity: (P⇒Q)∧(Q⇒R) entails P⇒R!

### 💡 Key Takeaway
```
Chain of promises: If rain→umbrella AND umbrella→dry,
then rain→dry! That's transitivity in logic.

EXAM TIP: To build a truth table:
  1. Count symbols (n) → make 2ⁿ rows
  2. Compute inner columns FIRST (P⇒Q, Q⇒R)
  3. Then compute the outer operation (∧, ∨, etc.)
  4. Read the final column for the answer
```

---

## Problem 2: Evaluating Sentences in a Model ⭐

### 🤔 Why This Matters
This is like "plugging in numbers" in algebra. Given a specific situation (model), you need to figure out if a statement is true or false. This skill is used in EVERY other problem type!

### 📝 Problem
**Model m₁ = {P₁₂=false, P₂₂=false, P₃₁=true}. Evaluate:**

### Part (a): ¬P₁₂ ∧ (P₂₂ ∨ P₃₁)

```
Substitute: ¬(false) ∧ (false ∨ true)
Step 1: ¬false = true
Step 2: false ∨ true = true
Step 3: true ∧ true = TRUE ✅
```

### Part (b): P₁₂ ⇒ (P₂₂ ∧ P₃₁)

```
Substitute: false ⇒ (false ∧ true)
Step 1: false ∧ true = false
Step 2: false ⇒ false = TRUE ✅
(When antecedent is false, implication is always true!)
```

### Part (c): (P₁₂ ∨ P₂₂) ⇔ P₃₁

```
Substitute: (false ∨ false) ⇔ true
Step 1: false ∨ false = false
Step 2: false ⇔ true = FALSE ❌
(Biconditional: sides don't match!)
```

---

## Problem 3: Checking Entailment via Model Checking ⭐⭐

### 🤔 Why This Matters
This is the **core question of AI reasoning**: "Does what I know GUARANTEE this conclusion?" This is how AI agents decide if something is definitely true.

### 📝 Problem
**KB = {A, A ⇒ B}. Does KB ⊨ B?**

### 📐 Step-by-Step

**Step 1:** Symbols: A, B → 2² = 4 models

```
 A  | B  | KB₁=A | KB₂=A⇒B | KB=KB₁∧KB₂ | α=B
────┼────┼───────┼─────────┼────────────┼─────
 F  | F  |   F   |    T    |     F      |  F
 F  | T  |   F   |    T    |     F      |  T
 T  | F  |   T   |    F    |     F      |  F
 T  | T  |   T   |    T    |     T ←    |  T ←
```

**Step 2:** KB true in only 1 model: {A=T, B=T}

**Step 3:** In that model, B=T ✅

**Conclusion:** M(KB) ⊆ M(B) → **KB ⊨ B ✅** (This is Modus Ponens!)

### 💡 Key Takeaway
```
ENTAILMENT CHECK RECIPE (use this every time!):
  1. List all symbols → figure out how many rows (2ⁿ)
  2. Make truth table with columns for KB parts
  3. Add a "KB" column = AND of all KB parts
  4. Find rows where KB = TRUE (highlight them!)
  5. Check: is the query TRUE in ALL highlighted rows?
     YES → Entailed (KB ⊨ α)
     NO  → Not entailed (KB ⊭ α)
```

---

## Problem 4: Wumpus World — Pit Detection ⭐⭐

### 🤔 Why This Matters
This is the textbook's star example — it shows how an agent reasons about danger it can't directly see. Very likely to appear on exams!

### 📝 Problem
**Agent at [2,1] perceives Breeze. At [1,1] perceived nothing. Is there a pit at [1,2]?**

### 🧒 Mind-Friendly Setup
You're exploring a dark cave. In room [1,1], you felt NO wind. Then you walked to room [2,1] and felt wind (breeze). Wind means there's a dangerous pit nearby. Is room [1,2] safe?

### 🔧 Tools You Need
```
1. ⇔ (biconditional) rule: if left side is false, right side MUST be false too
2. ∨ (OR) is false ONLY when ALL parts are false
3. Elimination: if A∨B is false → both A=F and B=F
```

### 📐 Step-by-Step

**First, let's write down everything we know (the KB):**

```
R₁: ¬P₁₁                           (no pit at [1,1] — game rule)
R₂: B₁₁ ⇔ (P₁₂ ∨ P₂₁)            (breeze at [1,1] ↔ pit at [1,2] or [2,1])
R₃: B₂₁ ⇔ (P₁₁ ∨ P₂₂ ∨ P₃₁)     (breeze at [2,1] ↔ pit at neighbor)
R₄: ¬B₁₁                           (we felt NO breeze at [1,1])
R₅: B₂₁                            (we DID feel breeze at [2,1])
```

**In plain English:**
- R₁: The starting room is always safe
- R₂: Room [1,1] has breeze IF AND ONLY IF there's a pit next door
- R₃: Room [2,1] has breeze IF AND ONLY IF there's a pit next door
- R₄: We didn't feel breeze at [1,1] (observation)
- R₅: We DID feel breeze at [2,1] (observation)

**Logical derivation:**
```
From R₂ + R₄:
  B₁₁ ⇔ (P₁₂ ∨ P₂₁) and B₁₁ = false
  → (P₁₂ ∨ P₂₁) = false      [biconditional: both sides match]
  → P₁₂ = false AND P₂₁ = false  [OR is false only when both false]
  → ¬P₁₂ ✅
```

**Model enumeration verification (symbols: P₁₂, P₂₂, P₃₁):**
```
Model | P₁₂ | P₂₂ | P₃₁ | KB true?
──────┼─────┼─────┼─────┼─────────
  1   |  F  |  F  |  F  |   ❌ (R₃ fails: breeze needs a pit)
  2   |  F  |  F  |  T  |   ✅
  3   |  F  |  T  |  F  |   ✅
  4   |  F  |  T  |  T  |   ✅
  5   |  T  |  F  |  F  |   ❌ (R₂ fails: pit at [1,2] means breeze at [1,1])
  6   |  T  |  F  |  T  |   ❌
  7   |  T  |  T  |  F  |   ❌
  8   |  T  |  T  |  T  |   ❌
```

**Valid models (2,3,4): P₁₂ = F in ALL → KB ⊨ ¬P₁₂ ✅ No pit at [1,2]!**

---

## Problem 5: Wumpus World — Wumpus Location ⭐⭐

### 🤔 Why This Matters
This demonstrates **elimination reasoning** — ruling out possibilities one by one until only one answer remains. It's the same logic detectives use!

### 📝 Problem
**Stench at [1,2], NO stench at [2,1]. Where is the Wumpus?**

### 📐 Step-by-Step

```
S₁₂ ⇔ (W₁₁ ∨ W₂₂ ∨ W₁₃)    and S₁₂ = true
S₂₁ ⇔ (W₁₁ ∨ W₂₂ ∨ W₃₁)    and S₂₁ = false
¬W₁₁                           (game rule)

From S₂₁=false + biconditional:
  W₁₁ ∨ W₂₂ ∨ W₃₁ = false
  → W₁₁=F, W₂₂=F, W₃₁=F

From S₁₂=true + biconditional:
  W₁₁ ∨ W₂₂ ∨ W₁₃ = true
  Substitute known: F ∨ F ∨ W₁₃ = true
  → W₁₃ = true!

ANSWER: Wumpus is at [1,3] 🎯
```

---

## Problem 6: Forward Chaining Step-by-Step ⭐⭐

### 🤔 Why This Matters
Forward chaining is used in real systems like email spam filters, smart home automation, and fraud detection. Trace questions appear frequently on exams!

### 📝 Problem
**Rules: R1: rain∧cold→snow, R2: snow→school_closed, R3: school_closed→happy_kids. Facts: {rain, cold}**

### 📐 Trace

```
Iteration 1: Facts = {rain, cold}
  R1: rain✅ ∧ cold✅ → FIRE! Add "snow"
  R2: snow? (not yet available at check time)
  R3: school_closed? No
  New: {rain, cold, snow}

Iteration 2: Facts = {rain, cold, snow}
  R1: already fired
  R2: snow✅ → FIRE! Add "school_closed"
  R3: school_closed? (not yet)
  New: {rain, cold, snow, school_closed}

Iteration 3: Facts = {rain, cold, snow, school_closed}
  R3: school_closed✅ → FIRE! Add "happy_kids"
  New: {rain, cold, snow, school_closed, happy_kids}

Iteration 4: No new facts → STOP ✅
```

**Result: {rain, cold, snow, school_closed, happy_kids}**

---

## Problem 7: Backward Chaining Step-by-Step ⭐⭐

### 🤔 Why This Matters
Backward chaining is how diagnostic systems work (like MYCIN). When a doctor asks "Could this be measles?", that's backward chaining! Exam favorite.

### 📝 Problem
**Same rules as Problem 6. Prove: happy_kids?**

### 📐 Trace (Proof Tree)

```
Goal: happy_kids?
  └─ R3 requires: school_closed?
       └─ R2 requires: snow?
            └─ R1 requires: rain? → YES ✅ (fact)
                              cold? → YES ✅ (fact)
            └─ snow PROVEN ✅
       └─ school_closed PROVEN ✅
  └─ happy_kids PROVEN ✅

Key: Backward chaining never checked irrelevant rules!
```

---

## Problem 8: Building a KB from Scratch ⭐⭐⭐

### 🤔 Why This Matters
This tests if you truly understand how to REPRESENT a problem in logic — the most creative and challenging skill. If you can do this, you understand the chapter!

### 📝 Problem
**Robot in 3×3 grid detects Heat (fire nearby) and Sound (alarm nearby). Write KB for cell [2,2].**

### 📐 Solution

```
Symbols:
  F_xy = fire at [x,y], H_xy = heat at [x,y]
  A_xy = alarm at [x,y], S_xy = sound at [x,y]

Adjacent to [2,2]: [1,2], [3,2], [2,1], [2,3]

KB = {
  H₂₂ ⇔ (F₁₂ ∨ F₃₂ ∨ F₂₁ ∨ F₂₃),   // heat rule
  S₂₂ ⇔ (A₁₂ ∨ A₃₂ ∨ A₂₁ ∨ A₂₃),   // sound rule
  ¬F₂₂,                                 // no fire at start
  H₂₂,                                  // observation: heat
  ¬S₂₂                                  // observation: no sound
}

From ¬S₂₂ + biconditional:
  → ¬A₁₂ ∧ ¬A₃₂ ∧ ¬A₂₁ ∧ ¬A₂₃ (no alarms adjacent!)

From H₂₂ + biconditional:
  → F₁₂ ∨ F₃₂ ∨ F₂₁ ∨ F₂₃ (fire in at least one neighbor!)
```

---

## Problem 9: Soundness & Completeness Analysis ⭐⭐

### 🤔 Why This Matters
Understanding when an algorithm makes mistakes (unsound) or misses truths (incomplete) is crucial for evaluating AI systems. Common theory question!

### 📝 Problem
**Identify: unsound, incomplete, or both?**

### Scenario A:
```
KB: Breeze(1,1)
Algorithm says: Pit(1,2)
Correct: Pit(1,2) ∨ Pit(2,1)

→ UNSOUND ❌ (derived Pit(1,2) which isn't entailed)
  Turned a disjunction into a specific fact = jumping to conclusions!
```

### Scenario B:
```
KB: Pit(2,2)∨Pit(3,1) and Pit(2,2)∨Pit(1,3)
Algorithm outputs both disjunctions but NOT Pit(2,2)
Correct: Pit(2,2) is entailed (resolution of the two disjunctions)

→ INCOMPLETE ❌ (missed a true conclusion)
→ Still SOUND ✅ (everything it said was correct)
  Missing step: failed to combine/resolve the two disjunctions.
```

### Scenario C:
```
KB: {A, A⇒B}
Algorithm says: B, C

→ UNSOUND ❌ (C is not entailed — made up!)
  B is correct, but C isn't. One wrong answer = unsound.
```

---

## Problem 10: Operator Precedence & Parsing ⭐

### Precedence: ¬ > ∧ > ∨ > ⇒ > ⇔ (Remember: "Naughty Ants Often Irritate Insects")

### (a) ¬A ∧ B ∨ C
```
Step 1: ¬ first  → (¬A) ∧ B ∨ C
Step 2: ∧ next   → ((¬A) ∧ B) ∨ C
Answer: ((¬A) ∧ B) ∨ C
```

### (b) A ∨ B ⇒ C ∧ D
```
Step 1: ∧ first  → A ∨ B ⇒ (C ∧ D)
Step 2: ∨ next   → (A ∨ B) ⇒ (C ∧ D)
Answer: (A ∨ B) ⇒ (C ∧ D)
```

### (c) A ⇒ B ⇔ C ⇒ D
```
Step 1: ⇒ first  → (A ⇒ B) ⇔ (C ⇒ D)
Answer: (A ⇒ B) ⇔ (C ⇒ D)
```

---

## Problem 11: Counting Models ⭐

### Quick Reference

```
Sentence        | Symbols | Total | Satisfying | Formula
────────────────┼─────────┼───────┼────────────┼──────────
P ∧ Q           | P,Q     |   4   |     1      | all T
P ∨ Q           | P,Q     |   4   |     3      | 2ⁿ - 1
P ⇒ Q           | P,Q     |   4   |     3      | 2ⁿ - 1
P ⇔ Q           | P,Q     |   4   |     2      | 2ⁿ⁻¹
A ∧ B ∧ C       | A,B,C   |   8   |     1      | all T
A ∨ B ∨ C       | A,B,C   |   8   |     7      | 2ⁿ - 1
¬P              | P       |   2   |     1      | half
True            | any     |  2ⁿ   |    2ⁿ      | all
False           | any     |  2ⁿ   |     0      | none
```

---

## Problem 12: Implication & Biconditional Practice ⭐

### Evaluate:

**(a)** "5 is even" ⇒ "Moon is cheese" = F ⇒ F = **TRUE** ✅
> Antecedent false → promise not tested → vacuously true

**(b)** "2+2=4" ⇒ "Paris in France" = T ⇒ T = **TRUE** ✅
> No causal connection needed — logic only checks truth values!

**(c)** "Dogs fly" ⇔ "2+2=5" = F ⇔ F = **TRUE** ✅
> Both false = they match

**(d)** "It rains" ⇔ "Ground wet" — appropriate in closed world; in reality ⇒ might be better (sprinklers also wet ground!)

---

## Problem 13: Full Wumpus Walkthrough with Score ⭐⭐⭐

### 📐 Complete Game Trace

```
Grid: Wumpus@[1,3], Gold@[2,3], Pits@[3,1],[3,3],[4,4]

Move | Action      | Percept at new loc           | Score | KB Update
─────┼─────────────┼─────────────────────────────┼───────┼──────────────
  1  | Start [1,1] | [None,None,None,None,None]   |  0    | [1,2],[2,1] safe
  2  | Fwd → [2,1] | [None,Breeze,None,None,None] | -1    | P₂₂∨P₃₁
  3  | TurnL×2     | —                            | -3    | —
  4  | Fwd → [1,1] | —                            | -4    | —
  5  | TurnL       | —                            | -5    | —
  6  | Fwd → [1,2] | [Stench,None,None,None,None] | -6    | W₁₃!, ¬P₂₂, P₃₁!
  7  | TurnR       | —                            | -7    | [2,2] safe!
  8  | Fwd → [2,2] | —                            | -8    | —
  9  | TurnL       | —                            | -9    | —
 10  | Fwd → [2,3] | [Stench,Breeze,Glitter,N,N]  | -10   | GOLD HERE!
 11  | Grab         | —                            | -11   | Has gold
 12  | TurnL×2     | —                            | -13   | —
 13  | Fwd → [2,2] | —                            | -14   | —
 14  | TurnR       | —                            | -15   | —
 15  | Fwd → [1,2] | —                            | -16   | —
 16  | TurnR       | —                            | -17   | —
 17  | Fwd → [1,1] | —                            | -18   | At exit!
 18  | Climb        | —                            | -19   | +1000 gold!

FINAL SCORE: +1000 - 19 = +981 🎉
```

---

## Problem 14: TT-ENTAILS Pseudocode Tracing ⭐⭐⭐

### 📝 Problem
**Trace TT-ENTAILS(KB={A, A⇒B}, α=B)**

### Pseudocode
```
function TT-ENTAILS?(KB, α):
    symbols ← all prop symbols in KB and α
    return TT-CHECK-ALL(KB, α, symbols, {})

function TT-CHECK-ALL(KB, α, symbols, model):
    if symbols is EMPTY then
        if KB is TRUE in model → return (α is TRUE in model)
        else → return true  (vacuously)
    P ← FIRST(symbols); rest ← REST(symbols)
    return TT-CHECK-ALL(KB, α, rest, model ∪ {P=T})
       AND TT-CHECK-ALL(KB, α, rest, model ∪ {P=F})
```

### 📐 Trace

```
TT-CHECK-ALL(KB, B, [A,B], {})
├── A=T: TT-CHECK-ALL(KB, B, [B], {A=T})
│   ├── B=T: TT-CHECK-ALL(KB, B, [], {A=T,B=T})
│   │   symbols empty! KB? A=T✅, A⇒B=T⇒T=T✅ → KB TRUE
│   │   α=B? T✅ → return TRUE
│   └── B=F: TT-CHECK-ALL(KB, B, [], {A=T,B=F})
│       symbols empty! KB? A=T✅, A⇒B=T⇒F=F❌ → KB FALSE
│       → return TRUE (vacuous)
│   Result: T AND T = TRUE
└── A=F: TT-CHECK-ALL(KB, B, [B], {A=F})
    ├── B=T: KB? A=F❌ → KB FALSE → TRUE (vacuous)
    └── B=F: KB? A=F❌ → KB FALSE → TRUE (vacuous)
    Result: T AND T = TRUE

FINAL: T AND T = TRUE → KB ⊨ B ✅
```

---

## ⚠️ Common Beginner Mistakes (Avoid These!)

```
MISTAKE 1: "P⇒Q is false when P is false"
  WRONG! P⇒Q is TRUE whenever P is false.
  Remember: false premise = promise not tested = not broken!

MISTAKE 2: "P∨Q means exactly one is true"
  WRONG! P∨Q is true when EITHER or BOTH are true.
  The "exclusive or" (exactly one) is a different operation (⊕).

MISTAKE 3: "If Breeze(1,1), then Pit(1,2)"
  WRONG! Breeze(1,1) means Pit(1,2) ∨ Pit(2,1).
  You can't pick just one — that's UNSOUND reasoning!

MISTAKE 4: Forgetting operator precedence
  ¬A ∧ B means (¬A) ∧ B, NOT ¬(A∧B)
  Always apply ¬ first, then ∧, then ∨, then ⇒, then ⇔

MISTAKE 5: Confusing Entailment (⊨) with Inference (⊢)
  ⊨ = "truth logically follows" (mathematical fact)
  ⊢ = "algorithm can derive it" (computational ability)
  An algorithm might not derive something even if it's entailed!
```

---

## 🎯 Problem-Solving Strategy Cheatsheet

```
╔══════════════════════════════════════════════════════╗
║          HOW TO SOLVE LOGIC PROBLEMS                 ║
╠══════════════════════════════════════════════════════╣
║ 1. IDENTIFY symbols (P, Q, R...)                    ║
║ 2. COUNT models (2ⁿ)                                ║
║ 3. BUILD truth table                                 ║
║ 4. EVALUATE KB in each model                        ║
║ 5. CHECK query in KB-true models                    ║
║ 6. ALL true? → entailed. Some false? → not entailed ║
║                                                      ║
║ SHORTCUTS:                                           ║
║  • P⇒Q false ONLY when P=T, Q=F                    ║
║  • P⇔Q means both ⇒ directions                     ║
║  • ¬(A∨B) = ¬A ∧ ¬B (De Morgan's)                  ║
║  • If A∨B and ¬A, then B (elimination)              ║
║  • Biconditional + false side → other side false     ║
╚══════════════════════════════════════════════════════╝
```

---

> 📝 **Numerical Guide for AI Unit III** | 🔗 [Theory Guide →](./logical_agents_theory_guide.md) | 🎯 [Exam Guide →](./logical_agents_exam_guide.md) | 🗺️ [Mind Map →](./logical_agents_mindmap.png)
