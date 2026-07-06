import pandas as pd

def merge_dataframes(left, right, on, how):
    """
    Returns: dict of column to value lists
    """
    left = pd.DataFrame(left)
    right = pd.DataFrame(right)
    result = left.merge(right, on= on, how = how)
    result =  result.to_dict("list")
    return result

    