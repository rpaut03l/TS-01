# 🧠 Logical Agents — Complete Theory Guide
### AI Unit III: Knowledge, Reasoning, and Planning
#### Based on *Artificial Intelligence: A Modern Approach* (Russell & Norvig, 3rd Edition)
#### Dr: SD,M. | Slides: Logical Agents (KRP-3.1 | Norvig)

---

## 📚 Table of Contents

| # | Topic | Jump Link |
|---|-------|-----------|
| 1 | [Introduction & Big Picture](#1--introduction--big-picture) | Why this matters |
| 2 | [From Reactive to Reasoning Agents](#2--from-reactive-to-reasoning-agents) | The evolution |
| 3 | [Why Study Logic?](#3--why-study-logic) | The "recipe" for intelligence |
| 4 | [Knowledge-Based Agents (KBA)](#4--knowledge-based-agents-kba) | The core architecture |
| 5 | [Declarative vs Procedural Approach](#5--declarative-vs-procedural-approach) | Two ways to build a KB |
| 6 | [The Wumpus World](#6--the-wumpus-world) | Our playground environment |
| 7 | [PEAS Description](#7--peas-description) | Performance, Environment, Actuators, Sensors |
| 8 | [Agent Walkthrough in Wumpus World](#8--agent-walkthrough-in-wumpus-world) | Step-by-step exploration |
| 9 | [Logic — The Skeleton](#9--logic--the-skeleton) | Syntax, Semantics, Models, Entailment |
| 10 | [Entailment in the Wumpus World](#10--entailment-in-the-wumpus-world) | Model checking example |
| 11 | [Inference: Soundness & Completeness](#11--inference-soundness--completeness) | Correctness guarantees |
| 12 | [Forward & Backward Chaining](#12--forward--backward-chaining) | Two inference strategies |
| 13 | [Types of Logic](#13--types-of-logic) | Propositional, FOL, Fuzzy, etc. |
| 14 | [Propositional Logic — Syntax](#14--propositional-logic--syntax) | Building sentences |
| 15 | [Propositional Logic — Semantics](#15--propositional-logic--semantics) | Truth tables & meaning |
| 16 | [Building a Wumpus World KB](#16--building-a-wumpus-world-kb) | Practical KB construction |
| 17 | [Model Checking Inference](#17--model-checking-inference) | The brute-force algorithm |
| 18 | [Mnemonics & Memory Aids](#18--mnemonics--memory-aids) | Quick recall tricks |
| 19 | [Cheatsheet](#19--cheatsheet) | One-page summary |
| 20 | [Real-World Examples](#20--real-world-examples) | Where this is used today |
| 21 | [Quick Revision Q&A](#21--quick-revision-qa) | Test yourself |

---

> 🔗 **Companion Guide:** [Numerical Problems & Step-by-Step Solutions](./logical_agents_numerical_guide.md)
>
> 🎯 **Exam Prep:** [Minor Exam Guide — 10 Expected Questions with Model Answers](./logical_agents_exam_guide.md)
>
> 🗺️ **Mind Map:** [Visual Mind Map](./logical_agents_mindmap.png)

---

## 🟢 Before You Begin — Zero-Knowledge Primer

**Never studied AI or logic before? No problem! Here's everything you need in 2 minutes:**

### What is an "Agent"?
An agent is just a **computer program** that can sense things around it and take actions. Think of a Roomba vacuum — it senses walls and dirt, then decides where to move. That's an agent!

### What is "Logic"?
Logic is just a way to write down **facts and rules**, then use those facts and rules to figure out **new facts** automatically. It's like solving a puzzle where each clue narrows down what's true.

### What is a "Knowledge Base"?
A knowledge base (KB) is like a **notebook** where an agent writes down everything it knows. When it needs to make a decision, it reads the notebook and figures out what to do.

### What are Symbols like P, Q, ⇒, ⊨?
These are just **shorthand** — like how in math "+" means "add." Here's a quick decoder ring:

```
SYMBOL DECODER RING (keep this handy! 👆)
──────────────────────────────────────────
P, Q, R        = Simple statements (like "it is raining")
¬P             = "NOT P" (the opposite — "it is NOT raining")
P ∧ Q          = "P AND Q" (both must be true)
P ∨ Q          = "P OR Q" (at least one is true)
P ⇒ Q          = "IF P THEN Q" (P causes/requires Q)
P ⇔ Q          = "P IF AND ONLY IF Q" (they always match)
KB             = Knowledge Base (the notebook of facts)
⊨ (double turnstile) = "logically guarantees" or "entails"
KB ⊨ α         = "what we know GUARANTEES α is true"
M(α)           = "all situations where α is true"
```

### The ONE Big Idea of This Entire Chapter
```
╔═══════════════════════════════════════════════╗
║   KNOWLEDGE  +  REASONING  =  INTELLIGENCE   ║
║                                               ║
║   (what you know)  (thinking)  (smart action) ║
╚═══════════════════════════════════════════════╝
```

An agent that **stores facts** and uses **logic rules** to figure out new facts can behave **intelligently** — even in situations it has never seen before!

> 🎯 **Reading Tip:** Every section has a "Mind-Friendly" box (💡) at the end. If a section feels confusing, jump to that box first for the simple version, then re-read the details!

---

## 1. 🌍 Introduction & Big Picture

### 📖 How to Study This Guide (Recommended Order)
```
First time reading? Follow this path:
  1. Read Section 1-3 (Big picture — 5 mins)
  2. Read Section 6-8 (Wumpus World story — fun! — 10 mins)
  3. Read Section 4-5 (KB Agents — now they make sense! — 5 mins)
  4. Read Section 9 (Logic skeleton — 5 mins)
  5. Read Section 14-15 (Propositional Logic — 15 mins, take notes!)
  6. Read Section 10-11 (Entailment & Inference — 10 mins)
  7. Read Section 12 (Forward/Backward chaining — 5 mins)
  8. Use Section 18-21 for revision before exams!
  9. Then do the Numerical Guide problems!
```

### What is this chapter about?

Imagine you're dropped into a **dark cave**. You can't see everything. You smell something weird. You feel wind blowing. Now — should you move forward or go back?

**This chapter teaches an AI agent how to THINK through exactly this kind of problem.**

### The Course Journey (Unit III → Unit IV)

Think of it like learning to drive:

| Unit III (This one!) | Unit IV (Next!) |
|---|---|
| 🚗 Driving with a **perfect GPS** | 🚗 Driving in **fog with a broken GPS** |
| World is clear: facts & rules | World is noisy & uncertain |
| Agent **knows** the rules | Agent must **learn** the rules |
| Planning with **known outcomes** | Planning with **maybe outcomes** |

### The Three Big Bridges

```
Unit III                          Unit IV
─────────────────────────────────────────────
Deterministic       →    Uncertain Environments
Passive Inference   →    Active Learning
Classical Planning  →    Probabilistic Decisions
```

> 💡 **Mind-Friendly:** Unit III = Playing chess where you can see all pieces. Unit IV = Playing battleship where you guess!

---

## 2. 🔄 From Reactive to Reasoning Agents

### What came before? (Plain English Version)

Think about how a **thermostat** works at home:
- Temperature drops below 20°C → Turn on heater
- Temperature rises above 25°C → Turn off heater

That's a **reactive agent** — it follows simple rules based on what it directly senses. No thinking involved!

But what if you're a **detective** investigating a crime? You can't just react — you need to:
- Remember clues from different locations
- Combine evidence gathered at different times  
- Figure out things you can't directly see

That's a **reasoning agent** — and that's what this chapter teaches!

Earlier in the course, we learned about agents that:
- **Search** through possible states (like BFS, DFS, A*)
- **React** to what they see directly
- Work great when you can **see everything** (fully observable)

### The Problem

What if the agent **CAN'T** see everything? 🤔

```
Reactive Agent: "I see fire → I run"          ✅ Simple, but limited
Reasoning Agent: "I smell smoke → fire nearby  ✅ Smart! Can handle
                  → which direction? → run      hidden dangers
                  AWAY from the smoke"
```

### The Doctor Analogy 🏥

| Reactive Agent | Reasoning Agent |
|---|---|
| Patient: "I have a rash" | Patient: "I have a rash" |
| Agent: "Here's cream" | Agent: "Rash + fever + recent travel = could be measles → let me check further" |
| Just reacts to what it sees | Uses **stored knowledge** to reason about what it **can't** see |

### Key Insight

**Intelligent behavior = Stored Knowledge + Reasoning (Inference)**

```
    ┌─────────────┐
    │  Knowledge   │──→ What the agent KNOWS
    │    Base      │    (facts, rules, observations)
    └──────┬──────┘
           │
           ▼
    ┌─────────────┐
    │  Inference   │──→ What the agent FIGURES OUT
    │   Engine     │    (new conclusions from old facts)
    └──────┬──────┘
           │
           ▼
    ┌─────────────┐
    │  Smart       │──→ What the agent DOES
    │  Action!     │
    └─────────────┘
```

> 💡 **Mind-Friendly:** A reactive agent is like a dog that runs when it hears thunder. A reasoning agent is like a detective who puts clues together to find the answer!

---

## 3. 🤔 Why Study Logic?

### The Simple Recipe

```
╔═══════════════════════════════════════════════════╗
║   Knowledge  +  Reasoning  =  Intelligence        ║
║   (what you know)  (how you think)  (smart action) ║
╚═══════════════════════════════════════════════════╝
```

### What does an intelligent agent need to do?

1. **Represent** what it knows → "There's a pit at [3,1]"
2. **Reason** about what it doesn't see → "I feel a breeze, so a pit is nearby"
3. **Derive correct conclusions** → "It's safe to move to [2,2]"
4. **Act** based on those conclusions → *moves to [2,2]*

### Why Logic specifically?

Logic gives us THREE superpowers:

| Superpower | What it does | Example |
|---|---|---|
| 🔤 **Syntax** | The language to write knowledge | `Pit(1,2) ∨ Pit(2,1)` |
| 🎯 **Semantics** | Rules for what's TRUE or FALSE | "This sentence is true when..." |
| ⚙️ **Inference** | Methods to derive NEW truths | "Since A is true and A→B, then B is true" |

### The Agent Intelligence Pipeline

```
Perception → Learning → Knowledge Representation → Reasoning → Planning → Execution
    │            │              │                       │           │          │
  See/hear    Update KB      Store facts             Think!      Decide     Do it!
```

> 💡 **Mind-Friendly:** Logic is like the grammar rules for a "language of thinking." Just like English has rules for making correct sentences, logic has rules for making correct conclusions!

---

## 4. 🏗️ Knowledge-Based Agents (KBA)

### The Heart of a KBA: The Knowledge Base (KB)

A **Knowledge Base** is simply a **collection of sentences** (facts and rules) about the world.

> ⚠️ "Sentence" here is a TECHNICAL term — not like English sentences. It's a formal statement in a logic language.

### Architecture Diagram

```
    ┌──────────────────────────────────────────────┐
    │          KNOWLEDGE-BASED AGENT                │
    │                                               │
    │  ┌──────────┐     ┌──────────────────┐       │
    │  │Environment│────▶│  Inference Engine │       │
    │  │  (Input)  │     │                  │──▶ Output
    │  └──────────┘     └────────┬─────────┘       │
    │                            │    ▲              │
    │                            ▼    │              │
    │                   ┌────────────────┐          │
    │                   │ Knowledge Base  │          │
    │                   │ (Facts & Rules) │          │
    │                   └────────────────┘          │
    │                            ▲                   │
    │                            │                   │
    │                   ┌────────────────┐          │
    │                   │   Learning     │          │
    │                   │ (Updating KB)  │          │
    │                   └────────────────┘          │
    └──────────────────────────────────────────────┘
```

### Two Operations on a KB

| Operation | What it does | Analogy |
|---|---|---|
| **TELL** | Add new sentences to the KB | 📝 Writing a new fact in your notebook |
| **ASK** | Query the KB for information | 🔍 Looking up something in your notebook |

Both TELL and ASK can involve **inference** — figuring out NEW facts from OLD facts.

### The Golden Rule of Inference

> When you ASK the KB a question, the answer MUST follow logically from what was TELLed before. **No making stuff up!**

### Real-World Example: MYCIN (Stanford, 1970s)

MYCIN was one of the first expert systems — a knowledge-based agent for diagnosing bacterial infections.

```
KB Rules (TELL):
  Rule 1: IF gram-positive bacteria AND rod-shaped → suggest Antibiotic-X
  Rule 2: IF gram-negative bacteria AND cocci-shaped → suggest Antibiotic-Y

Patient Data (TELL):
  Fact: bacteria is gram-positive
  Fact: bacteria is rod-shaped

Query (ASK):
  "What antibiotic should we use?"

Inference:
  Rule 1 matches! → Answer: Antibiotic-X ✅
```

> 💡 **Mind-Friendly:** A KB is like your brain's "fact notebook." TELL = writing a new fact. ASK = asking your brain a question. Inference = your brain connecting the dots!

---

## 5. 📋 Declarative vs Procedural Approach

### Two Ways to Build a Knowledge Base

| Feature | Declarative Approach | Procedural Approach |
|---|---|---|
| **What it stores** | Facts & Rules (WHAT is true) | Procedures (HOW to do it) |
| **Building method** | TELL sentences one by one | Write step-by-step code |
| **Flexibility** | Easy to add/change knowledge | Hard to modify |
| **Example System** | MYCIN (if-then rules) | Algorithm-based diagnosis |
| **Analogy** | 📖 A recipe book with ingredients & rules | 👨‍🍳 A chef who "just knows" the steps |

### Declarative Example (MYCIN Style)

```
KB:
  IF fever AND rash → measles
  IF measles → isolate_patient

TELL: "Patient has fever"
TELL: "Patient has rash"
ASK: "What should we do?"
→ Inference: fever + rash → measles → isolate_patient ✅
```

### Procedural Example (Algorithm Style)

```python
def diagnose(patient):
    if patient.temperature > 38:        # Step 1: Check temperature
        if patient.has_rash:            # Step 2: Check rash
            if patient.rash_duration > 3: # Step 3: Check duration
                return "measles"        # Step 4: Output
    return "unknown"
```

### Key Insight

> 🔑 **Best agents combine BOTH approaches!** Declarative knowledge can be compiled into efficient procedural code.

> 💡 **Mind-Friendly:** Declarative = a recipe card that says "flour + sugar + heat = cake." Procedural = step-by-step instructions "First put flour in bowl, then add sugar, then put in oven at 350°F."

---

## 6. 🐉 The Wumpus World

### Why Do We Need a "World"? 🤔
To understand how logical agents work, we need a **practice environment** — like how driving students use a parking lot before going on real roads. The Wumpus World is our "parking lot" — simple enough to understand, but complex enough to need real reasoning!

### What is it?

The Wumpus World is a **toy environment** (like a video game) designed to teach how knowledge-based agents think.

### The Setup

```
    ┌─────┬─────┬─────┬─────┐
  4 │Stench│Breez│     │ PIT │
    │      │     │     │     │
    ├─────┼─────┼─────┼─────┤
  3 │Wumps│Stenc│ PIT │Breez│
    │ 👻  │Gold │     │     │
    │     │ 💰  │     │     │
    ├─────┼─────┼─────┼─────┤
  2 │Stench│     │Breez│     │
    │      │     │     │     │
    ├─────┼─────┼─────┼─────┤
  1 │Agent│Breez│     │ PIT │
    │ 🧑  │     │Breez│     │
    └─────┴─────┴─────┴─────┘
      1     2     3     4
```

### The Story

- 🧑 **Agent** starts at [1,1], facing right
- 👻 **Wumpus** lurks in a room — it eats you if you enter!
- 🕳️ **Pits** are bottomless traps (Wumpus is too big to fall in)
- 💰 **Gold** is hidden somewhere — grab it and escape!
- 🏹 **Arrow** — you have ONE arrow to shoot the Wumpus

### Environment Properties

| Property | Value | Why it matters |
|---|---|---|
| Discrete | Yes, 4×4 grid | Finite number of states |
| Static | Yes, Wumpus doesn't move | Environment doesn't change while agent thinks |
| Single-agent | Yes | Only one player |
| Sequential | Yes | Rewards come after many actions |
| Partially observable | **YES** | Agent can't see everything — must REASON! |

> 💡 **Mind-Friendly:** Imagine you're blindfolded in a cave. You can smell bad things (stench = monster nearby), feel wind (breeze = hole nearby), and see sparkles (glitter = gold!). You have to figure out what's where WITHOUT seeing it!

---

## 7. 📊 PEAS Description

### Performance Measure (Score = Your Motivation!)

| Event | Points |
|---|---|
| 🏆 Climb out with gold | **+1000** |
| 💀 Fall in pit or eaten | **−1000** |
| 🚶 Each action taken | **−1** |
| 🏹 Using the arrow | **−10** |

> Game ends when: Agent dies OR Agent climbs out at [1,1]

### Environment

- 4×4 grid of rooms
- Agent starts at **[1,1]**, facing **right**
- Gold and Wumpus placed **randomly** (not at [1,1])
- Each non-start square: **20% chance** of being a pit

### Actuators (What the agent can DO)

| Action | Description |
|---|---|
| **Forward** | Move one square in the facing direction |
| **TurnLeft** | Rotate 90° left |
| **TurnRight** | Rotate 90° right |
| **Grab** | Pick up gold (if in same square) |
| **Shoot** | Fire arrow in facing direction (only 1 arrow!) |
| **Climb** | Climb out of cave (only works at [1,1]) |

### Sensors (What the agent can PERCEIVE)

| Sensor | Trigger | Range |
|---|---|---|
| **Stench** 🦨 | Wumpus in current or adjacent square | Direct + adjacent (not diagonal) |
| **Breeze** 💨 | Pit in adjacent square | Adjacent only |
| **Glitter** ✨ | Gold in current square | Current square only |
| **Bump** 🧱 | Walked into a wall | Current action |
| **Scream** 😱 | Wumpus killed | Anywhere in cave |

Percept format: `[Stench, Breeze, Glitter, Bump, Scream]`

Example: `[Stench, Breeze, None, None, None]` = "I smell something AND feel wind, but no sparkles, no wall-bump, no scream"

### Performance Measure vs Reinforcement Learning

| Planning Agent (This chapter) | RL Agent (Unit IV) |
|---|---|
| **Knows** the rules | **Doesn't know** the rules |
| **Knows** reward values | Discovers rewards by trying |
| Computes best action | Learns by trial & error |
| "Given rules, what's optimal?" | "What pattern of moves avoids death?" |
| Score = evaluation metric | Reward = training signal |

> 💡 **Mind-Friendly:** Percepts are like your 5 senses in the cave. Stench = "I smell the monster!" Breeze = "I feel wind from a hole!" Glitter = "Ooh, shiny gold!"

---

## 8. 🚶 Agent Walkthrough in Wumpus World

### Step-by-Step: How the Agent Explores

#### Step 1: Starting at [1,1]

```
Percept: [None, None, None, None, None]
Meaning: No stench, no breeze, no glitter, no bump, no scream

Agent thinks:
  "No stench → no Wumpus in [1,2] or [2,1]"
  "No breeze → no pit in [1,2] or [2,1]"
  "Both neighbors are SAFE (OK)!"

    ┌─────┬─────┬─────┬─────┐
  4 │     │     │     │     │
    ├─────┼─────┼─────┼─────┤
  3 │     │     │     │     │
    ├─────┼─────┼─────┼─────┤
  2 │ OK  │     │     │     │   Legend:
    ├─────┼─────┼─────┼─────┤   A = Agent
  1 │A,OK │ OK  │     │     │   OK = Safe
    └─────┴─────┴─────┴─────┘   B = Breeze
      1     2     3     4       P? = Maybe pit
```

#### Step 2: Move to [2,1]

```
Percept: [None, Breeze, None, None, None]
Meaning: No stench, YES breeze, nothing else

Agent thinks:
  "Breeze at [2,1] → pit in a neighbor"
  "Pit can't be at [1,1] (rules say no pit at start)"
  "So pit is in [2,2] OR [3,1] OR both"
  "I should go back to safety!"

    ┌─────┬─────┬─────┬─────┐
  4 │     │     │     │     │
    ├─────┼─────┼─────┼─────┤
  3 │     │     │     │     │
    ├─────┼─────┼─────┼─────┤
  2 │ OK  │ P?  │     │     │
    ├─────┼─────┼─────┼─────┤
  1 │V,OK │A,B  │ P?  │     │
    └─────┴V,OK─┴─────┴─────┘
      1     2     3     4
```

#### Step 3: Go back to [1,1], then move to [1,2]

```
Percept at [1,2]: [Stench, None, None, None, None]
Meaning: YES stench, no breeze, nothing else

Agent thinks (this is the HARD part!):
  "Stench at [1,2] → Wumpus is nearby"
  "Wumpus can't be at [1,1] (rules)"
  "Wumpus can't be at [2,2] (no stench at [2,1]!)"
  "Therefore: Wumpus MUST be at [1,3]!" ← W!

  "No breeze at [1,2] → no pit at [2,2]"
  "But earlier: pit at [2,2] OR [3,1]"
  "If no pit at [2,2] → pit MUST be at [3,1]!" ← P!

  "So [2,2] has NO pit and NO wumpus → it's SAFE!"

    ┌─────┬─────┬─────┬─────┐
  4 │     │     │     │     │
    ├─────┼─────┼─────┼─────┤
  3 │ W!  │     │     │     │
    ├─────┼─────┼─────┼─────┤
  2 │A,S  │     │     │     │
    │OK   │ OK  │     │     │
    ├─────┼─────┼─────┼─────┤
  1 │V,OK │V,B  │ P!  │     │
    └─────┴OK───┴─────┴─────┘
      1     2     3     4
```

#### Step 4: Move through [2,2] to [2,3]

```
Percept at [2,3]: [Stench, Breeze, Glitter, None, None]
Meaning: Stench + Breeze + GLITTER!

Agent thinks:
  "GLITTER! → Gold is HERE!"
  "GRAB the gold, then go home!"

Action sequence: Grab → navigate back to [1,1] → Climb
Score: +1000 - (actions × 1) = big win! 🎉
```

### The KEY Insight from this Walkthrough

> 🔑 **The inference at Step 3 is remarkable because it:**
> - Combines knowledge from **different times** (breeze at [2,1] earlier + stench at [1,2] now)
> - Combines knowledge from **different places** ([2,1] info + [1,2] info)
> - Uses the **absence** of a percept (no stench at [2,1]) as a crucial clue
>
> **This is what makes logical reasoning powerful — and what reactive agents CAN'T do!**

---

## 9. 🦴 Logic — The Skeleton

### Wait, What Even IS Logic? (The Simplest Possible Explanation)

Logic is just a **system for being precise about what's true**. In everyday life, we're often vague:
- "It might rain" — How likely? When?
- "That food is kinda spicy" — How spicy exactly?

Logic forces us to be **exact**: something is either TRUE or FALSE. No "maybe." No "kinda."

Why does this matter for AI? Because computers can't handle vagueness! They need clear, precise rules to work with. Logic gives us those rules.

### The Four Core Concepts

Logic has 4 fundamental concepts that apply to ALL types of logic (propositional, first-order, fuzzy, etc.):

```
    ┌──────────────────────────────────────┐
    │          THE LOGIC SKELETON           │
    │                                       │
    │  1. SYNTAX ──── How sentences look    │
    │  2. SEMANTICS ─ What sentences mean   │
    │  3. MODELS ──── Possible worlds       │
    │  4. ENTAILMENT─ What follows from what│
    └──────────────────────────────────────┘
```

### 1️⃣ Syntax — What Sentences LOOK Like

Syntax = the grammar rules for building valid sentences.

```
✅ Valid (well-formed):    x + y = 4
❌ Invalid:               x4y+ =

Syntax cares about FORM, not MEANING.
```

### 2️⃣ Semantics — What Sentences MEAN

Semantics = rules for determining if a sentence is **TRUE or FALSE** in a given world.

```
Sentence: x + y = 4

Model 1: {x=2, y=2} → TRUE  ✅
Model 2: {x=1, y=1} → FALSE ❌

In standard logic: every sentence is either true or false.
No middle ground!
```

### 3️⃣ Models — Possible Worlds

A **model** = a complete description of one possible state of the world.

```
We write M(α) to mean:
  "The set of ALL models where sentence α is TRUE"

Example:
  α = "x + y = 4"
  M(α) = {(0,4), (1,3), (2,2), (3,1), (4,0), ...}
         All the worlds where x + y = 4 is true
```

### 4️⃣ Entailment — What Logically Follows

**Entailment** (written α ⊨ β) means: "In EVERY model where α is true, β is ALSO true."

```
α ⊨ β   means   M(α) ⊆ M(β)

English: "β follows from α"
         "If α is true, β MUST be true"
         "α is STRONGER than β" (rules out more worlds)

Example:
  α = "x = 0"
  β = "xy = 0"
  α ⊨ β ✅  (in every world where x=0, xy=0 is also true)
```

### The Haystack Analogy 🌾

```
All consequences of KB = the HAYSTACK
The sentence α you're looking for = the NEEDLE

Entailment = the needle IS in the haystack (it exists)
Inference  = FINDING the needle (the algorithm that proves it)
```

> 💡 **Mind-Friendly:**
> - **Syntax** = How to spell words correctly
> - **Semantics** = What the words mean
> - **Models** = All the "what if" scenarios
> - **Entailment** = "If THIS is true, then THAT must also be true" — like "If it's a dog, it must be an animal"

---

## 10. 🔍 Entailment in the Wumpus World

### The Scenario

After moving to [2,1], the agent knows:
- Nothing detected in [1,1] → no pit in [1,2] or [2,1]
- Breeze in [2,1] → pit somewhere nearby

**Question:** Is there a pit in [1,2]? In [2,2]?

### The Model Checking Approach

The agent considers all adjacent squares: [1,2], [2,2], [3,1]. Each can have a pit or not → 2³ = **8 possible models**.

```
Model | P(1,2) | P(2,2) | P(3,1) | KB true?
──────┼────────┼────────┼────────┼─────────
  1   │  F     │  F     │  F     │   ❌ (breeze at [2,1] requires a pit nearby)
  2   │  F     │  F     │  T     │   ✅
  3   │  F     │  T     │  F     │   ✅
  4   │  F     │  T     │  T     │   ✅
  5   │  T     │  F     │  F     │   ❌ (pit at [1,2] would cause breeze at [1,1])
  6   │  T     │  F     │  T     │   ❌
  7   │  T     │  T     │  F     │   ❌
  8   │  T     │  T     │  T     │   ❌
```

**Only models 2, 3, 4 are consistent with the KB** (solid line in textbook figure).

### Checking α₁ = "No pit in [1,2]"

```
Model 2: P(1,2) = F → ¬P(1,2) is TRUE  ✅
Model 3: P(1,2) = F → ¬P(1,2) is TRUE  ✅
Model 4: P(1,2) = F → ¬P(1,2) is TRUE  ✅

In ALL models where KB is true, ¬P(1,2) is true.
M(KB) ⊆ M(¬P(1,2))
∴ KB ⊨ ¬P(1,2) ✅  → "There is NO pit in [1,2]"
```

### Checking α₂ = "No pit in [2,2]"

```
Model 2: P(2,2) = F → ¬P(2,2) is TRUE  ✅
Model 3: P(2,2) = T → ¬P(2,2) is FALSE ❌
Model 4: P(2,2) = T → ¬P(2,2) is FALSE ❌

NOT all models where KB is true have ¬P(2,2) true.
M(KB) ⊄ M(¬P(2,2))
∴ KB ⊭ ¬P(2,2) ❌  → "Can't conclude there's no pit in [2,2]"
(Also can't conclude there IS a pit — we just don't know yet!)
```

> 💡 **Mind-Friendly:** The agent makes a list of all possible worlds. Then crosses out the ones that don't match what it knows. If ALL remaining worlds agree on something, it's definitely true!

---

## 11. ✅ Inference: Soundness & Completeness

### Why Should I Care? 🤔
Imagine a medical AI that diagnoses diseases. Would you want it to:
- Tell you that you have a disease you DON'T have? (That's **unsound** — scary!)
- Miss a disease you DO have? (That's **incomplete** — dangerous!)

Soundness and completeness tell us how much we can **trust** an AI's conclusions. This is critical for real-world AI safety!

### What is Inference?

**Inference** = the process of deriving new sentences that are **entailed** by the KB.

We write: `KB ⊢ᵢ α` meaning "algorithm i derives α from KB"

### Two Critical Properties

| Property | Definition | Analogy |
|---|---|---|
| **Sound** 🔊 | Only derives TRUE conclusions | A judge who NEVER convicts an innocent person |
| **Complete** 📦 | Can derive EVERY true conclusion | A detective who ALWAYS finds the guilty person |

### Sound but Incomplete

```
Example: Algorithm processes each breeze separately, never combines them.

KB knows:
  From Breeze at [2,1]: Pit(2,2) OR Pit(3,1)
  From Breeze at [1,2]: Pit(2,2) OR Pit(1,3)

A complete algorithm would combine these:
  The common element is Pit(2,2) → therefore Pit(2,2) must be true!

But our incomplete algorithm just keeps the disjunctions separate.
It never deduces Pit(2,2).

It's still SOUND (never says anything wrong),
but INCOMPLETE (misses a true conclusion).
```

### Unsound Inference

```
Example: Algorithm jumps to conclusions.

KB: Breeze(1,1) is true
Algorithm concludes: Pit(1,2)    ← WRONG!

The correct conclusion is: Pit(1,2) OR Pit(2,1)
Converting a disjunction into a specific fact is UNSOUND.

KB ⊭ Pit(1,2), but the algorithm says Pit(1,2).
That's an error — it "convicted an innocent square."
```

### The Ideal

We want algorithms that are **BOTH sound AND complete**.

> **Model checking** is both sound and complete (but can be slow: O(2ⁿ) time).

### Grounding: Connecting Logic to the Real World

```
                  REPRESENTATION
    ┌─────────────────────────────────────────┐
    │  Sentences ──Entails──▶ Sentence        │
    │      ▲                      │           │
    │  Semantics              Semantics        │
    │      │                      ▼           │
    │  Aspects of ──Follows──▶ Aspect of      │
    │  real world              real world      │
    └─────────────────────────────────────────┘
                   REAL WORLD

Key idea: If the KB is true in the real world,
then ANY sentence derived by sound inference
is ALSO true in the real world!
```

> 💡 **Mind-Friendly:** **Sound** = "I never lie." **Complete** = "I always find the truth." Best agent = does both!

---

## 12. ⛓️ Forward & Backward Chaining

### Forward Chaining (Data-Driven) ▶️

**Start from what you KNOW, derive everything you CAN.**

> 🍳 **Cooking Analogy:** You open your fridge and see eggs, flour, sugar, and butter. You check your recipe book: "eggs + flour + sugar = cake", "eggs + butter = omelette." So you know you CAN make cake AND omelette. That's forward chaining — start from ingredients (facts), see what recipes (rules) you can complete!

```
Algorithm:
  1. Begin with known facts in KB
  2. Find rules whose IF-part matches known facts
  3. Fire those rules → add conclusions to KB
  4. Repeat until no new facts can be added

Example:
  Rules:                          Facts:
    IF fever AND rash → measles     fever ✓
    IF measles → isolate            rash ✓

  Step 1: fever + rash matches Rule 1 → add "measles"
  Step 2: measles matches Rule 2 → add "isolate"
  Step 3: No more rules fire → DONE!

  Result: {fever, rash, measles, isolate}
```

**When to use:** Monitoring systems, rule engines, when you want ALL possible conclusions.

### Backward Chaining (Goal-Driven) ◀️

**Start from what you WANT TO PROVE, work backwards.**

> 🍰 **Cooking Analogy:** You want to make cake. You check: "What do I need for cake? Eggs + flour + sugar." Do I have eggs? Check fridge — YES. Flour? YES. Sugar? YES. Great, I can make cake! That's backward chaining — start from the goal, check what's needed!

```
Algorithm:
  1. Start with a goal (query)
  2. Find rules that conclude the goal
  3. Check if premises of those rules are true
  4. If not known, recursively try to prove them

Example:
  Goal: measles?

  Step 1: Which rule concludes "measles"?
          → Rule: IF fever AND rash → measles
  Step 2: Is "fever" true? → Check KB → YES ✅
  Step 3: Is "rash" true? → Check KB → YES ✅
  Step 4: Both premises true → measles PROVEN! ✅
```

**When to use:** Diagnostic systems (like MYCIN), when you have a specific question.

### Comparison

```
Forward Chaining:           Backward Chaining:
  facts → → → → goal         goal ← ← ← ← facts

  "What can I conclude?"     "Can I prove this?"
  Explores everything         Focused on one question
  May derive irrelevant       Only explores relevant
  facts                       paths
```

> 💡 **Mind-Friendly:** **Forward chaining** = "I have ingredients, let me cook everything I can!" **Backward chaining** = "I want cake — do I have flour? Sugar? Eggs? Yes? Then I can make cake!"

---

## 13. 🧬 Types of Logic

### The Logic Family

```
                    LOGIC
                      │
    ┌─────────┬───────┼───────┬──────────┐
    │         │       │       │          │
Propositional  FOL  Fuzzy  Probabilistic  Non-monotonic
 (Mr. Pro)  (Ms.FOL)(Mr.Fuz)
```

| Type | What it handles | Key Feature | Example |
|---|---|---|---|
| **Propositional** | True/False facts | Simple, efficient | "It is raining" (T/F) |
| **First-Order (FOL)** | Objects + relationships | Very expressive | "∀x: Dog(x) → Animal(x)" |
| **Description** | Structured knowledge | Decidable subset of FOL | Ontologies, OWL |
| **Non-monotonic** | Changing conclusions | Can retract conclusions | "Birds fly... except penguins" |
| **Probabilistic** | Uncertain knowledge | Logic + probability | Markov Logic Networks |
| **Fuzzy** | Degrees of truth | Not just T/F | "Temperature is 0.7 hot" |

### Focus of This Chapter: Propositional Logic

Propositional logic is the **simplest** formal logic. It's the foundation for understanding all the others.

> 💡 **Mind-Friendly:** Types of logic are like types of languages. Propositional logic is like baby talk — simple but limited. FOL is like adult English — can say complex things. Fuzzy logic is like saying "kinda" — things can be partly true!

---

## 14. 🔤 Propositional Logic — Syntax

### What is Propositional Logic in Plain English?

Propositional logic is the **simplest type of logic**. It deals with statements that are either TRUE or FALSE — nothing in between.

**Everyday examples of propositions:**
```
"It is raining"          → TRUE or FALSE
"I am hungry"            → TRUE or FALSE  
"2 + 2 = 5"              → always FALSE
"The sky is blue"        → TRUE (usually!)
"If it rains, I'll bring an umbrella" → a rule connecting two propositions
```

**NOT propositions** (these can't be true or false):
```
"What time is it?"       → A question, not a statement
"Close the door!"        → A command, not a statement
"Wow!"                   → An exclamation, not a statement
```

Now let's learn how to write propositions formally...

### Atomic Sentences (The Simplest Building Blocks)

An atomic sentence = a single proposition symbol. Think of it as **one single fact**.

```
Examples: P, Q, R, W₁₃, North, Pit₂₂

Special constants:
  True  → always true in every model
  False → always false in every model
```

### Complex Sentences (Combining with Connectives)

| Connective | Symbol | Name | Example | Meaning |
|---|---|---|---|---|
| NOT | ¬ | Negation | ¬W₁₃ | "There is NO wumpus at [1,3]" |
| AND | ∧ | Conjunction | W₁₃ ∧ P₃₁ | "Wumpus at [1,3] AND pit at [3,1]" |
| OR | ∨ | Disjunction | P₁₂ ∨ P₂₁ | "Pit at [1,2] OR pit at [2,1] (or both)" |
| IMPLIES | ⇒ | Implication | P ⇒ Q | "IF P THEN Q" |
| IFF | ⇔ | Biconditional | P ⇔ Q | "P IF AND ONLY IF Q" |

### Terminology

| Term | Definition | Example |
|---|---|---|
| **Literal** | An atomic sentence or its negation | P (positive literal), ¬P (negative literal) |
| **Conjunction** | AND sentence | A ∧ B ∧ C |
| **Conjuncts** | Parts of a conjunction | A, B, C are conjuncts |
| **Disjunction** | OR sentence | A ∨ B ∨ C |
| **Disjuncts** | Parts of a disjunction | A, B, C are disjuncts |
| **Implication** | IF-THEN sentence | P ⇒ Q |
| **Premise/Antecedent** | The IF part | P in P ⇒ Q |
| **Conclusion/Consequent** | The THEN part | Q in P ⇒ Q |

### Operator Precedence (Like BODMAS!)

```
Highest priority → Lowest priority:

  ¬  >  ∧  >  ∨  >  ⇒  >  ⇔

Example: ¬A ∧ B means (¬A) ∧ B, NOT ¬(A ∧ B)
         Just like: -2 + 4 = 2, NOT -(2+4) = -6

When in doubt → USE PARENTHESES!
```

### Formal Grammar

```
Sentence         → AtomicSentence | ComplexSentence
AtomicSentence   → True | False | P | Q | R | ...
ComplexSentence  → (Sentence) | [Sentence]
                  | ¬ Sentence
                  | Sentence ∧ Sentence
                  | Sentence ∨ Sentence
                  | Sentence ⇒ Sentence
                  | Sentence ⇔ Sentence
```

> 💡 **Mind-Friendly:** Propositions are like LEGO blocks (P, Q, R). Connectives (AND, OR, NOT, IF-THEN) are how you snap them together to build bigger ideas!

---

## 15. 🎯 Propositional Logic — Semantics

### What is a Model?

In propositional logic, a **model** = an assignment of TRUE or FALSE to **every** proposition symbol.

```
If we have symbols P₁₂, P₂₂, P₃₁:

Model m₁ = {P₁₂ = false, P₂₂ = false, P₃₁ = true}

With 3 symbols → 2³ = 8 possible models
With n symbols → 2ⁿ possible models
```

### Truth Rules for Atomic Sentences

```
• True is true in EVERY model
• False is false in EVERY model
• Any other symbol: look up its value in the model
  Example: In m₁, P₁₂ = false
```

### Truth Rules for Complex Sentences

For any sentences P, Q in any model m:

| Connective | Rule | Plain English |
|---|---|---|
| ¬P | True iff P is false | Flips the truth value |
| P ∧ Q | True iff BOTH are true | Both must be true |
| P ∨ Q | True iff EITHER is true (or both) | At least one must be true |
| P ⇒ Q | True UNLESS P is true and Q is false | "If P happens, Q must happen" |
| P ⇔ Q | True iff both same (both T or both F) | "P and Q always match" |

### The Complete Truth Table

```
  P     Q   │ ¬P  │ P∧Q │ P∨Q │ P⇒Q │ P⇔Q
────────────┼─────┼─────┼─────┼─────┼─────
 false false│ true│false│false│ true│ true
 false true │ true│false│ true│ true│false
 true  false│false│false│ true│false│false
 true  true │false│ true│ true│ true│ true
```

### Understanding Implication (P ⇒ Q) — The Tricky One! 🎯

> ⚠️ **This is the #1 most confusing concept for beginners.** Read this section slowly!

**The common mistake:** People think P ⇒ Q means "P causes Q." It does NOT. It just means "whenever P is true, Q is also true." There's no cause-and-effect needed!

Think of P ⇒ Q as a **promise**:

> "If it rains (P), I will carry an umbrella (Q)."

| Situation | P (Rain?) | Q (Umbrella?) | P ⇒ Q | Why? |
|---|---|---|---|---|
| Rain + Umbrella | T | T | **TRUE** ✅ | Promise kept! |
| Rain + No Umbrella | T | F | **FALSE** ❌ | Promise broken! |
| No Rain + Umbrella | F | T | **TRUE** ✅ | Promise not tested, so not broken |
| No Rain + No Umbrella | F | F | **TRUE** ✅ | Promise not tested, so not broken |

> 🔑 **Key:** P ⇒ Q is only FALSE when P is true but Q is false. "I only lied if I said I would and then didn't."

### Understanding Biconditional (P ⇔ Q)

```
P ⇔ Q  =  (P ⇒ Q) AND (Q ⇒ P)

"If it rains, I carry umbrella" AND "If I carry umbrella, it's raining"
= "I carry an umbrella IF AND ONLY IF it rains"
= They always match! Both true or both false.
```

### Computing Truth Values — Example

```
Sentence: ¬P₁₂ ∧ (P₂₂ ∨ P₃₁)
Model m₁: {P₁₂=false, P₂₂=false, P₃₁=true}

Step 1: ¬P₁₂ = ¬false = true
Step 2: P₂₂ ∨ P₃₁ = false ∨ true = true
Step 3: true ∧ true = true ✅
```

> 💡 **Mind-Friendly:** A model is like a "what-if" story. "What if P is true and Q is false?" Then we check what the whole sentence equals. Like filling in numbers in a math equation to see if it works!

---

## 16. 📝 Building a Wumpus World KB

### Symbols We Need

For each square [x,y]:
- `Pxy` = "There is a pit at [x,y]"
- `Wxy` = "There is a wumpus at [x,y]"
- `Bxy` = "Agent perceives breeze at [x,y]"
- `Sxy` = "Agent perceives stench at [x,y]"

### The KB Sentences (Rules R₁–R₅)

```
R₁: ¬P₁₁                           "No pit at [1,1]" (game rule)

R₂: B₁₁ ⇔ (P₁₂ ∨ P₂₁)            "Breeze at [1,1] iff pit in
                                      [1,2] or [2,1]"

R₃: B₂₁ ⇔ (P₁₁ ∨ P₂₂ ∨ P₃₁)     "Breeze at [2,1] iff pit in
                                      [1,1] or [2,2] or [3,1]"

R₄: ¬B₁₁                           "No breeze perceived at [1,1]"
                                      (agent's observation)

R₅: B₂₁                            "Breeze perceived at [2,1]"
                                      (agent's observation)
```

### Why Biconditional (⇔) for Breeze Rules?

```
B₁₁ ⇔ (P₁₂ ∨ P₂₁)

This means BOTH:
  B₁₁ ⇒ (P₁₂ ∨ P₂₁)  "If breeze, then pit nearby"
  (P₁₂ ∨ P₂₁) ⇒ B₁₁  "If pit nearby, then breeze"

Using just ⇒ would be incomplete!
A square is breezy IF AND ONLY IF a neighbor has a pit.
```

> 💡 **Mind-Friendly:** The KB is like a rulebook + diary. The rules say "breeze means pit nearby." The diary says "I felt breeze at [2,1] but not at [1,1]." Combine them to figure out where the pits are!

---

## 17. 🖥️ Model Checking Inference

### Plain English First!
Model checking is the **brute force** approach to checking if something is true. It works like this:

1. **List every possible situation** (every combination of true/false for all facts)
2. **Cross out** situations that contradict what you already know
3. **Check** if your question is true in ALL remaining situations
4. If YES in all → it's guaranteed true! If NO in some → you can't be sure.

It's like a detective saying: "Let me consider every possible suspect. Now let me eliminate ones with alibis. If only one person is left... they did it!"

### The Algorithm (Pseudocode)

```
function TT-ENTAILS?(KB, α):
    symbols ← list of all proposition symbols in KB and α
    return TT-CHECK-ALL(KB, α, symbols, {})

function TT-CHECK-ALL(KB, α, symbols, model):
    if symbols is empty then
        if KB is TRUE in model then
            return α is TRUE in model    // check entailment
        else
            return true                  // KB false → vacuously true
    else
        P ← first symbol in symbols
        rest ← remaining symbols
        return TT-CHECK-ALL(KB, α, rest, model ∪ {P=true})
           AND TT-CHECK-ALL(KB, α, rest, model ∪ {P=false})
```

### Applied to Wumpus World

```
Symbols: B₁₁, B₂₁, P₁₁, P₁₂, P₂₁, P₂₂, P₃₁ → 7 symbols → 2⁷ = 128 models

Out of 128 models, only 3 make the KB (R₁ through R₅) true.

In all 3 models: P₁₂ = false → KB ⊨ ¬P₁₂ ✅ (no pit at [1,2])
In 2 of 3 models: P₂₂ = true → KB ⊭ ¬P₂₂ ❌ (can't conclude no pit at [2,2])
```

### Complexity

| Measure | Value |
|---|---|
| Time complexity | O(2ⁿ) where n = number of symbols |
| Space complexity | O(n) (depth-first enumeration) |
| Soundness | ✅ Yes (directly implements entailment definition) |
| Completeness | ✅ Yes (checks all models) |

> 💡 **Mind-Friendly:** Model checking is like trying EVERY possible combination of a lock. If all combinations that match your clues also match your guess, your guess must be right! It always works, but it's slow for big locks.

---

## 18. 🧩 Mnemonics & Memory Aids

### TELL-ASK-INFER (TAI)
```
T - TELL the KB new facts
A - ASK the KB questions
I - INFER new conclusions
"TAI knows things!" 🧠
```

### KB Agent Architecture: "EIK-L"
```
E - Environment (input)
I - Inference Engine (thinking)
K - Knowledge Base (memory)
L - Learning (updating)
```

### Logic Skeleton: "S-S-M-E"
```
S - Syntax (how it looks)
S - Semantics (what it means)
M - Models (possible worlds)
E - Entailment (what follows)
"Some Smart Minds Entail!" 🎓
```

### Connective Precedence: "Naughty Ants Often Irritate Insects"
```
¬ > ∧ > ∨ > ⇒ > ⇔
N   A   O   I   I
```

### Soundness vs Completeness
```
Sound    = "I'm SAFE — I never say wrong things"    (no false positives)
Complete = "I CATCH ALL — I find every truth"         (no false negatives)
```

### PEAS: "Please Eat All Sandwiches"
```
P - Performance, E - Environment, A - Actuators, S - Sensors
```

### Wumpus Percepts: "SBG-BS"
```
Stench, Breeze, Glitter, Bump, Scream
"Stinky Breezy Gold — Bumped & Screamed"
```

### Implication: "Only FALSE when T→F"
```
"A broken PROMISE: I said I would (T) but didn't (F)"
```

---

## 19. 📋 Cheatsheet

```
╔══════════════════════════════════════════════════════════════╗
║              LOGICAL AGENTS — CHEATSHEET                     ║
╠══════════════════════════════════════════════════════════════╣
║  CORE: Knowledge + Reasoning = Intelligence                  ║
║  KB OPS: TELL (add) | ASK (query) | INFER (derive)          ║
║  SKELETON: Syntax → Semantics → Models → Entailment          ║
║  ENTAILMENT: α ⊨ β  iff  M(α) ⊆ M(β)                      ║
║  INFERENCE: KB ⊢ᵢ α (algorithm i derives α)                 ║
║  SOUND = only true results | COMPLETE = finds all truths     ║
║  PRECEDENCE: ¬ > ∧ > ∨ > ⇒ > ⇔                            ║
║  P⇒Q FALSE only when P=T, Q=F                              ║
║  P⇔Q TRUE only when P,Q match                              ║
║  MODEL CHECK: O(2ⁿ) time, O(n) space, sound+complete        ║
║  FORWARD CHAIN: facts→rules→conclusions                      ║
║  BACKWARD CHAIN: goal→rules→check premises                   ║
║  WUMPUS: 4×4 grid, +1000 gold, -1000 death, -1/step        ║
║  PERCEPTS: Stench Breeze Glitter Bump Scream                ║
║  ACTIONS: Forward TurnL/R Grab Shoot Climb                   ║
╚══════════════════════════════════════════════════════════════╝
```

---

## 20. 🌐 Real-World Examples

| Domain | KB Contains | Inference Type | Action |
|---|---|---|---|
| **Medical (MYCIN)** | Disease rules, symptoms | Backward chaining | Recommend treatment |
| **Smart Home** | Automation rules, sensor data | Forward chaining | Control devices |
| **Game AI** | Game rules, enemy observations | Model checking | Strategic moves |
| **Fraud Detection** | Transaction rules, patterns | Forward chaining | Block suspicious txn |
| **Self-Driving Cars** | Traffic rules, sensor data | Hybrid inference | Brake, steer, yield |
| **Grammar Checkers** | Language rules, dictionary | Backward chaining | Suggest corrections |

---

## 21. ❓ Quick Revision Q&A

> 💡 **How to use:** Cover the "Answer" column with your hand, try answering, then check!

| # | Question | Answer | Think of it like... |
|---|---|---|---|
| 1 | Reactive vs Reasoning agent? | Reactive acts on percepts directly; Reasoning uses KB to infer hidden info | Thermostat vs Detective |
| 2 | Two KB operations? | TELL (add facts) and ASK (query) — both can involve inference | Writing in a diary vs Reading the diary |
| 3 | Why is Wumpus World partially observable? | Agent can't see other rooms — only gets indirect clues | Playing Minesweeper — you see numbers, not mines |
| 4 | What does KB ⊨ α mean? | In every model where KB is true, α is also true | "My notes GUARANTEE this answer" |
| 5 | Entailment vs Inference? | Entailment = truth exists; Inference = finding it | Needle exists in haystack vs Finding the needle |
| 6 | When is P ⇒ Q false? | Only when P=True and Q=False | A promise is broken only if you said you would AND didn't |
| 7 | Sound inference? | Never derives false conclusions | A judge who never convicts an innocent person |
| 8 | Complete inference? | Derives every entailed sentence | A detective who always catches the guilty person |
| 9 | Model checking complexity? | O(2ⁿ) time, O(n) space | Trying every combination of a lock — works but slow |
| 10 | Declarative vs Procedural? | Declarative = WHAT is true (rules); Procedural = HOW to do it (steps) | Recipe book vs Chef cooking from memory |

### 🎯 Top 5 Exam Tips
```
1. ALWAYS remember: P⇒Q is FALSE only when P=T, Q=F
2. Biconditional (⇔) means BOTH directions of implication
3. No breeze = no pit in ANY adjacent square (use ⇔ property)
4. Precedence order: ¬ ∧ ∨ ⇒ ⇔ (memorize the mnemonic!)
5. Model checking: 2ⁿ models for n symbols — draw the table!
```

---

> 📝 **Study Guide for AI Unit III** | 🔗 [Numerical Guide →](./logical_agents_numerical_guide.md) | 🎯 [Exam Guide →](./logical_agents_exam_guide.md) | 🗺️ [Mind Map →](./logical_agents_mindmap.png)
