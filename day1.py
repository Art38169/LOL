import math

def f(x):
    return math.sin(x)

low_x = 2
high_x = 4
x_middle = (low_x + high_x) / 2
count = 0

while True:
    if f(low_x) * f(high_x) < 0:
        if f(low_x) * f(x_middle) < 0:
            high_x = x_middle
            x_middle = (low_x + high_x) / 2
        elif f(low_x) * f(x_middle) > 0:
            low_x = x_middle
            x_middle = (low_x + high_x) / 2
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

print(x_middle)
print(count)

# Time Complexity = O(log(n)) b/c the list is halved every iteration