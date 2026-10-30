import math

def distance_metric(x: list, y: list, metric: str, p: float = 2) -> float:
    """
    Returns the selected distance as a rounded float.
    """
    sum1 = 0
    sum2 = 0
    maxd = 0 
    sum3 = 0 
    sumx = 0 
    sumy = 0
    sumxy = 0
    for xi,yi in zip(x,y):
        di = abs(xi-yi)
        sum1 += di
        sum2 += di ** 2
        maxd = max(maxd,di)
        sum3 += di ** p
        sumx += xi**2
        sumy += yi**2
        sumxy += xi * yi

    if metric == "euclidean":
        return float(round(math.sqrt(sum2),4))
    elif metric == "manhattan":
        return float(round(sum1,4))
    elif metric == "chebyshev":
        return float(round(maxd,4))
    elif metric == "minkowski":
        return float(round(sum3 ** (1/p), 4))
    else:
        if sumx == 0 or sumy ==0 :
            return float(0.0)
        else:
            return float(round(
                1 - sumxy / (math.sqrt(sumx) * math.sqrt(sumy))
                ,4))

    
        
        

         
