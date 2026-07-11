import numpy as np

def quantize_and_frame(data, decimals, pad_width):
    """Returns: np.ndarray of shape (3, m+2p, n+2p), stacked rounded, floored, ceiled with zero-padding"""
    arr = np.array(data, dtype = np.float64)
    rounded = np.round(arr, decimals)
    floored = np.floor(arr)
    ceiled = np.ceil(arr)
    results = []
    for array in [rounded, floored, ceiled]:
        padded = np.pad(array, pad_width , mode= 'constant', constant_values = 0)
        results.append(padded)

    return np.stack(results)

    