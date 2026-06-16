# ❤️ Heart Disease Prediction & Analysis

**Independent Data Science Project**
*Hala Wael Hagag — Applied alongside IBM Data Science Professional Certificate*

---

## Overview

This project builds a machine learning pipeline to predict heart disease risk using real patient data from the **Cleveland Heart Disease Dataset** (UCI ML Repository). It was developed independently to apply and extend the skills gained during the IBM Data Science Professional Certificate.

## Dataset

| Attribute       | Detail                                      |
|----------------|---------------------------------------------|
| Source          | UCI Machine Learning Repository             |
| Samples         | 303 patients                                |
| Features        | 13 medical attributes                        |
| Target          | Binary: Heart Disease (1) / No Disease (0)  |

**Features include:** age, sex, chest pain type, resting blood pressure, cholesterol, fasting blood sugar, ECG results, max heart rate, exercise-induced angina, ST depression, ST slope, number of vessels, thalassemia.

## Project Workflow

1. **Data Loading** — fetched directly from OpenML/UCI
2. **Exploratory Data Analysis** — class distribution, age analysis, feature distributions
3. **Visualization** — correlation heatmap, categorical breakdowns, KDE plots
4. **Preprocessing** — missing value imputation, train/test split, feature scaling
5. **Model Training** — 5 classifiers with 5-fold cross-validation
6. **Evaluation** — confusion matrix, classification report, ROC/AUC curves
7. **Feature Importance** — Random Forest feature ranking

## Models Compared

- Logistic Regression
- Decision Tree
- **Random Forest** ← Best performer (~85% accuracy)
- Support Vector Machine (SVM)
- K-Nearest Neighbors (KNN)

## Key Findings

- **Thalassemia**, **chest pain type**, and **maximum heart rate** are the top predictors.
- Patients with heart disease show lower max heart rate and higher ST depression during exercise.
- Random Forest achieves ~85% test accuracy and the highest ROC-AUC across all models.

## How to Run

```bash
# Install dependencies
pip install pandas numpy matplotlib seaborn scikit-learn

# Open the notebook
jupyter notebook heart_disease_prediction.ipynb
```

## Skills Demonstrated

This project directly applies skills from the IBM Data Science Professional Certificate:

- ✅ Python (pandas, numpy)
- ✅ Data Visualization (matplotlib, seaborn)
- ✅ Machine Learning (scikit-learn)
- ✅ Model Evaluation (cross-validation, ROC/AUC, confusion matrix)
- ✅ Statistical Analysis & EDA

---

*Developed by Hala Wael Hagag as an independent project alongside the IBM Data Science Professional Certificate capstone (SpaceX Falcon 9 Landing Prediction).*
