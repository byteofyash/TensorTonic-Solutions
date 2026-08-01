import numpy as np

def vector_projection(u, v):
    """
    Returns: float64 array, the projection of u onto v.
    """
    u = np.array(u, dtype=np.float64)
    v = np.array(v, dtype=np.float64)

    dot_uv = np.dot(u, v)
    dot_vv = np.dot(v, v)

    projection = (dot_uv / dot_vv) * v

    return projection