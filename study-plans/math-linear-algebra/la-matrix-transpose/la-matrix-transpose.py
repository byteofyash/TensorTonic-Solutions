import numpy as np

def matrix_transpose(A):
    """
    Returns: ndarray, the transpose of A.
    """
    a = np.array(A)
    n,m = a.shape
    result = np.zeros((m,n))
    for i in range(n):
        for j in range(m):
            result[j][i] = a[i][j]
    return result       
        
            