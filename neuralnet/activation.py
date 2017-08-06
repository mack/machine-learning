import numpy as np

def sigmoid(x, deriv=False):
    if (deriv):
        return (np.multiply(x, 1-x))
    else:
        return (1.0/(1.0 + np.exp(-x)))

def relu(x):
    return np.maximum(0,x)
