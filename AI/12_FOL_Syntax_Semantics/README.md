# 🔬 Topic 12 — First-Order Logic: Syntax & Semantics

> **Difficulty**: 🔴 Hard | **Syllabus Section**: Knowledge & Reasoning
>
> **Slides**: RB-M & SD-M | **Quiz Relevance**: ⭐⭐⭐⭐⭐

---

## 🍼 The Big Story (ELI5)

### Propositional Logic Can't Talk About THINGS!

Propositional logic: "It is raining." TRUE or FALSE. Done.

But what about: "ALL dogs bark"? "John's FATHER is tall"? "SOMEONE loves Mary"?

Propositional logic can't express these because it has no concept of **objects** (dogs, John, Mary), **properties** (tall, barking), **relationships** (loves, father-of), or **quantities** (all, some).

**First-Order Logic (FOL)** adds all of these!

> 🍼 **Kid Version**: 
> - Propositional logic = "This light is on." (just one specific fact)
> - FOL = "EVERY room has a light. SOME lights are on. The light in John's room is the BRIGHTEST." (talks about objects, properties, and relationships!)

---

## 📚 Table of Contents

1. [The Building Blocks of FOL](#1-building-blocks)
2. [Predicates vs Functions — FULLY Explained](#2-predicates-vs-functions)
3. [Quantifiers: ∀ and ∃](#3-quantifiers)
4. [The ∀→ and ∃∧ Rules (CRITICAL!)](#4-rules)
5. [🧮 20 English-to-FOL Translations](#5-translations)
6. [Nested Quantifiers (Order Matters!)](#6-nested)
7. [Negating Quantifiers](#7-negation)
8. [Key Takeaways](#8-key-takeaways)
9. [Exam Tips](#9-exam-tips)

---

## 1. The Building Blocks of FOL

| Element | What It Is | Example | ELI5 |
|---|---|---|---|
| **Constants** | Specific named things | `John`, `Mars`, `3` | Proper nouns: "John", "Mars" |
| **Variables** | Placeholder for ANY thing | `x`, `y`, `z` | "Someone", "something" |
| **Predicates** | Questions with yes/no answers | `Tall(John)` → T/F | "Is John tall?" Yes/No |
| **Functions** | Pointer to a THING | `Father(John)` → Henry | "John's father is..." → points to Henry |
| **Connectives** | AND, OR, NOT, →, ↔ | `P ∧ Q` | Same as propositional logic |
| **Quantifiers** | "For all" (∀), "Exists" (∃) | `∀x`, `∃x` | "Every...", "Some..." |

---

## 2. Predicates vs Functions — FULLY Explained

### This Is THE Most Confusing Part of FOL. Let's Make It Crystal Clear.

### Predicates = YES/NO Questions About Objects

A predicate takes one or more objects and returns **TRUE** or **FALSE**.

```
Tall(John)           → "Is John tall?"          → TRUE or FALSE
Loves(John, Mary)    → "Does John love Mary?"   → TRUE or FALSE
Brother(Bob, Alice)  → "Is Bob Alice's brother?" → TRUE or FALSE
GreaterThan(5, 3)    → "Is 5 > 3?"              → TRUE (yes!)
```

> 🍼 **Predicate = asking a question that can ONLY be answered YES or NO.**

### Functions = Pointers to Objects

A function takes an object and returns **ANOTHER OBJECT** (not true/false!).

```
Father(John)         → "Who is John's father?"   → Henry (a PERSON!)
Mother(John)         → "Who is John's mother?"    → Sarah (a PERSON!)
CapitalOf(France)    → "What is France's capital?" → Paris (a CITY!)
Plus(3, 5)           → "What is 3 + 5?"            → 8 (a NUMBER!)
```

> 🍼 **Function = a machine that takes in one thing and spits out ANOTHER thing.**

### 🧮 Side-by-Side Comparison

```
PREDICATE:                         FUNCTION:
─────────────────────             ─────────────────────
Input: John                        Input: John
Output: TRUE or FALSE              Output: An OBJECT (a person, thing, etc.)

Tall(John) → TRUE                  Father(John) → Henry
"Is John tall? YES"                "John's father = Henry"

Loves(John, Mary) → TRUE           BestFriend(John) → Bob
"Does John love Mary? YES"         "John's best friend = Bob"

Used as: A SENTENCE                Used as: A NAME for an object
"John is tall" (complete thought)  "John's father" (refers to a person)
```

### You Can COMBINE Them! (This Is Where It Gets Powerful!)

```
Tall(Father(John))
       ↑               ↑
   predicate        function
   (asks yes/no)    (returns Henry)

Step 1: Father(John) → Henry
Step 2: Tall(Henry)  → TRUE or FALSE

Full meaning: "Is John's father tall?"
```

```
Loves(Father(John), Mother(Mary))
       ↑                    ↑
   function → Henry     function → Susan

Step 1: Father(John) → Henry
Step 2: Mother(Mary) → Susan  
Step 3: Loves(Henry, Susan) → TRUE or FALSE

Full meaning: "Does John's father love Mary's mother?"
```

> 🍼 **Kid Version**: A PREDICATE is like a judge who says "GUILTY!" or "NOT GUILTY!" A FUNCTION is like a GPS that says "Turn left, your destination is on the right" (points to a place). You can combine them: "Is the place my GPS pointed to dangerous?" → GPS (function) finds the place, then the judge (predicate) evaluates it!

---

## 3. Quantifiers: ∀ and ∃

### ∀ = "For ALL" — The Box Checker

**∀x: P(x)** = "P is true for EVERY SINGLE object in the world"

```
∀x: Dog(x) → Barks(x)
"For ALL x: IF x is a dog, THEN x barks"
= "All dogs bark" = "Every dog barks"
```

> 🍼 **Kid Version**: Imagine you have a HUGE box of toys. ∀ means you check EVERY SINGLE toy in the box. "∀x: Toy(x) → Fun(x)" means you check every item: "Is it a toy? If yes, is it fun?" If even ONE toy is not fun → the statement is FALSE!

**How to think about ∀:**
```
∀x: P(x) is like a giant AND:
  P(object₁) AND P(object₂) AND P(object₃) AND ... AND P(objectₙ)
  
  ALL must be true for ∀ to be true!
```

### ∃ = "There EXISTS" — The Treasure Hunter

**∃x: P(x)** = "P is true for AT LEAST ONE object"

```
∃x: Dog(x) ∧ Friendly(x)
"There EXISTS an x such that x is a dog AND x is friendly"
= "Some dog is friendly" = "At least one friendly dog exists"
```

> 🍼 **Kid Version**: You're digging through the toy box looking for ONE specific thing. "∃x: Toy(x) ∧ Red(x)" means "Is there AT LEAST ONE red toy?" You dig through toys. Find one red toy? TRUE! Didn't find any? FALSE!

**How to think about ∃:**
```
∃x: P(x) is like a giant OR:
  P(object₁) OR P(object₂) OR P(object₃) OR ... OR P(objectₙ)
  
  At least ONE must be true for ∃ to be true!
```

---

## 4. The ∀→ and ∃∧ Rules (CRITICAL! EXAM FAVORITE!)

### 🚨 THE SINGLE MOST IMPORTANT RULE IN FOL 🚨

```
∀ (for all) ALWAYS goes with → (implication)
∃ (there exists) ALWAYS goes with ∧ (and)
```

### Why ∀ Uses → (Not ∧) — Explained Like You're 5!

**CORRECT**: ∀x: Dog(x) → Barks(x)
"For every x: IF x is a dog, THEN x barks"

What happens when x = a CAT?
```
Dog(cat) = FALSE
Dog(cat) → Barks(cat) = FALSE → anything = TRUE!
The rule is SATISFIED for cats — it says nothing about cats!
```

**WRONG**: ∀x: Dog(x) ∧ Barks(x)
"For every x: x is a dog AND x barks"

What happens when x = a CAT?
```
Dog(cat) ∧ Barks(cat) = FALSE ∧ anything = FALSE!
The statement claims the CAT is a dog! FALSE for every non-dog!
```

This would mean: "EVERYTHING in the universe is a barking dog" — cats, tables, numbers, the moon... all barking dogs?! 😱 That's obviously wrong!

> 🍼 **The Simple Memory Trick**: 
> - ∀ + → = "IF you're a dog, THEN you bark" (only applies to dogs, ignores non-dogs)
> - ∀ + ∧ = "You ARE a dog AND you bark" (claims EVERYTHING is a barking dog!)

### Why ∃ Uses ∧ (Not →) — Explained Like You're 5!

**CORRECT**: ∃x: Dog(x) ∧ Friendly(x)
"There exists an x that IS a dog AND IS friendly"
= "Some dog is friendly" ✅

**WRONG**: ∃x: Dog(x) → Friendly(x)
"There exists an x such that IF x is a dog, THEN x is friendly"

What happens when x = a ROCK?
```
Dog(rock) → Friendly(rock) = FALSE → anything = TRUE!
We found an x (the rock) that satisfies the formula!
```

But that proves "a rock satisfies 'if it's a dog, it's friendly'" — which is technically true but completely meaningless! It tells us NOTHING about whether any actual dog is friendly!

> 🍼 **The Simple Memory Trick**:
> - ∃ + ∧ = "I found something that IS a dog AND IS friendly" (found an actual friendly dog!)
> - ∃ + → = "I found something that would be friendly IF it were a dog" (could be a rock — useless!)

---

## 5. 🧮 20 English-to-FOL Translations

### Basic (Warm-Up)

| # | English | FOL |
|---|---|---|
| 1 | "All dogs bark" | ∀x: Dog(x) → Barks(x) |
| 2 | "Some dogs bark" | ∃x: Dog(x) ∧ Barks(x) |
| 3 | "No dogs fly" | ∀x: Dog(x) → ¬Flies(x) |
| 4 | "Not all birds fly" | ∃x: Bird(x) ∧ ¬Flies(x) |
| 5 | "John is tall" | Tall(John) |
| 6 | "John loves Mary" | Loves(John, Mary) |
| 7 | "John's father is tall" | Tall(Father(John)) |

### Intermediate

| # | English | FOL | Notes |
|---|---|---|---|
| 8 | "**Only** dogs bark" | ∀x: Barks(x) → Dog(x) | "Only A are B" → ∀x: B(x)→A(x) — FLIPS! |
| 9 | "Everyone loves someone" | ∀x: Person(x) → ∃y: Loves(x,y) | Each person has their own "someone" |
| 10 | "Someone is loved by everyone" | ∃y: ∀x: Person(x) → Loves(x,y) | ONE person loved by ALL |
| 11 | "Nobody likes Monday" | ∀x: Person(x) → ¬Likes(x, Monday) | Nobody = ∀...→¬ |
| 12 | "If you don't study, you fail" | ∀x: ¬Studies(x) → Fails(x) | |
| 13 | "You fail unless you study" | ∀x: ¬Studies(x) → Fails(x) | Unless = if not! Same as #12! |

### Advanced

| # | English | FOL |
|---|---|---|
| 14 | "Every student likes some teacher" | ∀x: Student(x) → ∃y: (Teacher(y) ∧ Likes(x,y)) |
| 15 | "There's a teacher all students like" | ∃y: Teacher(y) ∧ ∀x: (Student(x) → Likes(x,y)) |
| 16 | "The best friend of every person is nice" | ∀x: Person(x) → Nice(BestFriend(x)) |
| 17 | "Everybody's mother loves them" | ∀x: Person(x) → Loves(Mother(x), x) |
| 18 | "There's no largest number" | ∀x: Number(x) → ∃y: (Number(y) ∧ Greater(y, x)) |
| 19 | "All that glitters is not gold" | ∀x: Glitters(x) → ¬Gold(x) |
| 20 | "Some students passed every exam" | ∃x: Student(x) ∧ ∀y: (Exam(y) → Passed(x,y)) |

### 🧮 Detailed Walkthrough: #8 "Only dogs bark"

```
"All dogs bark" vs "Only dogs bark" — what's the difference?

"All dogs bark" = "Everything that IS a dog → barks"
  FOL: ∀x: Dog(x) → Barks(x)
  Meaning: Dogs bark. (But cats MIGHT also bark — we didn't say they can't!)

"Only dogs bark" = "Everything that barks → is a dog"
  FOL: ∀x: Barks(x) → Dog(x)
  Meaning: If it barks, it MUST be a dog. Nothing else barks!

NOTICE: The arrow FLIPS! 
  "All A are B" → ∀x: A(x) → B(x)
  "Only A are B" → ∀x: B(x) → A(x)
```

### 🧮 Detailed Walkthrough: #9 vs #10

```
#9:  "Everyone loves someone"
     ∀x: Person(x) → ∃y: Loves(x, y)
     
     Alice loves Bob. Charlie loves Diana. Eve loves herself.
     Each person has their OWN "someone" — they can all love different people!

#10: "Someone is loved by everyone"
     ∃y: ∀x: Person(x) → Loves(x, y)
     
     There's ONE person y (say, Bob) such that EVERYONE loves Bob.
     Alice loves Bob. Charlie loves Bob. Eve loves Bob. ALL love Bob!

#9 says everyone has at least one love. (Weaker)
#10 says there's one person loved by all. (MUCH stronger!)
```

---

## 6. Nested Quantifiers (Order Matters!)

| FOL | English | Diagram |
|---|---|---|
| ∀x ∀y: Loves(x,y) | Everyone loves everyone | All arrows from all to all |
| ∀x ∃y: Loves(x,y) | Everyone loves at least one person | Each person has ≥1 outgoing arrow |
| ∃x ∀y: Loves(x,y) | One person loves everyone | One person has arrows to ALL others |
| ∃x ∃y: Loves(x,y) | Someone loves someone | At least 1 arrow exists anywhere |

**The strength ordering**: ∃∃ (weakest) < ∀∃ < ∃∀ < ∀∀ (strongest)

---

## 7. Negating Quantifiers (De Morgan's for FOL)

```
¬(∀x: P(x))  ≡  ∃x: ¬P(x)       "NOT all are P" = "SOME are not P"
¬(∃x: P(x))  ≡  ∀x: ¬P(x)       "NONE are P" = "ALL are not P"
```

> 🍼 **Kid Version**: 
> "NOT all kids ate lunch" = "SOME kid didn't eat lunch"
> "NO kid is crying" = "EVERY kid is not crying"

Just like De Morgan's in propositional logic:
- ∀ flips to ∃ (like ∧ flips to ∨)
- ∃ flips to ∀ (like ∨ flips to ∧)
- The inner formula gets negated

---

## 8. Key Takeaways

1. **FOL adds objects, predicates, functions, and quantifiers** to propositional logic
2. **Predicates → T/F** ("Is John tall?"); **Functions → objects** ("John's father = Henry")
3. **∀ + →** is the ONLY correct pattern for "all A are B" (∀ + ∧ = WRONG!)
4. **∃ + ∧** is the ONLY correct pattern for "some A is B" (∃ + → = WRONG!)
5. **"Only A are B" FLIPS the arrow**: ∀x: B(x) → A(x)
6. **∀x∃y ≠ ∃y∀x** — order of quantifiers matters!
7. **¬∀ = ∃¬** and **¬∃ = ∀¬** — negation flips quantifiers

---

## 9. Exam Tips

### The #1 Exam Question

"Translate this English sentence into FOL" — you WILL get at least 3-5 of these!

### Common Mistakes

❌ ∀x: Dog(x) ∧ Barks(x) → means "everything is a barking dog"!
❌ ∃x: Dog(x) → Friendly(x) → true for any non-dog (vacuously true)!
❌ "Only dogs bark" → ∀x: Dog(x) → Barks(x) → WRONG! Arrow is FLIPPED!
❌ Mixing up ∀x∃y with ∃y∀x → very different meanings!

---

## 📖 References

- AIMA — Chapter 8

---

[⬅️ Prev: Propositional Logic](../11_Propositional_Logic/README.md) | [Back to Main](../README.md) | [Next: FOL Inference ➡️](../13_FOL_Inference_Unification/README.md)
