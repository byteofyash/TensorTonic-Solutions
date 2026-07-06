import pandas as pd

def apply_transform(data, column, operation):
    """
    Returns: dict with original columns plus column_transformed
    """
    df = pd.DataFrame(data)
    column_transformed = column + "_transformed"
    
    
    if operation == "normalize" :
        df[column_transformed] = ((df[column]- df[column].min())/(df[column].max() - df[column].min())).round(4)
    

    elif operation == "rank":
      df[column_transformed]=  df[column].rank().astype(int)
       

    elif operation == "cumsum":
        df[column_transformed]= df[column].cumsum()
    

    elif operation == "double":
         df[column_transformed]= df[column]*2
        
    
    df = df.to_dict("list")
    
    return df
    
    
    
    