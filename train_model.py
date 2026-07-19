import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
df = pd.read_csv("loan_approval_dataset.csv")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Remove loan_id column
df.drop("loan_id", axis=1, inplace=True)

# Create LabelEncoder
encoder = LabelEncoder()

# Convert text columns into numbers
df["education"] = encoder.fit_transform(df["education"])
df["self_employed"] = encoder.fit_transform(df["self_employed"])
df["loan_status"] = encoder.fit_transform(df["loan_status"])

# Features (X) and Target (y)
X = df.drop("loan_status", axis=1)
y = df["loan_status"]

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train the model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Check accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Save the model
saved_files = joblib.dump(model, "model.pkl")

print(f"Model Accuracy: {accuracy:.2f}")
print("Saved files:", saved_files)