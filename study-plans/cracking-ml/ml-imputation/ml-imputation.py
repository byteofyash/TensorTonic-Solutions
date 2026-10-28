import numpy as np

def impute(X: list, method: str = "mean") -> list:
    """
    Returns a new matrix with missing entries filled.
    """
    a = np.array(X, dtype = np.float64)
    [r,c] = a.shape
    b = np.isnan(a)

    for j in range (0,c):
        nj  = a[:,j][~b[:,j]]

        if np.size(nj) == 0:
            fill_val = 0 
        else:
            if method == "mean":
                fill_val = np.mean(nj)
            else:
                fill_val = np.median(nj)

        a[:, j][b[:, j]] = fill_val

    a = np.round(a,4).tolist()

    return a
        


                
        
    
    
    
