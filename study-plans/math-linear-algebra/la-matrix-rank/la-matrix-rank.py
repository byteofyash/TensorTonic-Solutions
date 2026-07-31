import numpy as np

def matrix_rank(A):
    """
    Returns: int, the rank of matrix A.
    """
    matrix = np.array(A, dtype=float)

    rank = np.linalg.matrix_rank(matrix)

    return int(rank)