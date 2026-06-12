
## 📌 Internship Details

| Field            | Details                        |
| ---------------- | ------------------------------ |
| **Intern ID**    | CITS2184                       |
| **Intern Name**  | Lavanya Vaidya                 |
| **Duration**     | 4 Weeks                        |
| **Project Name** | Mall Customer Segmentaion      |
| **Domain**       | Machine Learning               |

---

# 📖 Project Overview
# Mall Customer Segmentation
Mall Customer Segmentation is a Machine Learning project that groups customers into different categories based on their demographic information and purchasing behavior. The project uses the K-Means Clustering algorithm to identify meaningful customer segments that can help businesses improve marketing strategies, customer engagement, and decision-making.

The system provides a web-based interface where users can input customer details and predict the customer segment. It also includes a dashboard for visualizing customer insights and cluster statistics.

---

# 🎯 Project Scope
The project focuses on:

* Customer data analysis.
* Data preprocessing and feature engineering.
* Customer segmentation using K-Means Clustering.
* Customer segment prediction through a web application.
* Dashboard visualization of customer statistics.
* Business intelligence through cluster analysis.

Future enhancements may include:

* Real-time customer analytics.
* Recommendation systems.
* Advanced clustering algorithms.
* Interactive business reports.
  
---

# ✨ Key Features

* Groups customers into multiple clusters based on behavior and demographics.
* Predicts the segment of a new customer using the trained clustering model.
* Displays customer statistics and segmentation insights.
* Handles missing values and data cleaning.
* Generates useful features for better clustering performance.
* Provides cluster distribution and customer insights.
* Modern Bootstrap-based web interface.

---

# 🔄 Project Workflow

```text
Step 1: Data Collection
Load Mall Customers Dataset.
Explore customer information.
Step 2: Data Preprocessing
Remove duplicates.
Handle missing values.
Clean and validate data.
Step 3: Feature Engineering
Create useful features.
Prepare data for clustering.
Step 4: Data Scaling
Standardize numerical features using StandardScaler.
Step 5: Model Training
Train K-Means clustering model.
Generate customer clusters.
Step 6: Cluster Labeling

Assign meaningful business labels:

Premium Customers
Budget Customers
Young High Spenders
Average Customers
Careful Customers
Step 7: Model Saving

Store:

KMeans Model
StandardScaler

using Joblib.

Step 8: Prediction

User enters:

Gender
Age
Annual Income
Spending Score

The system predicts the customer segment.

Step 9: Dashboard Visualization

Display:

Total Customers
Total Clusters
Average Income
Average Spending Score
Cluster Distribution
---

---

# 🤖 Machine Learning Models Used

The following algorithms were implemented and evaluated:

1. K-Means Clustering
Type: Unsupervised Machine Learning
Purpose: Groups customers into different segments based on their behavior and demographics.
Output: Premium Customers, Budget Customers, Young High Spenders, Average Customers, and Careful Customers.

2. StandardScaler
Type: Data Preprocessing Technique
Purpose: Normalizes feature values before clustering to improve model performance.
Features Used
Gender
Age
Annual Income (k$)
Spending Score (1–100)

---

# 🛠️ Technology Stack

* Frontend      : React.js, Vite, Axios
* Backend       : Flask, Flask-CORS
* Machine Learning : Scikit-Learn, XGBoost, Imbalanced-Learn
* Data Analysis : Pandas, NumPy
* Visualization : Matplotlib, Seaborn, Plotly, Missingno
* Model Storage : Joblib
* Development   : Jupyter Notebook, VS Code
* Version Control : Git, GitHub
* Dataset       : IBM Telco Customer Churn Dataset

---

# 📁 Project Structure

```text
TELECOM_CHURN_PREDICTION/
│
├── backend/
│   │
│   ├── __pycache__/
│   │
│   ├── models/
│   │   ├── best_model.pkl
│   │   ├── best_model.pkl.bak
│   │   ├── scaler.pkl
│   │   └── scaler.pkl.bak
│   │
│   ├── notebooks/
│   │   ├── business_insights.ipynb
│   │   ├── data_cleaning.ipynb
│   │   ├── data_understanding.ipynb
│   │   ├── eda.ipynb
│   │   ├── feature_engineering.ipynb
│   │   ├── feature_importance.ipynb
│   │   ├── model_training.ipynb
│   │   └── shap_analysis.ipynb
│   │
│   ├── reports/
│   │   └── business_summary.csv
│   │
│   ├── app.py
│   └── requirements.txt
│
├── data/
│   │
│   ├── processed/
│   │   ├── cleaned_telco.csv
│   │   └── engineered_telco.csv
│   │
│   └── raw/
│       └── telco_churn.csv
│
├── frontend/
│   │
│   ├── node_modules/
│   │
│   ├── public/
│   │
│   ├── src/
│   │   ├── assets/
│   │   ├── components/
│   │   ├── App.css
│   │   ├── App.jsx
│   │   ├── index.css
│   │   └── main.jsx
│   │
│   ├── .gitignore
│   ├── eslint.config.js
│   ├── index.html
│   ├── package.json
│   ├── package-lock.json
│   ├── README.md
│   └── vite.config.js
│
├── .gitignore
└── README.md
```

---

⚙️ Installation & Setup

🚀 How to Run the Project

* Clone Repository
  
https://github.com/Lavanya-1506/Telecom_Churn_Prediction.git
* Install Dependencies
  
pip install -r requirements.txt
* Run Frontend
  
npm run dev
* Run Application
  
python app.py

---

# 🎯 Project Outcomes

* Developed an end-to-end Machine Learning system for predicting telecom customer churn.
* Performed comprehensive data cleaning, preprocessing, and feature engineering on telecom customer data.
* Conducted Exploratory Data Analysis (EDA) to identify customer behavior patterns and churn trends.
* Trained and compared multiple Machine Learning models, including Logistic Regression, Decision Tree, Random Forest, and XGBoost.
* Evaluated model performance using Accuracy, Precision, Recall, F1-Score, ROC-AUC Score, and Confusion Matrix.
* Identified key factors influencing customer churn through feature importance analysis.
* Built a predictive model capable of classifying customers as likely to churn or remain with the company.
* Developed a Flask-based REST API for model integration and prediction services.
* Created an interactive React dashboard for visualizing churn insights and prediction results.

---

# 👨‍💻 Developed By

**Lavanya Vaidya**

**Machine Learning Intern** 

---



