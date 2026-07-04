import pandas as pd

def data_types_overview(data):
    """
    Returns: dict with 'dtypes', 'type_counts', 'num_columns'
    """
    df = pd.DataFrame(data)
    dtypes = df.dtypes
    dtypes = {
        key : str(value)
        for key, value in dtypes.items()
    }
    type_counts = {}

    for dtype in dtypes.values():
        if dtype in type_counts:
            type_counts[dtype] += 1
        else :
            type_counts[dtype] = 1
    
    totalCols = len(df.columns)
    return{
        "dtypes" : dtypes,
        "type_counts" : type_counts ,
        "num_columns" : totalCols 
    
    }
    
    
