import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Define dataset path
dataset_path = os.path.join("dataset", "creditcardfraud", "creditcard.csv")

# Load dataset
df = pd.read_csv(dataset_path)

# Check if 'Class' column exists
if 'Class' not in df.columns:
    raise KeyError("Column 'Class' not found in dataset. Check dataset structure.")

# Split data into features and labels
X = df.drop(columns=['Class'])  # Features
y = df['Class']  # Target (0 = Normal, 1 = Fraud)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Standardize features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Ensure 'models' folder exists
os.makedirs("models", exist_ok=True)

# Save model & scaler
joblib.dump(model, "models/fraud_model.pkl")
joblib.dump(scaler, "models/scaler.pkl")

print("✅ Model training complete. Saved in 'models/' folder.")
