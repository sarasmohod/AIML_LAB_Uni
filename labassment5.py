# 1. MATH LIBRARY
import math

print("========== MATH LIBRARY ==========")
number = 25
print("Square root of", number, ":", math.sqrt(number))
print("Power (2^5) :", math.pow(2, 5))
print("Factorial of 5 :", math.factorial(5))
print("Value of PI :", math.pi)
print("Ceiling of 4.3 :", math.ceil(4.3))
print("Floor of 4.7 :", math.floor(4.7))

# 2. NUMPY LIBRARY
import numpy as np
print("\n========== NUMPY LIBRARY ==========")
marks = np.array([65, 72, 80, 75, 90])
print("Marks:", marks)
print("Sum:", np.sum(marks))
print("Mean:", np.mean(marks))
print("Median:", np.median(marks))
print("Standard Deviation:", np.std(marks))
print("Maximum:", np.max(marks))
print("Minimum:", np.min(marks))

# 3. SCIPY LIBRARY
from scipy import stats
print("\n========== SCIPY LIBRARY ==========")
# Calculate z-scores
z_scores = stats.zscore(marks)
print("Z-Scores:", z_scores)

# Calculate mode
mode_result = stats.mode(marks, keepdims=True)
print("Mode:", mode_result.mode[0])

# 4. PANDAS LIBRARY
import pandas as pd
print("\n========== PANDAS LIBRARY ==========")

# Create a DataFrame
data = {
    "Student": ["Amit", "Neha", "Rahul", "Sneha", "Priya"],
    "Maths": [78, 85, 72, 90, 88],
    "Python": [82, 90, 75, 95, 86],
    "AI": [80, 88, 70, 92, 90]
}
df = pd.DataFrame(data)
print("\nStudent Data:")
print(df)

# Calculate average marks
df["Average"] = df[["Maths", "Python", "AI"]].mean(axis=1)
print("\nData with Average:")
print(df)

# Display summary statistics
print("\nSummary Statistics:")
print(df.describe())

# 5. MATPLOTLIB VISUALIZATION
import matplotlib.pyplot as plt
print("\n========== MATPLOTLIB ==========")

# Bar chart
plt.figure(figsize=(8, 5))
plt.bar(df["Student"], df["Average"])
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.title("Average Marks of Students")
plt.show()

# 6. SEABORN VISUALIZATION
import seaborn as sns
print("\n========== SEABORN ==========")
# Scatter plot
plt.figure(figsize=(8, 5))
sns.scatterplot(
    x="Maths",
    y="Python",
    data=df,
    s=100
)

plt.title("Maths Marks vs Python Marks")
plt.xlabel("Maths Marks")
plt.ylabel("Python Marks")
plt.show()

# Heatmap of correlation
plt.figure(figsize=(7, 5))
correlation = df[["Maths", "Python", "AI"]].corr()
sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm"
)
plt.title("Correlation Between Subjects")
plt.show()