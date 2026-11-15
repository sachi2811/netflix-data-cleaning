import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("netflix_cleaned.csv")

# Organize Release Year
df["release_year"] = pd.to_numeric(
    df["release_year"], errors="coerce"
)
df = df.dropna(subset=["release_year"])

# Calculate Yearly Content Releases
yearly_content = (
    df.groupby("release_year")
    .size()
    .reset_index(name="Total Releases")
)

yearly_content = yearly_content.sort_values("release_year")

# Growth and Decline Analysis
yearly_content["Growth"] = yearly_content["Total Releases"].diff()

yearly_content["Growth Percentage"] = (
    yearly_content["Total Releases"].pct_change() * 100
)

# Highest Release Year
highest_year = yearly_content.loc[
    yearly_content["Total Releases"].idxmax()
]

print("Highest Release Year:", int(highest_year["release_year"]))
print("Highest Content Releases:", int(highest_year["Total Releases"]))

# Trend Visualization
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
plt.savefig("Task4_Release_Year_Trend.png", dpi=300)
plt.show()