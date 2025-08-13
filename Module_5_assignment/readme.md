## Breast Cancer PCA Analysis

### Project Overview

This project applies **Principal Component Analysis (PCA)** to the breast cancer dataset from `sklearn.datasets`. The goal is to identify the most important variables (features) for donor funding decisions by reducing the dataset from 30 features to just 2 principal components. As a bonus, **Logistic Regression** is implemented using these 2 components to classify tumors as malignant or benign.

---

### Objectives

1. Implement PCA to identify essential variables.
2. Reduce dataset dimensionality to **2 components (PC1 & PC2)**.
3. Train and evaluate Logistic Regression using the reduced dataset.

---

### Files

* **cancer\_pca\_assignment.py** — Main code with PCA and Logistic Regression implementation.
* **readme.md** — This documentation file.

---

### How to Run

1. **Install dependencies**:

```bash
pip install pandas matplotlib scikit-learn pyparsing
```

2. **Run the script**:

```bash
python cancer_pca_assignement.py
```


3. **Expected Output**:

* PCA scatter plot of **PC1 vs PC2**, colored by tumor type.
* Top contributing features for PC1 and PC2.
* Explained variance ratio for the two components.
* Logistic Regression classification accuracy and detailed report.

---

### Example Results

* **Explained Variance (PC1 + PC2):** \~63%
* **Top PC1 features:** worst concave points, worst radius, worst perimeter, mean concavity, mean perimeter.
* **Top PC2 features:** mean texture, mean smoothness, mean area, mean compactness, mean radius.
* **Logistic Regression Accuracy:** \~92% (varies slightly per run)

---

### Interpretation

* **PC1 and PC2 are not directly malignant vs benign**, but directions of maximum data variance.
* Features with the largest PCA loadings have the **highest influence** on these directions.
* Reducing from **30 features → 2 components** still preserves most of the information for classification.

---

### Author

Prepared by Albert Prince Mensah for Milestone Assignment.
