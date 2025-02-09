from flask import Flask, render_template, request
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

def newton_method(f, df, x0, tol):
    max_iter = 500
    x = x0
    errors = []
    iterations = 0
    for _ in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if abs(dfx) < 1e-10: 
            return x, iterations, errors
        x_new = x - fx / dfx
        error = abs(x_new - x)
        errors.append(error)
        iterations += 1
        if error < tol:
            break
        x = x_new
    return x, iterations, errors

def bisection_method(f, a, b, tol):
    max_iter = 500
    errors = []
    iterations = 0
    if f(a) * f(b) >= 0:
        return None, iterations, errors  
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        if f(c) == 0:
            return c, iterations, errors
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        errors.append(abs(b - a))
        iterations += 1
        if (b - a) / 2 < tol:
            break
    return (a + b) / 2, iterations, errors

# Route for handling form submission
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        func_input = request.form['function']
        interval_a = float(request.form['interval_a'])
        interval_b = float(request.form['interval_b'])
        tol = float(request.form['tolerance'])
        
        # Parse function using sympy
        x = sp.symbols('x')
        func = sp.sympify(func_input)
        f = sp.lambdify(x, func, 'numpy')
        df = sp.lambdify(x, sp.diff(func, x), 'numpy')
        
        # Apply Newton and Bisection methods
        root_newton, iterations_newton, errors_newton = newton_method(f, df, (interval_a + interval_b) / 2, tol)
        root_bisection, iterations_bisection, errors_bisection = bisection_method(f, interval_a, interval_b, tol)

        # Generate convergence graph
        plt.figure(figsize=(8, 6))
        plt.plot(range(1, len(errors_newton) + 1), errors_newton, label='Newton Method', marker='o')
        plt.plot(range(1, len(errors_bisection) + 1), errors_bisection, label='Bisection Method', marker='x')
        plt.xlabel('Iteration')
        plt.ylabel('Error')
        plt.title('Convergence Graph')
        plt.legend()
        
        # Save plot to a string and embed in HTML
        img = BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode('utf-8')
        
        return render_template('index.html', root_newton=root_newton, iterations_newton=iterations_newton,
                               root_bisection=root_bisection, iterations_bisection=iterations_bisection,
                               plot_url=plot_url)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
