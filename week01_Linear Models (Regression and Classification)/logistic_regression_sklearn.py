import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


# Features: hours studied and attendance
X = np.array([[1, 60], [2, 65], [3, 70], [4, 75], [5, 80], [6, 85], [7, 90], [8, 95]])

# Target: pass (1) or fail (0)
y = np.array([0, 0, 0, 0, 1, 1, 1, 1])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions on test data
predictions = model.predict(X_test)

print("Test predictions:", predictions)