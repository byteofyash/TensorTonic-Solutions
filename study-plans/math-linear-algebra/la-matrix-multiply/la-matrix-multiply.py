import numpy as np

def matrix_multiply(A: list, x: list) -> np.ndarray:
    """
    Returns the matrix product as a float64 array.
    """
    a = np.asarray(A, dtype=np.float64)
    x = np.asarray(x, dtype=np.float64) 
    r = a @ x
    return r