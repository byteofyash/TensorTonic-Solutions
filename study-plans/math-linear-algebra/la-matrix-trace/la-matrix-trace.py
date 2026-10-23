import numpy as np

def matrix_trace(A: list) -> float:
    """
    Returns the trace as a Python float.
    """
    a =  np.asarray (A, dtype= np.float64)
    [m,n] = a.shape
    sum = 0.0
    for i in range (0,m):
                sum += a[i][i]

    return float(sum)
    