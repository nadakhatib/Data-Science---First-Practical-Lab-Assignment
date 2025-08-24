# First Practical Lab Assignment – Iris Dataset

**University of Palestine**  
**Faculty of Software Engineering and Artificial Intelligence**  
**Data Science – Practical Lab**  

**Student:** Nada I. M. ElKhatib  
**Student ID:** 120220017  
**Lecturer:** Sahar Hammo  

**Semester:** Summer Semester – August 24, 2025  
**Academic Year:** 2025/2026  

---

## Abstract
The Iris Dataset is a classic dataset in data science and machine learning, widely used for exploring data analysis, cleaning, and visualization techniques.  

This project focuses on:  
- Importing the dataset into Python using pandas.  
- Handling potential data issues such as missing values, inconsistent entries, and outliers.  
- Visualizing the cleaned data to gain insights into the characteristics of iris flowers.  

By examining features like **sepal length, sepal width, petal length, and petal width**, and analyzing the differences between the three species (**setosa, versicolor, virginica**), this project demonstrates essential data preprocessing and visualization skills. Visualizations, including histograms, help in understanding the distribution of features and identifying patterns useful for further predictive modeling.

---

## Objective
- Import a dataset into Python using pandas.  
- Identify and handle missing, inconsistent, or noisy data.  
- Clean and preprocess the data for analysis.  
- Visualize the dataset using histograms and other charts to explore patterns.  

---

## Dataset
The **Iris Dataset** was selected from Kaggle. It contains **150 samples** of iris flowers from three species (**setosa, versicolor, virginica**).  
Each sample has four numeric features: `SepalLengthCm`, `SepalWidthCm`, `PetalLengthCm`, and `PetalWidthCm`.

---

## Methodology

### 1. Importing the Dataset
- Imported the dataset into Python using pandas.  
- Displayed the first 5 rows to verify successful import.

### 2. Data Cleaning

#### a) Missing Data
- Checked for missing values using `data.isnull().sum()`.  
- Numeric columns: filled missing values with the column mean.  
- Text columns: filled missing values with the mode.

#### b) Inconsistent Data
- Cleaned the `Species` column by removing extra spaces and converting text to lowercase.

#### c) Noisy Data (Outliers)
- Checked numeric columns for outliers using the Interquartile Range (IQR) method.  
- Removed samples outside `Q1 - 1.5*IQR` and `Q3 + 1.5*IQR`.

### 3. Data Visualization
- Plotted histograms for numeric columns.  
- Observations:  
  - Sepal and petal lengths show distinct distributions.  
  - Petal features help separate **setosa** from other species.  
  - Histograms provide a clear overview of feature distribution and data spread.

---

## Results

1. **First 5 Rows of the Dataset**  
The dataset was successfully imported with features and species column.

2. **Missing Values Check**  
No missing values were found in any column.

3. **Species Cleaning**  
All species names standardized to lowercase and stripped of extra spaces.

4. **Data Description**  
Statistical summary for numeric columns.

5. **Outlier Removal**  
After removing outliers using the IQR method, **146 samples remained** out of the original 150.

6. **Final Missing Values Check**  
No missing values remain after cleaning.

7. **First 5 Rows After Cleaning**  
Displayed to verify the cleaned dataset.

---

## Conclusion
This lab exercise demonstrated:  
- Importing and inspecting a dataset in Python.  
- Handling missing, inconsistent, and noisy data.  
- Cleaning and preprocessing data for analysis.  
- Visualizing feature distributions to gain insights.  

The Iris Dataset served as a perfect example to practice data cleaning and visualization skills, fundamental in data science projects.

---

**GitHub Repository:** [Data-Science---First-Practical-Lab-Assignment](https://github.com/nadakhatib/Data-Science---First-Practical-Lab-Assignment)

