
# Practical: Basic Data Preprocessing
# Dataset: UCI Adult Income Dataset

import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

# Step 1: Load the dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"

columns = [
    "age", "workclass", "fnlwgt", "education",
    "education_num", "marital_status", "occupation",
    "relationship", "race", "sex", "capital_gain",
    "capital_loss", "hours_per_week", "native_country",
    "income"
]

df = pd.read_csv(
    url,
    names=columns,
    skipinitialspace=True,
    na_values="?"
)

print("First five records:")
print(df.head())

print("\nDataset shape:", df.shape)

# Step 2: Identify missing values
print("\nMissing values before processing:")
print(df.isnull().sum())

# Step 3: Handle missing values
numerical_cols = df.select_dtypes(include=["number"]).columns
categorical_cols = df.select_dtypes(include=["object"]).columns

for col in numerical_cols:
    df[col] = df[col].fillna(df[col].median())

for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

print("\nMissing values after processing:")
print(df.isnull().sum())

# Step 4: Encode categorical variables
df_encoded = pd.get_dummies(
    df,
    columns=categorical_cols.drop("income").tolist(),
    dtype=int
)

encoder = LabelEncoder()
df_encoded["income"] = encoder.fit_transform(df_encoded["income"])

print("\nDataset after encoding:")
print(df_encoded.head())

# Step 5: Normalize numerical features
numeric_features = [
    "age", "fnlwgt", "education_num",
    "capital_gain", "capital_loss", "hours_per_week"
]

scaler = MinMaxScaler()
df_encoded[numeric_features] = scaler.fit_transform(
    df_encoded[numeric_features]
)

print("\nDataset after normalization:")
print(df_encoded.head())

# Step 6: Save the processed dataset
output_file = "adult_income_processed.csv"
df_encoded.to_csv(output_file, index=False)

print("\nProcessed dataset saved successfully!")
print("Final dataset shape:", df_encoded.shape)
print("Output file:", output_file)
