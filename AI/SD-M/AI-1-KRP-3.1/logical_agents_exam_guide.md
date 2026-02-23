# 🎯 Logical Agents — Minor Exam Preparation Guide
### AI Unit III: Knowledge, Reasoning, and Planning
#### Dr.: SD-M | Based on Russell & Norvig (3rd Edition)
#### EP-Focused: 8-10 Expected Questions with Model Answers

---

## 📚 Table of Contents

| # | Section | What's Inside |
|---|---------|--------------|
| 1 | [Exam Strategy & Tips](#-exam-strategy--tips) | How to approach the paper |
| 2 | [Question 1: KB Agent Architecture](#question-1-knowledge-based-agent-architecture) | Diagram + TELL/ASK/Inference |
| 3 | [Question 2: Wumpus World PEAS & Setup](#question-2-wumpus-world-peas-description) | PEAS + environment properties |
| 4 | [Question 3: Agent Reasoning Walkthrough](#question-3-wumpus-world-agent-reasoning-walkthrough) | Step-by-step inference in cave |
| 5 | [Question 4: Truth Table & Entailment](#question-4-truth-table-construction--entailment-check) | Build table + check KB ⊨ α |
| 6 | [Question 5: Propositional Logic Semantics](#question-5-propositional-logic--evaluate-sentences) | Evaluate in a given model |
| 7 | [Question 6: Soundness vs Completeness](#question-6-soundness-vs-completeness-analysis) | Identify unsound/incomplete |
| 8 | [Question 7: Forward & Backward Chaining](#question-7-forward--backward-chaining-trace) | Full trace with facts & rules |
| 9 | [Question 8: KB Construction from Scratch](#question-8-building-a-knowledge-base) | Write formal sentences |
| 10 | [Question 9: Entailment via Model Checking](#question-9-model-checking--entailment-in-wumpus-world) | 8-model enumeration |
| 11 | [Question 10: Short Answer Rapid Fire](#question-10-short-answer--conceptual-rapid-fire) | Quick theory questions |
| 12 | [Last-Minute Revision Cheatsheet](#-last-minute-revision-cheatsheet) | Print-friendly one-pager |

---

> 🔗 **Companion Guides:**
> - [Theory Guide (Full Concepts)](./logical_agents_theory_guide.md)
> - [Numerical Guide (14 Solved Problems)](./logical_agents_numerical_guide.md)
> - [Mind Map (Visual Overview)](./logical_agents_mindmap.png)

---

## 🧠 Exam Strategy & Tips

### Before You Open the Paper
```
╔═══════════════════════════════════════════════════════════════╗
║                    EXAM GAME PLAN                             ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  ✅ Read ALL questions first (2 mins)                        ║
║  ✅ Start with what you know best                            ║
║  ✅ Draw diagrams — they earn extra marks!                   ║
║  ✅ Use proper notation: ⊨ ¬ ∧ ∨ ⇒ ⇔                      ║
║  ✅ Label steps clearly (Step 1, Step 2...)                  ║
║  ✅ Mention keywords from slides (the professor checks!)     ║
║                                                               ║
║  ❌ Don't skip truth table rows — show ALL rows              ║
║  ❌ Don't confuse ⇒ (implication) with ⇔ (biconditional)   ║
║  ❌ Don't write "P implies Q is false" when P is false       ║
║     (Remember: P⇒Q is TRUE when P is false!)                ║
╚═══════════════════════════════════════════════════════════════╝
```

### What the Professor Likely Tests (Based on Slide Emphasis)
```
HIGH PROBABILITY (almost certainly appears):
  ★★★ Wumpus World walkthrough / inference reasoning
  ★★★ Truth table construction / evaluation
  ★★★ KB ⊨ α entailment checking
  ★★★ PEAS description for Wumpus World
  ★★★ Forward OR backward chaining trace

MEDIUM PROBABILITY:
  ★★  Soundness vs Completeness definitions + examples
  ★★  Declarative vs Procedural approach
  ★★  Types of logic comparison
  ★★  Operator precedence / parsing sentences

LOW PROBABILITY (but know the basics):
  ★   Grounding concept
  ★   Model checking pseudocode
  ★   Formal grammar of propositional logic
```

---

## Question 1: Knowledge-Based Agent Architecture
**Expected: 5-8 marks | Type: Diagram + Short Explanation**

### 📝 Likely Question
> *"Draw and explain the architecture of a Knowledge-Based Agent. What are the roles of TELL, ASK, and Inference? Give an example."*

### ✅ Model Answer

**Step 1: Draw this diagram (earns marks even before text!)**
```
       ┌──────────────────────────────────────────────┐
       │           Knowledge-Based Agent               │
       │                                               │
       │  ┌─────────────┐     ┌──────────────────┐    │
Input ─┼─▶│  Inference   │◄───▶│  Knowledge Base  │    │
from   │  │   Engine     │     │    (KB)          │    │
Env.   │  │              │     │                  │    │
       │  │  • Derives   │     │  • Set of        │    │
       │  │    new facts │     │    sentences      │    │
       │  │  • Uses      │     │  • Background     │    │
       │  │    TELL/ASK  │     │    rules + facts  │    │
       │  └──────┬───────┘     └────────┬─────────┘    │
       │         │                      │              │
       │         │    ┌────────────┐    │              │
       │         └───▶│  Learning  │◄───┘              │
       │              │(Update KB) │                    │
       │              └────────────┘                    │
       └─────────────────────┬────────────────────────┘
                             │
                         Output ──▶ Action
```

**Step 2: Explain the three operations**

| Operation | What It Does | Real-World Analogy |
|-----------|-------------|-------------------|
| **TELL** | Adds new sentences (facts/rules) to the KB | Writing in your notebook: "Patient has fever" |
| **ASK** | Queries the KB for what is known | Asking your notebook: "Does this patient have measles?" |
| **Inference** | Derives NEW facts from existing ones | Your brain combining: fever + rash = measles |

**Step 3: Give an example (MYCIN earns bonus points!)**
```
Example: MYCIN (Stanford, 1970s) — Medical expert system

KB contains rules like:
  IF gram-positive bacteria AND rod-shaped THEN suggest antibiotic X

Doctor TELLs the system: "Patient sample is gram-positive, rod-shaped"
Doctor ASKs: "What antibiotic should I prescribe?"
Inference Engine matches rules → Outputs: "Antibiotic X"
```

**Key sentence to write:** *"A knowledge base is a set of sentences expressed in a knowledge representation language, and inference must obey the requirement that answers follow from what has been previously told."*

---

## Question 2: Wumpus World PEAS Description
**Expected: 5-8 marks | Type: Table/Description + Environment Classification**

### 📝 Likely Question
> *"Describe the Wumpus World environment using the PEAS framework. Classify it as observable/unobservable, static/dynamic, etc."*

### ✅ Model Answer

**PEAS Table (draw this neatly — professors love tables!):**

| Component | Description | Details |
|-----------|------------|---------|
| **P**erformance | Scoring system | +1000 (gold + climb out), −1000 (death by pit/wumpus), −1 (per action), −10 (using arrow) |
| **E**nvironment | 4×4 grid cave | Agent starts at [1,1] facing right. Gold, wumpus placed randomly. Each non-start square has 0.2 probability of pit |
| **A**ctuators | Agent's actions | Forward, TurnLeft (90°), TurnRight (90°), Grab, Shoot, Climb (only at [1,1]) |
| **S**ensors | 5 percepts | Stench (wumpus nearby), Breeze (pit nearby), Glitter (gold here), Bump (hit wall), Scream (wumpus killed) |

**Environment Classification (frequently asked!):**

| Property | Classification | Reason |
|----------|---------------|--------|
| Observable | **Partially** observable | Agent can't see other rooms, only gets percepts in current room |
| Deterministic | **Deterministic** | Actions have predictable outcomes |
| Sequential | **Sequential** | Current actions affect future rewards; not just one-step |
| Static | **Static** | Wumpus and pits don't move while agent thinks |
| Discrete | **Discrete** | Finite number of states, actions, percepts |
| Single-agent | **Single-agent** | Wumpus is a feature of environment, not a competing agent |

**Key sentence to write:** *"The main challenge is the agent's initial ignorance of the environment configuration; overcoming this ignorance requires logical reasoning."*

---

## Question 3: Wumpus World Agent Reasoning Walkthrough
**Expected: 8-12 marks | Type: Step-by-step trace with grid diagrams**

### 📝 Likely Question
> *"Trace the knowledge-based agent's exploration of the Wumpus World. Show the agent's reasoning at each step, including what it infers and why."*

### ✅ Model Answer

**Step 1: Initial position [1,1]**
```
Percept: [None, None, None, None, None]

  4 │     │     │     │     │
    ├─────┼─────┼─────┼─────┤     REASONING:
  3 │     │     │     │     │     No stench → no wumpus in [1,2] or [2,1]
    ├─────┼─────┼─────┼─────┤     No breeze → no pit in [1,2] or [2,1]
  2 │ OK  │     │     │     │     
    ├─────┼─────┼─────┼─────┤     CONCLUSION: [1,2] and [2,1] are SAFE
  1 │A,OK │ OK  │     │     │     Agent decides: move to [2,1]
    └─────┴─────┴─────┴─────┘
      1     2     3     4
```

**Step 2: At [2,1]**
```
Percept: [None, Breeze, None, None, None]

  4 │     │     │     │     │
    ├─────┼─────┼─────┼─────┤     REASONING:
  3 │     │     │     │     │     Breeze → pit in a neighbor of [2,1]
    ├─────┼─────┼─────┼─────┤     Neighbors: [1,1], [2,2], [3,1]
  2 │ OK  │ P?  │     │     │     ¬P₁₁ (game rule) → not [1,1]
    ├─────┼─────┼─────┼─────┤     So: Pit(2,2) ∨ Pit(3,1)
  1 │V,OK │A,B  │ P?  │     │     
    └─────┴─────┴─────┴─────┘     DECISION: Go back, try [1,2]
      1     2     3     4
```

**Step 3: At [1,2] — THE KEY INFERENCE STEP**
```
Percept: [Stench, None, None, None, None]

  4 │     │     │     │     │     REASONING (this is the hard part!):
    ├─────┼─────┼─────┼─────┤
  3 │ W!  │     │     │     │     Stench at [1,2] → wumpus nearby
    ├─────┼─────┼─────┼─────┤       Candidates: [1,1], [2,2], [1,3]
  2 │A,S  │ OK  │     │     │       ¬W₁₁ (game rule eliminates [1,1])
    │OK   │     │     │     │       ¬W₂₂ (no stench at [2,1] eliminates [2,2])
    ├─────┼─────┼─────┼─────┤       ∴ Wumpus at [1,3]! (W!)
  1 │V,OK │V,B  │ P!  │     │
    └─────┴─────┴─────┴─────┘     No breeze at [1,2] → ¬P₂₂
      1     2     3     4           Earlier: P₂₂ ∨ P₃₁ and ¬P₂₂
                                    ∴ Pit at [3,1]! (P!)
                                    [2,2] is SAFE! (no pit, no wumpus)
```

**Step 4: Through [2,2] to [2,3]**
```
Percept at [2,3]: [Stench, Breeze, Glitter, None, None]
  → GLITTER means GOLD IS HERE!
  → Grab gold, navigate back to [1,1], Climb out
  → Score: +1000 − (actions) ≈ +980 🎉
```

**The critical insight to write:**
> *"This inference is remarkable because it combines knowledge gained at different times (breeze at [2,1] earlier + stench at [1,2] now) and different places, and relies on the ABSENCE of a percept (no stench at [2,1]) as a crucial clue. This is what logical reasoning enables that reactive agents cannot do."*

---

## Question 4: Truth Table Construction & Entailment Check
**Expected: 6-10 marks | Type: Build truth table, then check entailment**

### 📝 Likely Question
> *"Construct the truth table for (P ⇒ Q) ∧ (Q ⇒ R). Does this sentence entail P ⇒ R? Prove using model checking."*

### ✅ Model Answer

**Step 1: Identify symbols → P, Q, R (3 symbols → 2³ = 8 rows)**

**Step 2: Build truth table (show ALL rows — don't skip!)**
```
Row│ P │ Q │ R │ P⇒Q │ Q⇒R │ (P⇒Q)∧(Q⇒R) │ P⇒R │
───┼───┼───┼───┼─────┼─────┼──────────────┼─────┤
 1 │ F │ F │ F │  T  │  T  │      T       │  T  │
 2 │ F │ F │ T │  T  │  T  │      T       │  T  │
 3 │ F │ T │ F │  T  │  F  │      F       │  T  │
 4 │ F │ T │ T │  T  │  T  │      T       │  T  │
 5 │ T │ F │ F │  F  │  T  │      F       │  F  │
 6 │ T │ F │ T │  F  │  T  │      F       │  T  │
 7 │ T │ T │ F │  T  │  F  │      F       │  F  │
 8 │ T │ T │ T │  T  │  T  │      T       │  T  │
```

**How I computed P⇒Q:** FALSE only when P=T, Q=F (rows 5,6). All others = TRUE.

**How I computed the AND:** TRUE only when BOTH P⇒Q and Q⇒R are TRUE.

**Step 3: Check entailment**
```
Rows where (P⇒Q)∧(Q⇒R) is TRUE: rows 1, 2, 4, 8
In those rows, P⇒R values are:      T, T, T, T  ← ALL TRUE!

Since P⇒R is TRUE in EVERY model where the KB sentence is TRUE:
  M((P⇒Q)∧(Q⇒R)) ⊆ M(P⇒R)

∴ (P⇒Q) ∧ (Q⇒R) ⊨ P⇒R  ✅  [Transitivity of implication]
```

**Key sentence:** *"This demonstrates the transitivity of implication: if P implies Q and Q implies R, then P implies R."*

---

## Question 5: Propositional Logic — Evaluate Sentences
**Expected: 4-6 marks | Type: Plug in values, compute step by step**

### 📝 Likely Question
> *"Given the model m = {P₁₂=false, P₂₂=false, P₃₁=true}, evaluate:*
> *(a) ¬P₁₂ ∧ (P₂₂ ∨ P₃₁)  (b) P₁₂ ⇒ (P₂₂ ∧ P₃₁)  (c) (P₁₂ ∨ P₂₂) ⇔ P₃₁"*

### ✅ Model Answer

**(a) ¬P₁₂ ∧ (P₂₂ ∨ P₃₁)**
```
= ¬(false) ∧ (false ∨ true)        ← Substitute values
= true ∧ (false ∨ true)            ← ¬false = true
= true ∧ true                      ← false ∨ true = true (OR: at least one true)
= true  ✅                          ← AND: both true → true
```

**(b) P₁₂ ⇒ (P₂₂ ∧ P₃₁)**
```
= false ⇒ (false ∧ true)           ← Substitute
= false ⇒ false                    ← false ∧ true = false
= true  ✅                          ← REMEMBER: false⇒anything = TRUE
                                      (promise not tested = not broken!)
```

**(c) (P₁₂ ∨ P₂₂) ⇔ P₃₁**
```
= (false ∨ false) ⇔ true           ← Substitute
= false ⇔ true                     ← false ∨ false = false
= false  ❌                         ← Biconditional: sides must MATCH
                                      (false ≠ true, so result is false)
```

---

## Question 6: Soundness vs Completeness Analysis
**Expected: 4-6 marks | Type: Define, compare, give examples**

### 📝 Likely Question
> *"Define soundness and completeness of inference algorithms. Give an example of an unsound inference and an incomplete inference from the Wumpus World."*

### ✅ Model Answer

**Definitions:**

| Property | Definition | One-Line Memory Aid |
|----------|-----------|-------------------|
| **Sound** | An algorithm is sound if it derives ONLY sentences that are logically entailed by the KB | "I never say anything wrong" |
| **Complete** | An algorithm is complete if it can derive EVERY sentence that is logically entailed by the KB | "I find every truth that exists" |

**Model checking is BOTH sound and complete** (but has O(2ⁿ) time complexity).

**Unsound Example (from slides):**
```
KB: Breeze(1,1) is true
Correct entailment: Pit(1,2) ∨ Pit(2,1)  [pit in one OR both neighbors]

Unsound algorithm concludes: Pit(1,2)  ← WRONG!

This is UNSOUND because:
  KB ⊭ Pit(1,2) — the KB does NOT entail this specific claim
  The algorithm converted a disjunction (OR) into a specific fact
  That's like a judge convicting a specific person when they only know 
  "one of two suspects did it" — that's an unjust conviction!
```

**Incomplete Example (from slides):**
```
KB contains:
  From Breeze(2,1): Pit(2,2) ∨ Pit(3,1)
  From Breeze(1,2): Pit(2,2) ∨ Pit(1,3)

Complete algorithm would combine these via resolution:
  Common element = Pit(2,2) → therefore KB ⊨ Pit(2,2)

Incomplete algorithm processes each breeze separately:
  It knows Pit(2,2)∨Pit(3,1) and Pit(2,2)∨Pit(1,3)
  But it never COMBINES them → never deduces Pit(2,2)

  The missing step is RESOLUTION — failing to resolve
  two disjunctions together causes incompleteness.
```

---

## Question 7: Forward & Backward Chaining Trace
**Expected: 6-8 marks | Type: Show full trace with iterations**

### 📝 Likely Question
> *"Given these rules and facts, trace both forward chaining and backward chaining to determine if 'isolate_patient' can be derived."*
>
> *Rules: R1: fever ∧ rash → measles, R2: measles → isolate_patient, R3: fever ∧ cough → flu*
> *Facts: {fever, rash}*

### ✅ Model Answer — Forward Chaining (Data-Driven)

```
Start: Known facts = {fever, rash}

ITERATION 1:
  Check R1: fever ✅ AND rash ✅ → ALL premises met → FIRE!
    → Add "measles" to KB
  Check R2: measles? → Not yet in KB at start of iteration
  Check R3: fever ✅ AND cough? ❌ → Cannot fire
  New facts: {fever, rash, measles}

ITERATION 2:
  Check R1: Already fired (skip)
  Check R2: measles ✅ → FIRE!
    → Add "isolate_patient" to KB
  Check R3: cough still missing → Cannot fire
  New facts: {fever, rash, measles, isolate_patient}

ITERATION 3:
  No new rules can fire → STOP ✅

RESULT: isolate_patient IS derived ✅
  Derivation chain: fever + rash → measles → isolate_patient
  Note: R3 (flu) was NEVER triggered because "cough" was absent
```

### ✅ Model Answer — Backward Chaining (Goal-Driven)

```
GOAL: isolate_patient?

Step 1: Which rule concludes "isolate_patient"?
        → R2: IF measles → isolate_patient
        Sub-goal: Is "measles" true?

  Step 2: Is "measles" a known fact? → NO
          Which rule concludes "measles"?
          → R1: IF fever AND rash → measles
          Sub-goals: fever? AND rash?

    Step 3: Is "fever" a known fact? → YES ✅ (in KB)
    Step 4: Is "rash" a known fact?  → YES ✅ (in KB)

  Step 2 resolved: fever ∧ rash → measles PROVEN ✅

Step 1 resolved: measles → isolate_patient PROVEN ✅

FINAL: isolate_patient = TRUE ✅

PROOF TREE:
                isolate_patient ✅
                      │ R2
                   measles ✅
                    /    \
               R1 /      \ R1
                 /        \
            fever ✅    rash ✅
           (fact)      (fact)

KEY DIFFERENCE: Backward chaining NEVER looked at R3 (flu rule)
because it wasn't relevant to the goal. More efficient for specific queries!
```

---

## Question 8: Building a Knowledge Base
**Expected: 5-8 marks | Type: Write formal propositional logic sentences**

### 📝 Likely Question
> *"The agent is in the Wumpus World and has reached [2,1]. Write the formal KB sentences (using propositional logic) that the agent would use to reason about pits."*

### ✅ Model Answer

**Symbols defined:**
```
Pxy = "There is a pit at square [x,y]"
Bxy = "Agent perceives a breeze at square [x,y]"
```

**KB Sentences:**
```
R₁:  ¬P₁₁                          "No pit at start" (game rule)

R₂:  B₁₁ ⇔ (P₁₂ ∨ P₂₁)           "Breeze at [1,1] iff pit in 
                                       neighbor [1,2] or [2,1]"

R₃:  B₂₁ ⇔ (P₁₁ ∨ P₂₂ ∨ P₃₁)    "Breeze at [2,1] iff pit in
                                       neighbor [1,1], [2,2], or [3,1]"

R₄:  ¬B₁₁                          "No breeze perceived at [1,1]"
                                      (agent's observation)

R₅:  B₂₁                           "Breeze perceived at [2,1]"
                                      (agent's observation)
```

**Why use ⇔ (biconditional) and not just ⇒?**
```
Because the breeze rule works BOTH directions:
  B₁₁ ⇒ (P₁₂ ∨ P₂₁)    "If breeze, then pit nearby"
  (P₁₂ ∨ P₂₁) ⇒ B₁₁    "If pit nearby, then breeze"

Using just ⇒ gives only ONE direction → incomplete reasoning!
Using ⇔ gives BOTH directions → complete reasoning ✅

A square is breezy IF AND ONLY IF a neighboring square has a pit.
```

**Key sentence:** *"R₁–R₃ are general rules true in all Wumpus worlds. R₄–R₅ are specific observations (percepts) from this particular world instance."*

---

## Question 9: Model Checking & Entailment in Wumpus World
**Expected: 8-10 marks | Type: Enumerate models, check entailment**

### 📝 Likely Question
> *"Using the KB from the previous question (R₁–R₅), determine whether KB ⊨ ¬P₁₂ (no pit at [1,2]) and whether KB ⊨ ¬P₂₂ (no pit at [2,2]). Use model checking."*

### ✅ Model Answer

**Step 1: Identify relevant symbols**
```
Symbols: P₁₂, P₂₂, P₃₁ (3 unknown symbols)
Total models: 2³ = 8
```

**Step 2: Enumerate ALL 8 models and check which satisfy the KB**
```
Model│P₁₂│P₂₂│P₃₁│ R₁  │ R₂      │ R₃         │ R₄  │ R₅  │KB?
─────┼────┼────┼────┼─────┼─────────┼────────────┼─────┼─────┼────
  1  │ F  │ F  │ F  │  T  │T⇔F→T   │T⇔(F∨F∨F)→F│  T  │  T  │ ❌
     │    │    │    │     │(¬B,¬P:T)│(B₂₁=T but  │     │     │
     │    │    │    │     │         │ no pits→F)  │     │     │
  2  │ F  │ F  │ T  │  T  │  T     │     T      │  T  │  T  │ ✅
  3  │ F  │ T  │ F  │  T  │  T     │     T      │  T  │  T  │ ✅
  4  │ F  │ T  │ T  │  T  │  T     │     T      │  T  │  T  │ ✅
  5  │ T  │ F  │ F  │  T  │  F     │     F      │  T  │  T  │ ❌
  6  │ T  │ F  │ T  │  T  │  F     │     T      │  T  │  T  │ ❌
  7  │ T  │ T  │ F  │  T  │  F     │     T      │  T  │  T  │ ❌
  8  │ T  │ T  │ T  │  T  │  F     │     T      │  T  │  T  │ ❌
```

**Why models 5-8 fail:** P₁₂=T means pit at [1,2]. But R₂ says B₁₁⇔(P₁₂∨P₂₁). Since P₁₂=T, the right side is T, so B₁₁ must be T. But R₄ says ¬B₁₁. Contradiction! → KB is false.

**Why model 1 fails:** All pit symbols are F. R₃ says B₂₁⇔(P₁₁∨P₂₂∨P₃₁). Right side = F∨F∨F = F. But R₅ says B₂₁=T. So left side=T but right=F → biconditional is false → KB is false.

**Step 3: Check entailment**
```
Valid models (where KB is TRUE): models 2, 3, 4

Check α₁ = ¬P₁₂ ("no pit at [1,2]"):
  Model 2: P₁₂=F → ¬P₁₂ = TRUE ✅
  Model 3: P₁₂=F → ¬P₁₂ = TRUE ✅
  Model 4: P₁₂=F → ¬P₁₂ = TRUE ✅
  ALL valid models agree → KB ⊨ ¬P₁₂ ✅
  "There is definitely NO pit at [1,2]"

Check α₂ = ¬P₂₂ ("no pit at [2,2]"):
  Model 2: P₂₂=F → ¬P₂₂ = TRUE ✅
  Model 3: P₂₂=T → ¬P₂₂ = FALSE ❌
  Model 4: P₂₂=T → ¬P₂₂ = FALSE ❌
  NOT all valid models agree → KB ⊭ ¬P₂₂ ❌
  "Cannot conclude whether there is a pit at [2,2] or not"
```

**Key sentence:** *"Model checking directly implements the definition of entailment: enumerate all possible models, check that α is true in every model where KB is true. It is sound and complete but has time complexity O(2ⁿ)."*

---

## Question 10: Short Answer / Conceptual Rapid Fire
**Expected: 10-15 marks | Type: 1-2 line answers each**

### 📝 Likely Questions & Model Answers

**Q1: What is the formula for logical entailment?**
```
α ⊨ β  iff  M(α) ⊆ M(β)

"α entails β if and only if the set of all models where α is true
 is a SUBSET of the set of all models where β is true."
```

**Q2: When is P ⇒ Q false?**
```
P ⇒ Q is false ONLY when P is true and Q is false.
In all other cases (P false, or Q true), the implication is true.
"A promise is only broken if you said you would (T) but didn't (F)."
```

**Q3: What is the difference between entailment and inference?**
```
Entailment (⊨) = the truth EXISTS (semantic/mathematical property)
Inference (⊢)  = FINDING that truth (algorithmic/computational process)

Analogy: Entailment = needle IS in the haystack.
         Inference = actually FINDING the needle.
```

**Q4: What is the operator precedence in propositional logic?**
```
¬ > ∧ > ∨ > ⇒ > ⇔   (highest to lowest)

So: ¬A ∧ B ∨ C = ((¬A) ∧ B) ∨ C    (NOT first, then AND, then OR)
```

**Q5: What is the difference between declarative and procedural approaches?**
```
Declarative: TELL facts/rules to KB → WHAT is true
  Example: MYCIN → "IF gram-positive AND rod-shaped THEN antibiotic X"

Procedural: Encode knowledge as code → HOW to do things
  Example: Step 1: Check temperature, Step 2: If >38°C check rash...

Best approach: Combine both! Declarative knowledge can be compiled
into efficient procedural code.
```

**Q6: How many models exist for n proposition symbols?**
```
2ⁿ models. Each symbol can be TRUE or FALSE independently.
Example: 3 symbols → 2³ = 8 models
         7 symbols → 2⁷ = 128 models (as in the Wumpus KB example)
```

**Q7: What does it mean for a Wumpus World to be "partially observable"?**
```
The agent CANNOT see the entire state of the environment.
It doesn't know where the wumpus, pits, or gold are.
It only gets indirect clues through percepts (stench, breeze, glitter).
This is WHY logical reasoning is necessary — to figure out
hidden facts from partial information.
```

**Q8: Name 3 types of logic used in AI.**
```
1. Propositional Logic — facts are TRUE/FALSE propositions
2. First-Order Logic (FOL) — adds objects, relations, quantifiers (∀, ∃)
3. Fuzzy Logic — allows degrees of truth (e.g., 0.7 hot)
Others: Probabilistic Logic, Non-monotonic Logic, Description Logic
```

**Q9: What is grounding in the context of logic?**
```
Grounding = connecting logical sentences to the real world.
- Percepts (breezes, smells) come from sensors → grounded by construction
- Abstract rules ("wumpuses cause stench") come from learning
- Learning is fallible, so the KB might not be perfectly true
```

**Q10: Why is the inference at step 3 of the Wumpus exploration "remarkable"?**
```
Because it:
1. Combines knowledge from DIFFERENT TIMES (breeze at [2,1] earlier)
2. Combines knowledge from DIFFERENT PLACES ([2,1] info + [1,2] info)
3. Uses the ABSENCE of a percept (no stench at [2,1]) as a crucial clue

This multi-step, cross-temporal, cross-spatial reasoning is what
separates logical agents from simple reactive agents.
```

---

## 📋 Last-Minute Revision Cheatsheet

```
╔══════════════════════════════════════════════════════════════════════╗
║              LOGICAL AGENTS — EXAM CHEATSHEET                        ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  CORE FORMULA: Knowledge + Reasoning = Intelligence                  ║
║                                                                      ║
║  KB OPERATIONS: TELL (add) → ASK (query) → INFER (derive)          ║
║                                                                      ║
║  4 LOGIC PILLARS: Syntax → Semantics → Models → Entailment          ║
║  Mnemonic: "Some Smart Minds Entail"                                 ║
║                                                                      ║
║  ENTAILMENT:  α ⊨ β  iff  M(α) ⊆ M(β)                             ║
║  INFERENCE:   KB ⊢ᵢ α  (algorithm i derives α from KB)             ║
║                                                                      ║
║  SOUND = never derives wrong conclusions (safe judge)                ║
║  COMPLETE = finds every true conclusion (thorough detective)         ║
║                                                                      ║
║  5 CONNECTIVES + PRECEDENCE:                                         ║
║    ¬ (NOT) > ∧ (AND) > ∨ (OR) > ⇒ (IMPLIES) > ⇔ (IFF)            ║
║    "Naughty Ants Often Irritate Insects"                             ║
║                                                                      ║
║  IMPLICATION: P⇒Q FALSE only when P=T, Q=F                         ║
║  BICONDITIONAL: P⇔Q TRUE only when both sides MATCH                 ║
║                                                                      ║
║  MODEL CHECKING: O(2ⁿ) time, O(n) space, sound + complete           ║
║  n symbols → 2ⁿ possible models to check                            ║
║                                                                      ║
║  FORWARD CHAIN:  facts → rules → conclusions (data-driven)          ║
║  BACKWARD CHAIN: goal → rules → check premises (goal-driven)        ║
║                                                                      ║
║  WUMPUS WORLD:                                                       ║
║    4×4 grid │ +1000 gold, -1000 death, -1/action, -10 arrow         ║
║    Percepts: Stench, Breeze, Glitter, Bump, Scream (SBG-BS)         ║
║    Actions:  Forward, TurnL/R, Grab, Shoot, Climb                    ║
║    Key: ⇔ rules for breeze/stench (both directions!)                ║
║                                                                      ║
║  DECLARATIVE = WHAT is true (MYCIN rules)                            ║
║  PROCEDURAL  = HOW to do it (decision procedure steps)               ║
║                                                                      ║
║  EXAM TRAPS TO AVOID:                                                ║
║    ✗ P⇒Q is NOT false when P is false (it's TRUE!)                 ║
║    ✗ Don't convert P∨Q into just P (that's UNSOUND)                 ║
║    ✗ ⇔ means BOTH directions, not just one                          ║
║    ✗ Absence of percept IS useful information!                       ║
╚══════════════════════════════════════════════════════════════════════╝
```

---

> 📝 **Exam Guide for AI Unit III** | 🔗 [Theory Guide →](./logical_agents_theory_guide.md) | 🔢 [Numerical Guide →](./logical_agents_numerical_guide.md) | 🗺️ [Mind Map →](./logical_agents_mindmap.png)
