import pandas as pd

def multi_groupby(data, group_cols, value_col, aggfunc):
    """
    Returns: dict of lists (flat table with group columns + value column)
    """
    df= pd.DataFrame(data)
    grouped = df.groupby(group_cols)[value_col].agg(aggfunc)
    grouped = grouped.reset_index()
    grouped = grouped.to_dict("list")
    return grouped
    

    