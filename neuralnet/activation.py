import numpy as np

def sigmoid(x, deriv=False):
    if (deriv):
        return (np.multiply(x, 1-x))
    else:
        return (x/(np.exp(x) + 1))

def relu(x):
    return np.maximum(0,x)
