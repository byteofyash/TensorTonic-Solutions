import torch

def tensor_op(x: torch.Tensor, y: torch.Tensor, op: str) -> torch.Tensor:
    """
    Returns the operation result as a float32 tensor.
    """
    if op =='add':
        r = x +y
    elif op=='multiply':  
        r = x * y
    elif op =='matmul':
        r = x@y
    elif op=='power':
        r = x ** y
    else:
        r = torch.maximum(x,y)

    return r.float()
        
