
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load Dataset
df = pd.read_csv("netflix_cleaned.csv")

print("Dataset Loaded Successfully!")
print(df.head())

# Step 2: Calculate Movies and TV Shows
content_counts = df["type"].value_counts()

print("\nContent Type Count:")
print(content_counts)

# Step 3: Calculate Percentages
content_percentage = (content_counts / len(df)) * 100

print("\nContent Percentage:")
print(content_percentage.round(2))

# Step 4: Set Visualization Style
sns.set_theme(style="whitegrid")

# Step 5: Create Dashboard
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Pie Chart
axes[0].pie(
    content_counts,
    labels=content_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

axes[0].set_title("Movies vs TV Shows Distribution")

# Bar Chart
sns.barplot(
    x=content_counts.index,
    y=content_counts.values,
    ax=axes[1]
)

axes[1].set_title("Netflix Content Count")
axes[1].set_xlabel("Content Type")
axes[1].set_ylabel("Number of Titles")

# Show Values on Bars
for container in axes[1].containers:
    axes[1].bar_label(container)

# Step 6: Save Dashboard
plt.tight_layout()
plt.savefig("Task2_Content_Analysis.png")

plt.show()

# Step 7: Key Findings
print("\n--- KEY FINDINGS ---")

print("Total Movies:", content_counts.get("Movie", 0))
print("Total TV Shows:", content_counts.get("TV Show", 0))

print("Most Common Content Type:", content_counts.idxmax())

print("\nDashboard Created Successfully!")
