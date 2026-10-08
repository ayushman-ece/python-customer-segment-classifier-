import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


class CustomerClassifier:

    def __init__(self, file_name):
        self.data = pd.read_csv(file_name)

    def prepare_data(self):
        X = self.data[
            ["Age", "AnnualIncome", "SpendingScore"]
        ]

        y = self.data["Segment"]

        return X, y

    def train_model(self):
        X, y = self.prepare_data()

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )

        self.scaler = StandardScaler()

        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)

        self.model = KNeighborsClassifier(n_neighbors=5)

        self.model.fit(X_train_scaled, y_train)

        predictions = self.model.predict(X_test_scaled)

        accuracy = accuracy_score(y_test, predictions)

        print("\n===== MODEL TRAINED =====")
        print("KNN model trained successfully. ✅")

        print("\n===== MODEL EVALUATION =====")
        print(f"Accuracy: {accuracy * 100:.2f}%")

    def predict_segment(
        self,
        age,
        annual_income,
        spending_score
    ):
        new_customer = pd.DataFrame({
            "Age": [age],
            "AnnualIncome": [annual_income],
            "SpendingScore": [spending_score]
        })

        new_customer_scaled = self.scaler.transform(new_customer)

        prediction = self.model.predict(new_customer_scaled)

        print("\n===== CUSTOMER SEGMENT PREDICTION =====")
        print(f"Age             : {age}")
        print(f"Annual Income   : ₹{annual_income}")
        print(f"Spending Score  : {spending_score}")
        print(f"Predicted Segment: {prediction[0]}")