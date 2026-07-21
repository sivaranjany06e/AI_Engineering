import pandas as pd
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("06_Machine_Learning/02_Datasets/students.csv")

# Features
X = df[["Hours", "Attendance"]]

# Target
y = df["Marks"]

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("X Train")
print(X_train)

print("\nX Test")
print(X_test)

print("\ny Train")
print(y_train)

print("\ny Test")
print(y_test)