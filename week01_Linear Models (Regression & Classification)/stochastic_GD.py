import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


ata = pd.read_csv('data.csv')

x = data['hours_studied'].values
y = data['exam_score'].values

slope = 0
intercept = 0
learning_rate = 0.01
epochs = 100
for epoch in range(epochs):
    random_index = random.randint(0, len(x) - 1)
    x_i = x[random_index]
    y_i = y[random_index]

    y_pred = slope * x_i + intercept
    error = y_pred - y_i

    slope_gradient = error * x_i
    intercept_gradient = error

    slope -= learning_rate * slope_gradient
    intercept -= learning_rate * intercept_gradient
