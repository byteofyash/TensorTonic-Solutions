def normalize_image(image: list, mean: list, std: list) -> list:
    """
    Returns the normalized H-by-W-by-C list of floats, rounded to four decimals.
    """
    norm_img = []
    for row in image:
        new_row = []
        for pixel in row:
            new_val = []
            for (x,u,sd) in zip(pixel,mean,std):
                y = round(((x-u)/sd),4)
                new_val.append(y)

            new_row.append(new_val)

        norm_img.append(new_row)

    return norm_img
            