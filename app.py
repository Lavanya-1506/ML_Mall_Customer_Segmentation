from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# =========================
# Load Model
# =========================

kmeans = joblib.load("models/kmeans_model.pkl")
scaler = joblib.load("models/scaler.pkl")

# =========================
# Segment Labels
# =========================

segment_names = {
    0: "Premium Customers",
    1: "Budget Customers",
    2: "Young High Spenders",
    3: "Average Customers",
    4: "Careful Customers"
}

# =========================
# Home Page
# =========================

@app.route("/")
def home():
    return render_template("index.html")

# =========================
# Segments Page
# =========================

@app.route("/segments")
def segments():
    return render_template("segments.html")

# =========================
# Predict Page
# =========================

@app.route("/predict", methods=["GET", "POST"])
def predict():

    result = None

    if request.method == "POST":

        try:
            age = int(request.form["age"])
            income = float(request.form["income"])
            score = float(request.form["score"])

            # Model expects only 3 features
            customer = np.array([
                [
                    age,
                    income,
                    score
                ]
            ])

            customer_scaled = scaler.transform(customer)

            cluster = kmeans.predict(customer_scaled)[0]

            result = segment_names.get(
                cluster,
                "Unknown Segment"
            )

        except Exception as e:
            result = f"Prediction Error: {str(e)}"

    return render_template(
        "predict.html",
        result=result
    )

# =========================
# Dashboard
# =========================

@app.route("/dashboard")
def dashboard():

    try:
        df = pd.read_csv(
            "data/processed_data.csv"
        )

        total_customers = len(df)

        total_clusters = df["Cluster"].nunique()

        cluster_counts = (
            df["Cluster"]
            .value_counts()
            .to_dict()
        )

        avg_income = round(
            df["Annual Income (k$)"].mean(),
            2
        )

        avg_score = round(
            df["Spending Score (1-100)"].mean(),
            2
        )

    except Exception as e:

        print("Dashboard Error:", e)

        total_customers = 0
        total_clusters = 0
        cluster_counts = {}

        avg_income = 0
        avg_score = 0

    return render_template(
        "dashboard.html",
        total_customers=total_customers,
        total_clusters=total_clusters,
        cluster_counts=cluster_counts,
        avg_income=avg_income,
        avg_score=avg_score
    )

# =========================
# Run App
# =========================

if __name__ == "__main__":
    app.run(debug=True)