import pandas as pd

# Load the dataset
df = pd.read_csv("features.csv")

# Fill missing values with mean of each column
df.fillna(df.mean(), inplace=True)

# Save the filled dataset
df.to_csv("Features.csv", index=False)
