import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns sample variance and standard deviation as Python floats.
    """
    a = np.array(x, dtype = np.float64)
    variance = float(np.var(a, ddof = 1))
    std_dev = float(np.sqrt(variance))
    return {"variance": variance, "std_dev": std_dev}
    