def rgb_to_grayscale(image: list) -> list:
    """
    Returns the H-by-W grayscale list of floats, rounded to four decimals.
    """
    gray = []
    for row in image:
        new_row = []
        for pixel in row:
            r,g,b = pixel
            y = round((0.299*r + 0.587*g + 0.114*b),4)
            new_row.append(y)
        
        gray.append(new_row)

    return gray

    
            
            