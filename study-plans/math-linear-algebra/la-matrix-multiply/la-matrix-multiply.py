import numpy as np

def matrix_multiply(A, B):
    """
    Returns: 2-D float64 array, the matrix product A @ B.
    """
    A = np.array(A, dtype=np.float64)
    B = np.array(B, dtype=np.float64)

    rows_A, cols_A = A.shape
    rows_B, cols_B = B.shape

    result = np.zeros((rows_A, cols_B))

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result