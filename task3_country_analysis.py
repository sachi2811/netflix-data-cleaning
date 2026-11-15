
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load Dataset
df = pd.read_csv("netflix_cleaned.csv")

print("Dataset Loaded Successfully!")

# Step 2: Clean Country Column
df["country"] = df["country"].fillna("Unknown")

# Step 3: Split Multiple Countries
df["country"] = df["country"].str.split(", ")

# Step 4: Expand Country Data
country_df = df.explode("country")

# Step 5: Count Content by Country
country_counts = country_df["country"].value_counts()

print("\nTop 10 Countries:")
print(country_counts.head(10))

# Step 6: Create Top 10 Dataset
top_10 = country_counts.head(10).reset_index()
top_10.columns = ["Country", "Content Count"]

# Step 7: Visualize Data
sns.set_theme(style="whitegrid")

plt.figure(figsize=(12, 6))

sns.barplot(
    data=top_10,
    x="Content Count",
    y="Country"
)

plt.title("Top 10 Countries by Netflix Content")
plt.xlabel("Number of Titles")
plt.ylabel("Country")

plt.tight_layout()

# Step 8: Save Chart
plt.savefig("Task3_Country_Analysis.png")

plt.show()

# Step 9: Key Findings
print("\n--- KEY FINDINGS ---")
print("Top Content Producing Country:", country_counts.index[0])
print("Total Countries:", country_df["country"].nunique())

print("\nCountry Analysis Completed Successfully!")
