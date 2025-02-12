import numpy as np
import matplotlib.pyplot as plt

x_i = []
y_i = []
a = 0
b = 3
m = 4


def f(x):
    return np.sin(x)


for i in range(m):
    x_i.append(a + (b - a) * i/(m-1))
    y_i.append(f(a + (b - a) * i/(m-1)))


def lagrange(x, a):
    y = 1
    for i in range(m):
        if i != a:
            y *= (x - x_i[i])
            y /= (x_i[a] - x_i[i])
    return y


def interpolate(x):
    p_x = 0

    for i in range(m):
        p_x += y_i[i] * lagrange(x, i)
    return p_x

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