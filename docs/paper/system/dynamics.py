from .core import L

def dynamics(X, U):
    return -2 * L @ X + U
