# OSESM - Simon Jordan - 11912008

This is the repository for the Lecture 370.062 Open Source Energy System Modeling of Simon Jordan (11912008).

Copyright 2024 Simon Jordan

[![License](https://img.shields.io/badge/license-Apache%202.0-black)](https://github.com/SimonJordan/OSESM_Jordan_11912008/blob/main/LICENSE)

### This Python-based project contains fundamental curve analysis tools to inspect polynomial functions by using the Sympy library.

In "curve_analysis.py," three functions are provided to determine the real roots, turning points, and inflection points of polynomial functions.
These functions are essential for gaining insights into the behavior of polynomial functions, which are crucial for various applications in mathematics, engineering, and science.
Therefore, the coefficients are given as a list for the function parameters in descending order.
Example for the function "f(x) = k_3 * x ** 3 + k_2 * x ** 2 + k_1 * x + k_0" with the regarding coefficients = [k_3, k_2, k_1, k_0]

$$ f(x) = k_3 x^3 + k_2 x^2 + k_1 x + k_0 $$
$$ coefficients = [k_3, k_2, k_1, k_0] $$

* #### compute_real_roots:

This function calculates the real roots of a polynomial function provided in the form of its coefficients. It uses the roots function from Sympy to compute the roots and then filters out the real roots.

* #### compute_turning_points: 

This function determines the turning points of a polynomial function. It first constructs the polynomial function using the provided coefficients, then computes its first derivative using the diff function from Sympy. Finally, it finds the roots of the first derivative to locate the turning points.

* #### compute_inflection_points:

This function identifies the inflection points of a polynomial function. Similar to the turning points function, it constructs the polynomial function, computes its second derivative, and then finds the roots of the second derivative to locate the inflection points.
