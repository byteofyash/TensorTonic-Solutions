import math

def log_loss(y_true, y_pred, eps=1e-15):
    """
    Compute per-sample log loss.
    """
    losses = []

    for actual, pred in zip(y_true, y_pred):
        pred = max(eps, min(pred, 1 - eps))

        loss = -(actual * math.log(pred) +
                 (1 - actual) * math.log(1 - pred))

        losses.append(loss)

    return losses