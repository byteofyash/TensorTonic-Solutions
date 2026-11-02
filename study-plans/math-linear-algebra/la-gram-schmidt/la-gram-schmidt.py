import numpy as np

def gram_schmidt(vectors: list) -> np.ndarray:
    """
    Returns a float64 array whose rows form the ordered orthonormal basis.
    """
    v = np.array(vectors, dtype = np.float64)
    k,n = v.shape
    Q = np.zeros_like(v, dtype = np.float64)

    for i in range(k):
        ri0 = v[i].copy()
        for j in range(i):
            ri0 = ri0 - np.dot(ri0, Q[j])*Q[j]

        Q[i] = ri0/np.linalg.norm(ri0)

    return Q
        
    
    