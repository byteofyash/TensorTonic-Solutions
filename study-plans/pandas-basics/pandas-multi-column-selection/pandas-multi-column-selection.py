import pandas as pd

def select_columns(data, columns):
    """
    Returns: dict mapping selected column names to value lists
    """
    df = pd.DataFrame(data)
    multi = df.loc[:, columns].to_dict(orient="list")
    return multi

