import numpy as np

def channel_statistics(batch: list) -> dict:
    """
    Returns mean and std lists of C floats in a dictionary, rounded to four decimals.
    """
    a = np.array(batch, dtype = np.float64)
  
    u = (np.mean(a, axis = (0,1,2)))
    stddev = (np.std(a, axis=(0, 1, 2), ddof=0))
  

    return {
        "mean": [round(float(x), 4) for x in u],
        "std": [round(float(x), 4) for x in stddev]
    }
    
