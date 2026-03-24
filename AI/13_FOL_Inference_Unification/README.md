# ⚙️ Topic 13 — FOL Inference: Unification, Backward Chaining & Resolution

> **Difficulty**: 🔴 Hard | **Syllabus Section**: Knowledge & Reasoning
>
> **Slides**: RB-M & SD-M | **Quiz Relevance**: ⭐⭐⭐⭐⭐
---

## 🍼 The Big Story (ELI5)

### Teaching a Robot to Think 🤖

You've told the robot two things:
- **Rule**: "All dogs are animals" → ∀x: Dog(x) → Animal(x)
- **Fact**: "Rex is a dog" → Dog(Rex)

Now you ask: "Is Rex an animal?"

The robot needs to figure this out BY ITSELF! But how?

1. **Unification**: "Hey, Dog(x) and Dog(Rex) look similar. If I set x = Rex, they MATCH!" (like fitting puzzle pieces together)
2. **Apply the rule**: "Since Dog(Rex) is true and the rule says Dog(x) → Animal(x), and x = Rex, then Animal(Rex) must be true!"

> 🍼 **Kid Version**:
> - **Unification** = matching puzzle pieces. "Does this shape fit in that hole? Let me rotate it until it fits!" → finding that x = Rex makes Dog(x) match Dog(Rex)
> - **Backward Chaining** = working backwards from your question. "Is Rex an animal? What RULE gives me 'animal'? The one that says dogs are animals. Is Rex a dog? YES! So Rex IS an animal!"
> - **Resolution** = proof by contradiction. "Let me ASSUME Rex is NOT an animal. But I can prove he IS. Contradiction! So he MUST be an animal."

---

## 📚 Table of Contents

1. [The Big Picture: How FOL Inference Works](#1-big-picture)
2. [Instantiation: Making Rules Specific](#2-instantiation)
3. [Unification: Matching Patterns](#3-unification)
4. [🧮 Unification Examples (10 Problems!)](#4-unification-examples)
5. [Forward Chaining: Data → Conclusions](#5-forward-chaining)
6. [Backward Chaining: Question → Data](#6-backward-chaining)
7. [🧮 Backward Chaining Full Trace](#7-backward-trace)
8. [Resolution in FOL](#8-resolution)
9. [🧮 Converting to Clause Form (Step by Step!)](#9-clause-form)
10. [🧮 Resolution Proof (Complete Example)](#10-resolution-proof)
11. [Key Takeaways](#11-key-takeaways)
12. [Exam Tips](#12-exam-tips)

---

## 1. The Big Picture

### Why Is FOL Inference Harder Than Propositional?

In propositional logic: we have specific facts like `Rain` and `Wet`. Easy to match!

In FOL: we have VARIABLES like `∀x: Dog(x) → Animal(x)`. The `x` could be ANYTHING. The computer needs to figure out WHAT to put in for `x`. That's what **unification** does!

### The Inference Pipeline

```
Step 1: Take a general rule     ∀x: Dog(x) → Animal(x)
Step 2: Find a matching fact     Dog(Rex)
Step 3: UNIFY them               x = Rex (unification!)
Step 4: Apply the rule           Animal(Rex) ← NEW FACT!
```

---

## 2. Instantiation: Making Rules Specific

### Universal Instantiation (UI)

If something is true for ALL x, it's true for any SPECIFIC thing:

```
∀x: Dog(x) → Animal(x)    ← True for ALL x

Therefore (substituting specific things for x):
  Dog(Rex) → Animal(Rex)           ← substitute x = Rex
  Dog(Buddy) → Animal(Buddy)      ← substitute x = Buddy
  Dog(Father(John)) → Animal(Father(John))  ← substitute x = Father(John)

ANY ground term (no variables) can replace x. You can do this as many times as you want!
```

> 🍼 **Kid Version**: "The rule says ALL dogs are animals. Rex is a specific dog. So Rex is an animal. Buddy is another specific dog. So Buddy is an animal too. We can use the 'all' rule for any specific dog!"

### Existential Instantiation (EI)

If something EXISTS, give it a NAME:

```
∃x: Crown(x) ∧ OnHead(x, John)
"There exists SOME crown that's on John's head"

→ Crown(C₁) ∧ OnHead(C₁, John)
"Let's call that crown C₁"

C₁ is a BRAND NEW name (Skolem constant) that doesn't exist anywhere else.
You can only do this ONCE for each ∃.
```

> 🍼 **Kid Version**: "Someone in the room is wearing a red hat. I don't know who, but let's call them 'Red-Hat Person.' Now I can talk about Red-Hat Person without knowing their real name!"

### Skolemization (When ∃ Is Inside ∀)

When ∃ is NESTED inside ∀, the "someone" might be DIFFERENT for each "everyone":

```
∀x: ∃y: Loves(x, y)
"Everyone loves SOMEONE" (each person might love a different someone!)

Skolemize: Loves(x, F(x))
"Everyone loves F(x)" where F is a new FUNCTION that picks the loved person for each x

F(Alice) = Bob      ← Alice loves Bob
F(Charlie) = Diana  ← Charlie loves Diana
F(Eve) = Eve        ← Eve loves herself

F(x) is called a SKOLEM FUNCTION — it depends on x because the ∃ was inside ∀x.
```

**Compare**: If ∃ is NOT inside ∀:
```
∃y: ∀x: Loves(x, y) → Skolemize: Loves(x, c)    ← Skolem CONSTANT (same for everyone)
"Everyone loves the same person c"
```

> 🍼 **The Rule**:
> - ∃ with no ∀ outside → Skolem **constant** (one fixed name)
> - ∃ inside ∀x → Skolem **function** F(x) (depends on x)
> - ∃ inside ∀x∀y → Skolem **function** F(x, y) (depends on both)

---

## 3. Unification: Matching Patterns

### What Is Unification?

**Unification** finds a **substitution** (a mapping of variables to values) that makes two expressions IDENTICAL.

```
Expression 1: Knows(John, x)     ← "John knows someone (x)"
Expression 2: Knows(John, Jane)  ← "John knows Jane"

Can we make them match? YES! Set x = Jane!

Substitution: θ = {x/Jane}     ← "Replace x with Jane"

After applying θ:
  Knows(John, Jane) = Knows(John, Jane) ✅ MATCH!
```

> 🍼 **Kid Version**: Unification is like a fill-in-the-blank game!
> "John knows ___" and "John knows Jane" → fill in the blank with "Jane"!
>
> Sometimes BOTH sides have blanks:
> "___ knows ___" and "John knows Jane" → first blank = John, second blank = Jane!

### The Rules of Unification

```
1. A variable can match ANY term:         x matches Jane → {x/Jane}
2. A constant matches only ITSELF:        John matches John ✅, John matches Bob ❌
3. A function matches the SAME function:  Father(x) matches Father(John) → {x/John}
                                          Father(x) matches Mother(John) → FAIL ❌
4. Recursion: match the arguments one by one
5. OCCUR CHECK: x cannot match f(x) → would be infinite! x = f(f(f(f(...)))) 💀
```

---

## 4. 🧮 Unification Examples (10 Problems!)

### Easy Examples

**Example 1**: Unify `Knows(John, x)` with `Knows(John, Jane)`
```
Knows matches Knows ✅
John matches John ✅
x matches Jane → θ = {x/Jane} ✅

Result: θ = {x/Jane}
```

**Example 2**: Unify `Knows(John, x)` with `Knows(y, Bill)`
```
Knows matches Knows ✅
John matches y → y = John
x matches Bill → x = Bill

Result: θ = {y/John, x/Bill}
```

**Example 3**: Unify `P(x, A)` with `P(B, y)`
```
P matches P ✅
x matches B → x = B
A matches y → y = A

Result: θ = {x/B, y/A}
```

### Medium Examples

**Example 4**: Unify `Knows(John, x)` with `Knows(y, Mother(y))`
```
John matches y → y = John
x matches Mother(y) → but y = John → x matches Mother(John)

Result: θ = {y/John, x/Mother(John)}

Verification: 
  Knows(John, Mother(John)) = Knows(John, Mother(John)) ✅
```

**Example 5**: Unify `P(x, f(x))` with `P(A, y)`
```
x matches A → x = A
f(x) matches y → apply x=A → f(A) matches y → y = f(A)

Result: θ = {x/A, y/f(A)}
```

**Example 6**: Unify `P(x, x)` with `P(A, B)`
```
x matches A → x = A
x matches B → but x is already A!
  A = B? Only if A and B are the same constant. 
  If A ≠ B → FAIL! ❌

Result: FAIL (x can't be both A and B!)
```

### Hard Examples

**Example 7**: Unify `Knows(John, x)` with `Knows(x, Jane)`
```
John matches x → x = John
x matches Jane → but x = John → John matches Jane?
  John ≠ Jane → FAIL! ❌

Result: FAIL (x can't be both John and Jane!)
```

**Example 8**: Unify `P(x, f(y))` with `P(g(z), f(z))`
```
x matches g(z) → x = g(z)
f(y) matches f(z) → y matches z → y = z

Result: θ = {x/g(z), y/z}

Alternatively written as: θ = {x/g(y)} (since y=z, use either name)
```

**Example 9**: Unify `x` with `f(x)` — THE OCCUR CHECK!
```
Can x = f(x)?
If so: x = f(x) = f(f(x)) = f(f(f(x))) = ... INFINITE! 💀

Result: FAIL (occur check violation!)
```

**Example 10**: Unify `P(x, y)` with `P(y, x)`
```
x matches y → x = y (now x and y are the same variable)
y matches x → y = x (consistent with above)

Result: θ = {x/y}   (or equivalently {y/x})

Both P(y, y) = P(y, y) ✅
```

### Most General Unifier (MGU)

The **MGU** makes the LEAST SPECIFIC substitution:

```
Unify P(x) with P(y):
  MGU = {x/y}              ← Most general: just says x equals y
  Also valid: {x/John, y/John} ← But this is too specific! Commits to John unnecessarily
  
ALWAYS prefer the MGU!
```

---

## 5. Forward Chaining: Data → Conclusions

### The Idea

Start with KNOWN FACTS. Apply rules to derive NEW facts. Repeat until you find the answer.

```
Direction: Facts ──→ Rules ──→ New Facts ──→ Rules ──→ ... ──→ Answer!
           (bottom-up)
```

> 🍼 **Kid Version**: "Start with what I KNOW. Check: can any rule be used? If yes, derive new facts. Check again. Keep going until I find what I'm looking for!"

### Example

```
KB:
  Fact 1: Dog(Rex)
  Fact 2: Owns(John, Rex)
  Rule 3: ∀x: Dog(x) → Animal(x)
  Rule 4: ∀x,y: Owns(x, y) ∧ Animal(y) → Loves(x, y)

Forward chaining:

Iteration 1:
  Rule 3 matches Dog(Rex) with x=Rex → derive Animal(Rex) ← NEW FACT!

Iteration 2:
  Rule 4 matches Owns(John, Rex) ∧ Animal(Rex) with x=John, y=Rex
  → derive Loves(John, Rex) ← NEW FACT!

Done! We derived that John loves Rex! 🐕❤️
```

---

## 6. Backward Chaining: Question → Data

### The Idea

Start with the QUESTION. Find rules that could ANSWER it. Prove their premises. Work BACKWARDS!

```
Direction: Question ──→ "What rule gives me this?" ──→ "Can I prove the premises?" ──→ Facts!
           (top-down)
```

> 🍼 **Kid Version**: "I want to know if John loves Rex. What rule concludes 'Loves'? Rule 4! It needs Owns and Animal. Does John own Rex? YES (fact). Is Rex an animal? What rule concludes 'Animal'? Rule 3! It needs Dog. Is Rex a dog? YES (fact)! All proven! So John loves Rex!"

---

## 7. 🧮 Backward Chaining Full Trace

### The Knowledge Base

```
Fact 1: American(West)
Fact 2: Weapon(M1)
Fact 3: Sells(West, M1, Nono)
Fact 4: Hostile(Nono)
Rule 5: ∀x,y,z: American(x) ∧ Weapon(y) ∧ Sells(x,y,z) ∧ Hostile(z) → Criminal(x)
```

### Query: Is West a criminal? Criminal(West)?

```
GOAL: Criminal(West)

Step 1: "What rule concludes Criminal(x)?"
  → Rule 5: American(x) ∧ Weapon(y) ∧ Sells(x,y,z) ∧ Hostile(z) → Criminal(x)
  → Unify Criminal(x) with Criminal(West) → θ = {x/West}
  → Now I need to prove ALL four premises with x=West:
     Subgoal A: American(West)
     Subgoal B: Weapon(y)          ← y is still unknown!
     Subgoal C: Sells(West, y, z)  ← y and z unknown!
     Subgoal D: Hostile(z)

Step 2: Prove subgoal A: American(West)?
  → Check facts: Fact 1 says American(West) ✅ PROVEN!

Step 3: Prove subgoal B: Weapon(y)?
  → Check facts: Fact 2 says Weapon(M1)
  → Unify Weapon(y) with Weapon(M1) → θ = {y/M1}
  → ✅ PROVEN! And now y = M1

Step 4: Prove subgoal C: Sells(West, M1, z)?  (y is now M1)
  → Check facts: Fact 3 says Sells(West, M1, Nono)
  → Unify Sells(West, M1, z) with Sells(West, M1, Nono) → θ = {z/Nono}
  → ✅ PROVEN! And now z = Nono

Step 5: Prove subgoal D: Hostile(Nono)?  (z is now Nono)
  → Check facts: Fact 4 says Hostile(Nono) ✅ PROVEN!

ALL four subgoals proven! Therefore:
  Criminal(West) is TRUE! 🎯

Full substitution: θ = {x/West, y/M1, z/Nono}
```

> 🍼 **Kid Version**: 
> "Is West a criminal? → I need a rule about criminals. Found Rule 5! It says: to be criminal, you need to be American, sell weapons to a hostile country. → Is West American? YES (Fact 1). → Is there a weapon? Yes, M1 (Fact 2). → Does West sell M1 to someone? Yes, to Nono (Fact 3). → Is Nono hostile? YES (Fact 4). → All conditions met → **West IS a criminal!**"

### Forward vs Backward — When to Use Which?

| | Forward Chaining | Backward Chaining |
|---|---|---|
| **Direction** | Facts → Conclusions | Query → Facts |
| **Strength** | Finds everything derivable | Only explores relevant rules |
| **Weakness** | May derive lots of irrelevant stuff | Only answers one specific question |
| **Used in** | Database triggers, production systems | Prolog, expert systems, Q&A |
| **Like** | "What can I conclude from what I know?" | "How can I prove this specific thing?" |

---

## 8. Resolution in FOL

### Same Idea as Propositional, But With Unification!

```
Propositional resolution:
  P ∨ Q      and     ¬P ∨ R      →    Q ∨ R
  (P cancels with ¬P)

FOL resolution:
  Animal(x) ∨ Loves(x)    and    ¬Animal(Rex) ∨ Happy(Rex)
  
  Unify Animal(x) with Animal(Rex) → θ = {x/Rex}
  Apply θ: Loves(Rex) ∨ Happy(Rex)
```

### Resolution Proof Method (Proof by Refutation)

```
To prove KB ⊨ α (the knowledge base entails α):
1. Convert everything to CLAUSE FORM (CNF for FOL)
2. Add ¬α (assume the OPPOSITE of what we want to prove)
3. Apply resolution repeatedly
4. If we derive □ (empty clause = contradiction) → α is PROVEN!
```

---

## 9. 🧮 Converting to Clause Form (Step by Step!)

### The 7 Steps (Must Memorize This Procedure!)

Let's convert: ∀x: [Dog(x) → ∃y: Loves(y, x)]
"Every dog is loved by someone"

**Step 1: Eliminate → (implication)**
```
∀x: [¬Dog(x) ∨ ∃y: Loves(y, x)]
Using P → Q ≡ ¬P ∨ Q
```

**Step 2: Push ¬ inward (using De Morgan's)**
```
Already done (no ¬ to push in this example)
```

**Step 3: Standardize variables (give unique names)**
```
Already done (x and y are distinct)
```

**Step 4: Skolemize (remove ∃)**
```
∃y is INSIDE ∀x → Skolem FUNCTION F(x):
∀x: [¬Dog(x) ∨ Loves(F(x), x)]
"For every dog x, F(x) loves x" where F picks the lover for each dog
```

**Step 5: Drop universal quantifiers (∀)**
```
¬Dog(x) ∨ Loves(F(x), x)
(Everything remaining is implicitly ∀)
```

**Step 6: Distribute ∨ over ∧ (already in CNF!)**
```
¬Dog(x) ∨ Loves(F(x), x)    ← This IS a clause (an OR of literals)
```

**Step 7: Write as a set of clauses**
```
Clause: {¬Dog(x), Loves(F(x), x)}
```

### A Harder Example

Convert: ∀x: [∀y: Animal(y) → Loves(x,y)] → [∃y: Loves(y,x)]
"Everyone who loves all animals is loved by someone"

```
Step 1: Eliminate →
  ∀x: ¬[∀y: ¬Animal(y) ∨ Loves(x,y)] ∨ [∃y: Loves(y,x)]

Step 2: Push ¬ inward
  ∀x: [∃y: ¬(¬Animal(y) ∨ Loves(x,y))] ∨ [∃y: Loves(y,x)]
  ∀x: [∃y: Animal(y) ∧ ¬Loves(x,y)] ∨ [∃y: Loves(y,x)]

Step 3: Standardize variables (rename the two y's to avoid confusion!)
  ∀x: [∃y: Animal(y) ∧ ¬Loves(x,y)] ∨ [∃z: Loves(z,x)]

Step 4: Skolemize
  y inside ∀x → F(x)
  z inside ∀x → G(x)
  ∀x: [Animal(F(x)) ∧ ¬Loves(x, F(x))] ∨ [Loves(G(x), x)]

Step 5: Drop ∀
  [Animal(F(x)) ∧ ¬Loves(x, F(x))] ∨ Loves(G(x), x)

Step 6: Distribute ∨ over ∧
  [Animal(F(x)) ∨ Loves(G(x), x)] ∧ [¬Loves(x, F(x)) ∨ Loves(G(x), x)]

Step 7: Two clauses:
  C1: {Animal(F(x)), Loves(G(x), x)}
  C2: {¬Loves(x, F(x)), Loves(G(x), x)}
```

---

## 10. 🧮 Resolution Proof (Complete Example)

### Problem

```
KB:
  1. Dog(Rex)                              ← "Rex is a dog"
  2. ∀x: Dog(x) → Animal(x)               ← "All dogs are animals"
  3. ∀x: Animal(x) → LivingThing(x)       ← "All animals are living things"

Prove: LivingThing(Rex)                    ← "Rex is a living thing"
```

### Step 1: Convert to clause form

```
Fact 1: Dog(Rex)                           → Clause: {Dog(Rex)}
Rule 2: ∀x: Dog(x) → Animal(x)           → Clause: {¬Dog(x), Animal(x)}
Rule 3: ∀x: Animal(x) → LivingThing(x)   → Clause: {¬Animal(x), LivingThing(x)}
```

### Step 2: Add negation of goal

```
Goal: LivingThing(Rex) → Negate: ¬LivingThing(Rex)
Clause 4: {¬LivingThing(Rex)}
```

### Step 3: Resolve!

```
Our clauses:
  C1: Dog(Rex)
  C2: ¬Dog(x₁) ∨ Animal(x₁)        (I renamed x to x₁ for clarity)
  C3: ¬Animal(x₂) ∨ LivingThing(x₂)  
  C4: ¬LivingThing(Rex)

Resolve C3 and C4:
  C3 has LivingThing(x₂), C4 has ¬LivingThing(Rex)
  Unify: x₂ = Rex
  Cancel LivingThing(Rex) and ¬LivingThing(Rex)
  C5: ¬Animal(Rex)                    ← "Rex is not an animal" (temporary!)

Resolve C2 and C5:
  C2 has Animal(x₁), C5 has ¬Animal(Rex)
  Unify: x₁ = Rex
  Cancel Animal(Rex) and ¬Animal(Rex)
  C6: ¬Dog(Rex)                       ← "Rex is not a dog" (temporary!)

Resolve C1 and C6:
  C1 has Dog(Rex), C6 has ¬Dog(Rex)
  Cancel Dog(Rex) and ¬Dog(Rex)
  C7: □ (EMPTY CLAUSE!)               ← CONTRADICTION! 🎯
```

### Step 4: Conclusion

We assumed ¬LivingThing(Rex) and derived a contradiction. Therefore, **LivingThing(Rex) is TRUE!** ✅

```
Proof chain:
  C4: ¬LivingThing(Rex)     (assumed)
  C3 + C4 → C5: ¬Animal(Rex)
  C2 + C5 → C6: ¬Dog(Rex)
  C1 + C6 → C7: □ CONTRADICTION!

  Working backwards through the chain:
  Rex IS a dog (C1) → Rex IS an animal (C2) → Rex IS a living thing (C3) ✅
```

> 🍼 **Kid Version**: "I ASSUMED Rex is NOT a living thing. But Rule 3 says animals are living things, so Rex can't be an animal. But Rule 2 says dogs are animals, so Rex can't be a dog. But Fact 1 says Rex IS a dog! CONTRADICTION! My assumption was wrong — Rex IS a living thing!"

---

## 11. Key Takeaways

1. **Unification** = pattern matching with variables → finds substitution θ that makes two expressions identical
2. **MGU** = most general unifier (least specific substitution possible)
3. **Occur check**: x cannot unify with f(x) → infinite recursion!
4. **Skolemization**: remove ∃ by introducing Skolem constants (outside ∀) or Skolem functions (inside ∀)
5. **Forward chaining** = data → rules → new facts (bottom-up, like Prolog-engine)
6. **Backward chaining** = query → rules → subgoals → facts (top-down, like Prolog!)
7. **Resolution** = add ¬goal → resolve with unification → empty clause = PROVEN!
8. **Clause form conversion**: 7 steps — eliminate →, push ¬, standardize, Skolemize, drop ∀, distribute, split

---

## 12. Exam Tips

### Must-Know (You WILL Be Tested On These!)

1. **Unify two expressions** and give the MGU (at least 5 practice problems!)
2. **Trace backward chaining** on a KB with 3-4 rules
3. **Convert FOL to clause form** (all 7 steps!)
4. **Do a resolution proof** (add ¬goal, resolve to □)
5. **Know when unification FAILS** (same variable two different values, occur check)

### The Top Exam Mistakes

❌ **Unification**: Forgetting the occur check → Unify(x, f(x)) should FAIL!
❌ **Skolemization**: Using a constant when you should use a function → ∀x∃y needs F(x), not c!
❌ **Resolution**: Forgetting to NEGATE the goal before starting the proof!
❌ **Variables**: Not renaming variables → two different clauses sharing `x` should have different names!
❌ **Backward chaining**: Not propagating the substitution θ through all remaining subgoals

---

## 📖 References

- AIMA — Chapter 9 (Inference in First-Order Logic)

---

[⬅️ Prev: FOL Syntax](../12_FOL_Syntax_Semantics/README.md) | [Back to Main](../README.md) | [Next: Situation Calculus ➡️](../14_Planning_Situation_Calculus/README.md)
