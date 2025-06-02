import numpy as np


def softmax(z, axis=-1):
    z_max = np.max(z, axis=axis)
    exp_z = np.exp(z - z_max)
    return exp_z / np.sum(exp_z, axis=axis)
