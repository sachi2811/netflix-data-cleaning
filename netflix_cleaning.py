
import pandas as pd

# 1. Load the original dataset
df = pd.read_csv("Dataset.csv")

print("Original dataset shape:", df.shape)

# 2. Inspect missing values and duplicates
print("\nMissing values before cleaning:")
print(df.isnull().sum())

print("\nDuplicate rows before cleaning:")
print(df.duplicated().sum())

# 3. Remove extra spaces from text columns
text_columns = df.select_dtypes(include=["str"]).columns

for column in text_columns:
    df[column] = df[column].str.strip()

# 4. Convert date_added into proper date format
df["date_added"] = pd.to_datetime(
    df["date_added"],
    format="%m/%d/%Y",
    errors="coerce"
)

# 5. Remove exact duplicate rows, if any
df = df.drop_duplicates()

# 6. Save the cleaned dataset
df.to_csv(
    "netflix_cleaned.csv",
    index=False,
    date_format="%Y-%m-%d"
)

print("\nCleaned dataset saved successfully!")

# 7. Verify the exported CSV
cleaned_df = pd.read_csv(
    "netflix_cleaned.csv",
    parse_dates=["date_added"]
)

print("\nFINAL VERIFICATION")
print("Dataset shape:", cleaned_df.shape)
print("Missing values:", cleaned_df.isnull().sum().sum())
print("Duplicate rows:", cleaned_df.duplicated().sum())
print("Date column type:", cleaned_df["date_added"].dtype)

print("\nFirst 5 cleaned rows:")
print(cleaned_df.head())

print("\nProject cleaning and verification completed!")
