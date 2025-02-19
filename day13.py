import numpy as np
import matplotlib.pyplot as plt
import random



data = np.loadtxt("multilateration-data.csv", delimiter= ',', usecols= (0, 1))
d = np.loadtxt("multilateration-data.csv", delimiter= ',', usecols= 2)


N = len(d) - 1 
A = np.zeros((N, 2))
b = np.zeros(N)

for i in range(N):
    A[i, 0] = data[0, 0] - data[i + 1, 0]
    A[i, 1] = data[0, 1] - data[i + 1, 1]
    b[i] = (d[0]**2 - d[i+1]**2 + data[0, 0]**2 - data[i+1, 0]**2 +data[0, 1]**2 - data[i+1, 1]**2)/2
    
c = np.linalg.solve(A.T@A, A.T@b)
print(c)

for i in range(N+1):
    plt.scatter(data[i, 0], data[i, 1], color = "red")

plt.scatter(c[0], c[1], marker = "*")
plt.grid(True)
plt.legend()
plt.show()

