import pandas as pd

def create_pivot(data, index, columns, values, aggfunc):
    """
    Returns: nested dict {column_value: {index_value: agg_result}}
    """
    df = pd.DataFrame(data)
    pivot = df.pivot_table(
    values=values,        # column to aggregate
    index=index,          # row labels
    columns=columns,       # column labels
    aggfunc= aggfunc ,           # aggregation function
    fill_value=0
)

    pivot = pivot.to_dict()
    return pivot

    