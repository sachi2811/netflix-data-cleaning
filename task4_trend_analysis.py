
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load Dataset
df = pd.read_csv("netflix_cleaned.csv")

print("Dataset Loaded Successfully!")

# Step 2: Organize Content by Release Year
df["release_year"] = pd.to_numeric(
    df["release_year"], errors="coerce"
)

df = df.dropna(subset=["release_year"])

# Step 3: Calculate Yearly Content Releases
yearly_content = (
    df.groupby("release_year")
    .size()
    .reset_index(name="Total Releases")
)

yearly_content = yearly_content.sort_values("release_year")

print("\nYearly Content Releases:")
print(yearly_content.to_string(index=False))

# Step 4: Calculate Growth and Decline
yearly_content["Growth"] = yearly_content["Total Releases"].diff()

yearly_content["Growth Percentage"] = (
    yearly_content["Total Releases"].pct_change() * 100
)

print("\nGrowth and Decline Analysis:")
print(yearly_content.tail(15).to_string(index=False))

# Step 5: Find Highest Release Year
highest_year = yearly_content.loc[
    yearly_content["Total Releases"].idxmax()
]

print("\n--- KEY FINDINGS ---")
print("Highest Release Year:", int(highest_year["release_year"]))
print("Highest Content Releases:", int(highest_year["Total Releases"]))

# Step 6: Create Trend Visualization
sns.set_theme(style="whitegrid")

plt.figure(figsize=(13, 6))

sns.lineplot(
    data=yearly_content,
    x="release_year",
    y="Total Releases",
    marker="o"
)

plt.title("Netflix Content Release Trend by Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Content Releases")
plt.xticks(rotation=45)

plt.tight_layout()

# Step 7: Save Chart
plt.savefig("Task4_Release_Year_Trend.png", dpi=300)

plt.show()

print("\nTrend Analysis Completed Successfully!")
