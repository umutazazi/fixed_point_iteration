
from sympy import symbols, solve, sympify, lambdify

class FixedPoint:
    def fixed_point_iteration(g, x0, tol, max_iter):
        values = [float(x0)]  # Store the initial value as a float
        x = x0
        for i in range(max_iter):
            x_new = g(x)
            values.append(float(x_new))  # Ensure x_new is converted to a float
            if abs(x_new - x) < tol:
                return float(x_new), i + 1, values[:i + 2]  # Convert x_new to float
            x = x_new
        return float(x), max_iter, values  # Convert x to float and return the values list

    def find_gx(f_str):
        x = symbols('x')
        f_expr = sympify(f_str)
        f = lambdify(x, f_expr, 'numpy')  # Use numpy to ensure numerical evaluation
        solutions = solve(f_expr, x)

        if solutions:
            # Convert the SymPy solution to a float before returning the lambda function
            g = lambda x: float(solutions[0].evalf(subs={x: x}))
            return g
        else:
            return None



