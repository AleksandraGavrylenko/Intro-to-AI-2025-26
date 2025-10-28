import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load data
df = pd.read_csv(r'MLmodel\data.csv')

# Handle missing values
df = df.dropna()

# Define features (X) and target (y)
X = df[['Age', 'Income', 'Credit Score']]
y = df['Bought Car']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"\nTraining set size: {len(X_train)}")
print(f"Test set size: {len(X_test)}")

# Initialize Logistic Regression model
model = LogisticRegression(solver='liblinear', max_iter=200)

# Train the model
model.fit(X_train, y_train)
print("\nModel trained successfully!")

# Make predictions
y_pred = model.predict(X_test)
print("Predictions made!")

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"\nAccuracy: {accuracy:.2f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Predict on new data
new_data = pd.DataFrame({
    'Age': [32], #32
    'Income': [45000], #45000
    'Credit Score': [690] #690
})
prediction = model.predict(new_data)

print("\nNew Data for Prediction:")
print(new_data)
print(f"Prediction for new data (1 = will buy car, 0 = won't): {prediction[0]}")
