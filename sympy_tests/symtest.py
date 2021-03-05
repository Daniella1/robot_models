from sympy import symbols, lambdify
from sympy.parsing.sympy_parser import parse_expr
import numpy as np

xs = symbols('x1 x2')
ks = symbols('k1 k2')
strs = ['-k1 * x1**2 + k2 * x2', 'k1 * x1**2 - k2 * x2']
syms = [parse_expr(item) for item in strs]

# Convert each expression in syms to a function with signature f(x1, x2, k1, k2):
funcs = [lambdify(xs + ks, f) for f in syms]


# This is not exactly the same as the `my_odes` in the question.
# `t` is included so this can be used with `scipy.integrate.odeint`.
# The value returned by `sym.subs` is wrapped in a call to `float`
# to ensure that the function returns python floats and not sympy Floats.
def my_odes(x, t, k):
    all_dict = dict(zip(xs, x))
    all_dict.update(dict(zip(ks, k)))
    return np.array([float(sym.subs(all_dict)) for sym in syms])

def lambdified_odes(x, t, k):
    x1, x2 = x
    k1, k2 = k
    xdot = [f(x1, x2, k1, k2) for f in funcs]
    return xdot


if __name__ == "__main__":
    from scipy.integrate import odeint

    k1 = 0.5
    k2 = 1.0
    init = [1.0, 0.0]
    t = np.linspace(0, 1, 6)
    sola = odeint(lambdified_odes, init, t, args=((k1, k2),))
    solb = odeint(my_odes, init, t, args=((k1, k2),))
    print(np.allclose(sola, solb))