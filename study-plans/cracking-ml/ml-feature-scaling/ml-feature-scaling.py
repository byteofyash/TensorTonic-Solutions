import numpy as np

def feature_scale(X: list, method: str = "minmax") -> list:
    """
    Returns the independently scaled feature columns.
    """
    a = np.array(X,dtype = np.float64)
    [r,c] = a.shape
    if method == "minmax":
        for j in range (0,c):
            mini = min(a[:,j])
            maxi = max(a[:,j])

            den = 1.0 if maxi-mini ==0 else maxi-mini

            a[:,j] = (a[:,j]-mini) /den
 
        return np.round(a,4).tolist()

    else:
        for j in range (0,c):
            mean = np.mean(a[:,j])
            stdd = np.std(a[:,j], ddof = 0)
            stdd = 1.0 if stdd == 0 else stdd

            

            a[:,j] = (a[:,j]-mean) /(stdd)

        return np.round(a,4).tolist()

        
        
