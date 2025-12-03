# Model Performance Report — Credit Card Fraud Detection

## 1. Dataset Overview
The dataset contains 284,807 transactions and 31 features.  
Only 492 records are labeled as fraud (0.17%).

Assets:
Report/01_dataset_head_and_info.png  
Report/02_imports_and_dataset_preview.png  
Report/03_dataset_info_overview.png  


## 2. Data Quality Check
A full scan confirmed that the dataset has no missing values.

Asset:
Report/04_missing_values_check.png  


## 3. Class Imbalance Analysis
The dataset is highly imbalanced, with the majority of transactions being non-fraudulent.

Asset:
Report/05_class_imbalance_analysis.png  


## 4. Under-Sampling Process
The legitimate class was under-sampled to match the fraud class (492 vs 492).  
This created a balanced dataset of 984 rows.

Assets:
Report/06_amount_statistics_legit_vs_fraud.png  
Report/07_classwise_mean_and_undersampling_process.png  
Report/08_balanced_dataset_overview_and_feature_target_split.png  


## 5. Feature and Target Preparation
Thirty numerical features were used as input (X).  
The "Class" column served as the output label (Y).

Asset:
Report/09_feature_matrix_and_target_vector_preview.png  


## 6. Model Training
Training setup:
- StandardScaler for feature normalization  
- Train/Test split = 80/20 (stratified)  
- Logistic Regression (max_iter=2000)

Asset:
Report/10_train_test_split_and_model_training.png  


## 7. Model Evaluation
Training Accuracy: 0.9555  
Testing Accuracy: 0.9289  

Includes confusion matrix and classification report.

Asset:
Report/11_model_evaluation_confusion_matrix_classification_report.png  


## 8. Final Test Accuracy
Final accuracy on unseen data: 0.9289

Asset:
Report/12_test_accuracy_score.png  
