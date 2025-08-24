import pandas as pd
import matplotlib.pyplot as plt

# 1-Choose a random dataset (Iris Dataset from Kaggle)

# 2-Import the dataset
data = pd.read_csv("iris.csv")
print("First 5 rows:\n", data.head())

# 3-Data Cleaning (Missing Data, Inconsistent Data, Noisy Data)

# --- Missing Data ---
print("Missing values per column:\n", data.isnull().sum())

# Fill missing values in numeric columns with their mean
numeric_cols = data.select_dtypes(include='number').columns
data[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].mean())

# Fill missing values in text columns with the most frequent value (mode)
text_cols = data.select_dtypes(include='object').columns
for col in text_cols:
    data[col].fillna(data[col].mode()[0], inplace=True)

# --- Inconsistent Data ---
# Clean 'Species' column: remove leading/trailing spaces and convert to lowercase
data['Species'] = data['Species'].str.strip().str.lower()
print("Unique species after cleaning:", data['Species'].unique())

# --- Noisy Data (Outliers) ---
print("Data description:\n", data.describe())

# Calculate IQR for numeric columns
Q1 = data[numeric_cols].quantile(0.25)
Q3 = data[numeric_cols].quantile(0.75)
IQR = Q3 - Q1

# Remove outliers from numeric columns
data_cleaned = data[~((data[numeric_cols] < (Q1 - 1.5 * IQR)) | (data[numeric_cols] > (Q3 + 1.5 * IQR))).any(axis=1)]
print("Shape after removing outliers:", data_cleaned.shape)

# Final check for missing values
print("Missing values after cleaning:\n", data_cleaned.isnull().sum())

# Show first 5 rows after full cleaning
print("First 5 rows after cleaning:\n", data_cleaned.head())

# 4-Visualization

# Plot histograms for numeric columns
data_cleaned[numeric_cols].hist(figsize=(10,8), color='skyblue', edgecolor='black')
plt.suptitle("Histograms of Iris Dataset", fontsize=16)
plt.tight_layout()
plt.show()
