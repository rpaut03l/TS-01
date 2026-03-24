# 🤖 Artificial Intelligence — Complete Study Guide (ELI5 Edition)

[![AI](https://img.shields.io/badge/Subject-Artificial%20Intelligence-blue)]()
[![Topics](https://img.shields.io/badge/Topics-21-green)]()
[![Lines](https://img.shields.io/badge/Lines-9500%2B-orange)]()
[![Style](https://img.shields.io/badge/Style-ELI5%20(Explain%20Like%20I'm%205)-purple)]()

> **"Can machines think?"** — Alan Turing, 1950
>
> Imagine you're teaching a robot to be smart like a human. This entire folder is about HOW we make that happen — step by step, topic by topic!


---

## 📚 Course Overview

This repository covers the **complete AI syllabus** as taught by **Prof. Romi (RB-M)** and **Prof. Shilpa (SD-M)**.

**What makes this special:**
- 🍼 Every concept explained like you're 5 years old (ELI5) with stories and analogies
- 🧮 Every number, formula, and trace shown step-by-step with full arithmetic
- 📝 Exam-focused: common mistakes, tips, and worked problems for every topic
- 🔗 All reference links, slides, and recordings organized in one place

---

## 🧭 Syllabus → Folder Mapping

### 🔍 Search (Topics 01-05) — Quiz 1 Heavy!

| # | Syllabus Topic | Folder | Key Concepts |
|---|---|---|---|
| 01 | Uninformed Search Strategies | [`01_Search_Uninformed/`](./01_Search_Uninformed/) | BFS (Queue), DFS (Stack), UCS, IDS |
| 02 | Greedy Best-First & A* Search | [`02_Search_Informed_Greedy_Astar/`](./02_Search_Informed_Greedy_Astar/) | Heuristics, f=g+h, Admissibility |
| 03 | Memory-Bounded Heuristic Search | [`03_Search_Memory_Bounded_Heuristic/`](./03_Search_Memory_Bounded_Heuristic/) | IDA*, RBFS, SMA* |
| 04 | Local & Evolutionary Searches | [`04_Search_Local_and_Evolutionary/`](./04_Search_Local_and_Evolutionary/) | Hill Climbing, Simulated Annealing, GA |
| 05 | And-Or Search | [`05_Search_And_Or/`](./05_Search_And_Or/) | Nondeterministic, Conditional Plans |

### 🧩 Constraint Satisfaction (Topics 06-07) — Quiz 1 + Assignment!

| # | Syllabus Topic | Folder | Key Concepts |
|---|---|---|---|
| 06 | CSP — Backtracking Search | [`06_CSP_Backtracking/`](./06_CSP_Backtracking/) | Backtracking, AC-3, MRV, LCV |
| 07 | CSP — Local Search | [`07_CSP_Local_Search/`](./07_CSP_Local_Search/) | Min-Conflicts |

### ♟️ Adversarial Search (Topics 08-10) — Quiz 1!

| # | Syllabus Topic | Folder | Key Concepts |
|---|---|---|---|
| 08 | Minimax Algorithm | [`08_Adversarial_Search_Minimax/`](./08_Adversarial_Search_Minimax/) | Game Trees, Minimax, Eval Functions |
| 09 | Alpha-Beta Pruning | [`09_Alpha_Beta_Pruning/`](./09_Alpha_Beta_Pruning/) | α-β Pruning, Move Ordering |
| 10 | Expectimax Search | [`10_Expectimax_Search/`](./10_Expectimax_Search/) | Chance Nodes, Weighted Average |

### 📐 Knowledge & Reasoning (Topics 11-13) — Quiz 2 & Major!

| # | Syllabus Topic | Folder | Key Concepts |
|---|---|---|---|
| 11 | Propositional Logic & Reasoning | [`11_Propositional_Logic/`](./11_Propositional_Logic/) | Truth Tables, Modus Ponens, Resolution |
| 12 | FOL — Syntax & Semantics | [`12_FOL_Syntax_Semantics/`](./12_FOL_Syntax_Semantics/) | Predicates, Functions, ∀, ∃ |
| 13 | FOL — Inference & Unification | [`13_FOL_Inference_Unification/`](./13_FOL_Inference_Unification/) | Unification, Backward Chaining, Resolution |

### 🗺️ Planning (Topics 14-16) — Major!

| # | Syllabus Topic | Folder | Key Concepts |
|---|---|---|---|
| 14 | Situation Calculus | [`14_Planning_Situation_Calculus/`](./14_Planning_Situation_Calculus/) | Situations, Fluents, Frame Problem |
| 15 | STRIPS & Sub-goals | [`15_Planning_STRIPS_Subgoal/`](./15_Planning_STRIPS_Subgoal/) | STRIPS, Sussman Anomaly |
| 16 | Partial Order Planning | [`16_Planning_Partial_Order/`](./16_Planning_Partial_Order/) | POP, Threats, Promotion/Demotion |

### 🕸️ Probabilistic Reasoning (Topics 17-18) — Quiz 2 & Major!

| # | Syllabus Topic | Folder | Key Concepts |
|---|---|---|---|
| 17 | Bayesian Networks | [`17_Bayesian_Network/`](./17_Bayesian_Network/) | BNs, CPTs, d-Separation, Inference |
| 18 | Causality & Probabilistic Reasoning | [`18_Causality_Probabilistic_Reasoning/`](./18_Causality_Probabilistic_Reasoning/) | Causality, Simpson's Paradox, do() |

### 🎮 Reinforcement Learning (Topics 19-21) — Major!

| # | Syllabus Topic | Folder | Key Concepts |
|---|---|---|---|
| 19 | MDP & Policy | [`19_RL_MDP_Policy/`](./19_RL_MDP_Policy/) | MDP, V(s), γ, Bellman Equation |
| 20 | Q-Learning, Passive & Active RL | [`20_RL_Q_Learning_Passive_Active/`](./20_RL_Q_Learning_Passive_Active/) | TD Learning, Q-Learning, ε-Greedy |
| 21 | Policy Search | [`21_RL_Policy_Search/`](./21_RL_Policy_Search/) | REINFORCE, Actor-Critic |

### 📖 Reference

| File | Contents |
|---|---|
| [`Study_Materials.md`](./Study_Materials.md) | All slides, recordings, YouTube lectures, papers, textbook chapter mapping |


---

## 🍼 How to Use This Repo

1. **Start from Topic 01** and go in order — each builds on the previous
2. **Read the 🍼 ELI5 section first** — understand the BIG PICTURE before details
3. **Follow the 🧮 traces** — every number is computed step by step
4. **Check the ⚠️ Exam Tips** — know what mistakes to avoid
5. **Use [Study_Materials.md](./Study_Materials.md)** for video lectures if a topic is still unclear

> 💡 Each README has a difficulty meter: 🟢 Easy → 🟡 Medium → 🔴 Hard

---

*For Learning AI — one concept at a time!*
