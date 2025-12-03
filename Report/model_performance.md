Model Performance Report — Credit Card Fraud Detection
———————————————————————————
1. Dataset Overview
———————————————————————————

The dataset contains 284,807 transactions and 31 features.
Only 492 rows represent fraudulent activity (0.17%), resulting in a highly imbalanced classification problem.

Referenced files:
credit-card-fraud-detection-ml/Report/01_dataset_head_and_info.png
credit-card-fraud-detection-ml/Report/02_imports_and_dataset_preview.png
credit-card-fraud-detection-ml/Report/03_dataset_info_overview.png

———————————————————————————
2. Data Quality Assessment
———————————————————————————

A complete missing-value check showed 0 missing entries across all features.
No cleaning, dropping, or imputation was required.

Referenced file:
credit-card-fraud-detection-ml/Report/04_missing_values_check.png

———————————————————————————
3. Class Imbalance Analysis
———————————————————————————

The dataset is dominated by legitimate transactions.
Fraud cases occur in less than 0.2% of all rows — a scale that can severely distort training if not corrected.

Referenced file:
credit-card-fraud-detection-ml/Report/05_class_imbalance_analysis.png

———————————————————————————
4. Handling Imbalance — Under-Sampling
———————————————————————————

To build a balanced training environment, legitimate transactions were under-sampled to match the number of fraud cases (492).
The resulting dataset contains 984 rows — equal parts legit and fraud.

This section includes:
• Legit vs. Fraud amount statistics
• Class-wise mean comparison
• Undersampling procedure
• Final balanced dataset preview

Referenced files:
credit-card-fraud-detection-ml/Report/06_amount_statistics_legit_vs_fraud.png
credit-card-fraud-detection-ml/Report/07_classwise_mean_and_undersampling_process.png
credit-card-fraud-detection-ml/Report/08_balanced_dataset_overview_and_feature_target_split.png

———————————————————————————
5. Feature Matrix & Target Vector
———————————————————————————

The balanced dataset was divided into:
• X → 30 numerical features
• Y → Class label (0 = legit, 1 = fraud)

Referenced file:
credit-card-fraud-detection-ml/Report/09_feature_matrix_and_target_vector_preview.png

———————————————————————————
6. Train-Test Split & Model Training
———————————————————————————

Data was split using an 80/20 ratio, with stratified sampling to maintain balance.
A StandardScaler was applied to improve model convergence.
A Logistic Regression model (max_iter=2000, solver='liblinear') was used.

Referenced file:
credit-card-fraud-detection-ml/Report/10_train_test_split_and_model_training.png

———————————————————————————
7. Model Evaluation
———————————————————————————

Training Accuracy: ~0.955
Testing Accuracy: ~0.928

Confusion matrix and classification report show consistent performance across both classes, indicating balanced learning after under-sampling.

Referenced file:
credit-card-fraud-detection-ml/Report/11_model_evaluation_confusion_matrix_classification_report.png

———————————————————————————
8. Final Test Accuracy
———————————————————————————

The final test accuracy was recorded as 0.9289, confirming that the model generalizes well on unseen data.

Referenced file:
credit-card-fraud-detection-ml/Report/12_test_accuracy_score.png
