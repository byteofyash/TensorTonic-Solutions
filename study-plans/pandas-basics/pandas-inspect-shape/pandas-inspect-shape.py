import pandas as pd

def inspect_dataframe(data):
    """
    Returns: dict with 'rows', 'cols' (ints), 'columns' (list),
    'dtypes' (dict), 'total_values' (int)
    """
    df = pd.DataFrame(data)
    shape = list(df.shape)
    row_count = shape[0]
    column_count = shape[1]
    columns = list(df.columns)
    dtypes = df.dtypes.to_dict()

    for key, value in dtypes.items():
        dtypes[key] = str(value)
    
    
    

    total_values = row_count * column_count
    return{
        "rows" : row_count,
        "cols" : column_count,
        "columns" : columns,
        "dtypes" : dtypes,
        "total_values" : total_values
    }
    
    
    