import numpy as np

def cosine_similarity(a, b):
    """
    Returns: float in [-1, 1], cosine similarity between a and b.
    """
    a = np.array(a, dtype=np.float64)
    b = np.array(b, dtype=np.float64)
    num = np.dot(a,b)
    mag_a = np.sqrt(np.sum((a **2)))
    mag_b = np.sqrt(np.sum((b**2)))
    den = mag_a * mag_b
    if(den==0) : return 0.0
    else : return num/den