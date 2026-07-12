<div align="center">

## Hey there! 📚 Welcome to TS-01

**TS 01 · Study Notes · AI/ML**

*Every concept explained so simply. Every number computed step-by-step.*

![Singapore](https://img.shields.io/badge/Singapore-UTC%2B08%3A00-blue?style=flat-square) ![Currently Studying](https://img.shields.io/badge/🎯-Currently%20Studying-brightgreen?style=flat-square)

</div>

---

### 🏆 Featured Projects — Applied Portfolio

Beyond coursework: end-to-end applied work spanning cybersecurity, deep
learning, and MLOps — built, demoed, tested, and documented.

<table>
<tr>
<td width="50%" valign="top">

**🔓 [Reentrancy Attack — Smart Contract Security](https://github.com/rpaut03l/ts_02_safevault-reentrancy-demo)**

![Solidity](https://img.shields.io/badge/Solidity-363636?style=flat-square&logo=solidity&logoColor=white) ![Foundry](https://img.shields.io/badge/Foundry-000000?style=flat-square) ![MetaMask](https://img.shields.io/badge/MetaMask-F6851B?style=flat-square&logo=metamask&logoColor=white)

Live exploit + defense on Ethereum smart contracts — drains an 11 ETH vault
via a classic reentrancy bug, then blocks the identical attack with
Checks-Effects-Interactions + a `nonReentrant` guard. Built with Foundry,
Anvil, and a Next.js/MetaMask UI; proven with Forge tests exposing the full
recursive call trace. *CSL6010 Cyber Security · Group 6*

**🛡️ [PoisonedRAG + RAG-Shield — RAG Poisoning Defense](https://github.com/rpaut03l/poisonedrag-ragshield-group6-iitj)**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white) ![FAISS](https://img.shields.io/badge/FAISS-4285F4?style=flat-square)

Reproduces a USENIX Security 2025 RAG-poisoning attack (~90% attack success
from just 5 malicious documents), then builds **RAG-Shield** — a 3-ring
defense-in-depth pipeline (ingest screening, retrieval trust scoring,
cross-LLM consensus across Claude/Mistral/LLaMA) that drives attack success
down to ~13% while preserving normal-query accuracy. *CSL6010 · Group 6*

</td>
<td width="50%" valign="top">

**🎨 [Mode Collapse in GANs — Presentation Kit](https://github.com/rpaut03l/gan-mode-collapse-demo-grp-1-iit-j/tree/main)**

![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white) ![HTML5](https://img.shields.io/badge/Interactive_Demo-E34F26?style=flat-square&logo=html5&logoColor=white)

Solo-built deep-learning presentation kit: an interactive browser-based live
demo that simulates GAN mode collapse in real time (ten target classes
collapsing to one, live mode-coverage tracking, one-click fix reveal), a
presenter runbook, a Q&A guide, and full study notes running theory →
numericals → runnable PyTorch (simple GAN + DCGAN).
📦 [Repo](https://github.com/rpaut03l/gan-mode-collapse-demo-grp-1-iit-j/tree/main) · 🎥 [Live Demo](https://rpaut03l.github.io/gan-mode-collapse-demo-grp-1-iit-j/demo/mode_collapse_live_demo.html) · *Deep Learning · Group 1*

**🎭 [MLOps Emotion Pipeline — DistilBERT CI/CD](https://github.com/rpaut03l/mlops-emotion-pipeline-group-12-iit-j)**

![HuggingFace](https://img.shields.io/badge/🤗_HuggingFace-FFD21E?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![GitHubActions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white) ![W&B](https://img.shields.io/badge/Weights_%26_Biases-FFBE00?style=flat-square&logo=weightsandbiases&logoColor=black)

End-to-end MLOps: fine-tunes `distilbert-base-uncased` for 6-class emotion
classification (Kaggle GPU training + W&B experiment tracking), publishes to
a public Hugging Face model repo, packages inference in Docker, and ships via
GitHub Actions CI/CD with a branch-protected, peer-reviewed PR workflow.
*MLOps · Group 12*

</td>
</tr>
</table>

**🎓 More Deep Learning Demos — Batchmates' Work**

Interactive live demos from fellow M.Tech AI batchmates, worth a look:

| Demo | Topic | Live Link |
|---|---|---|
| 🎨 Watching a GAN Collapse | Generative Adversarial Networks — mode collapse, live | [rpaut03l.github.io/gan-mode-collapse-demo-grp-1-iit-j](https://rpaut03l.github.io/gan-mode-collapse-demo-grp-1-iit-j/demo/mode_collapse_live_demo.html) |
| 🎬 RBM Movie Recommender | Restricted Boltzmann Machines for recommendation | [teal-frangipane-2c6927.netlify.app](https://teal-frangipane-2c6927.netlify.app/) |
| 🧠 DBN Visualization | Deep Belief Networks, visualized | [nikhilsaini-iitj.github.io/dbn-visualization](https://nikhilsaini-iitj.github.io/dbn-visualization/) |
| 🔬 Interactive Demo | *(topic not specified — link as shared)* | [scarlet-hatti-38.tiiny.site](https://scarlet-hatti-38.tiiny.site/) |
| 🔗 Contrastive Learning (Group 21) | Self-supervised contrastive learning | [g25ait2134-tech.github.io/DL_Contrastive_Learning_Group21](https://g25ait2134-tech.github.io/DL_Contrastive_Learning_Group21/) |
| ♻️ Transfer Learning — Feature Reuse | Transfer learning & feature reuse | [sureshbabugandla.github.io/transfer-learning-feature-reuse](https://sureshbabugandla.github.io/transfer-learning-feature-reuse/#overview) |

---

### 🎒 What This Repo Contains

| | Subject | Description |
|---|---|---|
| 🤖 **AI** | [Artificial Intelligence](./AI/) | Search, Logic, Planning, Bayesian Networks, Reinforcement Learning — 21 topics, 9800+ lines of ELI5 notes |
| 🧠 **ML** | [Machine Learning](./ML/) | Ensemble Methods, Boosting, AdaBoost, Gradient Descent, Regularization, model building |
| 🔢 **Maths** | [Mathematics for AI/ML](./Maths/) | Linear Algebra, Probability & Statistics, Optimization, Calculus foundations |
| 💻 **DSA&T** | [Data Structures & Techniques](./DSA%26T/) | Arrays, Trees, Graphs, Dynamic Programming, Sorting & Searching |
| 📈 **ODS** | [Optimization for Data Science](./ODS/) | Convex Optimization, Gradient Descent, Convergence Analysis, Constrained Optimization, Duality |

---

### ⚡ Focus Areas

| Area | Topics Covered |
|---|---|
| 🔍 **Search & Optimization** | BFS · DFS · A* · IDA* · Hill Climbing · Simulated Annealing · Genetic Algorithms |
| 🧩 **Constraint Satisfaction** | Backtracking · AC-3 · Forward Checking · MRV · LCV · Min-Conflicts |
| ♟️ **Game Playing** | Minimax · Alpha-Beta Pruning · Expectimax · Evaluation Functions |
| 📐 **Logic & Reasoning** | Propositional Logic · First-Order Logic · Unification · Resolution · Backward Chaining |
| 🗺️ **Planning** | Situation Calculus · STRIPS · Partial Order Planning · Frame Problem |
| 🕸️ **Probabilistic Models** | Bayesian Networks · CPTs · d-Separation · Causality · Simpson's Paradox · do-Calculus |
| 🎮 **Reinforcement Learning** | MDP · Bellman Equation · Value Iteration · Q-Learning · REINFORCE · Actor-Critic |
| 🧠 **ML Algorithms** | Ensemble Methods · AdaBoost · Gradient Boosting · Regression · Clustering · Deep Learning |
| 📈 **Optimization** | Convex Functions · Gradient Descent · SGD · Convergence Rates · Duality · KKT Conditions |

---

### 🌟 What Makes This Special

| | Feature | Details |
|---|---|---|
| 🍼 | **ELI5 Explanations** | Every concept starts with a story — ice cream shops for Queues, plate piles for Stacks, melting ice cream for Discount Factor γ |
| 🧮 | **Full Arithmetic Traces** | No hand-waving. Every f=g+h, every e^(ΔE/T), every P(B\|J,M) computed with every multiplication shown |
| ⚠️ | **Exam Trap Alerts** | 200+ common mistakes flagged — the ones professors LOVE to test and students ALWAYS get wrong |
| 📊 | **Worked Examples** | 100+ step-by-step traces: BFS/DFS on graphs, A* on Romania, AC-3 REVISE calls, Q-table updates |
| 🔗 | **Linked Resources** | Every topic maps to: class data (ts-01), best YouTube lecture, AIMA textbook chapter |

---

### 🗺️ AI — Complete Topic Navigator

<table>
<tr>
<td width="50%" valign="top">

**🔍 Search (Quiz 1)**

| # | Topic | Lines |
|---|---|---|
| 01 | [Uninformed Search (BFS, DFS, UCS, IDS)](./AI/01_Search_Uninformed/) | 1061 |
| 02 | [Informed Search (Greedy, A*)](./AI/02_Search_Informed_Greedy_Astar/) | 645 |
| 03 | [Memory-Bounded (IDA*, RBFS, SMA*)](./AI/03_Search_Memory_Bounded_Heuristic/) | 305 |
| 04 | [Local & Evolutionary Search](./AI/04_Search_Local_and_Evolutionary/) | 544 |
| 05 | [And-Or Search](./AI/05_Search_And_Or/) | 295 |

**🧩 CSP (Quiz 1 + Assignment)**

| # | Topic | Lines |
|---|---|---|
| 06 | [Backtracking, AC-3, MRV, LCV](./AI/06_CSP_Backtracking/) | 539 |
| 07 | [Min-Conflicts](./AI/07_CSP_Local_Search/) | 328 |

**♟️ Adversarial Search (Quiz 1)**

| # | Topic | Lines |
|---|---|---|
| 08 | [Minimax Algorithm](./AI/08_Adversarial_Search_Minimax/) | 329 |
| 09 | [Alpha-Beta Pruning](./AI/09_Alpha_Beta_Pruning/) | 332 |
| 10 | [Expectimax Search](./AI/10_Expectimax_Search/) | 407 |

</td>
<td width="50%" valign="top">

**📐 Knowledge & Reasoning (Quiz 2)**

| # | Topic | Lines |
|---|---|---|
| 11 | [Propositional Logic](./AI/11_Propositional_Logic/) | 435 |
| 12 | [FOL — Syntax & Semantics](./AI/12_FOL_Syntax_Semantics/) | 376 |
| 13 | [FOL — Inference & Unification](./AI/13_FOL_Inference_Unification/) | 622 |

**🗺️ Planning (Major)**

| # | Topic | Lines |
|---|---|---|
| 14 | [Situation Calculus](./AI/14_Planning_Situation_Calculus/) | 249 |
| 15 | [STRIPS & Sub-goals](./AI/15_Planning_STRIPS_Subgoal/) | 355 |
| 16 | [Partial Order Planning](./AI/16_Planning_Partial_Order/) | 229 |

**🕸️ Bayesian & Causality (Quiz 2 + Major)**

| # | Topic | Lines |
|---|---|---|
| 17 | [Bayesian Networks](./AI/17_Bayesian_Network/) | 443 |
| 18 | [Causality & Probabilistic Reasoning](./AI/18_Causality_Probabilistic_Reasoning/) | 238 |

**🎮 Reinforcement Learning (Major)**

| # | Topic | Lines |
|---|---|---|
| 19 | [MDP & Policy](./AI/19_RL_MDP_Policy/) | 624 |
| 20 | [Q-Learning, Passive & Active RL](./AI/20_RL_Q_Learning_Passive_Active/) | 442 |
| 21 | [Policy Search & REINFORCE](./AI/21_RL_Policy_Search/) | 538 |

</td>
</tr>
</table>

---

### 🔗 Continue the Journey — TS-02 (DLOps & MLOps)

TS-01 covers the *foundations* (AI, ML, Maths, DSA&T, ODS). The applied,
production-facing continuation — Deep Learning Operations and ML Operations —
lives in the sibling repo **[TS-02](https://github.com/rpaut03l/TS-02)**.

<table>
<tr>
<td width="50%" valign="top">

**🔥 [DLOps](https://github.com/rpaut03l/TS-02/tree/main/DLOps)**
*PyTorch → CNNs → tracking → distributed → deployment*

| # | Topic | Notebook |
|---|---|---|
| 01 | [Intro to PyTorch](https://github.com/rpaut03l/TS-02/blob/main/DLOps/DLOPS_01_Intro_PyTorch.md) — tensors, autograd, first nn | [.ipynb](https://github.com/rpaut03l/TS-02/blob/main/DLOps/notebooks/01_Intro_To_PyTorch/PyTorch_Tutorial.ipynb) |
| 02 | [Basics for DL](https://github.com/rpaut03l/TS-02/blob/main/DLOps/DLOPS_02_Basics_PyTorch_DL.md) — activations, losses, optimizers | [.ipynb](https://github.com/rpaut03l/TS-02/blob/main/DLOps/notebooks/02_Basics_of_Pytorch_for_DL/Basics_of_Pytorch_for_DL.ipynb) |
| 03 | [CNN + Feature Extraction](https://github.com/rpaut03l/TS-02/blob/main/DLOps/DLOPS_03_CNN_Feature_Extraction.md) — CIFAR/LeNet, RandomForest hybrid | [.ipynb](https://github.com/rpaut03l/TS-02/blob/main/DLOps/notebooks/03_CNN_Feature_Extraction/3_Classification_and_Feature_Extraction_using_CNN.ipynb) |
| 04 | [Datasets & DataLoaders](https://github.com/rpaut03l/TS-02/blob/main/DLOps/DLOPS_04_Datasets_DataLoaders.md) — transforms, augmentation | [.ipynb](https://github.com/rpaut03l/TS-02/blob/main/DLOps/notebooks/04_Datasets_and_DataLoaders/4_Datasets_and_DataLoaders.ipynb) |
| 05 | [Custom Datasets](https://github.com/rpaut03l/TS-02/blob/main/DLOps/DLOPS_05_Custom_Datasets_Training.md) — ImageFolder, TinyVGG | [.ipynb](https://github.com/rpaut03l/TS-02/blob/main/DLOps/notebooks/05_Custom_Datasets_Training/5_DLops_Custom_Datasets_and_DataLoaders_Teaching.ipynb) |
| 06 | [TensorBoard](https://github.com/rpaut03l/TS-02/blob/main/DLOps/DLOPS_06_TensorBoard.md) — SummaryWriter, PR curves, hparams | [.ipynb](https://github.com/rpaut03l/TS-02/blob/main/DLOps/notebooks/06_TensorBoard/06_DLops_TensorBoard_Experiment_Tracking.ipynb) |
| 07 | [W&B Sweeps (course)](https://github.com/rpaut03l/TS-02/blob/main/DLOps/DLOPS_07_WandB_Sweeps_Course.md) — init/log/sweep/agent | [.ipynb](https://github.com/rpaut03l/TS-02/blob/main/DLOps/notebooks/07_WandB_Sweeps_Course/07_DLops_Hyperparameter_Tuning_with_WandB_Sweeps.ipynb) |
| 08 | [W&B Sweeps (official)](https://github.com/rpaut03l/TS-02/blob/main/DLOps/DLOPS_08_WandB_Sweeps_Official.md) — sweep_config grammar | [.ipynb](https://github.com/rpaut03l/TS-02/blob/main/DLOps/notebooks/08_WandB_Sweeps_Official/13c_Organizing_Hyperparameter_Sweeps_in_PyTorch_with_WandB.ipynb) |
| 09 | [W&B Artifacts](https://github.com/rpaut03l/TS-02/blob/main/DLOps/DLOPS_09_WandB_Artifacts.md) — data + model versioning | [.ipynb](https://github.com/rpaut03l/TS-02/blob/main/DLOps/notebooks/09_WandB_Artifacts/14_Pipeline_Versioning_with_WandB_Artifacts.ipynb) |
| 10 | [Distributed Training](https://github.com/rpaut03l/TS-02/blob/main/DLOps/DLOPS_10_Distributed_Training.md) — DataParallel, model parallel | [18a](https://github.com/rpaut03l/TS-02/blob/main/DLOps/notebooks/10_Distributed_Training/18a_data_parallel_tutorial.ipynb) · [18b](https://github.com/rpaut03l/TS-02/blob/main/DLOps/notebooks/10_Distributed_Training/18b_parallelism_tutorial.ipynb) · [18c](https://github.com/rpaut03l/TS-02/blob/main/DLOps/notebooks/10_Distributed_Training/18c_model_parallel_tutorial.ipynb) |
| 11 | [TorchScript](https://github.com/rpaut03l/TS-02/blob/main/DLOps/DLOPS_11_TorchScript.md) — trace vs script | [.ipynb](https://github.com/rpaut03l/TS-02/blob/main/DLOps/notebooks/11_TorchScript/15_Intro_to_TorchScript_tutorial.ipynb) |
| 12 | [ONNX](https://github.com/rpaut03l/TS-02/blob/main/DLOps/DLOPS_12_ONNX.md) — export, checker, onnxruntime | [.ipynb](https://github.com/rpaut03l/TS-02/blob/main/DLOps/notebooks/12_ONNX/16a_intro_onnx.ipynb) |

📎 Start here → [DLOps Hub](https://github.com/rpaut03l/TS-02/blob/main/DLOps/DLOPS_EXAM_00_Hub.md) · [README](https://github.com/rpaut03l/TS-02/blob/main/DLOps/README.md) · [all notebooks](https://github.com/rpaut03l/TS-02/tree/main/DLOps/notebooks)

</td>
<td width="50%" valign="top">

**⚙️ [MLOps](https://github.com/rpaut03l/TS-02/tree/main/MLOps)**
*Data → pipelines → containers → orchestration → production*

| Area | Covers |
|---|---|
| Systems Concepts | ML system design, reproducibility, the "why" behind MLOps |
| Preprocessing & EDA | Data cleaning, feature pipelines, exploratory workflows |
| Git · Docker · K8s | Containerizing training/serving, versioned pipelines, orchestration |
| Experiment Tracking | Bridges directly into DLOps modules 06-09 (TensorBoard, W&B) |
| Deployment | Serving patterns that pair with DLOps modules 11-12 (TorchScript, ONNX) |

🔗 Related: [K8s MLOps pipeline repo](https://github.com/rpaut03l/rptl_gn_mlops/tree/mlops-pipeline) ·
[ML workflows blog](https://www.rohitpatel.in/2025/11/machine-learning-workflows-ml-models.html)

</td>
</tr>
</table>

> **How the three repos fit together:** TS-01 (theory/foundations) →
> TS-02/MLOps (systems & pipelines) → TS-02/DLOps
> — read in that order, or jump straight to whichever layer
> you need.

---

### 🛠️ Tech Stack

**📚 Study & Notes**

![Markdown](https://img.shields.io/badge/Markdown-000000?style=flat-square&logo=markdown&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white)
![LaTeX](https://img.shields.io/badge/LaTeX-008080?style=flat-square&logo=latex&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)

**🐍 AI / ML / RL**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)

**☁️ Cloud & Infra**

![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazonaws&logoColor=white)
![GCP](https://img.shields.io/badge/GCP-4285F4?style=flat-square&logo=googlecloud&logoColor=white)
![Azure](https://img.shields.io/badge/Azure-0078D4?style=flat-square&logo=microsoftazure&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

**🔧 MLOps / AIOps**

![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=flat-square&logo=mlflow&logoColor=white)
![Kubeflow](https://img.shields.io/badge/Kubeflow-326CE5?style=flat-square&logo=kubeflow&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)
![ArgoCD](https://img.shields.io/badge/ArgoCD-EF7B4D?style=flat-square&logo=argo&logoColor=white)

---

### 📖 Key References

| Resource | Type | Link |
|---|---|---|
| AIMA (Russell & Norvig) | 📕 [Textbook](https://aima.cs.berkeley.edu/contents.html) | [artint.info](https://artint.info/3e/html/ArtInt3e.html) |
| Stanford CS221 | 🎓 Lectures | [YouTube](https://www.youtube.com/playlist?list=PLoROMvodv4rO1NB9TD4iUZ3qghGEGtqNX) |
| MIT AI (Patrick Winston) | 🎓 Lectures | [YouTube](https://www.youtube.com/playlist?list=PLUl4u3cNGP63gFHB6xb-kVBiQHYe_4hSi) |
| IIT Delhi AI | 🎓 Lectures | [YouTube](https://www.youtube.com/playlist?list=PLp6ek2hDcoNB_YJCruBFjhF79f5ZHyBuz) |
| Turing — "Can Machines Think?" | 📄 Paper | [PDF](https://courses.cs.umbc.edu/471/papers/turing.pdf) |

---

<div align="center">

### ⭐ Star this repo if it helped you study!

*Built with ❤️ and ☕ by [rpaut03l](https://github.com/rpaut03l)*

**AI/ML Enthusiast · Singapore 🇸🇬**

</div>
