def categorical_encode(data: list, method: str = "label"):
    """
    Returns label-encoded metadata or one-hot rows.
    """
    classes = sorted(set(data))


    idx_dict = {}
    for i,val in enumerate(classes):
        idx_dict[val] = i

    if method == "label":
        encoded = []
        for i in range(len(data)):
            encoded.append(idx_dict[data[i]])
            
        return {
            "classes" : classes,
            "encoded" : encoded
        }

    else:
        b = []
        k = len(classes)
        for i in range(len(data)):
            row = [0] * k
            row[idx_dict[data[i]]] = 1
            b.append(row)

        return b
        
        
        
        
        
         

    
