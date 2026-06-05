```python
# train_model.py

import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

DATA_PATH = "data/placement_data.csv"

df = pd.read_csv(DATA_PATH)

print("Dataset Loaded Successfully")
print("Shape:", df.shape)

# --------------------------------------------------
# Handle Missing Values
# --------------------------------------------------

df.dropna(inplace=True)

print("\nAfter removing missing values:")
print(df.shape)

# --------------------------------------------------
# Encode Categorical Features
# --------------------------------------------------

label_encoders = {}

for column in df.columns:

    if df[column].dtype == "object" and column != "PlacementStatus":

        encoder = LabelEncoder()

        df[column] = encoder.fit_transform(df[column])

        label_encoders[column] = encoder

# --------------------------------------------------
# Encode Target Variable
# --------------------------------------------------

target_encoder = LabelEncoder()

df["PlacementStatus"] = target_encoder.fit_transform(
    df["PlacementStatus"]
)

# --------------------------------------------------
# Split Features and Target
# --------------------------------------------------

X = df.drop("PlacementStatus", axis=1)

y = df["PlacementStatus"]

print("\nFeatures:")
print(X.columns.tolist())

# --------------------------------------------------
# Train-Test Split
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining Samples:", len(X_train))
print("Testing Samples:", len(X_test))

# --------------------------------------------------
# Train Model
# --------------------------------------------------

model = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    random_state=42
)

model.fit(X_train, y_train)

print("\nModel Training Completed")

# --------------------------------------------------
# Predictions
# --------------------------------------------------

y_pred = model.predict(X_test)

# --------------------------------------------------
# Evaluation
# --------------------------------------------------

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# --------------------------------------------------
# Feature Importance
# --------------------------------------------------

importance_df = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
)

print("\nFeature Importance:")
print(importance_df)

# --------------------------------------------------
# Create Models Directory
# --------------------------------------------------

os.makedirs("models", exist_ok=True)

# --------------------------------------------------
# Save Model
# --------------------------------------------------

joblib.dump(
    model,
    "models/placement_model.pkl"
)

print("\nModel saved successfully!")

# --------------------------------------------------
# Save Encoders
# --------------------------------------------------

joblib.dump(
    label_encoders,
    "models/label_encoders.pkl"
)

joblib.dump(
    target_encoder,
    "models/target_encoder.pkl"
)

print("Encoders saved successfully!")

# --------------------------------------------------
# Sample Prediction
# --------------------------------------------------

print("\nTesting Model with First Record")

sample = X.iloc[[0]]

prediction = model.predict(sample)

result = target_encoder.inverse_transform(prediction)

print("Prediction:", result[0])

print("\nTraining Pipeline Completed Successfully")
```

