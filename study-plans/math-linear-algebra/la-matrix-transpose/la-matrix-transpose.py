import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transpose as a float64 array.
    """
    a = np.asarray(A, dtype=np.float64)
    [m,n] = a.shape
    b = np.zeros_like(a).reshape(n,m)
    for i in range(0,m):
        for j in range (0,n):
            b[j][i]=a[i][j]

    return b
    pass