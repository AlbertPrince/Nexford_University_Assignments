from matplotlib import pyplot as plt
from pyparsing import cast
from sklearn.datasets import load_breast_cancer
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.utils import Bunch

# Load dataset
cancer = cast(Bunch, load_breast_cancer())

df = pd.DataFrame(data=cancer.data, columns=cancer.feature_names)
df['target'] = cancer.target

X = df.drop('target', axis=1)
y = df['target']

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# PCA to 2 components
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Create DataFrame with PCA results
pca_df = pd.DataFrame(data=X_pca, columns=['PC1', 'PC2'])
pca_df['target'] = y

print(pca_df.head())
print("Explained variance ratio:", pca.explained_variance_ratio_)
print("Total variance explained:", sum(pca.explained_variance_ratio_))

# PCA scatter plot
colors = {0: 'red', 1: 'blue'}  
plt.figure(figsize=(8, 6))
for target_value, color in colors.items():
    subset = pca_df[pca_df['target'] == target_value]
    plt.scatter(subset['PC1'], subset['PC2'], 
                c=color, label=cancer.target_names[target_value], alpha=0.6)

plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA of Breast Cancer Dataset')
plt.legend()
plt.show()

# PCA loadings
loadings = pd.DataFrame(
    pca.components_.T, 
    columns=['PC1', 'PC2'],
    index=cancer.feature_names
)

# Top contributing features
print("Top 5 features contributing to PC1:")
print(loadings['PC1'].abs().sort_values(ascending=False).head(5))
print("\nTop 5 features contributing to PC2:")
print(loadings['PC2'].abs().sort_values(ascending=False).head(5))


# Prepare data for Logistic Regression
X_pca_features = pca_df[['PC1', 'PC2']]
y_target = pca_df['target']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X_pca_features, y_target, test_size=0.2, random_state=42
)

# Train Logistic Regression
log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)

# Predictions
y_pred = log_reg.predict(X_test)

# Evaluation
print("\nLogistic Regression Results with 2 PCA Components:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=cancer.target_names))
