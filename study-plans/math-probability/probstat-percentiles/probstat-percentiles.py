import numpy as np

def percentiles(x: list, q: list) -> np.ndarray:
    """
    Returns the requested percentiles as a float64 array.
    """
    a = np.array(x, dtype = np.float64)
    q = np.array(q, dtype = np.float64)
    percentile = np.percentile(a,q, method="linear")
    return percentile
    
   