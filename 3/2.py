import numpy as np


def minmax_scale(x):
    if np.all(x == x[0]):
        return np.zeros_like(x, float)
    return (x - x.min(axis=0)) / (x.max(axis=0) - x.min(axis=0))


X = np.array([[1, 1], [1, 1]])

print(minmax_scale(X))
