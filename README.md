# 👥 Customer Segment Classifier

A beginner-friendly Machine Learning project that classifies customers into **HIGH**, **MEDIUM**, or **LOW** spending segments using the **K-Nearest Neighbors (KNN)** algorithm.

The project also demonstrates **Feature Scaling using StandardScaler**, which is important for distance-based algorithms such as KNN.

---

## 🚀 Project Overview

The model uses:

- Age
- Annual Income
- Spending Score

to predict a customer's segment.

```text
Customer Information
        ↓
Feature Scaling
        ↓
K-Nearest Neighbors
        ↓
Nearest Customers
        ↓
HIGH / MEDIUM / LOW
```

---

## 🎯 Objective

The goal is to understand:

- K-Nearest Neighbors
- Classification
- Distance-based Machine Learning
- Feature scaling
- Train/test splitting
- Model evaluation
- Prediction for new customers

---

## 🧠 K-Nearest Neighbors

KNN predicts a new data point by finding the closest training examples.

For example:

```text
K = 5

Neighbor 1 → HIGH
Neighbor 2 → HIGH
Neighbor 3 → MEDIUM
Neighbor 4 → HIGH
Neighbor 5 → HIGH

Final Prediction → HIGH
```

The majority class among the nearest neighbors becomes the prediction.

---

## 📏 Feature Scaling

KNN uses distance to determine which points are closest.

Our features have different numerical ranges:

```text
Age            → around 20–60
Annual Income  → thousands
Spending Score → 0–100
```

Therefore, `StandardScaler` is used before training.

```python
StandardScaler()
```

This prevents a large-scale feature such as income from dominating the distance calculation.

---

## 🔢 K Value

The model uses:

```python
KNeighborsClassifier(n_neighbors=5)
```

This means the model considers the **5 nearest neighbors** when making a prediction.

---

## 📊 Dataset

The dataset contains 30 sample customers.

| Column | Description |
|---|---|
| CustomerID | Customer identifier |
| Age | Customer age |
| AnnualIncome | Annual income |
| SpendingScore | Spending score from 0–100 |
| Segment | HIGH, MEDIUM, or LOW |

`CustomerID` is not used as a model feature because it is only an identifier.

---

## 🧪 Example

Input:

```text
Age: 24
Annual Income: ₹29000
Spending Score: 82
```

Possible output:

```text
Predicted Segment: HIGH
```

---

## 🗂️ Project Structure

```text
python-customer-segment-classifier/
│
├── main.py
├── customer_classifier.py
├── customers.csv
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run

```bash
python main.py
```

Enter the customer's:

- Age
- Annual Income
- Spending Score

The trained KNN model will predict the customer segment.

---

## 🧰 Technologies

- Python
- Pandas
- Scikit-learn
- KNN
- StandardScaler
- Machine Learning
- Classification

---

## 📚 What I Learned

1. What KNN is
2. How KNN uses distance
3. What `K` means
4. How nearest neighbors determine classification
5. Why feature scaling is important
6. How `StandardScaler` works in an ML pipeline
7. How to train a KNN classifier
8. How to evaluate classification accuracy
9. How to predict a new customer's segment

---

## ⚠️ Limitations

This is an educational project using a small synthetic dataset.

The model should not be considered a production-ready customer segmentation system.

A real system would require:

- Much larger datasets
- Real customer behavior
- Better feature engineering
- Cross-validation
- Hyperparameter tuning
- More robust evaluation

---

## 🔮 Future Improvements

- Test different K values
- Add confusion matrix
- Add precision, recall, and F1-score
- Visualize customer clusters
- Add more customer features
- Perform cross-validation
- Build a Streamlit interface
- Compare KNN with other classifiers

---

## 👨‍💻 Author

**Ayushman Tiwari**

GitHub: https://github.com/ayushman-ece

---

## 🛣️ Machine Learning Journey

```text
Linear Regression
       ↓
Logistic Regression
       ↓
Decision Tree
       ↓
Random Forest
       ↓
K-Nearest Neighbors
```

This project is part of my long-term Python → Data Science → Machine Learning → AI learning journey.