import math

x_prev = 1.5
count = 0

def g(x):
    return x - (x ** 2 - x - 2)/7.5

while True:
    x_new = g(x_prev)
    x_prev = g(x_new)
    count += 1
    if abs(x_new - x_prev) < 1e-10:
        break


print(x_new, count)


# Calculate Efficiency via errors in each iteration.