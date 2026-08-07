import math

def xavier_initialization(W, fan_in, fan_out):
    """
    Scale raw weights to Xavier uniform initialization.
    """
    limit = math.sqrt(6 / (fan_in + fan_out))

    scaled = []
    for row in W:
        new_row = []
        for value in row:
            # Convert [0, 1] -> [-limit, limit]
            new_row.append((2 * value - 1) * limit)
        scaled.append(new_row)

    return scaled
