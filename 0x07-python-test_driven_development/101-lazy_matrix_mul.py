#!/usr/bin/python3
import numpy as np
"""Task 7 - Lazy Matrix Multiplication
This is our function to be tested
"""


def lazy_matrix_mul(m_a, m_b):
    """Multiples two matrices
    Args:
        m_a (list): first matrix
        m_b (list): second matrix

    Returns:
        Returns the product matrix

    Raises:
        TypeErrors and ValueErrors
    """
    te1 = " must be a list"
    te2 = " must be a list of lists"
    te3 = " should contain only integers or floats"
    te4a = "each row of "
    te4b = " must should be of the same size"
    ve1 = " can't be empty"
    ve2 = "m_a and m_b can't be multiplied"
    if type(m_a) is not list:
        raise TypeError("m_a" + te1)
    if type(m_b) is not list:
        raise TypeError("m_b" + te1)
    if not any(isinstance(row, list) for row in m_a):
        raise TypeError("m_a" + te2)
    if not any(isinstance(row, list) for row in m_b):
        raise TypeError("m_b" + te2)
    for l in m_a:
        if len(l) == 0:
            raise ValueError("m_a" + ve1)
    for l in m_b:
        if len(l) == 0:
            raise ValueError("m_b" + ve1)
    for row in m_a:
        if not any(isinstance(e, (int, float)) for e in row):
            raise TypeError("m_a" + te3)
    for row in m_b:
        if not any(isinstance(e, (int, float)) for e in row):
            raise TypeError("m_b" + te3)
    if len(set(len(row) for row in m_a)) != 1:
        raise TypeError(te4a + "m_a" + te4b)
    if len(set(len(row) for row in m_b)) != 1:
        raise TypeError(te4a + "m_b" + te4b)
    if len(m_a[0]) != len(m_b):
        raise ValueError(ve2)
    return np.array(tuple(tuple(e) for e in np.matmul(m_a, m_b)))
