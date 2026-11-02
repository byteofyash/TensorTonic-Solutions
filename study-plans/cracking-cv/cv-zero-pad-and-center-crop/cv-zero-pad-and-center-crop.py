import numpy as np
def pad_and_center_crop(image: list, pad: int, crop_h: int, crop_w: int) -> list:
    """
    Returns the crop_h-by-crop_w list of floats, rounded to four decimals.
    """
    img = np.array(image, dtype = np.float64)
    H,W = img.shape

    padh = H + 2*pad
    padw = W + 2*pad

    padded = np.zeros((padh, padw), dtype = np.float64)

    padded[pad: pad+H, pad:pad+W] = img

    h = crop_h
    w = crop_w
    
    r0 = (padh-h) //2
    c0 = (padw-w) //2

    cropped = padded[r0:r0+h, c0:c0+w]

    final_img = cropped.tolist()

    for row in final_img:
        for val in row:
            val =round(val,4)

    return final_img
    