import numpy as np

def newtons_method(f, df, x0, tolerance=1e-10, max_iterations=1000):
    xn = x0
    for n in range(max_iterations):
        fxn = f(xn)
        if abs(fxn) < tolerance:
            print(f'Found solution after {n} iterations.')
            return xn
        dfxn = df(xn)
        if dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        xn = xn - fxn/dfxn
    print('Exceeded maximum iterations. No solution found.')
    return None

def f(x):
    return np.sin(x)

def df(x):
    return np.cos(x)

x0 = 5

root = newtons_method(f, df, x0)

print("Root is:", root)


