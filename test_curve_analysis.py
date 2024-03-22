import curve_analysis as ca
import os

def test_compute_real_roots():
    assert ca.compute_real_roots([1, -3, 2]) == [1, 2]
    assert ca.compute_real_roots([3, 3, 0, 0]) == [-1, 0]
    assert ca.compute_real_roots([1, 3, 2, 0]) == [-2, -1, 0]


def test_compute_turning_points():
    assert ca.compute_turning_points([1, 0, 0]) == [0]
    assert ca.compute_turning_points([1, -2, 2]) == [1]
    assert ca.compute_turning_points([2, -12, 20]) == [3]


def test_compute_inflection_points():
    assert ca.compute_inflection_points([1, 2, 3]) == []
    assert ca.compute_inflection_points([1, 3, 2, 0]) == [-1]
    assert ca.compute_inflection_points([3, 0, 7, -4]) == [0]
