import numpy as np

def sort_with_indices(data, axis):
    """Returns: np.ndarray of shape (2, m, n), stacked sorted values and sort indices"""
    a = np.array(data, dtype = np.float64)
    a_sorted = np.sort(a, axis)
    idx = np.argsort(a, axis)
    return np.stack((a_sorted, idx), axis = 0 )
    
    