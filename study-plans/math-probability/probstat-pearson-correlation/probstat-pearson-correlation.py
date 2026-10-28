import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the float64 feature-correlation matrix.
    """
    a = np.array(X, dtype = np.float64)
    

    b = np.corrcoef(a, rowvar = False)
    return b