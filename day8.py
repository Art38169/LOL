import numpy as np
import matplotlib.pyplot as plt


x_i = []
y_i = []
A = []
a = 0
b = 4
m = 10


def f(x):
    return np.sin(5 * x)


for i in range(m):
    x_i.append(a + (b - a) * i/(m-1))
    y_i.append(f(a + (b - a) * i/(m-1)))
    

for i in range(m):
    row = []
    for j in range(m):
        row.append(x_i[i] ** j)
    A.append(row)


sol_matrix = np.linalg.solve(A, y_i)

def interpolate(x):
    y = 0
    for i in range(m):
        y += sol_matrix[i] * (x ** i)
    return y


point_x = np.linspace(a, b, 100)
point_y = interpolate(point_x)

real_y = f(point_x)

plt.plot(x_i, y_i, "ro", label = "Real Point")
plt.plot(point_x, point_y, "--",  label = "Interpolate Graph")
plt.plot(point_x, real_y, label = "Real Graph")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()




