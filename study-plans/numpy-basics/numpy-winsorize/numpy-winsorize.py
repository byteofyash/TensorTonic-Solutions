import numpy as np

def winsorize(data, lo_q, hi_q):
    """Returns: np.ndarray of shape (3, m, n), stacked clipped values, lo_mask, hi_mask"""
    a = np.array(data, dtype = np.float64)
    low = np.percentile(a, lo_q, axis =0 )
    high = np.percentile(a, hi_q, axis = 0)
    b = np.clip(a,low,high)

    low_mask = a < low.astype(np.float64)
    high_mask = a > high.astype(np.float64)

    return np.stack((b,low_mask, high_mask), axis=0)
    
    

