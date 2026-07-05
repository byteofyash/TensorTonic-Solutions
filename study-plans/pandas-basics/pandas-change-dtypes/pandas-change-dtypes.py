import pandas as pd

def change_dtype(data, column, target_type):
    """
    Returns: list [dtypes_before, dtypes_after] (both dicts)
    """
    df = pd.DataFrame(data)
    
    dtypes_before =  df.dtypes.to_dict()

    for key, value in dtypes_before.items():
        dtypes_before[key] = str(value)
        
    df[column]= df[column].astype(target_type)
    
    
    dtypes_after=  df.dtypes.to_dict()
    for key, value in dtypes_after.items():
        dtypes_after[key] = str(value)

    return[
        dtypes_before, dtypes_after
    ]
    