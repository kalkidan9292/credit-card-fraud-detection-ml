# Model Performance Report — Credit Card Fraud Detection

## 1. Dataset Overview
The dataset contains 284,807 transactions and 31 features.  
Only 492 records are labeled as fraud (0.17%).

### Dataset Head & Info
![Dataset Head and Info](01_dataset_head_and_info.png)

### Dataset Imports & Preview
![Imports and Dataset Preview](02_imports_and_dataset_preview.png)

### Dataset Info Overview
![Dataset Info Overview](03_dataset_info_overview.png)


## 2. Data Quality Check
The dataset has **no missing values**.

### Missing Values Check
![Missing Values Check](04_missing_values_check.png)


## 3. Class Imbalance Analysis
The dataset is highly imbalanced with a dominant legitimate class.

### Class Distribution
![Class Imbalance Analysis](05_class_imbalance_analysis.png)


## 4. Under-Sampling Process
To create a balanced dataset, legitimate transactions were under-sampled from 284,315 → 492.

### Amount Statistics (Legit vs Fraud)
![Amount Stats](06_amount_statistics_legit_vs_fraud.png)

### Class-wise Mean Comparison & Under-Sampling
![Under-Sampling Process](07_classwise_mean_and_undersampling_process.png)

### Balanced Dataset Overview + Feature/Target Split
![Balanced Dataset](08_balanced_dataset_overview_and_feature_target_split.png)


## 5. Feature and Target Preparation
Thirty numerical features were used as X.  
The **Class** column served as Y.

### Feature Matrix & Target Vector
![Feature Matrix and Target Vector](09_feature_matrix_and_target_vector_preview.png)


## 6. Model Training
Training config:
- StandardScaler normalization  
- Train/Test Split (80/20, stratified)  
- Logistic Regression (max_iter=2000)

### Train/Test Split + Scaling + Training
![Train Test Split and Model Training](10_train_test_split_and_model_training.png)


## 7. Model Evaluation
Training Accuracy: **0.9555**  
Testing Accuracy: **0.9289**

### Confusion Matrix + Classification Report
![Evaluation Results](11_model_evaluation_confusion_matrix_classification_report.png)


## 8. Final Test Accuracy
Final accuracy on unseen data: **0.9289**

### Test Accuracy Score
![Test Accuracy Score](12_test_accuracy_score.png)
