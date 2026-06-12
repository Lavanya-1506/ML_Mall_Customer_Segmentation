
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

| Category         | Technology                           |
| ---------------- | ------------------------------------ |
| Language         | Python                               |
| Frontend         | HTML5, CSS3, JavaScript, Bootstrap 5 |
| Backend          | Flask                                |
| Machine Learning | Scikit-Learn                         |
| Data Processing  | Pandas, NumPy                        |
| Model Storage    | Joblib                               |
| Visualization    | Chart.js                             |
| Version Control  | Git, GitHub                          |
| IDE              | VS Code                              |
| Dataset          | Mall Customers Dataset               |


---

# 📁 Project Structure

```text
Mall-Customer-Segmentation/
│
├── data/
│   ├── Mall_Customers.csv
│   └── processed_data.csv
│
├── notebooks/
│   ├── EDA.ipynb
│   └── Model_Training.ipynb
│
├── models/
│   ├── kmeans_model.pkl
│   ├── scaler.pkl
│   └── cluster_labels.pkl
│
├── src/
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── train_model.py
│   ├── predict.py
│   └── utils.py
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   ├── js/
│   │   └── script.js
│   │
│   └── images/
│       ├── cluster_plot.png
│       └── dashboard_bg.jpg
│
├── templates/
│   ├── index.html
│   ├── dashboard.html
│   ├── segments.html
│   └── prediction.html
│
├── app.py
│
├── requirements.txt
│
├── README.md
│
└── .gitignore
```

---

⚙️ Installation & Setup

🚀 How to Run the Project
1. Clone the Repository

2. Navigate to the Project Directory
cd Mall-Customer-Segmentation
3. Install Required Dependencies
pip install -r requirements.txt
4. Train the Machine Learning Model
Navigate to the source folder and run:
cd src
python train_model.py
5. Run the Flask Application
python app.py
6. Open the Application in Browser
http://127.0.0.1:5000

---

# 🎯 Project Outcomes

After successful implementation, the system can:

* Segment mall customers into meaningful groups.
* Predict customer categories based on user input.
* Provide business insights through dashboards.
* Support targeted marketing strategies.
* Improve customer relationship management.
* Assist businesses in understanding spending behavior.

The project demonstrates the practical application of Machine Learning, Data Analysis, and Web Development in solving real-world business problems.

---

# 👨‍💻 Developed By

**Lavanya Vaidya**

**Machine Learning Intern** 

---



