import numpy as np

def row_extremes(data):
    """Returns: np.ndarray of shape (4, m), rows are max_val, max_col, min_val, min_col"""
    a = np.array(data, dtype= np.float64)
    col_of_min = a.argmin(axis=1)
    col_of_max = a.argmax(axis=1)
    row_indices = np.arange(a.shape[0])
    row_min = a[row_indices, col_of_min]
    row_max = a[row_indices, col_of_max]
    result = np.stack((row_max,col_of_max,row_min,col_of_min), axis =0)
    return result


    
    
    