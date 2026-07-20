import pandas as pd

df = pd.read_csv("06_Machine_Learning/02_Datasets/students.csv")

print(df)

X = df[["Hours", "Attendance"]]
y = df["Marks"]

print("\nFeatures (X):")
print(X)

print("\nTarget (y):")
print(y)