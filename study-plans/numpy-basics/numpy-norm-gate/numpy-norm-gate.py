import numpy as np

def norm_gate(X, W, threshold):
    """Returns: np.ndarray of shape (n, k), gated projection where rows below threshold are zeroed"""
    X = np.array(X, dtype = np.float64)
    W = np.array(W, dtype = np.float64)
    
    Y = X @ W          # shape (n, k)
    norms = np.linalg.norm(Y, axis=1)  # shape (n,)
    gate = (norms >= threshold).astype(np.float64)  # shape (n,)
    Z = Y * gate[:, np.newaxis]  # broadcast (n, 1) * (n, k)
    return Z
