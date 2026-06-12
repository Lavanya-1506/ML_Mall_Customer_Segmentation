import pandas as pd

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

import joblib

from data_preprocessing import (
    preprocess_data
)

from feature_engineering import (
    create_features
)


# --------------------
# Load Dataset
# --------------------

df = pd.read_csv(
    "../data/Mall_Customers.csv"
)

# --------------------
# Preprocess
# --------------------

df = preprocess_data(df)

# --------------------
# Feature Engineering
# --------------------

df = create_features(df)

# --------------------
# Features Used
# --------------------

X = df[
    [
        "Age",
        "Annual Income (k$)",
        "Spending Score (1-100)"
    ]
]

# --------------------
# Scaling
# --------------------

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

# --------------------
# Train Model
# --------------------

kmeans = KMeans(
    n_clusters=5,
    random_state=42,
    n_init=10
)

clusters = kmeans.fit_predict(
    X_scaled
)

df["Cluster"] = clusters

# --------------------
# Save Model
# --------------------

joblib.dump(
    scaler,
    "../models/scaler.pkl"
)

joblib.dump(
    kmeans,
    "../models/kmeans_model.pkl"
)

# --------------------
# Save Data
# --------------------

df.to_csv(
    "../data/processed_data.csv",
    index=False
)

print("Model Trained Successfully")