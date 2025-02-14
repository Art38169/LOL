import numpy as np
import matplotlib.pyplot as plt

t_i = []
x_i = []
y_i = []
a = 0
b = 2 * np.pi
m = 10

def x(t):
    return 16 * (np.sin(t) ** 3)

def y(t):
    return 13*np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t)


for i in range(m):
    t_i.append(a + (b - a) * i/(m-1))
    x_i.append(x(a + (b - a) * i/(m-1)))
    y_i.append(y(a + (b - a) * i/(m-1)))
    
def lagrange(t, a):
    y = 1
    for i in range(m):
        if i != a:
            y *= (t - t_i[i])
            y /= (t_i[a] - t_i[i])
    return y

def interpolate_x(t):
    p_x = 0
    for i in range(m):
        p_x += x_i[i] * lagrange(t, i)
    return p_x

def interpolate_y(t):
    p_x = 0
    for i in range(m):
        p_x += y_i[i] * lagrange(t, i)
    return p_x



t_fine = np.linspace(a, b, 100)
x_real = x(t_fine)
y_real = y(t_fine)
x_point = interpolate_x(t_fine)
y_point = interpolate_y(t_fine)

plt.plot(x_i, y_i, 'ro', label = 'real point')
plt.plot(x_real, y_real, 'b', label = 'real graph')
plt.plot(x_point, y_point, '--', label = 'interpolate graph')
plt.legend()
plt.show()

