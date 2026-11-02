import numpy as np

def vector_projection(u: list, v: list) -> np.ndarray:
    """
    Returns the float64 projection of u onto v.
    """
    u = np.array(u, dtype = np.float64)
    v = np.array(v, dtype = np.float64)

    numerator = np.dot(u,v)
    denominator = np.dot(v,v)

    p = (numerator/denominator) * v

    return p