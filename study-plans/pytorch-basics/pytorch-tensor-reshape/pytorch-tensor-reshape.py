import torch

def reshape_tensor(x: torch.Tensor, op: str) -> torch.Tensor:
    """
    Returns the reshaped float32 tensor, including a scalar tensor after a complete squeeze.
    """
    if op =='flatten':
        r = x.flatten()
    elif op=='squeeze':
        r = x.squeeze()
    else:
        r = x.transpose(0,1)

    return r.float()
    
    pass
