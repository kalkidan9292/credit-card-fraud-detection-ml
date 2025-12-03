# Credit Card Fraud Detection with Logistic Regression

> If every dataset is a puzzle, this project is about finding the first piece in one of the hardest puzzles: rare fraud events hidden inside massive transaction data.

## 📌 Project Overview

This project is an end-to-end implementation of a **Credit Card Fraud Detection** system using **Machine Learning in Python**.  
The goal is to build a model that predicts whether a credit card transaction is:

- `0` → Normal  
- `1` → Fraudulent  

The focus of this project is not just building a model, but **handling extreme class imbalance** and designing a workflow that could realistically be used in a production setting.

---

## 🧠 Key Objectives

- Load and explore a real-world credit card transaction dataset (Kaggle).
- Understand and visualize the **severe class imbalance** problem.
- Apply **downsampling** to create a balanced training dataset.
- Train a **Logistic Regression** classifier for fraud detection.
- Evaluate the model using accuracy and other relevant metrics.
- Document the full process in a clear, reproducible way.

---

## 🗂 Project Structure

```text
credit-card-fraud-detection-ml/
│
├── data/
│   ├── creditcard.csv              # Original dataset (tracked with Git LFS)
│   └── README.md                   # Dataset description + download instructions
│
├── notebooks/
│   ├── credit_card_fraud_detection.ipynb   # Full EDA + modeling walkthrough
│   └── credit_card_fraud_detection.py      # Script version of the workflow
│
├── Report/
│   ├── model_performance.md        # Final evaluation report
│   │
│   ├── 01_dataset_head_and_info.png
│   ├── 02_imports_and_dataset_preview.png
│   ├── 03_dataset_info_overview.png
│   ├── 04_missing_values_check.png
│   ├── 05_class_imbalance_analysis.png
│   ├── 06_amount_statistics_legit_vs_fraud.png
│   ├── 07_classwise_mean_and_undersampling_process.png
│   ├── 08_balanced_dataset_overview_and_feature_target_split.png
│   ├── 09_feature_matrix_and_target_vector_preview.png
│   ├── 10_train_test_split_and_model_training.png
│   ├── 11_model_evaluation_confusion_matrix_classification_report.png
│   └── 12_test_accuracy_score.png
│
│
├── .gitattributes                  # Git LFS tracking for large files
├── .gitignore                      # Ignored files
├── requirements.txt                # Project dependencies
└── README.md                       # Main project documentation
