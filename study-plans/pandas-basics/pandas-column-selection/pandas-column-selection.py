import pandas as pd

def select_column(data, column):
    """
    Returns: dict with 'values' (list) and 'length' (int)
    """
    df = pd.DataFrame(data)
    # req_column is a series so we convert it into a list
    req_column = df[column].to_list()
    length = len(req_column)
    
    return{
        "values": req_column,
        "length": length
    }
    pass