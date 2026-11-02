import numpy as np
def pad_and_center_crop(image: list, pad: int, crop_h: int, crop_w: int) -> list:
    """
    Returns the crop_h-by-crop_w list of floats, rounded to four decimals.
    """
    img = np.array(image, dtype = np.float64)
    H,W = img.shape
    padH = H + 2*pad
    padW = W + 2*pad
    
    padded = np.zeros((padH, padW), dtype = np.float64)

    padded[pad:pad+H, pad:pad+W] = img

    r0 = (padH - crop_h) // 2
    c0 = (padW - crop_w) // 2

    cropped = padded[r0: r0 + crop_h, c0: c0 + crop_w]

    finalcrop = cropped.tolist()
    for row in finalcrop:
        for value in row:
            round(value,4)
    
    return finalcrop

    
    

    
    

    
    

    