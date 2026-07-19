import numpy as np

def euclidean_distance(x, y):
    """
    Returns: float, the Euclidean distance between x and y.
    """
    x = np.array(x, dtype=np.float64)
    y = np.array(y, dtype=np.float64)
    diff = x-y
    square = diff ** 2
    sum = np.sum(square)
    return np.sqrt(sum)