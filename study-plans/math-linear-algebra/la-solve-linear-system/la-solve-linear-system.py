import numpy as np

def solve_linear_system(A: list, b: list) -> np.ndarray:
    """
    Returns the float64 solution vector.
    """

    A = np.array(A, dtype = np.float64)
    b = np.array(b, dtype = np.float64)
    x = np.linalg.solve(A,b)

    return x
    

    

    