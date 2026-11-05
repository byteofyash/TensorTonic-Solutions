import numpy as np

def lu_decomposition(A: list) -> dict:
    """
    Returns a dictionary containing float64 arrays L and U.
    """
    a = np.array(A, dtype = np.float64)
    n,n = a.shape
    l= np.eye(n)
    u = np.zeros((n,n))

    for k in range (0,n):

        #compute U
        for j in range(k,n):
            total = 0
            
            for s in range(0,k):
                total += l[k][s] * u[s][j]
            
            u[k][j] = a[k][j] - total

        #compute K
        for i in range ( k+1,n):
            total = 0
            for s in range(0,k): 
                total += (l[i][s] * u[s][k]) 
            
            l[i][k] =( a[i][k]- total )/ u[k][k]

    return{
        "L":l,
        "U":u    
    }

        


            
        
    
    