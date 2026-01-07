import pandas as pd

# Load dataset created in Task 1
df = pd.read_excel("quotes_dataset.xlsx")

print("=== DATASET OVERVIEW ===")
print("Total quotes:", len(df))
print("Total authors:", df["author"].nunique())

print("\n=== TOP AUTHORS ===")
print(df["author"].value_counts().head())

print("\n=== MOST COMMON TAGS ===")
tags = df["tags"].str.split(", ").explode()
print(tags.value_counts().head())

print("\n=== DATA QUALITY CHECK ===")
print("Missing values:")
print(df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())
