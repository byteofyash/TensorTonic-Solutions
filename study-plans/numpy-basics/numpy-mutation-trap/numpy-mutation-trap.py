import numpy as np

def original_and_clipped(data, row_idx, lo, hi):
    """
    Returns: 2D ndarray of float64 with shape (2, ncols)
    """
    a = np.array(data, dtype = np.float64)
    row = a[row_idx].copy()
    row_original = row.copy()
    np.clip(row, lo, hi, out = row)
    result = np.stack((row_original, row), axis = 0 )
    return result
    