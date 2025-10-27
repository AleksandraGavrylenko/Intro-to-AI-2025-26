import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

df = pd.DataFrame({
    'age': [18, 22, 25, 28, 30, 35, 40, 45, 50, 60],
    'income': [20000, 25000, 30000, 35000, 40000, 50000, 60000, 70000, 80000, 90000],
    'credit_score': [580, 600, 620, 640, 660, 700, 720, 740, 760, 800],
    'bought_car': [0, 0, 0, 1, 1, 1, 1, 1, 1, 1]  # Target column
})

df = df.dropna()

# X = all feature columns (everything except the target)
X = df[['age', 'income', 'credit_score']]

# y = target column (what you want to predict)
y = df['bought_car']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"\nTraining set size: {len(X_train)}")
print(f"Test set size: {len(X_test)}")

# For classification (0/1 prediction)
model = LogisticRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"\nAccuracy: {accuracy:.2f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))


new_data = pd.DataFrame({
    'age': [32],
    'income': [45000],
    'credit_score': [690]
})
prediction = model.predict(new_data)
print("\nNew Data for Prediction:")
print(new_data)
print(f"Prediction for new data (1 = will buy car, 0 = won't): {prediction[0]}")
