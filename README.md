# OSESM - Simon Jordan - 11912008

This is the repository for the Lecture 370.062 Open Source Energy System Modeling of Simon Jordan (11912008).
In this project, a Python-based program is provided with fundamental curve analysis tools to inspect polynomial functions by using the Sympy library.
Furthermore, a Python-based test program is available to run automatic tests for a push and pull_request.
Additionally, for each push, ruff is executed to fix and format the programmed files automatically and will terminate with a commit.

[![License](https://img.shields.io/badge/license-Apache%202.0-black)](https://github.com/SimonJordan/OSESM_Jordan_11912008/blob/main/LICENSE)

_Copyright 2024 Simon Jordan_

## curve_analysis.py

In [curve_analysis.py](/curve_analysis.py), three functions are provided to determine the real roots, turning points, and inflection points of polynomial functions.
These functions are essential for gaining insights into the behavior of polynomial functions, which are crucial for various applications in mathematics, engineering, and science.
Therefore, the coefficients are given as a list for the function parameters in descending order.
Example for the function "f(x) = k_3 * x ** 3 + k_2 * x ** 2 + k_1 * x + k_0" with the regarding coefficients = [k_3, k_2, k_1, k_0]:

$$ f(x) = k_3 \cdot x^3 + k_2 \cdot x^2 + k_1 \cdot x + k_0 $$

$$ coefficients = [k_3, k_2, k_1, k_0] $$

* #### compute_real_roots(coefficients):

This function calculates the real roots of a polynomial function provided in the form of its coefficients.
It uses the roots function from Sympy to compute the roots and then filters out the real roots.

* #### compute_turning_points(coefficients): 

This function determines the turning points of a polynomial function.
It first constructs the polynomial function using the provided coefficients, then computes its first derivative using the diff function from Sympy.
Finally, it finds the roots of the first derivative to locate the turning points.

* #### compute_inflection_points(coefficients):

This function identifies the inflection points of a polynomial function.
Similar to the turning points function, it constructs the polynomial function, computes its second derivative, and then finds the roots of the second derivative to locate the inflection points.

## test_curve_analysis.py

In [test_curve_analysis.py](/test_curve_analysis.py), the three functions provided, are tested.
These tests are based on pytest and check the functionality of [curve_analysis.py](/curve_analysis.py).

## requirements.txt

In [requirements.txt](/requirements.txt), all needed packages are listed.

## pytest.yaml

In [pytest.yaml](/.github/workflows/pytest.yaml), the automatic actions for testing are set up.

## ruff.yaml

In [ruff.yaml](/.github/workflows/ruff.yaml), ruff is set up for checking the code style.
Errors and unstructured parts of the code will be automatically fixed and formatted.
After this execution a commit will be created.
