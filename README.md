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
.
├── data/
│   └── README.md              # instructions on how to download the dataset
├── notebooks/
│   └── 01_fraud_detection_eda_model.ipynb
├── src/
│   ├── data_preprocessing.py
│   ├── model_training.py
│   └── evaluation.py
├── reports/
│   └── model_performance.md
├── images/
│   ├── class_distribution.png
│   ├── confusion_matrix.png
│   └── roc_curve.png
├── requirements.txt
├── .gitignore
└── README.md
