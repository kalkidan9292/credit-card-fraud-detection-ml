# -*- coding: utf-8 -*-
"""
Credit Card Fraud Detection

End-to-end ML pipeline:
- Load & explore data
- Handle class imbalance with undersampling
- Train/Test split
- Feature scaling
- Logistic Regression model
- Evaluation (accuracy, confusion matrix, classification report)
"""

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

# ==========================
# 1. Load the dataset
# ==========================
credit_card_data = pd.read_csv(
    r"C:\Users\kalki\Downloads\archive (2)\creditcard.csv"
)

# Peek at the data
print("First 5 rows:")
print(credit_card_data.head())

print("\nDataset info:")
credit_card_data.info()

print("\nMissing values per column:")
print(credit_card_data.isnull().sum())

# Class distribution
print("\nClass distribution (0 = legit, 1 = fraud):")
print(credit_card_data['Class'].value_counts())

# ==========================
# 2. Basic exploratory stats
# ==========================
legit = credit_card_data[credit_card_data.Class == 0]
fraud = credit_card_data[credit_card_data.Class == 1]

print("\nShape of legit transactions:", legit.shape)
print("Shape of fraudulent transactions:", fraud.shape)

print("\nAmount statistics for legit transactions:")
print(legit['Amount'].describe())

print("\nAmount statistics for fraudulent transactions:")
print(fraud['Amount'].describe())

print("\nMean values grouped by Class:")
print(credit_card_data.groupby('Class').mean())

# ==========================
# 3. Handle class imbalance (undersampling)
# ==========================
# Number of fraudulent transactions
num_fraud = fraud.shape[0]
print("\nNumber of fraudulent transactions:", num_fraud)

# Sample legit transactions to match the number of fraud transactions
legit_sample = legit.sample(n=num_fraud, random_state=42)

# Concatenate the samples to form a new balanced dataset
new_dataset = pd.concat([legit_sample, fraud], axis=0)

print("\nNew dataset class distribution:")
print(new_dataset['Class'].value_counts())

print("\nNew dataset mean values grouped by Class:")
print(new_dataset.groupby('Class').mean())

# ==========================
# 4. Split into features & target
# ==========================
X = new_dataset.drop(columns='Class', axis=1)
Y = new_dataset['Class']

print("\nFeature matrix shape:", X.shape)
print("Target vector shape:", Y.shape)

# Train/Test split (stratified to keep balance in both sets)
x_train, x_test, y_train, y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    stratify=Y,
    random_state=2
)

print("\nTrain feature shape:", x_train.shape)
print("Test feature shape:", x_test.shape)

# ==========================
# 5. Feature scaling
# ==========================
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

# ==========================
# 6. Model training (Logistic Regression)
# ==========================
model = LogisticRegression(
    max_iter=2000,
    solver='liblinear'
)

model.fit(x_train_scaled, y_train)

# ==========================
# 7. Predictions & Evaluation
# ==========================
y_train_pred = model.predict(x_train_scaled)
y_test_pred = model.predict(x_test_scaled)

train_accuracy = accuracy_score(y_train, y_train_pred)
test_accuracy = accuracy_score(y_test, y_test_pred)

print("\nTraining Accuracy:", train_accuracy)
print("Test Accuracy:", test_accuracy)

print("\nConfusion Matrix (Test Data):")
print(confusion_matrix(y_test, y_test_pred))

print("\nClassification Report (Test Data):")
print(classification_report(y_test, y_test_pred))
