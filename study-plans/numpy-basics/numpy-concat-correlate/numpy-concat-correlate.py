import numpy as np

def compare_correlations(a, b):
    """Returns: np.ndarray of shape (3, n, n), stacked correlation matrices"""
    a = np.array(a, dtype = np.float64)
    b = np.array(b, dtype = np.float64)

    combined = np.concatenate([a,b], axis =0)
    corr_combined = np.corrcoef(combined.T)
    a_corr = np.corrcoef(a.T)
    b_corr = np.corrcoef(b.T)

    return np.stack((a_corr,b_corr, corr_combined) , axis =0 )