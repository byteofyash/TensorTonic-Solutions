import numpy as np

def normalize(data):
    """Returns: np.ndarray of shape (m, n), z-score normalized per column"""
    a = np.array(data, dtype = np.float64)
    col_mean = a.mean(axis=0)
    col_std = a.std(axis=0)
    standardized = (a - col_mean) /col_std
    return standardized
    