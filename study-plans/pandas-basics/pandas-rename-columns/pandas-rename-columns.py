import pandas as pd

def rename_columns(data, rename_map):
    """
    Returns: dict mapping renamed column names to value lists
    """
    df = pd.DataFrame(data)
    renamed_dataframe = df.rename(columns=rename_map)
    renamed_dataframe = renamed_dataframe.to_dict("list")

    return renamed_dataframe
    
    