import pandas as pd

data = {
    "Name": ["Ram", "Sam", "Ravi", "John", "Kiran"],
    "Marks": [80, None, 90, 70, None]
}

df = pd.DataFrame(data)

print("Original Dataset")
print(df)

df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print("\nDataset After Cleaning")
print(df)

print("\nAverage Marks")
print(df["Marks"].mean())

print("\nHighest Marks")
print(df["Marks"].max())

print("\nLowest Marks")
print(df["Marks"].min())

print("\nTotal Students")
print(len(df))
