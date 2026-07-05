import pandas as pd

def replace_values(data, column, old_val, new_val):
    """
    Returns: dict with 'data' (dict) and 'count' (int)
    """
    df = pd.DataFrame(data)
    mask = df[column] == old_val 
    count = mask.sum()
    df[column] = df[column].replace(old_val, new_val)   # replace in a single column
    df = df.to_dict("list")


    return{
        "data": df,
        "count" : count
        
    }