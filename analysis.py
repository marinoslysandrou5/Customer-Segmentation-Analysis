import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data.csv")

# Show data
print("First rows:")
print(df.head())

# Basic stats
print("\nSummary statistics:")
print(df.describe())

# Create segments (simple logic)
def segment_customer(row):
    if row["Annual_Income"] > 60000 and row["Spending_Score"] > 70:
        return "High Value"
    elif row["Annual_Income"] < 30000:
        return "Low Income"
    else:
        return "Mid Value"

df["Segment"] = df.apply(segment_customer, axis=1)

print("\nCustomer Segments:")
print(df["Segment"].value_counts())

# Average spending by segment
segment_spending = df.groupby("Segment")["Spending_Score"].mean()
print("\nAvg Spending Score per Segment:")
print(segment_spending)

# Visualization
plt.figure()
segment_spending.plot(kind="bar", title="Spending Score by Customer Segment")
plt.ylabel("Spending Score")
plt.xlabel("Segment")
plt.tight_layout()
plt.savefig("segments.png")

print("\nSaved chart as segments.png")
