import pandas as pd

def boolean_filter(data, column, threshold):
    """
    Returns: dict with 'filtered_data' (dict) and 'count' (int)
    """
    df = pd.DataFrame(data)
    mask = df[column] > threshold
    filtered = df[mask]
    count = filtered.shape[0]
    filtered = df[mask].to_dict(orient="list")
    return{
        "filtered_data": filtered ,
        "count" : count
    }
    