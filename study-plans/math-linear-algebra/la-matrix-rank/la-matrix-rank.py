import numpy as np

def matrix_rank(A: list) -> int:
    """
    Returns the numerical rank as a Python integer.
    """
    a = np.asarray(A, dtype=np.float64)
    [m,n] = a.shape
    a = np.linalg.svd(a,compute_uv=False)
    tau = max(m,n) * max(a)* np.finfo(np.float64).eps 
    rank = 0 
    for i in range(0,min(m,n)):
        if a[i] > tau:
            rank +=1

    return int(rank)
            
    