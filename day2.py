import math



def f(x):
    return (x ** 4) + 3 * (x ** 3) + x ** 2 - (2 * x) - 0.5

def bisec(low_x, high_x):
    x_middle = (low_x + high_x) / 2
    while True:
        if f(low_x) * f(high_x) < 0:
            if f(low_x) * f(x_middle) < 0:
                high_x = x_middle
                x_middle = (low_x + high_x) / 2
            elif f(low_x) * f(x_middle) > 0:
                low_x = x_middle
                x_middle = (low_x + high_x) / 2
            else:
                return x_middle
            if high_x - low_x < 1e-10:
                return x_middle
        elif f(low_x) * f(high_x) == 0:
            if f(low_x) == 0:
                return low_x
            return high_x
        else:
            if high_x - low_x < 1e-1:
                return None
            new_high_x = high_x
            high_x = x_middle
            return bisec(low_x, high_x), bisec(high_x, new_high_x)
            
         
print(bisec(-3, 2))

