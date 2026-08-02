import numpy as np

def gram_schmidt(vectors):
    """
    Returns: float64 array of shape (k, n), orthonormal basis spanning the input space.
    """
    vectors = np.array(vectors, dtype=np.float64)
    basis = []

    for v in vectors:
        u = v.copy()

        
        for q in basis:
            u -= np.dot(v, q) * q

        
        u /= np.linalg.norm(u)
        basis.append(u)

    return np.array(basis, dtype=np.float64)