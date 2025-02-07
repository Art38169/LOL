import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x ** 2 - 4

def g(x):
    return -1/6 * (x**2 - 4) + x

def f_prime(x):
    return 2 * x

def bisection_method(func, a, b, num_iters, p=1e-10):
    x_vals = []
    if func(a) * func(b) > 0:
        print("No root found")
        return 0, 0, []
    
    iteration = 0
    while iteration < num_iters and abs(b - a) >= p:
        mid_point = (a + b) / 2
        x_vals.append(mid_point)
        print(f"Iteration: {iteration}, Midpoint: {mid_point}")
        
        if func(mid_point) == 0:
            break
        elif func(a) * func(mid_point) < 0:
            b = mid_point
        else:
            a = mid_point

        iteration += 1

    return mid_point, iteration, x_vals

def newton_s_method(func, d_func, start, num_iters, p=1e-10):
    x_vals = []
    x = start
    for i in range(num_iters):
        x_prev = x
        x -= func(x) / d_func(x)
        x_vals.append(x)
        
        print(f"Iteration: {i}, Value: {x}")
        
        if abs(x - x_prev) <= p:
            break

    return x, i, x_vals

def contraction_test(func, start, num_iters=1000, p=1e-10):
    x_vals = []
    x = start
    x_prev = x

    for i in range(num_iters):
        if abs(func(x) - x) <= p:
            return x, i, x_vals
        if i > 0 and abs(x_prev - x) <= p:
            return x, i, x_vals
        
        print(f"Iteration: {i}, Value: {x}")
        x_vals.append(x)
        x_prev = x
        x = func(x)
    
    return None, num_iters, x_vals

a, b = 0, 3
num_iter = 50


errors = np.linspace(-6, -2, 200)
errors = list(10 ** errors)

iter_newton_lst, iter_bisect_lst, iter_contract_lst = [], [], []

for err in errors:
  it_newton = newton_s_method(f, f_prime, 0.5, num_iter, p=err)[1]
  it_bisect = bisection_method(f, a, b, num_iter, p=err)[1]
  it_contract = contraction_test(g, 0.5, num_iter, p=err)[1]

  iter_newton_lst.append(it_newton) 
  iter_bisect_lst.append(it_bisect)
  iter_contract_lst.append(it_contract)

plt.plot(errors, iter_bisect_lst, label="Bisection Method")
plt.plot(errors, iter_contract_lst, label="Contraction Mapping")
plt.plot(errors, iter_newton_lst, label="Newton's Method")
plt.xscale("log")
plt.ylabel("Iterations")
plt.xlabel("Error")
plt.legend()
plt.show()


