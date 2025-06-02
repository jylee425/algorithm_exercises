import numpy as np


def one_hot_encoding(y):
    N = y.shape[0]
    C = np.max(y) + 1
    enc = np.zeros((N, C))
    enc[np.arange(N), y] = 1
    return enc
