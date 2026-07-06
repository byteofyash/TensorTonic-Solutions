import pandas as pd

def concat_dataframes(dfs):
    """
    Returns: list [shape, data] where shape is [rows, cols]
    """
    dfs = [ pd.DataFrame(x) for x in dfs ]
    result = pd.concat(dfs)
    
    result = result.reset_index(drop=True) # reset_index() produces a new object
    # Most pandas transformation methods return a new object.
    shape = list(result.shape)
    result = result.to_dict("list")
    return [ shape, result]
    

    