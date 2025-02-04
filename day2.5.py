import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x)

low_x = 2
high_x = 4
x_middle = (low_x + high_x) / 2
count = 0




for i in range(35):
    a = np.linspace(2, 4, 400)
    b = np.sin(a)

    plt.plot(a, b)
    plt.xlabel("x")
    plt.ylabel("y")
    if f(low_x) * f(high_x) < 0:
        if f(low_x) * f(x_middle) < 0:
            high_x = x_middle
            x_middle = (low_x + high_x) / 2
            fig, ax = plt.subplots()
            ax.plot(x_middle, f(x_middle), "ro")
            plt.savefig(f"bisect-demo-{i}.png")
            ax.clear
        elif f(low_x) * f(x_middle) > 0:
            low_x = x_middle
            x_middle = (low_x + high_x) / 2
            fig, ax = plt.subplots()
            ax.plot(x_middle, f(x_middle), "ro")
            plt.savefig(f"bisect-demo-{i}.png")
            ax.clear
        else:
            break
        count += 1
        if high_x - low_x < 1e-10:
            break
    elif f(low_x) * f(high_x) == 0:
        if f(low_x) == 0:
            x_middle = low_x
            break
        else:
            x_middle = high_x
            break
    else:
        print("No solution in this interval.")
        break
