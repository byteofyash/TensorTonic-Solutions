import numpy as np

def vector_norms(v):
    """
    Returns: float64 array of shape (3,) containing [L1, L2, L-inf] norms.
    """
    v = np.array(v, dtype=np.float64)
    l1 = np.sum(abs(v))
    l2 = np.sqrt(np.sum(v**2))
    l_inf = np.max(abs(v))
    return np.array([l1,l2,l_inf])
    