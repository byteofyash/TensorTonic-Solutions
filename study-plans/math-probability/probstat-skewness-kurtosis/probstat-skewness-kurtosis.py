import numpy as np

def skewness_kurtosis(data: list) -> dict:
    """
    Returns adjusted statistics and their interpretations in a dictionary.
    """
    a = np.array(data, dtype = np.float64)
    n = len(a)
    mean = np.mean(a)
    s = np.std(a, ddof = 1)

    z = (a-mean)/s

    sum1 = 0
    for i in range (0,n):
        sum1 += z[i] * z[i] * z[i]

    sum2 = 0
    for i in range (0,n):
        sum2 += z[i] * z[i] * z[i] * z[i]

    g1 = (n/((n-1)*(n-2))) * sum1
    g2 = ((n * (n+1)) / ((n-1)*(n-2)*(n-3)))*sum2

    g2 = g2 - (  3*(n-1)*(n-1) / ((n-2)*(n-3))  )

    g1 = float(round(g1, 4))
    g2 = float(round(g2, 4))

    if g1 >0.5:
        skew_interpretation = "right-skewed"                      
    elif g1 < -0.5 :
        skew_interpretation = "left-skewed"
    else:
        skew_interpretation = "approximately symmetric"

                   

    if g2 > 1:
        kurtosis_interpretation ="leptokurtic"
    elif g2 < -1:
        kurtosis_interpretation ="platykurtic"
    else:
        kurtosis_interpretation ="mesokurtic"


        
        
        

    return {"skewness": g1, 
            "kurtosis": g2, 
            "skew_interpretation": skew_interpretation, "kurtosis_interpretation": kurtosis_interpretation}

    