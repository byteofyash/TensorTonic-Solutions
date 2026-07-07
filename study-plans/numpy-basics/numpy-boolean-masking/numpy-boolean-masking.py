import numpy as np

def row_summary(data, threshold):
    """Returns: np.ndarray of shape (3, m, n), stacked element mask, any-filtered, all-filtered"""
    arr = np.array(data, dtype = np.float64)
    mask = arr > threshold #boolean array
    # converting to float64 having the values 1.0 and 0.0
    mask = mask.astype(np.float64) 

    row_mask1 = np.any(arr>threshold, axis =1)
    any_filtered = np.zeros_like(arr)
    any_filtered[row_mask1] = arr[row_mask1]
    
    row_mask2 = np.all(arr > threshold , axis = 1)
    all_filtered = np.zeros_like(arr)
    all_filtered[row_mask2] = arr[row_mask2]

    return np.stack((mask,any_filtered, all_filtered), axis =0)

