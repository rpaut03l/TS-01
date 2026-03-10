# 💻 Bayesian Network Inference — PRACTICE
### Artificial Intelligence · AI 
### Book: Norvig | Unit: Probabilistic Reasoning — Part 2

> **Navigation:** [📋 INDEX](./bn_inference_index.md) | [← THEORY](./bn_inference_theory.md) | [← NUMERICALS](./bn_inference_numericals.md) | 💻 **PRACTICE** *(you are here)*

---

## 📚 Table of Contents

| # | Section | What's In It |
|---|---------|-------------|
| 1 | [Exam Hacks](#1-exam-hacks) | 9 specific tricks for full marks |
| 2 | [Graded Practice Problems](#2-graded-practice-problems) | Easy / Medium / Hard with hidden answers |
| 3 | [Python — α Normalisation](#3-python--α-normalisation) | Colab-ready, fully commented |
| 4 | [Python — Full Posterior P(B\|j,m)](#4-python--full-posterior-pbjm) | Enumeration + VE, both compared |
| 5 | [Python — Variable Elimination Demo](#5-python--variable-elimination-demo) | Factor table + savings visualiser |
| 6 | [Self-Test Q&A](#6-self-test-qa) | 12 exam-style questions with answers |

---

## 1. Exam Hacks

> [🔝 Top](#-table-of-contents) · [Next §2 →](#2-graded-practice-problems)

### Hack 1 — Label X, e, Y BEFORE writing any formula
```
Source of 80% of errors: mixing up variable types.

Before picking up your pen, write:
  X = _____ (query — want this)
  e = _____ (evidence — know this, don't sum)
  Y = _____ (hidden — sum over ALL values!)

Then write the formula.
```

### Hack 2 — Pull P(b) Out First — Always
```
P(b) appears in EVERY world combination.
It is constant to BOTH the a-sum and the e-sum.
Pull it ALL the way out before doing anything else.

= P(b) × [everything else]

Saves writing 0.001 or 0.999 inside 4 separate table rows!
```

### Hack 3 — The 0.63 and 0.0005 Shortcut
```
For P(B|j=T, m=T):

When a=T:  P(j|T) × P(m|T) = 0.90 × 0.70 = 0.63
When a=F:  P(j|F) × P(m|F) = 0.05 × 0.01 = 0.0005

These appear in EVERY world. Compute once, write into table directly.
Saves 2 multiplications per world = 8 total saved.
```

### Hack 4 — α is Always Just "Divide by Total"
```
Never compute P(e) separately.

α = 1 / (P(X=T,e) + P(X=F,e))

The total of your two unnormalised values IS 1/α.
Divide each by the total → done!
```

### Hack 5 — Sum-to-1 is Your Error Detector
```
After normalising:
  P(X=T|e) + P(X=F|e) MUST = 1.0 exactly

If not → arithmetic error somewhere!
Go back and check which world's product is wrong.
```

### Hack 6 — Rare Priors → Posterior Stays Relatively Small
```
P(Burglary) = 0.001
Even after 284× boost: 0.001 × 284 = 0.284

If your posterior for a rare-prior event is 0.95+ → error!
Always sanity check against the prior.
```

### Hack 7 — Factor Table is the Core VE Deliverable
```
In any VE exam question, the marker wants to see:
  1. Correct reorganisation (P(b) outside, nested sums)
  2. Dependency table (what depends on what)
  3. Factor table f(b,e) with all 4 computed values
  4. Outer e-sum correctly using those factors
  5. Final normalisation

Get the factor table right → rest is straightforward.
```

### Hack 8 — VE Elimination Order Rule
```
The variable you eliminate LAST is in the OUTERMOST sum.
The variable you eliminate FIRST is in the INNERMOST sum.

For P(B|j,m):
  Eliminate A first (a-sum innermost)
  Eliminate E second (e-sum outer)
  B is query — NEVER eliminate it!
```

### Hack 9 — Complement Saves Half Your CPT Work
```
Every CPT only stores P(X=True).
P(X=False) = 1 - P(X=True) — always!

P(¬Alarm | B=T, E=T) = 1 - 0.950 = 0.050
P(¬John  | A=T)      = 1 - 0.900 = 0.100
P(¬Mary  | A=F)      = 1 - 0.010 = 0.990

Use this in every single table row for the 'F' cases.
```

---

## 2. Graded Practice Problems

> [← §1](#1-exam-hacks) · [🔝 Top](#-table-of-contents) · [Next §3 →](#3-python--α-normalisation)

### ⭐ Easy

**E1.** Given P(x,e) = 0.35 and P(¬x,e) = 0.65, find α, P(x|e) and P(¬x|e).

**E2.** In the Bruno network, classify each variable when computing P(Alarm=T | Earthquake=T):
- Burglary = ?
- Alarm = ?
- Earthquake = ?
- John = ?
- Mary = ?

**E3.** Which term ALWAYS exits both sums first when computing P(B|j,m)?

**E4.** If P(B=T|j,m) = 0.284, what is P(B=F|j,m)? No calculation allowed.

**E5.** Compute f(F,F) — the factor for b=F, e=F — from scratch.

---

### ⭐⭐ Medium

**M1.** Compute P(Burglary=T | JohnCalls=T) — only one piece of evidence.
(Hint: hidden = {A, E, M}. You'll need to marginalise over M too.)

**M2.** Apply the VE reorganisation step to this expression. Name the resulting factor:
`Σ P(j|a) × P(a|b,e) × P(b) × P(e)`

**M3.** P(x,e) = 0.05 and P(¬x,e) = 0.45. Find:
- α
- P(x|e)
- P(¬x|e)
- Check they sum to 1.0

**M4.** Draw the dependency table for:
`P(j|a) × P(m|a) × P(a|b,e) × P(b) × P(e)`
(Which terms contain 'a'? Which contain 'e'? Which contain neither?)

**M5.** In VE for P(B|j,m), why is f(T,F) ≈ 0.592 so much larger than f(F,F) ≈ 0.001?
Explain in plain English using the CPT values.

---

### ⭐⭐⭐ Hard

**H1.** Compute the FULL posterior P(Earthquake=T | JohnCalls=T, MaryCalls=T).
(Query=E, Evidence={j=T,m=T}, Hidden={A,B})

**H2.** Apply VE to P(E|j,m). Write the full reorganised formula and compute all factor values.

**H3.** Show algebraically that α × Σ_X P(X,e) = 1 always holds.

**H4.** Would P(Burglary|j=T, m=F) be higher or lower than P(Burglary|j=T, m=T)?
Justify without doing the full computation.

**H5.** Why is Likelihood Weighting better than Rejection Sampling for the query
P(Burglary | JohnCalls=T, MaryCalls=T)?

---

### Answers to Easy Problems

<details>
<summary>▶ Click to reveal Easy answers</summary>

```
E1: total = 0.35+0.65 = 1.0
    α = 1/1.0 = 1.0
    P(x|e)  = 0.35/1.0 = 0.35
    P(¬x|e) = 0.65/1.0 = 0.65
    Note: already normalised — α=1 means no scaling needed!

E2: Alarm     = X (query — what we want)
    Earthquake = e (evidence — fixed at T)
    Burglary  = Y (hidden — sum over T and F!)
    John      = Y (hidden — sum over T and F!)
    Mary      = Y (hidden — sum over T and F!)

E3: P(b) — it contains neither 'a' nor 'e', so it exits BOTH sums.

E4: P(B=F|j,m) = 1 - 0.284 = 0.716
    Complement rule — no calculation needed!

E5: f(F,F) = P(A=T|B=F,E=F)×0.63 + P(A=F|B=F,E=F)×0.0005
           = 0.001×0.63 + 0.999×0.0005
           = 0.000630 + 0.000500
           = 0.001130
```

</details>

---

## 3. Python — α Normalisation

> [← §2](#2-graded-practice-problems) · [🔝 Top](#-table-of-contents) · [Next §4 →](#4-python--full-posterior-pbjm)

> 📋 **Copy-paste into Google Colab — zero installs needed!**

```python
# ============================================================
# ALPHA NORMALISATION — Complete Demo
# From Prof. Shilpa Dang's slide example
# CSL7610 AI · IIT Jodhpur
# ============================================================

def normalise(unnorm_dict):
    """
    Given {label: unnorm_probability}, return:
    - normalised probabilities
    - alpha value
    """
    total = sum(unnorm_dict.values())
    alpha = 1.0 / total
    normalised = {k: v / total for k, v in unnorm_dict.items()}
    return normalised, alpha, total

# ── Slide Example ─────────────────────────────────────────────
print("=" * 50)
print("SLIDE EXAMPLE: P(x,e)=0.192  P(~x,e)=0.224")
print("=" * 50)

unnorm = {'x=True': 0.192, 'x=False': 0.224}
result, alpha, total = normalise(unnorm)

print(f"\nUnnormalised values: {unnorm}")
print(f"Total = {total}")
print(f"α     = 1/{total} = {alpha:.6f}")
print()
for label, prob in result.items():
    print(f"P({label} | e) = {prob:.4f}  ({prob*100:.2f}%)")

print(f"\nSum check: {sum(result.values()):.6f}  ✅" if abs(sum(result.values())-1)<1e-9 else "FAIL")

# ── Complement Verification ────────────────────────────────────
print("\n--- COMPLEMENT CHECK ---")
p_xt  = result['x=True']
p_xf_complement  = 1 - p_xt
p_xf_direct      = result['x=False']
print(f"P(x=F|e) via complement:  {p_xf_complement:.4f}")
print(f"P(x=F|e) via direct:      {p_xf_direct:.4f}")
print(f"Match: {abs(p_xf_complement - p_xf_direct) < 1e-10}")

# ── α is same for ALL values ───────────────────────────────────
print("\n--- α SCALES ALL VALUES BY SAME FACTOR ---")
for label, v in unnorm.items():
    print(f"α × {v} = {alpha:.4f} × {v} = {v * alpha:.4f}")
```

**Expected Output:**
```
==================================================
SLIDE EXAMPLE: P(x,e)=0.192  P(~x,e)=0.224
==================================================

Unnormalised values: {'x=True': 0.192, 'x=False': 0.224}
Total = 0.416
α     = 1/0.416 = 2.403846

P(x=True  | e) = 0.4615  (46.15%)
P(x=False | e) = 0.5385  (53.85%)

Sum check: 1.000000  ✅

--- COMPLEMENT CHECK ---
P(x=F|e) via complement:  0.5385
P(x=F|e) via direct:      0.5385
Match: True

--- α SCALES ALL VALUES BY SAME FACTOR ---
α × 0.192 = 2.4038 × 0.192 = 0.4615
α × 0.224 = 2.4038 × 0.224 = 0.5385
```

---

## 4. Python — Full Posterior P(B|j,m)

> [← §3](#3-python--α-normalisation) · [🔝 Top](#-table-of-contents) · [Next §5 →](#5-python--variable-elimination-demo)

```python
# ============================================================
# FULL POSTERIOR: P(Burglary | JohnCalls=T, MaryCalls=T)
# Both Enumeration AND Variable Elimination
# CSL7610 AI · IIT Jodhpur
# ============================================================

# ── CPT Tables ───────────────────────────────────────────────
cpt_b = {True: 0.001, False: 0.999}
cpt_e = {True: 0.002, False: 0.998}
cpt_a = {
    (True,  True):  0.950,
    (True,  False): 0.940,
    (False, True):  0.290,
    (False, False): 0.001,
}
cpt_j = {True: 0.90,  False: 0.05}   # indexed by Alarm value
cpt_m = {True: 0.70,  False: 0.01}   # indexed by Alarm value

def pa(a_val, b_val, e_val):
    pt = cpt_a[(b_val, e_val)]
    return pt if a_val else 1 - pt

def pj(j_val, a_val): return cpt_j[a_val] if j_val else 1 - cpt_j[a_val]
def pm(m_val, a_val): return cpt_m[a_val] if m_val else 1 - cpt_m[a_val]

# ── ENUMERATION ───────────────────────────────────────────────
print("=" * 55)
print("APPROACH 1: ENUMERATION")
print("=" * 55)

unnorm_enum = {}
for b in [True, False]:
    inner = 0
    for a in [True, False]:
        for e in [True, False]:
            world = pj(True,a) * pm(True,a) * pa(a,b,e) * cpt_e[e]
            inner += world
    unnorm_enum[b] = cpt_b[b] * inner

total_enum = sum(unnorm_enum.values())
print(f"\nP(B=T, j, m) = {unnorm_enum[True]:.9f}")
print(f"P(B=F, j, m) = {unnorm_enum[False]:.9f}")
print(f"Total (= 1/α) = {total_enum:.9f}")
print()
for b, v in unnorm_enum.items():
    label = 'T' if b else 'F'
    p = v / total_enum
    print(f"P(B={label} | j=T, m=T) = {p:.4f}  ({p*100:.2f}%)")

# ── VARIABLE ELIMINATION ──────────────────────────────────────
print("\n" + "=" * 55)
print("APPROACH 2: VARIABLE ELIMINATION")
print("=" * 55)

# Step 1: Compute factor f(b,e) — inner a-sum — ONCE per (b,e) combo
print("\nStep 1 — Factor table f(b,e):")
print(f"{'b':>5} {'e':>5} | f(b,e)")
print("-" * 25)
factors = {}
for b in [True, False]:
    for e in [True, False]:
        # a=T contribution
        t_a = pa(True,b,e)  * pj(True,True)  * pm(True,True)
        # a=F contribution
        t_f = pa(False,b,e) * pj(True,False) * pm(True,False)
        factors[(b,e)] = t_a + t_f
        bl, el = 'T' if b else 'F', 'T' if e else 'F'
        print(f"{bl:>5} {el:>5} | {factors[(b,e)]:.6f}")

# Step 2: Outer e-sum using saved factors
print("\nStep 2 — Outer e-sum:")
unnorm_ve = {}
for b in [True, False]:
    e_sum = sum(cpt_e[e] * factors[(b,e)] for e in [True,False])
    unnorm_ve[b] = cpt_b[b] * e_sum
    bl = 'T' if b else 'F'
    print(f"B={bl}: {cpt_b[b]} × {e_sum:.9f} = {unnorm_ve[b]:.9f}")

# Normalise
total_ve = sum(unnorm_ve.values())
print(f"\nStep 3 — Normalise:")
for b, v in unnorm_ve.items():
    bl = 'T' if b else 'F'
    p = v / total_ve
    print(f"P(B={bl} | j=T, m=T) = {p:.4f}  ({p*100:.2f}%)")

# ── Compare ────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("COMPARISON: ENUMERATION vs VARIABLE ELIMINATION")
print("=" * 55)
for b in [True, False]:
    bl = 'T' if b else 'F'
    e_ans = unnorm_enum[b] / total_enum
    v_ans = unnorm_ve[b] / total_ve
    match = "✅" if abs(e_ans - v_ans) < 1e-6 else "❌"
    print(f"B={bl}: Enum={e_ans:.6f}  VE={v_ans:.6f}  {match}")
```

---

## 5. Python — Variable Elimination Demo

> [← §4](#4-python--full-posterior-pbjm) · [🔝 Top](#-table-of-contents) · [Next §6 →](#6-self-test-qa)

```python
# ============================================================
# VARIABLE ELIMINATION — Operations savings visualiser
# CSL7610 AI · IIT Jodhpur
# ============================================================

def enum_ops(n_hidden):
    """Enumeration: 2^n worlds, each ~n multiplications."""
    return (2**n_hidden) * n_hidden

def ve_ops(n_hidden, avg_parents=2):
    """VE approximation: n × 2^avg_parents × 2."""
    return n_hidden * (2**avg_parents) * 2

print(f"{'Nodes':>8} | {'Enumeration':>15} | {'VE (approx)':>12} | {'Savings':>8}")
print("-" * 52)
for n in [2, 5, 10, 15, 20, 25, 30]:
    e_ops = enum_ops(n)
    v_ops = ve_ops(n)
    saving = (1 - v_ops/e_ops) * 100
    e_str = f"{e_ops:,}" if e_ops < 1_000_000_000 else f"{e_ops:.2e}"
    print(f"{n:>8} | {e_str:>15} | {v_ops:>12} | {saving:>7.2f}%")

# ── Factor reuse illustration ─────────────────────────────────
print("\n\n--- WHY FACTOR REUSE HELPS ---")
print()
print("Enumeration recomputes P(j|a)×P(m|a) for EACH (a,e) combination:")
for b_label in ['B=T', 'B=F']:
    print(f"  {b_label}: 4 worlds × compute 0.63 or 0.0005 each time")
print("  Total P(j|a)×P(m|a) computations = 8")
print()
print("VE computes P(j|a)×P(m|a) ONCE per a value:")
print("  a=T: 0.90 × 0.70 = 0.63    [computed ONCE, stored]")
print("  a=F: 0.05 × 0.01 = 0.0005  [computed ONCE, stored]")
print("  Total P(j|a)×P(m|a) computations = 2")
print(f"  Saved: 8 - 2 = 6 multiplications from this shortcut alone!")
```

---

## 6. Self-Test Q&A

> [← §5](#5-python--variable-elimination-demo) · [🔝 Top](#-table-of-contents)

```
Q1: What is α and what does it do?
A:  α = 1/P(e) = normalisation constant.
    It scales unnormalised joint probabilities so they sum to 1.
    α = 1 / (P(X=T,e) + P(X=F,e))

Q2: Why is α the same for P(x=T|e) and P(x=F|e)?
A:  Because P(e) — the denominator — is the same for both.
    Both probabilities are divided by the same total.

Q3: What are the three variable types in BN inference?
A:  X = query (want), e = evidence (know), Y = hidden (sum over).

Q4: What is the master inference formula?
A:  P(X|e) = α × Σ P(X,e,y)  where α = 1/Σ_X P(X,e)
                  y

Q5: What makes Variable Elimination faster than Enumeration?
A:  VE computes each inner sum (factor) ONCE and saves it.
    Enumeration recomputes the same inner sums repeatedly.
    Savings: 56% for 5 nodes, ~100% for 30 nodes.

Q6: What is a "factor" in Variable Elimination?
A:  f(b,e) = Σ P(a|b,e)×P(j|a)×P(m|a)
              a
    A pre-computed, saved intermediate sum.
    Computed once per (b,e) combo → reused for BOTH B=T and B=F.

Q7: What are the Two Golden Rules of VE?
A:  Rule 1: When summing over 'a', pull out terms not containing 'a'.
    Rule 2: When summing over 'e', pull out terms not containing 'e'.

Q8: Why does P(Burglary|j,m) = 28.4% even though both called?
A:  Prior P(B) = 0.001 is very rare.
    Evidence gives a 284× boost, but 0.001 × 284 = 0.284 = 28.4%.
    Rare events stay rare — always multiply by base rate!

Q9: What's the difference between Enumeration and VE accuracy?
A:  Both give EXACT answers. VE is smarter, not less accurate.

Q10: When to use Exact vs Approximate inference?
A:  < 20 nodes → Exact (VE or Enumeration).
    ≥ 20 nodes → Approximate (Likelihood Weighting or Gibbs).

Q11: Why does P(b) always get pulled outside all sums first?
A:  P(b) contains no 'a' and no 'e' → it is constant to BOTH sums.
    Pulling it out avoids repeating the 0.001 or 0.999 factor
    inside every single world computation.

Q12: What does P(¬x|e) = 1 - P(x|e) always hold — even after α?
A:  Yes! The complement rule holds for all proper probability distributions.
    After normalisation P(x=T|e) + P(x=F|e) = 1 by definition.
    So P(x=F|e) = 1 - P(x=T|e) — always a valid shortcut.
```

---

> **Navigation:** [📋 INDEX](./bn_inference_index.md) | [← THEORY](./bn_inference_theory.md) | [← NUMERICALS](./bn_inference_numericals.md) | 💻 **PRACTICE** *(you are here)*

> **Source:** Book: Norvig AI · AI 

[🔝 Back to Top](#-bayesian-network-inference--practice)
