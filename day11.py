import numpy as np
import matplotlib.pyplot as plt



x_points = np.loadtxt("x_points.txt")
y_points = np.loadtxt("y_points.txt")

A = np.zeros((2, 2))
B = np.zeros(2)

A[0, 0] = 50
A[0, 1] = np.sum(x_points)
A[1, 0] = np.sum(x_points)
A[1, 1] = np.sum(x_points ** 2)

B[0] = np.sum(y_points)
B[1] = np.sum(x_points * y_points)

c = np.linalg.solve(A, B)

print(c[0], c[1])

