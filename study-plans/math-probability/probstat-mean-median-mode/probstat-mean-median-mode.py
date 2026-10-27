import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns mean, median, and mode as Python floats in a dictionary.
    """
    a = np.array(x, dtype=np.float64)
    mean = np.mean(a)
    median  = np.median(a)
    [val, cnt] = np.unique(a, return_counts = True)
    idx = np.argmax(cnt)
    mode = val[idx]

    return {"mean": mean, "median": median, "mode": mode}
    
    
    
    