import numpy as np
import matplotlib.pyplot as plt
import random



c0 = 1
c1 = 1
a = 0
b = 10
m = 100

def f(x):
    return c0 + c1 * x

x_points = np.linspace(a, b, m)
y_points = f(x_points)
y_points_noisy = y_points + np.random.rand(m) - 0.5

A = np.zeros((2, 2))
B = np.zeros(2)

A[0, 0] = m
A[0, 1] = np.sum(x_points)
A[1, 0] = np.sum(x_points)
A[1, 1] = np.sum(x_points ** 2)

B[0] = np.sum(y_points_noisy)
B[1] = np.sum(x_points * y_points_noisy)

c = np.linalg.solve(A, B)

def P(x, c):
    return c[0] + c[1] * x

x_fine = np.linspace(a, b, 200)
f_value = f(x_fine)
p_values = P(x_fine, c)

plt.figure(figsize = (8, 6))
plt.plot(x_fine, f_value, label = 'f(x)', color = 'blue')
plt.plot(x_fine, p_values, label = 'P(x)', color = 'red', linestyle = '--')
plt.scatter(x_points, y_points_noisy, label = 'data points')
plt.legend()
plt.show()