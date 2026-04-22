
import numpy as np

# Laplacian Matrix
L = np.array([
    [2, -1, -1],
    [-1, 2, -1],
    [-1, -1, 2]
])

# Energy Function
def energy(X):
    return X.T @ L @ X

# PAC Transformation
def pac(X, eta=0.2):
    mean = np.mean(X)
    return X + eta * (mean - X)
