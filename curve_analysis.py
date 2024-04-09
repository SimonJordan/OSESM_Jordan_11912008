import sympy as sp
import cmath as cm

x = sp.Symbol("x")


def compute_real_roots(coefficients):
    """This function calculates the real roots of a polynomial function."""

    real_roots = []
    roots = sp.roots(coefficients)  # roots may include complex ones
    for root, order in roots.items():  # filter real roots
        if root.is_real:
            real_roots.append(root)

    return sorted(roots)


def compute_turning_points(coefficients):
    """This function calculates the turning points of a polynomial function."""

    f = sum(k * x**(i+1) for i, k in enumerate(reversed(coefficients)))  # create function
    f_1 = sp.diff(f, x)  # 1. derivative of the function
    turning_points = sp.solve(f_1, x)  # roots of the 1. derivative

    return sorted(turning_points)


def compute_inflection_points(coefficients):
    """This function calculates the inflection points of a polynomial function."""

    f = sum(k * x**i for i, k in enumerate(reversed(coefficients)))  # create function
    f_2 = sp.diff(f, x, 2)  # 2. derivative of the function
    inflection_points = sp.solve(f_2, x)  # roots of the 2. derivative

    return sorted(inflection_points)
