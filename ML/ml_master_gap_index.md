# 📑 ML Syllabus — MASTER GAP ANALYSIS & INDEX

### * Machine Learning · Pr. S Bhagat.

> 🔗 **Repo:** [github.com/rpaut03l/TS-01](https://github.com/rpaut03l/TS-01) / [TS-01-Pvt](https://github.com/rpaut03l/TS-01-Pvt) · ML Track

---

## 🔍 SYLLABUS vs REPO — STATUS MAP

```
FRACTAL I: SUPERVISED LEARNING (14 Lectures)
═══════════════════════════════════════════════════════════════════
 Topic                           Lectures  Status     Folder
─────────────────────────────────────────────────────────────────
 Introduction & Foundations         7       ✅ FULL    ML/Foundations/
   ├─ Definitions & Paradigms                          
   ├─ Datasets for ML                                  
   ├─ Data Normalization                               
   ├─ Hypothesis Evaluation                            
   ├─ VC-Dimensions & Distribution                     
   ├─ Bias-Variance Tradeoff                           
   └─ Regression (Linear)                   ✅ FULL    ML/Regression/
                                                       (SLR+MLR+Logistic+Ridge+Lasso trio)
                                                       
 Bayes Decision Theory              5       🟡 Partial ML/Bayesian-Decision-Theory/
   ├─ Bayes decision rule                              (guide + practice; needs
   ├─ Min error rate classification                     numerical trio file)
   └─ Normal density & discriminant                    
                                                       
 Parameter Estimation               2       ✅ FULL    ML/Parameter-Estimations-Guide/
   ├─ MLE                                              (theory + practice +
   └─ Bayesian Parameter Estimation                     numerical markdown trio)

FRACTAL II: UNSUPERVISED LEARNING (14 Lectures)
═══════════════════════════════════════════════════════════════════
 Discriminative Methods             6       Partial
   ├─ Distance-based methods (K-NN)          🟡 Partial ML/K-Nearest-Neighbors_(K-NN)/
   ├─ Linear Discriminant Functions          🟡 Partial ML/LDA/
   ├─ Decision Tree                          🟡 Partial ML/Decision-Tree/
   ├─ Random Forest                          ✅ FULL    ML/Random-Forest/
   │                                                    (standalone trio + Ch07 ensemble)
   └─ Boosting                               ✅ EXISTS  ML/Ch07_Ensemble_Learning/
                                                        ML/Ensemble_Boosting_AdaBoost/
                                                       
 Feature Selection & Dim Reduction  4       ✅ FULL    ML/Feature-Selection-DimRed/
   ├─ PCA                                              (ml_pca_ica_fs_*.md trio)
   ├─ LDA (for dim reduction)                          
   ├─ ICA                                             
   ├─ SFFS                                            
   └─ SBFS                                            
                                                       
 Clustering                         4       ✅ FULL    ML/Clustering/
   ├─ K-Means                                          (ml_kmeans_gmm_em_*.md trio)
   ├─ Gaussian Mixture Models                          
   └─ EM Algorithm                                     

FRACTAL III: KERNELS & NEURAL NETWORKS (14 Lectures)
═══════════════════════════════════════════════════════════════════
 Kernel Machines                    6       ✅ FULL    ML/SVM-Kernels/
   ├─ Kernel Tricks                                    (ml_svm_kernels_*.md trio)
   ├─ SVMs (primal & dual)                            
   ├─ K-SVR                                           
   └─ K-PCA                                           
                                                       
 Artificial Neural Networks         4       ✅ FULL    ML/Neural-Networks/
   ├─ MLP                                              (ml_nn_mlp_bp_*.md trio)
   ├─ Backpropagation                                  
   └─ RBF-Net                                         
                                                       
 Deep Learning Foundations          4       ✅ FULL    ML/Deep-Learning/
   ├─ DNN                                              (ml_dl_cnn_ae_*.md trio)
   ├─ CNN                                             
   └─ Autoencoders                                     
```

---

## 📂 Phase-1 additions (this PR)

| Folder | New files | Status |
|---|---|---|
| [ML/Parameter-Estimations-Guide/](Parameter-Estimations-Guide/) | [theory](Parameter-Estimations-Guide/ml_parameter_estimation_theory.md) · [numerical](Parameter-Estimations-Guide/ml_parameter_estimation_numerical.md) · [practice](Parameter-Estimations-Guide/ml_parameter_estimation_practice.md) | ✅ |
| [ML/Random-Forest/](Random-Forest/) | [theory](Random-Forest/ml_random_forest_theory.md) · [numerical](Random-Forest/ml_random_forest_numerical.md) · [practice](Random-Forest/ml_random_forest_practice.md) | ✅ |
| [ML/Regression/](Regression/) | [theory](Regression/ml_regression_theory.md) · [numerical](Regression/ml_regression_numerical.md) · [practice](Regression/ml_regression_practice.md) | ✅ |

> Legacy files (`simple_linear_regression_pe_*.md` in `ML/Regression/` and the PDFs in `ML/Parameter-Estimations-Guide/` and `ML/Random-Forest/`) remain untouched and continue to work.

---

## 🔭 Remaining gaps (future phases)

- **ML/K-Nearest-Neighbors_(K-NN)/** — needs `ml_knn_theory.md`, `ml_knn_numerical.md`
- **ML/LDA/** — needs `ml_lda_practice.md`, `ml_lda_numerical.md`
- **ML/Decision-Tree/** — needs `ml_decision_tree_practice.md`, `ml_decision_tree_numerical.md`
- **ML/Bayesian-Decision-Theory/** — needs `ml_bdt_theory.md`, `ml_bdt_numerical.md`

---

*AI · ML · github.com/rpaut03l/TS-01*
