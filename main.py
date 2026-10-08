from customer_classifier import CustomerClassifier


classifier = CustomerClassifier("customers.csv")

classifier.train_model()

print("\n===== ENTER CUSTOMER DETAILS =====")

age = int(input("Age: "))
annual_income = float(input("Annual Income: ₹"))
spending_score = float(input("Spending Score (0-100): "))

classifier.predict_segment(
    age,
    annual_income,
    spending_score
)