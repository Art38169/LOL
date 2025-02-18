import numpy as np
import matplotlib.pyplot as plt


def f1(t):
    return np.cos(t)

def f2(t):
    return np.sin(t)

def f3(t):
    return t

def f4(t):
    return t ** 2

def f5(t):
    return np.log(t)

def g(x, c):
    return c[0] + c[1] * f1(x) + c[2] * f2(x) + c[3] * f3(x) + c[4] * f4(x) + c[5] * f5(x)

x = np.loadtxt("data[1].csv", delimiter= ',', usecols= 0)
y = np.loadtxt("data[1].csv", delimiter= ',', usecols= 1)

N = 500
A = np.zeros((N, 6))
b = np.zeros(N)

for i in range(N):
    A[i, 0] = 1
    A[i, 1] = f1(x[i])
    A[i, 2] = f2(x[i])
    A[i, 3] = f3(x[i])
    A[i, 4] = f4(x[i])
    A[i, 5] = f5(x[i])
    b[i] = y[i]

c = np.linalg.solve(A.T@A, A.T@b)
print(f"c is: {c}")

x_fine = np.linspace(1, 5, 1000)
g_values = g(x_fine, c)
plt.plot(x_fine, g_values, color = 'orange', label = 'Regression Line')
plt.scatter(x, y, label = 'Data Points')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()


        