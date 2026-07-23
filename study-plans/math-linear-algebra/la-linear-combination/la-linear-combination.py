import numpy as np

def linear_combination(vectors, coefficients):
    """
    Returns: float64 array, the weighted sum of vectors.
    """
    v = np.array(vectors)
    c = np.array(coefficients)
    c = np.reshape(c, (-1,1))
    w = np.sum(c*v, axis =0)
    return w