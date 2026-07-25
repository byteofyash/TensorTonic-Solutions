import numpy as np

def matrix_trace(A):
    """
    Returns: float, the trace (sum of diagonal elements) of A.
    """
    trace = 0

    for i in range(len(A)):
        trace += A[i][i]

    return trace