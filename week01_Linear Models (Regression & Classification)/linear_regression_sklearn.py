import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load the data
df = pd.read_csv('data.csv')

# Prepare features and target
# Using hours_studied and attendance_percent to predict exam_score
X = df[['hours_studied', 'attendance_percent']].values
y = df['exam_score'].values

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

# Print model parameters
print("Linear Regression Model")
print("=" * 50)
print(f"Coefficients: {model.coef_}")
print(f"Intercept: {model.intercept_:.2f}")
print(f"\nFeatures: hours_studied, attendance_percent")
print(f"Equation: exam_score = {model.coef_[0]:.2f} * hours_studied + {model.coef_[1]:.2f} * attendance_percent + {model.intercept_:.2f}")
print("\n" + "=" * 50)

# Evaluate the model
train_mse = mean_squared_error(y_train, y_train_pred)
test_mse = mean_squared_error(y_test, y_test_pred)
train_r2 = r2_score(y_train, y_train_pred)
test_r2 = r2_score(y_test, y_test_pred)

print(f"\nTraining Set:")
print(f"  MSE: {train_mse:.2f}")
print(f"  R² Score: {train_r2:.4f}")
print(f"\nTest Set:")
print(f"  MSE: {test_mse:.2f}")
print(f"  R² Score: {test_r2:.4f}")

# Create visualizations
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Plot 1: Actual vs Predicted (Training)
axes[0, 0].scatter(y_train, y_train_pred, alpha=0.6, color='blue')
axes[0, 0].plot([y_train.min(), y_train.max()], [y_train.min(), y_train.max()], 'r--', lw=2)
axes[0, 0].set_xlabel('Actual Exam Score')
axes[0, 0].set_ylabel('Predicted Exam Score')
axes[0, 0].set_title(f'Training Set: Actual vs Predicted\nR² = {train_r2:.4f}')
axes[0, 0].grid(True, alpha=0.3)

# Plot 2: Actual vs Predicted (Testing)
axes[0, 1].scatter(y_test, y_test_pred, alpha=0.6, color='green')
axes[0, 1].plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
axes[0, 1].set_xlabel('Actual Exam Score')
axes[0, 1].set_ylabel('Predicted Exam Score')
axes[0, 1].set_title(f'Test Set: Actual vs Predicted\nR² = {test_r2:.4f}')
axes[0, 1].grid(True, alpha=0.3)

# Plot 3: Residuals (Training)
residuals_train = y_train - y_train_pred
axes[1, 0].scatter(y_train_pred, residuals_train, alpha=0.6, color='blue')
axes[1, 0].axhline(y=0, color='r', linestyle='--', lw=2)
axes[1, 0].set_xlabel('Predicted Exam Score')
axes[1, 0].set_ylabel('Residuals')
axes[1, 0].set_title('Training Set: Residual Plot')
axes[1, 0].grid(True, alpha=0.3)

# Plot 4: Residuals (Testing)
residuals_test = y_test - y_test_pred
axes[1, 1].scatter(y_test_pred, residuals_test, alpha=0.6, color='green')
axes[1, 1].axhline(y=0, color='r', linestyle='--', lw=2)
axes[1, 1].set_xlabel('Predicted Exam Score')
axes[1, 1].set_ylabel('Residuals')
axes[1, 1].set_title('Test Set: Residual Plot')
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('linear_regression_results.png', dpi=300, bbox_inches='tight')
print("\n✓ Plot saved as 'linear_regression_results.png'")

# Additional plot: Feature importance
fig2, axes2 = plt.subplots(1, 2, figsize=(14, 5))

# Hours studied vs Exam score
axes2[0].scatter(X[:, 0], y, alpha=0.6, color='purple')
axes2[0].set_xlabel('Hours Studied')
axes2[0].set_ylabel('Exam Score')
axes2[0].set_title(f'Hours Studied vs Exam Score\nCoefficient: {model.coef_[0]:.2f}')
axes2[0].grid(True, alpha=0.3)

# Attendance vs Exam score
axes2[1].scatter(X[:, 1], y, alpha=0.6, color='orange')
axes2[1].set_xlabel('Attendance Percent')
axes2[1].set_ylabel('Exam Score')
axes2[1].set_title(f'Attendance Percent vs Exam Score\nCoefficient: {model.coef_[1]:.2f}')
axes2[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('feature_analysis.png', dpi=300, bbox_inches='tight')
print("✓ Plot saved as 'feature_analysis.png'")
