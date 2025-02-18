import numpy as np
import matplotlib.pyplot as plt

def g(x, c):
    return c[0] + c[1] * np.sin(x) + c[2] * x ** 2

A = np.array([[1, 0, 0], [1, np.sin(1), 1], [1, np.sin(2), 4], [1, np.sin(3), 9]])
b = np.array([1, 2, 3, 2])

c = np.linalg.solve(A.T@A, A.T@b)

print(f"Corrupted Coefficient: {c}")

x_fine = np.linspace(0, 3, 400)
g_values = g(x_fine, c)
plt.plot(x_fine, g_values, label = "graphs")
plt.show()