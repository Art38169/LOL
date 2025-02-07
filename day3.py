import math

x_prev = 3
count = 0

def g(x):
    return x - (x ** 2 - 2 * x)/5

while True:
    x_new = g(x_prev)
    count += 1
    print(x_new, count)
    if abs(x_new - x_prev) < 5e-2:
        break
    x_prev = g(x_new)
    count += 1
    print(x_prev, count)
    if abs(x_new - x_prev) < 5e-2:
        break
    




# Calculate Efficiency via errors in each iteration.