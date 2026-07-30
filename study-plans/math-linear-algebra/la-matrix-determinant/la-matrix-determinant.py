import numpy as np

def matrix_determinant(A):
    """
    Returns: float, the determinant of square matrix A.
    """
    matrix = np.array(A, dtype=float)
    determinant = np.linalg.det(matrix)

    return float(determinant)