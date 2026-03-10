import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# load dataset
data = pd.read_csv('data.csv')

# show first rows
print(data.head())

# get x and y values
x = data['hours_studied'].values
y = data['exam_score'].values

# plot data
plt.scatter(x, y)
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.title("Dataset")
plt.show()


def loss_function(m, b, x, y):
    total_loss = 0
    N = len(x)

    for i in range(N):
        y_pred = m * x[i] + b
        total_loss += (y_pred - y[i]) ** 2

    return total_loss / N


def gradient_descent(m, b, x, y, learning_rate):
    m_gradient = 0
    b_gradient = 0
    N = len(x)

    for i in range(N):
        y_pred = m * x[i] + b

        m_gradient += -(2/N) * x[i] * (y[i] - y_pred)
        b_gradient += -(2/N) * (y[i] - y_pred)
    
    step_size_slope = learning_rate * m_gradient
    step_size_intercept = learning_rate * b_gradient

    print(f"m_gradient: {m_gradient}, step_size: {step_size_slope}")
    m -= step_size_slope
    b -= step_size_intercept

    return m, b


# training
m = 0
b = 0
learning_rate = 0.0001
epochs = 1000

for i in range(epochs):
    m, b = gradient_descent(m, b, x, y, learning_rate)

    if i % 100 == 0:
        loss = loss_function(m, b, x, y)
        print(f"Epoch {i}, Loss: {loss}")

print("Final parameters:")
print("m =", m)
print("b =", b)


# plot regression line
y_pred = m * x + b
plt.scatter(x, y)
plt.plot(x, y)
plt.plot(x, y_pred)
plt.show()